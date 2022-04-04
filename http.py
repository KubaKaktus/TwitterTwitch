import requests

url = "https://twitter.com/i/api/1.1/friendships/create.json"

payload='include_profile_interstitial_type=1&include_blocking=1&include_blocked_by=1&include_followed_by=1&include_want_retweets=1&include_mute_edge=1&include_can_dm=1&include_can_media_tag=1&include_ext_has_nft_avatar=1&skip_status=1&user_id=1409525686876913674'
headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0',
  'Accept': '*/*',
  'Accept-Language': 'en-GB,en;q=0.5',
  'Accept-Encoding': 'gzip, deflate, br',
  'Content-Type': 'application/x-www-form-urlencoded',
  'Referer': 'https://twitter.com/dreamsecretclub',
  'x-twitter-auth-type': 'OAuth2Session',
  'x-twitter-client-language': 'en',
  'x-twitter-active-user': 'yes',
  'x-csrf-token': '3e2bfe76f3316083ddf707e3f6d2ac4b152eb3dcf43826b0ba1ece6f753f06094d13fed4f9174f1e08969764643f3e437a53f0395aec99226242af669751adb744a9041981ea32ea94a5b1ca50ab0cd6',
  'Origin': 'https://twitter.com',
  'Sec-Fetch-Dest': 'empty',
  'Sec-Fetch-Mode': 'cors',
  'Sec-Fetch-Site': 'same-origin',
  'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
  'Connection': 'keep-alive',
  'Cookie': 'guest_id=v1%3A163657050970076789; eu_cn=1; g_state={i_l:1,i_p:1646846243191}; ct0=3e2bfe76f3316083ddf707e3f6d2ac4b152eb3dcf43826b0ba1ece6f753f06094d13fed4f9174f1e08969764643f3e437a53f0395aec99226242af669751adb744a9041981ea32ea94a5b1ca50ab0cd6; kdt=5urnpEaimZUdlLCrrmai56MkZQ3SOiLaHWdkovUw; twid=u%3D1267780668546826242; auth_token=c49f46086ce40573e7b7f4cda6c49c381c418bcd; night_mode=2; d_prefs=MToxLGNvbnNlbnRfdmVyc2lvbjoyLHRleHRfdmVyc2lvbjoxMDAw; guest_id_ads=v1%3A163657050970076789; guest_id_marketing=v1%3A163657050970076789; personalization_id=v1_I6QzTINvVQgDqaXRNSttGw==; dnt=1; _twitter_sess=BAh7CSIKZmxhc2hJQzonQWN0aW9uQ29udHJvbGxlcjo6Rmxhc2g6OkZsYXNo%250ASGFzaHsABjoKQHVzZWR7ADoPY3JlYXRlZF9hdGwrCKR%252FiuV%252FAToMY3NyZl9p%250AZCIlYTQ5M2JlMDA4OGM5NTk5MzFmNTQxMjZmMDJlMjdkYWI6B2lkIiU2MmQ4%250AODRkZmIwNTRjNWZmZGEyNjVmOWRiYTdmY2MxNQ%253D%253D--ef0bceb3f981b767edc1587bb3a186421f35bee7; external_referer=padhuUp37zjgzgv1mFWxJ12Ozwit7owX|0|8e8t2xd8A2w%3D; mbox=session#e45db1eeb1cc4444b63b2ac482ea14b5#1648982599|PC#e45db1eeb1cc4444b63b2ac482ea14b5.37_0#1712225539; at_check=true; des_opt_in=Y'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)