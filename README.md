# REST-API-Project
1. Learn how to play with Postman or anyother API client you prefer. Make sure you master the tool. I recommend Postman coz it is free :)
2. Read the document of DjangoRestFramework and go over the examples. Please make sure you understand
    2.1 the concept and role of serializers in general:

      *Serilizers - The porcess of converting a data stracture or an object into binary in order to comunicate with other systems or save it into the memory.

    2.2 understand the difference between serializers.Serializer and serializers.ModelSerializer:

      *Just like Form and ModelForm, Serializer and ModelSerializer are very similar. serializers.Serializer isa great way to recive input that is not directly interact with models. serializers.ModelSerializer is better when you want to save data and to have an access to the same daya later on. For serializers.ModelSerializer there should be a field definition from a specified model class and methods to deal with saving data to the database

    2.3 understand how to encapsulate views with
        2.3.1 mixins.ListModelMixin + GenericAPIView
        2.3.2 generics.ListAPIView
        2.3.3 viewsets + Router

 

3. Understand how to use RBAC(Role Based Access Control) model to implement a permission management system
    3.1 What is RBAC?
    3.2 What is a complete RBAC cycle?
    3.3 How to implement a RBAC with DjangoRestFramework?
    3.4 How to implement a system to charge our customers on API calls?

 

4. How to develop a cache machanism with DjangoRestFramework? Why we need this?
