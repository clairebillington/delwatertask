#This is a simple To-do app built on Gooey Pie
#https://www.gooeypie.dev/start

import gooeypie as gp


def five_min(event):
    #add to 5 minute block
    five_min_todo_list.add_item(task_inp.text)
    #Clear Task box out
    task_inp.clear()


def fifteen_min(event):
    #add to 15 minute block
    fifteen_min_todo_list.add_item(task_inp.text)
    #Clear Task box out
    task_inp.clear()


def thirty_min(event):
    #add to 30 minute block
    thirty_min_todo_list.add_item(task_inp.text)
    #Clear Task box out
    task_inp.clear()


def sixty_min(event):
    #add to 60 minute block
    sixty_min_todo_list.add_item(task_inp.text)
    #Clear Task box out
    task_inp.clear()


def done_5(event):
    done_btn_5.text = 'Nice!'
    #move task to done list
    done_list.add_item(five_min_todo_list.remove_selected())

def done_15(event):
    done_btn_15.text = 'Nice!'
    #move task to done list
    done_list.add_item(fifteen_min_todo_list.remove_selected())

def done_30(event):
    done_btn_30.text = 'Nice!'
    #move task to done list
    done_list.add_item(thirty_min_todo_list.remove_selected())

def done_60(event):
    done_btn_60.text = 'Nice!'
    #move task to done list
    done_list.add_item(sixty_min_todo_list.remove_selected())

def delete_5(event):
    five_min_todo_list.remove_selected()
    

def delete_15(event):
    fifteen_min_todo_list.remove_selected()


def delete_30(event):
    thirty_min_todo_list.remove_selected()


def delete_60(event):
    sixty_min_todo_list.remove_selected()


def clear_all(event):
    done_list.items=[]


  
app = gp.GooeyPieApp('Timely')
app.width = 300

#Task
task_lbl = gp.Label(app, "Task")
task_inp = gp.Input(app)
task_inp.width = 50

#Time Estimate Buttons
five_min_btn = gp.Button(app, '5', five_min)
min_lbl = gp.Label(app, 'Mins')
fifteen_min_btn = gp.Button(app, '15', fifteen_min)
thirty_min_btn = gp.Button(app, '30', thirty_min)
sixty_min_btn = gp.Button(app, '60', sixty_min)

#5 min bucket
five_min_todo_list = gp.Listbox(app)
five_min_todo_list.height = 5
five_min_todo_lbl = gp.Label(app, '5 Min Tasks')

#15 min bucket
fifteen_min_todo_list = gp.Listbox(app)
fifteen_min_todo_list.height = 5
fifteen_min_todo_lbl = gp.Label(app, '15 Min Tasks')

#30 min bucket
thirty_min_todo_list = gp.Listbox(app)
thirty_min_todo_list.height = 5
thirty_min_todo_lbl = gp.Label(app, '30 Min Tasks')

#60 min bucket
sixty_min_todo_list = gp.Listbox(app)
sixty_min_todo_list.height = 5
sixty_min_todo_lbl = gp.Label(app, '60 Min Tasks')

#Done bucket
done_list = gp.Listbox(app)
done_list.height = 5
done_list_lbl = gp.Label(app, 'Done')
clear_all_button = gp.Button(app, 'Clear Done List', clear_all)

#Done? buttons
done_btn_5 = gp.Button(app, 'Done?', done_5)
done_btn_15 = gp.Button(app, 'Done?', done_15)
done_btn_30 = gp.Button(app, 'Done?', done_30)
done_btn_60 = gp.Button(app, 'Done?', done_60)

#Delete buttons
delete_btn_5 = gp.Button(app, 'Delete', delete_5)
delete_btn_15 = gp.Button(app, 'Delete', delete_15)
delete_btn_30 = gp.Button(app, 'Delete', delete_30)
delete_btn_60 = gp.Button(app, 'Delete', delete_60)

#Formatting
app.set_grid(14, 6)
app.add(task_inp, 1, 2, align='center', column_span=5)
app.add(task_lbl, 1, 1, align='center')
app.add(min_lbl, 2, 1, align='center')
app.add(five_min_btn, 2, 2, align='left')
app.add(fifteen_min_btn, 2, 3, align='left')
app.add(thirty_min_btn, 2, 4, align='left')
app.add(sixty_min_btn, 2, 5, align='left')
app.add(five_min_todo_list, 3, 2, align='left', column_span=4)
app.add(five_min_todo_lbl, 3, 1, align='center')
app.add(done_btn_5, 4, 2, align='left')
app.add(delete_btn_5, 4, 3, align='left')
app.add(fifteen_min_todo_list, 5, 2, align='left', column_span=4)
app.add(fifteen_min_todo_lbl, 5, 1, align='center')
app.add(done_btn_15, 6, 2, align='left')
app.add(delete_btn_15, 6, 3, align='left')
app.add(thirty_min_todo_list, 7, 2, align='left', column_span=4)
app.add(thirty_min_todo_lbl, 7, 1, align='center')
app.add(done_btn_30, 8, 2, align='left')
app.add(delete_btn_30, 8, 3, align='left')
app.add(sixty_min_todo_list, 9, 2, align='left', column_span=4)
app.add(sixty_min_todo_lbl, 9, 1, align='center')
app.add(done_btn_60, 10, 2, align='left')
app.add(delete_btn_60, 10, 3, align='left')
app.add(done_list, 11, 2, align='left', column_span=4)
app.add(done_list_lbl, 11, 1, align='center')
app.add(clear_all_button, 12, 2, align="left", column_span=2)

#RUNNNNNN!
app.run()
