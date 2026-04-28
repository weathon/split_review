# ContraDiff: Planning Towards High Return States via Contrastive Learning

- Decision: Accept
- Avg Score: 5.67
- Scores: 5, 6, 6

## Abstract
The performance of offline reinforcement learning (RL) is sensitive to the proportion of high-return trajectories in the offline dataset. However, in many simulation environments and real-world scenarios, there are large ratios of low-return trajectories rather than high-return trajectories, which makes learning an efficient policy challenging. In this paper, we propose a method called Contrastive Diffuser (CDiffuser) to make full use of low-return trajectories and improve the performance of offline RL algorithms. Specifically, CDiffuser groups the states of trajectories in the offline dataset into high-return states and low-return states and treats them as positive and negative samples correspondingly. Then, it designs a contrastive mechanism to pull the trajectory of an agent toward high-return states and push them away from low-return states. Through the contrast mechanism, trajectories with low returns can serve as negative examples for policy learning, guiding the agent to avoid areas associated with low returns and achieve better performance. Experiments on 14 commonly used D4RL benchmarks demonstrate the effectiveness of our proposed method. Our code is publicly available at \url{https://anonymous.4open.science/r/CDiffuser}.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces ContraDiff, a novel offline reinforcement learning method that leverages contrastive learning to make better use of low-return trajectories by pulling states towards high-return regions and pushing them away from low-return areas. While the approach shows promising results across various environments and demonstrates advantages in handling sub-optimal datasets, several limitations remain, including unclear theoretical justification for the relationship between contrastive and RL losses, heavy reliance on hyperparameters for positive/negative sample selection, and lack of trajectory-level temporal information in the contrastive learning design. Despite these limitations, the paper presents a well-structured contribution with comprehensive experiments, providing a new perspective on utilizing sub-optimal data in offline RL.

### Strengths
1. The paper is well-structured and easy to follow, with clear motivation and comprehensive explanations of each component in the proposed method.

2. The empirical evaluation is thorough, covering 27 sub-optimal datasets and including extensive ablation studies, hyper-parameter analysis, and visualizations that help understand the method's behavior.

3. The proposed method provides a novel perspective on utilizing low-return trajectories in offline RL, and the implementation is relatively simple with only a few additional hyperparameters compared to the base diffusion model.

### Weaknesses
1. The relationship between contrastive loss and RL loss needs further detailed justification. Intuitively, these two losses appear highly correlated, especially when considering low-return trajectories as negative samples. The paper claims the RL loss in diffusion-based methods simply fits the trajectory distribution, but this ignores the value-guided sampling inherent in these methods, which already biases towards high-return trajectories. This raises concerns that the contrastive loss might merely serve as a redundant enhancement to the RL loss rather than a meaningful regularization term that needs to be balanced against the primary objective. A numerical analysis comparing these losses across trajectories with different returns would be valuable to verify if they indeed show similar trends, and to quantify the degree of redundancy.
2. The methodological differences illustrated in Figure 1(d)(e)(f) lack sufficient justification. This figure fails to demonstrate why pushing away from low-return states is fundamentally superior to upweighting high-return trajectories, or why return-based contrastive learning outperforms traditional trajectory-based approaches. The comparison should explicitly address how the proposed method handles situations where the agent is trapped in low-return states and whether the contrastive mechanism offers a unique advantage over methods that only upweight high-return trajectories.
3. The paper's method of determining positive and negative samples relies heavily on hyperparameters (ξ, ζ, σ) without theoretical justification for their value ranges. The paper lacks a principled approach to determine these thresholds across different environments. A more systematic study on how different return thresholds affect the distribution of positive/negative samples and their impact on learning dynamics would strengthen the method's foundation. The current approach seems ad-hoc and lacks a clear rationale for how these thresholds should be set for different datasets.
4. The current state-level contrastive learning approach breaks the temporal correlation between states within trajectories, as it samples positive and negative states purely based on return values (SR) or clustering results (SRD). This design might lose important sequential information that could be better captured through trajectory-level contrastive learning. The paper should explore trajectory-aligned state sampling strategies and conduct comparative experiments between state-level and trajectory-level contrastive learning to provide more solid empirical evidence for the design choices. The current approach risks discarding valuable temporal dependencies within trajectories.
5. The competitive performance of baselines like CDE and HD raises questions about the necessity of the proposed contrastive mechanism, especially considering these methods achieve comparable results without any specific designs for handling low-return trajectories. While ContraDiff shows improvements in certain scenarios, the performance overlap with these simpler methods suggests that the advantages of explicitly handling low-return trajectories might be less significant than claimed. This observation calls for a more thorough analysis of what unique benefits, if any, are brought by the contrastive mechanism for low-return trajectory utilization. The paper needs to demonstrate more clearly that the contrastive mechanism provides a unique advantage beyond what can be achieved by simpler methods.

### Questions
See weakness

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper presents a method called ContraDiff, which leverages contrastive learning to guide an agent towards high-return states and pushing agents away from low-return states. The proposed method builds upon diffusion-based trajectory planning models and aims to solve offline reinforcement learning problems especially when high-return trajectories are limited in the offline dataset. Experiments are conducted on standard D4RL tasks and exhibit better performance as compared to baselines.

### Strengths
The combination of contrastive learning and diffusion-based trajectory planning model is a novel idea, allowing the model to learn from both high- and low-return samples. The main figure is clear and well-organized, making it easy to understand the method. Experiments are extensively conducted across many test environments.

### Weaknesses
1. While the idea of using contrastive learning is well motivated, the section on how "positive" and "negative" examples are identified requires additional explanations. The paper did not specify how the clustering is performed -- if the clustering is to enforce "dynamic consistency", I would assume the information is already available in the offline dataset? For me it is unclear how well the clustering captures reachability or state transitions beyond just grouping next states together. This could be a limitation in environments with complex or non-linear dynamics.
2. The paper lacks discussion on the complexity or runtime implications introduced by k-means clustering, especially for large offline RL datasets.
3. The increases in performance are mostly marginal. For many tasks the increase falls within one standard deviation of the baseline methods.
4. The authors mentioned  "comparing ContraDiff with other regular methods" but didn't include specific indication of where the results are presented. I later found the results in the appendix, but the authors may consider additional illustrations and explanations on the results. Furthermore methods like CQL are only tested on the standard D4RL datasets but not the mixture dataset proposed by the authors. More experiment results would be needed here to better demonstrate model performance.
5. It is unclear how the baseline results were obtained -- whether they came from existing code, were reimplemented by the authors, or taken from other sources.
6. The writing, especially in the experiments section, is not very clear to understand. Some sentences and typos make the paper harder to follow. For example: 
* L290: "...high-return sample sparsity situations"
* L301: "...which are focus on addressing..."
* L364: "...declines with the ratio declines"
* Table3: "Walekr2d"

### Questions
Aside from mentioned in the Weakness section, my questions mostly come from experiments presented by the paper:
1. When comparing Table 3 with Table 1, it seems like introducing the expert trajectory leads to a decrease in performance, unexpectedly. For instance, DT achieves a score of 36.6 at original HalfCheetah-MR dataset but 7.5, 6.7, 6.1 in three conditions where expert data is introduced. I was wondering if the same codebase is used in achieving these results, and if so, could the authors share insights on why DT’s performance drops so drastically with the added expert data?
2. In most tasks ContraDiff-SR outperforms ContraDiff-SRD -- this seems unexpected given the author's intuition mentioned in section 3 that ContraDiff-SR may ignore the transition dynamics in its sampling process?  
3. How would the proposed model perform on sparse-reward tasks like AntMaze? This benchmark is commonly used in offline RL evaluations but results for it are missing here.

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
This paper introduces a novel approach, ContraDiff, designed to enhance offline reinforcement learning (RL) by leveraging low-return trajectories in a contrastive learning framework. Offline RL's performance often depends on the presence of high-return trajectories, which are frequently sparse in datasets. ContraDiff addresses this challenge by classifying trajectories into high- and low-return groups, treating them as positive and negative samples, respectively. The approach applies a contrastive mechanism that pulls the agent's trajectories toward high-return states while pushing them away from low-return ones. This strategy enables low-return trajectories to serve as a guiding force to avoid suboptimal regions, enhancing policy performance.

### Strengths
The paper presents a compelling approach to enhancing offline reinforcement learning (RL) through a novel contrastive framework, which incorporates low-return trajectories in ways that previous approaches overlook. ContraDiff’s use of a contrastive learning framework to distinguish between high- and low-return trajectories is an innovative application of contrastive learning within the offline RL domain. Instead of merely reweighting high-return samples, the method leverages low-return trajectories as guiding forces, creating a “counteracting force” that helps the policy avoid suboptimal states. This approach represents a shift from traditional methods that focus primarily on high-return trajectories, expanding the value of underutilized low-return data.

### Weaknesses
While the paper presents contrastive learning as a means to exploit low-return data, it could better clarify why this mechanism is theoretically optimal for avoiding low-return states compared to other potential approaches, such as weighting adjustments or imitation-based filtering. Specifically, the paper does not sufficiently explain why explicitly pushing away from low-return states is superior to simply prioritizing high-return states, especially given that both aim to achieve the same goal of optimal policy learning. The contrastive loss function, while novel in this context, needs more justification regarding its theoretical underpinnings in comparison to other established methods.

* The authors are not clear enough in describing the use of weighted contrast loss to constrain trajectory generation. The description lacks detail on how the weighting is specifically applied within the contrastive learning framework and how it impacts the learning dynamics. The paper should provide a more precise formulation of the weighted loss and its effect on the generated trajectories, including how the weights are determined and how they influence the model's behavior during training.

### Questions
* In the 3.3 model learning section, I noticed that the optimized trajectory generation by minimizing the Mean Square Error between the ground truth and neat trajectory predicted. Therefore, the diffusion should denoise the data from the noisy data completely. I think it's more expensive to train like this. Can you show some experiments comparing the cost of training?
* ContraDiff planning towards high return states, leading policy improvements. It is very similar to some offline RL methods, such as SAW[1], A2PR[2], LAPO[3]. Can you add some discussion with these methods in the related works or more experiments comparison? 
* Did you experiment with setting different thresholds for what qualifies as “low” or “high” return? If so, how did varying these thresholds impact the learned policy or the model’s ability to generalize to novel tasks?

References：
[1] Lyu, Jiafei, et al. "State advantage weighting for offline RL." arXiv preprint arXiv:2210.04251 (2022).

[2] Liu, Tenglong, et al. "Adaptive Advantage-Guided Policy Regularization for Offline Reinforcement Learning." In International Conference on Machine Learning (ICML). PMLR, 2024.

[3] Chen, Xi, et al. "Latent-variable advantage-weighted policy optimization for offline rl." arXiv preprint arXiv:2203.08949 (2022).

### Soundness
3

### Presentation
3

### Contribution
3
