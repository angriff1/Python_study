import wx
from userdb import *

# App
sqlitedb = SqliteDb('shopdb.db')
sqlitedb.makeTable()
udb = UserDb('shopdb.db')
userdbSelected = udb.select()

data = []; userListData = []
for u in userdbSelected:
    id, pwd, name, age = u.sqlmap()
    data.append('%s %s %s %d' % (id, pwd, name, age))
    userListData.append('%s %s %d' % (id, name, age))

# UI
app = wx.App()
frame = wx.Frame(None, title = 'Shop Management')
panel1 = wx.Panel(frame)
panel2 = wx.Panel(frame)
panel1.SetBackgroundColour(colour = 'blue')
panel2.SetBackgroundColour(colour = 'green')

textId = wx.TextCtrl(panel1)
textPwd = wx.TextCtrl(panel1)
textName = wx.TextCtrl(panel1)
textAge = wx.TextCtrl(panel1)
textId.SetHint('id')
textPwd.SetHint('pwd')
textName.SetHint('name')
textAge.SetHint('age')
bt = wx.Button(panel1, label = 'ADD')

userList = wx.ListBox(panel2, choices = userListData)
userList.SetBackgroundColour(colour = 'white')
userList.SetSize(wx.Size(180,200))

# List event
def itemselect(event):
    dataCnt = userList.GetSelection()
    wx.MessageBox(data[dataCnt], 'User Information', wx.OK)

userList.Bind(wx.EVT_LISTBOX, itemselect)

# Button event
def onClick(event):
    id = textId.GetValue()
    pwd = textPwd.GetValue()
    name = textName.GetValue()
    age = textAge.GetValue()
    wx.MessageBox(id, 'Alert', wx.OK)

    user = User(id, pwd, name, int(age))
    udb.insert(user)
    data.append(user.sqlmap())
    userList.Append('%s %s %d' % (id, name, age))

    textId.SetValue('')
    textPwd.SetValue('')
    textName.SetValue('')
    textAge.SetValue('')

bt.Bind(wx.EVT_BUTTON, onClick)
box1 = wx.BoxSizer(wx.VERTICAL)
box1.Add(textId)
box1.Add(textPwd)
box1.Add(textName)
box1.Add(textAge)
box1.Add(bt)
panel1.SetSizer(box1)

# Grid
grid = wx.GridSizer(1,2,10,10)
frame.SetSizer(grid)

grid.Add(panel1, 0, wx.EXPAND)
grid.Add(panel2, 1, wx.EXPAND)

frame.Show(True)
app. MainLoop()