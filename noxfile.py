import nox


@nox.session(python=["3.8", "3.7", "3.6"])
def tests(session):
    args = session.posargs or ["--cov", "-vv"]
    session.run("poetry", "install", external=True)
    session.run("pytest", *args)


locations = "activejson", "tests", "noxfile.py"


@nox.session(python=["3.8", "3.7", "3.6"])
def lint(session):
    args = session.posargs or locations
    session.install("flake8")
    session.run("flake8", *args)
