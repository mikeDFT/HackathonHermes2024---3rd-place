import socket


DATA = {
    "SPEED_BUFF": "SABO:SPEED:10",
    "JUMP_BUFF": "SABO:JUMP:-20",
    "KNOCKBACK_BUFF": "SABO:KNOCK:0",
    
    "SPEED_NERF": "SABO:SPEED:3",
    "JUMP_NERF": "SABO:JUMP:-9",
    "KNOCKBACK_NERF": "SABO:KNOCK:120",
}

def send_to_player(target_ip, target_port, data):
    """
    Sends malicious UDP packets to nerf the other player's stats.
    
    Args:
        target_ip (str): IP address of the player to attack.
        target_port (int): Port number of the player to attack.
    """
    # Create a UDP socket
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # Send the packets
    s.sendto(data.encode(), (target_ip, target_port))
    



if __name__ == "__main__":
    # Replace these values with the target player's IP and port
    TARGET_IP = "192.168.35.249"  # Example IP
    TARGET_PORT = 1234  # Example Port
    
    send_to_player(TARGET_IP, TARGET_PORT, DATA["KNOCKBACK_NERF"])
