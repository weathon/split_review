# Taming Overconfidence in LLMs: Reward Calibration in RLHF

- Decision: Accept
- Scores: 6, 8, 6, 5

## Abstract
Language model calibration refers to the alignment between the confidence of the model and the actual performance of its responses.
While previous studies point out the overconfidence phenomenon in Large Language Models (LLMs) and show that LLMs trained with Reinforcement Learning from Human Feedback (RLHF) are overconfident with a more sharpened output probability, in this study, we reveal that RLHF tends to lead models to express verbalized overconfidence in their own responses.
We investigate the underlying cause of this overconfidence and demonstrate that reward models used for Proximal Policy Optimization (PPO) exhibit inherent biases towards
high-confidence scores regardless of the actual quality of responses. 
Building upon this insight, we propose two PPO variants: PPO-M: \underline{PPO} with Calibrated Reward \underline{M}odeling and PPO-C: \underline{PPO} with Calibrated Reward 
\underline{C}alculation. 
PPO-M integrates explicit confidence scores in reward model training, which calibrates reward models
to better capture the alignment between response quality and verbalized confidence.
PPO-C adjusts the reward score during PPO based on the difference between the current reward and the moving average of past rewards. 
\textit{Both PPO-M and PPO-C can be seamlessly integrated into the current PPO pipeline and do not require additional golden labels.}
We evaluate our methods on both \texttt{Llama3-8B} and \texttt{Mistral-7B}
across six diverse datasets including multiple-choice and open-ended generation.
Experiment results demonstrate that both 
of our methods
can reduce calibration error and maintain performance comparable to standard PPO. 
We further show that they do not compromise model capabilities in open-ended conversation settings.}

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
In instruction-following for language models, the paper studies the task of reporting a confidence score in the helpfulness and accuracy of the model's own response. The paper shows that existing reward models are biased in favor of high-confidence scores, and proposes two mitigation methods. The first method involves data augmentation for the reward model, and the second method adds a customized term to the reward in PPO. The methods show improved calibration with no noticeable performance degradation.

### Strengths
The paper studies an important and interesting topic, that of verbalized calibration in instruction-following for language models. It is easy to follow and clearly demonstrates the existence of the problem and the success of the proposed mitigation methods. The methods do not require new data to be collected, making them straightforward to use, and yet the improved calibration transfers from reward model scores to accuracy on multiple-choice datasets.

### Weaknesses
Although the paper studies a broadly important topic and is well-executed, I think the strength of the contribution itself is somewhat limited:
- From a scientific perspective, the methods do not offer much insight: there is no distinction between different confidence levels other than "high scores" and "low scores", and the methods just increase the reward for high scores for high quality responses and low scores for low quality responses. So it is not really surprising that they improve calibration.
- This wouldn't be a problem if the methods had a lot of practical value. But from a practical perspective, the methods don't seem that useful either: if the user wanted a confidence score in the quality of the response, you could just display the reward model score (or some prompt-calibrated version) to the user. It's true that it's nice to have this distilled into the model, but there are many alternative ways in which one could do this, such as distilling the reward model score into a special token's logit. And if you just want a calibrated confidence score in the accuracy of a short-form response, there are many existing alternatives available.

In spite of this weakness, I consider the paper to be above the acceptance threshold because of the careful analysis the paper provides.

I also have a more minor issue with the definition of gamma for the PPO-C method (Line 279): the factor of |r_i (hat)| doesn't make sense to me. Unless the reward model is trained with an L2 penalty on the rewards or similar, the location of the reward is meaningless, since the loss uses only the difference between rewards, so taking an absolute value doesn't make sense. Even if the reward model is trained with an L2 penalty, I don't see why there should be a bigger adjustment for rewards that are far from 0 – or if there is some reason, it may be good to discuss it. Instead, to ensure that gamma is correctly scaled, it would make more sense to me to use some measure of spread of the rewards, such as standard deviation.

A couple typos:
- Line 134: "Dand" -> "D and"
- Line 1046: "calirbation" -> "calibration"

### Questions
I didn't understand the paragraph at Lines 239-244. It sounds like you are saying you didn't train the reward model yourself for PPO-M, but I don't see how that could be, since you need a reward model trained on your new calibration dataset. Are you saying that you fine-tuned an existing reward model on the new calibration dataset? Please clarify.

### Soundness
4

### Presentation
4

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper focuses on LLM calibration: the alignment between the confidence a model expresses and its actual performance. Previous research has demonstrated the phenomenon of overconfidence in LLMs, especially those trained using RLHF, which tend to have a sharpened output probability. The systematic bias in reward models used for RLHF is one of the key causes of LLM overconfidence.

