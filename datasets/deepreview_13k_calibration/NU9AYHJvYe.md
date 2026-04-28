# Optimal Sample Complexity of Contrastive Learning

- Decision: Accept
- Avg Score: 7.50
- Scores: 8, 8, 6, 8

## Abstract
Contrastive learning is a highly successful technique for learning representations of data from labeled tuples, specifying the distance relations within the tuple.
    We study the sample complexity of contrastive learning, i.e. the minimum number of labeled tuples sufficient for getting high generalization accuracy.
    We give tight bounds on the sample complexity in a variety of settings, focusing on arbitrary distance functions, both general $\ell_p$-distances, and tree metrics. Our main result is an (almost) optimal bound on the sample complexity of learning $\ell_p$-distances for integer $p$.
    For any $p \ge 1$ we show that $\tilde \Theta(\min(nd,n^2))$ labeled tuples are necessary and sufficient for learning $d$-dimensional representations of $n$-point datasets.
    Our results hold for an arbitrary distribution of the input samples and are based on giving the corresponding bounds on the Vapnik-Chervonenkis/Natarajan dimension of the associated problems.
    We further show that the theoretical bounds on sample complexity obtained via VC/Natarajan dimension can have strong predictive power for experimental results, in contrast with the folklore belief about a substantial gap between the statistical learning theory and the practice of deep learning.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies the sample complexity of contrastive learning, which learns the similarity (usually the distance in a metric space) between domain points, given tuples each labeling a most-similar input point to a given point (anchor).

This paper proves matching (or some almost matching) bounds on the sample complexity for contrastive learning of different metrics (arbitrary distance, cosine similarity, and tree metric), with generalization to learning with hard negatives (separated $\ell_2$ distance), quadruplet learning, or learning with $k$ negatives.

The results are based on an output-based assumption: there is an embedding into a $d$-dimensional vector space. This enables reasoning on the VC/Natarajan dimension to study the PAC learning framework, both for the realizable and the agnostic cases, to get non-vacuous PAC-learning bounds with predictive powers.

The proof is on representing the decision boundary of contrastive learning under such metrics as a low-degree polynomial, and upper bounding its number of possible satisfiable sign changes (Lemma 3.5 proved in Section B), hence the largest shattered set of tuples, and VC/Natarajan dimension.

The theoretical result is also experimentally verified on popular image datasets (CIFAR-10/100 and MNIST/Fashion-MNIST), by learning the representations with a ResNet18 trained from scratch with different contrastive losses.

### Strengths
The proof is by _understanding the problem via transforming it_ to another equivalent representation: the decision boundary of contrastive learning under common metrics as a low-degree polynomial, and bounding its number of possible satisfiable sign changes. There is no loss until invoking the algebraic-geometric bounds on number of connected components by Warren, and the sample complexity bounds on Natarajan dimension by Ben David et al. 

And at a high level, the paper shows that when the learned representation is expressive enough (such as ResNet18), PAC-learning bounds (e.g., by VC/Natarajan dimension) can have predictive powers.

The theoretical result is also experimentally verified on popular image datasets (CIFAR-10/100 and MNIST/Fashion-MNIST), by learning the representations with a ResNet18 trained from scratch with different contrastive losses (Appendix F).

### Weaknesses
The proof arguments, while mathematically sound, rely heavily on counting arguments and the pigeonhole principle. This leads to a non-constructive approach, which limits the practical applicability of the theoretical findings. For instance, while the theory effectively explains the observed error rate growth in the experiments (Appendix F), it falls short of providing a clear path towards developing more efficient learning algorithms. Furthermore, the reliance on these counting arguments suggests that the constants derived in the sample complexity bounds are unlikely to be tight. This could be seen as a limitation, especially when considering the potential for optimizing these bounds in future work. A more constructive approach, perhaps one that provides insights into the structure of the learned representations, could significantly enhance the practical implications of this work. Specifically, the connection between the dimensionality of the embedding space and the required number of samples, as suggested by the theory, could benefit from a more detailed analysis. For example, how does the choice of the embedding dimension 'd' impact the learning process for different types of data distributions or network architectures?  While the theory provides general bounds, it doesn't offer specific guidance on how to choose 'd' optimally in practice. The statement that approximately 'nd' samples are needed for a Euclidean embedding layer of dimension 'd' provides a general guideline, but it lacks the specificity needed for practical implementation. How does this requirement change when dealing with different similarity metrics, such as cosine similarity or tree metrics? A deeper exploration of these aspects would strengthen the practical relevance of the theoretical findings.

