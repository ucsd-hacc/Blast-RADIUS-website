# Local Development

## Installation

To compile this website locally, install [Jekyll](https://jekyllrb.com/docs/installation/) (which requires you to have [Ruby](https://www.ruby-lang.org/en/downloads/)).

### Install ruby
Start by [installing ruby](https://www.ruby-lang.org/en/documentation/installation/).

On MacOS consider doing the following to be able to change ruby installations:
```bash
brew install chruby ruby-install
ruby-install ruby
# restart terminal
chruby 3.2.2
```

### Install bundler

```bash
gem install bundler
bundler install
```
## Run locally

Use the `--watch` to enable automatic rebuilds as well as updating of the local web server.

For building, run:
```bash
bundle exec jekyll build --watch
```

```bash
bundle exec jekyll serve --watch --port 8000
```

The website should now be accessible under [http://127.0.0.1:8000](http://127.0.0.1:8000).

# Access Dev Website

To access the developer website, connect to the VPN:
```
sudo openvpn --config webb-vpn-radius.ovpn
```

The website is accessible under [http://10.10.11.6:4242/](http://10.10.11.6:4242/).

Accessing it requires the following user and password:
```
user: eve
password: blast-radius
```
