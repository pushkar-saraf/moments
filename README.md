# Moments

A photo sharing social networking app built with Python and Flask. The example application for the
book
*[Python Web Development with Flask (2nd edition)](https://helloflask.com/en/book/4)* (《[Flask Web 开发实战（第 2 版）](https://helloflask.com/book/4)》).

Demo: http://moments.helloflask.com

![Screenshot](demo.png)

## Installation

Clone the repo:

```
$ git clone https://github.com/greyli/moments
$ cd moments
```
Install dependencies with [PDM](https://pdm.fming.dev):

## Setup Azure Vision API

Azure Computer Vision API Setup (Optional but Recommended)
To enable automatic generation of image alt text and tags, configure Azure Cognitive Services.

a. Install Azure SDK Packages
```bash
pdm add azure-cognitiveservices-vision-computervision python-dotenv msrest
(or pip install them manually if not using PDM.)
```

b. Create a .env file
Create a .env file at the project root with the following content:
```
ENDPOINT=your_azure_endpoint_here
KEY=your_azure_key_here
```
You can obtain these credentials by creating an Azure Computer Vision resource in your Azure portal.

## Installation
```
$ pdm install
```

Create a .env file in the root folder and add asure vision credentials
> ENDPOINT=YOUR ENDPOINT
> KEY=YOUR KEY

> [!TIP]
> If you don't have PDM installed, you can create a virtual environment with `venv` and install
> dependencies with `pip install -r requirements.txt`.

To initialize the app, run the `flask init-app` command:

```
$ pdm run flask init-app
```

If you just want to try it out, generate fake data with `flask lorem` command then run the app:

```
$ pdm run flask lorem
```

It will create a test account:

* email: `admin@helloflask.com`
* password: `moments`

Now you can run the app:

```
$ pdm run flask run
* Running on http://127.0.0.1:5000/
```

## License

This project is licensed under the MIT License (see the
[LICENSE](LICENSE) file for details).
