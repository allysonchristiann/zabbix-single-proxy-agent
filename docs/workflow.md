# Workflow

1. Jenkins starts the deployment pipeline.
2. Python retrieves proxy information from Zabbix API.
3. The proxy with the lowest number of assigned hosts is selected.
4. Ansible receives the selected proxy IP.
5. The Zabbix Agent configuration is rendered using Jinja2.
6. The host is created in Zabbix already assigned to the selected proxy.

## Final agent configuration

```ini
Server={{ proxy_ip }}
ServerActive={{ proxy_ip }}
