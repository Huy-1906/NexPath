


          
# NexPath - LFAM Platform

![NexPath Logo](https://via.placeholder.com/200x80?text=NexPath)

## Overview

NexPath is an intelligent software platform for Large Format Additive Manufacturing (LFAM) that integrates AI-assisted toolpath generation, thermal simulation, real-time process monitoring, and hybrid manufacturing support. The system is designed for industrial-scale 3D printing environments.

## Table of Contents

- [NexPath - LFAM Platform](#nexpath---lfam-platform)
  - [Overview](#overview)
  - [Table of Contents](#table-of-contents)
  - [Features](#features)
  - [Architecture](#architecture)
  - [Installation](#installation)
    - [Prerequisites](#prerequisites)
    - [Development Setup](#development-setup)
    - [Docker Setup](#docker-setup)
  - [Usage](#usage)
    - [Running the Application](#running-the-application)
      - [Development Mode](#development-mode)
      - [Production Mode (Docker)](#production-mode-docker)
    - [User Interface](#user-interface)
  - [Core Modules](#core-modules)
    - [UI/UX Layer](#uiux-layer)
    - [AI Copilot](#ai-copilot)
    - [Thermal Simulation Engine](#thermal-simulation-engine)
    - [Toolpath Generator](#toolpath-generator)
    - [Hybrid Manufacturing Module](#hybrid-manufacturing-module)
    - [Real-Time Monitoring](#real-time-monitoring)
    - [Cloud Backend](#cloud-backend)
    - [Plugin API System](#plugin-api-system)
  - [Development](#development)
    - [Project Structure](#project-structure)
    - [Technology Stack](#technology-stack)
    - [Contributing](#contributing)
  - [Testing](#testing)
  - [Deployment](#deployment)
    - [Docker Deployment](#docker-deployment)
    - [Manual Deployment](#manual-deployment)
  - [License](#license)
  - [Contact](#contact)

## Features

- **AI-Assisted Toolpath Generation**: Automatically generate optimized toolpaths using machine learning models trained on geometric and mechanical datasets.
- **Thermal Simulation**: Predict and visualize thermal behavior during deposition to prevent warping, delamination, and other issues.
- **Real-Time Process Monitoring**: Capture and analyze thermal camera data, deposition rate, material usage, and other metrics during printing.
- **Hybrid Manufacturing Support**: Coordinate additive and subtractive manufacturing processes with CAM integration.
- **Cross-Platform Interface**: Intuitive UI for designers, engineers, and operators, available on desktop and web.
- **Plugin System**: Extensible architecture allowing third-party tools and manufacturers to build custom modules.

## Architecture

NexPath follows a modular architecture with the following components:

```
┌─────────────────────────────────────────────────────────────┐
│                        UI/UX Layer                           │
│           (React, TailwindCSS, Electron, Three.js)          │
└───────────────────────────────┬─────────────────────────────┘
                                │
┌───────────────────────────────┼─────────────────────────────┐
│                        API Layer                             │
│                  (FastAPI, Node.js, Redis)                   │
└───────────────────────────────┬─────────────────────────────┘
                                │
┌─────────────┬─────────────┬───┴───────┬─────────────┬───────┐
│  AI Copilot │   Thermal   │  Toolpath │    Hybrid   │ Real- │
│             │ Simulation  │ Generator │ Manufacturing│ Time  │
│  (PyTorch)  │  (FEniCS)   │  (Python) │   Module    │Monitor│
└─────────────┴─────────────┴───────────┴─────────────┴───────┘
```

## Installation

### Prerequisites

- Docker and Docker Compose
- Node.js 16+ (for local development)
- Python 3.9+ (for local development)
- Git

### Development Setup

1. Clone the repository:

```bash
git clone https://github.com/yourusername/nexpath.git
cd nexpath
```

2. Set up the Python virtual environment:

```bash
python -m venv .venv
.venv\Scripts\activate
cd backend
pip install -r requirements.txt
```

3. Set up the frontend:

```bash
cd ../frontend
npm install
```

### Docker Setup

For a complete environment with all services:

```bash
docker-compose up -d --build
```

This will start the following services:
- Frontend (React + Electron)
- Backend API (FastAPI)
- Database (PostgreSQL)
- Cache (Redis)

## Usage

### Running the Application

#### Development Mode

1. Start the backend:

```bash
cd backend
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

2. Start the frontend:

```bash
cd frontend
npm run dev
```

3. For Electron desktop app:

```bash
cd frontend
npm run electron:dev
```

#### Production Mode (Docker)

```bash
docker-compose up -d
```

Access the web interface at http://localhost:80

### User Interface

The NexPath interface consists of the following main sections:

- **Dashboard**: Overview of recent projects, system status, and quick actions
- **Model Viewer**: 3D visualization of models with analysis tools
- **Toolpath Generator**: Create and edit toolpaths with AI assistance
- **Thermal Simulation**: Run and visualize thermal simulations
- **Settings**: Configure system parameters and user preferences

## Core Modules

### UI/UX Layer

The user interface is built with React, TailwindCSS, and Material-UI components. For desktop applications, Electron is used to create a native experience.

**Key files:**
- `frontend/src/App.jsx`: Main application component
- `frontend/src/components/Layout.jsx`: Application layout structure
- `frontend/src/pages/`: Individual page components

### AI Copilot

The AI Copilot module uses machine learning to optimize toolpaths based on geometric features, material properties, and manufacturing constraints.

**Key files:**
- `engine/ai_copilot/ai_optimizer.py`: Core AI optimization algorithms

### Thermal Simulation Engine

The thermal simulation engine predicts temperature distribution and thermal history during the printing process using finite element analysis.

**Key files:**
- `engine/thermal_sim/thermal_simulator.py`: Thermal simulation implementation

### Toolpath Generator

The toolpath generator converts 3D models into machine instructions (G-code) with support for various infill patterns, layer heights, and printing strategies.

**Key files:**
- `engine/slicer/slicer.py`: Core slicing and toolpath generation logic

### Hybrid Manufacturing Module

This module coordinates additive and subtractive processes, allowing for machining operations between deposition layers.

### Real-Time Monitoring

The monitoring system collects and analyzes data from sensors, cameras, and machine controllers during printing.

### Cloud Backend

The backend provides API services, database access, authentication, and job management.

**Key files:**
- `backend/main.py`: Main FastAPI application
- `backend/models/`: Database models and schemas
- `backend/api/`: API endpoints

### Plugin API System

The plugin system allows third-party developers to extend NexPath functionality with custom modules.

## Development

### Project Structure

```
nexpath/
├── frontend/              # React-based GUI (Electron or Web)
│   ├── electron/          # Electron-specific code
│   ├── src/               # React source code
│   │   ├── components/    # Reusable UI components
│   │   ├── pages/         # Page components
│   │   └── utils/         # Utility functions
│   └── ... 
├── backend/               # FastAPI server for API handling
│   ├── api/               # API endpoints
│   ├── models/            # Database models
│   ├── services/          # Business logic
│   └── utils/             # Utility functions
├── engine/                # Core slicing, simulation, AI logic
│   ├── slicer/            # Toolpath generation
│   ├── thermal_sim/       # Thermal simulation
│   └── ai_copilot/        # AI optimization
├── data/                  # Toolpath datasets, material profiles, logs
├── docs/                  # Documentation
├── tests/                 # Unit/integration tests
└── docker/                # Docker configuration
```

### Technology Stack

**Frontend:**
- React.js with Hooks and Context API
- TailwindCSS for styling
- Material-UI components
- Three.js for 3D visualization
- Electron for desktop applications

**Backend:**
- FastAPI (Python) for REST API
- SQLAlchemy for ORM
- PostgreSQL for database
- Redis for caching and job queues

**AI/ML Components:**
- PyTorch for machine learning models
- NumPy for numerical computing
- Scikit-learn for data processing

**Simulation:**
- FEniCS for finite element analysis
- NumPy for numerical operations

**DevOps:**
- Docker and Docker Compose for containerization
- Nginx for reverse proxy

### Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature-name`
3. Commit your changes: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin feature/your-feature-name`
5. Open a pull request

## Testing

NexPath uses a combination of unit tests, integration tests, and end-to-end tests.

```bash
# Run backend tests
cd backend
python -m pytest

# Run frontend tests
cd frontend
npm test
```

## Deployment

### Docker Deployment

The recommended deployment method is using Docker Compose:

```bash
docker-compose -f docker-compose.yml -f docker-compose.prod.yml up -d
```

### Manual Deployment

For manual deployment, refer to the detailed instructions in the `docs/deployment.md` file.

## License

This project is licensed under the [MIT License](LICENSE).

## Contact

For questions, support, or collaboration opportunities, please contact:

- Email: giahuy196cv@gmail.com
- Website: 

---

© 2025 NexPath. All rights reserved.

        # NexPath
# NexPath
# NexPath
# NexPath
