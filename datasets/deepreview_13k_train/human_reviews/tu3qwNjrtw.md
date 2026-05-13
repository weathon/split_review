# Composable Interventions for Language Models

- Decision: Accept
- Scores: 8, 6, 6, 6, 3

## Abstract
Test-time interventions for language models can enhance factual accuracy, mitigate harmful outputs, and improve model efficiency without costly retraining.
But despite a flood of new methods, different types of interventions are largely developing independently.
In practice, multiple interventions must be applied sequentially to the same model, yet we lack standardized ways to study how interventions interact.
We fill this gap by introducing \textit{composable interventions}, a framework to study the effects of using multiple interventions on the same language models, featuring new metrics and a unified codebase.
Using our framework, we conduct extensive experiments and compose popular methods from three emerging intervention categories---\textit{knowledge editing}, \textit{model compression}, and \textit{machine unlearning}.
Our results from 310 different compositions uncover meaningful interactions: compression hinders editing and unlearning, composing interventions hinges on their order of application, and popular general-purpose metrics are inadequate for assessing composability.
Taken together, our findings showcase clear gaps in composability, suggesting a need for new multi-objective interventions.edu}, \texttt{kyobrien@microsoft.com}}

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper experimentally demonstrates the effect of composing various inference time setups for LLMs and suggests possible setups for better performance from its analysis.

### Strengths
S1. The paper conducts experiments on various methods and compositions on multiple models to provide a deeper insight.

S2. The method proposes metrics that correlate with the effect of a composition.

S3. The presentation is lucid and easy to follow.

S4. The codebase will be useful to the community for further studies.

### Weaknesses
W1. Some comparisons on the base models, chat, and RLHF could be interesting which could provide insight into pretraining, instruction tuning, and post-training with the interventions.

W2. With a similar spirit as W1, it is important to see the results for different generations of the same model family and sizes.

W3. The sensitivity (standard deviation) of the experiments is unclear if run multiple times in Table 2.

W4. Practitioners need to perform a grid search for their domain-specific requirements as some results depend on specific settings outside composition.

### Questions
Please refer to the weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes a new framework to assess the effects of combining different test-time interventions on language models to improve factual accuracy, efficiency, and mitigate harmful outputs. Traditionally, methods such as knowledge editing, model compression, and machine unlearning have been developed separately, but practical applications often require these interventions to work together. The authors introduce two novel metrics—Order-free Error and Order Sensitivity—to evaluate the composability of interventions, aiming to ensure that each intervention's success is minimally impacted by other interventions.

Key contributions include: (1) extensive experiments across 417 combinations of interventions, uncovering findings, such as compression often hindering the success of knowledge editing and unlearning, and the significant impact of intervention order on outcomes. (2) They will provide a codebase featuring popular intervention methods, supporting future multi-objective intervention research and development.
The paper emphasizes the need for composable, multi-objective intervention methods and creates a foundation for systematically evaluating intervention interactions in language models.

### Strengths
* Addresses an important program in model updates and adaptations to real-world requirements.
Introduces new metrics and provides extensive experimental results. 
* Codebase hypothetically supports is flexible enough to scale to other inference-time interventions. There is no code uploaded, so hard to say for sure.
* Well-written paper

### Weaknesses
 * Hard to say if the findings using the specific models and datasets used generalize more broadly (e.g., Llama 3, WMDP). WMDP, for instance, specifically notes that “benchmarking on only WMDP may yield a false sense of model safety after unlearning.”
* The paper lacks guidelines for ordering interventions or insights/analysis into why some orderings are not robust or how to make them more robust.

### Questions
See weaknesses.

### Soundness
2

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
4

### Summary
The paper proposes a framework (evaluation metrics) to study the effect of the composable interventions on LLMs. Authors claim that interventions like model compression, knowledge editing, and unlearning can affect each other and hence they study this phenomenon.

### Strengths
1. The paper is written in a very clear, nice, and easy to understand way. 
2. The motivation of the paper is clear. 
3. The paper studies an interesting problem.

### Weaknesses
While the paper is written very clearly and it studies an interesting problem, I have a major concern. My major concern is that the technical contribution of the paper might not be rigorous although insights and findings are good and the paper studies an interesting problem. perhaps one way to improve the paper would be to propose a method to make LLMs more robust to composable interventions or even design the interventions themselves in a way to not see degrade in their performance after other interventions are applied on top. Or even using the proposed evaluation framework as a recommendation framework to provide recommendation on how the interventions should be applied based on a given LLM and the intervention method.

Another concern I have is that the framework might be limited as it only considers two interventions at a time. Can the method be expanded to study more than two interventions at a time?

