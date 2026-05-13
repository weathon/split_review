# Causal Graph Learning via Distributional Invariance of Cause-Effect Relationship

- Decision: Reject
- Scores: 5, 6, 6, 3

## Abstract
This paper introduces a new framework for recovering causal graphs from observational data, leveraging the fact that the distribution of an effect, conditioned on its causes, remains invariant to changes in the prior distribution of those causes. This insight enables a direct test for potential causal relationships by checking the variance of their corresponding effect-cause conditional distributions across multiple downsampled subsets of the data. These subsets are selected to reflect different prior cause distributions, while preserving the effect-cause conditional relationships. Using this invariance test and exploiting an (empirical) sparsity of most causal graphs, we develop an algorithm that efficiently uncovers causal relationships with quadratic complexity in the number of observational features/variables, reducing the processing time by up to 25x compared to state-of-the-art methods. Our empirical studies on a diverse benchmark of large-scale datasets demonstrate that the developed algorithm consistently performs better or comparable to existing works while generally achieving better scalability.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
The paper utilizes the invariance property of $P(X \mid \text{Pa}(X))$ despite having different $P(\text{Pa}(X))$ to find the causal parents. For this purpose, they choose some source priors, generate corresponding datasets, and verify the invariance. Finally, they show their performance on a variety of synthetic and real-world setups.

### Strengths
The paper is well written. The figure is helpful for understanding the algorithm. The experiments are extensive.

### Weaknesses
## Minor weaknesses:
* The authors mentioned “finding the maximum clique in an augmented bidirectional graph” multiple times but without a proper definition or example/visualization. It's unclear how this graph is constructed and what the nodes and edges represent. A concrete example would greatly aid understanding, especially since this concept is central to the algorithm.
* The source variables should be defined in a little more detail. It's not immediately clear what distinguishes them from other variables in the context of causal discovery. A more formal definition would be beneficial.
* What does $P'$ in equation 2 refer to? It should be precise. The notation is ambiguous and needs clarification to ensure the reader understands the conditional probability being discussed.
* “The intuition is if we can re-sample $D_i$ from $D \sim P(X)$ such that $D_i \sim P_i(X)$,” This is a little unclear. How are $D \sim P(\mathbf{X})$ and $D_i \sim P_i(\mathbf{X})$ different? The relationship between the original dataset and the resampled datasets is not clearly explained. What specific properties of $P_i(X)$ are being targeted through resampling?
* It is unclear how $D_1, D_2, \dots, D_M$ are sampled. How are the $m$ source priors ($P_i(\mathbf{B})$) obtained? Although these are discussed later, some hints/intuitive discussion should be provided earlier in the paper. This lack of clarity makes the initial understanding of the method challenging.
* “We cannot compute $P_i(X)$, … we can re-sample $D_i$ from $D$ so that $D_i \sim P_i(X)$” – based on my understanding, the first case is computing the numerical probability table, and the second case is sampling without any such table. This difference should be made clear. The distinction between these two approaches needs to be explicitly stated, including why direct computation is not feasible.
* More details on "downsampling without replacement" are needed. The specific mechanism of how data points are selected during downsampling is not sufficiently detailed. What criteria are used to ensure a representative downsample?
* An intuitive explanation of the “minimal downsampled rate” is required. The significance of this rate and how it relates to the preservation of causal relationships is not immediately apparent.


## Major weaknesses
* Suppose $Z$ is not a parent but an ancestor. Shouldn’t we also get variance = 0 (equation 1) in such cases? Does a change in $P(\text{Ancestor})$ affect $P(\text{descendant} \mid \text{ancestor})$? This raises a fundamental concern about the scope of the invariance test and whether it can distinguish between parents and ancestors.
* Many important concepts are delayed until section 4.2. The authors should consider introducing them earlier in the paper. This delay makes it hard to follow the core ideas of the paper in the initial sections.

### Questions
## Questions:
* How are the authors resampling the datasets?
* Do you have to perform this invariance test for all possible parent sets?
* Why is $Pa[B] = \emptyset$ in the definition of set $\mathbf{B}$ (section 4.1)? What does that imply?
* In practice with real-world data, is the variance always zero for all true parents (equation 1)? Why or why not? Should a threshold be used?
* How expensive is it to compute $\phi(X)$? Do we have to iterate over all $X$? And do it again after performing step ii in Theorem 3?

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
Based on the fact that the distribution of an effect, conditioned on its causes, remains invariant to changes in the prior distribution of those causes, this paper proposes a causal discovery algorithm for large-scale datasets. Specifically, it designs an invariance test, which is achieved by a downsampling scheme. It also makes the best of searching Markov blankets of all variables, to reduce the time complexity. Experiments on synthetic datasets and real-world networks show better scalability.

### Strengths
- This paper is written well, with clear descriptions and motivations. 

- The authors propose practical algorithms for causal discovery, with some interesting theoretical findings, e.g., the basis of a DAG, the minimal downsampling rate, etc. 

