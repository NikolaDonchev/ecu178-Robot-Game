#Liam Walsh
#binary algorithm



class Binarysearch:  #simpler solution

    def BS(self,graph,search):

        path=[]
        search = []
        while search:
            i=search
        if i not in path:
            self.path = path+[i]
            search = search + graph[i]
        elif i in path:
            graph.remove(i)
            return True



