import tkinter
import tkinter.messagebox
import customtkinter

import ffmpeg
import pytube
import time

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("green")


class App(customtkinter.CTk):

    WIDTH = 810
    HEIGHT = 450

    def __init__(self):
        super().__init__()

        self.title("Youtube downloader")
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frame_left = customtkinter.CTkFrame(master=self,
                                                 width=180,
                                                 corner_radius=0)
        self.frame_left.grid(row=0, column=0, sticky="nswe")

        self.frame_right = customtkinter.CTkFrame(master=self)
        self.frame_right.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

        self.frame_left.grid_rowconfigure(0, minsize=10)
        self.frame_left.grid_rowconfigure(5, weight=1)
        self.frame_left.grid_rowconfigure(8, minsize=20)
        self.frame_left.grid_rowconfigure(11, minsize=10)

        self.label_1 = customtkinter.CTkLabel(master=self.frame_left,
                                              text="CustomTkinter GUI",
                                              #text_font=("Roboto Medium", -16)
                                              )
        self.label_1.grid(row=1, column=0, pady=10, padx=10)

        self.label_mode = customtkinter.CTkLabel(master=self.frame_left, text="Témaválasztó:")
        self.label_mode.grid(row=9, column=0, pady=0, padx=20, sticky="w")

        self.optionmenu_1 = customtkinter.CTkOptionMenu(master=self.frame_left,
                                                        values=["Light", "Dark", "System"],
                                                        command=self.change_appearance_mode)
        self.optionmenu_1.grid(row=10, column=0, pady=10, padx=20, sticky="w")

        self.frame_right.rowconfigure((0, 1, 2, 3), weight=1)
        self.frame_right.rowconfigure(7, weight=10)
        self.frame_right.columnconfigure((0, 1), weight=1)
        self.frame_right.columnconfigure(2, weight=0)

        self.frame_info = customtkinter.CTkFrame(master=self.frame_right)
        self.frame_info.grid(row=0, column=0, columnspan=2, rowspan=4, pady=20, padx=20, sticky="nsew")


        self.frame_info.rowconfigure(0, weight=1)
        self.frame_info.columnconfigure(0, weight=1)

        self.label_info_1 = customtkinter.CTkLabel(master=self.frame_info,
                                                   text= "itt fognak megjelenni a videó adatai, ha elkészült a letöltés",
                                                   height=300,
                                                   corner_radius=6,
                                                   fg_color=("white", "gray38"),
                                                   justify=tkinter.LEFT)
        self.label_info_1.grid(column=0, row=0, sticky="nwe", padx=15, pady=15)


        self.radio_var = tkinter.IntVar(value=0)

        self.label_radio_group = customtkinter.CTkLabel(master=self.frame_right,
                                                        text="Válassz letöltési módot")
        self.label_radio_group.grid(row=0, column=2, columnspan=1, pady=20, padx=10, sticky="")

        self.radio_button_1 = customtkinter.CTkRadioButton(master=self.frame_right,
                                                           variable=self.radio_var,
                                                           text='Egyszerű videó',
                                                           value=0)
        self.radio_button_1.grid(row=1, column=2, pady=10, padx=20, sticky="n")

        self.radio_button_2 = customtkinter.CTkRadioButton(master=self.frame_right,
                                                           variable=self.radio_var,
                                                           text='Privát videó',
                                                           value=1)
        self.radio_button_2.grid(row=2, column=2, pady=10, padx=20, sticky="n")

        self.radio_button_3 = customtkinter.CTkRadioButton(master=self.frame_right,
                                                           variable=self.radio_var,
                                                           text='Lejátszási lista',
                                                           value=2)
        self.radio_button_3.grid(row=3, column=2, pady=10, padx=20, sticky="n")


        self.combobox_1 = customtkinter.CTkComboBox(master=self.frame_right,
                                                    values=["2160p 4K", "1080p FHD", "720p HD"])
        self.combobox_1.grid(row=6, column=2, columnspan=1, pady=10, padx=20, sticky="we")

        self.check_box_1 = customtkinter.CTkCheckBox(master=self.frame_right,
                                                     text="Csak audió")
        self.check_box_1.grid(row=6, column=0, pady=10, padx=20, sticky="w")

        self.check_box_2 = customtkinter.CTkCheckBox(master=self.frame_right,
                                                     text="Audió + videó")
        self.check_box_2.grid(row=6, column=1, pady=10, padx=20, sticky="w")

        self.entry = customtkinter.CTkEntry(master=self.frame_right,
                                            width=120,
                                            placeholder_text="Ide másold be a videó linkjét")
        self.entry.grid(row=8, column=0, columnspan=2, pady=20, padx=20, sticky="we")

        self.button_5 = customtkinter.CTkButton(master=self.frame_right,
                                                text="LETÖLTÉS",
                                                border_width=2,
                                                fg_color=None,
                                                command= lambda: self.start_download())
        self.button_5.grid(row=8, column=2, columnspan=1, pady=20, padx=20, sticky="we")



        self.optionmenu_1.set("Dark")
        self.combobox_1.set("Felbontás")
        self.radio_button_1.select()
        self.radio_button_3.configure(state=tkinter.DISABLED)
        self.check_box_1.configure(state=tkinter.DISABLED, text="Csak audió")
        self.check_box_2.select()

    def change_appearance_mode(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def on_closing(self, event=0):
        self.destroy()

    def start_download(self):

        link = self.entry.get()
        yt = pytube.YouTube(link, use_oauth=True, allow_oauth_cache=True)
        """
        self.label_info_1.set_text(
        'Cím:  ' + yt.title + '\n' +
        'Feltöltö:  ' + yt.author + '\n' +
        'Megtekintések száma:  ' + str(yt.views) + '\n' +
        'Videóhossz:  ' + str(yt.length) + ' másodperc' + '\n' +
        'letöltési link:  ' + link
        )
        """
        yt.streams.get_highest_resolution().download()

        def clean_filename(name):
            forbidden_chars = '"*\\/\'.|?:<>'
            filename = (''.join([x if x not in forbidden_chars else '#' for x in name])).replace('  ', ' ').strip()
            if len(filename) >= 176:
                filename = filename[:170] + '...'
            return filename

        def download_video(link, res_level='FHD'):
            ti = time.time()
            yt = pytube.YouTube(link, use_oauth=True, allow_oauth_cache=True)
            print(yt.title, '|', yt.author, '|', yt.publish_date.strftime("%Y-%m-%d"), '|', yt.views, '|', yt.length, 'sec')

            if res_level == '4K':
                dynamic_streams = ['2160p|160kbps', '1440p|160kbps', '1080p|160kbps', '720p|160kbps', '720p|128kbps',
                                   '480p|160kbps', '480p|128kbps']
            elif res_level == 'FHD':
                dynamic_streams = ['1080p|160kbps', '720p|160kbps', '720p|128kbps', '480p|160kbps', '480p|128kbps']
            for ds in dynamic_streams:
                try:
                    yt.streams.filter(res=ds.split('|')[0], progressive=False).first().download(filename='video.mp4')
                    yt.streams.filter(abr=ds.split('|')[1], progressive=False).first().download(filename='audio.mp3')
                    break
                except:
                    continue

            audio = ffmpeg.input('audio.mp3')
            video = ffmpeg.input('video.mp4')
            filename = 'downloadedvideos' + clean_filename(yt.title)

            duplicated = ['', '1', '2', '3', '4', '5']
            for dup in duplicated:
                try:
                    ffmpeg.output(audio, video, filename + dup + '.mp4').run()
                    break
                except:
                    continue

            print(ds, 'Video letöltve innen:', link)
            print('ennyi ideőt vett igénybe: {:.0f} mp.'.format(time.time() - ti))


if __name__ == "__main__":
    app = App()
    app.mainloop()