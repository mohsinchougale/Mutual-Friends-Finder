# Python implementation of Kosaraju's algorithm to print all SCCs

from collections import defaultdict
import PIL.ImageTk
import PIL.Image
import random
from tkinter import *

nodes = 15
scc_graph = [[0 for i in range(nodes)] for i in range(nodes)]

#UI intial code
app = Tk()
app.configure(bg='black')

#output_label declared as global to avoid overwriting
run_output_label = Label(app)
rf_output_label = Label(app)
mutual_f_output_label = Label(app)

#global scc_output string as recursion is used
scc_output = ""

#This class represents a directed graph using adjacency list representation
class Graph:

	def __init__(self,vertices):
		self.V= vertices #No. of vertices
		self.graph = defaultdict(list) # default dictionary to store graph

	# function to add an edge to graph
	def addEdge(self,u,v):
		self.graph[u].append(v)

	#function to print the graph
	def print_graph_list(self):
		print(self.graph)

	# A function used by DFS
	def DFSUtil(self,v,visited,temp_list):
		global scc_output

		#temp list to store a scc
		# Mark the current node as visited and print it
		visited[v]= True
		scc_output  = scc_output + str(v) + " "
		temp_list.append(v)

		#Recur for all the vertices adjacent to this vertex
		for i in self.graph[v]:
			if visited[i]==False:
				self.DFSUtil(i,visited,temp_list)


	def fillOrder(self,v,visited, stack):
		# Mark the current node as visited
		visited[v]= True
		#Recur for all the vertices adjacent to this vertex
		for i in self.graph[v]:
			if visited[i]==False:
				self.fillOrder(i, visited, stack)
		stack = stack.append(v)


	# Function that returns reverse (or transpose) of this graph
	def getTranspose(self):
		g = Graph(self.V)

		# Recur for all the vertices adjacent to this vertex
		for i in self.graph:
			for j in self.graph[i]:
				g.addEdge(j,i)
		return g


	def add_to_matrix(self,temp_list):
		for i in range(len(temp_list) -1):
			for j in range(1,len(temp_list)):
				if( i != j):
					#adding to scc matrix representation
					scc_graph[ temp_list[i] ][ temp_list[j] ] = 1
					scc_graph[ temp_list[j] ][ temp_list[i] ] = 1

					#adding to scc dictionary representation
					sub.addEdge(temp_list[i],temp_list[j])
					sub.addEdge(temp_list[j],temp_list[i])

	# The main function that finds and prints all strongly
	# connected components
	def printSCCs(self):
		global scc_output
		global run_output_label
		run_output_label.destroy()

		temp_list = []
		scc_output = ""
		stack = []

		# Mark all the vertices as not visited (For first DFS)
		visited =[False]*(self.V)
		# Fill vertices in stack according to their finishing
		# times
		for i in range(self.V):
			if visited[i]==False:
				self.fillOrder(i, visited, stack)

		# Create a reversed graph
		gr = self.getTranspose()

		# Mark all the vertices as not visited (For second DFS)
		visited =[False]*(self.V)

		# Now process all vertices in order defined by Stack
		while stack:
			i = stack.pop()
			if visited[i]==False:
				temp_list = []
				gr.DFSUtil(i, visited,temp_list)
				self.add_to_matrix(temp_list)
				scc_output += "\n"

		run_output_label = Label(app, text= scc_output,font=('times',18,'bold'),fg="white",bg="black")
		canvas1.create_window(150, 300, window=run_output_label)

#------------------------------------------------------------------------------------------
	def give_a_random_friend(self):
		global rf_output_label
		rf_output_label.destroy()

		output = ""
		friend = int(friend_entry.get() )

		if( self.graph.get(friend) == None):
			output = output +"No friend is present"
		else:
			output = output + "Friend is : "+str( random.choice(self.graph[friend]) )

		rf_output_label = Label(app, text= output,font=('times',18,'bold'),fg="white",bg="black")
		canvas1.create_window(700, 240, window=rf_output_label)


