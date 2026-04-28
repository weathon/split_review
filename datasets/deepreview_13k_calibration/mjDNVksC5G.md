# Can Transformers Perform PCA ?

- Decision: Reject
- Avg Score: 4.20
- Scores: 5, 3, 5, 3, 5

## Abstract
Transformers demonstrate significant advantage as the building block of Large Language Models. Recent efforts are devoted to understanding the learning capacities of transformers at a fundamental level. This work attempts to understand the intrinsic capacity of transformers in performing dimension reduction from complex data. Theoretically, our results rigorously show that transformers can perform Principle Component Analysis (PCA) similar to the Power Method, given a supervised pre-training phase. Moreover, we show the generalization error of transformers decays by $n^{-1/5}$ in $L_2$. Empirically, our extensive experiments on the simulated and real world high dimensional datasets justify that a pre-trained transformer can successfully perform PCA by simultaneously estimating the first $k$ eigenvectors and eigenvalues. These findings demonstrate that transformers can efficiently extract low dimensional patterns from high dimensional data, shedding light on the potential benefits of using pre-trained LLM to perform inference on high dimensional data.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper theoretically and empirically investigates whether one can use the Transformer architecture and supervised, in-context learning (ICL) to perform PCA, specifically the power method for computing top principle components.
The results build upon [Bai et al. (2024)](https://arxiv.org/abs/2306.04637)'s recent work on using Transformers and ICL to implement various ML algorithms (least-squares, ridge, lasso, and SGD).
The theoretical results provide an approximation bound on the PCs as well as a generalization error bound of $n^{-1/5}$.
Empirically, the authors show that the Transformer can approximate the first few principle components and the corresponding eigenvalues on Gaussian synthetic data and on real data (MNIST and Fashion-MNIST).

### Strengths
- The high-level problem statement is clear, timely, and potentially interesting. The theoretical and empirical results are novel.
- The theory portion of the paper appears to be rigorous (I did not check the proofs in detail).
- The experiments are generally reasonable and the results are consistent with the theory to some extent.

### Weaknesses
 - The biggest issue for me is that the paper is not very clear about the significance of the results: _why_ is it important that Transformers can perform PCA? I don't imagine people using Transformers to compute PCA instead of the existing methods, so instead the results have to give meaningful insights on what it is about Transformers, or the ICL procedure, that allows them to perform PCA. I think there is a lot of missed potential in the discussion section to elaborate on this.
- A related question is: what is it about the task of PCA that sets it apart from other ML tasks in Bai et al. (2024), like least-squares, ridge, and lasso? Does the proof reveal any interesting insight about how either Transformers or ICL suit the specific task? Or is it just that any iterative algorithm can (in principle) be implemented in an ICL setting? How much would the performance degrade if I replace the Transformer model (partly or entirely) but keep the ICL framework? I think the paper has to be restructured in a way that some of the theoretical results are presented a bit more briefly and these questions are discussed (in words) in a lot more detail.
- The empirical results show that the principle components are not very accurate beyond the first few and/or in high dimensions. I think one thing that will make things clearer is if there were a baseline using just the power method on the same data, as this will clarify whether this is a limitation of the Transformer or the power method itself. It's unclear if the observed limitations are due to the Transformer architecture or inherent to the power method's convergence properties, especially in higher dimensions or with more complex data structures.
- Some of the conditions in the theorem are not well-explained/motivated in words, e.g., that the eigenvalues are distinct and that the L2 norm of the input is bounded (I don't see $B_X$ appearing in the resulting error bound). In particular, I think it's important to distinguish which conditions are necessary for the Power Method to work in the first place, and which are necessary for the Transformer to perform PCA. The distinct eigenvalue condition is particularly limiting, as real-world data often has repeated or near-repeated eigenvalues, and it's not clear how the method would perform in such cases. The role of the input norm bound also needs further clarification, especially since it doesn't explicitly appear in the final error bound, making it difficult to assess its practical impact.
- I'm not sure if I agree with the claim that "transformers are able to produce small error on predicting eigenvalues" on real data. The RMSE numbers are 10x larger than the synthetic case, and the eigenvectors are not similar for k >= 3. I think it would be more accurate to say that, on real data, the Transformer can approximate the first few eigenvectors and eigenvalues well, but not necessarily all of them. (This is not a weakness per se, but I think it's important to be clear about the limitations of the method.)

### Questions
- p. 4, text: I believe you means "symmetric" not "asymmetric" here? There are different terminologies being used between "principle eigenvectors", "left singular vectors", and of course "principle components" in PCA. My recommendation is to consistent terminology throughout the paper.
- p. 5, figure 1: what's the difference between blue and purple blocks?
- p. 6, remark 3: typo in "frist"
- p. 6, remark 5: what is the significance of the $n^{-1/5}$ rate specifically? How does one make sense of how good or bad this rate is?
- p. 7, line 375: typo "Figure ??", "differernt"
- p. 8, line 431: why exactly do these metrics (not loss functions, to be precise) match the intuition of eigenvalues/vectors?
- table 1: what is shown in parentheses? 
- figures 2 & 4: why does the RMSE decrease as k increases for synthetic data, but increase for MNIST? Also, it may be a bit more intuitive to show the RMSE for individual components rather than the sum of the first k components.

### Soundness
3

### Presentation
1

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This work studies the problem of whether transformers can perform PCA. For this, they used a supervised setting where the outputs are principal components of the inputs. Inspired by the classical power iteration method, they construct the weights of a transformer model that approximately does PCA. For this, they assume that the eigenvalues are spaced out and bounded, and use classical results on random vectors to construct an auxiliary matrix they utilize to prove their bounds. Experiments on synthetic and real-life data weakly validate their studies. The target audience are people working on ML theory.

### Strengths
- The paper studies approximation capabilities of transformers from a theoretical perspective. This adds to a recent array of works which study the theoretical capabilities of transformers [1, 2, 3] and is potentially interesting.

- The experiments probe ablations of a few different parameters in both simulated and a couple of real-life datasets. While the observations are intuitive, it (weakly) validates some observations of the theory.

#### References:
- [1] Transformers Learn Shortcuts to Automata
- [2] Do LLMs dream of elephants (when told not to)? Latent concept association and associative memory in transformers.
- [3] (Un)interpretability of Transformers: a case study with bounded Dyck grammars

### Weaknesses
 - While the question of transformers can perform PCA sounds interesting on the surface, I'm unable to gauge how interesting the bounds given here are. For one, we have universality results for neural networks that the authors cite, but do not seem to carefully compare against. Specifically, the paper does not address how the approximation capabilities of transformers for PCA compare with other neural network architectures, or even simpler linear models, given known universality results. Secondly, the bounds derived seem highly complicated and as the authors mention, it's not clear if they're tight. It's also not clear if they're useful or not, apart from being some generic generalization bounds. See also the question at the end.

- To continue the above point, this is more of a work on approximation of a transformer model to power iteration specifically, rather than to PCA. The paper focuses on showing that a transformer can mimic the power iteration method, which is just one algorithm for computing PCA, rather than directly demonstrating that transformers can learn the principal components themselves. Lower bounds approximately validating their bounds would be useful here.

- The experiments seem a bit standalone and does not connect deeply to the theory, in particular the terms that arise in the loss. For example, the dimension D is hidden in the universal constant in remark 3, however it may be good to quantify the exact dependence and moreover, validate a version of it in the experiments. The experiments should more directly validate the theoretical claims, for example by showing how the error scales with the number of layers, attention heads, or other parameters that appear in the theoretical bounds. The current experiments do not provide a clear connection between the theoretical results and the empirical observations.

- The paper seems hastily written, e.g. in L142, definition 3, The sentence defining \tilde{D} seems incomplete, L375 contains a missing citation, see also typos at the end.

### Questions
Some questions were raised above.

- I maybe misunderstanding something but aren't principal eigenvectors linearly related to the given vectors? If so, a linear matrix, instead of transformers, should suffice for this purpose?

#### Typos:

- L111: "along the it gives us"
- L132: "convinience"
- L233: "propogation"
- L308: "isotorpic"
- L721: "setps"
- ReLU, relu and Relu are used interchangeably.

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
1. The paper shows how to do PCA using a forward pass through the transformers without going through power iteration
2. The error bounds are derived for Gaussian data, and they look sound
3. However, I believe the authors are trying a more difficult problem of estimating k eigenvectors simultaneously. For practical data, the method can solve the problem of finding the top eigenvector with sufficient accuracy. Instead, they can solve the easier problem of estimating the top one and then finding the next through successive elimination. It will still be fast enough for high dimension than power method

### Strengths
The maths in the paper is well-derived and sound. The method works well for the top eigenvector for datasets such as MNIST or F-MNIST. It has the potential to become useful. However, I believe the authors are trying a more difficult problem of estimating k eigenvectors simultaneously, and for practical data the method can solve find the top eigenvector with sufficient accurac. Instead they can solve the easier problem of estimating the top one, and then find the next ones through successive passes on X - \lambda ww'.

### Weaknesses
1. The error bound in Proposition 1 is proportional to d, the Gaussian dimension. I doubt the algorithm will work in high dimension

2. The experiments on synthetic data can include datasets for high dimensions (D). For D=50, people will simply use power iteration. The method's usefulness lies in whether it can predict the eigenvector/values for a high dimension, which the authors skipped for the synthetic data.

3. For the experiments on MNIST or F-MNIST, the cosine distance drops to 0.5 or below for k>1. This is concerning. If the transformer is trained to predict the top eigenvalue (say w) and eigenvector (say v) from X with sufficient accuracy, it can take another forward pass on X - w v v^T to predict the second pair. Why is the error for the eigenvector for k>1 so high? I believe the method needs some revision to be applicable

### Questions
Please see Weakness.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
2

### Summary
This paper explores the potential of transformer models to perform Principal Component Analysis (PCA) through a theoretical and empirical lens. Authors demonstrate that a pre-trained transformer can approximate the power method for PCA. The paper provides a rigorous proof of the transformer’s ability to estimate top eigenvectors and presents empirical evaluations on both synthetic and real-world datasets to validate these findings.

### Strengths
- The finding that transformers can effectively implement the power iteration method is intriguing and expands the known possibilities of transformers.
- The paper is theoretically rigorous, and the experiments on both synthetic and real-world datasets effectively support the proposed theoretical framework.

### Weaknesses
 - The practical implications of the results are somewhat unclear. The paper does not sufficiently explore whether the observed behavior of transformers approximating the power method for PCA translates to effective PCA performance in practical scenarios, particularly on in-context examples. The analysis lacks a clear connection to how this theoretical finding can be leveraged in real-world applications.
- The novelty of this result is questionable. While the paper demonstrates that transformers can learn to approximate PCA, it does not adequately address the fact that simpler models, such as linear autoencoders, can also achieve this. The paper needs to clarify what unique insights transformers bring to PCA that are not already achievable with simpler models. The justification for using a complex model like a transformer for PCA, given the existence of more efficient methods, is not well established.
- The supervised pre-training phase seems unrealistic in practical applications, which makes the analysis and experimental results appear less impactful. The reliance on a supervised pre-training phase, where the transformer is trained to predict the next token, is not aligned with typical unsupervised learning scenarios for PCA. This pre-training step introduces a significant deviation from the standard PCA setup, making the practical relevance of the findings questionable. The paper needs to address how the pre-training phase influences the results and whether the same behavior can be observed without such a phase.
- The paper is challenging to follow due to unclear writing, which affects readability and the accessibility of its main ideas. The lack of clarity in the writing makes it difficult to understand the core contributions and the underlying mechanisms. The paper would benefit from a more precise and accessible presentation of the theoretical framework and experimental results.
- Lines 142-143: "Consider output dimension to be \tilde{D}, the…" – this sentence appears incomplete
- Several notations in the main body are not clearly defined. Implementing a more systematic notation or including a glossary would significantly improve readability.
- The notation L is used both for the number of layers and the loss function, which creates confusion.
- Could PCA not be formulated as an optimization problem and solved with gradient descent, using existing methods (e.g., [1])?

### Questions
- Lines 142-143: "Consider output dimension to be \tilde{D}, the…" – this sentence appears incomplete
- Several notations in the main body are not clearly defined. Implementing a more systematic notation or including a glossary would significantly improve readability.
- The notation L is used both for the number of layers and the loss function, which creates confusion.
- Could PCA not be formulated as an optimization problem and solved with gradient descent, using existing methods (e.g., [1])?

[1] Von Oswald, Johannes, et al. "Transformers learn in-context by gradient descent." *International Conference on Machine Learning*. PMLR, 2023.

### Soundness
3

### Presentation
1

### Contribution
1

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper asks if a transformer can be used to calculate the top k eigenvectors of the covariance of an input data matrix. Towards this end, it uses the transformer to implement a power-method approach to this problem. The paper then analyzes the accuracy of this implementation (with respect to the true eigenvectors).

The question of what sort of data analysis transformers can do is interesting. While the paper makes some headway on this problem, it has some key limitations, discussed below:  


1. For large enough transformers, why is it surprising that any analysis method, and in particular PCA can be implemented? Specifically, since the transformer described here can use self-attention (with relu) to calculate the covariance and then has enough layers to do the power iterations, why is it surprising that it can calculate PCA?


2. In Theorem 3.1., epsilon0 is used before being defined. You should write this more clearly/correctly by first quantifying over epsilon0 and then using it. But it still is strange that tau is upper bounded rather than lower bounded. Eg why not use tau=0. This theorem needs to be better written. 


3. In the theory part ,d denotes the number of rows of X and D denotes the dimension after augmentation, but then in the experiments only D is mentioned as the dimension of the data. Is this a mistake? It seems like also in the experiments you would need both d and D.  Generally it is not clear what role P (augmentation matrix) plays in the experiments.


4. The standard method for calculating multiple eigenvectors is Lancoz, which I don’t think is what you are using. Have you considered using this instead?


5. There is a long line of work on implementing PCA with online rules such as Oja. It would be good to comment about this.


6. The paper is not very well written, with quite a few grammatical errors and typos (“One critical and most fundamental questions”, “Hence, practioners use various of methods”, “such that forward propagate along the it gives”).


7. What does “helps us screen out all the covariates” mean?


8. It seems like the use of ReLU is important for carrying out the covariance computation and that it would be hard to do with a softmax. Although there is some discussion of this, it seems like a significant restriction since softmax is much more broadly used.


9. I’m not sure how to understand the empirical results. They seem to mostly show that for smaller models it is harder to calculate PCA, which is perhaps not that surprising. Is

### Strengths
See above.

### Weaknesses
1. For large enough transformers, why is it surprising that any analysis method, and in particular PCA can be implemented? Specifically, since the transformer described here can use self-attention (with relu) to calculate the covariance and then has enough layers to do the power iterations, why is it surprising that it can calculate PCA?


2. In Theorem 3.1., epsilon0 is used before being defined. You should write this more clearly/correctly by first quantifying over epsilon0 and then using it. But it still is strange that tau is upper bounded rather than lower bounded. Eg why not use tau=0. This theorem needs to be better written. 


3. In the theory part ,d denotes the number of rows of X and D denotes the dimension after augmentation, but then in the experiments only D is mentioned as the dimension of the data. Is this a mistake? It seems like also in the experiments you would need both d and D.  Generally it is not clear what role P (augmentation matrix) plays in the experiments.


4. The standard method for calculating multiple eigenvectors is Lancoz, which I don’t think is what you are using. Have you considered using this instead?


5. There is a long line of work on implementing PCA with online rules such as Oja. It would be good to comment about this.


6. The paper is not very well written, with quite a few grammatical errors and typos (“One critical and most fundamental questions”, “Hence, practioners use various of methods”, “such that forward propagate along the it gives”).


7. What does “helps us screen out all the covariates” mean?


8. It seems like the use of ReLU is important for carrying out the covariance computation and that it would be hard to do with a softmax. Although there is some discussion of this, it seems like a significant restriction since softmax is much more broadly used.


9. I’m not sure how to understand the empirical results. They seem to mostly show that for smaller models it is harder to calculate PCA, which is perhaps not that surprising. Is

### Questions
See above.

### Soundness
2

### Presentation
1

### Contribution
2
