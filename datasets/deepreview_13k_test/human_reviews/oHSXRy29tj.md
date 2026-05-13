# Hierarchical overlapping clustering: cost function, algorithm and scalability

- Decision: Reject
- Scores: 6, 3, 6, 5, 8

## Abstract
Overlap and hierarchy are two prevalent phenomena in clustering, and usually coexist in a single system. There are several studies on each of them separately, but it is unclear how to characterize and evaluate the hybrid structures yet. To address this issue, we initiate the study of hierarchical overlapping clustering on graphs by introducing a new cost function for it. We show the rationality of our cost function via several intuitive properties, and develop an approximation algorithm that achieves a provably constant approximation factor for its dual version. Our algorithm is a recursive process of overlapping bipartition based on local search, which makes a speed-up version of it extremely scalable. Our experiments demonstrate that the speed-up algorithm has good performances in both effectiveness and scalability on synthetic and real datasets.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors introduce a novel cost function for hierarchical overlapping clustering and methods for approximating an optimal solution based on local search.

### Strengths
S1) Clusterings that are hierarchical and at the same time overlapping are an important research area. The authors suggest a fitting and coherent solution for a cost function that is consistent with existing research. 

S2) The paper is written well, the authors explain their methods and give the intuition behind them. 

S3) Supported by theoretic proofs.

### Weaknesses
W1) Experimental evaluation should contain more methods than just one baseline competitor. 

W2) I'm also missing a more extensive evaluation of the method regarding the datasets. How does your cost function perform for different numbers of clusters, different percentages of overlap, and different models of clusters (centroid-based vs arbitrarily shaped)?

W3) The only baseline results are taken from the original paper they were reported in as the authors were "not able to compile correctly their codes published online". Usually, one would reimplement the method based on the publication s.t. it is possible to compare the methods for more experiments. 

Small note: the citation format is sometimes a bit off, especially when the publication is referred to by the authors' names (e.g., lines 094 - 102 : try that the authors's names are not just repeated twice)

### Questions
Q1) How is the NMI computed in Figure 1? As far as I know, there is no standard way to include the concepts of overlapping and hierarchical clustering in the evaluation with NMI, so how did you measure it?

### Soundness
2

### Presentation
3

### Contribution
4

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper presents the problem of hierarchical overlapping clustering (HOC) for graph data, where clusters may overlap and form hierarchies. The paper presents a cost function for the problem, characterises it formally, and introduces an algorithm that builds on a restricted 2OC version of the problem. It presents lower and upper bounds, as well as approximate versions with guarantees. It presents an  empirical comparison with an existing 2OC solution.

### Strengths
S1. The paper is generally well-written and the structure is easy to follow.
S2. The study of hierarchical overlapping clusters on graphs is an interesting potential contribution.
S3. The formalisation and theoretical analysis is adequate.

### Weaknesses
W1. The paper should be revised to more clearly present the differences in the problem definition to existing problems OC and HC, respectively.

W2. The experimental results focus only on 2-OC, which is a special case of the proposed general k-HOC, that was already studied in existing work.
An example visualisation of 4-HOC clustering is presented. As the result does not indicate a hierarchy, comparison with existing OC approaches would be in order.
Experiments should demonstrate the benefits of HOC over standard OC for k > 2.

W3. The runtime results in the experiments are not sufficiently described. This is a major concern as the evaluation only compares against a single competitor, by including results from the competitor paper, without re-running. This means that it is unclear whether differences in runtime may be due to implementation details or evaluation framework choices. In particular, the description of the implementation of Orecchia et al. 2022 seems to suggest that it is not optimised for efficiency, meaning that the observed runtime benefits may not necessarily be due to differences in method.  

W4. The benefits of the hierarchical aspect of the proposed method are unclear. In the experimental evaluation, the hierarchy is disregarded for calculating NMI, and the visualisation does not present hierarchical results, The paper should provide specific examples or experiments that demonstrate the advantages of the hierarchical structure in HOC compared to flat OC. 

W5. The paper should clarify early on (ideally in title, but certainly in abstract or introduction) that the clustering targets graph data.

W6. There are some minor language issues, and the paper would benefit from a strong motivation on the use of the cluster tree results.
Some vague descriptions should be rephrased e.g. "not so many nodes for migration", "we move all movable nodes."

