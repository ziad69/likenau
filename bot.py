# -*- coding: utf-8 -*-

import LINETCR
from LINETCR.lib.curve.ttypes import *
from datetime import datetime
import time,random,sys,json,codecs,threading,glob,re,base64

cl = LINETCR.LINE()
cl.login(qr=True)
cl.loginResult()

ki = kk = kc = cl 

print "login success"
reload(sys)
sys.setdefaultencoding('utf-8')
KAC=[cl,ki,kk,kc]
mid = cl.getProfile().mid
Amid = ki.getProfile().mid
Bmid = kk.getProfile().mid
Cmid = kc.getProfile().mid

Bots=[mid,Amid,Bmid,Cmid]
admin=["u6dc040137eac599ca446f80f45bbd93c"]
wait = {
    'contact':True,
    'autoJoin':True,
    'autoCancel':{"on":True,"members":1},
    'leaveRoom':True,
    'timeline':True,
    'autoAdd':True,
    'message':"Thanks for add me, Creator= https://line.me/ti/p/~anaichiro",
    "lang":"JP",
    "comment":"Thanks for add me, Creator= https://line.me/ti/p/~anaichiro",
    "commentOn":False,
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "clock":False,
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "protectionOn":True,
    "atjointicket":False
    }

wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{}
    }

setTime = {}
setTime = wait2['setTime']


def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1

#---------------------------[AutoLike-nya]---------------------------#
def autolike():

			for zx in range(0,20):

				hasil = cl.activity(limit=20)

				if hasil['result']['posts'][zx]['postInfo']['liked'] == False:

					try: 

						cl.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)

						cl.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like By Z i A d line://ti/p/~anaichiro")

						kk.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)

						kk.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"50C:4K Pc AJon :v")

						print "DiLike"

					except:

							pass

				else:

						print "Sudah DiLike"

			time.sleep(500)

thread2 = threading.Thread(target=autolike)

thread2.daemon = True

thread2.start()


#---------------------------[AutoLike-nya]---------------------------#

def NOTIFIED_READ_MESSAGE(op):
    try:
        if op.param1 in wait2['readPoint']:
            Name = cl.getContact(op.param2).displayName
            if Name in wait2['readMember'][op.param1]:
                pass
            else:
                wait2['readMember'][op.param1] += "\n・" + Name
                wait2['ROM'][op.param1][op.param2] = "・" + Name
        else:
            pass
    except:
        pass

#-------------------------[Jangan Dihapus]------------------------#

def bot(op):
    try:
        if op.type == 0:
            return
        if op.type == 5:
            if wait["autoAdd"] == True:
                cl.findAndAddContactsByMid(op.param1)
                if (wait["message"] in [""," ","\n",None]):
                    pass
                else:
                    cl.sendText(op.param1,str(wait["message"]))
        if op.type == 13:
                if op.param3 in mid:
                    if op.param2 in Amid:
                        G = ki.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)

                if op.param3 in Amid:
                    if op.param2 in Bmid:
                        X = kk.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        kk.updateGroup(X)
                        Ti = kk.reissueGroupTicket(op.param1)
                        ki.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        kk.updateGroup(X)
                        Ti = kk.reissueGroupTicket(op.param1)

                if op.param3 in Bmid:
                    if op.param2 in Cmid:
                        X = kc.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        kc.updateGroup(X)
                        Ti = kc.reissueGroupTicket(op.param1)
                        kk.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        kc.updateGroup(X)
                        Ti = kc.reissueGroupTicket(op.param1)

                if op.param3 in Cmid:
                    if op.param2 in mid:
                        X = cl.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        cl.updateGroup(X)
                        Ti = cl.reissueGroupTicket(op.param1)
                        kc.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        cl.updateGroup(X)
                        Ti = cl.reissueGroupTicket(op.param1)

#----------------------[Masukin Semua SC Yang Ente Pengen Disini]----------------------#
        if op.type == 25:
            msg = op.message
            if msg.text in ["Speed","speed"]:
                    start = time.time()
                    elapsed_time = time.time() - start
                    cl.sendText(msg.to, "%sseconds" % (elapsed_time))
		elif msg.text == "$Cek sider":
					if msg.from_ in admin:
						cl.sendText(msg.to, "Siapa Yang Sider ayoo ≧∀≦")
						try:
							del wait2['readPoint'][msg.to]
							del wait2['readMember'][msg.to]
						except:
							pass
						wait2['readPoint'][msg.to] = msg.id
						wait2['readMember'][msg.to] = ""
						wait2['ROM'][msg.to] = {}
						print wait2
            elif msg.text == "$Sider":
				if msg.from_ in admin:
						if msg.to in wait2['readPoint']:
							if wait2["ROM"][msg.to].items() == []:
								chiya = ""
							else:
								chiya = ""
								for rom in wait2["ROM"][msg.to].items():
									print rom
									chiya += rom[1] + "\n"

							cl.sendText(msg.to, "Readed By %s\nthat's it\n\nignored By\n%sIt is abnormal ♪\n\nReading point creation date n time:\n[%s]"  % (wait2['readMember'][msg.to],chiya,setTime[msg.to]))
						else:
							cl.sendText(msg.to, "An already read point has not been set.\n「set」you can send ♪ read point will be created ♪")
				elif msg.text in ["Tagall"]:
					if msg.from_ in admin:
						group = cl.getGroup(msg.to)
						nama = [contact.mid for contact in group.members]
						cb = ""
						cb2 = ""
						strt = int(0)
						akh = int(0)
						for md in nama:
								akh = akh + int(5)	
								cb += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(md)+"},"""

								strt = strt + int(6)
								akh = akh + 1
								cb2 += "@nrik\n"

						cb = (cb[:int(len(cb)-1)])
						msg.contentType = 0
						msg.text = cb2
						msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}

						try:
							kk.sendMessage(msg)
						except Exception as error:
							print error					
						
#----------------------[Masukin Semua SC Yang Ente Pengen Disini]----------------------#

        if op.type == 59:
            print op


    except Exception as error:
        print error


def a2():
    now2 = datetime.now()
    nowT = datetime.strftime(now2,"%M")
    if nowT[14:] in ["10","20","30","40","50","00"]:
        return False
    else:
        return True

while True:
    try:
        Ops = cl.fetchOps(cl.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(cl.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            cl.Poll.rev = max(cl.Poll.rev, Op.revision)
            bot(Op)
            
#-------------------------[Jangan Dihapus]------------------------#            
