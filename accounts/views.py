from rest_framework import status
from rest_framework.views import APIView
from .serializer import *
from .utils import *
from .models import *
from .task import *
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
class SalesRegistrationView(APIView):

    def post(self, request):
        try:
            full_name = request.data['full_name']
            email = request.data['email']
            is_superadmin = request.data['is_superadmin']

            User.objects.create(username=email)

            sale = Sales.objects.get(email=email)
            sale.sale_password = generate_password()

            if sale.sale_password is not None:
                serializer = SalesSerializer(data=request.data)
                serializer.is_valid(raise_exception=True)

                sale.full_name = serializer.validated_data.get('full_name')
                sale.email = serializer.validated_data.get('email')
                sale.is_superadmin = serializer.validated_data.get('is_superadmin')
                sale.save()
                mail = SendEmailToSales(str(sale.email), str(sale.email), str(sale.sale_password))

                return Response({'success': True, 'message': 'User Created Successfully', 'data': serializer.data},
                                    status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'success': False, 'message': e.args[0], 'data': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


@method_decorator(csrf_exempt, name="dispatch")
class LoginView(APIView):

    def post(self, request):
        try:
            email = request.data['email']
            sale_password = request.data['sale_password']
            is_superadmin = request.data['is_superadmin']

            user = Sales.objects.filter(email=email, sale_password=sale_password, is_superadmin=is_superadmin)
            if user:
                is_active = True
                user = User.objects.get(username=email)
                refresh = RefreshToken.for_user(user)
                return Response({"success": True, "message": "Your account has been successfully activated!!",
                                'refresh': str(refresh),
                                'access': str(refresh.access_token)},
                               status=status.HTTP_200_OK)
            else:
                return Response({'success': False, 'data': None, 'message': 'user does not exist'},
                               status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'success': False, 'data': None, 'message': e.args[0]},
                            status=status.HTTP_400_BAD_REQUEST)


class ChangePasswordView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def put(self, request, pk):
        user = request.user.pk
        sale = Sales.objects.get(user_id=user)
        serializer = ChangePasswordSerializer
        if serializer.is_valid():
            if not sale.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            sale.set_password(serializer.data.get("new_password"))
            sale.save()
            return Response({'success': True, 'message': 'Password updated successfully', 'data': []})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeveloperApi(APIView):

    def get(self, request):
        if request.query_params['developer_id'] == "null":
            developer_data = Developer.objects.all().values()
            return Response({"success": True, "message": "Successfull", "data": developer_data}
                            )
        else:
            developer_id = request.query_params['developer_id']
            developer_data = Developer.objects.filter(id=developer_id).values()
            return Response({"success": True, "message": "Successfull", "data": developer_data},)

    def post(self, request):
        serializer = DeveloperSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"success": True, "message": "Developer Data Saved", "data": serializer.data})
        return Response({"success": False, "message": "NA", "data": serializer.errors})

    def patch(self, request):
        serializer = DeveloperSerializer(data=request.data)
        print(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProjectApi(APIView):

    def get(self, request):
        if request.query_params['project_id'] == "null":
            project = Project.objects.all().values()
            return Response({"success": True,"message": "All projects", "data": project}, status=status.HTTP_200_OK)
        else:
            project_id = request.query_params['project_id']
            project = Project.objects.filter(id=project_id).values()
            return Response({"success": True, "message": "Successfull", "data": project},status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"success": True, "message": "Project Data Saved", "data": serializer.data})
        return Response({"success": False, "message": "NA", "data": serializer.errors})


class CilentApi(APIView):

    def get(self, request):
        if request.query_params['cilent_id'] == "null":
            cilent = Cilent.objects.all().values()
            return Response({'success': True, 'message': 'All Cilent', 'data': cilent}, status=status.HTTP_200_OK)
        else:
            cilent_id = request.query_params['cilent_id']
            cilent = Cilent.objects.filter(id=cilent_id).values()
            return Response({"success": True, "message": "Successfull", "data": cilent}, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"success": True, "message": "Cilent Data Saved", "data": serializer.data},
                            status=status.HTTP_200_OK)
        return Response({"success": False, "message": "NA", "data": serializer.errors},
                        status=status.HTTP_400_BAD_REQUEST)


class Scheduled_call(APIView):

    def get(self, request):
        scheduled_call = Scheduled_call.object.all()
        serializer = CilentSerializer(scheduled_call, many=True)
        return Response({"success": True, "message": "Developer Data Saved", "data": serializer.data})

    # def post(self, request):
    #     dev_uuid = request.GET['dev_uuid']
    #     client_uuid = request.GET['client_uuid']
    #     project_uuid = request.GET['project_uuid']
    #     project_client_dev_data=list(project_client_dev.objects.filters(dev_uuid=dev_uuid).values_list('client_uuid',flat=True))
    #     if(len(project_client_dev_data)==0):
    #         start_time = request.data['start_time']
    #         start_date = request.data['start_date']
    #         end_time = request.data['end_time']
    #         end_date = request.data['end_date']
    #         cilent_mail = request.data['cilent_mail']
    #         # developer_mail = request.data['developer_mail']
    #         meeting_link = createMeeting()
    #         mail = SendEmail(str(cilent_mail), meeting_link[0], meeting_link[1])
    #         project_client_dev_obj = project_client_dev_data(dev_uuid=dev_uuid, client_uuid=client_uuid,project_uuid=project_uuid)
    #         project_client_dev_obj.save()
    #         return Response({'success': True, 'message': 'Test'})
    #     else:
    #         return Response({'success': True, 'message': 'Selected Developer is already alined within a project'})
