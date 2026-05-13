# CITER: Collaborative Inference for Efficient Large Language Model Decoding with Token-Level Routing

- Decision: Reject
- Scores: 3, 5, 6, 5

## Abstract
Large language models (LLMs) have achieved remarkable success in natural language processing tasks but suffer from high computational costs during inference, limiting their deployment in latency-constrained applications. To address this issue, we propose a novel \textbf{C}ollaborative \textbf{I}nference with \textbf{T}oken-l\textbf{E}vel \textbf{R}outing (CITER) framework that introduces a token-level routing mechanism, enabling efficient collaboration between small and large language models (SLMs \& LLMs). Specifically, CITER enables routing non-critical tokens to an SLM to reduce computational overhead, while critical tokens are processed by an LLM to maintain generation quality. We formulate the training of the router as a reinforcement learning task, where the router receives rewards based on both the quality of predictions and the inference cost of generation. This allows the router to learn to predict token-level routing scores and make routing decisions based on both the current token and the future impact of its decisions. To further accelerate reward evaluation process, we introduce a shortcut for reward function estimation, significantly reducing the cost of the reward estimation and improving the practicality of our approach. Extensive experiments across four benchmark datasets demonstrate that CITER reduces inference cost while preserving high-quality generation, offering a promising solution for real-time and resource-constrained applications.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper proposes a routing process to combine an LLM and a SLM to improve efficiency while do not sacrifice accuracy.

### Strengths
The proposed method is sound, and positive results are demonstrated across multiple benchmarks.

### Weaknesses
1) At least from my option, I don't see significant advantages (differences) over existing collaborative decoding methods. For example, this paper cites the co-LLM, what is the core difference and what is the core difference between this work and the work by UW yejin's team?

2) only one policy is used (QWen)

3) paper is not clear to read, you do not need so many equations for sections like 2.1.2.

I'm open to upgrade my score if the paper is significantly improved.

### Questions
1) what is the core difference and what is the core difference between this work and the work by UW yejin's team?

2) what the situation for Llama3?

3) what is a more specific reason for iteratively updating the router since your method is a inference method where LLM and SLM are fixed.

4) do you train specific router for each benchmark tested?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
Large language models (LLMs) perform exceptionally well in natural language processing tasks; however, their computational costs during the inference phase are extremely high, especially in real-time applications. Existing approaches primarily address this issue by routing entire user queries to different models, a method that lacks flexibility and often results in inefficiency. To tackle this problem, the authors propose a novel framework—Collaborative Inference with Token-level Routing (CITER)—which achieves a balance between efficiency and accuracy by predicting token importance and routing tokens to the appropriate model. The authors formalize the training of the router as a reinforcement learning problem and introduce a shortcut for reward function estimation to accelerate the training process.

### Strengths
1. The token-level routing framework for collaborative inference is quite novel. The idea of using small language models to collaboratively generate tokens in order to reduce the inference generation of large language models is very interesting for accelerating model inference speed.

2. The experimental design for evaluating the CITER framework's inference acceleration is comprehensive and rich, with thorough experimental evaluations conducted across multiple benchmark datasets.

### Weaknesses
1. The paper only conducts experiments with the Qwen series of models. If the model were switched to the Llama3 series, would the CITER architecture still be able to achieve rapid inference with large models?

2. The generality of the rapid convergence of the iterative training process is not supported by detailed evidence, which undermines the validity of the iterative training approach.

### Questions
Since I do not have much knowledge about inference acceleration methods, I am curious about how the method proposed in this paper should be compared with existing non-token-level inference acceleration frameworks.

### Soundness
2

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
The paper introduces Collaborative Inference with Token-level Routing a framework designed to enhance the efficiency of large language model (LLM) inference while maintaining output quality. By implementing a token-level router that predicts the importance of individual tokens, CITER enables smaller language models (SLMs) to handle less critical tokens, reserving LLMs for essential ones. This approach formulates a reinforcement learning (RL) problem to minimize inference costs and introduces a shortcut for reward estimation, significantly accelerating training. Experiments on four benchmark datasets show that CITER can reduce LLM calls by up to 30% while preserving high accuracy or improve accuracy by 25% with the same call ratio. Additionally, ablation studies reveal that token-level routing is more flexible and effective than query-level routing, highlighting the benefits of considering long-term routing impacts.

### Strengths
- The paper is well written and easy to follow.
- The RL-based router training method is novel, and a shortcut to the reward function is proposed to make training easier.
- Experimental results show that the proposed method can achieve better performance under the same call to LLM.

### Weaknesses
- While the framework introduces a shortcut for estimating the reward function, the initial training of the token-level router still requires significant computational resources due to the need for reinforcement learning, which can be a barrier for practical implementation.
- The effectiveness of CITER heavily relies on the accuracy of token importance predictions. If the router fails to accurately assess which tokens are critical, it could lead to suboptimal routing decisions, potentially compromising the quality of the generated outputs. More analytical experiments should be conducted to prove this point.
- The main experiment in Figure 2 involves a few baselines. If a comparison with the LLM Inference Acceleration method can be added, the effectiveness of the proposed method will be more prominent.
- Most experimental results show "% Call to LLM". I hope to show more intuitive metrics in the experiment, such as the amount of computation (FLOPs) or inference time/speed, which will help readers to have an intuitive feeling.

### Questions
Refer to weaknesses.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces CITER, a collaborative inference framework based on token-level routing to accelerate LLM inference. The framework employs a reinforcement learning-trained router to assess token importance, enabling efficient task allocation between small language models (SLMs) and LLMs.

### Strengths
The study addresses the critical practical issue of reducing LLM inference costs, which is vital for real-world deployment. CITER achieves equivalent performance with 30% fewer LLM calls and improves performance by up to 25% with the same number of LLM calls. Technical innovation is notable, featuring fine-grained control through token-level routing, systematic router training via reinforcement learning, and enhanced training efficiency using shortcut reward estimation. The validation is thorough, with extensive experiments conducted across four benchmarks, a detailed ablation study, and verification across various model sizes.

### Weaknesses
The paper lacks sufficient overhead analysis, with no evaluation of the router's computation and memory costs, potential latency from model switching, or end-to-end performance assessment. Especially, the overhead analysis is missing in terms of inference and training as well. 

Its generalizability remains uncertain, as evaluations are limited to QA tasks and a single model series (Qwen2), without verification in multilingual or long-form generation contexts. 

The theoretical justification is also limited, with insufficient rationale for the router's structural choices, no convergence analysis for iterative training, and inadequate verification of shortcut methods' accuracy.

### Questions
What is the additional latency introduced by the router?
I strongly doubt that single large model call can be more efficient than your approach in case of including training and fine-tuning. 

Do similar benefits hold for larger models?
How does the framework perform with inputs of varying lengths?
How does it perform on tasks with high token dependency?

What are the anticipated challenges in real-world deployment?

### Soundness
2

### Presentation
3

### Contribution
2
