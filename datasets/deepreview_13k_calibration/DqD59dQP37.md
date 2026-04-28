# Causal Fairness under Unobserved Confounding: A Neural Sensitivity Framework

- Decision: Accept
- Avg Score: 5.67
- Scores: 6, 6, 5

## Abstract
Fairness of machine learning predictions is widely required in practice for legal, ethical, and societal reasons. Existing work typically focuses on settings without unobserved confounding, even though unobserved confounding can lead to severe violations of causal fairness and, thus, unfair predictions. In this work, we analyze the sensitivity of causal fairness to unobserved confounding. Our contributions are three-fold. First, we derive bounds for causal fairness metrics under different sources of unobserved confounding. This enables practitioners to examine the sensitivity of their machine learning models to unobserved confounding in fairness-critical applications. Second, we propose a novel neural framework for learning fair predictions, which allows us to offer worst-case guarantees of the extent to which causal fairness can be violated due to unobserved confounding. Third, we demonstrate the effectiveness of our framework in a series of experiments, including a real-world case study about predicting prison sentences. To the best of our knowledge, ours is the first work to study causal fairness under unobserved confounding. To this end, our work is of direct practical value as a refutation strategy to ensure the fairness of predictions in high-stakes applications.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper integrates a recent framework for sensitivity analysis within a common causal fairness family.

### Strengths
The paper is nicely laid out and mostly easy to follow. The problem is important, as sensitivity analysis plays a substantive role in a variety of causal estimands. End-to-end learning to produce fair classifiers is presented, illustrating that sensitivity analysis doesn't need to take place just for standard causal estimands such as average causal effect.

### Weaknesses
May main comment is to what extent this mostly is a direct application of Frauen et al. (2023). If I understood it well, is the main technical innovation the use of Lemma 1 in the context of GMSM? Or is this even more closely related to the cited paper?

I’m confused by Eq. (11): there is an expectation over $Y$. Why is this form of aggregation sensible? I’d expect that we would like to enforce the constraint uniformly over all possible values in the same sample space of $Y$ instead of  performing any sort of probabilistic averaging. Speaking of which, which distribution are we marginalizing over, is this the marginal distribution of $Y$? What happens to $a_i$, $a_j$ from (1)-(3)?

Maybe this is well-explored in the causal fairness literature, but the switch between “real Y” and $f_\theta$ in the training procedure in Section 5 is very confusing: we design $f$, so any confounding between “$Y$ “ (that is, $f_\theta$) vanishes by design. Why would we consider any sort of sensitivity parameter for “$Y$”?

I’m worried about the theoretical results. In Appendix D.3 the authors state that they “extensively use the following corollary”, which boils down to Eq. (33). This equation refers to “$P(X |do(A=a), A\neq a)$”. The event past the conditioning bar has probability zero, as the control signal $do(A = a)$ implies $A = a$ (yes, we can condition on measure-zero events, that’s what we do for continuous variables, but even then we take for granted the careful textbook measure-theoretical characterization of this conditional that we implicitly accept by default, but that’s a non-trivial (and not unique!) characterization of conditioning. But  (33) doesn’t appear to make sense even for discrete $A$). I may be missing something obvious, in which case I will appreciate a clarification – if this indeed “follows directly from basic probability theory” I’m happy to be taught the baby steps explicitly…  Of course we can say that 

$$P(X | do(A = a)) = P(X(a)) = P(X(a) | A = a)P(A = a) + P(X(a) | A \neq a)P(A \neq a) = $$
$$P(X | A = a)P(A = a) + P(X(a) | A \neq a)P(A \neq a) , $$

but $P(X(a) | A \neq a)$ is not the same thing as $P(X | do(A = a), A \neq a)$. Among other things, $X$ is not $X(a)$ when $A \neq a$, but it is undefined what $X$ even means under regime $do(A = a)$ and event $A \neq a$.

### Questions
This is. summary of the above.

- What is the novelty?

- Why averaging over $Y$ in Eq. (11) makes sense (and which distribution are we averaging over)?

- Is there any point in prescribing sensitivity analysis between $Y$ and $A$, given that $Y$ is not involved in the prediction?

- Explaining better the meaning of Eq. (33) and where it is used.

I would also would like to know whether any path-specific effect could be tackled and not only the three default ones.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper establishes the partial identification bound for causal fairness under GMSM, which can be used for learning causally fair predictors under specified GMSM and SCM. Authors provide theoretical guarantee for the partial identification bound and demonstrate its benefit using synthetic and real-world data.

### Strengths
I find the paper interesting and easy to read. It establishes the partial identification bound for causal fairness under GMSM, which can be used for learning causally fair predictors under specified GMSM and SCM. 

I believe the problem studied is important and has important practical value and the paper is theoretically sound and made a step toward better estimation of causal fairness.

