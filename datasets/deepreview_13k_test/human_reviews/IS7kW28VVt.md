# AlphaQCM: Alpha Discovery with Distributional Reinforcement Learning

- Decision: Reject
- Scores: 3, 5, 3

## Abstract
Finding synergistic formulaic alphas is very important but challenging for researchers and practitioners in finance. In this paper, we reconsider the discovery of formulaic alphas from the viewpoint of sequential decision-making, and conceptualize the entire alpha-mining process as a non-stationary and reward-sparse Markov decision process. To overcome the challenges of non-stationarity and reward-sparsity, we propose the AlphaQCM method, a novel distributional reinforcement learning method designed to search for synergistic formulaic alphas efficiently. The AlphaQCM method first learns the Q function and quantiles via a Q network and a quantile network, respectively. Then, the AlphaQCM method applies the quantiled conditional moment method to learn unbiased variance from the potentially biased quantiles. Guided by the learned Q function and variance, the AlphaQCM method navigates the non-stationarity and reward-sparsity to explore the vast search space of formulaic alphas with high efficacy. Empirical applications to real-world datasets demonstrate that our AlphaQCM method significantly outperforms its competitors, particularly when dealing with large datasets comprising numerous stocks.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces AlphaQCM, a distributional reinforcement learning method designed for the discovery of  the so-called formulaic alphas in financial markets, with a focus on overcoming the challenges of non-stationarity and reward sparsity inherent in alpha-mining. The authors conceptualize alpha discovery as a non-stationary and reward-sparse MDP and employ the quantiled conditional moments (QCM) method to estimate unbiased variances as exploration bonuses. This setup enables efficient exploration of the vast search space in formulaic alpha generation. The paper further demonstrates that AlphaQCM outperforms existing alpha-mining methods, such as AlphaGen and genetic programming, across multiple financial datasets.

### Strengths
The strength of this paper include the development of a new RL-based framework that could potentially address the mentioned financial problem.

### Weaknesses
I believe this paper has several fundamental weaknesses.

First, I find the paper poorly organized and hard to read. This includes several aspects:

1. The authors frequently refer to other sources for definitions of financial terminologies. Given the niche nature of this topic, many researchers are unlikely to be familiar with the setup, and they may not consult external references to understand it fully. As a result, even after multiple readings of Figure 1, I am still unclear on the role of certain tokens.