The paper proposes two methods to address the issue of verbalized overconfidence in LLMs trained with RLHF:

(1) **PPO-M**: a reward model re-training objective that aims to fine-tune existing BT-based reward models. PPO-M achieves this by augmenting existing pairwise ranking datasets with verbal confidence scores. The author filtered samples from various open-source datasets, prepended a confidence-query system prompt to each, and randomly assigned high and low confidence scores, creating a modified training dataset.

(2) **PPO-C**: a reward-shaping method that dynamically adjusts reward scores during PPO training based on a moving average of past rewards and the model's verbalized confidence level. PPO-C differs from vanilla PPO in that it incorporates a confidence-query system prompt into a portion of the training prompts to elicit verbal confidence scores from the model. The reward function promotes higher confidence for responses exceeding the moving average and lower confidence for those falling below.

---
*Nov. 26 update*: most of my concerns are resolved, satisfied with the added evaluations, and raised the rating from 6 ---> 8 while maintaining my confidence of 3.

### Strengths
- This paper is very well-written and easy to follow. The motivation is well-supported by evidence, including visualizations of confidence distributions and accuracy, that highlight the overconfidence phenomenon.
- The proposed methods are straightforward, yet backed by a sufficient amount of evaluation on different families of open-weights models and on diverse benchmarks. The thorough evaluation, along with the authors' transparency in presenting both the strengths and limitations of their approach, makes their findings trustworthy - small improvements in the factuality-focused benchmarks as expected (e.g. TruthfulQA benchmark) and almost no improvement in chat performance (e.g. MT-Bench, Arena-Hard).

### Weaknesses
 - Referring to Eq. 2 as the "PPO-M" loss could be confusing, as it is not directly related to the standard PPO objective. This equation is, in fact, a re-training objective for the reward model rather than a modification of PPO itself. The labels "PPO-M" and "PPO-C" might suggest that the paper centers on enhancing PPO objectives, when the proposed methods primarily aim at co-training the reward model with verbal confidence. This distinction could benefit from clarification to prevent misunderstanding.

- While not introduced in this work, the use of verbal confidence to measure a model's confidence in its response may not be ideal. Language models, especially those under 70B parameters, may simulate confidence without true understanding due to limitations in reasoning capability. Have you examined the logits for the 0–10 range when asking for verbal confidence? Observing how these tokens are distributed might provide insight into whether the model is indeed producing a typical probability distribution or simply outputting values. Given these concerns, more concrete metrics, such as those derived from entropy in token-space, might be more accurate indicators of true confidence.

- The confidence metric presented in Figure 2 lacks clarity, and the "perfect calibration" line does not contribute meaningful differentiation between a model's overconfidence and cases where the dataset may simply be too easy. Maybe Llama-3-8B-PPO's performance on CommonsenseQA could indicate that the questions are too easy leading to high confidence in correct answers.

- Given that Figure 2 does not reflect the effects of PPO-M and PPO-C, it would be valuable to include a distribution of confidence scores after tuning with these proposed methods. This would enable a direct comparison of the effects of the calibration techniques on model confidence.

-  Figure 3 would benefit from results that combine the answer and confidence score to more clearly illustrate how the proposed methods affect the chosen/rejected ratio.

### Questions
- I understand that just for the sake of an evaluation of how the current chat models are conditioned on the given verbal confidence, appending a random confidence score to the RewardBench dataset may make sense. Why not simply prompt the chat models to self-annotate? Asking models to generate their own confidence scores could yield a more genuine assessment of how they internally gauge response certainty.

- Figure 2 primarily highlights instances of overconfidence, but are there scenarios where the SFT model consistently exhibits low confidence? It would be interesting to see if the proposed methods can help address underconfidence in addition to overconfidence, particularly if SFT models tend to understate confidence levels.

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
5

### Summary
The paper tackles the problem of calibration in LLMs that went through RLHF, and specifically calibration through verbalized confidence. Based on prior work that showed that RLHF hurt the model calibration, the authors point to the reward model as the source of the problem. They demonstrate that off-the-shelf reward model have a bias towards answers with high-confidence. As a solution, they propose two different methods that should overcome this problem - one focus on the reward model training and the other fix the rewards given during policy optimization.

### Strengths
- The paper has a clear structure, beginning with analysis experiments, moving to the proposed method, and concluding with experiments that showcase its effectiveness.
- The experiments are comprehensive, covering multiple datasets and showing clear improvement in calibration metrics.
- The problem addressed is relevant and of interest to the community.

### Weaknesses
 - The conclusion drawn from Figure 2 doesn’t align with the plots. It’s not that the model after RLHF isn’t overconfident, but rather that the model before RLHF is also overconfident. Nearly all the bins fall below the diagonal line, indicating overconfidence. Additionally, why are the data points so sparse? How many prompts were used in this experiment?

