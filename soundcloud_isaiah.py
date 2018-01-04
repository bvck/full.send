import requests
import json

#make the spotify api query
url = "https://api.spotify.com/v1/search?type=track&q=isaiah+rashad&limit=48"

# send the query
r = requests.get(url)
# turn the query into a JSON string so we can look through it
data = json.loads(r.text)

# create the string that will turn into the html file
html = ''

# add the migos button link to the page
html += '''
    	<form action="migos.html">
		Sup<br>
		<input value = "MIGOS" type="submit"/><br>
	</form>
    '''
    
# make the black background
html += '<style> body {background-color: black;}</style>'

# embedded youtube player
#html += '<iframe src="http://www.youtube.com/embed/OpIQNxiKJoE?&autoplay=1" frameborder="0" style="overflow:hidden;overflow-x:hidden;overflow-y:hidden;height:50%;width:50%;position:absolute;top:300px;left:400px;right:0px;bottom:0px" height="50%" width="50%"></iframe>'

# embedded soundcloud player
html += '<iframe width="100%" height="450" scrolling="no" frameborder="no" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/289147848&amp;auto_play=true&amp;hide_related=false&amp;show_comments=true&amp;show_user=true&amp;show_reposts=false&amp;visual=true"></iframe>'

# parses the spotify query for album covers, adds them to the html file one by one
for track in data['tracks']['items']:
    img = track['album']['images'][1]['url']
    html += '<img src="' + str(img) +'" />'
    print img

# the clock counter thing i added. maybe useless
#html += '<iframe src="http://free.timeanddate.com/countdown/i5n58b87/n4797/cf107/cm0/cu4/ct0/cs0/ca0/cr0/ss0/cac09f/cpc000/pcfff/tcfff/fs100/szw320/szh135/tatthis%20is%20a%20countdown%20but%20roll%20with%20it/tac090/tptTime%20since%20Event%20started%20in/tpc000/matYou\'ve%20been%20studying%20for%3A/mac00f/mpc000/iso2017-03-23T00:00:00" allowTransparency="true" frameborder="0" width="0" height="0"></iframe>'

# finally writes the whole thing to an html file in the directory that this python script is saved
f = open('isaiah.html', 'w')
f.write(html)
f.close
