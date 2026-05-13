# Beyond Scaling Laws: Understanding Transformer Performance with Associative Memory

- Decision: Reject
- Scores: 5, 8, 6, 8

## Abstract
<- trailing '%' for backward compatibility of .sty file
Increasing the size of a Transformer does not always lead to enhanced performance. This phenomenon cannot be explained by the empirical scaling laws. Furthermore, the model's enhanced performance is closely associated with its memorization of the training samples. 
We present a theoretical framework that sheds light on the memorization during pre-training of transformer-based language models. We model the behavior of Transformers with associative memories using Hopfield networks, such that each transformer block effectively conducts an approximate nearest-neighbor search. 
In particular, the energy function in modern continuous Hopfield networks serves as an explanation for the attention mechanism, which we approximate with a distance-based energy function. By observing that the softmax function corresponds to the gradient of the LogSumExp function in the energy, and employing the majorization-minimization technique, we construct a global energy function designed to capture the layered architecture. We demonstrate a dependency between the model size and the dataset size for the model to achieve optimal performance, and we show that the achievable cross-entropy loss is bounded from below.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces a theoretical framework for studying *causal* Transformer models and their scaling properties from the perspective of Associative Memories. The paper studies a "stacked" colelction of attractor energy functions to model a multi-layered Transformer where the argmin of one layer's energy is passed to the next layer. The next layer will further optimize its energy function in the local region around the output of the first layer, and so on. The authors validate their theoretical claims on vanilla transformers and GPT models.

### Strengths
(S1) **A novel theoretical analysis** of transformers. The paper describes a causal transformer as a sequence of energy functions (but these energy functions only model attention, see weaknesses) that serve as surrogates for optimizing a global energy function (eq. (6)) according to  the MM algorithm. This is an interesting perspective that could shed light on what the fundamental operation of a transformer could be.

### Weaknesses
(W1) **The equation for $E_{MCHN}^\beta(x)$ [L250] is incorrect (or at the very least undefined)**, since $M$ seems to be written as a linear operator over a vector of dimension $n=T_{\text{max}}d_{\text{emb}}$, which is not the attention operation of transformers because the `LogSumExp` in this equation is the summation index over the memorized examples instead of the sequence dimension... Could the authors please clarify this equation? If it is incorrect, the following propositions in the paper no longer hold.

(W2) **The equation for attention [L203] is incorrect**. $Q$, $K$, and $V$ should each have a sequence dimension, whereas no sequence dimension is mentioned in this equation. Is this intentional or a typo? Given my other reservations about the soundness of the analysis, I am inclined to believe that the authors misunderstand the attention operation of transformers.

(W3) **Assumption 1 is a BIG assumption**. Assumption 1 assumes that *every sample in the training set is memorized verbatim* as a vector of length $n$, which is not a reasonable assumption for an LLM or even any Associative Memory trained on abundant data. Can the authors discuss the implications of this assumptions not holding in real-world scenarios? Or provide some empirical evidence/theoretical justification for why their results might still be relevant despite this assumptions?

(W4) **Eq (5) shows optimal $x^{(t)}$ being passed to the next layer $t+1$**. However, the update rule of a vanilla Transformer is not guaranteed to minimize the energy $E_{t}(x)$ and I wonder how the authors could have made the assumption that each step returns the `argmin` of the energy function for a particular layer. Vanilla transformers (using the config specified in App. F.1) are allowed to learn any value matrix in the attention, which could lead to the defined energy *increasing* after each update and not satisfy the assumption of Eq. (5)

(W5) **Unconvincing (and arguably unrelated) empirical results**. This is a fundamental weakness of the paper. The empirical results study vanilla Transformer architectures: architectures that include layer normalization and feed-forward networks, do not use the proposed metric in $g(x)$ from Eq. (2), whose update rule is not guaranteed to minimize the energy function on L250, and whose attention operation is not reasonably modeled by Eq. (4). I don't know how to reconcile this weakness. Given the fundamental incompatibility with the experimental results and the actual Transformer architecture, I am surprised that the theoretical results "align closely" [L449] with the empirical results and would ask the authors to dig deeper into why this could be the case.

(W5) **Overloaded notations make exposition unclear**. The mathematical notation $d$ is a little confusing. It represents:

1. The number of samples in the training set or validation set [L148-149]
2. The embedding dimension of each token [L152]
3. The metric [L156]

**Summary**

As mentioned in the Strengths section above, I find the perspective of MM as a description of what the Transformer architecture is doing fascinating. I am willing to reconsider my score if the authors can clarify where I have fundamentally misunderstood the paper. I cannot recommend this paper in its current state for acceptance.

### Questions
(Q1) Why bother making a distinctive definition of a validation set at all? If $\tilde{\mathcal{D}} \subset \mathcal{D}$ [L191] i.e., the validation set is some subset of the memorized training points, why consider it at all?

