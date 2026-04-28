# RRM:  Robust Reward Model Training Mitigates Reward Hacking

- Decision: Accept
- Avg Score: 6.50
- Scores: 5, 8, 8, 5

## Abstract
Reward models (RMs) play a pivotal role in aligning large language models (LLMs) with human preferences. However, traditional RM training, which relies on response pairs tied to specific prompts, struggles to disentangle prompt-driven preferences from prompt-independent artifacts, such as response length and format. In this work, we expose a fundamental limitation of current RM training methods, where RMs fail to effectively distinguish between contextual signals and irrelevant artifacts when determining preferences. To address this, we introduce a causal framework that learns preferences independent of these artifacts and propose a novel data augmentation technique designed to eliminate them. Extensive experiments show that our approach successfully filters out undesirable artifacts, yielding a more robust reward model (RRM). Our RRM improves the performance of a pairwise reward model trained on Gemma-2-9b-it, on RewardBench, increasing accuracy from 80.61\% to 84.15\%. Additionally, we train two DPO policies using both the RM and RRM, demonstrating that the RRM significantly enhances DPO-aligned policies, improving MT-Bench scores from 7.27 to 8.31 and length-controlled win-rates in AlpacaEval-2 from 33.46\% to 52.49\%.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
Traditional reward model (RM) training for large language models (LLMs) struggles to separate prompt-driven preferences from irrelevant artifacts like response length and format. This work introduces a causal framework and data augmentation technique to remove these artifacts, resulting in a robust reward model (RRM) that improves performance across benchmarks, enhancing accuracy and alignment scores significantly.

### Strengths
This paper addresses an important issue in preference datasets: how to disentangle prompt-driven preferences from prompt-independent artifacts.

### Weaknesses
While the problem studied in this paper is significant, the proposed solution is relatively straightforward, focusing only on expanding the dataset. To remove prompt-independent artifacts, the dataset size needs to be several times larger, increasing the training cost. Additionally, as shown in Figure 5, the effect of this costly augmentation is not very significant—after inserting 30% artifacts, the RRM only decreases from the original RM’s 25% to 20%.

Regarding Table 1, the reasoning performance declines, and the authors explain this as due to math and coding tasks being less affected by non-contextual artifacts. This raises the question of whether the proposed method might have a negative impact on attributes unaffected by non-contextual artifacts.

### Questions
The method proposed in this paper to 'disentangle prompt-driven preferences from prompt-independent artifacts' seems to only eliminate biases unrelated to the input while preserving input-related preferences. This can effectively reduce bias under the 'helpful' alignment objective. However, if our alignment goal is 'safety', the response might be prompt-independent, typically just refusing to reply. Yet humans may still have preferences for different ways of refusal. In this case, how can we disentangle prompt-independent preferences from prompt-independent artifacts?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper aims to learn reward models that are unbiased by “artifacts” that come from human preference data: namely length biases and formatting. To do so, they propose to augment the RLHF preference dataset with preference pairs where one sample is in response to the prompt, and the other example is not in response to the prompt. They evaluate their learned reward model on reward bench and use it to improve downstream policy performance.

### Strengths
- The authors study a very relevant and timely problem.
- The paper shows significant improvement in both reward modeling accuracy and in downstream policy performance.
- The authors do a really interesting study where they artificially add artifacts to the preference dataset, and find their method is more robust to it.

### Weaknesses
 - The main weakness of this paper is that the experiments are not that comprehensive. Although the results are strong, the experiments are only conducted on one dataset, with one model, and with one random seed. Therefore we cannot tell if the results are statistically significant or generalizable.
- The baseline is pretty weak with regards to reward bench. RLHFFlow with Llama 3 8B gets 87.1 on reward bench, while the author’s baseline gets 80.
- The writing describing the methodology not that clear. I think more plainly describing the data augmentation would be better.
- The data filtering step used in their method hurts their experiments interpretability, as it may be the case that the sole reason RRM gets good performance is due to the data filtering step. They should include a baseline where the original dataset is filtered, and then a RM is trained based on that.

### Questions
- How did the authors tune the hyperparameters?
- What are the “three possible prompts” described in line 226?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper presents a method to enhance the robustness of the reward model for LLM alignment. More specifically, rewards models are trained based on the question and the human labelers' preference over the answer pairs. A commonly observed un-robust behavior of the reward model is that there are spurious correlations between the label and the artifacts in the answers which is not relevant to the question. The existence of such spurious correlations causes the reward model to favor certain types of artifacts, e.g. the length of the answer.

