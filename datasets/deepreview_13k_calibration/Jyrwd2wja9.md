# Measurement Manipulation of the Matrix Sensing Problem to Improve Optimization Landscape

- Decision: Reject
- Avg Score: 3.75
- Scores: 3, 3, 6, 3

## Abstract
This work studies the matrix sensing (MS) problem through the lens of the Restricted Isometry Property (RIP). It has been shown in several recent papers that two different techniques of convex relaxations and local search methods for the MS problem both require the RIP constant to be less than 0.5 while most real-world problems have their RIPs close to 1. The existing literature guarantees a small RIP constant only for sensing operators having an i.i.d. Gaussian distribution, and it is well-known that the MS problem could have a complicated landscape when the RIP is greater than 0.5. In this work, we address this issue and improve the optimization landscape by developing two results. First, we show that any sensing operator with a model not too distant from i.i.d. Gaussian has a slightly higher RIP than i.i.d. Gaussian, and that its RIP constant can be reduced to match the RIP constant of an i.i.d. Gaussian via slightly increasing the number of measurements. Second, we show that if the sensing operator has an arbitrary distribution, it can be modified in such a way that the resulting operator will act as a perturbed Gaussian with a lower RIP constant. Our approach is a preconditioning technique that replaces each sensing matrix with a weighted sum of all sensing matrices. We numerically demonstrate that the RIP constants for different distributions can be reduced from almost 1 to less than 0.5 via the preconditioning of the sensing operator.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper considers the matrix sensing problem through Restricted Isometry Property (RIP). Since a larger RIP constant lead to performance degradation & a substantial number of practical sensing operators belong to such case, they propose to reduce the RIP constant through the pre-conditioning trick.

### Strengths
1. This paper is quite easy to follow. 
2. The analysis seems to be sound. I randomly sampled some proofs and can verify their correctness.

### Weaknesses
1. My major concern comes from the setting itself. The authors basically change the sensing operator, e.g., from $A$ to $\tilde{A}$ in Algorithm 1. If this operation is allowed, I wonder why the authors bother with the pre-conditioning trick, they can simply ignore the original operator $A$ and use a Gaussian i.i.d. sensing operator. The RIP constant can be guaranteed. It is unclear what constraints are placed on the transformation from $A$ to $\tilde{A}$, and if the transformation is unconstrained, then it would be more effective to directly use a random Gaussian matrix as the sensing operator. The paper needs to clarify the practical limitations that necessitate the specific pre-conditioning approach, as opposed to a direct replacement of the sensing operator.
2. The justification of the pre-conditioning is not convincing enough. In Section 2, they prove the RIP constant will increase in the presence of perturbation. There are several issues. First, their analysis is on the upper-bound on RIP. It's unclear how the RIP constant change. The RIP constant can remain constant while the upper bound of RIP constant can change from $c$ to $2c$. Second, the upper-bound is a little confusing for me. It seems that there a optimal sensing number $m$. Intuitively, the performance should keep improving with the increasing sampling number, as the deviation becomes smaller. The analysis in Section 2 focuses on bounding the RIP constant, but it does not clearly explain how the actual RIP constant behaves with respect to perturbations. The upper bound could be loose, and the actual RIP constant might not change as drastically. Furthermore, the existence of an optimal sensing number $m$ is counterintuitive, as one would expect performance to improve monotonically with more samples. The paper should provide more insight into the practical implications of this bound and how it relates to the true RIP constant.
3. The techniques in the analysis is quite standard.
4. A minor regarding to Figure 2 is to plot the error bar of the simulated RIP constant. Unless you exhaustively check all possible rank-$s$ matrices, there is no possibility of getting the exact RIP constant. Based on the content, it seems that you use Monte-Carlo simulation to find the RIP constant, which is fine. Still, it looks better to include the variance.

### Questions
See above

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper considers the matrix sensing problem where a low-rank matrix is sensed via inner products with a set of sensing matrices, resulting in a set of scalar measurements. The results consider the restricted isometry property (RIP) constants for perturbed matrix constructions, where the baseline are matrices with i.i.d. Gaussian entries. The paper also shows that by orthogonalizing the rows of a matrix the RIP constant improves, and by mixing multiple sensing matrices the RIP constants improve as well.

