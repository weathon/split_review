# Nonlinear Sequence Embedding by Monotone Variational Inequality

- Decision: Accept
- Scores: 8, 6, 8, 8

## Abstract
In the wild, we often encounter collections of sequential data such as electrocardiograms, motion capture, genomes, and natural language, and sequences may be multichannel or symbolic with nonlinear dynamics. We introduce a new method to learn low-dimensional representations of nonlinear time series without supervision and can have provable recovery guarantees. The learned representation can be used for downstream machine-learning tasks such as clustering and classification. The method is based on the assumption that the observed sequences arise from a common domain, but each sequence obeys its own autoregressive models that are related to each other through low-rank regularization. We cast the problem as a computationally efficient convex matrix parameter recovery problem using monotone \glspl{vi} and encode the common domain assumption via low-rank constraint across the learned representations, which can learn the geometry for the entire domain as well as faithful representations for the dynamics of each individual sequence using the domain information in totality. We show the competitive performance of our method on real-world time-series data with the baselines and demonstrate its effectiveness for symbolic text modeling and RNA sequence clustering.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This work aims to learn the low dimensional representation of sequential data with nonlinear dynamics. It combines low-rank matrix recovery and monotone VI to learn low-rank representation of nonlinear signals, while maintaining the signal recovery problem’s convexity for acceleration. The low-rank constraint is enforced through nuclear norm regularization with proximal algorithms, while the modeling of the nonlinear dynamics and the monotone VI both rely on the monotone nonlinear link function.

### Strengths
1. Well written work, with comprehensive introduction, clear problem statement, detailed methodology presentation and thorough experiments. Pseudocode is also given.
2. Dimension reduction or representation of sequential data is indeed a crucial problem.
3. The method looks novel and sound.
4. The experiments can clearly reflect this method’s efficacy.

### Weaknesses
## Major

1. I think the performances of linear and nonlinear monotone autoregressive models (both with low-rank regularization) might need to be compared with further experiments. It seems to me that the choice of the link function $\eta$ is still kinda restrictive and problem specific, as it needs to be monotone and remains fixed after being selected. Intuitively if a nonlinear $\eta$ is very similar to $\eta(\mathbf{x}) = \mathbf{x}$, the models using them may not be significantly different in terms of performance. Not sure if spending so much effort making the autoregressive model a tad nonlinear is worth it, especially considering that the nonlinear one needs the additional evaluation of $\mathcal{A}$ and $\mathcal{A}^*$. 
    - However, l like this paper overall, so this is not fatal.
    - See Question 2 for more detail.
2. The authors had better mention their method’s limitations and suggests some future research directions. For instance, a few things mentioned in the my questions. 

## Minor

1. You should briefly explain why the *monotone property* of the link function is important when you first introduce it on Line 122 and 132 (like simply referring to Sec. 3.2), or cite related works given that you have so many examples. 
In addition, you should explicitly refer the readers to Line 263 for the accurate definition of  “monotone”. A better option is to turn Line 262 to 269 into a formal Definition block with number (given how crucial monotonicity is to your method), then \ref it on Line 122.
2. Line 136, is the subspace linear? If so, you had better mention it explicitly here, or claim that all subspaces in this work mean linear subspaces.
3. “Geometry” in phrases like “geometry of the subspace” “geometry for the entire domain” “geometry of the representations” is a very awkward term for your work. The subspaces in this work are just flat planes with no special “geometry”. It’s not like you have to deal with Riemannian metric, angle, geodesic, curvature and so forth on a nonlinear submanifold. 
    1. For instance, on Line 154, you can basically just say “the subspace…captures…’’
    2. If you insist on using “geometry”, be clear about what you mean by it. 

## Trivial:

1. Use the correct citation format: \citep and \citet. For example, Line 089. 
2. Typos. For instance:
    1. Line 053: duplicate “indicates”
    2. Line 106 “thewfirst”; Line 285 “spacewof”
    3. Line 115, missing “by”
3. Clarify your special notation when it’s introduced. What is “vec()”? Vectorize? Flatten? 
4. In Table 2, make the best Avg. in each column stand out with bold font.

