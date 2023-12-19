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

### mwmup

[mwmup](https://github.com/mwmdev/tools/blob/main/mwmup/mwmup.py) uses `wp-cli` and `git` to update Wordpress plugins, stage the new files, add commits and push to the repo.

Settings are defined in an `.env` file like so :

```
user=[USER]
server=[IP]
port=[PORT]
path=[PATH]
mergeinto=[BRANCH]
ignore=[PLUGIN1,PLUGIN2]
```

Sample output :

```
On branch « main », do you want to update plugins? (Y/n): Y
Setting « WP_DEBUG » to « false »
Checking for plugin updates...
Found 3 plugin(s) with updates : facetwp mailpoet google-site-kit
Also found 1 plugin(s) to ignore : user-role-editor 
Do you want to update 3 plugin(s)? (Y/n): Y
Updating « facetwp »
Update of « facetwp » successful.
Updating « mailpoet »
Update of « mailpoet » successful.
Updating « google-site-kit »
Update of « google-site-kit » successful.
Pushing changes to remote.
```