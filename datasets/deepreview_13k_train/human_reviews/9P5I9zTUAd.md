# Mixture-of-Instructions: Aligning Large Language Models via Mixture Prompting

- Decision: Reject
- Scores: 6, 5, 3, 6, 3

## Abstract
With the proliferation of large language models (LLMs), the comprehensive alignment of such models across multiple tasks has emerged as a critical area of research. Existing alignment methodologies primarily address single task, such as multi-turn dialogue, coding, mathematical problem-solving, and tool usage. However, AI-driven products that leverage language models usually necessitate a fusion of these abilities to function effectively in real-world scenarios. Moreover, the considerable computational resources required for proper alignment of LLMs underscore the need for a more robust, efficient, and encompassing approach to multi-task alignment, ensuring improved generative performance. In response to these challenges, we introduce a novel technique termed Mixture-of-Instructions (MoI), which employs a strategy of instruction packing combined with diverse system prompts to boost the alignment efficiency of language models. We have also compiled a diverse set of seven benchmark datasets to rigorously evaluate the alignment efficacy of the MoI-enhanced language model. Our methodology was applied to the open-source Qwen-7B-chat model, culminating in the development of Qwen-SFT-MoI. This enhanced model demonstrates significant advancements in generative capabilities across coding, mathematics, and tool use tasks.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces a technique known as Mixture-of-Instructions (MoI) for improving the alignment efficiency of large language models (LLMs) across multiple tasks. The technique uses instruction packing and diverse system prompts to enhance the model's performance. The authors applied this methodology to the Qwen-7B-chat model, resulting in the development of Qwen-SFT-MoI, which showed significant improvements in tasks like coding, mathematics, and tool use. The paper contributes by identifying and addressing conflicts between new and old knowledge during SFT, introducing the MoI method for joint multi-task training, and demonstrating the effectiveness of the MoI in enhancing SFT models.

### Strengths
1) The authors effectively identify a gap in existing alignment methodologies that typically focus on single task and propose a multi-task solution that is particularly relevant for AI-driven products. 
2) The authors also provide a comprehensive evaluation of their method using seven benchmark datasets, demonstrating its effectiveness. The resulting model, Qwen-SFT-MoI, shows significant improvements in generative capabilities across multiple tasks. 
3) The paper is well-written and clear in its presentation of the methodology and results. The work is significant as it offers a practical solution to a key challenge in the field of AI, namely the efficient alignment of LLMs for multi-task performance.

### Weaknesses
The primary concern revolves around the originality. The suggested MoI method incorporates several techniques, such as a distinct system prompt for each task, balanced sampling, and chunk-based attention. However, these techniques have already been introduced in previous research. For instance, the significance of the prompt for SFT has been highlighted by "Keeping llms aligned after fine-tuning: The crucial role of prompt templates, Lyu et al., 2024" and "Reducing the cost: Cross-prompt pre-finetuning for short answer scoring, Funayama et al., 2023". The technique of balanced sampling has been employed by "Sampling bias and class imbalance in maximum-likelihood logistic regression, Oommen et al., 2011", and the concept of chunk-based attention has been put forth by "Shifted chunk encoder for transformer based streaming end-to-end ASR, Wang et al., 2022" and "Statistically defined visual chunks engage object-based attention, Lengyel et al., 2021".

Considering these techniques are not innovative, the method seems more of an engineering blend if it fails to offer fresh perspectives or intriguing discoveries. Nevertheless, the positive outcomes and comprehensive experiments render the work robust and beneficial for the industrial sector.

### Questions
LN038: How did you come to the conclusion that the model generates less than ideal solutions due to conflicts in prompt-induced knowledge? Is there any research or experimental evidence to back this up?

LN040: Can you explain why modifying prompts can help in resolving knowledge conflicts?

LN085: What is the approach you use to identify conflicts between new and old knowledge during SFT? I couldn't find this information in section 2.

LN099: Are there any previous studies that highlight the significance of system prompts? If so, you should reference them and compare your method to theirs to demonstrate its superiority. If you're the first to do this, it's also worth mentioning.

LN470: The main focus of this study is multi-task learning, but I don't see a thorough discussion or comparison with existing methods.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper addresses a practical issue on multi-task supervised fine tuning (SFT). In order the model to be trained propoerly on all the tasks they propose packing the instructions belonging to different tasks in a balanced fashion. This results in superior performance on a number of tasks.

### Strengths
This is a clever and practical idea. The impact of this is clearly presented and I appreciate the comprehensive paper with many analyses.

### Weaknesses
However I feel like it may not constitute a full ICLR paper. Instead in the model system card, this could have been mentioned in a paragraph. For example Llama or Olmo model system cards have similar technical details like this.

### Questions
- Does the idea work for existing open SFT tuned models like Llama
- Does the idea apply to all model sizes and task categories?

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper introduces a Mixture-of-Instructions (MOI) strategy, which combines instruction packing with diverse system prompts to enhance multiple downstream tasks. The multi-task training technique is applied to a Qwen-7B-Chat model, which demonstrates good performance in mathematical reasoning, code generation, tool usage, and chat benchmark.

### Strengths
1. The proposed strategy is straightforward and easy to follow yet achieves competitive performance against many open-source models. It can be effective guidance for SFT training and data utilization.

2. The experiments and ablation studies are comprehensive, which can clearly reflect the effectiveness of the method and explain how it works.

### Weaknesses
1. The novelty is limited. The idea of Mixture of Instructions has already been explored by the works of FLAN serious. Packing multiple samples into a single one and balanced sampling are also common strategies employed by many works, as cited in the paper. The main innovation of this work is the chunk-based packing and attention mask. However, the effectiveness and generalization of this strategy are still not clear when the model size and task numbers increase in the view of the scaling law.

2. In each chunk, the instructions are packed and reordered. One concern is whether the models would be sensitive to the order of instructions. Have the authors ever explored the influence of different orders of the packed instructions in the chunk?

3. The extensibility of this strategy is not clear. The work has tried four tasks, namely mathematical reasoning, code generation, tool usage, and daily chat. When the task number increases, does this strategy still work? If the length of packed instructions exceeds the maximum sequence length, e.g., 4096 in llama, how can we solve this issue?

4. The description of the system prompt is somewhat confusing. In Section 2.4, the authors say that unique system prompts for each domain-specific task are set to ensure tailored guidance. However, in Table 1, they highlight that for all benchmark computations, they consistently use the system prompt "You are a helpful assistant." How can these conflict statements be understood? Does that mean the system prompts are different in training and testing?

5. In section 2.2, the authors mention that training on combined data can lead to model bias toward certain tasks, enhancing performance in some while degrading it in others. This is related to the studies of catastrophic forgetting [1,2], which should be discussed in the related work or compared as baselines.

### Questions
See above.

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
4

### Summary
This paper introduces Mixture-of-Instructions (MoI), a novel methodology aimed at enhancing the alignment of large language models (LLMs) across multiple tasks through a combination of instruction balanced packing and diverse system prompts. Traditional alignment methods focus on single tasks, which limits the effectiveness of LLMs in real-world, multi-faceted applications. To address this, the authors propose MoI, which assigns unique system prompts to different tasks and integrates them into a unified instruction set, facilitating comprehensive multi-task training. The approach is evaluated using seven benchmark datasets encompassing mathematics, programming, tool usage, common sense, and dialogue, demonstrating significant improvements in generative performance. The methodology is applied to the open-source Qwen-7B-chat model, resulting in the enhanced Qwen-SFT-MoI model, which outperforms existing models across various benchmarks.

### Strengths
**1. Important Research Questions**

The paper addresses the critical challenge of multi-task alignment in LLMs, which is increasingly relevant given the diverse applications of AI-driven products. By focusing on harmonizing various capabilities—such as coding, mathematical reasoning, and multi-turn dialogues—the study tackles the complex interplay between different task domains, which is essential for creating versatile and reliable language models.

**2. Rich Experiments and Evaluations**

The authors conduct extensive experiments across seven diverse benchmark datasets, including MT-Bench, HumanEval, MBPP, MATH, GSM8K, MMLU, and T-EVAL. This comprehensive evaluation framework ensures that the proposed MoI methodology is rigorously tested across multiple domains, demonstrating its efficacy in improving generative performance. Additionally, ablation studies and comparisons with existing models underscore the robustness of the approach.

**3. Carefully Crafted Implementation Details**

The introduction of chunk-based attention masking is a meticulous enhancement that addresses the issue of attention cross-contamination during multi-task training. Coupled with balanced sampling techniques, these implementation strategies effectively mitigate dataset biases and ensure that the model maintains high performance across all tasks. The detailed explanation of the loss function modifications further showcases the depth of the methodological advancements.

### Weaknesses
 **1. Lack of Explanation on MoI's Absence of System Leading to Performance Degradation**

The paper briefly touches upon the performance decline observed when not using the chunk-based attention masking but fails to delve deeply into the underlying reasons. A more thorough analysis or theoretical justification for why the absence of a system prompt within MoI leads to performance degradation would provide greater clarity and strengthen the argument for the proposed solution. Specifically, the paper lacks a discussion on how the system prompt interacts with the attention mechanism and why its absence causes a drop in performance. It would be beneficial to explore whether the system prompt acts as a crucial anchor for the model's attention, guiding it towards relevant parts of the input sequence, and how this anchoring is disrupted when the prompt is removed. Furthermore, the paper should investigate if the performance degradation is uniform across all tasks or if certain tasks are more sensitive to the absence of a system prompt, which could provide insights into the nature of the prompt's role in different task domains.

