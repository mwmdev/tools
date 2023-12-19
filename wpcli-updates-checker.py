import os
import sys
import subprocess
import re

# set wp-cli path
wp_cli_path = "/../"

# Get the path from the command line argument
if len(sys.argv) > 1:
    path = sys.argv[1]
else:
    path = os.getcwd()

# Get the list of folders and subfolders
folders = []
for root, dirs, files in os.walk(path):
    for name in dirs:
        folders.append(os.path.join(root, name))

# Loop through the folders and subfolders
for folder in folders:
    # Check if the file wp-load.php exists
    if os.path.isfile(folder + "/wp-load.php") and os.path.isdir(folder + "/wp-admin"):
        print()

        # Get Local DB host
        db_host = ""
        try:
            with open(folder + wp_cli_path + "wp-cli.php", "r") as f:
                if f.mode == "r":
                    for line in f:
                        if "DB_HOST" in line:
                            db_host = re.findall(r"'(.*?)'", line)[1]
                else:
                    print("Error: wp-cli.local.php not readable")

            try:
                # Change DB host
                cmd = ["wp", "config", "set", "DB_HOST", db_host, "--path=" + folder]
                result = subprocess.run(cmd, capture_output=True, text=True)

                # Get the site name
                cmd = ["wp", "option", "get", "blogname", "--path=" + folder]
                site_name = subprocess.run(cmd, capture_output=True, text=True)

                if site_name.stdout != "":
                    print("")
                    print("Site : {}".format(site_name.stdout))

                    # Get the number of plugin updates
                    cmd = [
                        "wp",
                        "plugin",
                        "list",
                        "--update=available",
                        "--format=count",
                        "--path=" + folder,
                    ]
                    plugin_updates = subprocess.run(cmd, capture_output=True, text=True)
                    print("- Plugin updates: {}".format(plugin_updates.stdout))

                    # Get the number of core updates
                    cmd = [
                        "wp",
                        "core",
                        "check-update",
                        "--format=count",
                        "--path=" + folder,
                    ]
                    core_updates = subprocess.run(cmd, capture_output=True, text=True)
                    print("- Wordpress updates: {}".format(core_updates.stdout))

                    # Get the number of theme updates
                    cmd = [
                        "wp",
                        "theme",
                        "list",
                        "--update-available",
                        "--format=count",
                        "--path=" + folder,
                    ]
                    theme_updates = subprocess.run(cmd, capture_output=True, text=True)
                    print("- Theme updates: {}".format(theme_updates.stdout))

                    # Get the number of translation updates
                    cmd = [
                        "wp",
                        "language",
                        "core",
                        "list",
                        "--update-available",
                        "--format=count",
                        "--path=" + folder,
                    ]
                    language_updates = subprocess.run(
                        cmd, capture_output=True, text=True
                    )
                    print("- Language updates: {}".format(theme_updates.stdout))

                # Change DB host back to localhost
                cmd = [
                    "wp",
                    "config",
                    "set",
                    "DB_HOST",
                    "localhost",
                    "--path=" + folder,
                ]
                result = subprocess.run(cmd, capture_output=True, text=True)

            except subprocess.CalledProcessError as e:
                print("Error: {}".format(e))

        except FileNotFoundError:
            pass
            print("Error: wp-cli.php not found for {}".format(folder))
