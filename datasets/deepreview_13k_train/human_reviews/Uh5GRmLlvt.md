# On Rollouts in Model-Based Reinforcement Learning

- Decision: Accept
- Scores: 5, 5, 8, 6

## Abstract
Model-based reinforcement learning (MBRL) seeks to enhance data efficiency by learning a model of the environment and generating synthetic rollouts from it. However, accumulated model errors during these rollouts can distort the data distribution, negatively impacting policy learning and hindering long-term planning. Thus, the accumulation of model errors is a key bottleneck in current MBRL methods. We propose Infoprop, a model-based rollout mechanism that separates aleatoric from epistemic model uncertainty and reduces the influence of the latter on the data distribution. Further, Infoprop keeps track of accumulated model errors along a model rollout and provides termination criteria to limit data corruption. We demonstrate the capabilities of Infoprop in the Infoprop-Dyna algorithm, reporting state-of-the-art performance in Dyna-style MBRL on common MuJoCo benchmark tasks while substantially increasing rollout length and data quality.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This paper proposes Infoprop, a rollout mechanism designed to improve sample efficiency and asymptotic performance in model-based reinforcement learning (MBRL). Infoprop addresses the issue of epistemic model uncertainty typically introduced by ensemble methods or dropouts. It projects sampled next states into the maximum likelihood distribution of the predicted next state distribution and uses an information-theoretic criterion to determine the termination point of rollouts. When applied to Dyna-style MBRL, Infoprop demonstrates state-of-the-art performance, as shown in experiment results.

### Strengths
1. **Significance**: Model error remains a significant challenge in MBRL, and Infoprop addresses it through the rollout process.
2. **Extensive Experimentation**: The authors provide comprehensive experiments and analysis, including detailed evaluations of algorithm trajectories and environment buffers, which validate the effectiveness of the Infoprop algorithm.

### Weaknesses
1. **Assumptions**: The approach relies on two key assumptions. It is important to empirically assess the extent to which these assumptions hold in experimental environments. Specifically, the assumption that epistemic uncertainty is the primary source of model error needs further scrutiny. While the method may perform well under this assumption, it is crucial to understand its limitations when other sources of error, such as aleatoric uncertainty or structural model misspecification, are present. The paper should include experiments that explicitly test the robustness of the method to violations of this assumption.
2. **Organization**: The theoretical section could benefit from clearer structure. Presenting the main results in the form of definitions or theorems could improve readability. Simplifying technical details and focusing on the implementation—particularly regarding Equation (14)—would make the logical flow smoother. The current presentation makes it difficult to follow the derivation of the information-theoretic criterion and its connection to the rollout termination condition. A more step-by-step explanation of how the equations are derived and how they relate to the algorithm would be beneficial.

### Questions
1. Is the model error come solely from epistemic noise?
2. What is the advantage of using AES models, and why do you believe Infoprop does not impact their effectiveness?

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper presents a rollout mechanism that uses information theory to reduce the impact of epistemic uncertainty in MBRL. The paper presents some experimental analysis and a derivation of a result related to information loss.  The paper uses the idea of marginal entropy and mutual information to determine data corruption and stop a rollout.

### Strengths
Soundness
======
The paper uses the idea of marginal entropy and mutual information to determine data corruption and stop a rollout in MBRL. The idea is presented carefully with a derivation for the main result.
  
Significance & Related work
=========
The paper has a brief related work section, as part of the main paper, which is appreciated. However, there is a need for a deeper analysis of existing work, including  more in-depth comparisons that show the benefit of Infoprop to others, specifically including work in using simulated rollouts to guarantee performance, robust MBRL (Sung 2024, Kuo 2021), risk sensitivity (e.g. Webster 2021) and other uses of information theory in MBRL.

Presentation
=========
The paper is well written with few typos, usually around empty spaces in the text.

Quality
======
My main concerns are around the quality of the experimentation (see below) and on the need for authors to explore the limitations of their approach a bit deeper before publication. For example, the authors mention that the rollouts exhibit excellent data quality and yet there are instabilities: is this a function of the integration mechanism or of overfitting?

