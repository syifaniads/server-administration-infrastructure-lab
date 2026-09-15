# Verified Results

This file records results that are explicitly supported by the retained final report.

## Storage
- New virtual disk detected by the Ubuntu VM.
- Physical Volume created and added to the existing Volume Group.
- Logical Volume for `/home` expanded and filesystem resized.
- Capacity increase verified with `df -h`.

## Local identity & permissions
- Local user and group operations were exercised.
- Sudo membership was verified with `sudo whoami` returning `root`.
- Ownership and permission scenarios were validated for separate developer/designer users.

## LDAP
- OpenLDAP + LDAP Account Manager configured with organizational units, groups, and Unix users.
- LDAP search output showed the directory hierarchy.
- A client-login problem was traced to the client identity lookup/authentication integration and fixed by adjusting the LDAP-backed name-service configuration and restarting the relevant service.

## Nginx & TLS
- Nginx ran successfully on Ubuntu.
- Two independent virtual hosts returned different content.
- Self-signed TLS was enabled and HTTP-to-HTTPS redirection configured.
- Static caching, gzip, and worker-connection tuning were applied.

## DNS
- BIND9 served two forward zones.
- A reverse zone/PTR record was configured.
- Client-side `nslookup` returned the expected address for both lab domains.

## MySQL replication
- Primary binary logging and replica connection parameters were configured.
- Replica status reported both IO and SQL threads running.
- A data change on the primary was observed on the replica.

## Redis experiment
- Direct database access: **~0.07 s (70 ms)**.
- Redis-backed access: **~0.0037 s (3.7 ms)**.
- Report interpretation: approximately **19× faster** in that specific lab run.

> This is a single educational experiment, not a controlled benchmark across hardware/workloads.

## Kubernetes on AWS
- One control-plane and one worker EC2 instance formed a cluster.
- containerd, kubeadm/kubelet/kubectl, and Calico were used.
- Both nodes reached **Ready**.
- Reported troubleshooting included EC2 IP detection, containerd extraction/pathing, Kubernetes repository/GPG setup, API-server security-group access, and swap disabling.

## HAProxy
- One HAProxy VM fronted two Nginx web-server VMs.
- `balance roundrobin` was configured.
- Repeated `curl` calls alternated between server 1 and server 2 responses.

## Monitoring
- Node Exporter exposed CPU, memory, disk, and network metrics.
- Prometheus scraped the target and showed Node Exporter as **UP**.
- Grafana used Prometheus as a data source and displayed the Node Exporter Full dashboard.
- Prometheus API queries were exercised through cURL and Python.