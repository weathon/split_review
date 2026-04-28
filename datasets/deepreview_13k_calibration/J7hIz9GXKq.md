# Collaborative Compressors in Distributed Mean Estimation with Limited Communication Budge

- Decision: Reject
- Avg Score: 5.25
- Scores: 5, 5, 5, 6

## Abstract
Distributed high dimensional mean estimation is a common aggregation routine used often in distributed optimization methods (e.g. federated learning). Most of these applications call for a communication-constrained setting where vectors, whose mean is to be estimated, have to be compressed before sharing. One could independently encode and decode these to achieve compression, but that overlooks the fact that these vectors are often similar with each other.  To exploit these similarities, recently Suresh et al., 2022, Jhunjhunwala et al., 2021, Jiang et al, 2023, proposed multiple {\em correlation-aware compression schemes.} However, in most cases, the correlations have to be known for these schemes to work. Moreover, a theoretical analysis of graceful degradation of these correlation-aware compression schemes with increasing {\em dissimilarity} is limited to only the $\ell_2$-error in  the literature. 
    In this paper, we propose four different collaborative compression schemes  that agnostically exploit the similarities among vectors in a distributed setting.  Our schemes are all simple to implement and computationally efficient, while resulting in big savings in communication. We do a rigorous theoretical analysis of our proposed schemes to show how the $\ell_2$, $\ell_\infty$ and cosine estimation error varies with the degree of similarity among vectors. In the process, we come up with appropriate dissimilarity-measures for these applications as well.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes a sequence of collaborative compressors for distributed mean estimation problem, exploiting the observation that the local vectors can share similarities with each other. The authors design one compression scheme for each similarity metric among $\ell_\infty$ norm, $\ell_2$ norm, and cosine similarity. Their respective upper bounds on estimation error is also provided, decaying with the number of clients $m$ and relying on the difference between local vectors. Experiments on distributed mean estimation, KMeans, power iteration, and linear regression are conducted.

### Strengths
* It is an interesting problem to exploit the similarities between local vectors for compression.
* The paper considers multiple similarity metrics and provides rigorous analysis on the estimation error bound for each of the compression scheme.
* The presentation of this paper is mostly clear to me.

### Weaknesses
 * The error bounds developed in this paper have an extra term $\Delta$ that does not decay with $m$. On the contrary, previous works as summarized in Table 2 of this paper can avoid this problem. This theoretical gap is confusing to me and I look forward to authors' explanations. Specifically, the presence of a non-decaying $\Delta$ term in the error bound raises concerns about the practical scalability of the proposed method in scenarios with a large number of clients. The analysis does not sufficiently address how the magnitude of $\Delta$ impacts the overall performance, particularly when the number of clients ($m$) increases.  It is unclear under what conditions the proposed method would be preferred over existing methods that offer error bounds decaying with $m$. 
* The experiments on gradient aggregation are performed only for linear regression tasks. I would suggest working on logistic regression or neural networks to better demonstrate the performance of the proposed schemes in modern machine learning settings. The current experimental setup does not adequately demonstrate the applicability of the proposed compression schemes to more complex and realistic machine learning tasks. The absence of experiments on non-convex optimization problems, such as those found in neural network training, limits the generalizability of the findings.


### Questions
* There is a typo at your openreview submission title.

* "However, independent compressors suffer from a significant drawback, especially when the vectors to be aggregated are similar/not-too-far, which is often the case for gradient aggregation in distributed learning." I'm not sure if this is the case, because data heterogeneity (which leads to heterogeneous local gradients) seems to be a major challenge discussed in literature. I hope the authors can further clarify on this.

* In Figure 2(a): The blue curve (RandK) is missing.

* In Figure 2(i): What does the y-axis stand for? Why do the curves not converge and not descend too much (from 1.14e4 to 1.06e4)? Will you need more iterations for this experiment?

* In caption of Table 1: I suggest the authors do not cite Wikipedia articles in academic writing.

* In Line 265: Is it $j\in[m]$ or $j\in[d]$?

* In Line 921: There is one more $+$ sign in the equation.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes several different collaborative compression schemes. For each schemes this paper proposes corresponding collaborative compression algorithms and theoretically analyse the estimation error on different metrics. This paper conducts experiments on standard dataset to test the algorithms.

### Strengths
This paper studies a relatively new direction on distributed optimzation and compression techniques: collaborative compression. The author proposes three different schemes, using different norm to measure the estimate error and provides theoretical analysis.

### Weaknesses
1. The literature research is not enough. The author provides comparison of existing independent compression and collaborative compression methods in Table 2. But in the list the independent compression techniques are not the latest achievements. At least, considering error feedback techniques, the accumulated error of independent compression techniques can be bounded and the convergence rate is faster than those proposed in Table 2. Specifically, the comparison should include recent advancements in error feedback mechanisms and their convergence properties, which are not adequately addressed in the current literature review.
2. The theoretical analysis is too simple. Considering collaborative compression methods are not first proposed by author, the theoretical analysis should be more deep-going. In fact the author only computes the estimate error of the compression algorithms under different  norm. It is lack of novelty.  The analysis should delve deeper into the theoretical underpinnings of the proposed collaborative compression schemes, exploring aspects such as the tightness of the error bounds, the conditions under which the proposed methods are optimal, and the limitations of the analysis. A more rigorous and comprehensive theoretical treatment is needed to establish the significance of the contributions.
3. The experiment results are also not enough. I think at least conducting experiments on basic neural networks and standard dataset is necessary, for example, tiny transformers on OpenWebtext. In other words, it is necessary to test the algorithm in practical tasks rather than only in the DME. In practical distributed training, the global gradient is the mean estimate of local ones. Can such algorithms work? I think copying the experimental setting in [1] is not enough. The experiments should include a broader range of practical tasks and datasets, particularly those involving neural networks and large-scale datasets. The evaluation should also consider the performance of the algorithms in the context of distributed training, where the global gradient is estimated from local gradients.

