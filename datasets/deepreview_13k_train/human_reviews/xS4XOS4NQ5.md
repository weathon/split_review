# General Preference Modeling with Preference Representations for Aligning Language Models

- Decision: Reject
- Scores: 5, 3, 6, 6

## Abstract
Modeling human preferences is crucial for aligning foundation models with human values. Traditional reward modeling methods, such as the Bradley-Terry (BT) reward model, fall short in expressiveness, particularly in addressing intransitive preferences. Although supervised pair preference models (PairPM) can express general preferences, their implementation is highly ad-hoc and cannot guarantee a consistent preference probability of compared pairs. Additionally, they impose high computational costs due to their quadratic query complexity when comparing multiple responses. In this paper, we introduce \emph{preference representation learning}, an approach that embeds responses into a latent space to capture intricate preference structures efficiently, achieving linear query complexity. Additionally, we propose preference score-based General Preference Optimization (GPO), which generalizes reward-based reinforcement learning from human feedback. Experimental results show that our General Preference representation model (GPM) outperforms the BT reward model on the RewardBench benchmark with a margin of up to 5.6\% and effectively models cyclic preferences where any BT reward model behaves like a random guess. Furthermore, evaluations on downstream tasks such as AlpacaEval2.0 and MT-Bench, following the language model post-training with GPO and our general preference model, reveal substantial performance improvements with margins up to 9.3\%. These findings indicate that our method may enhance the alignment of foundation models with nuanced human values.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper studies the intransitive (cyclic) preferences problem in reward modeling. Traditional reward models such as BT model and PairRM cannot handle cyclic preferences scenarios. To address this issue, this paper proposes General Preference Optimization (GPM) via embedding the preference information in the latent space (called preference representation learning). The proposed  reward model can be applied to common direct preference alignment methods such as DPO and SPPO. The experimental results validate the effectiveness of GPM in handling cyclic preference scenarios.

### Strengths
1. This paper studies the intransitive (cyclic) preferences problem, and analyzes the weakness of traditional BT and PairRM reward models. This problem in preference rewarding is very interesting and needs more efforts from the community.
2. The proposed GPM method is well-motivated, and it keeps the computational complexity with the BT model while can handle the cyclic preferences in the same time. Besides, this method can be adapted into the direct preference alignment methods (though may not be directly used in RLHF pipeline with policy-gradient based method e.g., PPO since it is pair based optimization, please correct me if understand wrong).
3. The experimental results demonstrate the effectiveness of the proposed method in handling the cyclic preferences.

### Weaknesses
1. It may be not appropriate to use Games such as Tic-Tac-Toe, Go, starcraft Elo system to establish the motivation of the cyclic preference. This paper mainly studied the language model preference, i.e., the generated response for the given question. Generally, for the given user question, the preferences of candidate responses satisfies total ordering, which means there will be nearly no cyclic preference cases. Think about in the preference annotation workflow, for the same question, it rarely has the case Response A > Response B  > Response C while Response A < Response C, except changing the criteria of evaluating the response. Also, the success of Lmsys Chatbot Arenas system can also validate this point.
2. The strength of GPM in terms of computational complexity is overclaimed. Starting at L324, the authors claim that they have advantage in computational efficiency. However, the most commonly used BT reward model only has O(K) complexity (K times inference forward), and does require the embedding computation, which means it has better efficiency than the proposed GPM. I hope the authors can revise this paragraph to make it clear.
3. Actually, the cyclic preference is very rare in the chatbot (LLM generation) scenarios, thus the authors have to establish a specially designed cyclic "instruction following ≻ honesty ≻ truthfulness ≻ helpfulness ≻ instruction following" for ultrafeedback dataset. This preference criteria establish needs to be explained and justified. How well it aligns with the overall score? It is also suggested to show provide the accuracy in terms of overall score in Table 1. Thus, the results may not directly validate the effectiveness of the proposed method since the established criteria is not well justified.
4. The alignment performance of  LLMs using GPM is somewhat moderate, showing no surprises. As shown in Table 3 and Table 4, the performance of GPM in the iteration 3 is marginally better than methods using BT model. Notably, for a more fair comparison, we should control the length bias in the preference. The length controlled win-rate results are shown in Table 6 (Appendix), which show that the GPM has no significant advantages in aligning the LLM over BT model. And I suggest the authors to use the LC win rate to show their results in the main body, as LC win rate is more fair.

### Questions
Please see the weakness. My major concern is about the commonness or generalization of cyclic preference in LLM alignment (chatbot scenario), and the relatively weak alignment performance using GPM.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper introduces the GPM with preference representation learning for efficiently capturing complex human preferences. Traditional models, such as the BT, struggle to represent intransitive preferences and suffer from computational inefficiencies, particularly for tasks with large response sets. 
The GPM model addresses these issues by embedding responses into a latent space, enabling more expressive preference modeling with linear complexity. This paper also proposes GPO and show gains on policy optimization. 

Summary of contributions: 
- This paper proposed GPM, which efficiently models complex, cyclic, and intransitive preferences with linear complexity.
- This paper demonstrates that GPM outperforms BT on various benchmarks, including RewardBench.
- Enhanced language model alignment on tasks such as AlpacaEval2.0 and MT-Bench when using GPO (w/ GPM).

### Strengths
- This paper is well written and is very clear. 
- This paper provides a novel approach by embeds responses into a latent space to capture intricate preference structures efficiently. The preference representation learning and skew-symmetric operators is innovative and well-suited for addressing limitations of traditional methods

### Weaknesses
 - It's very interesting to see GPM can capture the cyclic preferences that previous methods cannot. Further experiments on how "capture cyclic preferences" can help existing LLMs to produce better results or show some improvement on downstream applications can demonstrate the true value of this.  

- As the authors already mentioned in the limitations section, this paper would benefit from having enough discussion and analysis on representation vector (v) generation (model architecture choice). Without solid ablation study, it's hard to judge whether this method can be generalized. The performance pattern difference on 2b and 8b models also shows that this method may require specific recipe for specific use cases.

### Questions
- Can the authors elaborate a bit more on line474-475, "To avoid the preference bias when using GPT-4-turbo as the evaluator"? Why GPT 4omini would be better to be used as alpacaeval2.0 evaluator here? 
- Are the results using GPM general longer than baseline? As alpaca 2.0 eval introduced LC WR to mitigate length bias, it could be helpful for the authors to further elaborate why they think WR is a better metric to use (Table 3 in main text) in this case? As shown in appendix Table 6, the gain of the proposed methods on LC WR is smaller.

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
3

### Summary
* In terms of methods proposed:
    * This paper proposes the GPM approach to model general preference. GPM computes preference probability by multiplying a skew-symmetric block-diagonal matrix (referred to as “Skew-symmetric Preference Operator”) with learned embeddings (referred to as “preference representation”). This approach has several advantages: (1) ensures P(y1>y2) = P(y2<y1) by design, regardless of input positions. (2) has the capacity to model cyclic preference (e.g., A>B>C>A) which the Bradley-Terry model fails at; (3) has linear complexity O(K) in computing preference among a pool of K candidates compared to previous approaches like PairRM which has quaratic complexity O(K^2). 
    * This paper proposes the GPO objective to align LLM with preference models. GPO is adapted from the SPPO loss by Wu et al. (2024b) for iterative preference optimization except that the preference score instead of preference probability in the loss form. 
* In terms of experiments conducted:
    * (1) Train and evaluate Reward models on a cyclic preference dataset constructed from UltraFeedback. The aim is to show GPM can model cyclic preferences while BT cannot.
    * (2) Train GPMs using the Skywork Reward Data Collection and evaluate on Reward Bench with two base models (2B & 8B). The aim is to show that GPM outperforms BT-based RM in terms of reward modeling. 
    * (3) Finetune a 2B and a 8B model with GPO and SPPO using the BT-based Reward model and the GPM reward model. Evaluate on AlpacaEval 2.0 and MT-Bench. The aim is to show GPO+GPM yields better downstream LLMs.
* In terms of experimental results:
    * (1) They show that GPM has the capacity to model cyclic preferences as intended.
    * (2) They show that GPM attains overall higher scores on reward bench compared to BT-based RM. The gain with 2B model is substantial (+5.6), while the gain with 8B model is marginal (+1.0). 
    * (3) They show substantial gain with GPO+GPM compared to SPPO+BT RM on AlpacaEval 2.0. The results for MT-Bench warrant more discussion than there is in the paper (see Question 5).

### Strengths
* The proposed GPM approach enjoys several desirable theoretical properties as explained in the Summary. This is a good contribution for preference modeling.
* The three sets of experiments are well designed. They cover the main research questions nicely formualed on Line 384-389 that are warranted by the proposed GPM and GPO approaches.
* Experimental results of GPO+GPM as evaluated on AlpacaEval 2.0 shows substantial gain compared to previous SPPO+BT RM approach.

### Weaknesses
 * Presentation of methods:
    * The von Neumann winner is introduced in Sec.5 where GPO is proposed, but it is not clear how this concept relates to the proposed GPO. 
    * The current presentation of Sec.5 is confusing and redundant. It starts with a general review of previous work, repeats the points on computational efficiency that are already made in the introduction, and finally introduces the GPO method in Sec. 5.2. It seems more appropriate to move the texts up to Sec.5.1 into Background/Related Work to make a clear distinction of previous work and this paper's contribution. 
    * Key modeling techniques (Eigenvalue Scale Gate; Eigenvector Embedding Head) are in the Appendix rather than the main text. 
