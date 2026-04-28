# Beyond Surface Structure: A Causal Assessment of LLMs' Comprehension ability

- Decision: Accept
- Avg Score: 5.75
- Scores: 6, 6, 6, 5

## Abstract
Large language models (LLMs) have shown remarkable capability in natural language tasks, yet debate persists on whether they truly comprehend deep structure (i.e., core semantics) or merely rely on surface structure (e.g., presentation format). Prior studies observe that LLMs' performance declines when intervening on surface structure, arguing their success relies on surface structure recognition. However, surface structure sensitivity does not prevent deep structure comprehension. Rigorously evaluating LLMs' capability requires analyzing both, yet deep structure is often overlooked. To this end, we assess LLMs' comprehension ability using causal mediation analysis, aiming to fully discover the capability of using both deep and surface structures. Specifically, we formulate the comprehension of deep structure as direct causal effect (DCE) and that of surface structure as indirect causal effect (ICE), respectively. To address the non-estimability of original DCE and ICE --- stemming from the infeasibility of isolating mutual influences of deep and surface structures, we develop the corresponding quantifiable surrogates, including approximated DCE (ADCE) and approximated ICE (AICE). We further apply the ADCE to evaluate a series of mainstream LLMs (and the one with random weights), showing that most of them exhibit deep structure comprehension ability, which grows along with the prediction accuracy. Comparing ADCE and AICE demonstrates closed-source LLMs (e.g., GPT) rely more on deep structure, while open-source LLMs (e.g., Llama) are more surface-sensitive, which decreases with model scale. Theoretically, ADCE is a bidirectional evaluation, which measures both the sufficiency and necessity of deep structure changes in causing output variations, thus offering a more comprehensive assessment than accuracy, a common evaluation in LLMs. Our work provides new insights into LLMs' deep structure comprehension and offers novel methods for LLMs evaluation.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The manuscript investigates the comprehension abilities of large language models (LLMs) beyond superficial structures by introducing a causal mediation framework. The authors propose the use of approximated direct causal effect (ADCE) and approximated indirect causal effect (AICE) as proxies to quantify comprehension of deep and surface structures, respectively. Through this framework, they empirically evaluate the reliance of mainstream LLMs, such as GPT and Llama, on deep versus surface structures across a range of tasks, including mathematical reasoning and commonsense understanding.

### Strengths
+ The paper presents an innovative method to quantify the comprehension of deep structures in LLMs through causal analysis.
+ Comprehensive datasets and models are used for evaluation.
+ Experimental results across multiple tasks suggest that ADCE is a valuable metric for assessing model comprehension.

### Weaknesses
 - It is unclear how deep structures are accurately identified and separated from surface structures, which is crucial for the validity of the interventions.
- The ADCE and AICE are presented as approximations, but it is unclear how accurately they reflect the true causal effects intended for evaluation.

### Questions
Overall, I appreciate the authors’ efforts in introducing a novel approach to assessing the comprehension ability of LLMs, especially in quantifying deep structure reliance. However, I have a few questions and points for clarification:

- Your approach relies on interventions targeting deep and surface structures. In your experiments, how are deep structures accurately identified and separated from surface structures? It would be helpful to understand the criteria or methods used to make this distinction reliably.

- Since ADCE and AICE are approximations, have you conducted any experiments to validate these metrics against true causal effects? Any validation results would help clarify the accuracy and reliability of these metrics in capturing the LLMs’ reliance on different structural components.

- I have a question regarding the use of causal mediation analysis within the causal structure presented in Figure 3.
As I understand it, causal mediation analysis is typically used to assess how the effect of a treatment variable X on an outcome Y is mediated through an in intermediate variable Z. This approach is often applied to measure both the direct effect of X on Y and the indirect effect mediated by Z (i.e., X -> Z -> Y). For example, a drug X might have a direct effect on a disease Y, but it may also cause patients to take aspirin Z, which further impacts Y through this indirect pathway.
In your causal graph, however, it seems that the deep structure d and surface structure s within the input x, independently affect the outcome Y through separate pathways (d -> Y and s -> Y). Since d does not mediate or influence s, these pathways appear to act in parallel rather than in a sequential manner where one variable mediates the effect of another.
Given this structure, could you please clarify whether causal mediation analysis is appropriate in this context? It would be helpful to understand how the direct and indirect effects are conceptualized in this framework, especially if the mediation structure does not strictly follow the conventional X -> Z -> Y pathway.

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
The paper introduces a framework to evaluate LLMs by distinguishing between their reliance on deep structures and surface structures. Using causal mediation analysis, it proposes metrics called Approximated Direct Causal Effect for deep structure comprehension and Approximated Indirect Causal Effect for surface structure, offering a more nuanced assessment of model understanding than accuracy alone. The findings reveal that closed-source models, like GPT, rely more on deep structure, whereas open-source models, like Llama, are more sensitive to surface structures, though this sensitivity decreases with model size

