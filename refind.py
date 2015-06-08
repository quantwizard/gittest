import re

data = '''
<html><head><link rel="ICON" href="images/favicon.ico" type="image/x-icon"><link rel="SHORTCUT ICON" href="images/favicon.ico" type="image/x-icon"><title>Report for Build: player_master-150516-964</title></head><body bgcolor="#ffffff"><table border=0 cellspacing=0 cellpadding=2 bgcolor=#000000 width=100%>
  <tr>
    <td align=left valign=right>
      <b><FONT SIZE=+1> <FONT COLOR=#0000FF>Real</FONT>
      <FONT COLOR=#FFFFFF>Networks</FONT></FONT></b>
    </td>
  </tr>
</table><table border=0 cellspacing=0 cellpadding=2 width=100% bgcolor=e6e6e6>
<tr>
  <td align=center>[<a href="http://mag-build.prognet.com/~build/index.html">Build Home</a>]</td>
  <td align=center>[Search: <a href="http://mag-build.prognet.com/~build/builddb.cgi">Builds</a>,
  <a href="http://mag-build.prognet.com/~build/filedb.cgi">Files</a>,
  <a href="http://mag-build.prognet.com/~build/builddb.cgi?days_ago=0">Today</a>]</td>
  <td align=center>[<a href="http://mag-build.prognet.com/~build/bif.cgi">BIF Viewer</a>]</td>
  <td align=center>[<a href="http://mag-build.prognet.com/~build/queue.cgi">Build Queue</a>]</td>
  <td align=center>[<a href="http://mag-build.prognet.com/~build/status.cgi">Machine Status</a>]</td>
  <td align=center>[<a href="http://mag-build.prognet.com/~build/build.cgi">Submit Build</a>]</td>
</tr>
</table>
<h1>Report for Build: player_master-150516-964</h1><table bgcolor=e6e6e6 width=100%><tr><td>
<table>
<tr>
  <td align="right" valign="top">
    <b>Build ID:</b></td><td>29731</td>
</tr>
<tr>
  <td align="right" valign="top"><b>Timestamp:</b></td><td>2015/05/16 13:55:37</td>
</tr>
<tr>
  <td align="right" valign="top"><b>Tag:</b></td><td>player_master-150516-964</td>
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
  <td align="right" valign="top"><b>Date:</b></td><td>Sat May 16 13:55:26 2015</td>
</tr>
<tr>
  <td align="right" valign="top"><b>URL:</b></td><td><a href="http://mag-build.prognet.com/~build/build/realplayer_18_0_0/player_master/player_master-150516-964">http://mag-build.prognet.com/~build/build/realplayer_18_0_0/player_master/player_master-150516-964</a> (<a href="download.cgi?id=29731">Download</a>)</td>
</tr>
<tr>
  <td align="right" valign="top"><b>Summary:</b></td><td>player_master:ckarusala:archive,drmsign,embed_manifest,map,pdb,ribosome,symbols,checkout_bytime,release:realplayer_18_0_0:win-x86-vc10:helix-realplayer-defines:ribosome-3_0_21</td>
</tr>
<tr>
  <td align="right" valign="top"><b>Actions:</b></td><td>
<a href="http://mag-build.prognet.com/~build/archive.cgi?id=29731">Archive</a>, 
<a href="buildbranch.cgi?branch=realplayer_18_0_0&target=player_master&platforms=win-x86-vc10&opts=archive%2Cdrmsign%2Cembed_manifest%2Cmap%2Cpdb%2Cribosome%2Csymbols%2Ccheckout_bytime%2Crelease&tag=2015/05/16%2013%3A55%3A37&profile=helix-realplayer-defines&ribotag=ribosome-3_0_21">Rebuild</a>, 
<a href="http://mag-build.prognet.com/~build/rebuild.cgi?id=29731&platform=&confirm=no&action=Kill">Kill</a>, 
<a href="http://mag-build.prognet.com/~build/rebuild.cgi?id=29731&platform=&confirm=no&action=tag">Tag</a>, 
<a href="http://mag-build.prognet.com/~build/rebuild.cgi?id=29731&platform=&confirm=no&action=branch">Branch</a>, 
<a href="http://mag-build.prognet.com/~build/rebuild.cgi?id=29731&platform=&confirm=no&action=diff">Diff</a>
</td></tr>
</table>
<form method=post action="report.cgi">
<input type=hidden name=id value=29731>
<table><tr>
  <tr><th align=left>Comments</th></tr>
  <td><textarea cols=80 rows=10 name=comment>RealTimes V2 Launch RC6</textarea></td>
  <td alight=right valign=bottom>
    <input type=submit value="Set Comment"></td>
  </td>
</table>
</form>
</td></tr></table><br><table width=100%% border=0 cellspacing=0 cellpadding=5><tr bgcolor=#88ff88><th colspan=7><h3><u>Platform Specific Build Information</u></h3></th></tr><tr bgcolor=#88ff88><th align=left>Platform</th><th align=left>Status</th><th align=left>Build Time</th><th align=left># of Failed Modules<br>(Details Below)</th><th align=left>Link to Build</th><th align=left>Download</th><th align=left>Fast rebuild</th></tr><tr bgcolor=#ccccee><td align=left>win-x86-vc10</td><td align=left>Complete</td><td align=left>2:32.09</td><td align=left>0</td><td align=left><a href="http://mag-build.prognet.com/~build/build/realplayer_18_0_0/player_master/player_master-150516-964/win-x86-vc10">Click Here</a></td><td align=left><a href="download.cgi?id=29731&platform=win-x86-vc10">Zip</a></td><td align=left>Not available</td></tr><tr bgcolor=#88ff88><th align=left>&nbsp</th><th align=left>&nbsp</th><th align=left>&nbsp</th><th align=left>&nbsp</th><th align=left>&nbsp</th><th align=left>&nbsp</th><th align=left>&nbsp</th></tr></table><br><table width=100%% border=0 cellspacing=0 cellpadding=5><tr bgcolor=#88ff88><th colspan=6><h3><u>Component Version Numbers</u></h3></th></tr><tr bgcolor=#88ff88><th align=left>Version File</th><th align=left>Major</th><th align=left>Minor</th><th align=left>Release</th><th align=left>Build</th><th align=left>Build Name</th></tr><tr bgcolor=#ccccee><td align=left>realplay/realplay.ver</td><td align=left>18</td><td align=left>0</td><td align=left>0</td><td align=left>112</td><td align=left>&nbsp</td></tr><tr bgcolor=#ffffff><td align=left>realtimes/rtcreator.ver</td><td align=left>17</td><td align=left>4</td><td align=left>1</td><td align=left>445</td><td align=left>&nbsp</td></tr><tr bgcolor=#88ff88><th align=left>&nbsp</th><th align=left>&nbsp</th><th align=left>&nbsp</th><th align=left>&nbsp</th><th align=left>&nbsp</th><th align=left>&nbsp</th></tr></table><br><table width=100%% border=0 cellspacing=0 cellpadding=5><tr bgcolor=#88ff88><th colspan=3><h3><u><a href="http://mag-build.prognet.com/~build/build/realplayer_18_0_0/player_master/player_master-150516-964/win-x86-vc10">win-x86-vc10</a></u></h3></th></tr><tr bgcolor=#88ff88><th align=left>Module</th><th align=left>During Build Mode</th><th align=left>Error Output</th></tr><tr bgcolor=#88ff88><th align=left>&nbsp</th><th align=left>&nbsp</th><th align=left>&nbsp</th></tr></table>
<!-- Total time used: 0.102485 seconds -->
<p><hr>Maintained by <a href="mailto:es@realnetworks.com">Engineering Support</a></p></body></html>'''
pat = re.compile(r'\player_master-\d{6}-\d{1,5}')
items = pat.findall(data)
print items
