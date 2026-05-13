# Relative-Translation Invariant Wasserstein Distance

- Decision: Reject
- Scores: 3, 5, 5, 3, 3

## Abstract
We introduce a new family of distances, relative-translation invariant Wasserstein distances ($RW_p$), for measuring the similarity of two probability distributions under distribution shift. Generalizing it from the classical optimal transport model, we show that $RW_p$ distances are also real distance metrics defined on the quotient set $\mathcal{P}_p(\mathbb{R}^n)/\sim$ and invariant to distribution translations. When $p=2$, the $RW_2$ distance enjoys more exciting properties, including decomposability of the optimal transport model, translation-invariance of the $RW_2$ distance, and a Pythagorean relationship between $RW_2$ and the classical quadratic Wasserstein distance ($W_2$). Based on these properties, we show that a distribution shift, measured by $W_2$ distance, can be explained in the bias-variance perspective. In addition, we propose a variant of the Sinkhorn algorithm, named $RW_2$ Sinkhorn algorithm, for efficiently calculating $RW_2$ distance, coupling solutions, as well as $W_2$ distance. We also provide the analysis of numerical stability and time complexity for the proposed algorithm. Finally, we validate the $RW_2$ distance metric and the algorithm performance with three experiments. We conduct one numerical validation for the $RW_2$ Sinkhorn algorithm and show two real-world applications demonstrating the effectiveness of using $RW_2$ under distribution shift: digits recognition and similar thunderstorm detection. The experimental results report that our proposed algorithm significantly improves the computational efficiency of Sinkhorn in certain practical applications, and the $RW_2$ distance is robust to distribution translations compared with baselines.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
Many machine learning pipelines rely on training objective losses involving comparing probabilities measures. One of the mostly used in these pipelines are optimal transport (OT), aka Wasserstein distance,  that leverages the geometrical information of the distributions in question. In a nutshell, Wasserstein distance seeks for the cheaper cost to transport a source distribution to a target one, where the optimization problem behind consists in a linear programming problem. 

This paper addresses a major limitation of classical Wasserstein distance that corresponds to a translation shift in the source distribution. It introduces a family of relative-translation invariant Wasserstein $RW_p$ that behave like to Wasserstein distance and invariant to translation. For $p=2$, $RW_2$ enjoys a decomposition of the relative translation optimal transport (ROT). In addition, $RW_2$ can be solved using Sinkhorn iterations. The papers ends up with empirical results on weather detection dataset.

### Strengths
- The authors propose relative translation optimal transport (ROT) which induces a Wasserstein like distance on the quotient space of probability measures induced by the translation relation. 
- For quadratic ROT, a decomposition in terms of Wasserstein distance (horizontal function) summed with a quadratic term including the shifting parameter $s$. 
- The authors test ROT approach on weather detection dataset.
- I checked the proofs of the main results and they sound correct.

### Weaknesses
 - In Definition 4, the relative transplantation invariant Wasserstein, $RW_p(\mu, \nu)$ is given with respect to an $s$-shifting of the source distribution $\mu$. However in Theorem 2, $RW_p$ is proper distance on the quotient set of shifting probabilities. Since the main results of the paper are based with respect to a shifting of the source, I’am wondering about the properties of $RW_p$ outside the quotient set. Specifically, it would be beneficial to understand how $RW_p$ behaves when applied to distributions that are not related by a simple translation. Does it retain desirable properties such as non-negativity and the triangle inequality? A more thorough investigation into the behavior of $RW_p$ for general probability measures would strengthen the theoretical foundation of this work.

- The quadratic $RW_2$ is very closed to the translation property of Wasserstein distance with a quadratic cost (see Remark 2.19 in [1]). Namely, if one considers only the case of shifting the source distribution, the decomposition of Quadratic ROT can be straightforwardly derived from this remark and a simple optimization minimisation over the shifting parameter $s$. Specifically, given the decomposition $W_2^2(T_s\mu, \nu) = W_2^2(\mu, \nu) + ||s||^2 - 2\langle s, \bar{\nu} - \bar{\mu} \rangle$, minimizing over $s$ directly yields the optimal shift $s^* = \bar{\nu} - \bar{\mu}$. Substituting this back into the decomposition provides a closed-form expression for $RW_2^2(\mu, \nu)$. This connection to existing results should be acknowledged and discussed more explicitly. I think this point weakens the novelty of this paper.

