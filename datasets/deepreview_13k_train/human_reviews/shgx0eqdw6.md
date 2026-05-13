# ARGS: Alignment as Reward-Guided Search

- Decision: Accept
- Scores: 8, 6, 8, 6

## Abstract
Aligning large language models with human objectives is paramount, yet common approaches including RLHF suffer from unstable and resource-intensive training. In response to this challenge, we introduce \textbf{\ABC}, Alignment as Reward-Guided Search, a novel framework that integrates alignment into the decoding process, eliminating the need for expensive RL training. By adjusting the model's probabilistic predictions using a reward signal, {\ABC} {generates texts with semantic diversity while being aligned with human preferences}, offering a promising and flexible solution for aligning language models. Notably, \ABC~demonstrates consistent enhancements in average reward compared to baselines across diverse alignment tasks and various model dimensions. For example, under the same greedy-based decoding strategy, our method improves the average reward by {19.56\%} relative to the baseline and secures a preference or tie score of {64.33\%} in GPT-4 evaluation. We believe that our framework, emphasizing decoding-time alignment, paves the way for more responsive language models in the future.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper addresses the question: Do we really have to only have one model for sampling language? Recent work distills or amortizes reward models into language models via PPO or DPO, so that sampling is simple. This paper proposes a method for avoiding the distillation step. They instead perform decoding with the product of experts obtained by combining a language model with a reward model. The method does not require training; it directly uses the reward model, trained only on scoring complete sequences, to score incomplete prefixes during search.

Experiments show that, compared to the SFT baseline, taking a product of experts ensemble of the language and reward models on incomplete prefixes during search results in better average rewards overall.

### Strengths
There are two steps in this paper:
1. Decoupling reward and language models as a product of experts (PoE)
2. Using the reward model, unmodified, on prefixes

The first idea is the primary focus of the paper, and the second idea is not discussed. The second idea is just as, if not more important than the first. The reason PPO or DPO is used in the first place is that the reward model is an energy-based model that scores complete sequences, which can be amortized into a left-to-right autoregressive policy. This work bypasses that issue by directly applying the reward model to incomplete prefixes. The application of the reward model to prefixes instead of complete sequences requires experimental justification -- more on this in the weaknesses.

Other than that, the originality, clarity, and significance were good.

### Weaknesses
The decision to directly apply the reward model on prefixes should be justified experimentally, and separately from the decision to decouple the language and reward models. The main question I am interested in is: What is the performance loss from using the reward function on incomplete prefixes? Secondly, when is the predicted reward from the reward function most unreliable (likely on sequences further from completion)?

Separately, I understand that DPO [1] could maybe be considered concurrent work, but there should be comparisons against it.

### Questions
## Questions and comments
1. Can you add a sentence in section 3.1 stating that SFT on HH-RLHF means fine-tuning on the winning responses, if that is what was done.
2. In section 3.2, can you say a relative improvement of 19.56% *in average rewards*.
3. Is PPO the most widely used training-time alignment approach, or DPO?
4. The contributions I would like to see are 1. Decouple reward and LM as product of experts, 2. Show that reward models can be reasonably applied on prefixes, and 3. Experimental validation. 

## Experimental ideas to strengthen the paper
1. You could combine multiple reward functions pretty easily.
2. It would be interesting to see if other reward models return sensible rewards on prefixes.

### Soundness
3 good

### Presentation
3 good

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
The paper introduces a novel framework called ARGS (Alignment with Reward-Guided Sampling) for aligning language models with human preferences. The framework offers a flexible and efficient solution that eliminates the need for expensive RL training. With ARGS, you can generate texts with semantic diversity while being aligned with human objectives.

### Strengths
1. Resource-efficient: The ARGS framework is designed to be resource-efficient, making it an ideal solution for smaller institutions or businesses without the capacity for large-scale training. This can potentially level the playing field, allowing those with limited computational resources to benefit from state-of-the-art models without incurring significant costs.

2. Broader applicability: The compatibility of the ARGS framework with different reward models extends its applicability across various domains and industries. This can accelerate the adoption of machine learning solutions in fields where resource constraints or rapidly changing data are prevalent.

3. Easy to integrate: The ARGS framework is easy to integrate into existing language models, making it a practical solution for aligning language models with human preferences. The authors provide a detailed explanation of how to integrate ARGS into a pre-trained GPT-3 model, making it accessible to a wider range of users.

### Weaknesses
1. Limited evaluation: The evaluation of the ARGS framework is limited to a few specific tasks (e.g., harmfulness), and it is unclear how well the framework would perform on other tasks (more complex ones like multi-step reasoning), especially when a good reward model is not easy to train. This may limit its applicability in certain domains.