* Clarity in experimental setup and reporting:
    * It seems like the RMs in Table 1 are trained and evaluated on the same dataset. If that's the case, it should be made clear in the main text.
    * It is not clear in the main text how the BT RM is trained (see Question 4). 
    * The "1st" and "2nd" columns in Table 4 lacks explicitly explanation in the caption. 
* Under-discussed experimental results:
    * Table 2, 3 and 4 warrant more thorough discussion. For example, Line 481 reads: “These results suggest that integrating the General Preference representation model (GPM) into policy optimization can enhance the downstream performance of language models”, but Table 4 for MT-Bench shows GPM+GPO yielding marginal gain in MT-Bench score compared to SPPO+BT RM. The results do not support this general claim. 
* Overall, while the paper has good novelty and presents a good set of experimental results, a more detailed, methodical discussion of results is in order. Presentation and clarity in methods could also be improved. The paper would make a much stronger case if these issues are addressed.

[Line 453] Table 2 presents the results. The GPM consistently outperforms the BT model for both base models on RewardBench,with notable improvements in tasks involving complex reasoning (e.g.,Chat Hard and Reasoning).These results highlight the superior expressiveness of the GPM in preference modeling.

[Line 487] Table 2 shows that increasing the embedding dimension generally improves performance. 

[Table 2] Other state-of-the-art models

There are more performant models on the RewardBench leaderboard (https://huggingface.co/spaces/allenai/reward-bench) than the ones cited in Table 2. In particular, the 8B model from Skywork achieves an overall score of 93.1 and seems to me more comparable to the reward models reported in the table in terms of size. 

I would not use the headline "Other state-of-the-art models" because it is inaccurate. What about something like "Other models reported on Reward Bench"? 

Are there particular reasons why these models are more suitable for comparison? If so, they could be included in the caption.

### Questions
1. How is the von Neumann winner related to GPO?
2. I am not sure what the bold font in Table 4 represents. Could you clarify?
3. How is the BT RM trained? From appendix it looks like BT RM refers to the reward model formed by the DPO-trained policy and the reference model, where rewards are calculated as the log-likelihood ratio multiplied by beta. If so, it should be made clear in the main text. 
4. Line 1307 (Appendix B.2): "For the Bradley-Terry (BT) model, the temperature parameter β was set to 1, following standard practice (Rafailov et al., 2024)". Can you clarify what "standard practice" refers to? It is not standard to set beta = 1 in Rafailov et al. In fact, beta is an important hyper-parameter that needs sweeping. 
5. Could you explain the experimental results on MT-Bench in Table 4 in more detail? Specifically, it seems like the improvement is within the margin from sampling compared to the baseline even with the proposed GPO+GPM.

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper proposes a novel approach to modeling human preferences for enhancing the alignment of foundation models with human values. Traditional methods, such as the Bradley-Terry (BT) reward model and supervised pair preference models (PairPM), have limitations in expressiveness, consistency, and computational efficiency. The authors introduce preference representation learning, which embeds responses into a latent space to capture complex preference structures, achieving linear query complexity. They also propose a preference score-based General Preference Optimization (GPO) method, extending reward-based reinforcement learning from human feedback. The experimental results demonstrate that the proposed General Preference Model (GPM) outperforms the BT reward model on the RewardBench benchmark by up to 5.6% and effectively models cyclic preferences. Additionally, evaluations on downstream tasks like AlpacaEval2.0 and MT-Bench show significant performance improvements of up to 9.3% after post-training with GPO and GPM.

### Strengths
1. The preference representation learning approach can capture intricate preference structures, addressing the limitations of traditional methods in handling intransitive preferences.

2. By embedding responses into a latent space, the method achieves linear query complexity, making it computationally more efficient than PairPM, which has quadratic query complexity.

3. The proposed method ensures a more consistent preference probability of compared pairs, reducing the ad-hoc nature of PairPM implementations.

4. Extensive experiments on benchmarks and downstream tasks demonstrate the superiority of GPM over existing methods, providing strong empirical evidence for its effectiveness.

### Weaknesses
1. The introduction of a latent space and preference representation learning adds complexity to the model, which might require more sophisticated training and tuning processes.

2. The latent space embeddings and preference scores might be less interpretable compared to simpler models, making it harder to understand why certain preferences are modeled in specific ways.

3. While the paper provides comparisons with the BT reward model and PairPM, a more comprehensive comparison with other state-of-the-art methods would strengthen the claims about the superiority of GPM.

### Questions
I don't understand why the acc of GPM is 100% on cyclic preference data. Does the experiment involve any information or data leakage?

### Soundness
3

### Presentation
3

### Contribution
3
