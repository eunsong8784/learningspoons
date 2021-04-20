from django.db import models
#이 코드 덕분에 장고 모델이라는 것을 알 수 있음
from django.conf import settings
from django.utils import timezone
# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    #models.ForeignKey는 다른 모델에 대한 링크를 의미
    title = models.CharField(max_length= 200) #글자수 제한 있을 때
    text = models.TextField() #글자수 제한 없을 때
    created_date = models.DateTimeField(default=timezone.now())
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()
    def __str__(self):
        return self.title

#새 모델 추가하려면 migrate 실행해야 함
