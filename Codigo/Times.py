class Times(object):
    def __init__(self):
        self.t=0
        self.tde2=0
        self.tde4=0
        self.tde8=0
        self.tde40=0
        self.tde80=0
        self.tde200=0
        self.trespawn = []
        self.gameover = False
        self.winner = False
        self.tiempoanterior = 0
    def update_times(self):
        self.t+=1
        self.tde2+=1
        self.tde4+=1
        self.tde8+=1
        self.tde40+=1
        self.tde80+=1
        self.tde200+=1
        if self.t>1: self.t=0
        if self.tde2>2: self.tde2=0
        if self.tde4>4: self.tde4=0
        if self.tde8>8: self.tde8=0
        if self.tde40>40: self.tde40=0
        if self.tde80>80: self.tde80=0
        if self.tde200>200: self.tde200=0
        for respawntimes in self.trespawn:
            respawntimes.update()