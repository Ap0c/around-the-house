# Around the House

A simple database-backed, web UI for keeping track of media in a household, i.e. books, DVDs, music and so on. It's built against Python 3.5 and based on the Flask web framework. Testing is managed with Nose.

## Install

```
pip install -r requirements.txt
```

## Run

Run:

```
python run.py
```

and then navigate to `<localhost>:3000` (or `<server_ip_address>:3000` if accessing from a different computer on the network) in a browser.

## Test

Testing is handled by the Nose test framework. To run the tests:

```
nosetests
```

This will provide a printout in the shell and also produce a coverage report, accessible at `cover/index.html`.
