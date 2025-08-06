# NexPath - Intelligent LFAM Platform
## Overview
NexPath is an advanced software platform for Large Format Additive Manufacturing (LFAM) that integrates AI-driven toolpath generation, thermal simulation, real-time monitoring, and hybrid manufacturing capabilities. Designed for industrial-scale 3D printing, NexPath optimizes manufacturing processes through intelligent algorithms and comprehensive analysis tools.

## Features
- AI-Powered Toolpath Generation : Create optimized toolpaths automatically using machine learning models trained on geometric and mechanical datasets
- Real-Time Thermal Simulation : Predict and visualize thermal behavior during deposition to prevent defects and ensure part quality
- Process Monitoring : Track and analyze thermal data, deposition rates, and material usage during printing operations
- Hybrid Manufacturing : Seamlessly coordinate additive and subtractive processes with integrated CAM functionality
- Cross-Platform Interface : Access the platform through intuitive web and desktop applications
- Extensible Plugin System : Customize functionality with third-party tools and manufacturer-specific modules
## Quick Start
### Prerequisites
- Docker and Docker Compose
- Node.js 16+ (for development)
- Python 3.9+ (for development)
- Git
### Development Setup
1. 1.
   Clone the repository
```
git clone https://github.com/yourusername/nexpath.
git
cd nexpath
```
2. 1.
   Backend setup
```
python -m venv .venv
.venv\Scripts\activate
cd backend
pip install -r requirements.txt
```
3. 1.
   Frontend setup
```
cd ../frontend
npm install
```
4. 1.
   Start the backend server
```
cd ../backend
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```
5. 1.
   Start the frontend application
```
cd ../frontend
npm run dev  # For web interface
# OR
npm run electron:dev  # For desktop application
```
### Docker Deployment
For a complete containerized environment:

```
docker-compose up -d
```
Access the web interface at http://localhost:80

## Architecture
NexPath follows a modular architecture with clear separation of concerns:

```
┌───────────────────────────────────────────────────
──────────┐
│                        UI/UX 
Layer                           │
│           (React, TailwindCSS, Electron, Three.
js)          │
└───────────────────────────────┬───────────────────
──────────┘
                                │
┌───────────────────────────────┼───────────────────
──────────┐
│                        API 
Layer                             │
│                  (FastAPI, Node.js, 
Redis)                   │
└───────────────────────────────┬───────────────────
──────────┘
                                │
┌─────────────┬─────────────┬───┴───────┬───────────
──┬───────┐
│  AI Copilot │   Thermal   │  Toolpath │    
Hybrid   │ Real- │
│             │ Simulation  │ Generator │ 
Manufacturing│ Time  │
│  (PyTorch)  │  (FEniCS)   │  (Python) │   
Module    │Monitor│
└─────────────┴─────────────┴───────────┴───────────
──┴───────┘
```
## Core Modules
### UI/UX Layer
Modern, responsive interface built with React, TailwindCSS, and Three.js for 3D visualization. Available as both web application and Electron-based desktop app.

### AI Copilot
Machine learning algorithms that optimize toolpaths based on part geometry, material properties, and manufacturing constraints.

### Thermal Simulation Engine
FEniCS-based finite element analysis that predicts temperature distribution and thermal history during printing.

### Toolpath Generator
Advanced slicing engine that converts 3D models into optimized machine instructions with support for various infill patterns and printing strategies.

### Hybrid Manufacturing Module
Coordinates additive and subtractive processes, enabling machining operations between deposition layers.

### Real-Time Monitoring
Collects and analyzes sensor data, thermal imaging, and machine feedback during printing operations.

### Cloud Backend
FastAPI-based server providing API services, database access, authentication, and job management.

## Project Structure
```
nexpath/
├── frontend/              # React-based GUI 
(Electron or Web)
│   ├── electron/          # Electron-specific code
│   ├── src/               # React source code
│   │   ├── components/    # Reusable UI components
│   │   ├── pages/         # Page components
│   │   └── utils/         # Utility functions
├── backend/               # FastAPI server for API 
handling
│   ├── api/               # API endpoints
│   ├── models/            # Database models
│   ├── services/          # Business logic
│   └── utils/             # Utility functions
├── engine/                # Core slicing, 
simulation, AI logic
│   ├── slicer/            # Toolpath generation
│   ├── thermal_sim/       # Thermal simulation
│   └── ai_copilot/        # AI optimization
├── data/                  # Toolpath datasets, 
material profiles, logs
├── docs/                  # Documentation
├── tests/                 # Unit/integration tests
└── docker/                # Docker configuration
```
## Technology Stack
- Frontend : React, TailwindCSS, Material-UI, Three.js, Electron
- Backend : FastAPI, SQLAlchemy, PostgreSQL, Redis
- AI/ML : PyTorch, NumPy, Scikit-learn
- Simulation : FEniCS, NumPy
- DevOps : Docker, Nginx
## Running the Application
### Development Mode
Backend:

```
cd backend
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```
Frontend (Web):

```
cd frontend
npm run dev
```
Frontend (Desktop):

```
cd frontend
npm run electron:dev
```
### Production Mode
```
docker-compose up -d
```
## Testing
```
# Backend tests
cd backend
python -m pytest

# Frontend tests
cd frontend
npm test
```
## Contributing
1. 1.
   Fork the repository
2. 2.
   Create a feature branch: git checkout -b feature/your-feature-name
3. 3.
   Commit your changes: git commit -m 'Add some feature'
4. 4.
   Push to the branch: git push origin feature/your-feature-name
5. 5.
   Open a pull request
## License
This project is licensed under the MIT License .

## Contact
For questions, support, or collaboration opportunities:

- Email: giahuy196cv@gmail.com
- Website: [Coming Soon]
© 2025 NexPath. All rights reserved.