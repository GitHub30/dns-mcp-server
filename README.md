# dns-mcp-server

![Run Tests](https://github.com/GitHub30/dns-mcp-server/actions/workflows/test.yml/badge.svg)

A Model Context Protocol (MCP) server that provides DNS lookup capabilities using `dnspython`.

## Features

- **A Records**: Look up IPv4 addresses.
- **AAAA Records**: Look up IPv6 addresses.
- **MX Records**: Look up Mail Exchange records.
- **TXT Records**: Look up Text records.
- **NS Records**: Look up Name Server records.
- **CNAME Records**: Look up Canonical Name records.
- **PTR Records**: Perform reverse DNS lookups.
- **Any Record**: Generic lookup for any record type.

## Installation

1. Clone the repository.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the server:
```bash
python server.py
```

## Available Tools

- `lookup_a_record(domain: str)`: Get A records.
- `lookup_aaaa_record(domain: str)`: Get AAAA records.
- `lookup_mx_record(domain: str)`: Get MX records.
- `lookup_txt_record(domain: str)`: Get TXT records.
- `lookup_ns_record(domain: str)`: Get NS records.
- `lookup_cname_record(domain: str)`: Get CNAME records.
- `lookup_ptr_record(ip_address: str)`: Get PTR records for an IP.
- `lookup_any_record(domain: str, record_type: str)`: Get any DNS record.

## Testing

Run the test script:
```bash
python test.py
```