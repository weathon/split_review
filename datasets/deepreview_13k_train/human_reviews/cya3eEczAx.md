# Adaptive Proximal Gradient Optimizer: Addressing Gradient Inexactness in Predict+Optimize Framework

- Decision: Reject
- Scores: 1, 3, 1

## Abstract
To achieve end-to-end optimization in the Predict+Optimize (P+O) framework, efforts have been focused on constructing surrogate loss functions to replace the non-differentiable decision regret. 
While these surrogate functions are effective in forwarding training, the backpropagation of the gradient introduces a significant but unexplored problem: the inexactness of the surrogate gradient, which often destabilizes the training process. To address this challenge, we propose the Adaptive Proximal Gradient Optimizer (AProx), the first gradient descent optimizer designed to handle the inexactness of surrogate gradient backpropagation within the P+O framework. 
Instead of explicitly solving proximal operations, AProx uses subgradients to approximate the proximal operator, simplifying the computational complexity and making proximal gradient descent feasible within the P+O framework. We prove that the surrogate gradients of three major types of surrogate functions are subgradients, allowing efficient application of AProx to end-to-end optimization.
Additionally, AProx introduces momentum and novel strategies for adaptive weight decay and parameter smoothing, which together enhance both training stability and convergence speed.
Through experiments on several classical combinatorial optimization benchmarks using different surrogate functions, AProx demonstrates superior performance in stabilizing the training process and reducing the optimality gap under predicted parameters.

## Human Reviews

## Human Reviewer 1

### Rating
1

### Rating Number
1

### Confidence
3

### Summary
This paper addresses the predict and optimize framework, which utilises learning algorithms to predict parameters for optimization problems in an end to end fashion. Unforutnately, incorporating the optimization stage into the problem results introduces nonsmoothness into the objective. The paper addresses this issue by utilizing a proximal framework. The authors analyse the theoretical convergence and practical performance of their algorithm.

### Strengths
- The topic of the paper is interesting.
- The paper provides a review of related works.

### Weaknesses
There is a major error in the proof of theorem 1: on line 772 a lower bound is incorrectly combined with an upper bound. Specifically, the inequality on line 772 appears to be attempting to bound a term from below using a term that is only known to be an upper bound, which invalidates the subsequent steps. Since this is the basis for the main convergence result, this error compromises the theoretical results presented.  

I believe there is another error in the proof of corollary 2 (883-886). The sequence $||d_k|| $ need not converge to zero. For example, consider, $||d_k|| = (\delta\eta)/c$ which satisfies (44) but clearly does not converge to zero. The argument relies on the assumption that the term $||d_k||$ must approach zero because of the inequality, but this is not necessarily the case if the other terms in the inequality do not also converge to zero.

I also believe that there are major flaws in the specification of Algorithm 1. For example on line 3 the $ \hat{c_k} = \hat{c}(\theta_k) $, while in line 10 $ {\hat{c}}_{k+1} $ is computed as an update sequence based on the gradient. This inconsistency in how $\hat{c}$ is updated raises concerns about the algorithm's correctness. On line 12 a set of smoothed $ \tilde{\hat{c}}_k $ are computed but not utilised (so far as I can tell). The purpose of these smoothed parameters is unclear, and their lack of integration into the algorithm is a significant oversight.

Another concern I have with is the smoothing function selected by the authors. To compute the gradient of $f(\hat{c}) = \frac{1}{2} || \hat{c} - c||^2$ with respect to $\hat{c}$ requires knowledge of the "true cost parameters", which precludes practical implementation. This is a significant limitation as the true cost parameters are generally unknown in real-world scenarios. The authors do not address this critical issue, which undermines the practical applicability of their method.

Additionally, paper is significantly hindered by the quality of the writing with many awkward and confusing sentences, confusing notation and typos. The paper is difficult to follow due to theses issues. For example, in section 2.1 equation (3) is stated with no relation to the previous paragraph and (4) is stated with no discussion. There are issues like this in almost every section of the paper.

### Questions
See the weaknesses section. If the authors can clarify the theoretical concerns and substantially improve the quality of the text, I will be happy to take a second look at the paper.

### Soundness
1

### Presentation
1

### Contribution
1

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This work proposes to use an adaptive proximal gradient optimizer in order to address issues arising in inexact gradient computations in predict+optimize works. The idea is to first add a smooth function $f$ to the regret $R$. Next, this work integrates adaptive learning rate, momentum, and parameter averaging in the minimization of $\Phi = f + R$.

### Strengths
1) The proposed work is interesting and aims to tackle a well-known issue arising in the non-differentiability of the loss function in Predict & Optimize.
2) The numerical experiments show promising results for the proposed approach. 
3) The introduction and related works are well-written.

### Weaknesses
Major Comments:

1) The proof of the main theorem is incorrect. The inequality in Line 772 does not necessarily hold as a result of Line 765. The authors should revisit the proof and correct these details. Specifically, the transition from a bound on the expected value to a bound on the individual terms within the summation requires careful justification, and the current argument lacks this rigor. The proof needs to explicitly address how the adaptive learning rate and momentum terms interact with the regret function's properties to ensure convergence.

