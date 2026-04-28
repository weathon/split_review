# A Critical Look At Tokenwise Reward-Guided Text Generation

- Decision: Reject
- Avg Score: 5.50
- Scores: 3, 6, 8, 5

## Abstract
Large language models (LLMs) can significantly be improved by aligning to human preferences---the so-called reinforcement learning from human feedback (RLHF).  However, the cost of fine-tuning an LLM is prohibitive for many users.
	Due to their ability to bypass LLM finetuning, tokenwise reward-guided text generation (RGTG) methods have recently been proposed.
	They use a reward model trained on full sequences to score partial sequences during a tokenwise decoding, in a bid to steer the generation towards sequences with high rewards.
	However, these methods have so far been only heuristically motivated and poorly analyzed.
	In this work, we show that reward models trained on full sequences are not compatible with scoring partial sequences.
	To alleviate this issue, we propose to explicitly train a Bradley-Terry reward model on partial sequences, and autoregressively sample from the implied tokenwise policy during decoding time.
	We study the property of this reward model and the implied policy.
	In particular, we show that this policy is proportional to the ratio of two distinct RLHF policies.
	We show that our simple approach outperforms previous RGTG methods and achieves similar performance as strong offline baselines but without large-scale LLM finetuning.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper pointed out that current RGTG methods struggle as they rely on full-sequence reward models for partial sequences. To improve this, the authors augment the training on partial sequences, assuming that the ranking won't change, achieving good tokenwise guidance. This method outperforms previous RGTG techniques and bridge the gap between the quality compared to finetuning solutions such as DPO and PPO baselines.

### Strengths
- This work gives good recap on RLHF and DPO for people who are not familiar with the fields can get to connect the dots.
- This work show that by a simple approach of dropping some follow sequence and train on the partial rewards can help inference time generation quality (by LLM-judge).

### Weaknesses
I think this reward model training on partial inputs are not novel as there are quite a few works of using partial observation to train reward models. For example, Learning to Rank Generation with Pairwise Partial Rewards (https://aclanthology.org/2023.emnlp-main.371.pdf), Teacher Forcing Recovers Reward Functions for Text Generation (https://openreview.net/pdf?id=1_gypPuWUC3), Reward-Augmented Decoding: Efficient Controlled Text Generation With a Unidirectional Reward Model (https://arxiv.org/pdf/2310.09520), etc.

In line 323, the authors claimed “These algorithms are different from our work as they do not align language models using reward models or preference datasets.” I think this is not a valid claim? Many work such as PPLM and GeDi they are using a classifier (as a way to provide “reward”, either through classifier final logits or forward gradient computation), which is the same as this work as the authors are also not using the reward models to finetune the base LLMs. The key difference is whether the reward model is trained on full or partial sequences, which the authors do not clearly highlight as the main contribution.

### Questions
n/a

### Soundness
3

### Presentation
3

### Contribution
1

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
- The paper argues that existing inference-time reward-guided text generation (RGTG) has a flaw: it provides arbitrary rewards for partial sequences, as these reward models are trained on full sequences.
- To address this issue, the authors propose training reward models (RMs) using partial sequences.
- Experiments demonstrate that these RMs perform better in reward-guided text generation across four tasks: summarization, dialogue, fine-grained text generation, and machine translation.

### Strengths
- The paper proposes a straightforward method for training RMs on partial sequences.
- The presentation is clear and well-structured, covering classic RLHF concepts, DPO, and decode-time RGTG.
- The experiments evaluating performance and additional inference costs are thorough and balanced.

### Weaknesses
 - Beyond theoretical analysis, the claim that full reward models produce arbitrary rewards would be stronger with empirical evidence, such as human experiments.  
  - For instance, an ablation study demonstrating the sensitivity of full RMs to varying sequence lengths could strengthen this argument.
 - To validate that the token-level RMs (using partial sequences) are more effective than full sequence RMs, it would be beneficial to train PPO and compare it against full sequence RMs. One might expect that token-level rewards lead to faster convergence, ultimately resulting in superior performance.


### Questions
- Interestingly, the win rate of PARGS over PPO is high, even though the reward scores suggest otherwise.
- For HH dialogue, why was PPO omitted?
- Regarding GPT evaluation, what are the evaluation criteria? It would be helpful to include the exact prompts used for evaluation.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper proposed RGTG. It aims to improve LLMs without expensive fine-tuning. They identify issues as the existing approaches use the full-sequence reward model to score the partial sequences during decoding. To alleviate this issue, the paper proposed to train Bradley-Terry reward model.

### Strengths
The theoretical analysis is great and the empirical evaluation is comprehensive. It is important to improve the text generation without expensive fine-tuning. The proposed method gave a practical approach with strong empirical experimental results.

### Weaknesses
The experiments only focus on automated metrics and GPT-4 evaluation. It can benefit from some human evaluation, even on a small scale. It can provide additional validation of the claimed improvements.

### Questions
1. Could you include an ablation study session to show the impact of different components?

2. It will be great if the paper can provide some examples of generated text, comparing to the baseline models. It will give readers a better sense of the improvements.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper demonstrate the deficiency of utilizing bandit-setting RM for alignment by reward-guided sampling (ARGS), and propose to train RM with partial sentences of preference corpora for ARGS. Experimental results validate the effectiveness of their method.

### Strengths
1. The analysis about deficiency of the original bandit RM in ARGS is enlightening.
2. The performance improvement comparing to baselines is inspiring.

### Weaknesses
1. The assumption that the partial sequence $y_{1:i}^w$ is also preferred to the partial sequence $y_{1:i}^l$” is quite strong, since in most cases like reasoning, undesirable parts of the response just occur in specific steps or tokens.

2. Lack of some experiments. See Question 4/5.

3. The training cost for RM would be multiplied by the token number, which might be unbearable under current situations where sentence length is generally hundreds of tokens.

### Questions
1.	In Eq.3 and corresponding context, $\beta$ should be $1/\beta$. Otherwise, change $\beta$ to$1/\beta$ in Eq.2.
2.	Better clarify what the subscripts $i$,$i-1$ of $\pi_{RLHF}$ mean in Theorem 3.
3.	Since the prefix lengths in the training objective are the same for chosen and rejected response as in Eq.4, it seems unable to directly induce Lemma 2 with different prefix lengths ($i$ for $y_1$, $j$ for $y_2$). Can you provide more detailed derivations about Lemma 2?
4.    How do you implement Best-of-N sampling? Do you use your reward model the same as in the bandit setting?  For a fair comparison, you could try to use your RM to score partial sentence and determine the final score of a sentence by the the minimum/summation/mean of these partial scores.
5.    Would PARGS perform stably under different $\beta,k$ in Algorithm 1? Would different $k,\beta$ affect generative diversity?

### Soundness
3

### Presentation
2

### Contribution
2