2. As an expert in theoretical reinforcement learning, I struggled to understand the setup after reading Section 3.2 multiple times. The paper lacks a foundational formulations of the underlying MDP (For example, I didn't see a formal definition of the transition kernel, let alone an explanation of the non-stationarity issue). In my opinion, this significantly affects the paper’s readability and clarity.

Second, I feel that this paper mainly applies off-the-shelf RL algorithms to a specific financial application. Furthermore, it offers very little insight into why RL is particularly beneficial in this setting or how it advances researchers' understanding of the underlying problems. In other words, the paper lacks depth.

Third, the experiments rely solely on data from the Chinese market, which falls outside the traditional scope of empirical studies in finance, financial economics, or asset pricing. While using Chinese financial data is not inherently problematic, including comparisons with well-established financial datasets would aid in communicating the findings, as researchers could more easily relate the results to their existing understanding. Given that many of these datasets are publicly available, this additional comparison would be straightforward to implement.

### Questions
See Weaknesses.

### Soundness
2

### Presentation
1

### Contribution
1

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
The paper proposes a novel approach combining Distributional Reinforcement Learning (DRL) and quantiled conditional moments (QCMs) to derive synergistic formulaic alphas. The alpha-mining problem is important in finance, and the proposed DRL algorithm could be adaptive for non-stationary and reward-sparse environments. Tests on multiple real-world datasets benchmarked against baseline methods highlight the model's improved performance.

### Strengths
The paper is well-organized and generally accessible, with clear explanations of most components used in the proposed methods. Notably, this work is among the first to apply Distributional Reinforcement Learning to the alpha-mining problem. Experimental results demonstrate that the proposed method consistently outperforms all baseline models.

### Weaknesses
1. The primary distinction between this work and AlphaGen lies in the use of a Distributional RL algorithm rather than a Proximal Policy Optimization (PPO) approach. The authors argue that their DRL algorithm outperforms PPO by better handling non-stationary and reward-sparse environments, which they claim accounts for the observed performance improvement over AlphaGen. However, the paper lacks empirical evidence, explanation, or references to substantiate this claim. The improvement could also stem from factors such as network parameter sizes or other intrinsic properties of the alpha-mining environment.

2. Certain parts of the paper lack clarity. For instance, while “Distributional Reinforcement Learning” appears in the title, it is not explicitly referenced in the abstract or introduction; instead, it is only implicitly referenced via terms such as "quantile" and the IQN algorithm, which may lead to confusion.

3. There is also a problem in the design of the algorithm. According to Equation (5), the algorithm aims to encourage exploration by incorporating $h$ as the variance of $Q$. The UCB algorithm, for example, used in Chen et al. (2017) [1], leverages a Q-network ensemble variance to guide exploration, aligning with UCB theory as the ensemble variance correlates with the estimation error of the Q function. In contrast, if I understand correctly, the variance in this work represents the intrinsic variance of the $Z$ function, which may not directly correlate with the Q-estimation error.


[1] Chen, Richard Y., et al. "Ucb exploration via q-ensembles." *arXiv preprint arXiv:1706.01502* (2017).

### Questions
1. Do the authors have evidence or references supporting that the improved performance is due to the DRL algorithm’s superior handling of non-stationary and reward-sparse environments compared to PPO?

2. In the appendix, it is mentioned that hyperparameters were kept consistent with AlphaGen for a fair comparison. However, given that the PPO policy network in AlphaGen is not directly comparable with the Q-network and quantile network in this paper, could the authors clarify the number of networks and parameters used in both their method and the AlphaGen baseline?

3. In Section 3.3.2, only $\hat{h}$ is estimated from the quantile network. Does this mean that the parameters $s$, $k$, and $\zeta$ discussed in Section 3.3.1 are not utilized in the proposed algorithm? If so, would it be possible to reduce Section 3.3.1 to improve conciseness?

4. According to Equation (5), the algorithm aims to encourage exploration by incorporating $h$ as the variance of $Q$. Are there references supporting this approach? As mentioned in the weakness part, the variance in your work represents the intrinsic variance of the $Z$ function, which may not directly correlate with the Q-estimation error. How does adding $h$ enhance exploration in this context?


[1] Chen, Richard Y., et al. "Ucb exploration via q-ensembles." *arXiv preprint arXiv:1706.01502* (2017).

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper presents a new approach to "alpha discovery" in finance using deep reinforcement learning. Alpha discovery is the problem of finding a function that maps stock histories onto predictive signals for future returns. The authors claim that this problem is challenging because the domain is non stationary and reward stationarity. The authors propose a distributional reinforcement learning approach called AlphaQCM. Some theoretical analysis is provided and experiments compare the proposed method with some baselines.

### Strengths
- The writing is generally clear. 
- The problems of nonstationarity and reward sparsity are interesting.

### Weaknesses
The most salient weakness is that the paper appears to be written for a finance audience. Please see questions below.

### Questions
Questions:
- What is a synergistic formulaic alpha?
- What is alpha mining? 
- It is unclear whether the paper aims to contribute to financial modeling or reinforcement learning. 
- Why is the definition of "alpha" in a footnote. For a technical conference, given that this is the goal of the work, I would expect the authors to explain what this is and why it is important first. 
- What does it mean for alpha to be subtle and intricate? 
- Line 035, I don't know that "surpass" conveys the intended meaning here. 
- What is AlphaGen? 
- Neither nonstationarity nor reward sparsity are adequately defined in the introduction. 
- It is not clear why these methods are chosen for comparison. I see that we are supposed to look in an Appendix for the justification, but why wouldn't this be in the main text? 
- Specifically, I would expect to see, for a machine learning audience, a justification for the alternative models in terms of their prior performance in non stationary and/or sparse reward settings. 
- Why are the only datasets financial in nature? There are other examples of non stationary sparse domains. I would expect those to be included, if the goal of the algorithm is to overcome those challenges.

### Soundness
2

### Presentation
2

### Contribution
1
