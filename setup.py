#!/usr/bin/env python3
import json
import os
import argparse


class Config(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string):
        droplet_id = values[0]
        host = values[1]
        port = values[2]
        interval = values[3]
        d = {"droplet_id": droplet_id, "host": host, "port": port, "interval": interval}
        return super().__call__(parser, namespace, d, option_string)


def main():
    parser = argparse.ArgumentParser(
        description="This setup file creates a configuration for dokeepalive.  You can either run the file with no arguments, or you can pass arguments describing a single API instance with sites from the command line.  If you require a configuration for multiple API tokens (-t), you must run without arguments, but you can create multiple site (-s) instances on the command line.")
    parser.add_argument("-t", "--token", metavar="API_TOKEN", help="Digitalocean API token")
    parser.add_argument("-s", "--site", metavar=("DROPLET_ID", "HOST", "PORT", "INTERVAL"), nargs=4,
                        help="enter droplet_id host port interval", action=Config)
    args = parser.parse_args()
    if args:
        conf = [
            {
                "token": args.token,
                "sites": args.site
            }
        ]
    else:
        conf = []
        print(
            "This will help you create a configuration file for dokeepalive.  It will be stored in the ./conf/dokeepalive directory.")
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
                    conf.append(
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
        json.dump(conf, conf_file, indent=2)


if __name__ == "__main__":
    main()
