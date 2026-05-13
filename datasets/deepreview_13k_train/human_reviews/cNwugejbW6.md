# SoftHash: High-dimensional Hashing with A Soft Winner-Take-All Mechanism

- Decision: Reject
- Scores: 6, 5, 6, 5

## Abstract
Locality-Sensitive Hashing (LSH) is a classical algorithm that aims to hash similar data points into the same bucket with high probability.
Inspired by the fly olfactory system, one variant of the LSH algorithm called $\textit{FlyHash}$, assigns hash codes into a high-dimensional space, showing great performance for similarity search.
However, the semantic representation capability of $\textit{FlyHash}$ is not yet satisfactory, since it is a data-independent hashing algorithm, where the projection space is constructed randomly, rather than adapted to the input data manifold.
In this paper, we propose a data-dependent hashing algorithm named $\textit{SoftHash}$. In particular, $\textit{SoftHash}$ is motivated by the bio-nervous system that maps the input sensory signals into a high-dimensional space, to improve the semantic representation of hash codes. 
We learn the hashing projection function using a Hebbian-like learning rule coupled with the idea of Winner-Take-All (WTA).
Specifically, the synaptic weights are updated solely based on the activities of pre- and post-synaptic neurons. Unlike the previous works that adopt the hard WTA rule, we introduce a soft WTA rule, whereby the non-winning neurons are not fully suppressed in the learning process.
This allows weakly correlated data to have a chance to be learned to generate more representative hash codes.
We conduct extensive experiments on six real-world datasets for tasks including image retrieval and word similarity search. The experimental results demonstrate that our method significantly outperforms these baselines in terms of data similarity search accuracy and speed.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes SoftHash, a data-dependent hashing algorithm. To overcome the randomness of LSH, SoftHash learns the hashing projection function using a Hebbian-like learning rule coupled with the idea of Winner-Take-All (WTA). This allows SoftHash to adapt to the input data manifold and generate more representative hash codes. The authors also introduce a soft WTA rule, whereby the non-winning neurons are not fully suppressed in the learning process. This allows weakly correlated data to have a chance to be learned, which further improves the semantic representation capability of SoftHash.

### Strengths
Here are some specific strengths of the paper:

1. Overall, the paper is well-written and presents a novel and effective hashing algorithm. The authors provide a clear motivation for their work, and their experimental results are convincing. 

2. The authors evaluate SoftHash on some real-world datasets and tasks, and their experimental results demonstrate that SoftHash significantly outperforms some baseline methods.

### Weaknesses
1. It would be better to include more baselines including Mongoose paper's learnable hash functions[1].

2. Maybe the authors could justify more on the theoretical analysis of the motivation of Softhash. Similar studies would be [2]

### Questions
1. How to provide search quality guarantees for Softhash in retrieval?

2. What is the convergence rate of the SoftHash learning process?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduced a SoftHash, which is a data-dependent hash algorithm. It produces sparse and high-dimensional hash codes. Also, unlike other algorithms such as BioHash, this paper did not use a hard winner-take-all(wta) mechanism. They adopted a soft wta mechanism with an exponential function. The authors conducted experiments on similar image searches and semantical similar word searches.

### Strengths
This paper proposed a new high-dimensional hashing algorithm. The authors use soft WTA to enable the learning of weak-correlated data, which differs from existing work. 

 The paper demonstrated the differences between their algorithm and one existing algorithm BioHash.

The explanation of SoftHash is clear.

### Weaknesses
The experiment part was not clear to me. Many important details are in the appendix or are missing, such as the train/test set split.  I keep the questions in the next section.

1. Appendix D.1 mentioned that for test: "10 query per class for cifar100, 100 for cifar10".  The test size seems small to me. In BioHash, they used 1000 queries per class for cifar10. Any reason why you chose a smaller query size?
2. Appendix D.1 mentioned that "Ground truth is the top 1000 nearest neighbors of a query in the database, based on Euclidean distance between pairs of images in pixel space. " whereas, in BioHash, the ground truth is based on class labels. For me, it makes more sense to use class labels. Is there any reason for using Euclidean distance?
3. Appendix D.1 mentioned that "Output dim is 2000". It is smaller than the 3072-dim input in cifar10/cifar100. Can you explain if this still satisfies high-dimensional hash?
4.  SoftHash-1 and SoftHash-2 used different parameter initialization. The conclusion is that SoftHash2 is better than SoftHash1. But any intuition as to why it's better? Instead of putting them in the main result table, you can put different initialization results as an ablation study. It's really confusing when looking at the main result table because there is no definition of SoftHash 1 in the main paper.
5. I couldn't find train/test split and output dimensions for word search experiments.
6. The reference for "Can a fruit fly learn word embeddings?" needs to be updated: not arxiv preprint; it was published at iclr 2021.

