# BIND9 DNS

## Verified lab outcomes
- Installed BIND9 on Ubuntu.
- Defined separate forward zones for two lab domains.
- Added a reverse zone with PTR mapping.
- Allowed DNS traffic through UFW.
- Pointed a client to the DNS server.
- Verified forward resolution using `nslookup`.

## Request path

```mermaid
sequenceDiagram
  participant C as Client
  participant D as BIND9
  participant Z as Zone data
  C->>D: Query site1.example
  D->>Z: Lookup A record
  Z-->>D: Address
  D-->>C: DNS answer
```

See [`examples/bind9/named.conf.local.example`](../examples/bind9/named.conf.local.example) for a sanitized example.