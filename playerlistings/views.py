from django.shortcuts import render
from rest_framework import generics,status
import pandas as pd
from rest_framework.response import Response
from django.core.files import File
from playerlistings.models import Intuit
from playerlistings.serializers import FileUploadSerializer,SaveFileSerializer
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser

# Create your views here.
class UploadFileView(generics.CreateAPIView):
    serializer_class = FileUploadSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        file = File(open("/Users/hamsinisankaran/Desktop/People.csv"), 'rb')
        reader = pd.read_csv(file, na_filter= False)
        print(reader)
        for _, row in reader.iterrows():
            new_file = Intuit(
                player_id=row['playerID'] or None,
                birth_country=row['birthCountry'] or None,
                birth_state=row['birthState'] or None,
                birth_city=row['birthCity'] or None,
                birthYear=row['birthYear'] or None,
                birthMonth=row['birthMonth'] or None,
                birthDay=row['birthDay'] or None,
                deathYear= row['deathYear'] or None,
                deathMonth=row['deathMonth'] or None,
                deathDay=row['deathDay'] or None,
                deathCountry=row['deathCountry'] or None,
                deathState=row['deathState'] or None,
                deathCity=row['deathCity'] or None,
                nameFirst=row['nameFirst'] or None,
                nameLast=row['nameLast'] or None,
                nameGiven=row['nameGiven'] or None,
                weight=row['weight'] or None,
                height=row['height'] or None,
                bats=row['bats'] or None,
                throws=row['throws'] or None,
                debut=row['debut'] or None,
                finalGame=row['finalGame'] or None,
                retroID=row['retroID'] or None,
                bbrefID=row['bbrefID'] or None
            )
            new_file.save()
        return Response({"status": "success"},
                        status.HTTP_201_CREATED)

    def get_player_list(request):
        if request.method == "GET":
            players = Intuit.objects.all()
            players_serializer = SaveFileSerializer(players, many=True)
            return JsonResponse(players_serializer.data, safe=False)

    def player_detail(request, pk):
        # ... tutorial = Tutorial.objects.get(pk=pk)
        try:
            players = Intuit.objects.get(pk=pk)
            if request.method == 'GET':
                players_serializer = SaveFileSerializer(players)
                return JsonResponse(players_serializer.data)
            elif request.method == 'PUT':
                player_data = JSONParser().parse(request)
                players_serializer = SaveFileSerializer(players, data=player_data)
                if players_serializer.is_valid():
                    players_serializer.save()
                    return JsonResponse(players_serializer.data)
                return JsonResponse(players_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except players.DoesNotExist:
            return JsonResponse({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND)