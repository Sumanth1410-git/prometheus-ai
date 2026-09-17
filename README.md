# PROMETHEUS

**PROMETHEUS — An Intrinsically Motivated Cognitive Architecture for Autonomous Scientific Knowledge Discovery**

PROMETHEUS is an AI research project focused on cognitive architectures, knowledge representation, scientific knowledge discovery, intrinsic motivation, curiosity-driven learning, knowledge graphs, and autonomous reasoning.

## Project Status

**Phase:** Phase 1 — Execution Platform Preparation

The project specifications and engineering documentation have been established and validated. Implementation is now progressing through the approved implementation roadmap.

### Completed

- Repository foundation and canonical project structure
- Engineering and product documentation baseline
- Development tooling baseline
- CI quality checks
- Pre-commit validation
- Development Docker container baseline
- Container build and runtime validation
- Ruff, Black, and Pytest validation inside the development container
- Python package dependency validation with `pip check`

### Current Focus

**Phase 1 — Execution Platform Preparation**

The current implementation focus is establishing the execution and infrastructure foundation before higher-level platform services and cognitive modules are implemented.

## Documentation

### Product Documentation

- [Project Vision](docs/product/00_ProjectVision.md)
- [Brand Identity](docs/product/01_BrandIdentity.md)
- [Design System](docs/product/02_DesignSystem.md)
- [Information Architecture](docs/product/03_InformationArchitecture.md)

### Engineering Documentation

- [Scope & Research Boundary](docs/engineering/01_Scope_and_Research_Boundary.md)
- [Design Decision Log](docs/engineering/02_Design_Decision_Log.md)
- [Module Specification](docs/engineering/03_Module_Specification.md)
- [System Architecture](docs/engineering/04_System_Architecture.md)
- [Implementation Roadmap](docs/engineering/05_Implementation_Roadmap.md)
- [Project File Structure](docs/engineering/06_Project_File_Structure.md)
- [Development Workflow](docs/engineering/07_Development_Workflow.md)
- [Claude Implementation Guide](docs/engineering/08_Claude_Implementation_Guide.md)

## Development Environment

The project currently provides a development Docker image based on Python 3.13.

The development container includes the project's development tooling and runs under a dedicated non-root user.

Container validation currently includes:

- Ruff
- Black
- Pytest
- `pip check`

## Development Philosophy

PROMETHEUS follows an architecture-first, verification-driven development process.

Implementation must remain consistent with the approved project specifications.

## Repository

GitHub: https://github.com/Sumanth1410-git/prometheus-ai
