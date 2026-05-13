# Identifiable Exchangeable Mechanisms for Causal Structure and Representation Learning

- Decision: Accept
- Scores: 6, 5, 6, 8, 8, 6

## Abstract
Identifying latent representations or causal structures is important for good generalization and downstream task performance. However, both fields have been developed rather independently. We observe that several methods in both representation and causal structure learning rely on the same 
data-generating process (DGP), namely, exchangeable but not i.i.d.\ (independent and identically distributed) data. We provide a unified framework, termed Identifiable Exchangeable Mechanisms (IEM), for representation and structure learning under the lens of exchangeability. IEM provides new insights that let us relax the necessary conditions for causal structure identification in exchangeable non--i.i.d.\ data.
We also demonstrate the existence of a duality condition in identifiable representation learning, leading to new identifiability results.
We hope this work will pave the way for further research in causal representation learning.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper introduces Identifiable Exchangeable Mechanisms (IEM), a general framework that unifies causal discovery (CD), independent component analysis (ICA), and causal representation learning (CRL). The IEM model relies on the exchangeable data (e.g., data from multiple environments), and generalizes the Causal de Finetti theorem. The authors showed, that some assumptions required by CD, ICA, and CRL are special cases of the proposed IEM model.

### Strengths
The introduced framework provides a unifying perspective on several multi-environment causal inference tasks: CD, ICA, and CRL.  The paper is well-structured and clearly written. I appreciate a broad Discussion and future directions section.

### Weaknesses
In my opinion, the major weakness of the paper is the lack of empirical evaluation or case studies for each of the mentioned settings (Sec 3.2, 3.3, 3.4). I encourage the authors to provide at least one synthetic/real-world dataset, where the IEM is applied in all three settings. I understand, that the main contribution of the paper is theoretic, but a case study can provide some applied insights, e.g., how degrees of non-i.i.d. in data facilitate a causal inference task at hand.  

I am happy to raise my score, if this weakness is addressed during the rebuttal.

### Questions
- Does the proposed framework generalize to a setting where we allow for hidden confounds between causal variables?
- There seems to be an issue with the notation in Eq. 6?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces the Identifiable Exchangeable Mechanisms (IEM) framework, which unifies key methods in causal structure discovery, Independent Component Analysis (ICA), and causal representation learning within a single probabilistic graphical model. The authors use the IEM framework to generalize the Causal de Finetti theorem, relaxing the necessary conditions for causal structure identification in exchangeable data. They introduce new conditions termed "cause and mechanism variability" and provide novel identification results.

### Strengths
1. The paper effectively bridges the relatively different identifiable methods of causal structure identification and representation learning by introducing the IEM framework. This framework offers a novel, theoretically grounded perspective that could be influential for identifying latent structures and causal mechanisms.
2. By generalizing the Causal de Finetti theorem, the authors relax traditional assumptions and derive new identification conditions for causal structures.

### Weaknesses
Although the theoretical contribution is rigorous, some experiments are still needed to evaluate the effectiveness of the proposed IEM framework.

### Questions
See above.

### Soundness
3

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
2

### Summary
From the perspective of IEM, the paper uses the identifiable exchangeable mechanisms framework that unifies causal discovery, independent component analysis and causal representation learning. The authors further shows how exchangeability can model out-of-distribution and interventional distribution.

### Strengths
The paper provides an analysis of causal discovery, independent component analysis and causal representation learning through the framework of IEM, Providing theoretical connections among these methods. This provides researchers deeper understanding of the assumptions and inter-connections among these methods.

### Weaknesses
1. The arguments in section 3 seem to be loosely connected, and not enough time was spent tying these sections together. I would expect more detail in explaining how this framework can benefit the development of these fields. Section 4 briefly discusses how the framework could be used to unify research in CD, ICA, and CRL but then shifts to discussing OOD and interventional distributions. A more in-depth discussion on the connections among these fields and how advancements in one field could benefit others would be beneficial.

