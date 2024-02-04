import flet as ft 
import random
import pyautogui
def main(page: ft.Page):
    page.title="Factorial"
    def hel(e):
        pyautogui.alert(text="Freamwork: Flet\nبرنامه نویس : آتیلا پاشازاده\nProgramming language: Python",title="Factorial")
    page.window_resizable=False
    page.window_maximizable=False
    page.window_width=450
    page.window_height=450
    bb=("#FF9B9B","#6527BE","#EF6262","#1A5D1A","#FF2171","#E1AEFF","#DD58D6","#DB005B","#FFB84C","#F266AB","#A459D1","#2CD3E1","#8B1874","#B71375","#FC4F00","#D4FAFC")
    def allshow(e):
            pyautogui.alert(text="%s\nanswer:%s"%(answer.value,answer1.value),title="Answer")
    def javab(e):
        
        field.border_color=random.choice(bb)
        
        try:
            num = int(field.value)
            if num == 0:
                answer.value = "1"
                answer1.value = "1"
            else:
                result = 1
                formula = ""
                for i in range(1, num + 1):
                    result *= i
                    if i != 1:
                        formula += "x"
                    formula += str(i)
                answer.value = str(num) +"!="  + " "+formula
                answer1.value=result
                answer.color=random.choice(bb)
                answer1.color=random.choice(bb)
        except:
            answer.value="value is not Integer"
            answer1.value=""
        page.update()
    field=ft.TextField(border_color="red",text_align=ft.TextAlign.CENTER,border_radius=50)
    answer=ft.Text(value="",color=random.choice(bb))
    answer1=ft.Text(value="",color=random.choice(bb))
    page.add(
        ft.AppBar(
            title=ft.Text(value="محاسبه فاکتوریل"),
            center_title=True,
            leading=ft.PopupMenuButton(
                icon=ft.icons.MENU,
                items=[
                    ft.PopupMenuItem(icon=ft.icons.INFO,text="Info",on_click=hel),
                ]
        )
    ),
        field,
        ft.Row([
            ft.ElevatedButton(text="ENTER",on_click=javab,bgcolor="green"),
            ft.ElevatedButton(text="showall",bgcolor="red",on_click=allshow)
        ],alignment=ft.MainAxisAlignment.CENTER),
        ft.Text(value=""),
        ft.Text(value=""),
        
        
        ft.Row(
            [
                answer
            ],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row(
            [
                answer1
            ],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        
    )


ft.app(target=main)