In previous works, some of the artifacts are specifically dealt with, like introducing a penalty for the length of the answer. However, the solutions lack a principle and can not handle other artifacts like the word preference and style of the answers. In this work, a systematic approach is proposed based on a causal framework, which is effective in debiasing the reward model from various artifacts.

### Strengths
- The causal framework has been effective and widely used in other problems, but this is the first time I see it applied in LLM reward modeling, and it very well suits the problem under consideration.
- The implementation is very straightforward, just augment the data, no empirical tricks.

### Weaknesses
 - It seems suboptimal to me to train the reward model that is only dependent on the S, because the A part could contribute nontrivially to the reward function, in the case where both answers are equal in terms of the contextual quality, the labeler could prefer the answer which is organized as bullet points for readability.
- The explanation on why "reasoning" is performing worse under RRM is not quite convincing. Even if they are less affected by non-contextual artifacts, the augmented data should not have caused the degrade of performance either (as the augmented data are simpler pairs). I would suggest two other hypothesis to investigate:
  - Look into how "-Neutral" works on "Reasoning" as requiring 50/50 preference over some random pairs could be too strong.
  - Try to add back the "A only" reward model, as mentioned above the artifact could contribute nontrivially to the reward, removing it entirely could be detrimental especially for math and code, where a high quality answer should be good in formatting which is noncontextual.

### Questions
- The same augmentation and disentangle technique can be applied to learn a artifact only model. Some of the artifacts would improve the quality of the answer, if there is a consensus preference on such artifacts in the labelers. Is there any proposal to combine the contextual & non-contextual models? Would adding these two reward models work, or do we need to take the min of these two models? Any suggestions from the authors?

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes a robust reward model (RRM) training method to mitigatge reward hacking by utilizing causal inference framework. A causal graph for human preference modeling is introduced to enable the model to distinguish contextual preference signals and context-free artifacts. The training data is augmented by re-organizing the (prompt, positive, negative) triplet guided by the causal inference framework. Experiments show that the proposed approach can filter out undesirable artifacts in reward model training and yields a more robust reward model. Specifically, the reward model is trained on Gemma-2-9b-it, and RRM improves RM by an absolute 3.54% accuracy gain on Reward-Bench. Experiments also demonstrate the policy induced by RRM outperforms RM and ODIN in MT-Bench and AlpacaEval-2 benchmark. Analysis show that length artifact and deliberately designed artifact can be eliminated.

### Strengths
Reward hacking is an important problem in LLM alignment. This paper introduces causal inference framework in reward modeling to mitigate reward hacking, which offers an interesting perspective. This idea makes a lot of sense since the essence of reward hacking mitigation is to find out the irrelevant artifacts that have no causal relationship with the preference label, and causal inference algorithms just offer a useful tool. The idea is clearly presented and illustrated. The experiment results verify the effectiveness of proposed method.

### Weaknesses
The experiments are insufficient. First, the experiments in this paper only cover two possible artifacts, namely length and a deliberately designed phrase, which is not compatible with author's claim that this method should be capable of handling "all potential exploitation patterns". More patterns such as format, emojis, and other stylistic variations should be investigated in the experiments to demonstrate the robustness of the proposed method across a wider range of potential reward hacking strategies. Second, the reward model is trained only using Gemma-2-9b-it. More experiments should be conducted on different model types such as llama, and larger model sizes such as 57B and 72B. It is in doubt that when the model size increases, the reward hacking problem can be naturally mitigated and the effectiveness brought by this method may diminish. The paper should explore if the proposed method's benefits are consistent across different model architectures and scales, as larger models may exhibit different biases and sensitivities to reward hacking. Third, in terms of policy evaluation, this method is only verified in DPO training whereas various other methods should also be considered such as PPO, whose performance relies heavily on reward model quality. The evaluation should include a broader range of policy optimization algorithms to ensure the generalizability of the findings. Last, the author is suggested to add more baselines in experiment, such as reward model ensemble which can also alleviate reward hacking. The lack of comparison with ensemble methods limits the understanding of the proposed method's relative advantages.

### Questions
1. Explain why it is needed to add neutrals and set both non-contextual responses as tie in Section 3.2. What is the necessity of this step?
2. In Table 2, why the performance of RRM is not consistent in two chat datasets such as Chat and Chat Hard? In Chat dataset, RRM outperforms RM while in Chat Hard dataset, RRM is even worse.

### Soundness
1

### Presentation
3

### Contribution
2
