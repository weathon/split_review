# Depth Extrapolation of Decoders Trained on Nested Structures

- Decision: Reject
- Scores: 6, 6, 3, 3

## Abstract
Reasoning problems with deeply nested formal statements are challenging for humans and machines alike. We investigate how next-token predictors learn such structures, and whether they extrapolate to more deeply nested cases, within a single inference pass. A case study of Boolean logic simplification demonstrates that a specialized decoder Transformer seems to perform well when it overfits, but fails at extrapolating. To understand if this limitation is universal, we propose a theoretical grounding of memorization in a self-attention head. We apply this theory to a simpler problem: completion of a bounded stack of parentheses. From the theoretical construction we derive a closed-form model that perfectly fits a single sequence training set. We prove that it also completes any out-of-sample parentheses prefix, regardless of the context depth. In contrast, we observe that decoder Transformers trained with gradient descent on this task fail at depth extrapolation. Gradient-trained decoders demand large samples and a high-dimensional embedding space to achieve high accuracy on test sets nearly as deep as the training set. However, when the gap between training and test depths widens, gradient-trained models fail.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper studies how Transformer learns bounded hierarchical language and how the model extrapolates over different depths. They present a theoretical construction of a 1-layer Transfomer with learned position encoding that can memorize a long training data and generalize over any depths. They further show through experiments that in practice, the model learns very different solutions.

### Strengths
1. The paper presents an interesting construction for Transformer that can generate the Dyck language, which is very different from any previous works.

2. The paper presents a vast range of empirical studies to justify the theoretical assumptions and also strongly show that the learned architecture is different from the generalizable architecture the paper constructed.

### Weaknesses
1. While the construction that the authors presented can successful generate valid dyck sequence for any valid dyck prefix, it will not minimize the pretraining loss. For example, consider a training set that contains multiple sequences (which is the setting in the experiments) and two sequences have shared prefix and different conclusions, the current construction would not be able to minimize training loss. This seems to explain the discrepancy between theory and experiments, and shows that the construction is restricted to the single sequence authors considered.

2. The depth generalization setup is studied in previous works [1] and the authors haven't provided a thorough discussion on how the current results differ from them.

### Questions
1. How to accomodate the current theoretical result to setting with multiple sequences (see weakness 1)?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper studies the ability of transformers to extrapolate reasoning on harder tasks by studying their behaviour on boolean expression and dyck languages. The authors first show that transformers are can not reason beyond the given depth q of a clause, that is, while the transformer models do quite well on "in-sample" data, i.e, data that matches the same complexity (in terms of depth and number of clauses) as the training data, the fails to extrapolate the reasoning beyond that. 

Next, the authors study the ability of transformer models to study Dyck languages with a single layer and single head Transformer model. Here the point is to show the effects a learned position embedding could have towards memorization of LLM towards the input data.  The authors show that when training the models over one data distribution, under the conditions when Q = 0, based on the value, the learned position embeddings can sometimes force the model to complete a sequence in a way that it sees during training.

### Strengths
- The observation on training over more difficult depth enables better performance over relatively simpler depth $q$ is quite interesting!

- The result in Theorem 3.1, which shows that for appropriately scaled value $v$ and $\gamma$ parameter, the model can either correctly predict the sequence, or get worse (i.e, in the case when $\gamma$ and $v$ have opposing signs and are small).
- The experiments with dyck languages and how the position encoding effects the training of the model is very interesting. The authors show that sometimes the learned position encodings could be the reason why the model chooses to finish a clause the way it does. That is, it memorizes. 

- Through their experiments on deeper layers and larger embedding dimensions the authors show that they learned models when trained on sufficiently large number of samples are able to do well on validation set. 
- The observation on the fact that the value functions can be approximated by $-vI$ is pretty interesting. esp given the theory results.

### Weaknesses
 - I am curious as to why we expect a model like GPT to reason about and do well on the reasoning for boolean clauses task, especially when the depth increases. That is not what the model is trained on, and could also be quite a difficult task for humans to solve. I realize that this is not the main focus of the paper, but expecting an LLM to do well on a boolean logic simplification task seems to be asking for a bit much.
- It seems like the theoretical setup is too simplistic.
	- The authors make a key assumption here that the Query is 0. If the Query is not zero, would the dependence on the position encodings still be as great, esp if the inner product between the query and value is high?
	- The results on multiple sequences assume that the tokens in each sequence are also independent, which basically is a small extension of the single sequence result.
       - How would tokens that are not iid change the results?
