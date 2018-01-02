Usage
The initial state is set to?user.
Every time?user?state is triggered to?advance?to another state, it will?go_back?to?user?state after ¡§work¡¨ or ¡§free¡¨.
* user
o Input-1-1: "monday"
* Reply: "work or free"
o Input-2: "work"
* Reply: "ok,work"
* bo back to user
o Input-2: "free"
* Reply: "ok,free"
* bo back to user
o Input-1-2: "tuesday"
* Reply: "work or free"
o Input-2: "work"
* Reply: "ok,work"
* bo back to user
o Input-2: "free"
* Reply: "ok,free"
* bo back to user
o Input-1-3: "wednesday"
* Reply: "work or free"
o Input-2: "work"
* Reply: "ok,work"
* bo back to user
o Input-2: "free"
* Reply: "ok,free"
* bo back to user
o Input-1-4: "thursday"
* Reply: "work or free"
o Input-2: "work"
* Reply: "ok,work"
* bo back to user
o Input-2: "free"
* Reply: "ok,free"
* bo back to user
o Input-1-5: "friday"
* Reply: "work or free"
o Input-2: "work"
* Reply: "ok,work"
* bo back to user
o Input-2: "free"
* Reply: "ok,free"
* bo back to user

o Input-1-6: "saturday"
* Reply: "work or free"
o Input-2: "work"
* Reply: "ok,work"
* bo back to user
o Input-2: "free"
* Reply: "ok,free"
* bo back to user
o Input-1-7: "sunday"
* Reply: "work or free"
o Input-2: "work"
* Reply: "ok,work"
* bo back to user
o Input-2: "free"
* Reply: "ok,free"
* bo back to user

