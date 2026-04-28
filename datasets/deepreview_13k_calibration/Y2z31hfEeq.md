# Discovering Data Structures: Nearest Neighbor Search and Beyond

- Decision: Reject
- Avg Score: 5.25
- Scores: 5, 3, 8, 5

## Abstract
We propose a general framework for end-to-end learning of data structures. Our framework adapts to the underlying data distribution and provides fine-grained control over query and space complexity. Crucially, the data structure is learned from scratch, and does not require careful initialization or seeding with candidate data structures.
We first  apply this framework to the problem of nearest neighbor search. In several settings, we are able to reverse-engineer the learned data structures and query algorithms. For 1D nearest neighbor search, the model discovers optimal distribution (in)dependent algorithms such as binary search and variants of interpolation search. In higher dimensions, the model learns solutions that resemble k-d trees in some regimes, while in others, elements of locality-sensitive hashing emerge. Additionally, the model learns useful representations of high-dimensional data and exploits them to design effective data structures. We also adapt our framework to the problem of estimating frequencies over a data stream, and believe it could be a powerful discovery tool for new problems.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper aims at discovering data structures for nearest neighbor search in an end-to-end manner. The method proposed in this paper employ two networks, i.e., data-processing network and query execution network, for the purpose. The proposed method is pretty costly such that only very few data points are included in the experiments, which makes the method difficult to be evaluated for its practical usefulness.

### Strengths
S1. This paper studies an interesting problem. 

S2. The method may work. 

S3. It is a novel work.

### Weaknesses
W1. The method proposed is too costly for finding such data structures. 

W2. The experiments are not sufficient to support its practical usefulness. 

W3. The data structures found seems too simple, i.e., sorting and K-d trees.

### Questions
Q1. Is it possible to verify the effectiveness of the method with a large data that approaches the real applications?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The article proposes an end-to-end learning framework for data structures, and implement it in the cases of sorting, nearest neighbor search, and frequency estimation. The method is based on joint learning of a data processing network (8 layer transformer model in the implementation of the article) and query processing networks (MLPs in the implementation of the article). The data processing network is used to learn an index structure by ranking and then sorting the original data set. The query processing networks are trained to predict the correct output (e.g., the nearest neighbor of the query point) given the output of the data processing network and the query execution history (i.e., the outputs of the earlier lookups). 

The proposed framework differs from the earlier work on learning-augmented data structures since it does not require specifying the data structure that is used, but is completely end-to-end. The authors test they approach on very small ($N \approx 100$, $d =1,2,30$) simulated data sets, and show that it can match the performance of or outperform simple worst-case algorithms and data structures, such as binary search, k-d trees, and locality-sensitive hashing (LSH).

### Strengths
The proposed framework is novel as far as I know. It is curious that the models learn to replicate binary search and a k-d tree structure. The article is well-written and easy to follow.

### Weaknesses
The article is very exploratory. The data sets are simulated and several magnitudes smaller ($N \approx 100$) and have smaller dimensionality ($d=1,2,30$) than the ones used in the practical applications of nearest neighbor search, and the baseline algorithms are very elementary. While the results have some curiosity value, it seems very unlikely that the proposed method could be (a) scaled to the data sets that are used in the real applications of nearest neighbor search (typically, $N>1000 000$ and $d \in [100,1000]$ ) AND (b) match the performance of SOTA approximate nearest neighbor search algorithms, such as ScaNN (Guo et al., 2020) and HNSW (Malkov & Yashunin, 2018). And even if it were be possible, this would require enormous computational resources.

Approximation algorithms, such as approximate nearest neighbor search, are used to _save_ computational resources and speed up ML pipelines that use computationally heavy components. For instance, ANN search has recently been used for approximate attention computation in transformer models (Kitaev et al. 2020; Roy et al., 2021), and to speed up inference in retrieval-augmented generation (RAG) (Borgeaud et al., 2022; Lewis et al., 2020). 

