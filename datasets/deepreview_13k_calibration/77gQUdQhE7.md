# Inference-Aware Fine-Tuning for Best-of-N Sampling in Large Language Models

- Decision: Accept
- Avg Score: 5.67
- Scores: 5, 6, 6

## Abstract
Recent studies indicate that effectively utilizing inference-time compute is crucial for attaining good performance from large language models (LLMs). Specifically, the Best-of-N (BoN) inference strategy, where an LLM generates multiple responses and a verifier selects the best, has shown strong empirical performance. Motivated by this, we develop a novel inference-aware fine-tuning paradigm, which encompasses the BoN-aware inference framework as a special case. We devise the first imitation learning and reinforcement learning (RL) methods for fine-tuning LLMs using BoN, overcoming the challenging, non-differentiable argmax operator in BoN. We empirically demonstrate that our BoN-aware models implicitly learn a per-example "meta-strategy", which interleaves best responses with more diverse responses that might be better suited to a test-time input—a process reminiscent of the exploration-exploitation trade-off in RL. Our experiments demonstrate the effectiveness of BoN-aware fine-tuning in terms of improved performance and inference-time compute. In particular, we show that our methods improve the BoN performance of Gemma 2B on Hendrycks MATH from 26.8% to 30.8%, and Pass@K from 60% to 67%.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper proposes a novel inference-aware fine-tuning paradigm, aiming to enhance the inference performance when scaling the compute. 

To overcome the non-differential argmax operator within best-of-N (BoN), the paper proposes the first imitation learning and reinforcement learning methods for fine-tuning language models with BoN. 

The experimental results show the BoN improvement of Gemma 2B on Hendrycks MATH from 26.8% to 30.8%, and Pass@K from 60% to 67%.

### Strengths
1. The studied problem is interesting and important: how to improve best-of-N sampling in the test time through advanced training methods applied to fine-tune the models. 

2. The proposed method is reasonable and could be sound and useful if the method can be verified carefully and thoroughly.

### Weaknesses
- The paper writing can be improved: it is not easy to follow the core idea of the proposed methods. A visual Figure showing the core mechanism of the method is strongly suggested. 

- The experiments are not sound enough to demonstrate the effectiveness of the proposed method, specifically:

**Regarding the co-scaling behavior of sample number N and temperature**: this analysis was conducted using only a single policy model and a single reward model.

How might the curves in Figure 2 appear if different language models or stronger reward models were used?

The conclusions drawn here cannot be readily generalized to other language models or reward models.


**The results presented in Figure 4 make it challenging to conclude that the proposed inference-aware fine-tuning significantly improves performance.**

One potential issue lies in the weakness of the reward model: the solution selected as having the highest reward is often inaccurate, and fine-tuning solely on this data may result in suboptimal model performance.

Selecting a broader range of solutions could benefit fine-tuning, as a correct answer might be found within these additional options.

Therefore, the observed improvement may stem from identifying a correct solution through an increased sample selection rather than from the inference-aware fine-tuning itself.


- I would also suggest conducting experiments on the alignment tasks and testing the models on AlpacaEval or Arena-Hard test sets.

### Questions
1. How is the accuracy of the used reward model? 

2. How does best-of-N sampling relate to majority vote in math reasoning?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper presents a finetuning approach for large language models (LLMs) that incorporates the inference strategy directly into the model’s training process, with a particular focus on Best-of-N (BoN) inference. The authors argue that there is a disparity between the best-of-N policy typically used at inference time and the policy learned through standard supervised fine-tuning (SFT). To address this, they formalize an inference-aware fine-tuning problem that integrates the inference strategy into the training objective. Specifically, they develop a supervised BoN-aware fine-tuning method and a BoN-aware reinforcement learning (RL) with binary rewards, using policy gradients derived only from positive examples to mitigate data inefficiency. The proposed methods are evaluated on the Gemma 2B model, primarily using the Hendrycks MATH benchmark, with an emphasis on understanding the relationship between the number of samples and temperature.

### Strengths
- The paper addresses an important and timely problem, as best-of-N inference with verifiers has become increasingly popular for reasoning tasks.
- The paper provides a solid theoretical framework supporting the proposed methods with a clear formalization of inference-aware training objectives.

### Weaknesses
 - The method is only evaluated on a single model and a single task, which limits insights into its broader applicability.
- Although BoN-aware fine-tuning is a key contribution, the experiments predominantly examine the relationship between the number of samples and temperature. This leans more toward an analysis of the proposed methods than a comparative assessment against strong baselines, leaving questions about its competitive advantages unanswered.

### Questions
1. Will inference-aware SFT and inference-aware RL reduce the model’s generalizability? How does the model perform when using beam search alone, without a verifier?
2. For inference-aware SFT experiments, what type of verifier is used? How does the method perform if there’s a mismatch between the training and testing verifiers?
3. In Figure 1, how is the empirical frequency calculated? What defines the best BoN performance? Also, what are the definitions of "easy" and "difficult" problems, given that the figure is based on the same set of MATH benchmark problems?

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
This paper proposes an inference aware fine-tuning strategy for Best-of-N (BoN) to overcome the non-differentiable argmax operator for BoN. The proposed strategy incentivizes the model to balance the best and diverse responses for fine-tuning, achieves better performance compared to the base Gemma 2B model on the MATH dataset.

### Strengths
1. The incorporating of inference strategy into training is a compelling and well-founded idea.
2. The proposed BoN-aware fine-tuning to balance the trade-off between the best and diverse responses is well-motivated.

### Weaknesses
1. The experiments are conducted on a base model (Gemma 2B) and an evaluation dataset (MATH). More evaluation results on different base models and evaluation datasets are needed.
2. What is the underlying rationale for the BoN-SFT loss function presented in Equation (7)? The function appears to penalize y', even in scenarios where the sampled y' demonstrates high quality, as evidenced by r(x, y') approaching r(x, y). This raises a question: If the sampled y' exhibits desirable characteristics, wouldn't it be more beneficial for the policy model to learn from these high-quality responses?
3. It would be valuable to conduct a comparative analysis of BoN-SFT against several straightforward baseline approaches. These could include:

(1) Fine-tuning the base model using the highest-quality response selected from N generated samples.

(2) Fine-tuning the base model utilizing the ground truth responses.

(3) Fine-tuning the base model with all the sampled N responses.

(4) Fine-tuning the base model with the combination of all the sampled N responses and the ground truth responses.

### Questions
See "Weaknesses".

I would be happy to discuss further with the authors and reassess my score based on the rebuttal stage.

### Soundness
2

### Presentation
3

### Contribution
3
