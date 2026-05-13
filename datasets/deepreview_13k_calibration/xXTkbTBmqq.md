# OLMoE: Open Mixture-of-Experts Language Models

- Decision: Accept
- Avg Score: 8.67
- Scores: 8, 8, 10

## Abstract
We introduce \model{}, a fully open, state-of-the-art language model leveraging sparse Mixture-of-Experts (MoE). \modelsmall{} has 7 billion (B) parameters but uses only 1B per input token. We pretrain it on 5 trillion tokens and further adapt it to create \modelsmalldpo{}. Our models outperform all available models with similar active parameters, even surpassing larger ones like Llama2-13B-Chat and DeepSeekMoE-16B. We present various experiments on MoE training, analyze routing in our model showing high specialization, and open-source all aspects of our work: model weights, training data, code, and logs.

\begin{center}
\begin{tabular}{rcl}
\multirow{2}{*}{\huggingface} & \textbf{Weights} & \url{https://hf.co/allenai/OLMoE-1B-7B-0924}\\
& \textbf{Data} & \url{{https://hf.ai/ai2-llm/olmoe/reports/OLMoE-1B-7B-0924--Vmlldzo4OTcyMjU3}{\texttt{https://wandb.ai/ai2-llm/olmoe/reports/}}\\
& & \href{https://wandb.ai/ai2-llm/olmoe/reports/OLMoE-1B-7B-0924--Vmlldzo4OTcyMjU3}{\texttt{OLMoE-1B-7B-0924--Vmlldzo4OTcyMjU3}}\\
\end{tabular}
\end{center}

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper introduces OLMoE, a fully open, state-of-the-art language model built on a sparse Mixture-of-Experts (MoE) architecture. The authors conducted extensive experiments to validate the effectiveness of the proposed method, including evaluations after pre-training and adaptation phases. Additionally, they explored key design choices within the MoE framework, examining factors like expert granularity, routing strategies. Their analyses provided valuable insights into MoE, including router saturation, expert co-activation, and domain/vocabulary specialization.

### Strengths
- The writing in this paper is clear and easy to follow.
- The paper advances MoE research by providing a fully open-sourced, state-of-the-art MoE architecture, which is beneficial for the research community.
- The paper presents a thorough analysis of key design choices in MoE, offering valuable guidance on building high-performance MoE models.
- The analysis is insightful, with discussions on phenomena such as router saturation and expert co-activation providing fresh perspectives and meaningful implications for the field.

### Weaknesses
I have a question regarding the experimental results: were the model parameters quoted directly from the original paper for the results shown in Table 2? For instance, in the original paper, OpenMOE’s activation parameter count is reported as 2.1B, whereas Table 2 shows an activation parameter count of 2.9B for OpenMOE. I recommend that the authors carefully verify the accuracy of these values.

### Questions
See Above.

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
This paper presents a mixture-of-experts (MoE) LLM model called OLMoE that has 1B active parameters and 7B total parameters. The OLMoE model Pareto dominates many state-of-the-art models in the performance vs. active parameters space. The paper explores and presents insights on what is optimal in the design-space of MoE parameters and present analysis of routing behavior in MoEs.

### Strengths
1) Strong empirical results with state-of-the-art performance for 1B active parameters.
2) Good exploration of the MoE design space which forms a good guide for MoE model design.
3) Novel analysis of routing behavior in MoE models during training and inference.
4) This is the only MoE model where the model weights, code, data and checkpoints are openly available and thus the work is entirely reproducible.

### Weaknesses
1) Other state-of-the art MoE models in related works are not exactly in the same parameter count configuration (1B/7B) so an exact comparison cannot be made to this model's performance.
2) Most of the design choices and training choices are based on prior work and the novelty is more in the design space exploration and analysis of routing behavior.

### Questions
The work is well presented and possible suggestions for improvements are addressed in the future work section.

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
10

### Rating Number
10

### Confidence
5

### Summary
This work is devoted to sharing the insights, data, and checkpoints of a series of MoE LLMs. The model achieved promising results on various benchmarks as a fully open model family.

### Strengths
1) There is no doubt that training MoE LLMs is challenging. This work offers a couple of important takeaways about how to train a good MoE LLMs, which is very helpful to the community.
2) The presentation is very clear. For instance, the Table 1 delivers many key designs clearly at the early section of the paper.
3) The model performance is good as well. As shown in Table 2 and 3, the model performs competitive with dense open models and partially open models (e.g. Qwen, Deepseek).
4) The Analysis in Section 5 is informative, which greatly help readers and authors to understand how is the model working. This can also greatly speedup the growth of the community.

### Weaknesses
1) Although the model has been relatively large, it is still much smaller than the SoTA MoE LLMs. I understand it is hard to get enough training resource for a fully open projects.


### Questions
1) What do you think about the necessity of expert parallelism? This model used dropless MoE, so it anyway will be unbalanced when using expert parallelism during training and inference. Without expert parallelism, it is still okay when the model is small. However, if we are aiming at a very large model, which has very large experts even if we are using the "fine-grained MoE", the expert parallelism would still be required? So how can we handle the token drop problem in this case?

### Soundness
4

### Presentation
4

### Contribution
4
