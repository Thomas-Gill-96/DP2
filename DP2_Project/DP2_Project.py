from tkinter import *
import InsertItem

#Function Declarations

#Clear Overlay Screen
def Clear_Overlay():
	for x in overlayFrame.winfo_children():
		x.destroy()

#Create an Empty Frame or Spacer
def Create_Empty_Frame(masterFrame, paddingY):
	tempFrame = Frame(
		masterFrame,
		height = paddingY,
		borderwidth = 5,
		relief = "ridge"
		)
	tempFrame.pack_propagate(False)
	tempFrame.pack()

#Generic Title Creation for Overlay Screens
def Title_Label_Creation(titleName):
	tempTitleLabel = Label(
		overlayFrame,
		text = titleName,
		font = subHeadingFont
		)
	tempTitleLabel.pack(fill=BOTH, pady = (30, 10))

#Generates an entry field, along with a label for the entry
def Generate_Text_Entry(masterFrame, labelTitle, anchoredPos, paddingX, paddingY, textBoxLength):
	tempLabel = Label(
		masterFrame,
		text = labelTitle,
		font = buttonFont
		)
	tempEntry = Entry(
		masterFrame,
		width = textBoxLength,
		borderwidth = 2,
		relief = "sunken",
		font = textFont
		)
	tempLabel.pack(anchor = anchoredPos, padx = paddingX, pady = paddingY)
	tempEntry.pack(anchor = anchoredPos, padx = paddingX, pady = paddingY)

def Unlock_Accept_Button():
	for button in subMenuFrame.winfo_children():
		if(button['text'] == "Accept"):
			button['state'] = NORMAL
			break

def Unlock_Cancel_Button():
	for button in subMenuFrame.winfo_children():
		if(button['text'] == "Cancel"):
			button['state'] = NORMAL
			break

def Unlock_Export_Button():
	for button in subMenuFrame.winfo_children():
		if(button['text'] == "Export"):
			button['state'] = NORMAL
			break

def Lock_Sub_Buttons():
	for button in subMenuFrame.winfo_children():
		button['state'] = DISABLED

def Create_Sales_Record_Row(masterFrame, stockName, stockPrice, stockQuanity, totalPrice, paddingX, paddingY):
	
	tempRowFrame2 = Frame(
		masterFrame,
		borderwidth = 3,
		relief = "ridge"
		)
	tempRowFrame2.pack(fill = X)
	
	stockNameFrame = Frame(
		tempRowFrame2,
		borderwidth = 3,
		relief = "ridge",
		height = 20
		)
	stockPriceFrame = Frame(
		tempRowFrame2,
		borderwidth = 3,
		relief = "ridge",
		height = 20
		)
	stockQuanityFrame = Frame(
		tempRowFrame2,
		borderwidth = 3,
		relief = "ridge",
		height = 20
		)
	totalPriceFrame = Frame(
		tempRowFrame2,
		borderwidth = 3,
		relief = "ridge",
		height = 20
		)

	stockNameFrame.pack(side = LEFT, fill = X, expand = 2.5)
	stockPriceFrame.pack(side = LEFT, fill = X, expand = 1.0)
	stockQuanityFrame.pack(side = LEFT, fill = X, expand = 1.0)
	totalPriceFrame.pack(side = LEFT, fill = X, expand = 1.5)

	tempRowFrame = Frame(
		masterFrame,
		borderwidth = 3,
		relief = "ridge"
		)
	tempRowFrame.pack(fill = X)

	stockNameEntry = Entry(
		tempRowFrame,
		width = 1,
		borderwidth = 2,
		relief = "sunken",
		font = textFont
		)
	stockNameEntry.insert(0, stockName)

	stockPriceEntry = Entry(
		tempRowFrame,
		width = 1,
		borderwidth = 2,
		relief = "sunken",
		font = textFont
		)
	stockPriceEntry.insert(0, stockPrice)

	stockQuanityEntry = Entry(
		tempRowFrame,
		width = 1,
		borderwidth = 2,
		relief = "sunken",
		font = textFont
		)
	stockQuanityEntry.insert(0, stockQuanity)

	totalPriceEntry = Entry(
		tempRowFrame,
		width = 1,
		borderwidth = 2,
		relief = "sunken",
		font = textFont
		)
	totalPriceEntry.insert(0, totalPrice)

	stockNameEntry.pack(side = LEFT, fill = X, anchor = W, expand = 2.5, padx = paddingX, pady = paddingY)
	stockPriceEntry.pack(side = LEFT, fill = X, anchor = CENTER, expand = 1.0, padx = paddingX, pady = paddingY)
	stockQuanityEntry.pack(side = LEFT, fill = X, anchor = CENTER, expand = 1.0, padx = paddingX, pady = paddingY)
	totalPriceEntry.pack(side = LEFT, fill = X, anchor = CENTER, expand = 1.5, padx = paddingX, pady = paddingY)

	print("Created a row of entries")

