# Summary

API for displaying game manuals in response to emulation station events.
Game manuals are expected to be pdfs and match the name of the corresponding rom
game manual folders are expected to match the naming convention for
consoles in retropie.

## Hardware

- Raspberry Pi 4b
- 10.1" touch screen

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
curl http://raspberrypi:8000/<console-name>/<rom-name>/manual
```

Example:

```bin/bash
curl http://raspberrypi:8000/console/new_game/manual

/media/pi/SANDISK250/manuals/console//new_game.pdf
```

## Troubleshooting

Verify your cron service is enabled

```bin/bash
sudo systemctl status cron.service
```
