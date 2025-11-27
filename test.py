from server import lookup_a_record, lookup_mx_record, lookup_txt_record, lookup_ns_record
import time

def test_dns_tools():
    domain = "google.com"
    print(f"Testing A record lookup for {domain}...")
    a_records = lookup_a_record(domain)
    print(f"A Records: {a_records}")
    assert any("Error" not in r for r in a_records), "Failed to get A records"

    print(f"\nTesting MX record lookup for {domain}...")
    mx_records = lookup_mx_record(domain)
    print(f"MX Records: {mx_records}")
    assert any("Error" not in r for r in mx_records), "Failed to get MX records"

    # TXT records can be large or slow, try example.com if google fails or just retry
    print(f"\nTesting TXT record lookup for {domain}...")
    txt_records = lookup_txt_record(domain)
    if any("lifetime expired" in r for r in txt_records):
        print("Timeout, retrying with example.com...")
        txt_records = lookup_txt_record("example.com")
    
    print(f"TXT Records: {txt_records}")
    assert any("Error" not in r for r in txt_records), "Failed to get TXT records"
    
    print(f"\nTesting NS record lookup for {domain}...")
    ns_records = lookup_ns_record(domain)
    print(f"NS Records: {ns_records}")
    assert any("Error" not in r for r in ns_records), "Failed to get NS records"

    print("\nAll tests passed!")

if __name__ == "__main__":
    test_dns_tools()
