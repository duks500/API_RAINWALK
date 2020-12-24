# REST-API-Project


## 1. Learn how to play with Postman or another API client you prefer. Make sure you master the tool.


## 2. Read the document of DjangoRestFramework and go over the examples. Please make sure you understand

### 2.1 the concept and role of serializers in general

- Serializers - The process of converting a data structure or an object into binary in order to communicate with other systems or save it into the memory.

### 2.2 understand the difference between serializers.Serializer and serializers.ModelSerializer
- Just like Form and ModelForm, Serializer and ModelSerializer are very similar. serializers.Serializer is a great way to receive input that does not directly interact with models. serializers.ModelSerializer is better when you want to save data and to have access to the same data later on. For serializers.ModelSerializer there should be a field definition from a specified model class and methods to deal with saving data to the database


### 2.3 understand how to encapsulate views with
#### 2.3.1 mixins.ListModelMixin + GenericAPIView
- Mixins - is a class that provides the user with the basic view behavior in a much easier way (No need to define the handler, just provides the action methods).
- GenericAPIView - is an extended class REST framework that adds commonly required behavior for the standard list and detail views

#### 2.3.2 generics.ListAPIView
- generics.ListAPIView is used for read-only endpoints to represent a collection of models instance (need to provide get)



#### 2.3.3 viewsets + Router
- Viewsets - is a class-based view that does not provide method handlers like get() and post(). instead, the class provided list() and create(). The purpose of the class is to only bound to the corresponding actions at the point of finalizing the view
- Routers - allows you to quickly declare all of the common routers for a given resourceful controller instead of declaring separate routes of index


## 3. Understand how to use RBAC(Role-Based Access Control) model to implement a permission management system

### 3.1 What is RBAC?
- RBAC is an approach for restricting system access based on the user authorization.

### 3.2 What is a complete RBAC cycle?
- N/A

### 3.3 How to implement an RBAC with DjangoRestFramework?
- In order to implement RBAC using Django first, there is a need to assign a unique token for every customer. By doing so there will be an option to check whether the user has the authority to view/edit the information. The second step is to implement the following packages: SessionAuthentication, TokenAuthentication, IsAuthenticated and to add them into the code to check for the token.

### 3.4 How to implement a system to charge our customers on API calls?
- There is a need to add an authorization to the code by checking at the beginning of every function whether the user has the right authorities to use the function/class.

## 4. How to develop a cache mechanism with DjangoRestFramework? Why we need this?

- The issue with dynamic websites is that every time the user requests a page, the server makes all sorts of different calculations in the background. Those calculations can be very expensive and time-consuming. Therefore, by using the cache mechanism, the server can save the results of those calculations in case there will be a need to make the same call later on.
- To use the cache mechanism in Django REST Framework can be achieved by using the cache_page() function which will cache the page for a fixed number of seconds/minutes/hours. 
