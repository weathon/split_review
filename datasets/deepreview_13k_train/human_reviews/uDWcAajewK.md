# Learning from interval targets

- Decision: Reject
- Scores: 5, 6, 6, 6

## Abstract
We consider regression problems where the exact real-valued targets are not directly available; instead, supervision is provided in the form of intervals around the targets—that is, only lower and upper bounds are known. Such a "learning from interval targets" setup arises in domains where labeling costs are high or there is inherent uncertainty in the target values. In these settings, traditional regression loss functions, which require exact target values, cannot be directly applied. To address this challenge, we propose two approaches: (i) modifying the regression loss function to be compatible with interval ground truths, and (ii) formulating a min-max problem where we minimize the typical regression loss with respect to the "worst-case" label within the interval. We provide theoretical guarantees for our methods, analyze their computational efficiency, and evaluate their practical performance on real-world datasets.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper investigates the regression problem in a situation where the learner has access only to an interval around the true response. It proposes two approaches:
 
1. Modifying the regression loss function with a projection and learning a hypothesis lying within the interval
2. Minimizing a typical regression loss with respect to the worst-case label

### Strengths
This work investigates an interesting situation where the learner has access only to an interval around the true response, rather than the exact response as in the standard supervised learning setting. Due to the high cost of getting exact responses, learning from intervals has significant practical meanings. 

It proposes two approaches and provides both theoretical analysis and experiments on real-world datasets. For the theoretical results, the proofs are clear and easy to follow, accompanied by a sufficient explanation of the derivations.

### Weaknesses
1. This paper highlights a generalization bound in Section 3.3 as its main result. However, this bound seems too straightforward and can be quite vacuous -  e.g., Theorem 3.5 is only taking an expectation of Equation (12), which is the worst-case analysis on a single instance. The bound essentially states that the expected error is bounded by the expected worst-case error on a single instance, which doesn't provide much insight into the generalization capabilities of the proposed methods. It lacks a clear connection to the empirical performance one would observe on a test set, making it difficult to assess the practical relevance of the bound.
2. The multiple parameters appearing in the generalization bound are difficult, if impossible at all, to obtain. For example, in order to get the bound in Theorem 3.5, one needs to know $I_\eta$. $I_\eta$ consists $r_\eta$, which involves the calculation of an expectation with respect to $X$ (Equation 9). Usually, one is not able to compute the expectation efficiently. Furthermore, the Lipschitz constant $m$ of the hypothesis class, which appears in the bound, is also difficult to estimate in practice, especially for complex models like neural networks. This makes the bound impractical for model selection or performance prediction.
3. To obtain an estimate of $\eta$, one needs to know the Rademacher complexity of $\Pi(F)$, which can be quite difficult to obtain. The Rademacher complexity is a measure of the richness of the function class, and its computation often requires specialized techniques and assumptions about the function class. Without a practical way to estimate this quantity, the bound remains largely theoretical and difficult to use in practice. The paper does not provide any guidance on how to estimate this quantity for common hypothesis classes.

### Questions
1. It's mentioned that Theorem 3.5 can be tight for certain hypothesis classes, for instance, constant hypotheses. However, the constant hypothesis seems to be too restrictive. Could you provide another instance of hypothesis class, where this theorem can be relatively tight?
2. Is it possible to obtain the parameters in the generalization bounds in an efficient way?
3. In lines 179-182, it's mentioned that a value of $\eta$ is obtained from the RHS of Equation (6); how would one calculate the Rademacher complexity of $\Pi(F)$? How does the tightness of an estimation of $\eta$ affect the later generalization bounds?
4. In lines 201-202, why $\eta_n = O(1/\sqrt n)$? How does the Rademacher complexity of $\Pi(F)$ affect the order of $\eta_n$?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper investigates a weakly supervised regression setting called “learning from interval targets," where the exact real-valued targets are not directly available; instead, supervision is provided in the form of intervals around the targets. The authors suggest that previous research assumptions for theoretical analysis were overly simplistic (SMALL AMBIGUITY DEGREE ASSUMPTIONS). Therefore, they propose new theoretical analyses to address more robust real-world scenarios. To tackle this problem, the authors propose two methods: (1) using surrogate loss functions to align targets with weak supervision labels (PROJECTION APPROACH); and (2) considering the worst-case scenario within the intervals and minimizing that risk (MINMAX OBJECTIVE). Extensive experiments validate the effectiveness of the authors' methods.

