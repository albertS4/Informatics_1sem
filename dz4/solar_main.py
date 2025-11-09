import tkinter
from tkinter.filedialog import *
# раскомментируйте три строки ниже
from solar_visuals import * 
from solar_physics import *
from solar_read import *

magenta_selection = None
cyan_selection = None
show_selection = False


sigma = 0
omega = 0
ang_velocity = None
sec_velocity = None

perform_execution = False
"""Флаг цикличности выполнения расчёта"""

physical_time = 0
"""Физическое время от начала расчёта.
Тип: float"""

displayed_time = None
"""Отображаемое на экране время.
Тип: переменная tkinter"""

time_speed = 100

time_step = 1000
"""Шаг по времени при моделировании.
Тип: float"""

space_objects = []
"""Список космических объектов."""


def execution():
    """Функция исполнения -- выполняется циклически, вызывая обработку всех небесных тел,
    а также обновляя их положение на экране.
    Цикличность выполнения зависит от значения глобальной переменной perform_execution.
    При perform_execution == True функция запрашивает вызов самой себя по таймеру через от 1 мс до 100 мс.
    """
    global physical_time
    global displayed_time
    global omega
    global ang_velocity
    global sigma
    global sec_velocity
    recalculate_space_objects_positions(space_objects, time_step.get())
    for i in range(len(space_objects)):
        body = space_objects[i]
        update_object_position(space, body, selection_cyan=(cyan_selection == i and show_selection), selection_magenta=(magenta_selection == i and show_selection))
    physical_time += time_step.get()
    displayed_time.set("%.1f" % physical_time + " seconds gone")



    A = space_objects[magenta_selection]
    B = space_objects[cyan_selection]
    #сидерический год
    sigma = 0.5*((31558149.54)/(149597870691)**2)*((B.x - A.x)*(B.Vy - A.Vy) - (B.y - A.y)*(B.Vx - A.Vx))
    if A.x != B.x or A.y != B.y:
        omega = 2*sigma/(((B.x - A.x)/149597870691)**2 + ((B.y - A.y)/149597870691)**2)
    else:
        omega = 0
    
    ang_velocity.set("{number:.4f} рад/год".format(number = omega))

    sec_velocity.set("{number:.4f} а.е.^2/год".format(number = sigma))


    if perform_execution:
        space.after(101 - int(time_speed.get()), execution)


def start_execution():
    """Обработчик события нажатия на кнопку Start.
    Запускает циклическое исполнение функции execution.
    """
    global perform_execution
    perform_execution = True
    start_button['text'] = "Остановить"
    start_button['command'] = stop_execution

    execution()
    print('Запущено исполнение...')


def stop_execution():
    """Обработчик события нажатия на кнопку Start.
    Останавливает циклическое исполнение функции execution.
    """
    global perform_execution
    perform_execution = False
    start_button['text'] = "Запустить"
    start_button['command'] = start_execution
    print('Paused execution.')


def open_file_dialog():
    """Открывает диалоговое окно выбора имени файла и вызывает
    функцию считывания параметров системы небесных тел из данного файла.
    Считанные объекты сохраняются в глобальный список space_objects
    """
    global space_objects
    global perform_execution
    global magenta_selection
    global cyan_selection
    global show_selection
    show_selection = True
    perform_execution = False
    for obj in space_objects:
        space.delete(obj.image)  # удаление старых изображений планет
    in_filename = askopenfilename(filetypes=(("Text file", ".txt"),))
    space_objects = read_space_objects_data_from_file(in_filename)
    max_distance = max([max(abs(obj.x), abs(obj.y)) for obj in space_objects])
    calculate_scale_factor(max_distance)

    for obj in space_objects:
        if isinstance(obj, Star):
            create_star_image(space, obj)
        elif isinstance(obj, Planet):
            create_planet_image(space, obj)
        else:
            raise AssertionError()

    if len(space_objects) == 1:    
        magenta_selection = 0
        cyan_selection = 0
    elif len(space_objects) >= 2:
        magenta_selection = 0
        cyan_selection = 1


