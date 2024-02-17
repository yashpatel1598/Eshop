from django.shortcuts import render,redirect
from django.http import  HttpResponse, JsonResponse
from .models import *
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

# Create your views here.
def index(request):
    Products = Product.getall_prodcuts()
    Categorys = Category.getall_category()
    data = {}
    data['products'] = Products
    data['Categorys'] = Categorys
    return render(request, 'index.html', data)

class CategoryById(APIView):
    permission_classes = (AllowAny,)
    def get(self, request, category_id):
        # print(category_id)

        if not category_id:
            Products = Product.getall_prodcuts()
            Categorys = Category.getall_category()
            data = {}
            data['products'] = Products
            data['Categorys'] = Categorys
            return render(request, 'index.html', data)
            
        cat_by_pro = Product.objects.filter(category = category_id)
        Categorys = Category.getall_category()
        # print(cat_by_pro)
        data = {}
        data['products'] = cat_by_pro
        data['Categorys'] = Categorys
        return render(request, 'index.html', data)

class SignUp(APIView):
    permission_classes = (AllowAny,)
    def get(self, request):
        return render(request,'signup.html')
    
    def post(self, request):
        firstname=request.data["firstname"]
        lastname=request.data["lastname"]
        email = request.data["email"]
        phoneNumber = request.data["phoneNumber"]
        password = request.data["password"]
        RepeatPassword = request.data["RepeatPassword"]

        values = {
            'firstname' : firstname,
            'lastname': lastname,
            'email': email,
            'phoneNumber': phoneNumber
        }
        
        
        #>>>>>>>validation<<<<<<<
        if Customer.checkemail(email):
            return render(request,'signup.html',{"error":"Email already exists", "values" : values}) 
            # return JsonResponse({"message":"Email already exists"}, status=406)
        
        elif len(password) < 8 :
            return render(request,'signup.html',{"error":"Password must be grater then 8 characters", "values" : values})  
            # return JsonResponse({"msg": "Password must be grater then 8 characters"},status=401)
        
        elif password != RepeatPassword:
            return render(request,'signup.html',{"error":"Password not matched", "values" : values})  
            # return JsonResponse({"msg": "Password not matched"},status=401)
                
        else:  
            customer = Customer(firstName=firstname,lastName=lastname,email=email,phoneNumber=phoneNumber,password=password).save()
            data = {
                'message': "User Created Succesfully",
                'values': values
            }
            return redirect('homepage')
            # return JsonResponse({'message':'Customer Details Fetched','status':True, 'status_code':200}, status=200) 
        # user = User(email=youremail,first_name=firstname,last_name=lastname,phone=phoneno)
        # user.set_password(password) 
        # try :
        #     user.save()
        #     serializer = UserSerializer(user, many=False)
        #     data['message']="User Created Successfully"
        #     data['status']='success'
        #     data['token']=serializer.data['auth_token']
        # except Exception as e:
        #     data['message']=str(e)
        #     data['status']='failure'
        # return Response(data)

# class UserLogin(APIView):
#     permission_classes = (AllowAny,)

#     def post(self, request):
#         email = request.data['youremail']
#         password = request.data['password']
#         user = authenticate(username=email, password=password)
#         if user is not None:
#             login(request, user)
#             serialized_user = UserSerializer(user, many=False)
#             response_data = {
#                 'id': serialized_user.data['id'],
#                 'first_name': serialized_user.data['first_name'],
#                 'last_name': serialized_user.data['last_name'],
#                 'email': serialized_user.data['email'],
#                 'auth_token': serialized_user.data['auth_token']
#             }
#             return Response(response_data, status=HTTP_200_OK)
#         else:
#             return Response({'error': 'Invalid Credentials'}, status=HTTP_400_BAD_REQUEST)
    
# @api_view(['GET'])
# def get_current_user(request):
#     """
#     Get the current logged in user details
#     """
#     user = request.user
#     if user.is_authenticated:
#         serialized_user = UserSerializer(user, many=False)
#         return Response(serialized_user.data)
#     else:
#         return Response({'error':'Not Authenticated'}, status=HTTP_401_UNAUTHORIZED)  

# class UserLogout(APIView):
#     def post(self, request):
#         logout(request)
#         return Response({}, status=HTTP_200_OK)  
        
# class UserUpdateProfile(RetrieveUpdateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UpdateUserSerializer
#     permission_classes = [IsAuthenticated]

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)  # Calling the update method from RetrieveUpdateAPIView
#         return self.update(request, *args, **kwargs)
