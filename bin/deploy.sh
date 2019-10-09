# Carries the image back to the image branch, and commits
if [[ $TRAVIS_BRANCH != "master" ]]; then
  exit 0
fi

COMMIT=$(git rev-parse --short HEAD)

echo Saving new image as $COMMIT.png

rm previous.png
git add previous.png

git add $COMMIT.png
git stash
git checkout images
git stash pop

rm latest.png
cp $COMMIT.png latest.png

git add latest.png $COMMIT.png

git commit -m "Travis deploy: ${TRAVIS_COMMIT} ${TRAVIS_COMMIT_MESSAGE}"
git remote set-url origin https://${GH_TOKEN}@github.com/asherfoster/blobchain.git
git push origin images
