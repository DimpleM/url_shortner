To insatll dependencies, run
    pip install -r requirements.txt

Navigate to the Directory:
    cd url_shortner_system

Run the Applicaiton:
    python manage.py runserver 8000
    (Add Allowed Host in settings and run python manage.py runserver 8000 HostIP)

Open the WebApp in Browser
    Open http://localhost:8000/home for Shorten URL(Expiry Time: expiration of the url, Private Token: for privacy, Custom Code: for creating custom url)
    Open http://localhost:8000/retrieve for Unshorten URL