### Questions
1. Appendix D.1 mentioned that for test: "10 query per class for cifar100, 100 for cifar10".  The test size seems small to me. In BioHash, they used 1000 queries per class for cifar10. Any reason why you chose a smaller query size?
2. Appendix D.1 mentioned that "Ground truth is the top 1000 nearest neighbors of a query in the database, based on Euclidean distance between pairs of images in pixel space. " whereas, in BioHash, the ground truth is based on class labels. For me, it makes more sense to use class labels. Is there any reason for using Euclidean distance?
3. Appendix D.1 mentioned that "Output dim is 2000". It is smaller than the 3072-dim input in cifar10/cifar100. Can you explain if this still satisfies high-dimensional hash?
4.  SoftHash-1 and SoftHash-2 used different parameter initialization. The conclusion is that SoftHash2 is better than SoftHash1. But any intuition as to why it's better? Instead of putting them in the main result table, you can put different initialization results as an ablation study. It's really confusing when looking at the main result table because there is no definition of SoftHash 1 in the main paper.
5. I couldn't find train/test split and output dimensions for word search experiments.
6. The reference for "Can a fruit fly learn word embeddings?" needs to be updated: not arxiv preprint; it was published at iclr 2021.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes a new data-dependent hashing algorithm called SoftHash based on a Hebbian-like update rule from biology. The method iteratively trains projection weights and biases using both the input data $x$ and output $y$, and generates sparse binary codes by a topk filter on $y$. Experiments show that SoftMax performs better than several previous methods in preserving the cosine similarity between the data points, as well as in dowsnstream similarity search tasks.

### Strengths
The presentation is in general clear and easy to follow. There are some grammar issues, e.g., "Such that, ...". A proofread is suggested.

In my understanding, the main algorithmic contribution is to improve the prior BioHash algorithm by replacing the hard thresholding with a softmax function. The idea seems plausible and should work, as one can always add a hyperparameter to softmax to make it a hard thresholding. The method introduces more flexibility.

### Weaknesses
1. Some similar contents have already appeared in other works. For example, the paragraph saying "$w_i$ is implicitly normalized" is similar to the text around Eq (3) in the BioHash paper (except that $Topk(y)$ is replaced by $y$). Eq (7) also has similar form in the BioHash paper. A clear comparison should be made in the paper regarding the difference and connections.

2. The design is not very well motivated and rather simple. If we write Eq (2) in your notation for SoftHash, then Oja's rule should be $\eta u_j(x_j-w_j^iu_j)$. The difference with Eq (3) is that the first $u_j$ is replaced by $y=softmax(u)$. The difference is that you added a non-linear softmax function on the scalar. Why is softmax used, can we use other functions? Is there also "biological interpretation" for that?

3. From the experiments, it seems that the SoftHash requires some delicate tuning on several floating parts. The choice of hyperparameters and tuning strategy need further explanation. Ablation study is also needed to understand the performance of the proposed method.
(1) SoftHash-1 and SoftHash-2 are not explained in the main paper, please revise. From the appendix, it seems that they refer to 2 different weight initialiation methods (uniform and Gaussian). Why is the performance gap so big given that this approach is learning-based? This is confusing to me. Also, why is the batch size set as 3584? It that carefully picked or just a random number?
(2) For BioHash, why you used $p=4$ and $\triangle=0.4$ and $0.3$? For SoftHash, how is the temperature paramter $T$ chosen? Did you tune these parameters?

### Questions
1. Does BioHash have the bias term $b$ in the model? How important is this bias term? Any empirical results for illustration?
2. I think "ConvHash" is usually referred to as "SimHash" or simply "LSH". Perhaps changing the name would be better.
3. Is the "Sokal and Michener similarity function" simply the Hamming similarity? If so, using the later is more straightforward.
4. In Table 2, what are the metrics when the code length is larger (256, 512)?
5. Is there an interpretation of Oja's rule in terms of gradient-based optimization? It seems that Eq (2) is the gradient of $||x-wy||^2$? Is it related to the clustering formualtion you mentioned?
6. There is a recent paper [SignRFF: Sign Random Fourier Features, NeurIPS 2023] that extends SimHash to non-linear features. It may perform better than SimHash on some datasets. Please consider adding this baseline as well as deep hashing methods to make the experiments stronger.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
Inspired by the bio-neverous system of fruit fly and existing work bio-hash, this paper proposed a data-dependent hashing method dubbed SoftHash, which is characterized in three aspects: (1) a novel algorithm what can generate sparse and yet discriminative high-dimensional hash codes; (2) a mechanism that combines a Hebbian-like local learning rule and the soft WTA; (3) evaluation on image retrieval and word similarity search tasks.

### Strengths
(1) A novel algorithm: The proposed SoftHash is interesting with simple and effective interpretable learning mechanism.
(2) Solid experiments: two different kinds of tasks, image retireval and word similarity search, are designed to validate SoftHash's good performance in compact semantic embeddings.

### Weaknesses
(1) There are many places that were not clearly explained, such as, what is ConvHash? what is the difference between SoftHash-1 and Soft-Hash-2? The description of ConvHash is too vague, lacking details on the random matrix generation and the specific form of the sign function. The distinction between SoftHash-1 and SoftHash-2 is also unclear; the paper should explicitly state what aspects of the weight initialization differ (e.g., mean, variance, distribution type) and how these differences impact the learning process and final hash code quality.
(2) Why not just choose SH and ITQ? there are more similar papers such as SGH [1], DGH [2], COSDISH [3]? The paper should justify why the chosen baselines are sufficient and why other relevant methods, especially those that also employ graph-based or discrete hashing techniques, are not included in the comparison. The absence of these comparisons makes it difficult to assess the true novelty and performance of the proposed method.
(3) W.r.t. others, please refer to the Question part.

### Questions
I have several questions listed as follows:
(1) What is the main differences between the bio-inspired hashing methods with sparse-and-high-dimensional {0,1}-vectors and the conventional hashing methods with dense-and-low-dimensional {0,1}-vectors?
(2) How does the bio-inspired hashing codes capture the data samples' semantics?
(3) With respect to the storage and computation, how does the bio-inspired hashing approaches realize economic memory and fast retrieval/semantic computing?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