- I think that the computational efficiency of Sinkhorn $RW_2$ over classical Sinkhorn is not significant since the maximum over the shift cost matrix needs a lower bound of the L2 norm $\||\bar{\mu} - \bar{\mu}\||$ with an order of $\sqrt{n}$. Specifically, the computation of the maximum involves finding the largest element in a matrix of size $n \times n$, which inherently requires at least $O(n)$ operations. While the proposed Sinkhorn variant may offer some improvements, the dependence on the dimensionality $n$ through the L2 norm suggests that the computational gains might be limited, especially for high-dimensional data.

### Questions
**Minor Typos**
- M179: « coupling «  —> « Coupling »
- L325: « Thoorem »

### Soundness
2

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
3

### Summary
This paper presents a new Wasserstein-based distance function, called the relative-translation invariant Wasserstein distance $RW_p$, which given two distributions $\mu$ and $\nu$, finds the optimal pair of shift and transport map $(s, P)$ that minimizes the transport cost of $P$ between $\mu$ and the translated distribution $\nu$ by a vector $s$. It is shown that this distance is a metric and can be computed by computing the gradients and alternatively updating the shift $s$ and the transport map $P$. 

When $p=2$, the paper shows that the object function of $RW_2$ can be expressed as minimizing the sum of two functions, where one is independent of the shift and the other is independent of the transport map. In this case, the authors use the Sinkhorn algorithm to speed up the computation of $RW_2$. Furthermore, the authors show that the diameter of the point sets after applying the optimal shift would reduce for empirical distributions derived from sub-Gaussian distributions, hence improving the execution time of the Sinkhorn algorithm.

### Strengths
- The paper presents the properties of finding the Wasserstein distance when we are allowed to shift the distributions.
- The paper also presents algorithms for approximating the $RW_p$.

### Weaknesses
### weaknesses:
 - I think the proof of triangle inequality has some mistakes. My main concern is where you set $W_p(\eta, \eta')$ to 0 from line 2 to line 3. If $[W_p]$ refers to the Wasserstein distance between the classes of $\mu$ and $\nu$, then essentially $RW_p=[W_p]$ and from line 1 to line 2 of the Equation, you are assuming the triangle inequality holds for your distance. If $[W_p]$ just means the Wasserstein distance, then $W_p(\eta, \eta')$ might not be 0. To elaborate, the jump from line 2 to line 3 seems to assume that if $\eta$ and $\eta'$ are optimal translations, their Wasserstein distance is zero. This may not hold true without further justification. It's crucial to clarify whether $[W_p]$ represents the Wasserstein distance between optimally translated distributions or just any Wasserstein distance. (It seems reasonable that $RW_p$ is a metric, so my concern mostly is that the proof is not written correctly and not that the theorem is incorrect.)
- It is good that the method is implementable and can be used to test the performance of the new distance function, but current experimental results do not convey the message. For the numerical validation part, see my questions below. For the thunderstorm pattern detection, although visually $RW_2$ performs better than $W_2$ in Figure 4, I would say it is hard to judge the results in Figure 9 and Figure 8. I would strongly suggest adding experiments with a ground truth to your next version; something like an image retrieval task on labeled images, where you randomly shift a dataset of labeled images and show an improvement in the accuracy of the retrieved images for each query image when using $RW_2$ instead of $W_2$. A quantitative comparison using a standard metric like precision or recall would significantly strengthen the empirical validation.

