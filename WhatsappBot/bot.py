from selenium import webdriver
import time

class WhatsappBot:
    def __init__(self):
        self.mensagem = 'oi eu sou o bot'
        self.grupos = ['teste']
        self.ultimo = 'teste'
        self.n = 0
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver')

    def inicio(self):
        self.driver.get('https://web.whatsapp.com/')
        time.sleep(20)

#<div class="_210SC" style="z-index: 132; transition: transform 200ms ease-in-out 0s; height: 72px; transform: translateY(0px);"><div tabindex="-1" aria-selected="false" role="option"><div class="eJ0yJ"><div class="_325lp"><div class="_1BjNO" style="height: 49px; width: 49px;"><img src="https://web.whatsapp.com/pp?e=https%3A%2F%2Fpps.whatsapp.net%2Fv%2Ft61.24694-24%2F56870254_2289711214578198_1921914765932756992_n.jpg%3Foh%3D1c759f5b88d99ac674237b56d49cf1f6%26oe%3D5EFD9870&amp;t=s&amp;u=558185996258-1469839903%40g.us&amp;i=1469840089&amp;n=b0ZrqqfmmX9ZAMIMWqbDX1Cw5pP%2FBBN%2B%2FfEHB3Rzb9g%3D" alt="" draggable="false" class="_2goTk _1Jdop _3Whw5" style="visibility: visible;"><div class="_1V82l"><span data-icon="default-group" class=""><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 212 212" width="212" height="212"><path fill="#DFE5E7" class="background" d="M105.946.25C164.318.25 211.64 47.596 211.64 106s-47.322 105.75-105.695 105.75C47.571 211.75.25 164.404.25 106S47.571.25 105.946.25z"></path><path fill="#FFF" class="primary" d="M61.543 100.988c8.073 0 14.246-6.174 14.246-14.246s-6.173-14.246-14.246-14.246-14.246 6.173-14.246 14.246 6.174 14.246 14.246 14.246zm8.159 17.541a48.192 48.192 0 0 1 8.545-6.062c-4.174-2.217-9.641-3.859-16.704-3.859-21.844 0-28.492 15.67-28.492 15.67v8.073h26.181l.105-.248c.303-.713 3.164-7.151 10.365-13.574zm80.755-9.921c-6.854 0-12.21 1.543-16.336 3.661a48.223 48.223 0 0 1 8.903 6.26c7.201 6.422 10.061 12.861 10.364 13.574l.105.248h25.456v-8.073c-.001 0-6.649-15.67-28.492-15.67zm0-7.62c8.073 0 14.246-6.174 14.246-14.246s-6.173-14.246-14.246-14.246-14.246 6.173-14.246 14.246 6.173 14.246 14.246 14.246zm-44.093 3.21a23.21 23.21 0 0 0 4.464-.428c.717-.14 1.419-.315 2.106-.521 1.03-.309 2.023-.69 2.976-1.138a21.099 21.099 0 0 0 3.574-2.133 20.872 20.872 0 0 0 5.515-6.091 21.283 21.283 0 0 0 2.121-4.823 22.16 22.16 0 0 0 .706-3.193c.16-1.097.242-2.224.242-3.377s-.083-2.281-.242-3.377a22.778 22.778 0 0 0-.706-3.193 21.283 21.283 0 0 0-3.272-6.55 20.848 20.848 0 0 0-4.364-4.364 21.099 21.099 0 0 0-3.574-2.133 21.488 21.488 0 0 0-2.976-1.138 22.33 22.33 0 0 0-2.106-.521 23.202 23.202 0 0 0-4.464-.428c-12.299 0-21.705 9.405-21.705 21.704 0 12.299 9.406 21.704 21.705 21.704zM145.629 131a36.739 36.739 0 0 0-1.2-1.718 39.804 39.804 0 0 0-3.367-3.967 41.481 41.481 0 0 0-3.442-3.179 42.078 42.078 0 0 0-5.931-4.083 43.725 43.725 0 0 0-3.476-1.776c-.036-.016-.069-.034-.104-.05-5.692-2.581-12.849-4.376-21.746-4.376-8.898 0-16.055 1.795-21.746 4.376-.196.089-.379.185-.572.276a43.316 43.316 0 0 0-3.62 1.917 42.32 42.32 0 0 0-5.318 3.716 41.501 41.501 0 0 0-3.443 3.179 40.632 40.632 0 0 0-3.366 3.967c-.452.61-.851 1.186-1.2 1.718-.324.493-.6.943-.841 1.351l-.061.101a27.96 27.96 0 0 0-.622 1.119c-.325.621-.475.975-.475.975v11.692h82.53v-11.692s-.36-.842-1.158-2.195a35.417 35.417 0 0 0-.842-1.351z"></path></svg></span></div></div></div><div class="_2kHpK"><div class="_3dtfX"><div class="_3CneP"><div class="_357i8"><span dir="auto" title="teste" class="_3ko75 _5h6Y_ _3Whw5">teste</span><div class="_3XFan"></div></div></div><div class="m61XR">00:00</div></div><div class="_1582E"><div class="_3tBW6"><span class="_2iq-U" title="‪sss‬"><div class="zFnXi"><span data-icon="status-check" class=""><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 14 18" width="14" height="18"><path fill="currentColor" d="M12.502 5.035l-.57-.444a.434.434 0 0 0-.609.076l-6.39 8.198a.38.38 0 0 1-.577.039l-2.614-2.556a.435.435 0 0 0-.614.007l-.505.516a.435.435 0 0 0 .007.614l3.887 3.8a.38.38 0 0 0 .577-.039l7.483-9.602a.435.435 0 0 0-.075-.609z"></path></svg></span></div><span dir="ltr" class="_3ko75 _5h6Y_ _3Whw5">sss</span></span></div><div class="m61XR"><span></span><span></span><span></span></div></div></div></div></div></div>

    def envia(self, mensagem):
        #contatos = self.driver.find_element_by_class_name('_210SC')

        box = self.driver.find_element_by_class_name("_210SC")
        time.sleep(1)
        box.click()
        #contato = self.driver.find_element_by_xpath(f"//span[@title='{contato}']")
        #contato.click()
        chat_box = self.driver.find_element_by_class_name('_3uMse')
        time.sleep(1)
        chat_box.click()
        chat_box.send_keys(mensagem)
        botao_enviar = self.driver.find_element_by_xpath("//span[@data-icon='send']")
        time.sleep(1)
        botao_enviar.click()
        time.sleep(2)

    def organizaLista(self, lista):
        #lista = lista[::-1]
        novaLista = []
        c = 0
        linha = []
        for i in range(len(lista)):
            item = lista[i]
            if not item in ['1','2','3','4']:
                linha.append(item)
                c += 1
            if c == 3:
                c = 0
                novaLista.append(linha)
                linha = []
        else:
            novaLista.append(linha)

        return novaLista



    def run(self):
        self.inicio()
        box = self.driver.find_element_by_class_name("_210SC")
        time.sleep(1)
        while True:
            box = self.driver.find_element_by_class_name("_1qDvT")
            elementos = box.text.split('\n')
            elementos = self.organizaLista(elementos)
            time.sleep(1)
            self.n += 1
            for i in elementos:
                print(i)
            print('#'*15)
        #self.envia('bot oi2')

    def enviarMensagem(self):
         #<span dir="auto" title="Saxofonistas&nbsp;&nbsp;Pernambuco" class="_3ko75 _5h6Y_ _3Whw5">Saxofonistas&nbsp;&nbsp;Pernambuco</span>
         #<div tabindex="-1" class="_3uMse">
         #<span data-icon="send" class=""><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24"><path fill="currentColor" d="M1.101 21.757L23.8 12.028 1.101 2.3l.011 7.912 13.623 1.816-13.623 1.817-.011 7.912z"></path></svg></span>

        self.driver.get('https://web.whatsapp.com/')

        time.sleep(30)

        for grupo in self.grupos:
            grupo = self.driver.find_element_by_xpath(f"//span[@title='{grupo}']")
            time.sleep(1)
            grupo.click()
            chat_box = self.driver.find_element_by_class_name('_3uMse')
            time.sleep(1)
            chat_box.click()
            chat_box.send_keys(self.mensagem)
            botao_enviar = self.driver.find_element_by_xpath("//span[@data-icon='send']")
            time.sleep(1)
            botao_enviar.click()
            time.sleep(2)

bot = WhatsappBot()
bot.run()
