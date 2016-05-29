class Ring:
    def __init__(self,ring=[]):
        self.ring = ring

    def __getitem__(self,key):
        try:
            start = key.start%len(self.ring)
        except AttributeError:
            return (self.ring[key%len(self.ring)])
        if key.start == None:
            start = 0
        if key.stop == None:
            if key.step < 0 :
                stop = start + 1
            elif key.step > 0:
                stop = start + 1              
            
        stop = key. stop% len(self.ring)
        if stop < start:
            goal = self.ring[start:]+self.ring[:stop]
            print(goal)
            return(goal[::key.step]+go)
        return(self.ring[start:stop:key.step]+self.ring[stop])

    def __setitem__(self,key,value):
        key  %= len(self.ring)
        self.ring[key] = value
        
    def __repr__(self):
        output = 'Ring(' + str(self.ring) + ')'
        return(output)

    def __str__(self):
        return(str(self.ring))

    def __len__(self):
        return(len(self.ring))
