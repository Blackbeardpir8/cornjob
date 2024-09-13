form .models import News

def my_schedule_job():
    News.objects.create(
        title="Scheduled News",
        description="This is a description for scheduled news.",
        image="https://pypi.org/project/django-crontab/",
        external_link="https://pypi.org/project/django-crontab/"
    )
