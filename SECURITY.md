# Security & Redaction Policy

This is a public portfolio repository.

## Do not commit

- passwords or password hashes;
- cloud access keys/tokens;
- SSH private keys;
- TLS private keys;
- `.env` files with real secrets;
- private/internal IP inventories when unnecessary;
- student identification numbers;
- raw screenshots that expose credentials or personal data;
- the unredacted 181-page source report.

## Historical material

The original coursework includes educational/default credentials, local/cloud addresses, and screenshots of lab environments. Those values are deliberately not reproduced here.

Any credential that was ever exposed in a report, screenshot, chat, or repository should be considered compromised and rotated before reuse.

## Example configuration

Files in `examples/` use placeholders such as:

- `<SERVER_IP>`
- `<LDAP_BASE_DN>`
- `<REPLICA_USER>`
- `<CHANGE_ME>`

They are documentation aids, not production-ready secret-management patterns.