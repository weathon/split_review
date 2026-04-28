# FairDen: Fair Density-Based Clustering

- Decision: Accept
- Avg Score: 6.75
- Scores: 6, 5, 8, 8

## Abstract
Fairness in data mining tasks like clustering has recently become an increasingly important aspect. 
However, few clustering algorithms exist that focus on fair groupings of data with sensitive attributes. 
Including fairness in the clustering objective is especially hard for density-based clustering, as it does not directly optimize a closed form objective like centroid-based or spectral methods.  

This paper introduces FairDen, the first fair, density-based clustering algorithm.
We capture the dataset's density-connectivity structure in a similarity matrix that we manipulate to encourage a balanced clustering. 
In contrast to state-of-the-art, FairDen inherently handles categorical attributes, noise, and data with several sensitive attributes or groups.
We show that FairDen finds meaningful and fair clusters in extensive experiments.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper proposes a method for fair density-based clustering, whereby the discovered groupings satisfy certain fairness criteria in the context of sensitive attributes.  Whilst fairness criteria have been explored  for other clustering methods, this appears to be the first work that addresses it for density based clustering.  The key insight of the paper is to model density connectivity between points using a continuous representation, that facilitates a so-called fairness-balancing procedure.  The proposed method is distinguished in its ability to handle aspects such as categorical attributes, noise and mixed data.

### Strengths
-fills a gap in the fair clustering literature through its focus on density based clustering.  Density based methods can be particularly attractive through their ability to handle scenarios with categorical data and noise

-proposed method is able to handle scenarios with categorical attributes and mixed type data, in contrast to some baselines.  It can also handle scenarios with multiple sensitive attributes.  It is thus quite “expressive” in terms of fair clustering approaches.

-its formulation leverages well known and principled approaches through spectral clustering

-solid experimental performance in terms of balance for a single sensitive attribute.  Some exploration of the benefits of multiple sensitive attributes.

### Weaknesses
 -approach is potentially expensive computationally being O(d*n^3).  The experiments don’t explore runtime of the method, particularly for larger datasets.  The selected real world datasets appear to be of smaller size. 
  Can this aspect be explored further to provide more insight?

-The proposed method allows inclusion of noise points, which is a strength.  However, it is not so clear from the experiments what can be the advantages of handling noise.  Indeed noise points are specifically excluded in some of the evaluations.  Could a specific experiment be designed to evaluate the role of noise for fair clustering?

### Questions
Figure 1 – it is hard to visually distinguish which methods are producing better clusters.  They all look rather similar.  It’s also hard to visually match the balance and dcsi values to the clusters.  DCSI is mentioned in the caption before it has been defined in the paper.

In Table 2 and Table 3, the ARI/NMI seem very low (close to zero).  Earlier it is mentioned that higher is preferable.  How is one supposed to interpret such low values – is it a drawback of the clustering method?

To what extent would be the approach for the fairness constraint described in 2.2, be extendible to different or multiple fairness constraints?   Does feasibility need to be worked through on a case by case basis?

Can scalability and noise be examined further, as described above.

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
4

### Summary
The paper introduces a new density-based clustering method called FairDen - it is designed to incorporate fairness without compromising the density-based structure of the data.  Fairness has been studied in clusterings, but density-based clustering algorithms have not been studied through the fairness lens.

Density-based clustering methods come with their own merits - eg, they can handle categorical data (or in general, mixed data types) and can handle noise.  FariDen inherits these nice properties.  In addition, it can handle mutiple sensitive attributes simultaneously.  Experiments on real-world datasets show that FairDen produces fairer and more balanced clusters compared to other density-based algorithms and better captures density-based clusters than existing fairness-oriented algorithms - thus achieving the better of both worlds. 

Technically, the key idea is based on Eqn (11) - how to incorporate the fairness constraint into the normalized cut objective.  Eqn (12) essentially summarizes the paper's contribution.  The task then is show how to solve (12) via spectral clustering.  Luckily, the fairness constraint is (rigid and) easy enough to be able to reshape the constrained problem into an unconstrained spectral clustering problem.

