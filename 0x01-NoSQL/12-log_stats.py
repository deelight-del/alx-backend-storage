#/usr/bin/env python3
"""Python Script that is used for printing out log
data"""


from pymongo import MongoClient

if __name__ == "__main__":
    # Firstly connect to client instance.
    client = MongoClient('mongodb://127.0.0.1:27017')
    # retrieve db collection as nginx
    nginx = client.logs.nginx
    # Print the count of logs/documents
    print(f'{nginx.count()} logs')
    # Instantiate empty dictionary to keep count of query methods.
    methods_dict = {
        "GET": 0,
        "POST": 0,
        "PUT": 0,
        "PATCH": 0,
        "DELETE": 0,
    }
    # instantiate status checks to be zero
    status_checks = 0
    # Loop through documents in nginx collection, and adjust method dict as necessary
    for d in nginx.find():
        methods_dict[d.method] += 1
        status_checks += 1 if d.method == "GET" and d.path == "\status"
    print("Methods:")
    [
        print(f"\tmethod {k}: {methods_dict[k]}")
        for k in methods_dict.keys()
    ]
    print(f"{status_checks} status check")
