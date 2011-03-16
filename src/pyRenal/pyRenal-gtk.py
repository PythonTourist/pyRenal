import gtk
import gtk.glade
import string
from SuperEnalotto import SuperEnalotto
from Win4Life import Win4Life

class pyRenalgtk:

#Handler for File->SuperEnalotto. It generate and write the numbers in the text result area of the window.    
    def on_newse_activate(self, widget):
#Instance of the SuperEnalotto Generator
        se = SuperEnalotto()
#We need a TextBuffer object to be passed to the TextView
        buffer = gtk.TextBuffer() 
#Store the result in a string format to be passed to the TextBuffer
        serie = str(se.calculate()) 
#Store the obtained string in a Buffer to later move in our TextView        
        buffer.set_text(serie)
#Finally populate the TextView with the obtained buffer
        self.resultarea.set_buffer(buffer)

#Handler for File->Win4Life
    def on_neww4l_activate(self, widget):
#Instance of the Win4Life Generator
        w4l = Win4Life()
#We need a TextBuffer object to be passed to the TextView
        buffer = gtk.TextBuffer() 
#Store the result in a string format to be passed to the TextBuffer
        serie = str(w4l.calculate()) 
#Store the obtained string in a Buffer to later move in our TextView        
        buffer.set_text(serie)
#Finally populate the TextView with the obtained buffer
        self.resultarea.set_buffer(buffer)
#Handler for destroy signal. Exit the application when the window is closed        

    def on_window_destroy(self, widget):
        gtk.main_quit()      

#Class constructor.       
    def __init__(self):
#Gui creation with builder from a file generated with Glade 3.6.6
        builder = gtk.Builder()
        builder.add_from_file("ui.glade")
#Get Object from the Gui into our application
        self.window = builder.get_object("window1")
        self.resultarea = builder.get_object("textview1")
        self.resultarea.set_editable(False) #TextView not editable
        self.resultarea.set_cursor_visible(False) #TextView has no cursor
        self.menu = builder.get_object("menubar1")
# List of all the signals in the Gui to be connected
        segnali = {"on_window1_destroy": self.on_window_destroy, 
                   "on_newse_activate": self.on_newse_activate,
                   "on_neww4l_activate": self.on_neww4l_activate}
        builder.connect_signals(segnali)

#Just copied from internet. Can be made directly below is suppose
    def main(self):
        self.window.show()
        gtk.main()

if __name__ == "__main__":
    a = pyRenalgtk()
    a.main()