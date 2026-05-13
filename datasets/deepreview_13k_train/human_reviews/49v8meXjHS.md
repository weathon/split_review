# $k$NN Attention Demystified: A Theoretical Exploration for Scalable Transformers

- Decision: Accept
- Scores: 8, 5, 5, 5, 8

## Abstract
Despite their power, Transformers \citep{vaswani2017attention} face challenges with long sequences due to the quadratic complexity of self-attention. To address this limitation, methods like $k$-Nearest-Neighbor ($k$NN) attention have been introduced \citep{roy2021efficient}, enabling each token to attend to only its $k$ closest tokens. While $k$NN attention has shown empirical success in making Transformers more efficient, its exact approximation guarantees have not been theoretically analyzed. In this work, we establish a theoretical framework for $k$NN attention, reformulating self-attention as expectations over softmax distributions and leveraging lazy Gumbel sampling \citep{mussmann2017fast} with $k$NN indices for efficient approximation. Building on this framework, we also propose novel sub-quadratic algorithms that approximate self-attention gradients by leveraging efficient sampling techniques, such as Markov Chain-based estimation. Finally, we demonstrate the practical effectiveness of these algorithms through empirical experiments, showcasing their benefits in both training and inference.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper theoretically analyzes kNN attention, which improves on the quadratic complexity (with respect to context length, $n$) of traditional full attention. The authors do this by viewing the self-attention matrix as an expectation over multiple softmax distributions, and then use the Gumbel-Max trick, along with the concentration properties of the Gumbel distribution, to efficiently approximate the original self-attention. This lazy Gumbel sampling, combined with k-MIPS, results in a total runtime of $O(n^{1.5})$. Additionally, the work approximates the attention gradients using length-1 random walk sequences, reducing the naive complexity from $O(n^2d)$ to $O(nd^2)$, providing high-probability approximation bounds.

### Strengths
The paper focuses on the important and relevant topic of the quadratic complexity of attention, given the ever-increasing context length in LLMs, and provides a rigorous theoretical analysis behind the empirical performance of kNN attention.
The paper is generally well-written, easy to read, and the ideas are clearly organized and discussed throughout. I enjoyed reading it, and liked how the authors first decompose the attention matrix as expectations over softmax, then use median-of-means boosting to achieve high-probability approximation bounds and runtime complexity bounds. The use of the Gumbel-Max trick and the concentration properties of the Gumbel distribution is also cute, ultimately leading to the gain over quadratic attention.

The use of 1-step random walks over the transition matrix P to approximate matrix-vector products (giving attention gradients in this case), although known, is also pretty nice. Overall, I appreciate how different well-known ideas are effectively combined.

### Weaknesses
I don’t have many weaknesses to point out, but I do have some questions/points I’d like to raise/discuss:


—The experiments in Figure 3b) show that for $k>n^{⅛}$, kNN attention performs quite well, and there doesn’t seem to be much need for $n^{1/2}$ (as suggested in your theory). I understand you’ve mentioned this as potential future work in the conclusion, but why do you think this is the case? As far as I understand, the choice of $k=\sqrt{n}$ in your theory arises because you want to balance the samples outside $S_i$​, which could, in expectation, ruin the top score after the addition of Gumbel noise, and the accuracy of lazy Gumbel sampling. This factor of $n/k$ also appears in the discussion in (Routing Transformers, Roy et al.), where the complexity is $O(nkd+n^2d/k)$, and $\sqrt{n}$ is the optimal choice. What do you think explains this significant gap?


—(Related to the above) For kNN attention without median-of-means (Sec 2.3), you randomly sample outside the top $k$ similarity products and upweigh them to capture the tail of interactions, and this is the algorithm used in the experiments. Median-of-means doesn’t consider the tail at all. Do you think capturing the tail behavior is critical to $k≪\sqrt{n}$​ performing well?

—Regarding the experiments in Section 4.2: The true benefit in the backward pass should only show up with large $n$. I understand that training larger models is difficult, but it would be interesting to see what happens with a moderate $n∼1000$ when training with cross-entropy.

