# No Foundations without Foundations: Why semi-mechanistic models are essential for regulatory biology

- Decision: Reject
- Scores: 7, 7, 4

## Abstract
Despite substantial efforts, deep learning has not yet delivered a transformative impact on elucidating regulatory biology, particularly in the realm of predicting gene expression profiles. Here, we argue that genuine ``foundation models'' of regulatory biology will remain out of reach unless guided by frameworks that integrate mechanistic insight with principled experimental design. We present one such ground-up, semi-mechanistic framework that unifies perturbation-based experimental designs across both in vitro and in vivo CRISPR screens, accounting for differentiating and non-differentiating cellular systems. By revealing previously unrecognised assumptions in published machine learning methods, our approach clarifies links with popular techniques such as variational autoencoders and structural causal models. In practice, this framework suggests a modified loss function that we demonstrate can improve predictive performance, and further suggests an error analysis that informs batching strategies. Ultimately, since cellular regulation emerges from innumerable interactions amongst largely uncharted molecular components, we contend that systems-level understanding cannot be achieved through structural biology alone. Instead, we argue that real progress will require a first-principles perspective on how experiments capture biological phenomena, how data are generated, and how these processes can be reflected in more faithful modelling architectures.

## Human Reviews

## Human Reviewer 1

### Rating
7

### Rating Number
7

### Confidence
4

### Summary
The paper contends that efforts to build “foundation models” for gene-regulatory biology will fail unless they incorporate mechanistic knowledge rather than rely solely on ever-larger, purely data-driven architectures. It formalises this stance with a semi-mechanistic causal framework that links three experimental regimes—baseline growth, single-gene CRISPR perturbations, and combinatorial interventions—and derives modified loss terms that respect steady-state constraints and unperturbed-cell baselines. The authors show, on a public perturb-seq time-series dataset, that adding their mechanistic loss to a Neural ODE lowers test MSE and yields more stable parameter convergence than a vanilla end-to-end model. They discuss hidden assumptions in current practice (e.g., “cells don’t respond to media” and “perturbations map to unique attractors”) and propose concrete experimental-design guidelines, such as including untreated controls in every batch. The paper closes with a call for coordinated data collection and hybrid loss functions as the only plausible route to reliable regulatory-biology foundation models.

### Strengths
Clear, bold stance: “No foundations without foundations” crystallises why blindly scaling data-driven models is insufficient for regulatory biology.

Provides a unified mathematical framework that ties perturb-seq, batch effects, and dynamical systems into a single causal graph, exposing hidden assumptions in prior ML work.

Offers actionable items—modified loss terms, advice to include baseline controls per batch—and demonstrates a proof-of-principle Neural-ODE that improves test MSE on a real CRISPR dataset.

Thorough literature bridge: spans structural biology, causal ML, optimal-transport, and single-cell perturbation studies, positioning the work squarely in ongoing debates.

### Weaknesses
Empirical evidence is narrow (one dataset, one toy model); no cross-lab replication or other modalities (e.g., imaging, proteomics) tested.

Core assumptions—cells at baseline steady state, unique attractors—may not hold in primary or differentiating tissues, but diagnostic guidance is minimal.

Alternative data-efficient paths (e.g., active-learning exploration or self-supervised pre-training on multimodal atlases) are acknowledged yet not quantitatively compared.

### Questions
Have you tried the mechanistic loss on other modalities (imaging-based pooled screens or RNA + protein multi-omics) to test generality?

How would you validate the “no baseline response” assumption in heterogeneous primary tissues where steady state is unclear?

With limited resources, which lever yields the biggest benefit first: richer perturb-time series, improved batch design, or mechanistic loss terms—and why?

### Presentation
2

---

## Human Reviewer 2

### Rating
7

### Rating Number
7

### Confidence
4

### Summary
This paper critically examines the limitations of deep learning approaches in predicting gene expression profiles and introduces a novel semi-mechanistic modeling framework that unifies data from both in vitro and in vivo CRISPR screens. It reveals key implicit assumptions inherent in mainstream prediction methods, leading to the derivation of improved, more biologically grounded loss functions and optimized batching strategies. By explicitly integrating mechanistic insights with data-driven learning, this hybrid framework aims to more accurately capture the complexity of gene regulation. Furthermore, it provides a stronger theoretical foundation for building more reliable and biologically interpretable models of gene expression.

### Strengths
1.The paper introduces a novel semi-mechanistic framework that unifies mathematical formalisms for both in vitro and in vivo CRISPR perturbation screens across differentiating and non-differentiating cellular systems, addressing a critical gap in regulatory biology modeling.

2.It successfully diagnoses overlooked assumptions in existing machine learning methods, such as the implicit supposition that unedited cells exhibit no response to baseline media in non-differentiating models, thereby promoting algorithmic transparency.

3.The work delivers practical contributions, including a modified loss function enforcing steady-state dynamics and data-batching strategies grounded in error analysis, which demonstrably improve performance in neural ODE experiments.

### Weaknesses
1.The framework's applicability to in vivo systems remains inadequately substantiated, as validation relies solely on in vitro iPSC data despite claims of generalizability to physiological contexts.

2.Counterarguments advocating data-centric approaches are oversimplified, with insufficient engagement against paradigm-shifting successes like AlphaFold, which achieved breakthroughs without explicit mechanistic integration.

3.Scalability concerns arise from increased model complexity due to mechanistic components, yet the paper omits analysis of computational trade-offs or real-world deployment feasibility.

### Questions
1.Given the framework's assumption of instantaneous genetic perturbations, could the authors quantitatively evaluate how temporal delays in in vivo CRISPR delivery might compromise prediction accuracy in physiological environments?

2.In scenarios where biological mechanisms remain incompletely characterized, such as non-coding RNA regulation or epigenetic feedback loops, how does the semi-mechanistic approach prevent reverting to de facto black-box modeling while preserving its interpretability claims?

3.To translate experimental recommendations like time-series validation into practice, what specific incentives, collaborative frameworks, or data-sharing standards would the authors propose to align experimental biologists priorities with this methodology ’s requirements?

### Presentation
4

---

## Human Reviewer 3

### Rating
4

### Rating Number
4

### Confidence
2

### Summary
This paper presents the position that semi-mechanistic models are essential for regulatory biology. They lay out a strong theoretical framework detailing why this is the case, including mathematical formulations of their assumptions.

### Strengths
(S1) The paper presents a clear, logical argument for their position. I especially appreciate the approach of systematically explaining why scaling existing approaches are unlikely to succeed.

(S2) The paper makes an important contribution by explicitly articulating assumptions that are often hidden in ML models for biology. This systematic exposition of experimental design considerations (batch effects, measurement artifacts, etc.) is valuable. 

(S3) The paper is well-written and easy to follow. References are made where appropriate, and appear to be consistent with the statements they are supporting.

### Weaknesses
(W1) This paper almost reads like a submission that was intended as a technical submission and not as a position paper. It does a better job of describing a proposed regulatory biology foundation model than of presenting a forward-looking vision for a broader field/community.  

(W2) The significance of the position within the broader landscape of ML is not elaborated on, which limits the potential for discussion outside the specific field of regulatory biology, and the specific applications discussed.  

(W3) There is no discussion of societal significance or importance. Some inclusion of the intersection between the proposed position and societal impact would strengthen the work as a position paper as opposed to a modeling methodology paper.

### Questions
(Q1) What broader lessons does your framework offer for ML applied to other complex biological systems beyond regulatory biology?
(Q2) Given that you've identified why current approaches fail, what concrete next steps should the community take?

### Presentation
3
