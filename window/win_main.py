#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-

import tkinter as tk


class IpEntry(tk.Frame):
    def __init__(self, parent, **kwargs):
        tk.Frame.__init__(self, parent, width=230, height=55)
        self.__dict__.update(kwargs)

        self.is_disable = kwargs.get('is_disable', False)
        self.is_range = kwargs.get('is_range', False)
        self.is_disable_range = kwargs.get('is_disable_range', False)

        self.ip_ent = tk.Entry(self, font="Arial 14", takefocus=0)
        self.ip_ent.place(width=230)

        if self.is_range is True:
            self['width'] = 500

            self.ip_ent_r = tk.Entry(self, font="Arial 14", takefocus=0)
            self.dash_lbl = tk.Label(self, text='—', font="Arial 14")

            self.dash_lbl.place(x=235, y=1, height=22)
            self.ip_ent_r.place(x=265, width=230)

        if self.is_disable is True:
            self.ip_ent.config(state=tk.DISABLED)

            if self.is_range is True:
                self.ip_ent_r.config(state=tk.DISABLED)

        if self.is_range is True and self.is_disable_range is True:
            self.ip_ent_r.config(state=tk.DISABLED)

        self.str_ip = []
        self.ip = []

        x = -59
        if self.is_range is True:
            y = 8
        else:
            y = 4

        for i in range(0, y):
            if i == 4:
                x = x + 85
            else:
                x = x + 60

            self.str_ip.append(tk.StringVar())

            self.vcmd = (self.register(self.validate_val), '%P')
            self.ip.append(tk.Entry(self, bd=0, font="Arial 14", justify='center', validate='key',
                                    validatecommand=self.vcmd, textvariable=self.str_ip[i]))

            self.ip[i].place(x=x, y=1, width=49)

            if self.is_disable is True or (self.is_range is True and self.is_disable_range is True and i >= 4):
                self.ip[i].config(state=tk.DISABLED)

        self.ip_dot = []

        x = -10
        if self.is_range is True:
            y = 6
        else:
            y = 3

        for i in range(0, y):
            if i == 3:
                x = x + 145
            else:
                x = x + 60

            self.ip_dot.append(tk.Label(self, text=".", font="Arial 14"))
            self.ip_dot[i].place(x=x, y=1, height=24)

            if self.is_disable is False and self.is_range is True and self.is_disable_range is True and i >= 3:
                pass
            elif self.is_disable is True:
                pass
            else:
                self.ip_dot[i].config(bg='#ffffff')

        self.err_lbl = tk.Label(self, text='err', fg='#ff0000', font="Arial 8")

        if self.is_range is True:
            self.err_lbl.config(width=81, justify=tk.CENTER)

        for i, str_var in enumerate(self.str_ip):
            str_var.trace("w", lambda name, index, mode, j=i: self.validate_ip(self.str_ip, self.ip, j))

        for i, entry in enumerate(self.ip):
            entry.bind('<Right>', lambda event, j=i: self.next_ent(event, self.ip, j))
            entry.bind('<Left>', lambda event, j=i: self.prev_ent(event, self.ip, j))

    def validate_val(self, val):
        if len(val) == 0:
            return True
        elif val.isdigit():
            return True
        else:
            return False

    def validate_ip(self, str_list, entry_list, index):
        if self.is_range is True:
            err_val = 'Недопустимое значение {val}. Укажите значение в диапазоне от 0 до 255.'
        else:
            err_val = 'Недопустимое значение {val}.\nУкажите значение в диапазоне от 0 до 255.'

        ip_ent = str_list[index].get()

        self.err_lbl.place_forget()

        if len(ip_ent) == 3:
            if int(ip_ent) > 255:
                str_list[index].set('255')
                self.err_lbl.configure(text=err_val.format(val=ip_ent))
                self.err_lbl.place(y=26)
            else:
                entry_list[index].tk_focusNext().focus()
        elif len(ip_ent) > 3:
            str_list[index].set(ip_ent[:3])

    def next_ent(self, event, entry_list, index):
        if self.is_range is True and self.is_disable_range is True and index == 3:
            next_i = 0
        else:
            next_i = (index + 1) % len(entry_list)

        if entry_list[index].index(tk.INSERT) == entry_list[index].index(tk.END):
            entry_list[next_i].focus_set()
            entry_list[next_i].icursor(0)

    def prev_ent(self, event, entry_list, index):
        if self.is_range is True and self.is_disable_range is True and index == 0:
            prev_i = 3
        else:
            prev_i = (index - 1) % len(entry_list)

        if entry_list[index].index(tk.INSERT) == 0:
            entry_list[prev_i].focus_set()
            entry_list[prev_i].icursor(entry_list[prev_i].index(tk.END))


class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.real_ip_lbl = tk.Label(self, text='Реальный IP адрес для вычисления', font="Arial 8")
        self.real_ip_ent = IpEntry(self)

        self.r_real_ip_lbl = tk.Label(self, text='Реальные IP адреса', font="Arial 8")
        self.r_real_ip_ent = IpEntry(self, is_range=True)

        self.r_virt_ip_lbl = tk.Label(self, text='Виртуальные IP адреса', font="Arial 8")
        self.r_virt_ip_ent = IpEntry(self, is_range=True, is_disable_range=True)

        self.virt_ip_lbl = tk.Label(self, text='Вычисленный виртуальный IP адрес', font="Arial 8")
        self.virt_ip_ent = IpEntry(self, is_disable=True)

        self.real_ip_lbl.grid(row=0, column=0, ipady=5, padx=10)
        self.real_ip_ent.grid(row=1, column=0, padx=10)

        self.r_real_ip_lbl.grid(row=2, column=0, ipady=5, padx=10)
        self.r_real_ip_ent.grid(row=3, column=0, padx=10)

        self.r_virt_ip_lbl.grid(row=4, column=0, ipady=5, padx=10)
        self.r_virt_ip_ent.grid(row=5, column=0, padx=10)

        self.virt_ip_lbl.grid(row=6, column=0, ipady=5, padx=10)
        self.virt_ip_ent.grid(row=7, column=0, padx=10)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("ViPNet IP Калькулятор")
    root.geometry('520x325+50+50')
    root.resizable(0, 0)
    MainApplication(root).pack(fill="both", expand=True)
    root.mainloop()