Thus, I really fail to see how adding a computationally intensive component, such as a transformer model, to the approximation pipeline could be a useful or valuable contribution, even though it resulted in a slightly decreased query latency compared to the SOTA ANN algorithms (which the article is not even close to demonstrating). In contrast, the SOTA ANN libraries, such as FAISS and ScaNN (Douze et al., 2024) use elementary tools, such as $k$-means clustering, for indexing. This is because they have to scale to billion-scale data sets, and thus the index construction time has to be reasonable.

### Questions
I do not have any particular questions for the authors.

### Soundness
3

### Presentation
4

### Contribution
1

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper proposes using deep learning to create data structures. The model learns to rank, i.e. learns a mapping of data element to scalar. The model optionally also can output further auxiliary data to help accelerate the data structure. Querying is performed by M lookups into the data structure, where each lookup is chosen by a separate MLP. The Mth lookup is the query result.

This paper looks at the following data structure problems:
* 1D nearest neighbors
* 2D, 30D, and MNIST (high-dimensional with structure) nearest neighbors
* Frequency estimation, done with a separate model architecture.

The paper shows that the models are effective and adapt to the data distributions presented to it during training.

### Strengths
* Impressive visualizations and demonstrations of distribution awareness: the plots showing k-d tree resemblance and effectiveness over binary search on a 1D Zipfian distribution were especially impressive.
* Novel idea with good execution
* Paper is well organized and written, and easy to follow

### Weaknesses
 * Impractical for now: only works for small datasets (100 and 500 elements were tested).
* Still requires a moderate amount of inductive bias: for example, the frequency estimation architecture is very different than the nearest neighbors one, and does not seem obvious to me. It seems that generalizing this approach to new data structure problems isn't entirely trivial and requires at least some trial-and-error, as well as expertise in how classical approaches to the data structure may work. The specific architecture choices for frequency estimation, such as the use of a separate model and the specific tokenization method, lack clear justification and appear somewhat ad-hoc. The reliance on problem-specific architectures undermines the claim of a general framework.
* In short, the main advantage of this paper's idea is its ability to adapt to data distribution, but the real-world benefit of this is hampered by the fact that for now, this work cannot scale to datasets large enough for distribution-fitting to really show impact (especially when considering the performance impact of MLPs vs, for instance, comparing integers in a BBST). The overhead of using MLPs for lookups, even with a small number of lookups M, is likely to be significant compared to the highly optimized comparison operations in traditional data structures. The paper does not provide a detailed analysis of the computational cost of the MLPs, making it difficult to assess the practical feasibility of the approach.
* No code release, especially disappointing given that the training tasks require only synthetic data and MNIST, and involve small models.

### Questions
Do you have code to share to replicate your results?

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper presents a framework for end-to-end learning of data structures, enabling deep learning models to autonomously discover efficient data structures optimized for specific data distributions. The framework is applied to two problems: nearest neighbor (NN) search and frequency estimation. Key findings include the model learning sorting and search strategies for NN search that rival or outperform traditional methods like binary search, k-d trees, and locality-sensitive hashing (LSH) in some cases. Beyond NN search, the authors apply the model to frequency estimation in data streams, where it demonstrates competitive performance with traditional data structures like CountMin Sketch.

### Strengths
S1. The paper is well-motivated and the problem is interesting. The paper is motivated based on the observation that many data structures are designed to be worst-case optimal and agnostic to the underlying data and query distribution. Neural networks show potential in other tasks e.g. SAT solving. So it is natural to study if neural networks can learn data structures that are optimal for specific data and query distribution in an end-to-end manner.

S2. Experiments show that the proposed framework shows a potential to learn the distribution-specific data structures that are more efficient than the traditional worst-case optimal data structures with synthetic data and the mnist dataset, for the problem of NN search and frequency estimation. This demonstrates the potential of applying neural networks to learn data structures.

