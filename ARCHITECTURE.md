# Architecture & Scope

This repository represents a **series of labs**, not one monolithic application.

## Conceptual progression

```mermaid
flowchart TD
  F[Linux foundation] --> I[Identity & access]
  I --> S[Web / DNS services]
  S --> D[Database & cache]
  D --> C[Container orchestration]
  C --> A[Availability]
  A --> O[Observability]

  F --> F1[LVM]
  F --> F2[Users / groups / permissions]
  I --> I1[OpenLDAP]
  S --> S1[Nginx + TLS]
  S --> S2[BIND9]
  D --> D1[MySQL replication]
  D --> D2[Redis]
  C --> C1[Kubernetes + containerd + Calico on EC2]
  A --> A1[HAProxy + 2 Nginx backends]
  O --> O1[Node Exporter + Prometheus + Grafana]
```

## Trust boundaries encountered

1. **Local OS boundary** — Unix users, groups, sudo, file permissions.
2. **Directory-service boundary** — LDAP server vs LDAP clients.
3. **Network-service boundary** — Nginx, BIND9, MySQL and Redis listening interfaces/firewall rules.
4. **Cloud network boundary** — EC2 security groups separating Kubernetes roles and ports.
5. **Observability boundary** — exporters expose telemetry endpoints that should be restricted in production.

## Production-readiness perspective

The labs intentionally use educational shortcuts such as self-signed certificates, simple local domains, direct service installation, and small node counts. Production systems should additionally consider secret management, automated configuration/IaC, backup/restore testing, TLS from trusted PKI, restrictive firewall policy, service hardening, alerting, redundancy, upgrades, and disaster recovery.