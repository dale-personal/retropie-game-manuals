# Summary

API for displaying game manuals in response to emulation station events.
Game manuals are expected to be pdfs and match the name of the corresponding rom.
Game manual folders are expected to match the naming convention for
consoles in retropie.

## Hardware

- Dedicated Raspberry Pi 4b
- [10.1" touch screen](https://www.amazon.com/Raspberry-NORSMIC-Responsive-Capacitive-Compatible/dp/B0B71C9TTX/ref=sxin_15_pa_sp_search_thematic_sspa?content-id=amzn1.sym.6b029eb3-7d41-4744-b45d-69fe835e098d%3Aamzn1.sym.6b029eb3-7d41-4744-b45d-69fe835e098d&crid=IZNDTKO3DSNA&cv_ct_cx=raspberry%2Bpi%2Btouch%2Bscreen&keywords=raspberry%2Bpi%2Btouch%2Bscreen&pd_rd_i=B09KB7XKB2&pd_rd_r=0ba11825-5e8d-4a6e-b921-ec4480fc1396&pd_rd_w=6Cw42&pd_rd_wg=DhUSq&pf_rd_p=6b029eb3-7d41-4744-b45d-69fe835e098d&pf_rd_r=W1RMX5RM7SQZYC617250&qid=1665662735&qu=eyJxc2MiOiI1LjA5IiwicXNhIjoiNC43MyIsInFzcCI6IjQuMTkifQ%3D%3D&sprefix=raspberrypi%2Btouch%2Bscreen%2Caps%2C119&sr=1-2-a73d1c8c-2fd2-4f19-aa41-2df022bcb241-spons&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExWlI2Mlk0S0NYRUU0JmVuY3J5cHRlZElkPUEwMzMzNTcxMk1TNVY2SFQ5U1Y5RiZlbmNyeXB0ZWRBZElkPUEwNjE2NDA2MklUU0ZPUDBaSlZPRiZ3aWRnZXROYW1lPXNwX3NlYXJjaF90aGVtYXRpYyZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU&th=1)

## Pre-Requisites

```bash
sudo apt update
sudo apt install git
sudo apt install wmctrl
sudo apt install qpdfview
sudo apt install python3 idle3
python3 -m pip install Flask
```

## Setup

- Perform the following command line steps:

```bash
git clone https://github.com/dale-personal/retropie-game-manuals.git
cd retropie-game-manuals
sudo chmod +x launch.sh
```

- Note: launch.sh should be modified to pass in the game manual root folder you intend to use:

```bash
python3 <your-path-to-app.py>/app.py <your-path-to-game-manuals>
```

- Finally, schedule a cron job to run launch.sh:

```bash
crontab -e
```

Enter the following at the end of the file:

```bash
@reboot env DISPLAY=:0 <your-path-to-launch.sh>/launch.sh
```

Reboot, and you should be able to test:

```bin/bash
curl http://raspberrypi.local:8000/<console-name>/<rom-name>/manual
```

Example:

```bin/bash
curl http://raspberrypi.local:8000/console/new_game/manual

/media/pi/SANDISK250/manuals/console//new_game.pdf
```

## Troubleshooting

Verify your cron service is enabled

```bin/bash
sudo systemctl status cron.service
```