### Strengths
* DBScan is widely used and practical clustering algorithm and a fair version of it is a natural question

* The ability to handle categorical data, which is more of a property of DBScan.

* The proposed method can handle several sensitive attributes.

* The paper has good experimental results, showing good outcomes on both the balance aspect as well the density aspect

### Weaknesses
 * The ideas are incremental and largely based on based on existing work.  The dc distance (continuous) formulation is from the KDD paper of Beer et al and solving such problems with spectral methods is quite standard, even in the fairness literature.

* The fairness constraint it treated in a very rigid way, which makes the problem way too simple.  (Eqn (12)).  A more relaxed accommodation of fairness (instead of equality, an approximation in some matrix-norm sense) would be more meaningful here.  Specifically, the constraint enforces strict equality of representation across sensitive groups within each cluster, which is often unrealistic and overly restrictive in practice. A more flexible approach that allows for some degree of imbalance while still promoting fairness would be more robust and applicable to real-world scenarios.

* The scalability of the algorithm is also unclear for large datasets (complexity=O(n^3)), given its reliance on spectral methods.  (This criticism is applicable to some other but not all work on fair clustering).  Combinatorial or sketching algorithms might have better running times.  The paper does not discuss any optimization techniques or approximations to mitigate the computational cost associated with spectral decomposition, which is a major concern for practical applications on large datasets.

* The writing is extremely poor.  It assumes that the reader has a lot of background on the KDD 2023 paper and even about DBScan.  The paper is hardly self-contained - the authors could have written more clearly or provided missing details in the Appendix.  For example, they assume the reader knows what an ultrametric is or an ultrametric leads to a hierarchy ... there are many such instances.  See minor comments below.

Minor comments:

93: not sure e-range is standard -> use eps-radius?

89-93: sloppily written - hard to parse

116: the ddc distance is taken from Beer et al - not even defined in the text

119: what is the hierarchy you are talking about?

127-134: hard to parse

145: state I_k is the kxk identity matrix

161: The model itself is not clear here: what does single index S_i mean?  Is the setting as simple as a bipartite graph of X times S, where edges from X to S denote membership of a user in a sensitive group?  At the end of the sentence, i is used to index attributes where in the beginning, it is used to index the user (data). In fact, for S_{ij} what does i and j stand for?

