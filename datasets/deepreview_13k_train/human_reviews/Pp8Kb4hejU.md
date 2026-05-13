# Adjustable Quantile-Guided Diffusion Policy for Diverse Behavior Generation in Offline RL

- Decision: Reject
- Scores: 5, 3, 3, 5

## Abstract
Offline Reinforcement Learning (RL) addresses the challenge of learning optimal policies from pre-collected data, making it a promising approach for real-world applications where online interactions with an environment are costly or impractical. We propose an offline RL method named Quantile-Guided Diffusion Policy~(qGDP), which trains a quantile network to label the training dataset and uses these labeled samples to train the diffusion model and generate new samples with the trained model according to classifier-free guidance.
qGDP can adjust the preference of sample generation between imitating and improving behavioral policies by adjusting the input condition and changing the guidance scale without re-training the model, which will significantly reduce the cost of tuning the algorithm.
qGDP exhibits exceptional generalization capabilities and allows easy adjustment of action generation preferences without model retraining, reducing computational costs. Experimental results on the D4RL dataset demonstrate state-of-the-art performance and computational efficiency compared to other diffusion-based methods.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper presents a novel offline Reinforcement Learning (RL) algorithm, Quantile-Guided Diffusion Policy (qGDP), which aims to learn optimal policies from pre-collected data without the need for costly or impractical online interactions. The qGDP method involves a quantile network for dataset labeling, and leverages labeled data to train a diffusion model, enabling sample generation for policy improvement or imitation. The flexibility of the qGDP is highlighted in its ability to modify action generation preferences without retraining, promising computational efficiency. Experimental validation is provided through the D4RL benchmark, where qGDP shows superior performance and efficiency relative to existing diffusion-based approaches.

### Strengths
1. The manuscript is well-structured, providing clear insight into the proposed method and its implications for offline RL.

2. It addresses an essential challenge in RL regarding behavior generation diversity, which is critical for robust policy learning.

3. Section 5 effectively elucidates the distinct advantages of qGDP over other methods, offering valuable context and justification for the proposed approach.

### Weaknesses
1. The paper lacks an introductory explanation of quantile networks and their relevance to the proposed method, potentially hindering comprehension for readers less versed in the domain. The authors are encouraged to elaborate on the concept and role of quantile networks within qGDP to provide readers with a foundational understanding of the methodology. An illustration to overview the entire work would be helpful.

2. The core innovation, applying quantile labels to guide the diffusion process, appears somewhat incremental, casting doubt on the method's novelty. Clarification on the specific novelties and contributions of qGDP  would be beneficial.

3. The introduction does not adequately articulate how qGDP surmounts the limitations of prior diffusion-based offline RL methods. It would be advantageous to outline explicitly how qGDP addresses the deficits of previous diffusion-based methods in the introduction.

4. While informative, Section 5 may benefit from condensation to improve readability and maintain focus. Considering the length of Section 5, it is recommended to distill the content to the most salient points to maintain the reader's engagement and enhance clarity.

### Questions
Please refer to the weaknesses.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a novel offline RL algorithm qGDP using quantile labeling and conditional diffusion models. It shows competitive results on D4RL benchmarks compared to other diffusion-based methods. The approach allows tuning action distributions without retraining. However, there are some limitations in justifying the quantile conditioning and comparing against other offline RL methods.

### Strengths
1. Achieves state-of-the-art results among diffusion-based offline RL methods on D4RL.
2. Novel approach of conditioning diffusion on quantile labels for offline RL.
3. Allows flexible tuning of action distributions without retraining.

### Weaknesses
1. The quantile labels rely on the action values Q learned by IQL, which may have overestimation bias. Errors in Q would propagate to incorrect quantile labels, which could be amplified for higher quantiles. This could negatively impact the quality of the diffusion model training.
2. The quantile input y for guiding the diffusion model is constrained to the range [0,1] or not ?  It will limit the scope of behavioral patterns that can be generated. Values greater than 1 may allow more generalization, but this is not explored. And I expected to find the experiment results of different value of y for different generation, but failed.
3. While the quantile input is motivated by IDQL, the paper does not sufficiently differentiate the advantages of the quantile mechanism compared to IDQL itself. The paper does not sufficiently differentiate the advantages of the quantile input compared to just using weighted actions like in IDQL. The results between qGDP and IDQL in Table 1 are fairly close. More analysis is needed to clearly explain the relationship between the two methods and highlight the unique benefits of the quantile inputs.
4. The paper over-emphasizes the impact of tuning the guidance scale, even though adjusting the scale for diversity is intrinsic to diffusion models themselves. However, the main innovation of the paper is using the quantile network to label samples and train the diffusion policy conditioned on quantiles. More analysis is needed on how the quantile inputs specifically affect diversity, rather than just tuning the guidance scale which is a general feature of diffusion models.
5. In Table 4, the runtime of the proposed offline RL algorithm qGDP is compared to the older online RL algorithm DQL? I cannot get the meaning of this comparison.  For a fair runtime comparison, it would make more sense to compare against other recent offline RL algorithms such as IDQL.

