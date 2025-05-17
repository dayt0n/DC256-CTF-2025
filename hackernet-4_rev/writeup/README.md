Reverse the golang binary you received in hackernet-3. You will see a DecodeKey(data) function with a hardcoded AES key.

That (data) comes from the /api/get_signing_key endpoint on hackernet, which you can access using your credentials + a `file` parameter in a POST request. 

Decrypt that AES CFB-encrypted signing key with CyberChef and you get the flag: `uah{k3y_3ncryp7_1ng_k3y}`.
