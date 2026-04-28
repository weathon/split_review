# Unified Parameter-Efficient Unlearning for LLMs

- Decision: Accept
- Avg Score: 7.00
- Scores: 8, 8, 6, 6

## Abstract
The advent of Large Language Models (LLMs) has revolutionized natural language processing, enabling advanced understanding and reasoning capabilities across a variety of tasks. Fine-tuning these models for specific domains, particularly through Parameter-Efficient Fine-Tuning (PEFT) strategies like LoRA, has become a prevalent practice due to its efficiency. However, this raises significant privacy and security concerns, as models may inadvertently retain and disseminate sensitive or undesirable information. To address these issues, we introduce a novel instance-wise unlearning framework, LLMEraser, which systematically categorizes unlearning tasks and applies precise parameter adjustments using influence functions. Unlike traditional unlearning techniques that are often limited in scope and require extensive retraining, LLMEraser is designed to handle a broad spectrum of unlearning tasks without compromising model performance. Extensive experiments on benchmark datasets demonstrate that LLMEraser excels in efficiently managing various unlearning scenarios while maintaining the overall integrity and efficacy of the models.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper suggest a unified and feasible way to address multiple unlearning scenarios under a single framework. It first generalizes three unlearning objectives. Then, proposes to use influence-functions to approximate the influence of datapoints requested to be unlearned. It then proposed to use PEFT to avoid full finetuning of the model, by training each adapter separately.

### Strengths
The paper unifies three unlearning objective under a single simple framework.
The paper directly addresses the complexity concerns the framework seems to have in two simple ways: using fast Hessian-vector product, and using mini-batches. It then provides a convincing argument for why such problem formulation would converge using SGD.

### Weaknesses
The paper is a bit hard to read. I would suggest putting most equations in the appendix and focus on high-level explanation in the body of the paper. It is unclear exactly what exactly how adapters are used in Algorithm 1. The evaluation is a bit limited, consider comparing this method performance to other unlearning approaches. Evaluating efficiency in seconds can be a nice addition but the main evaluation should compare an asymptotic running-time complexity.

In the limitation section is mentioned a limited due to "first-order Taylor expansion", but I thought influence functions rely on second order expansion, which one is it?

### Questions
In the limitation section is mentioned a limited due to "first-order Taylor expansion", but I thought influence functions rely on second order expansion, which one is it?

### Soundness
4

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper introduce a novel instance-wise unlearning method that utilizes influence functions to adjusting parameters for unlearning tasks. Specifically, the method can remove specific sample from the training dataset, adjust input tokens in user queries, as well as correct model response. Experimental results show that the method can perform unlearning tasks with high accuracy while ensuring efficiency.

### Strengths
1. The problem is important and interesting. The three unlearning tasks are practical and meaningful in real-world settings.

2. The unlearning approach edits model parameters based on influence functions, which avoids finetuning or re-training the models

3. The evaluations are comprehensive. 

4. The writing is clear and easy to follow.

### Weaknesses
My concern is mainly about evaluation datasets. 

1. Although the paper claims to address privacy concerns in LLMs, the authors primarily evaluated the method using tabular datasets for recommendation tasks and a multimodal dataset for a classification task. While these tasks are representative, they are relatively simple and straightforward. Although the authors applied prompt engineering to those data, the training data are still very similar. 

2. In real AI applications, LLMs are used for text generation more often, and the training data consists of documents from various sources and may contain sensitive information, such as bank accounts, addresses, and SSNs. Thus, this paper lacks evaluations in more practical and meaningful scenarios that would better demonstrate its effectiveness in addressing privacy concerns in real-world settings.

### Questions
see weakness. Also, how is the performance of the method on text-generation tasks? Could you evaluate your approach on some QA datasets?

### Soundness
3

### Presentation
4

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
This paper studies machine unlearning for parameter-efficient fine-tuning (PEFT) of large language models (LLM). The authors first propose a framework called LLMEraser for three different unlearning tasks: instance removal, query modification, and response correction. The core of LLMEraser is based on the influence function, based on which the algorithm can minimize the effect of the removed or modified samples. Some experiment results are presented to show the effectiveness of the proposed algorithm.

### Strengths
1) The paper shows the motivation and derivation of the proposed algorithm/framework.
2) The proposed algorithm demonstrates that it can effectively maintain good performance on different tasks, including recommendation and relation mining tasks.
3) The proposed algorithm is also shown to have high efficiency compared to the existing algorithms.

### Weaknesses
1) All the experiments show how well the models can perform after unlearning a certain amount of training samples. However, it seems the paper does not present or compare how effectively the algorithms can let the model "forget" those training samples, which is the original goal of the unlearning algorithm. Specifically, there is a lack of evaluation on how much the model's behavior changes with respect to the removed data, such as measuring the drop in performance on the removed samples or the change in model output for those samples.
2) As PEFT is fine-tuning the model, it is unclear how to distinguish the influence of a sample when it is in the fine-tuning training set or the pre-training training set. When the sample was also used in the pre-training set, it is also unclear whether it is reasonable to require the PEFT to eliminate those 
3) The experiment settings in the paper do not include the generative tasks of LLMs. It is crucial to evaluate the unlearning performance on generative tasks, as these are a core capability of LLMs and may exhibit different unlearning characteristics compared to classification or regression tasks.
4) Some minor typos, such as "handling handle" near the end of page 9.