### Strengths
1. The paper introduces a unique framework that goes beyond accuracy to assess how language models rely on deep versus surface structures.
2. The ADCE and AICE metrics are interpretable and allow for precise distinctions between models' reliance on core semantics and surface-level structures.
3. The framework highlights significant differences between closed-source and open-source models in their reliance on deep vs. surface structures, contributing valuable insights into model development trends.

### Weaknesses
1. Although the metrics provide valuable insights, their exact interpretations may vary depending on model architecture, making it difficult to generalize findings across diverse LLMs without further context.
2. The approach may require internal access to models for accurate analysis, potentially limiting its use with proprietary or black-box models where such transparency isn’t feasible.

### Questions
1. Could the authors clarify how practitioners might interpret ADCE and AICE values across different model architectures?
2. How does the approach perform on NLP tasks involving noisy or unstructured data?

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
This paper presents a causal mediation analysis framework to assess LLMs' comprehension ability of deep structure versus surface structure. The authors propose ADCE and AICE metrics to quantify comprehension of deep and surface structures. They demonstrate that most LLMs exhibit genuine deep structure comprehension that increases with model scale, while dependence on surface structure varies between open and closed-source models.

### Strengths
- Paper is well-written.
- Comprehensive empirical evaluation across multiple tasks and model families with insightful findings about deep vs surface structure reliance
- This paper is novel; proposes ADCE and AICE for quantification based on causal mediation analysis.
- The method is task-agnostic; evaluation on 5 tasks across math, logic, common sense benchmarks.

### Weaknesses
 - The relationship between ADCE and fine-tuning (Section 4.3) is only briefly explored.

### Questions
- ADCE seems to capture both sufficiency and necessity of deep structure changes in causing output variations. How might different post training strategies influence a model's reliance on deep vs. surface structure?

### Soundness
4

### Presentation
3

### Contribution
4

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This paper proposes to use the casual mediation analysis method to examine the following question: does the LLM really understand the deep semantic meaning for problem-solving or merely rely on text surface forms? Authors claim that previous methods usually investigate this effect in specific tasks without generalization. This paper presents approximated direct causal effect (ADCE) and approximated indirect causal effect (AICE) to empirically quantify the LLM dependencies on deep structure understanding or shallow surfaces. 

The reviewer is not familiar with related works in this field, and therefore, the commentary below is from a general NLP researcher's point of view. The confidence score is set to 2 to reflect this point.

### Strengths
1. The paper presents a novel point of view to evaluate if the LM relies on the deep structures or surface forms to answer questions. Empirical and theoretical results show that the proposed ADCE is a better metric when evaluating LLM deep structure dependency.

2. The findings that closed-source LLMs rely more on deep structure while open-source models are sensitive to surface indicate that the current open-source SFT / alignment stages still need further investigation to have a higher reliance for the models on deep structure.

3. The proposed ADCE metric indicates that the accuracy of specific tasks could be misleading.

### Weaknesses
1. I am concerned about the necessity of applying causal mediation analysis to this research question. Mask, Replace, Swapping, etc., are common practices for augmenting text data as well as examining the sensitivity of LLMs to slight variations in the input text. The motivation for the CMA application in this submission is not clear to me, given the current writing. Specifically, while the paper argues that these methods do not isolate deep structure understanding, it does not provide a clear explanation of why the proposed CMA approach is superior in this regard. The paper needs to clarify why simply observing changes in output after masking or swapping is insufficient, and what specific advantage the causal framework provides.

2. Following 1, Section 3.3 is intuitive by itself without the theories in Section 3.1 and 3.2. If I understand correctly, Equation 5 is a simple combination of several indicator functions that reflects if intervention to the question has actual effects. The connection between the theoretical framework and the practical implementation in Section 3.3 is not clearly established. The paper needs to better articulate how the theoretical concepts of direct and indirect causal effects are translated into the specific masking and rephrasing operations, and how Equation 5 is derived from the preceding theoretical framework.

### Questions
Refer to the Weaknesses Part.

### Soundness
3

### Presentation
3

### Contribution
3
