# Position: Evaluations Should Acknowledge Model Multifacetedness in the Era of Large Language Models

- Decision: Reject
- Scores: 3, 3, 4

## Abstract
The rapid evolution of Artificial Intelligence (AI), particularly Large Language Models (LLMs), marks a significant departure from earlier machine learning (ML) paradigms. This advancement has exposed critical misconceptions in our understanding of the "model" itself, especially evident in evaluation methodologies that often rely on narrow observational windows to assess overall model quality. 
This paper argues that a fundamental reconceptualization of the "model" itself is necessary to address this evaluative crisis. We introduce a five-tiered hierarchical framework. Specifically, we divide models into: Noumenal, Conceptual, Instantiated, Reachable, and Observable ones. Using this framework, we examine the historical development of how models have been conceptualized and evaluated within the ML field, analyzing the roles of experiments, ablation studies, and datasets. The paper further argues that LLMs' current development fundamentally challenges these long-standing evaluation patterns, as existing benchmarks and metrics increasingly fail to capture the true capabilities and limitations of these complex models. Our primary contribution is to consolidate and structure many of these historical insights and evolving challenges. By organizing these often fragmented pieces of understanding into the proposed five-tiered hierarchical framework, we aim to offer a more cohesive and systematic lens for approaching AI model evaluation. We believe that such a structured approach, which encourages assessment strategies to be explicitly contextualized by a model's position within this hierarchy and informed by its preceding layer, can help cultivate a more robust and meaningful comprehension of these increasingly complex LLM systems.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The authors contend that the current manners in which models are evaluated is insufficient, thereby proposing a multi-tiered system to define specific manners in which models should be evaluated based on the end goal or desiderata. The paper goes through a summary of different models and evaluation methods to reinforce their claims.

### Strengths
The motivation is clear and the evidence appears to be well supported.

### Weaknesses
Some of the questions that the authors raise do appear to be already out-in-the-open questions which researchers have been exploring for quite some time, hence there should be some discussion about methodologies that have already been proposed and why these may fall short of what is necessary to reach the ideals set by the authors.

### Questions
Why do the authors specifically limit their framework to the levels proposed (this is not a criticism but rather a way to let the authors reflect and maybe internally reflect on the framework they created)? Is there any gray area for overlap where what is being evaluated could be difficult to judge directly? Is there further granularity that the authors believe is appropriate but may not be fully compatible with the proposed framework?

### Presentation
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This position paper addresses the “evaluative crisis” in the era of LLM, arguing that current evaluation method rely on benchmark dataset that create a misleading simulacrum of true model capabilities. To address this, the authors propose a fundamental reconceptualization of the “model” itself through a five-tiered hierarchical framework. This framework deconstructs the model into the Noumenal (MN), Conceptual (MC), Instantiated (MI), Reachable (MR), and Observable (MO) tiers. The paper promotes an ongoing “model cartography” approach, focusing on understanding how each tier relates to.

### Strengths
* The proposed "five-tiered hierarchical framework" provides a valuable and structured vocabulary for diagnosing evaluation shortcomings. 
* The five-tier structure provides a useful lens for analyzing evaluation gaps, especially the divergence between MR and MO.
* Concept of "model cartography" offers a compelling alternative to the current culture of SOTA-chasing.

### Weaknesses
* While the framework is conceptually sound, it offers limited actionable steps for practical implementation.

* A significant conceptual tension exists in the proposal to use dynamic benchmarks and interactive protocols to explore the Reachable space". The authors critique static benchmarks for creating a limited MO. However, any new dynamic protocol, by definition, also creates a new MO. The paper does not sufficiently address how these new, more complex observational windows would be immune to the same fundamental problems of bias, overfitting, or creating a "hyperreal assessment environment" that it critiques.

* Including inherently unknowable tiers (e.g., MN) and aiming to assess all five levels may be unrealistic for the community

### Questions
* How can the proposed "dynamic benchmarks" be designed to prevent the formation of a new, equally susceptible MO, thereby avoiding the same "simulacrum" of understanding that the paper critiques in current methods?

### Presentation
2

---

## Human Reviewer 3

### Rating
4

### Rating Number
4

### Confidence
4

### Summary
The paper identifies an issue with the evaluation protocol of current LLMs, claiming that current evaluations only assess LLMs through a “small observation window” which may lead to an erroneous understanding of the true model capabilities. Instead, the paper argues for a hierarchical framework of what constitutes a model. This framework is inspired by philosophical ideas (e.g., Kant’s Critique of Pure Reason). The framework includes the Noumenal, Conceptual, Instantiated, Reachable, and Observable models which form a hierarchy that either encompasses or equals the other. The Noumenal model is the true, underlying reality the AI is attempting to approximate, while the observable model is the small window through which current evaluation protocols view the model. The paper argues that we should focus on evaluating and assessing each of these models rather than just the observable model.

### Strengths
- Using philosophical ideas and concepts within the machine learning community is an interesting idea that the community can benefit from, especially when working with topics such as LLMs and epistemic questions regarding knowledge, understanding, and truth.

- Broadening the scope of LLM evaluations is an important and significant area that should receive more attention.

- The distinction between the different types of models is interesting.

### Weaknesses
- The paper focuses most of its attention on the definitions of the different models and how they differ from each other, and does not provide much detail on how each of these models should be evaluated. While the paper does give general ideas in 4.2 and App. A., they are vague and few. 

- The different model types and the differentiation between them are not always clear. I think the writing can be improved to make it more intuitive.

- The paper does not offer an alternative position.

- The paper focuses a lot on the philosophical definitions, and the writing has a philosophical tone to it. For a machine learning conference, I think it has too few machine learning aspects, details, and implications, I believe the paper can be improved by making it more accessible to the wider machine learning community (e.g., while I hold Kant’s Critique of Pure Reason in high regard, I doubt many researchers in the community have read it and I am not sure using Kantian terms helps the paper). 

- The paper does not provide any empirical evidence that demonstrates the position is feasible and useful.

### Questions
- Is it possible to add a few figures that demonstrate the main ideas of the paper and summarize them?

- Do you have empirical evidence that demonstrates the position is feasible and that using the proposed framework is useful? Alternatively, if no such evidence is present, can the paper clearly explain where and how the framework would be useful?

- Can the authors include a more detailed plan on how to evaluate each of the models and what direct benefit the community would have from doing so?

### Presentation
2
