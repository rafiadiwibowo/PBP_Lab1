from django.urls import path
from wishlist.views import show_wishlist
from wishlist.views import wishlist_xml
from wishlist.views import wishlist_json
from wishlist.views import show_json_by_id
from wishlist.views import show_xml_by_id

app_name = 'wishlist'

urlpatterns = [
    path('', show_wishlist, name='show_wishlist'),
    path('xml/', wishlist_xml, name='wishlist_xml'),
    path('json/', wishlist_json, name='wishlist_json'),
    path('json/<int:id>', show_json_by_id, name='show_jason_by_id'),
    path('xml/<int:id>', show_xml_by_id, name='show_xml_by_id'),
]   