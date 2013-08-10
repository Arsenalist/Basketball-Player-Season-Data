
# this is basically the basketball reference query string which is produced after you execute a search

url = 'http://www.basketball-reference.com/play-index/psl_finder.cgi?request=1&match=single&type=totals&per_minute_base=36&lg_id=NBA&is_playoffs=N&year_min=1980&year_max=&franch_id=&season_start=1&season_end=-1&age_min=0&age_max=99&height_min=0&height_max=99&birth_country_is=Y&birth_country=&is_active=&is_hof=&is_as=&as_comp=gt&as_val=0&pos_is_g=Y&pos_is_gf=Y&pos_is_f=Y&pos_is_fg=Y&pos_is_fc=Y&pos_is_c=Y&pos_is_cf=Y&qual=mp_per_g_req&c1stat=&c1comp=gt&c1val=&c2stat=&c2comp=gt&c2val=&c3stat=&c3comp=gt&c3val=&c4stat=&c4comp=gt&c4val=&c5stat=&c5comp=gt&c6mult=1.0&c6stat=&order_by=ws_per_48'

import urllib2
from pyquery import PyQuery as pq

offset = 0

while True:
    realurl = url + '&offset=' + str(offset)
    f = urllib2.urlopen(realurl)
    html = f.read()
    d = pq(html)
    trs = d('table#stats tbody tr')
    if trs.length == 0:
        break;
    for tr in trs:
        tdhtml = pq(tr).html()
        row = ''
        d = pq(tdhtml)
        tds = d('td')
        for i, td in enumerate(tds):
            row = row + pq(td).text()
            if i != len(tds) - 1:
                row = row + ','
        row = row
        print row
    offset = offset + 100
