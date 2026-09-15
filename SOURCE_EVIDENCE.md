# Source Evidence

Primary retained source: **Modul Akhir Administrasi Sistem Server Kelas A**, 181-page final course document, academic year 2025/2026.

The raw PDF is not committed publicly because it contains student identifiers, historical environment details, screenshots, and credentials/default passwords that are inappropriate for a public portfolio.

## Report mapping

| Report section | Approx. report pages | Portfolio area |
|---|---:|---|
| LK 1 — Tantangan Administrasi Sistem Server | 5–9 | conceptual systems operations context |
| LK 2 — Disk Management (LVM) | 10–27 | `docs/01-storage-lvm.md` |
| LK 3 — User Management | 28–36 | `docs/02-user-permissions.md` |
| LK 4 — User Management (LDAP) | 37–53 | `docs/03-openldap.md` |
| LK 5 — Web Server & Virtual Hosts | 54–79 | `docs/04-nginx-tls.md` |
| LK 6 — DNS | 80–92 | `docs/05-bind9-dns.md` |
| LK 7 — Database | 93–116 | `docs/06-mysql-replication.md` |
| LK 8 — Cache Server | 117–130 | `docs/07-redis-caching.md` |
| LK 9 — VM & Container | 132–149 | `docs/08-kubernetes-aws.md` |
| LK 10 — High Availability | 150–160 | `docs/09-haproxy-load-balancing.md` |
| LK 11 — Monitoring | 161–180 | `docs/10-prometheus-grafana.md` |

## Evidence examples retained in the report

- before/after LVM capacity screenshots;
- local user/group/sudo permission outputs;
- LDAP Account Manager tree and `ldapsearch` output;
- Nginx service, virtual-host, TLS, and client responses;
- BIND9 zone configuration and client `nslookup`;
- MySQL primary/replica status and replicated data;
- Redis vs direct database timing output;
- Kubernetes node status and AWS-oriented troubleshooting;
- HAProxy alternating backend responses;
- Prometheus target status and Grafana dashboards.

## Claim discipline

This repository distinguishes evidence from general knowledge. Production recommendations in docs are clearly framed as recommendations, not as historical implementation facts.