### Strengths
- The authors discuss an intriguing weakly supervised regression problem: learning from interval targets. Most research has only considered classification problems, but they overlook that regression problems are equally important.
- The authors provide (reasonable) theoretical analyses for their methods, demonstrating the effectiveness of the proposed approaches.
- The methods proposed by the authors are both natural and reasonable, and the paper is well-organized and easy to understand.

### Weaknesses
 - The experimental setup considered by the authors is too simplistic, as it only involves a small number of UCI datasets, and the selected datasets are simple (small and low-dimensional). Previous research seems to have also considered experimental setups in CV and NLP.

- The authors' analysis is based on the rejection of the SMALL AMBIGUITY DEGREE ASSUMPTIONS, but I believe their rejection of this assumption is not convincing enough, as it would be impossible to learn if noise is always present.

- The description of how pseudo-labels are generated in the PL (max) and PL (mean) methods is insufficiently detailed. While the authors mention that pseudo-labels are derived from a hypothesis $f_j$, the process of obtaining $f_j$ is not clearly explained. Specifically, the experimental setup used to determine $f_j$ is not clear, which is a critical component of the PL (max) and PL (mean) methods. The explanation lacks specifics on the data used and the precise steps involved in minimizing the empirical projection loss to obtain $f_j$.

### Questions
- The authors believe that the SMALL AMBIGUITY DEGREE ASSUMPTIONS are not applicable in regression scenarios primarily because regression tasks differ from classification tasks in having exact labels. Therefore, directly applying the previous SMALL AMBIGUITY DEGREE ASSUMPTIONS is unreasonable. Should the AMBIGUITY DEGREE ASSUMPTIONS be redefined instead of being directly rejected? A larger AMBIGUITY DEGREE might result in intervals that are always mixed with noise, making it impossible to discern the true label distribution. Alternatively, could the size of intervals be used to constrain the AMBIGUITY DEGREE to satisfy a new relationship?
- In the PL (max) and PL (mean) methods, the authors utilize pseudo labels, but it seems there is no mention of how these pseudo labels are generated.
- The projection loss proposed by the authors (Equation 5) appears to be consistent with the surrogate loss function in [1]. Does this imply that the method in [1] can still be applicable under the new setting (SMALL AMBIGUITY DEGREE ASSUMPTIONS does not apply) ?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper considers a regression analysis problem where the outcome of each training sample is given by not single value but an interval. An existing method assumes the "realizability" and "ambiguity degree < 1" in the existing method, and it employs the loss function called the "projection loss" and proved the theoretical performances. However, since these assumptions are too restrictive, the paper relaxes the assumptions, and accordingly constructed another learning setup called "minmax objective".

### Strengths
-   The formulations of the problem and the method looks clear.
-   The method introduced less restrictive constraint than existing work: the class of hypotheses ${\cal F}$ must contain only $m$-Lipschitz functions. Also, the experiment in Section 5.2 examines the effect of the choice of $m$ in the algorithm. (As discussed with equation (16), $m$ should not be too small or too large.)

### Weaknesses
 -   It looks that a part of experimental setups are lacked. Please see Section "Question" below.
-   Just notation problems, but it is difficult to follow the effect of the Lipschitz constant $m$. It may be better to add "$m$" to all operations affected by $m$ (e.g., replacing $l_{x'\to x}$ with $l^{(m)}_{x'\to x}$).

