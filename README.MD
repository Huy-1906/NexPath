# NexPath: Intelligent Platform for Large Format Additive Manufacturing (LFAM)

---

## Table of Contents
- [Introduction](#introduction)
- [Key Features](#key-features)
- [System Architecture](#system-architecture)
- [Technology Stack](#technology-stack)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Development Setup](#development-setup)
  - [Production Deployment (Docker)](#production-deployment-docker)
- [Running the Application](#running-the-application)
- [Testing](#testing)
- [Contributing](#contributing)
- [FAQ](#faq)
- [Support & Contact](#support--contact)
- [License](#license)

---

## Introduction
NexPath is an advanced, modular software platform designed for Large Format Additive Manufacturing (LFAM). It integrates AI-driven toolpath generation, real-time thermal simulation, process monitoring, and hybrid manufacturing capabilities. NexPath empowers industrial-scale 3D printing with intelligent algorithms, comprehensive analysis tools, and a modern, cross-platform user interface.

Whether you are a researcher, engineer, or manufacturer, NexPath provides the tools to optimize your additive manufacturing processes, reduce defects, and accelerate innovation.

---

## Key Features
- **AI-Powered Toolpath Generation**: Automatically generate optimized toolpaths using machine learning models trained on geometric and mechanical datasets. Supports custom infill patterns and advanced printing strategies.
- **Real-Time Thermal Simulation**: Predict and visualize temperature distribution during deposition using FEniCS-based finite element analysis. Prevent defects and ensure part quality.
- **Process Monitoring**: Track and analyze thermal data, deposition rates, and material usage in real time. Integrate with sensors and machine feedback for closed-loop control.
- **Hybrid Manufacturing**: Seamlessly coordinate additive and subtractive processes, enabling machining operations between deposition layers.
- **Cross-Platform Interface**: Access NexPath via a modern web application or an Electron-based desktop app, both built with React, TailwindCSS, and Three.js for 3D visualization.
- **Extensible Plugin System**: Customize and extend platform functionality with third-party tools and manufacturer-specific modules.
- **Cloud-Ready Backend**: FastAPI-based server provides robust API services, database access, authentication, and job management.

---

## System Architecture
NexPath is built with a modular, layered architecture for scalability and maintainability:

```text
┌──────────────────────────────────────────────┐
│                UI/UX Layer                  │
│   (React, TailwindCSS, Electron, Three.js)   │
└──────────────────────┬───────────────────────┘
                      │
┌─────────────────────┼───────────────────────┐
│                API Layer                    │
│      (FastAPI, Node.js, Redis)              │
└─────────────────────┬───────────────────────┘
                      │
┌─────────────┬─────────────┬─────────────┬─────────────┐
│ AI Copilot  │ Thermal Sim │ Toolpath    │ Hybrid      │
│ (PyTorch)   │ (FEniCS)    │ Generator   │ Manufacturing│
│             │             │ (Python)    │ Module      │
└─────────────┴─────────────┴─────────────┴─────────────┘
```

### Core Modules
- **UI/UX Layer**: Modern, responsive interface for both web and desktop, with 3D visualization.
- **AI Copilot**: Machine learning algorithms for toolpath optimization based on part geometry, material, and constraints.
- **Thermal Simulation Engine**: FEniCS-based finite element analysis for temperature prediction and thermal history.
- **Toolpath Generator**: Advanced slicing engine converting 3D models into optimized machine instructions.
- **Hybrid Manufacturing Module**: Coordinates additive and subtractive operations.
- **Real-Time Monitoring**: Collects and analyzes sensor data, thermal imaging, and machine feedback.
- **Cloud Backend**: FastAPI server for API, database, authentication, and job management.

---

## Technology Stack
| Layer      | Technologies Used                                 |
|------------|---------------------------------------------------|
| Frontend   | React, TailwindCSS, Material-UI, Three.js, Electron |
| Backend    | FastAPI, SQLAlchemy, PostgreSQL, Redis            |
| AI/ML      | PyTorch, NumPy, Scikit-learn                      |
| Simulation | FEniCS, NumPy                                     |
| DevOps     | Docker, Nginx                                     |

---

## Project Structure
```text
NexPath/
├── frontend/         # React-based GUI (Web/Electron)
│   ├── electron/     # Electron-specific code
│   ├── src/          # React source code
│   │   ├── components/ # Reusable UI components
│   │   ├── pages/      # Page components
│   │   └── utils/      # Utility functions
├── backend/          # FastAPI server for API handling
│   ├── api/          # API endpoints
│   ├── models/       # Database models
│   ├── services/     # Business logic
│   └── utils/        # Utility functions
├── engine/           # Core slicing, simulation, AI logic
│   ├── slicer/       # Toolpath generation
│   ├── thermal_sim/  # Thermal simulation
│   └── ai_copilot/   # AI optimization
├── data/             # Toolpath datasets, material profiles, logs
├── docs/             # Documentation
├── tests/            # Unit/integration tests
├── docker/           # Docker configuration
```

---

## Getting Started

### Prerequisites
- **Docker** and **Docker Compose** (for containerized deployment)
- **Node.js** (v16+) for frontend development
- **Python** (3.9+) for backend development
- **Git**

### Development Setup
1. **Clone the repository**
   ```sh
   git clone https://github.com/yourusername/nexpath.git
   cd nexpath
   ```
2. **Backend Setup**
   ```sh
   python -m venv .venv
   # On Windows:
   .venv\Scripts\activate
   # On Linux/macOS:
   source .venv/bin/activate
   cd backend
   pip install -r requirements.txt
   ```
3. **Frontend Setup**
   ```sh
   cd ../frontend
   npm install
   ```
4. **Start the Backend Server**
   ```sh
   cd ../backend
   uvicorn main:app --reload --host 0.0.0.0 --port 8000
   ```
5. **Start the Frontend Application**
   - For Web:
     ```sh
     cd ../frontend
     npm run dev
     ```
   - For Desktop (Electron):
     ```sh
     cd ../frontend
     npm run electron:dev
     ```

### Production Deployment (Docker)
For a fully containerized environment:
```sh
docker-compose up -d
```
Access the web interface at [http://localhost:80](http://localhost:80)

---

## Running the Application
- **Backend (Development):**
  ```sh
  cd backend
  uvicorn main:app --reload --host 0.0.0.0 --port 8000
  ```
- **Frontend (Web):**
  ```sh
  cd frontend
  npm run dev
  ```
- **Frontend (Desktop):**
  ```sh
  cd frontend
  npm run electron:dev
  ```
- **Production:**
  ```sh
  docker-compose up -d
  ```

---

## Testing
- **Backend Tests:**
  ```sh
  cd backend
  python -m pytest
  ```
- **Frontend Tests:**
  ```sh
  cd frontend
  npm test
  ```

---

## Contributing
We welcome contributions from the community! To contribute:
1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature-name`
3. Commit your changes: `git commit -m 'Add some feature'`
4. Push to your branch: `git push origin feature/your-feature-name`
5. Open a pull request

Please read our [contributing guidelines](docs/user/CONTRIBUTING.md) (if available) before submitting a PR.

---

## FAQ
**Q: What platforms are supported?**
A: NexPath supports Windows, macOS, and Linux for both web and desktop (Electron) applications.

**Q: Can I use my own AI models or plugins?**
A: Yes! NexPath is designed to be extensible. You can add custom plugins and integrate your own AI models.

**Q: How do I report bugs or request features?**
A: Please open an issue on our GitHub repository or contact us directly (see below).

---

## Support & Contact
For questions, support, or collaboration opportunities:
- Email: giahuy196cv@gmail.com
- Website: [Coming Soon]

---

## License
This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

© 2025 NexPath. All rights reserved.