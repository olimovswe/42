import time
from servers_data import SERVERS
from balancer import get_next_server, toggle_server_status


def print_servers():
    print("\n--- Serverlar Holati ---")
    for idx, server in enumerate(SERVERS):
        status = "ONLINE 🟢" if server["is_healthy"] else "OFFLINE 🔴"
        print(f"[{idx}] {server['ip']}:{server['port']} -> {status}")


def main():
    while True:
        print_servers()
        print("1 - HTTP So'rov yuborish")
        print("2 - Serverni o'chirish/yoqish (Crash simulation)")
        print("3 - Chiqish")

        choice = input("\nBuyruq raqamini kiriting (1-3): ").strip()

        if choice == "1":
            server = get_next_server()
            if server:
                print(f"\n[HTTP 200 OK] So'rov yo'naltirildi -> {server['ip']}:{server['port']}")
            else:
                print("\n[HTTP 503 Bad Gateway] Barcha serverlar o'chirilgan!")
            time.sleep(1)

        elif choice == "2":
            try:
                idx = int(input("Server indeksini kiriting (0, 1, 2): "))
                updated = toggle_server_status(idx)
                if updated:
                    state = "ONLINE 🟢" if updated["is_healthy"] else "OFFLINE 🔴"
                    print(f"\n[INFO] {updated['ip']}:{updated['port']} holati {state} ga o'zgardi!")
                else:
                    print("\n[XATO] Noto'g'ri indeks kiritildi!")
            except ValueError:
                print("\n[XATO] Faqat raqam kiriting!")

        elif choice == "3":
            print("\nDastur to'xtatildi.")
            break

        else:
            print("\nNoto'g'ri buyruq!")


if __name__ == "__main__":
    main()