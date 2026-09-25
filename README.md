# Repo Annotator Practice

Practice repository for Python testing, mocking, Linux CLI, and Docker.

## Run tests locally

```bash
pytest -v
```

## Run tests with Docker

```bash
docker build -t repo-annotator-test .
docker run --rm repo-annotator-test
```

The Docker container provides a reproducible environment for running the test suite.
