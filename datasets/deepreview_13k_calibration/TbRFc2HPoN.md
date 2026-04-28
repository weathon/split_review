# Distributionally Robust Policy Learning under Concept Drifts

- Decision: Reject
- Avg Score: 4.33
- Scores: 5, 3, 5

## Abstract
Distributionally robust policy learning aims to find a policy that performs well 
    under the worst-case distributional shift, and yet most existing methods for 
    robust policy learning consider the worst-case {\em joint} distribution of 
    the covariate and the outcome. The joint-modeling strategy can be unnecessarily conservative
    when we have more information on the source of distributional shifts. This paper studies
    a more nuanced problem --- robust policy learning under the \emph{concept drift}, 
    when only the conditional relationship between the outcome and the covariate changes. 
    To this end, we first provide a doubly-robust estimator for evaluating
    the worst-case average reward of a given policy under a set of perturbed conditional distributions. 
    We show that the policy value estimator enjoys asymptotic normality even if the nuisance parameters 
    are estimated with a slower-than-root-$n$ rate.
    We then propose a learning algorithm that outputs the policy maximizing the 
    estimated policy value within a given policy class $\Pi$, and show
    that the sub-optimality gap of the proposed algorithm is of the order 
    $\kappa(\Pi)n^{-1/2}$, with $\kappa(\Pi)$ is the entropy integral of $\Pi$ under the Hamming distance
    and $n$ is the sample size. A matching lower bound is provided to show the optimality of the rate.
    The proposed methods are implemented and evaluated in numerical studies, 
    demonstrating substantial improvement compared with existing benchmarks.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper studies robust policy learning under the concept drift, where the distributional shift occurs only in the conditional reward distribution. The authors first develop a doubly-robust estimator for the worst-case policy value under concept drift, which is proved to be asymptotic normal, and then design a robust policy learning algorithm which achieves $n^{-1/2}$ regret.

### Strengths
Separating concept shift from covariate shift offers a fresh and insightful perspective in this field. The methods developed in this paper come with strong theoretical guarantees: the policy value estimator exhibits asymptotic normality, and the policy learning algorithm has $n^{-1/2}$ sub-optimality gap, improving previous results. Additionally, experiments conducted in a synthetic environment demonstrate that the proposed algorithm consistently outperforms baseline methods, further supporting the effectiveness of the approach.

### Weaknesses
While the paper is motivated by the idea that existing methods may be suboptimal under concept shift alone, it does not clearly demonstrate how its proposed rates improve upon existing ones. The improvement noted in Remark 4.3 seems more a result of advanced theorem-proving techniques (e.g., chaining) rather than a genuine improvement in performance metrics. Specifically, the paper does not provide a clear comparison of its regret bounds with those of existing methods under similar assumptions, making it difficult to assess the practical significance of the theoretical improvements. The use of chaining, while a valid technique, does not inherently guarantee a practically meaningful improvement if the underlying problem structure remains the same. Additionally, while the introduction raises the question of "optimal worst-case average performance" (lines 75-77), the paper lacks an optimality analysis of the derived bounds. Consequently, the theoretical contributions do not align strongly with the paper's motivation and feel somewhat insufficient in addressing the posed questions. The absence of a lower bound analysis makes it difficult to determine if the proposed algorithm's performance is indeed optimal or if further improvements are possible. Furthermore, the experiments are conducted solely in a synthetic environment, with no practical examples illustrating the benefits of the proposed algorithm. The lack of real-world validation limits the practical impact of the research, as synthetic environments may not accurately reflect the complexities of real-world concept shifts.

### Questions
How are the rates here compared with existing rates?

Are there lower bounds of value estimation and regret?

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
This paper studies the problem of distributionally robust contextual bandit, where the uncertainty only lies in the conditional reward distribution P(Y|X).

Some major comments are listed below:
1. First, Lemma 2.3 cannot be claimed as the contribution of this paper, as it is a standard result in the literature of KL constrained DRO. The authors shall provide credit to existing literature properly. 
Kullback-Leibler Divergence Constrained Distributionally Robust Optimization, Hu and Hong
Moreover, min over \eta in (3) has a closed form solution. Please check theorem 1 in the above paper. Therefore, there is no need for an iterative method to obtain \eta^*.

