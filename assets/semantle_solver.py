#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 12:27:24 2022

This is a script to solve semantle

@author: smazurchuk
"""

import numpy as np
from scipy.spatial.distance import pdist, cdist, squareform
import gensim.downloader as api
from tqdm import tqdm

print("Hello! Welcome to the semantle solver \n")
# Load w2v model
print('Loading w2v representations')
wv = api.load('word2vec-google-news-300')
     

def main():
    print("""Let's start! \nTo restart, enter the word "restart" \n""")
    guess1 = input("First guess: ")
    sim1   = float(input("Similarity: ")) 
    model  = semantleSolver(guess1,sim1)
    while True:
        guess = input("Next guess: ")
        if guess == "restart":
            guess1 = input("First guess: ")
            sim1   = float(input("Similarity: ")) 
            model  = semantleSolver(guess1,sim1)
            continue
        sim   = float(input("Similarity: ")) 
        model.addGuess(guess,sim)
        
class semantleSolver():
    def __init__(self, word, similarity):
        self.guesses    = [word]
        self.guess_sims = np.array(similarity).reshape(1,1)
        self.cosine_similarities = ((1-wv.distances(word))*100).reshape(-1,1)
        self.get_nGuess()

    def addGuess(self, word, similarity):
        self.guesses.append(word)
        self.guess_sims = np.c_[ self.guess_sims , similarity]
        self.update(word)
        self.get_nGuess()
    
    def update(self,word):
        self.cosine_similarities = np.c_[self.cosine_similarities, (1-wv.distances(word))*100]
    
    def get_nGuess(self):
        distances = cdist(self.cosine_similarities,self.guess_sims)
        top15 = distances.argsort(axis=0)[:15]
        if len(self.guesses) > 1:
            formatedSims = [", ".join([f'{self.cosine_similarities[k,i][0]:.2f}' for i in range(len(self.guesses))]) for k in top15]
            words = "\n".join([f"{wv.index_to_key[int(k)]} \t\t {formatedSims[i]}" for i,k in enumerate(top15)])
        else:
            words = "\n".join([f"{wv.index_to_key[int(k)]}  \t\t {self.cosine_similarities[k][0][0]:.2f}" for k in top15])
        # Top Guesses
        print(f'########\nYour top guesses are: \n{words} \n###########')

if __name__ == '__main__':
    main()
