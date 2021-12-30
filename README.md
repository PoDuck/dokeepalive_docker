DO Keepalive keeps tabs on DigitalOcean servers that have a tendency to freeze up, or that require a high degree of
availability. It will check if a given port is open, and if it isn't, it will use the DO(Digitalocean) API to reboot the
server. This is much different
than [the method Digitalocean suggests](https://www.digitalocean.com/community/tutorials/how-to-set-up-highly-available-web-servers-with-keepalived-and-floating-ips-on-ubuntu-14-04)
, which fails over to a secondary server only, and makes no attempt to recover the original server if it becomes
unresponsive.

If you really need to ensure that you maintain high availability, you may decide to use dokeepalive in conjunction with
keepalived, just in case the backup server goes down before you notice the main server has failed. In fact, if you run
dokeepalive on both servers and keep tabs on the other, it will ensure that your failover server is available in case
your main server goes down.

### Simple Setup Instructions:

1. Clone this repository into a folder on your stable server.
2. [Setup Docker and docker-compose](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-compose-on-ubuntu-20-04)
3. Create a JSON configuration file with any name and place it in the `conf` directory. You can use multiple files, or
   you can place the entire configuration in a single file. The configuration should take the form:

```json
[
  {
    "token": "DIGITAL OCEAN API TOKEN",
    "sites": [
      {
        "droplet_id": "FIRST DROPLET ID",
        "host": "DOMAIN OF HOST TO CHECK",
        "port": "PORT TO TEST",
        "interval": "5m"
      },
      {
        "droplet_id": "SECOND DROPLET ID",
        "host": "DOMAIN OF HOST TO CHECK",
        "port": "PORT TO TEST",
        "interval": "5m"
      }
    ]
  }
]
```

Intervals take the form `Nu` where `N` is the number, and `u` is the units. Units can be `s` - seconds, `m` -
minutes, `h` - hours `d` - days. Multiple sets of units can be used, such as for 1 day 5 hours and 20 minutes `1d5h20m`

This file can be created on the host filesystem by running the `config_setup.py` file.

The setup file creates a configuration for dokeepalive. You can either run the file with no arguments, and answer the
questions, or you can pass arguments describing a single API instance with sites from the command line. If you require a
configuration for multiple API tokens (-t), you must run without arguments, but you can create multiple site (-s)
instances on the command line.

4. `docker-compose up -d`

The compose file has the app set to `restart: always`, so it should restart after a reboot of the server. Change or
remove that line if you do not want that behavior.