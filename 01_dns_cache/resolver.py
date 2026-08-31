from dns_data import MASTER_DNS_RECORDS

DNS_CACHE = {}

def resolve_domain(domain_name):

    clean_domain = domain_name.strip().lower()

    if clean_domain in DNS_CACHE:
        return DNS_CACHE[clean_domain], "CACHE"

    if clean_domain in MASTER_DNS_RECORDS:
        ip_address = MASTER_DNS_RECORDS[clean_domain]
        DNS_CACHE[clean_domain] = ip_address
        return ip_address, "MASTER"

    return None, None