def save_file_dialog():
    """Открывает диалоговое окно выбора имени файла и вызывает
    функцию считывания параметров системы небесных тел из данного файла.
    Считанные объекты сохраняются в глобальный список space_objects
    """
    out_filename = asksaveasfilename(filetypes=(("Text file", ".txt"),))
    write_space_objects_data_to_file(out_filename, space_objects)


def main():
    """Главная функция главного модуля.
    Создаёт объекты графического дизайна библиотеки tkinter: окно, холст, фрейм с кнопками, кнопки.
    """
    global magenta_selection
    global cyan_selection

    global ang_velocity
    global sec_velocity
    global omega
    global sigma

    global physical_time
    global displayed_time
    global time_step
    global time_speed
    global space
    global start_button
    global show_selection

    print('Симуляция запущена!')
    physical_time = 0

    root = tkinter.Tk()
    root.title("Симуляция солнечной системы")
    # космическое пространство отображается на холсте типа Canvas
    space = tkinter.Canvas(root, width=window_width, height=window_height, bg="black")
    space.pack(side=tkinter.TOP)
    # нижняя панель с кнопками
    frame1 = tkinter.Frame(root)
    frame1.pack(side=tkinter.BOTTOM)
    frame = tkinter.Frame(root)
    frame.pack(side=tkinter.BOTTOM)

    start_button = tkinter.Button(frame, text="Запустить", command=start_execution, width=9)
    start_button.pack(side=tkinter.LEFT)

    time_step = tkinter.DoubleVar()
    time_step.set(300)
    time_step_entry = tkinter.Entry(frame, textvariable=time_step)
    time_step_entry.pack(side=tkinter.LEFT)

    time_speed = tkinter.DoubleVar()
    time_speed.set(100)
    scale = tkinter.Scale(frame, variable=time_speed, orient=tkinter.HORIZONTAL)
    scale.pack(side=tkinter.LEFT)

    load_file_button = tkinter.Button(frame, text="Открыть файл...", command=open_file_dialog)
    load_file_button.pack(side=tkinter.LEFT)
    save_file_button = tkinter.Button(frame, text="Сохранить в файл...", command=save_file_dialog)
    save_file_button.pack(side=tkinter.LEFT)

    displayed_time = tkinter.StringVar()
    displayed_time.set(str(physical_time) + " секунд прошло")
    time_label = tkinter.Label(frame, textvariable=displayed_time, width=30)
    time_label.pack(side=tkinter.RIGHT)



    l = tkinter.Label(frame1, text= "Угловая и секторная скорости Голубого выделения(меняется <- и ->) относительно Розового выделения (меняется ^ и v). Показать/скрыть - пробел")


    ang_velocity = tkinter.StringVar()
    ang_velocity.set(str(omega) + " рад/год")
    l1 = tkinter.Label(frame1, textvariable=ang_velocity, width=30)


    sec_velocity = tkinter.StringVar()
    sec_velocity.set(str(sigma) + " а.е.^2/год")
    l2 = tkinter.Label(frame1, textvariable=sec_velocity, width=30)

    l2.pack(side=tkinter.BOTTOM)
    l1.pack(side=tkinter.BOTTOM)
    l.pack(side=tkinter.BOTTOM)
    

    def mplus(x):
        global magenta_selection
        magenta_selection = (magenta_selection + 1)%len(space_objects)
    def mminus(x):
        global magenta_selection
        magenta_selection = magenta_selection - 1
        if magenta_selection < 0:
            magenta_selection = len(space_objects) - 1
    root.bind("<Up>", mplus)
    root.bind("<Down>", mminus)
    def cplus(x):
        global cyan_selection
        cyan_selection = (cyan_selection + 1)%len(space_objects)
    def cminus(x):
        global cyan_selection
        cyan_selection = cyan_selection - 1
        if cyan_selection < 0:
            cyan_selection = len(space_objects) - 1
    root.bind("<Right>", cplus)
    root.bind("<Left>", cminus)
    def toggle_selection(x):
        global show_selection
        show_selection = not show_selection
    root.bind("<space>", toggle_selection)
    root.mainloop()
    print('Симуляция завершена!')

if __name__ == "__main__":
    main()