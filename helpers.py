import os
import shutil
from pathlib import Path
import constants as cst

def generate_compiled_proto(files):
    response = ""
    for file in files:
        filename = "protos/" + file + ".proto"
        file_content = Path(filename).read_text()
        for ignore in cst.IGNORE_LINES:
            file_content = file_content.replace(ignore, "")
        response += file_content
    return response

def build_models_package(channel, package_version, package_name=cst.PACKAGE, output_dir=cst.OUTPUT_FOLDER):
    # Initialise required file and folder names
    file_name = channel + ".proto"
    filename = file_name.split(os.path.sep)[-1]
    input_dir = cst.PACKAGE + "/"
    target_dir = os.path.join(output_dir, package_name)
    folder = file_name.replace(filename,"").replace(input_dir + os.path.sep, "")

    # Build proto files using GRPC library
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
    command = "python3 -m grpc_tools.protoc -I. \
                             --proto_path=" + input_dir + " \
                             --python_out=" + target_dir + " \
                             --grpc_python_out=" + target_dir + " \
                            " + package_name + "/" + file_name
    out = os.system(command)
    if out != 0:
        raise ValueError

    # Prepare package by adding init and setup files
    asd = os.path.join(output_dir, package_name, package_name, "__init__.py")
    os.system("touch " + asd)
    with open(os.path.join(output_dir, package_name, "setup.py"), "+w") as setup:
        setup_content = "from setuptools import setup \n" + cst.PACKAGE_META
        setup_content = setup_content.replace('{%BRANCH%}', os.getenv("BRANCH", default=cst.DEFAULT_BRANCH))
        setup_content = setup_content.replace('{%CHANNEL%}', channel)
        setup_content = setup_content.replace('{%VERSION%}', package_version.replace("\n", ""))
        setup.write(setup_content)
    command = "cd " + target_dir + " && python3 setup.py sdist"
    out = os.system(command)

    # Copy built package to dist folder
    if not os.path.exists(cst.DIST_FOLDER):
        os.makedirs(cst.DIST_FOLDER)
    
    complete_file_name = package_name + "-" + channel + "-" + os.getenv("BRANCH", default=cst.DEFAULT_BRANCH) + "-" + package_version + ".tar.gz"
    final_file = os.path.join(cst.DIST_FOLDER, complete_file_name)
    shutil.copyfile(
        os.path.join(output_dir, package_name, "dist", complete_file_name),
        final_file
    )

    # Delete output folder
    shutil.rmtree(os.path.join(output_dir))