from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from .serializers import ExerciseSerializer
from .models import Exercise

class ExerciseAPIView(APIView):
    permission_classes = [AllowAny]
    
    def get(self, request):
        exercises = Exercise.objects.all()
        # DRF recommends getting a fresh queryset when using a class-level queryset.
        serializer = ExerciseSerializer(exercises, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ExerciseSerializer(data=request.data)
        if serializer.is_valid():
            exercise = serializer.save()
            return Response(ExerciseSerializer(exercise).data, status=201) # 201 Created indicates that the request was successful and a new resource was created as a result.
        return Response(serializer.errors, status=400) # 400 Bad Request indicates that the server cannot process the request due to a client error (e.g., validation errors).