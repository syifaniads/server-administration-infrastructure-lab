# Nginx Virtual Hosts & TLS

## Verified lab outcomes
- Nginx service active on Ubuntu.
- Two sites hosted from separate document roots and `server` blocks.
- `nginx -t` used before reload/restart.
- Self-signed certificate generated with OpenSSL.
- HTTPS listener configured on 443.
- HTTP redirected to HTTPS.
- Static asset caching, gzip compression, and worker-connection tuning applied.

A sanitized representative config is available at [`examples/nginx/site.example.conf`](../examples/nginx/site.example.conf).

## Scope
Self-signed TLS is appropriate for a lab but not a substitute for a trusted production certificate and automated certificate renewal.