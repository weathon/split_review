# Efficient Causal Decision Making with One-sided Feedback

- Decision: Accept
- Scores: 6, 6, 8, 6

## Abstract
We study a class of decision-making problems with one-sided feedback, where outcomes are only observable for specific actions. A typical example is bank loans, where the repayment status is known only if a loan is approved and remains undefined if rejected. In such scenarios, conventional approaches to causal decision evaluation and learning from observational data are not directly applicable. In this paper, we introduce a novel value function to evaluate decision rules that addresses the issue of undefined counterfactual outcomes. Without assuming no unmeasured confounders, we establish the identification of the value function using shadow variables. Furthermore, leveraging semiparametric theory, we derive the efficiency bound for the proposed value function and develop efficient methods for decision evaluation and learning. Numerical experiments and a real-world data application demonstrate the empirical performance of our proposed methods.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper addresses decision-making with one-sided feedback, where outcomes are observable only for chosen actions, such as approved loans. The authors introduce a new value function for evaluating decisions without assuming the no unmeasured confounders (NUC) condition. Using shadow variables, they establish identifiability and derive the efficient influence function (EIF) and the semiparametric efficiency bound of the value function. Motivated by the EIF, they develop two efficient estimators for the value function, applicable to binary and continuous outcomes, respectively. They propose a weighted, classification-based framework to learn the optimal decision rule. Empirical results validate the method's effectiveness.

### Strengths
The paper's main strength  is introducing a modified value function and establishing identifiability for this value function by leveraging so called shadow variables (SVs). The authors derive the efficient influence function (EIF) and the semiparametric efficiency bound of the value function. Additionally, in the case of continuous distributions, their proposed estimation strategy avoids estimating the density when the outcome is continuous, thus preventing instability. Furthermore, they demonstrate that their estimators are consistent and achieve the semiparametric efficiency bound under mild conditions for nuisance function approximation.

### Weaknesses
The assumption of knowing the shadow variables (SVs) may restrict the practical application of the proposed approach. Specifically, the requirement that these variables are truly independent of the action assignment mechanism, conditional on observed covariates, is a strong assumption that may not hold in many real-world scenarios. The paper would benefit from a more thorough discussion of the sensitivity of the results to violations of this assumption. Similarly, assumption 4.2 could also limit the applicability of the proposed methods. While the authors cite some relevant papers for assumption 4.2, more discussion is needed to clarify how restrictive this assumption is, especially in cases where the conditional distribution of the outcome given the action and covariates does not belong to a well-behaved family. The proposed methodology requires that conditional expectations \( P(Y | A = 1, X) \) be consistently estimated. This might be an issue particularly for high-dimensional discrete covariates, i.e., categorical variables that can take on a large number of distinct categories or levels. The paper does not adequately address the challenges of estimating these conditional expectations when faced with a sparse design matrix resulting from one-hot encoding or similar techniques for high-cardinality categorical features.

### Questions
I have some questions/comments for the authors:

* The authors state that assumption 4.2 guarantees the uniqueness of $ \phi(u,y) $. Can the authors explain how this assumption guarantees this? Also, is it a sufficient condition for uniqueness, or could there be necessary or more relaxed conditions?

* Regarding assumption 4.2, it is worthwhile to discuss in the paper how restrictive this assumption is. Perhaps the authors could mention some cases where it does not hold.

* How do high-dimensional categorical covariates affect the estimation for the conditional expectations as required by assumption 5.1?

* The authors mentioned that the maximizer for the efficient estimator denoted by $ \hat{\pi} $ is a natural estimator for the true optimal decision rule $ \pi^* $, which is a maximizer of the true value function. Although in experiments, the authors show percentages of making correct decisions (PCD), can they provide any discussion on how far $ \hat{\pi} $ can be from the true optimal rule $ \pi^* $ in general?

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper defines a new value function for the problem of 'one-sided feedback' in causal inference for decision making.

It provides identification results, using the so called 'shadow variables'.

The authors also provide efficiency bounds using semi-parametric. 

Finally, they also provide empirical evidence for their new method.

### Strengths
The paper is strong in exposition of its core idea, methods, experiments and results.

It seems technically sound.

### Weaknesses
I struggle to accept the core assumption made in line 157:

