# Dimension-Independent Rates for Structured Neural Density Estimation

- Decision: Reject
- Scores: 5, 8, 6, 8

## Abstract
We show that deep neural networks achieve dimension-independent rates of convergence for learning structured densities such as those arising in image, audio, video, and text applications. More precisely, we demonstrate that neural networks with a simple $L^2$-minimizing loss achieve a rate of $n^{-1/(4+r)}$ in nonparametric density estimation when the underlying density is Markov to a graph whose maximum clique size is at most $r$, and we provide evidence that in the aforementioned applications, this size is typically constant, i.e., $r=O(1)$. We then establish that the optimal rate in $L^1$ is $n^{-1/(2+r)}$ which, compared to the standard nonparametric rate of $n^{-1/(2+d)}$, reveals that the effective dimension of such problems is the size of the largest clique in the Markov random field. These rates are independent of the data's ambient dimension, making them applicable to realistic models of image, sound, video, and text data. Our results provide a novel justification for deep learning's ability to circumvent the curse of dimensionality, demonstrating dimension-independent convergence rates in these contexts.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper studies learning distributions (ie generative models) under the assumption that the Markov Random Field (MRF) generating the data has no large cliques. [A MRF has an associated graph $G$ which captures the conditional independence stucture of the data $x$: if any path from $i$ to $j$ in G goes through $k$, then $x_i$ and $x_j$ are conditionally indepndent given $k$. Crucially, the distribution p(x) can be written as a product of terms that depend only on $x_S$, where S is a subset of nodes in a clique of G.] The main result (Theorem 4.2) shows that the distribution can be learned in $n$ samples up to TV distance $n^{-1/(4+r)}$ where $r$ is the size of the largest clique in $G$ by ERM over a class of NNs.

This paper provides an alternative viewpoint to the manifold hypothesis for why generative models can perform well without needing a number of samples exponential in the ambient dimension. The authors posit that the MRF assumption may better capture the stucture in the data than the manifold hypothesis when many parts of the data are [conditionally] independent: for example pixels far apart in images, or words far apart in language.

### Strengths
- The paper is well-written and very clear, including the proofs. 
- The motivation of wanting to consider structural assumptions that go beyond the manifold hypothesis is sound.
- While the MRF assumption is certainly idealistic, the authors suggest in their conclusion that ultimately these 2 could be viewed in conjunction, since they capture orthogonal types of structure in the data.

### Weaknesses
My main concern is the theoretical contibutions are quite weak (and this is a theory paper)/
- The main result shows that Lipshitz MRFs can be learned by ERM over $\prod_{S \in clique(G)} \psi_S(x_S)$ neural networks, where $x_S$ is $x$ restricted to the inputs in the set $S$, and each $\psi_S$ is a neural network, achieving a rate of $n^{-1/(r + 4)}$. However, it is known how to learn such Lipshitz MRFs at a better rate of $n^{-1/(r + 2)}$, with a different (non NN-based) algorithm. While this algorithm may be computationally intractable, ERM over NNs is not necessarily tractable. 
- The proof of the main result (Thrm 4.2) seem to follow closely from results in Schmidt-Hieber 2017 which gives approximation of Liphsitz functions by NNs. I am unaware if there is any significant technical novelty in using this for MRFs.
- The consequences in section 4.3 are all quite trivial.

Discussion of Related work lacking:
- There is no discussion of the literature on learning MRFs. I am not an expert in the area but this is glaringly lacking, and I do wonder if the authors are reinventing the wheel with Theorem 4.8.
- Can the MRF be learned if the graph $G$ is unknown? The authors should discuss the literature here.


In light of some of the discussions with the authors, I am willing to see this paper accepted, though I feel the theoretical result should be better contextualized, including discussion of the following:

(1) Other work on non-parametric density estimation, in particular which avoids the curse of dimensionality. As in the authors' comments, they should explain which are subsumed by the MRF or Manifold hypothesis. 
(2) The difference between this work and the well-studied with MRFs, which typically involves learning the graph structure (though typically with additional parameteric assumptions). 
(3) Why do the authors get a $n^{-1/(r + 4)}$ rate for neural networks? Can NN possibly achieve the $n^{-1/(r + 2)}$ rate, or are they intrinsically limited? Other works (eg. https://arxiv.org/abs/2212.13848) achieve the minimax $n^{-1/(d + 2)}$ rate for learning Lipschitz functions on $R^d$.

Ultimately, I still feel the theoretical contribution is non-surprising and not-particularly challenging: the paper shows that under the MRF assumption with clique size $r$ --- meaning the density can be written as a product of Lipshitz functions on $r$ coordinates --- density estimation can be done at the $n^{-1/(r + 2)}$ rate, matching the rate for Lipshitz density estimation in $r$ dimensions. If the density function is fit with neural networks, the rate achieved is slightly worse: $n^{-1/(r + 4)}$, while other works (eg. see above) in non-parametric learning with neural-networks do achieve the minimax rate.

Overall, I still feel the technical contribution of this paper is **extremely** lacking especially given the **absence of proper contexturalization** within the related work. I am also reducing my score because on further inspection of the proofs, they are not clearly written [for example Proposition A.1: I could not find equation (2) or why it is true from the Chang lecture notes reference, and I am confused because $V'' \subset V'$, and yet $V'' \setminus V'$ is non-empty?].

### Questions
See above.

### Soundness
3

### Presentation
3

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
The paper studies classical density estimation under the assumption that the data has markov random field structure. They show that there exist betwork architectures such that the curse of dimensionality (type $n^{-c/d}$ convergence rates, for $c$ some constant) is overcome by an ERM procedure if the dependency graph structure is sufficiently benign. I.e., if the largest clique is $O(r)$, the effective dimension is $r$ not $d$.

### Strengths
* The authors offer an interesting pespective on ambient dimensionality via MRF clique size. 

* Overall I found the paper well-written/structured and easy to follow 

*I believe the results relating clique size to convergence rate are novel

* The paper is well-contextualized (i.e., wrt manifold hypothesis) and written with ample motivation with examples in mind.

* The power graph construction is interesting

### Weaknesses
 * I am not entirely convinced about dependence (in terms of graph hops, mixing or other related concepts) accurately capturing the hardness of a problem as opposed to support on low-dimensional manifold. See my question Q3 below. 

*Comment:  While I could infer the assumptions of the main theorem from the text preceding it, the assumptions are stated too implicitly for my taste. I think in particular the "markov property with respect to G" should be explicitly defined somewhere in the text (ideally with \cref in thm 4.2 to ease readibility).



### Questions
Q1. Is it assumed that p is realizable by the hypothesis class in question in thm 4.2?

Q2. Could you comment on your section modeling CIFAR10 as an MRF. It is not obvious to me from your discussion following Corollary 4.5 that either hop structure is appropriate for modeling the ground truth distribution. Are there known results characterizing the locality of dependence on CIFAR (genuine question --- have very little background on image classification)?

Q3. I am not sure whether the MRF/clique assumption is so different from the manifold hypothesis, and would be interested to hear further comments on this. The example I have in mind is the following (which has both low clique size and low effective dimension --- neither of which actually capture the convergence rate of ERM which actually decreases with $d$). Consider, the Gaussian  autoregression $X_{t+1} = aX_t +W_t$ (say for a fix sequence length $d$) does not just have global dependence between all coordinates $X_t$ but is actually easier to learn for $|a| \geq 1$ (more dependency/no mixing --- see the classical result from Mann&Wald 1943 and note that regression is equivalent to density estimation in KL for this model).  Note also that if $|a| >> 1$ the process is concentrated on the last coordinates, making dimensionality relevant instead. Overall, this kind of begs the question to me what the actual notion of signal-noise actually is in density estimation?

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
The author(s) analyze a general class of densities that are markov to an undirected graph. Under the sense of density estimation, they derive the convergence rate of neural networks. The rate only depends on the effective dimension of the graph, i.e. the maximium clique size r.

### Strengths
It's a joy to read the paper. The paper proposed a sound theorem on dimension-free convergence rate, which looks right to me. The paper clearly claimed the assumption for the convergence rate theorem, and justified the assumption and its connection to the real world applications. They put a lot of discussion on the assumption and explain the gap between the assumption.

### Weaknesses
Though a lot of discussion on the assumption, the paper lacks the numerical results (example or real world application) to illustrate the convergence rate. Specifically, the theoretical results are not validated with experiments on synthetic or real-world datasets. The paper would benefit from demonstrating the convergence rate empirically, showing how the error decreases with increasing training data, and how this aligns with the derived theoretical rate. As mentioned in line 511, it lacks the proof when the optimal rate happens. This is a significant gap, as it leaves open the question of whether the derived rate is tight or if there is a possibility of achieving a faster convergence rate under certain conditions.

I'm confused about the figure 3. The author(s) try to claim that the dependency of pixels are reduced given the observations of a neighboring pixel. The explanation of how MRF is applied in this scenario is not clear enough. The paper should explicitly state how the MRF structure is defined for the image data, including the neighborhood system and the potential functions. The current discussion is too high-level and lacks the necessary details for a reader to understand how the MRF is actually used to model the image data. Furthermore, the paper does not provide any experiments on the convergence rate with neural networks trained on data generated from an MRF, which would be crucial to justify how MRF helps bypass the curse of dimensionality.

### Questions
I'm confused about the figure 3. The author(s) try to claim that the dependency of pixels are reduced given the observations of a neighboring pixel. Can author(s) explain how MRF is applied in this scenario and also provide experiment on the convergence rate with neural networks (better with MRF), in order to justify how MRF helps bypass the curse of dimensionality?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The authors study the upper bounds of the sample requirements for probability density estimation using deep learning. They establish an upper bound on the $L_1$ error for probability density estimation based on the size of the largest clique in the undirected graph of data, i.e., the Markov random field (MRF). Furthermore, for one-dimensional or two-dimensional array data, the authors present an upper bound on the $L_1$ error, deriving an upper bound on the size of cliques of the data. They also provide proofs for these theoretical results.

### Strengths
* To the best of my knowledge, the upper bound on the estimation error for density estimation based on the structure of the undirected graph model is novel. The theoretical results of this study are considered important for understanding the sample requirements of density estimation for high-dimensional data.
* Proofs are provided for these theoretical results, and no major errors have been found.

### Weaknesses
#### Major weaknesses:
* The empirical evidence is limited for supporting the author's conclusions regarding the MRF structure of image data. Specifically, the experiments do not provide a direct validation of the assumed Markov Random Field (MRF) structure in image data, making it unclear if the sample requirements in Corollary 4.5 are truly applicable to image data. The presented results in Figure 3, while suggestive, do not offer a rigorous confirmation of the theoretical bounds derived under the MRF assumption. It remains uncertain whether the observed performance aligns with the predicted $O(n^{-1/9})$ convergence rate for image data.
* Additionally, it is desirable to conduct numerical experiments using synthetic data where the underlying probability distribution is known and the clique size can be controlled. This would allow for a more direct validation of the theoretical upper bounds on the $L_1$ error for probability density estimation based on the size of the largest clique, providing a stronger empirical link to the theoretical findings.

#### Minor weaknesses:
* Line 016-017: The statement “this size is typically independent of the data dimensionality” is more appropriate than “this size is typically constant, i.e., $r = O(1)$” in the lines, as this study does not focus on cases where the data dimensionality approaches infinity. The use of 'constant' might be misleading, as it could imply a fixed value rather than a value that doesn't scale with dimensionality in the context of this paper.
* Lines 419-422: A more detailed explanation or definition of $L_{d \times d'}$ and $L^+_{d \times d'}$ would clarify their specific meanings. Currently, the description is somewhat vague, and a more precise mathematical definition would improve the clarity and reproducibility of the results.

### Questions
* You suggest that the image data is a MRF such that $L_{d \times d'}$ and $L_{d \times d'}^+$, $L_{d \times d'}^2$, or 
$(L_{d \times d'}^+)^2$ (lines 258-290 and lines 444-451).
     According to Corollary 4.5, this implies that the sample requirement for density estimation of the image data is at most $O(n^{-1/9})$. 
     However, it seems slightly challenging to reliably reach this conclusion solely based on the results presented in Figure 3. Could you provide references to any research that has empirically tested this claim using image data, thereby supporting the upper bound presented in the corollary? Alternatively, are there any experimental methodologies that could confirm this upper bound?
* In lines 1402-1403, which theoretical results or resarch does "However, it is known that no estimator can achieve this rate" refer to?
* The discription in lines 446-451 is confusing. Does it mean that, assuming that CIFAR-10 is a MFR of $(L_{32 \times 32}^+)^2$, the probability density of the images can be estimated with the data sample requirement of $(L_{32 \times 32}^+)^2$, i.e., $n^{-1/9}$ in Corollary 4.5?

### Soundness
2

### Presentation
3

### Contribution
4