**2. Insufficient Exploration of Long Input and Output Scenarios**

While the study effectively evaluates MoI on various tasks, it overlooks scenarios that involve prolonged inputs and outputs, such as Retrieval-Augmented Generation (RAG) and long-form text creation. Including these cases would offer a more comprehensive understanding of how MoI performs under conditions that demand handling of extensive contextual information and sustained generation over longer sequences. The paper should include experiments that specifically test the model's ability to maintain coherence and relevance over extended sequences, as well as its capacity to integrate retrieved information effectively in RAG settings. This would involve evaluating metrics such as coherence, consistency, and the accuracy of information integration, which are essential for real-world applications that require handling complex and lengthy inputs and outputs.

**3. Lack of Evaluation on Larger-Scale Models**

The experiments are primarily conducted on the Qwen-7B-chat model and smaller variants. Testing the MoI methodology on larger models with more parameters (like Qwen-72B or Qwen-MoE) would provide insights into its scalability and effectiveness in more powerful architectures. This omission leaves a gap in understanding how MoI can be generalized to state-of-the-art LLMs with significantly higher capacities. The paper needs to address whether the benefits of MoI are maintained or diminished when applied to models with significantly larger parameter counts, and if the training process requires adjustments to accommodate the increased complexity of these models. Furthermore, the paper should explore if the computational cost of applying MoI scales linearly or exponentially with model size, which is crucial for practical deployment of the methodology.

### Questions
1. See the weakness section. Maybe elaborate more on your opinions about point 1.

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
4

### Summary
This paper proposes a method called Mixture-of-Instructions (MoI), which employs a strategy of instruction packing combined with diverse system prompts to boost the alignment efficiency of language models. The methods mainly include balanced instruction packing and chunk-based attention. The experimental results show that the methods can enhance the ability of cross-domain tasks by multi-task learning.
In addition, this authors also conduct some experiments on the impact of system prompt for different tasks and find that system prompt matters.

### Strengths
1. The research scope of this work, how to perform multi-task learning in SFT is indeed key to LLMs.

2. The proposed method is simple and easy to implement. Researchers would love to replicates this work if they believe the reported results of this work.

3. This paper employs some benchmarks and visualization analysis to demonstrate its effectiveness, which enhances the readers' comprehensive understanding of this work.

### Weaknesses
1. The chunk-based attention, packing the data and unmasking attention across different tasks, is quite unreasonable from intuition. Isolated attention is for removing unrelated contexts and full attention is for efficiency. So what is the motivation of the chunk-based attention? Moreover, some related works (Zhao et al, 2024) that this paper has even cited have pointed out that similar samples should be packed together to enhance the final performance. However, this work, chooses the opposite way, unmask the attention across different tasks in a chunk. What is the motivation and why is it better? This concern could become more important to me when I see the coding ability gets greatly enhanced by MoI compared to balanced packing, which is kind of magic to me.

* PS: I don't think the paragraph "Why is MoI effective?" can convince me. The paragraph only points out that the attention of MoI in SFT is significantly different from one in Chat, which is quite natural and normal (in my opinion) if we unmask the attention between different instructions. I expect more essential reasons, that is, why the altered attention distribution is more useful rather than more useless?

2. The contribution (or motivation) listed in line 085-087 seems contradictive to the actual implementation in MoI, which uses a unified "Assistant" system prompt. The authors emphasize that the system prompt is important (and conduct some experiments to prove this) but finally adopt a simple "Assistant" system prompt in their proposed model. What is the connection between them?

3. In fact, many SFT training samples have their own specific system prompts rather than a simple sentence "You are ....". Moreover, the huge impact (sensitivity) of system prompt seems well-known by LLM/NLP community. From my perspective, the exploration about system prompt in this work is kind of shallow and the possible insight is limited.

### Questions
1. How do you control balance when the numbers of samples of different tasks are different? And according to Table 9, the numbers of samples are indeed unbalanced. How do you order them? Conversely, if the balanced packing required the same number of samples across all tasks, that would bring out a great limitation.

2. The system prompt part is confusing for me. Why do you always adopt the unified "Assistant" system prompt for all tasks in MoI model rather than different system prompts? What system prompt do you use for other baseline models in training and inference?  I strongly recommand a table to present the system prompts in training and inference stages for each model.

3. What is the difference between "Isolated attention mask" in Table 8 and "Qwen-SFT-balanced" in Table 1? Why are the results not the same?

### Soundness
2

### Presentation
2

### Contribution
2