### Questions
- Corollary 1 seems to be extendable to all values of p and not only p=2. The proof of it might not be straightforward, but I am curious to know if you already have some counter-examples showing that if $P$ is an optimal map for the untranslated distributions, then after translating the distributions, the same $P$ would not have an optimal cost. 
- For the experiments on numerical validation, can you explain why the Sinkhorn algorithm running time is not changing for the values of $s\in[0,2.4]$ and then suddenly drops to around 0 times (Figure 3 (c))? Based on your discussion in Section 4.4, when the shift increases, the diameter should also increase and we should expect to see higher running times.  
- In the same experiment, why is there a sharp increase in the error of the Sinkhorn algorithm for $s>2.4$ (Figure 3 (d))? Am I right that for $s>2.4$, the Sinkhorn algorithm did not compute anything and just returned 0 as the output cost? 
- Figure 3 (b): what is the computation error? Why do the two methods have the same set of errors for all values of s?  
- Also, based on the experiments in the appendix on numerical validation, there are sharp increases and decreases in the results, which is unintuitive. What is the number of runs you performed for each value of $s$ that resulted in those plots?

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
The paper introduces a shifting invariant Wasserstein-based metric called relative-translation invariant Wasserstein distances $RW_p$ to measure the similarity between shifted distributions. We can see this distance generalized the original Wasserstein by being invariant to distribution translations. For $p = 2 $, the $RW_2$ distance shows promising properties such as the decomposability of the optimal transport model and translation invariance of coupling solutions. The authors propose two algorithms for computing general $RW_p$ and a variant of the Sinkhorn algorithm for $RW_2$ computation. Also, the theoretical analysis of numerical stability and time complexity is provided. In the end, they conducted two experiments in comparison with Sinkhorn to validate the new metric performance, which includes a computational time comparison and an image retrieval task with a weather dataset.

### Strengths
- Novelty, paper presents a novel shifting-invariant Wasserstein-based metric, which extends the original Wasserstein distance to be invariant under shifting translations
- Clarity and Mathematical Soundness, this paper is generally well-written with clear explanations. The authors provide solid mathematical proofs for the metric properties and the relation to Wasserstein distance.
- Algorithm Development, this paper proposed two algorithm implementations for the $RW_p$ distances, the $RW_2$ Sinkhorn preforms better than the original Sinkhorn according to the experiment results

### Weaknesses
 - This paper does not provide an analysis of the convergence rates of the $RW_p$ distances as a distribution measure. 

- This paper lacks theoretical and experimental comparisons with Gromov-Wasserstein (GW) distance that has similar invariance properties. The GW distance is also translation-invariant and compares distributions based on the shapes, which makes it a good benchmark for comparison in the experiment section [1]. A recent work [2] proposed a robust p-Wasserstein distance (RPW), that claims robustness under shifting perturbations, especially when $p = 2$. A similar image retrieval task was conducted in this work. In general, I feel like the paper lacks comparisons with related works, such as GW distance and RPW both in theory and practice. 

With these two major drawbacks, I tend to reject this paper for major revisions.

### Questions
- How does the proposed $RW_p$ distance compare with the GW distance in theory and experiment, which is also translation-invariant and focuses on shape similarity? Which types of distributions translation where the $RW_p$ distances may not perform well compared to other invariant metrics? Again, including such comparisons supports the paper with the broader range of translation invariant Wasserstein-based distances.

- Could you provide theoretical analysis or empirical observations on the convergence rates of $RW_p$? 

- Can the $RW_p$ be extended to handle other types of distribution shifts, such as scaling or rotation? 

- For the pattern detection experiment, is the thunderstorm snapshot data labeled? If it is, could you provide the accuracy of retrieved similar patterns to better quantify the performance of $RW_p$?

- Is the code public for the experiment section?

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper focuses on finding a distance metric between distributions that is invariant to translation while also possessing the desirable properties of the Wasserstein distance. The authors propose a new metric and provide both theoretical and numerical proofs demonstrating that it satisfies the properties of a metric and is invariant to translation. Their analysis is conducted specifically for discrete distributions. Additionally, the paper introduces an algorithm for measuring a special case referred to as RW_2.

### Strengths
The paper is well written, and the mathematical proofs are rigorous.

