# Anidata Twitter Data Project
[![Build Status](https://travis-ci.com/anidata/twitter-data.svg?branch=master)](https://travis-ci.com/anidata/twitter-data)

This project is for collecting and analyzing Twitter data sets to identify
potential social good projects.

## Usage
Place your four twitter api keys in config.py

Run:
```
docker build -t <container-name> .
docker run -v <host-path>:/app
```

## How it works
app.py will continuously store tweets relating to the query variable in the script. Tweets go back as far as Twitter is currently allowing, up to current time. Once all tweets have been exhausted, or Twitter API rate-limit has been reached, app will wait until more are available or we are allowed to continue downloading.


## Bugs or see a feature that missing?
Please file a bug report or a feature request ([link](https://github.com/anidata/twitter-data/issues/new/choose)).

## Contributing
Please see [CONTRIBUTING.md](CONTRIBUTING.md) for details.
