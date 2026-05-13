# The Generalization Gap in Offline Reinforcement Learning

- Decision: Accept
- Scores: 8, 6, 6, 6

## Abstract


## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces a benchmark for evaluating generalization in offline learning. Based on the benchmark, state-of-the-art offline policy learning algorithms, including BC, sequence modeling approaches, and offline RL algorithms, are tested. The results show that all the offline learning methods perform worse than online RL in both train and test environments. The results also reveal that BC is stronger to generalize to new environments than other offline learning methods.

### Strengths
1. This paper presents new results on the generalization of offline learning. As we know, it is important to understand the generalization ability of offline learning methods in order to apply offline methods to real-world problems. Although not very surprising, this paper first confirms that offline RL and sequence modeling approaches can be struggling to generalize to new environments.
2. The results may have a broad impact on the community. Indeed, we can no longer ignore the generalization problem of existing offline learning methods. So, more investigation is needed. The results may also have an impact on our choice of offline learning methods in application scenarios.
3. The experimental results are sufficient and convincing. In the experiments, multiple sequence modeling methods and multiple offline RL algorithms are included, two kinds of games are tested, and multiple settings are tested. 
4. The new benchmark is new and an important contribution.

### Weaknesses
1. The paper does not discuss in depth the root causes of the generalization problem. I think it would be a great credit to the paper if the authors could share some thoughts on why.
2. There are minor problems:
- The color of the lines in Figure 2(a) is wrong.
- The results on Leaper are missing in Figure 11 and Figure 12.

### Questions
Can the authors share some thoughts on why offline RL does not generalize well?

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
This paper studies the generalization abilities of offline RL algorithms across different environments. In particular, it introduced a collection of offline RL datasets of different sizes and skill-levels from the Procgen and WebShop environments. Experiments show that existing offline RL methods perform significantly worse than online RL on both train and test environments. Additional experiments show that an increase in data diversity improves generalization while an increase of the size of training data does not.

### Strengths
- This paper investigates an important problem in offline RL.

- It introduced a collection of offline RL datasets of different sizes and skill-levels from the Procgen and WebShop environments.

- The experiments are thorough.

- The writing is clear and easy to follow.

### Weaknesses
 - The novelty of the study is somewhat restricted. Given that many existing offline RL algorithms do not inherently prioritize generalization ability in their design, so the current experimental results are mostly within expected outcomes.

- There are many duplicate references: "Leveraging procedural generation to benchmark reinforcement learning", "Offline q- learning on diverse multi-task data both scales and generalizes", "Deep residual learning for image recognition.", "The nethack learning environment."

- This paper primarily serves as a summary of empirical observations, and no specific solutions are proposed to address the generalization issue. IMHO, there is a lack of deeper understanding of the generalization issue of offline RL agents and the take aways for readers from this work is limited.

### Questions
I appreciate the authors' efforts to investigate an important question in offline RL. However, upon reviewing the current draft, I find the perspective presented to be somewhat one-sided. It is essential to acknowledge that the overall conclusions drawn in the paper might be confined to the specific benchmark dataset being utilized. There have been notable instances demonstrating the impressive generalization capabilities of offline RL agents [1] [2]. Consequently, it would be prudent to avoid overly definitive statements in this paper, given these successful examples.

Moreover, I would like to highlight a gap in the current work—there is a lack of more in-depth analysis to elucidate the key question: "why certain offline RL agents [1][2] exhibit superior generalization skills while others do not?"

A more profound theoretical analysis might be instrumental in explaining these discrepancies.

[1] (Agarwal et al., 2020) An Optimistic Perspective on Offline Reinforcement Learning

[2] (Kumar et al., 2023) Offline Q-Learning on Diverse Multi-task Data Both Scales and Generalizes

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper study and benchmark the generalization abilities of existing offline RL algorithms, revealing several interesting and helpful conclusions regarding to current offline RL learning researches.

### Strengths
1. The problem studied in this paper is important and interesting. Existing offline RL benchmarks indeed require more practical metrics for evaluation.
2. The experiments conducted in this paper seem solid and abundant. The conclusions made sound convincing.
3. Hyperparameters are provided and the results seem reproducible.

### Weaknesses
1. The algorithms included are a bit limited. Methods like model-based learning [1-2], curriculum imitation [3], and other methods are not involved. More useful conclusions can be made when the benchmarking algorithms are expanded.

2. Benchmark included is a bit limited. Most of the results are concluded from a simulated benchmark ProcGen, only a small part of experiments are conducted on the real-world dataset "WebShop". The author may consider expanding their tested benchmark to more real-world problems as introduced in [4].

### Questions
1. Will the author open-source their benchmark and evaluation codes?
2. Can the author explain more about the setup of Webshop? What is the state/action/reward/objective/transition of this problem? An example would be better (can lie in the appendix).
3. Can you explain how you fine-tune these algorithms and how the results are selected? It is thorny and important to select the best model in practice.

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
This paper studies the problem of generalization for popular offline RL algorithms. By carrying out extensive experiments of state-of-the-art offline RL algorithms (IQL, CQL, DT, etc) on procgen and webshop environments, this paper presents the findings that although offline RL methods outperform BC in training environments with suboptimal data, they fail to generalize as well to testing environments similar to training environments.

### Strengths
This paper carries out extensive experiments on procgen and another more realistic environment webshop, covering most state-of-the-art offline rl methods such as CQL, IQL and BCQ. 

The problem of generalization of offline reinforcement learning is important yet relatively scarcely touched.

The paper is well-written and easy-to-follow. The format of using red text boxes makes it easy to capture important takeaways.

### Weaknesses
I have concerns that some of the offline RL baselines might not be tuned appropriately. For example, in the procgen environments, there seems to be a large gap between BC and CQL both in the train and test environment. However, CQL contains a weighted combination of TD-learning loss and behavior cloning loss so a proper tuning of the weights should make CQL at least comparable to BC.

Although procgen is a relatively popular benchmark, it is not the primary benchmark for those offline RL methods. They are most extensively tested on continuous control tasks such as D4RL (https://arxiv.org/abs/2004.07219), so authors should explain why they did not conduct experiments in the setting of continuous control. For example, the different test environments can be attained by modifying the environment parameters such as gravity.

The conclusion of the paper is derived mostly through empirical observations. It would be important to also have theoretical understandings of why offline RL does not work as well as BC in terms of generalization, similar to the analysis done in https://arxiv.org/pdf/2204.05618.pdf.

### Questions
Why IQL cannot be used in the setting of webshop? The expectile regression part should not depend on the number of actions for each state and as long as the expectile regression can be implemented it should be fine?

In section 4.5, is it possible to extend the plot a bit to show around how much data the learning curve stops to grow? It seems that we also need more than 3 data points to draw a valid conclusion regards to the trend.

In Figure 3, why is the blue line sometimes higher than the red line? Isn't the data collected by expert PPO?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
