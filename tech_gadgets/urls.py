from django.urls import path
from .views import start_page_view, single_gadget_int_view, single_manuf_int_view, GadgetView, RedirectToGadgetView, ManufacturerView


urlpatterns = [
    path('start/', start_page_view),
    path('', RedirectToGadgetView.as_view()),
    path('<int:gadget_id>', RedirectToGadgetView.as_view()),
    path('gadget/', GadgetView.as_view()),
    path('gadget/<int:gadget_id>', single_gadget_int_view),
    path('gadget/<slug:gadget_slug>', GadgetView.as_view(), name="gadget_slug_url"),
    path('manufacturer/', ManufacturerView.as_view()),
    path('manufacturer/<int:manuf_id>', single_manuf_int_view),
    path('manufacturer/<slug:manuf_slug>', ManufacturerView.as_view(), name="manuf_slug_url"),    

]
