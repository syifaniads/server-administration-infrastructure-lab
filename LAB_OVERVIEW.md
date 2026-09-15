# Lab Overview

The final coursework documented 11 worksheets. The first was a systems-administration discussion exercise; the remaining modules were hands-on labs.

| Worksheet | Topic | Main engineering outcome |
|---:|---|---|
| 1 | Challenges in server administration | AIOps, human accountability, AI/quantum-era risks |
| 2 | Disk management | Ubuntu VM + LVM expansion workflow |
| 3 | User management | Local users, groups, sudo, ownership and permissions |
| 4 | LDAP | Centralized identities with OpenLDAP/LAM + client integration |
| 5 | Web server & virtual hosts | Nginx multi-site hosting, TLS, redirect and tuning |
| 6 | DNS | BIND9 forward/reverse zones and client validation |
| 7 | Database | MySQL, PHP-FPM/phpMyAdmin, asynchronous replication |
| 8 | Cache server | Redis cache layer in front of MySQL with timing comparison |
| 9 | VM & container | Two-node Kubernetes cluster on AWS EC2 |
| 10 | High availability | HAProxy distributing traffic to two Nginx backends |
| 11 | Monitoring | Node Exporter, Prometheus, Grafana and monitoring APIs |

## Why this is one portfolio repository

The coursework was designed as a progression in operating server infrastructure, so this portfolio keeps the modules together while explicitly avoiding the false impression that all components belonged to one production topology.

## Evidence philosophy

- **Verified**: configuration plus retained runtime/test result.
- **Configured**: configuration is shown, but final behavioral proof is limited.
- **Discussed**: conceptual material or production recommendation, not an implementation claim.

See [docs/EVIDENCE_MAP.md](docs/EVIDENCE_MAP.md).