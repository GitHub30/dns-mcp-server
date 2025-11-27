from fastmcp import FastMCP
import dns.resolver
import dns.reversename
from typing import List

# Initialize FastMCP server
mcp = FastMCP("dns-server")

def _format_answer(answer) -> List[str]:
    """Helper to format DNS answer to a list of strings."""
    return [str(rdata) for rdata in answer]

@mcp.tool()
def lookup_a_record(domain: str) -> List[str]:
    """
    Look up A records (IPv4 addresses) for a domain.
    """
    try:
        answer = dns.resolver.resolve(domain, 'A')
        return _format_answer(answer)
    except dns.exception.DNSException as e:
        return [f"Error: {str(e)}"]

@mcp.tool()
def lookup_aaaa_record(domain: str) -> List[str]:
    """
    Look up AAAA records (IPv6 addresses) for a domain.
    """
    try:
        answer = dns.resolver.resolve(domain, 'AAAA')
        return _format_answer(answer)
    except dns.exception.DNSException as e:
        return [f"Error: {str(e)}"]

@mcp.tool()
def lookup_mx_record(domain: str) -> List[str]:
    """
    Look up MX records (Mail Exchange) for a domain.
    """
    try:
        answer = dns.resolver.resolve(domain, 'MX')
        return _format_answer(answer)
    except dns.exception.DNSException as e:
        return [f"Error: {str(e)}"]

@mcp.tool()
def lookup_txt_record(domain: str) -> List[str]:
    """
    Look up TXT records for a domain.
    """
    try:
        answer = dns.resolver.resolve(domain, 'TXT')
        return _format_answer(answer)
    except dns.exception.DNSException as e:
        return [f"Error: {str(e)}"]

@mcp.tool()
def lookup_ns_record(domain: str) -> List[str]:
    """
    Look up NS records (Name Servers) for a domain.
    """
    try:
        answer = dns.resolver.resolve(domain, 'NS')
        return _format_answer(answer)
    except dns.exception.DNSException as e:
        return [f"Error: {str(e)}"]

@mcp.tool()
def lookup_cname_record(domain: str) -> List[str]:
    """
    Look up CNAME records for a domain.
    """
    try:
        answer = dns.resolver.resolve(domain, 'CNAME')
        return _format_answer(answer)
    except dns.exception.DNSException as e:
        return [f"Error: {str(e)}"]

@mcp.tool()
def lookup_ptr_record(ip_address: str) -> List[str]:
    """
    Look up PTR records (Reverse DNS) for an IP address.
    """
    try:
        addr = dns.reversename.from_address(ip_address)
        answer = dns.resolver.resolve(addr, 'PTR')
        return _format_answer(answer)
    except dns.exception.DNSException as e:
        return [f"Error: {str(e)}"]

@mcp.tool()
def lookup_any_record(domain: str, record_type: str) -> List[str]:
    """
    Look up any DNS record type for a domain.
    """
    try:
        answer = dns.resolver.resolve(domain, record_type)
        return _format_answer(answer)
    except dns.exception.DNSException as e:
        return [f"Error: {str(e)}"]

if __name__ == "__main__":
    mcp.run()
