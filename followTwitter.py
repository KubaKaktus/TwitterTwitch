import requests

url = "https://twitter.com/i/api/1.1/friendships/create.json"

payload='include_profile_interstitial_type=1&include_blocking=1&include_blocked_by=1&include_followed_by=1&include_want_retweets=1&include_mute_edge=1&include_can_dm=1&include_can_media_tag=1&include_ext_has_nft_avatar=1&skip_status=1&user_id=1409525686876913674'
headers = {
  'Content-Type': 'application/x-www-form-urlencoded',
  'Referer': 'https://twitter.com/xxxxx',
  'x-twitter-auth-type': 'OAuth2Session',
  'x-csrf-token': 'xxxxx',
  'authorization': xxxxx',
  'Cookie': 'guest_id=v1%3A163657050970076789; eu_cn=1; g_state={i_l:1,i_p:1646846243191}; ct0=xxxx; kdt=xxx; twid=u%3D1267780668546826242; auth_token=xxxx; night_mode=2; d_prefs=xx; guest_id_ads=v1%3A163657050970076789; guest_id_marketing=v1%3A163657050970076789; personalization_id=v1_I6QzTINvVQgDqaXRNSttGw==; dnt=1; _twitter_sess=BAh7CSIKZmxhc2hJQzonQWN0aW9uQ29udHJvbGxlcjo6Rmxhc2g6OkZsYXNo%250ASGFzaHsABjoKQHVzZWR7ADoPY3JlYXRlZF9hdGwrCKR%252FiuV%252FAToMY3NyZl9p%250AZCIlYTQ5M2JlMDA4OGM5NTk5MzFmNTQxMjZmMDJlMjdkYWI6B2lkIiU2MmQ4%250AODRkZmIwNTRjNWZmZGEyNjVmOWRiYTdmY2MxNQ%253D%253D--ef0bceb3f981b767edc1587bb3a186421f35bee7; external_referer=padhuUp37zjgzgv1mFWxJ12Ozwit7owX|0|8e8t2xd8A2w%3D; mbox=session#e45db1eeb1cc4444b63b2ac482ea14b5#1648982599|PC#e45db1eeb1cc4444b63b2ac482ea14b5.37_0#1712225539; at_check=true; des_opt_in=Y'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