def Create_Sales_Record_List(masterFrame):
	tempMasterFrame = Frame(
		masterFrame,
		borderwidth = 5,
		relief = "ridge"
		)
	tempMasterFrame.pack(fill = X)

	for x in range(0, 4):
		Create_Sales_Record_Row(tempMasterFrame, x, "", x, "", 20, 10)
	overlayElementsMasterFrame = tempMasterFrame
	print("Doing Things")

def Add_Stock_Callback():

	Clear_Overlay()

	Unlock_Accept_Button()
	Unlock_Cancel_Button()

	Title_Label_Creation("Add a Stock Item")
	stockOverlayFrame = Frame(
		overlayFrame,
		width = 480,
		height = 600,
		borderwidth = 5,
		relief = "ridge"
		)
	stockOverlayFrame.pack_propagate(False)
	Generate_Text_Entry(stockOverlayFrame, "Date", CENTER, 5, (5, 5), 10)
	Create_Empty_Frame(stockOverlayFrame, 100)
	Generate_Text_Entry(stockOverlayFrame, "Stock Name", W, 5, (0, 5), 20)
	Create_Empty_Frame(stockOverlayFrame, 20)
	Generate_Text_Entry(stockOverlayFrame, "Stock Price", W, 5, (0, 5), 20)
	stockOverlayFrame.pack()

def Add_Sales_Record_Callback():
	
	Clear_Overlay()
	Lock_Sub_Buttons()
	Unlock_Accept_Button()
	Unlock_Cancel_Button()

	print("Adding a sales record....")
	Title_Label_Creation("Add a Sales Record")
	stockOverlayFrame = Frame(
		overlayFrame,
		width = 480,
		height = 600,
		borderwidth = 5,
		relief = "ridge"
		)
	stockOverlayFrame.pack_propagate(False)
	Generate_Text_Entry(stockOverlayFrame, "Date", CENTER, 5, (5, 5), 10)

	Create_Empty_Frame(stockOverlayFrame, 50)

	#Move to a function later

	#Header Frame
	headerFrame = Frame(
		stockOverlayFrame,
		width = 480,
		height = 10,
		borderwidth = 2,
		relief = "ridge"
		)
	headerFrame.pack(fill = X)
	#expand = True
	#Table Headers
	stockNameLabel = Label(
		headerFrame,
		text = "Stock Name",
		font = buttonFont,
		bg = "white"
		)
	stockPriceLabel = Label(
		headerFrame,
		text = "Price",
		font = buttonFont
		)
	stockQuanityLabel = Label(
		headerFrame,
		text = "Quanity",
		font = buttonFont
		)
	totalPriceLabel = Label(
		headerFrame,
		text = "Total",
		font = buttonFont
		)
	stockNameLabel.pack(side = LEFT, fill = X, anchor = CENTER, expand = 2.5)
	stockPriceLabel.pack(side = LEFT, fill = X, anchor = CENTER, expand = 1.0)
	stockQuanityLabel.pack(side = LEFT, fill = X, anchor = CENTER, expand = 1.0)
	totalPriceLabel.pack(side = LEFT, fill = X, anchor = CENTER, expand = 1.5)

	#List Stuff
	Create_Sales_Record_List(stockOverlayFrame)

	stockOverlayFrame.pack()