-   Section 2, line 133: What is the "$\ell$1 loss as the surrogate" for the 0-1 loss? The l1-loss surrogate for (1) is not so obvious, although we can understand it after reading its mathematical expression in (Cheng et al., 2023a).
-   Section 2, equation (2): What are the capital letters $L$ and $U$? Perhaps the lower and upper bounds as random variables? (If so, what are their distributions?)
-   Section 3, equation (6) and the succeeding sentences: Are $\pi_{\ell}$ and $\pi_l$ the same? (Perhaps just non-unified notations?)
-   Section 3.2, Proposition 3.2: What situation the induced lower bound and upper bounds of $f(x)$ is effective? As far as my understanding, if the size of the bounds is small at $x'$, the size at another point $x$ must be accordingly small under the constraint of Lipschitz continuity.
-   Section 3.3.1, equation (13): What are the definitions of $I_0$ and $I_\eta$? (Although I could guess them,) their specific definitions seems not to be given.
-   Section 3.3.1, equation (14): Is the equation correct? The rightmost expression of the equation looks like independent from $x$.
-   Section 4: Are the notations "$f'$'s" in equations (20) and (21) are related? If not, it is better to introduce different variables.
-   Section 5 (Appendix D): What is the obstacle (e.g., computational cost) to run the proposed method for a larger dataset? The datasets used in the experiments have up to 10000 samples.
-   Section 5: The proposed method assumes that the class of hypotheses is $m$-Lipschitz, but in the experiment how can we limit the prediction model (MLP in this case) as $m$-Lipschitz? (The paper refers the existing work (Cheng et al., 2023a), but in the existing work it looks that $m$-Lipschitz is not employed.)
-   Section 5: What loss function does the experiment employed? (More specifically, $\psi$ in Assumption 1)

### Questions
-   Section 2, line 133: What is the "$\ell$1 loss as the surrogate" for the 0-1 loss? The l1-loss surrogate for (1) is not so obvious, although we can understand it after reading its mathematical expression in (Cheng et al., 2023a).
-   Section 2, equation (2): What are the capital letters $L$ and $U$? Perhaps the lower and upper bounds as random variables? (If so, what are their distributions?)
-   Section 3, equation (6) and the succeeding sentences: Are $\pi_{\ell}$ and $\pi_l$ the same? (Perhaps just non-unified notations?)
-   Section 3.2, Proposition 3.2: What situation the induced lower bound and upper bounds of $f(x)$ is effective? As far as my understanding, if the size of the bounds is small at $x^\prime$, the size at another point $x$ must be accordingly small under the constraint of Lipschitz continuity.
-   Section 3.3.1, equation (13): What are the definitions of $I_0$ and $I_\eta$? (Although I could guess them,) their specific definitions seems not to be given.
-   Section 3.3.1, equation (14): Is the equation correct? The rightmost expression of the equation looks like independent from $x$.
-   Section 4: Are the notations "$f^\prime$"'s in equations (20) and (21) are related? If not, it is better to introduce different variables.
-   Section 5 (Appendix D): What is the obstacle (e.g., computational cost) to run the proposed method for a larger dataset? The datasets used in the experiments have up to 10000 samples.
-   Section 5: The proposed method assumes that the class of hypotheses is $m$-Lipschitz, but in the experiment how can we limit the prediction model (MLP in this case) as $m$-Lipschitz? (The paper refers the existing work (Cheng et al., 2023a), but in the existing work it looks that $m$-Lipschitz is not employed.)
-   Section 5: What loss function does the experiment employed? (More specifically, $\psi$ in Assumption 1)

### Soundness
3

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
2

### Summary
This paper studies a regression model where only an interval around the true response is known to the learner. Given such weak supervision, the goal of the learner is to learn a predictor whose population risk is small. To tackle this problem, the authors propose two methods. The first modifies the standard regression loss functions to account for interval ground truths. In particular, a projection loss is defined which penalizes the the output a learned predictor when its outputs lie outside the interval for a specific instance. The second formulates a minimax problem with an objective that minimizes the original regression loss with respect to the worst-case label within the interval (available to the learner). In both settings, the authors show how the smoothness of the function class (measured via Lipschitzness) can be beneficial. The authors provide theoretical guarantees for both methods and corroborate their results with experiments.

### Strengths
- Paper is well written and organized
- Paper improves upon previous works by removing assumptions and the ideas seem novel as far as I can tell
- I think the Figures do a good job of giving intuition about the methods

### Weaknesses
 - Unclear objective. I think the authors can do a better job about making explicit the fact that although the learner observes interval targets, the goal is to still do well with respect to the original regression loss. This goal is sort of hidden in lines 101-102, and it would be nice to emphasize this more. 

