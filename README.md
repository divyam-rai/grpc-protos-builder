## gRPC Protos Builder

This project helps create python packages from a set of proto files. The generated package could then simply be installed into any other project and used as normal. This allows distributed projects ensure they have the same centralised set of gRPC definitions, as long as they have installed the same version of the generated package.

Currently, it contains a proto file containing definitions for a mongo service.

There are 2 ways to run this project :

i) **Docker** : One could simply build a Docker image using the Docker file in the repository using `docker build -t name_of_image .` and then running it using `docker run --rm --env BRANCH=dev -v /path/to/version.txt:/usr/src/app/version.txt name_of_image`.

ii) **Manual** : To run this project out of Docker, we would need to do the following while in the project root:
- Create a virtualenv (`virtualenv -p python3 venv/`) and activate it (`source venv/bin/activate`)
- Install the requirements (`pip install -r requirements.txt`)
- Create the logs folder (`mkdir logs/`)
- Run the application (`python main.py`)

In order to add protos, you can create the proto files in the protos folder. You would then need to go to main.py and modify the protos variables adding the different packages that need to be created with the proto files that each package must contain.

While creating your proto files, kindly exclude the import statements as the builder automatically combines all definitions into a single file before packaging.