2. Despite the strong theoretical elements in the paper, it lacks specific examples. In the case studies for each subsection, it would be better if the authors could provide examples or counterexamples, along with a more detailed discussion of these examples/test cases, so that readers can gain a clearer understanding.

### Questions
Could you elaborate more on the framework of IEM and the exchangeability of data? Specifically, could you explain, with examples, the physical intuition behind exchangeable sequences? Moreover, the variable $Z$ is referred to multiple times as a causal variable. Is there a rigorous definition of this variable, and how can a variable contain cause-effect relationships?

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper “Identifiable Exchangeable Mechanisms for Causal Structure and Representation Learning” proposes the Identifiable Exchangeable Mechanisms (IEM) framework to unify causal discovery (CD), Independent Component Analysis (ICA), and Causal Representation Learning (CRL) in the context of exchangeable data. This framework generalizes the Causal de Finetti theorem (Guo et al., 2022) by introducing relaxed identifiability conditions called cause and mechanism variability. These new conditions aim to enable causal structure identification across non-i.i.d. datasets, thus extending traditional causal inference to handle multi-environment data. The authors theoretically derive and discuss these conditions and provide conceptual examples to illustrate the IEM framework's utility.

### Strengths
The IEM framework proposed in this paper provides a novel theoretical contribution by unifying causal discovery, ICA, and CRL using exchangeability and probabilistic graphical models. The introduction of cause and mechanism variability as identifiability conditions broadens the applicability of causal inference to non-i.i.d. data. This relaxation of traditional i.i.d. assumptions aligns well with current trends in causality research, which increasingly focus on real-world, structured data that deviate from idealized assumptions, thus contributing to the field's practical impact.

### Weaknesses
1.	The paper lacks empirical validation on either synthetic or real-world datasets. Given that the IEM framework is proposed as a practical tool for identifying causal structures in multi-environment data, empirical tests on structured datasets would significantly bolster its practical relevance and demonstrate its utility across different applications.

2.	While theoretically motivated, the cause and mechanism variability assumptions remain abstract, and their practical applicability may be challenging for readers to conceptualize. Including concrete, real-world examples to illustrate where these assumptions hold would enhance the understanding of the framework's assumptions in practical scenarios.

3.	Although the IEM framework aims to unify CD, ICA, and CRL, the paper lacks a direct comparative analysis to benchmark IEM against established methods within these areas. A comparative discussion, even theoretical, could better highlight IEM’s unique contributions and clarify where it stands relative to traditional ICA, causal discovery, or representation learning methods.

### Questions
1.	I suggest that the authors provide specific, real-world scenarios where the assumptions of cause and mechanism variability would hold, to help contextualize these conditions.

2.	Has the framework been considered for use on any real-world datasets, such as those in biology or social sciences, to evaluate its generalization and robustness in non-idealized data?

3.	Are there foreseeable extensions of IEM to structured but non-exchangeable data (such as time series), which would broaden its applicability further?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This work introduces a unified framework that formulates causal mechanisms and causes through a new class of identifiable exchangeable mechanisms, addressing the identifiability of latent noise variables, latent causal variables z, and the latent structure among z. This framework centers on two key sources of variability—cause variability and mechanism variability. By analyzing these variabilities, this work provides a rigorous approach to identifying both latent noise/causal variables and the latent structure among these causal variables.

### Strengths
1) This work addresses a challenging problem in causal representation learning, namely identifiability analysis.

2) The proposed framework is novel and provides a valuable perspective for examining the relationship between cause variability, mechanism variability, and the identifiability of latent noise, latent causal variables, and the associated causal structure.

3) TCL is a very elegant and simple framework for nonlinear ICA. The analysis connecting identifiable exchangeable mechanisms to temporal contrastive learning (TCL) is insightful. Notably, this work introduces a novel approach to identify latent noise variables by analyzing changes in the mixing mapping from latents to observed data, distinguishing it from traditional nonlinear ICA, which typically relies on changes in the distributions of latents.