### Questions
1) How effectively can the proposed algorithm let the model forget the samples?
2) How effectively can the proposed algorithm maintain the model performance on generative tasks?
3) If a sample is also used in the pre-training, can it still be unlearned? 
4) How can we tell whether the unlearning (or failure to unlearn) is on the PEFT module but not on the pre-trained model?

### Soundness
2

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
This paper introduces LLMEraser, a unified framework for parameter-efficient unlearning in large language models (LLMs), specifically tailored to address privacy and security concerns in domain-specific fine-tuning. The framework utilizes influence functions to perform instance-wise unlearning tasks such as instance removal, query modification, and response correction. LLMEraser allows unlearning without requiring full model retraining, and has demonstrated efficacy in preserving model performance across various unlearning tasks.

### Strengths
1. The paper is written clearly and is easy to follow, with clearly presented formulations.
2. The taxonomy of unlearning tasks is well-defined, providing clarity on the types of unlearning scenarios addressed. 
3. Extensive experiments are conducted across diverse unlearning tasks with both LLMs and MLLMs, covering recommendation and multimodal relation mining applications. 
4. LLMEraser accelerates the computation of the inverse Hessian-vector-product in the influence function, enabling efficient implementations. This improvement is valuable for LLM applications, where computational efficiency is a growing concern.

### Weaknesses
1. While LLMEraser reduces the need for retraining, the memory-intensive computation of inverse Hessian-vector products remains demanding. This requirement may limit scalability, particularly for very large models or environments with limited GPU memory. The paper does not provide a detailed analysis of the memory footprint, especially concerning the storage of intermediate gradients and Hessian approximations, which are critical for large language models. The method's reliance on iterative solvers for the inverse Hessian-vector product, while avoiding explicit matrix inversion, still necessitates storing and updating these approximations, potentially leading to significant memory overhead.
2. The method’s reliance on first-order Taylor expansion in influence functions can introduce estimation errors. A lack of detailed error analysis makes it difficult to assess the impact of these errors, especially in tasks requiring high unlearning precision. The paper does not thoroughly investigate how the approximation error scales with the magnitude of the perturbation or the curvature of the loss landscape. This is particularly concerning given the non-convex nature of LLM loss functions, where first-order approximations may be inadequate.
3. Limited generalizability is a concern, as the LLM experiments primarily focus on LLMs for recommendation (LLM4Rec). Broader evaluation across more diverse LLM unlearning tasks would strengthen the claims. The current experiments do not explore the method's performance on tasks such as text generation, question answering, or summarization, which are common applications of LLMs. This narrow focus limits the understanding of the method's applicability across different LLM use cases.
4. Key experimental details, such as PEFT configurations and the number of trainable parameters, are not fully provided. These details are essential for evaluating the method's complexity and efficacy across different settings. The paper lacks specific information on the LoRA rank, the number of trainable parameters, and the optimization settings used for fine-tuning. This lack of detail makes it difficult to reproduce the results and assess the method's sensitivity to these hyperparameters.

### Questions
1. Could the authors provide a detailed analysis of estimation errors to demonstrate their impact on performance? Given the importance of precision in unlearning tasks, such an analysis would help establish whether the errors introduced by the method are indeed within an acceptable range and do not significantly detract from the efficacy of LLMEraser in high-precision unlearning scenarios.

2. The LLM4Rec unlearning tasks are different from those unlearning tasks used in the baseline paper. Could the authors provide performance results on additional unlearning tasks more closely aligned with those proposed in other baselines? Additionally, how do the LLM4Rec tasks reflect the generalizability of LLMEraser across diverse unlearning scenarios? 

3. While LoRA was used in the experiments, it would be helpful to know the specific experimental setup, including the number of trainable parameters. Since computational complexity is directly related to the number of trainable parameters and rank values in LoRA, could the authors clarify these settings and present results across different ranks? Additionally, could they specify the sample sizes used in unlearning experiments, as sample size likely affects the overall complexity?

4. While the method demonstrates computational efficiency, I am concerned about memory efficiency, particularly for broader applications. Could the authors provide an analysis of the memory cost and specify whether LLMEraser could run on a lower-memory GPU than an Nvidia A100? If the method is limited to high-memory GPUs, this could hinder its practical application. A comparison of memory usage with baseline methods is also important to clarify this point.

I would be happy to engage with the authors to help improve the presentation of the method and evaluation, but my concerns are not insignificant. Clarifications would need to resolve my questions in order for my score to improve.

### Soundness
3

### Presentation
3

### Contribution
3
