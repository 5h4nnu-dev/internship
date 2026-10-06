# Web Application Penetration Testing Framework

A modular, AI-assisted web application penetration testing framework inspired by modern security frameworks like Strix.

## Overview

This framework provides a structured approach to automated web application security testing with modular components, AI integration, and a clean architecture designed for extensibility.

## Features

- **Modular Architecture**: Easy to add new security testing capabilities without modifying the core engine
- **AI Integration**: Uses Ollama as local LLM backend for analysis and planning
- **Comprehensive Reconnaissance**: Discovers endpoints, parameters, forms, APIs, and technologies
- **Structured Findings**: Standardized finding structure with severity, confidence, and remediation
- **Controlled Execution**: Explicit target declaration and safety controls for authorized testing
- **Rich CLI**: Terminal-based interface with progress tracking and results display

## Architecture

```
web_pentest_ai/
├── run.py                    # Main CLI entry point
├── core/
│   ├── __init__.py
│   ├── engine.py             # Core assessment engine
│   ├── base_module.py        # Abstract base class for modules
│   ├── target.py             # Target model
│   ├── context.py            # Assessment context management
│   ├── finding.py            # Finding structure
│   └── logger.py             # Logging configuration
├── modules/
│   ├── __init__.py
│   ├── endpoint_discovery.py # Endpoint discovery module
│   └── vulnerability_tests/  # Vulnerability testing modules
├── ai/
│   ├── __init__.py
│   ├── llm.py                # Ollama LLM integration
│   ├── analyzer.py           # AI analysis layer
│   └── planner.py            # AI planning layer
├── crawler/
│   ├── __init__.py
│   └── crawler.py            # Web crawling components
├── http/
│   ├── __init__.py
│   └── client.py             # HTTP client abstraction
├── reports/                  # Reporting components
├── config/                   # Configuration files
├── tests/                    # Unit tests
└── notebooks/                # Jupyter notebooks for analysis
```

## Getting Started

### Prerequisites

- Python 3.7+
- Ollama (for AI features)

### Installation

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Usage

Run a basic assessment:
```bash
python run.py --target https://example.com
```

Run with specific modules:
```bash
python run.py --target https://example.com --modules endpoint_discovery
```

## Components

### Core Engine
The `PentestEngine` orchestrates the entire assessment, managing:
- Target initialization
- Module loading and execution
- Context management
- Results collection and reporting

### Modules
Modules are designed to be independent and extensible:
- `endpoint_discovery`: Discovers endpoints, URLs, and API routes
- Additional modules can be added in the `modules/` directory

### AI Layer
The AI layer provides:
- Analysis of reconnaissance results
- Planning of security modules to run
- Correlation of findings
- Structured LLM responses

### HTTP Client
A centralized HTTP client with:
- Session management
- Request handling and retries
- Cookie and header management
- Rate limiting support

## Safety Controls

The framework is designed for authorized testing with:
- Explicit target declaration
- Scope restrictions
- Request timeouts
- Rate limiting
- Controlled execution
- No unrestricted LLM-generated shell commands

## Roadmap

1. **Phase 1 - Foundation**: Core engine, modules, HTTP client, CLI
2. **Phase 2 - Reconnaissance**: Technology detection, JavaScript analysis, parameter discovery
3. **Phase 3 - AI Integration**: Ollama integration, structured AI responses
4. **Phase 4 - AI Planning**: Attack-surface analysis, module selection
5. **Phase 5 - Vulnerability Testing**: Individual vulnerability modules
6. **Phase 6 - Reporting**: HTML and JSON reports
7. **Phase 7 - Autonomous Workflow**: Complete autonomous testing workflow

## Development

### Adding New Modules

Create a new module in the `modules/` directory:

```python
from core.base_module import BaseModule, ModuleCategory, ModuleResult

class MyNewModule(BaseModule):
    def __init__(self):
        super().__init__(
            name="my_module",
            description="Description of what this module does",
            category=ModuleCategory.RECONNAISSANCE
        )

    def execute(self, context):
        # Implementation here
        return ModuleResult(
            module_name=self.name,
            success=True,
            data={"result": "example"}
        )

def create_module():
    return MyNewModule()
```

## License

This project is intended for authorized security testing, research, and educational purposes only.