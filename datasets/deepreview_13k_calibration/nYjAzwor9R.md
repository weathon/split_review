# Tree-Wasserstein Distance for High Dimensional Data with a Latent Feature Hierarchy

- Decision: Accept
- Avg Score: 7.00
- Scores: 6, 8, 6, 8

## Abstract
Finding meaningful distances between high-dimensional data samples is an important scientific task. To this end, we propose a new tree-Wasserstein distance (TWD) for high-dimensional data with two key aspects. First, our TWD is specifically designed for data with a latent feature hierarchy, i.e., the features lie in a hierarchical space, in contrast to the usual focus on embedding samples in hyperbolic space. Second, while the conventional use of TWD is to speed up the computation of the Wasserstein distance, we use its inherent tree as a means to learn the latent feature hierarchy. The key idea of our method is to embed the features into a multi-scale hyperbolic space using diffusion geometry and then present a new tree decoding method by establishing analogies between the hyperbolic embedding and trees. We show that our TWD computed based on data observations provably recovers the TWD defined with the latent feature hierarchy and that its computation is efficient and scalable. We showcase the usefulness of the proposed TWD in applications to word-document and single-cell RNA-sequencing datasets, demonstrating its advantages over existing TWDs and methods based on pre-trained models.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper presents a new Tree-Wasserstein Distance that is specifically designed for a hierarchical data and presents a novel flow matching method. This method can be applied to high dimensional data measured at non-equidistant time points without reducing dimensionality, so that the dynamics of the data are not oversimplified. The method is validated on several datasets and showed the improvement compared to existing methods.

### Strengths
I think this paper is a nice combination of three ideas, 1) from finite data construct a hyperbolic embedding, 2) from points in hyperbolic space construct a tree 3) compute tree wasserstein distance on that tree. The part 1) is borrowed from Lin et al. (2023) and part 3) is the usual tree wasserstein distance, but in 2) algorithms and theoretical works seems to be their own and nice combinations from hyperbolic geometry. I felt this originality and signifcance should be appreciated. Although, my research is not in tree wasserstein distance or hyperbolic geometry with machine learning, so I cannot correctly evaluate originality or significance. I think the paper is is clearly written. I think the paper is in general in good quality, though some theoretical results are a bit skeptical: see weaknesses below.

### Weaknesses
In Theorem 1, the latent tree distance $d_{T}$ and the decided tree metric $d_{B}$ are claimed to be bilipschitz with constants $1/\sqrt{2}$ and $1$. However, I am not sure if the bilipschitz constants are correct. The authors just said that "Specifically, by taking $\alpha\rightarrow 1/2$ and $\beta =2$ in
Section 3 in Leeb & Coifman (2016) and Appendix C in Lin et al. (2023), the bilipschitz constants $c$
and $C$ can be determined by $1/\sqrt{2}$ and $1$ in $d_{H} \simeq d_{T}$, respectively." and did not provide detailed proof for why the constant can be $1/\sqrt{2}$ and $1$. However, proofs of Section 3 in Leeb & Coifman (2016) and Appendix C in Lin et al. (2023) are "all up to constants" and did not trace exact constants.

