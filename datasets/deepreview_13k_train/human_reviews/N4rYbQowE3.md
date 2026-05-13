# Learning-Augmented Search Data Structures

- Decision: Accept
- Scores: 6, 6, 8, 8

## Abstract
We study the integration of machine learning advice to improve upon traditional data structure designed for efficient search queries. Although there has been recent effort in improving the performance of binary search trees using machine learning advice, e.g., Lin et. al.  (ICML 2022), the resulting constructions nevertheless suffer from inherent weaknesses of binary search trees, such as complexity of maintaining balance across multiple updates and the inability to handle partially-ordered or high-dimensional datasets. For these reasons, we focus on skip lists and KD trees in this work. Given access to a possibly erroneous oracle that outputs estimated fractional frequencies for search queries on a set of items, we construct skip lists and KD trees that provably provides the optimal expected search time, within nearly a factor of two. In fact, our learning-augmented skip lists and KD trees are still optimal up to a constant factor, even if the oracle is only accurate within a constant factor. We also demonstrate robustness by showing that our data structures achieves an expected search time that is within a constant factor of an oblivious skip list/KD tree construction even when the predictions are arbitrarily incorrect. Finally, we empirically show that our learning-augmented search data structures outperforms their corresponding traditional analogs on both synthetic and real-world datasets.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper considers the problem of augmenting search data structures like skip lists and kd trees with learning advice, in particular, an oracle that gives (possibly erroneous) estimates of the probability of query elements. When the oracle estimate is perfect, the search time for the proposed data structure is within a factor of 2 of the optimal expected search time (upto a constant additive slack). The estimator is also shown to be robust to errors in oracle estimates. For instance, even if the oracle is arbitrarily erroneous, the expected search time is still within a constant factor of the search time for the corresponding oblivious data structure. The superior performance of proposed data structures is also shown with experiments.

Some details of data structure construction: 

Skip lists: Skip lists are built in levels, with the bottom level as an ordered linked list. Higher levels store subsets of items to speed up search. Traditional skip lists promote items to higher levels randomly with a fixed probability (e.g., 1/2). In the proposed skip list, if an item's oracle probability exceeds a level dependent threshold, it is promoted up with probability 1 (this leads to faster access for more frequent items). For other items, they are still promoted up with a fixed probability (this leads to robustness to errors in oracle).

Kd tree: In traditional kd trees, each node splits the points according to the median across a selected dimension, iterating between different dimensions at different levels of the tree.  In the proposed data structure, one doesn't necessarily iterate between dimensions. The splitting point and dimension at any node is chosen such that the probability of the query being on either branch is as close to 0.5 as possible.

### Strengths
The part on skip lists is a complete and meaningful contribution. The idea of promoting higher frequency elements to higher levels with more probability is both natural and easy to implement. Optimality as well as robustness of the proposed data structure is shown, and it is also shown to be superior in practice with both perfect and erroneous oracles.

### Weaknesses
The part on kd trees felt rushed and left me confused about both the motivation and the details of the setting.

Motivation: In the paper, kd trees are considered for doing lookups for high dimensional points (as opposed to nearest neighbor search). But if one is just interested in lookups, it is unclear to me why we need kd trees. Why not just use something like the proposed skip lists after labeling the points from 1 to n? If we want to also support fast membership queries for frequent items not in the dataset, we can also add them to the skip list as is done in the current kd tree construction.

Setting: In the kd tree part, there is a big universe of items and a subset of it constitutes the dataset. The query can be any element in the universe. While in the skip list part, the  the query is always one of the dataset elements. Both settings seem reasonable but I was confused why different settings are considered in the two scenarios. It would be great if this can be clarified in the paper.