### Questions
1. Does the link function $\eta$ have to be continuous? 
    - Just curious, where does the name “link” come from originally? Why is it called "link"?
2. Because the $\eta$ is monotone and fixed, does the model in (1) in general have enough complexity to capture the nonlinear dynamics of a complicated sequence, e.g., a sequence with many high frequency components with rather large amplitude? 
    - Which hyperparameters of it can affect the complexity? 
        - If my sequential data have very low $C$ and complicated dynamics, is increasing $d$ basically the only way to increase your model's complexity? Can increasing $d$ always improve the signal recovery effectively?
    - I guess that if the link function is not good enough, $\mathrm{rank}~\mathbf{B}$ cannot be sufficiently reduced, right? How to choose or design one?
3. It seems like the model can be used for denoising by limiting $\mathrm{rank}~\mathbf{B}$. What if some very important signal components have very low SNR, and I don’t care much about the principal signal components with large SNR? Can the model potentially differentiate between them and only remove the noise? 
4. Why does the relative reconstruction error have a quadratic relation w.r.t. $\lambda$ in Fig 1.a? Underfitting and overfitting?
5. How long does it take to search for $\lambda$? Does it scale with the problem’s dimensionality?
6. What is the speed difference between recurrence (8) and (15)?
7. How widely applicable is the assumption "we suppose..." on Line 114 in reality?

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
2

### Summary
This work introduces an unsupervised method for learning low-dimensional representations of sequences. Specifically, it assumes that each sequence relates through a low-rank latent autoregressive matrix, and, by casting the problem as matrix recovery, the authors derive an efficient algorithm to obtain the latent matrix. The authors evaluated the resulting representations obtained by the proposed method in the UCR time-series classification task and clustering on language and genome sequences.

### Strengths
- The paper is well-written and easy to follow. 
- Bringing the matrix recovery technique in sequential learning enables us to efficiently compute latent autoregressive parameters with some theoretical guarantees such as computational complexity and parameter recovery guarantees, which look a good contribution to the representation learning of sequential data.

### Weaknesses
 - Regarding the clustering experiments; it is hard to tell the model's significance since the authors do not include any other model's results. I see the obtained representations by the proposed method are well-clustered in every dataset, but how do they become when using different models (e.g. models shown in table 2.)?


### Questions
Typo
- l:285 the spacewof -> the space of ?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper introduces a novel approach for unsupervised learning of low-dimensional representations for multiple related time series using a monotone variational inequality framework. The approach combines traditional autoregressive modeling with a low-rank regularization, which leads to efficient matrix recovery and nonlinear sequence embedding while maintaining convexity. The authors test their approach through model recovery experiments on synthetic linear AR sequences and applications to real world time series classification and more complex symbolic datasets, such as language and genomics.

### Strengths
- The paper is neatly written, and I overall found the presentation of the figures and clarity of writing nice.
- The paper looks mathematically rigorous and well-rooted in related literature and approaches.

### Weaknesses
 - Method Section: I am admittedly not familiar with much of the literature cited in this section. I appreciate the mathematical rigor but found some details in this section hard to follow. This also makes it harder to assess which parts of this section are novel contributions. A summary section at the end of the introduction or the method section that explicitly states what is novel about this approach could make the main contributions of the paper clearer.

- Results: Linear and Nonlinear Models: The shift between linear and nonlinear models was somewhat confusing on the first read. 
Section 4.3 mentions learning representations for sequences with nonlinear dynamics, but the nonlinear approach seems to be applied earlier in Section 4.2 as well. 

- The model recovery experiments are specifically for the linear case. Clarifying why only the linear model was used for parameter recovery while not applied to real data would help. Is the idea to test the nuclear ball regularization separately in a simpler setting?

- On the other hand, including a direct comparison between the linear and nonlinear models in terms of performance on the real-world data might also be interesting. Vice versa, it could also be beneficial to add parameter recovery experiments for the nonlinear case as well.

