# Copies the latest image from images branch to master

# Travis does a single branch pull, which messes with the refs. This resets it back to normal
git config remote.origin.fetch +refs/heads/*:refs/remotes/origin/*
# Fetch the new refs, and switch to the images branch
git fetch
git checkout origin/images

# Grab the last image, and stage it
cp latest.png previous.png
git add previous.png

# Stash the last image, switch back to master, and get the image back
git stash
git checkout master
git stash pop

# We don't want to track it
git rm --cache previous.png
