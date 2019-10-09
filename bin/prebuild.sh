# Copies the latest image from images branch to master
# Travis does a single branch pull. This undoes that
git config remote.origin.fetch +refs/heads/*:refs/remotes/origin/*
git fetch
git checkout origin/images

cp latest.png previous.png
git add previous.png

git stash
git checkout master
git stash pop
