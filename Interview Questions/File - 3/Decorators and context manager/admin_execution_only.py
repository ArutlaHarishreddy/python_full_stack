#Write a decorator that only allows function execution if the user is "admin".
def admin_only(delete_user):
    def wrapper(user,*args,**kwargs):
        if user != "admin":
            print("Access Denied!, Only admin can access this function")
            return
        print("Access Granted! Executing function...")
        return delete_user(user,*args,**kwargs)
    return wrapper

@admin_only
def delete_user(user):
    print("User deleted successfully")

delete_user("admin")
delete_user("user")
