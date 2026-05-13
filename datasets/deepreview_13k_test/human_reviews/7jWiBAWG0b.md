# Learning Guarantees for Non-convex Pairwise SGD with Heavy Tails

- Decision: Reject
- Scores: 5, 6, 5

## Abstract
In recent years, there have been a growing number of works studying the generalization properties of pairwise stochastic gradient descent (SGD) from the perspective of algorithmic stability. However, few of them devote to simultaneously studying the generalization and optimization for the non-convex setting, especially the ones with heavy-tailed gradient noise. This paper establishes the stability-based learning guarantees for non-convex, heavy-tailed pairwise SGD by investigating its generalization and optimization jointly. Firstly, we bound the generalization error of pairwise SGD in the general non-convex setting, after bridging the quantitative relationships between $\ell_1$ on-average model stability and generalization error. Secondly, a refined generalization bound is established for non-convex pairwise SGD by introducing the heavy-tailed gradient noise to remove the bounded gradient assumption. Finally, the sharper error bounds for generalization and optimization are provided under the gradient dominance condition. In addition, we extend our analysis to the corresponding pairwise minibatch SGD and derive the first stability-based near-optimal generalization and optimization bounds which are consistent with many empirical observations. These theoretical results fill the learning theory gap for non-convex pairwise SGD with heavy tails.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies generalization and excess risk bounds for pairwise learning with SGD under non-convex loss functions. The main tool for proving generalization is a notion of $\ell_1$ on-average stability, which is adapted to the pairwise setting. It is shown that the bounded gradient condition for the loss function can be relaxed when having sub-Weibull noise in SGD iterates, which captures potentially heavy-tailed noise. Further assuming a PL condition leads to an improved generalization bound along with an optimization guarantee which overall leads to an excess risk bound for pairwise learning with SGD.

### Strengths
Relaxing the Lipschitzness requirement for the loss function and covering heavy-tailed noise distributions can be a significant forward step for stability-based SGD generalization bounds. Furthermore, the improvement from $T^{1/2}$ to $T^{1/4}$ in the stability bounds is a major improvement.

### Weaknesses
* My main concern is with the readability and precision of the current submission. The main text seems to lack sufficient intuition on the techniques behind the improvements and how prior analyses are modified to achieve the refined rates. Some examples for improving readability:
    * What is the valid range of values for $c$ in Table 1? Is it allowed to simply let $c \to 0$? This is important in order to compare the $T$-dependence of the current stability bounds with the literature.
    * Have the stability bounds of this paper, i.e. $\tilde{O}(T^{1/2}/n)$ and $\tilde{O}(T^{1/4}/n)$ under an additional PL condition, been established in the pointwise setting under the same assumptions or are they completely new?
    * What is the intuition behind improving prior dependencies on $T$ to $T^{1/2}$ under smoothness and $T^{1/4}$ under PL and smoothness? Specifically, how does the PL allow a transition from $T^{1/2}$ to $T^{1/4}$?
    * What is the dependence of the bounds in Theorems and Corollaries 4.6 to 4.11 on $\mu$? Without any hidden dependencies, it seems that one can let $\mu \to 0$ to prove the same results without the PL condition. Similarly, it seems like the dependence on $\beta$ is hidden in most statements which might be useful to highlight.

* The bounds of this paper are in expectation, while many similar bounds in the literature are stated with high probability. It might be useful to add a discussion on the possibility of establishing high probability bounds, especially how such bounds would interact with the heavy-tailed noise of SGD.

### Questions
* It seems that a term $|\mathbb{E}[F_S(w(S))] - F(w^*)|$ is missing from the RHS of Equation (4).

* Why is SGD initialized at zero in Definition 3.1? Is this a fundamental limitation or is it possible to handle arbitrary initialization?

* Perhaps there could be a discussion on why Definition 3.5 is called $\ell_1$ on-average stability even though the $\ell_2$ norm is used in the definition.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper studies the generalization performance of pairwise SGD in the non-convex setting, and in the presence of heavy tailed gradient noise. The generalization error for any learning algorithm is first bounded in terms of the $\ell_1$ on-average stability under the bounded gradient assumption.  A similar relationship is derived for the SGD under the assumption of heavy tailed gradient noise (without bounded gradient assumption). Next, bounds on the  $\ell_1$ on- average stability are derived for pairwise SGD under the aforementioned assumptions, which lead to explicit bounds on the generalization error.  Furthermore, bounds on generalization error and excess risk are derived for pairwise SGD under the PL condition, and assuming heavy-tailed gradient noise. These bounds are also extended to pairwise minibatch SGD.

### Strengths
1. The paper is written well overall with a clear problem setup, notation and motivation. Moreover, the related work section is very thorough and puts into perspective the results of the paper.

