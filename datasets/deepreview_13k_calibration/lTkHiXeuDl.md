# HMoRA: Making LLMs More Effective with Hierarchical Mixture of LoRA Experts

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 6

## Abstract
Recent studies have combined Mixture of Experts (MoE) and Parameter-Efficient Fine-tuning (PEFT) to fine-tune large language models (LLMs), holding excellent performance in multi-task scenarios while remaining resource-efficient. Yet, existing MoE methods still  exhibit  three major limitations: (1) Current multi-granular routing methods overlook that different LLM layers capture features at varying granularities, resulting in inefficient routing. (2) Task-level routing methods are confined to tasks encountered during training, failing to generalize to unseen tasks. (3) The lack of certainty in existing MoE routing methods hinders the specialization of the experts. To address these challenges, we propose HMoRA, aHierarchical fine-tuning method that combines MoE and LoRA, employing hybrid routing that integrates token-level and task-level routing in a hierarchical manner. This hierarchical hybrid routing allows the model to more efficiently capture both fine-grained token information and broader task contexts. To improve the certainty of expert selection, a novel routing auxiliary loss is introduced. This auxiliary function also enhances the task router's ability to differentiate tasks and its generalization to unseen tasks. Additionally, several optional lightweight designs have been proposed to significantly reduce both the number of trainable parameters and computational costs. Experimental results demonstrate that HMoRA outperforms full fine-tuning across multiple NLP benchmarks, while fine-tuning only 3.9\% of the parameters. The code is  available on: https://anonymous.4open.science/r/HMoRA-2648.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper presents HMoRA, a hierarchical fine-tuning method that combines Mixture of Experts (MoE) and LoRA for large language models. The key innovation lies in its hybrid routing mechanism, which hierarchically combines token-level and task-level routing. This allows the model to capture information at different granularities, enhancing its understanding capabilities. Additionally, a novel routing auxiliary loss is introduced to improve the certainty of expert selection and maintain a balanced selection of experts. The method also incorporates several optional lightweight designs that significantly reduce the number of trainable parameters and computational costs without sacrificing much performance.

### Strengths
The combination of hierarchical routing and the auxiliary loss function is a novel contribution. The hybrid routing that integrates token-level and task-level routing in a hierarchical manner allows the model to capture different granularities of information, which is a significant improvement over existing methods that focus on only one level of routing.

The experimental results demonstrate that HMoRA outperforms full fine-tuning across multiple NLP benchmarks while fine-tuning only a small percentage (3.9%) of the parameters. This shows the effectiveness of the proposed method in achieving good performance with limited computational resources.

The proposed optional lightweight designs are a practical addition as they significantly reduce both the number of trainable parameters and computational costs without significantly compromising performance. This makes the method more applicable in resource-constrained environments.

### Weaknesses
The paper claims that the method can generalize to unseen tasks, but the experiments and analysis related to unseen tasks could be more in-depth. There is a need for more experiments that closely mimic real-world scenarios where the model encounters truly unseen tasks.

While some ablation studies are presented, they could be more comprehensive. For example, for aspects like the hierarchical routing shown in Figure 2(a), more investigation could be done on where exactly to best divide the shallow and deep layers for optimal performance.

### Questions
-How well does the method perform on a more diverse set of unseen tasks? Are there any specific characteristics of tasks that might affect its generalization ability? Could the authors provide more details on how the model's performance on unseen tasks was evaluated? What metrics were used and how were the unseen tasks selected?

-Regarding the hierarchical routing in Figure 2(a), what are the criteria for determining the optimal division between shallow and deep layers? How sensitive is the model's performance to this division?

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
2

### Summary
The paper introduces HMoRA (Hierarchical Mixture of LoRA Experts), presenting a significant advancement in fine-tuning LLMs by effectively combining MoE and LoRA with innovative hierarchical routing and auxiliary loss mechanisms. This approach not only improves multi-task performance and expert specialization but also ensures parameter and computational efficiency, making it a promising technique for scalable and versatile natural language processing applications.

### Strengths
-  HMoRA successfully combines Mixture of Experts (MoE) with Parameter-Efficient Fine-Tuning (PEFT) methods like LoRA. This integration enables the model to outperform traditional fine-tuning approaches when handling a wide range of tasks. By utilizing specialized experts, HMoRA enhances the model’s ability to generalize across multiple tasks, resulting in outstanding performance on various natural language processing benchmarks.

- One of the standout features of HMoRA is its ability to achieve high performance by fine-tuning only 3.9% of the model’s parameters. This significant reduction in trainable parameters greatly decreases the computational and memory overhead compared to full parameter fine-tuning. Consequently, HMoRA proves to be an exceptionally efficient method for deploying large-scale models in environments with limited resources.

- The paper is well-written, presenting its concepts and methodologies clearly. Additionally, it showcases sufficient innovation, contributing novel ideas and approaches to the field of large language model fine-tuning.

### Weaknesses
 - The experiments presented in the paper were primarily conducted using the Qwen2 1.5B model and did not extend to larger-scale models (such as those with hundreds of billions of parameters) or to different architectural frameworks. As a result, the scalability and effectiveness of HMoRA on larger or alternative types of LLMs remain unclear.

- Furthermore, although the introduction of lightweight designs is commendable, HMoRA still requires additional computational resources to manage hybrid routing and auxiliary loss functions. However, this increase is understandable given the overall efficiency improvements, and I would not place undue criticism on this aspect.

- Additionally, the auxiliary loss function involves setting multiple hyperparameters (such as γb and γc), which adds complexity to effective tuning across various tasks and datasets. Has there been any investigation into how these hyperparameters impact the ablation studies, and what parameter tuning techniques were employed?

### Questions
See weaknesses. Since I am not a researcher in this field, I cannot be certain that the questions I have raised are correct

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
3

### Summary
This paper introduces a hierarchical method, HMoRA, for effective fine-tuning. Specifically, HMoRA integrates token-level and task-level routing to combine MoE and LoRA and utilizes a routing auxiliary loss to improve the certainty of expert selections. Experimental results show that HMoRA outperforms full fine-tuning and some other baseline methods.

### Strengths
1. The paper is well-organized and easy to read with clear explanations of the technical details.
2. The approach is straightforward but performs good performance. The hybrid routing that combines token-level and task-level routing is innovative and allows the model to capture multi-granularity information. 
3. It is intuitive to apply Generalized Jensen-Shannon divergence for router selection. The experiment results also demonstrate the effectiveness of the auxiliary loss.
4. The overall experimental results show the effectiveness and the potential of the proposed method.

### Weaknesses
1. Yet the method shows promising performance in this paper, its novelty is limited in my opinion. The task-level MoE and GJS divergence is not a new topic in MoE or noisy learning areas.
2. The description of task-level routing is somewhat vague. In Figure 2, the inputs include T^in and T^tg. Are these two distinct tasks? How are they set up during training and evaluation?
3. The task representation is encoded based on a task embedding, how can it expand into new tasks? In addition, task routing is a crucial method component, yet there appears to be no ablation experiment focused on task routing within the experiments conducted.

### Questions
See Weaknesses.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
In this paper, authors target at the routing problem in existing MoE methods: data granularity used by MoE layer and the generalization to unseen task and expert specialization. The authors introduced HMoRA, a method combining MoE and LoRA used to fine tune LLMs. It includes a hybrid routing strategy that incorporates token-level and task-level routing. They redesign the routing auxiliary loss, and employ lightweight designs to reduce parameters and computational costs.

### Strengths
1. The experiments to validate the idea are well designed and thoroughly covers most of the scenarios.

### Weaknesses
1. Presentation could be further improved. I feel like the appendix C and D are also important contributions for this idea. However, the organization of the paper make it difficult to identify what is the key contribution and insight of the proposed approach.
2. The idea of mixture of lora and using MoE for both token routing and task routing is not new. I do think a highlight of clear difference between HMoRA and this line of work should be added.


### Questions
1. It seems all the components are somehow disconnected. A lot of efforts are put on introducing the new gating algorithm. How is related to apply MoE to LoRa and enable MoE to both token and tasking routing. I feel like the gating algorithm is a separate problem.

### Soundness
2

### Presentation
2

### Contribution
2
