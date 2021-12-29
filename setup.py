#!/usr/bin/env python3
import json
import os


def main():
    users = []
    print("This will help you create a configuration file for dokeepalive.  It will be stored in the ./conf/dokeepalive directory.")
    tokens_finished = False
    while not tokens_finished:
        token = input("Enter digital ocean API token for first user. (Blank line to quit): ")
        if token != '':
            sites_finished = False
            sites = []
            while not sites_finished:
                droplet_id = input("droplet ID (Blank line if no more sites): ")
                if droplet_id != '':
                    host = input("Host: ")
                    port = input("Port: ")
                    interval = input("Interval: ")
                    sites.append(
                        {
                            'droplet_id': droplet_id,
                            'host': host,
                            'port': port,
                            'interval': interval
                        }
                    )
                else:
                    sites_finished = True
            if sites:
                users.append(
                    {
                        'token': token,
                        'sites': sites
                    }
                )
        else:
            tokens_finished = True
    current_dir = os.getcwd()
    conf_dir = os.path.join(current_dir, 'conf')
    print(os.path.join(conf_dir, 'dokeepalive.conf'))
    if not os.path.isdir(conf_dir):
        os.mkdir(conf_dir, 0o775)
    with open(os.path.join(conf_dir, 'dokeepalive.conf'), 'w') as conf_file:
        json.dump(users, conf_file, indent=2)


if __name__=="__main__":
    main()
