from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from .models import collection

class StatusCountView(View):
    def get(self, request):
        start_time = int(request.GET.get('start'))
        end_time = int(request.GET.get('end'))

        pipeline = [
            {"$match": {"timestamp": {"$gte": start_time, "$lte": end_time}}},
            {"$group": {"_id": "$status", "count": {"$sum": 1}}}
        ]

        results = list(collection.aggregate(pipeline))
        status_counts = {str(result["_id"]): result["count"] for result in results}

        return JsonResponse(status_counts)