def Edit_Sales_Record_Callback():
	
	Clear_Overlay()
	Lock_Sub_Buttons()
	Unlock_Accept_Button()
	Unlock_Cancel_Button()

	print("Editing a sales record....")
	Title_Label_Creation("Edit a Sales Record")
	stockOverlayFrame = Frame(
		overlayFrame,
		width = 480,
		height = 600,
		borderwidth = 5,
		relief = "ridge"
		)
	stockOverlayFrame.pack_propagate(False)
	Generate_Text_Entry(stockOverlayFrame, "Date", CENTER, 5, (5, 5), 10)
	stockOverlayFrame.pack()

def Display_Sales_Record_Callback():
	
	Clear_Overlay()
	Lock_Sub_Buttons()
	Unlock_Accept_Button()
	Unlock_Cancel_Button()
	Unlock_Export_Button()

	print("Displaying a sales record....")
	Title_Label_Creation("Sales Record")
	stockOverlayFrame = Frame(
		overlayFrame,
		width = 480,
		height = 600,
		borderwidth = 5,
		relief = "ridge"
		)
	stockOverlayFrame.pack_propagate(False)
	Generate_Text_Entry(stockOverlayFrame, "Date", CENTER, 5, (5, 5), 10)
	stockOverlayFrame.pack()

def Generate_Sales_Report_Callback():
	
	Clear_Overlay()
	Lock_Sub_Buttons()
	Unlock_Accept_Button()
	Unlock_Cancel_Button()
	Unlock_Export_Button()

	print("Generating Sales Report....")
	Title_Label_Creation("Sales Report")
	stockOverlayFrame = Frame(
		overlayFrame,
		width = 480,
		height = 600,
		borderwidth = 5,
		relief = "ridge"
		)
	stockOverlayFrame.pack_propagate(False)
	Generate_Text_Entry(stockOverlayFrame, "Date", CENTER, 5, (5, 5), 10)
	stockOverlayFrame.pack()

def Accept_Button_Callback():
	print("I Accepted Something")
	Lock_Sub_Buttons()

def Cancel_Button_Callback():
	print("I Canceled Something")
	Clear_Overlay()
	Lock_Sub_Buttons()

def Export_Button_Callback():
	print("I Exported Something")
	Clear_Overlay()
	Lock_Sub_Buttons()

#Generates and fills content for the title frame
def Initialise_Title_Frame():
	titleLabel = Label(
	master=titleFrame,
	text = "People Health Pharmacy Inc.",
	font = headingFont
	)
	titleLabel.pack()

def Initialise_Side_Menu_Frame():
	#Frame for Logo
	logoFrame = Frame(sideBarFrame)
	logoFrame.pack()
	#Logo Creation
	logoLabel = Label(
		master = logoFrame,
		image = phpLogo
		)
	logoLabel.pack(pady = (30,50))

	#Main Menu Buttons
	mainMenuButtonsFrame = Frame(sideBarFrame)

	#Add Stock Item Button
	addStockButton = Button(
		master=mainMenuButtonsFrame,
		text = "Add a Stock Item",
		width = 20,
		height = 3,
		font = buttonFont,
		bg = LIGHTGRAY,
		fg = ALMOSTBLACK,
		command = Add_Stock_Callback
		)
	addStockButton.pack(padx = 15, pady = 10)

	#Add Sales Record Button
	addSalesRecordButton = Button(
		master=mainMenuButtonsFrame,
		text = "Add a Sales Record",
		width = 20,
		height = 3,
		font = buttonFont,
		bg = LIGHTGRAY,
		fg = ALMOSTBLACK,
		command = Add_Sales_Record_Callback
		)
	addSalesRecordButton.pack(padx = 15, pady = 10)

	#Edit Sales Record Button
	editSalesRecordButton = Button(
		master=mainMenuButtonsFrame,
		text = "Edit a Sales Record",
		width = 20,
		height = 3,
		font = buttonFont,
		bg = LIGHTGRAY,
		fg = ALMOSTBLACK,
		command = Edit_Sales_Record_Callback
		)
	editSalesRecordButton.pack(padx = 15, pady = 10)

	#Display Sales Record Button
	displaySalesRecordButton = Button(
		master=mainMenuButtonsFrame,
		text = "Display a Sales Record",
		width = 20,
		height = 3,
		font = buttonFont,
		bg = LIGHTGRAY,
		fg = ALMOSTBLACK,
		command = Display_Sales_Record_Callback
		)
	displaySalesRecordButton.pack(padx = 15, pady = 10)

	#Generate Report Button
	generateReportButton = Button(
		master=mainMenuButtonsFrame,
		text = "Generate a Sales Report",
		width = 20,
		height = 3,
		font = buttonFont,
		bg = LIGHTGRAY,
		fg = ALMOSTBLACK,
		command = Generate_Sales_Report_Callback
	)
	generateReportButton.pack(padx = 15, pady = 10)
	
	mainMenuButtonsFrame.pack()

