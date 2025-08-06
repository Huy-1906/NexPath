import numpy as np
from typing import List, Dict, Any, Tuple

class Slicer:
    def __init__(self, config: Dict[str, Any]):
        """
        Initialize the slicer with configuration parameters
        
        Args:
            config: Dictionary containing slicer configuration
                - layer_height: Height of each layer in mm
                - infill_density: Percentage of infill (0.0 to 1.0)
                - wall_thickness: Thickness of outer walls in mm
                - print_speed: Print speed in mm/s
        """
        self.config = config
        self.model = None
        self.layers = []
        
    def load_model(self, file_path: str) -> bool:
        """
        Load a 3D model from file
        
        Args:
            file_path: Path to the STL or OBJ file
            
        Returns:
            bool: True if model loaded successfully
        """
        try:
            # In a real implementation, we would use a library like numpy-stl or trimesh
            # to load the actual 3D model
            print(f"Loading model from {file_path}")
            self.model = {"path": file_path, "loaded": True}
            return True
        except Exception as e:
            print(f"Error loading model: {e}")
            return False
    
    def slice(self) -> List[Dict[str, Any]]:
        """
        Slice the loaded model into layers
        
        Returns:
            List of layer data
        """
        if not self.model:
            raise ValueError("No model loaded")
            
        # In a real implementation, this would perform actual slicing
        # Here we just simulate the process
        layer_height = self.config.get("layer_height", 0.2)
        model_height = 100  # Simulated model height in mm
        
        num_layers = int(model_height / layer_height)
        self.layers = []
        
        for i in range(num_layers):
            z_height = i * layer_height
            # Simulate layer contours and paths
            layer = {
                "layer_num": i,
                "z_height": z_height,
                "contours": self._generate_dummy_contours(z_height),
                "infill": self._generate_dummy_infill(z_height)
            }
            self.layers.append(layer)
            
        return self.layers
    
    def _generate_dummy_contours(self, z_height: float) -> List[List[Tuple[float, float]]]:
        """
        Generate dummy contour data for visualization
        """
        # Simulate a simple shape that changes with height
        radius = 50 - (z_height / 10)
        if radius < 10:
            radius = 10
            
        # Create a circle contour
        points = []
        for angle in range(0, 360, 10):
            rad = np.radians(angle)
            x = radius * np.cos(rad)
            y = radius * np.sin(rad)
            points.append((float(x), float(y)))
            
        return [points]  # List of contours (just one in this case)
    
    def _generate_dummy_infill(self, z_height: float) -> List[List[Tuple[float, float]]]:
        """
        Generate dummy infill pattern
        """
        infill_density = self.config.get("infill_density", 0.2)
        spacing = 10 / infill_density  # Adjust spacing based on density
        
        # Create a grid pattern
        lines = []
        radius = 50 - (z_height / 10)
        if radius < 10:
            radius = 10
            
        # Horizontal lines
        for y in np.arange(-radius, radius, spacing):
            lines.append([(-radius, float(y)), (radius, float(y))])
            
        # Vertical lines
        for x in np.arange(-radius, radius, spacing):
            lines.append([(float(x), -radius), (float(x), radius)])
            
        return lines
    
    def generate_gcode(self, output_path: str) -> bool:
        """
        Generate G-code from the sliced layers
        
        Args:
            output_path: Path to save the G-code file
            
        Returns:
            bool: True if G-code generated successfully
        """
        if not self.layers:
            raise ValueError("No sliced layers available")
            
        try:
            with open(output_path, 'w') as f:
                # Write G-code header
                f.write("; NexPath LFAM G-code\n")
                f.write(f"; Generated on {np.datetime64('now')}\n")
                f.write(f"; Layer height: {self.config.get('layer_height', 0.2)}mm\n")
                f.write(f"; Infill density: {self.config.get('infill_density', 0.2) * 100}%\n")
                f.write("\n")
                
                # Initialize
                f.write("G28 ; Home all axes\n")
                f.write("G90 ; Use absolute coordinates\n")
                f.write("M82 ; Use absolute distances for extrusion\n")
                f.write("M140 S60 ; Set bed temperature\n")
                f.write("M190 S60 ; Wait for bed temperature\n")
                f.write("M104 S200 ; Set extruder temperature\n")
                f.write("M109 S200 ; Wait for extruder temperature\n")
                f.write("G92 E0 ; Reset extruder position\n")
                f.write("G1 Z0.2 F3000 ; Move to start position\n")
                f.write("G1 X0 Y0 F3000 ; Move to start position\n")
                f.write("\n")
                
                # Process each layer
                for layer in self.layers:
                    f.write(f"; Layer {layer['layer_num']}, Z = {layer['z_height']}\n")
                    f.write(f"G1 Z{layer['z_height']} F3000 ; Move to layer height\n")
                    
                    # Process contours
                    for contour in layer['contours']:
                        # Move to first point without extruding
                        first_point = contour[0]
                        f.write(f"G1 X{first_point[0]} Y{first_point[1]} F3000 ; Move to contour start\n")
                        f.write("G1 E0.5 F1500 ; Prime extruder\n")
                        
                        # Trace contour
                        for point in contour[1:] + [contour[0]]:  # Close the loop
                            f.write(f"G1 X{point[0]} Y{point[1]} E1 F1500 ; Contour\n")
                    
                    # Process infill
                    f.write("G1 E-0.5 F1800 ; Retract\n")
                    for line in layer['infill']:
                        # Move to line start
                        f.write(f"G1 X{line[0][0]} Y{line[0][1]} F3000 ; Move to infill line\n")
                        f.write("G1 E0.5 F1500 ; Prime extruder\n")
                        
                        # Draw line
                        f.write(f"G1 X{line[1][0]} Y{line[1][1]} E1 F1500 ; Infill\n")
                        f.write("G1 E-0.5 F1800 ; Retract\n")
                
                # End G-code
                f.write("\n")
                f.write("G1 E-2 F1800 ; Retract\n")
                f.write("G1 Z" + str(self.layers[-1]['z_height'] + 10) + " F3000 ; Move Z up\n")
                f.write("G1 X0 Y0 F3000 ; Move to origin\n")
                f.write("M104 S0 ; Turn off extruder\n")
                f.write("M140 S0 ; Turn off bed\n")
                f.write("M84 ; Disable motors\n")
                
            return True
        except Exception as e:
            print(f"Error generating G-code: {e}")
            return False