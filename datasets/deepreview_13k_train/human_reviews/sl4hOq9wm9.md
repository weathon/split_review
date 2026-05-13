# Knowledge Augmentation: In-context or In-parameter?

- Decision: Reject
- Scores: 6, 5, 6, 5

## Abstract
Large Language Models (LLMs) have achieved remarkable performance in various natural language processing tasks by leveraging relevant external knowledge provided by the users or retrieved from external sources. 
Traditionally, this external information is incorporated by appending it directly to the model’s input context, a paradigm known as in-context knowledge injection.
However, this paradigm faces significant limitations due to the finite input context length of LLMs and often results in shallow integration between the external knowledge and the model’s internal representations.
To address the limitations of in-context knowledge injection, we propose a new knowledge injection paradigm called in-parameter knowledge injection, which temporarily embeds the external knowledge relevant to the user’s input directly into the model’s parameters rather than its input context. 
This new paradigm overcomes the context length limitations of LLMs and enables deeper integration of external information within the model’s internal representations. 
Through extensive experiments across tasks of varying complexity, we demonstrate that in-parameter knowledge injection achieves significant benefits for complex tasks requiring intricate reasoning. 
In contrast, in-context injection remains effective for simpler tasks where answers can be directly extracted from the provided information.

We have open-sourced all the code, data, and models in the following anonymous GitHub link: https://anonymous.4open.science/r/In-parameter-Knowledge-Injection/

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces a method named In-Parameter Knowledge Injection to integrate external knowledge into the large language models. Different from the in-context learning methods that adopt natural language to represent external knowledge, the in-parameter method represents knowledge through parameters, thus avoiding length constraints and becoming more compatible with the foundation LLM.

### Strengths
The experimental results show the effectiveness of In-Parameter Knowledge Injection method on 1B, 3B, and 8B LLMs. 

The idea is novel. Embedding knowledge through model parameters will ideally represent how a LLM “understand” certain external knowledge.

### Weaknesses
1. As shown in Figure 3, knowledge can be effectively represented and understood through either natural language or parameters. So, which kind of knowledge should be integrated through parameters? More explorations and investigations are recommended here. Specifically, the paper lacks a clear delineation of the types of knowledge that benefit most from in-parameter injection versus in-context learning. The current justification relies on task complexity, but this is a rather broad criterion. A more granular analysis, perhaps based on the inherent structure or relational nature of the knowledge itself, would be beneficial. For example, is in-parameter injection more suitable for factual knowledge, while in-context learning is better for procedural knowledge, or vice versa? This distinction needs to be investigated more thoroughly.

2. The method demands additional pre-training or post-training costs. I suggest incorporating an additional baseline method where a copy of the LLM is adopted to represent the knowledge. The baseline will also demonstrate the contribution of knowledge encoding phrase. The absence of a baseline that uses a separate LLM to encode knowledge makes it difficult to isolate the impact of the proposed in-parameter injection method. It's unclear whether the performance gains are due to the specific encoding process or simply the introduction of additional parameters that have been trained on relevant data. A comparison with a baseline where a separate LLM is used to encode the knowledge, and then that encoded knowledge is used in a similar way, would help clarify this.

3. Will the In-Parameter Knowledge Injection method generalize to LLMs with a larger scale (e.g., Llama 3.1 70B Instruct, Llama 3.2 11B instruct, etc.)? It’s unclear about the exact contribution of the method, since the model scale is relatively small. The experiments are limited to relatively small models (1B, 3B, and 8B parameters). It is not clear if the observed benefits of in-parameter knowledge injection would persist with larger models, such as those with tens or hundreds of billions of parameters. It is possible that the benefits of the proposed method might diminish or even disappear as model size increases, due to the increased capacity of larger models to learn and store knowledge internally.

### Questions
See weakness

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper investigates two methods of knowledge augmentation in language models: in-context knowledge injection and in-parameter knowledge injection. In-context augmentation involves adding external information directly to the model’s input prompts, while in-parameter augmentation temporarily embeds this knowledge into the model’s parameters. Through a series of tasks with increasing complexity—ranging from fact extraction to comparative and multi-step reasoning—the study evaluates the effectiveness of both methods. The findings indicate that in-parameter injection performs better on complex reasoning tasks, whereas in-context methods are more effective for simpler fact extraction. The authors provide insights into the advantages of each approach based on task complexity and computational efficiency.

### Strengths
• Systematic Comparison: The paper offers a clear and structured comparison between in-context and in-parameter knowledge injection methods, elucidating the trade-offs in different scenarios.

• Experimental Design: The progression from simple to complex tasks effectively demonstrates how each method scales, offering insights into their applicability across various task demands.

### Weaknesses
• Limited Novelty: The in-parameter knowledge injection method is essentially LoRA with additionally synthetic augmentation. The paper does not sufficiently acknowledge this overlap or explain how its approach differs from or improves upon existing parameter-efficient fine-tuning methods.

