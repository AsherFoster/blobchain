# Blobchain
[![Build Status](https://travis-ci.com/AsherFoster/blobchain.svg?branch=images)](https://travis-ci.com/AsherFoster/blobchain)

Blobchain is a random community driven experiment. Ever commit added to the repository modifies
the image created by the last. These changes chain over time, creating a recursive image defined
by the process each commit applies

[![Latest Image](https://raw.githubusercontent.com/AsherFoster/blobchain/images/latest.png)](https://github.com/AsherFoster/blobchain/blob/images/latest.png)

## Contributing
Go ahead and submit a PR!

I'd suggest editing `blobchain/process.py` to add your own transformation to the image, but I'll be
accepting as many PRs as possible.

## How it works
Blobchain is powered by TravisCI. Every commit to master gets run through a CD pipeline that:
- Grabs the last image generated (see bin/prebuild.sh)
- Processes that image (Currently, using Python + Pillow)
- Saves that image back to the image branch (see deploy.sh)

## Future features
- Testing
- Automatic PRs
- Sentience
