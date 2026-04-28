# Self-Play Preference Optimization for Language Model Alignment

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 6

## Abstract
Standard reinforcement learning from human feedback (RLHF) approaches relying on parametric models like the Bradley-Terry model fall short in capturing the intransitivity and irrationality in human preferences. Recent advancements suggest that directly working with preference probabilities can yield a more accurate reflection of human preferences, enabling more flexible and accurate language model alignment. In this paper, we propose a self-play-based method for language model alignment, which treats the problem as a constant-sum two-player game aimed at identifying the Nash equilibrium policy. Our approach, dubbed \textit{\algname} (SPPO), utilizes iterative policy updates to provably approximate the Nash equilibrium. 
Additionally, we propose a new SPPO objective which is both strongly motivated by theory and is simple and effective in practice.
In our experiments, using only 60k prompts (without responses) from the UltraFeedback dataset and without any prompt augmentation, by leveraging a pre-trained preference model PairRM with only 0.4B parameters, SPPO can obtain a model from fine-tuning Mistral-7B-Instruct-v0.2 that achieves the state-of-the-art length-controlled win-rate of 28.53\% against GPT-4-Turbo on AlpacaEval 2.0. It also outperforms the (iterative) DPO and IPO on MT-Bench, Arena-Hard, and the Open LLM Leaderboard.
Starting from a stronger base model Llama-3-8B-Instruct, we are able to achieve a length-controlled win rate of 38.77\%.
Notably, the strong performance of SPPO is achieved without additional external supervision (e.g., responses, preferences, etc.) from GPT-4 or other stronger language models.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper proposes a novel self-play alignment method, SPPO, that leverages relative win rates instead of scalar-based reward models. SPPO aligns the language model without external pairwise preference pairs, highlighting its efficiency over pairwise alignment methods. Through iterative training with a theoretical guarantee of converging to the ideal policy, SPPO shows strong performance over previous methods.

### Strengths
1. SPPO is derived from a solid theoretical background with a theoretical guarantee on the convergence of training policy to the ideal policy.
2. Interpreting SPPO from several different perspectives (e.g., token-level Q-learning and policy gradient) further strengthens its validity.
3. SPPO led to monotonic improvements of both models in majority of tasks, highlighting the effectiveness of SPPO.

### Weaknesses
 **1. Lack of comparisons against relative methods**

As the paper precisely depicts SPPO as a "semi-online" variant of the policy gradient method, SPPO has the potential to be interpreted as an online method by leveraging on-policy generations and having access to a preference model. Moreover, along with the foundational alignment methods like DPO and IPO, there are some strong offline methods like SimPO [1] that outperform IPO and DPO. However, any RL-based methods [2] or recent performant offline methods are compared to SPPO in the paper. Specifically, the paper lacks a comparison to methods that also leverage relative preferences or implicit rewards, such as those derived from the Bradley-Terry model, which could provide a more direct benchmark for the proposed approach. Furthermore, the absence of comparisons with methods that explicitly optimize for win-rates, rather than scalar rewards, makes it difficult to assess the true novelty and effectiveness of SPPO's approach.

&nbsp;

**2. Insufficient analysis of empirical aspects of SPPO**

While SPPO's performance on diverse benchmarks is impressive, the paper does not suggest any analysis of how SPPO-trained models are aligned to PairPM. Especially regarding the choice of total training epochs of 18 and the iterative nature of SPPO, analysis of gradual shifts happening throughout the training would be needed, such as the loss trends or PairPM win rate changes. The paper should include a more detailed analysis of the training dynamics, such as how the policy changes over iterations, and how the win rate against the reference model evolves. This would provide a better understanding of the convergence behavior of SPPO and the impact of its iterative nature. Furthermore, the paper should investigate the sensitivity of SPPO to the number of training iterations and epochs, as well as the learning rate schedule.


&nbsp;

**3. Clarifications on terminologies for experiments**

Some experiment terminologies are not clearly stated. For instance, the concepts of "iteration", "round", or "epoch" are not clearly separated, so it is hard to follow the exact training procedure of SPPO in the paper. Related to this point, hyperparameters for DPO and IPO experiments throughout the iterations should also be more explicitly stated. The paper needs to clearly define what constitutes an "iteration," "round," and "epoch" within the context of SPPO training. Specifically, it should clarify whether an iteration refers to a complete pass through the dataset or a single update step, and how these relate to the concept of an epoch. The hyperparameters for DPO and IPO, such as the learning rate, batch size, and beta values, should be explicitly stated for each iteration to ensure reproducibility.

### Questions
Along with some points above, some additional questions are:

**1. Generation length and SPPO?**

In common, DPO and SPPO are leveraging the sum of log ratio between $\pi$ and $\pi_t$ given the prompt and response pair $(x, y)$, which could be sensitive to the length of generation. As SPPO is a single response-based method, length variance in $\mathbf{y}\sim \pi_t(\cdot|\mathbf{x})$ could induce high variance in the SPPO loss, which could lead to spurious length biases during the optimization as in DPO [1]. Regarding SPPO also results in longer generations as in iterative DPO in Table 1, would SPPO also be prone to the length bias?

&nbsp;


**2. Compatibility with classifier RMs?**

As the paper thoroughly shows, PairRM best fits the algorithmic design of SPPO. However, the Bradley-Terry model-based reward models (i.e., classifier RMs) are also applicable to approximate $P(y > \pi_t|x)$ by comparing the scalar values. Furthermore, there are many classifier RMs which are probably better than PairRM on classifying the better/worse response regarding the moment of submission [2]. How would those RMs impact SPPO?


&nbsp;
&nbsp;


**References**

[1] Disentangling Length from Quality in Direct Preference Optimization (Park et al., 2024)

[2] RewardBench: Evaluating Reward Models for Language Modeling (Lambert et al., 2024)

### Soundness
3

### Presentation
3

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
This paper introduces SPPO an approach to align language models with human preferences. SPPO models alignment as a two-player, constant-sum game aimed at reaching the Nash equilibrium, which provides a theoretically sound basis for iteratively optimizing preferences. The approach uses a smaller, pre-trained preference model PairRM and a limited dataset to achieve high alignment performance across various benchmarks, including AlpacaEval 2.0, MT-Bench, and the Open LLM Leaderboard, without additional supervisions from stronger models.

### Strengths
- Introduced a self-play, game-theoretical framework for preference alignment, leveraging a Nash equilibrium formulation.
- Proposed a new optimization objective that improves practical application and is theoretically motivated.
- SPPO demonstrates state-of-the-art results in multiple language model benchmarks and alignment benchmarks, outperforming DPO and IPO.

### Weaknesses
 - Lack of comparison with conventional RLHF methods. This paper does not include a direct comparison with conventional RLHF methods, i.e., BT formulated RM and PPO training with it. The absence of this comparison makes it difficult to assess the practical advantages of SPPO over established techniques, particularly given the widespread use and understanding of PPO in the RLHF domain. Specifically, the paper lacks an analysis of how SPPO's performance compares to a standard PPO implementation with a reward model trained using Bradley-Terry (BT) pairwise comparisons, which is a common approach for learning reward functions from human preferences.
- Lack of comparison with similar methods. The paper lacks a comparison with conceptually similar work, such as Nash Preference Optimization (NPO). Without this, it is difficult to assess whether the proposed objectives in SPPO offer practical or theoretical advantages over existing approaches. The absence of this comparison makes it difficult to determine whether the gains observed with SPPO are due to the specific game-theoretic formulation or if similar performance could be achieved with existing methods that also aim to optimize for Nash equilibria in preference learning.

### Questions
The results indicate that the performance of DPO and IPO declines in iterations 2 and 3, whereas SPPO continues to improve across iterations. Could the authors provide insights why can SPPO maintains steady improvements while DPO and IPO do not?

### Soundness
4

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
This paper proposes a new preference learning algorithm, self-play preference optimization (SPPO for short), the main contribution comes from the new loss objective, which does not rely on pairwise comparisons. Experimental results show consistent improvements over iterative DPO and IPO.

### Strengths
1.	SPPO casts the RLHF as a constant-sum two-player game, and solves Nash equilibrium policy by proposing a simple form of loss function.
2.	This paper also draws some connections with policy gradient and token-level Q* learning approaches.

### Weaknesses
1.	The annotation step in line 4 of Algorithm 1 requires K^2 calls for preference model, which should be time consuming. 
2.	The preference model in this paper should play a critical role, however, this paper only test on a very specific model, called PairRM, it is not clear to me how reliable this algorithm works on other tasks. Also, SPPO should be an online algorithm, the preference model should be also updated together with policy model in order to capture the probability distribution of evolving policy.
3.	Experiments are on prompts from Ultrafeedback, LLMs of 7-8B, and only one fixed preference model PairRM, SPPO should be tested in more general settings.

