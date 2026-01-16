from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework import status
from .models import Item
from .serializers import ItemSerializer

# 1. Pure API View (Returns JSON)
class ItemListAPIView(APIView):
    renderer_classes = [JSONRenderer]

    def get(self, request):
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)

# 2. Web View (Returns HTML using DRF Renderer)
class ItemListWebView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'api_demo/item_list.html'

    def get(self, request):
        items = Item.objects.all()
        # We pass the data to the template context
        return Response({'items': items})
