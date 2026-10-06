# Phase 2 - Reconnaissance Modules

This document describes the reconnaissance modules implemented in Phase 2 of the web application penetration testing framework.

## Overview

Phase 2 adds comprehensive reconnaissance capabilities to the framework, enabling it to discover and analyze various aspects of a target application's infrastructure and configuration.

## Implemented Modules

### 1. Technology Detection (`technology_detection`)
- Detects technologies, frameworks, and server information
- Analyzes HTTP headers for technology clues
- Parses HTML content for framework indicators
- Checks robots.txt and sitemap.xml for technology hints
- Identifies CMS, web servers, databases, and JavaScript frameworks

### 2. JavaScript Endpoint Extraction (`javascript_endpoint_extraction`)
- Extracts JavaScript file references from HTML
- Analyzes JavaScript files for API endpoint calls
- Identifies endpoints used in fetch, XMLHttpRequest, jQuery AJAX, and Axios calls
- Detects URLs in string literals within JavaScript code
- Supports both relative and absolute URL patterns

### 3. Parameter Discovery (`parameter_discovery`)
- Discovers parameters from URLs and query strings
- Extracts form field parameters
- Identifies parameters from endpoints and JavaScript analysis
- Removes duplicate parameters
- Categorizes parameters by source (URL, form, endpoint)

### 4. API Discovery (`api_discovery`)
- Discovers common API endpoint patterns (/api/, /v1/, /graphql, etc.)
- Identifies API documentation files (swagger.json, openapi.yaml)
- Analyzes HTTP headers for API-related information
- Detects API endpoints from common file locations
- Removes duplicate API endpoints

### 5. Security Header Analysis (`security_header_analysis`)
- Analyzes HTTP security headers for vulnerabilities
- Checks Content-Security-Policy (CSP) configuration
- Validates X-Content-Type-Options header
- Reviews X-Frame-Options header settings
- Analyzes X-XSS-Protection header
- Checks Strict-Transport-Security (HSTS) configuration
- Evaluates Referrer-Policy, Permissions-Policy, and other security headers

## Integration with Core Engine

All Phase 2 modules integrate seamlessly with the core engine:
- They inherit from the BaseModule class
- They follow the same execution pattern
- They return structured ModuleResult objects
- They update the assessment context with discovered information
- They maintain proper error handling and logging

## Usage

To run all Phase 2 modules:
```bash
python run.py --target https://example.com --modules endpoint_discovery technology_detection javascript_endpoint_extraction parameter_discovery api_discovery security_header_analysis
```

## Extensibility

The framework is designed to be easily extensible:
- New reconnaissance modules can be added to the `modules/` directory
- Each module follows the same interface pattern
- Modules automatically load when the engine initializes
- The core engine handles module execution and context management