- The role of  $\lambda$: what role does the low-rank constraint play on performance? You mentioned you tuned lambda on the training set. Can we learn something about the complexity of the datasets depending on which lambda is optimal? How much better does performance get using $\lambda$, compared to the unconstrained case?

- Choice of comparisons: None of the evaluated comparisons incorporate low-rank constraints. While as the authors mentioned, time series classification is just one example downstream task (that is easy to quantify), some more direct comparison to other low-rank approaches could make the specific advantages of your method more clear.

- Limitations:
There is no discussion of limitations. Besides descriptions of the approach/metrics, it is hard for me to assess what potential shortcomings/challenges the approach faces if I were to use it in practice. Tuning for $\lambda$ is discussed in a lot of detail, but not so much for other aspects of the algorithm. This part could also include something on potential extensions, such as handling higher-dimensional examples.

Typos:
- indicates twice around page break between pages 1 to 2
- Page 3: sufficiently captured an order (missing “by”)
- Page 6: spacewof matrices

### Questions
- Related Work: this is a broad field, so it’s challenging to cover every related approach. A class of approaches that goes in a similar direction which could be mentioned as well are hierarchical (Bayesian) time series models, e.g. Random Effects Models for Longitudinal Data (Laird and Ware, 1982) or dynamical hierarchical models (Zoeter and Heskes, 2003). Likewise, in the field of dynamical systems modeling, there are some approaches going in a similar direction, extracting low-rank representations across multiple observed time series (e.g. CoDA, Kirchmayer, ICML 2022)

Typos:
- indicates twice around page break between pages 1 to 2
- Page 3: sufficiently captured an order (missing “by”)
- Page 6: spacewof matrices

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper introduces an unsupervised representation learning framework for sequential data, formulated as a low-rank matrix recovery problem using a convex optimization approach with monotone VIs.
The framework assumes a shared underlying domain among sequences and enforces this assumption through a low-rank constraint on the learned representations, implemented as a constraint of a nuclear norm ball.
This method is theoretically grounded and shows competitive empirical performance, while achieving provable recovery guarantees.

### Strengths
1. **Theoretical Rigor**: The proposed framework is strongly backed by theoretical foundations, leveraging low-rank matrix recovery and convex optimization over monotone VIs.
The approach is both well-formulated and analytically justified, with provable recovery guarantees under the low-rank assumption, which strengthens the theoretical contribution.
2. **Empirical Performance**: Experimental results support the framework’s ability to recover parameter matrix and demonstrate competitive performance across real-world data.

### Weaknesses
1. **Benchmark Comparisons**: Given the objective of learning representations, it would strengthen the work to benchmark against established representation learning techniques like contrastive learning and masked modeling. The absence of these comparisons makes it difficult to assess the relative strengths and weaknesses of the proposed method in the context of the current state-of-the-art. Specifically, the paper should demonstrate how its method performs against methods that explicitly learn representations by maximizing mutual information between different views of the data (contrastive learning) or by reconstructing masked portions of the input (masked modeling). These are standard approaches in the field, and their omission is a significant gap.
2. **Minor Issues**
    - **Clarity**: Consistency in notation, particularly in equations and indexing conventions such as the program notation in eqs. (6-7) and the loss function in eq. (14), would enhance readability. The current notation makes it difficult to follow the mathematical development of the method. For example, the indexing in equations (6-7) seems to be inconsistent with the loss function in equation (14), leading to confusion about the precise scope of the optimization problem. The paper should clarify the relationship between the variables and indices used in these equations.
    - **Notation**: The notation should be updated to $\mathcal{H}_{i,t}$ for clarity and consistency. The current notation is not sufficiently clear and could be misinterpreted. Using $\mathcal{H}_{i,t}$ would explicitly denote the history of sequence *i* up to time *t*, which is crucial for understanding the temporal dependencies in the model.
    - **Errata**: There are minor typos, such as repeated words on pages 1–2 and “spacewof” instead of “space of” on p6.

### Questions
1. Could the authors elaborate on their choice not to include benchmarks against popular representation learning methods?

### Soundness
3

### Presentation
2

### Contribution
2