2. Unfair evaluation: The evaluation of the ARGS framework is evaluated on the score from reward model. However, there are some limitations: (1) ARGS will certainly achieve higher scores since the RM is integrated during the decoding process. Essentially, applying any RM constraints during the decoding stage will result in higher scores when being evaluated by that RM. (2) The calibration of RM remains unclear -- does a higher reward score certainly lead to a better response, especially the reward score difference is less than 1?

Overall, I think it not very fair if the authors use the same RM in their methods and evaluation.

### Questions
1. A good reward model is vital in ARGS, have you ever tried to enhance the RM? The paper does not show the relation between **RM quality** and **Effectiveness of ARGS**. For example, you might use some techniques from [a,b,c] to strengthen your RM.

(a) The Trickle-down Impact of Reward (In-)consistency on RLHF 2023

(b) Aligning Language Models with Preferences through f-divergence Minimization 2023

(c) Fine-Grained Human Feedback Gives Better Rewards for Language Model Training 2023

2. How would you evaluate the instruction-following ability of model based on ARGS? Since Diversity/Coherence are measuring the naturalness of model responses, there is a blank space for quantifying whether model completes the instruction (in your case, it is ethical property).

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces ARGS, a new framework for aligning LLMs with human preferences without the expensive RL training (i.e., RLHF). To this end, ARGS aligns the LLM with human preferences during the decoding step. Through a set of experiments, the authors show that ARGS leads to better alignment and diversity than the non-aligned baselines while preserving good coherence.

### Strengths
This paper introduces ARGS; a simple decoding-based model for LLMs alignment with reward models. In particular, ARGS only introduces an additional hyper-parameter "w" to tune at inference time.

This method is simple and leads to competitive results compared to PPO while not requiring any finetuning step. The authors do discuss the extra computation added at inference time and show its feasibility. I believe that such a method is interesting and useful for the literature even with this extra weight at inference. For example, it can be used to iterate over different reward models before running only one finetuning, or used directly if we have a small enough and good reward model.

### Weaknesses
This paper aims to replace the RL step for human alignment with a more lightweight, only decoding-based, process. This means that PPO (as noted in Table 4) is the main baseline for ARGS. However, this comparison is not elaborated enough in the paper. This work focuses instead on other decoding-based baselines that do not aim for human alignment. For example, it would be interesting to add the Win-Tie(%) results for ARGS vs. PPO in Table 2 and discuss the low "Diversity" numbers for PPO in Table 4 (is it an issue of the KL penalty, was it hard to cross-validate this term?) These points would be an interesting addition to this paper.

### Questions
.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper introduces ARGS, a decoding framework that enhances the alignment of generated text with human preferences. It achieves this by employing a reward mechanism that guides the text-generation process of a language model. The method consists of reward-guided scoring and token selection. The goal is to generate text that is both coherent and contextually relevant while satisfying specific alignment criteria or objectives. The method improves the average reward compared to standard decoding and demonstrates better lexical diversity without compromising contextual consistency. The experiments validate the effectiveness of ARGS in aligning the generated text with human preference.

### Strengths
- Authors aim to resolve an important problem in the reasearch area. 

- The problem is interesting. 

- Good discussion on broader impacts.

### Weaknesses
 - There are some serious issues in citation. "Decoupled weight decay regularization" is an ICLR-19 paper, not an arxiv. Please refer to https://openreview.net/forum?id=Bkg6RiCqY7. The authors should list all wrong citations and revise them. I will check the similar issues in all citations one by one. 

- Qualitative results are limited. I suggest that the authors provide more results to support the claims. It is hard for me to have a clear understanding of the improvements. If an anonymous web demo or a code link is provided, I will revise my rating. 

- In Figure 2, different types of lines are not shown in the figure. It is not very clear. 

- Compared with classical decoding methods, ARGS has higher time complexity. Although the $k$ can be small, it also has a higher complexity. Besides, small $k$ is not good for performance. 

- No period in Equation $T_{ARGS}(n, m, k)$. 

- The latest baseline method is a paper published in 2022. More baselines should be compared. 

- I am concerned about the technical novelty of the paper. The idea of reward-guided search has been proposed in SCST (Self-Critical Sequence Training). Besides, the technical contribution compared with the baseline is a tricky implementation, which is marginal. 

- The user study is needed for evaluation. 

- Missing discussion on limitation. 

Overall, the writing of this submission is unprofessional and the technical contribution is marginal. I provide a reject rating here and I will revise the rating according to the authors; rebuttal and other reviews.

### Questions
See weakness.

---

Revise rating from 3 to 5, 5->6.

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair
