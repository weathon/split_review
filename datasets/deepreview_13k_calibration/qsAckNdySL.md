# Causality is Invariance Across Heterogeneous Units

- Decision: Reject
- Avg Score: 4.25
- Scores: 3, 6, 5, 3

## Abstract
Learning a model from data for the three layers of Pearl Causal Hierarchy (PCH) (i.e., the associational, the interventional, and the counterfactual) is a central task in contemporary causal inference research, and it becomes particularly challenging for counterfactual queries. The prevailing scientific understanding is anchored in the three-step counterfactual algorithm (i.e., abduction, action, and prediction) proposed by Judea Pearl, which he considers is one of his most pivotal contributions. While this algorithm offers a theoretical solution, the absence of complete knowledge on structural causal models (SCMs) renders it highly impractical in most scenarios. To tackle the tasks of PCH, this paper introduces the DiscoModel, grounded in the core principle that "Causality is invariance across heterogeneous units." The underlying causal modeling theory of our model is \textit{Distribution-consistency Structural Causal Models} (DiscoSCMs), which extends both \textit{structural causal models} and the potential outcome framework. The former infers the selection variable on heterogeneous units, while the latter encapsulates the invariant causal relationship. DiscoModel exhibits remarkable capability for all the three layers of PCH simultaneously, providing practical and reasonable answers to important counterfactual questions (e.g., ``For a user on a certain internet platform observed with high subsidy and high retention, what if this user had not received a high subsidy in the past? Would there still be high retention now?''). To the best of our knowledge, DiscoModel is the first to provide non-trivial answers to such queries, substantiated through experiments on both simulated and real-world data.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper studies the problem of predicting potential outcomes. The model assumption is that the target is independent of the features given the treatment and a hidden variable called the unit variable. A neural network structure is proposed to learn a causal representation of the unit variable. While identifiability guarantees for the causal representation are absent.

### Strengths
A novel neural network structure is proposed for learning causal representations.

### Weaknesses
1. The model assumption is that $Y$ is independent of $X$ given $T$ and some unobserved $U$. The main idea of the method is to learn a representation for $U$ (denoted as Z) and then use $(Z, T)$ to predict $Y$. The idea is simple but the description in Section 2.1 only makes the method sound complicated. 

2. The causal representation $z_{S(e)}$ is not formally defined in the population case. How is it related to Equations (2)-(4)? This should be explained in detail.

3. There are no identifiability results regarding the causal representations $z_{S(e)}$.

4. Plenty of other notations are not formally defined. e.g., $Y_{u}(t)$, $S(e)$.  Also, what is the relation between $U$ and $S$?

### Questions
I think the main problems of the paper are the writing and the lack of identifiability results. 

I may raise my score depending on the response.

### Soundness
2 fair

### Presentation
1 poor

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
The "Disco" (distribution consistency) framework is presented in which, for each unit, the consistency assumption is satisfied not deterministically, but only in law. A counterfactual model is developed along the lines of the famous three-step method for evaluation, consisting of two separate neural networks, one for the selection variable and the second for the causal mechanisms. Simulation studies showing and comparing efficacy are done, one on generated data and another one on real personalized incentives data.

### Strengths
The setting and problem are interesting, and the approach is mostly new to my knowledge. It's an advantage that the model can handle counterfactuals natively.

I think using neural networks in a way that can handle counterfactuals is quite novel.

### Weaknesses
The way of modeling unit heterogeneity here is interesting but the ultimate contribution to the conceptual side may not be too big. It is possible to model the same thing within the SCM framework simply by adding more exogenous variables to the main one {U} that represents the choice of individual. For instance new independent variables U' for the different units would allow modeling the same effects as achieved in the Disco framework.



### Questions
The running example does not seem to make sense. It says a user is observed with a high subsidy and high retention, and asks "were they given a low subsidy, what would be their retention?" It's claimed that consistency implies the retention would also be high, but consistency implies nothing about this scenario, since the intervention of giving a low subsidy is not the same as what was observed (a high subsidy). In the referenced paper (Gong 2023) the example is stated correctly, as "were they again given a high subsidy, what would be their retention?"

Minor comments:
- Abstract: "considers is one of his" -> "considers as one of his"
- Section 5.1: "when lack complete knowledge" -> "when lacking complete knowledge"
- "reducible pocket" on pg. 9: I don't understand the metaphor, why is that like a pocket?

### Soundness
3 good

