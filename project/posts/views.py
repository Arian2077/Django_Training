from rest_framework.views import APIView 
from rest_framework.response import Response
from rest_framework import mixins,generics,viewsets,status,permissions


from django.http import Http404

from .models import Post
from .serializers import PostSerializer

# #simple API

# class PostListRequest(APIView):
    
#     def get(self,request):
#         posts = Post.objects.all()
#         serializer = PostSerializer(posts, many=True)
#         return Response(serializer.data)
    
#     def post(self,request):
#         serializer = PostSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)    

# class PostDetailView(APIView):
    
#     def get_object(self,pk):
#         try:
#             post = Post.objects.get(pk=pk)
#         except Post.DoesNotExist:
#             raise Http404
#         return post
    
#     def get(self,request,pk):
#         post = self.get_object(pk)
#         serializer = PostSerializer(post)
#         return Response(serializer.data)
    
#     def put(self,request,pk):
#         post = self.get_object(pk)
#         serialize = PostSerializer(post,data=request.data)
#         if serialize.is_valid():
#             serialize.save()
#             return Response(serialize.data,status=status.HTTP_200_OK)
#         return Response(serialize.errors,status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self,request,pk):
#         post = self.get_object(pk)
#         post.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

#################################################################  
# #using  generic view and mixins


# class PostListRequest(mixins.ListModelMixin,
#                    mixins.CreateModelMixin,
#                     generics.GenericAPIView):

#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
    
#     def get(self, request , *args, **kwargs):
#         return self.list(request, *args , **kwargs)
    
#     def post(self,request,*args,**kwargs):
#         return self.create(request,*args,**kwargs)


# class  PostDetailView(
#     mixins.RetrieveModelMixin,
#     mixins.UpdateModelMixin,
#     mixins.DestroyModelMixin,
#     generics.GenericAPIView):
    
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
    
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
    
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
    
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)

#################################################################

# #easist way!

# class PostListRequest(generics.ListCreateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer  

# class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

#################################################################

# #using viewsets and snippets

class PostView(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
   
        
    