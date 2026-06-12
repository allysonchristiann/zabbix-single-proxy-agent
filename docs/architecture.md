# Architecture

```text
+---------+
| Jenkins |
+---------+
     |
     v
+-----------+
| Ansible   |
+-----------+
     |
     v
+-------------------+
| Proxy Selection   |
| Python Logic      |
+-------------------+
     |
     v
+-------------+
| Zabbix API  |
+-------------+
     |
     v
+-------------+
| Host Create |
+-------------+
     |
     v
+-------------+
| Proxy Assign|
+-------------+
```
