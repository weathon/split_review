# Behavioral Entropy-Guided Dataset Generation for Offline Reinforcement Learning

- Decision: Accept
- Scores: 6, 6, 6, 6

## Abstract
Entropy-based objectives are widely used to perform state space exploration in reinforcement learning (RL) and dataset generation for offline RL. Behavioral entropy (BE), a rigorous generalization of classical entropies that incorporates cognitive and perceptual biases of agents, was recently proposed for discrete settings and shown to be a promising metric for robotic exploration problems. In this work, we propose using BE as a principled exploration objective for systematically generating datasets that provide diverse state space coverage in complex, continuous, potentially high-dimensional domains. To achieve this, we extend the notion of BE to continuous settings, derive tractable $k$-nearest neighbor estimators, provide theoretical guarantees for these estimators, and develop practical reward functions that can be used with standard RL methods to learn BE-maximizing policies. Using standard MuJoCo environments, we experimentally compare the performance of offline RL algorithms for a variety of downstream tasks on datasets generated using BE, R\'{e}nyi, and Shannon entropy-maximizing policies, as well as the SMM and RND algorithms. We find that offline RL algorithms trained on datasets collected using BE outperform those trained on datasets collected using Shannon entropy, SMM, and RND on all tasks considered, and on 80\% of the tasks compared to datasets collected using Renyi entropy.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper studies dataset generation for offline RL. More specifically, this paper extends recently proposed behavioral entropy (BE) for discrete settings to continuous tasks, and designs estimator and RL algorithms for exploration and data generation. The paper compares offline RL performance on BE-generated data with other entropy-based data generation and shows that the proposed method outperforms other baselines in the Walker and Quadruped environments.

### Strengths
1. The proposed method is well-motivated and theoretically grounded.
2. The writing is clear and easy to follow.

### Weaknesses
While well-motivated, I have some questions about this work:

1. The authors propose a KNN-based estimator with convergence guarantee. I wonder in practice how $k$ is chosen and if KNN introduces huge computation overhead compared to other baselines. For instance, if SE and RE have the same computation budget as BE, will they collect more data and hence perform better?
2. The experiments only generate 500K elements for each task, which might be not enough for the offline RL to learn a good policy. Can we test if the performance of BE, SE, and RE will scale with more data?

Minor:

1. While this paper focuses on the offline RL setting, I am curious about whether this entropy-based exploration can be applied in the online RL setting and how it performs compared with other online exploration methods.

Overall, while this paper presents some interesting ideas, I am unable to recommend acceptance at this stage given the questions mentioned above. However, I would consider raising my score if the authors could address my concerns.

### Questions
There are some questions and concerns, which I have outlined in the previous section.

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
This paper explores how to extend Behavior Entropy to high-dimensional continuous settings and leverages this as a metric for exploration to elicit high state space coverage. This exploration objective can be systematically applied to dataset generation for offline RL algorithms. The authors additionally derive tractable KNN estimators and practical reward functions that can be used in tandem with RL to learn an effective policy. They empirically show that generated datasets with Behavior Entropy outperform datasets generated using Shannon entropy and Rényi entropy with offline RL algorithms such as CQL on Mujoco tasks.

### Strengths
The authors have a novel contribution with the extension of Behavior Entropy to continuous domains as well as a tractable formulation using KNNs (with convergence guarantees) to define an reward function for RL. They show initial empirical validation on a subset of the Mujoco domains in the Walker and Quadraped tasks with three offline RL algorithms: CRR, CQL and TD3. Additionally, the visualizations of the dataset generation provide insights into what differentiates the different exploration approaches.

### Weaknesses
Some of the empirical results aren’t compelling such as the $\alpha$/$q$ sweep done in Figure 4, where the gap from BE and Shannon/Renyi Entropy is minimal or within the margin of error for domains, which questions the advantages of the dataset generated. Specifically, the performance differences across various $\alpha$ and $q$ values are not substantial enough to clearly demonstrate the superiority of Behavior Entropy (BE) over Shannon Entropy (SE) or Rényi Entropy (RE). The lack of a clear trend or significant performance boost in these sweeps raises concerns about the practical benefits of using BE for dataset generation. Additionally, it would be good to check the consistency of the dataset generation, where the dataset generation process is repeated for each $\alpha$ or $q$, $N$ times and performance is aggregated across these generation attempts. This is crucial to ensure that the observed results are not due to random variations in the dataset generation process. Without this analysis, it's difficult to determine if the reported performance is consistent or if it's highly dependent on the specific dataset generated. Additionally, the domains evaluated are state based and a limited subset of the Mujoco benchmark. It would be good to see the clear benefits of BE-generated datasets across multiple tasks and algorithms. The current evaluation is limited to a small set of MuJoCo tasks, which may not be representative of more complex or diverse environments. The lack of evaluation on a wider range of tasks and algorithms makes it difficult to generalize the findings and assess the robustness of the proposed approach. Additionally, there are a myriad of other exploration objectives people consider such as RND, Count Based Exploration, etc. It would be good to empirically compare against these approaches for the synthetic dataset generation. The absence of a comparison with other well-established exploration methods makes it difficult to contextualize the performance of BE and understand its relative strengths and weaknesses.

