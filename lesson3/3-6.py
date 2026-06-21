is_logged_in = True
is_admin = True

if is_logged_in:
    print("User is logged in")
    if is_admin:
        print("Admin Panel Access Granted")
    else:
        print("show regular dashboard")
    
else:
    print("Redirect to login page")