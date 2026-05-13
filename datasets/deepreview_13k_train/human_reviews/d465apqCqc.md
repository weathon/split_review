# BA-LoRA: Bias-Alleviating Low-Rank Adaptation to Mitigate Catastrophic Inheritance in Large Language Models

- Decision: Reject
- Scores: 6, 8, 3, 3, 8

## Abstract
Large language models (LLMs) have demonstrated remarkable proficiency across various natural language processing (NLP) tasks. However, adapting LLMs to downstream applications requires computationally intensive and memory-demanding fine-tuning procedures. To alleviate these burdens, parameter-efficient fine-tuning (PEFT) techniques have emerged as a promising approach to tailor LLMs with minimal computational overhead. While PEFT methods offer substantial advantages, they do not fully address the pervasive issue of bias propagation from pre-training data. This work introduces Bias-Alleviating Low-Rank Adaptation (BA-LoRA), a novel PEFT method designed to counteract bias inheritance. BA-LoRA incorporates three distinct regularization terms: (1) a consistency regularizer, (2) a diversity regularizer, and (3) a singular value decomposition regularizer. These regularizers aim to enhance the models' consistency, diversity, and generalization capabilities during fine-tuning. We conduct extensive experiments on natural language understanding (NLU) and natural language generation (NLG) tasks using prominent LLMs such as LLaMA, Mistral, and Gemma. The results demonstrate that BA-LoRA outperforms LoRA and its state-of-the-art variants. Moreover, our method effectively mitigates the adverse effects of pre-training bias, leading to more reliable and robust model outputs.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces Bias-Alleviating Low-Rank Adaptation (BA-LoRA) with three regularization terms: (1) a consistency regularizer, (2) a diversity regularizer, and (3) a singular value decomposition regularizer. They conduct experiments on natural language understanding and natural language generation tasks, and the results demonstrate that BA-LoRA outperforms LoRA and PiSSA.

### Strengths
Three regularization terms are proposed for LoRA to mitigate the detrimental effects of Catastrophic Inheritance from pre-training.

The paper conducts experiments on natural language understanding and natural language generation tasks with serveral benchmarks and LLMs.

### Weaknesses
The experiments are not sufficient, which only compare limited baselines, but ignore many relevant methods, such as DoRA, LoHA, DyLoRA, DeltaLoRA, which are mentioned in related works. The paper does not provide enough evidence to support its claim that BA-LoRA outperforms LoRA and its state-of-the-art variants.

In the experiments, according to Table 1 and 2, why Full FT has worse performance than PEFT method?

The discussion about why these three regularization terms can mitigate the detrimental effects of Catastrophic Inheritance is not sufficient.

In my option, these regularization terms should be universally applicable. That is to say, the regularization terms should be added to LoRA’s variants, and improve their performance. More experiments should be conducted for this.

In section 3, why PISSA is described in such detail, is it highly relevant to BA-LoRA?

### Questions
See the weaknesses.

### Soundness
2

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
This paper investigates the challenges associated with fine-tuning large language models (LLMs), particularly focusing on catastrophic forgetting and bias introduction. It introduces BA-LoRA, a method aimed at improving the adaptation of LLMs while minimizing computational costs. The authors highlight the issue of catastrophic inheritance, where models lose previous knowledge when trained on new tasks. BA-LoRA employs a low-rank adaptation technique, allowing for efficient parameter updates during fine-tuning. Experimental results demonstrate that this approach effectively mitigates forgetting and reduces bias in adapted models, outperforming traditional fine-tuning methods. The findings suggest that BA-LoRA represents a significant step forward in making LLM adaptation more efficient and reliable for various natural language processing applications.

### Strengths
A regularization formula for LoRA training was proposed for NLU and NLG tasks respectively, and excellent improvement was achieved in model performance.

### Weaknesses
1.Ablation experiments need to supplement the experimental results of  Ltask_NLG and  Ltask_NLU to enrich Figure 2.


2.According to the results in Figure 2, Ldr_NLG improves LlaMA-2-7B more significantly than Gemma-7B. Is the " while LDR_NLG had a notably strong impact on Gemma-7B." in the text inconsistent with the picture information?


3.Why can we conclude that 'BA-LoRA can effectively alleviate the impact of imbalanced data in pre-training' based on Figure 1 and the observation that 'BA-LoRA in sub-figures (b) and (d) shows clearer category separation'? What is the relationship between these two observations?

### Questions
See Weaknesses

### Soundness
3

### Presentation
3

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
In this paper, authors proposed a BA-LoRA, which focuses on mitigating the bias propagation issue from the pertaining data used for different LLMs. BA-LoRA includes three different regularization loss functions regarding NLG and NLU tasks, i.e., a consistency regularizer, a diversity regularizer, and a singular value decomposition regularizer to enhance model's consistency, diversity and generalization during fine-tuning. BA-LoRA was evaluated on different NLG and NLU datasets using different LLMs, such as LLaMA 2 7B, Gemma 7B, and some encoder-only LMs, such as BERT-Large, RoBERTa-Large, which demonstrates the better performance of BA-LoRA.

### Strengths
- BA-LoRA designed 3 different regularizations in terms of consistency, diversity and generalization for NLG and NLU datasets based on the principle singular values and singular vectors adaptation (PISSA), respectively.
- Based on the experiment results, BA-LoRA improves several baselines on NLG and NLU datasets.

### Weaknesses
 - The definition of noise and imbalance in this work is not clear regarding different NLG and NLU datasets
- It lacks enough baselines to compare in terms of "Catastrophic Inheritance", especially for the noise and imbalance on the NLG and NLU datasets.
- BA-LoRA needs adapted regularization terms designed for NLG and NLU tasks, which might bring generalization concerns for this BA-LoRA if it is applied to other tasks that are not discussed in this paper, such as classification task.

