from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse, HttpResponseNotFound, Http404
import json
from django.utils.text import slugify
from django.urls import reverse
from django.views import View

from .dummy_data import gadgets, manufacturers

from django.views.generic.base import RedirectView

# Create your views here.


class RedirectToGadgetView(RedirectView):
    pattern_name = "gadget_slug_url"

    def get_redirect_url(self, *args, **kwargs):
        slug = slugify(gadgets[kwargs.get("gadget_id", 0)]["name"])
        new_kwargs = {"gadget_slug": slug}
        return super().get_redirect_url(*args, **new_kwargs)


def start_page_view(request):
    return render(request, 'tech_gadgets/test.html', {"gadget_list": gadgets})


def single_gadget_int_view(request, gadget_id):
    if len(gadgets) > gadget_id:
        new_slug = slugify(gadgets[gadget_id]["name"])
        new_url = reverse("gadget_slug_url", args=[new_slug])
        return redirect(new_url)
    return HttpResponseNotFound("not found by me")


class GadgetView(View):
    def get(self, request, gadget_slug):
        gadget_match = None
        for gadget in gadgets:
            if slugify(gadget["name"]) == gadget_slug:
                gadget_match = gadget

        if gadget_match:
            return JsonResponse(gadget_match)
        raise Http404()

    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body)
            print(f"received data: {data}")
            return JsonResponse({"response": "Das war was!"})
        except:
            return JsonResponse({"response": "Das war nix"})


class ManufacturerView(View):
    def get(self, request, manuf_slug):
        manuf_match = None
        for manuf in manufacturers:
            if slugify(manuf["name"]) == manuf_slug:
                manuf_match = manuf

        if manuf_match:
            return JsonResponse(manuf_match)
        raise Http404()

    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body)
            print(f"received data: {data}")
            return JsonResponse({"response": "Das war was!"})
        except:
            return JsonResponse({"response": "Das war nix"})

def single_manuf_int_view(request, manuf_id):
    if len(manufacturers) > manuf_id:
        new_slug = slugify(manufacturers[manuf_id]["name"])
        new_url = reverse("manuf_slug_url", args=[new_slug])
        return redirect(new_url)
    return HttpResponseNotFound("not found by me")