"On the other hand, if π(X) = 0, indicating loan rejection, the bank neither earns nor loses any money. Therefore, the newly defined value function V1(π) quantifies the expected monetary outcome for the bank when implementing decision rule π for loan approvals"

I want to argue that the bank in fact does lose money when it rejects a loan. Some of the loans, might have in fact not defaulted and therefore produced a profit for the bank. This concept is known to me as "opportunity cost", sometimes defined as "the loss of potential gain from other alternatives when one alternative is chosen".

In this case, it'd be the loss of the potential gain from giving out the loan, when choosing to reject the loan applicant.

There seems to be no discussion of whether this new definition of the value function makes conceptually sense. It is assumed to be valid, and technical challenges are solved (probably successfully).

If it's just a technical convenience, but no practical relevance, than the contribution of this paper is hard to justify without a stronger discussion of why a user should accept this value function.

### Questions
Can you help me understand why your new value function is of practical value and relevance?

- Is the concept of 'opportunity cost' relevant? Why or why not?
- Is there a practical background for this new value function? is it already being used in decision making elsewhere?
- What was the inspiration for this value function? Is it simply the observation that we can't do anything otherwise or is there a more fundamental observation from e.g. banking where this function is being actively used?

If it's just a technical convenience, but no practical relevance, than the contribution of this paper is hard to justify without a stronger discussion of why a user should accept this value function.

If there is more to it than just a technical connivence, than I am very keen to learn about that!

Thanks!

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
The paper addresses decision-making scenarios where only specific actions yield observable outcomes. Since counterfactuals are undefined in this setting, a new method beyond conventional causal inference approaches is needed. The paper proposes a novel value function to evaluate decision rules in one-sided feedback contexts without assuming no unmeasured confounders. An efficiency bound, $\Gamma(\pi)$, is provided for the value function. The paper also introduces efficient estimators for decision evaluation and learning. Through simulations and applications on real-world data, including a bank loan dataset, the paper demonstrates that the proposed method surpasses traditional approaches in robustness and efficiency for evaluating and learning decision rules.

### Strengths
Please find the strengths below:
1. The paper studies an important problem in practice. In applications like credit card applications and bank loans, the outcomes may not be observable when certain actions are taken.
2. The algorithm for learning and evaluating the causal relationship is theoretically effective. The use of shadow variables is innovative and removes the requirement of the NUC assumption.
3. The paper provides both numerical and practical experiments. The experiments show the efficiency of the proposed estimators for the one-sided feedback setting.
4. The method in the paper appears flexible and adaptable to me, allowing it to be extended to a variety of settings with partial feedback.

### Weaknesses
Please find the weaknesses below:
1. The paper only considers binary actions, i.e., $A=0,1$, which is relatively limited. Given that this is an initial work on partial feedback learning, this limitation is acceptable to me.
2. I did not find any discussion on the optimality of the semiparametric efficiency bound $\Gamma(\pi)$.
3. The numerical experiment is based on a specific setting, which is not general enough (both the action distribution and the outcome function are fixed). The experiment on the bank loan dataset does not show a very notable improvement of the proposed method over IPW-eff, compared to the results in the numerical experiment.

### Questions
Refer to the weaknesses section above, and find the additional questions below:
1. Is it possible to extend the work to non-binary action settings and more general partial feedback causality settings?
2. Including a wider range of settings in the numerical experiments would make the results more persuasive.
3. The theoretical analysis considers binary and continuous outcome variables. Does the theoretical analysis also apply to categorical outcomes?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The authors study a class of decision-making problems with one-sided feedback, where outcomes are only observable for specific actions. They introduce a value function to evaluate decision rules that address the issue of undefined counterfactual outcomes. Without assuming no unmeasured confounders, they establish the identification of the value function using shadow variables. Furthermore, leveraging semiparametric theory, they derive the efficiency bound for the proposed value function and develop efficient methods for decision evaluation and learning. Numerical experiments and a real-world data application demonstrate the empirical performance of proposed methods.

### Strengths
The paper is well-written. The paper establishes rigorous identification results and semiparametric theory.

### Weaknesses
It seems that the framework essentially treats all $Y(0)$ as 0. Then is the task just to predict the sign of $Y(1)$?

### Questions
It seems that the framework essentially treats all $Y(0)$ as 0. Then is the task just to predict the sign of $Y(1)$?

### Soundness
2

### Presentation
3

### Contribution
2
