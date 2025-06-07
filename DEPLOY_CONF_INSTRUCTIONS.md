# Configuring Deployment

sudo mkdir -p /home/github_bot/.ssh
sudo vim /home/github_bot/.ssh/authorized_keys

sudo chown -R github_bot:github_bot /home/github_bot/.ssh
sudo chmod 700 /home/github_bot/.ssh
sudo chmod 600 /home/github_bot/.ssh/authorized_keys

sudo usermod -aG docker github_bot

ssh -i ~/.ssh/gh_vps github_bot@89.58.48.214

## Configuring VPS access

This steps will help you fill the secrets:

- VPS_HOST
- VPS_USER
- VPS_SSH_KEY

1. Create a service account on the VPS with scaled down privileges

    ```sh
    sudo adduser --disabled-password --gecos "" github_bot
    sudo mkdir -p /home/github_bot/.ssh
    sudo usermod -aG docker github_bot # user will have to run docker
    ```

2. Generate a new key on the local machine

    ```sh
    ssh-keygen -t ed25519 -C "deploy@domain.tld" -f /c/Users/<user>/.ssh/gh_vps
    cat ~/.ssh/gh_vps.pub
    ```

3. Copy the key to the VPS and give permissions

    ```sh
    sudo mkdir -p /home/github_bot/.ssh
    sudo vim /home/github_bot/.ssh/authorized_keys # Paste the key from step 2

    sudo chown -R github_bot:github_bot /home/github_bot/.ssh
    sudo chmod 700 /home/github_bot/.ssh
    sudo chmod 600 /home/github_bot/.ssh/authorized_keys
    ```

4. Test SSH Access

    ```sh
    ssh -i ~/.ssh/gh_vps github_bot@machine.ip
    ```

5. Add variables into the Github pipelines

## Configuring Cloudflare Cache Token

This steps will help you fill the secrets:

- CLOUDFLARE_API_TOKEN

1. Go to [Cloudflare → My Profile → API Tokens → Create Token](https://dash.cloudflare.com/profile/api-tokens)

2. Choose "Custom Token" with:

    Permissions: Zone → Cache Purge → Purge

    Zone Resources: Include → Specific Zone → select your specific site

3. Click Create Token and copy it.
4. Add it as a GitHub Secret:
    Name: CLOUDFLARE_API_TOKEN
    Value: (paste the token)
