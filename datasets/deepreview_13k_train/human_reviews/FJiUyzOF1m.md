# Bayesian Low-rank Adaptation for Large Language Models

- Decision: Accept
- Scores: 6, 6, 6, 8

## Abstract
Low-rank adaptation (LoRA) has emerged as a new paradigm for cost-efficient fine-tuning of large language models (LLMs). However, fine-tuned LLMs often become overconfident especially when fine-tuned on small datasets. Bayesian methods, with their inherent ability to estimate uncertainty, serve as potent tools to mitigate overconfidence and enhance calibration. In this work, we introduce Laplace-LoRA, which applies a Bayesian approach to the LoRA parameters. Specifically, Laplace-LoRA applies a Laplace approximation to the posterior over the LoRA parameters, considerably improving the calibration of fine-tuned LLMs.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
A Bayesian LoRA approach has been proposed to fine-tune large language models (LMMs) by estimating the weight posterior through layer-wise Laplace approximation. Experiment results on six QA benchmark datasets were provided in terms of accuracy, calibration, and OOD generalization, compared with three baseline methods.

### Strengths
- **Timely research**: The proposed method focuses on improving the calibration performance when finetuning LLMs on small-scale datasets, which is an important and urgent research problem along with the rapid growth of large models. 

- **Clear Bayesian treatment**: The proposed method adopts well-established techniques from prior works of Bayesian neural networks and uncertainty reasoning, and successfully incorporates such a Bayesian treatment into parameter-efficient tuning approaches. The proposed Laplace-LoRA seems to be a scalable solution to enable uncertainty estimation for large models.

- **Good experiment design**: Despite some practical issues (see *weakness*), the experiment was conducted well on six public datasets with several strong baseline methods, in terms of three settings -- 1) early stopping, 2) finetuning with validation, and 3) OOD generalization. The proposed method generally achieves better ECE scores across different cases.

### Weaknesses
 - **Unclear uncertainty estimation**: While the proposed Laplace-LoRA naturally estimates the weight posterior, it is unclear how to apply the proposed method to compute model uncertainties. Specifically, the paper does not detail how the approximated posterior over LoRA weights translates into a predictive distribution over the output logits, which is crucial for calibration. It remains unclear if the proposed method can handle the structured uncertainty estimation for next-token predictions (e.g., *Uncertainty estimation in autoregressive structured prediction, ICLR'21*). It would also be interesting to compare the proposed method with semantic uncertainty [Kuhn et al., ICLR'23].
- **Lack of LLM backbones**: The empirical evidence of the proposed method is somewhat weak due to the lack of more LLM backbones. Some concerns include: 1) can the proposed Laplace-LoRA work with larger model sizes (e.g., 13B, 70B)? 2) Can Laplace-LoRA be applied to models other than LLaMA2 (e.g., Mistral 7B, GPT-2, etc.)? The current experiments are limited to LLaMA2 models, which raises questions about the general applicability of the method across different architectures and scales.
- **Comparison to ensemble**: Besides the checkpoint ensemble, it is also expected to implement a baseline given by the LoRA ensemble (similar to the deep ensemble approach). The absence of this comparison makes it difficult to assess whether the performance gains are due to the Bayesian treatment or simply an ensemble effect.

### Questions
Please refer to the questions raised in *Weaknesses*.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces Laplace-LoRA, a Bayesian inference method designed specifically for the LoRA parameters in LLM fine-tuning using a post-hoc Laplace approximation. They conducted extensive experiments on six commonsense reasoning tasks and show dramatic improvements in calibration of fine-tuned LLMs.

### Strengths
1. This idea of combining Laplace inference with the fine-tuning LLMs using LoRA adapters is novel, which provides a new way of doing Bayesian fine-tuning on LLMs.
2. They conducted extensive experiments on six commonsense reasoning tasks under in/out-of-distribution settings and provided detailed analysis of the experiment results.
3. The writing is well-structured, clear and easy to understand.

### Weaknesses
1. It has some novelty, but not dramatic, because both Laplace Approximation and LoRA method are well-studied.
2. It is quite weird that the Section 3 Background followed by Section 4 Results directly, without a Method section in between. Maybe it needs a better section name.

### Questions
Does free-text generation tasks (e.g., free-from QA) still work under this framework? Why that kind of reasoning tasks are not considered in your experiments?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper presented a Bayesian approach to improve the calibration of LoRA. It adopted Laplace approximation to the posterior of the low rank parameters. Empirical results on both in-distribution and out-distribution finetuning indicated the Bayesian approach does improve the calibration and the proposed Laplace approximation outperform a variety of baseline methods.

### Strengths
1. This paper is the first to present a comprehensive result on using Laplace approximation to LoRA for LLMs.
2. This paper has clear presentation with visualization.
3. Claims are supported with sufficient amount of convincing experiment result. e.g., smaller datasets experience larger difference in ECE compares with larger datasets.

### Weaknesses
1. Limited novelty. The Bayesian method part (as indicated in the paper) is well explored in the literatures listed in the software paper Laplace Redux [1]. This paper can be viewed as empirical results applying [1] to a specific model - LoRA for LLMs. 
2. Majority of the benefits of Laplace-LoRA including ''post-hoc'' and ''scalable'' are from the existing method, which limits the contribution of this work. This one together with Weakness #1 above are the major concerns from my point of view.
3. There was some discussion on the cost to perform Laplace approximation when introducing Fasher. However, there is no empirical results that support it.
4. The ablation study (LLLA vs LA) is also from the [1]. Only comparing LA with Last Layer LA is not very convincing on where the uncertainty comes from.

### Questions
1. Laplace Redux has discussion on relative wall-clock time cost and memory consumption comparison with other methods, is there similar result for Laplace-LoRA?
2. More ablation study is expected. For example, LA on different types of layers (attention, dense, etc.), LA on different layers and different number of layers (first k layers or random select layers), or some fusion of the two mentioned above.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposed a new fine-tuning procedure based on LoRA using Bayesian prospective.

### Strengths
This paper is very well-written and the algorithm is presented in a very clean way. Although the algorithm is straightforward, as far as I know, nobody has made it work before. The empirical analysis is done carefully which is appreciated. Code is also linked.

### Weaknesses
1. It looks like all the tasks using in this paper are still classification tasks. How it is different from standard Bayesian deep learning evaluation? I want to understand where the benefit is coming from on those eval metrics through a principled way. I feel it will be good to comment some potential on generation tasks that can reflect more of the autoregressive nature of transformers.

2. Where is the comparison of computational complexity and memory usage? How much additional memory you will use?

### Questions
See above.

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
4 excellent
