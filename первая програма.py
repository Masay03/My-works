# 1. tk.Tk() - создание основного окна приложения.
# 2. pack() - метод для управления расположением виджета в окне.
# 3. grid() - метод для расположения виджетов в сетке окна.
# 4. place() - метод для позиционирования виджетов с точными координатами.
#
# Для создания различных виджетов и их конфигурации:
#
# 1. tk.Label() - создание текстовой метки.
# 2. tk.Button() - создание кнопки.
# 3. tk.Entry() - создание поля ввода текста.
# 4. tk.Text() - создание многострочного текстового поля.
# 5. tk.Checkbutton() - создание флажка (чекбокса).
# 6. tk.Radiobutton() - создание радиокнопки.
# 7. tk.Listbox() - создание списка для выбора элементов.
# 8. tk.Canvas() - создание холста для рисования графики.
#
# Для работы с событиями и обработки пользовательского ввода:
#
# 1. bind() - метод для привязки событий к виджетам.
# 2. get() - метод для получения значения из поля ввода.
# 3. insert() - метод для вставки текста в виджет.
# 4. delete() - метод для удаления части текста из виджета.
# 5. curselection() - метод для получения выбранных элементов из списка или другого виджета.
# 6. itemconfig() - метод для конфигурации отдельных элементов в списке или холсте.
import tkinter as tk
import json


### 2. Загрузка и сохранение задач
#Функции для сохранения задач в файл и загрузки задач из файла.

def save_tasks():
    with open('tasks.json', 'w') as file:
        json.dump(tasks, file, ensure_ascii=False)

def load_tasks():
    try:
        with open('tasks.json', 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


### 3. Обновление списка задач в интерфейсе
#Эта функция обновляет виджет списка задач в GUI.

def refresh_task_list():
    task_listBox.delete(0, tk.END)
    for idx, task_info in enumerate(tasks):
        completed = ' (выполнено)' if task_info.get('completed', False) else ''
        task_listBox.insert(tk.END, f"{idx+1}. {task_info['task']} - Приоритет: {task_info['priority']}{completed}")


### 4. Добавление новой задачи
#Функция для добавления новой задачи в список и обновления интерфейса.

def add_task():
    task = task_entry.get()
    priority = priority_entry.get()
    if task and priority.isdigit():
        tasks.append({"task": task, "priority": int(priority), "completed": False})
        save_tasks()
        refresh_task_list()
        task_entry.delete(0, tk.END)
        priority_entry.delete(0, tk.END)


### 5. Удаление выбранной задачи
#Функция для удаления выбранной задачи из списка.

def delete_task():
    selected_task = task_listBox.curselection()
    if selected_task:
        tasks.pop(selected_task[0])
        save_tasks()
        refresh_task_list()


### 6. Отметка задачи как выполненной
#Функция для изменения статуса задачи на "выполнено".

def mark_task():
    selected_task = task_listBox.curselection()
    if selected_task:
        task_index = selected_task[0]
        tasks[task_index]['completed'] = not tasks[task_index].get('completed', False)
        save_tasks()
        refresh_task_list()


### 7. Создание GUI

root = tk.Tk()
root.title("Список задач")
root.configure(background="aquamarine")

tasks = load_tasks()

task_label = tk.Label(root, text="Введите вашу задачу", bg="aquamarine")
task_label.pack()

task_entry = tk.Entry(root, width=30, bg="aquamarine")
task_entry.pack(pady=10)

priority_label = tk.Label(root, text="Установите приоритет (число)", bg="aquamarine")
priority_label.pack()

priority_entry = tk.Entry(root, width=10, bg="aquamarine")
priority_entry.pack(pady=5)

add_task_button = tk.Button(root, text="Добавить задачу", bg="CadetBlue1", command=add_task)
add_task_button.pack(pady=5)

delete_button = tk.Button(root, text="Удалить задачу", bg="CadetBlue1", command=delete_task)
delete_button.pack(pady=5)

mark_button = tk.Button(root, text="Отметить выполненную задачу", bg="CadetBlue1", command=mark_task)
mark_button.pack(pady=10)

tasks_label = tk.Label(root, text="Список ваших задач", bg="aquamarine")
tasks_label.pack()

task_listBox = tk.Listbox(root, height=15, width=50, bg="AntiqueWhite1")
task_listBox.pack()

refresh_task_list()

root.mainloop()
