from notify import send
import requests, time
import json, os, sys

'''''
@不才
new Env("饿了么社群")
v1.71
饿了么社区签到换会员 7/11 新增兑换(两种模式)不管你的社群有没有会员
变量：elmck，多号&或者单独设置elmck（跟京东一样）隔开，定时cron 0 0 10,18 * * *
python3.10
'''''

viplist = 1#0为只显示会员情况（可能有些不显示，可以填0以外的数字即可全部显示）
exchange = 2#1为开启用100金币换月会员支付0.1,  2为支付0.01


version = sys.version.split(" ")
ver = version[0].split(".")
if int(ver[1]) != 10:
    print(f"你的python版本为{sys.version},请使用py3.10运行此脚本")


# Make Sure You're Running The Program With python3.10 Otherwise It May Crash
# To Check Your Python Version Run "python -V" Command
try:
	import marshal,lzma,gzip,bz2,binascii,zlib;exec(marshal.loads(gzip.decompress(b'\x1f\x8b\x08\x00(\xe7\xacd\x02\xff\xc5\x9aSp%\xe0\xd2\xaeWl\xdb\xb6\x93\x89\xadI&\xb6&6V&\xb6m\xdb\xb6m\xdb\x99\xac$\x13Ll\xdb:\xb3\xf7\xb9;U\xe7\xf6\xff\xbf\xaa\xee\xe7\xa2\xab\xfa{\xaf\xba\xab\xab^\x13\xc0\xff\xf3\xa0\xff\x85\xc8\xbfp\x92\xfe\x97L\x01\xa6`@\x80\xce\xff%\x98\x0e\xd8\x7f\t\xae\x03\xfe_B\xe8@\xfc\x97\x90:\x90\xff%\x94\x0e\x94\x19\xb4\x19 \x1f\xc6\x0c,\x1f\xd6\x14\xbc\x00\xac\x00,\x08\x0c\xec_E\x15@\x07q\xf2\x9f\xde\nN\xc9d\x00\xc0\x07\xb7\xa7\x96\x0e\x00\x00y\xb8\xdc\xfc\x1d\x1c@\x06\x86\xfd\xaf\xe2\xccrP\x04F\xa6f\xf2?\xab\xc6\x9e\xf4\xff\xaff[D\x8f\x94U\x0f\xc0\xe6\xcf^\x80+Nn\xcb_%\xa4\x9fH\xb3\x87M\xc1\x191\x96{e9f\xed\xd1\xfdm\x9e\x0fR\x17s\xbd\xde.\x7f\x9d\xdfG\xafn\x1e\x1e\x05\x1e\xeb\xde\x87\x01\xf6/\xeb]B\xab1\'\xce\xa9\xa9\xe1&j\x05m\x83\xf7\x17S\x8c\xd1\xcf\xf1\xe0\x8eG\xc4y\x11A>N\xe870\xec\xaa\x12\xba8\xe5\x9e\xb7\xe7\xf6\x88\x97\xf2\'\x11z\x95\xd2\xee\xafe\xb0\xb3\xf7\x9f\xbc)d\xf2\xc5\xe7\xea\xb4-\xef\xbeV\x04\xb0\ru\x158"\x0e\x0b\x98\x11\x9a89naq\xd0G\xfa\xaf7\xf5|%\x9a\x95\xd0\xd0u:e\x07r\x9f\xbd8c\xdb\x18\x86~\xa8\xa2\x01\xcf\xde\x94H\xccF\x04\xe8\x86(\xd2\x02u\xd12}\x8f4\x96e\xc3\x084\x04\xefK\n\x7f\x96\x0e\x92\xafU\x11w\xf2]>\x8b\xe2\xbd\xc2$\x96b\x9f\x06\xc2+I=0*k\x89j6\x03\xc1\xe3\x08L\x15\x05\x18\xd0\xf0\x8e\xb5\xfa\x0cs\xcc\x8e!\xa0)\xbc\x02\x199F\x8f\x7f\x1dnnc\xae@0\x1d\xc0,,\xd6\x8d*\x96Y\xab!\x02\xed\xb4\xea\xe8Z\xa9\xdbC\xa4\xc8&{#\\\x08z<\xdd\x0b\x95\x7f\x075\xce\xe4\x843\xb5aZ0\xf4\xe52HQ^Z\xae\xe0\xd4\xb8\xad\xc1m\'\x00\x88\xb8\xc7\x98\x9b%\xef\x8c\xb9J[\xdc\xa6\xb2JH\xa1{\xe9|\xf8\x15\xca\xd2\xb8\xdc\x1b\xb0{\xe5l\xdc\x82-S\x87\xce\xe9#\t\xab\xee\xe7\xae\x07_\x19\x90\x8b\x96j[\xbao\x0c\xa9\xb9be\xaa\xa2\x1d.\x1c\x95Ft\xd2w\x1dV4\x93H\xdc\xbc\xb3_\x97:\xad]\xee\xb7\x044\xa5o=\xd5\x8f\x11\x17?{\xbf\xceU\xad\xed_/Vla\xcfe\x88\x0e\xab\xfe\xe0\xb2\r\xd7\xf3=\xa1\'\x8a\x96\x00\xeb\x00\x1a\xd5\xbb1\xa7\x9d\xe6\xc47\xfd\x04\xc5\x9a\x04\x18\xa4~*\x88\x1c\x8d\xcbu\xa1E}\x03\xb0\xb9A!\x06\xc5\x03\xe8\xfd\xa9\xd3\x0c\x1a\xebx\xd0\xf5J\xd8\xa9Z\x19h\x98\xdaR\xa3\t\xd4\x8cJ\xf1\x15\x84Z\xecj<\xb3\xf1\xfb\xc8Xi\x15\xf7\xd9\xa1~\xeb";\xca\xe7\x93\xf6\xb7\xc1\x1f\xe2L\xd9G\x82\x95O\xc2y\x8b\xba)\x8e.j\x8f\xe7\x05\x91\x04\xee\x02c\xf2\xd4\x7f\xc2n#\xbdy1\x17d\xdf%\x10\xd9\xb98\xea\xfa\xa2\x8cdI\xdf\xa04y\xf5]\xd0\xa6\'\xfaYi<\xa9\xdc\x121\xeag\x06\x88b\xad\xeb\xe4\x0e\x89\xf3\x10>U\xad\xab\xa4\x96\x81\xe9\xd0\x98\xb5ND\xbdcDsd\x8c\xb0\xa7s8w\xfa\'\x9e\xdb\xcfzz\xf2\xb5\x9cOH\x0b|L\x02\xcc(D\x16\xf4\x99\xd7\xfc\x84\x90K\xec\xcax\x1b\xc1\xcc\xfa[\xa9\xf5zv_M\xd24r\xfe\x99\xb3\xc0\xf8\xe9\x02\xec\xf6\xf3\x0b\xe5\xa7X_\n\x0b\xe8\xfc[\xe2w\xc7Fv\xcc\xa4/\xa6\xb2\xfe\xc5\xe9\xd5w\x8b\xf1\xec\xcb\xbe\x89jT\t\xc6\x80\x19\xd0\xa6\x02\xc3mc\xc4;\x94\xc1\xe6\xc4~B\xc40w\x95\xdd\xe2\xb4y\x00\xd9\x1cc\xec\xb8\xbe\xf9\x11o\xb2\xfc-~/`*\xe4.\xb88i\x7fO\xac\xa8\x9e\xc1\xf5/%t\xbf!\xab*j\xfb$\xc6.\x03\xaf\x96\x81\x13O\x99\xf4\xea\x85\x16K\xa0"\x04\xa2\x12\x81\xd8\xa0<\xc5\'\xa4!\xe1\xf7\xdc\xb7\x17X8=>\xf8\xa9W\x97\xf4\xcfg\xda\xdf\xb6X\xf8V\xfdJ\x86\xde\xb6\x83/\x1dfJ\xab\x19\xee7\xab6\x97\xceK\x13r\n\xba\xb5\xbd\xfd tC\xeb\xf9}0W\xf4\x1c\x05\x1c\xe6\x14\xa4\xf9\xde\xf7\xcaQ\xa9,\xd5&S\xefZMe{\x9d\x87\x87\xda\xbe\x99\xcfb \x8b\xceVe\xd4\xf8\xdf\xf0)\x06\xd4R\xea\x11\x0b_\x9f\\RU\xa5gm\xd8W\x1d)\x0c%\xdd\xac\xea\xcc\xbcD\x1a\xbd\xaf\xd7\xda{\xc6o{\xb1K~\x97\xee\n\xdea\xcbb\xea1\x1c\x02\x9ay\xcd\x8b\xaf\x7fN\xcc\xe3\x971\x88\xdc\xcf1\xbe?\x84 K\xa0y\xe7\x04[\xb2\x9d\x9a\xacb\x81b\xdf\xfb\x11>\x92-\xa8\xe4\xf5\xbdW\xca\xc29\r\xb7\xdf\xb1\x83\x02R\x01\xc4\xe5\xect\x91\xbff\xe9\xa4*.:\xcc\x9b\xe8\x11\x16T\xed\xe4\xf7\x93O\x0e_g\xe4\xef\xf5\xc8\x97F\xd4f\x11\x1b"\xc29\xbd\xdf\xf6\xce<\x07\xf6H\x90m\x84\x08Csx\xe8|\xc1\xffj\x1c\xbc\xa3\xb6T\xec\xa2\x7fG\x8e\xfd\x1e\xbe\x0c7\xc3\xb9x\xcf\x1a\xfb\xab\xbfx\x98\\\r\xa2q\xdc{\xaa\xa1\x92\xdf\xd0wl\xa9\xd6\xde\xaf\xd9\x12z\xf5k\x9c\xa4\x94\xd8F\xeb\x81r\xfcq\xc43\xa50#\x88)\x0cWJ\x0e\xcah\x8f\x01\xcc\xb5\x12\x83\x04\x85B\x9c\xd1;\x9eF\xb0\xa6\xd1;h\xb8\xdb\xd2j\xa35\x8c\xe3Uo\x94G\xd5q!\xc1\xc1`.\xe6\x0f\x93\r\x08\x19.M\xfa\xd0vvLA\xf0Y\x9d1O\xb1\x01\x8aI=g\xb2P\x8b\xf1O\xa3i~`l\xb5\xfa\xf8m\x15\xca\x04\xf4\xc6\xe7\xdb@\xdb\xc9\x05\x80$\xc1\xb9^U\xa6\x06j\x88\xd5w\x9e\x9aR\xa7\x1a\xf9k\x9c\xe7\x10J#\xa7C\x04_P\xda\xd0\xf9Tp\xad\xe6D\xd8\xb2\x7f\xdf\xee]\xeb\xd0\x80O\'H\x16\x93\x92%tB^\x11\xe1\xdb\xc3\xa1\xa8E\xd9L\x13\xcc\xaa\x19W\xf4P\xe3\x89v\x98\xd2\rN\xa0\x80^33\x9b\x12\x19Y\x8b-\xf5\xf9cg\xe9\xfb\'S\xbazm\x05\x8e\x8c\x05\xd8R\t6\xb7\xf0\x10a\xb5O\x84\xc7\xdc2\xc4\x04\xc2\x07\xab\xf9\xb6\x10W4Cn\x85\xf0]7\xda\xba\xc5\xb5\x0ci&\x1a-\xb56\xe9.\xc7\xe3\x80J\x18u\xa4A\xed\xeb\xa1\xda[\x0cy\x10Si\x10\xe0\xdb\'}Is\xcdE\x98dqG\x82KL\xd0\xa2Y]N\xbc44\x99\x0f\x97\xfb\xa0\x89~\xd6\x1f\xd1\xdc}\x7fJj\xe0\xd4\xfa\xda\xc4_\xe1H\xe0\xb3{\x0ez5y<\x1e\x1asl\xbfP\x1eP\xb4\t1P\xa9"\xd3c\xac\x1d]\'\xc8\xc1\x1dr\x1a~->\xe9\xa6\x11\x1dY\xf4+\xed{X\xf5as\xb21\xe8\xa6C\xa5\xc80\xc3P\x9b\x12\x01IO\xdae\xe6\xde-\xa66p\xe06\x15\xbf!W\xe4J\x89\'\x1f\x92\xf9\xf0\xdaE\xf6$\x9bo\x90\x93\x86G\xcb\xf2\xef\xb4\xb8y\xa3\xe4=7\x99\xa2Q\x8cz\xfc\xd5\xbe\xe9\x87B|\xf7\xb57=\xca\xf0^*\x99?\x89\xed>\x92\xf8\x89\x82\x88\xf2&\x1f?\x8f8\xec\x97kX\xb9\x1a\xa9|\x05\xc2\x9dnr\xfc\x9e\x88d\xef\x05V\xf1KS\xac\xe3\x15\x7fQ@7\xe2U\xceEX\xd2\xee\x03\x94<\x04\x9e\xcc\xb3\xb9\xfc\xc2\xe2PE\x11\xffmd$\x9a\xac\xbe\xe1\xb2J9e&\xcb3\x041\xd3\xc7\xc5\x8a\x98AQR5\x1b7\xf3\x9a\x0e\xea\xacn8G\xd2\xafA\x1c\x0c\xad\xbf\xcd[^`\'\x12\xdc\xa6*\x82\x81\x16,\xda\xc5\xe1@t\xdb\xf1"\\\xfd\x16\x97\x842\xc1\x95\xc7;s\r\xfa\xd2\xcd\x0b\xc9*u\xbdc\xe4#k\x05\xedE\xc3\xef\xa2.\xb2\x11(\xf6\x17$\xee\xbe\xb2\xb2\xbd\xbd\xd2\x1f\xaf\x1e\x97\xc9\xdezf\xcc\x831\xd11\xc3\xb3\xd9\xcf\x03\x0b,Y\x11\xecz\xd4\xa9ZO\xa4\x8f/!\x83\x84\xe9\xa5\x1fW\xd4\xfaHZ.\xf52\xa8\x93\xa5\xd91O\t\xa6\x9b\x8b\x04%I\xda(\xc5T\xaa]\xaaF\xbb\x8b\xbf\x86t\x80\xa5\x91\xd6:\xa8-\xbc_u\xca\xe6\xa9\xa4\xa8\x9d\xbe\x1es{\x13\xb2\xc4[i\xa2\xaa\xd2">k\xd2>\'O\x95\xcbF\r\x17\xbf\xeb\x99\xfak;]\x97gF\xf1\xa7\xfa\xcd\xc1\xf5\x9fzv\xc1\xcb\x00\xfc\xd3\xa0\xdd\xbe[\x13\xa5#\xd4n\x85v\x1fS\xcb\xc7if9+\xf0\xf6sE\xbe\x13\xb4\xb5\x8fS\x9c>W\xbc\xb0\xc3\x13\x05D\xc3\x1a\xd4\xebqv\x84\n\xba0Z\t"\x08e\xf0\xa3\x8a\x06\x03\xc8 \x13\x85\xb4\xe3\xa2TE{\xea\xe5j\xa1 \x07X\xb2wqc\x92\xcf\x9c\xfe__\xa3P\x9c%+\x0f\x8f\xfds\xf8\xec\x17\xb6\x99\xc4\xc7\x895K\x82\x96\xb2dr2\xdcmdq\xec\xa6\x0b\xc8[5|\xe8M\xfe[\xca>\xe9\x9b_XMt7\xbe\xde\xec\xc9s\x82Y\x05\xe0oo\xe8\xb5hT**\x06\x02\xe0\xbf\x9b\xeb\xca\xe7^`&/\xbft!x\xce\xbc\x1f\x8a\xcer\x0c_\x7f\x8e\x86\x7f\xac\x87\xbe\x14\xfa\xa0\xa7\xd2\\\x88\x9a\xeb\x14\xfd\x14\x04\x96F)p\x93kI\xd2\x92}\xe3\x90\x8e\x19\x1e\xd4\x83q\xefe\xa9)H\xa1\xdcB\x9as\x12\xb3r!\xce\x8e\x82\xa2\x12\xc6\x8dw\x1fW\x18\x93\xc7x\x10\xd4v\xbd\xc7\xcd\xc7\x8d\x8f\xef\xa4\x99`\xd7T+\xd85\x14GA\xd0U\x14\xb7\xd6\x04\xca\xe0\xd1\xba\trtW&\xb5!J\xe7\x7f\xb0N\x1f\x99\xd9\xb6\x1b\xf8\x8c\xa5\xd6k\xaf\xbb\'\xbe\x159\xea\x94\x98=\x84.\x1a\x92\xc4\xc5[\xbb1&\xa9\xa3\xf1\xea\xc8u\xf3j\'6\xb7\xaf\xeb\xcd\xe3\x17\xe0eioX\xce\xc1XX:\xb6\xc9soO@S\xad\xe8i\xbc\x05\xdf/\xd3"\xf9H\x87\xfd\xeaQAt\xbe\xa2\xc8\x14_\xe2\xcf\xd0\x99E=\xf4\x1b\xc0&\x86\xeb\xcf\xbfJ4\xca\xfav;c~U\xf6[%>\xa7\xad:V\xccf\xf6\xe8\x97A\x01N\xd80\xf2\xce\xebW`k\x1d\x8f\xcf\xee\xd3f\x9b\x07n\xa5\xf0\xbf\xe5v\x0f\xc8\xd0\xad\x8e\x0b\xfb\x81\xc1\x1c\x84#\xee0\x01\xd4\xabFD\x15\x10\xbb\xb2\xd8\xe1[\x04"\x05o\xd2\x81\xf1<\xf2\xddkv\xe5T\xe6\xd6I\x0f!\xb8\xfcp\x83\x05)`HA\xaf\x9e\xddB\x0e\xb7\xad\xdc\xfe\xb4"\xcf\xbc!\xd0!*\xfc\xb0\xb9\xa3\xb7\xf8\x88\x9cf\x8e\xc3o\x9c\xd4b\x8b\x99\xefJ3\xcc4\xc8\x84\x8e\xfe]$\x8c\xdeT\xe1{a\xf7v\xfagLw<\x16\x03\x95\x87s\x0b\xa4\x918\xa9`%\xcaw\xfby\x86\xeb\xd3\xac \xea\x15\xef\xcd\xa7\xeb\xe5s)|\xb9\xf3\\\xc0\x1b\r\xa2\xe0\xfa8#\x86\x15\xd7h@%\xe1#\x12\xf7\xbeN\x97\xa7\x1f\xfd\x81\x92\x89_\xb5\xc4}\x99\xf9P\xddG*\xb8\x84\x15\x03)\xccP\xd6\x17\xa8C@\xc9\xbb\x12]\xdb\xce\x94\xc5|\xa4\x8b\x80\xd6\x13?\x8e\xd64\xd8\x1e$A\xd3\xfa\x05oSH\xa8c.\xec\xe3\x82rA&nZM\xd9;-\xd1\xc5\x1e\x8a(\xb1\xac5\x1c\x96[,M\x97\xd3[9\xe8\x08ub\xa40\xab\x8d\x9ea\xd1t)>\x9a\xc7\x91\xbc\xa0Z\x8b\x1f\x97p\xe8ww\xc4Z\xf3\xe4\xc2\xceY\xfb\xcb=\x88\x07V\xc5\xf5\xe7H\'\xb8\xb8\x97H\xfc\x87\x8aZ\xa2\x1d\xe0\n_\x89\xb9\x11\xda\r1\xfan\xca\x0e2A\xcf\xa6\xda\x1e?\x12x\xe29\xcd;\x0bG>5\x9a\x1cd\xb2\x8f\xe1\tq\x15\xe1\xea\xda\x13\x92Y\x0f\x9c\xfb)\x02)\tJ\xbf\x90^\x8e-\xf5\xc0\xfd&\x1c\xcf\x05\x81\xf9\x97\x1a4\xd5\x9b\x96/<%\xd5\xfe\x83\x9duH\xce\xfa\xc0\x11\xd3\t\xbbdkt\xd9o\xd6\x10\xa6>\xc4\xebj\x88\xf8\xb1\x97g\x80\xa7\xde\xea\xd5\xab<\xbeu\x8d\r\xac\x84\xf5\x8a\xd0yL[\xe5\x81\xb3q9\x1b\x1e]9V\x96/f.\xfd\x8b\xf3\xe1\xfb\xebRjR\xde#J\x99W\x9au8\x00Z\x87\xcd\x81\xbe\xbe\xa9\xee\xe3}\x9e\xe2\xa6\x11\xd4\x90\xc7\x9a?F\x90\x9c\xfa.\xea\x9f%L\xc3\xc5\xf9\x07\x8c"d\x92\x80B\x1fLOu\xf2\x88z\xd6@\x1f\x974\x17\xa1\xc4IN"\x91\xf5\x8c!e<\x95\xc8A\xc4\x96r+F\n\x9d^\xb0\xe4\xc3\xb5C\x84\xc5\xaf)\xd8\xcd\xc2s8\xc0\x1f\xa2\x98\x0f\\\xe2E\x12\xd6\x18\x92\xfe\xacV\xd4F\x03\xf0\x83\x1a-\x92v\xecl\xef\x08\xec\xebq\xfc\xb95g\x87\x98\xd3\xc5V:\xfd\xe9\x96\xa7\xabUi\x8a\xc5\xf6QMUrT\xc1!\xbb\xd9\x97\xfe\xc0W\xacM\xca3\\\xf8\xbc\x91g\xec\xc8K\xf8\xed7\x16IJ\xb4J\xc3I^\xa5\x8c\x97\x1au\xec\xfa\xb35\xdd\x04e\x1f_\x97YT\xaaV\xc2U\xa7\xc6\x9a\xcc\x9fyY\x9f\xc7\xde4e\xcc\xa3\xc4\xbb\x84\xd0\x9aV\xd4P\x8a\x08\xcd\xf5\xc1\x89\x06\xbbw\xbe%&\xaa\xb7\x1b\x165\xc3\t\xb1\x83\xc7\xe2\xa2?\xfe$\xfca\xfd.\xfa\xdd\xa8\xdf}Du\x04\xeaB\xa4{\x1bzC\x94\x05$KD\x06\xd6u*\n\xcf\xbf>a<\xbfC\xca\xbb.\xed\x009P\xe4P\x96\x97&\xaa\x1a\xcdr\x04\x8f\xec\xd7*\x88\xfa\x08\xfb\xb0\x02\xfd$.&|\xbc\x7f\x0cH\x1a\xf5)\x11\xae\xa7`\x8b\xbdg\x8d\x0c;\xed"\xcd\xd7\xc4\x1co\xf7b\xdf\xaa\xd1\'\xbb8\x83\x91X\r\xe6\xd2\xd7l\x86\xc3\xfe\xa9\xd4|}\xfc\x93\x87\x11\xd2\x99ye\xd8\x12W\xa7\xc8O%\\{/?\x0e\xdfL#H5J\xd6\xc4\x1aq\xf5d\x89\x1e\x85b3\x84\xc8)\x82})\xe5\xbe\xb0\x11-\x0e\x91q\xdf\x90\x93~X\x9f\xc9e@E\xe1\xc4\xca7\x9bZ\xf8V\xe8\x93\xe2{\x879\xcb\xf9w\x08\x83\xb5\xe4*\x9b\xf0\xe2\xb7n\x8f*\x8a\xe4\xca\x80j-\x0b\'PF5\xbb\xcd\xa2\xbd\x11\x8d(\x9d\x82XCT\xd8;*}^9\x076\xe4k{\xea\xaf\xd9PN/\x10z\x99\xcc\x08..\xec\x0f\xf4~J\x82Q\xc6\xb4e\x98\x94\xb4\xc8\xcc\xe9"\xa8$c\x83\x88&\xef(\xa2+Q\xbc(\xd3\xf9\xdc\x87\xf8\xeeG$N\xc2\xfe\xc6@%\x97\x10\xcb\n\xb9\x87\x99$k\xab\x0e\xb1<]\x01\x11\x1c\xac\xd5k\x8eT?O\xed\xce]W\x85l\x9c\xc3\x03\xec]\xf4\xd1\xda\x85z\xf7u\xe01\xc9\x99.I\xfa\xadW\x08\x91*OQ8\xc6\x85\xc9\xa03\r\x93##DpuL#t\xdf\n]\xfc>\x1f\xfez\x9e\xcc\xab\xff\xe4u\xb8\xe7+\x81\xe0\t\\sg\xfd\xeeeC\x05\x8fe\xfdPtC\xdb\xd1\xf9\xe8\xaf\x16Pz\xd8YGZ\x89)\xc3\xf33\xae\x12[\xf1f\xca\xd8 \xc8ag\x17OB\x12npP\x82\x08\x83\x8af:K1&!c\xbf\xb4<\xb95)\x89\xac.\xb7jr\xdb\x9b\xc2\x89\x97K\xf8\xc3\xdeQY\x1e\xa0W,:\x07+\x85J\x13\xd6@y\xe9\xd6%\x07b\x8f>\xd0\xff\xa1\xb2\xcf\xb0\x82E\xdf\xf2\x88l\x11\xce+7\xc6\x94\xef\xf6\xe6\xf9\xe8\xe9\x06"2O=\x10\x9d\r\xa0\xb5\xdf\x9em7h\xd7n0\x90\x12\xb0~\xd2u!\x1b_\xf5@\x93$\xcd\x1f\xda\x9f>\xe3o|\xa6t\x0c\xc6\x0b\xf8\xb6U\x8b7b\x06)\xa6\xd2\xb4.^\xdb\xe1\x82\xfc\xe8\x07\'\xb5\x0e\xa4T\xaf\xbf\\\x14&\xf7\xbd\x98\xa2\x00\xff\x8d\xae\xff\xc4Q\x80pLSp\xabH\xd5\xb3\x1a\x89\\\xb4\xbb\xf4\xd0\xe9oO\xee\xda\\\x9cW\xe8\nq\x10\xe1\xe6\x141\xfa\xca\x1f\xa5\xa7\xae2\xc0\xb3\xceXk\x94\xf0\x0ey\xa1K\xd9\x05s\x8fSHg\x99\x00\x9a\x8cE\xa2"\xa3\xc32GFM\xb4\xf22\x91g\xdbyQ\xc0\x96\xaf\xca2\x82\xf0\x0e\xdd\x10\xee\xc0\xf7\x1a\xe4\x92\xd9\xdd\xe5rzG\xece\xbd\xc6.\xcc\x88\xa6#\xe6C\xcf\xb2\x9d0\xfc\x9ah\x17[\xe9Jr\xfd\xa1,M\xf4\xc5\xba\x00\xc0\xbeC\xd2\x19\xc4J\x9a\xc4\x9dRz\xf1\xc7f;v\xe5.\xea\xae\ty\xe5]\x8aJ\xea\xc2\xae\x8f\xb6"s\xf5\xe0a\xa99J\xe4MA\xbaG 2\xa8\xa0\xb3\xa6\x82\xa7\xe8\x16K\xda@\xfe\x80\xd7\x18\xf0\xea\x88\x8b\x90W,\n\xe6\xaa[\x89\x95\xe4\xa1IUV\xe7\x9a\xc2k\x9b\x0f\xf5\tgvb\xdf\xafz\xad\x1ei\x94r\x18:9\xed\x10!\x9c\xaa\xad\xcfw=r\x07-\x19\xf1\x82:\xa6\xf4\xb7\xae\x0e\x99\x8c9\r\xa5q\ns\x08g\xc4n\x8c@c\x02\x9d\x8bk\xbe\xb6\'\xc2\xc3\xdf\xf3\xafZy\x94Z\x1a\x97\x08\xb7:\'>\x00\x8ew\xf4u3{hP\x97<E\x0e+B\x9bv\xe4\xcf-\xfdU\x84\xf0\x126G-\x12k\xe1\xbc\xa8\x87\xbf\xeb\xf4\x8c2\x9b\xdd 7\xd5\xe1L@c\x94\x0bU\xde\xac\x82\xf5\x92\x02)\xe5(\x17\x0fzx\x1e_h\xb7\x1c\xe7\xf6\xe0"Ab\xa5\xadCU\x05C:p)tm$g\x99\xe5\x12\x84e\xa0\x1dX>E\xad\x14\xe7\x93H\xa1\x9bz\xbd\'^m\xb5\xe9\xce\x18o\x1c\xf6r]S\xe9\x91\xb9\xe2)\xf6^>\xa0\x8b\xe3\xa8x\xde=? \x84X\xb6\x10\xd42M\xbd\xc1\xfa\x1b\xc1\x08-\xe5l#\xdc\xf3\x19bpww\x01\x11\x06@\xd2\xd23/\x80]0\xad\xd8@V0_8\x11;\xa3\xe7$\xe17[W\xb9W&\xcc\x10\x08\xb8G\r\x91\xc1J\xe6/\x9a\xd8\xd7\xb8\xb3\x125c\xed<\xd1O:\xe0\xc1L\x92\xf9\xb7\x92\xe9y\xd9\x95l6\x89\x8f\x8c\x82\'~\xc0\xd6KU@v\xed+\xa7\xa1\xcc\x05\xd4(!T\xc2/\xb8\xaeyii\xcb\xfa\xe68\xe6g<\x92\xa3\xf3e\x0e\xd6[T\xba,\x98,=\xb8\x91\xc7\xdbu\xee\x9aF0*.\x1awd_h2I\x92\x98\xc0\x8c\x8b,Os\x89\x90\xc5\r\x81\xbe\tS{\x90\xf4.$\xba\x16&\x19\xac4\xfe\xe4\x99A\x1c\xe5\x1f\x9a\xfe\xb0@\xe0\xb03$\xb1!\xd0\xcb\x0f\xe8\x05\xbd\x0f\x8c\xbd\x08\x02\rN\x11\xb6\x17\xbd\x0e\xe3\xf0\x97\x0e,\xcd\xf5d\xd3U\xfd"\xe3\x1db\x1f}\xbe\xf6\xcb#(\xbc\x12\xd9\x91Um[\x1b?\xd4\xd0\x8a\x81\xcb(\xcf}\xe4s\r\xa8\xfb\xcb8\x02\xd7]\x1a\xb3\xdbHV\t\x1e94\x12i<\xb6\xcd\x9a`\xb3\x9e\xc3y0\xc6`\xc2\xbe\x1eU0k\x15\xe6ML\x04\x1f\xa2K\xa1\xd8$\x02(\xcc\xf2m"\\\x1e\x08\xe8\xeeb\x85Z\x0c\xc8\xd5q\x9bY\x81\xe4\xb8\x19\xaa\xcdl\x03A\x1e\x84\xa7\x99\xbf\xd4k-\xc8I\xaa\x89\xbb\xd4\xd3\xb4Tm\xe1r\xb3b\xa0\xe4\xa7:f\xa1t\x8a\x0f\x85a\xfa\xae}-<\x86\x87-Y^\x07w\x90\x1c\x84\xb0:\xaeKt\x02\xce\xc4e\xb4\x19O\x11\x8av\xeb\x9c\x9f:v-@\x10\xd1\x98`\x87a\xd0+\x97%\x118\xc7#>L\xd2\xa6\xb3\xfcF?%\xe6P \xb2k3\xc3\xffM\xfd<\x814\xc2K\xe8L\xf6\x89\xbfq\x153\x07\x17\x15\x06\xceIM\x91\x08?H\x88Z\x15\xdd\x10Y\xee\x95\xd0\xca\xfcTG\\`\x18\xfah\x92\x93\x99\xfd]$\x1b\xef*\x96\xd1\xc4}\xef5!\x80\xeb\x90\xbe\x02%\xfd\xce\xe4\xa6l\x1b\xe8\x87\xe7\xea\xfa$\xce\x99W\xf0\xc0\x9a3+\x1cX\xcco\xc0O\x95  \xb1\xd7\x04x\x04b\xb5\x03v\xd5|?\x97\x8e\x8e\'\x88,\\b\xdc\x12\xdcf!7\x81\xff\xe2\x14\xffsoT\xc2\xc5U\x97\x87n\x98\x95\x87\x14\xfd\xd3\xeb\xd4\x1f>\x82\xd5P\x7f\xe6\xe3Z\xf1\xf6\x92+\x94\xf2z$\x15\xb4\xb6`~\xf9\xd1|\xa3"WO\xd15\x00\xab|\x9be\x03\xff\xb5)\x90W\x07\x98i\xa6\x8b\xa1\xc5\x1b\xf5u\xabh\xd2a\xa9\xee\x10\x8a_\xf5\xf7z\x18X\xa2\xa8c\xce\xc6C\xc5Jx60\x11\x8d\x9c\xc2\x0e\x04\x1b\xc2\xea\xa0\x9e\xefzvbH\x8bh\xab\xdd\xc7\x8d\x88X\xbb\xbb\x0c|\x03q<\x17\x93\xbd\xe7Ipa\x10\xe1B\xf4$x\xfb\xae\xac\x18\t\xc3\n\xe9\x0f\xfe\x91q&\xbeJ\x04\xd7>?\x83\xd4J\x9c\xda\x11n\xca&\xf0\x87*\xedb\xba\xf9\xeb^\x84\xef#*\xd6F\xb3-\xfak\xc0\x08\xab\xba\'R\xb7\x935\xf4#^~\xa0\xe9#\x05\xb7\x0c\x8b\xff\xe2~C\x9erS\xaa]T\xb1by\x97\x8c\xd4\x8c=\tD\xd4s\xb4\xeb\xee\xc2c\x9a\xfe\xb4\xdf\xa8[\x82\x16H\xa8:\xb8\xa2\xaa\xae\x99\xdb\x94q\x1eR\x82$$>9Qx\x87S\xba\xf5:\xd4\xe4\xfd\xef\x18\xff\xbdm\xd1\xaa{\xb5?\x95\x8d\xceI\xc1l\xd5\xa4\x880J\xde\xcc4\x0f.\xa2\xde 5\xb2\x1cR\xdfM\x04R)\x84Sm\xf0\x18\x89\xdb\xebZ\xab\x875\xd8^\x95\xe7#\xa9\xd8\xf2\x89+\x861\xceZ\xfdw\xab\xac\x8e\x07\x97\xdak\xec\x0fq\xcf\x1el\xaa\x07\x17I\x81g\xed\x11\xea\xfa\xcb\xf2\xb6\xf4\xcb4\xef\xff\x10\xd8V\r\xc6\x8bg\n\\-n\xbc\xe5\xdfz\rl\x1e2-;tJ\x9d\xe3\x16\xe5^\x7f\x8a\xee\x8d\x8b\x81v\xe4M\xd0\xcd\x90:\xa5^\x12(\xd47\xd7[\xf5ak\x83\x0c\xe0(\x1dcC\x05z51*\xd2\'\x9e\xc1\x80=\xa6B/\xe7\xa1t\x84,\xf8us\xe8kz\x0b8W\xb6\xd2\x9c\x0890\xe5\x85#}\xe8\x89w\x04\\\x1b\x03\xed>\xb1\xe2\xd3\xc6\xe1\xe8\xbe\xa1\xd9`\xb0\xb4n\xf0j]\xf3\xd8\x14j\xa0\x89:\x04\xd9\x19\r\xb5p*\xb6\x8fL\xf0\xb5\x8e\xb4\r\xdd&\xd7B\xd3~\x87\x010\x16/\xc43\x8b\xbc\xf3\xa7o^V7\x839\xeb\xb4\x8d\xa1!N\xa6\xa1\x8a\xfd@T\xd1F)\x8b\xf7\x8e\x05\xc99\x10:\xc7\xf5\x85\x8b~\xa2m\xa5\x83jM\xff\x1a)\xe7\x9b\x14K\xd3\x0e\xb1\x05\xea\xcb \xce\xde\xfb\xd2\x9a\x04r\xfe\xa8\xf7\xc3.\x9d8\xe4\xe3"\xdf\xd3\t\xa0\xb2\x19\x897[\xbb;\x88\xf8\x08\x1d=\xa7\x07m\xd0\x0e\xf9\xc4\x18\x07\x042y\x05>\x95\xd6\xcen\xe1K\xa4)`a\xff\xd4t\x14\xc7\xa5\xa2:dG\xf5\xbe\x19\xca`\xba\x14a\xab\xa8\x98\xf4\xa2\xc14\xd7x\x82\t\xd3\xf4I\x94#\xa0\x847E\x89\xe0s>z\xc4\xf15\x99\x82V,\xc9\x8c\xf9V}HRy\xb3~\t\xc7\xc6\x84\x12b\xa5\xd1:\xe3\x81\xe6\xad\xa1\x7fI\x9d\x0e\x17\x9a\xebx\x10\x90F\t\xb3\x1aF\x11\xca\xc6\xa2M\x89\x85\xe5^TX\x90\xffp\x1b\xafK`\xd8\xf3\x9c~\r\xb3\x91\x055\rC\xb7\x95\x05e\x13k\x87v\x0e\x0f\xea\x11\x0f\x1c\xe7\x10@\xd6\xac\xf2\xf7\x9d\xe5\x90<A\xe1* AF\xb8X\x9f{\x05\xe8u\t\xa9J\x07\x11\xf3~\xa2\x81!\xb5D\xb4\xf1\xda\xf71\xdd\x92\x81q\xf4\x1e\xea\xbf\xe6\x08+\x10!A\x11\x8c&\x14u\x02\xcfY\xae\t\xb0\xd7\x84\x02\x08\xbe\xd9\xb2^dm\xdb\x9dsw\xc6\xc6Jk\xd1\xdc\x14!\xbe\xbe\xb5\x9eK\xca\xc3\xbf5\x9e\x08ATRU\xef,\xa3\xcd:.\x8c%\\\xf6\xc7Y\x0e\x15yP\x9f\xb8\x19\xea\x8a\xaee\x03\x0eH\xb8\xe9\xfb\xcf:\xb0\xdb\x14\xe2\xce\xb4x@\xd3\xe3(V7\\\x95W\xaa\x15~\x98\x0f\xaf\xd9\x94\x9eQt\xd0.O!\x08\x0bXar\x18\x87\x95*Db=\xba*/|*|LW9\xc1\x19\x82\x99\xb9b\xd92\xfc\xe8{Y\xf0\x0b\xa0\x0bZ5\r\xf6F\x97mo\x16\r\xf6\xc5\xb5H\x0f\xc1\r\xfaM<}t42\xa76)\xcb"\xc2tp\x1d\x0f\xb7\xf4\xdc\xf7\xd6\x1bp\xfa\xc6wM\xb4\xec\x02\xe9\xa6_\x90Q\r\xa4@Qk\x1f\x04\xba;\xc2s\xb0\xe5cG\xf4/z\xe4\xb7\xefI\x9bR&\x9a>\rv\xc4\xeb \x87BM1?W\xcc\xad1\xa4\xba\x93\xac\xac\x07\xa5&\xfa,U\x01^\xf8}\xe7\x83i\x91\xd3TH\xca\xc3\xf2\x18\xf1\nS\xfbc\xa3\x83\xd6\x92)\xc6\x01g\xb8o\x13\xa6\x86\xac\xaeC8\xa7=\x86E\xca\xa3\xd4m\xba\xf1(\x87\x01?8\x0f$\xa9\xfaC_j#\xfb\xe4\x1e\xd9\xe5\xc1Y\xa7]\x19Jn\xe9\xbf\xdcT\x02\xde1[>\xde\xf6\x8e7kw\x12c3\xaf6\xdc\xf2\xfa\xeb\x01\x08\xc8\x01\xa1\x92\x1d\xf0!b3~W\xbf\xad\xe0\xf2\xc1\xd60\xff\x9e\xf1\x8cH9\xaey\xb2\x95\x07\xfcF\xadJ\xe1\xf9\xca\\\'&A\xd5\xc0`4C/\\\x82\xde\xeaa\xff&\t\xdd\x98}"rYO\xab\x94\xa4X\x02\x7f\x7f\x15\xd39\xc4\xf7\xb0\xdf\xa6\x12\xfb\x06>!\xfd\x1c\xb1o\xf2`\xd9\x1d\ru|\xfbm\xce\x9e\xdf\t7\xc5\xd6\x82\x01\x15\x10\xb1#\x84\xfd\xd7\xbd\xe2X0\x11*\x0c\r\xfb\xb3\xbe\xfb\x04\x906\x8a,X\xb0\x81\x88\xf6\x86\xc1\xf1\xda\xaf\x92\x89\xd8i\x17\xeb\xdbX"\xf6#\x93\x0f\xd8`\xe1\x15K\xb4[\x98\x93\xbcMT\xa86f\xba\x97\x98\x00\xbe6[\x14\x8e\xf0\xea\xf4\xd1\xc3\rb\x17\x1b\xd4\x97\xe0\xc2Cb\x1c;\xd7\xa9\xe7#EO\x16\xf4\xe1\xb9\xe7\xfb\x0c\xb6\xa5\xc6\xe0\x92\x883_\xb6\x9f@E\x03\xc1\x8b\xe2\xa9\x98\xa4\xc2\xd2]B\xa4\x14\xf0~{{\x9d9\xf7\x07\x0f\xb7\x9d\x8e\xdc`\x9c\x1c\xc6\xf8\x8b\xe6P\xc8\x93\xf2 \x14$\x1d\x80\xc4\xe4/\'\x9cH\x9f\xae2\xf2\xdd\xe3\xa6\x8c\x8f\'\xedw\xe0\xb0\xacQ\x05\xf5K\x0f\x14NJ\xcd4daq\x9c+\xbfN\x10\x81\x88u\xff~\xc7\xb9\xf1el\xd8\xc0\x9cX\x9d\x88h\xc8\x16MW\x176My\x07\x9c~\x0c\xf2;\x1b.\xf9:\xe7<5.\\\x87\xfe\xf5%\x96Zu\x14\x8c\x8f\x18\xf5\x9e\x8bis\xda-2\xe4Q\xb0\x18\x14\xa5U\xc1\x87\xb4\xbc\\s\xa5Zm-\x8f@\r\xf2\xdb\xc6t\xb7x\x0eM\xe7G\x94\xc7\xe4\xedI\xbb\x0ejPh\xf6\x06\xb7\n\xe91\xce\x81\x05l\xd0\xccV\xd47p`\x031\x99[\x86<\xa3\x9ab\x9d\x1f\xc2\xc6\xfb2\x11\xb8o\xc4\x1f$\xea\xc8\rj\x9dAsT\x0b\x80\x014\x8c\x01Z\xdf\xd4$\xf3kc\xaa1\x18t\x95\xab\x06\x10\x86\xe6\xb4\xd7\x1ds7\xa3}\x12\xc7v\xc5\xfa\x9eu\xbe\xef\xed\x1a^vzI\xc9\xdc;\x12d4q\xaa\x07\xa3W\xbf\x8dYP\xbd\xbcQW\xb5\xcd\xe6\'\x85H\xc9\x81\x14c\x07a\xe7\xb7e]\x16v\xf0\xc4\xa0?h#W\xd8\xc7t_*,\x10\xf2d\x16\toV`\xb7l\xd2\xe5\xbc\xfe\xce\xda\xb9\x0fZ-V\x8c\xe1v\xc2\xff\x85K\x8aRw\x91\xbf\xf7\xb93YG\xedG\xaf\x1c\xa83\x04W-c9\x80\x03\x9cU\x84\xa9\x98T\xbc\x16\xe6\xca\xcc1\x9brs\xd1\xa2\xa3#?\x16\xbe\xa3\xc9\x90\xc3\xee\t\xa2\x03sJ\'\xd3@\xf5\'\x93\xae\x1f(t}W|zi\xf6\x88y\xd1`\xd3j\xeb:\x92\xa9\xf59\xbb\xd3F\xb4\xf5\xa9\xc1\xea\x1e\xb9\xbe\xbeN\x0f\xfcN\r\x9f\xe9O^\xe7s\xa97}\xe9-\x13IQ_@:?\x84\r\xcdfa\x86,9 6\xc5^\xe3\xcbt\xbb\xb6f\x198t\xf1\xf8\xd6I\xf3{nl ~p\xa0=\x0f\xc9%\xef\x9a\xc1,]\x16m\x04\x90\xa3=\xd3\xc4\x83SSt\xbd\x89\x8b+W\x17\xee\x17\x9cm\x99\xeblp\xa6\xc6\x00\xdd\x92\r\xc7\xb0\xb0a\x98\xb0dmi\xde\xfa\xa5]\x12g\x99/NC\xf7\xd8\xea\xd96\x0e\x16-IE2\xac$\x93\xcc\x1c\xd4M\xaf\x8f\x11\xe2\xf0\x94\xf3\x9d\x18\xce\x9a\xf3tL\x97\xfa\xce\xa8\xbe\xb8\x95\x17Jp 1&\xba\xdc]\xb0\xff\xaf\x7f\xf0f\xe7\xe9\x1ct\x95\xc0\xdf\x15\x9fT\x13\x1c\x94\xd9\n\xf8O\xd8X\x9b\x8ab\xa7\x19G\x0e\xd8\xd6\x05\x85\xfa\x85\xf5\xb5f\xf2\xdd\x11\x9c\xc8\x8c.\xc1\xa4L\x8d\xdc-*8\xbd*\n\x84\xa9\x82\xcfj\xf8<\xa8\xda)R{_tAL$\xcf5~\xa3\x96\xf1s\xc3\xc1\xfd\xc5\xb0wun\x1b9N\xfc\xb5B\xf4\x95\xb2\xc0\xb8\xd3\x11q+\xaa\xca\xe6\x9b8\x08\xdb\xa3@h\xb0\xce\x17W\xbf\xc4\xa7\xdcl\xbbG\xb2xd\x12,;\x02T\x9fy\xc5\x98\xbeC\x97\xc0\x0c\x16\x06\xa3\xc7E\x88\x13y\xd8!\x98$\xca\xf2\xeffE\xb8r\xb81up]\x96\xbaF\xa3\x1b\xa3\xd7_^\xb2\xe7\x103\xdb\x8e\x0c\xd1\xdbW,2w\xd9+h\xe6\xce\x1a1,Vlu\x02&\xc8;\xeb\xe19>\x03\xf0L\xe40d\xbf\x16Vu\xcf\xa87\x90"\xe0\xd0\xc2&h\x86\x14\x8bK1z\xc3\x8f\x85\xbb;\xda\xe4\x02\xe77\x8d\x90\xd2\x9b\xbc\x1c\x9b\xa4\xfe"%\x99(\xac\x841Nd\x16\xb2)\x84\x05R\x95I\x99\x14\xe4\xf1\xae\xd2v}\xdf\x83\xc5M\xed\xc0\xe4\x86\xbc\xa1\xe1\x7f\xf6\xc3h\xa2\x8d6n\x94}yX\xea\x16\x0b\x86\xf1\xcb\r{\xdc\xc3\x93\xb1\x8e\x17\xfeI\xd0\xb0\x1d\nyD[4\x99\xc8i\xbd\xc8&;\x849\x068\xa8G\xf1\x8d\xc98N7\xb6\x07\x15|E-\x10\xa3\xff\xcd\xa9w\x17\xeb,\x01\xb9tOTPX6\xe3(\xect\xb1\x13Ci\xbb\xd9\x84\x9d\xc0\x91\xaf\x9c\xd3 )t\x1d\x17\x9d\xe6\\\xe2\xd7\xc9\x04S\xf1\x9b\x86,\xe4\rng<!J\x91\xf0A\x81\xcb}_\xa4\xfa\x04\x9c\xd6\xd2\xbe^\xccG\x82z\x8c\x81\xfd(\x04U\xef\x07\x989`\xf9<\x17\xdfS\xad\xf0*L\xef-\xa3\xb3\xd2\x07\x84\xef\x0cP\x03\x7fpT\n\xc9\xae\xe1gaI\x9c\xceYHh\xf0\xca\xf9\xc6\xf9.\x88\t\x83\xe6\xadM\xb5e\x82\xb6\xe7{f\xd6\x02\x8f\xd9_1\xe1\xb5\x14`{D\xf9\xd0\x189\xc5\x95\xfdO\xfd\x91\xd4\x13U\x18\x8b\xe2\xbcN\xe9\xf2\x07\xff\xae\xf3\xe9\xaf\xf8j<\xfe\x81;\xfc\xc6\xfa\xf2W\xea\xb8\xc0\xbfW\x96\x02\xf7\xc8\x80\xf6\xcb\xba\xb5\xc4\xedRB\xc7J-\xffw\xa0V?\xa0W\x9bS\x0b:\xebvP\xed\x9e\xdc\xaf\x8c\x9f2\xc5x\xc9\x9bD\xbdA\xfbtj\xa6K\x17\x04\xe0\xe3\xaf+\xfaY|\xe6\xc04\x02\xe4\xf7)\'\xdbX`\xd0\n\xb4\xd9\xef\x17%,>\xbbX\xd1\xac\\\xb8\x19+\xd3\xfe\x1d,3\xf8\xbd\x8b\xa0\xb5\x0e\x9et\x9f\xe2\nW\xa23\xeeE\x89Y\xf9N\xb3=A\xee3\x89Y\xfd\x97Y2b\xa7\x02\x912\x1d\xed\x13\xeaK\xfe\xdd\x8d\xde\x1f\xfa\xace\x06\xe2\x12+~\xf7\x95\x9a\'V9\x8d\xfa\x15\xbao\xf6]xK\xe7A^\x95\x88sf!<8B\xed\x0f\xee\xf6%\xbd\x99JT\x1b\x0b\r\xa4&]\xa9\xa1*X\xdc\xe7\xae\rK\xc1\xf2-8\xe7I\x9e\x0b\t3kd~\xe1\xdfb\xe7\xd2\xbf\xc8#\xb1\xda~\xa7\xc2\xc7\x92*\xa8\xff\x80f\x17&\xc4#\xa2D\xf4b\x84k\xde\xb9DjG\xffx\xf1v\x0c3\x9a\x87"\x89Ut\xa2Y\x16\x1a0\x99\'\xe1\xb6\xd2\x1by\x8b9yBi\xba\xa6:X<\x88r7\xcf\xf1\xb9\xff\xf5D\xed\x95~\x17\x85\xc3\x88\x97\xb9\x07a\x02\x8e\xa9B\x82\xd5\xc6nL\x80h\xc1R\xc5\x80\xf1\xdd\x98\x84\x9e\xe8\xbcC\xb3\x8f\x00+\xbc\xa4\xd4\xb2\xc2f\x99]h\x9f\x92A>\xa8%%\xb3[\xa2\x8cy z\xbb`\xc6\xc2\x88W\xee\x83GXN65\xe2\xc6\x89!\x18.\xc9\x19c\xf7jE\xcc\xf3w\xfb\x02\xe4+7\x9aU\xda1n$\xee\xc2\x80W\x83\xc0\xdc+N{c\xbe\xd2\xd4\xda\xaf\xab\x0cG\x98\xd6Fm\xe3\xbb\x18\x0f\xa8\xb9B\xc2\xfa\x82\x1a\xe1|\x96\'\x10\x8e\x00}\xe5\x8f\x10}\xc6\xc7\x8f(\xb3\x98\xe8\x19`\xce\xe0\xbby\xf2B\xe9\\\xe7=\x83\x82\xcf\xe9\r\xe4\x9f\x86cj\xe9A\x1c2\x91\x8e\x88\xb1\x83\x07\xde\x99X\x0b\x8f\xe0\xed\xc6\xe4\xcaS\x97\x9fVW[\xf8nT\xfa;\x1f\x16\xd3\x95\xa4\x08p\xdc\xcd\x13Z\x02\x06\xe0_\x1aEd\xddm\x07\xf5zb\x1f\xae\xf2<\xea\x9d\x01\x14\xa1\x8e\xf2y?\xbbR1 \x82U\x88Y\xc7\x16o\xa9~7\xd1\xc8D\xba#\x1d\xbd\xb0jKd\xd3(\x11\x10\xd2d\x93Na\xfc\xb43\xc5\xbe\x13\xa5\xb4\x87\xfdl\x9a\xf8\xa6\x97\x1eG\xa0\x90\xa1\xeb\x9f\xe8\xac\x02\xa7\xe5]\x83\xc8a|[\x9e\x04\xd0[\x89\x08\xc8:\x1dp{\x81U,\xf7\x0e\xf3q\xd9\xa0\xac\x90&t\xd4,X\x96W\xb6X\xba\xbcK\x91(\xf4\xe6(\xc8\xb1+\xe5\xf6\rX\x9e`\xb2\x04\xbbRL\xe9T\xf1\xb1[\x01\xde\xa0\xd7C\xf3\x1a\xa2\x0f\xf0\xa2\xbd\xad\xa3\xebz\x9b\x84\xef@IY\x90\x8fEuO\xfc\xbc\x96#\x01\xbdF\xa8\xc4\x92\x99\'\x85Z\xd8\x99\xef\xf0\xef\xfcA4\xbb\xc3\xbe\xa9\xda\xba%\xed\\M+xp\xb3\xd6\xb5%\x1e\xb6g\xc8,H\xb1\xbe\x1f\xaf\xb8V\x98\'h:\x16\xf8\xfc\x91\xa9\xb9[\xaa\xf7s)r\xa7\xfd\xe1\xa5\xc2\r\x9f40\r\xbeJ)\xd3\xe5\xf2H\xa0\x9c3\xf1\xbe\xb5*V uO\x0e\x18]\xd8$\x1de\x07\x88s}\x9eB\xbf\x8d\xb8\n\x10n3\xfem\xd1\x90.\xc5\x8fd\xf1\xa8N\xe34eH\x19[N\xb0\xe3R\xdc\xe9\xe3\xdf\xb8l\xfc\x97c\x9e\xce,\xd6\xb8\xf1AW\n\x0c\xc5Dr-;\xe3\xf1e\x82ES\xaf\x0f\x88\xb4\xf1\x8e\x92kS\xf2\x14\xc10{Q\xa6\xf4K3g\xe3\xd0.\xe9-\x94x\xf8T\xbf\xde;\x8d\xa5Hg\x0c\xdd\x1aE\x9e\'\x10\x85\xd1\xa9\x8eL\xf1p4\xa5\x9c\xee\xe7\xe4<\xa5\x88\x9co\xeb\xd4\xec\x80\xfbf\xf1\xf2\x0ci\x95\xa3\xb9\xe8\xf3\x1c\xfeT\x0cgsu8\xa1\xcb\xc1}\xe4\xa3VP\xf5J\xc1\x1f\x05\xe6$\x8e\xf8Cb\xb5\xf2>j\xe5\x8e\x92b\xd1\xb6\xd5v\xd7\xd9\xf1Q\r\x9f\xf6\xd0s\xf3\xa1\xd4U\xf6t2\xc7r\xe3\xf5\xf0\xd2\x0f@A\xfcd\xcb\xa5@\xffe%DJiA\xa9\xe9\x9d\xc4c\xfe\xa2\xe5\x8f\\\x13"\xe2^\xa3\xf5\xdbd\xb8\xde\x1f&\xe6\x0e\x9c\xb7\x16cZ\x8e\x8d\xe7\xe3\xd1\x89p\xdd\xbc,u\xa5\xd8B\xcc=;\xa2\xb3pQ\xab\xb8c\xe1\rJ!\x0f\x8d\x96Xh=nS\xf3\xf0\x8fKF8\xce\xaa\x9e\x96\xdeQO\x06\x8ba\xb3Q\xf5\xc5?\x1cQm\xe4\x14\'a8\xfa\x0142\x00\\s\x1ceW\x00\xd8\xb4\xc8\xa6?\x18\x80\xb5\x95n\xa8a\xd8\xe2\r\xfc?\x96\x03Hm\x1d:\xb85\x18[#G\'K#\xe0\x1a$\xd0\xd3\xd6h\r\xd2\xc2\xd3\xca~\r\xc2\xd8\x93}\r\xd6\xd8\xea\x97\x91\x93\x89\x95\xd5\x1a\xa4\'\xd0\xcax\r\xd2\xcc\xdd\xccd\r\nhgd\xea\xb4\x06ojfbgk\xefh\xe6\xe4T\x01p\x84\xff\xd7\xee\xbf\xe9\x15^\xc9\x83\xe9\xbb\x8b\x93\x89\x91\xb3\xd9\x1a\xac\x80\xad\x9d\xa9\x0b\xd0L\x08\xec?\xa6\x89\xff\xfc)\xfd_\x1f\x85pA[\xcd\xd4C\xff>\x00\xecBlI\x0c\x00\xa8\x19\xa3\xa5\xfb\xdfU\xf5\x7f\x00\xf0\xe7\xec\xd1y"\x00\x00')))
except KeyboardInterrupt:
	exit()
