# DLP-LoRA: Efficient Task-Specific LoRA Fusion with a Dynamic, Lightweight Plugin for Large Language Models

- Decision: Reject
- Scores: 3, 3, 3

## Abstract
Recent advancements in Large Language Models (LLMs) have achieved robust performance across diverse tasks, but fine-tuning these models for specific domains remains resource-intensive. Parameter-Efficient Fine-Tuning (PEFT) methods like Low-Rank Adaptation (LoRA) address this challenge by fine-tuning a small subset of parameters. However, existing methods for fusing multiple LoRAs lack dynamic fusion based on contextual inputs and often increase inference time due to token-level operations. We propose DLP-LoRA, a Dynamic Lightweight Plugin that employs a mini-MLP module with only 5M parameters to dynamically fuse multiple LoRAs at the sentence level using top-$p$ sampling strategies. This approach reduces inference time to less than twice that of single LoRA inference by leveraging parallel computation. Evaluations across 26 tasks—including multiple-choice questions and question answering—demonstrate that DLP-LoRA achieves an average accuracy of 92.34\% on multiple-choice datasets and significant improvements in BLEU and ROUGE scores on QA datasets, outperforming different LLMs backbones under composite task settings. DLP-LoRA effectively balances performance and efficiency, making it a practical solution for dynamic multi-task adaptation in LLMs.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper proposes a method to dynamically fuse pre-trained task-specific LoRA modules. The idea is to train a sentence-level router for different tasks, and simply use that for routing and fusing different LoRA modules. The method is evaluated on both classification and language generation tasks such as QA.

### Strengths
1. the paper is addressing an important problem in efficiently re-using expert modules. The proposed method is more efficient since it uses sentence-level routing, and it is evaluated on various classification and language generation tasks.
2. the paper also includes discussions on inference efficiency, which is very relevant to the practical usage of the method.

### Weaknesses
1. the paper lacks important baselines. the routing module is trained jointly on N tasks, so the method assumes that one has access to all the task-specific training data for each LoRA module. Therefore, the authors should compare to a joint multitask training LoRA setting where the LoRA module is optimized on all task data. Note that the LoRA for joint multitask training should have a larger rank so that the number of tunable parameters is equivalent to tuning individual LoRA modules for each task.
2. the results in table 1 shows that the proposed method is worse than baselines for classification, but it's better for generation tasks in table 2. However, there is not enough explanation or intuition on why that's the case.
3. there are some highly relevant work on compositional LoRA with sentence-level routing that's not cited: https://aclanthology.org/2023.eacl-main.49.pdf, https://arxiv.org/abs/2402.17934

### Questions
1. how does your method compares to tuning a LoRA module with a higher rank on all multitask training data?

### Soundness
1

### Presentation
2

### Contribution
1

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper focuses on achieving a more efficient dynamic fusion of multiple LoRA experts in multi-task adaptation for LLMs. To this end, the authors propose DLP LoRA, which operates as a sentence-level Mixture-of-Experts MoE gating mechanism. Specifically, a pre-trained task classifier is used to obtain the probability distribution of the input sentence across various tasks, and then the gating mechanism fuses selected LoRAs filtered by a fixed probability threshold. Additionally, the paper presents a parallel CUDA acceleration strategy to improve inference efficiency. Experiments are conducted on 26 tasks adaptation, achieving performance comparable to single-task LoRA.

### Strengths
1. The paper provides a deeper exploration into previous methods for dynamically fusing multiple LoRA experts and attempts incremental improvements.

2. The topic investigated in this paper has considerable application value.

### Weaknesses
1. The proposed DLP-LoRA is largely incremental and lacks sufficient novelty.

2. The experimental evaluation is unconvincing: 1）The baselines in Tables 1, 2, and 3 are weak and insufficient, and the authors should consider introducing relevant methods from this field for comparison; 2）The paper emphasizes the proposed methodʼs efficiency advantages, yet lacks quantitative experiments on efficiency compared to single LoRA inference and previous methods.

3. There are some issues in the writing that reflect a lack of rigor: 1）The paper incorrectly refers to top-p sampling; to my knowledge, top-p sampling restricts the candidate set based on cumulative probability thresholds, whereas the paper independently filters LoRA experts below a fixed probability threshold, which is inconsistent; 2）The introduction claims that previous methods require additional fine-tuning when tasks change, yet DLP-LoRA seems unable to solve this problem either.

### Questions
1. The paper repeatedly emphasizes that the proposed method achieves less than twice the inference time of single LoRA inference; Is there quantitative experimental data to support this claim?

2. Why does Table 5 compare the LLaMA-2 13B with a smaller, fine-tuned LLM? From an inference speed perspective, a smaller LLM outperforming a larger LLM is expected; from a performance perspective, a fine-tuned model outperforming an un-fine-tuned model is also expected. Is this a fair comparison?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
- The study proposes a dynamic lightweight plugin to fuse multiple LoRA adapters that enable the adaptation of language models to specific downstream tasks and new data domains.
- The proposed approach involves a “mini-MLP plugin” that combines the weights of multiple LoRA modules based on the contextual information provided by the language model input.
- The authors DLP method aims to improve efficiency over token-level LoRA mixture approaches by utilizing sentence-level representations. The performance benchmark indicates that their DLP-LoRA method achieves similar performance to single task-specific LoRA modules.

### Strengths
- The evaluation across 26 diverse tasks including multiple choice questions, question answering, summarization, translation is quite extensive. They include ablation studies evaluating inference time and contrast model size and performance results.
- The authors clearly describe the benefits of their proposed DLP-LoRA method.
- the performance evaluation includes multiple medium-sized decoder-only language models with Llama and Qwen

### Weaknesses
 - The differences to related methods are not clear or not specifically evaluated in regards to their performance or efficiency contribution. How does the approach differ methodologically from i.e. PHATGOOSE [1], or LoRAMoE [2] and how does the performance differ?
- The authors list various mixture of expert methods in their related works and introduction, but only include single LoRAs and the base model in their benchmark results. This makes it difficult to assess the true benefits of the proposed method compared to other LoRA mixture approaches.
- Some claims remain unsupported by the empirical results presented in the study. The authors mention that additional fine-tuning for new tasks is not required in their DLP framework, yet there is no performance benchmark on unseen tasks. Furthermore, they describe the framework as lightweight but lack the parameter and space complexity comparison with related LoRA mixture approaches. The parameter count of the mini-MLP is mentioned, but not the overall parameter increase compared to other methods.
- The description of their proposed method lacks details regarding the training of the LoRA modules that are combined to perform the downstream tasks. It is unclear if these LoRAs are trained jointly or independently, and what data is used for their training.

### Questions
- Are the single LoRAs included in the selection of different LoRA modules DLP is combining?
- Can you elaborate why the performance of multiple LoRA modules combined through your DLP method, which include the single task-specific LoRA module, is similar or worse than the single-LoRA module?
- The inference time comparisons in Table 4 are not explained in the caption. Metric and reference time is missing.
- Section 5 lists selecting adapters based on their relevance vs. fixed k as a key limitation of related work. Do you have empirical results that support this claim for your DLP method?
- Can you elaborate on the differences between the base model performances in Table 1? Specifically, Llama 3 8b seems to perform significantly better than Llama 2, and both Qwen models.

### Soundness
2

### Presentation
2

### Contribution
2
