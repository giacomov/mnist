rm -rf ~/.gitconfig
cat << EOF > ~/.gitconfig
[user]
    email = ${CNVRG_EMAIL}
[url "https://${GITHUB_TOKEN}:@github.com/"]
    insteadOf = https://github.com/
EOF