### Questions
1. I think at least the basic application of such estimator is necessary to study. For example, the convergence rates (or gradient complexities) of algorithms applied to smooth optimization are necessary in a theory work. Only bounding the estimate error can not illustrate the effectiveness of compression algorithms when applying to specific tasks. Moreover, the communication complexity is also necessary.
2. This work follows [1] but has few novelty. I think this paper needs more deep-going study. The existing content is not sufficient to support publication.

[1]  Shuli Jiang,Pranay Sharma,and Gauri Joshi.Correlation aware sparsified mean estimation using random projection.

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper considers the distributed mean search problem. This may be applicable, for example, when gradients are averaged in distributed learning. The authors present new collaborative compressors for this problem. The authors provide a comprehensive theoretical analysis for the "variance" estimation and small experimental comparison with some competitors.

### Strengths
1) Overall the paper is easy to read.

2) The ideas look new and are a quite good contribution. 

3) The authors do a pretty good job of giving intuition and explaining the details of the new operators, as well as the theoretical results (physics of the various $\Delta$ and so on)

4) The literature review is not badly done, comparison with other papers is partly inherent, although it seems incomplete - see 1st weakness.

5) I went through the proofs quickly, the results seem correct, and relatively expected.

### Weaknesses
1) Estimates in terms of $\Delta_2$ are more interesting than in terms of $B$ as given by the authors. Let me explain. From the point of view of distributed optimization it is important how the method that uses compressed communications converges. 

For example, in the paper (Szlendak et al., 2021)  the estimate on PermK is written in terms of $Delta_2$, the MARINA optimization algorithm has good convergence estimates. If we write these estimates in terms of $B$, is it possible to get such good estimates? The paper under review does not answer this question. I will ask an even more general question: how does a distributed gradient descent (or a more advanced method) with compression operators presented in the paper converge? The current analysis only provides an additive error term, which does not guarantee convergence to the optimal solution, especially in the smooth case, which is a significant limitation.

2) The experiments are weak.
а) They look quite simple and seem even simpler than in the original paper (Suresh, 2016).

b) Different competitors are used in different experiments. This looks strange and suspicious. 

с) Tuning algorithms are not described (maybe I didn't look carefully). 

d) Obviously, gradient descent is not the most advanced algorithm. The same PermK paper uses MARINA, which is a more advanced algorithm designed for distributed setting with compression.


3) The paper is written in a rush. I'm not the most diligent typos finder, but 

a) style of citation - without brackets looks weird

b) "$\ell_2$-error" or $\ell_2 error$?

c) line 333: a dot at the beginning

d) line 523: space 2i

e) Plots design: 1) sometimes there is a dot in the legend (e-i), sometimes there is not (a-d), 2) lines do not start from one point (f,e), 3) axis on (g) is cut off, 4) where is green on (e,h)? 5) legend of (a-c) is smaller than of others

f) may be make sense to put Algorithm 1 into Appendix 

g) OpenReview title: Budge

### Questions
1) How do the operators proposed in the paper relate to the uncertainty principle from (Safaryan et al., 2021)? Does the answer to this question depend on the similarity of $g_i$? It seems that it does. How? If all $g_i$ are the same? 

2) How do the gradient similarities introduced in the paper relate to the similarities used for example in the paper?

It uses hessian similarities: 
Hendrikx, Hadrien, et al. "Statistically preconditioned accelerated gradient method for distributed optimization." International conference on machine learning. PMLR, 2020.

Why I ask, the similarity of the gradients often varies from point to point and may in general be not bounded at all (e.g. solve on $R^d$ two quadratic problems with different matrices = linear regressions with a quadratic loss function on two different datasets). Hessian similarity is better.

### Soundness
3

### Presentation
1

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
The paper addresses the problem of high-dimensional mean estimation. It introduces several collaborative compression schemes designed to exploit similarities among vectors in distributed settings. These schemes come with error guarantees across various metrics, including $\ell_2$-error, $\ell_{\infty}$-error, and cosine distance, with error rates improving as the number of clients increases and degrading with greater dissimilarity among clients. In low dissimilarity scenarios, the proposed methods can outperform several baseline approaches.

### Strengths
- The work addresses a relevant problem in distributed machine learning. It provides error guarantees for different error metrics, which adds robustness to its evaluation.

- The proposed methods can benefit from client similarity, offering a potential advantage for applications with close-to-homogeneous data distributions. This is reflected both in theory and in experiments.

### Weaknesses
 - The proposed schemes are designed to work in the setting where the data is close to homogeneous, and perform worse when clients have high dissimilarity. In such settings, the introduced methods do not perform as well as baseline approaches. This significantly limits their usefulness in many real-world application, e.g., federated learning, where client data is often highly heterogeneous.

 - It is unclear in Section 3 what parts are original contributions by the authors versus prior work. The abstract mentions three new schemes, while the conclusion refers to four, which makes the contributions hard to identify. Could the authors clarify this point?
- Is "Technique I" from Section 3 actually introduced in the paper?

### Questions
- It is unclear in Section 3 what parts are original contributions by the authors versus prior work. The abstract mentions three new schemes, while the conclusion refers to four, which makes the contributions hard to identify. Could the authors clarify this point?
- Is "Technique I" from Section 3 actually introduced in the paper?

### Soundness
3

### Presentation
3

### Contribution
3
