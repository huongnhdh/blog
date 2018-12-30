#!/usr/bin/env bash
TARGET_REPO=huongnhdh/wiki.git

echo -e "Deploy with travis"
echo -e "$VARNAME"

if [ "$TRAVIS_PULL_REQUEST" == "false" ]; then
    echo -e "Starting to deploy to Github Pages\n"
    if [ "$TRAVIS" == "true" ]; then
        rm -rf .git/
        git init
        git config user.name "huongnhdh"
        git config user.email "huong.nhdh@gmail.com"
        git config --global push.default simple
        git remote add origin https://${GH_TOKEN}@github.com/${TARGET_REPO}
        make github
    fi
fi