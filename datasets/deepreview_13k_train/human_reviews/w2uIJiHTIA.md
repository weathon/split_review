# Multilayer Correlation Clustering

- Decision: Reject
- Scores: 5, 5, 3, 6

## Abstract
Correlation Clustering, introduced by Bansal et al. (FOCS~'02), is an elegant optimization model 
that formulates clustering of objects based on their similarity information. 
In the model, we are given a set $V$ of $n$ elements, 
where each pair of elements labeled either `$+$' (representing that they are similar) or `$-$' (representing that they are dissimilar) 
together with a nonnegative weight quantifying the degree of similarity/dissimilarity. 
The goal is to find a clustering of $V$ that minimizes the so-called disagreements, 
i.e., the sum of weights of misclassified pairs in terms of the given similarity information. 

In this paper, we establish Multilayer Correlation Clustering, a novel generalization of Correlation Clustering to the multilayer setting. 
In this model, we are given a series of inputs of Correlation Clustering (called layers) over the common set $V$. 
The goal is then to find a clustering of $V$ that minimizes the $\ell_p$-norm ($p\geq 1$) of the disagreements vector, 
which is defined as the vector (with dimension equal to the number of layers), 
each element of which represents the disagreements of the clustering on the corresponding layer. 
For this generalization, we first design an $O(L\log n)$-approximation algorithm, where $L$ is the number of layers, 
based on the well-known region growing technique. 
We then study an important special case of our problem, namely the problem with the probability constraint, 
where each pair of elements in $V$ has both labels `$+$' and `$-$' but the sum of weights of both labels equals $1$. 
For this case, we first give an $(\alpha+2)$-approximation algorithm, where $\alpha$ is any possible approximation ratio 
for the single-layer counterpart. 
For instance, we can take $\alpha=2.5$ in general (Ailon et al., JACM~'08) and $\alpha=1.73+\epsilon$ for the unweighted case (Cohen-Addad et al., FOCS~'23). 
Furthermore, we design a $4$-approximation algorithm, which improves the above approximation ratio of $\alpha+2=4.5$ for the general probability-constraint case. 
Computational experiments using real-world datasets demonstrate the effectiveness of our proposed algorithms.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper extends the literature on the fundamental problem of Correlation Clustering. The plot twist here is that there are many correlation clustering instances that we have to solve on the same set of n vertices. The paper proceeds by formalizing the problem using the notion of multilayer-disagreements vector and then the authors give approximation algorithms for this. The goal is to find a common clustering
of V that is consistent with as much as possible all layers. The main algorithm attains an Llogn-approximation where L is the number of layers. Moreover, they study the problem with probability constraints, where on each layer,  there are ‘+’ and ‘−’ edge labels, with nonnegative weights in [0, 1] whose sum is equal to 1, hence the name probability constraints.

Notice that the multilayer-disagreements vector the authors introduce has dimension equal to the number of layers L and every element of represents the disagreements of the clustering on the corresponding layer. The objective used is ell-p norm minimization on the said vector. For the case of probability constraints  the authors give an (\alpha+2)-approximation  where we can use as a black box existing algorithms to get \alpha approximation for the standard correlation clustering problem. In some cases, they slightly improve upon this generic (\alpha+2)-approximation result.

### Strengths
+cute problem for correlation clustering where multiple instances are present. This is a nice twist in a famous problem and I am curious if this has been studied for more traditional clustering problems like k-means or other graph partitioning problems.

+overall, the statements are clean for approximation and interesting.

+well-motivated problem.

### Weaknesses
-one major concern I have is that there is limited novelty. Introducing a new problem is always interesting however in terms of techniques the paper heavily relies on prior works. The L layers in the input are handled in a relatively straighforward way and the analysis is a bit incremental, given the large bode of works for correlation clustering. I like the paper, but this is an important concern that I have.

### Questions
-The main premise, could it be applied to more problems? Are there related works that are directly related? This is a nice twist in a famous problem and I am curious if this has been studied for more traditional clustering problems like k-means or other graph partitioning problems.

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
In classical correlation clustering, we have a complete graph, where every edge is either labeled + or -. And there are non-negative weights on edges. The goal is to cluster the nodes into parts, so that the total disagreement is minimized. That is, total weight of + edges going between parts, and total weight of - edges going inside parts. 
General problem  admit O(log n) approximation using region growing approach, and special case when weights are all 1, admits O(1) approximation ratio, which has been improved over many prior work.

This paper studies a new generalization. Imagine we have L such graphs with weights and labels, and wish to find a "single" clustering which works well for all L graphs. How to aggregate the scores? let (D_1, D_2, .., D_L) denote the L scores for a given clustering. Then we can consdier the l_p norm of this vector to be the quantitiy we are trying to optimize.

Paper also studies one more "probability" version, where each edge has two weights w+ and w-, which add up to 1. 

For the general problem, they show O(L log n) approximation factor.
For the probability version (where the weights add up to 1 for each layer), they show two results: one alpha+2 approximation and one 4-approximation, where alpha is the single-layer approximation factor.

### Strengths
Well written paper
Results are interesting from a theoretical perspective
Paper could spark nice follow-up work as it leaves many interesting challenges open
It is rare to find a theory paper run experiments of the kind this paper does, so much credit to the authors :)

### Weaknesses
Not sure how suitable the paper is for ICLR audience, as it is more of a SODA/ALENEX type paper in my humble opinion. 
(Not taking anything away from the technical merits!)

In Section 5.1, Authors could do much more justice in explaining how they use Problem 2 to solve the general problem. In particular, what metric they use, what are x1, .., x_L and what is F? Are these the different solutions we get from the convex program? and metric space is the space of all solutions? Adding this details would make it more readable and interesting.  Also stress that Problem 3 is challenging only because the metric space could be huge.

6.1 Are there no real-world datasets without any semi-synthetic aspect to sampling the weights? Especially sampling negative weights from the positive weights.

Why is pick the best not run for the larger datasets?

Are there any other baselines one can think of? Perhaps some combination of adding the weights and pick a best? Perhaps using some approximation for l_p norm and then inferring a sampling strategy based on that? Like Multiplicative Weights method to weight the different layer instances?

Line 135: "2.5 approximation, respectively" -- means what? this is unclear. 
Line 138: Just to understand better, if the - weights satisfy triangle inequality, are the - label weights themselves positive values, or are the negative values?  This becomes clearer later, but was unclear at this point. 

Line 231: "Note however that for Problem 1 of the unweighted case" -- what does this mean?

### Questions
Line 135: "2.5 approximation, respectively" -- means what? this is unclear. 
Line 138: Just to understand better, if the - weights satisfy triangle inequality, are the - label weights themselves positive values, or are the negative values?  This becomes clearer later, but was unclear at this point. 

Line 231: "Note however that for Problem 1 of the unweighted case" -- what does this mean?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The authors propose a generalization of correlation clustering problem, termed as multilayer correlation clustering. In addition, polynomial time $O(L \log(n) )$-accurate approximation algorithms are proposed to solve the generalized problem. The main idea is to relax the original problem to a convex problem.

### Strengths
The main contribution is to propose a polynomial time algorithm to output a solution of $O(L \log(n))$ accuracy for the generalized correlation clustering problem.

### Weaknesses
1, The proposed multilayer correlation clustering problem lacks motivations. The aggregation of information from multiple weight functions $w_{l}^{+}$, $w_{l}^{-}, l=1,2, \dots, L$ can be done through more convenient and efficient ways. For instance, one can aggregate information by aggregating the weight functions by considering $w^{+} = \max_l w_{l}^{+}$,  $w^{-} = \max_l w_{l}^{-}$ or  $w^{+} = \sum_l w_{l}^{+}$, $w^{-} = \sum_l w_{l}^{-}$ or $w^{+} = (\sum_l (w_{l}^{+})^p)^{1/p}$, $w^{-} = (\sum_l (w_{l}^{-})^p)^{1/p}$. The benefits of solving the multilayer correlation clustering problem are not be well-established in the paper.

2, In section 6.1, since the case $p=\infty$ is considered, it's fairer to compare with aggregated functions $w^{+} = \max_l w_{l}^{+}$,  $w^{-} = \max_l w_{l}^{-}$. The current evaluation of the proposed algorithm uses the same objective function as the algorithm itself, which is not a fair comparison.

3, Two baseline optimization methods for solving problem 1 are compared in the simulations. However, a method for comparing information gain and clustering accuracy for problem 1 is currently lacking. The evaluation focuses solely on the objective function value, which does not provide a complete picture of the clustering quality. Specifically, it is unclear how well the resulting clusters align with the underlying structure of the data, or if the proposed method provides any additional insights compared to simpler aggregation techniques.

### Questions
What additional information can be gained from multilayer correlation clustering compared to simply utilizing aggregated weight functions?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper studies multilayer correlation clustering, which is a generalization of correlation clustering. Each layer represents a distinct correlation clustering instance on the same set of vertices. The goal is to find a consistent clustering for all layers while minimizing the p-norm of the multilayer-disagreements vector. 

The main result is an $O(L\log n)$-approximation algorithm for multilayer correlation clustering and improved algorithms for the special case of the problem with a probability constraint. The authors provide theoretical proofs and experimental evaluations to demonstrate the effectiveness of the algorithms.

### Strengths
- The definition of "multilayer correlation clustering" looks natural, and the motivation is clear.

- Under the new model, the proposed algorithm achieves a good approximation ratio. In the case of probability constraints, the algorithm can achieve a constant approximation ratio.

- The paper is easy to read. The explanation of the convex programming problem and the algorithm is clear.

- The experimental results are good, obtaining near-optimal solutions in various real-world datasets.

### Weaknesses
 - Lack of theoretical justification for the effectiveness of the results: There is no comparative analysis of the algorithm with related work (e.g., MCCC, Bonchi et al. (2015)), nor is there a lower bound provided.

- The approach requires to solve CV or LP which are heavy for larger datasets. (In the experiments, only $p = \infty$ was tested; I suspect that if other values of $p$ are used, the running time will be longer due to the need to solve CV.)



### Questions
- Only arXiv version is cited for several papers — are they published in a conference? Please check.

- The baselines (Pick-a-Best and Aggregate) are relatively trivial algorithms, but in the experiments, their results seem to also approach the optimal solution of the LP. Does this suggest that there may be some issues with the experimental setup?

### Soundness
3

### Presentation
3

### Contribution
3
