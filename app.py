def get_serviceName(port_number):
    ports_services = {21: "ftp", 22: "ssh", 80: "http", 443: "https"}
    return ports_services[port_number]

print(get_serviceName(22))