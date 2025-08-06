import numpy as np
from typing import Dict, Any, List, Tuple
import os
import json

class ThermalSimulator:
    def __init__(self, config: Dict[str, Any]):
        """
        Initialize the thermal simulator
        
        Args:
            config: Configuration parameters for the simulation
                - resolution: Grid resolution in mm
                - time_step: Simulation time step in seconds
                - material: Material properties dictionary
        """
        self.config = config
        self.grid = None
        self.temperature = None
        self.time = 0.0
        self.history = []
        
    def initialize_grid(self, dimensions: Tuple[float, float, float], resolution: float) -> None:
        """
        Initialize the simulation grid
        
        Args:
            dimensions: (x, y, z) dimensions in mm
            resolution: Grid resolution in mm
        """
        # Calculate grid size
        nx = int(dimensions[0] / resolution) + 1
        ny = int(dimensions[1] / resolution) + 1
        nz = int(dimensions[2] / resolution) + 1
        
        # Initialize temperature grid (ambient temperature)
        ambient_temp = self.config.get("ambient_temperature", 25.0)  # 25°C default
        self.temperature = np.ones((nx, ny, nz)) * ambient_temp
        
        # Initialize material grid (0 = air, 1 = material)
        self.grid = np.zeros((nx, ny, nz))
        
        print(f"Initialized grid with dimensions {self.grid.shape}")
        
    def add_layer(self, layer_data: Dict[str, Any], z_level: int) -> None:
        """
        Add a printed layer to the simulation
        
        Args:
            layer_data: Layer geometry data
            z_level: Z-level in the grid
        """
        if self.grid is None:
            raise ValueError("Grid not initialized")
            
        # In a real implementation, this would convert toolpath to material grid
        # Here we just simulate a simple shape
        
        nx, ny, _ = self.grid.shape
        center_x, center_y = nx // 2, ny // 2
        radius = min(center_x, center_y) - 5
        
        # Create a circular layer
        for i in range(nx):
            for j in range(ny):
                dist = np.sqrt((i - center_x)**2 + (j - center_y)**2)
                if dist <= radius:
                    self.grid[i, j, z_level] = 1  # Material
                    
                    # Set initial temperature for newly printed material
                    extrusion_temp = self.config.get("extrusion_temperature", 200.0)
                    self.temperature[i, j, z_level] = extrusion_temp
        
    def simulate_step(self) -> None:
        """
        Simulate one time step of thermal diffusion
        """
        if self.grid is None or self.temperature is None:
            raise ValueError("Grid not initialized")
            
        # Get simulation parameters
        time_step = self.config.get("time_step", 0.1)  # seconds
        material = self.config.get("material", {})
        
        # Material properties (defaults if not specified)
        thermal_conductivity = material.get("thermal_conductivity", 0.5)  # W/(m·K)
        specific_heat = material.get("specific_heat", 2000.0)  # J/(kg·K)
        density = material.get("density", 1.0)  # g/cm³
        
        # Ambient conditions
        ambient_temp = self.config.get("ambient_temperature", 25.0)  # °C
        convection_coeff = self.config.get("convection_coefficient", 10.0)  # W/(m²·K)
        
        # Create a copy of the current temperature grid
        new_temp = self.temperature.copy()
        
        # Simple finite difference method for heat diffusion
        # In a real implementation, this would use a proper FEM solver like FEniCS
        nx, ny, nz = self.grid.shape
        for i in range(1, nx-1):
            for j in range(1, ny-1):
                for k in range(1, nz-1):
                    if self.grid[i, j, k] > 0:  # Only simulate material points
                        # Diffusion term (Laplacian)
                        laplacian = (
                            self.temperature[i+1, j, k] + 
                            self.temperature[i-1, j, k] + 
                            self.temperature[i, j+1, k] + 
                            self.temperature[i, j-1, k] + 
                            self.temperature[i, j, k+1] + 
                            self.temperature[i, j, k-1] - 
                            6 * self.temperature[i, j, k]
                        )
                        
                        # Diffusion rate
                        alpha = thermal_conductivity / (density * specific_heat)
                        
                        # Update temperature
                        new_temp[i, j, k] += alpha * time_step * laplacian
                        
                        # Convection cooling for exposed surfaces
                        is_surface = False
                        for di, dj, dk in [(1,0,0), (-1,0,0), (0,1,0), (0,-1,0), (0,0,1), (0,0,-1)]:
                            ni, nj, nk = i+di, j+dj, k+dk
                            if 0 <= ni < nx and 0 <= nj < ny and 0 <= nk < nz:
                                if self.grid[ni, nj, nk] == 0:  # Neighbor is air
                                    is_surface = True
                                    break
                        
                        if is_surface:
                            # Convection cooling
                            cooling = convection_coeff * (ambient_temp - self.temperature[i, j, k])
                            new_temp[i, j, k] += cooling * time_step / (density * specific_heat)
        
        # Update temperature grid
        self.temperature = new_temp
        
        # Update simulation time
        self.time += time_step
        
        # Save history (downsampled for efficiency)
        if len(self.history) % 10 == 0:  # Save every 10th step
            self.history.append({
                "time": self.time,
                "max_temp": float(np.max(self.temperature)),
                "min_temp": float(np.min(self.temperature)),
                "avg_temp": float(np.mean(self.temperature[self.grid > 0])) if np.any(self.grid > 0) else ambient_temp
            })
    
    def run_simulation(self, num_steps: int) -> Dict[str, Any]:
        """
        Run the thermal simulation for a specified number of steps
        
        Args:
            num_steps: Number of simulation steps to run
            
        Returns:
            Simulation results summary
        """
        for _ in range(num_steps):
            self.simulate_step()
            
        # Analyze results
        results = self.analyze_results()
        
        return results
    
    def analyze_results(self) -> Dict[str, Any]:
        """
        Analyze the simulation results
        
        Returns:
            Dictionary of analysis results
        """
        if self.grid is None or self.temperature is None:
            raise ValueError("No simulation data available")
            
        # Find areas of potential issues
        cooling_rate_threshold = self.config.get("cooling_rate_threshold", 5.0)  # °C/s
        max_temp_threshold = self.config.get("max_temp_threshold", 250.0)  # °C
        
        # Calculate cooling rates from history
        cooling_rates = []
        for i in range(1, len(self.history)):
            time_diff = self.history[i]["time"] - self.history[i-1]["time"]
            if time_diff > 0:
                temp_diff = self.history[i-1]["max_temp"] - self.history[i]["max_temp"]
                cooling_rates.append(temp_diff / time_diff)
        
        # Find maximum cooling rate
        max_cooling_rate = max(cooling_rates) if cooling_rates else 0.0
        
        # Check for potential issues
        potential_issues = []
        if max_cooling_rate > cooling_rate_threshold:
            potential_issues.append({
                "type": "high_cooling_rate",
                "value": max_cooling_rate,
                "threshold": cooling_rate_threshold,
                "message": f"High cooling rate detected: {max_cooling_rate:.2f}°C/s"
            })
            
        max_temp = np.max(self.temperature)
        if max_temp > max_temp_threshold:
            potential_issues.append({
                "type": "high_temperature",
                "value": float(max_temp),
                "threshold": max_temp_threshold,
                "message": f"High temperature detected: {max_temp:.2f}°C"
            })
        
        # Prepare results
        results = {
            "simulation_time": self.time,
            "num_steps": len(self.history) * 10,  # Accounting for downsampling
            "temperature_stats": {
                "final_max": float(np.max(self.temperature)),
                "final_min": float(np.min(self.temperature)),
                "final_avg": float(np.mean(self.temperature[self.grid > 0])) if np.any(self.grid > 0) else 0.0
            },
            "cooling_stats": {
                "max_cooling_rate": max_cooling_rate,
                "avg_cooling_rate": np.mean(cooling_rates) if cooling_rates else 0.0
            },
            "potential_issues": potential_issues,
            "history": self.history
        }
        
        return results
    
    def save_results(self, results: Dict[str, Any], output_path: str) -> bool:
        """
        Save simulation results to a file
        
        Args:
            results: Simulation results to save
            output_path: Path to save the results
            
        Returns:
            bool: True if saved successfully
        """
        try:
            os.makedirs(os.path.dirname(output_path), exist_ok=True)
            with open(output_path, 'w') as f:
                json.dump(results, f, indent=2)
            return True
        except Exception as e:
            print(f"Error saving simulation results: {e}")
            return False