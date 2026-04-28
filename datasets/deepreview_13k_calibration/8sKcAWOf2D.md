# Fine-Tuning Enhances Existing Mechanisms: A Case Study on Entity Tracking

- Decision: Accept
- Avg Score: 5.67
- Scores: 6, 6, 5

## Abstract
Fine-tuning on generalized tasks such as instruction following, code generation, and mathematics has been shown to enhance language models' performance on a range of tasks. Nevertheless, explanations of how such fine-tuning influences the internal computations in these models remain elusive. We study how fine-tuning affects the internal mechanisms implemented in language models. As a case study, we explore the property of entity tracking, a crucial facet of language comprehension, where models fine-tuned on mathematics have substantial performance gains. We identify the mechanism that enables entity tracking and show that (i) in both the original model and its fine-tuned versions primarily the same circuit implements entity tracking. In fact, the entity tracking circuit of the original model on the fine-tuned versions performs better than the full original model. (ii) The circuits of all the models implement roughly \emph{the same} functionality: Entity tracking is performed by tracking the position of the correct entity in both the original model and its fine-tuned versions. (iii) Performance boost in the fine-tuned models is primarily attributed to its improved ability to handle the augmented positional information. To uncover these findings, we employ: Patch Patching, DCM, which automatically detects model components responsible for specific semantics, and CMAP, a new approach for patching activations across models to reveal improved mechanisms. Our findings suggest that fine-tuning enhances, rather than fundamentally alters, the mechanistic operation of the model.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors investigate the effects of fine-tuning on circuit-level mechanisms within large language models (LLMs) using entity tracking as a focal point. Initially, they employ a path-patching technique to isolate circuits responsible , categorizing attention heads into four groups based on the characteristics inherent to entity tracking. By defining four distinct groups, they ascertain the consistency and effectiveness of these circuits across various models. To delve deeper into the functionality of each group, they outline three main desiderata: Object, Label, and Position. Through activation patching, they discern the role of each group and confirm the commonality of circuit functionality across all models using Desiderata-Based Component Masking. The final phase involves Cross-Model Activation Patching, a method requiring the overlay of activations from similar components of different models on identical inputs. This assists in elucidating how a math-fine-tuned model augments an existing circuit in a base model, leading to enhanced performance in entity tracking. Experiments on LLaMA-7B and its two fine-tuned variants, Vicuna-7B and Goat-7B, reinforce their conclusions.

### Strengths
1. The authors effectively elucidate the impact of fine-tuning on the internal computations of large models, particularly with respect to entity tracking. This provides a deeper understanding of how fine-tuning influences model behavior. Utilizing path patching, they constructed four distinct groups of attention heads and enable a granular examination of the model's functionalities. Demonstrated consistency across different models, validating the universality of the identified circuits in performing the entity tracking task.
2. In subsequent tests of the individual capabilities within the identified paths, three out of the four attention head groups exhibited similar functionalities.This substantiates the hypothesis that the circuits in fine-tuned models implement similar functionalities.
3. Experimental results on DCM concerning the Positional Transmitter and Value Fetcher in Goat-7B, as opposed to the original LLaMA-7B, align well with the CAMP experiment. This consistent alignment between the experimental findings and the initial hypotheses strengthens the paper's credibility.

### Weaknesses
1. The study's scope is limited to a single foundational model, raising concerns about the generalizability of the conclusions. Without further investigation across a broader spectrum of models, it's challenging to ascertain if the observed mechanisms are universally applicable. Specifically, the reliance on LLaMA-7B and its fine-tuned variants, Vicuna-7B and Goat-7B, provides a narrow view of circuit behavior. It remains unclear whether the identified four groups of attention heads and their associated functionalities would manifest similarly in models with different architectures or pre-training datasets. This limitation hinders the ability to make broad claims about the nature of fine-tuning effects on circuit-level mechanisms.
2. When establishing the Desiderata for identifying circuit functionality, the connection between the three tasks and their corresponding abilities remains ambiguously articulated. The paper introduces Object, Label, and Position desiderata, but the precise manner in which these desiderata map to specific circuit functions is not sufficiently clear. For instance, while the Object desideratum aims to identify components encoding object information, the mechanism by which this is achieved through activation patching and how it differs from Label or Position desiderata is not explained with enough detail. This lack of clarity makes it difficult to understand the exact role of each identified component.
3. The section detailing the use of CMAP to patch activations from Goat-7B to Llama-7B lacks clarity, particularly when validating the impact of QKV on the model's performance. The rationale behind why patching the QK-circuit of the Value Fetcher and the value vector of the Position Transmitter heads results in the most significant enhancement is not well-explained. It's unclear why these specific components show the most pronounced effect, and the underlying mechanisms that lead to this observation are not sufficiently discussed. The paper would benefit from a more detailed analysis of the specific computations within the QK and OV circuits and how they are altered by fine-tuning.