### Questions
While the experimental results (in Appendix F) verify the growth of error rates as predicted by the theory for ResNet18 on certain parameter ranges, there is not much explanations regarding, e.g., what representations (e.g., deep learning architectures) are expressive enough to achieve the sample bounds as predicted by the theory. That is, the representations (given by the theory) are somehow non-explicit/ineffective, is that the case?

### Typos?

Statement of Theorem 1.3 (Page 4):
The sample complexity of contrastive learning ~for contrastive learning~ under cosine similarity is...

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
Given labeled sample $(x_1,y^+_1,z^-_1),\ldots,(x_n,y^+_n,z^-_n)$, the goal of contrastive learning is to create a distance function $\rho$ such that $\rho(x,y) < \rho(x,z)$. This study comes in theoretical flavour, providing lower and upper bound for sample complexity of contrastive learning via PAC-learning framework. The main ingredient of the proof of the bound is the Natarajan dimension (which is a generalization of the VC dimension) and the results from Ben David et al. (1995). 

Reference:  
S. Bendavid, N. Cesabianchi, D. Haussler, P.M. Long, Characterizations of Learnability for Classes of {0, ..., n)-Valued Functions, Journal of Computer and System Sciences, Volume 50, Issue 1, 1995, Pages 74-86.

### Strengths
- The study covers a wide range of distance functions, both in lower bounds and upper bounds.
- Interesting use of an algebraic geometry result to prove the upper bound.
- The theory is well-supported by the empirical results.
- The authors discuss possible directions for future work.

### Weaknesses
Personally, I find the organization of the results somewhat difficult to follow. For instance, while Section 3 is ostensibly focused on bounds within the $\ell_p$ norm, Theorem 3.1, which pertains to arbitrary distances, seems misplaced. A more logical structure might involve presenting Theorem 3.1 prior to the detailed discussion of $\ell_p$ norm bounds. Furthermore, the clarity of the paper could be significantly improved by dedicating Section 3 exclusively to the case where $k=1$ and reserving Section 4 for the exploration of scenarios where $k>1$. This separation would allow for a more focused and in-depth treatment of each case, enhancing the reader's understanding.

Regarding Table 1, I suggest a few modifications to enhance its clarity and accuracy. Firstly, it would be beneficial to group "$(1+\alpha)$-separable $\ell_2$" alongside the $\ell_p$ category, as they share a common underlying structure. Secondly, the "Same" labels in the table currently create ambiguity. Specifically, the "Same" label for quadruplet learning appears to refer to all preceding distance functions, whereas the "Same" label for $k$ negatives seems to be restricted to $\ell_p$ distances. To avoid this confusion, the authors should revise the table to explicitly differentiate the scope of each "Same" label. For example, distinct labels or more descriptive annotations could be used to indicate whether the label applies to all distance functions or only a subset.

### Questions
See Weaknesses.

### Soundness
4 excellent

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper explores the efficacy of contrastive learning, a method for learning data representations based on labeled tuples that detail distance relationships within the tuples. The main focus is on understanding the sample complexity of this method, which refers to the minimum number of labeled tuples needed to achieve accurate generalization. 

This work provides specific bounds for sample complexity across various settings, especially for arbitrary distance functions, $\ell_p$-distances, and tree metrics. A central finding is that for learning $\ell_p$-distances, a minimum of $\Theta(\min(nd,n^2))$ labeled tuples is sufficient and necessary for depicting $d$-dimensional representations of $n$-point datasets. These results are applicable regardless of the input samples' distribution and derive from bounds on the Vapnik-Chervonenkis/Natarajan dimension of related problems. 

This paper also demonstrates that theoretical boundaries derived from the VC/Natarajan dimension correlate strongly with experimental outcomes.

