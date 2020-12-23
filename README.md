# REST-API-Project
1. Learn how to play with Postman or anyother API client you prefer. Make sure you master the tool. I recommend Postman coz it is free :)
2. Read the document of DjangoRestFramework and go over the examples. Please make sure you understand
    2.1 the concept and role of serializers in general
        *Serilizers - The porcess of converting a data stracture or an object into binary in order to comunicate with other systems or save it into the memory.

    2.2 understand the difference between serializers.Serializer and serializers.ModelSerializer
        *Just like Form and ModelForm, Serializer and ModelSerializer are very similar. serializers.Serializer isa great way to recive input that is not directly interact with models. serializers.ModelSerializer is better when you want to save data and to have an access to the same daya later on. For serializers.ModelSerializer there should be a field definition from a specified model class and methods to deal with saving data to the database

    2.3 understand how to encapsulate views with
        2.3.1 mixins.ListModelMixin + GenericAPIView
        * Mixins - is a class that provides the user with the basic view behavior in a much eaiser way (No need to define the handler, just provides the action methods).
        * GenericAPIView - is an extends class REST framework that adds commonly required behavior for the standart list and detail views

        2.3.2 generics.ListAPIView
        * generics.ListAPIView is used for read only endpoints to represent a collection of models instance (need tp provide get)
        2.3.3 viewsets + Router
        * Viewsets - is a class-based view that doesn not provides method handlers like grt() and post(). instead, the class provided list() and create(). The purpose of the class is to onlt bound to the corresoinding actions at the point of finalizing the view
        * Routers - allows you to quickly decalre all of the common routers for a gicin resourceful controller instead of declaring separte routes of index

 

3. Understand how to use RBAC(Role Based Access Control) model to implement a permission management system
    3.1 What is RBAC?
    *RBAC is an approach for restricting system access based on the user autheroization.
    3.2 What is a complete RBAC cycle?
    3.3 How to implement a RBAC with DjangoRestFramework?
    * In order to implement RBAC using Django first, there is a need to assigen a uniqe token for every costumer. By doing so there will be an option to check whetrer the user has the authorities to view/edit the information. The second step is to implement the following packages: SessionAuthentication, TokenAuthentication, IsAuthenticated and to add them into the code to check for the token.
    3.4 How to implement a system to charge our customers on API calls?

 

4. How to develop a cache machanism with DjangoRestFramework? Why we need this?
