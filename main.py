import os
import shutil
from pathlib import Path
import constants as cst, helpers as hp

# Dictionary of packages to create with different set of protos
protos = {
    "mobile" : ["database"],
    "web" : ["database"],
    "bundle" : ["database"]
}

# Get current package version and increment file
package_version = Path(cst.VERSION_FILE).read_text()
next_version_number = int(package_version.replace(".", "")) + 1
with open(cst.VERSION_FILE, 'w') as version:
    next_version_str = "0.0." + str(next_version_number)
    version.write(next_version_str)

for channel, models in protos.items():
    # Create Package folder
    folder_name = cst.PACKAGE
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)
    
    #Write to filename
    filename = folder_name + "/" + channel + ".proto"
    with open(filename, 'w') as output:
        output.writelines(cst.IGNORE_LINES)
        text_to_write = hp.generate_compiled_proto(models)
        output.write(text_to_write)

    # Build Package
    hp.build_models_package(channel, package_version)

    # Remove package folder
    shutil.rmtree(folder_name)