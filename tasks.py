import sys
import time
from urllib.request import urlopen
from invoke import Collection
from invoke import task

from invoke_tasks.helpers import is_task_file_changed


@task
def deploy(ctx):
    pull_result = ctx.run("git pull origin master")
    if is_task_file_changed(pull_result):
        sys.exit("Pyinvoke task file(s) is changed. Please re-run this task.")
    ctx.run("pip install -r requirements.txt")
    ctx.run("python manage.py makemigrations")
    ctx.run("python manage.py migrate")
    ctx.run("python manage.py collectstatic --noinput")
    # ctx.run("sudo cp /home/ubuntu/authome/api/templates/error/502.html /home/ubuntu/authome/")
    # Restart receiving server and batch server.
    ctx.run("sudo systemctl restart authome", pty=True)
    # Give some time for reloading application.
    time.sleep(1)
    # Test if the site works well.
    with urlopen("https://autho.me") as response:
        if not response.getcode() == 200:
            sys.exit("CRITICAL: The site respond CODE " + response.getcode())
    # Success!
    print("Deploy succeeded.")

namespace = Collection(deploy)
