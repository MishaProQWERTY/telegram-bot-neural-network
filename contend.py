import tensorflow as tf
import numpy as np
import random
import json

checkpoint_filepath = 'assets/cp-0003.keras'
model = tf.keras.models.load_model(checkpoint_filepath, compile=False)

with open('assets/text_vec_vocabulary.json', 'r', encoding='utf-8') as f:
    vocabulary = json.load(f)


text_vec_layer = tf.keras.layers.TextVectorization(
    split="character",
    standardize="lower"
)

text_vec_layer.set_vocabulary(vocabulary)

def shakespeare_model(text=['']):
    input_vectorized = text_vec_layer(text)
    x = tf.keras.layers.Lambda(lambda x: x - 2)(input_vectorized)
    output = model(x)
    return output


def next_char(text, temperature=1):
    input_text = text[-30:]
    y_proba = shakespeare_model([input_text])[0, -1:]
    rescaled_logits = tf.math.log(y_proba) / temperature
    char_id = tf.random.categorical(rescaled_logits, num_samples=1)[0, 0]
    return text_vec_layer.get_vocabulary()[char_id + 2]

def extend_text(text, n_chars=50, temperature=1):
    initial_len = len(text)
    for _ in range(n_chars):
        next_c = next_char(text, temperature)
        text += next_c
        if '\n\n' in text[initial_len:]:
            break
    return text


def buildPhrase(text):
    l = extend_text(text + '\n\n', temperature=random.uniform(0, 1))
    l = l.replace(text + '\n\n', '', 1)
    return l