### Questions
- For BE, is there a clear selection procedure for $q$ empirically that would transfer across algorithms/tasks?
- Currently, the approach relies on a k-NN estimator, which has limitations as the state dimensionality increases or the size of the dataset is large. As offline RL scales to be used with more realistic domains, these concerns will be more common place. Are there tradeoffs with using this as an estimator?
- Along with the qualitative visualizations you have provided (e.g PHATE/tsne), could a quantitative analysis of the dataset state/action coverage be done to compare the different dataset generation approaches?

### Soundness
3

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
4

### Summary
Entropy-based objectives are widely used to perform state space exploration in reinforcement learning (RL) and dataset generation for offline RL. In this paper, the authors borrow the idea of behavioral entropy (BE) from a prior robotics exploration paper and extend it to continuous space. This paper argues that, compared to prior entropy metrics, using BE as the RL objective enables more complete state coverage.

### Strengths
State coverage is an important direction of unsupervised RL, which could benefit downstream task solving by learning useful skills, or, as in this paper, by generating a dataset for offline RL.

Regarding originality, even though the idea of applying BE to exploration originates from a cited prior work, to the best of my knowledge, the idea of applying it to state coverage is novel. Further, the authors extend BE from discrete to continuous space and propose a knn-based measurement.

Regarding clarity, the figures in the paper are well designed: Fig 2 clearly illustrates the property of BE under different values of $\alpha$ (one of its parameter) and the differences between BE and prior entropy metrics. Meanwhile, the paper uses the same color for each entropy metric across the paper, which further eases the reading.

### Weaknesses
My main questions are about the evalution on state coverage and offline RL performance. Specifically:
1. Could authors explain, in Fig3, why visualizing each experiment using separate plots is a valid metric of state coverage? IIUC, PHATE, t-SNE, and methods does some non-linear projection to project data to 2D, and this brings two problems when comparing these figures:
* As state trajectories go through non-linear projection, the distance between points more reflect their similarity rather their true distance, thus making it hard to say more spanned points covers large state space (I may be wrong on this). Regarding this, one way may be to visualize trajectories of some points and see if they are indeed very distinct states. Another way I would like to see is to run experiments on some 2d domains so we can visualize without PHATE.
* As each experiment is visualized separately, the PHATE may use different projections in different subfigures, making it hard to say points indeed spread out or the projection makes them look spread out. Regarding this, one more fair way is to draw PHATE plots on trajectories across all experiments to ensure they share the same projection.
2. If we assume PHATE plot is a valid, I still have some questions:
* I do not see singnificant difference between SE and BE for Quadruped coverage, is there any? If not, why that's the case?
* In offline RL experiments, do you train each method until it converges? Authors mentions "we performed just 100K offline training steps", but I thought it's more fair to compare performance under convergence.
* The authors motivates in the intro that better state coverage should lead to better offline RL performance, but in Fig 6, the $\alpha$ leading to best coverage ($\alpha$=5) typically has the worst performance across all alpha, why that's the case? Is the state coverage metric wrong or the assumption of better state coverage leading to better performance wrong or becase of other reasons?

Minor suggestions on writing:
1. In intro, authors motivates the usage of BE by only saying "it's widely used in behavioral economics to model human probability perception" and the results from Suresh et al. (2024). This feels void and doesn't explain why it could helps. There is no explanation why reweighting the entropy (making it more uniform or sharper) could lead to better coverage.
2. L100, "We derive practical RL methods", it's more of a different reward/objective, as you still use an existing RL algorithm.

### Questions
What is admissible generalized entropies and why "admissible"  and "generalized" are important?

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
4

### Summary
The paper proposes to use behavioral entropy (BE), a generalized version of Shannon's entropy using a reweighting function, as reward to generate datasets and tests whether these datasets would be better suited for offline RL. 
The behavioral entropy allows reweighting low-probable events and high-probable events, and it was used in Economics to explain human behavior. 
The paper shows that data generated with maximizing BE can lead to higher downstream task performance in offline RL.

### Strengths
- analysis of behavior entropy on exploration
- nice visualizations
- continuous space estimators for BE

### Weaknesses
 - another hyperparemeter introduced, not unsurprising that better performance can be achieved by tuning this parameter per environment
- computationally heavy (because of k-NN that needs to be rebuild every time) and no mentioning of that
- no comparison to simple baselines like RND
- no improvements for strong offline methods

### Questions
- The intuition behind BE did not came across well. Also, why would one want a different weighting of high and low-prob. values?
- The graphics look nice, but in the context of beh. generation and exploration, there is no parametric underlying distribution (like Bernoulli) but essentially, one is trying to achieve uniform distribution over the state-space. An illustration on how this exploration strategy really performs differently and how would be interesting.

- how often does the $k$-NN tree for fast retrieval be rebuild? After every episode? 
- Since alpha<1 and q<1 work best, one could say that seldomly visited states (low probability) should give a higher weighting in the reward / entropy
- How was alpha / q selected? 
- How does the method scale to high-dimensional input?

## Post rebuttal update
the authors have improved the paper significantly and addressed most of my concerns. I am increasing my score to 6.

### Soundness
3

### Presentation
3

### Contribution
2