### Weaknesses
Experimentation
=========
The experimental analysis show the benefits of Infoprop when it runs in simple environments, however deeper experimentation is needed. For example, I would have expected to see some ablation studies showing the impact of the choice of lambda, instability, overfitting and other issues. 

Overall the paper presents a very promising initial idea with several avenues of experimentation that need to be explored to ensure its maximum potential is reached.

### Questions
The main limitations of the work, as identified above, are in the quality and significance as discussed above. These could be alleviated with a more in-depth experimentation which would lead to a more mature solution, and a more in-depth discussion of related work. All of them require space, and a such my questions relate to the guidance for the discussion section.

Specifically:
1. where is overfitting most prominent with Infoprop?
2. where there other information theoretic metrics (e.g redundancy) considered in the Infoprop design? If no, why not? if yes, why were they discarded?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper proposes a model rollout method for model-based reinforcement learning called infoprop. The main idea is to control for epistemic uncertainty using model rollout to reduce model error accumulation and in turn improve value or policy optimization. The concrete method is a re-weighting of ensemble predictions and an entropy-based criteria to stop rollout. The Mujoco experiments demonstrated substantial improvement in reducing error accumulation as well as convergence speed.

### Strengths
The proposed method is original and sound. The experiment hypotheses are very clear the the results clearly demonstrated the advantage of the proposed method.

### Weaknesses
The paper could benefit a lot from intuitive explanations of the proposed approach. For example, what's the intuition of the covariance intersection fusion result for readers that are not familiar with this literature.

* How does eq 14 actually follow from eq 4 and 9? 
* When the authors say eliminate epistemic uncertainty, does that mean setting the last term in eq 9 to zero? If so is the rest of the derivations simply accounting for $\mu^{\Delta}$?

### Questions
* How does eq 14 actually follow from eq 4 and 9? 
* When the authors say eliminate epistemic uncertainty, does that mean setting the last term in eq 9 to zero? If so is the rest of the derivations simply accounting for $\mu^{\Delta}$?

### Soundness
4

### Presentation
3

### Contribution
4

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The author presents a new method called *Infoprop*, which can be used as a plugin for Dyna-style model-based RL. The plugin increases the quality of data rollouts from the estimated model, thus enhancing the Dyna-style model-based RL. The experiment in Mujoco showed the SOTA performance except for the humanoid environment. The author also provides a solid theoretical analysis of why the plugin can increase the quality of rollouts based on the estimated model.

### Strengths
The author developed a new method, Infoprop, that enhances the performance of Dyna-style model-based RL:

*Versatility*: The Infoprop method can be integrated as a plugin for Dyna-style model-based RL, making it a flexible and adaptable enhancement for existing frameworks.

*Improved Data Quality*: By increasing the quality of data rollouts from the estimated model, Infoprop enhances the overall performance of Dyna-style RL approaches.

*Experimental Results*: The experiments conducted in Mujoco environments demonstrate state-of-the-art (SOTA) performance, showcasing the effectiveness of Infoprop in most environments, with the exception of the humanoid scenario.

*Theoretical Foundation*: The method is backed by robust theoretical analysis, explaining how the plugin improves rollout quality from the estimated model, which adds credibility to the approach.

### Weaknesses
1. The theoretical results in Section 4 are difficult to follow. A summary of the main result should be given at the start of the section. Also, I suggest the author clearly present the main result as a theorem. 
2. Too many notations have been introduced, which could be simplified. For example, Section 2.4 could be condensed into a single sentence, accompanied by equation (5) and relevant citations since it represents a well-known formulation in model-based RL.
3. The enhancement applies specifically to Dyna-style RL, not all model-based RL approaches. Making the title misleading.
4. The Assumptions at the end of Section 4.2 are stated without any explainations.

### Questions
In Figure 6, INFOPROP Dyna does not outperform MACURA. However, if I understand correctly, the proposed method can be used as a plugin within MACURA, which makes it puzzling that INFOPROP Dyna does not surpass MACURA.

### Soundness
4

### Presentation
3

### Contribution
3
