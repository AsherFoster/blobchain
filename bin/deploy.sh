# Carries the image back to the image branch, and commits

# We don't want to deploy anything if this isn't master
# Normally this would be configured by .travis.yml, but idk how
if [[ $TRAVIS_BRANCH != "master" ]]; then
  exit 0
fi

# Grab the commit id, so we know what to save the new image as
COMMIT=$(git rev-parse --short HEAD)

echo Saving new image as $COMMIT.png

# Get rid of the old image
rm previous.png
mv output.png $COMMIT.png

# Shift the output image over to the images branch
git add $COMMIT.png
git stash
git checkout images
git stash pop

# Overwrite the latest image with the new one
rm latest.png
cp $COMMIT.png latest.png
git add latest.png

# Commit and push back to github
git commit -m "Travis deploy: ${TRAVIS_COMMIT} ${TRAVIS_COMMIT_MESSAGE}"
git remote set-url origin https://${GH_TOKEN}@github.com/asherfoster/blobchain.git
git push origin images
