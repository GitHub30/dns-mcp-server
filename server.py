from fastmcp import FastMCP
import dns_utils

# Initialize FastMCP server
mcp = FastMCP("dns-server")

# Register tools
mcp.add_tool(dns_utils.lookup_a_record)
mcp.add_tool(dns_utils.lookup_aaaa_record)
mcp.add_tool(dns_utils.lookup_mx_record)
mcp.add_tool(dns_utils.lookup_txt_record)
mcp.add_tool(dns_utils.lookup_ns_record)
mcp.add_tool(dns_utils.lookup_cname_record)
mcp.add_tool(dns_utils.lookup_ptr_record)
mcp.add_tool(dns_utils.lookup_any_record)

if __name__ == "__main__":
    mcp.run()