### Strengths
1. This paper primarily studies the sample complexity of contrastive learning, and provides tight bounds in some settings, including arbitrary distance functions and $\ell_p$-distances for even $p$ and almost tight bounds for odd $p$. For constant $d$, this work also provides a matching upper and lower bound. 
2. This paper studies both realizable and agnostic settings, as is standardly considered in PAC learning. The sample complexity bounds in terms of $\epsilon$ coincide with the standard results in PAC learning in both realizable and agnostic settings. 
3. The proposed proof idea extends to various settings, including the cases where $k >1$ (multiple negative examples in one tuple) and quadruple samples.

### Weaknesses
1. It would be good to provide a thorough comparison with the known sample complexity bounds that appeared in the existing literature. Specifically, the paper should more clearly delineate how its distribution-independent bounds compare to those derived under specific distributional assumptions or using different loss functions. The current discussion lacks concrete examples of how the derived bounds relate to or improve upon existing results in metric learning or contrastive learning literature.
2. While I understand the page limit of the main body, there seems to be relatively less than enough content on the main results of this work in the main body. The presentation of the main theorems and their implications feels somewhat rushed, and the reader might benefit from more detailed explanations and examples directly in the main text. The current structure makes it challenging to immediately grasp the significance of the theoretical results without delving into the appendix.
3. The structure of the paper could be reorganized a bit: e.g., the paragraph "Reducing dependence on $n$" could be part of the discussions after presenting the full main results. This section feels somewhat disconnected from the main flow of the paper and could benefit from being integrated more cohesively with the presentation of the core results. The current placement interrupts the logical progression from the main theorems to their extensions.

### Questions
1. What do you think is the primary season/insight that the upper bounds for $\ell_p$-distances are different between odd and even $p$?
2. Do you think it is possible to characterize the sample complexity bound when the cardinality of $V$ is infinite? 
3. Minor:
- In the paragraph "Outline of the techniques" on Page 4, why "P is some polynomial of degree $2d$"?
- In the paragraph above "Outline of the techniques" on Page 4, $(x_1^-, x_2^-)$ ->  $(x_3^-, x_4^-)$?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
Suppose $V$ is a set of $n$ data points, each embedded into a $mathbb{R}^d$. Suppose we observe $m$ triplets $(x,y,z) \in V^3$ and their labels in $\{ -1, 1\}$ where the label is $1$ if $x,y$ are closer than $x,z$ in the embedding space in $\ell_p$ distance and $-1$ otherwise. The paper gives optimal order for sample complexity $m$ required to get to a misclassification error of $\epsilon$. 

The high level technique is to derive VC dimension (and Natarajan dimension for larger tuples, but we ignore results in the larger tuple case for now). The authors derive nearly tight order for VC dimension of such triplet classifiers. For upper bounding the VC dimension, they formulate the classification function as the sign of a polynomial in $nd$ dimensions. The key ingredient here is a fact from Warren (1968) that there are at most $(4epm/nd)^{nd}$ connected components in $\mathbb{R}^{nd}$ where in each connected component, the signs of the $m$ polynomials are fixed. For proving the lower bound on VC dimension, the authors give a clever construction of a set of triplets which can be shattered.

Authors give their results to realizable and agnostic cases. They extend their results to several distance functions and tuples of size more than 3. They also study the well-separated case where the labeled triplets $(x,y^+,z^-)$ satisfy $\rho(x,z) \geq (1+\alpha) \rho(x,y)$ etc. for some $\alpha > 0$.

### Strengths
* The derivations are interesting, short and non-trivial.
* The results are relevant because contrastive learning is practical.

### Weaknesses
Nothing significant.

### Questions
Typos/Minor comments:
* page 4: Outline of techniques: P is a polynomial of degree $2$, not $2d$.
* Reducing dependence on $n$: It may be good to state bounds with the assumptions mentioned ($k$ latent classes etc.)
* Theorem 3.3 proof, first line: Should it be $d < n$ here?
* In Definition 2.1, the symbol $S_3$ seems to be used before definition.
* Please search for "Kulis Kulis" and "Warren Warren" in the paper and remove such duplicates.
* page 8, second line: Should $<$ be replaced by $\leq$?

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good
