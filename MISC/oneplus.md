# Oneplus N100 FRP bypass 

Disclaimer in finnish:
Oneplus nord N100 puhelimen FRP:n ohittaminen. Kirjoitan nämä muistiinpanot englanniksi, mutta ohjeet helposti käännettävissä suomeksi vaikka Googlen kääntäjällä. Helpolla pääset kun valitse laitetta käynnistäessä kieleksi englannin. FRP on **F**actory **R**eset **P**rotection, eli tehdasasetusten palauttamisen suojaus. Tällä pyritään suojaamaan laite, jos se esimerkiksi joutuu vääriin käsiin. Sen voi ajatella vaikka varkauden estona.

## Background

From [android central](https://www.androidcentral.com/factory-reset-protection-what-you-need-know) see more details. Main points:
* Factory Reset Protection (FRP) is a security method that was designed to make sure someone can't just wipe and factory reset your phone if you've lost it or it was stolen.
* On most phones, it will be automatically done whenever you choose to reset the data through the phone's settings. If your phone has an extra layer of reset protection from the company who built it or has a "find my phone" app from the company who built it, you'll want to disable that manually first.

### The case in hand
In this case a young person with Google Family link **tried to bypass the family link by doing a factory reset.** This resulted in a situation in where all data had been deleted and ALSO now the account which had been used to activate the device was forgotten and couldn't be recovered from the device. Nice going kid! FRP actived and the device had to be unlocked with the original user account or the FRP was to be bypassed. There was no way to get or recover the account.

*Also the normal* reboot menu options tried, but where not sufficient.

## Steps

I followed instructions from this [video](https://www.youtube.com/watch?v=OO9154XHiyc)

1. Open the device normally
2. Connect to WiFi
3. Let it do the updates
4. Go back, take **add network** option from the WiFi list
5. Try to use google voice typing, but when prompted with permission click dismiss. Repeat this step few times
6. To bottom appears info box where is:*"Gboard needs microphone acces to enable voice typing"* Click allow!
7. You are tranfered to permission settings. Use search from above and search for Chrome and click the app from results.
8. You are tranfered to Chrome app settings, click *open*
9. Check allow everything asked. **Now** you can browse the internet because you have an open browser and internet connectiong set up in step 2
10. Searct ictfix, which gives you ictfix.net and go to APK & FRP
11. Choose *open settings app.* Now, I didn't try without but the link on [ictfix.net](https://ictfix.net/apk-frp/) is *intent://com.android.settings/#Intent;scheme=android-app;end* **but** doesn't it refer straight to your devices settings without any meddling?
12. Go to apps, check 3 dots on upper right corner and choose to see system apps. Disable, force stop and clear the storage & cache for *android setup* and *google play services*
13. Use the go back button (triangle) and go all the way back to terms and conditions. Remember android stacks screens on top of each other, so browse back! Agree, after reading ofcourse. 
14. Skip mobile setting if prompted
15. From WiFi screen choose *set up offline*
16. From here proceed normally the setting procedure until the phone is ready to be used. **Congratulations!**

## After
When the phone was open with a user I did a factory reset from the settings menu and did a normal set up with a new Google account which was linked to family link all ready.


This was done on march 10th 2022.






