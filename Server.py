import socket
dns_table = {"www.google.com": "192.165.1.1", "www.youtube.com":"192.165.1.2",
"www.python.org":"192.165.1.3", "www.aurcc.ac.in":"192.165.1.4",
"www.amazon.in":"192.165.1.5", "www.gmail.com":"192.165.1.6"}
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print("Starting Server…")
s.bind(("127.0.0.1",1234))
while True:
    data, address = s.recvfrom(1024)
    print(f"{address} wants to fetch data!")
    data = data.decode()
    ip = dns_table.get(data, "Not found!").encode()
    send = s.sendto(ip, address)
    break
s.close()