### Questions
1.	I believe the preference model, here is PairRM, is critical for the final performance of SPPO, it will be good if the authors also run experiments with other models (e.g. UltraRM-13B)
2.	The annotation step in line 4 of Algorithm 1 requires K^2 calls for preference model, then, the authors select the highest and lowest PairRM scores and winning and losing responses. This setting is used also for DPO and IPO? If so, the only differences come from the loss function definition?
3.	The work of SPO from Swamy et al. uses win rate as reward, and SPPO also computes K^2 preference scores, which should be very easy to be converted into win rate, then you can apply PPO etc for update. I’d like to see those results in Table 1 (this comparison can also answer some comments and questions from paragraph 4 in Section 1.)
4.	Snorkel-Mistral-PairRM-DPO should be a fair comparison for SPPO, as they both use PairRM in their pipeline. What’s the difference between Snorkel-Mistral-PairRM-DPO and Mistral-7B-DPO? The gap is very significant.
5.	In Figure 1 (should be Table?), why the base policy Mistral-7B-Instruct-v0.2 becomes worse at the first and second iterations. And the difference between 7.59 and 7.51 should be not significant.
6.	Do authors also evaluate Snorkel-Mistral-PairRM-DPO in Table 3? And Mistral-7B-DPO and IPO are worse than their base policy model. Thus, the prompts from Ultrafeedback should be not useful for GSM8k and other tasks?

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
The work proposes a new method of LLM alignment called Self-Play Preference Optimization (SPPO). This algorithm is an iterative process. In each iteration, the Mean Square Error (MSE) loss function is minimized between the implicit reward formulated by Rafailov [1], in which the policy from the previous iteration acts as the reference policy, and the reward normalized by a function Z (x), which depends on the prompt (in practical implementation, this function is replaced by a constant).

Based on works that consider online alignment methods from the perspective of game-theory,  the expected probability that the response y is better than the responses of the policy from the previous iteration is used as reward for the answer y (in a practical implementation, the expectation is estimated by a finite number of responses using a preference model).

Proof of convergence to the Nash equilibrium on average is demonstrated. The proposed algorithm's connection with the Policy Gradient (PG) algorithm and Token-level Q* learning is shown. 

The experimental setup used Llama-3-8B-Instruct and Mistral-7B-Instruct-v0.2 models, UltraFeedback dataset, and PairRM was used as the preference model. The quality was evaluated using AlpacaEval 2.0, Arena-Hard, MT Bench, and OpenLLM LeaderBoard benchmarks. The results show that SPPO generally outperforms their baseline counterparts.

### Strengths
- Convergence: A proof of algorithm convergence is provided.
- Relation to Other Methods: Theoretical analysis demonstrates how the proposed algorithm relates to other popular methods.
- Benchmarks: The algorithm's performance is evaluated on a large number of popular benchmarks for assessing general assistants.

### Weaknesses
The main weaknesses of this paper are threefold:

- Missing Analysis of Hyperparameter $\eta$ ($\beta$ in Rafailov et al. [1]): Rafailov et al. [2] demonstrated a clear relationship between the KL divergence with the original policy and the quality of responses. Comparing algorithms with different KL divergences is incorrect, as one may have lower response quality due to a lesser KL divergence with the original policy. Quality can be improved by adjusting the hyperparameter  $\eta $ ($\beta$). The results would be more convincing if presented as a Pareto front, as done by Rame et al. [3].
- Absence of Comparison with Other Game-Theory-Based Methods: Since the work relies on Nash equilibrium and cites other methods grounded in the same theory, it is logical to compare the proposed method with the Nash-MD [4] algorithm, as well as Nash-EMA [4] and DNO [5] (For Nash-MD and Nash-EMA the convergence was proven by the last iteration rather than on average).
- Limited Experimental Setup: The algorithm's efficacy was tested only on two models of approximately the same size and one dataset. It would be interesting to see how the proposed method behaves with models of different sizes and on other tasks.

### Questions
Am I correct in understanding that the equality between equations 3.9 and 3.10 is not strict and is accurate up to a constant $\frac{2}{\eta}$?

### Soundness
3

### Presentation
3

### Contribution
3
