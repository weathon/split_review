# Counterfactual Learning under Rank Preservation

- Decision: Reject
- Avg Score: 4.25
- Scores: 3, 3, 6, 5

## Abstract
Counterfactual inference aims to estimate the counterfactual outcome given knowledge of an observed treatment and the factual outcome, with broad applications in fields such as epidemiology, econometrics, and management science. In this paper, we propose a principled approach for identifying and estimating the counterfactual outcome.  Specifically, we introduce a simple and intuitive rank preservation assumption to identify the counterfactual outcome without relying on a known structural causal model. Building on this, we propose a novel ideal loss for theoretically unbiased learning of the counterfactual outcome and further develop a kernel-based estimator for its empirical estimation. Our theoretical analysis shows that the proposed ideal loss is convex, and the proposed estimator is unbiased. Extensive semi-synthetic and real-world experiments are conducted to demonstrate the effectiveness of the proposed method.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper proposes a new method for counterfactual estimation. The method needs slightly less stringent assumptions than existing approaches.  Based on a novel convex loss function, the paper proposes a kernel-based counterfactual estimator and shows its unbiasedness.

### Strengths
- The paper proposes a fundamental approach to counterfactual inference, an important topic, and can be a basis for future research in the field of counterfactual inference.
- Although the proposed approach is simple, it allows for a slight release of the stringent assumption in counterfactual inference.
- The paper is very well written and motivated.

### Weaknesses
 - The proposed rank-preservation assumption is still very strong and unrealistic in practice.
- The mathematical notation could be introduced more thoroughly (line 87).
- The proposed method (and the loss function) only apply to continuous outcomes. However, this is not stated in the paper. Furthermore, the paper even argues with discrete outcomes (line 227).
- The related work section mostly discusses and cites works irrelevant to the topic (e.g., the paragraphs on CATE estimation and on the applications).
- The empirical evaluation is not suitable for evaluating the proposed method. It evaluates the method for estimating treatment effect (and compares it to baselines for treatment effect estimation).
However, the proposed method tackles counterfactual estimation. Although these two topics are obviously very connected, a proper evaluation of the main task of the method and a comparison with proper baselines for this task is necessary.

### Questions
- What is the intuition behind the definition of the introduced loss function? Could the authors please elaborate?
- How could the loss function and the method handle discrete outcomes?
- The paper states the asymptotic unbiasedness of the estimator. However, there are no statements on finite-sample performance. How does the kernel-smoothing affect the finite-sample performance (for different variable types of z)? 
How does it compare to a discretized version (of the potentially continuous Z)? In the latter case, one would not need to perform smoothing.
- The method needs to learn the propensity function before the counterfactual estimation. How does the propensity estimation error propagate to the final counterfactual estimation error?
- Line 369: What is meant by "robustness of our method"?
- There are some typos in the text, and some citations are mixed up (unintentionally).

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper introduces a rank preservation assumption to identify counterfactual outcomes. Building on this foundation, it proposes a loss function that yields an unbiased estimator, and further develops a kernel-based estimator for empirical estimation.

### Strengths
(1) The paper is clearly written and easy to read. It provides a comprehensive review of previous work on counterfactual learning, identifies gaps, and discusses similarities and differences in assumptions and estimation strategies compared to prior research.

(2)  The proposed loss function does not require prior estimation of the structural causal model, nor does it assume that the two conditional quantile models are identical. Additionally, it does not require explicit estimation of a different quantile value for each individual.

### Weaknesses
The experimental results can benefit from additional discussions, such as why your method has in general higher uncertainty around its performance compared to Quantile Reg (see Table 1 and Figure 1).

Also, it is a bit strange that the results for your method has notably higher standard error for $m=5$. Why is that? Because this would have important implications on methods' utility in worst case, it is important to understand and discuss the reasons behind it.

For instance, are there special data-generating cases where your method performs worse in particular? That does not necessarily put your method down, but it is important to identify and discuss those cases.

Misc--

Line 377 - Typo: "Prepossessing"

Table 1 - CFQP has better out-sample PEHE perf.

### Questions
Please see Weaknesses.

### Soundness
2

### Presentation
2

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
Authors study counterfactual inference problem and propose a novel identification/estimation strategy, demonstrating its advantages through existing methods.

### Strengths
The paper is well written and organized. Authors clearly list their assumptions and describe their contributions.

The related work is well-covered and it motivates the approach presented in the paper.

The technical contribution is novel. Authors identify an alternative assumption sufficient for identifying the CATE and show how it can be estimated in an unbiased way through a convex loss function.

Experimental evaluation includes many baselines that are prevalent in the literature, and the proposed approach seems to present a notable performance boost.

### Weaknesses
The experimental results can benefit from additional discussions, such as why your method has in general higher uncertainty around its performance compared to Quantile Reg (see Table 1 and Figure 1).

Also, it is a bit strange that the results for your method has notably higher standard error for $m=5$. Why is that? Because this would have important implications on methods' utility in worst case, it is important to understand and discuss the reasons behind it. 

For instance, are there special data-generating cases where your method performs worse in particular? That does not necessarily put your method down, but it is important to identify and discuss those cases.


Misc--

Line 377 - Typo: "Prepossessing"

Table 1 - CFQP has better out-sample PEHE perf.

### Questions
See above.

### Soundness
4

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
This paper proposes a new identification condition, under which the individual counterfactual can be identified. The condition requires the rank of counterfactuals to be in accordance with the observed outcomes. The authors then provide an algorithm for learning the counterfactuals via empirical risk minimization. The proposed algorithm is evaluated on synthetic and real data.

### Strengths
This paper considers a very challenging and interesting question and offers a thought-provoking solution (the new identification scheme). There is an exhaustive literature review and comparison with existing work.

### Weaknesses
If I understand correctly, the new identification condition requires the rank of the observables to be *almost surely* the same as that of the counterfactuals.This appears to be a very strong assumption to me: if patient A has a better baseline than a similar patient B, then the potential outcome of patient A under treatment *has*to be better than that of patient B; but in practice, one could imagine that there can be (at least) some randomness such that this condition is violated. It would be helpful to provide more discussion on why this is a reasonable condition.

### Questions
Apart from the comment/question in the weakness section, I have the 
following question regarding the learning algorithm guarantee: 
1. It appears that Theorem 5.3 applies to a fixed value of t, which does not imply the 
guarantee on minimizer of $\hat R_{x'}(t \mid x,z,y)$. If that is the case, I wonder if 
the results can be generalized to data-driven t?
2. Does one need to solve an optimization problem for each $(x,z,y)$?

### Soundness
3

### Presentation
3

### Contribution
2
