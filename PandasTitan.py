import pandas as pd
import time
import datetime
import numpy as np
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.progress import Progress
from rich.syntax import Syntax
from rich.prompt import Prompt
import pyfiglet
def new_rows():
	print('\n')
	progress_bar(0.01,'Loading')
	banner_rename = pyfiglet.figlet_format('New Info',font='slant') 
	console.print(banner_rename,style='cyan')
	#Logic
	while True:
		task=Prompt.ask("[bold]1.Add new column.\n2.Add new row.[/bold]\n: ",choices=['1','2'])
		if task=='1':
			
				col_name=Prompt.ask("\n[bold]What is the column name? [/bold]")
				if col_name in list(df.columns):
					console.print(Panel("Sorry, column name already exists! Enter another..."),style='red')
				else:
					formula = Prompt.ask('[bold]What is the formula?(1.column by column 2.Column by a number.)[/bold]',choices=['1','2'])
					if formula=='2':
						
						if col_name in list(df.columns):
							console.print(Panel("Sorry, column name already exists! Enter another..."),style='red')
						else:
							col_1=Prompt.ask("[bold]First column: [/bold]")
							operation=Prompt.ask("[bold]Enter operation(+,-,*,/,**): [/bold]",choices=['+','-','*','/','**'])
							num=Prompt.ask("\n[bold]What is the number for operation? [/bold]")
							if num.isalpha()==False:
								if operation=='+' and col_1 in list(df.columns):
									df[col_name]=df[col_1]+int(num)
									console.print(df,style='green')
									export(df.copy())
									break
								elif operation=='-' and col_1 in list(df.columns):
									df[col_name]=df[col_1]-int(num)
									console.print(df,style='green')
									export(df.copy())
									break
								elif operation=='*' and col_1 in list(df.columns):
									df[col_name]=df[col_1]*int(num)
									console.print(df,style='green')
									export(df.copy())
									break
								elif operation=='/' and col_1 in list(df.columns):
									df[col_name]=df[col_1]/int(num)
									console.print(df,style='green')
									export(df.copy())
									break
								elif operation=='**' and col_1 in list(df.columns):
										df[col_name]=df[col_1]**int(num)
										console.print(df,style='green')
										export(df.copy())
										break
					elif formula == "1":
						col_1=Prompt.ask("[bold]First column: [/bold]")
						col_2=Prompt.ask("[bold]Second column: [/bold]")
						operation=Prompt.ask("[bold]Enter operation(+,-,*,/,**): [/bold]",choices=['+','-','*','/','**'])
						if operation == '+'and col_1 in list(df.columns) and col_2 in list(df.columns):
							df[col_name]=df[col_1]+df[col_2]
							console.print(df)
							export(df.copy())
							break
						elif operation == '-'and col_1 in list(df.columns) and col_2 in list(df.columns):
							df[col_name]=df[col_1]-df[col_2]
							console.print(df)
							export(df.copy())
							break
						elif operation == '*'and col_1 in list(df.columns) and col_2 in list(df.columns):
							df[col_name]=df[col_1]*df[col_2]
							console.print(df)
							export(df.copy())
							break
						elif operation == '/'and col_1 in list(df.columns) and col_2 in list(df.columns):
							df[col_name]=df[col_1]/df[col_2]
							console.print(df)
							export(df.copy())
							break
						elif operation == '**'and col_1 in list(df.columns) and col_2 in list(df.columns):
							df[col_name]=df[col_1]**df[col_2]
							console.print(df)
							export(df.copy())
							break
						else:
							console.print(Panel("Invalid input, Check column names and try again"),style='red')						
					
		elif task=='2':
			col_values=[]
			for i in range(df.shape[1]):
				col_val=Prompt.ask(f"[bold]Enter the value of column [green]{df.columns[i]}[/green]: [/bold]")
				col_values.append(col_val)
		df.loc[len(df)]=col_values
		new = df.copy()
		console.print(new,style='green')
			
def drop_duplicates():
	print('\n')
	progress_bar(0.01,'Loading')
	banner_rename = pyfiglet.figlet_format('Duplicates',font='slant') 
	console.print(banner_rename,style='cyan')
	#Logic
	while True:
		if df.duplicated().any().any():
			console.print(Panel(f"There are {df.duplicated().sum()} duplicates in this dataframe."),style='red')
			q = Prompt.ask("[bold]Are you sure you want to drop duplicates? [/bold]",choices=['y','n'])
			if q == 'y':
				new=df.drop_duplicates()
				console.print(new,style='yellow')
				export(new)
				break
			elif q=='n':
				break
		else:
			console.print(Panel(f"There are {df.duplicated().sum()} duplicates in this dataframe."),style='green')
			break
			
def first_last():
	print('\n')
	progress_bar(0.01,'Loading')
	banner_rename = pyfiglet.figlet_format('Fast n Last',font='slant') 
	console.print(banner_rename,style='cyan')
	
	#Logic
	while True:
		num=Prompt.ask("[bold]Enter number of of rows you want: [/bold]")
		if num.isalpha()==False:
			console.print(Panel(f"First {num} items"),style="yellow")
			console.print(df.head(int(num)),style="green")
			new = df.head(int(num))
			
			console.print(Panel(f"Last {num} items"),style="yellow")
			console.print(df.tail(int(num)),style="green")
			new_last = df.tail(int(num))
			export(new)
			export(new_last)
			break
		
def code():
	print('\n')
	progress_bar(0.01,'Loading')
	banner_rename = pyfiglet.figlet_format('Codes',font='slant') 
	console.print(banner_rename,style='green')
	#Logic
	while True:
		console.print("[bold]1.Summary Statistics ~ Aggregation,mean,median etc\n2.Rename columns\n3.Fill empty values(Nan,Null)\n4.Sort data\n5.Conditionals\n6.Add new rows/columns.\n7.Check and remove duplicates.\n8.Get first(n) and last(n) data.\n[/bold]",style="yellow")
		menu_option=Prompt.ask("[bold]What do you want to do(# to go to main menu)? [/bold]",choices=['1','2','3','4','5','6','7','8','#'])
		code_1=f"""
		import pandas as pd
		#The summary of a data frame
		df=pd.read_csv({filename})
		df.describe()
		print(df)
		"""
		code_2=f"""
		import pandas as pd
		#Renaming columns
		df=pd.read_csv({filename})
		df.rename(inplace=True)
		"""
		code_3=f"""
		import pandas as pd
		df=pd.read_csv({filename})
		#check for null values
		if df.isna().any().any():
			print('Null values: '+df.isna().sum())
		else:
			print('No null values')
		#fill null values
		df.fillna(inplace=True)
		#Forward fill
		df.ffill(inplace=True)
		#Backward fill
		df.ffill(inplace=True)
		
		"""
		code_4=f"""
		import pandas as pd
		df=pd.read_csv({filename})
		df.sortvalues(by="column name",ascending=True)
		"""
		code_5=f"""
		import pandas as pd
		df=pd.read_csv({filename})
		# Get all items in the column "column name" less than 20
		#You can use any data type in place of value
		value = 20
		print(df.loc[df['column name']<value])
		
		"""
		code_6=f"""
		import pandas as pd
		df=pd.read_csv({filename})
		#Add new rows ~ list must have same otems as the columns in the data frame
		df.loc[len(df)]=["val1","val2"]
		#Add new columns
		df["new column"]==["val1",val2]
		#or
		df['new column']=df["old column"] * 2
		"""
		code_7=f"""
		import pandas as pd
		df=pd.read_csv({filename})
		df.drop_duplicates(inplace=True)
		"""
		code_8=f"""
		import pandas as pd
		df=pd.read_csv({filename})
		#first n values
		df.head(n)
		#last n values
		df.tail(n)
		"""
		if menu_option=='#':
			break
		elif menu_option=='1':
			print('\n')
			console.print(Panel("Code by [cyan]Onesmus bett[/cyan]"),style='green')
			console.print(Syntax(code_1,'python',line_numbers=True,theme='rainbow_dash'))
		elif menu_option=='2':
			print('\n')
			console.print(Panel("Code by [cyan]Onesmus bett[/cyan]"),style='green')
			console.print(Syntax(code_2,'python',line_numbers=True,theme='rainbow_dash'))
		elif menu_option=='3':
			print('\n')
			console.print(Panel("Code by [cyan]Onesmus bett[/cyan]"),style='green')
			console.print(Syntax(code_3,'python',line_numbers=True,theme='arduino'))
		elif menu_option=='4':
			print('\n')
			console.print(Panel("Code by [cyan]Onesmus bett[/cyan]"),style='green')
			console.print(Syntax(code_4,'python',line_numbers=True,theme='fruity'))
		elif menu_option=='5':
			print('\n')
			console.print(Panel("Code by [cyan]Onesmus bett[/cyan]"),style='green')
			console.print(Syntax(code_5,'python',line_numbers=True,theme='solarized'))
		elif menu_option=='6':
			print('\n')
			console.print(Panel("Code by [cyan]Onesmus bett[/cyan]"),style='green')
			console.print(Syntax(code_6,'python',line_numbers=True,theme='rainbow_dash'))
		elif menu_option=='7':
			print('\n')
			console.print(Panel("Code by [cyan]Onesmus bett[/cyan]"),style='green')
			console.print(Syntax(code_7,'python',line_numbers=True,theme='solarized'))
		elif menu_option=='8':
			print('\n')
			console.print(Panel("Code by [cyan]Onesmus bett[/cyan]"),style='green')
			console.print(Syntax(code_8,'python',line_numbers=True,theme='paraiso_dark'))
			
				