—What is $n$ for the final set of experiments (perplexity and approximation error)? Also, for the mean error of the kNN ($k$ vs. $n$) experiment, what is the range of $n$? I couldn’t find these details in the appendix.


—Minor point: There is no figure number for the figure at the top of page 9, which I believe should be Figure 3. Please fix this and the rest.

### Questions
Please see weaknesses section.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The submission presents a theoretical framework for *k*-nearest neighbors (kNN) attention, an alternative to standard self-attention where each token attends to only the *k* "closest" tokens instead of all tokens. Additionally, the authors propose approximation methods for self-attention gradients using kNN search.

More precisely, the submission is organized as follows:

- In part 1, the theoretical results are outlined in brief.
- Part 2 focuses on kNN attention, introduced as an approximation algorithm. In Section 2.1, self-attention is reformulated as an expectation, and Theorem 4 presents the primary approximation results, comparing the outputs of true self-attention and kNN attention, both of dimension $n \times d$.
  - Section 2.2 discusses efficient sampling from the softmax distribution (with each empirical distribution corresponding to a row of the attention matrix) via Gumbel sampling.
  - Section 2.3 introduces an alternative method for computing kNN attention outputs, designed to be more compatible with modern hardware.
- Part 3 describes randomized algorithms to approximate self-attention gradients (with derivations in the appendix). These estimations leverage random walk simulations, and Theorem 10 provides a theoretical runtime analysis.
- Part 4 shows experimental results on kNN attention’s efficiency in terms of space and time costs (Figure (a)) and shows approximation error as a function of k (Figure (b)). Figure 3 compares learning curves for standard gradients obtained using backpropagation with those of the proposed approximation in part 3. Figure 4 evaluates perplexity and approximation error on real-world data using nanoGPT.

### Strengths
- The problem studied in the paper is well defined in the abstract. 
- Understanding the approximation abilities of sparse attention models, of which kNN attention are a special case, is a significant research question. 
- Similarly, proposing alternatives to computationally costly gradient computations in Transformers could have a strong impact in the community.
- The code is provided which enables to reproduce the experimental results.

### Weaknesses
I do not believe this paper to be ready to be published at ICLR for the following reasons:

Overall clarity:

The paper is generally quite difficult to follow. Importantly, it is difficult to understand what is new in the paper. A clear statement of the contributions would be helpful.

I am adding specific suggestions / questions for improvement below:

- It should be clearly mentioned that Part 1 sketches the results that are later detailed in Parts 2 and 3. 
- Whenever a theorem is stated, a *detailed* proof should be attached to it, even if it is in the appendix. I could not find a proof for each theorem (for instance, theorem 10). Please let me know if I am wrong. 
- Lemma 1 is hard to understand as is. What is a multiplicative estimate ? If this is detailed in App A, then the remark in l. 77 should be added before the lemma. 
- Line 60 is unclear. For a reader encountering this sentence for the first time, the phrase "how to extend the method to approximate the backward pass" is confusing. Please clarify why this is important and what connection it has to kNN attention.
- Mathematically, the paper lacks rigor. For instance, in line 104, is this an assumption on the differentiability of $\phi$, or is it just notation? Also, where are the precise assumptions on the norms of $Q$, $K$, and $V$ stated? These should appear immediately following the theorem.
- The source of the probability $1 - \delta$ in all the theorems (e.g., line 92) is unclear. Please specify the source of randomness; is it due to sampling over the softmax-induced distribution?
- In line 129, what does $T$ represent?
- In line 120, the term $k_k$ in equation (3) is confusing.
- Similarly, equation (5) is unclear because it takes the expectation with respect to $k$, yet there is an index $k$ in the sum. This could be clarified.

Theoretical Contributions:

- In general, I find the results challenging to interpret. How do these results compare to previous work? What are typical values?
- Presenting attention as an expectation of the value matrix is not new. For instance, see *Attention: Marginal Probability is All You Need* (https://arxiv.org/abs/2304.04556). As written, it seems the submission presents this as a novel contribution, which is misleading.
- Line 181: this is a proof sketch, not a full proof. I could not find the complete proof in the appendix.
- The proof of Theorem 4 is also only a sketch. For instance, see the last two lines.

Experiments:

- There should be experiments specifically validating the theoretical bounds. As is, the experiments are rather qualitative.
- I had to make some manual adjustments to get the provided code running. Including a `setup.py` would be helpful.
- I ran your code for the gradient approximation in Figure 3. On my laptop, the approximated gradient takes approximately 100 times longer to compute than standard gradients. Did you observe similar behavior? In which settings do you expect it to offer speed advantages?
- Similarly, I profiled the code from Appendix G against standard attention on a single GPU, using $B$, $H$, $N$, $D = 256$, $8$, $500$, $32$, and $k = 5$. I observed a runtime of 0.5831 seconds for kNN Attention versus 0.0061 seconds for Traditional Attention. If you do not observe similar results, could you provide code showing that your method leads to a speed advantage?

### Questions
Please see the questions in the previous part. 

In addition: 

- Regarding the conditions in Theorem 8: are these practically achievable? For instance, can $n$, $d$, $T$, and $k$ be expected to yield satisfying approximation errors?

### Soundness
3

### Presentation
2

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
This paper studies the theoretical aspects of k-Nearest-Neighbor (kNN) attention (Roy et al., 2021) and addresses the challenge of quadratic complexity in self-attention. 

It reformulates self-attention as expectations over softmax distributions, leveraging Lazy Gumbel Sampling (Mussmann et al., 2017) for efficient approximation. Then, novel sub-quadratic algorithms are introduced for approximating self-attention gradients using Markov Chain methods.

### Strengths
- The paper presents a theoretical analysis of kNN attention (Roy et al., 2021), connecting it to Gumbel noise sampling and Markov Chain methods for efficient gradient approximation. 

- I think the paper is well-structured. 

- Additionally, the author provides empirical experiments that demonstrate scalability and effectiveness in reducing computational and memory overhead.

### Weaknesses
 - The authors need to clarify their contributions in the introduction and compare the theoretical novelty to Mussmann et al. (2017). The differences between this work and prior works are not clear until one reads the algorithms and theorems in detail. Specifically, the introduction should clearly articulate how the proposed approach advances beyond existing uses of Lazy Gumbel Sampling, particularly in the context of sparse attention mechanisms. The connection to prior work on sparse attention is also not clearly established.

 - Many theorems are presented without proofs or discussions (please see my questions below). This is problematic as even if the proofs are clear to the authors, they should provide proper references or detailed discussions on the theorems. For example, the paper states that Theorem 7 is easily derived from Algorithm 1, but this requires more explicit justification. The lack of detailed proofs makes it difficult to assess the validity and novelty of the theoretical results.

 - The literature contains many randomized attention methods, such as Nyströmformer and Skyformer. These should be discussed in the related works. Adding benchmarks from these methods would also be useful. The absence of these comparisons makes it hard to contextualize the performance of the proposed method against other state-of-the-art techniques.

 - In the experiments section, some parts need clarification (please see my questions). For example, the authors used "kNN" as a legend, but it is unclear whether this refers to standard kNN or their modified version. Similarly, in several places, they mention "our algorithm" without specifying which algorithm they are referring to. This ambiguity makes it difficult to interpret the experimental results and their implications. The experimental setup needs to be more clearly defined, including the specific parameters used for each algorithm and the datasets used.

### Questions
1) Could you please clarify the theoretical novelty? For example:
- Is Theorem 4 a direct consequence of Median-Of-Means Boosting?
- Does Theorem 8 (main result) rely heavily on Mussmann et al. (2017)?

2) Where is the proof of Theorem 2? Is it a direct consequence of another specific theorem?  
3) In Theorem 4, what does $O(T)$ refer to? A discussion on the different parameters in the theorem is needed.  
4) In Theorem 28, how large can $\rho$ be? Does it approach 1?  
5) Where is the proof of Theorem 29? Is it a direct consequence of (Alman & Song, 2024a; b)?  