2) The paper claims that this paper uses a proximal update. However, the update is given by $\hat{c}_{k+1} = \hat{c}_k - \eta (\nabla f(\hat{c}) - g(\hat{c}))$, where  $g$ is an inexact gradient estimate of the non-smooth loss/regret term. The authors claim this is "implicitly a proximal update" in line 188, but this resembles a subgradient descent instead. It would benefit the paper if the authors could further elaborate on how this update relates to or a proximal update, or revise their claims if they cannot justify this connection. The connection to a proximal update is not clear, as a proximal update would typically involve solving a minimization problem involving a proximal term, which is not explicitly present in the given update rule. The authors need to clarify how their update implicitly achieves the effect of a proximal operator.

3) The main theorem relies on $R(\hat{c}) = c^\top(z^\star(\hat{c}) - z^\star(c))$ being convex in $\hat{c}$. However, it is not obvious that the regret is convex. This paper would benefit if it either provides a proof of convexity for the regret function, or discuss the implications if this assumption does not hold and how it might affect the validity of the results. The convexity of the regret function is a crucial assumption, and without a clear justification, the theoretical results are questionable. The paper should either provide a rigorous proof of this convexity under specific conditions or discuss the limitations of the proposed method if this assumption is violated.

Minor Comments:

1) The authors should update their references. For example, "Differentiation of Blackbox Combinatorial Solvers" is not cited properly, as it is already a published article.
2) The paper uses $\nabla R$ and $g$ interchangeably. However, $\nabla R$ is the true gradient of the regret (and assumes $R$ is differentiable), whereas $g$ is an approximation. The authors should update this in, e.g., Line 5 of the pseudocode and in line 259.  
3) Line 052: "non-differentiate" -> "non-differentiable"
4) Line 068: "gradient inexact" -> "inexact gradients"
5) $R(\hat{c})$ is never explicitly written. It would make the paper more readable if the authors explicitly defined it in Section 2
6) Line 161: "introduces" -> "introduced"
7) Line 233 "approachfocuses" -> "approach focuses"

### Questions
1) How do you tune hyperparameters $\eta$, $\lambda$, $\beta_s, \beta_m, \beta_p$? 
2) What does Table 7 show? Entries are denoted by "yes" and "no". There is no description in the caption. It is also not referenced in the main draft. The authors should remove unreferenced tables or reference them in the main draft. 
3) Line 368 states that Table 1 shows training with "several different regrets". However, Table 1 only shows optimization algorithms and not regrets. Is this line referencing the wrong table?

### Soundness
1

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
1

### Rating Number
1

### Confidence
4

### Summary
The "predict then optimize” (P+O) framework is a two-step approach for decision-making in scenarios where optimization is dependent on uncertain data. First, a predictive model (e.g., neural network) estimates unknown parameters or outcomes (e.g., demand, prices, costs) based on historical or contextual data. Next, using these predictions as inputs, an optimization model (LP solver) determines the best decision according to an objective function (e.g., maximizing profit, minimizing cost) under given constraints.

The framework assumes that the true prediction parameters are available when training the predictive model. However, training with direct supervision on these parameters (e.g., with squared loss) ignores the downstream performance metric -- the regret. Unfortunately, regret is not differentiable, or the gradients are zero, which does not allow end-to-end training. Therefore, several methods proposed surrogate losses (like SPO+) or surrogate gradients (IMLE, CMAP, DBB, NID - as denoted in the paper).

The paper under review proposes an optimizer designed explicitly for the P+O framework that should utilize the surrogate gradients better than existing general optimizers. The method is inspired by proximal gradient descent and utilizes existing ingredients like momentum, adaptive lr, and smoothing.
The work claims some convergence guarantees in the convex case with a bound on convergence rates and empirically compares them to existing popular optimizers.

### Strengths
The paper tries to tackle an important problem in the popular P+O framework. Proving convergence is not straightforward, even in a simple setting with exact gradients.

### Weaknesses
### weaknesses:
 The paper attempts to address a significant challenge within the "predict then optimize” (P+O) framework but falls short in several critical areas. It appears that the core contribution essentially boils down to adding a squared loss on the prediction parameters (costs) to an existing surrogate loss function (or, equivalently, adding the gradient of a squared loss to an existing surrogate gradient). This is done in a rather convoluted manner, and the method is then paired with a customized version of the Adam optimizer and weight decay. This approach lacks novelty and does not significantly advance the understanding or methodology in the field of P+O optimization.

Specifically, the paper recalls proximal gradient descent (Equation 8) but fails to utilize it effectively. The claim that "computing the proximal operator $prox_{\eta R}$ can be impractical in P+O problems" is used as justification to instead utilize an existing surrogate gradient. However, Equation 9 reveals that this surrogate is combined with the gradient of an $\ell^2$ norm, which undermines the initial premise of leveraging proximal methods for improved optimization within the P+O framework.