- In Figure 3, since the reward models haven’t been trained with this type of prompt, I would suggest running a control experiment—appending the prompt with a random confidence score to both chosen and rejected answers (similar to PPO-M training). With random confidence scores, we would expect the reward model, on average, to still prefer the chosen answer. If it doesn’t, this would indicate that the prompt is so far out of distribution that the reward model isn’t applicable (which highlights its brittleness, though that’s a separate issue).

- While I understand the algorithm used in PPO-C, the intuition behind it isn’t clear to me. Why would the average reward across the dataset serve as a threshold for determining if a model’s response is correct? Couldn’t it be that most responses are either correct or incorrect, depending on the dataset and model? This approach seems like a heuristic that would only work on datasets where the model is correct about 50% of the time. 
Additionally, why is $\Delta r$ defined as a running average of $r$ rather than $\hat{r}$? On a related note, wouldn’t an off-the-shelf reward model struggle to assign rewards to answers that include confidence scores (i.e., $r$) since it wasn’t trained on such data?


### Questions
- Regarding PPO-M, is it intended to be an additional objective to equation 1? Because there is nothing in equation 2 that will make the reward of the chosen answer higher than the rejected one.

- Line 270: what do you mean by “biased response”? Why does asking for confidence create bias?

### Soundness
2

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
3

### Summary
This paper identifies a systematic bias in reward models that favors high-confidence responses regardless of their actual quality. They propose two solutions for this bias issue: PPO-M, which calibrates reward modeling by aligning confidence levels with response quality, and PPO-C, which adjusts standard reward model scores during PPO training. Empirical results show their methods can reduce expected calibration error without compromising accuracy or instruction-following ability in open-ended generation.

### Strengths
1. Good motivation to identify the systematic bias and propose intuitive solutions.
2. The presentation is clear and easy to follow, with a logical and well-reasoned train of thought.
3. Sufficient empirical results to justify the effectiveness of proposed methods

### Weaknesses
1. Regarding the proposed PPO-M, there is no guarantee that the model would prefer $(y_c,h_c)$ over $(y_r,l_r)$. This could be a potential reason why the calibrated model results in lower ACC metrics than the uncalibrated PPO shown in the tables. Although the systematic bias may cause the model to prefer $h_c$ over $l_r$, PPO-M lacks an explicit mechanism to enforce this preference. Have you considered jointly optimizing (1) and (2) to enforce $y_c$ over $y_r$ as well?

2. Since PPO-C depends on a running average reward for confidence calibration, the $\alpha$ affecting the moving average could be an important factor. However, there seems no evaluation of how $\alpha$ affects PPO-C. I suggest experiments to show how varying $\alpha$ influences reward magnitude and performance. Moreover, are you assuming that $\hat{r}(y_c)>\Delta r$ and $\hat{r}(y_r)<\Delta r$? If so, would be helpful to explicitly state the assumption and analyze its appropriateness.

3. The design and evaluation of the proposed algorithms, as noted above, lack clarity or rigor. The formulations would benefit from a more detailed and persuasive explanation. Ideally, theoretical support should be provided to justify that the approach achieves debiasing without compromising model performance. At present, the methods appear to rely heavily on heuristics rather than principled algorithm design, which diminishes the significance of the contribution.

### Questions
1. Why not add something similar to (1) onto (2) to enforce the preference of $(y_c,h_c)$ over $(y_r,l_r)$?
2. Why do PPO-M and PPO-C often result in lower ACC?
3. How does $\alpha$ affect the results of PPO-C?
4. Are you assuming that $\hat{r}(y_c)>\Delta r$ and $\hat{r}(y_r)<\Delta r$?

Overall, It is a well-motivated work presented in a structured manner. However, the contributions lack substantial impact. The proposed algorithms resemble engineering techniques rather than rigorous, principled approaches.

## Lower confidence after discussion
I maintain my critique of the heuristic algorithm's lack of rigorous design but am less certain if this empirical research meets ICLR standards. I've reduced my confidence to 3. 

To be honest, the algorithm's design and naming seem somewhat inelegant and naive. While empirical results are solid, nowadays it has become increasingly difficult to determine whether their success stems from effective code-level implementation, a limited dataset, or a genuinely strong algorithm.

Since other reviewers have given higher ratings, I am open to its acceptance as a poster. That said, I would be deeply disappointed if it were elevated to the level of a spotlight or oral presentation, as I believe this would set a poor precedent for ICLR's standards.

### Soundness
2

### Presentation
4

### Contribution
2
