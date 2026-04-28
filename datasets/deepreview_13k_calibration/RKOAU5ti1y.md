# A Distributional Approach to Uncertainty-Aware Preference Alignment Using Offline Demonstrations

- Decision: Accept
- Avg Score: 7.00
- Scores: 8, 8, 6, 6

## Abstract
Designing reward functions in Reinforcement Learning (RL) often demands significant task-specific expertise. Offline preference-based Reinforcement Learning (PbRL) provides an effective alternative to address the complexity of reward design by learning policies from offline datasets that contain human preferences between trajectory pairs. Existing offline PbRL studies typically model a reward function by maximizing its likelihood of generating the observed human preferences. However, due to the varying number of samples within the limited dataset, less frequently compared trajectories exhibit greater uncertainty, which potentially leads to unrelible behaviors during reward and policy updates. To solve this issue, in this work, we introduce Uncertainty-Aware PbRL (UA-PbRL) to learn a distributional reward model and a risk-sensitive policy from an offline preference dataset. Our approach employs a Maximum A Posteriori (MAP) objective to update trajectory rewards and incorporates an informative prior to account for the uncertainties. Building upon this reward update, we propose a generative reward model to capture the reward distribution, utilizing the offline distributional Bellman operator and the Conditional Value-at-Risk (CVaR) metric to train a risk-sensitive policy. Experimental results demonstrate that UA-PbRL effectively identifies and avoids states with high uncertainty, facilitating risk-averse behaviors across various tasks, including robot control and language model alignment.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper proposes an uncertainty-aware version of the preference-based RL (PbRL) framework for offline settings. The method first fits a distributional model of human rewards using offline preference data using a MAP estimate with a learned beta prior. This model is then used with an offline distributional policy learning objective, enabling risk-averse optimization with CVaR. Didactic results are presented in a gridworld, as well as evaluation on control tasks (maze and swimmer), and in an LLM RLHF setting, showing an improved ability to safely adhere to human preferences.

### Strengths
- Better algorithms for risk-averse optimization of human preference models is an important and timely problem for creating safe and aligned AI agents
- Approach shows good performance across diverse settings, including in an LLM setting, where widely-adopted RLHF methods could benefit from methods to avoid catastrophic outcomes (see, e.g., Gemini safety training issues with racial bias)
- Didactic gridworld visualizations are helpful
- Algorithm is theoretically justified (see questions for a few points to clarify)

### Weaknesses
 - All human preference data was synthetically generated
- A few points of confusion (see questions below)

- What is dist() in Eq. (9)?
- Could the authors briefly discuss the advantages of the iterative approach for the MAP estimate in Eq. (8) / Theorem 4.1 over using a single step learned model?
- Similarly, what are the advantages of separately fitting the prior (Sec. 4.2) and then doing a MAP estimate (Sec. 4.3)? Is this performing a form of type II MLE? And could this be converted to a single step approach?
- Line 222: "we enforce the geometric mean strength to be one"; how is this enforced? Is this part of the prior in Eqs. (2) and (3), or a constraint?

Minor formatting:
- Line 277: "In specific" $\Rightarrow$ "To be specific"
- Line 245: Use ``...'' for quotes instead of '...'

### Questions
- What is dist() in Eq. (9)?
- Could the authors briefly discuss the advantages of the iterative approach for the MAP estimate in Eq. (8) / Theorem 4.1 over using a single step learned model?
- Similarly, what are the advantages of separately fitting the prior (Sec. 4.2) and then doing a MAP estimate (Sec. 4.3)? Is this performing a form of type II MLE? And could this be converted to a single step approach?
- Line 222: "we enforce the geometric mean strength to be one"; how is this enforced? Is this part of the prior in Eqs. (2) and (3), or a constraint?

Minor formatting:
- Line 277: "In specific" $\Rightarrow$ "To be specific"
- Line 245: Use ``...'' for quotes instead of '...'

### Soundness
4

### Presentation
3

### Contribution
4

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper introduces Uncertainty-Aware Preference-Based Reinforcement Learning (UA-PbRL), an uncertainty-aware preference alignment approach for PbRL. Unlike traditional PbRL approaches that are often risk-neutral, UA-PbRL leverages a distributional reward model and a risk-sensitive policy to better capture uncertainties inherent in human preferences. Key components include a Maximum A Posteriori (MAP) objective for reward updates using an informative Beta prior and a Conditional Value-at-Risk (CVaR) metric to develop a risk-averse policy. The method is evaluated across various domains, such as robot control, pointmaze, and language model alignment tasks, demonstrating its ability to handle uncertain scenarios effectively.

