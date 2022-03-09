from invoke import task

#@task
#def start(ctx):
#    ctx.run("flask run", pty=True)

@task()
def pytest(ctx):
    ctx.run("pytest src", pty=True)

@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest", pty=True)

@task(coverage)
def coverage_report(ctx):
    ctx.run("coverage html", pty=True)

@task()
def robot(ctx):
    ctx.run("sh run_robot_tests.sh", pty=True)

@task
def lint(ctx):
    ctx.run("pylint src")

@task(pytest, robot, lint)
def test(ctx):
    print("Lorem ipsum")