- Lack of specification on how error rates decay with sample size. It is not clear how the excess risk in lines (13) and (16) decays with the sample size $n$. For all I know, it may not decay at all, making the error bounds vacuous. At the very minimum, it would be nice if the authors can provide error rates for a specific class of functions. This is also an issue in line (22) - I have no intuition on how the error might decay with the sample size here.  I think this is a significant limitation and is the main reason for my rating. I will raise my score if the authors can give me a sense of how the non-asymptotic error rates decay with $n$, even it is for a specific function class. 

- Unclear method. I am confused about certain aspects of the methods proposed in Section 4.1 See Questions below for more details.

- Does Proposition 3.1 hold uniformly for all $x \in X$? If so, I am confused since $f \in \tilde{F_{0}}$ only guarantees that $f(x) \in [l_x, u_x]$ almost surely. So there could still be $x$'s (albeit in a measure $0$ set), for which this is not true. 
- What norm is being used on line 236?
- Is the guarantee on line 267 pointwise or in expectation? If it is pointwise for every $x$, how are you accounting for the fact that the functions $f \in \tilde{F_{\eta}}$ may have projection loss bigger than $\eta$ for low probability $x$? Is this accounted for by definition of $r_{\eta}(x)$ and $s_{\eta}(x)$? If so, it would be good to explain how the buffer $r_{\eta}(x)$ and $s_{\eta}(x)$ account for that. 
- Is $\tilde{F}_0$ known to the learner in Equation (23)? It seems like the learner needs to know the distribution $D$ over $X$ to compute $\tilde{F}_0$ based on line 170. So because the learner doesn't know $D$, it shouldn't be able to perform the optimization in Equation (23). What am I missing here?
- Based on the bullet points above, how does the learner know that the $f_1, ..., f_j$ in line 409-410 belong to $\tilde{\mathcal{F}}_0$ if $\tilde{\mathcal{F}}_0$ is not known?
- Do the upper bounds in Equations (13) and (16) decay with the sample size $n$? If so, it would be good to comment and be explicit about how they decay with $n$ (i.e what is the rate of decay?). 
- In Equation (24), are the minimizations and maximizations over $f$ and $f^{\prime}$ being done both over $\mathcal{F}$? Or is the maximization of $f^{\prime}$ being done over $\tilde{F}_0$? If it is the latter, the same question I had above holds - how can the learner do this if $\tilde{F}_0$ is unknown?

### Questions
- Does Proposition 3.1 hold uniformly for all $x \in X$? If so, I am confused since $f \in \tilde{F_{0}}$ only guarantees that $f(x) \in [l_x, u_x]$ almost surely. So there could still be $x$'s (albeit in a measure $0$ set), for which this is not true. 
- What norm is being used on line 236?
- Is the guarantee on line 267 pointwise or in expectation? If it is pointwise for every $x$, how are you accounting for the fact that the functions $f \in \tilde{F_{\eta}}$ may have projection loss bigger than $\eta$ for low probability $x$? Is this accounted for by definition of $r_{\eta}(x)$ and $s_{\eta}(x)$? If so, it would be good to explain how the buffer $r_{\eta}(x)$ and $s_{\eta}(x)$ account for that. 
- Is $\tilde{F}_0$ known to the learner in Equation (23)? It seems like the learner needs to know the distribution $D$ over $X$ to compute $\tilde{F}_0$ based on line 170. So because the learner doesn't know $D$, it shouldn't be able to perform the optimization in Equation (23). What am I missing here?
- Based on the bullet points above, how does the learner know that the $f_1, ..., f_j$ in line 409-410 belong to $\tilde{\mathcal{F}}_0$ if $\tilde{\mathcal{F}}_0$ is not known?
- Do the upper bounds in Equations (13) and (16) decay with the sample size $n$? If so, it would be good to comment and be explicit about how they decay with $n$ (i.e what is the rate of decay?). 
- In Equation (24), are the minimizations and maximizations over $f$ and $f^{\prime}$ being done both over $\mathcal{F}$? Or is the maximization of $f^{\prime}$ being done over $\tilde{F}_0$? If it is the latter, the same question I had above holds - how can the learner do this if $\tilde{F}_0$ is unknown?

### Soundness
3

### Presentation
3

### Contribution
3