### Strengths
- The use of a distributional approach and risk-sensitive metrics provides a robust framework for handling uncertainty in human preference data.
- The empirical results demonstrate that UA-PbRL outperforms baseline methods in both mean and worst-case performance, validating its efficacy in high-risk scenarios.
- The empirical results across multiple domains (robot navigation, LLM alignment) highlights its adaptability for wide adoption.
- The code is provided for reproducibility.

### Weaknesses
 - Although the method is evaluated across various domains, the evaluation on stochastic D4RL [1], which is an important benchmark for risk-averse offline RL (used in both O-RAAC and CODAC), is missing.
- Lack of discussing recent online PbRL methods [2, 3, 4, 5].
- The LLM experiments lack proper baseline. If the authors want to show the effectiveness of UA-PbRL in the LLM setting, they should compare it with the state-of-the-art methods in the LLM setting, such as [6].
- The choice of baselines could be further discussed, especially regarding differences in reward model architectures. If Transformer-based models are not used consistently, this may influence performance comparisons.

### Questions
Besides the weaknesses above, further question is as follows:

- Whether the baselines use Transformer-based reward models? If not, I think the comparison is not fair. At least, the authors should compare with Preference Transformer to ignore the architecture difference.
- Since UA-PbRL’s policy optimization is risk-averse, how does this impact its overall performance, particularly in tasks where risk-neutral policies might perform better in terms of mean rewards?
- How does UA-PbRL perform when the human preference data is noisy or inconsistent?

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
3

### Summary
The paper introduces Uncertainty-Aware Preference-based Reinforcement Learning (UA-PbRL), a framework for learning policies from offline human preference data while accounting for uncertainties in trajectory comparisons. 
UA-PbRL proposes to first train an informative prior, followed by distributional reward model with a Maximum A Posteriori (MAP) objective to improve reward estimation and policy updates in the presence of uncertain samples. 
By employing the Conditional Value-at-Risk (CVaR) metric, UA-PbRL facilitates risk-sensitive policy learning, demonstrating enhanced risk-averse behaviors across tasks like robot control and language model alignment.

### Strengths
1. The motivation for the need to learn a distributional reward function through offline preference data is well understood.
2. The methodology for learning the distributional reward function is theoretically well-grounded and novel.
3. The effectiveness of the UA-PbRL framework is demonstrated through experiments across various domains (from simple gridworld to LLM alignment).

### Weaknesses
 1. Notation issues
* In Equation 9, an explanation of the distance metric is omitted, and additional question about the distance metric is detailed in Q4.
* In line 318, isn't Zπ a random variable? This seems to be expressed as an expectation. 
2. Experiment on LLM alignment
* In the LLM alignment experiment, the main focus have to be results about red teaming experiment (i.e., how uncertain inputs are handled). However, there is a lack of comparative analysis on risk-averse behaivor of LLMs given harmful prompts that were not seen during the reward model training process.  
* It would be helpful to provide information on how much the rate of evasive responses increases compared to the baseline (currently, only an example for one sample is provided in Appendix D.3). 
3. Analysis on the various preference labelling setup.
* Over entire experiments, expected likelihood of a risky trajectory outranking a risk-averse one is set to be 0.6. 
* At least in the gridworld experiment, I want to see how the results change with preference labelling setup other than p(τ2 >τ1 )=0.6. 
* Specifically, it would be useful to analyze whether the uncertainty-aware reward function still estimates high variance for τ2  even when the preference for τ2  increases to around 0.7 or 0.8. 

### Questions
1. Can you provide additional explanation for Equation 2 (derivation of the prior of the reward function)? I have difficulty understanding the transition from the first term to the second term and from the third term to the fourth term (Does d indicate a derivative?). 

2. Rather than training neural network for informative beta prior, isn’t it possible to simply define parameters of Beta distribution using the statistics in the data (i.e., the number of times a specific trajectory wins over another trajectory / loses within the offline preference data)?  Of course, if you aimed to obtain the distribution of ϕ(τ) for any arbitrary trajectory, then this approach might be necessary, but aren’t you using offline trajectories D to train the reward model? 

3. Regarding the proof of Theorem 4.1, Is there a guarantee that the p.d.f of the posterior distribution of r(τ) is concave? If not, how can Equation 22 ensure a “global” maximum?

4. r^K in the equation 9, which is a point estimate of the posterior distribution, seems to serve as a target value for the distributional reward model. But I wonder how does it provide sufficient learning signal for the distributional reward model to output correct \sigma, as the r^K does not contain any information about the variance of the posterior distribution.

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
3