### Weaknesses
W1: The paper’s reliance on a transformer model with self-attention for data processing presents efficiency and scalability issues for the NN search task. The self-attention mechanism incurs a computational complexity of $O(n^2)$, limiting its application to datasets with a few hundred points due to memory and processing constraints. Considering the NN search problem has a trivial solution with $O(n)$ complexity, this constraint raises concerns about the framework's practicality in real-world applications where much larger datasets are typical. The indexing cost of $O(n^2)$ is prohibitively high, especially when considering the additional overhead introduced by the model parameters, making it questionable to adopt such a costly approach when its effectiveness appears only comparable to common baselines. While the authors suggest that alternative models, such as linear transformers, could reduce costs, they do not present results to substantiate these claims. A more scalable approach, such as a different backbone structure, could significantly extend the applicability of this work by reducing computational demands and enabling a larger $n$. Without such efficiency improvements, the method is impractical.

W2: Most experiments rely on synthetic data, except for the MNIST image dataset, which limits the framework's demonstration of generalizability to learn challenging real-world data distributions. While synthetic data offers control over distributions, testing on real-world datasets with unknown or complex distributions would better illustrate the framework’s ability to discover meaningful data structures. The additional results on the SIFT (128-dim) and Fashion-MNIST (100-dim) datasets are appreciated, however, in Fig. 26, the results for the proposed method are not particularly strong, ranking only 3rd. The explanation that hyperparameter tuning was omitted to respond quickly to reviewers is difficult to accept, as it leaves uncertainties about the model's true potential. It would be more convincing to provide tuned results, even in subsequent revisions.

W3: The paper’s methodology section lacks sufficient clarity on some technical aspects.
- (1) The paper uses NanoGPT, a decoder-only transformer that typically requires discrete tokens for input and output. However, the paper doesn’t clearly explain how continuous data inputs are tokenized or how outputs are transformed into the scalar ranking $o_i$ values. More detail on the embedding and decoding process for continuous data is necessary to understand the data flow and model structure.
- (2) In experiments involving CNNs, essential details about the CNN architecture, such as the number of layers, kernel sizes, or feature extraction strategies, are missing. Including these specifications would make it easier to interpret the model's capabilities and constraints, especially regarding performance in high-dimensional settings.

W4: For high-dimensional NN search, the paper compares its model only against the data-independent LSH baseline. However, recent advancements in unsupervised learning-to-hash methods provide competitive alternatives that also leverage data distribution knowledge, for example [1] and [2]. Including comparisons with these modern hashing approaches could help position the framework’s performance more accurately within the field and reveal any advantages or limitations when competing with other data-aware methods.

W5: The transition from NN search to frequency estimation is somewhat abrupt and lacks a unified explanation of how these tasks fit within the general framework. The two tasks use different backbones and have different outputs for each component. While both applications involve end-to-end data structure learning, the framework’s flexibility for adapting to different problems is not fully articulated. Clarifying the underlying principles that guide network design for new tasks within the framework would enhance its usability. The response primarily reiterates points from the original paper without offering substantial new insights or clear illustrations of how the framework unifies the two problems. The explanation still gives the impression of two separate methods rather than a truly cohesive framework. Additionally, generalizing this framework to other data structure problems is not straightforward. It requires considerable trial-and-error, along with expertise in the classical methods for the specific data structures being addressed. This lack of explicit design principles or guidelines limits the framework’s scalability, making it challenging for researchers to adapt it to new problems without substantial domain knowledge and iterative experimentation.

### Questions
1. Could the author discuss the justification for why a transformer with $O(n^2)$ complexity is necessary, and why using such a network is still feasible and beneficial for the NN search task? (W1)

2. Could the author demonstrate how well the model performs on real-world data distributions in addition to MNIST by including other real-world datasets that may not follow synthetic patterns? (W2)

3. Could the author clarify the implementation details and/or provide the code for the experiments? (W3)

4. Is there a reason that more recent learning-to-hash methods were not included as baselines for the high-dimensional nearest neighbor search experiment? (W4)

5. The application of the framework to nearest neighbor search and frequency estimation seems somewhat disconnected. Could the authors elaborate on the principles that unify these applications within the framework? Could the authors provide a set of design principles or guidelines for adapting the framework to other tasks? This would make it clearer how researchers can extend this work. (W5)

### Soundness
3

### Presentation
2

### Contribution
2
