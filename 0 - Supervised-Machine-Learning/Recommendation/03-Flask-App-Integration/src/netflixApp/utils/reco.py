# -*- coding: utf-8 -*-
import pickle
import numpy as np
import os
from utils.load import get_similarity_scores, get_idx_to_mid, get_mid_to_idx, \
    get_movies, get_movie_name

idx_to_mid = None
mid_to_idx = None
movies = None
similarity_scores = None

def load_files():
    global similarity_scores
    global idx_to_mid
    global mid_to_idx
    global movies
    similarity_scores = get_similarity_scores()
    idx_to_mid = get_idx_to_mid()
    mid_to_idx = get_mid_to_idx()
    movies = get_movies()


def get_sim_scores(list_mid):
    if isinstance(list_mid, int):
        list_mid = [list_mid]
    sims = []
    for mid in list_mid:
        sims.append(similarity_scores[mid_to_idx[int(mid)]])
    return sims

def get_ranked_recos(sims):
    recos = []
    sum_sims = np.sum(sims, axis = 0)
    most_similar_movies = np.argsort(-sum_sims)
    for index in most_similar_movies:
        recos.append((idx_to_mid[index], sum_sims[index], movies[idx_to_mid[index]]['title']))
    return recos

def get_reco(list_mids, N=5, exclude_selection=False):
    load_files()
    if exclude_selection:
        return get_ranked_recos(get_sim_scores(list_mids))[len(list_mids):N+len(list_mids)]
    else:
        return get_ranked_recos(get_sim_scores(list_mids))[:N]
    # [BONUS]: remove movies selected by user from final recommendations
    # when exclude_selection is set to True
    # We start by loading the files as global variable