6) For notation, please clarify Gumbel $(a, b)$ and Bin $(a, b)$.  
7) In my opinion, the statement and proof of Theorem 5 are vague. Are you trying to say there exists an index \(\hat{j}\) that gives the maximum, and can you provide a proof for this?  
8) In Lines 184–189, what is the Moment Generating Function of the Gumbel distribution used in the proof of Lemma 6?  
9) Where is the proof of Theorem 7? What do you mean by "it is easy to derive from Algorithm 1"?  
10) In Theorem 7, how strong is the assumption $k = \sqrt{n}$?  

11) Algorithm 2 takes $\epsilon$ and $\delta$ as parameters, but I couldn't find them in the algorithm's steps. How are they used? Also, what is the range of these parameters?  

12) Theorem 8 is unclear. Why do we need $k$ and $\ell$ to satisfy two inequalities and then set them equal from another inequality? Why not use only the equality case? Considering $\epsilon$ and $\delta$ between 0 and 1, for larger $\ell$, we have:
$
k \geq \sqrt{\frac{8n^2 \varepsilon^{-2} \log(4/\delta)}{\ell}}.
$
However, this assumption seems unrealistic as $k$ scales with $n$.

13) Some parts of Algorithm 3 need clarification. In Line 2, "lg" should be "log". Why should $N$ be selected in that way? This requires more explanation. Also, what is $1^n$?  

14) In Line 246, which algorithm are you referring to?  
15) It is unclear how the total runtime in Line 224 was obtained. Is this result similar to Theorem 4 under comparable assumptions?  

16) What is Figure 3(a)? I couldn’t find it.  
17) What is the error definition in the discussion on "Efficiency of kNN Attention" (Lines 421–425)?  
18) What do you mean by convex and non-convex cases? In both settings, the attention approximation problem is non-convex due to softmax and the product of $Q$, $K$, and $V$.  

19) In the experiments section, you refer to “kNN” and “our algorithms” when comparing them with exact gradients or attention mechanisms. It is still unclear what "kNN" and "our algorithms" refer to in the context of this paper.  

20) What specific gains can be observed from the experiments in Sections 4.2 and 4.3? Should we expect time improvements in these sections, for example, in the NanoGPT case? How can we precisely measure the efficiency of the proposed methods, especially for self-attention gradient computation?

### Soundness
2

### Presentation
1

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper provides a theoretical analysis of $k$-NN attention, which is often explored as a method to reduce the quadratic time complexity of self-attention in Transformers. 
Specifically, it demonstrates that by combining $k$-NN with lazy Gumbel sampling, an unbiased estimate of self-attention can be obtained within an $\epsilon$-multiplicative error with sub-quadratic time and space complexity. 
Additionally, the paper proposes a method for approximating the gradient of self-attention within $\epsilon$-additive error using random walk simulation, also achieving sub-quadratic time complexity.

### Strengths
- The paper excellently ties the use of $k$-NN in self-attention to the context of lazy Gumbel sampling by framing self-attention as an expectation calculation.
- Clear pseudocode is provided for each algorithm.
- The authors have made their experimental code publicly available.

### Weaknesses
 - **Lack of originality**
  + At the beginning of Section 2.1, the authors claim that the first contribution of this paper is interpreting the softmax computation in self-attention as an expectation calculation. However, this interpretation itself is not a novel idea. For example, see [1].
  + Much of Section 2 simply applies results from [2] to the computation of self-attention. The authors should cite [2] in Theorems 5, 7, and 8, as well as in Lemma 6. Furthermore, Lemma 2.1 and Theorem 2.3 should also cite [1], as the statements of these results were already shown in [1]. While Lemma 2.1 provides a new proof, it should be explicitly stated that the result itself is not novel.
