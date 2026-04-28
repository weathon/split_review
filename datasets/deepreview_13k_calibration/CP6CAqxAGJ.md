# Unifying Vocabulary of Large Language Model with Statistical Token-level Alignment

- Decision: Reject
- Avg Score: 5.67
- Scores: 5, 6, 6

## Abstract
Large Language Models (LLMs) achieve great success across many general tasks, but the mismatch among different vocabularies hinders further applications like token-level distillation and inference with various models. To align the vocabularies of LLMs, we propose a simple yet effective method named **UnifyVocab** to replace the vocabulary of an LLM at a limited cost. A new vocabulary alignment method is devised first to align the source vocabulary to the target one. We then rearrange the corresponding parameters like embeddings, and progressively fine-tune the model. Experimental results on models across multiple parameter scales demonstrate the effectiveness and generalization of UnifyVocab, which costs as few as 10B tokens to recover 98.02\% performance of the vanilla models on average. We further find that unifying the vocabularies significantly facilitates the token-level distillation which remarkably boosts (+4.4\%) the model with only 235M tokens. Moreover, our method provides a better initialization of multilingual vocabulary for LLMs to adapt to new languages.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes UnifyVocab, a method to replace the vocabulary of an LLM. 
This involves using a tokenizer from another model and training new GloVe embeddings, which are aligned with cosine similarity to an existing embedding set, and then are used to replace the original embedding matrix and finetuned with the model. 

Experiments use the Pythia base model and training corpus, and experiment with replacing the vocabulary with those from Gemma, Qwen2, and LLaMa 2 & 3.  
UnifyVocab is compared to a random initialization, random permutation, and FOCUS from Dobler & de Melo (2023). 
English results are compared across 6 standard tasks, and cross-lingual transfer is compared for 12 languages (+English) on 4 standard tasks.  
Results show that the method preserves on average 98% of the original performance, and leads to improved cross-lingual transfer compared to FOCUS. 
Two-stage tuning (first finetuning the vocabulary-related parameters in the model with the rest frozen, and then fine-tuning the full model) improves performance compared to fine-tuning the full model directly. 
Token-level distillation requires less training data and generally leads to improved performance over sequence-level distillation. 

The method, though, requires ~10B tokens for training, which is a significant cost compared to past approaches applied to e.g. machine translation where separately trained embeddings may be adapted to work with a model with <20k tokens. 
Aligning embeddings with cosine similarity assumes that a) similar representation spaces are learned and so an explicit alignment step is not needed and b) the vocabularies are near-isomorphic, which are not guaranteed with the procedure used, and these assumptions are not mentioned. It would be easier to trust that the results would generalize if these were explored here and for example an explicit alignment step compared and more specific analysis about the conditions where the method is and is not successful (for example, if 6% vocabulary overlap with Gemma and Pythia makes the model much slower to converge, how similar is this to random initialization? are the cosine similarities considerably lower in this case, and/or less one-to-one mappings chosen? if something other than cosine similarity were used, how would this change?)

### Strengths
Straightforward method to replace the tokenizer / vocabulary of an LLM, given sufficient data.

### Weaknesses
Method is costly and does not consistently recover original model's performance. Insufficient analysis to understand the conditions where the method will succeed.

Aligning embeddings with cosine similarity assumes that a) similar representation spaces are learned and so an explicit alignment step is not needed and b) the vocabularies are near-isomorphic, which are not guaranteed with the procedure used, and these assumptions are not mentioned. It would be easier to trust that the results would generalize if these were explored here and for example an explicit alignment step compared and more specific analysis about the conditions where the method is and is not successful (for example, if 6% vocabulary overlap with Gemma and Pythia makes the model much slower to converge, how similar is this to random initialization? are the cosine similarities considerably lower in this case, and/or less one-to-one mappings chosen? if something other than cosine similarity were used, how would this change?)

