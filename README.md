## Tools

### mwmuc

[mwmuc](https://github.com/mwmdev/tools/blob/main/mwmuc/mwmuc.py) uses `wp-cli` to list the number of Wordpress updates (core, plugins, theme and translations) for any Wordpress install it finds in a specific folder and it's subfolders.

It is intended to work with [Local](https://localwp.com/) using a global install of [wp-cli](https://wp-cli.org/), following [this configuration](https://salferrarello.com/wp-cli-local-by-flywheel-without-ssh/). Also tested with [VVV](https://varyingvagrantvagrants.org/).

Example output :

```
Site name: TestProject

- Plugin updates: 17
- Wordpress updates: 2
- Theme updates: 1
- Language updates: 1


Site name: AnotherProject

- Plugin updates: 5 
- Wordpress updates: 1
- Theme updates: 2
- Language updates: 1
```
