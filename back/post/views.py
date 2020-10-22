import json

from django.shortcuts import render, get_object_or_404

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import FormParser, MultiPartParser

from drf_yasg.utils import swagger_auto_schema

from .models import *
from .serializers import *


class CreateDiary(APIView):

    parser_classes = (FormParser, MultiPartParser, )

    # [{"post":1,"sticker":1,"width":0,"deg":0,"top":0,"left":99},{"post":1,"sticker":1,"width":1,"deg":0,"top":0,"left":0}]
    @swagger_auto_schema(request_body=CreatePostSerializer)
    def post(self, request, format=None):
        serializer = CreatePostSerializer(data=request.data)
        stickers = json.loads(request.data.get('stickers',[]))
        for sticker in stickers:
            sticker_serializer = PostStickerSerializer(data=sticker)
            if sticker_serializer.is_valid(raise_exception=True):
                sticker_serializer.save()
        if serializer.is_valid(raise_exception=True):
            # emotion = AI 분석
            # music = emotion 통한 추천
            serializer.save(user_id=1)
            post = Post.objects.get(pk=1)
            # 로그인 로직 구현 후 user=request.user로 변경
            return Response(ReadPostSerializer(instance=post).data, status=status.HTTP_201_CREATED)


class diary(APIView):
    def get_object(self, post_id):
        return get_object_or_404(Post, pk=post_id)
        
    def get(self, request, post_id):
        mypost = self.get_object(post_id)
        serializer = ReadPostSerializer(instance=mypost)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=UpdatePostSerializer)
    def put(self, request, post_id):
        mypost = self.get_object(post_id)
        serializer = UpdatePostSerializer(instance=mypost,data=request.data)
        stickers = json.loads(request.data.get('stickers', []))
        for sticker in stickers:
            sticker_id = sticker['id']
            post_sticker = PostSticker.objects.get(pk=sticker_id)
            poststicker_serializer = PostStickerSerializer(instance=post_sticker, data=sticker)
            if poststicker_serializer.is_valid(raise_exception=True):
                poststicker_serializer.save()

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(ReadPostSerializer(instance=Post.objects.get(pk=1)).data)
            return Response(serializer.data, status=status.HTTP_200_OK)
    
    def delete(self, request, post_id):
        mypost = self.get_object(post_id)
        mypost.delete()
        
        msg = {
            "detail": "오늘 하루가 사라졌습니다."
        }

        return Response(msg, status=status.HTTP_200_OK)