- The experiments under synthetic datasets and real-world networks are extensive, which verified the advantages in large-scale datasets.

### Weaknesses
 - Some details seem to be missing in the paper.
For example, 

i) Footnote 2 and Theorem 1 tell how to find non-parent sets, whereas how to set the threshold for the variance is not clear. Please give the details in the paper. Specifically, while the text suggests finding the smallest variance, the practical implementation of this comparison, especially with noisy data, requires a clear thresholding mechanism. Without a defined threshold, the algorithm's robustness is questionable, and it is unclear how to differentiate between a true zero variance and a near-zero variance due to sampling or noise.

ii) How to learn the different priors $P_i(X)$, with the estimated $m$? Did the authors assume some distributions? The paper mentions sampling from a simplex, but it's unclear how this simplex is parameterized and how it relates to the underlying data distribution. The practical implications of this sampling procedure, especially in high-dimensional spaces, need further clarification. The choice of categorical distributions and the method for sampling from them should be detailed, as this choice can significantly impact the algorithm's performance.

- Theorem 2 provides a necessary condition to test whether a subset $Z$ is the parent set of X. However, it is not a sufficient condition. Although the authors stated, “When m is infinitely large, the implication in Eq. (1) becomes bi-directional and $V[P+(X | Z)] = 0$ definitively implies $Z = Pa[X]$”. It is not that clear why this implication we can get. The jump from a necessary condition to a bi-directional implication with an infinite number of samples needs more rigorous justification. The paper should elaborate on how the variance converges to zero as m approaches infinity, and what assumptions are made about the underlying data distribution for this convergence to hold. The practical implications of this theoretical result, especially with finite samples, should also be discussed.

- It is better to perform some real-world datasets for validation. This is because bnlearn provides real networks and it generates the data based on the networks. These datasets look like semi-synthetic. BTW, in Table 2, when dealing with small-scale datasets (or even a large-scale dataset Munin), the runtime all seem not to be satisfactory. Please explain it.

### Questions
- Does the proposed causal discovery algorithm work for time-series data? What are the challenges?

I would be very glad to increase my score if the authors could resolve my concerns.

### Soundness
3

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
5

### Summary
This paper introduces a novel approach to causal learning through a new invariance test for causality, which underpins a reliable and scalable algorithm for reconstructing causal graphs from observational data. This method leverages a core insight that the conditional distribution of the effect given the cause remains invariant under changes in the prior distribution of the cause. This insight enables a parent-identification process for each variable using synthetic data augmentation. This process is integrated with an efficient search algorithm that utilizes prior knowledge of each effect variable’s Markov blanket, along with the empirically observed sparsity of causal graphs, to significantly reduce computational complexity.

### Strengths
1. The proposed method is rather novel.   
2. Overall, the paper is well-structured and clearly written.    
3. The experiments are extensive, covering 3 types of functional causal models, 6 causal discovery baseline methods, and varying graph sizes.

### Weaknesses
Any thoughts on how to extend your method to handle heterogeneous or time-series datasets?

### Questions
(See above)

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper proposes a new framework that leverages the invariance of effect conditioned on its causes for causal discovery from observational data. The main idea is it try to disturb the p(cause) distribution and see whether the p(effect|cause) would change after the disturbance.

### Strengths
- This work leverages the invariance of conditional distribution and then proposes a downsampling method, combining them to find the parent set.

### Weaknesses
 - The main issue is that since the real intervention is not applicable to the observational data, it provides a downsampled technique to approximate the p(effect|cause) after the disturbance, which, however, has no theoretical guarantee. This is, how to guarantee such a downsampled correctly corresponds to the real distribution after the disturbance? The core of the problem lies in the fact that observational data, by its nature, lacks the necessary information to infer the effects of interventions. The proposed downsampling method, while attempting to mimic an intervention, does not provide a principled way to bridge this gap. Without a theoretical foundation, it is unclear under what conditions this approximation would be valid, and how much the results would deviate from the true interventional distribution. This is a fundamental limitation, as the method relies on an assumption that the downsampled distribution is a good proxy for the interventional one, without providing any justification for this assumption.
- Since the basis variables would include the leaf vertices, in such a case, changing the prior basis variables will not affect the distribution of their ancestors, and thus it may not have a similar effect to changing prior over source variables. Specifically, if a leaf node is included in the basis, perturbing its distribution will not propagate any changes to its parent nodes, which are the actual causes of the leaf node. This is because the causal influence flows from parent to child, not the other way around. Therefore, the method's attempt to simulate interventions by perturbing the basis variables may not have the desired effect on the causal structure, especially when leaf nodes are included in the basis. This could lead to incorrect causal inferences, as the method might not be able to detect the true causal relationships between the variables.

Typos:
- "Theorem 2" -> "Theorem 4" in Theorem 5

### Questions
See the weakness above.

### Soundness
1

### Presentation
3

### Contribution
2
