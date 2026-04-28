# LLaVA-MoD: Making LLaVA Tiny via MoE-Knowledge Distillation

- Decision: Accept
- Avg Score: 6.50
- Scores: 8, 6, 8, 5, 6, 6

## Abstract
We introduce LLaVA-MoD, a novel framework designed to enable the efficient training of small-scale Multimodal Language Models (\emph{s}-MLLM) distilling knowledge from large-scale MLLM (\emph{l}-MLLM). Our approach tackles two fundamental challenges in MLLM distillation. First, we optimize the network structure of \emph{s}-MLLM by integrating a sparse Mixture of Experts (MoE) architecture into the language model, striking a balance between computational efficiency and model expressiveness. Second, we propose a progressive knowledge transfer strategy for comprehensive knowledge transfer. This strategy begins with mimic distillation, where we minimize the Kullback-Leibler (KL) divergence between output distributions to enable \emph{s}-MLLM to emulate \emph{l}-MLLM's understanding. Following this, we introduce preference distillation via Preference Optimization (PO), where the key lies in treating \emph{l}-MLLM as the reference model. During this phase, the \emph{s}-MLLM's ability to discriminate between superior and inferior examples is significantly enhanced beyond \emph{l}-MLLM, leading to a better \emph{s}-MLLM that surpasses \emph{l}-MLLM, particularly in hallucination benchmarks.
Extensive experiments demonstrate that LLaVA-MoD surpasses existing works across various benchmarks while maintaining minimal activated parameters and low computational costs. Remarkably, LLaVA-MoD-2B surpasses Qwen-VL-Chat-7B with an average gain of 8.8\%, using merely $0.3\%$ of the training data and 23\% trainable parameters. The results underscore LLaVA-MoD's ability to effectively distill comprehensive knowledge from its teacher model, paving the way for developing efficient MLLMs.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
LLaVA-MoD introduces a framework for creating efficient small-scale multimodal language models through knowledge distillation from larger models. The approach tackles two key challenges: optimizing network structure through sparse Mixture of Experts (MoE) architecture, and implementing a progressive knowledge transfer strategy. This strategy combines mimic distillation, which transfers general and specialized knowledge, with preference distillation to reduce hallucinations. The framework represents an advancement in making multimodal language models more efficient and practical for real-world applications.

### Strengths
The technical design features a well-constructed progressive distillation strategy that combines mimic distillation for knowledge transfer with preference distillation for reducing hallucinations. The integration of MoE architecture into small-scale models is thoughtfully implemented, striking an effective balance between computational efficiency and model performance.

The empirical validation is thorough. The authors present comprehensive evaluations across multiple benchmarks, showing that LLaVA-MoD-2B not only outperforms larger models while using fewer resources, but also achieves better results in hallucination reduction compared to existing methods. The ablation studies demonstrate the contribution of each component to the overall performance.

The work also shows strong practical relevance, addressing the challenge of deploying efficient multimodal language models in resource-constrained environments. The reduction in required training data and parameters while maintaining or improving performance makes this work valuable for real-world applications.

### Weaknesses
The most significant technical constraint is the requirement that student and teacher models must belong to the same LLM family to ensure vocabulary space consistency. This limitation restricts the framework's flexibility and broader applicability. Specifically, the method requires that both models have identical vocabulary sizes and token IDs, which prevents the transfer of knowledge between models trained with different tokenization schemes. Additionally, the training process demands substantial memory resources as it requires loading both student and teacher models simultaneously, which limits the scalability of the approach, especially when using large teacher models. 

The experimental evaluation, while comprehensive in many aspects, lacks detailed analysis in key areas. The paper could benefit from a more thorough examination of inference costs and computational requirements in real-world deployment scenarios. For example, the paper does not provide a breakdown of latency, throughput, and memory usage during inference, which are critical for practical applications. There is also limited exploration of training stability across different configurations and minimal discussion of failure cases or error patterns. It is unclear how the method behaves under different hyperparameter settings or in the presence of noisy data. The paper also lacks a detailed analysis of failure modes, such as specific types of inputs that lead to poor performance or hallucinations.

The architectural exploration could be more extensive, particularly regarding different MoE configurations and alternative approaches to reducing memory requirements during training. The paper does not explore the impact of different routing algorithms or the number of experts on the overall performance and efficiency of the model. Furthermore, the paper does not investigate alternative approaches to reduce memory requirements, such as gradient checkpointing or model parallelism.

### Questions
Why does increasing the number of experts from 4 to 8 fail to improve performance, and is there a fundamental limitation in the MoE architecture?

How can the framework be modified to enable distillation between different model families, rather than requiring the same LLM family for student and teacher?

What specific mechanisms enable preference distillation to reduce hallucinations more effectively than RLHF-based methods?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper presents LLaVA-MoD, a framework for efficiently training a small-scale multimodal language model (MLLM) by distilling knowledge from a larger, more capable MLLM (I'll denote this as L for brevity). The main contributions are twofold: introducing a sparse MoE architecture for the student (I'll denote this as S for brevity) and developing a progressive distillation strategy. The MoE architecture adds multiple FFN heads with a linear routing mechanism, for efficiency and model expressiveness. The progressive distillation approach occurs in two stages: (1) mimic distillation, which minimizes KL divergence to align S’s outputs with the L’s outputs, and (2) preference distillation, which enhances the student’s ability to distinguish preference between examples, thus reducing hallucination rates. Compared to existing approaches, LLaVA-MoD is notably efficient both in terms of training data and the number of trainable parameters.

### Strengths
- The paper provides extensive experimental comparisons with prior work, especially highlighting gains in data efficiency and trainable parameters, which is a strong advantage for low-resource training.
- I found the preference distillation interesting in that it reduces hallucination. This aspect could benefit from a deeper explanation of the mechanism behind this reduction, but it’s a notable strength.
- Given the complexity of the architecture, the authors include an extensive ablation study to evaluate each component’s effectiveness, which helps to validate the design choices.

### Weaknesses
 - While training sample efficiency and the number of trainable parameters are discussed, it would be helpful to see more detail on the total parameters required for training and inference. Efficiency in trainable parameters doesn’t always translate directly to lower memory or computational costs-full backpropagation through the LLM is still necessary even if only adapter and FFN heads are updated. Information on actual memory usage or wall-clock time would give a more complete picture of the framework’s practical efficiency.
- The architecture is fairly complex, and although the authors do a good job with the explanation, some details remain a bit unclear. For example, the architectural differences between S and L could be more explicitly described to clarify distinctions. See questions

### Questions
- Since the paper emphasizes data efficiency, could you clarify how the other methods in the comparison were trained? For instance, is there any early-stopping strategy, or specific training limits set for them? And for LLaVA, how do you know that “5M” samples are enough?
Do the S and L need to be the same architecture, or is there some flexibility here? As I understand it, L is distinct from S, where S is initially trained as a dense model before introducing sparsity. Is that correct?
- For Table 1, could you clarify the comparison parameters? Are the final model sizes (S) similar across comparisons? And do the models differ in their teacher models, or is it consistent in that regard?

### Soundness
3

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
This work introduces a framework called LLaVA-MoD for building efficient small-scale multimodal large language models (MLLMs) using a sparse Mixture-of-Experts (MoE) architecture. The framework specifically applies MoE to MLP layers within transformer blocks. To preserve the capabilities of larger MLLMs while maintaining efficiency, the authors developed a specialized distillation approach combining KL divergence loss and Preference Optimization (PO) loss between the student (small) and teacher (large) models.

### Strengths
This work introduces a new framework for better tuning small-scale MLLM. This framework provides solutions in real world problems by offering a more efficient approach to model inference and deployment across diverse application scenarios.

The experiment is comprehensive, covering a wide range of tasks and models, on both general comprehension benchmarks and hallucination benchmarks. The design of s-MLLM is efficient and effective, achieving superior performance compared to other models of similar size across multiple benchmark tests. The distillation pipeline is clear and well defined. The paper is clearly written.

### Weaknesses
This work  can also be related to inference efficiency and inference acceleration. It would be good if it included inference measurements like FLOPs and inference latency showing the work’s practical benefits in deployment scenarios.

### Questions
1. There are more small-scale MLLM coming out these days with higher performance and comparable size (0.5B) [1]. Could the sparse MoD architecture and distillation strategy be applied to these newer models to further enhance their performance?

2. I am wondering about the performance of Preference Distillation vs DPO in the second stage. Does it show advantages using distillation instead of direct DPO, in terms of model performance or training efficiency?


[1] Li, Bo, et al. "Llava-onevision: Easy visual task transfer." arXiv preprint arXiv:2408.03326 (2024).

### Soundness
4

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
The paper introduces LLaVA-MoD, a framework aimed at distilling knowledge from large multimodal language models (MLLMs) to create smaller, efficient multimodal language models (s-MLLMs) that retain high performance with reduced computational requirements. LLaVA-MoD achieves this by employing a sparse Mixture of Experts (MoE) architecture to maintain expressive power while minimizing parameters. The distillation process is twofold: Mimic Distillation aligns the smaller model with the larger one through Kullback-Leibler (KL) divergence, and Preference Distillation enhances the smaller model’s ability to judge quality, outperforming the larger model on tasks prone to hallucination. Experimental results highlight LLaVA-MoD's efficiency, achieving significant performance improvements with minimal data and trainable parameters.