162: what is k? (i assume # clusters)

167: r_ij is not the whole dataset (as written it reads that way)

176: it might be enough to index balance_{ij} instead of balance_{S_{ij}}

197: what is the quantifier for l in (10)

219: why does the inverse ultrametric even matter?

305: Aren't there are scenarios where heavy bias is inevitable and hence replicating the biases in the clusterng is also inevitable?  

357: again, what is k?

### Questions
The constraint in (11) is very rigid.  Could you methods be adopted to relax it to say an approximation of it?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper presents FairDen, a density based clustering algorithm with group fairness considerations. As it is written in the paper, it is a novel approach, forming fair clusters that supports mixed-type data types, and multiple sensitive attributes, with a weighting mechanism. The contributions include the formulation of the algorithm in an analytical way, and a standard set of experimentation.

### Strengths
Overall, this is a solid work, but to name a few strengths, I can mention these:
1- The method is clearly described with some sound step by step derivation of the last optimization objective.
2- The implementation is submitted as well.
3- The experiments section cover a good set of algorithms and datasets.

### Weaknesses
There are a few things that could be better about this paper. Given these are addressed, I am willing to increase my scores:

1- The limitations, such as the reduced performance on very small sensitive minority groups, are scattered throughout the text. A dedicated limitations section before the conclusion that consolidates these points would be beneficial.
2- Figure 1 is a canonical figure, but could be more clear. Mainly because it is too visually dense and the description of it is broken down into pieces being in introduction section in the beginning and the related works towards the end. As an option, breaking it up into multiple figures with more information rich descriptions, especially, on the third colour used for the DBSCAN sub-figure would be beneficial.
3- In the complexity analysis section, it is mentioned "Note that runtime can be reduced significantly, e.g., by using the GPU for matrix computations.". Although it is becoming a common knowledge that using parallel approaches can decrease practical runtime, this claim does not seem to be supported by an experiment. If there is explicit evidence to support it, it should be added. Otherwise, removal is advised.
4- There are some writing issues that could be fixed:
 4.1- Setting the most common abbreviations such as i.e., and e.g. aside, the paper has numerous abbreviations that is best to be omitted. 
 Here are the list I found: "iff" on line 92, s.t. on lines 117, 221,523,... w.r.t on lines 416, 418 ... 
 A full review of the paper and spelling out the non-standard abbreviations is advised.
 4.2- The line numbers of Algorithm 1 are not appropriately referenced in the text. For example: on line 201, it is ambiguous that (line 4) is 
mentioning Algorithm 1 in the appendix. Making the reference explicit make the paper more readable.

### Questions
Is there minimum number on the count of data types for the algorithm to be effective? In another words, how many numerical features are needed, relatively to be able to form fair clusters given various number of sensitive attributes? Has there been any more studies done on the algorithm that could be included to give more insights on this aspect of the algorithm?

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
This paper proposes a density clustering method based on fair learning. The authors claim that it is the first fair clustering algorithm capable of handling mixed-type data and multiple sensitive attributes simultaneously. The algorithm also includes the ability to detect noise.

### Strengths
1. The proposed method successfully detects fair clusters of arbitrary shapes while achieving balance.
2. The proposed density-based fair clustering method sounds interesting, and research in the field of fair machine learning also enhances contributions to the community.

### Weaknesses
1. The proposed method involves two existing ways to compute similarity matrices, and the form of the objective function is fundamentally consistent with spectral clustering. Although the authors emphasize that the distinction between their method and spectral clustering lies in the Laplacian matrix, this level of innovation is insufficient for ICLR. The core of the method relies on adapting existing similarity measures and applying spectral clustering, with the modification of the Laplacian matrix being a relatively minor adjustment. The novelty of this modification needs to be more thoroughly justified, especially given the extensive literature on spectral clustering and its variations.

2. The discussion on existing fair clustering methods is insufficient and should include the following relevant literature:

[1] Chen X, Fain B, Lyu L, et al. Proportionally fair clustering[C]//International conference on machine learning. PMLR, 2019: 1032-1041.
[2] Esmaeili S, Brubach B, Tsepenekas L, et al. Probabilistic fair clustering[J]. Advances in Neural Information Processing Systems, 2020, 33: 12743-12755. 
[3] Esmaeili S, Brubach B, Srinivasan A, et al. Fair clustering under a bounded cost[J]. Advances in Neural Information Processing Systems, 2021, 34: 14345-14357.
[4]Dickerson J, Esmaeili S, Morgenstern J H, et al. Doubly constrained fair clustering[J]. Advances in Neural Information Processing Systems, 2024, 36.

The paper should also discuss how the proposed method compares to these existing approaches in terms of both methodology and performance. The current discussion is too narrow and does not adequately place the work within the broader context of fair clustering.

3. There are several omissions in the paper. For instance, vol(c) should be vol(c_l), and the output of Algorithm 1 is also unclear. The lack of clarity regarding the output of Algorithm 1 makes it difficult to understand the complete workflow of the proposed method. The paper should explicitly state what data structure is returned by the algorithm and how it is used in subsequent steps.

4. The latest comparison method is from five years ago, which raises questions about the algorithm's effectiveness. Even without involving the most recent fair clustering methods, the referenced conventional clustering methods should not be limited to only DBSCAN. The choice of a single baseline clustering method, DBSCAN, is insufficient to demonstrate the robustness and effectiveness of the proposed approach. The paper should include comparisons with other conventional clustering methods to provide a more comprehensive evaluation.

### Questions
1. Why does Table 3 not include results from other fair comparison methods?
2. Do the experimental results depend on the parameters? The authors did not conduct experiments on this aspect.
3. How does the proposed method address the issue of sensitive attribute combinations (e.g., Black women), particularly regarding the physical meaning of Equation 7? Could the authors provide a detailed explanation?

### Soundness
3

### Presentation
3

### Contribution
3