- What is the intuition of $\gamma$? what effects does it have on the position encodings? Can the authors elaborate on that? 
- Some of the experimental results are not surprising (given their lack of ability to also length generalize), i.e, the generalization to deeper depth getting more difficult as the training data complexity is further and further away from the testing data complexity.

### Questions
- some of the notation and terms used is a bit unclear. Where does $\gamma$ come from? Is $\gamma$ something that the authors *fix* themselves, i.e, is part of the constructed solution to the position encodings?
- The authors use the term out-of-sample basically validation set (i.e, data with the same properties as the input data) and in-sample samples from the training data?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This papers considers decoder transformers trained on boolean simplification and dyck language completion tasks. Evidence is given that models trained on those tasks often fail to extrapolate to unseen expression depths.
For a dyck language completion, an analytical solution for a 1 layer, 1 head transformer with 1 embedding dimension is derived, capable of arbitrary depth generalization, and its stability properties are analyzed.

### Strengths
- I enjoy the analytical transformer solution, showing that this problem should indeed be solvable with the given architecture.
- Figure 1 and the associated analysis on stability given $\lambda$ is insightful.
- The approach to try to minimize the design space is generally pleasing, although that comes with a weakness (bullet 1)
- I like the consistent formatting of showing “Training setup”, then a Figure, and then “Observations”. This is something I will employ in future papers.

### Weaknesses
 - I question the validity of restricting the general attention mechanism (like setting $Q = 0$), where the only constraint on the restriction is that there still exists a solution in the resulting function space. One has to be very careful what kind of conclusions can be drawn from that. This procedure is baking in (possibly extremely useful) inductive biases that a model has a hard time learning with finite data. Specifically, setting $Q=0$ eliminates the possibility of the model learning to attend to different parts of the input sequence based on the query, which is a core feature of the general attention mechanism. This drastically simplifies the model and may not reflect the behavior of standard transformers.
- Related to bullet 1: Something I am missing here are the ablation studies of piece by piece hard-coding the inductive biases used to define the generalizing 1-d model to see which of those biases are important for model training. Those biases are:
1. Setting embeddings to -1 and +1 (or opposite sign vectors of the correct dimension)
2. $Q=0$
3. $V=vI$
It would be beneficial to see how performance changes when each of these constraints is relaxed individually, to understand their relative importance. For example, what happens if the embeddings are initialized randomly, or if Q is a learnable parameter? This would help to isolate the critical inductive biases for generalization.
- The writing is quite confusing. Section 2 and 3-5 seem somewhat disconnected. I don’t need a boolean simplification example to introduce dyck language completion, it seems like “fluff” to make the paper longer. I was often confused while reading, and only sometimes had “aha” moments much later. The evaluation protocol in Sec 4.2 is very unclear. It is not clear how the training and test sets are constructed, especially with regard to the depth parameter q. The paper would benefit from a clearer explanation of how the training data is generated and how the out-of-sample test data is created, especially when training on a range of q values and testing on a different range.
- I find the evidence in Fig 3 unconvincing. The second largest singular value is positive. Also it looks like this is only one model. For different seeds, is the largest singular value always negative? It is unclear what the authors mean by the “value matrix (times projection transpose)”. The connection between the low rank of this matrix and $V=-vI$ is not clearly explained. The authors should provide a more detailed explanation of the spectral analysis and its implications.
- After having read the paper, I am unsure what to conlude. What knowledge am I supposed take away from this paper? On a high level, it seems “models fail to extrapolate in some way (in this case nesting depth), even though they have computational capability to succeed”, which I don’t think is a very novel conclusion at this point. However, breaking it down to a setup this minimal is a good step!

### Questions
- Table 1: Are these results from training q≤N or only q=N? Your table suggests the latter while the “observations” section suggest the former.
- Table 1: it is quite interesting that train q=2/test q=3 in-sample is (top-left) is worse than train q=5/test q=6 oos. Do you know why?
- You say you train on 7.3e10 tokens in 7.2e7 sequences. Do you somehow make sure the #tokens/ seq is the same for different q? Or do the numbers refer to the union of all training sets? I’m wondering whether my previous question can be explained by an increased number of training tokens
- Fig 2 (left) is on a held out sample? how big is the training set there?
- I am not sure I grasp the evaluation protocol of Fig 2 (right). Training happens on q≤4,8,12, and the evaluation is actually on q ≥ 9 (or 12? or 13?) Please make this clearer, I am very confused.
- Page 8, “Observations”: Except for d=2, it does not look to me like the models’ performance clusters by embedding dimension. Where do you see that?
- It is unclear to me which singular values you are plotting in Fig 3. The “value matrix (times projection transpose)”. What is that? How does a low rank of this thing indicate $V=-vI$ ? I think it helps if you write that down in the section.

### Nits:

- Is it normal that the line numbers are not well aligned with the text? I give approximate line numbers.
- L192:  $E_{s_{i,:}}$  is indexed incorrectly
- it is kind of weird to denote the set of $\mathbf{s_i}$ as $\mathbf{s}$, since that set should also have an index $r$
- the explanation on why $\lambda < 0$ attracts and $\lambda > 0$ repulses could be clearer, you explain it better on Page 15 “Generalization”, but please link to that in the main text (sec 4.1).
- Fig 2 (left) is missing a y axis label. Was the intention to share the label with Fig 2 (right)?

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The authors investigate at what level decoder-based transformers handle nested formal statements, with an example on boolean logic simplification. They train a small (8 layers) decoder-based transformer that out-performs larger models, and show it relies on memorization.
The authors develop a theory of memorization in a similar toy case, and use it to develop a closed-form model that, given a single training example generalizes and outperforms larger pretrained models on Dyck language related tasks.

### Strengths
The ideas presented in the paper seem interesting.
For example, the authors' framing of memorization into a toy closed form model seems original and interesting.
Another positive example for originality is the usage of a specific problem with varying levels of difficulty (i.e. the simplification of boolean expressions with varying depths) to test large models for generalization is neat. I am personally unfamiliar with other works who did this (but this isn't my specialty).

### Weaknesses
The paper is written rather poorly, and is difficult to follow. This is exemplified in several points - 

**1.** In the abstract:
    1.1. The main points in the abstract are not clear. Is the main contribution the closed form presentation of memorization? Or the application of this on the nested sequence modeling? I think a better, more ordered presentation is required. 
    1.2. Generally, the abstract contains sentences which is unclear how they relate to each other. For example, it is unclear how the sentence "We elicit relations between positional and token embeddings, which explain how large embedding dimensions scale with context size and number of topics in the training set." relates to the previously-presented nested formal statements. Another example is the last two sentences of the abstract, which mean the same thing (at least to my understanding) but are connected with a contradiction ("However"), and it's unclear how they relate to earlier parts.

**2.** Some experiments presented in the paper do not reveal new information, and it is unclear how they relate to other sections. For example, the goal of the analysis in section 2.2 is unclear. I think that the statement by the authors "This finding suggests that training data must contain samples as close as possible to the test set" isn't new, and it's unclear how the results in this section are related to following sections. The authors do not provide a clear motivation for why this specific experiment is necessary to support the overall claims of the paper, and how it relates to the core idea of memorization versus generalization.

**3.** Unclear notations make it difficult to follow the complex claims in the paper - for example, γ appears first in line 232, but undefined anywhere near there. Another example is the matrix V, shown in line 203 (presumably the value weight matrix of the attention mechanism) but not properly defined anywhere. The authors also mention concepts early on (e.g. "a single attention head model") but don't describe them until much later (and sometimes not at all). The lack of clear definitions for key variables and model components makes it exceptionally challenging to verify the theoretical claims and understand the experimental setup.

**4.** There are many irrelevant references - e.g. in line 104 - "See Appendix" has no valid reference to any appendix.

The above points make it **very difficult to closely follow the lemmas and proofs to verify their correctness**, as well as to understand the main claims made by the authors.

Another weakness is the experimental soundness - many experiments (the ones I was able to follow) don't seem to be rigorous. For example, the experiment of measuring large model accuracy on boolean logic simplifcation (line 104) reports 90% accuracy, but in the appendix the authors mention they only tested 10 samples with depth 1 and only 5 samples of depth 3, which **isn't enough test samples to say anything meaningful**. Furthermore, the lack of error bars or statistical significance tests makes it difficult to assess the reliability of the reported results.

In addition, another weakness is the application of these supposed findings on real cases, other than the simple toy case (of a single attention block with a specific type of positional embedding). There doesn't seem to be any implication it will generalize to real models.

### Questions
1. In section 2.2 the authors claim that language models often return wrong simplifications of boolean expressions. Did the authors verify permutation equivariance? e.g. a simple case - (p3 & p2) should be considered the same as (p2 & p3). If so, this should be explicitly stated.

2. In section 2.1, why did the authors choose these specific values for the model? Were other settings, that might lead to better performance, considered?

### Soundness
1

### Presentation
1

### Contribution
2
