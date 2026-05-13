# Data-adaptive Differentially Private Prompt Synthesis for In-Context Learning

- Decision: Accept
- Scores: 8, 6, 6, 6

## Abstract
Large Language Models (LLMs) rely on the contextual information embedded in examples/ demonstrations to perform in-context learning (ICL). To mitigate the risk of LLMs potentially leaking private information contained in examples in the prompt, we introduce a novel data-adaptive differentially private algorithm called {\bf AdaDPSyn} to generate synthetic examples from the private dataset and then use these synthetic examples to perform ICL. The objective of AdaDPSyn is to adaptively adjust the noise level in the data synthesis mechanism according to the inherent statistical properties of the data, thereby preserving high ICL accuracy while maintaining formal differential privacy guarantees. A key innovation in AdaDPSyn is the {\it Precision-Focused Iterative Radius Reduction} technique, which dynamically refines the aggregation radius - the scope of data grouping for noise addition - based on patterns observed in data clustering, thereby minimizing the amount of additive noise. We conduct extensive experiments on standard benchmarks and compare AdaDPSyn with DP few-shot generation algorithm \citep{tang2023privacy}. The experiments demonstrate that AdaDPSyn not only outperforms DP few-shot generation, but also maintains high accuracy levels close to those of non-private baselines, providing an effective solution for ICL with privacy protection.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
In this work, the authors focus on the privacy problem involved in potential leakage of in-context learning (ICL) examples for LLMs. Building on the prior work in the literature, the authors introduce a novel data-adaptive differentially private (DP) algorithm that can generate synthetic samples from the private dataset to be used in the ICL framework. Their extensive empirical studies demonstrate that this novel approach significantly improves prior work and also gets very close to the non-private ICL baselines.

### Strengths
The paper is well organized and focus on an important problem in privacy where jailbreaks attempts on LLMs can lead to the leakage of prompt which can lead to the leakage of private data samples presented in the prompt as few-shot manner.

Their approach is a novel improvement of prior work by making the synthetic generation of tokens "data-adaptive" as opposed to applying the same amount of noise as in the prior work.

This approach results in significant improvements in the private ICL performance as shown in a wide range of empirical studies and also gets close to the non-private ICL baselines.

### Weaknesses
I don't have too much to say here. I think it'd be informative to investigate the trade-offs between directly DP fine-tuning and generating synthetic ICL samples with DP but I think that's beyond the scope of this paper.

### Questions
Is there any good intuition on how to best divide the overall privacy budget across the privacy-consuming steps of Algorithm 1?

### Soundness
4

### Presentation
4

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
The paper presents AdaDPSyn, a novel data-adaptive differentially private algorithm designed to generate synthetic examples from a private dataset for in-context learning (ICL) with large language models (LLMs). To prevent potential leakage of private information in the examples used for ICL, AdaDPSyn adjusts the noise level (introduced by differential privacy) during data synthesis based on the statistical properties of the dataset. This adjustment ensures high ICL accuracy while adhering to differential privacy guarantees. A key innovation is the Precision-Focused Iterative Radius Reduction technique, which dynamically refines the noise aggregation radius by analyzing data clustering patterns, effectively reducing additive noise.

### Strengths
S1: Experiments demonstrate that AdaDPSyn outperforms the baseline of 'DP few-shot generation'.

S2: The paper is well-written, and the ideas are easy to follow.

### Weaknesses
W1: Only one baseline was considered, specifically "DP few-shot generation."

W2: If I am not mistaken, the iterative aspect is not utilized significantly, as $\hat{T}$ is frequently set to 1.

### Questions
Please refer to section 'Weaknesses'.

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
4

### Summary
This work focuses on mitigating privacy leakage during in-context learning of LLMs. To do this, they take an existing DP ICL framework from Tang et al., 2023 and include a data-adaptive step during private aggregation. The key idea is that the majority of the output distributions can be clustered together via a ball with some radius R which can be utilized as the local sensitivity. The authors scale the Guassian noise with a differentially private estimate of R. Their experimental results demonstrate that this data-adaptive step boosts the utility over the original framework.

### Strengths
1. The paper tackles an important problem of preserving privacy during In-Context Learning of LLMs.
2. I believe the direction of data-adaptive techniques to improve privacy-utility tradeoffs of DP algorithms is important for broader adoption of DP
3. Their proposed technique is technically interesting 
4. The paper is well-written, and the analysis seems sound. In particular, I appreciate that the authors use the Amplification by subsampling theorem (Wang et al., 2019) in their analysis, which is the correct amplification to use as opposed to Poisson subsampling used by Tang et al., 2023.

### Weaknesses
1. Although the data-adaptive technique is novel, the work relies heavily on the framework introduced by Tang et al., 2023. Seemingly, author’s overall contribution is only a modification on top of an existing DP generation framework by adding a data-adaptive technique to the private aggregation step.
2. Their method introduces 4 more parameters, $\hat{T}, \lambda, \sigma_0, \sigma_2$, than Tang et al., 2023, which requires additional hyperparameter tunning on other datasets. Furthermore, the authors do not provide ablation studies on $\sigma_0, \sigma_2$ which makes it difficult to interpret their effect on the privacy-utility tradeoff. 
3. I’m a bit confused about some of the experimental setup. Why did the authors use only a pre-trained, open-weight model in their evaluations, but additionally included two instruction fine-tuned, closed-source models in their ablation? Could you provide results for the instruction fine-tuned Llama-2-7b model?
4. What about the zero-shot performance for GPT-3.5 Turbo and GPT-4o mini in the varying LLMs ablation?
5. The ablation studies are insufficient. For varying LLMs, it would be nice to compare LLMs of similar scale, e.g. Llama-2-7b vs gemma-7b. I’m unsure if GPT-3.5 Turbo and GPT-4o mini are even on the same parameter scale as Llama-2-7b. Moreover, another ablation like varying model size similar to Tang et al., 2023 is missing.

### Questions
1. What were the center values and how were the center values chosen for the experiments in Table 1?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This work introduces AdaDPSyn to safeguard sensitive data used in LLM prompts in the ICL process. A hypothesis that the next-token predictions by different examples approximately reach a consensus is verified and used to motivate the DP guaranteed in-context sample synthesis in an adaptive manner.

### Strengths
This paper developed a dynamic method to obfuscate real private samples to DP guaranteed private sample from being leaked by the LLM during ICL. They dynamic radius update for privately aggregation is interesting although the idea of replace real sample with its DP version is widely applied.

### Weaknesses
1. An amount of M queries needs to be made for synthesizing one DP in-context sample. This is of high computation cost. I would like to see some of the computational cost analysis, including the time cost comparison with baselines used in the paper.
2. The comparison of generated DP samples and real private samples are not adequate. Only DP samples of epsilon=4 is shown without direct comparison with private samples. Results of epsilon of other values as well their comparison with private samples should be included.

3. The paper does not explore the impact of varying epsilon values on the quality of the generated DP samples and the downstream ICL performance. It is unclear if the chosen epsilon value is optimal or if smaller epsilon values would significantly degrade performance and sample quality. Further investigation into the relationship between epsilon and the utility of the generated samples is needed.


### Questions
I am wondering, sine the goal of this paper is "to mitigate the risk of LLMs potentially leaking private information contained in examples in the prompt", if an example is used as in-context learning samples and sent to the LLMs, why should its privacy issue be considered? The sender party already knows the sample, and the LLM sees the sample. So who should be stopped from seeing the sample?

### Soundness
3

### Presentation
3

### Contribution
2