For example, for the Lipschitz constant $1$, i.e., $d_{B} \geq d_{T}$, it is somewhat necessary to argue that $d_{\mathcal{M}} \leq d_{T}$, where $d_{\mathcal{M}}$ is the distance in Lin et al. (2023). In Lin et al. (2023), the corresponding proof is Proposition C.2, and here the constant $1$ contains several constants as $A$ and $\epsilon$ (different from $epsilon$ in the authors' paper). In particular, the $\epsilon$ is from Lemma 3 in Leeb & Coifman (2016), which is $C_{1}\Psi(1) - C_{2}\Phi(A-1)$ in the corresponding proof. It does not seem possible to simplify everything and conclude that we can take the constant $1$.

I think authors should provide proof for how the bilipschitz constants $1/\sqrt{2}$ and $1$, or they should change the statement of Theorem 1 should be weakened to "there exists some constants $C_1$ and $C_2$ so that $C_1 d_B \leq d_T \leq C_2 d_B$".

Another thing is about the hyperparameter tuning. The suggested algorithm is based on the diffusion operator P in Equation (2) to provide similarity between data points. To compute Equation (2), the user needs to determine the scale parameter $epsilon>0$. Hence, I think providing a guideline for choosing $epsilon$ should be helpful to readers, for e.g., Lin et al. (2023) suggested the median of distances between data points multiplied by a constant.

### Questions
I put the suggestions in the weakness.

### Soundness
2

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
3

### Summary
The authors propose an algorithm for constructing a binary tree from data points in the Poincaré half-space. They furthermore propose a method for learning a distance between histograms, assuming a latent hierarchical relation between the bins of the histograms. The method starts with embedding the columns of the data matrix (where each sample/row is a histogram) into Poincaré half-spaces using a combination of diffusion embeddings at multiple scales. In a second step, the tree construction algorithm is applied to these embeddings, resulting in a tree on the bins of the histograms. Finally, they plug this tree into the definition of the Tree Wasserstein distance, resulting in the desired distance between histograms.

For the tree construction algorithm the authors show that, asymptotically in the number of dimensions and scales, it recovers a tree defined by the hyperbolic lowest common ancestor metric on the Poincaré half-space. For the complete method, it is shown that (asymptotically in the number of dimensions and scales) the resulting distance is equivalent within a factor 1/sqrt(2) to TWD using a “ground latent tree” (which is unfortunately left undefined). 

The authors validate the theoretical results using experiments with a synthetic dataset (where “ground latent tree” is a probabilistic graphical model), a text dataset as well as single-cell gene expression dataset.

### Strengths
The proposed method is well-motivated and combines an innovative application of previous results (on hyperbolic diffusion embeddings) with novel contributions (tree construction algorithm based on hyperbolic LCAs).

The paper clearly highlights the contributions. The related work and preliminaries sections are clearly written and contain necessary background material together with the appropriate references. The exposition of the method is at an appropriate level of detail and easy to follow once the preliminaries have been digested. The appendix contains further material related to the efficient implementation of the method.

The problem of computing distances between histograms based on a latent tree is well-motivated by practical applications to single-cell sequencing data.

### Weaknesses
The paper never gives a definition of the "ground latent tree" used in the statements of Theorems 1 and 2. Theorem 1 references Section 4.1, which however does not seem to contain any formal definitions. The proof of Theorem 1 (via Theorem C.1) references Lin et al. (2023) Theorem 1 for the convergence of the manifold metric to the "hidden tree metric". Without a definition of the "hidden tree" or "ground latent tree", the Theorems and the paper as a whole are incomplete. It is unclear how the theoretical results connect to the experimental setup without a precise definition of this ground truth. The experiments use a probabilistic graphical model as the ground truth, but this connection is not made explicit in the theoretical development, leaving a gap in the justification of the method.

At first reading, it was unclear to me what is meant by "features" and "feature hierarchy" and which are the measures to which the Wasserstein distance is eventually applied. The paper states for the first time that it "focuses" on data points that are essentially histograms on page 4, l.172 and only confirms that the method is limited to histograms on page 7, line 372. It would greatly improve the presentation of the paper if the setting was made clear from the start. The lack of clarity regarding the input data type and the specific application of the Wasserstein distance makes it difficult to assess the broader applicability of the proposed method. The paper should explicitly state that the method is designed for histogram data and clarify how the tree structure relates to the bins of the histograms from the outset.

l. 113 V is not defined, should this be [m]?

### Questions
* l. 113 V is not defined, should this be [m]?

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
3

### Summary
In their paper "Tree-Wasserstein distance for high dimensional data with a latent feature hierarchy", the authors consider the problem of constructing a NxN pairwise distance matrix between samples, given a data matrix X of NxM size and under assumption that the M features show some unknown hierarchical organization. The authors suggest a three-stage approach: (1) embed the M features into a hyperbolic space using diffusion eigenvectors; (2) construct a binary tree of the M features from the embedding; (3) use tree-Wasserstein distance between samples given the feature tree. In experiments, the authors argue that resulting distance yields superior kNN classification accuracy in bag-of-words and scRNA-seq datasets.

### Strengths
The paper considers an interesting problem setting, and suggests what seems to be a sensible algorithm. Technically the paper is well done, with high-quality figures and reasonably clear mathematical exposition.

### Weaknesses
The experimental evaluation is missing naive baselines, and in general lacks details.

Overall, I am giving a borderline score which I would be willing to revise upwards (or downwards) based on authors' clarifications regarding the experiments.

### Questions
MAJOR COMMENTS

* All comparisons in Table 1 are with other TWD distances. However, I would like to see a comparison to kNN classification accuracy directly in the feature space (R^M), as a baseline. The main point of the article is that inferring latent feature hierarchy is beneficial, so I'd like to see a comparison to a non-TWD approach. Please use the same distance function as elsewhere (I think you used cosine distance?).

* There are A LOT of TWD methods used for comparison in Table 1. Here I got a bit confused (because I am not familiar with this literature). From the introduction to this paper, my impression was that there are no existing TWD methods that estimate the latent feature tree. So what do all these TWD methods in Table 1 do instead? The description in section 5.1 suggests that you estimate the tree in many different ways and then use TWD with that. Why do all these methods of tree estimation work so much worse than yours? Maybe you need a part in the Introduction / Related work that would introduce these methods and explain what you are doing differently.

* The performance of kNN classification on the X matrix directly for RNAseq or text data will likely strongly depend on the normalization/transformation of the data. In RNAseq literature, row-normalized counts are usually log1p-transformed. In the NLP literature, words counts are usually transformed into TF-IDF with log-scaling. Operating on raw row-normalized counts without any transformation should perform much worse. It wasn't clear to me what data representation you use as input to your TWD benchmarking.


MINOR COMMENTS

* line 39: "due to its exponential growth" -- unclear formulation, whose growth?

* line 113: What is V? This notation wasn't introduced.

* line 126: Usually normalized Laplacian is defined with D^{-1/2} on both sides instead of D^{-1}. So I would expect to see Q hat defined as D^{-1/2} Q D^{-1/2}. Is this a typo? If not, why did you use D^{-1}? You say "following Coifman & Lafon 2006", but I am pretty sure they used D^{-1/2}. Furthermore, I would expect P to be defined directly as D^{-1} Q, instead of \hat D^{-1} \hat Q. Can you clarify?

### Soundness
2

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
This paper presents an approach for learning distances between samples when (a) features are known to exhibit hierarchical structure, and (b) data points are represented as distributions over features. The paper leverages previous work on multi-scale diffusion embeddings to obtain hyperbolic representations of features (not samples) and uses single-linkage clustering to build a tree of said features. The tree-Wasserstein distance is used to compute distances between samples, which leverages (a) the fact that data is represented as a distribution over features and (b) the learned feature hierarchy.

### Strengths
Originality: The idea of learning an explicit hierarchy of features (instead of samples) is a clever one, and it lends itself to applying the TWD when data points are represented as distributions over features. 

Quality: The method appears to beat existing approaches as measured by tree reconstruction quality on synthetic data and nearest neighbor classification accuracy on real data. 

Clarity: The paper is well-written and clear and uses consistent notation.

Significance: Metric learning for data where features exhibit hierarchical structure is important, as this is a common phenomenon. So any effort to (a) recover the feature hierarchy, and (b) extract a metric that reflects that hierarchy is significant.

### Weaknesses
1. The method assumes features are necessarily leaves in the ground-truth feature hierarchy. I can imagine simple situations (in language data) where this may not hold - for example, if 'fruit' was included as a word in the synthetic example provided in the paper, this assumption would not hold, it seems.

2. The construction of the feature diffusion operator could be explained in more detail. Primarily, the computation of the distance between features d(i,j) (which I assume to be the Euclidean distance between X[:, i] and X[:, j]) was not explicitly stated from what I can see. Can the authors add an explicit description of how these distances are computed?

3. On line 150 the LCA relaxation was referenced but never directly defined. Please add a restatement of the definition from Wang et. al in the body of the paper or add a description to the appendix.

4. The method doesn't address cases where the underlying feature tree cannot be isometrically embedded in Euclidean space. Can discussion be added to address this? For example, how would this affect the performance of the proposed approach?

5. No intuition is given for why a single-linkage tree construction approach performs better than other tree constructions given the hyperbolic embeddings. Could some intuition or theoretical justification be added?

### Questions
1. Can you clarify the construction of the diffusion operator as referred to above?
2. Does the method require assuming the feature tree can be isometrically embedded in Euclidean space?

### Soundness
3

### Presentation
3

### Contribution
3
