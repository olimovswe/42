from  servers_data import SERVERS

current_index = 0

def get_next_server():
    global current_index
    healthy_server = []
    for server in SERVERS:
        if server["is_healthy"] == True:
            healthy_server.append(server)

    if len(healthy_server) == 0:
        return None

    selected_index = current_index % len(healthy_server)
    selected_server = healthy_server[selected_index]

    current_index += 1

    return selected_server



def toggle_server_status(index):
    if 0 <= index < len(SERVERS):
        SERVERS[index]["is_healthy"] = not SERVERS[index]["is_healthy"]
        return SERVERS[index]

    return None