### Presentation
3 good

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
The Pearl Causal Hierarchy (PCH) delineates three layers for understanding causality: associational, interventional, and counterfactual, with the counterfactual being the most demanding. Pearl's three-step counterfactual algorithm offers a theoretical approach but is often impractical due to incomplete knowledge of the underlying structural causal models. The paper introduces the so-called DiscoModel, based on the belief that "Causality is invariance across heterogeneous units," and its underlying theory is the Distribution-consistency Structural Causal Models (DiscoSCMs), which is reviewed in the Appendix of the manuscript. The authors claim that the DiscoModel can effectively address all three PCH layers and is the first to provide concrete answers to complex counterfactual questions, as shown through experiments.

### Strengths
What the paper proposes is a valid and important contribution to causal reasoning, which is especially true about the underlying DiscoSCM. DiscoModel presents several strengths.

It can be claimed that it is a novel approach to causality, which treats causality as invariance across heterogeneous units. This inherent flexibility in treating heterogeneous units is both novel and relevant.

It introduces ActionNet,  a new mechanism to compute parameters for the outcome variable. By taking heterogeneous unit representation as input, it offers a level of granularity that may be missing in other models.

Unlike traditional causal modeling frameworks, which often make consistent predictions based on a consistency rule, DiscoSCM can predict outcomes with varied probabilities, acknowledging the idea that decisions often occur under circumstances where chance cannot be controlled. 

DiscoModel is claimed to be able to provide practical and reasonable estimations across the three layers of valuations. This broad spectrum applicability enhances its utility in diverse scenarios.  DiscoModel allows for heterogeneous counterfactual estimation across units. Notably, as per the authors, this hadn't been reached by any prior work.

### Weaknesses
The main weakness of the paper is that it is very poorly written. There are notation issues that hinder the precise understanding of what is being proposed. For instance, the use of 'u' to represent both an individual unit and an exogenous variable is confusing and leads to ambiguity in the mathematical formulations. Furthermore, it is essentially impossible to understand the proposed DiscoModel, without understanding DiscoSCM, which is briefly described in the Appendix, However, this description is also not very clear, mainly due to poor choices of notation. The description of the core concepts, such as the unit causal representation assumption, is not explicitly stated, making it difficult to assess the validity of the approach. It is also not clear what DiscoSCM offers in addition to the classical do-calculus of Pearl. The paper lacks a rigorous explanation of how the proposed ActionNet computes parameters for the outcome variable, and the connection between the heterogeneous unit representation and the final outcome is not clearly established. The derivations of key equations, such as Equations (2) and (8), are not sufficiently detailed, making it hard to follow the mathematical reasoning.

### Questions
No questions.

### Soundness
2 fair

### Presentation
1 poor

### Contribution
3 good

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors

### Strengths
I like the general theme of trying to get at the estimation of counterfactual predictions by insisting on invariance across heterogeneity and using a specific neural network structure to accomplish this. This is an important topic, and the authors have added to the discussion here.

### Weaknesses
1.  The abstract could helpfully be rewritten to indicate just what is being proposed in this paper. It’s a bit unfocused.
2.  There is some history in the literature for identifying invariant causal modules as a way of understanding what causality means, especially for large causal systems and in the context of neural networks interpreted causally. This literature should be identified and reviewed, and the current proposal placed in that context in a precise way. A Google Scholar search should identify relevant papers.
3.  The idea of estimating counterfactual predictions is also not new. Again, the literature on that enterprise should be reviewed, and the current proposal situated in this larger literature.
4.  On p. 3, the proposal of representing discrete models using degenerate Gaussian distributions is entertained. A paper from several years ago elaborates this idea in the context of CSL: Andrews et al. Learning high-dimensional directed acyclic graphs with mixed data-types. In The 2019 ACM SIGKDD Workshop on Causal Discovery (pp. 4-21). PMLR. Perhaps this and other such papers should be cited here.
5.  I agree that an empirical example was required for this paper, though not including any results from these experiments in the main text, I believe, was an unforced error for this conference.
6.  I found Section 5.1 to be somewhat unfocused; if these are considerations that need to be discussed, perhaps they could be discussed earlier on in a more focused way.

### Questions
1. What is the range of literature against which this paper is written? Has this range been taken cognizance of in the writing of this paper? (I couldn't tell.)

2. For someone who doesn't read the supplement, what conclusions are we to draw from the empirical investigations? No actual results are given in the main text.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
