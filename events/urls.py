from django.urls import path
from events.views import dashboard_page,event_details,arrange_event_view,insert_participant_view, category_create_view, create_category_view, show_category, update_event, event_search_view, search_participant_view, update_participant_view, category_update_list_view, update_category_view,delete_event_search_view,delete_event_view, search_participant_delete_view, delete_participant_view, show_categories_to_delete, delete_category_view, organizer_view
urlpatterns = [
    path('dashboard/', dashboard_page, name='dashboard'),
    path('event-details/<int:id>/', event_details, name='event_details'),
    path('arrange-event/', arrange_event_view, name='arrange_event'),
    path('insert-participant/',insert_participant_view, name="insert_participant"),
    path('category-create/', category_create_view, name="category_create"),
    path('create-category/', create_category_view, name='create_category'),
    path('show-category/', show_category, name="show_category"),
    path('event-search/', event_search_view, name='event_search'),
    path('update-event/<int:id>/', update_event, name='update_event'),
    path('participant-search/', search_participant_view, name='search_participant'),
    path('participant-update/<int:id>/', update_participant_view, name='update_participant'),
    path('category-update/', category_update_list_view, name='category_update_list'),
    path('category-update/<int:id>/', update_category_view, name='update_category'),
    path('delete-event/', delete_event_search_view, name='delete_event_search'),
    path('delete-event/<int:id>/', delete_event_view, name='delete_event'),
    path('participant-delete/', search_participant_delete_view, name='search_participant_delete'),
    path('participant-delete/<int:id>/', delete_participant_view, name='delete_participant'),
    path('delete-category/', show_categories_to_delete, name='delete_category_list'),
    path('delete-category/<int:id>/', delete_category_view, name='delete_category'),
    path('organizer/', organizer_view, name='organizer'),
]
