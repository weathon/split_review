# Segmenting Text and Learning Their Rewards for Improved RLHF in Language Models

- Decision: Reject
- Avg Score: 5.25
- Scores: 6, 6, 6, 3

## Abstract
Reinforcement learning from human feedback (RLHF) has been widely adopted to align language models (LMs) with human preference.
Prior RLHF works typically take a bandit formulation, which, though intuitive, ignores the sequential nature of LM generation and can suffer from the sparse reward issue.
While recent works propose dense token-level RLHF, treating each token as an action may be oversubtle to proper reward assignment. 
In this paper, we seek to get the best of both by training and utilizing a segment-level reward model, which assigns a reward to each semantically complete text segment that spans over a short sequence of tokens.
For reward learning, our method allows dynamic text segmentation and compatibility with standard sequence-preference datasets.
For effective RL-based LM training against segment reward, we generalize the classical scalar bandit reward normalizers into location-aware normalizer functions and interpolate the segment reward for further densification.
With these designs, our method performs competitively on popular RLHF benchmarks in both reward modeling and LM policy learning.
Ablation studies are conducted to further demonstrate our method.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper tackles the challenge of reward sparsity issue in RLHF by introducing a segment-level reward model. Traditional RLHF approaches generally apply a bandit formulation, assigning rewards only at the sequence level, which leads to sparse feedback. Meanwhile, token-level reward models give more detailed feedback but may be overly granular. This paper proposes a middle-ground solution: segment-level rewards, where rewards are allocated for semantically complete segments within the text. The approach includes dynamic text segmentation, adaptable reward normalization methods, and an interpolation mechanism to further densify training signals. The method is evaluated against popular RLHF benchmarks, demonstrating improvements in reward modeling accuracy and effective LM policy training.

### Strengths
The paper conducts extensive experiments with multiple RLHF benchmarks and ablation studies. The proposed method shows competitive performance across all three benchmarks, achieving improvements in both reward model accuracy and downstream LM policy quality. The ablation studies provide thorough insights into certain design choices.

### Weaknesses
The proposed method lacks novelty. Densify the fine-grained reward signal for RLHF training have been extensively discussed in previous studies. A key challenge is learning a fine-grained reward model without costly process supervision data. In this paper, the authors directly reference (Yang et al., 2023) in Equation 3 for segment-level reward model learning. Additionally, text sequence segmentation through entropy thresholding in language models has been explored in previous studies as well. It appears that the main contribution of this work lies in showing that segment-level rewards empirically outperform token-level rewards. However, this may not represent a substantial departure from existing ideas. The paper does not sufficiently address the computational overhead introduced by segment-level reward computation, particularly during PPO training. While the authors demonstrate improved performance, the increased computational cost might limit the practical applicability of the method, especially for very large language models or extensive training runs. Furthermore, the method's reliance on a fixed entropy threshold for segmentation could be problematic. The optimal threshold may vary across different datasets and tasks, and the paper lacks a systematic approach for determining the appropriate threshold, potentially requiring extensive hyperparameter tuning for new applications.

### Questions
1. In Table 1, the segment-level reward model (85.93) outperforms the bandit reward model (81.11), with both models evaluated at the sequence-level on RewardBench. Since the segment-level reward model is also trained using BT loss (Eq 3), could you provide any insights into why the segment-level action space enhances reward modeling?
2. Does using different pre-trained models as reward functions significantly impact the performance?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
To retain the optimization benefits of sparse rewards in PPO within RLHF while alleviating potential issues with reward assignment and the anomalies of language intuition, the authors propose a segment-level reward model that assigns rewards to each semantically complete text segment composed of a small number (or just one) of tokens. This approach facilitates RL-based language model training due to denser feedback and provides more accurate training guidance through the semantic completeness of each action. Technically, the authors differentiate the aggregation of segment rewards within the text sequence into parameterized sequence evaluation, addressing the limitations of classical reward normalizers (i.e., the mean and standard deviation of complete sequence rewards) by extending the scalar mean and standard deviation of classical bandit normalizers into functions that can output mean and standard deviation normalizers for rewards at arbitrary positions within the text sequence. They also experimentally test related methods.

### Strengths
1. Extensive and detailed ablation experiments have been conducted, providing sufficient evidence for the rationale behind the design choices of the reward model.

