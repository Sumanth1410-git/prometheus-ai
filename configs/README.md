# Configuration

This directory contains the declarative configuration artifacts for **PROMETHEUS**.

Configuration is version-controlled where appropriate and organized by environment, configuration domain, validation boundary, and deployment concern.

## Configuration Architecture

The configuration layer is divided into:

- Environment-specific configuration
- Default configuration
- Configuration schemas
- Feature flags
- AI configuration
- Infrastructure configuration
- Observability configuration
- Security configuration
- Templates
- Validation artifacts

Runtime configuration loading and the Configuration Registry are implemented as part of the shared platform configuration component in Phase 2.

## Environments

**PROMETHEUS** supports six configuration environments:

| Environment | Directory | Purpose |
|---|---|---|
| Development | `development/` | Active development environment |
| Local Testing | `testing/` | Local testing and validation |
| Integration | `integration/` | Integration testing across components |
| Staging | `staging/` | Pre-production validation |
| Production | `production/` | Production deployment |
| Research Sandbox | `research/` | Isolated research and experimentation |

The standard promotion path is:

```text
Development -> Testing -> Integration -> Staging -> Production
```

The Research Sandbox is experimental and is not part of the standard promotion path.

## Directory Structure

```text
configs/
├── defaults/
├── development/
├── testing/
├── integration/
├── staging/
├── production/
├── research/
├── schemas/
├── feature_flags/
├── templates/
├── ai/
├── infrastructure/
├── observability/
├── security/
└── validation/
```

## Configuration Domains

### `defaults/`

Contains baseline configuration values shared across environments.

Defaults provide the common configuration baseline. Environment-specific configuration may override or extend these values.

### Environment Directories

Each environment contains configuration for:

- Application
- Database
- AI
- Storage
- Cache
- Security
- Logging
- Monitoring
- Features

Environment-specific configuration is intended to describe deployment-specific behavior without embedding secrets directly into version-controlled files.

### `schemas/`

Contains umbrella schemas for configuration categories.

The schemas are organized by configuration domain rather than requiring one schema file for every individual YAML configuration file.

| Schema | Covers |
|---|---|
| `application.schema.yaml` | Application configuration |
| `ai.schema.yaml` | AI-related configuration |
| `infrastructure.schema.yaml` | Infrastructure, database, cache, and storage configuration |
| `security.schema.yaml` | Security configuration |
| `observability.schema.yaml` | Logging, metrics, monitoring, tracing, alerts, and related observability configuration |
| `feature_flags.schema.yaml` | Feature flag configuration |

### `feature_flags/`

Contains feature flag definitions and rollout-related configuration.

### `ai/`

Contains AI-specific configuration, including:

- Providers
- Prompts
- Embeddings
- Retrieval
- Reasoning
- Evaluation
- Safety

### `infrastructure/`

Contains infrastructure configuration for:

- PostgreSQL
- Redis
- Qdrant
- Neo4j
- Object storage
- Networking
- Deployment

### `observability/`

Contains configuration related to:

- Logging
- Metrics
- Tracing
- Alerts
- Dashboards
- Health checks

### `security/`

Contains security-related configuration and reserved locations for security templates, secret-provider references, and rotation-related configuration.

Secret values must not be committed to version control.

### `templates/`

Reserved for reusable configuration templates.

Template structure and contents will be specified as the corresponding configuration requirements are implemented.

### `validation/`

Reserved for configuration validation artifacts.

Validation rules and supporting artifacts will be specified as the configuration validation requirements are implemented.

## Configuration Metadata

Configuration files must include the required metadata defined by the engineering specification:

- Version
- Owner
- Last updated
- Compatible application version
- Migration notes

Each configuration group must document:

- Purpose
- Supported fields
- Defaults
- Examples
- Validation rules
- Compatibility notes

## Environment Variables

Deployment-specific values may be supplied through environment variables.

The defined environment-variable contract includes:

```text
PORT
HOST
DATABASE_URL
REDIS_URL
OBJECT_STORAGE_ENDPOINT
VECTOR_DB_URL
GRAPH_DB_URL
SECRET_PROVIDER
```

Environment variables are intended for deployment-specific values and must not be used to encode business configuration.

## Configuration Loading Boundary

Phase 1 establishes the declarative configuration structure, templates, and environment-variable contract.

The Phase 2 Configuration Manager / Configuration Registry is responsible for runtime configuration management, including loading and runtime behavior.

The documented configuration precedence is:

```text
Default
    |
Environment
    |
Environment Variables
    |
Runtime Overrides
```

Each configuration layer must be validated according to the applicable configuration rules.

## Security

Secrets must never be committed as plaintext values.

Version-controlled configuration may contain:

- Non-secret configuration
- Secret references
- Secret-provider configuration
- Templates
- Rotation metadata
- Validation rules

Actual secret values must be supplied through the appropriate secret-management mechanism.

## Current Scope

This directory currently establishes the configuration structure and declarative configuration boundary for Phase 1.

Infrastructure provisioning, runtime configuration loading, Configuration Registry behavior, runtime overrides, startup enforcement, and other runtime configuration capabilities belong to their respective implementation phases.