def about():
	print('\n')
	progress_bar(0.01,'Loading')
	banner_rename = pyfiglet.figlet_format('About',font='slant') 
	console.print(banner_rename,style='red')
	#Logic
	console.print(Panel("About Project Pandas Titan"),style='yellow')
	console.print("""
	[bold]Pandas titan[/bold] by [cyan]onesmus bett[/cyan] is a lightweight console app that lets you do data manipulation with the python pandas library.The main objective of this project is:\n[yellow]1.[bold]Simplify Data analysis[/bold]~ It uses easy to learn and understand concepts.\n2.[bold]Archive every days tasks with your data.[/bold]\n3.[bold]Find code that suits your needs.[/bold][/yellow]\n\n Visit my github page and see more of my projects. You can contact me on [green]onesmuskipchumba5@gmail.com[/green]\n\n[red]All rights preserved by the owner.[/red]
	""")
	nxt=Prompt.ask("\n[bold]Press any key to exit: [bold]")
	
	
def conditionals():
	print('\n')
	progress_bar(0.01,'Loading')
	banner_rename = pyfiglet.figlet_format('Conditionals',font='slant') 
	console.print(banner_rename,style='cyan')
	#Logic
	while True:
		col=Prompt.ask("[bold]What column is the condition based on? [/bold]")
		condition=Prompt.ask("\n[bold]What is the condition(less[<],less or equal[<=],equal[=],more[>],more or equal[>=])? [/bold]",choices=['<','<=','=','>','>='])
		val = Prompt.ask("\n[bold]What is the value to equate to(1.number or 2.word)? [/bold]",choices=['1','2'])
		if val=='2':
			word=Prompt.ask('\n[bold]Whats the word to equate to?[/bold]')
			if word.isalpha():
				new = df.loc[df[col]==word]
				print('\n')
				console.print(Panel(f'Your condition: [cyan]Locate values in column {col} which have the word [cyan]{word}[/cyan] in {filename}[/cyan]\n[green]Mathematically: [/green] {col} == {word}'))
				console.print(new,style='green')
				export(new)
				break	
		elif val == '1':
			#not done-only numbers
			num = Prompt.ask('\n[bold]Whats the number?[/bold]')
			
			if condition=='<' and num.isalpha()==False:
				new=df.loc[df[col]<int(num)]
				print('\n')
				console.print(Panel(f'Your condition: [cyan]Locate values in column {col} which are less than {num} in {filename}[/cyan]\n[green]Mathematically: [/green] {col} < {num}'))
				console.print(new,style='green')
				export(new)
			elif condition=='<=' and num.isalpha()==False:
				new=df.loc[df[col]<=int(num)]
				print('\n')
				console.print(Panel(f'Your condition: [cyan]Locate values in column {col} which are less than or equal to {num} in {filename}[/cyan]\n[green]Mathematically: [/green] {col} <= {num}'))
				console.print(new,style='green')
				export(new)
			elif condition=='=' and num.isalpha()==False:
				new=df.loc[df[col]==int(num)]
				print('\n')
				console.print(Panel(f'Your condition: [cyan]Locate values in column {col} which are equal to {num} in {filename}[/cyan]\n[green]Mathematically: [/green] {col} == {num}'))
				console.print(new,style='green')
				export(new)
			elif condition=='>'and num.isalpha()==False:
				new=df.loc[df[col]>int(num)]
				print('\n')
				console.print(Panel(f'Your condition: [cyan]Locate values in column {col} which are more than {num} in {filename}[/cyan]\n[green]Mathematically: [/green] {col} > {num}'))
				console.print(new,style='green')
				export(new)
			elif condition=='>='and num.isalpha()==False:
				new=df.loc[df[col]==int(num)]
				print('\n')
				console.print(Panel(f'Your condition: [cyan]Locate values in column {col} which are more than or equal to {num} in {filename}[/cyan]\n[green]Mathematically: [/green] {col} >= {num}'))
				console.print(new,style='green')
				export(new)
				
