#!/usr/bin/python

import numpy as np
import scipy.stats
import networkx as nx
import pandas as pd

#################################################
# PART 1: Correlation Matrix
#################################################

# Read in counts and store column(sample) names and row(gene) names
counts_matrix = pd.read_table("fin_mirna_mature_counts.txt",sep='\t',index_col=0)
print(counts_matrix.head())
#gene_names = counts_matrix_for_labels.index
#print(gene_names)

# Read in counts and store as matrix of counts
#counts_matrix = np.genfromtxt("fin_mirna_mature_counts.txt",delimiter="\t",dtype=int,usecols=range(1,34),skiprows=1,missing_values="NA")
#print(counts_matrix[1])

# Compute Pearson correlation matrix - Do not use
#cor_matrix = np.corrcoef(counts_matrix)

# Compute Spearman correlation matrix (note that function returns matrix as [0] and p-values as [1])
cor_matrix = counts_matrix.corr(method='spearman')
#cor_matrix = scipy.stats.spearmanr(np.transpose(counts_matrix))[0]
#print(cor_matrix)
cor_matrix.to_csv("fin_all_timepoints_spearman_corr_matrix.txt",sep='\t')

# Find minimum Spearman correlation for each miRNA after excluding each sample individually
# to address samples that may be particularly influential
# # Loop over each column in counts_matrix
# # STEP 1: Remove column
# # STEP 2: Calculate Spearman correlation and save each correlation matrix
# # Make a new correlation matrix where the values represent the minimum for each cell
# # STEP 1: Interate over each row and column
# # STEP 2: Look up corresponding values in each of the saved correlation matrices and take the minimum
# # STEP 3: Save the minimum value in the final correlation matrix

np_df = cor_matrix.as_matrix()

print(len(np_df))

cor_matrices = [[{} for _ in range(len(np_df))] for _ in range(len(np_df))]
final_cor_matrix = [[0 for _ in range(len(np_df))] for _ in range(len(np_df))]

# Find number of samples to interate over
num_samples = len(np_df)
print(num_samples)

df = pd.DataFrame(counts_matrix)

print(counts_matrix.columns)

# Iterate through counts matirx to insure that each value is added into the list 
headerList = []
for sample in counts_matrix.columns:
  
    headerList.append(sample) 

print("HEADERS:")
print(headerList)

# NOTES:
# NOT seperate columns
# Might need dimension
# Need the index to make the correcation matrix below
# Use dictionary with key as #

# Interate over samples, remove a sample and calcuate Spearman correlation for each
for sample in headerList:
    print(sample)
    # Remove sample from counts
    #### THIS IS WHERE THE PROBLEM NOW STARTS AS WE DON'T KNOW TO REMOVE A SAMPLE FROM A pandas Data Frame
#    counts_without_sample = np.delete(counts_matrix,i,1)
    counts_without_sample = df.drop(sample, axis=1)
    print(counts_without_sample)

    #counts_without_sample = counts_matrix.drop(columns=1)
    #print(len(counts_without_sample[0]))
    # Calculate Spearman correlation
    i = 0
    cor_matrices[i] = scipy.stats.spearmanr(np.transpose(counts_without_sample))[0]
    i = i+1
    
print("CORR MATRICIES")
print(cor_matricies)
print("got here")    
# Find number of rows (and therefore columns) to iterate over
num_rows = len(cor_matrix[0])
#print(num_rows)


# Iterate over each cell and find minimum correlation
for i in range(num_rows):
    for j in range(num_rows):
        # Iterate over each correlation matrix and find minimum value
        min_value = 999;
        for k in range(1,num_samples):
            if (cor_matrices[k][i][j] < min_value):
                min_value = cor_matrices[k][i][j]
        final_cor_matrix[i][j] = min_value

num_rows = len(final_cor_matrix[0])

np.savetxt("fin_all_timepoints_min_spearman_corr_matrix.txt",final_cor_matrix,delimiter="\t")

#################################################
# PART 2: Network Analysis
#################################################

cor_matrix_df = pd.read_table("fin_all_timepoints_min_spearman_coor_matrix.txt",sep='\t',index_col=0)

graph = nx.from_pandas_dataframe(cor_matrix_df)

