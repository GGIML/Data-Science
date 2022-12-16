import logging
from tqdm import tqdm

import nltk
from nltk.corpus import wordnet as wn
from pytorch_pretrained_biggan.utils import IMAGENET

nltk.download('wordnet')

logging.basicConfig(level = logging.INFO)
logger = logging.getLogger(__name__)

def generate_raw_dataset(patterns=['i saw a <WORD>.'], tokenizer=None):
    """ Utility function to generate a dataset of string sequence associated to each imagenet class
        Args:
            - patterns: a list of string to use as patterns in which <WORD> will be replaced by
                a word related to each ImageNet class (e.g. dog, fish...).
                Example of pattern: 'i saw a <WORD>.' will be converted in 'i saw a dog' for the ImageNet class associated to dog.
            - tokenizer: a tokenizer from Transformers library.
                List of possible names: https://huggingface.co/transformers/pretrained_models.html

        Returns: dictionnaire that maps each ImageNet class to a list of sentences following the patterns provided
    """


    # The IMAGENET dict provided in pytorch_pretrained_biggan is
    # a dict of {wordnet.synset_offset: ImageNet class index}
    # For more informations on ImageNet classes relation with wordnet:
    # see http://www.image-net.org/download-API
    # Let's inverse the dict and link it with wordnet synsets:
    class_to_synset = dict((v, wn.synset_from_pos_and_offset('n', k)) for k, v in IMAGENET.items())

    # %%
    # Some classes in ImageNet are associated to complexe and rare words like breeds of dog
    # To make it simpler for us in the first step, we'll filter the words
    # to associate a more common word to each class or remove the class if we can't find a
    # common word or if all the common words associated to the class are already taken.
    # A common word here is a word that is in Bert tokenizer vocabulary.
    logger.info('Building a list of simple words associated to ImageNet classes')
    words_dataset = {}
    all_words = set()
    for i, synset in tqdm(class_to_synset.items()):
        current_synset = synset
        while current_synset:
            for lemma in current_synset.lemmas():
                name = lemma.name().replace('_', ' ').lower()
                if name in all_words:
                    continue  # Word is already assigned
                if tokenizer.convert_tokens_to_ids(name) != tokenizer.unk_token_id:
                    # Word is in Bert tokenizer vocabulary
                    words_dataset[i] = name
                    all_words.add(name)
                    current_synset = False # We're good
                    break
            if current_synset and current_synset.hypernyms():
                current_synset = current_synset.hypernyms()[0]
            else:
                current_synset = False

    # Now let's build a simple sentence for each ImageNet category
    # to use as input to our language model
    logger.info('Building a list of sentences associated to each selected ImageNet class')
    # Here we only provide one simple pattern but better ways
    # to build a diverse dataset could be used.
    examples_dataset = {}
    for i, word in tqdm(words_dataset.items()):
        sent_list = []
        for pat in patterns:
            sent_list.append(pat.replace('<WORD>', word))
        examples_dataset[i] = sent_list

    return examples_dataset