### Questions
Please clarify whether Orecchia et al. 2022 runtime results may be the result of their non-optimised implementation but not due to their method as such.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This work introduces and studies the hierarchical overlapping clustering (HOC) problem. In the clustering literature, many works have focussed on either (i) overlapping or (ii) hierarchical clustering; this work's aim is to reconcile both topics.

As a first contribution -- inspired by the well-known Dasgupta cost function -- this paper introduces a _cost function_ for overlapping hierarchical clustering. The proposed cost function has serveral desirable properties such as compatibility, additivity, and binary optimality.

As a second contribution, the paper further proposes approximation algorithms for the dual and primal variants of the new cost function. These approximation algorithms hold for a restricted variant of the HOC problem, namely the $k$-HOC problem and the $2$-HOC problem.

As a final contribution, the algorithm is tested on synthetic and real-world dataset. To speed up the algorithm, the paper uses local search heuristics.

### Strengths
**S1)** The paper studies a new important problem, that is worth to study. The problem formulation itself is quite intuitive (although rather difficult to grasp from the current writeup, see W1), and a natural way to combine the hierarchical and overlapping clustering problems. This work could potentially lay the groundwork for future algorithms to be developed on. Throughout the main body and appendix the paper also states and proves intuitive properties of the cost function, which is a nice contribution.
  
**S2)** The paper also introduces 2 approximation algorithms for the new objective function, one for the $2$-OC problem, and another $k$-HOC problem. These algorithms could provide a good starting point for future work on HOC.

**S3)** Finally, the theory for the cost function and the proofs for the approximation guarantees seem sound to me - and non-trivial for the most part.

### Weaknesses
**W1)** The current writeup explaining the cost function is difficult to understand. Although the proposed objective function is intuitive, it is more involved than Dasgupta's cost, and thus requires clear explanation. With the way it's currently written in the first 10 pages, I found it difficult to understand. Lines 162-171 are densely written with non-intuitative explanations. To be more specific, the sentence "(...) they are possible unrelated in meaning and clustered by different mechanism (...)" is confusing. Later, when defining the node-to-node belonging factor, on line 191 it states: "To better understand the belonging factor, it is easy to verify that the above definition is equivalent to the following plain one". The following plain definition after is not plain at all, and contains ambiguous phrasing such as "keeps the same for the other two cases".

In the remark starting on page 240, the paper introduces the notion of "width" for HOC, however it is not clear to me exactly what the width is (See Q1). The explanation here is also difficult for me to understand; "intuitively, it can be considered as a set of key clusters that are close to the leaves on the HOC graph" is an ambiguous explanation.

I think the paper would greatly benefit from having a figure in the main body. In the appendix, Figures 3 & 4 provide a much clearer picture of HOC (and the belonging factors), and also very nicely illustrate in what settings HOC makes more sense than HC. The reason I emphasise this point is because if one of the key contributions of this work is to introduce a new cost function that will be used widely, it should be easy to understand for the community


**W2)** The approximation guarantees are given on fairly restricted settings; for the primal and dual variants of $2$-OC and $k$-HOC. the $2$-OC problem studies the overlapping bipartition problem, and contains no hierarchical structure. The $k$-HOC problem does have a hierarchical component, but restricts itself to at most $k$ clusters/nodes. The approximation guarantee on the latter is only given on the dual variant of the problem (which in general is a bit easier to prove, like the dual of Dasgupta's cost function (Mosely & Wang, 2017)). It seems that the approximation guarantee follows rather directly from the approximation guarantee of the dual of $2$-OC.

**W3)** This is a minor weakness: the experiment section is slightly dis-coupled from the main body of the work

**a)** The proposed algorithms are rather slow ($O(n^4)$ factor in the running time) which prohibits the algorithm from being applied at a large scale. This requires the paper to introduce local search heuristics to make the algorithms implementable. As such, Algorithm 2 is not 'formally' compared.

**b)** $k$-HOC experiments are only performed on synthetic data, and it is not clear to me how some metrics (such as NMI) are computed for overlapping settings for both methods compared (See Q4).

**c)** No qualitatative results on real-world datasets; the real-world datasets are only used for scalability experiments. There are experiments on MNIST in the appendix, however the NMI in those experiments is calculated using non-overlapping clusters.