def sort_data():
	print('\n')
	progress_bar(0.01,'Loading')
	banner_rename = pyfiglet.figlet_format('Sort Data',font='slant') 
	console.print(banner_rename,style='red')
	while True:
		col = Prompt.ask("[bold]Which row would you like to sort? [/bold]")
		prompt=Prompt.ask(f"[bold]How would you like to sort [green]{col}[/green](1.Ascending,2.Descending)? [/bold]",choices=['1','2'],default='1')
		if col in list(df.columns) and prompt=='1':
			new=df.sort_values(by=col,ascending=True)
			console.print(Panel("Here is you data in descending order"),style='green')
			console.print(new,style='green')
			
			export(new)
			progress_bar(0.01,'Back to main menu')
			break
		if col in list(df.columns) and prompt=='2':
			new=df.sort_values(by=col,ascending=False)
			console.print(Panel("Here is you data in descending order"),style='green')
			console.print(new,style='green')
			export(new)
			progress_bar(0.01,'Back to main menu')
			break
		else:
			console.print(Panel('No such column! please try again'),style='red')
def fill_null():
	print('\n')
	progress_bar(0.01,'Loading')
	banner_rename = pyfiglet.figlet_format('FillIt',font='slant') 
	console.print(banner_rename,style='cyan')
	print('\n')
	progress_bar(0.01,'Searching null values')
	#logic
	console.print(df.isna().sum(),style="green")
	while True:
		if df.isna().any().any():
			console.print(Panel("There are null values in your dataset!"),style="red")
			prompt = Prompt.ask("[bold]Would you like to fill them up? [/bold]",choices=['y','n'])
			if prompt=='n':
					progress_bar(0.01,"Back to main menu")
					break
			elif prompt=='y':
				console.print('There are [bold]three[/bold] main methods here: [green]\n1.Back fill ~ fill values with the bottom ones filling up missing values at the top.\n2.Forward fill ~ fill values with the top ones filling up null values at the bottom.\n3.Interpolate ~ Fill null values with close to appropriate values.[/green]')
				method=Prompt.ask("[bold]Which do you choose '#' to go to main menu: [/bold]")
				if method=='#':
					progress_bar(0.01,"Back to main menu")
					break
				elif method=='1':
					#Back fill
					new=df.bfill()
					console.print(df.isna().sum(),style='green')
					console.print(Panel('Success, no more null values'),style='green')
					export(new)
					progress_bar(0.01,"Back to main menu")
					break
				elif method=='2':
						new=df.ffill()
						console.print(new.isna().sum(),style='green')
						console.print(Panel('Success, no more null values'),style='green')
						progress_bar(0.01,"Back to main menu")
						break
				elif method=='3':
			
						new=df.interpolate()
						console.print(df.isna().sum(),style='green')
						console.print(Panel('Success, no more null values'),style='green')
						progress_bar(0.01,"Back to main menu")
						export(new)
						break		
		else:
			console.print(Panel("Hurray!!,There are no null values in your dataset!"),style="green")
			progress_bar(0.01,"Back to main menu")
			break