4) Many insights from this work are likely to be highly significant for advancing our understanding of causal representation learning.

### Weaknesses
Overall, this work is highly interesting and provides valuable insights that advance our understanding of causal representation learning. The proposed framework is novel, and its discussion on identifiability offers a fresh perspective on key challenges in the field. I appreciate the significant insights presented, which have the potential to drive progress in this area. Below, I outline some concerns to discuss with the authors:

1) In general, for causal discovery in multi-domain data, the causal structure can be identified using the principle of Independent Causal Mechanisms (ICM). Specifically, in the causal direction, the parameters of the causal mechanism tend to be independent, whereas in the reverse direction, these parameters show dependency. Thus, ICM can be used to determine causal direction (see [1,2]). Furthermore, if latent causal variables can be identified by leveraging both cause variability and mechanism variability, then the causal structure should also become evident. Given this, is it necessary to discuss causal structure separately once latent causal variables have been identified? This also suggests a possible connection between the conditions required to identify latent causal variables and those needed to identify causal structure.

2) I find the concept of the duality between cause and mechanism variability in TCL fascinating. It's particularly interesting to consider changes in the mixing mapping rather than changes in the distribution of latent variables. Are there any insights into real-world applications for this setting?

3) Equations (11) for CauCA and (5) for Liu et al., 2024 represent two distinct yet crucial conditions for identifiability, both relying on sufficient changes along the edges. Are there any new insights from the framework of identifiable exchangeable mechanisms that could shed light on these different formulations of edge changes? (Note that CauCA does not guarantee identifiability of the exogenous variables.)

a. In line 78, 'GCL' is introduced for the first time; please expand the acronym upon its first mention.

b. In line 95, two different mappings, specifically from s to o and from z to o, are defined using the same function f. It may be clearer to use distinct notation for these mappings.

c. Please ensure consistency in the notation for \psi in Equation (3) and in line 131.

d. \theat^{g}_{i0} has not been defined.

e. In Equation (6), the term p(y∣???) needs clarification.

### Questions
See above

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 6

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces a novel framework called Identifiable Exchangeable Mechanisms (IEM). IEM aims to unify approaches in Causal Discovery (CD), Independent Component Analysis (ICA), and Causal Representation Learning (CRL) for identifying causal structures and learning representations. By extending the Causal de Finetti (CdF) theorem, IEM introduces the concepts of "cause variability" and "mechanism variability." This framework relaxes the assumption of independent and identically distributed (i.i.d.) data, allowing for causal structure and representation identification under broader conditions. Additionally, it establishes a new duality in ICA techniques, incorporating Time-Contrastive Learning (TCL) and other auxiliary variables.

### Strengths
The IEM framework, which extends the CdF theorem to provide a theoretical foundation for identifying causal structures based on exchangeable data, is a significant contribution bridging the fields of causal inference and representation learning. By unifying Causal Discovery (CD), Independent Component Analysis (ICA), and Causal Representation Learning (CRL) within a cohesive framework, it offers a straightforward and intuitively convincing approach. This paper is expected to play an essential role, particularly as causal representation learning continues to advance.

### Weaknesses
The paper attempts to present a wide range of theories within a limited space, which results in a somewhat abstract discussion. While readers well-versed in causal discovery might follow its value, those less familiar with the area may struggle to appreciate the paper’s contributions fully. Although it may be challenging, adding concrete examples to illustrate the unification of CD, ICA, and CRL would likely make the framework’s significance clearer and broaden its appeal.

Additionally, a few minor issues are noticeable:

- In line 107, "tequence's" appears to be a typo and should be "sequence's."
- In Equation (6), $p(y^i|^i)$ might be missing the term $\psi$.
- In the first sentence of Theorem 2, there is a misplaced bracket (]).

### Questions
Would it be possible to illustrate the significance of this paper with concrete examples?

### Soundness
4

### Presentation
3

### Contribution
4