(Q2) The analysis of sections 4 and 5 seems to have nothing to do with the actual transformer architecture. 

(Q3) [L348-352] The attention softmax is irrelevant to the final cross-entropy, and including this statement here only confused me. Can the authors justify why we care about the softmax in the attention when considering the softmax in the cross-entropy loss?

**(More) Typos:**
- Eq (3) has incorrect indices of summation, if it is supposed to align with $E_{\text{MCHN}}$.
- L252: Typo, the definition of LogSumExp RHS uses $\rho^{i}$, when the function is defined in terms of $Mx$.

**Improvements**
(I1) Scaling laws (eq (1)) $N$ and $D$ are not defined. Is $N$ the same as the definition in line 153? Is $D$ the same as the definition in line 151? If so, please put these definitions closer to when they are first introduced

(I2) [L122] A bit non-standard notation for the partition function $Z_{\theta}$ -- generally this is expressed with integrating variable `dx` on the RHS

**Additional Comments**
(C1) The following statement is deceptive:

> As the attention layers and the FF layers contribute to the majority of the model’s parameters...

This is only true when we ignore the embedding and unembedding layers of a Transformer, which can be incredibly large with large vocab sizes. For smaller transformer models with large vocab sizes, it is possible that the embedding and unembedding matrices dominate the parameter count. 
Take for example `Model 1` in App F.1, where the number of parameters in the embedding+unembedding layers given the vocab size is ~96M parameters, whereas the reported total number of transformer params is 40M.
Please clarify, perhaps "The MHA and FF layers account for most of the parameters outside the embedding/unembedding layers" or "The fundamental operations of the Transformer are the MHA and FF layers", since parameter count is not the reason why you are focusing on these operations.

(C2) A gripe: the authors treat their version of the transformer as "standard", when it is arguably wrong or at least far from standard. This is summarized in the following quote from L419-420

> Also, modifications to the transformer blocks, such as additional layer normalization may contribute to the lower bound of the cross-entropy.

It is an open challenge to get high-performant transformers without normalization, and all modern transformers (including the models tested in this work!) use some form of normalization.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper investigates the scaling laws of transformer models, under the lenses of energy-based models, specifically, Hopfield networks. The authors expand on the classic work of Ramsauer on MCHNs, and show how hierarchical models can be described using a simpler energy function, based on the euclidean distance instead of the dot product, that implements a kind of nearest neighbor. Such an energy function is not local anymore (that is, it is not the sum of the energies of the single layers).

### Strengths
The analysis in well made, the problem tackled is an important one in the literature, and the work is well structured and clear. Furthermore, the connection with the nearest neighbour search is (to my knowledge) novel. The experimental evaluation is also well performed.

### Weaknesses
The section on cross entropy loss is a little less clear than the rest of the work: Maybe you could add another ‘proposition’ or a statement that summarizes the results of the second part of the section?

Scaling laws in the related works: N and D are never introduced. 

“*It has been shown that the feed-forward layers can be interpreted as persistent memory vectors, and the weights of the attention and feed-forward sub-layers can be merged into a new all-attention layer without compromising the model’s performance*” This part is not well explained in the introduction in my opinion: could the authors dedicate to this a couple more sentences? Or, remove it and leave it as it is later in the paper?   

The provided energy function is not ‘local’, as it is in other energy based models such as standard Hopfield networks, predictive coding, etc. This is quite interesting. However, I feel there is little discussion on the consequences of this. Why is this important? What does it tell us that is different from the previous literature?

### Questions
Using the euclidean distance inside an Hopfield networks: This has already been done, and it has shown good performance in simple image retrieval tasks [1]. Hence, interestingly your approach could be seen as using universal Hopfield networks to model the energy function of the transformer model.    


[1] Millidge, Beren, et al. "Universal hopfield networks: A general framework for single-shot associative memory models." International Conference on Machine Learning. PMLR, 2022

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
Nowadays, it is common to scale up a Transformer model to achieve great performance across a variety of tasks. However, increasing the size of the model does not necessarily lead to performance improvement. Meanwhile, an interesting phenomenon occurs--as the model's ability to memorize the training samples so does its generalization ability. Consequently, this work provides a theoretical framework which elucidates the memorization process in the Transformer model via the lens of Modern Associative Memory or Hopfield models. The contributions include a novel analysis of memorization in each Transformer block as a function of modern Hopfield energy, and mathematical illustrations of the dependency of the size of the model and dataset respectively that is needed for the model to attain optimal performance. Such illustrations highlight the optimal cross entropy loss is bounded by a constant.

