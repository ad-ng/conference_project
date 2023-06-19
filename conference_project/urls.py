urlpatterns = [
    # www.conference.rw/admin/
    path('admin/', admin.site.urls),


    path('', include('core.urls')),
    path('speakers/', include(speakers.urls))

]