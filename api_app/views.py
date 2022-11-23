from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from.models import api_model
from rest_framework.views import APIView
from.serializer import api_serializer
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK,HTTP_400_BAD_REQUEST,HTTP_204_NO_CONTENT

# Class Based View Api View
class Api_create_read(APIView):
    def post(self,request,*args,**kwargs):
        serailizer = api_serializer(data=request.data)
        if serailizer.is_valid():
            serailizer.save()
            return Response(serailizer.data,status=status.HTTP_200_OK)
        return Response(serailizer.errors,status=status.HTTP_400_BAD_REQUEST)
    def get(self,request,*args,**kwargs):
        qs = api_model.objects.all()
        serailizer = api_serializer(qs,many=True)
        return Response(serailizer.data)

class Api_read_update_delete(APIView):
    def get(self,request,pk,*args,**kwargs):
        qs = api_model.objects.get(id=pk)
        serializer = api_serializer(qs,many=False)
        return Response(serializer.data)
    def put(self,request,pk,*args,**kwargs):
        qs = api_model.objects.get(id=pk)
        serailizer = api_serializer(qs,data=request.data)
        if serailizer.is_valid():
            serailizer.save()
            return Response(serailizer.data,status=status.HTTP_200_OK)
        return Response(serailizer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk,*args,**kwargs):
        qs = api_model.objects.get(id=pk)
        qs.delete()
        return Response('delete_data successfully',status=status.HTTP_204_NO_CONTENT)

# Function based View Apiview
@api_view(['POST','GET'])
def Api_view_create(request):
    if request.method == 'POST':
        serailizer = api_serializer(data=request.data)
        if serailizer.is_valid():
            serailizer.save()
            return Response('created data successfully',status=status.HTTP_200_OK)
        return Response(serailizer.errors,status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET'])
def Api_view_list(request):
    qs = api_model.objects.all()
    serailizer = api_serializer(qs,many=True)
    return Response(serailizer.data)
@api_view(['GET'])
def Api_view_retrieve(request,pk):
    qs = api_model.objects.get(id=pk)
    serializer = api_serializer(qs)
    return Response(serializer.data)
@api_view(['PUT'])
def Api_view_update(request,pk):
    qs = api_model.objects.get(id=pk)
    serializer = api_serializer(qs,data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response('update data successfully',status=status.HTTP_200_OK)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
@api_view(['DELETE'])
def Api_view_delete(request,pk):
    qs = api_model.objects.get(id=pk)
    qs.delete()
    return Response('delete data successfully',status=status.HTTP_200_OK)