### Strengths
1. The paper highlights the characteristics (i.e., pros and cons) of the Modern Hopfield Network's energy function given high dimensionality and continuous values, while providing an alternative energy function which maintains convexity. This energy function, i.e., logsumexp of a euclidean distance between a target $x$ and a stored pattern $\rho^{(i)}$, describes the dynamic of each Transformer block as an associative memory retrieval system.

2. Using the above (layer-wise) energy function, the paper also introduces a global energy function which accounts for the stacking of homogenous blocks in Transformer model. This particular global energy function enables the description of probability density function of the entire Transformer model. Using this description, the paper works out the optimal condition for the partition function $Z$ relating back to the scaling law from [Hoffmann et al (2022)](https://proceedings.neurips.cc/paper_files/paper/2022/file/c1e2faff6f588870935f114ebe04a3e5-Paper-Conference.pdf).

3. The paper also provides fantastic mathematical descriptions of memorization using their proposed energy function.

### Weaknesses
1. The authors might not be aware of this paper due to its title. But the proposed energy function (eq. 3) in the paper was recently introduced/used in [Saha et al. (2023)](https://proceedings.mlr.press/v202/saha23a/saha23a.pdf), with the exception that they use $\beta$ in their formulation and descriptions of the function's properties. However, I do not think this fact compromises the novelty of the work.

2. Much of the current analyses of storage capacity in Hopfield models relies heavily on uncorrelated patterns. Consequently, the claim of exponential capacity does not necessarily hold true for natural (or correlated) data. Similarly, a weakness of this work is assumption 3, since the work focuses on text data. The authors can instead make a claim that the Transformer blocks are storing the latent data, obtained from passing the text data to an embedding layer ---which should be much more uncorrelated--- to reinforce their narrative.

3. The writing for the experimentation is unclear, especially to unfamiliar readers. For example, I think the authors should elaborate more on the findings of the mean and median nearest neighbor distances, and why such results corroborate eq. 12. Finally, I'm not sure what section 6.3 is trying to demonstrate. How was $\sigma$ chosen? To find $D^*$, you would have to train multiple models across a variety of data sizes $D^{(k)}$ for $k=1...M$ sizes. Perhaps, there should be an elaboration on the selection of the size of different models and each chosen data sizes in relation to $N \approx \frac{A l d_{max}}{T_{max}} n$ and $D = T_{max} n$. The inclusion of these details should fortify the reasonings behind these experiments.

### Questions
1. Is it possible to collect the activation outputs up to 5% of the documents? If it's not possible due to limited compute, I understand. However, I think collecting activation outputs from 1% of the documents might be too limited. 

2. I believe you forgot to include the citation for RMSNorm, see the paragraph which describes the hypersphere volume on page 8 of the manuscript and where you mentioned LayerNorm.

3. In the description for the cross entropy loss $L$ in Proposition 4, you should perhaps replace that equation with eq. 13 in appendix D, since there is a mention of $c$ which is not found in the equation in the main text. 

4. There is an inconsistency in labeling the equations in the main text. Please organize them better since the mathematical descriptions provided in this paper are great. For example, I understand that $N \approx \frac{A l d_{max}}{T_{max}} n$ and $D = T_{max} n$ is mentioned in the prior sections of the manuscript. It is still certainly an important equation to be labeled/numbered.

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper looks at the performance of transformer-architecture models, particularly looking at the performance of such models with respect to the number of parameters. Recently proposed scaling laws may not reflect the true effect of parameter count on performance, and some smaller transformers outperform larger ones. The authors employ associative memories to model the behavior of transformers, specifically modelling each transformer unit with a single Hopfield network. Individual Hopfield energies are analyzed in a fashion similar to the Majorization Minimization technique. This allows an energy function to be associated with a transformer block, from which the paper forms a "global energy function" over the entire model. The global energy function relates the transformer size, the dataset size, and the optimal performance of the model. In particular, the authors find that the optimal loss is bounded by a constant term. Experiments are conducted that corroborate these results using a variety of transformer architectures on several datasets. Although some of these experiments were bounded by the computational resources (the authors note the work could be considered preliminary investigations) the results are still seemingly in agreement with the theoretical predictions made in previous Sections.

### Strengths
This paper offers a theoretical analysis of the optimal loss for transformer-architecture models, which is corroborated in practical experiments. A novel energy function for the Dense Associative Memory (which the paper refers to as the Modern Continuous Hopfield Network) is proposed, which gives interesting behaviors in comparison to the original energy function from Ramsauer et al. 2020. The work is robustly proven with mathematical analysis that is rooted in both statistical mechanics and prior work on associative memories, and is hence of great quality. The clarity of the paper is reasonable, with the caveat that much of the theoretical work is based in mathematics that is reasonably dense, and is often deferred to the appendix. The theoretical findings appear very significant in the context of transformer-architecture models, although the experimental results may not be as strong in this regard.

### Weaknesses
Several decisions / assumptions of the paper are made without discussion that would be useful for the reader. For example, it seems that all training set patterns to be stored explicitly in memory for the proposed energy function to be implemented, which is contrary to the traditional understanding of an associative memory. Almost all of the mathematical proofs are relegated to appendices, which is somewhat disappointing considering how vital these are to the main body of research.

### Questions
A slight nitpick, but on line 060 the authors state that the Hopfield network has only been recently generalized to continuous values. However, the continuous value Hopfield network was introduced only shortly after the 1982 paper. See Hopfield, J. "Neurons with graded response have collective computational properties like those of two-state neurons", 1984. The Dense Associative Memory (Modern Hopfield Network), introduced by Krotov and Hopfield 2016, was generalized to continuous values by Ramsauer et al. 2020, so perhaps this is what the authors intended? Reading on, this is discussed more in Section 2, subsection on Hopfield models, so my apologies for citing literature the authors are aware of! A slight rephrasing of line 060 may still be prudent.

The discussion on Hopfield models in Section 2 is excellent, but towards the end (e.g. works on the Energy Transformer and U-Hop networks) are seemingly only tangentially related to the main text. These could be left in for completion, but are they necessary for a reader's understanding of the main text? Perhaps with more explicit ties in later sections these would make more sense for a reader.

Section 3 lays out the model architecture. Section 3.1 discusses the associative memory formulation and how sequences of tokens may be interpreted as patterns in associative memories. Since each prediction will have access to a different number of previous tokens (e.g. predicting token 5 will have access to 4 previous tokens, predicting token 6 will have access to the previous 5, and so on) does this mean the associative memory here must be capable of handling retrieval for patterns of different lengths? Or are all patterns to be padded to a uniform length, such as in a traditional transformer, in which was the associative memory would have a much lower proportion of initial contents for subsequences that are early in the task (e.g. predicting the 5th token compared to predicting the 500th)? Perhaps I am misunderstanding the associative memory structure or pattern structure here? The initial paragraph of Section 3 seems to imply the latter, that all patterns are equal to the maximum token length. Is this correct? If so, how does this affect the retrieval of patterns that have only a small number of tokens available?

Definition 1 is a nice formalization of storage and retrieval in (continuous) associative memories. The condition that the intersection of any two balls must be null seems superfluous, however. If the intersection of B_i and B_j exists that would imply that the same point (i.e. any point in the intersection) would converge to both rho^i and rho^j, which is impossible. Unless this formalization of the associative memory somehow allows for multiple points of convergence? Is the condition of null intersection required for this definition, or could it be removed / discusses as a consequence of the requirement of convergence?

In reference to Assumption 2, are we free to assume that the held-out samples are likely to be stored in a similar fashion to the training set? In typical associative memories even samples from the same distribution as the training set are not stored, instead patterns from the training set have their basin of attraction (here, associated ball) expand to cover the hyper-volume of the validation distribution --- does this intuition not carry over to this architecture for some reason? If not, why not? 

The main difference between the MCHN energy function and the proposed energy function appears to be the removal of the regularization terms. Instead, the negative distances are fed into the LogSumExp function, rather than the pattern matrix times the probe vector. To my understanding, this implies that the proposed energy function requires all patterns in the training set to be kept explicitly in memory such that the calculation in Equation 3 can be performed. Later, in Equation 4, the energy function near the patterns of the training set is replaced by the nearest neighbor search which again requires knowledge of all training patterns. Is this correct? In typical associative memories we try to avoid storing the training set patterns directly, as this would defeat the purpose of a model that can learn to retrieve items. However, this paper seems to use the nearest-neighbor-search explicitly which is relatively counterintuitive in the context of associative memories as a whole. The formalization of the search as an energy function is interesting, but I am not yet convinced this leads to a useful associative memory --- if we have the training set explicitly stored, why not conduct a nearest-neighbor search over this data instead of using the energy function? 

Assumption 3 references back to the condition that the all balls around training set patterns are well separated. Is this not repeated from the discussion in Section 3? The authors also discuss briefly what this assumption means in practice, but is this property common in real datasets? Or is this a property that is nice to reason about, but in practice can be violated somewhat? It feels that the requirement in Assumption 3 limits the proposed energy function to only very nicely behaved data --- is that correct?

In Section 6.1, from line 465 onwards, the experimental radius of each ball is determined to be 10. Equation 12 would predict this radius to be 7.74. This seems like a fairly large discrepancy; some 30% larger than expected. Is this large a discrepancy expected in practice? The final line of the Section offers some respite, but perhaps increasing the number of documents to verify that the presented radius is larger that the actual value would be useful.

### Soundness
4

### Presentation
3

### Contribution
3