2. In terms of novelty, I believe there are no existing stability based guarantees for pairwise SGD with heavy tailed gradient noise in the nonconvex setting. Moreover, the relationship between generalization error and $\ell_1$ on average stability (Theorem 4.1) seems new to my knowledge.

### Weaknesses
1. Currently, no proof outline (or sketch) is provided in the main text. This makes it difficult to understand the extent of the novelty in the ideas underlying the proof. From my understanding, the proof steps seem to build heavily upon existing ideas from the literature on nonconvex pairwise SGD based learning (Lei et al, 2021b).


2. The results are stated in expectation throughout, which is weaker than the "high probability" results that exist in the literature for similar learning problems that use stability based analysis.

### Questions
1. In Assumption 3.8, is the expectation over all sources of randomness, including $w_t$?

2. In Theorem 4.1 (b), it is not clear to me whether this applies to any learning algorithm A, or is specific to SGD? This is because of the gradient noise assumption made therein which suggests that it is for SGD.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors study the algorithmic stability type results for non-convex, heavy-tailed pairwise SGD by investigating the generalization performance and optimization jointly. Many theoretical results are obtained under various assumptions, including the general non-convex, non-convex without Lipschitz condition, non-convex with PL condition settings for pairwise SGD, and non-convex minibatch pairwise SGD.

### Strengths
A sequence of theoretical results is achieved, and the proofs seem to be correct and the logic is reasonable. The authors also introduced some new definition for pairwise learning algorithm to be $\ell_{1}$ on-average model stable. The paper is well written.

### Weaknesses
First, the model setup is a bit misleading. In the title and abstract, the authors call the setting heavy tails and heavy-tailed. However, what the authors really study is the sub-Weibull tails (Definition 3.6) that excludes polynomial decays as contrast to many papers the authors cited in the paper. Although there is no unique definition of heavy-tailedness, many readers would assume that you are talking about polynomial decay noise while you actually did not. I suggest you at least mention in the abstract that you are working with sub-Weibull tails. 

Second, the technical novelty and the necessity of working with sub-Weibull distributed gradient noise is not very convincing to me. The reason is that I understand that sub-Weibull type distribution can appear in the concentration type inequalities if you want to obtain some high probability guarantees. But this is not what the authors are doing in this paper. The authors simply use very standard $L^2$ type arguments to study the SGD. What I meant by that is that if you look carefully at the proofs in the appendix, the authors only need some assumption to bound the 2nd moment, instead of relying on the full definition of the sub-Weibull distribution as is described in Definition 3.6. That means all the existing proof techniques in SGD for finite variance setups can all be directly used in the paper. If all you need is an application of Lemma C.3. with $p=2$, i.e. a second-moment estimate, why don’t you simply assume that instead of your Definition 3.6. in your paper? Will all the results still go through? Essentially, Lemma C.3. with $p=2$ says that if the second-moment depends on the parameter $\theta$ in a certain way (where $\theta$ measures the heaviness of the tail), then it will also appear in the final results. In my view, the authors are not using the full information of sub-Weibull distribution, and there are numerous papers in the literature about SGD with finite variance, and hence to include heavy tails in the title and abstract and use that as a selling point is a bit misleading. 

Third, maybe I didn’t read the paper carefully enough, but it is not clear to me whether the same setting has been studied for pointwise SGD. If the answer is yes, then the authors should highlight the technical novelty and difficulty to extend the results to pairwise setting, which to me does not seem to be very difficult. Moreover, the authors should compare the results with the pointwise setting. On the other hand, if the answer is no, then I am wondering why the authors do not study the pointwise setting, which is much more common and popular in the literature, and the authors should comment on whether similar results can hold for pointwise SGD.

### Questions
For the main results, it would be better if the authors can provide some discussions on the monotonic (or not) dependence of the bound on $\theta$, which measures the heaviness of the tail, and provide some insights.  

On page 2, before you talk about developing previous analysis techniques to the heavy-tailed pairwise cases, you should also cite some works about algorithmic stability and generalization bounds for pointwise SGD with heavy tails from the literature. 

On page 3, you wrote that it is demonstrated in Nguyen et al. (2019); Hodgkinson and Mahoney (2021) that the generalization ability of SGD may suffer from the heavy-tailed gradient noise. However, I recently came across two more recent papers Raj et al. (2023) “Algorithmic stability of heavy-tailed stochastic gradient descent on least squares” and Raj et al. (2023) “Algorithmic stability of heavy-tailed SGD with general loss functions” that seem to argue heavy tails of gradient noise can help with generalization. I suggest you add more citations and discussions.

Assuming the gradient of loss function being Lipschitz is very reasonable. But assuming the gradient and the loss function itself are both Lipschitz seems to be quite strong. It would be nice if you can add some examples and discussions about your Assumption 3.7.

In Assumption 3.8. and Assumption 3.9., it would be better for you to add a line or two to explain what the expectations are taken with respect to.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
