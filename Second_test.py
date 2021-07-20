import networkx as nx
import matplotlib.pyplot as plt
from textblob import Word
import csv
import numpy as np
import collections
synonyms=[]
words=[]

def centrality(G, nodes):
    top = set(nodes) 
    
    s = 1.0/len(top) 
    centrality = dict((n,d*s) for n,d in G.degree(top)) 
   
    return centrality
def Ranking(G):
    pagerank_dict=nx.pagerank(G);
    import operator
    sorted_x = sorted(pagerank_dict.items(), key=operator.itemgetter(1))
    return list(reversed(sorted_x))
with open('twitter_result.txt','r') as file:
    for w in file:
        words=w.split(",")
words.remove('')
#print(words)
G=nx.Graph()

for aword in  words:
    if not aword in  words:
        words.append(aword)
        G.add_node(aword)
            
for word1 in  words:
    for word2 in  words:
        tweets = open('RESUILT.csv', 'r',encoding='ISO-8859-1')
        for t in csv.reader(tweets):
            tweet=t[1] 
            #print(tweet)
            if word1 in tweet and word2 in tweet: 
                G.add_edge(word1,word2)

#print(G.nodes(data=True))
pos = nx.spring_layout(G,k=1)
nx.draw(G, pos, font_size=16,font_color='blue', with_labels=True)

betweenness_dict = nx.betweenness_centrality(G) # Run betweenness centrality
eigenvector_dict = nx.eigenvector_centrality(G) # Run eigenvector centrality
clo_cen = nx.closeness_centrality(G)
centrality_dict=nx.degree_centrality(G)
# Assign each to an attribute in your network
nx.set_node_attributes(G, betweenness_dict, 'betweenness')
nx.set_node_attributes(G, eigenvector_dict, 'eigenvector')
nx.set_node_attributes(G, clo_cen, 'closeness')
nx.set_node_attributes(G, centrality_dict, 'closeness')
print("\nnodes by betweenness centrality:")
print(betweenness_dict)
print("\nnodes by eigenvector centrality:")
print(eigenvector_dict)
print("\nnodes by closeness centrality:")
print(clo_cen)
print("\nnodes centrality:")
print(centrality(G,words))
final_dict={k: betweenness_dict.get(k, 0) + eigenvector_dict.get(k, 0)+ clo_cen.get(k, 0)+ centrality_dict.get(k, 0) for k in set(betweenness_dict)}
print("\nFinal  node weights:")
print(final_dict)

for n in  G:
    print("\nimportant neighbors nodes for -->",n)
    #for j in G.neighbors(n):
       # print("----->>",j)
fig = plt.gcf()
fig.set_size_inches(18.5, 10.5)
fig.savefig('test2png.png', dpi=100)
plt.savefig("path.png")
print("\nTerm frequency:")
plt.show()

fwords=[]



with open('words.txt','r') as file:
    for w in file:
        fwords=w.split(",")
fwords.remove('')
word_counts = collections.Counter(fwords)

    
max_c=max(word_counts, key=word_counts.get)
print(max_c)

min_c=min(word_counts, key=word_counts.get)
print(min_c)

maximum=0
minimum=0
for word, count in sorted(word_counts.items()):
    #print('%s ----->%d' % (word, count))
    if word==max_c:
        maximum=count
    if word==min_c:
        minimum=count
        
s_list=sorted(word_counts, key=word_counts.get, reverse=True)      
print("minimum ",minimum)
print("maximim ",maximum)

ranks=Ranking(G)
print("\nRanks of Extracted Words")
rank=1
output=[]
for key, value in ranks:
    print("%s -- %d"%(key,rank))
    output.append(key)
    rank+=1
    
old_words = ['t', 'i', 'a', 'u', 'vaccin', 'th', 'peopl', 'covid', 'birth', 'leav', 'would', 'be_born', 'ignor', 'passport', 'gather', 'dr', 'forget', 'unmask', 'agit', 'keep_quiet', 'usa', 'left', 'hospit', 'chose', 'camp', 'also', 'california', 'break', 'exist', 'report', 'say', 'differ', 'discharg', 'govern', 'conspiraci', 'fall', 'news', 'fox', 'vaccine', 'unbreak', 'answer', 'dose', 'cant']
y_pred = ['Martyred', 'uri', 'attack', 'terror', 'pm' , 'army', 'ignor', 'passport', 'gather', 'dr', 'forget', 'unmask', 'agit', 'keep_quiet', 'usa', 'left','soldiers', 'condemns', 'surgical','strike' ,'terrorist', 'india','Pakistan','surgicalstrike', 'pak', 'Kashmir','uriattack']
y_pred = ['harry', 'potter' , 'be_born', 'ignor', 'passport', 'gather', 'finally', 'oscar', 'harrypotter','break', 'exist', 'report' 'series', 'time', 'books', 'read', 'winning', 'half-blood', 'prince', 'Radcliff']

TP=0
FP=0
FN=0
for w in output:
    if w in  old_words:
        TP+=1
        print(w)
FP=len(output)-TP
FN=len(old_words)-TP
# print("True Positive is :",TP)
# print("False Positive is :",FP)
# print("False Negative is :",FN)

pre=TP/(TP+FP)
rec=TP/(TP+FN)
print("Precision is :",pre)
print("Recall is :",rec)
F1=2*((pre*rec)/(pre+rec))
print("F1-Score is :",F1)

# print("copy this for next reference")
# print(output)

# import sklearn.metrics
# if len(old_words)<=len(output):
#     s=sklearn.metrics.accuracy_score(output[0:len(old_words)], old_words)  
#     print("Accuracy Score is: ", s)
# else:
#     s=sklearn.metrics.accuracy_score(old_words[0:len(output)], output)  
#     print("Accuracy Score is: ", s)  
