#!/usr/bin/env python3
"""Validate sanitized infrastructure examples against documented lab invariants.

This is a repository-integrity check, not a substitute for running Nginx,
BIND9, HAProxy, Kubernetes, Prometheus, MySQL, Redis, or LDAP.
"""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]


def read(path: str) -> str:
    p = ROOT / path
    if not p.exists():
        raise AssertionError(f"missing artifact: {path}")
    return p.read_text(encoding="utf-8")


def require(text: str, needle: str, label: str) -> None:
    if needle not in text:
        raise AssertionError(f"{label}: expected {needle!r}")


def main() -> int:
    nginx = read("examples/nginx/site.example.conf")
    bind = read("examples/bind9/named.conf.local.example")
    haproxy = read("examples/haproxy/haproxy.cfg.example")
    prometheus = read("examples/prometheus/prometheus.yml.example")
    k8s = read("examples/kubernetes/sample-app.yaml")

    require(nginx, "listen 80;", "Nginx HTTP listener")
    require(nginx, "return 301 https://$host$request_uri;", "HTTP to HTTPS redirect")
    require(nginx, "listen 443 ssl;", "Nginx TLS listener")
    require(nginx, "ssl_certificate_key", "TLS key reference")

    require(bind, 'zone "site1.example.test"', "BIND forward zone 1")
    require(bind, 'zone "site2.example.test"', "BIND forward zone 2")
    require(bind, "in-addr.arpa", "BIND reverse-zone intent")

    require(haproxy, "balance roundrobin", "HAProxy balancing mode")
    require(haproxy, "server web1", "HAProxy backend 1")
    require(haproxy, "server web2", "HAProxy backend 2")
    require(haproxy, "check", "HAProxy health checks")

    require(prometheus, "scrape_interval: 15s", "Prometheus scrape interval")
    require(prometheus, ":9100", "Node Exporter target")

    require(k8s, "apiVersion: apps/v1", "Kubernetes Deployment API")
    require(k8s, "kind: Deployment", "Kubernetes Deployment")
    require(k8s, "replicas: 2", "Kubernetes replica count")
    require(k8s, "kind: Service", "Kubernetes Service")
    require(k8s, "type: ClusterIP", "Kubernetes service exposure")

    # Keep common credential patterns out of the public examples.
    suspicious = re.compile(
        r"(?im)^\s*(?:password|secret|private[_-]?key|token|access[_-]?key)\s*(?:=|:)\s*(?!<REDACTED>|<CHANGE_ME>|<[^>]+>|\$\{).+"
    )
    for path in (ROOT / "examples").rglob("*"):
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        if suspicious.search(text):
            raise AssertionError(f"possible literal secret in {path.relative_to(ROOT)}")

    print("infrastructure portfolio validation passed")
    print("- Nginx HTTP→HTTPS and TLS references present")
    print("- BIND forward/reverse-zone intent present")
    print("- HAProxy round-robin + backend health checks present")
    print("- Prometheus Node Exporter target present")
    print("- Kubernetes Deployment + ClusterIP Service present")
    print("- no obvious literal secret assignments detected")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except AssertionError as exc:
        print(f"validation failed: {exc}", file=sys.stderr)
        raise SystemExit(1)