### Questions
Please see the above weakness and address my concerns.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes a modification of IDQL with an additional quantile network for offline RL setting. The quantile network predicts values at different quintiles at the same time, thus avoiding re-training when selecting the optimal quantile value. The experiments are evaluated on two domains of D4RL tasks and show superior performance over IQL, IDQL, DQL, etc. I think the proposed method is a quite straightforward generalization of IDQL and the only novelty is the quantile network, which provides some convenience for hyperparameter searching over the quantile value. Some statements need to be further justified.

### Strengths
The writing is clear and the method is described well.

The experiments on bandit and D4RL are thorough, demonstrating the difference of the proposed methods over the previous ones.

The performance of the proposed algorithms beats previous SOTA results, but mostly by small margins.

### Weaknesses
One of my major concerns is as follows. One main advantage of the proposed method is that it can extrapolate high-value samples outside the training distributions based on the reward function’s trend. However, why is this valid for offline RL settings? The values of out-of-distribution samples are usually penalized as the pessimism of value estimation in order to achieve conservative and best performant policies in online evaluation. Please justify why simple extrapolation based on the trends of reward function is valid. One can easily construct a counterexample to make qGPD totally failed in the bandit example, by setting a first increasing then suddenly decreasing reward structure, e.g., by letting the purple regions in Fig. 3 (c)(f) to have very low reward values.

Another problem bothers me is the performance improvement over IDQL. From what I understand, the qGDP only improves over IDQL by predicting over more quantiles, so why the performance of qGDP can be better than IDQL if the quantiles considered for two methods are the same, or is the improvement just caused by qGDP searches over a larger space of quantiles or with a smaller grid size? If the improvement mainly comes from this, I cannot be convinced that qGDP is a very novel method.

Some minor suggestions:

Please illustrate more clearly about the output structure of the quantile network and the choice of N.

Please indicate what is the hyperparameter (quantile or guidance) in the caption of Fig. 2 
, also provide ground truth distributions in Fig. 2.


### Questions
In section 4, what does the equation $V_\eta^i(s)i=1^N$ mean? I don’t get this one.

In Eq. (11), why is the quantile loss different from Eq. (8)?

In Sec. 6.4, why is qGDP faster than DQL? Please provide more explanations.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes to train a diffusion policy from offline data conditional on the output of a pretrained quantile network. This allows actions to be naturally biased to be higher quality without the need to take gradients through a Q-network at test-time. The resulting approach is validated on the D4RL benchmark, with comparable performance with the prior SOTA.

### Strengths
- The problem setting is well-motivated and a natural extension of prior work.
- The paper enables a classifier-free method to increase the quality of actions sampled at test-time. This significantly improves inference time over the baseline.
- Clear presentation of the algorithm and informative toy experiments.

### Weaknesses
 - **(Unclear empirical benefit)** Whilst the paper shows a strong improvement on speed, the empirical benefit of the approach is unclear, as there is only a slight gain over the baseline DQL. This is compounded by the fact that the main empirical evaluation in Section 6.1 maximizes over an extremely large 70 different hyperparameter configurations, which is extremely unrealistic for offline reinforcement learning. Coupled with the sweep in Figure 4, the main empirical evaluation is likely maximizing over statistical noise. The results over a smaller hyperparameter space in Section 6.3 do not show a clear improvement.
- **(Quantitative metric of success in toy experiments)** Whilst the authors helpfully compare the effect of different guidance and sampling schemes on their toy dataset in Figure 2-3, it is unclear what the optimal or desired behavior is. It would be helpful to include some indication of what the optimal behavior should be and some kind of metric to assess this (e.g. conforming to some desired distribution).
- **(Incomplete speed discussion)** Whilst Table 4 shows an improvement over DQL, it would be also valuable to compare runtime to related approaches, IDQL and SfBC. Furthermore, details are missing on which environment exactly is being timed in the table.

Minor:
- Figure 1 is presented without context, which is confusing for the readers. The authors should include the purpose of these datasets in the description.
- Axis labels and text in Figure 2,3,4 are very small and hard to read.
- Overall summary totals in Tables 1, 2, 3 should also have standard deviation. Given the mild improvement over the baseline, it would also be valuable to perform RLiable [1] analysis to assess the statistical significance of the method.

### Questions
I would greatly appreciate responses and rebuttals to the concerns raised in the weaknesses section.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good
