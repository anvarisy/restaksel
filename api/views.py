
from django.http import JsonResponse
from django.views import View
import json
from django.contrib.auth.hashers import make_password

from api.models import Santri
# Create your views here.

class CreateSantri(View):
    def post(self, request):
        try:
            data = json.loads(self.request.body)
            nisSantri = data["nis_santri"]
            emailSantri = data["email_santri"]
            pwdSantri = make_password(data["password_santri"])
            nameSantri = data["name_santri"]
            genderSantri = data["gender_santri"]
            addSantri = data["address_santri"]
        except:
            return JsonResponse({
            "status":False,
            "message":"Json error",
            })
        santri = Santri(nis=nisSantri, email= emailSantri, password=pwdSantri,name=nameSantri,gender=genderSantri,address=addSantri)
        santri.save()
        return JsonResponse({
            "status":True,
            "message":"Santri created",
            })
        
class GetAllSantri(View):
    def get(self, request):
        data = Santri.objects.all()
        result = []
        for item in data:
            santri = {
                "nis_santri":item.nis,
                "email_santri":item.email,
                "name_santri":item.name,
                "gender_santri":item.gender,
                "add_santri":item.address,
            }
            result.append(santri)
        return JsonResponse(
            {
            "status":True,
            "message":"Data santri",
            "data":result
            }
        )

class UpdateSantri(View):
    def post(self, request, nis):
        try:
            data = json.loads(self.request.body)
            santri = Santri.objects.get(nis=nis)
        except:
             return JsonResponse(
                {
                "status":False,
                "message":"Santri not found",
                })
        emailSantri = data["email_santri"]
        pwdSantri = make_password(data["password_santri"])
        nameSantri = data["name_santri"]
        genderSantri = data["gender_santri"]
        addSantri = data["address_santri"]
        santri.email= emailSantri
        santri.password=pwdSantri
        santri.name=nameSantri
        santri.gender=genderSantri
        santri.address=addSantri
        santri.save()
        return JsonResponse(
            {
            "status":True,
            "message":"Update Success",
            } 
        )

class GetSantriById(View):
     def get(self, request, nis):
        try:
            santri = Santri.objects.get(nis=nis)
        except:
             return JsonResponse(
                {
                "status":False,
                "message":"Santri not found",
                })
        santri = {
                "nis_santri":santri.nis,
                "email_santri":santri.email,
                "name_santri":santri.name,
                "gender_santri":santri.gender,
                "add_santri":santri.address,
            }
        return JsonResponse(
            {
            "status":True,
            "message":"Data santri",
            "data":santri
            }
        )

class DeleteSantri(View):
    def post(self, request, nis):
        try:
            santri = Santri.objects.get(nis=nis)
        except:
             return JsonResponse(
                {
                "status":False,
                "message":"Santri not found",
                })
        santri.delete()
        return JsonResponse(
            {
            "status":True,
            "message":"Data santri berhasil dihapus",
            }
        )
