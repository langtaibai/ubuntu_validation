# Ubuntu Validation Framework
A lightweight automated validation framework for ubuntu systems.

## features

- SSH remote execution
- System boot validation
- Service failure detection
- Log collection (journalctl / dmesg)

## Installation
git clone git@github.com:langtaibai/ubuntu_validation.git
pip install -r requirements.txt
python3 main.py

## Framework
Dev Machine -> SSH -> DUT (Ubuntu)
      |
Test Runner
      |
Boot / Service / Network Tests
      |
Logs & Reports
 
