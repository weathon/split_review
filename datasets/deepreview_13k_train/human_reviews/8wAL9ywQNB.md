# Generalizability of Neural Networks Minimizing Empirical Risk Based on Expressive Power

- Decision: Accept
- Scores: 3, 8, 8, 6, 5

## Abstract
The primary objective of learning methods is generalization. Classic generalization bounds, based on VC-dimension or Rademacher complexity, are uniformly applicable to all networks in the hypothesis space. On the other hand, algorithm-dependent generalization bounds, like stability bounds, address more practical scenarios and provide generalization conditions for neural networks trained using SGD. However, these bounds often rely on strict assumptions, such as the NTK hypothesis or convexity of the empirical loss, which are typically not met by neural networks. In order to establish generalizability under less stringent assumptions, this paper investigates generalizability of neural networks that minimize the empirical risk. A lower bound for population accuracy is established based on the expressiveness of these networks, which indicates that with adequately large training sample and network sizes, these networks can generalize effectively. Additionally, we provide a lower bound necessary for generalization, demonstrating that, for certain data distributions, the quantity of data required to ensure generalization exceeds the network size needed to represent that distribution. Finally, we provide theoretical insights into several phenomena in deep learning, including robust overfitting, importance of over-parameterization networks, and effects of loss functions.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper studies generalization error of 2 layer neural networks that minimize empirical risk in a binary classification problem. The authors present a lower bound for accuracy based on the expressiveness of these networks, indicating that, with a sufficiently large training sample and network size, these networks can generalize. They offer an extension of the result to approximate empirical risk minimizers. They consider several other implications (relationship between the size of the neural network needed to represent the target distribution, and the quantity of data required to ensure generalization, robustness, etc.).

### Strengths
One strength is that the work is studying an important problem: explaining deep learning generalization.

Another strength is that they are using unconventional hypotheses, namely relying on the size of a network that exactly matches the data. This hypothesis was considered by Buzaglo et al in recent work (ICML 2024).

### Weaknesses
There are many weaknesses.

Perhaps the biggest issue is that there's no new insight here. We have old school uniform convergence analyses, coming together with universal approximation arguments, but what have we learned? Negative results are for "some distribution" and don't explain practice. And there's no evidence the accuracy lower bounds (use error not accuracy) are strong enough to explain practice.

