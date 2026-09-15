# Evidence Map

| Claim | Evidence | Classification |
|---|---|---|
| `/home` storage was expanded with LVM | PV/VG/LV commands + before/after capacity output | VERIFIED |
| Unix permission model was exercised | user/group/sudo/chown/chmod outputs | VERIFIED |
| LDAP centralized identities worked | LAM hierarchy + `ldapsearch` + client-login analysis | VERIFIED |
| Nginx hosted two sites | separate virtual-host config + separate client responses | VERIFIED |
| HTTPS was enabled | OpenSSL certificate creation + Nginx 443 config + browser access | VERIFIED |
| BIND9 resolved lab domains | forward/reverse zone config + `nslookup` | VERIFIED |
| MySQL replication worked | binary log/replica status + IO/SQL threads + replicated data | VERIFIED |
| Redis reduced latency in one run | 0.07 s vs 0.0037 s output | VERIFIED EXPERIMENT |
| Kubernetes cluster worked | control-plane/worker setup + both nodes `Ready` | VERIFIED |
| HAProxy round-robin worked | repeated `curl` alternating backend responses | VERIFIED |
| Monitoring stack worked | Node Exporter target `UP`, Grafana dashboard, API queries | VERIFIED |
| Production HA/SLO/security posture | not comprehensively tested in retained course evidence | RECOMMENDATION ONLY |

## Why classifications matter

A portfolio should make it possible for an interviewer to distinguish between “I configured it,” “I observed it working,” and “I know how I would harden it.” This repository keeps those categories separate.