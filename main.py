from guizero import App, Picture, Text, Box
cuaso = App(title = "cac cuon sach yeu thich", width = 370, height = 550, layout = "grid")
pic1 = Picture(cuaso, image = "pic1.png", grid = [0,0,1,2], width = 180, height = 270)
pic2 = Picture(cuaso, image = "pic2.png", grid = [1,0,1,1], width = 180, height = 270)
pic3 = Picture(cuaso, image = "pic3.png", grid = [1,1,1,1], width = 180, height = 270)
cuaso.display()