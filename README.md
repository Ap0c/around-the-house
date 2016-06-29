# Around the House

A simple database-backed, web UI for keeping track of media in a household, i.e. books, DVDs, music and so on. It's built against Python 3.5 and based on the Flask web framework. Testing is managed with Nose.

## Raspberry Pi

The project comes bundled with an installation script for the Raspberry Pi. This will install the necessary dependencies and create a systemd service that launches the app on boot. Simply download the repository, navigate to the directory, and run:

```
sudo ./setup.sh
```

The app should now be running at `<pi_ip_address>:3000`.

## Install

Alternatively, to install the dependencies manually:

```
pip install -r requirements.txt
```

## Run

To run the app manually:

```
python run.py
```

and then navigate to `localhost:3000` (or `<server_ip_address>:3000` if accessing from a different computer on the network) in a browser.

## Test

Testing is handled by the Nose test framework. To run the tests:

```
nosetests
```

This will provide a printout in the shell and also produce a coverage report, accessible at `cover/index.html`.
