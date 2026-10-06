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
│   ├── sql_injection_test.py # SQL injection test module
│   ├── xss_test.py           # XSS test module
│   ├── command_injection_test.py # Command injection test module
│   ├── ldap_injection_test.py # LDAP injection test module
│   ├── nosql_injection_test.py # NoSQL injection test module
│   └── broken_authentication_test.py # Broken authentication test module
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
- `sql_injection_test`: Tests for SQL injection vulnerabilities
- `xss_test`: Tests for Cross-Site Scripting vulnerabilities
- `command_injection_test`: Tests for Command Injection vulnerabilities
- `ldap_injection_test`: Tests for LDAP Injection vulnerabilities
- `nosql_injection_test`: Tests for NoSQL Injection vulnerabilities
- `broken_authentication_test`: Tests for Broken Authentication vulnerabilities
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

1. **Phase 1 - Foundation**: Core engine, modules, HTTP client, CLI (COMPLETED)
2. **Phase 2 - Reconnaissance**: Technology detection, JavaScript analysis, parameter discovery, API discovery, security-header analysis (COMPLETED)
3. **Phase 3 - AI Integration**: Ollama integration, structured AI responses (COMPLETED)
4. **Phase 4 - AI Planning**: Attack-surface analysis, module selection, result correlation (COMPLETED)
5. **Phase 5 - Vulnerability Testing**: Individual vulnerability modules (COMPLETED - Full OWASP Top 10 coverage)
6. **Phase 6 - Reporting**: HTML and JSON reports (IN PROGRESS)
7. **Phase 7 - Autonomous Workflow**: Complete autonomous testing workflow (IN PROGRESS)

## Current Status

The framework currently implements:
- Core engine with modular architecture
- Endpoint discovery module
- SQL injection test module
- XSS test module
- Command injection test module
- LDAP injection test module
- NoSQL injection test module
- Broken authentication test module
- AI analysis and planning capabilities
- HTTP client abstraction
- Structured findings system

The framework is designed to be easily extensible with additional vulnerability testing modules for full OWASP Top 10 coverage.

## Vulnerability Testing

The framework currently includes:
- **Endpoint Discovery** - Basic reconnaissance
- **SQL Injection Test** - Basic SQL injection detection
- **XSS Test** - Basic XSS detection
- **Command Injection Test** - Command injection detection
- **LDAP Injection Test** - LDAP injection detection
- **NoSQL Injection Test** - NoSQL injection detection
- **Broken Authentication Test** - Broken authentication detection

Additional OWASP Top 10 vulnerability modules are in development and will be added incrementally.

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