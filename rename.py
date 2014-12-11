import wx
import os
import libtorrent as bt
import sys

reload(sys)
sys.setdefaultencoding('utf8')


def getname(torrentname):
    info = bt.torrent_info(torrentname)
    name = info.name()
    return name + '.torrent'


if __name__ == '__main__':
    app=wx.App()
    wildcard = 'torrent file(*.torrent)|*.torrent'
    dialog = wx.FileDialog(None , 'Choose Torrent File', os.getcwd(), '', wildcard, wx.OPEN)
    if dialog.ShowModal() == wx.ID_OK:
       filename = dialog.GetPath()
       torrentname = getname(filename)
       newname = os.path.dirname(filename) + '\\' + torrentname
       os.rename(filename, newname)
       
    dialog.Destroy()
