# Toward a Sheaf-Theoretic Understanding of Compositionality in Large Language Models

- Decision: Reject
- Avg Score: 4.33
- Scores: 3, 5, 5

## Abstract
Compositionality has long been considered a fundamental aspect of human cognition -  enabling the learning, manipulation, and generation of natural language. Understanding how this concept applies to Large Language Models (LLMs) and how it can be effectively evaluated remains a key challenge. In this work, we explore the potential of formalizing cognitive notions from theory, such as compositionality, to develop more nuanced evaluation frameworks for LLMs. Using a sheaf-theoretic approach, we define compositionality through four distinct conditions that capture its multifaceted nature. This formalization offers a structured perspective on evaluating LLMs, moving beyond surface-level assessments to uncover deeper insights into their behavior. Our findings suggest that theoretical frameworks like this one can play a crucial role in advancing the understanding and evaluation of LLMs, providing a foundation for more comprehensive and precise performance analyses.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper introduces a mathematical framework for compositionality in LLMs based on sheaf topology, defining four basic conditions: restriction maps, gluing conditions, locality conditions, and natural transformations. The authors tested each condition with a specific dataset and found that instruction-tuned models have inconsistent performance across different aspects of compositionality.

### Strengths
- The paper presents a nice initial effort in defining compositionality with a mathematical framework rigorously
- The paper is well-structured and well-written

### Weaknesses
 - (Major) Limited novelty and applicability of the findings:
	- The formalization of compositionality via the sheaf-theoric framework is novel, but it is not clear its purpose, how it can be used in practice in the real world and whether it's correct or not (due to a weak experimental part).
	- There is no novelty in the evaluation part since it uses known datasets and results for the literature, except for the introduction of the COMPCOMB dataset.
	- In general, there are very few contributions that justify this paper.