### Questions
see weakness

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work aims to answer the question: why fine-tuning language models (LMs) can enhance their performance on a range of tasks? As a case study, the authors experiment with LLaMA-7B and two fine-tuned versions, Vicuna-7B and Goat-7B, on the entity tracking task. They first apply Path Patching to extract the circuit, a subset of LM heads, from LLaMA-7B and find that all three models can reach high faithfulness scores with the circuit identified in Llama-7B, a.k.a., all three models share a similar circuit. Then, they apply Desiderata-based Component Masking (DCM) to identify LM heads responsible for specific functionality and find that each group of LM heads on all three models share the same functionality. Finally, they propose the Cross-Model Activation Patching (CMAP) to attribute the performance gain of fine-tuning to specific components, a.k.a., Value Fetcher, and Position Transmitter heads.

The work conducts extensive experiments to uncover the internal mechanisms of fine-tuning by applying two existing methods, Path Patching and DCM, and proposing one novel method, CMAP. The authors disclose some interesting experiment findings, e.g., the performance gain of fine-tuning attributes to the improved ability to handle positional information.

### Strengths
- A novel method CMAP for mechanistic interpretability.

- The authors conducted extensive experiments by applying Path Patching, DCM, and their proposed CMAP to analyze the underlying mechanism of fine-tuning, which discloses several exciting findings, e.g., (1) The language model (LM) and its two fine-tuned versions share the same circuit. (2) The components of this circuit in these three models share the same functionality. (3) The performance gain of fine-tuning attributes to the improved ability to handle positional information.

- The presentation is clear, although it requires the reader to have some background of mechanistic interpretability.

### Weaknesses
 - The experiment results can not lead to the claim that the original model and its fine-tuned versions implement entity tracking with the “same” circuit: (1) the fine-tuned model, Goat-7B, reaches an accuracy of 82% while the circuit identified in Llama-7B reaches an accuracy of 68%; this considerable performance gap indicates that Goat-7B’s circuit may be different from Llama-7B’s circuit, although these two circuits may have considerable overlap. (2) It is necessary to explore the mentioned overlap. For example, could authors apply Path Patching to Vicuna-7B and Goat-7B to extract their circuits and compute the overlap between their circuits and Llama-7B’s circuit?

- As mentioned in (Wang et al., 2022) [1], faithfulness is not sufficient to prescribe which circuits explain the behavior well. Why do not authors show the completeness and minimality scores, similar to (Wang et al., 2022) [1]? 

- In Section 4.2: CIRCUIT EVALUATION, the expression F(Cir \ K) - F(Cir \ (K U {v})) / F(Cir \ (K U {v})) in the Minimality paragraph seems wrong. Moreover, the authors mention that they filter out the heads that contribute less than 0.5% of the functionality defined by subset K. This description is inconsistent with the above expression since the denominator of the equation is the functionality defined by the remaining nodes after removing K and v.

### Questions
- What is the motivation to divide heads into four groups (A, B, C, D) instead of three or five? In other words, since authors iteratively identify groups of heads with high direct effects on each other using the path patching score, why did authors end with four groups instead of other numbers?

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper examines the impact of fine-tuning on the internal computations of language models through a case study. Specifically, the authors investigate the entity tracking mechanism of Llama-7B and its fine-tuned versions. The authors argue that the performance enhancements resulting from fine-tuning can be attributed to the improved ability of attention heads to handle positional information.
They utilize Desiderata-based Component Masking (DCM) to confirm that the entity tracking mechanism and the functionality of a subset of attention heads remain the same in Llama-7B and its fine-tuned variants. Additionally, they introduce CrossModel Activation Patching (CMAP) to reveal the improved mechanisms of attention heads.

### Strengths
1. The paper is generally well-written and easy to follow.

2. The authors provide an explanation for the performance enhancement observed in the fine-tuned model, focusing on the entity tracking circuits.

### Weaknesses
1. The methods employed in this paper are limited to a single type of model on an entity tracking dataset. Moreover, the entity tracking mechanism is likely just one of many contributing factors, raising questions about the generalizability of their claims. Specifically, the exclusive use of Llama-7B and its fine-tuned versions on a single entity tracking dataset limits the scope of the conclusions. The authors do not explore other model architectures or datasets, which makes it difficult to ascertain whether the observed improvements in attention head behavior are specific to this model and task, or if they represent a more general phenomenon. The study would benefit from including models with different architectures, such as encoder-only models or models with varying layer sizes, and also by testing the proposed methods on datasets that probe different cognitive mechanisms.

2. I personally do not see the significance of the entity tracking problem to be particularly high. While the authors focus on the entity tracking mechanism, it is not clear how this specific mechanism is crucial for broader language understanding. The paper would benefit from a more thorough explanation of why this particular mechanism is important and how it relates to more general language understanding capabilities. The current presentation does not convincingly demonstrate the broader relevance of the findings.

### Questions
Why is it justified to employ attention mechanisms to delve into the entity-tracking circuit? I acknowledge there may be some associations between them, but are these connections truly substantial?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
