# Portfolio / CV Copy

## One-line summary

**Server Administration & Infrastructure Lab** — Led a three-person team through a semester-long Linux infrastructure lab spanning LVM, Linux IAM, OpenLDAP, Nginx/TLS, BIND9, MySQL replication, Redis caching, Kubernetes on AWS EC2, HAProxy, and Prometheus/Grafana.

## CV bullets

- **Led a three-person systems administration team** completing and documenting 10+ hands-on Linux infrastructure modules across storage, identity, networking, data services, container orchestration, high availability, and monitoring.
- Built a **two-node Kubernetes cluster on AWS EC2** with containerd, kubeadm, and Calico; troubleshot security-group reachability, runtime installation, repository/GPG issues, EC2 IP detection, and swap configuration until both nodes reached `Ready`.
- Configured **Nginx/TLS, BIND9, OpenLDAP, MySQL primary-replica replication, Redis caching, and HAProxy round-robin**, validating behavior through client requests, directory queries, replication status, timing measurements, and backend-response tests.
- Implemented **Prometheus + Node Exporter + Grafana** monitoring and queried metrics programmatically through Prometheus APIs; validated Node Exporter as an `UP` scrape target.

## Interview talking points

### “What was the hardest troubleshooting?”
Kubernetes produced the richest troubleshooting path: EC2 IP-detection assumptions, containerd extraction/location, changed Kubernetes repository/GPG setup, API-server network access, and persistent swap configuration.

### “What did you measure?”
The Redis lab recorded ~70 ms for direct database access and ~3.7 ms for the cached path in that run. HAProxy was validated through alternating responses, and Prometheus target health was verified as `UP`.

### “What would you change for production?”
Use configuration management/IaC, a secret manager, trusted PKI, restrictive network policy, automated backups and restore tests, multi-node HA control planes/data services, alerting/SLOs, upgrade plans, and reproducible CI-based configuration validation.

## Suggested tags

`Linux` · `Ubuntu` · `System Administration` · `LVM` · `OpenLDAP` · `Nginx` · `BIND9` · `MySQL` · `Redis` · `Kubernetes` · `AWS EC2` · `containerd` · `Calico` · `HAProxy` · `Prometheus` · `Grafana` · `Infrastructure` · `Observability`