Furthermore, Theorem 1 is not proven correctly and likely does not hold in its presented form. Several issues plague the theorem:
- Equation 13 includes a constant $\delta$, which is not properly quantified. It is only mentioned in Equation 5, where it requires a uniform bound across $\hat c$. The reliance on $\delta = \sup_{\hat c}\|g(\hat c)\|$, where $g(\hat c)$ is the surrogate gradient, is problematic because the true gradient of the LP solution is either zero or undefined.
- The definition of $d_k$ is unclear, as $\nabla R(\hat c_k)$ is not uniquely defined.
- The inequality in line 834 does not hold. For instance, if $\eta$ is close to $1/L$, the left-hand side (LHS) approaches zero, while the right-hand side (RHS) becomes negative (close to $-\delta/L\|d_k\|$).
- In line 836, the 'higher order terms' $L\eta^2\delta^2$ cannot be simply 'neglected' without a limiting process. The assumption that $\delta$ is 'small' is also incorrectly applied here.

The proof of Corollary 2 is also flawed. Equation 44 does not guarantee the convergence of the sum. For example, the sums $\sum_{k=1}^N 1/k -\sum_{k=1}^N 1/\sqrt k\le 0$ both diverge, invalidating the claim.

The paper suffers from numerous incorrect or imprecise statements:
- Line 67 states, "The problem of gradient inexact caused by the agent function for P+O under the end-to-end framework has not been emphasized, and research is lacking." This is inaccurate, as the referenced papers directly address this issue.
- Line 36 claims, "end-to-end approaches are also an emerging topic in the decision-making process." This statement is overly broad and lacks specific context.
- In the section "Inexact Gradient Challenge in P+O Framework," the statement "The existence of errorbound can mislead the direction of descent, which will eventually lead to the problem of unstable or non-convergence of the training process" is misleading. The true gradient is always zero or undefined; thus, any informative descent direction would increase $\delta$. There is no direct link between $\delta$ and instability or non-convergence, or it might be the opposite, that a large $\delta$ is required for convergence.
- In the section "Adaptive Proximal Gradient Optimizer (AProx)," line 165 states, "$R(\hat c)$ is not trivial." This statement is vague and lacks meaning.
- Line 172 states, "The number 1/2 as coefficients of $f(\hat c)=\tfrac12|\hat c-c|^2$ is to avoid its excessive influence on the  gradient of the composite function." This is incorrect; the coefficient is used to avoid an unnecessary constant in the proximal gradient step.
- Line 188 claims, "This approach effectively integrates the proximal operator implicitly and allows us to proceed without its explicit computation." This is inaccurate; it effectively ignores the proximal map.
- In the section "Theoretical Convergence Analysis," line 240 states, "It is worth noting that Lemma 2 rests on the fact that R(·) is a convex function. In the solution approaches of P+O, most of the constructed surrogate functions can satisfy convexity." This is not entirely true. While some methods might involve convex functions, it does not guarantee the overall convexity of the surrogate function. For instance, "DBB uses linear interpolations..." which is correct but does not ensure convexity, and similarly for IMLE.

The paper also employs nonstandard or misleading terminology:
- "Agent function" and "agent gradient" are used instead of surrogate loss/gradient.
- "Discovergence" is a nonstandard term.
- The term 'gradient' is frequently used for objects that are not true gradients but surrogate ascent directions.
- "Training rounds," "step size," and "calendar hours" are used instead of epochs.
- Other examples include "We ... give an inference on the rate of descent" (line 80), "We propose the inexact surrogate gradient problem" (line 74), "the optimizer, which is improved on the proximal gradient" (line 77), "to address the inexact gradient challenge in Predict+Optimize (P+O) challenge" (line 156), and "we used the l2 paradigm term for the prediction error" (line 170).

Regarding the experiments:
- The benchmark settings in Tables 1, 3, and 5 are not clearly defined. The claim that "Table 1 shows the step size and training time per epoch required for convergence when training with several different regrets" is confusing. It seems "regrets" refers to surrogates like IMLE, NID, CMAP, SPO, or DBB, but the calculation of the statistics is not described. The large standard deviations in the tables also make it difficult to draw any meaningful conclusions.
- The experimental setup is not well-explained. The metric used (relative optimal gap) measures the performance of the trained model, not the optimizers. The training process is not detailed, and the significance of the results is unclear, with no statistical testing or standard deviations reported.

Overall:
- The paper proposes an enhancement to optimization within the P+O framework but lacks clarity and rigor in both theoretical claims and experimental evaluation.
- The main contribution—adding a squared loss to an existing surrogate with a custom optimizer—is presented in a confusing way and does not offer novel insights or a better understanding of existing methods.
- Theoretical issues, particularly in Theorem 1 and Corollary 2, contain significant flaws.
- Misleading terminology and insufficient experimental setup description, along with inadequate statistical analysis, limit the work's impact.

### Questions
I have no questions

### Soundness
1

### Presentation
1

### Contribution
1
