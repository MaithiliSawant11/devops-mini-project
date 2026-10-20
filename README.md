# DevOps Mini Project

A small Flask web app used to demonstrate an end-to-end DevOps workflow.

## Run locally
1. Install Python 3.12 or later.
2. Open a terminal in this folder.
3. Run `python -m pip install -r requirements.txt`
4. Run `python app.py`
5. Open http://127.0.0.1:5000 in a browser.
6. Health check: http://127.0.0.1:5000/health

## Run tests
`python -m unittest discover -s tests -v`

## Build and run with Docker
`docker build -t devops-mini-project .`
`docker run --rm -p 5000:5000 devops-mini-project`

Then open http://127.0.0.1:5000.

## GitHub Actions
The workflow in `.github/workflows/ci.yml` runs on pushes and pull requests to `main`.
It installs Python dependencies, runs tests, and builds the Docker image.

## Jira tasks to create
- DEV-01: Create application repository
- DEV-02: Implement the sample web application
- DEV-03: Add automated tests and CI workflow
- DEV-04: Create Docker image
- DEV-05: Run and verify the application

Record actual issue keys, results, and screenshots from your own run.
