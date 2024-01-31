# CSGY9223 OSPSD

## Overview
This repository is a template for Python projects using Flask. It's designed to provide a strong foundation for building and developing Flask applications, complete with essential tools and practices for a robust development workflow.

## Features
- **Programming Language**: Python3.9
- **Code Formatting**: Black
- **Static Analysis**: Flake8
- **Continuous Integration**: CircleCI
- **Testing Framework**: Pytest
- **Package Management**: PDM (Python Dependency Management)
- **License**: MIT

## Getting Started
### Prerequisites
Ensure you have Python 3.9 and PDM installed on your machine. 

### Installation
* Clone the repository:
```shell
git clone https://github.com/Jas000n/CSGY9223_OSPSD
```
* Navigate to the cloned directory:
```shell
cd CSGY9223_OSPSD
```
* Install dependencies using PDM:
```shell
pdm install
```

### Running the Flask Application
Execute the following command to start the Flask server:
```shell
pdm run python src/opensource/app.py 
```
## Testing
Run tests using Pytest:
```shell
pdm run pytest
```
## Static Analysis
To perform static analysis using Flake8, run:
```shell
pdm run flake8 .
```
## Code Formatting
To format code using Black, execute:
```shell
pdm run black .
```

## Continuous Integration
This template is configured with CircleCI for continuous integration. The CI pipeline is defined in `.circleci/config.yml`.

## Contributing
Work in progress for template for issue and pull request. 
## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


