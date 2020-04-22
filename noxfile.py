import nox

# Excluding black from the sessions run by default
nox.options.sessions = "lint", "tests"


@nox.session(python=["3.8", "3.7", "3.6"])
def tests(session):
    args = session.posargs or ["--cov", "-vv"]
    session.run("poetry", "install", external=True)
    session.run("pytest", *args)


locations = "activejson", "tests", "noxfile.py"


@nox.session(python=["3.8", "3.7", "3.6"])
def lint(session):
    args = session.posargs or locations
    session.install("flake8", "flake8-black", "flake8-import-order")
    session.run("flake8", *args)


@nox.session(python="3.8")
def black(session):
    args = session.posargs or locations
    session.install("black")
    session.run("black", *args)