def export(renamed_df):
	print('\n')
	export = Prompt.ask("[bold]Do you want to export the data frame? [/bold]",choices=['y','n'])
	if export == 'y':
			name = Prompt.ask("[bold]Enter name of the file(.csv/.xlsx)? [/bold]")
			if '.csv' in name:
				renamed_df.to_csv(name)
				progress_bar(0.01,"Exporting")
				console.print(Panel('File exported successfully!'),style='green')
				
			elif '.xlsx'in name:
				try:
					renamed_df.to_excel(name)
					print('\n')
					progress_bar(0.01,"Exporting")
					console.print(Panel('File exported successfully!'),style='green')
				except ModuleNotFoundError:
					console.print(Panel('Unsuccessful ~ Module openpyxl not found. Try running pip install openpyxl!',style='red'))
				
			else:
				console.print(Panel('Unsuccessful ~ Format not recognised!',style='red'))
	elif export == 'n':
		print('\n')
		analysis_base()	
def rename_cols():
	print('\n')
	progress_bar(0.01,'Loading')
	banner_rename = pyfiglet.figlet_format('Rename',font='slant') 
	console.print(banner_rename,style='cyan')
	#logic
	while True:
	
		col_name=Prompt.ask("[bold]Enter column you wish to rename: [/bold]")
		new_name=Prompt.ask(f"[bold]Enter new name for [green]{col_name}[/green]: [/bold]")
		if new_name == '':
			console.print('\nName cannot be empty',style='red')
		else:
			renamed_df=df.rename(columns={col_name:new_name})
			console.print(Panel("Here is you renamed data frame"),style="cyan")
			console.print(renamed_df,style='green')
			export(renamed_df)
	
def summary_stats():
	print('\n')
	progress_bar(0.01,'Calculating')
	banner_stats = pyfiglet.figlet_format('Titan Stats',font='slant') 
	console.print(banner_stats,style='red')
	console.print(Panel("Here is you summarised stats."),style='cyan')
	console.print(df.describe(),style="green")
	new=df.describe()
	
	while True:
		print('\n')
		console.print(Panel('Other features: '),style='cyan')
		console.print("1.Group data by column(e.g,by gender,class etc)\n2.show the code.")
		agg=Prompt.ask("[bold]Choose from above or enter '#' to go back to main menu: [/bold]",choices=['1','2','#'])
		if agg=='#':
			export(new)
			print('\n')
			break
		elif agg=='2':
			console.print(Panel("[bold]Code:[/bold] by [green]ONESMUS BETT[/green]"))
			code=f'''
			import pandas as pd
			df = read_csv('{filename}')
			#code for summary stats
			df.describe()
			#You can use .mean,count,sum or median
			df.groupby('col_name')['stats_column'].mean()
			'''
			syntax=Syntax(code,"python",theme='monokai',line_numbers=True)
			console.print(syntax)	
		elif agg=='1':
			console.print(f"[blink]Columns[/blink]: [green]{str(list(df.columns))}[/green]")
			col_name = Prompt.ask('[bold]Please, enter a column name for grouping data: [/bold]')
			stat_col=Prompt.ask("\n[bold]Enter the column with the statistics: [/bold]")
			method=Prompt.ask("\n[bold]Enter the mode e.g, mean,median,count,sum: [/bold]")
			if method == 'mean':
				console.print(df.groupby(col_name)[stat_col].mean(),style="green")
			elif method=='median':
				console.print(df.groupby(col_name)[stat_col].median(),style="green")
			elif method=='count':
				console.print(df.groupby(col_name)[stat_col].count(),style="green")
			elif method=='sum':
				console.print(df.groupby(col_name)[stat_col].sum(),style="green")
					
	progress_bar(0.01,'Back to main menu')
	