2. The technical presentation is hard to follow. Notations are not defined or not clearly introduced before use. For example g_\pi is not defined. What does propensity score function \pi_0 represent is not clear. Does the propensity score function mean the same thing as the behavior policy? 

3. Assumption 3.3. holds if $\theta^*_{\pi}(x)$ is continuous in x. Can the authors provide examples for this to hold?

4. The problem in this paper is in an offline setting, however, assumption 2.1 guarantees that any action can be visited in the training dataset with high probability, and therefore, the most challenging part of offline RL, e..g, partial coverage, is not addressed in this paper. How the performance depends on the concentrability coefficient is not clear from this paper. This limits the significance of this work. 

5. This paper investigates only distributional shift in the conditional reward, however, this does not seems to require development of new techniques comparing to distribution shift in the entire P(x,y).

### Strengths
see the summary

### Weaknesses
This paper studies the problem of distributionally robust contextual bandit, where the uncertainty only lies in the conditional reward distribution P(Y|X).

Some major comments are listed below:
1. First, Lemma 2.3 cannot be claimed as the contribution of this paper, as it is a standard result in the literature of KL constrained DRO. The authors shall provide credit to existing literature properly. 
Kullback-Leibler Divergence Constrained Distributionally Robust Optimization, Hu and Hong
Moreover, min over \eta in (3) has a closed form solution. Please check theorem 1 in the above paper. Therefore, there is no need for an iterative method to obtain \eta*.

2. The technical presentation is hard to follow. Notations are not defined or not clearly introduced before use. For example g_\pi is not defined. What does propensity score function \pi_0 represent is not clear. Does the propensity score function mean the same thing as the behavior policy? 

3. Assumption 3.3. holds if $\theta^*_{\pi}(x)$ is continuous in x. Can the authors provide examples for this to hold?

4. The problem in this paper is in an offline setting, however, assumption 2.1 guarantees that any action can be visited in the training dataset with high probability, and therefore, the most challenging part of offline RL, e..g, partial coverage, is not addressed in this paper. How the performance depends on the concentrability coefficient is not clear from this paper. This limits the significance of this work. 

5. This paper investigates only distributional shift in the conditional reward, however, this does not seems to require development of new techniques comparing to distribution shift in the entire P(x,y).

### Questions
see the summary

### Soundness
2

### Presentation
1

### Contribution
1

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper addresses distributionally robust policy learning under concept drift, focusing on cases where only the conditional relationship between covariates and outcomes changes. Using a KL-divergence-based framework, the authors define an uncertainty set that constrains shifts in the conditional distribution and develop a computational approach supported by duality to evaluate and optimize policies efficiently. They provide theoretical guarantees, including asymptotic normality and convergence rates, adding robustness to the methodology. Initial numerical results suggest the approach is less conservative than traditional joint distribution shift methods.

### Strengths
This paper discusses distributionally robust policy learning under concept shift. It relies on standard assumptions and considers a KL-divergence-based evaluation framework. It presents a duality result and provides an efficient estimator based on this result, with guarantees for asymptotic estimation rates and asymptotic normality.

The result is interesting and proposed concept shift makes sense because in practice, considering the worst-case joint distribution of the covariate and the outcome can be too conservative.

### Weaknesses
- The duality and theoretical results appear fairly standard, with proofs similar to existing literature. 
- The numerical results are very preliminary and lack in-depth discussion.  For example, $𝑥$ is assumed to follow a Gaussian distribution. 
- Additionally, the authors should expand on the results in Table 1. While they claim their method is better, the table mainly shows it is less conservative (which is expected, given the smaller uncertainty set they consider compared to the joint distribution worst-case uncertainty set). 
- They should provide more justification for why this choice makes sense in practice and discuss how to empirically determine the appropriate uncertainty type for policy learning (joint distribution shift vs. concept shift), which is not covered in the experiments.

### Questions
The authors could also expand on how to choose the uncertainty set parameter, as the results depend heavily on this choice. Additionally, they could discuss why they opted for KL-divergence over alternatives like Wasserstein distance, which might offer different insights or benefits in the context of distributional robustness.

### Soundness
2

### Presentation
3

### Contribution
2