### Questions
- As mentioned in the weakness section, this work highlights the catastrophic inheritance issue in the pertaining data, which is not better solved by other LoRAs. However, this work did not provide a clear definition of what kinds of noise and imbalance issues this work will consider. Especially, authors claim that BA-LoRA effectively mitigates the adverse effect of Catastrophic Inheritance, fostering consistent, diverse and generalized model outputs in line 379 section 4.4.1 based on the results of Tables 1 and 2. As the definition is unclear, it is hard to directly conclude that all credits for improvements from Tables 1 and 2 can be given to noise and imbalance mitigation. We need to see more examples that BA-LoRA can actually mitigate the specific noise and imbalance issues.
- In Table1, it is not clear that what kind of metric is used to evaluate the performance in NLG tasks.
- In section 4.3, the values of $\lambda_1$, $\lambda_2$, and $\lambda_3$ for NLG and NLU tasks are so small. Do these values bring enough contributions to the entire loss function?
- In sections 4.4.2 and 4.4.3, there are only results and analyses on NLU datasets. More results on both tasks are needed to better demonstrate the ability of BA-LoRA

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper addresses the issues of bias and catastrophic inheritance, proposing several loss components based on prior studies to regularize LLMs. It includes experiments demonstrating the method's superiority over regular LoRA, PiSSA, and full fine-tuning without regularization.

### Strengths
The regularization of LLMs is a crucial area of study, and the proposed techniques have a strong foundation with clear descriptions. 

The paper is well-written, and the experiments are notable, including recent benchmarks like MT-Bench.

### Weaknesses
 **The baselines are insufficient.**

While LoRA and PiSSA are included, they lack any regularization. As stated in the paper, dropout is set to 0, meaning there is no regularization within the layers for these baselines, nor is there any weight decay applied. Consequently, the baselines may easily collapse due to the choice of hyperparameters. As it stands, it's unclear whether the gains from your method could simply be achieved by incorporating weight decay and optimized dropout.

The lack of regularization is further evident from the fact that full fine-tuning performs worse than LoRA. While isolated cases of this behavior might occur, it shouldn’t be a consistent trend; otherwise, tuning the entire network would serve little purpose.

**Novelty**

Regarding novelty, regularization has been an extensively studied topic. Although the paper cites works on entropy, KL regularization, and spectral regularization, there is an implication that these are novel contributions, which they are not. If these regularizers have been previously studied, they should be included as baselines. This approach would essentially frame the study as an adaptation of these regularizers to LLMs and a combination of them, without showing each individually. Thus, it appears there is limited novelty beyond incremental adaptations and combinations tailored for LLMs.

**Computational Costs**

The computational costs appear to counteract the main advantage of PEFT. For instance, consistency regularization requires an additional forward pass and doubles the storage for activations. The diversity component is somewhat manageable, but the SVD aspect raises concerns. Based on my knowledge and experience, computing all eigenvalues, particularly for large matrices, can be significantly time-consuming. This is further complicated by being a CPU-bound task, which limits parallelization. For example, the smallest matrix in LLaMA is 4096x4096, requiring roughly 5 seconds to compute, and this is just the smallest case. It raises serious doubts about the practical scalability of this approach.

**Catastrophic Inheritance**

I doubt that bias and catastrophic inheritance were truly assessed. According to the paper, it is simply done by using models that were "probably" trained on noisy data, such as BERT and GPT-2. Moreover, they are outdated and not commonly used in current applications. Improvements in final scores do not necessarily indicate any effective handling of biases.

Regarding MNLI, it’s unclear how it is described as imbalanced. The official dataset on Hugging Face has an equal distribution across classes, so any claims about imbalance need clarification.

### Questions
There seems to be no clear difference between spectral regularization applied to NLU and NLG tasks. And what is the overall need to distinguish between them? Why do we need to target them separately?

### Soundness
1

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper proposes BA-LoRA, a parameter-efficient fine-tuning method to mitigate the catastrophic inheritance issue in LLMs. Key contributions include (1) three regularization terms for bias mitigation, (2) optimized adaptation methods for NLU/NLG tasks, and (3) comprehensive evaluations across various models and benchmarks.

### Strengths
This paper addresses an essential issue for the practical deployment of large language models (LLMs) by proposing BA-LoRA, a parameter-efficient fine-tuning method aimed at mitigating catastrophic inheritance problems. 

The motivation is clear and timely, given the growing demand for efficient fine-tuning techniques in LLMs. The work introduces technical innovations, including a novel combination of regularization strategies tailored to handle task-specific characteristics in natural language understanding (NLU) and natural language generation (NLG). 

The method effectively integrates with existing LoRA frameworks, enhancing its applicability and relevance. Experimental validation is thorough, covering various models and demonstrating substantial performance improvements over baseline approaches. The analysis is supported by detailed component studies and persuasive qualitative analysis, including t-SNE visualizations, which further illustrate the effectiveness of BA-LoRA.

### Weaknesses
However, the paper has some limitations in terms of theoretical analysis, experimental scope, and comparative analysis. 

Theoretical analysis is lacking, with no clear basis for the selection of regularization weights and limited discussion on computational complexity and convergence. 

The experimental scope is restricted, as the study only tests on English datasets, leaving the method's performance in multilingual contexts unexplored( and also other tasks as well ). Additionally, the analysis of computational overhead is minimal.

### Questions
How do you determine the optimal values for the regularization weights (λ1, λ2, λ3)?
What is the computational overhead compared to standard LoRA?
How does the performance fare on non-English datasets or other NLP tasks?
Have you tested the effects on other types of bias beyond those mentioned in the paper?

### Soundness
4

### Presentation
3

### Contribution
3