Details of the algorithm: It would be good to spend a paragraph discussing various algorithmic choices like was done in the skip list part (space doesn't seem to be a concern as the paper is already half page below the limit). For example, the motivation for handling low probability elements (prob less than 1/n^2) differently was unclear to me as there can be at most n of them. Also, if the authors can elaborate a bit more on how they are handling these points, that would be helpful.

### Questions
My main question is about the motivation of the kd tree setting as stated in the weaknesses section. 

Another question: Would the proposed skip list data structure be able to handle deletions? For instance, if we delete some elements after constructing the dataset, would it still have the property that for the remaining elements, the data structure is close to optimal wrt the adjusted relative query frequencies? It would be good to include some discussion of deletion in the paper.

Minor formatting comment: The font size used for plots needs to be made larger.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper proposes learning-augmented search data structures based on skip lists and KD trees. The authors achieve optimal expected search time and demonstrate robustness to inaccurate frequency predictors. Experimental results verify the effectiveness of the proposed algorithms.

### Strengths
1. The integration of learned frequencies into skip lists and KD trees is well-constructed and achieves optimal performance.
2. Experiments show that the proposed algorithm outperforms classical algorithms and is robust to noise.
3. The paper is clearly written and easy to read. The ideas are simple, yet novel and effective. I appreciate the clear comparison

### Weaknesses
 1. The authors slightly overstate their contributions. For example, the claim of constant expected search time under the Zipfian distribution holds only when the exponent $s>1$, which is due to the entropy being of constant order (Lemma 2.3). In other words, for any data structure that achieves optimality has the same property. Additionally, in the abstract, the claim on the robustness when predictions are arbitrarily incorrect is not what you describe later.
 2. The noise robustness measure, denoted as $(\alpha,\beta)$-noisy, is somewhat unconventional and may lack generality. It is not clear how this definition relates to more standard measures of distribution divergence, such as total variation distance or KL divergence. The lack of connection to these established metrics makes it difficult to interpret the practical implications of the $(\alpha,\beta)$-noisy definition.
 3. The experiments do not include comparisons with other learning-augmented algorithms given frequency predictions.
 4. A closely related work [1] is not discussed in the paper, where the authors propose learning-augmented search trees that achieve optimality for arbitrary input distributions.

### Questions
1. In the abstract, the paper claims that for Zipfian distribution, the expected search time for an item is constant, while the traditional skip list or KD tree has an expected search time of $O(\log n)$. However, I could not find a detailed explanation for this claim in the main text. Specifically, is there theoretical support for vanilla skip lists (without learning) showing that the expected search time is $\Omega(\log n)$ under a Zipfian input distribution?
2. In the abstract, the paper claims for arbitrarily incorrect predictions, the algorithm is within a constant factor. Does this exactly come from your $(\alpha,\beta)$-noisy definition?
2. The noise robustness measure is unconventional. I suggest using KL divergence to quantify the distance between the predicted and true frequency distributions, as it may provide a more standard and interpretable measure of prediction accuracy.
3. I suggest adding additional experiment comparisons with other learning-augmented algorithms.

### Soundness
4

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
The  studies using machine learning models for improving other machine learning algorithms, namely search algorithms that use efficient data structures to organize data elements. 

The paper considers skip lists and KD-trees and augments them by adding an output of a learning algorithm. Skip lists organize data probabilistically in hierarchical and traversal is similar to binary search but with larger number of splits.

The paper consider unbalanced data distributions, mentioning that unbalanced distributions may result in suboptimal balancing behavior when underlying data structure construction algorithm expects balanced data. Authors propose to use an external machine learning algorithm that predicts statistics of the input data and provides an information to adjust the baseline search algorithm and data structure.

Proposed learning augmented skip list uses predicted probabilities to promote items to next levels with exponentially increasing required thresholds for predicted probabilities. 

While it may seem reasonable to use simple frequency estimation when number of possible items is not large, when number of items in the dataset is larger than number of encountered queries, having a machine learning oracle estimate expected frequency of previously unseen queries is a good idea. The work allows using such oracles to improve search data structures and proves better bounds on search time in general case and in case of an important and popular in real world datasets Zipfian distribution; and proves similar bounds for noisy oracle (representing real machine learning model with positive probability of incorrect guesses).

The idea behind learning augmented KD-tree is to make sure that each node or leaf has same probability on each tree height. Oracle predicted probabilities are used to ensure balanced splitting, improving search time if the oracle is usually correct. To limit algorithm complexity, low probability items are inserted into the tree using conventional approach. Similar bounds, as in case of skip lists, are proven for the augmented KD-tree.  

Empirically, the paper shows constant factor speedup of the augmented data structures, compared to the conventional approach

### Strengths
- Provided approach is an elegant way to improve search data structure performance by considering probabilistic nature of the data. 
- Given the abundance of machine learning and statistical methods to serve as an oracle, proposed approach can be widely used in practice.
- New bounds were proven theoretically and experimental results partially support the theoretical findings.

### Weaknesses
 - From the paper it was not fully clear how to use proposed method with real machine learning oracle models (that non-trivially predict frequencies), instead of statistical oracles (that just calculate the table of frequencies).
- Some graphs, such as Figure 2, show a constant factor speed up. It would be nice to clarify what is theoretically predicted speedup in the cases of various datasets and parameters, and how theory aligns with practice.

### Questions
- In the experiments, as I understood, simple history-based oracles were used. Is it the main use-case of the proposed method, or do we expect large oracles, such as deep learning models to be used as well?
- If the main use case will be using large machine learning oracles, I have the following question: for example, for image search, an oracle can be a neural network that takes an image and outputs expected query frequency; or for text search it could be a language model that outputs expected frequency of text or part of the text -- will the accuracy of real-world machine learning models be enough to guarantee improvement over conventional search structures?
- Would be nice to present graphs with theoretically expected improvement and actual improvement in various settings.

### Soundness
3

### Presentation
4

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
The paper studies search data structures augmented with an "oracle" (some ML-based prediction) of query frequencies, which can be used to improve over the classical setting that assumes no foresight into the query distribution. It focuses specifically on skip lists and KD-trees. It develops ML-augmented analogs, proves bounds on their performance under perfect and imperfect predictions, and presents an empirical evaluation.

### Strengths
The problems are interesting and relevant, the theoretical results seem solid, and the empirical results show improvement. It is overall a solid submission.

### Weaknesses
-- No related work section nor discussion, except for a couple of very specifically related recent/concurrent papers. No broader positioning in the literature; even though there is past work on very similar topics which goes unmentioned and unreferenced (like learning-augmented KD-trees in Cayton et al., see below).

-- The font size in the figures is beyond excusable

### Questions
How do your methods and results compare to the learning-based data structures of Ailon et al. Cayton et al., and other works related to those? They seem to study very similar problems in related settings.

Ailon, N., Chazelle, B., Clarkson, K. L., Liu, D., Mulzer, W., & Seshadhri, C. (2011). Self-improving algorithms. SIAM Journal on Computing, 40(2), 350-375.

Cayton, L., & Dasgupta, S. (2007). A learning framework for nearest neighbor search. Advances in Neural Information Processing Systems, 20.

### Soundness
3

### Presentation
3

### Contribution
2
