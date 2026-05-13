# Learning mirror maps in policy mirror descent

- Decision: Accept
- Scores: 6, 6, 8

## Abstract
\looseness = -1
Policy Mirror Descent (PMD) is a popular framework in reinforcement learning, serving as a unifying perspective that encompasses numerous algorithms. These algorithms are derived through the selection of a mirror map and enjoy finite-time convergence guarantees. Despite its popularity, the exploration of PMD's full potential is limited, with the majority of research focusing on a particular mirror map---namely, the negative entropy---which gives rise to the renowned Natural Policy Gradient (NPG) method. It remains uncertain from existing theoretical studies whether the choice of mirror map significantly influences PMD's efficacy. In our work, we conduct empirical investigations to show that the conventional mirror map choice (NPG) often yields less-than-optimal outcomes across several standard benchmark environments. Using evolutionary strategies, we identify more efficient mirror maps that enhance the performance of PMD. We first focus on a tabular environment, i.e.\ Grid-World, where we relate existing theoretical bounds with the performance of PMD for a few standard mirror maps and the learned one. We then show that it is possible to learn a mirror map that outperforms the negative entropy in more complex environments, such as the MinAtar suite. Our results suggest that mirror maps generalize well across various environments, raising questions about how to best match a mirror map to an environment's structure and characteristics.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper studies the impact of different mirror graphs within the Policy Mirror Descent (PMD) framework in reinforcement learning, traditionally dominated by negentropy graphs. Through empirical testing, the authors identify alternative mirror mappings that significantly improve performance and generalization in different environments, challenging the default choice of mirror mappings in PMD.

### Strengths
1. The author presents a novel approach by replacing the conventional mirror map with a learned mirror map, offering valuable insights for reinforcement learning research.
2. The experiments cover both a tabular setting and a real-world application, enhancing the potential for this work to be applied to real-world problems.

### Weaknesses
1. There are some typos in this paper, for example, in equation (5), it should be $\pi_{\theta_t}$ instead of $\pi_{t}heta$?
2. The author didn't provide related works of this paper, making it hard to understand and follow. And it is better to provide more training details in Appendix C.
3. It seems that the author only provides comparisons of their method with the negative entropy and d $\ell_2$-norm mirror map. Can the author provide comparisons with other methods?
4. The computational cost of the proposed method appears to be relatively high. It would be beneficial for the author to include a discussion comparing the computational cost of this method to that of existing approaches. This comparison would provide a valuable disscussion for understanding the trade-offs in efficiency and practicality.

### Questions
See weaknesses.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper explores the role of mirror maps in the Policy Mirror Descent (PMD) framework in reinforcement learning (RL), which includes various algorithms for policy optimization. Traditionally, the negative entropy mirror map, giving rise to the Natural Policy Gradient (NPG), is the most studied, but the authors argue that this choice is often sub-optimal. Through empirical experiments, they show that alternative, learned mirror maps can enhance PMD's performance across different RL environments, starting with tabular settings like Grid-World and scaling to more complex scenarios like MinAtar and MuJoCo. Their findings suggest that mirror map choice has a more substantial impact on PMD performance than theoretical convergence guarantees indicate. The manuscript highlights the potential for learned mirror maps to generalize across tasks and calls for further theoretical research to understand the influence of mirror maps on PMD's effectiveness.

### Strengths
- Empirical validation: the authors provide empirical evidence that challenges the reliance on the negative entropy mirror map in PMD.
- Comparison with theory: the paper highlights a gap between theoretical bounds and actual empirical performance.
- Algorithm: the use of ES makes sense here and is well justified.
- Clarity: the background and methodology sections are well written.

### Weaknesses
 - Reliance on ES which may not be very scalable (to higher dimensional mirror map parameterization).
- Experiments only include small environments where finding better mirror maps may not lead to significantly superior learning curves. Testing on a broader array of environments, especially those with different reward structures or high-dimensional state spaces would enhance the robustness and applicability of the findings.
- Experiments do not seem statistically significant and may hinder hyper-parameter optimization for some methods and not e.g. for the negative entropy mirror map baseline.

### Questions
1. How does the mirror map learned on e.g. Hopper perform on very different environments (other than Mujoco's)? Is performance/training dynamics significantly different from using the negative entropy mirror map?
2. I find it surprising that using negative entropy or l2 norm does not solve Asterix-MinAtar under 10M steps. I personally recall experimenting with Asterix and rather easily solving it. Could you provide a more detailed description of how hyperparameters were selected for each method, or include ablation studies showing the impact of key hyperparameters?

### Soundness
2

### Presentation
4

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
This paper investigates the Policy Mirror Descent in RL, which is known for its finite-time convergence guarantees and encompasses various algorithms by selecting a mirror map. However, the study explores the potential of alternative mirror maps (instead of negative entropy mirror map, which leads to the Natural Policy Gradient method), demonstrating that the conventional choice often results in suboptimal performance. In empirical studies, the authors use evolutionary strategies to identify more effective mirror maps, showing improved performance in tabular and non-tabular environments. The research highlights that the choice of mirror map significantly affects PMD's effectiveness, challenging existing theoretical assumptions and suggesting new directions for future research.

### Strengths
1. The research effectively highlights the limitations of existing convergence guarantees in capturing the impact of mirror maps. It provides robust empirical evidence that challenges the conventional choice of mirror maps, offering a fresh perspective on the potential of PMD. 

2. The experimental design is well-conceived and rigorous, aligning closely with the preceding analysis.

3. The paper is well-written, with clear definitions and precise descriptions. Despite covering a substantial amount of theory, it remains accessible and easy to read.

### Weaknesses
From my perspective, this paper makes a satisfactory and engaging contribution, though there is always room for improvement.

1. The paper offers compelling empirical evidence but does not provide a comprehensive theoretical framework to elucidate why certain mirror maps outperform others. Although developing such a framework is challenging, it represents a promising avenue for future research.

2. the study's focus on specific benchmark environments may not fully encompass the diversity and complexity of real-world scenarios in reinforcement learning, potentially limiting the generalizability of the findings.

### Questions
Q1: Although the experiments demonstrate that the learned map is more effective, I believe this does not necessarily conflict with the theoretical assertion that these methods share the same bound. Could the authors provide further explanation on this point?

Q2: In lines 165-166, what is the relationship between Bregman divergence and the mirror map $h$? Could this be further clarified?

Q3(minor): There is a typo in Equation 5 (\theta).

### Soundness
3

### Presentation
3

### Contribution
3
