#Liam Walsh
#binary algorithm



"""class Binarysearch:  #simpler solution
"""
def BS(graph,start):

    path=[]
    search = [start]
    while search:
        i=search.pop(0)
    if i not in path:
        path = path+[i]
        (search = search + graph[i])
        return search

graph = {'Z':['A','B']},{'X':['E','C']},{'Y':['F','D']}
print "BS search",BS(graph,'Z')