### Weaknesses
The motivation and solution seem disconnected. Authors suggest practitioners can audit the unobserved confounding in the data in the introduction, but the solution using GMSM requires prior knowledge of UC strength. In this case, we need to know the unobserved confounding strength in order to estimate or optimize the causal fairness. It is unclear how the proposed 'auditing' process would work in practice when the true level of unobserved confounding is unknown. The authors should clarify what specific insights this auditing process provides and how it aids in real-world scenarios where the unobserved confounding is not directly measurable.

The novelty is relatively low. The causal fairness and the partial identification bound under MSM/GMSM is extensively studied, the paper simply combined them. The paper does not sufficiently demonstrate that the combination of these concepts leads to a non-trivial result. The authors need to more clearly articulate the specific challenges in combining these concepts and why existing methods cannot be directly applied to this problem.

Authors did not report accuracy measures in the paper, which should also be reported. I assume such fairness constraint would impact the prediction accuracy a lot. The lack of accuracy metrics makes it difficult to assess the practical trade-offs between fairness and prediction performance. The authors should include a comprehensive analysis of the impact of their fairness constraints on prediction accuracy, including specific metrics and visualizations.

A natural criticism is the method is restricted to discrete features, while in practice, variables like crime history may be highly contextual (videos, images, text, ..) . Can authors discuss the difficulty in extending it to high dimensional features? The current restriction to discrete features limits the applicability of the method to real-world problems involving complex, high-dimensional data. The authors should address the challenges in extending their method to handle continuous and high-dimensional features, and discuss potential approaches for overcoming these limitations.

Can authors explain more on "Fairness bounds in non-identifiable settings": why general non-identifiability in these papers does not encompass the unobserved confounding case? Nabi & Shpitser, 2018 also uses unobserved confounding as one of the examples.

Typo: abstract, sources of unobserved confounding? "ours is the first work to study causal fairness under observed confounding." miss-specification.

Writing: Why repeat the contribution at the end of section 1. The research gap seems to repeat contribution again and such gap is already mentioned before.

### Questions
See weakness.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper delves into the sensitivity analysis of causal fairness criteria, specifically focusing on counterfactual direct effect (Ctf-DE), indirect effect (Ctf-IE), and spurious effects concerning unobserved confounding. The authors establish bounds for these measures by utilizing the generalized marginal sensitivity model (GMSM) and present a model for learning fair predictions. Experimental results underscore the method's effectiveness to some extent.

### Strengths
- The sensitivity analysis on unobserved confounders on causal fairness criterion is a relevant and important research problem.

- The experiments on synthetic data and real data demonstrate the effectiveness of the proposed method at some extent.

### Weaknesses
 - Limited Contribution and Novelty. The contribution and novelty of this paper may be limited. The theorem presented in the paper, Theorem 1, appears to be a specific application of the Generalized Marginal Sensitivity Model (GMSM) introduced by Frauen et al. (2023), which offers a comprehensive framework for causal sensitivity analysis under unobserved confounding in various settings. It would be beneficial to clarify the distinct contributions and challenges of this work compared to Frauen et al. (2023).

- Limited Scope in Fairness Notions. The paper is somewhat misleading in its claim to perform sensitivity analysis on causal fairness under unobserved confounding. In fact, the focus of this paper is confined to specific causality-based fairness notions based on counterfactual direct effect (Ctf-DE), indirect effect (Ctf-IE) and spurious effects. However, causal fairness encompasses a broader range of notions, such as ones based on proxy discrimination, path-specific causal effects, path-specific counterfactual effects (including natural direct or indirect causal effect), etc. Additionally, it is misunderstanding to call the definitions Ctf-DE, Ctf-IE and Ctf-SE in Zhang & Bareinboim (2018a) as ‘path-specific causal effects’, which differs from their formal definition [1], thus leading to confusion.

- Incomplete Literature Review. The paper lacks a comprehensive review of prior literature on sensitivity analysis on causal effects to unobserved confounding, such as marginal sensitivity model. Additionally, it would be beneficial to provide a brief overview of sensitivity analysis models, including the GMSM, and discuss their strengths and weaknesses.

- Enhanced Experimental Analysis. In the experimental section, it would be advantageous to report and compare prediction performance across various models under different levels of confounding. This would provide a more robust assessment of the proposed method's performance.

- Handling Continuous Variables. The paper assumes that the variables Z and M are discrete, yet many real-world variables are continuous. Therefore, it is essential to discuss how the proposed method can be extended to accommodate continuous variables.

### Questions
The authors state that "A key benefit of the GMSM is that it can deal with discrete mediators and both discrete and continuous outcomes." It is not convincing. It would be helpful to elaborate on other reasons for adopting the GMSM and discuss the strengths and weaknesses of alternative sensitivity models.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair
