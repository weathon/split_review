# Knowledge And Capability Transfer Through Large Language Models' Parameters Fusing

- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 6, 8, 6

## Abstract
The post-training phase of large language models (LLMs) plays a pivotal role in refining models to follow instructions and align with human preferences. However, this phase is fraught with challenges, particularly in sourcing high-quality post-training data. This paper introduces a novel approach, termed Parameters Fusing, that simplifies the post-training process by amalgamating model parameters delta from existing instruct-tuned checkpoints with a new base model tailored to specific domain data obtained by continual pre-training. Utilizing open-weight models such as Meta's Llama, our method replicates the effects of the traditional post-training phase while significantly reducing both time and resource costs. This approach not only minimizes the challenges of post-training data acquisition but also provides a flexible and efficient framework for enhancing LLMs with domain-specific knowledge or capabilities.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces an innovative approach for post-training large language models (LLMs) through "Parameters Fusing," a method that fuses model parameters from instruct-tuned checkpoints into a newly pre-trained model. The goal is to replicate post-training effects without the extensive time and resource costs typically required. By leveraging parameter deltas, the authors enable the efficient transfer of domain-specific knowledge and model capabilities, showcasing the model's ability to maintain or enhance performance across multiple benchmarks. Experiments validate that fusing models can rival or even exceed the effectiveness of traditional post-trained models.

### Strengths
- The paper clearly explains the challenges of post-training and the need for efficient knowledge transfer, establishing a strong foundation for the introduction of Parameters Fusing.
- The "Parameters Fusing" approach is a creative and resource-efficient alternative to conventional post-training, presenting a valuable technique for the efficient transfer of knowledge in LLMs.
- The paper includes rigorous experiments across multiple benchmarks, which provide clear empirical support for the proposed method's performance and efficiency.
- By using open-weight models like Llama, the authors demonstrate an adaptable approach that can be widely applied across different models and domains.
- The paper offers a well-structured theoretical grounding, discussing the relationships among model parameters, training steps, and knowledge acquisition.

### Weaknesses
 - The study could benefit from comparisons with other parameter-efficient methods in addition to traditional post-training, such as adapter-based or LoRA methods, to contextualize its performance and efficiency.
-  It is unclear if Parameters Fusing will perform as effectively on larger models. Expanding the analysis to address scalability and potential limitations in diverse applications would strengthen the paper.
- While the paper focuses on Llama models, it does not fully address whether the approach is model-agnostic or if any adjustments would be necessary for different architectures.
- The approach may introduce a risk of overfitting in highly specialized domains. Including an analysis of model generalizability when exposed to new or unseen tasks would improve the robustness of the findings.
- Although Parameters Fusing is efficient, there is limited discussion about interpretability and potential risks (e.g., model degradation) when applying delta parameters from various sources.

### Questions
- There is minimal discussion on the risks of model degradation when fusing parameters from multiple sources, especially when domain mismatches or conflicting knowledge bases are involved. Investigating and reporting any observed performance declines, conflicts in fused knowledge, or mitigation strategies would strengthen the paper.

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
4

### Summary
This paper introduces a novel post-training approach termed "Parameters Fusing" designed to simplify the transfer of knowledge and capabilities in large language models (LLMs) during the post-training phase. Traditional post-training requires extensive high-quality data and significant resource consumption. This research innovatively achieves the effects of the post-training phase by merging parameter deltas from existing instruct-tuned models with a newly pre-trained base model, thereby enhancing instruction-following capabilities and domain-specific knowledge without conventional post-training.

### Strengths
1.	Innovation: The "Parameters Fusing" approach leverages parameter deltas to achieve post-training effects, representing an innovative advancement over traditional methods which requires high-quality training data.
2.	Cost effectiveness: This method significantly reduces post-training costs, making model customization more economical and efficient.
3.	Flexibility: Parameter delta operations allow freedom within homologous models, enabling fine-tuning across characteristics like coding ability and tool usage.
4.	Experiments: Experimental results show that fused models perform excellently across benchmarks, approaching or even exceeding traditional post-trained models, validating the method's effectiveness.

### Weaknesses
1.	Potential Performance Limitations: In some benchmarks, fused models slightly underperform compared to traditional post-trained models, indicating potential limitations in transfer efficiency. This is particularly concerning when considering the computational overhead of large language models; even small performance degradations can be significant in practical applications. The paper should include a more detailed analysis of these performance differences, including statistical significance tests and a breakdown of performance across different task types.
2.	Experimental Transparency: Certain experimental details, particularly criteria for choosing different parameter delta combinations and the implementation process, are insufficiently detailed, potentially affecting reproducibility. The paper lacks a clear explanation of how the parameter deltas were extracted, what specific layers were included, and how the fusion was performed at the tensor level. Without this information, it is difficult for other researchers to replicate the results or build upon this work.
3.	Lack of Adaptive Delta Selection: The method relies on manual tuning of delta combinations, which increases costs and limits flexibility. The absence of an automated or principled approach to selecting which deltas to combine, and how to weight them, represents a significant limitation. This manual process is not scalable and may not lead to optimal performance, especially when dealing with a large number of potential source models.

### Questions
Please refer to the weakness

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper introduces a novel approach, parameter fusing, which simplifies knowledge and capability transfer in large language models (LLMs) by integrating parameter deltas—the differences between instruct-tuned and base model checkpoints—into a new base model. This technique allows LLMs to incorporate specialized skills or domain-specific knowledge without the need for resource-intensive post-training phases. Parameter Fusing is grounded in the observation that performance improvements correlate with a concave relationship to changes in parameters, suggesting diminishing returns as models approach an optimal performance plateau. This relationship was validated through comprehensive experiments, showing that parameter fusion not only matches but can sometimes enhance the effects of traditional post-training. By leveraging open models, such as Meta’s Llama, this method enables efficient and flexible customization of LLMs, significantly reducing costs and time associated with conventional fine-tuning while ensuring adaptability for diverse applications.

### Strengths
This work builds on prior research in parameter aggregation but offers fresh insights and significant contributions. Notably, it presents an intriguing hypothesis that links performance gains to parameter changes—a relationship convincingly supported by experimental results. Beyond its theoretical contributions, the paper demonstrates a practical application for its proposed Parameter Fusing approach: when LLMs require continual pretraining to acquire specialized skills or domain-specific knowledge, Parameter Fusing offers a resource-efficient alternative to traditional post-training. The experimental outcomes are promising, validating the method's effectiveness. Overall, this paper introduces a novel perspective on post-pretraining, with potential for wide-reaching applications in future research. It is poised to make a meaningful impact on the LLM research community.

### Weaknesses
My major concern is that there lacks a quantitative evaluation to evaluate if the new knowledge in a continual pretrained model will be preserved in the fused model. In the current experiments, this validation is achieved by showing merely one example in Table 4. More concrete results should be provided in the main experiment section. Specifically, the paper lacks a systematic evaluation across a diverse set of tasks or datasets to rigorously assess the retention of knowledge after parameter fusion. The current evaluation relies on a single example, which is insufficient to draw broad conclusions about the efficacy of the proposed method in preserving learned information. Furthermore, it is unclear how the fused model performs on tasks that require a combination of the original base model's knowledge and the new, specialized knowledge acquired during continual pretraining. A more comprehensive evaluation should include metrics that specifically measure the degree to which both types of knowledge are retained and utilized effectively.

### Questions
When fusing parameters from different checkpoints, is there any criteria that can be used to select the most effective parameter deltas?

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes to use the change of model parameters for representing the knowledge learned by LLMs. The core idea is to perform a weight averaging operation for pre-trained and post-trained model parameters. It is discovered that such weight averaging leads to comparable results.

### Strengths
- The idea itself is interesting;

- The method is straightforward, easy to follow.

- The results provide some insights on how to transfer pre-trained LLMs to a new task/domain: if we have a pretrained LLM $f$, and two other checkpoints, one ($g_1$) is pretrained, the other ($g_2$) is post-trained on the new domain, then we can adapt f to this new domain by $f + (g_2 - g_1)$.

### Weaknesses
 - The method itself is simple, but the presentation needs substantial improvements. Now the presentation makes the paper seem complicated. The core ideas are clear and easy to follow, but the writing is confusing with so many long subscriptions in equations. For example, $\theta_{model_i-pretrain}, \theta_{post-train-llama3.1-8b}$ are redundant expressions, making readers more confusing.
  
- Moreover, the figures are so small. The x and y labels are hard to see. It is highly recommended that the authors improve the representation of equations, and provide a straightforward illustration of their method by figures. This is also an effect of too long subscriptions.

- The empirical improvements are marginal (Figs 1, 2, Tabs 1, 2). The current results fail to provide useful insights or surprising ovservations. It is recommended that the authors show some scenarios where existing post-trained models cannot achieve very good results, yet the proposed method easily outperform them with simple parameter fusing.

### Questions
- To my understanding, the technical novelty is limited. Parameter fusing is performed via valinna operations. Simplicity is a strength, but the technical novelty is lacking, given that the obtained results are not very promising (the improvements are marginal). Although I'm not an expert on LLMs, it could be easily found that the method requires naive addition/subtractions on the whole model parameters. Therefore, I cannot accurately assess the value of the proposed parameter fusing approach. It is recommended that the authors elaborate on how their approach differs from or improves upon existing parameter fusion techniques in the context of LLMs.

- What if $f$ and $g_1$ are pre-trained on different domains (the notations is from the strength part)? Does the method assume that both of them have already be pre-trained on a variety of data, and share some common knowledge?

### Soundness
2

### Presentation
1

### Contribution
2