def analysis_base():
	progress_bar(0.01,'Analising')
	panel_analyse=Panel(f"[bold]{filename}[/bold] has the following features....")
	columns = df.shape[1]
	rows=df.shape[0]
	console.print(panel_analyse)
	print('\n')
	data_table = Table(title=f"{filename} Analysis",style='yellow')
	data_table.add_column("Name",style='bold')
	data_table.add_column("Info")
	data_table.add_row("Columns",f"{str(list(df.columns))} {df.shape[1]} in total")
	data_table.add_row("\nRows",f"\nTotal: {df.shape[0]} rows")
	data_table.add_row("\nShape",f"\n{str(df.shape)}")
	data_table.add_row("\nNull Values",f"\nTotal:\n{df.isna().sum()}")
	console.print(data_table)
	while True:
		print('\n')
		console.print(Panel("MAIN MENU ~ choose from options below."),style="green")
		console.print("[bold]1.Summary Statistics ~ Aggregation,mean,median etc\n2.Rename columns\n3.Fill empty values(Nan,Null)\n4.Sort data\n5.Conditionals\n6.Add new rows/columns.\n7.Check and remove duplicates.\n8.Show the code.\n9.Get first(n) and last(n) data.\n10.About.[/bold]",style="cyan")
		menu_option=Prompt.ask("[bold]What do you want to do? [/bold]",choices=['1','2','3','4','5','6','7','8','9','10'])
		if menu_option=='6':
			new_rows()
		elif menu_option=='7':
			drop_duplicates()
		elif menu_option=='8':
			code()
		elif menu_option=='9':
			first_last()
		elif menu_option=='10':
			about()
		elif menu_option=='5':
			conditionals()
		elif menu_option=='4':
			sort_data()
		elif menu_option=='1':
			summary_stats()
		elif menu_option =='2':
			rename_cols()
		elif menu_option == '3':
			fill_null()
#progress bar function
def progress_bar(time_speed,message):
	with Progress() as progress:
		task=progress.add_task(f"[red]{message}...[/red]",total=100)
		for i in range(100):
			time.sleep(time_speed)
			progress.update(task,advance=1)
	print('\n')
			
console=Console()
banner=pyfiglet.figlet_format("Pandas Titan",font='rounded')
banner2=pyfiglet.figlet_format("Onesmus bett co.",font='3-d')
console.print(banner,style="green")
console.print(banner2,style="red")
progress_bar(0.02,'Loading')
welcome_panel=Panel('[bold]Welcome to pandas Titan by Onesmus Bett[/bold]')
console.print(welcome_panel)
console.print('This is a project that aids in pandas data manipulation and analysis!',style='yellow')
print('\n')
import os
while True:
	try:
		script_dir=os.path.dirname(os.path.abspath(__file__))
		console.print(f"Files in directory: [bold]{script_dir}[/bold]")
		for file in os.listdir(script_dir):
			console.print(file,style="yellow")
		print('\n')
			
		filename=Prompt.ask('[bold]Please, enter the name of the csv/excel file here: [/bold]')
		if '.csv' in filename:
			df=pd.read_csv(filename)
			console.print(df.head(),style='green')
			print('\n')
			analysis_base()
			break
		elif '.xlsx' in filename:
			df=pd.read_excel(filename)
			console.print(df.head(),style='green')
			print('\n')
			analysis_base()
			break
	except FileNotFoundError:
				print('\n')
				progress_bar(0.06,"Searching")
				console.print(f"[bold]No such file '{filename}' found! Ensure the file is in the same directory as the script and try again![/bold]",style='red')
				print('\n')