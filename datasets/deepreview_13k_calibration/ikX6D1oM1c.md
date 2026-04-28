# A Neural Framework for Generalized Causal Sensitivity Analysis

- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 8, 6, 6

## Abstract
Unobserved confounding is common in many applications, making causal inference from observational data challenging. As a remedy, \emph{causal sensitivity analysis} is an important tool to draw causal conclusions under unobserved confounding with mathematical guarantees. In this paper, we propose \frameworkname, a neural framework for \emph{generalized} causal sensitivity analysis. Unlike previous work, our framework is compatible with (i)~a large class of sensitivity models, including the marginal sensitivity model, $f$-sensitivity models, and Rosenbaum's sensitivity model; (ii)~different treatment types (i.e., binary and continuous); and (iii)~different causal queries, including (conditional) average treatment effects and simultaneous effects on multiple outcomes. The generality of \frameworkname is achieved by learning a latent distribution shift corresponding to a treatment intervention using two conditional normalizing flows. We provide theoretical guarantees that \frameworkname can infer valid bounds on the causal query of interest and also demonstrate this empirically using both simulated and real-world data.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors provide a framework for generalized causal sensitivity analysis, an approach that subsumes three previous methods and provides additional advantages.

### Strengths
The key advantage of the authors' approach (according to the authors) is that it is much more widely applicable than any other single approach (which typically focus on a specific sensitivity model, treatment type, and causal query).

The paper is well-written, and it provides substantial background about existing methods for causal sensitivity analysis.

The experiments appear consistent with the existing literature, well-motivated, and useful.

### Weaknesses
The generality of the approach appears to come at a substantial cost in terms of complexity (with a corresponding potential for unexpected sources of error, bias, or misspecification). The single advantage over MSM appears to be allowing causal queries with multiple outcomes.

It is unclear the extent to which alternative (non-neural) implementations of the GTSM are possible. The paper would be improved by clearly describing what advantages the neural implementation provides over alternatives.

It seems somewhat odd to cite D'Amour 2019 (an excellent paper about a very specific topic) for the idea that "unobserved confounding often renders causal inference challenging." That has been known for more 50 years, going back at least to Reichenbach's common cause principle.

### Questions
Are alternative (non-neural) implementations of the GTSM possible? What advantages does the neural implementation provides over alternatives? How does the complexity (e.g., number of hyper-parameters and other implementation choices) of NeuralCSA compare to MSM?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes NeuralCSA, a framework for performing causal sensitivity analysis, i.e., partially identification of a causal functional under assumptions on the unmeasured confounders. They propose a 2-stage training procedure, modeling the latent distributions using normalizing flows.

### Strengths
- The paper overall is well-written and easy to understand. I found the motivation and setup to be clear. I also appreciated comparisons to existing sensitivity models.
- The GTSM framework subsumes many of the existing sensitivity models and thus is more generally applicable. In principle, the framework also applies to arbitrary functionals (e.g., quantiles) of the interventional outcome distributions.
- The clarity of the two-stage procedure can be improved (see Weaknesses section), but overall, the procedure is simple and easy to follow. It is also nicely motivated using Theorem 1.

### Weaknesses
 - I found Sec 5.1 and 5.2 difficult to read and I think clarity can be improved. What confused me initially was that you suggest fixing $P^*(U|x, a)$ but then the $\sup$ in Eq. 5 is also over the distributions $p(u|x, A)$. Reading it further, the sup is only for $A \neq a$ but I think clarifying that you only fix for the treatment $a$ that enters into $Q$ would be useful. Maybe this is obvious, but it will still make it easier to understand what is being optimized over in the $\sup$.
- It would also be nice to have some intuition of the proof of Theorem 1. Also, the invertible function $f^*$ would depend on the fixed $P^*$. Does certain distributions $P^*$ make it easier to determine $f^*$. In practice, how should you determine which $P^*$ to fix?

### Questions
See weaknesses section.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a generalized sensitivity analysis framework that is compatible with many different sensitivity models, including the marginal sensitivity model, f-sensitivity model, and Rosenbaum's sensitivity model. The framework is suitable for different treatment types and different causal queries. The authors propose to learn the latent distribution shift with two separately trained conditional normalizing flows.

### Strengths
- The concise summary of sensitivity models enhances the paper's readability and flow.
- The authors introduce a novel learning strategy to model the latent distribution.
- Experiments with both synthetic and real-world data are used to demonstrate the validity and effectiveness of the proposed method.

### Weaknesses
 - It is not very obvious how does the bounds the proposed framework compares with some existing works such as GMSM. 
- The section 5.1 might be a little hard to follow. Please find some questions I have below.

- Regarding the color coding in equation (4), does it indicate the parameters for the optimization problem? Does the right supremum also maximize over $P(U|x,a)$?
- I'm not fully understand the two-stage procedure. Could you to provide a more detailed explanation about replace the right supremum with 
 fixed of $\mathbb{P}^*(U|x,a)$ and $\mathbb{P}^*(Y|x,u,a)$?
- In relation to the optimization problem presented in equation (5), are there specific constraints placed on the functional $\mathcal{D}_{x,a}$ to ensure that the global optimal can be achieved?

### Questions
- Regarding the color coding in equation (4), does it indicate the parameters for the optimization problem? Does the right supremum also maximize over $P(U|x,a)$?
- I'm not fully understand the two-stage procedure. Could you to provide a more detailed explanation about replace the right supremum with 
 fixed of $\mathbb{P}^*(U|x,a)$ and $\mathbb{P}^*(Y|x,u,a)$?
- In relation to the optimization problem presented in equation (5), are there specific constraints placed on the functional $\mathcal{D}_{x,a}$ to ensure that the global optimal can be achieved?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a neural framework for generalized causal sensitivity analysis that aims to achieve lower and upper bounds for some causal queries when exact identification is not possible due to unobserved confounding. Specifically, the framework leverages two normalizing flows to encode the latent distributions that are compatible with the observed ones and optimize the causal quantities of interest and can be used to approximate previous sensitivity analysis models.

### Strengths
1. The writing is clear, and the paper is easy to follow.
2. The proposed neural network-based causal sensitivity analysis method is effective and general, which is compatible with previous studies like MSM and f-sensitivity models and can be easily extended to other models by modifying the constraints that specify the strength of unobserved confounding.

### Weaknesses
The experiments, to some extent, appear to be lacking in comprehensiveness. The semi-synthetic datasets utilized in this study are exclusively derived from the MIMIC-III dataset. The findings derived from this single source may not offer an adequate illustration of the model's performance.

I noticed that the authors apply the augmented Lagrangian method to incorporate the sensitivity constraints in the optimization process. I wonder to what extent could the constraints be satisfied since the constraint now becomes a soft one that may well be violated. It is possible that the effective constraint parameter $\Gamma$ achieved by the optimization significantly deviates from the intended value, which may make the final bounds less useful. Additionally, I am concerned about the stability of training the normalizing flows, as instability in this aspect could further exacerbate the situation.

### Questions
I noticed that the authors apply the augmented Lagrangian method to incorporate the sensitivity constraints in the optimization process. I wonder to what extent could the constraints be satisfied since the constraint now becomes a soft one that may well be violated. It is possible that the effective constraint parameter $\Gamma$ achieved by the optimization significantly deviates from the intended value, which may make the final bounds less useful. Additionally, I am concerned about the stability of training the normalizing flows, as instability in this aspect could further exacerbate the situation.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good
