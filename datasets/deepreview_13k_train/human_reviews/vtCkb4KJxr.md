# Adaptive Threshold Sampling for Fast Noisy Submodular Maximization

- Decision: Reject
- Scores: 6, 5, 5, 6

## Abstract
We address the problem of submodular maximization where objective function $f:2^U\to\mathbb{R}_{\geq 0}$ can only be accessed through i.i.d noisy queries. This problem arises in many applications including influence maximization, diverse recommendation systems, and large-scale facility location optimization. We propose an efficient adaptive sampling strategy, called Confident Sample (CS), that is inspired by algorithms for best-arm-identification in multi-armed bandit, which significantly improves sample efficiency. We integrate CS into existing approximation algorithms for submodular maximization, resulting in algorithms with approximation guarantees arbitrarily close to the standard value oracle setting that are highly sample-efficient. We propose and analyze sample-efficient algorithms for monotone submodular maximization with cardinality and matroid constraints, as well as unconstrained non-monotone submodular maximization. Our theoretical analysis is complemented by empirical evaluation on real instances, demonstrating the superior sample efficiency of our proposed algorithm relative to alternative approaches.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The topic of this paper is the problem of submodular maximization:
given a ground set $U$ and a an oracle access to a
submodular objective function $f: U \to \mathbb{R}$,
our task is to find $S\subseteq U$ with the highest value of $f(S)$.     
They study also the classical constrained versions where
we maximize $f(S)$ subject to cardinality and matroid constraints.

The authors study submodular maximization in the setting,
where
exact evaluation of $f(S)$ is not possible 
and one can obtain only noisy estimate. In particular, they assume
the oracle returns a noisy estimate which is unbiased and 
is $R$-subgaussian. 
This setting was already studied before, e.g. by Singla et al. '15, who
achieved almost the same approximation guarantees as in the classical
non-noisy setting and provided bounds on the number of the performed
noisy queries.      
Authors provide theoretical bounds which they compare to previous
works and they also present an empirical comparison.

The main difference between their work and Singla et al. '15
is that their algorithm is based on a faster implementation
of the classical greedy algorithm by Badanidiyuru and Vondrak which, instead
of comparing the marginal gain of the elements to each other, it compares
their marginal gain to a threshold chosen during algorithm's runtime.
Therefore, instead of a quadratic dependence on the gap $\Delta_{max}$
between the two top marginal gains, they have a quadratic dependence on the
gap from the threshold (their parameter $\phi$).

### Strengths
The problem is important and their setting seems relevant and well motivated.
They achieve improvements in sample complexity over previous works at least in
some settings. They have a better running time as well.

### Weaknesses
The results are somewhat difficult to appreciate for me,
despite that they provide more than a page long comparison with the
previous works in Appendix discussing the differences in the long formulas.
For example, it is not clear to me why is it better to have dependence
on $\phi$ instead of $\Delta_{max}$.
Is $\phi$ always smaller than $\Delta_{max}$?

I am not an expert in the field. While I see that the authors do achieve
an improvement over the previous works, I do not see its significance.
Therefore my rating.

### Questions
* Can you comment on the weakness above?

* Can you say that your algorithm has a better sample complexity
than the previous works always?

* Knowing something about the properties of the input instance, how can
you estimate the value of $\phi$ without running your algorithm?
I am asking this to understand whether your bounds can be used to predict your algorithm's performance. Note that, for example, $\Delta_{max}$ can be
estimated in advance based on the properties of the input instance.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The paper studies the constrained submodular maximization under noise problem that arises in many applications in AI and ML Communities. The key algorithm of this work is Confident Sample (CS), which is inspired by algorithms for best-arm-identification in multi-armed bandit. The CS algorithm can then be integrated into many existing approximation algorithms for submodular maximization under constraints. The authors show that the integrated algorithms take fewer samples on both theoretical and practical sides.

### Strengths
- This work studies an interesting and meaningful research problem in the AI ​​and ML community. The paper is well-written and structured. 
- The core algorithm, Confident Sample (CS), has been shown to be effective in estimating the expectation of the objective submodular function in Gause distributions. The theoretical analysis is natural and reliable. However, the techniques for proving them are pretty elementary.

### Weaknesses
 - Except for CS, the remaining algorithms are not new. The author's main contribution is how to apply CS algorithm to existing algorithms and the corresponding theoretical analysis.
