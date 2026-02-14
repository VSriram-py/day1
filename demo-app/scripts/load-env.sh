#!/bin/bash

if [[ "$GITHUB_REF" == "refs/heads/main" ]]; then
    cp config/stage.env .env
elif [[ "$GITHUB_REF" == "refs/heads/release" ]]; then
    cp config/beta.env .env
elif [[ "$GITHUB_REF" == "refs/heads/prod" ]]; then
    cp config/production.env .env
fi

echo "Environment loaded:"
cat .env