#Generate Sub Menu
def Initialise_Sub_Menu_Frame():
	exportButton  = Button(
		master = subMenuFrame,
		text = "Export",
		width = 20,
		height = 3,
		font = buttonFont,
		bg = LIGHTGRAY,
		fg = ALMOSTBLACK,
		state = DISABLED,
		command = Export_Button_Callback
		)
	exportButton.pack(side = LEFT, anchor = W)

	cancelButton  = Button(
		master = subMenuFrame,
		text = "Cancel",
		width = 20,
		height = 3,
		font = buttonFont,
		bg = LIGHTGRAY,
		fg = ALMOSTBLACK,
		state = DISABLED,
		command = Cancel_Button_Callback
		)
	cancelButton.pack(side = LEFT, anchor = CENTER)

	AcceptButton  = Button(
		master = subMenuFrame,
		text = "Accept",
		width = 20,
		height = 3,
		font = buttonFont,
		bg = LIGHTGRAY,
		fg = ALMOSTBLACK,
		state = DISABLED,
		command = Accept_Button_Callback
		)
	AcceptButton.pack(side = LEFT,anchor = E)

#Constants
LIGHTGRAY = "#a6a6a6"
ALMOSTBLACK = "#292929"

#Global Varaibles
root = Tk()
root.geometry('1280x960')
phpLogo = PhotoImage(file="images/logo2.png")
#overlayFrameList = [] No used anymore, Delete if no use is found
overlayListElements = [4]
print(overlayListElements)

#Overlay Elements Master Frame Reference
overlayElementsMasterFrame = Frame

#Title Frame Creation
titleFrame = Frame(
	root,
    width = 800,
    height = 60,
    borderwidth = 5,
	relief = "ridge"
	)

#Side Menu Creation
sideBarFrame = Frame(
	root,
	height = 900,
	borderwidth = 5,
	relief = "ridge"
	)

#Overlay Area Creation
overlayFrame = Frame(
    root,
    width = 800,
    height = 750,
    borderwidth = 5,
	relief = "ridge"
    )

#Sub Menu Creation (Bottom Menu)
subMenuFrame = Frame(
	root,
	width = 800,
    height = 150,
    borderwidth = 5,
	relief = "ridge"
	)

#Fonts
buttonFont = ("Avenir", "14")
headingFont = ("Avenir", "26", "bold")
subHeadingFont = ("Avenir", "20", "bold")
#dateFont = ("Avenir", "18") If we end up doing a calender drop down box
textFont = ("Avenir", "12")

#Frame Intialisation
Initialise_Title_Frame()
Initialise_Side_Menu_Frame()
Initialise_Sub_Menu_Frame()

#Pack Order
sideBarFrame.pack(side = LEFT, fill = BOTH)
titleFrame.pack(fill = BOTH)
overlayFrame.pack(fill = BOTH, expand = 1)
subMenuFrame.pack_propagate(False)
subMenuFrame.pack(fill = BOTH)

root.mainloop()