## Tools

### wpcli-updates-checker

[wpcli-updates-checker](https://github.com/mwmdev/tools/blob/main/wpcli-updates-checker.py) is a script that uses `wp-cli` to list the number Wordpress updates (core, plugins, theme, translations) for any Wordpress install it finds in a specific folder and it's subfolders.

It is intended to work with [Local](https://localwp.com/) using a global install of [wp-cli](https://wp-cli.org/), using [this configuration](https://salferrarello.com/wp-cli-local-by-flywheel-without-ssh/).

Example output :

```
Site name: TestProject

Plugin updates: 17
Wordpress updates: 2
Theme updates: 1
Language updates: 1


Site name: AnotherProject

Plugin updates: 5 
Wordpress updates: 1
Theme updates: 2
Language updates: 1
```