• Insufficient Differentiation from LoRA: Given the similarities to LoRA, the paper should have provided a detailed comparison, highlighting any unique contributions or advantages. Specifically, the paper lacks a rigorous ablation study to isolate the impact of the synthetic augmentation from the core LoRA adaptation. Without this, it's difficult to ascertain whether the observed performance gains are due to the novel aspects of the method or simply the application of LoRA.

• Scope of Evaluation: The experiments focus on a limited range of tasks. Expanding the evaluation to include more diverse or real-world applications could enhance the robustness and generalizability of the conclusions. For example, the tasks are primarily fact-based and do not explore more complex scenarios such as open-ended generation or tasks requiring more nuanced understanding.

• Lack of Theoretical Advancement: The paper does not offer new theoretical insights into knowledge augmentation or parameter adaptation in language models, limiting its contribution to an empirical comparison that may already be addressed in existing literature. The work does not delve into the underlying mechanisms of how in-parameter injection affects the model's internal representations, making it difficult to generalize the findings beyond the specific experimental setup.

### Questions
1. How might in-parameter knowledge injection perform in tasks beyond fact-based reasoning, such as creative writing or dialogue generation?

2. Can the authors elaborate on how their work differentiates from previous studies on knowledge augmentation and knowledge editing in language models?

3. What challenges might arise when scaling in-parameter knowledge injection to larger models or datasets, and how could these be addressed?

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
5

### Summary
This paper studies different ways of injecting new knowledge into the LLMs. Specifically, it proposes a new way of first extracting QA pairs from contexts and then training the model with LORA using the QA pairs as a new in-parametric knowledge injection solution. Following that, this paper compares the proposed solution with the widely used in-context solution on different tasks. Experiment results show that on simpler tasks, the in-context solution is still stronger, but on more complex tasks that require complex reasoning of the updated knowledge, the proposed in-parameter solution might be helpful.

### Strengths
1. The proposed method is sound, and the introduction is clear.
2. The experiment setting is comprehensive.

### Weaknesses
The proposed solution has several bottlenecks: (1) the quality of extracted QA pairs is crucial for the effectiveness of the knowledge injection. For example, the context might contain many details, and it is unlikely that the generated QA pairs could cover all of them, so the proposed solution will lose those details. (2) LORA is a way for efficient tuning. There is no guarantee that the model learns all the knowledge in the extracted QA pairs; (3) since LORA directly changes all the parameters, this might hurt the model's performance on other tasks.

### Questions
1. How will the proposed solution hurt the model's general performance?
2. Can you present a more detailed analysis of the QA extraction quality? Especially when we do not have a strong external model, can we use the same model to do that, and how will that influence the final performance?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper discusses the differences in two kinds of ways to augment language models with external knowledge: in-context learning or in-parameter augmentation. The authors propose to use LoRA parameters tuned from QAs that are synthetically generated by language models to augment the models. Experiments on 1B-sized models show good performance on various knowledge-intensive tasks such as fact extraction and comparative reasoning.

### Strengths
1.	The topic is important and interesting. There is indeed a limitation with in-context fixed language-based knowledge. 
2.	The experiments are comprehensive, with an evaluation of various models and settings. A good number of details of the decisions and prompts are provided in the appendix. The test set suite is also good. All the tasks included are indeed relevant and require external knowledge.
3.	This paper is well-written, the paragraphs and figures are clear and easy to follow.

### Weaknesses
1. More work in the literature can be discussed in Section 2. The discussion on in-context/in-parameter knowledge injection can be improved with more details in the literature, e.g., a similar setting of parameter updates with knowledge updates is defined in the paper Fast Model Editing at Scale (Mitchell, et al., 2022). Also, much previous work on parameter-efficient fine-tuning (PEFT) is relevant but not discussed, e.g., Adapter.
2. From my understanding of the paper, the LoRA weights are tuned from QAs from the whole knowledge base. If so, what is the difference between the proposed in-parameter method and LLM-based data augmentation? This seems to limit the novelty of the method part. Also, it may influence the fairness of comparing with in-context learning. How are the exemplars chosen? Given the current framework, it can be extended to a novel method if, for each test example, you consider different LoRA weights associated with different data points, groups, and external knowledge source K. This paper may provide further intuition along this direction: https://arxiv.org/pdf/2110.04366.
3. It is quite surprising to me that in-context learning yields such bad performance on comparative tasks. It is possible that the model sizes might limit the reasoning capability. It would be good if the authors could provide the ICL performance of larger models (e.g., 70/405B Llama) as a reference or extend the IP experiments on these models.

### Questions
1.	What is the difference between in-parameter knowledge injection and knowledge editing?
2.	What is the difference between IP and LLM-based data augmentation + LoRA? If IP is not an online method where each test example is augmented with different LoRA weights?
3.	In Section 3.3, the authors mention the comparison of the complexity. Is there any comparison of IC and IP on efficiency, e.g, with FLOPs or time?


Typos:
1.	Line 50, no year in the citation; Line 516-517, wrong citation formats

### Soundness
2

### Presentation
3

### Contribution
2
