tuples_port = (21, 22, 80, 443)

list_port = [21, 22, 80, 443]

dic_port = {"FTP": 21, "HTTP": 80}



change_list_port = list_port[1] = "FTP"
# change_tuple_port = tuples_port[1] = "FTP"

print(change_list_port)

print(dic_port["FTP"])

print(tuples_port)