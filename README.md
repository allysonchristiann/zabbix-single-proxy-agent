# Zabbix Single Proxy Agent

Automated Zabbix Agent deployment with dynamic proxy assignment using Ansible, Python and Zabbix API.

## Overview

This project was created to solve a common monitoring challenge in large Zabbix environments:

- Automatic host registration
- Dynamic proxy assignment
- Agent deployment automation
- Reduction of manual operational tasks
- Better proxy workload distribution

## Technologies

- Ansible
- Python
- Zabbix API
- Jenkins
- Linux
- Jinja2 Templates

## Features

- Automated Zabbix Agent installation
- Dynamic proxy selection
- Automatic host creation through Zabbix API
- Agent configuration templating
- Single proxy assignment per host

## Repository Structure

```text
zabbix-single-proxy-agent/
├── ansible/
│   ├── install-agent.yml
│   └── templates/
│       └── zabbix_agentd.conf.j2
├── python/
│   └── proxy_selector.py
├── examples/
│   └── inventory_example.ini
└── docs/
    └── architecture.md
```

## Architecture

Host
↓
Ansible Playbook
↓
Python Proxy Selection Logic
↓
Zabbix API
↓
Host Creation + Proxy Assignment

## Results

- Eliminated manual proxy assignment
- Standardized agent deployment
- Reduced operational effort
- Improved monitoring scalability

## Disclaimer

This repository contains a simplified and sanitized version of the implementation.
No customer, company, infrastructure or confidential information is included.

## Architecture

For more details about the workflow and components:

👉 [View Architecture Documentation](docs/architecture.md)
