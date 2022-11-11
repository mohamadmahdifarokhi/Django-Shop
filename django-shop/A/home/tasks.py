from bucket import bucket
from celery import shared_task


# bara inke bad inke etelaat ro greftim site load beshe
# kare js karas
# TODO: can be async?
def all_bucket_objects_task():
    result = bucket.get_abjects()
    return result


# bara inke selery beshnase
@shared_task
def delete_object_task(key):
    bucket.delete_object(key)


@shared_task
def download_object_task(key):
    bucket.download_object(key)
