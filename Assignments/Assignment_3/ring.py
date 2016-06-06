class Ring:

    def __init__(self,ring=[]):
        import re
        if type(ring) not in [type([]),type(()),type('aa')]:
                        ss = str(type(ring))
                        raise TypeError( '’{}’ object is not subscriptable'.format( ss[8:-2]))
        self.ring = ring
        self.start = 0
        self.step = 1

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
        elif key.step == 0:
            return type(self.ring)()
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
        import math
        List = []
        for i in value:
            List.append(i)
        if type(key) is int:
            key  %= len(self.ring)
            self.ring[key] = value
            return
        start = key.start % len(self.ring)
        stop = (key.stop + 1) % len(self.ring)
        step = key.step
        if key.step == None:
            step = 1
        if step == 0:
            if stop == 0:
                self.ring[start:] = List
                return
            if start < stop:
                self.ring[start:stop] = List
                return
            print(start,stop)
            self.ring = List + self.ring[stop:start] # if start > stop
            return

        if step > 0 :
            start += 1
            print(start,stop)
            if  start < stop:  ######################might wrong: number of element########
                if (stop - start) //step != len(List):
                    raise ValueError('attempt to insert sequence of size {} to extended slice of size {}'.format(len(List), (stop - start) //step))
            if start >= stop:
                if math.ceil((len(self.ring) - start + stop) / step) != len(List):
                    print(math.ceil((len(self.ring) - start + stop) / step))
                    raise ValueError('attempt to insert sequence of size {} to extended slice of size {}'.format(len(List), math.ceil((len(self.ring) - start + stop) / step) ))
            i = start #insert behind start
            for k in List:
                 i = i % len(self.ring) #go to beginning
                 self.ring.insert(i,k)
                 i += step + 1
        if step < 0:
            step = -step
            stop -= 1
            if start < stop:
                if math.ceil((stop - start +1 ) / step) != len(List):
                    raise ValueError('attempt to replace sequence of size {} to extended slice of size {}'.format(len(List), math.ceil((stop - start +1 ) / step)))
            if start >= stop:
                if math.ceil((len(self.ring) - start + stop +1) / step) != len(List):
                    raise ValueError('attempt to insert sequence of size {} to extended slice of size {}'.format(len(List), math.ceil((len(self.ring) - start +1 + stop) / step) ))
            i = start
            for k in List:
                i = i % len(self.ring)
                self.ring[i] = k
                i += step

    def __iter__(self):
        return self.next()

    def next(self):
        start = self.start % len(self.ring)
        yield(self.ring[start])
        start += self.step
        start %= len(self.ring)
        while start != self.start % len(self.ring):
            yield(self.ring[start])
            start += self.step
            start %= len(self.ring)





    def __repr__(self):
        output = 'Ring(' + str(self.ring) + ')'
        return(output)

    def __str__(self):
        return(str(self.ring))

    def __len__(self):
        return(len(self.ring))

