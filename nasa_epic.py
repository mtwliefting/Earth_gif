import sys
import json
import urllib.request as urllib2
import imageio

data = urllib2.urlopen('http://epic.gsfc.nasa.gov/api/images.php')
data = json.loads(data.read())

with imageio.get_writer('~/Desktop/earth.gif', mode='I') as writer:

    for i in data:
        filename = 'http://epic.gsfc.nasa.gov/epic-archive/jpg/' + i['image'] + '.jpg'
        image = imageio.imread(filename)
        writer.append_data(image)