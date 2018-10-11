import csv
import networkx as nx
import sys


edgeGraph = nx.Graph()
edges = []

def create_network(inFile,outFile):


    with open(inFile) as csvfile:

        csvRead = csv.reader(csvfile, delimiter=',')

        # empty list for tuples to convert to edges
        edgeList = []
        # list for just nodes not tuples, used in later function
        nodeList = []

        for row in csvRead:
            print(row)

            # add tuples to empty list
            edgeList.append(

                (row[0],row[1])
            )
            if row[0] in nodeList:
                # If first node is already used e.g. (x,y) & x is already in the list...
                nodeList.append(row[1])
                # check list
            else:
                # If first node is not already used, add both nodes
                nodeList.append(row[0])
                nodeList.append(row[1])


        # add edges from list to graph object
        edgeGraph.add_edges_from(edgeList)

        # checks
        print(edgeList)
        print(nodeList)
        edges.append(edgeList)

        # report stats and graph info
        reportAndWriteStatistics(edgeGraph,outFile)

        print("Edges are:" + str(edgeGraph.number_of_edges()))

        #calls function below
        removeNodes(nodeList,edgeGraph,outFile)






def removeNodes(nodeList,edgeGraph,outFile):

    # create temp to run perculation on
    tempEdgeGraph = edgeGraph.copy()

    # perculate graph for each node in the list
    for node in nodeList:

        # checks
        '''
        print(node)
        print(nx.info(tempEdgeGraph))
        print(nx.betweenness_centrality(tempEdgeGraph))
        print(nx.nodes(tempEdgeGraph))

        '''

        tempEdgeGraph.remove_node(node)
        print("REMOVING NODE " + (node))


        # Report summary stats and info
        reportAndWriteStatistics(tempEdgeGraph,outFile)

        # reset graph to original
        tempEdgeGraph = edgeGraph.copy()



        '''
        
        Test for minimum number of edges 
        
        Text file (tab deliniated)
       
        '''



def reportAndWriteStatistics(graph,outFile):

    # Print statistics
    print('Betweenness Centrality')
    print(nx.betweenness_centrality(graph))
    print('\n')
    print('Denisty')
    print(nx.density(graph))
    print('\n')
    print('Graph info')
    print(nx.info(graph))
    print('\n')
    print('Average Clustering Coefficient')
    print(nx.average_clustering(graph))
    print('\n')
    print('Radius')

    writeStatistics(graph,outFile)




def writeStatistics(graph,outFile):

    statisticsList = []

    statisticsList.append(str(nx.eigenvector_centrality(graph)))
    statisticsList.append(str(nx.density(graph)))
    # statisticsList.append(nx.info(graph))
    statisticsList.append(str(nx.average_clustering(graph)))

    if len(nx.edges(graph)) is 0:      # radius function can not run on a graph with no edges
        statisticsList.append('ERR: Edges = 0')

    else:
        statisticsList.append(str(nx.radius(graph)))
        statisticsList.append(str(nx.diameter(graph)))


    print("STATISTICS LIST")
    print(statisticsList[0])
    print(statisticsList)

    centrality = nx.eigenvector_centrality(graph)
    print(centrality)
    print(['%f' % (centrality[node]) for node in centrality])
    output = open(outFile, "w")
    output.write(['%f'%(centrality[node]) for node in centrality])
    # outFile.write(statisticsList)
    # with open(outFile, "w") as out_f:
        # out_f.write('\t'.join(statisticsList[0]))
        # out_f.write(['%s\t%0.2f'%(node,centrality[node]) for node in centrality])
        # out_f.write(['%s' % (node) for node in centrality])
        # out_f.write(['%f' % (centrality[node]) for node in centrality])

    output.close()




# allows program to run on command line
def main(arguments):
    inFile = arguments[1]
    outFile = arguments[2]
    # open(outFile, 'w')
    create_network(inFile,outFile)


if __name__ == '__main__':
        main(sys.argv)