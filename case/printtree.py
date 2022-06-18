def printTree(node,nodeInfo,indent=""):
    label,children = nodeInfo(node)
    print(indent[:-3] + "|_ "*bool(indent) + str(label))
    for more,child in enumerate(children,1-len(children)):
        childIndent = "|  " if more else "   "
        printTree(child,nodeInfo,indent+childIndent)



T = {'data': 1, 'children':
        [ { 'data':2, 'children':
            [ {'data':6 }, {'data':7} ]},
          {'data':3},
          {'data':4},
          {'data':5, 'children':
           [{'data':10}]}
        ]
     }

printTree(T,lambda d:(d['data'],d.get('children',[])))