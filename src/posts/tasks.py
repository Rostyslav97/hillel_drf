from config.celery import app

@app.task
def create_post():
    print("Post was created")