from nox import Session, session


@session(venv_backend="uv")
def test(session: Session) -> None:
    session.install(".", "pytest")
    session.run("pytest")