### Strengths
The numerical results verify the benefit of pre-conditioning the sensing matrices to be orthogonal to one another.

Perturbing sensing matrices to improve their performance is an interesting idea.

### Weaknesses
The analytical results show that the RIP constants increase with perturbation; it is not clear then what is the benefit of perturbation if it requires more measurements (e.g., Remark 2). The matrix perturbation proposed is not tested numerically.

The broadest results I am aware of for RIP of random matrices are based on subgaussianity of the underlying distribution of its entries. Thus focusing on Gaussian matrices in a comparison may be too narrow; and I note that some of the improvements claimed here involve subgaussian distributions already. Furthermore, sums of Gaussian and subgaussian matrices are subgaussian.

It is well known in the CS literature that orthogonalizing the rows of the sensing matrix improves its performance (these are so-called orthogonal projectors). See for example https://doi.org/10.1109/TIT.2005.862083 and https://mdav.ece.gatech.edu/publications/dwb-tr-2006.pdf - this may also relate to the Haar distributed random matrices used in Section 3.1, although they have not been defined in this paper. The preconditioning algorithm is therefore commonly applied in the CS literature, and that proposed here is a straightforward extension from measurement vectors to sensing matrices.

It is also straightforward to see that a weighted mixture of matrices will have distribution closer to Gaussian (akin to the law of large numbers). In addition, sum of subgaussian random variables are subgaussian as well (akin to Corollary 1).

It is not clear why Theorem 1 defines its constants in terms of $\epsilon$ when a bound of $\epsilon$ itself is already included in the assumptions; the best constant can be obtained by having $\epsilon$ meet its bound.

### Questions
In line 86, the RIP constant is defined as the smallest number $\delta_s$ such that the inequality holds; so it should be unique if it exists.

In line 119, a statement is made about nearly isometry, but a distribution for $\mathcal{A}$ is not established. Is it the one in the following sentence? (i.i.d. Gaussian)

In line 163, it appears that the mat(.) operator must know the size of the target matrix (as an additional input?)

In Theorem 3, is it implicitly assumed that $m > n^2$? Otherwise you would not be able to have all $A_1,\ldots,A_m$ orthogonal.

Typo: Line 52 board -> broad

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
3

### Summary
The paper discusses the robustness of the restricted isometry property constant of matrices to perturbations, and a pre-processing algorithm to improve the RIP constant of a large class of matrices, with the matrix sensing problem in mind. The main application discussed is the matrix sensing problem.

### Strengths
The RIP contant is a fundamental property with a great deal of practical importance in compressed sensing, matrix sensing, and other regression tasks.
The paper is mostly self-contained, the proofs are quite simple and easy to follow, and convincing numerics are also provided to showcase the proposed algorithm for various types of matrix ensembles. The algorithm seems very robust. The overall redactional quality is high.

### Weaknesses
 The main two weaknesses from my viewpoint are: firstly, it is not clear that ICLR is the right avenue for this paper that is very strongly signal processing oriented. Secondly, the motivation of the processing algorithm is not clear: if one can design the sensing matrices at their will, what is then the advantage of starting from given ones and try to improves them? Why not taking directly Gaussian matrices with good RIP constant? This needs to be discussed at it appears nowhere.



### Questions
+ I would ask the authors to authors to discuss the above point:  if one can design the sensing matrices at their will, what is then the advantage of starting from given ones and try to improves them? Why not taking directly Gaussian matrices with good RIP constant? Provide an example where the re-design is natural 

+ first line below def 2 is not clear. What A are we talking about that is nearly isometric? Please rephrase 

+ what is a variance « proxy » in corollary 1 or theorem 2?

+ rmk 2: where does it come from that A has RIP O(1/sqrt m)? Is this automatic from nearly isometrically distributed?