### Questions
Presentation note: only the best vocabulary replacement results in the tables. In Tables 4 and 5 there are times when the original Pythia model outperforms any of the replacement methods, and so should likely be bolded instead so that this is clear.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper tackles a vocabulary extension issue in LLMs and introduce a method called UnifyVocab to replace the vocabulary of LLM, aligning token IDs between two vocabularies. The proposed approach allows vocabularies of LLMs to get replaced based on the token-token co-occurences, enabling new vocabulary adaptation with lower costs. Experimental results show some effectiveness in (cross-lingual) knowledge transfer between models.

### Strengths
- proposes vocabulary adaptation technique which will be useful in multilingual/crosslingual LLM  application
- Experimental results show some effectiveness of the proposed approach in multiple multilingual NLP tasks

### Weaknesses
 - There is some missing citation on vocabulary adaptation like [1]. Comparison and/or discussion would be required.  
[1] OFA: A Framework of Initializing Unseen Subword Embeddings for Efficient Large-scale Multilingual Continued Pretraining. In Proc of NAACL2024 findings

### Questions
- Have you ever tried other (semantic) metrics like COMET scores instead of BLEU while evaluating the performance of alignment Matrix?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper wants to address the mismatch among different vocabularies used by various LLMs. UnifyVocab is proposed. The high-level idea is to use the embeddings of the tokens from the source tokenizer to initialize the embeddings of tokens from the target tokenizer. To achieve this, the authors train GloVe embeddings for the tokens in the source and target vocabularies respectively, and then align the tokens using the similarity between the source and target tokens.

### Strengths
- The paper is generally easy to follow.

- The experiments are extensive.

- UnifyVocab seems to be simple and effective in aligning tokens among the vocabularies of two tokenizers.

### Weaknesses
 - The method is sensitive to the selection of the corpus used to learn the token-token alignment.

- The pipeline is very similar to WECHSEL [1]. If I understand correctly, the method proposed in this work is a simple extension to the scenario where the source and the target languages are the same (in WICHSEL they are different).

- WECHSEL additionally needs to align the learned fastText embeddings because the source and target embeddings are in different spaces. I guess this step is omitted in UnifyVocab because the authors assume the learned token GloVe embeddings (for tokenizer A and tokenizer B) are in the same space. However, this assumption might not hold true. Two embedding matrices learned from the same corpus can be quite different, even if they have the same vocabulary (and in your case, this does not hold true) [2]. Specifically, the GloVe embeddings are trained independently for each vocabulary, and without any explicit alignment, there's no guarantee that the embedding spaces will be comparable. This could lead to suboptimal mappings between tokens.

- I am not sure if I agree the motivation of the paper is well-established. If a model performs well with its own tokenizer (e.g., LLama and the LLama tokenizer), why would one be interested in exchanging its tokenizer with another model's tokenizer that is intended to work on the same domain or language? I think replacing the tokenizer is mostly only meaningful when we want to have a new domain or a new language to adapt to.

### Questions
$\textbf{Questions/Suggestions}$:

- I don't think Figure 3 (b) is meaningful. The authors claim that there is a negative relationship between the first-step training loss nad the BLEU. But the BLEU is very very bad, only around 2.4. For such a small BLEU, the differences between different initializations are basically negligible.

- In Table 4, does "0" in the column "#Tune (B)" without any training? In other words, does that line indicate the performance of right after replacing the tokenizer? If it is, maybe the authors can make it more clear in the caption.

- It is better to use the same color and same order in the legend of Figure 3 for better consistency. 

- There is one related paper [3] for zero-shot tokenizer transfer. They proposed ZETT where a hypernetwork is used to predict embeddings of the new tokens in the target tokenizer. The authors may consider this as a stronger baseline method.


$\textbf{Typos}$:

Line 174: "which belongs both vocabularies." -> "which belongs to overlapping vocabularies."
Line 177: "randomly chosen token from the source vocabulary." -> "a randomly chosen token from the source vocabulary."


[3] https://arxiv.org/abs/2405.07883

### Soundness
3

### Presentation
2

### Contribution
2
