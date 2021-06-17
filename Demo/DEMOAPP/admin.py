from django.contrib import admin

from .models import creditotp1,debitotp1,PostDebit,Post
admin.site.register(creditotp1)
admin.site.register(debitotp1)
admin.site.register(PostDebit)
admin.site.register(Post)