### Summary
This paper introduces UA-PbRL, which employs a distributional reward model to capture uncertainty in offline PbRL settings. This distributional model is then leveraged to train a risk-sensitive policy. The paper presents a MAP objective for reward learning, incorporating Beta priors to account for uncertainty, which is learned via variational inference. Additionally, it utilizes a distributional Bellman operator and the CVaR metric for policy optimization. Empirical evaluations across various tasks demonstrate the effectiveness of UA-PbRL compared to other PbRL baselines.

### Strengths
The paper is well-organized and addresses a significant problem in PbRL. The proposed method is evaluated across a variety of tasks, demonstrating its effectiveness.

### Weaknesses
The paper is well-organized and addresses a significant problem in PbRL. The proposed method is evaluated across a variety of tasks, demonstrating its effectiveness.

Please see Questions.

1. In line 71, preference assignment -> preference alignment.

2. Clarification on Problem Setting and Example: Is the uncertainty mainly due to too few comparisons rather than imbalance in the dataset? This remains unclear to me. Could you provide further clarification?

3. In the motivation example for the imbalanced preference dataset, what do you mean by "outlier trajectories"? Based on Assumption 3.1, all $N_1+N_2$ trajectories should have an equal probability of being selected to form a pair. The authors state that "a specific trajectory such as $\tau_2^\prime$ and other outlier trajectories are less likely to be selected during sampling from the dataset." Could you clarify why this is the case?

4. The derivation of Equation 2, particularly the first step, is unclear to me. Since this is a crucial part of the approach, please provide more detail in the main text and the appendix if necessary.

5. In Section 4.2, please clarify what is meant by "positive" and "negative" human feedback.

6. It seems that the authors aim to learn a data-driven prior distribution of $\phi$ using a variational distribution, with the marginal distribution of $\phi$ defined by $\alpha_0, \beta_0$. Do varying choices of $\alpha_0$ and $\beta_0$ significantly impact prior learning and subsequent reward and policy learning?

7. Is variational inference computationally expensive, and does it risk converging to a local optimum?

8. The authors refer to two prior works on PbRL that especially focus on confidence and uncertainty [1,2], which could serve as reasonable baselines. Why were these approaches not included for comparison?

9. The uncertainty of preference alignment in LLMs may have different motivations compared to control tasks. A brief discussion on this distinction in the introduction or experiment section would be beneficial.

10. The paper lacks an evaluation on offline dataset collected from real human feedback.

### Questions
1. In line 71, preference assignment -> preference alignment.

2. Clarification on Problem Setting and Example: Is the uncertainty mainly due to too few comparisons rather than imbalance in the dataset? This remains unclear to me. Could you provide further clarification?

3. In the motivation example for the imbalanced preference dataset, what do you mean by "outlier trajectories"? Based on Assumption 3.1, all $N_1+N_2$ trajectories should have an equal probability of being selected to form a pair. The authors state that "a specific trajectory such as $\tau_2^\prime$ and other outlier trajectories are less likely to be selected during sampling from the dataset." Could you clarify why this is the case?

4. The derivation of Equation 2, particularly the first step, is unclear to me. Since this is a crucial part of the approach, please provide more detail in the main text and the appendix if necessary.

5. In Section 4.2, please clarify what is meant by "positive" and "negative" human feedback.

6. It seems that the authors aim to learn a data-driven prior distribution of $\phi$ using a variational distribution, with the marginal distribution of $\phi$ defined by $\alpha_0, \beta_0$. Do varying choices of $\alpha_0$ and $\beta_0$ significantly impact prior learning and subsequent reward and policy learning?

7. Is variational inference computationally expensive, and does it risk converging to a local optimum?

8. The authors refer to two prior works on PbRL that especially focus on confidence and uncertainty [1,2], which could serve as reasonable baselines. Why were these approaches not included for comparison?

9. The uncertainty of preference alignment in LLMs may have different motivations compared to control tasks. A brief discussion on this distinction in the introduction or experiment section would be beneficial.

10. The paper lacks an evaluation on offline dataset collected from real human feedback.


[1] Wanqi Xue, Bo An, Shuicheng Yan, and Zhongwen Xu. Reinforcement learning from diverse human preferences. arXiv preprint arXiv:2301.11774, 2023.

[2] Jie Cheng, Gang Xiong, Xingyuan Dai, Qinghai Miao, Yisheng Lv, and Fei-YueWang. Rime: Robust preference-based reinforcement learning with noisy preferences. arXiv preprint arXiv:2402.17257, 2024.

### Soundness
2

### Presentation
3

### Contribution
3
