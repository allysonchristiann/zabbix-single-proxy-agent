# Troubleshooting

## Problem

Agents configured with multiple proxies can generate unnecessary traffic and connection attempts.

## Symptoms

- High proxy workload
- Agent logs showing repeated connection attempts
- Unbalanced proxy usage
- Difficult host distribution troubleshooting

## Validation

After deployment, validate the agent configuration:

```bash
grep -E "Server=|ServerActive=" /etc/zabbix/zabbix_agentd.conf
