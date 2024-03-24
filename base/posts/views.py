from rest_framework.views import APIView

# Create your views here.

class GetPostView(APIView):
    def get_queryset(self,post_id):
