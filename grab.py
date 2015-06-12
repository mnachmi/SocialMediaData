#! /usr/bin/env python

#import pdb
#pdb.set_trace()
import json
import urllib2
import argparse
import sys

username = ''
CLIENT_ID='f9387851ff8001b7abacd24a73fe1044'
def get_user_id(username, username_url):
    """
    Get user id from username.
    """
    try:
        user_obj = urllib2.urlopen(username_url)
        user_data = json.load(user_obj)
        user_id = user_data['id']
    except:
        print "username invalid"
        sys.exit(0)
    return  user_id

def get_user_info(username):
	pass

def main():
	parser = argparse.ArgumentParser(description='\
            A sample program to grab user data from soundcloud')
	parser.add_argument('-u', action='store',
	                    dest='username',
	                    help='Store the username')
	results = parser.parse_args()
	username = results.username
	#pdb.set_trace()
	#print username
	username_url = 'http://api.soundcloud.com/users/'+username+'.json?client_id='+CLIENT_ID
	api_loc='http://api.soundcloud.com/users/'\
	        +str(get_user_id(username, username_url))+'\
                /playlists/?client_id='+CLIENT_ID

	#print get_user_id(username, username_url)
	#print api_loc
	#print username_url
	#print get_user_id(username)
	try:
            json_obj = urllib2.urlopen(api_loc)
            data = json.load(json_obj)
            print data
            #print len(data)
            #print len(data)
            #print (str(id(data)))
	except:
	    print "username inresolved ... !!"
	    sys.exit(0)
#	with open(str(username)+'.json', 'a') as f:
#		for item in data:
#			f.write("%s" % item)
#		for i in item:
#			print(i, item[i])

if __name__=="__main__":main()
