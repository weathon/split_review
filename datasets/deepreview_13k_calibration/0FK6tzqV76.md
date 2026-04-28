# RTDiff: Reverse Trajectory Synthesis via Diffusion for Offline Reinforcement Learning

- Decision: Accept
- Avg Score: 5.75
- Scores: 6, 6, 6, 5

## Abstract
In offline reinforcement learning (RL), managing the distribution shift between the learned policy and the static offline dataset is a persistent challenge that can result in overestimated values and suboptimal policies. Traditional offline RL methods address this by introducing conservative biases that limit exploration to well-understood regions, but they often overly restrict the agent's generalization capabilities. Recent work has sought to generate trajectories using generative models to augment the offline dataset, yet these methods still struggle with overestimating synthesized data, especially when out-of-distribution samples are produced. To overcome this issue, we propose RTDiff, a novel diffusion-based data augmentation technique that synthesizes trajectories *in reverse*, moving from unknown to known states. Such reverse generation naturally mitigates the risk of overestimation by ensuring that the agent avoids planning through unknown states. Additionally, reverse trajectory synthesis allows us to generate longer, more informative trajectories that take full advantage of diffusion models' generative strengths while ensuring reliability. We further enhance RTDiff by introducing flexible trajectory length control and improving the efficiency of the generation process through noise management. Our empirical results show that RTDiff significantly improves the performance of several state-of-the-art offline RL algorithms across diverse environments, achieving consistent and superior results by effectively overcoming distribution shift.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
To address the distribution shift issue in offline reinforcement learning, this paper proposes a novel diffusion-based data augmentation technique, namely RTDiff, where rather than generating forward trajectories, the reverse one is synthesized, which is also the paper's main contribution. Furthermore, the performance of RTDiff is enhanced with the introduction of trajectory length control and noise management. Experimental results show the effectiveness of the proposed approach.

### Strengths
The ideas in this paper are interesting and novel, where to my knowledge, this is the first work that utilizes the concept of generating the reverse trajectories to address the distribution shift issue. The paper is clearly written and well-motivated.  The effectiveness of the proposed method is verified in various environments, and ablation studies are also conducted to validate the effectiveness of different components of the proposed method.

### Weaknesses
The main concern of the paper is whether the reverse synthesis can actually address the issue of distribution shift. As it is not state clearly whether the OOD detector is incorporated with other data augmentation baselines, e.g., SynthER and ATraDiff, it is not very certain whether the better performance achievement of RTDiff is due to the reverse synthesis or the using of the OOD detector. In Section 6, an analysis is conduct by using a simple illustrative environment to show why reverse synthesis avoids issues present in normal synthesis. However, on the one hand, it is better to directly use an environment used in the experiments for the analysis, on the other hand, it is confusing why the reverse synthesis generates trajectories that move from the dangerous area to the upper or lower areas while normal synthesis generates trajectories that start from the lower area and enter the middle dangerous area. Do these two approaches both start from a state in the offline data, and then generate the trajectories in different ways? If the OOD detector is used in the normal synthesis, can the dangerous areas also be avoided? Moreover, the theoretical contribution of the proposed is not very significant.

### Questions
1. Are the OOD detector and noise management incorporated with other data augmentation baselines, e.g., SynthER and ATraDiff?

2.In Section 6, a very specific environment is adopted to show the advantages of reverse synthesis over normal synthesis, what is the reason/possible explanation that normal synthesis with OOD detector even produces significantly more In2Out than normal synthesis without OOD detector? (18.2%11.2)

3. For other questions, please see questions raised in Weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes RTDiff, a novel diffusion-based data augmentation technique that synthesizes trajectories in a reverse direction. Such reverse generation naturally mitigates the risk of overestimation by ensuring that the agent avoids planning through unknown states. RTDiff also introduces some other tricks including flexible trajectory control and noise management to improve sythesis quality. Emprirical results show the advantage of reverse generation over forward generation.

### Strengths
1. The article is well-written, with clear expression and logic, effectively reflecting the main argument.
2. The experiments are very comprehensive. The authors validate the effectiveness of their method across a series of tasks, including both proprioceptive observations and visual observations.

### Weaknesses
1. I believe the authors miss a key related work (called ROMI [1]), which is the first to propose using reverse trajectory generation in the field of offline reinforcement learning. The motivation described for reverse trajectory generation in these two work is also very similar. Therefore, considering that this paper is neither the first to propose the use of reverse trajectory generation in offline RL nor the first to use diffusion for data augmentation, I would say the novelty of this paper is quite limited.
2. I think this paper lacks comparisons with model-based offline RL methods in the experimental section. According to my understanding, using a diffusion model for data augmentation essentially falls under the same category as previous model-based offline RL methods. For instance, MOPO [2] essentially generates a batch of synthetic samples to supplement the original samples. Therefore, the authors should compare some model-based offline RL methods, such as MOPO, RAMBO [3], etc.

