from  resolver import resolve_domain

def main():
    print("=== Local DNS Resolver & Cache System ===")
    print("Type 'exit' to exit the program.\n")

    while True:
        domain_input = input("Enter domain name: ")

        if domain_input.strip().lower() == "exit":
            print("The program has ended. Bye!")
            break

        if not domain_input.strip():
            print("[WARNING] Please enter a valid domain name!\n")
            continue

        ip_address, source = resolve_domain(domain_input)

        if ip_address is None:
            print(f"[ERROR] {domain_input}, (404 Not Found)\n")
        elif source == "CACHE":
            print(f"[SUCCESSFUL] {domain_input} -> {ip_address} (Cached) \n")
        elif source == "MASTER":
            print(f"[SUCCESSFUL] {domain_input} -> {ip_address} (found and cached from Master DNS ) \n")


if __name__ == "__main__":
    main()