- (Critical) The experimental part is extremely weak and not convincing:
	- In Table 1 there is a significant drop between base models and instruction-tuned models like a huge ~40% (0.82 vs 0.42) on SCAN. The authors provide an explanation that  L402 "instruction tuning likely leads to a loss in the development of restriction maps, which could be explained by the fact that while the model retains its most important generalizations, it loses some local information to accommodate instruction tuning, leading to loss of restriction mapping". This is in contrast with results in the literature where instruction-tuned models perform generally better. I believe there is not enough empirical evidence to sustain this statement and the huge performance drop might be due to issues in the evaluation setup. The authors mention the use of "computing the model’s log probabilities for two possible completions" but this has been shown to be problematic, especially in instruction-tuned models that might lose the calibration in their logits after RLHF (https://arxiv.org/abs/2402.14499 , https://arxiv.org/abs/2303.08774). I suggest using a different eval strategy (e.g., comparison with the ground truth and exact match metric) and distinguishing results between instruction-tuning and models tuned via RLHF.
	- In general, I don't think the experiments are thorough enough to convince me without any doubt that an increase/decrease of the score on a specific dataset (e.g., SCAN) means an increase/decrease of a compositional condition defined in the framework (e.g., Restriction Condition). There are several other factors involved in the evaluation that might lead to spurious correlations and an increase/decrease in the score. I think the author should definitively pay more attention to the evaluation of the components defined in the framework.
- (Minor) The presentation of the results is not optimal:
	- The results proposed (Figures and Tables) are never referenced from the text. This creates ambiguity in the text because it's not clear what results you are commenting on. 
	- The proposed plots lack clarity. The rationale for using a radar plot to compare accuracies in Figure 1 is unclear, and both the scale and raw values in the plot are difficult to interpret.
- (Minor) There is a minimal discussion of related works. Missing related papers (e.g., [A Complexity-Based Theory of Compositionality](https://arxiv.org/abs/2410.14817))

### Questions
N/A

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
Compositionality is a topic on human cognition. 
LLMs appear to show their superior language processing capability and thus evaluating the compositionality become a portal to gain insights into these models.
This paper introduced a sheaf-theoretic framework with 4 different datasets to assess LLMs performance on compositionality.
Key findings include 1) larger models tend to be more performant. 2) instruction finetuned models may behave inconsistently in different tasks.

### Strengths
- Paper investigated both query (aka, prompt output) and internal representation in different tasks.
- To reviewer's knowledge, this paper is clear and original in proposing the sheaf-theoretic framework for LLMs compositionality assessment.
- Two orders of relationship are investigated, entity level and relation level.
- Proposed 4 datasets, namely SCAN, ANTAILS, COMPCOMB, PLANE, aim to unveil insights in restriction maps, gluing condition, locality condition, and natural transformation. 
- Appendix provided abundant information about generation process of each dataset.

### Weaknesses
 - A related work section would help readers to better understand the background and prepare readers well to follow the sheaf-theoretic framework.
- While 4 tasks cover distinct aspects, the size of these dataset could be limited to capture the compositionality of LLMs. Specifically, the number of examples in each dataset is not provided, making it difficult to assess the robustness of the findings. Furthermore, the diversity within each dataset is unclear, potentially limiting the generalizability of the conclusions.
- Compositionality is an important in human cognition and investigating it in LLMs is also exciting. The paper would be more complete if authors include the importance of LLMs compositionality in applications. What are the aspects or benefits if LLMs gains better compositionality performance. For instance, how does improved compositionality translate to better performance in downstream tasks such as complex reasoning or planning?
- There is limited description of the experiment setup. It would be preferable if there are more justifications for the methodology and choice of prompting. For example, the paper does not discuss why specific prompting strategies were chosen over others, or how these choices might influence the results. The absence of details on hyperparameter tuning or model selection further limits the reproducibility of the experiments.
- (line 908) There is a table or figure missing about the SCAN setup, showing **??**
- Appendix also shows the template used but it would be better to include additional examples in each dataset to help readers gain insights. For instance, providing a few diverse examples for each task, including both successful and unsuccessful cases, would help readers better understand the nuances of each dataset.
- There are many extremely long sentences, which requires a second pass and thus affect the readability of the paper.

### Questions
- Is llama2 chat hf an instruction-following checkpoint?
- Would it be possible to include Qwen in the evaluation for additional trends and patterns revealing? Also llama released 3 and 3.1.
- When introducing 4 tasks, the ordering is not consistent, is there any special consideration? 
For example, the order in table 1 or figure 1 (1SCAN, 2ANTAILS, 3COMPCOMB, 4PLANE) is different from the order in section 2 and section 3.3. 
- What is the size of each dataset?
- Could you provide an example for each dataset? 
- Could chain-of-thought prompting apply during evaluations?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
1. This work proposes a novel way to use sheaf theory for compositionality for Large Language Models (LLMs). Compositionality is a central concept of human cognition that understands complex things through simpler components. This new definition of compositionally contains four distinct conditions: restriction maps, gluing conditions, locality conditions, and natural transformations.

2. The experiments conducted across multiple LLMs (such as Llama2, CodeLlama, and Mistral) show that larger models tend to exhibit better compositional abilities overall. However, instruction-tuned models experience a significant decline in performance, particularly in tasks related to the restriction condition and natural transformations. This suggests that while instruction tuning may enhance generalization, it can degrade the model's ability to handle compositional information.

### Strengths
1. The paper introduces a completely new, higher-level definition of compositionality using sheaf theory, which provides a fresh perspective on evaluating the compositional abilities of LLMs. This novel approach broadens the understanding of how complex linguistic expressions are structured and processed by LLMs. Provide a more comprehensive way to measure LLMs' ability.

2. The authors evaluate various LLMs (such as Llama2, CodeLlama, and Mistral) across four different angles, providing a detailed comparison of their compositional performance. This analysis helps identify which models excel in certain tasks and where they fall short, offering useful insights for improving future models.

### Weaknesses
1. The paper does not include a dedicated Related Work section, which is critical for situating the proposed framework within the existing literature. This omission makes it difficult to understand how the new approach builds upon or differs from existing methods for evaluating compositionality in LLMs. Specifically, without a clear discussion of prior work, it is unclear how this sheaf-theoretic approach compares to more traditional methods of evaluating compositionality, such as those based on symbolic manipulation or logical inference.

2. The paper falls short of the 10-page limit. This space could be used to conduct a more thorough analysis of the experimental results, including more detailed error analysis and exploration of the limitations of the proposed framework. For example, the paper could include a more detailed breakdown of the performance on specific types of compositional tasks, rather than just reporting overall scores. Additionally, the authors could have explored the impact of different model sizes and architectures on the observed compositional abilities in more detail.

3. While the proposed sheaf-theoretic framework is innovative and offers a high-level definition of compositionality, its real-world applicability remains uncertain. The framework may be too abstract or theoretical for immediate use in practical model development or evaluation, raising questions about its tangible impact. The paper does not provide concrete examples of how the framework can be used to improve the performance of LLMs in real-world tasks, such as question answering or text summarization. The lack of direct connection to practical applications limits the immediate usefulness of the proposed framework.

4. The paper does not provide a better solution for improving compositionality in LLMs. While the framework is useful for evaluating compositionality, it does not offer any specific techniques or strategies for enhancing the compositional abilities of LLMs. The paper should have included a discussion of potential avenues for future research that could build upon the proposed framework to develop more compositional LLMs.

### Questions
1. Are there any situations or specific tasks where the proposed sheaf-theoretic framework might not be applicable?

2. The performance shifts observed in Table 1 indicate differences across various models. What insights can these performance variations provide regarding model architecture, training methodologies, or the training data used?

### Soundness
3

### Presentation
2

### Contribution
3
