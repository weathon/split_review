# Understanding Alignment in Multimodal LLMs: A Comprehensive Study

- Decision: Reject
- Scores: 8, 6, 6

## Abstract
Preference alignment has become a crucial component in enhancing the performance of Large Language Models (LLMs), yet its impact in Multimodal Large Language Models (MLLMs) remains comparatively underexplored. Similar to language models, MLLMs for image understanding tasks encounter challenges like hallucination. In MLLMs, hallucination can occur not only by stating incorrect facts but also by producing responses that are inconsistent with the image content. A primary objective of alignment for MLLMs is to encourage these models to align responses more closely with image information. Recently, multiple works have introduced preference datasets for MLLMs and examined different alignment methods, including Direct Preference Optimization (DPO) and Proximal Policy Optimization (PPO). However, due to variations in datasets, base model types, and alignment methods, it remains unclear which specific elements contribute most significantly to the reported improvements in these works. In this paper, we independently analyze each aspect of preference alignment in MLLMs. We start by categorizing the alignment algorithms into two groups, offline (such as DPO), and online (such as online-DPO), and show that combining offline and online methods can improve the performance of the model in certain scenarios. 
We review a variety of published multimodal preference datasets and discuss how the details of their construction impact model performance. Based on these insights, we introduce a novel way of creating multimodal preference data called Bias-Driven Hallucination Sampling (BDHS) that needs neither additional annotation nor external models, and show that it can achieve competitive performance to previously published alignment work for multimodal models across a range of benchmarks.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper addresses challenges in aligning MLLMs with human preferences to improve response accuracy and reduce hallucinations. It reviews various offline and online alignment strategies, including DPO  and RLHF, and introduces BDHS. BDHS generates preference data without human annotation, leveraging model-inherent biases to enhance performance cost-effectively. Results indicate BDHS is competitive with established preference datasets, demonstrating its potential as a lightweight alternative to traditional alignment approaches for MLLMs, especially in tasks requiring high fidelity between visual inputs and textual responses.

### Strengths
1. The paper introduces a unique approach to generate preference data for MLLMs by utilizing model biases without human or external model annotations.
2. The paper provides empirical analysis, comparing BDHS with other alignment methods across multiple benchmarks, highlighting its effectiveness and resource efficiency in aligning MLLMs.

### Weaknesses
1. The proposed data sampling approach partially mitigates hallucination issues in MLLMs but does not completely resolve them.
2. The BDHS method's dependency on hyperparameters, such as mask thresholds, could affect reproducibility across different model implementations.

### Questions
1. Will the code be open-sourced to facilitate further research in this area?
2. How does the proposed approach ensure that the distribution of generated hallucination data aligns with real-world hallucination data distributions?

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
This paper investigates preference alignment techniques for Multimodal Large Language Models (MLLMs), focusing on how they address hallucinations, which occur when models produce responses not grounded in visual inputs. The study categorizes alignment methods into offline and online approaches and examines various multimodal preference datasets. The authors propose a novel data generation method called Bias-Driven Hallucination Sampling (BDHS), which does not require human annotations or external models. Experimental results demonstrate BDHS’s effectiveness compared to more resource-intensive methods.

### Strengths
1、Comprehensive Analysis: The paper provides a detailed comparison of alignment methods, including offline and online strategies, and evaluates their effectiveness using diverse datasets.


2、Novel Data Generation Method: The introduction of BDHS offers a cost-effective alternative to traditional alignment approaches, reducing the need for human annotation or external supervision while maintaining competitive performance.

### Weaknesses
1、Clarification of Methodological Choices: It would be helpful to better understand why specific thresholds and parameters were chosen for BDHS, such as the similarity score threshold and masking strategy. The paper lacks a detailed justification for the specific values used, such as the similarity threshold for filtering non-preferred responses and the extent of attentional masking. Without a clear rationale, it's difficult to assess the robustness of these choices and whether they are optimal, or if they were simply chosen empirically. The paper should include a more thorough sensitivity analysis of these parameters.

2、Generalizability of BDHS: It remains unclear whether BDHS can be effectively applied to models beyond the specific ones studied. Further discussion on its applicability to other MLLMs or domains would strengthen the paper. The experiments are limited to a specific model architecture (LLaVA) and a narrow set of tasks. It is not clear if the BDHS method would be equally effective on other MLLMs with different architectures, pre-training procedures, or in different application domains. The paper needs to provide more evidence or theoretical arguments to support the generalizability of the proposed method.

### Questions
1、The DHS method induces hallucinations by performing attentional masking in the latent space. Is it possible that this strategy could affect the sensitivity of the model to critical details in the image? Have ablation experiments been performed to quantify the effect of this attentional masking in scenes of varying visual complexity? In addition, how to select the range of attention masking, and whether the alignment effect can be optimized by dynamic adjustment?

2、The paper mentions filtering out different non-preferred responses by semantic similarity score. For this filtering mechanism, is it possible that there is a bias that makes the model perform better or worse on specific types of semantic content? Have comparative experiments with different similarity scoring models been conducted to confirm the robustness of the selection mechanism? Furthermore, could this similarity score lead to a tendency for models to oversimplify when faced with less common or more complex visual scenes?

3、Does the performance of the BDHS method on the LLaVA 1.6-7B model generalize to larger or smaller model sizes? Have any experiments been conducted on models with different parameter numbers to explore whether this approach exhibits different advantages or disadvantages depending on the model size? Especially on small-scale models, is it possible that the method effect is not significant due to parameter limitations?

4、To what extent do current hallucina-evaluation benchmarks such as POPE and MMHALBench-V truly reflect model performance in real-world applications?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper explores preference alignment for improving Multimodal Large Language Models (MLLMs), specifically focusing on reducing hallucinations and increasing alignment between model outputs and image content. It provides a thorough analysis of various alignment methods and introduces a novel approach, Bias-Driven Hallucination Sampling (BDHS), which effectively generates preference data without human annotation or external models.

### Strengths
1. The study systematically compares offline and online alignment methods, examining their impact on model performance across various metrics like hallucination reduction and response quality.
2. BDHS presents a low-cost, innovative solution to generate preference data, showing competitive results against other data-heavy methods.

### Weaknesses
1. While the paper examines alignment techniques and datasets, it does not clearly articulate the primary findings from these investigations, which can make it challenging for readers to grasp the significance and implications of the study

2. BDHS demonstrates promising results; however, its effectiveness may differ across various MLLMs and visual tasks. Conducting additional experiments with diverse model architectures would bolster claims regarding its generalizability.

### Questions
1. What are the effects of scaling up BDHS in terms of data size or complexity on model performance?
2. What specific modifications could be made to BDHS to achieve state-of-the-art results on key benchmarks?

### Soundness
3

### Presentation
3

### Contribution
2
