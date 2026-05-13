# A Precise Characterization of SGD Stability Using Loss Surface Geometry

- Decision: Accept
- Scores: 6, 3, 8, 6

## Abstract
Stochastic Gradient Descent (SGD) stands as a cornerstone optimization algorithm with proven real-world empirical successes but relatively limited theoretical understanding. Recent research has illuminated a key factor contributing to its practical efficacy: the implicit regularization it instigates. Several studies have investigated  the \emph{linear stability} property of SGD in the vicinity of a stationary point as a predictive proxy for sharpness and generalization error in overparameterized neural networks \citep{wu2022alignment, jastrzebski2019break, cohen2021gradient}. In this paper, we delve deeper into the relationship between linear stability and sharpness. More specifically, we meticulously delineate the necessary and sufficient conditions for linear stability, contingent on hyperparameters of SGD and the sharpness at the optimum. Towards this end, we introduce a novel \emph{coherence measure} of the loss Hessian that encapsulates pertinent geometric properties of the loss function that are relevant to the linear stability of SGD. It enables us to provide a simplified sufficient condition for identifying linear instability at an optimum. Notably, compared to previous works, our analysis relies on significantly milder assumptions and is applicable for a broader class of loss functions than known before, encompassing not only mean-squared error but also cross-entropy loss.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper analyzes the linear stability of SGD through the lens of the loss surface geometry. Assuming a scenario where the model perfectly fits the data, the necessary and sufficient conditions for linear stability is characterized by learning rates, batch sizes, sharpness (the maximum eigenvalue of the Hessian), and a coherence measure of the individual loss Hessians, which is newly proposed in this work. The theoretical findings are validated through experiments on a synthetic optimization problem.

### Strengths
- The paper relaxes certain assumptions in characterizing the stability of SGD, e.g., the restriction to MSE loss, from existing works.
- The mathematical derivations appear to be sound and accurate.

### Weaknesses
- The paper lacks intuitive and qualitative explanations of the characterized linear stability, which could enhance its accessibility. Specifically, the connection between incoherent Hessians and the divergence of SGD is not clearly established. For example, it would be helpful to understand if the overshooting behavior described in the second setting of Section 3.1 directly contributes to this divergence and, if so, how.

- The experiments are limited to engineered quadratic losses without considering actual neural networks or real-world data. This raises concerns about the practical applicability of the theoretical findings. While the authors focus on additively decomposable loss functions, demonstrating the theory's validity on more complex scenarios, such as those involving neural networks trained on real datasets, would significantly strengthen the paper's impact.

- The paper should address scenarios where the condition $\nabla_w l_i (w) = 0$ is violated. There may be various cases that $\| \nabla_w l_i \|$ is small but non-zero, e.g., cross-entropy loss without label smoothing, early stopping, and so on. How can the proposed analysis accommodate these cases? The current analysis seems to heavily rely on this assumption, and its relaxation would broaden the applicability of the results.

- There are existing works to characterize the stability of SGD considering the noise covariance matrix $\Sigma = \frac{1}{n}\sum_i \nabla l_i(w) \nabla l_i(w)^T - \nabla L(w) \nabla L(w)^T$, without assuming $\nabla_w l_i (w) = 0$. The paper should clarify how its results relate to these existing works. Specifically, how does the proposed coherence measure compare to the information captured by the noise covariance matrix? A more thorough discussion of the relationship between these approaches would provide a clearer understanding of the paper's contributions in the context of prior research.

### Questions
- What is the exact notion of stability considered in the paper? It is not clearly explained in the manuscript.
- Is the coherence measure easily computable for typical neural networks? How complex would it be to compute in practice?
- On page 4, the term $x_i$ is used but not defined. 
- It seems that the second last paragraph on page 4 assumes that $H_i$ is a matrix of rank one. Is this the case?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this paper, the authors considered quadratic approximations of the loss function around the zero-loss manifold that allows the definition of the 'linearized SGD dynamics' (given in Equation 1). This quadratic approximation allows the definition of the coherence measure (Definition 1), which is used in the statement of Theorem 1: SGD dynamics diverge when the coherence measure lower bounds the first eigenvalue of the Hessian of the loss function. In Theorem 2, they provide a partial converse to their proven divergence results in Theorem 1. The paper concludes with some experiments.

### Strengths
- an important problem on the stability of SGD
- having experiments

### Weaknesses
The introduction section (i.e., the first two pages) is poorly written. For example, the definition of 'linearized dynamics of SGD' is missing and is just referred to in Section 2. But this is probably one of the most necessary things one needs to know to follow the paper. Moreover, the section 'contributions' is also vague. Instead of long sentences, it's better to use a concise way to deliver the message. It's fairly impossible to identify the contributions of the paper based on that section (before reading the whole paper).