### Strengths
1. LLaVA-MoD achieves high performance with only a small fraction of the data and computational resources required by traditional large MLLMs. This makes it more suitable for real-world applications, especially in low-resource environments.
2. Reduced Hallucination: By incorporating preference distillation, LLaVA-MoD significantly reduces hallucination rates, making it more reliable for applications where factual accuracy is critical.
3. Flexible Architecture with MoE: The use of a sparse MoE architecture allows the model to selectively activate different "experts" for specific tasks, ensuring computational efficiency while retaining expressive power.
4. Superior Performance: LLaVA-MoD surpasses larger models like Qwen-VLChat-7B in various benchmarks, demonstrating the effectiveness of its knowledge distillation approach.

### Weaknesses
--The progressive distillation method, which includes dense-to-sparse transitions and multi-task training, could be complex to implement and tune effectively. Specifically, the transition from dense to sparse architectures during distillation introduces challenges in maintaining stable training dynamics. The multi-task training regime, while beneficial, adds further complexity in balancing the learning objectives and preventing interference between tasks. This complexity could lead to increased sensitivity to hyperparameter settings and require significant computational resources for effective tuning.
--While preference distillation enhances hallucination mitigation, it does not consistently improve the model’s comprehension capabilities, which might limit its applicability in understanding complex instructions. The focus on reducing hallucinations might come at the expense of the model's ability to accurately interpret and process nuanced or intricate instructions, potentially leading to a trade-off between factual accuracy and comprehension. This is particularly concerning in scenarios where both accurate information retrieval and complex reasoning are required.
--The effectiveness of LLaVA-MoD is heavily reliant on the quality and capacity of the teacher model. If the teacher model is limited, the distilled s-MLLM might inherit those limitations. The distillation process, while effective in transferring knowledge, is inherently constrained by the capabilities of the teacher model. Any biases, weaknesses, or limitations present in the teacher model could be propagated to the student model, potentially hindering the overall performance and generalizability of the distilled model.

### Questions
--What's the computational complexity?
--How do you address the limitation of the teacher's model?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces LLaVA-MoD, which is a framework that distills large multimodal models into efficient, small-scale ones using a sparse MoE and progressive knowledge transfer. By optimizing both model architecture and distillation strategy, LLaVA-MoD achieves high performance with minimal data and parameters, even surpassing larger models on multimodal tasks. This framework enables cost-effective deployment of high-performing models in resource-limited settings

### Strengths
- The paper combines MoE with knowledge distillation in a novel way, optimizing small multimodal models efficiently without sacrificing performance.
- The proposed method is robust, with a progressive distillation process that includes preference-based fine-tuning to mitigate hallucinations.
- The paper is well-written and clearly explains the framework.
- Experiments were done on a comprehensive set of evaluations.

### Weaknesses
 - The paper does not provide an analysis of how different MoE configurations (e.g., number of experts, routing strategies, parameter k from top-k routing) impact performance and computational trade-offs. Including such an analysis could provide further valuable insights for the model.
- The results presented in Table 2 is relatively modest in improvement. LLaVA-MoD-2B only outperforms the other 2B baselines (Imp-2B) by 2.7% on average while using twice as many data samples.

### Questions
See above in weaknesses.

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
4

### Summary
The paper proposes a framework LLaVA-MoD for distilling knowledge from large multimodal models to smaller models. The method incorporates mixture-of-experts for enhancing the expressiveness of small multimodal models. Additionally, the method uses two stage distillation -- Mimic Distillation for general knowledge alignment and Preference Distillation to enhance the student model's discriminatory capabilities for superior generalization. The experimental results are quite interesting -- The 2-billion parameter LLaVA-MoD outperforms larger models like Qwen-VL-Chat-7B by 8.8%, using only 23% of trainable parameters and 0.3% of the training data. LLaVA-MoD performs significantly well on 7 multimodal tasks and hallucination benchmarks.

### Strengths
The paper proposes a scalable approach for distilling large multimodal models to smaller one, which is a very relevant topic in recent time. The proposed methodology is somewhat novel and addresses key challenges faced by the existing small multimodal models. The experiments are extensive and performance improvement shown by the proposed methodology is significant.

### Weaknesses
1. The experimental setup is not very convincing to me. The authors claim their method to be an alternative distillation method without much empirical comparison. In order to establish the effectiveness of their method, the authors must compare some of the existing KD methods -- KD and GKD, to show why their distillation method is needed. 

2. The dense-to-sparse loss is very similar to the competitive loss proposed by Sengupta et al., 2023 [1]. The authors should show how their proposed losses differ from these losses.

3. The authors should elaborately discuss why dense vs sparse architecture works. The authors mostly report the numbers with little explanation of the how part.

4. The lower performance of Mimic+preference than mimic in Table 4 should be discussed. It is counterintuitive.

5. The authors claim that their method is efficient. More detailed analysis with training/inference time and memory should be discussed.

### Questions
See the above comments.

### Soundness
3

### Presentation
3

### Contribution
3