2. The use of "segment" instead of "sentence" in the token-level reward modeling process is unique.

### Weaknesses
1. The layout of Section 2 is confusing; during the reading process, I did not fully understand the relevance of this paragraph to the experimental setup discussed later.

2. In the experiments presented in Table 6, the segment method does not demonstrate its optimality in most cases. Does this undermine the effectiveness of the method?

### Questions
For which specific tasks does the segment method have a greater advantage than the sentence and token methods? The experiments presented in the paper do not seem to highlight the superiority of the segment method.

### Soundness
2

### Presentation
2

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
The paper formulates RLHF on segment-level MDP. The authors propose a method to train a segment-level reward model, and correspondingly use it on online RL methods, i.e. PPO. They also improve the original PPO pipeline with two modifications: 1) a new reward normalization method; 2) a way to assign token-level reward from segment-level reward. The experiments, especially ablation studies, are comprehensive to validate their implementation choices.

### Strengths
1. The motivation of the segment-level reward is quite intuitive, since the token-level reward breaks down the natural semantic unit. The segment-level MDP setting is novel to existing RLHF society, and might inspire more relevant works.

2. The ablation studies are comprehensive.

### Weaknesses
1.	The most important procedure in the segment-level RLHF pipeline, semantic segmentation, would increase the computational burden of online RL and is theoretically unguaranteed. 

2.	In the experiments, authors train all model on PPO for only one epoch. I wonder whether it is enough for PPO to converge since the paper does not show any training dynamics. This might affect a lot to experimental analysis, since the improvement might stem from faster convergence compared to bandit setting, but with lower final performance.

3.	There are some designs/implementations lack of intuition or analysis. (Question 4/5)

### Questions
1.	In Line45, I suggest to remove “/step” from “per-token/step reward signal” since it is easy to connect step-level reward to process reward model rather then token-level reward model in the context.
2.	As mentioned in Line195, different dataset might require different $f(\cdot)$, could you provide any guidance?
3.	Since a new reward normalizer is one of your key contributions, better introduce some corresponding preliminaries in section 2.1
4.	Why does $p$ can be simplest defined as $t/T$? It seems that the latter actions would have a higher p. Maybe provide some intuitive or relevant explanations? The definition of completion portion $p$ would better be clarified.
5.	The enhancement from evenly splitting segment-level rewards to each token is somewhat counter-intuitive and surprising. Can you explain some potential reasons/intuition about this design? Moreover,  decomposing the segment-level reward to token-level signal kind of contradicts to your main novelty, segment-level MDP, and the experiments proves this decomposition is beneficial, which in contrast mitigates the attraction of segment-level MDP setting.
6.	In experiments of RewardBench, how do you determine the final score of a sentence by multiple token-level/segment-level rewards?

### Soundness
3

### Presentation
3

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
The paper proposes a new approach to improve Reinforcement Learning from Human Feedback (RLHF) for language models by using a segment-level reward model. This method strikes a balance between dense token-level rewards and sequence-level bandit rewards. Rather than assigning rewards to individual tokens (which may lack semantic meaning) or entire sequences (which leads to sparse rewards), the model assigns rewards to semantically meaningful text segments. The authors also introduce techniques for dynamic text segmentation, segment-based reward learning, and novel reward normalizers that adapt to different points in a sequence. The approach shows competitive performance on RLHF benchmarks and demonstrates improved sample efficiency and reward assignment compared to previous methods.

### Strengths
(1) The use of a segment-level reward model addresses the limitations of both bandit and token-level approaches, allowing for more meaningful and semantically complete feedback, which can enhance the training signal.

(2) By implementing dynamic segmentation based on the entropy of the model's predictive distributions, the method can effectively identify semantically coherent segments, improving the accuracy of reward assignments.

(3) The approach mitigates the sparse reward issue commonly found in RLHF by providing denser feedback through segment-level rewards, potentially leading to more efficient learning and better policy optimization.

### Weaknesses
(1) The results are not convincing. The author should utilize larger models like llama3-8B to further illustrate their contributions.
(2)  why not conduct experiments on RLHF models like phi-dpo?
(3) Segment-level does not intuitive to me. I consider larger models have solved the challenged the author purpose.

### Questions
See the weakness section.

### Soundness
1

### Presentation
2

### Contribution
2