**Minor points & typos**
- Line 102: "Knadekar et al. Khandekar et al. (2014)" repetition, can be avoided using \citet for the citation. Same for Orecchia et al on line 108. Also for Nepusz et al and Nicosia et al on lines 178 and 179.

- I think it would be slightly better to state the hardness of the objective value right after definition 2.8, so it's immediately clear for the reader (instead of line 272 as it is now)

- A suggestion: Figure 2 does not add much understanding (for me), and I'd prefer to see either Figure 2 or 3 in the main body instead.

### Questions
**Q1.)** What is the formal definition of the "width" of a HOC graph?

**Q2.)** What is the hardness of the $k$-HOC problem and $2$-OC problems?

**Q3.)** Does the introduction of the local search heuristics break the approximation guarantees?

**Q4.)** How is the NMI computed for both methods in Figure 1? Section C.1. formally defines NMI for overlapping clusters, however, the reason I ask is that is might follow trivially that the Dasgupta variant in Figure 1 does worse on NMI if it can only assign a single label to each cluster. i.e., the Dasgupta variant returns $k$ non-overlapping clusters.

**Q5.)** Related to above: In Figure 1, does the Dasgupta variant return $k$ non-overlapping or $k$ overlapping clusters?

The rating I've given currently is a 5, however, I am open to increasing my score based on the rebuttal.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper studies hierarchical overlapping clustering (HOC), in which vertices are assigned to a hierarchical structure of overlapping clusters. In comparison with non-overlapping HC, we construct a DAG rather than an HC tree.

The paper introduces an objective function for this problem, generalising Dasgupta's cost function for HC, and gives a constant-factor approximation algorithm for the dual objective. Finally, the paper includes some experimental evaluation and compares the algorithm with non-hierarchical overlapping clustering algorithms, finding that the new algorithm has a faster running time.

### Strengths
The paper introduces a new problem which has not been previously studied: hierarchical overlapping clustering, thus the whole paper is quite original. The paper is broadly readable and clear. The given objective function extends Dasgupta's cost in a sensible way to the case with overlapping clusters. The given algorithm is quite practical, performing well on synthetic data, and with a fast running time on large real-world datasets.

### Weaknesses
1. The motivation for HOC is not very clear. It would be helpful to discuss a little more about cases and applications where HOC would be useful where OC or HC does not already suffice.
2. I found the technical description of the HOC graph and the objective function quite difficult to follow. In particular, the definition of parent / child nodes seems non-standard as the edges are oriented from the children towards the parents (or should in-degree and out-degree be swapped in definition 2.1?)
3. The main theoretical result is the approximation algorithm for the dual problem (Theorem 3.7). However, I am a little unsure about the significance of this algorithm. In particular, it is shown that an upper bound of the objective is $n w(E)$ and the proof of Theorem 3.7 shows only that the result of the algorithm has objective at least $\alpha n w(E)$, where $\alpha$ is the claimed approximation guarantee. Thus the guarantee on the output of the algorithm does not depend on the optimal objective value of the input. The result would be much stronger if the approximation was proved directly with respect to the optimal objective of the input.
4. The paper could be further improved with more discussion on the computational complexity of optimising the proposed objective function: it is known that Dasgupta's objective is NP-hard to optimise. Is the same true for the new objective?

### Questions
1. Is there hope to prove that the approximation algorithm performs better on instances with a higher objective?
2. Is the new objective function NP-hard to optimise?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper introduces the first cost function for hierarchical clustering with overlap.
The cost function is a natural extension of DasGupta for the case of overlap.
The authors provide a polynomial time algorithm that achieves as constant factor approximation (under some assumptions on the overlap) for the dual. The authors complement the theory results with some experiments.

### Strengths
I think this is a great model (combining hierarchical clustering and overlap). To make it clear, the model is the main contribution for me.

The cost function is very natural

The algorithms seem natural.

There are rigorous theory results.

### Weaknesses
The presentation can be improved. A running example for all the definitions would be extremely useful. Also, give intuitions for all the definitions. 

The definition of 2-OC needs to be better motivated and made much clearer.

Talk more about the primal and dual version.

### Questions
Are you willing to add an example (can be in the supplementary material) for all definitions?

### Soundness
3

### Presentation
2

### Contribution
4
