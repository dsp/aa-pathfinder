# Alliance Auth Pathfinder Sync

This is a plugin for [Alliance Auth](https://gitlab.com/allianceauth/allianceauth) (AA). It synchronizes users to a whitelist in [Pathfinder](https://github.com/exodus4d/pathfinder).

![License](https://img.shields.io/badge/license-MIT-green) ![python](https://img.shields.io/badge/python-3.6-informational) ![django](https://img.shields.io/badge/django-3.1-informational) ![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)

## Features

- Once installed, groups provided in the PATHFINDER_GROUPS setting will be
  synchronized to a whitelist of allowed characters in Pathfinder.

## How to use it

Install the plugin
```
$ pip install aa-pathfinder
```

Add the groups you want to `settings/local.py` and set your whitelist file
location:
```
PATHFINDER_GROUPS = [
    "Wormhole",
    "Supers",
]

PATHFINDER_WHITELIST = "/srv/pathfinder/aa-whitelist"
```

Update your Pathfinder `apps/pathfinder.ini` and include
```
PATHFINDER_WHITELIST = /srv/pathfinder/aa-whitelist
```

## Contribute

If you made a new app for AA please consider sharing it with the rest of the community. For any questions on how to share your app please contact the AA devs on their Discord. You find the current community creations [here](https://gitlab.com/allianceauth/community-creations).