The hypothesis that some network exactly labels the data with a margin c is too strong in practice. This hypothesis rules out situations where there is label noise. It even rules out situations where there is no noise, but the decision boundary cannot be exactly represented by a neural network. (Approximation theorems don't help here.) The assumption of a fixed margin 'c' also seems particularly restrictive, as it implies a uniform separation across the entire input space, which is unlikely in real-world scenarios.

The results are uniform convergence results and so it's not clear how they get around the roadblock identified by Nagarajan and Kolter (2022)'s work on uniform convergence not explaining deep learning.

### Questions
How do the results relate to Buzaglo et al (ICML 2024)?

How do the results relate to Nagarajan and Kolter (NeurIPS best paper: arXiv:1902.04742)? How do you sidestep the issues they raise?

What would empirical validation of these theories look like?



## FOLLOW UP QUESTIONS - PLEASE RESPOND IF YOU CAN ##

I have a question that would help me move to quickly resolve my concerns. The questions/remarks below ("Other questions / comments.") are less important and you should simply aim to address these in your own revisions. They are likely small typos or minor points that would confuse readers.

Key questions:

1. 
In the proof of Lemma B.5, in (3) you write "The L1,Inf norm of the three transition matrices...". It would seem that there is assumption hidden here about the L1,Inf norms of the networks in H_W(n). I don't see any assumptions about the L1,Inf norms in definition of H_W(n) at the top of page 4. Can you maybe offer a bit more detail on the arguments arriving at these three norm bounds?



Other questions / comments.

1. It seems that the (W0,c) delivered by Proposition 4.2 are rather important in practice. These terms appear in the final bound as (W0 + c)/ cN and so, in particular, the tradeoff between W0 and c is essential. It may be the case that the minimum W0 is W0** but for that width W0**, the corresponding c** might be 2^{-100}, and maybe each increase in W0 only brings you a small improvement in c. Of course, these are just constant, but they would make the bounds impractical (and thus not explain practice).

2. Defn 3.1. There is no standard notion of inf over a pair of random variables. You should make a probability one statement over the two samples: y_1 != y_2 ==> ||x_1 - x_2||_2 > 0. In particular, this implies no noise and a zero Bayes error rate. These are strong assumptions that should be highlighted with a remark. There is no role for the L2 norm here. The assumption is simply that H(y|x) = 0. for (x,y) ~ D, IINM.

3. Proposition 3.2 is written in an odd way. M_W \subset H_W and so you are simply arguing that M_W is non-empty, using uniform continuity (compactness + continuity).

4. Proof of Proposition 4.2. There is a claim that I do not believe is true, starting "Then, because D has a positive separation distance, [there exists a continuous function that f(x)=y with probability one under D]" You would likely need a uniform gap ||x_1 - x_2||_2 >= gap  for some constant gap > 0. Regardless, it seems the only use of this assumption is to guarantee this continuous function f, and so just make that your assumption in the first place, which is then the weakest assumption that makes your argument go through, and is also the clearest explanation of your assumption.

5. Theorem A.1. Missing quantification over x. 

6. Lemma B.4. b_i is a vector and so it doesn't have an L1,Inf norm. Do you mean L1. Wen et al. talk about the L1,inf of the combined bias and weights, so I believe you want L1?  And what is the justification for the claim that the L1,Inf norms at layer i are bounded by c_i? Or is this mean to be a definition? (If so, remove "Then" and write "We also assume...". 

Wen et al. (Statistica Sinica 31 (2021), 1397-1414 doi:10.5705/ss.202018.0468) On CIFAR, c >= 15 in their experiments to 


Notation:

7. Using W for the width and W_i for weight matrices is rather nonstandard. You elsewhere use w_i for whole matrices. Would be nice to have the notation consistent throughout the work.

### Soundness
3

### Presentation
1

### Contribution
1

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper addresses the generalization of neural networks from the perspective of their expressive power. The authors provide new generalization bounds based on a network’s expressive capacity and without strong assumptions. The paper also provide a lower bound of generalizability. Additionally, the paper explores implications for over-parameterized networks, robustness, and the impact of different loss functions on generalizability.

### Strengths
This paper provide a novel generalization bound based on expressive power of the network, which is different to traditional bounds. The assumption that there exists a network separates the distribution is more natural in practice than convexity or NTK. With rigorous analysis to both sample comlexity and lower bound of generalizability, the paper shows integrity of this research topic. Moreover, this work also provide some insights to the phenomena in deep learning such as overparameterization, robustness and the effect of different loss functions. Additionally, the paper is well organized and easy to understand.

### Weaknesses
This is a good paper in general. But I have some concerns about the contribution. The main results of the paper is showing the generalizability of shallow ReLU networks on a positive separated distribution that can be expressed by a smaller network. This maybe not a siginificant contribution since it seems really natural. Intuitively, if the data distribution can be separated by a network, there must exist functions in the class of larger networks that can also separate the data distribution. With large enough sample size, the ERM solution certainly can generalize with high probability. And techinically, there are Rademacher complexity type bounds with sample complexity $O(1/\sqrt{N})$ [1]. The only difficult of the main theorem is to estimate the Rademacher complexity of the class of larger ReLU networks. 
So I doubt a little bit about the contribution of this paper.

### Questions
See weakness part.

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
4

### Summary
The authors provide a number of useful generalization results for neural networks. They base their analysis on a definition of expressivity of *distributions* rather than functions (the classic universal approximation theory framework), and focus specifically on the case of distributions that satisfy a strict separability assumption, that implies that the Bayes risk is 0. The expressivity definition gives a natural, architecture-dependent measure of distribution complexity, W0. The authors focus do an algorithm-dependent analysis, focusing of empirical risk minimizers.

The main result is a lower bound on test accuracy of ERM, which depends on the ratio between W0 and the network’s width, W, and the number of training examples, N. Roughly, it implies that having a network width greater than W0 and a number of training examples which exceeds W0*[dimension] is sufficient for generalization.

They provide further analysis to follow-up on the main result, including upper bounds on generalization when the dataset is not big enough, generalization results for when ERM yields a local optimal point, and the explanation for various interesting phenomena (robustness, overparametrization, etc). The authors also provide discussion of implications of their results, and comparison to other existing results in literature.

### Strengths
The explicit dependence of the bounds on both training set size, but also the width of the network is not common in statistical learning theory bounds and is very important to explain various width-related generalization phenomena. 

There is thorough analytical follow-up of the main result, including upper bounds on generalization when the dataset is not big enough, generalization results for when ERM yields a local optimal point, and the explanation for various interesting phenomena (robustness, overparametrization, etc). The authors also provide good discussion of implications of their results, and comparison to other existing results in literature.

The literature review, and comparison to relevant literature is complete.

### Weaknesses
1. Many grammatical errors and typos. Most of them are inconsequential for comprehension, but some actually make check the validity difficult:  Line 723: “Miximum” is that a maximum or a minimum?

2. While the authors state their positive separation assumption in Definition 3.1, it would improve clarity if they repeated in the statements of subsequent theorems that they only apply to distributions that satisfy the separation. Same for Lin 304-305. The results are discussed as if they hold for any distribution, which is not true. Specifically, the theorems should explicitly state that the results hold under the assumption of Definition 3.1, and this should be reiterated in the discussion of the results.

3. There are some minor issues with rigour: 
- Line 721: “for all (x,y)~D” is an odd statement. It is not clear whether the authors mean “surely” or “almost surely” with respect to distribution D. This needs to be clarified, and the correct terminology should be used.
- The infimum in Definition 3.1 is not well defined. Is (z,-1)~D meant to signify any z in the support of D conditional on the label being -1? This needs to be clarified. The definition should specify whether the infimum is taken over all z in the support of D conditioned on y=-1, or if it is a different condition.

4. [minor] The pervasive use of passive voice can be confusing. The authors use passive voice interchangeably for their own contributions, and for existing results (by other authors) in literature.

### Questions
Please look at weaknesses section for some comments that might require a response.

### Soundness
4

### Presentation
3

### Contribution
4

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper investigates the generalizability of neural networks trained by empirical-risk-minimization (ERM) algorithms, focusing on understanding the factors that contribute to their ability to generalize well to unseen data. The authors consider two-layer networks and approach generalizability from the perspective of the network's expressive ability, which refers to the network's capacity to represent complex functions and effectively fit the underlying data distribution. The paper establishes a lower bound for the accuracy of neural networks that minimize empirical risk, suggesting that these networks can generalize effectively given sufficiently large training datasets and network sizes. The paper further investigates the lower bound by examining scenarios without enough data. The paper finally provides insights into several observed phenomena in deep learning, including robust overfitting, the importance of over-parameterization, and the impact of loss functions.

### Strengths
1. The paper explores generalization from a unique perspective by connecting it to the expressive ability of neural networks, providing a fresh perspective on understanding why neural networks generalize well.
2. The paper do not place strong assumptions on data or loss functions, making the results more applicable to practical scenarios.
3. The paper highlights the importance of choosing appropriate network models and activation functions tailored to the specific data distribution to enhance generalization capabilities.

### Weaknesses
1. The focus on two-layer networks might limit the applicability of the findings to more complex and deeper network architectures prevalent in practice. Specifically, the theoretical results may not directly translate to the behavior of deep networks with multiple non-linear transformations, which are known to exhibit different generalization properties. The analysis does not account for phenomena such as vanishing or exploding gradients, which are common in deep networks and can significantly impact training dynamics and generalization.
2. The paper primarily focuses on theoretical analysis and does not include empirical studies to validate its claims and insights. While theoretical results are valuable, the absence of experimental verification makes it difficult to assess the practical relevance and applicability of the proposed bounds. It remains unclear how well the theoretical bounds align with the actual performance of neural networks on real-world datasets.
3. The assumptions on separable data distributions potentially oversimplifies the complexities of real-world deep learning applications. The requirement of a positive separation bound may not hold for many practical scenarios, such as those involving noisy or overlapping data distributions. This assumption limits the generalizability of the theoretical results to more realistic settings where data points from different classes may not be clearly separable.

### Questions
1. In Theorem 1.1., please clarify the meanings of "expressing the data distribution with a neural network" and "with high probability of a dataset". 
2. Under Theorem 1.2, what are the definitions of "robust memorizing" and "robust fitting"?
3. Why is "positive separation bound" important for the data distributions? How would the results change if the data distribution does not have a positive separation bound?
4. In Section 5, the authors provide upper bound for accuracy without enough data. Could the authors relate the upper bound and the previously derived lower bound and have some discussions?
5.  Under Theorem 6.2, it would be better to elucidate more on the dependency of $c_1$ on $\epsilon$.
6. In Proposition 6.5, how do the numbers "0.9" and "0.6" come out? Similarly for Theorem 6.7.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper studies the generalization capabilities of two-layer neural networks (NNs) with small empirical error. Based on the expressive power of NNs, the authors derive a lower bound for classification accuracy, or equivalently, an upper bound for classification error, in NNs trained with minimum empirical risk. Their results show that large network width and large sample size can lead to high classification accuracy. Additionally, this conclusion extends to NNs with somewhat higher empirical risk. By their theoretical analysis, the authors provide insights on factors influencing generalization, such as the choice of activation functions, the role of overparameterization, and the impact of loss function selection

### Strengths
1. Unlike many previous results that rely on bounded loss functions, this paper analyzes the more practically relevant cross-entropy loss. Additionally, the theoretical results in this paper do not depend on any convexity or smoothness assumptions of the loss function.

2. The derived lower bound on classification accuracy suggests that wider NNs have more potential for high accuracy, which is desirable for deep learning theory.

### Weaknesses
1. Although the authors acknowledge that restricting the analysis to two-layer NNs is a limitation, there are some additional constraints in problem setups, such as focusing only on binary classification tasks and constraining the parameter space to $[-1,1]^d$ (where $d$ is the number of total parameters). It seems that these constraints are essential for the theoretical developments, and further relaxing these constraints does not seem straightforward.

2. My another concern arises from the use of Rademacher complexity to derive the lower bound on accuracy (or equivalently, the upper bound on error), which could be loose. For example, Corollary 4.4 in this paper indicates that Theorem 4.3 requires the width and sample size to be sufficiently large for the lower bound to be non-vacuous (i.e., the lower bound itself is non-negative). Thus, outside the large-sample regime, Theorem 4.3 may lack practical relevance, limiting its applicability. In fact, considering that the paper already studies generalization for empirical risk minimizers, it might be more interesting to use bounds based on local Rademacher complexity rather than the original Rademacher complexity, which could give a decay rate of $O(1/N)$ instead of $O(1/\sqrt{N})$ for hypotheses with low risk or variance.

Additional concerns are outlined in the questions below.

### Questions
1. Along with the constrained parameter space, the input data space is assumed to lie within $[0,1]^n$, is it possible to relax this requirement? I think normalizing input data to $[-1,1]^n$ is also common in practice.

2. In the proof of Proposition 3.2, it seems that the bounded domain of the parameter space play a critical role in proving the existence of an empirical risk minimizer. How would this apply to practical scenarios with an unbounded parameter space? Moreover, if the cross-entropy loss used in Proposition 3.2 has the reachable upper and lower bounds, does that imply it is also a "bad" loss function as defined in Definition 6.6?

3. In the proof of Proposition 4.2, in Line 723-725, it’s stated that $\mathcal{F}_A$ is a network whose parameter is the corresponding parameter of $\mathcal{F}$ divided by $A$, with $\mathcal{F}_A=\mathcal{F}/{A^2}$. Could you clarify why this equality holds? In addition, if $A<1$, then each parameter of $\mathcal{F}_A$ might exceed the domain $[-1,1]$, it seems that the parameter domain constraint will be violated.

4. In the proof of Theorem 4.3, could you explain how the $L_{1,\infty}$ norm for the three transition matrices in Line 786 were obtained? Additionally, if input data is not restricted to $[0,1]^n$ and the parameter space is unbounded, can these $L_{1,\infty}$ norms still be derived? Furthermore, in Line 838-839, the inequality $|S|< Ne^{-kc/2+2}$ is only meaningful if $kc\geq 4$, as $|S|\leq N$ clearly holds. This is also implied in Line 853, where the lower bound would be vacuous for $kc\leq 4$ since $\mathbb{E}_{(x,y)\sim\mathcal{D}}yg(x)\geq -\frac{kc}{2}$ already holds trivially. Perhaps adding a condition such as $W\geq \frac{4(W_0+1)}{c}$ in the theorem statement might improve clarity.

5. The motivation for the loose results in Section 5.1 is unclear, as the conclusions and insights from these $W$-independent results seem well-known.

6. In your abstract, you mention that the theoretical results in this work can provide insights into robust overfitting, but what you explore in Section 6.1 is not related to the robust overfitting phenomenon, which is proposed in [R1]. Perhaps "robust generalization", as used in the introduction, would be a more accurate term.

[R1] Leslie Rice, Eric Wong, and Zico Kolter. "Overfitting in adversarially robust deep learning." International conference on machine learning. PMLR, 2020.

Minor comments:

1. Some references are missing. For example, stability-based bounds have been extended beyond Hardt et al. (2016) to cover nonsmooth cases (e.g., [R2, R3]), among others. Additionally, PAC-Bayesian and information-theoretic generalization bounds are well-known for being algorithm-dependent and, in some cases, data-dependent. These methods generally do not assume Lipschitz continuity, convexity, or smoothness and some derive fast-rate bounds in the low empirical risk regime. Refer to [R4, R5] for further reading on these types of generalization bounds.

[R2] Raef Bassily, et al. "Stability of stochastic gradient descent on nonsmooth convex losses." Advances in Neural Information Processing Systems 33 (2020): 4381-4391.

[R3] Yunwen Lei. "Stability and generalization of stochastic optimization with nonconvex and nonsmooth problems." The Thirty Sixth Annual Conference on Learning Theory. PMLR, 2023.

[R4] Pierre Alquier. "User-friendly introduction to PAC-Bayes bounds." Foundations and Trends® in Machine Learning 17.2 (2024): 174-303.

[R5] Fredrik Hellström, et al. "Generalization bounds: Perspectives from information theory and PAC-Bayes." arxiv preprint arxiv:2309.04381 (2023).

2. The paper would benefit from substantial proofreading, as there are numerous typos (e.g., Line 092: "reached is minimum" ---> "reached its minimum"; Line 082: "robust memorizing"--->"robustly memorizing", ...) and inconsistencies in notation (e.g., $\mathcal{F}$ vs. $F$; $Z_{2W}(n)$ vs. $\mathbf{H}_{2W}(n)$, ...). Please review the manuscript carefully to identify and fix these issues.

### Soundness
2

### Presentation
2

### Contribution
2
