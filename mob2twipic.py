# -*- coding: utf-8 -*-
"""
Mob2Twipic, share your pictures in twitter using your s60 based nokia. 
    Copyright (C) 2009  Licio Fonseca

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
 


"""

__scriptname__ = 'Mob2Twitpic'
__version__ = '0.00'
__author__ = 'Licio Fonseca'
__web__ = 'http://www.licio.eti.br/'
__copyright__ = 'Copyright (C) 2009 Licio Fonseca'


import appuifw as gui
import appuifw
import e32
import os


class Mob2Twitpic:

    def get_list_img(self):
	self.filelist = [x.decode('utf-8') for x in os.listdir(IN_PATH) \
				if os.path.isfile(IN_PATH + x.decode('utf-8')) and \
				(os.path.splitext(x.decode('utf-8'))[1][1:3]).lower() == "jp" ]
	if self.filelist == []:
		self.disp_msg(['', '＊＊No JPG File in dir＊＊'],fontsize='normal')
                self.set_dirmenu()
                return

	self.filelist.sort()
	self.filelist.reverse()

	menu_list = [u'file select',u'all files',u'cancel']
	menu = appuifw.selection_list(menu_list)
	if menu == 0:
        	self.index = appuifw.multi_selection_list(choices=self.filelist)
	if not self.index:
		self.refresh()
		return #exit
	elif menu == 1:
		self.index = [x for x in range(len(self.filelist))]
	else:
		self.refresh()
		return #exit

    def disp_msg(self,msg,fontsize='dense'):
	#Copied from http://masaland.cocolog-nifty.com/blog/files/PyMyViewer_000_2.py
		

	self.canvas = appuifw.Canvas()
	self.cwidth,self.cheight = self.canvas.size
	appuifw.app.body = self.canvas
	txt_img = graphics.Image.new((self.cwidth,self.cheight))
	txt_img.rectangle(((0,0),(self.cwidth,self.cheight)),fill=(0,0,0))
	for i in range(len(msg)):
	    py = 36 * (i+1)
	    pt1 = py - 24
	    pt2 = py + 2
	    if msg[i]:
	        txt_img.rectangle(((15,pt1),(345,pt2)),fill=(247,70,70))
	        txt_img.text((50,py), unicode(msg[i]), \
					fill=(255,255,255), font=fontsize)
	self.canvas.blit(txt_img)




    def close(self):
        self.app_lock.signal()

    def about(self):
        gui.note( u"Mob2Twipic: share your pictures in twitter", "info" )

    def lst_cbk(self):
        idx = self.body.current()
        gui.note( u"List cbk %d" % idx, "info" )

    def main(self):
        gui.app.exit_key_handler = self.close
        gui.app.title = u"Mob2Twipic"
        gui.app.menu = [( u"About", self.about ),
                        ( u"Exit", self.close )]

        self.body = gui.Listbox([ u"Demo a", u"Demo b" ], self.lst_cbk )
        gui.app.body = self.body
        self.app_lock = e32.Ao_lock()
        self.app_lock.wait()

if __name__ == "__main__":
    dm = Mob2Twitpic()
    dm.main()