- The idea of the CS algorithm is not new. It existed in previous algorithms (For example, in Alg 2 in [Mat]). 
- It is natural to apply CS algorithms to existing algorithms, but it is not difficult to derive theoretical bounds.

### Questions
1. What are the differences (ideas, theoretical analysis) between CS and Alg 2 in [Mat]?
2. What are the challenges in getting better theoretical bounds when applying CS algorithms to existing algorithms?
3. Does the CS algorithm work well with other distributions?
4. Can the CS algorithm be applied to the Minimum Cost Submodular Cover (MCSC) problem? The paper's contribution would be better if it is possible to apply CS to MCSC with better theoretical bounds.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper studies submodular maximization in a noisy model. Formally, the goal is the same as in the standard monotone submodular maximization with cardinality or matroid constraints, but the algorithm has access to the function via a noisy oracle. In particular, given a set $S$ and element $x$, the algorithm can query $(S,x)$ to the oracle and receives a random (unbiased) estimator of the marginal value of $x$ with respect to $S$. The authors assume that such estimator is subgaussian (of parameter $R$ that is known).

The paper's contribution is to provide tight approximation results for cardinality and matroid constraints by adapting known techniques with a sample efficient estimation procedure called Confident Sample (CS).

### Strengths
Submolar maximization is a relevant topic for the NeurIPS/ICML/ICLR audience, given its vast applicability in ML. The model of noisy queries is natural and well-motivated. The sample complexity bounds are not trivial (as the authors explain, using Hoeffding would already yield some results).

### Weaknesses
 - The technical contribution is moderate. In the end, the paper's contribution lies in rewriting concentration bounds, parameterized by a notion of gap. Threshold-based algorithms are well-known in the submodular literature. The core idea of using a threshold to decide whether to include an element is not novel, and the paper's contribution seems to be primarily in the analysis of the sample complexity within this framework. The authors adapt existing techniques, but the novelty of the adaptation is not very high. The use of a subgaussian estimator is a standard assumption, and the main technical work seems to be in deriving the specific sample complexity bounds with the gap parameter.
- The sample complexity bounds are pretty involved. Many parameters are entailed, and a clear picture is difficult to get. The bounds involve several terms, including the subgaussian parameter R, the approximation factor epsilon, the failure probability delta, and the gap parameter phi. It is not immediately clear how these parameters interact and how the overall sample complexity scales with each of them. The dependence on the gap parameter, while intuitive, makes the bounds less practical since the gap is usually unknown in advance. The presentation of these bounds could be improved to provide more intuition and guidance on how to apply them in practice.

### Questions
Do you have any tightness results on the sample complexity?

### Soundness
3

### Presentation
2

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
The paper introduces the Confident Sample (CS) algorithm to maximize submodular functions under noisy conditions efficiently. By leveraging insights from multi-armed bandit algorithms, CS reduces the number of noisy queries required to approximate submodular functions, making it applicable to diverse optimization tasks such as influence maximization and recommendation systems. Theoretical analysis and empirical results demonstrate the effectiveness of CS in achieving competitive approximation guarantees with significantly improved sample efficiency compared to traditional methods.

### Strengths
The paper proposes the Confident Sample (CS) algorithm, which effectively reduces the number of noisy queries by dynamically adjusting the sample size according to the level of uncertainty. This adaptive approach contrasts with traditional fixed-precision methods, offering substantial improvements in sample efficiency. The work's theoretical contributions are robust, providing guarantees on both approximation quality and sample complexity, making it a competitive alternative to existing methods like ExpGreedy. These theoretical insights are further supported by empirical evaluations on real-world datasets, where the proposed algorithms demonstrate superior sample efficiency, highlighting the practical relevance of the approach.

### Weaknesses
I do not have significant negative comments regarding the contributions of this paper. My only concern is whether the topic aligns well with ICLR's scope, as I have not come across purely theoretical work on submodular maximization algorithms published at ICLR before. While submodular maximization is indeed a crucial problem in machine learning, ICLR, to my knowledge, tends to focus more on areas related to deep learning and neural networks. Therefore, would it be more appropriate to consider submitting this paper to venues like NeurIPS or ICML, which might better align with its focus?

### Questions
Please refer to weaknesses.

### Soundness
2

### Presentation
2

### Contribution
2