#-------------------------------------------------------------------------------------------
	def get_mutual_friend(self):
		x = int(friend_entry_1.get())
		y = int(friend_entry_2.get())

		global mutual_f_output_label
		mutual_f_output_label.destroy()
		output = ""

		if(self.graph.get(x) == None or self.graph.get(y) == None ):
			output = output +"No mutual friend present"
		else:
			a_set = set(self.graph.get(x) )
			b_set = set(self.graph.get(y) )

			if (a_set & b_set):
				s = list(a_set & b_set)
				out_str = ' '.join(map(str, s))
				output = output +"Mutual friends are : " +out_str
			else:
				output = output +"No mutual friend elements"

		mutual_f_output_label = Label(app, text= output,font=('times',18,'bold'),fg="white",bg="black")
		canvas1.create_window(700, 470, window = mutual_f_output_label)




#Main code
if __name__=="__main__":
	#UI code
	app.title("Kosaraju Algorithm simulator")
	app.geometry("1600x900")

	#Addition of background image
	load = PIL.Image.open("C:\\Users\\admin\\Desktop\\DAA mini project\\bg_image.jpg")
	render = PIL.ImageTk.PhotoImage(load)

	img = Label(app,image = render)
	img.place( x=0 ,y=0 )


	# Create a graph given in the above diagram
	g = Graph(nodes)
	sub  = Graph(nodes)
	#Adding edges
	g.addEdge(1, 0)
	g.addEdge(0, 2)
	g.addEdge(2, 3)
	g.addEdge(3, 4)
	g.addEdge(4, 5)
	g.addEdge(5, 1)

	g.addEdge(6, 3)
	g.addEdge(6, 8)
	g.addEdge(8, 10)
	g.addEdge(10, 7)
	g.addEdge(7, 8)

	g.addEdge(7, 9)
	g.addEdge(9, 4)

	g.addEdge(5,12)
	g.addEdge(12, 11)
	g.addEdge(11, 13)
	g.addEdge(13, 14)
	g.addEdge(14, 12)

	#Creating Title canvas
	title_canvas = Canvas(app, bg='black',width = 1000, height = 200)
	title_canvas.pack()

	#Additon of image at the top right corner
	logo_img = PhotoImage(file="logo.png")
	title_canvas.create_image(800,0, anchor=NW, image=logo_img)

	#Title label
	title_label = Label(app,text="Kosaraju's Algorithm",font=("Times",45),fg="white",bg="black" )
	title_canvas.create_window(400,100,window=title_label)

	#Creating the canvas1
	canvas1 = Canvas(app, bg='black',width = 1000, height = 700)
	canvas1.pack()


	#Running Kosaraju's algorithm
	run_label = Label(app, text='Press this button to run'+'\n'+"Kosaraju's Algorithm",font=('times',24,'bold'),fg="white",bg="black")
	canvas1.create_window(200, 100, window = run_label)

	run_button = Button(text='Run', command = g.printSCCs,bg="black", fg="white", activebackground="white", activeforeground="black", relief="raised", padx=12, pady=4, bd=4)
	canvas1.create_window(150, 180, window = run_button)


	#Getting a random friend function
	txt_label = Label(app, text='Enter the name of person  here ',font=('times',24,'bold'),fg="white",bg="black")
	canvas1.create_window(700, 90, window = txt_label)

	friend_entry = Entry (app, font=('times',18,'bold') )
	canvas1.create_window(700, 150, window = friend_entry)

	random_friend_button = Button(text='Get a friend', command = sub.give_a_random_friend,bg="black", fg="white",
				   activebackground="white", activeforeground="black", relief="raised", padx=12,
				   pady=4, bd=4)
	canvas1.create_window(700, 200, window = random_friend_button)


	#Getting mutual friend function
	txt_label_2 = Label(app, text='Enter the name of people  here',font=('times',24,'bold'),fg="white",bg="black")
	canvas1.create_window(700, 300, window = txt_label_2)

	friend_entry_1 = Entry (app, font=('times',18,'bold') )
	canvas1.create_window(560, 360, window = friend_entry_1)

	friend_entry_2 = Entry (app, font=('times',18,'bold') )
	canvas1.create_window(820, 360, window = friend_entry_2)

	mutual_friend_button = Button(text='Get Mutual friend', command = sub.get_mutual_friend,bg="black", fg="white",
				   activebackground="white", activeforeground="black", relief="raised", padx=12,
				   pady=4, bd=4)
	canvas1.create_window(700, 420, window = mutual_friend_button)

	#tkinter close
	app.mainloop()
