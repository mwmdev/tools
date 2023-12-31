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

[mwmup](https://github.com/mwmdev/tools/blob/main/mwmup/mwmup) uses `wp-cli` and `git` to update Wordpress plugins, stage the new files, add commits and push to the repo.

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

### mwmdp

[mwmdp](https://github.com/mwmdev/tools/blob/main/mwmdp/mwmdp) uses `wp-cli` and `glab` to merge and deploy to a server. It uses the same `.env` file as `mwmup`.

Sample output :
```
On branch: « main »
Do you want to deploy? (Y/n):
We are on branch « main », no need to merge.
Testing connection to « ftp.myhost.net » on port « 22 » with user « johndoe » ...
Connecting to « ftp.myhost.net »
Entering path « /path/to/www »
Pulling changes ...
```
### mwmgs

[mwmgs](https://github.com/mwmdev/tools/blob/main/mwmgs/mwmgs) is a simple bash script that looks for folders named `public_html` in the current folder recursively and gathers the number of unstaged git changes in each folder, then displays the results in a table.


Example output :

```
Project         | Unstaged Changes
-------         | ----------------
myproject       | 0
anotherproject  | 3
testproject     | 1
```

### mwmpl

[mwmpl](https://github.com/mwmdev/tools/blob/main/mwmpl/mwmpl) is a simple bash script that uses `wp-cli` and `WP Migrate` to pull the DB from a remote Wordpress site.

Settings are defined in an `.env` file like so :

```
wpmdb_key=[WP Migrate site key]
live_url=[Live site URL]
```

Example output :

```
Are you sure you want to pull the database from https://mysite.com ? (Y/n):
Verifying connection...
Initiating migration...
Migrating tables      100% [==========================================================================================================] 0:37 / 0:36
Cleaning up...
Flushing caches and rewrite rules...
Success: Migration successful.
```