Finally, results on other LLMs are not fully consistant across all the studied dimensions which makes the finding of the paper not super reliable. It would be good to do some statistical significance test (e.g., across various LLMs).

### Questions
1. Why did you decide to focus on the three interventions in particular mentioned in the paper? (unlearning, compressing, model editing)
Would this choice limit the scope of study?

2. As also mentioned in the weaknesses above, the framework might be limited as it only considers two interventions at a time. Can the method be expanded to study more than two interventions at a time?

### Soundness
2

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
4

### Summary
This work introduces a "Composable Interventions" for language models, addressing a practical, real-world need. The authors develop new metrics and a unified codebase to evaluate the effectiveness of combining multiple interventions, such as knowledge editing, model compression, and machine unlearning. Through rigorous and extensive experimentation with 417 intervention combinations, the research underscores the significance of the sequence in which interventions are applied on model performance. The exposition is clear and well-organized. This study tackles the complexities of applying multiple interventions simultaneously, providing foundational insights that pave the way for future research on robust and adaptable language models.

### Strengths
- The authors introduces two new metrics:Order-free Error and Order Sensitivity, that evaluate the robustness of intervention sequences, highlighting the importance of intervention order.
- The authors also conducted extensive experiments using various compositions, showcasing the interaction effects of various interventions.
- The authors present several important findings. For instance, the success of interventions is highly dependent on the order of application; compression hinders editability; unlearning and editing are relatively compatible; and certain methods are inherently more suitable for sequential applications. Additionally, they found that conventional metrics are inadequate for measuring composability, underscoring the need for new intervention techniques explicitly designed for this purpose.

### Weaknesses
 - The authors present numerous findings and insights, such as Compression consistently hinders Knowledge Editing and Unlearning, which is a relatively straightforward conclusion. It would be valuable for the authors to explore deeper analysis and hypotheses beyond identifying patterns such as 'A affects B' or 'A and B are compatible,' moving from experimental observations to more comprehensive insights.
- In combined interventions, it appears that certain combinations do not yet have a clear consensus. For instance, in composing model compression with knowledge editing, the preferred order can vary significantly by method: for GPTQ, editing seems more effective first, whereas for AWQ, compression may be preferable. This suggests that optimal ordering may rely on experimental results specific to each method.
- While Order-free Error and Order Sensitivity offer valuable insights, the small differences in outcomes and variations across metrics suggest that additional measures may be needed to fully capture intervention interactions.

### Questions
Refer to Weaknesses

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper highlights a gap in the practical application of model interventions, where multiple techniques, such as information removal, model editing, and efficiency optimization (e.g., pruning and quantization) are often needed in combination but have largely been studied in isolation. The authors systematically explore how these interventions interact when used together, analyzing the sensitivity to intervention order and the broader implications of composability. This research offers insights into the outcome of utilizing multiple interventions and emphasizes the need for multi-objective intervention metrics to gauge their effective composability.

### Strengths
The research effectively highlights an oversight in current evaluation methodologies, where interventions are assessed independently despite concurrent deployment requirements in productionized environments.

Analysis of compositional effects across multiple intervention types, incorporating various established techniques from each domain (editing, unlearning, and model compression).

Findings provide valuable insights into the compatibility and limitations of different intervention combinations, offering practical usage guidance.

### Weaknesses
While the study provides a thorough documentation of interactions among various interventions, it falls short in examining the underlying issues or mechanisms that lead to compositional failures. A deeper analysis of the interference patterns or cause-effect relationships between interventions is necessary to understand why the composition of approaches works more effectively in some cases than in others. Exploring why certain techniques exhibit superior composability over others would greatly enhance the study’s contribution. Such insights would also help clarify the conditions under which specific interventions interact constructively or destructively, offering guidance for future research in designing more robust and composable interventions.

Compression introduces performance limitations, with a direct trade-off between compression percentage and model capabilities. The performance degradation appears predictable.

Unlearning effectiveness varies by approach. Parameter shifts during unlearning could potentially be mitigated by compression, particularly when parameters are subsequently quantized or pruned. A deeper analysis is required to comprehensively understand these interactions.

Table 11 indicates performance decline correlates with compression extent. Reduced fine-tuning performance suggests broader model trainability challenges rather than composability.

My final comment is that the work's primary contribution is a framework that highlights systemic challenges in intervention interactions, which necessitates rigorous, granular reasoning to substantiate its claims.

### Questions
How do different interventions interact with one another? Are there any interference patterns or dependencies that affect their compositional effectiveness?

Why do certain techniques exhibit better composability than others? Are there particular properties or design choices in those techniques that lend themselves to more effective composition?

### Soundness
2

### Presentation
3

### Contribution
2
