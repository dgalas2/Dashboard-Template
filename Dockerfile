FROM python:3.11
# This is an example Dockerfile for this template. It uses poetry for its build and run. 

# set env vars
ENV ENTRY_POINT="my-app" \
    PROJECT_DIR="s2-dashboard-template/" \
    ENV="LOCAL_TEST" \
# POETRY VARS
    POETRY_HOME="/"


COPY $PROJECT_DIR .

#install poetry
RUN curl -sSL https://install.python-poetry.org | python3 -

RUN /bin/poetry version

#install project reqs
RUN /bin/poetry install

# run entry point script on container start
CMD ["/bin/poetry","run","my-app"]

# expose port 8050 for dashboard
EXPOSE 8050/tcp