Section 2: the approximation is called 'linearized dynamics,' but I think this is not the right word since you are essentially approximating the loss function with a quadratic function. Moreover, this dynamics only happens if you project to the zero-loss manifold at each step; otherwise, there is a term relating to the gradient. As a result, the setting is quite limited to only quadratic loss functions. 


The word 'stability of dynamics' is used frequently in the paper while not being explained in the early pages.


- the font used in the paper looks weird; I think the authors have changed something in the latex code

- In Theorem 1, $\hat{J}_i$ is used, while it is never defined (the reference to Definition 1 only defines $\hat{J}$).

- After Theorem 1, why the expectation and the arg max are equal? Also, how does divergence allow you to conclude that for almost all initial parameters, SGD convergences? These claims are not clear and are vague.

### Questions
- the font used in the paper looks weird; I think the authors have changed something in the latex code

- In Theorem 1, $\hat{J}_i$ is used, while it is never defined (the reference to Definition 1 only defines $\hat{J}$).

- After Theorem 1, why the expectation and the arg max are equal? Also, how does divergence allow you to conclude that for almost all initial parameters, SGD convergences? These claims are not clear and are vague.





------------------------------------------------------------------------------------------------------------


After the rebuttal: I appreciate the authors for their response. They partially answered some of my concerns but this paper is still not well-written, in my opinion. The authors only referred me to another reviewer for this part of my comments which I think is not an approrpiate response.

### Soundness
2 fair

### Presentation
1 poor

### Contribution
1 poor

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper analyzes the linear stability of SGD of any additively decomposable loss function around the minimum $w^*$. The paper then derives a necessary and sufficient condition for the (in)stability, which relies on a novel *coherence measure* $\sigma$, which is, in turn, intuitively connected to the alignment property of the collection of Hessians (of individual loss function). This is verified experimentally.

### Strengths
1. Very well-written. I especially liked how the theoretical discussions are backed with intuitions and specific examples. I very much enjoyed reading this work.
2. Although the mathematics used here are rather elementary, the theoretical discussions are complete; a necessary-sufficient condition for stability is provided, and the motivation and intuition behind the coherence measure $\sigma$ are well-explained. (Elementaryness is a plus for me)
3. Clear contribution and a good advancement in the linear stability analysis of SGD

### Weaknesses
1. The analysis relies on the Bernoulli sampling model, which, although is in expectation the same as with replacement sampling or uniformly sampling from all $B$-sets, still is a bit different as the size of $\mathcal{S}$ itself now becomes random. Have the authors tried to consider multinomial distribution as the sampling distribution? Specifically, how does the variance in the effective batch size, arising from the Bernoulli model, affect the stability condition, particularly when $B$ is small? It would be beneficial to see a theoretical comparison between the stability conditions derived under Bernoulli sampling versus multinomial sampling, perhaps through a bound on the difference between the two conditions. Furthermore, the authors could investigate if there is a relationship between the magnitude of this difference and the alignment of the Hessians.

2. Moreover, without replacement sampling where the event $i \in \mathcal{S}$ is dependent on $j \in \mathcal{S}$ (depending on the order), there should be some theoretical discussions on the effect of using these two (most-widely-used) random sampling schemes. While the experiments provide empirical evidence, a theoretical analysis is needed. For instance, how does the dependency between sample selections in the without-replacement scheme impact the derived stability condition? Can we quantify the deviation of the stability boundary in this scenario compared to the Bernoulli model? It would be valuable to understand if this deviation can be expressed as a function of $n$, $B$, and the coherence measure $\sigma$.

### Questions
1. The analyses presented here are solely on the stability of the iterates, i.e., whether they diverge or not. Is there any chance that this gives some insight into whether they converge? Even further, depending on the alignment of the Hessians, can we say something about the local convergence rate?
2. The relationship between batch size and learning rate that I'm more familiar with (e.g., starting from Goyal et al. (2017)) is the linear scaling rule, but here it is shown to be squared, which has also been reported in the past (e.g., Krizhevsky (2014)). Can the authors elaborate on why this stability analysis leads to squared? Then, at least locally, is squared scaling law the way to go, given that the Taylor expansion is accurate?
3. In Figure 1, for small batch sizes, there is a large gap between Theorem 2 and the red boundary for $\eta = 0.8$. Any particular reason for this?
4. How would this be extended to momentum gradient descent or any of the adaptive gradient methods (e.g., Adam)? If the time allows, can the authors provide experiments for these as well in the same setting?
5. In the prior works on linear stability, were there any quantities that resemble $\sigma$ in their role? If there were, can the authors compare those to the proposed $\sigma$?

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
4 excellent

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This manuscript investigates the linear stability of SGD and obtain a sufficient condition for instability (equivalently, a necessary condition for stability).
The authors introduce a coherence measure $\sigma$ to measure the strength of  alignment among Hessian matrices. Using this measure, they derive their main result Theorem 1, which, as they claim, is more general than Theorem 3.3 in [Wu et al, 2022]. The authors also show that Theorem 1 is nearly optimal given that $\sigma$ and $n/B$ are $O(1)$ quantities. Some experiments are carried out to support the theoretical results.

