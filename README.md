# IP Changer

Orospor Labs research utility for rotating a local Tor SOCKS egress identity on
a fixed interval.

This repository contains a small Python wrapper around the local Tor service. It
starts Tor, points traffic at `127.0.0.1:9050`, reloads the Tor circuit every few
seconds, and prints the current observed egress IP through the Tor proxy.

## Responsible use

Use this only for privacy testing, lab traffic routing, and defensive research
on systems you own or are authorized to assess. Do not use rotating egress to
bypass controls, evade abuse detection, scrape services without permission, or
send unwanted traffic.

## What it does

- Installs missing Python SOCKS support when needed.
- Installs Tor through `apt` when Tor is not present.
- Starts the local Tor service.
- Checks the current Tor egress IP through `http://checkip.amazonaws.com`.
- Reloads Tor every 5 seconds to request a new circuit.
- Exposes an optional `aut` launcher through `install.py`.

## Requirements

- Linux host with `apt`
- Python 3
- `sudo` privileges for Tor installation and service control
- Tor service listening on SOCKS `127.0.0.1:9050`

Manual dependency install:

```bash
sudo apt update
sudo apt install -y tor
python3 -m pip install "requests[socks]"
```

## Quick start

Clone and run directly:

```bash
git clone https://github.com/orospor/ipchanger.git
cd ipchanger
python3 autoTOR.py
```

Install the global `aut` command:

```bash
git clone https://github.com/orospor/ipchanger.git
cd ipchanger
sudo python3 install.py
aut
```

Set any test application that should use the rotated egress path to the local
SOCKS proxy:

```text
SOCKS host: 127.0.0.1
SOCKS port: 9050
```

## How it works

`autoTOR.py` uses the local Tor SOCKS proxy for outbound IP checks:

```python
proxies = {
    "http": "socks5://127.0.0.1:9050",
    "https": "socks5://127.0.0.1:9050",
}
```

Every interval, it reloads Tor:

```bash
service tor reload
```

Tor then selects a fresh circuit when available, and the script prints the
observed public IP.

## Uninstall

If you installed the global launcher, run:

```bash
sudo python3 install.py
```

Choose `N` when prompted to remove `/usr/bin/aut` and `/usr/share/aut`.

## Notes

- Tor circuit rotation is not guaranteed to provide a new exit IP every time.
- Some services block Tor exits by policy.
- This tool routes only applications configured to use the SOCKS proxy. It does
  not transparently route all system traffic.
- Keep test rates low and respect the terms and rules of every network you use.

## Orospor Labs

More projects and updates: [Orospor](https://orospor.com).

## License

Use and modify this project responsibly under the license terms published in
this repository.
