# Privately Aligning Language Models with Reinforcement Learning

- Decision: Accept
- Scores: 8, 6, 6

## Abstract
Positioned between pre-training and user deployment, aligning large language models (LLMs) through reinforcement learning (RL) has emerged as a prevailing strategy for training instruction following-models such as ChatGPT.
In this work, we initiate the study of privacy-preserving alignment of LLMs through Differential Privacy (DP) in conjunction with RL. 
Following the influential work of \citet{ziegler2020finetuning}, we study two dominant paradigms: (i) alignment via RL without human in the loop (e.g., positive review generation) and (ii) alignment via RL from human feedback (RLHF) (e.g., summarization in a human-preferred way). 
We give a new DP framework to achieve alignment via RL, and prove its correctness.
Our experimental results validate the effectiveness of our approach, %in privately aligning LLMs, 
offering competitive utility while ensuring strong privacy protections.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper offers an approach to align Large Language Models with human preferences and feedback via a privacy preserving RLHF methodology and perform some comparison experiments to show the correctness of their method.

### Strengths
(1) The approach proposed in this paper for aligning language models with PPO in a privacy-preserving way is original; (2) The paper is clearly written and well-organized. (3) The paper gives a quite comprehensive analysis of the procedure and emphasize the difficult issues in the implementation.

### Weaknesses
 (1)The DP part is too condensed to understand.  The authors used DP-SGD on several occasions but without a clear explanation of this algorithm. And in the main text, I could not find a concrete DP algorithm and a clear procedure how it is combined with the alignment. Specifically, the paper lacks a detailed explanation of how the gradient clipping and noise addition mechanisms are implemented within the DP-SGD framework. It is unclear how the sensitivity of the gradients is calculated, which is crucial for determining the appropriate amount of noise to add. Furthermore, the paper does not specify the privacy parameters (epsilon and delta) used in the experiments, making it difficult to assess the privacy-utility trade-off. (2) Algorithm 1 is not original. I don’t see the reason why it was presented in detail in the paper.  The PRIVATE alignment should be more interesting.

### Questions
(1)What is non-private REWARD model? What is the private REWARD model? DP mechanisms are not equivalent to adding noises.  Could you specify the DP mechanisms in the alignment?

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors provide privacy-preserving technique for fine-tuning large language models. They apply differentiall-private SGD (DP-SGD) to the PPO reinforcement learning algorithm during model fine tuning. They demonstrate that for single-digit privacy budgets it is possible to fine tune GPT-2 such that there is improved utility on positive reward score.

### Strengths
The paper combines two well-understood algorithms, DP-SGD and PPO in a well-motivated task of reinforcement with human feedback and supervised fine-tuning. The experiments and the results are clear and the application of private model fine-tuning is reasonable.

The paper is well organized and the writing is clear. The paper is well written and the algorithm is clearly explained. Their claims are based on the GPT-2 family of models and run experiments on the ROUGE metrics and the TweetEval benchmark. The authors offer a privacy-preserving technique to undertake reinforcement learning with human feedback. They combine DP-SGD and PPO with a few adaptations and show utility benefits on NLP benchmarks.

### Weaknesses
While the examples are helpful, the overall motivation could be a bit stronger. What are we protecting and why? What is the threat model around incorporating human feedback? Are their examples of memorization from human feedback?

The experiments in the main body do not include error or number of trials details. It is unclear in Table 1 why models with less privacy should do worse than those with more privacy (GPT-2 Medium, eps 4->8, or GPT-2 Large eps 8->Inf). Such results demand further study and/or ablations and are difficult to interpret without confidence intervals. The use of corporate imagery (Reddit / OpenAI) weakens the overall presentation and the generality of the results. Work in differential privacy and RL can be traced to differentially-private policy evaluation (Balle, Gomrockchi, Precup). The paper touches on the privacy accounting implications when  $T_{\text{PPO}} \neq 1$
, but does not offer evaluate the implication of fixing it to the default value of 4.

### Questions
What are the confidence intervals for your reported experiments?
Are there other domains where the fine-tuning method can be better understood?
What are we losing by setting $T_{\text{PPO}} \neq 1$ instead of 4 in terms of utility? Is this trade-off significant?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper focuses on aligning large language models (LLMs) through reinforcement learning (RL) while preserving user privacy using Differential Privacy (DP). The paper introduces a new DP framework for this alignment and validates its effectiveness through experiments.

### Strengths
1. The paper proposes a differentially private framework for aligning LLMs with RL, offering mathematical guarantees of privacy.
2. The paper empirically evaluates the framework on tasks like positive review generation and summarization, showing that it offers competitive utility while ensuring strong privacy protections.

### Weaknesses
1. The paper employs DPSGD to ensure privacy in the alignment of large language models through reinforcement learning. While the use of DPSGD is well-established in the privacy literature. Furthermore, the paper does not introduce significant modifications to the RLHF process. The innovation seems to be more focused on engineering adjustments rather than novel theoretical contributions. Specifically, the application of DPSGD to each step of the RLHF pipeline, while necessary for end-to-end privacy, does not present a novel algorithmic contribution. The core RLHF algorithm remains largely unchanged, with the primary modification being the incorporation of DP noise during gradient updates. This raises questions about the depth of the contribution beyond a straightforward application of existing DP techniques.

2. The paper discusses the trade-offs between privacy and utility but does not present these results in an intuitive manner. A Pareto frontier could be more illustrative in showing how different levels of privacy (varying ε) impact the model's performance. This would provide a clearer understanding of the trade-offs involved. The current presentation lacks a clear visualization of how the utility of the model degrades as stronger privacy guarantees are enforced. A more detailed analysis, perhaps with multiple performance metrics plotted against different privacy levels, would be beneficial.

3. If the reward in step 2 is DP, is it necessary to use the DPPPO in step 3 as the learning reward is already DP?

### Questions
Please check the weaknesses.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