### Strengths
On a whole I think these results are neat, novel and have their own advantages.  The characterization seems to be rather precise and Lemma 4.1 is of particular interest.

### Weaknesses
 - The writing of this manuscript needs to be improved. In particular, the many details are present in an unclear way and I find it very hard to follow them smoothly. The citations and references also need to be re-organized. See Question section for more details. 

- The definition of ``Coherence measure'' is not intuitive.  Personally, I do not understand why the proposed definition can quantify the coherence among Hessian matrices. In particular, the authors claim that $\lambda_1(H_i)$ is the i-th diagonal entry of $S$. This is obviously not true unless that $H_i$ is rank-1. The authors should clarify this assumption and provide a more detailed justification for why rank-1 Hessians are a reasonable simplification, especially in the context of overparameterized models.

- The authors might make a better interpretation of Theorem 1. What does this result imply about the implicit regularization of SGD (beyond that of GD)? How stability is related to the hyperparameters, e.g. $\eta$, $B$, and alignment of $H_i$? Some relevant discussion can be found in the experiment part Section 5.2, but I think it would be better to provide some intuition right after Theorem 1. The current discussion lacks a clear explanation of how the derived stability condition relates to practical training scenarios and hyperparameter tuning.

 - In Section 3.2.1 the authors compare Theorem 1 to Theorem 3.3 in [Wu et al, 2022], and stated the advantages of their result. Among these stated advantages,
   - The first point makes sense to me.
   - In the second point, why do you say ``This definition is notably weaker than our notion of stability''? The authors need to provide a more rigorous justification for why the stability definition in [Wu et al, 2022] is weaker, possibly by giving a concrete example where their definition holds but the prior one does not.
   - By the third point, you seem to imply that the bound in Theorem 1 is sharper in the low-rank case. But what is the point in considering $\sigma$ equal to one? To me, the third point is an unclear comparison between two results, which cannot prove the advantage of Theorem 1. The authors should clarify what specific scenarios make their bound tighter, and why the case of $\sigma=1$ is particularly relevant.


- Theorem 2, the optimality of Theorem 1, strongly relies on the condition that $\sigma, n/B = O(1)$. There are two concerns:
   - In Theorem 2 the authors assume that $\sigma \in [n]$. Is there anything to guarantee $\sigma \leq n$? I don't think it is clear from the definition of $\sigma$. Is $\sigma$ inherently bounded? Moreover, do you mean $\sigma\leq n$? Hence, it is unclear what the assumption $\sigma=O(1)$ means. The authors should provide a proof or a clear argument for why $\sigma$ is bounded by $n$ or clarify that this is an assumption. The current explanation is not sufficient.
   - Also, I do not think it is natural to assume $n/B=O(1)$ as usually $B\ll n$. This assumption limits the practical relevance of the optimality result, and the authors should discuss the implications of this assumption more clearly.

### Questions
- In paragraph 1, when introducing the concept of "implicit bias", instead of citing (Li et al., 2022), I think it is more appropriate to cite the seminar works  (Neyshabur et al., arXiv:1412.6614) and (Zhang et al., ICLR 2017). 
 - In paragraph 2, when citing empirical works on relating sharpness to generalization, I think the important comprehensive investigations by (Jiang et al., ICLR2020) is missed.  
 - In paragraph 4, when stating "GD ... empirically validated to predict the sharpness of overparameterized neural network", the author cites (Cohen et al., 2021). However, this empirical predictability of linear stability analysis has been observed in (Wu et al., NeurIPS2018).
 - In Section 2
 	- In paragraph 1, when stating the rationale for assuming over-parameterization, the authors cite the work (Allen-Zhu et al., 2019). This seems quite strange to me. 
 	- In Definition 1,  it is unclear whether the sampling is done with or without replacement.
- In Section 3
	- What is the $\frac{1}{B}\sum_{i=1}^n x_i H_i$ in the second paragraph. 
	- In Theorem 1, what does the subscript in $\hat{J}_i$ stand for? Complexity measure => coherence measure. 
	- In Theorem 2, what do you mean $\sigma\in [n]$? Is $\sigma$ a real value?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good
