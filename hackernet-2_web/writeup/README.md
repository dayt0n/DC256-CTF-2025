First you need to discover the /source path

Then from /source?method= you need to inspect main, which is just a common name

You'll there's a get_secret method

inspect get_secret, observe the code, copy it, get the secret: qWUXugwTzgUjSOYZ

You also can inspect index, which will tell you that you get a cookie if you have authorized: true in your session you will get a separate page, and a flag will flash.

That can be used with a tool like flask-unsign to inspect your cookie:
    `flask-unsign --sign --cookie "{'authorized': True}" --secret "qWUXugwTzgUjSOYZ"`

Which gets you a cookie, you replace your session cookie with that, and you have access to a new index page, a flag also flashes.

Flag: `uah{U23_S3CUR3_S35510N_T0K3NS}`