- **Presentation issues**
  + The reference to [2] is listed as an arXiv preprint, but it was accepted at Uncertainty in Artificial Intelligence 2017.
  + In equation (3), the dot is used inconsistently between $q_i^\top \cdot k_k$ and $q_i^\top k_s$.
  + The time complexity in Theorem 2 should be clarified as time complexity in expectation.
  + The citation format on line 97 of page 2 should be consistent with others.
  + "BIN" in Algorithm 1 is not defined.
  + The term "kNN index" lacks sufficient explanation.
  + The sentence "if we assume that..." on line 222 of page 5 was unclear to me; further clarification would be appreciated.
  + It would be helpful to clearly indicate which parts of Algorithm 2 constitute pre-processing.
  + Theorem 8 seems to rely on Theorem 3.5 from [2], which requires the assumption that $V_{sj}$ is bounded. If, like Theorem 2, the assumption $\|V\|_{\infty} = O(\log n)$ is used, this should be explicitly stated in the theorem.
  + The reference to Figure 3(a) and (b) is ambiguous; it seems to refer to the figure at the top of page 9. If so, the figure at the bottom of page 9 should be renumbered as Figure 4.
  + Numbered and unnumbered equations are mixed inconsistently. Additionally, on the left-hand side of Equation (5), it seems that the multiplication of the variance and the expectation is upper-bounded by $B \cdot O_{ij} \cdot O_{ij}^{-2} = B \cdot O_{ij}^{-1}$. It is unclear where the $O^{-1}_{ij}$ term goes, and it should be explicitly stated that $O_{ij}$ is lower bounded by a constant, as this is crucial for the approximation.


### Questions
- In Sections 2.2 and 2.3, two approximation methods are proposed. Can their performance be compared directly?
- In Section 4.1, the experiments are conducted with the matrices $Q,K$, and $V$ sampled from a uniform distribution. How would the performance change if $Q,K$, and $V$ were sampled from more biased distributions, such as those encountered in real-world data?
- In Figure 3(a), why does the computational time for $k=n^{1/4}$  outperform $k=\sqrt{n}$? Also, what does "Brute Force" refer to in this figure?
- In Section 4.2, would it be possible to include a comparison of computation speeds?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper provides a theoretical analysis of the KNN-nearest-neighbor sparse attention techniques for efficient attention computations. In that setting, every token attends only to its k nearest neighbors. By leveraging developed theoretical framework, the Authors propose a novel algorithm for the sub-quadratic time approximation of the self-attention gradients for efficient Transformer-training (default computations involving attention modules in Transformers require quadratic time in the sequence length, a prohibitively large time complexity for longer input sequences). The conducted analysis leverages an interpretation of the attention mechanism as computing the average value vector with respect to the softmax distribution defined on all the keys. Experimental evaluations confirms Authors' theoretical findings.

### Strengths
Great paper, that sheds new light on sparse attention mechanisms leveraging the notion of the kNN-graph. The probabilistic interpretation of the attention mechanism is actually well-known in the literature, yet it is very elegantly applied here to conduct a rigorous theoretical analysis of the method. New algorithm for the sub-quadratic computations of the attention gradients is yet another contribution of very practical impact. The idea to approximate the expectation coming from the probabilistic interpretation of the attention module via lazy Gumbel Noisy sampling is yet another beautiful insight that the paper provides.

### Weaknesses
The paper might further benefit from placing newly developed sparse attention mechanisms in the context of other efficient attention methods, e.g. those based on low-rank linear attention. It is also not clear how to choose the optimal value k, since, as the Authors explain, practically optimal value k is often significantly smaller than \sqrt{n}. Specifically, the paper lacks a discussion on how the performance of the proposed method compares to other sparse attention techniques under various sequence lengths and computational constraints. The theoretical analysis, while rigorous, does not provide a clear practical guideline for selecting the hyperparameter k, and the empirical justification for the chosen values of k is not sufficiently detailed. Furthermore, the paper does not explore the potential sensitivity of the method to the choice of the distance metric used to define the nearest neighbors, which could significantly impact the performance of the kNN attention mechanism.

### Questions
1. The Authors cast it in the paper as an open question, yet I wonder whether they have any intuition how the optimal values of k can be derived in the more mathematically principal way (rather than just empirically), by leveraging the theoretical framework that was already developed in the paper. 

2. Did the Authors try to apply proposed in the paper sub-quadratic attention-gradient algorithm for other modalities than text, e.g. in the context of the ViTs ?

### Soundness
4

### Presentation
4

### Contribution
4