### Weaknesses
The literature review section needs improvement; it fails to explain why this problem is important and does not address previous efforts made to solve it. Additionally, the work is not clearly positioned within the existing literature. The paper does not adequately justify the need for a new metric when a straightforward approach of subtracting the means and then calculating the Wasserstein distance appears to be a viable alternative, particularly when considering the application of weather pattern analysis which relies on the L2 norm. The authors should provide a more compelling argument for the necessity of their proposed method over this simpler baseline in the context of the L2 norm.

### Questions
The first approach that comes to mind for solving this problem is to subtract the mean of both distributions, thereby transforming them into zero-mean distributions. We could then calculate the Wasserstein distance between these two zero-mean distributions. However, I am concerned about why the method proposed by the authors is superior to this straightforward option. If the authors can address this question, I may reconsider my score.

### Soundness
3

### Presentation
3

### Contribution
1

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposed a relative-translation invariant Wasserstein distance $RW_p$. Two algorithms were proposed to compute the RW distance: a two-stage algorithm for the general $p$ case, and a variant Sinkhorn algorithm to compute $RW_2$.

### Strengths
Classical Wasserstein distance $W_p$ cannot identify similar "shape" patterns in data when their exact locations are irrelevant. Motivated by detecting weather patterns from geographical images and robustness in distributional shift, the paper proposed a new distance metric on the space of probability distributions, called the relative-translation invariant Wasserstein ($RW_p$) distance.

The decomposition of the relative translation optimal transport (ROT) problem into a vertical move along orbit in the quotient space and a horizontal move is interesting. For $p=2$, this decomposition turns out to be an orthogonal "bias-variance" structure of the $W_2$ distance. This effectively generalizes the Bures-Wasserstein distance for Gaussians to translation invariant distributions.

The proposed Algorithm 1 for general $RW_p$ is a coordinate-type algorithm for solving ROT: the vertical component is solved via gradient descent and the horizontal is solved by Sinkhorn or linear programming. When $p=2$, proposed Algorithm 2 is essentially an orbit debiased Sinkhorn algorithm, to avoid numeric instability. Some numerical experiments are performed to demonstrate better numeric stability.

### Weaknesses
In Section 4.4, the paper claims that "Consequently, our $RW_2$ method achieves better time complexity compared to $W_2$" in Remark 1 (page 8). I am not convinced why it is so. Theorem 5 only proves that with high probability the largest value of centered pairwise distances between source and target distributions (i.e., worst cost value) gets improved. It is widely unclear why this result alone implies better time or iteration complexity for solving $RW_p$ than $W_p$. In particular, if $p \neq 2$, solving $W_p$ requires only a pass of solving Sinkhorn, while $RW_p$ (with unknown means of source and target) has to solve many Sinkhorn subproblems. In such case, an iteration complexity should be given to justify better time complexity compared to $W_p$. If $p=2$, the proposed Algorithm 2 is almost identical to the Sinkhorn algorithm with an additional step to pre-compute the mean vectors to avoid numeric instability. I don't see much computational advantage in practice for using $RW_p$.

In practice, we need to choose $p$. Different $p$'s seem to give very different results (e.g., Section 5.2). What is the practical and/or theoretical guidance of choosing $p$? Moreover, for $p \neq 2$, how to determine the step size parameter $\eta_1$ in the horizontal gradient descent? Is it constant step size or is it annealed? Any theoretical justification should be helpful to guide the choice of $\eta_1$.

The simulation example in Section 5.1 is too simple. For Gaussians, it is not necessary to compute Wasserstein distances (vanilla and proposed) based on Sinkhorn. One should have closed form for both distances. More extensive settings (such as much higher-dimensional non-Gaussian distributions for general $p \geq 1$) should be used to demonstrate numerical benefit of debiasing the centers.

### Questions
Some minor comments:

In Algorithm 1, where was $\eta_2$ used?

In Theorem 4, $\bar{\mu}$ and $\bar{\nu}$ are not defined. They are only defined later.

### Soundness
2

### Presentation
3

### Contribution
2
