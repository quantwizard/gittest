from HTMLParser import HTMLParser

class CRTCHTMLParser(HTMLParser):
    idFlag  = 0
    dataDict  = {}
    list = []

    
    
    def handle_starttag(self, tag, attrs):
        if tag == "tr":           
        	self.idFlag = 1
            
    def handle_endtag(self, tag):
        if tag == "tr":
            self.idFlag = 0
    
    def handle_data(self, data):
        if self.idFlag == 1:
            if len(data) > 3:
                self.list.append(data)
                
                #dataDict[list[0].strip()] = list[1].strip()
        

if __name__ == "__main__":
    htmlData = '''
<tr>
  <td align="right" valign="top">
    <b>Build ID:</b></td><td>30418</td>
</tr>
<tr>
  <td align="right" valign="top"><b>Timestamp:</b></td><td>2015/06/03 20:25:37</td>
</tr>
<tr>
  <td align="right" valign="top"><b>Tag:</b></td><td>player_master-150603-1043</td>
</tr>
<tr>
  <td align="right" valign="top"><b>Ribosome Tag:</b></td><td>ribosome-3_0_21</td>
</tr>
<tr>
  <td align="right" valign="top"><b>Owner:</b></td><td>ckarusala</td>
</tr>
<tr>
  <td align="right" valign="top"><b>Branch:</b></td><td>realplayer_18_0_0</td>
</tr>
<tr>
  <td align="right" valign="top"><b>Target:</b></td><td>player_master</td>
</tr>
<tr>
  <td align="right" valign="top"><b>Profile:</b></td><td>helix-realplayer-defines</td>
</tr>
<tr>
  <td align="right" valign="top">
    <b>Platforms:</b></td><td>win-x86-vc10</td>
</tr>
<tr>
  <td align="right" valign="top"><b>Type:</b></td><td>release</td>
</tr>
<tr>
  <td align="right" valign="top"><b>Options:</b></td><td>archive, drmsign, embed_manifest, map, pdb, ribosome, symbols, checkout_bytime</td>
</tr>
<tr>
  <td align="right" valign="top"><b>Date:</b></td><td>Wed Jun  3 20:25:26 2015</td>
</tr>'''
    
    htmlParser = CRTCHTMLParser()
    htmlParser.feed(htmlData)
    #print htmlParser.list
    index = htmlParser.list.index("Branch:")
    print htmlParser.list[index+1]
    index = htmlParser.list.index("Tag:")
    print htmlParser.list[index+1]