+ the text below the proof to Theorem 3 is important but a bit too condensed to be well understood. Please expand it

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The authors are concerned with the so-called RIP constant of linear operators. The authors motivate their study with results from the matrix sensing literature.
There exist a plethora of randomly constructed linear operators that operate at an optimal sample complexity (i.e., number of measurements is modulo polylog-terms in the ambient dimension equal to the degrees of freedom of the problem) and have the RIP with high probability. Almost all of these rest upon the assumption of near isometry, i.e. that $\mathbb{E}(\Vert \mathcal{A}(X)\Vert^2) = \Vert X \Vert^2$. The authors argue that this assumption in many applications is not given, and propose to extend the results in two directions.
First, they prove a pertubation result: In essence, if an operator is close to an operator with the RIP, it also has the RIP with a slightly higher RIP constant. Secondly, they propose a preconditioning scheme, based on replacing the sensing operator with its right singular vectors (or, equivalently, preconditioning it with $\mathcal{A}\mathcal{A}^T$. They prove a bound on the RIP constants of the preconditioned matrix, and showcase the efficiency of their approach with a numerical experiment.

### Strengths
The authors study a relevant problem and connect it nicely to the matrix sensing literature. The article is written in a way which is easy to follow.
As far as the scientific content goes, their result on the RIP of perturbed Gaussian matrices can be highlighted. The appeal of the result is that no assumption what soever is put on the pertubation - it may in particular be deterministic. Since the RIP constant is continously dependent on the matrix operator, it is no surprise that such a result can be proven, but I am unaware of a concrete bound like this in the literature.

### Weaknesses
 The second part of the paper, related to the improvement of the RIP constants through conditioning, unfortunately suffers from weaknesses.

#### Questionable novelty
The idea to replace a matrix with its left singular vectors is a very natural one, and it has indeed been proposed before in the literature -- in the manuscript of Chen and Lin (2021) that the authors cite. In there, it is motivated via and formulated in the context of sparse recovery, but the mathematics are more or less equivalent. This severely impacts the value of the empirical success of their method.

I am not convinced by Lemma 1 -- the right-singular vector matrix will only be Haar distributed if the distribution of the operator $\mathcal{A}$ fulfills some orthogonal invariance, which is not the case for many of the distributions they use in their numerical experiments. The authors aim to address scenarios where the measurement operator is *not* Gaussian, which is a case where orthogonal invariance does not hold, making the relevance of Lemma 1 questionable in the context of their goals.

#### Unclear interpretation of Theorems 4 and 5
From my point of view, Theorems 4 and 5 do little to explain the empirical success of the preconditioning strategy. As the authors point out, Theorem 4 only provides a better bound on the RIP constant if $\sigma_1(A)^2\leq 1+\delta_s$. Since $\delta_s \geq \max(1-\sigma_m(A)^2, \sigma_1(A)^2-1)$, this can essentially only be the case if the singular values of $A$ are biased downward. In particular, in the Gaussian setting that they consider in Theorem 5, it is not. Indeed, $1-(1-\delta)/(1+ \sqrt{n^2/m}(1+\epsilon)\geq\delta$ for all values of $\delta$ -- i.e., the 'direct bound' that is given by previous results is better. In their proof, they seem to argue that since $A$ has the $\delta$-RIP, it also has the $2\delta$-RIP, and then compare their bound to $2\delta$ instead of $\delta$. I have a hard time understanding the latter reasoning. The bound in Theorem 5, which includes a term $\sqrt{n^2/m}$, seems to necessitate the number of measurements, $m$, to grow proportionally to $n^2$, which contradicts the goals of compressed sensing to avoid such a dependence. This is a major limitation of the theoretical results.

#### Impact of noise
When performing the preconditioning in practice, it will not only transform the measurement operator, but also noise in measurements $y=\mathcal{A}(X)+\epsilon$. Since the success of their method relies on the singular values of $\mathcal{A}$ being small (see Theorem and Remark 4), this means that the noise *necessarily* is amplified. A discussion on this, and possible mitigations, such as in (Chen, Lin; 2021) would make the work more complete.

#### Small inaccuricies
While the paper generally is well written, it would benefit from another round of proofreading. There are some inconsistencies in the notation: The norm $\Vert \mathcal{A}\Vert_\infty$ is never defined, on page 9, there is a term $\mathcal{A}(M)$ that should be a $\mathcal{A}(X)$, and so forth.

### Questions
The points that I think are most crucial for the authors to clarify are my above concerns about Theorems 4 and 5 above, i.e.

- The necessity of $m$ being in the order of $n^2$.
- The fact that the new lower bound the theorems provide never seem to be smaller than the original $\delta$.

### Soundness
2

### Presentation
3

### Contribution
2
