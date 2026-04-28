# Hierarchical Autoregressive Transformers for Tokenizer-Free Language Modelling

- Decision: Accept
- Avg Score: 7.00
- Scores: 8, 8, 5

## Abstract
Tokenization is a fundamental step in natural language processing, breaking text into units that computational models can process. While learned subword tokenizers have become the de-facto standard, they present challenges such as large vocabularies, limited adaptability to new domains or languages, and sensitivity to spelling errors and variations. To overcome these limitations, we investigate a hierarchical architecture for autoregressive language modelling that combines character-level and word-level processing. It employs a lightweight character-level encoder to convert character sequences into word embeddings, which are then processed by a word-level backbone model and decoded back into characters via a compact character-level decoder. This method retains the sequence compression benefits of word-level tokenization without relying on a rigid, predefined vocabulary. We demonstrate, at scales up to 7 billion parameters, that hierarchical transformers match the downstream task performance of subword-tokenizer-based models while exhibiting significantly greater robustness to input perturbations. Additionally, during continued pretraining on an out-of-domain language, our model trains almost twice as fast, achieves superior performance on the target language, and retains more of its previously learned knowledge. Hierarchical transformers pave the way for NLP systems that are more robust, flexible, and generalizable across languages and domains.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper proposed a technique for tokenizer-free language modeling. They design hierarchical processing to aggregate character-level embeddings into word-level embeddings. They achieved similar performance as models with word-level tokenizers while being more robust to input pertubation. They improved the continued pretraining speed when switching domain from English to German while maintaining the performance.

### Strengths
- A method of tokenizer-free langauge modelling that is more robust to input perturbation and input domain shift.

### Weaknesses
 - The proposed method only works for character-based languages.

### Questions
- I'm curious how the model works when doing inference in the same language but when the text is from a different distrubtion (out-of-domain).

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
I had wrongly entered the review of another paper - I have now corrected this. I apologise and commend the authors for having tracked down the correct review! 

They propose a hierarchical transformer model which does not rely on a tokeniser to preprocess the dataset into tokens of a fixed sized vocabulary. Instead it proposes an encoder decoder which takes words as a sequence of bytes and encodes and decodes the byte sequences into a word embedding which is then processed by a backbone transformer model. They show that this hierarchical model is theoretically computationally efficient in terms of FLOPs and performs well across a number of tasks. Furthermore they show that it is more robust errors than the baseline which rely on the fixed tokenisation from the original training corpus.

### Strengths
The model is well motivated as being a good balance between word and byte level representations. 
They scale these up to 7B which other hierarchical work did not 
They show their model is better than models which do not take word boundaries into account

### Weaknesses
They do not situate the work in the long history of hierarchical models, and character and byte based literature. Why is this paper the one that will convince us to move away from sub-word units? The case is not clearly made.
There are important details that they do not explain clearly like the dimensions of the backbone model, the test sets and their experimental design. They do not deal with the case of CKY languages.

In table 2 you show compute matched settings for the baseline and you model. They only match in terms of parameters for the first 1.1B model, for 3.1B your model is 4B, and for 7B your model is 9.2B which are both much bigger. Does this mean that they comparisons in Table 1 are unfair on the baseline and overestimate the advantage of your hierarchical model?

There is no explanation of the test sets in Table 1. In particular what is Lambada and why does the hierarchical model perform so well on it and what does this mean?

You do not explain the German Occiglot dataset - why is this considered out of distribution? The Llama model has likely seen quite a bit of German data.

### Questions
Why not discuss in more depth how this work relates to other work on byte/pixel/character based models? This is a fundamental shift in the transformer paradigm and has a lot of implications. More discussion here would have been welcome. Eg. Mielke, Sabrina J., et al. "Between words and characters: A Brief History of Open-Vocabulary Modeling and Tokenization in NLP." Computing Research Repository (arXiv) (2021).

How would your model cope with languages without whitespace characters as work separations eg. Mandarine? How would your model handle CKY languages with tiny vocabularies, or multilingual models which include CKY and many other scripts?

4.2 It was not clear what the relationship between the backbone and the encoder was. You say you keep the backbone to the 1:1 aspect ratio - what did you mean here? And if you chose the encode to be (8,4) what does this mean for the backbone/encoder? You have 8 heads and 4 layers on the encoder and decoder - but what do you have on the backbone - not clear!

In table 2 you show compute matched settings for the baseline and you model. They only match in terms of parameters for the first 1.1B model, for 3.1B your model is 4B, and for 7B your model is 9.2B which are both much bigger. Does this mean that they comparisons in Table 1 are unfair on the baseline and overestimate the advantage of your hierarchical model?

There is no explanation of the test sets in Table 1. In particular what is Lambada and why does the hierarchical model perform so well on it and what does this mean?

I like Figure 4! It clearly shows that the hierarchical model is more robust.

You do not explain the German Occiglot dataset - why is this considered out of distribution? The Llama model has likely seen quite a bit of German data.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The authors propose a method to avoid large lookup table in word-level tokenization by utilizing a small character-level lookup mechanism. They employ a light weight character level encoder to convert character sequences into word embeddings, which are then processed by a word-level backbone model and decoded back into characters. Compared with subword tokenization, word-level tokenization with character-level lookup reduces the lengths of sequences processed by the backbone LLM and allows a larger number of parameters under the same computation budget.

### Strengths
1. Compared with subword tokenization, word-level tokenization reduces the lengths of sequences processed by the backbone LLM and allows a larger number of parameters under the same computation budget.
2. Experiments show the proposed method is more robust to input perturbation and cross-lingual continued pretraining.

### Weaknesses
1. **I disagree with the claim that this method is tokenization-free.** Actually, it does employ a word-level tokenization approach. It heavily relies on a space-based tokenization mechanism. The backbone autoregressive model operates on word-level embeddings.
2. **The primary contribution of this work seems to be more like "how to avoid a large lookup table in word-level tokenization." The proposed method addresses this issue by utilizing a small character-level lookup table.** It aggregates the embeddings of individual characters within a word during encoding and employs an autoregressive model to decode each character from a word-level embedding during inference.
3. Clearly, this method cannot be applied to languages without using an alphabet system (e.g., Chinese, Japanese) or without a space tokenization mechanism (e.g., Arabic, Thai). Therefore, the adaptation experiments in Section 4.6 is not very convincing, which chooses languages from the same language family.
4. The contribution appears incremental compared to Megabyte [1]. **While Megabyte employs a fixed patch size, this work utilizes a predefined tokenization mechanism to segment each patch. However, this predefined tokenization approach reduces the flexibility of the method, preventing it from being considered tokenization-free.**

### Questions
Please see the weaknesses.

### Soundness
1

### Presentation
3

### Contribution
2