### Questions
1. Can the authors discuss in detail the differences between this paper and previous similar works (like ROMI)?
2. This method is built on IQL, TD3BC, and CQL. Have there been any adjustments to the hyperparameters of these methods after using data augmentation?
3. Is it possible to conduct a quantitative evaluation of the quality of the generated trajectories? For example, assessing the model error of the generated trajectories, etc.

### Soundness
3

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
4

### Summary
This paper introduces a novel diffusion-based data augmentation method, RTDiff, for offline reinforcement learning. First, RTDiff mitigates the data distribution shift issue present in previous data augmentation methods by generating reverse trajectories instead of forward ones. Second, RTDiff trains an out-of-distribution (OOD) detector to truncate the OOD segments of generated trajectories, further enhancing sample authenticity. Finally, the authors propose a new noisy control method to improve sample generation efficiency. Experimental results validate the effectiveness and efficiency of RTDiff and different components across both vector-based and pixel-based tasks.

### Strengths
1. This paper is well-written and easy to follow.
2. RTDiff introduces reverse trajectory generation, an OOD detector, and a noisy control method to achieve efficient and reliable sample generation. These approaches are intuitively sound.
3. The authors conduct extensive benchmark and ablation experiments. Experimental results demonstrate that RTDiff outperforms previous baselines on both vector-based and pixel-based tasks, and each component—reverse trajectory generation, the OOD detector, and noisy control—exhibits its effectiveness.

### Weaknesses
1. Reverse trajectory generation is not new to offline RL, and the paper lacks a discussion and experimental comparison of prior works, such as [1]. Specifically, the paper should clarify how the proposed method differs from existing approaches that also utilize reverse trajectories, particularly in the context of dynamics learning and rollout strategies. The current discussion does not adequately address the novelty of the approach in relation to these existing methods.
2. The paper lacks a clear and well-reasoned explanation of the issues with previous data augmentation methods. In lines 88-90, this paper claims that previous data augmentation methods suffer from the data distribution shift, potentially leading to value overestimation. However, since all of these works use offline RL algorithms, I think data distribution shift is not the key issue. On the contrary, data augmentation is only effective when the generative model can produce samples that differ from the training data. The paper needs to articulate more precisely why forward trajectory generation is problematic for offline RL and how reverse trajectory generation specifically addresses these issues beyond simply generating different samples.
3. Generated data fidelity is a more critical factor. The paper lacks a quantitative evaluation of the fidelity of generated samples. It is not sufficient to only demonstrate improved RL performance; the paper must also show that the generated samples are of high quality and not simply random noise. The absence of metrics like the Fréchet Inception Distance (FID) or similar measures of sample quality is a significant oversight.

### Questions
See weaknesses.

### Soundness
3

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
Traditional offline reinforcement learning methods often introduce conservative biases to limit exploration to familiar regions, but this can restrict an agent's ability to generalize. While recent approaches use generative models to expand offline datasets, they can overestimate synthesized data, particularly when it includes out-of-distribution samples. RTDiff is introduced to address this, which is a diffusion-based data augmentation technique that creates trajectories in reverse, moving from unknown to known states. This reverse approach reduces the risk of overestimation by ensuring the agent avoids planning through unfamiliar regions. It also supports generating longer trajectories, utilizing diffusion models effectively while maintaining reliability. RTDiff further optimizes the process with flexible trajectory length control and noise management to improve generation efficiency.

### Strengths
The reverse generation method, which has been empirically verified, effectively reduces the augmentation of data in risky regions. This concept is intuitively illustrated in the diagram.

### Weaknesses
1.Previous research [1] introduced a reverse data generation approach using a transition model. In the current work, the vanilla model is replaced with a diffusion model, yet the fundamental concept remains unchanged, limiting the overall contribution.

2.The explanation relies on an intuitive diagram, but it would be more effective to demonstrate several specific cases. Identifying which states are risky.  For example, some states are prone to be overestimated and easily generated by a forward model, but the reverse model effectively avoids generating them.

3.Minor errors are present, such as in line 156, where "dat" should be corrected to "data."

4.Environments based on visual data should be included in the analysis.

### Questions
Please see weaknesses.

### Soundness
2

### Presentation
2

### Contribution
2
