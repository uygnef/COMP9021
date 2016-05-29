class Ring:
    def __init__(self,ring=[]):
        self.ring = ring

    def __getitem__(self,key):
        
        try:
            if key.start == None:
                start = 0        
            else:
                start = key.start%len(self.ring)
        except AttributeError:
            return (self.ring[key%len(self.ring)])

        if key.step == None:
            step = 1
        else:
            step = key.step
            
        if key.stop == None:
            if step < 0 :
                stop = start + 1
            elif step > 0:
                stop = start - 1
        else:
            stop = key.stop
            
        stop = stop% len(self.ring) + 1
        if stop <= start and step > 0:
            goal = self.ring[start:]+self.ring[:stop]
            return(goal[::step])
        if stop >= start and step < 0:
            goal = self.ring[start::-1] + self.ring[:stop-2:-1]
            return(goal[::-step])

        return(self.ring[start:stop:step])

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
