# Efficient Multi-agent Offline Coordination via Diffusion-based Trajectory Stitching

- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 6, 8, 6

## Abstract
Learning from offline data without interacting with the environment is a promising way to fully leverage the intelligent decision-making capabilities of multi-agent reinforcement learning (MARL). Previous approaches have primarily focused on developing learning techniques, such as conservative methods tailored to MARL using limited offline data. However, these methods often overlook the temporal relationships across different timesteps and spatial relationships between teammates, resulting in low learning efficiency in imbalanced data scenarios. To comprehensively explore the data structure of MARL and enhance learning efficiency, we propose Multi-Agent offline coordination via Diffusion-based Trajectory Stitching (MADiTS), a novel diffusion-based data augmentation pipeline that systematically generates trajectories by stitching high-quality coordination segments together. MADiTS first generates trajectory segments using a trained diffusion model, followed by applying a bidirectional dynamics constraint to ensure that the trajectories align with environmental dynamics. Additionally, we develop an offline credit assignment technique to identify and optimize the behavior of underperforming agents in the generated segments. This iterative procedure continues until a satisfactory augmented episode trajectory is generated within the predefined limit or is discarded otherwise. Empirical results on imbalanced datasets of multiple benchmarks demonstrate that MADiTS significantly improves MARL performance.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper investigates the use of diffusion models for offline multi-agent reinforcement learning (MARL), extending certain diffusion-based approaches originally developed for single-agent offline RL to a multi-agent setting. Specifically, the authors combine Denoising Diffusion Probabilistic Models (DDPM), stitching techniques (to merge high-reward and low-reward data points and address data imbalance), and Integrated Gradients (IG) for identifying underperforming agents. This results in a data augmentation process that can enhance offline datasets and other MARL algorithms. Experiments are conducted using MPE and SMACv1, with comparisons to BC and OMIGA.

### Strengths
- The diffusion approach makes sense. Using a diffusion model to enrich offline datasets could support several other MARL algorithms.
- The employed techniques align with recent advancements in diffusion-based RL.
- The paper is well-written and easy to follow.

### Weaknesses
1. The techniques seem to be a straightforward extension from diffusion-based single-agent RL.
2. Most techniques, except those in Section 4.2, appear to be directly adapted from single-agent settings, with single-agent states and actions replaced by global observations and actions.
3. There is already existing work on diffusion models for offline MARL. For instance, how does this approach compare to MADiff [1], which also develops diffusion models to enhance offline datasets in offline MARL? Notably, MADiff compares its methods against several MARL baselines, which seems lacking in this work.
4. In addition to MPE and SMACv1, more challenging MARL tasks like MAMuJoCo and SMACv2 should be considered for comparisons.
5. It’s unclear how this approach compares to other data-augmentation techniques in offline MARL. Additional citations, discussions, and experimental comparisons would be needed.

### Questions
- How does your approach compare to MADiff?
- Can these methods be applied to cooperative-competitive settings?
- Would the approach work effectively with balanced but bad datasets? What would happen if the data were balanced but consisted primarily of transitions with low rewards?

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
The paper proposes the MADiTS method to address the imbalance of offline datasets in both temporal and spatial dimensions. Specifically, it uses diffusion models to generate trajectory segments, then employs bidirectional environmental dynamics constraint to ensure the consistency of trajectories with environmental dynamics, and finally utilizes offline credit assignment technique to identify and optimize the behavior of underperforming agents in the generated segments.

### Strengths
1.	The overall structure of the paper is complete, the content is substantial, and the experimental evidence is convincing.
2.	Generating trajectories using diffusion models and ensuring the generated segments conform to environmental dynamics with bidirectional dynamic constraints is similar to learning a world model and using it to verify the rationality of trajectories.
3.	As a data augmentation method, MADiTS is compatible with any offline MARL algorithm and has good versatility.

### Weaknesses
1.	The paper uses several certain threshold hyperparameters (environment-independent), which may make the method too sensitive to the setting of hyperparameters. Moreover, the paper does not conduct experimental analysis on methods with different hyperparameters. Specifically, the lack of analysis on how these thresholds interact with the diffusion model's generation process and the bidirectional dynamics constraint is a significant oversight. For example, the reconstruction error threshold $\delta_{recon}$ directly influences which generated trajectory segments are deemed valid, but the paper does not explore how different values of this threshold affect the diversity and quality of the augmented dataset, nor how it impacts the final performance of the offline MARL algorithm. This lack of sensitivity analysis makes it difficult to assess the robustness and generalizability of the proposed method.
2.	MADiTS involves multiple models and steps, which may lead to computational complexity. Additionally, the paper does not include experimental analysis on this aspect. The paper does not provide a detailed breakdown of the computational cost associated with each stage of the MADiTS pipeline, such as the diffusion model training, trajectory generation, dynamics constraint verification, and credit assignment. Without this analysis, it's difficult to evaluate the practical applicability of the method, especially in resource-constrained environments. Furthermore, the paper does not compare the computational overhead of MADiTS with other offline MARL data augmentation techniques, making it hard to assess its efficiency.

### Questions
1.	How does the proposed method address the imbalance of the dataset in terms of time and space? For example, which technique solves the time imbalance problem, and which solves the spatial imbalance problem?
2.	How are environment-independent hyperparameters like $\delta_{recon}$ determined? What effects do different values have?

### Soundness
3

### Presentation
3

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
The paper presents a novel data augmentation method, MADiTS, to generate high-quality multi-agent trajectories for offline policy learning. A multi-agent trajectory diffusion model is trained to generate augmented future trajectories conditioned on the first-step joint observations. Multiple techniques are proposed to improve the quality of augmented trajectories. First, a forward dynamics model is used together with the inverse dynamics model to filter out dyanmic inconsist segments. Then, the interagted gradient is adopted to determine underperforming agents, and regenerating those agents' trajectories while keeping others' fixed. Experimental results on MPE and SMAC datasets demonstrate superior performence of MADiTS over baseline augmentation methods.

### Strengths
1. The paper is well-written and easy to follow.

2. The idea of using the interagted gradient to find underperforming agents is novel to me, and I believe it might have border potential in multi-agent learning.

3. The experiment results are impressive, achieving SOTA performance on all datasets.

### Weaknesses
1. The experiments are limited to environments with a small number of agents (up to five). The effectiveness of MADiTS on datasets with a larger number of agents has not been demonstrated.

2. Given the known issues [1] with SMAC (v1), why were results not included for SMACv2?

3. Unlike DiffStitch, which conditions on both the first and last trajectory segments, the diffusion model in MADiTS generates the subsequent trajectory based solely on the first state, which makes the naming of "Stitch" a little confusing.

4. A key highlight of this paper is the use of integrated gradients to identify underperforming agents. However, this part lacks sufficient analysis. It would be beneficial to quantitatively demonstrate a general correlation between the value of integrated gradients and underperformance degrees across different environments.

5. I have doubts about the extent to which regeneration can improve the overall reward. The multi-agent diffusion model learns from the joint trajectory distribution, meaning it is constrained by the combination of cooperative capabilities existed in the training data. Suppose, in a two-agent environment (agent 0 and agent 1), the training set includes two joint trajectories, $\tau_1$ and $\tau_2$. In $\tau_1$, agent 0 significantly contributes to the team reward, while agent 1’s contribution is minimal. In $\tau_2$, the situation is reversed. Now, suppose the model’s first generation produces a trajectory where agent 0 has high contribution and agent 1 has low contribution. If we successfully use integrated gradients to identify agent 1 and attempt to condition on agent 0’s trajectory to regenerate agent 1’s trajectory, the model should be unable to produce a high-contribution trajectory for agent 1, as the training dataset lacks joint trajectories where both agents have high contributions. Therefore, in this case, MADiTS may not effectively combine individual trajectories to yield better joint trajectories. The authors should discuss similar cases, clarifying the method’s limitations and maybe requirements for the training dataset.

### Questions
See weaknesses.

### Soundness
3

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
The authors propose a method called MADiTS to enhance the quality of imbalanced offline datasets in Multi-Agent Reinforcement Learning (MARL). By applying diffusion-based data augmentation, MADiTS generates high-return trajectories while enforcing dynamics constraints to ensure they align with the environment dynamics. Additionally, a behavior correction mechanism correct the actions of suboptimal agents, improving their trajectories within shared reward contexts. Experiments on MPE and SMAC datasets show that MADiTS can improve the performance of offline algorithms like Behavior Cloning (BC) and other offline algorithms.

### Strengths
- The authors address an important issue of dataset quality in MARL, particularly relevant for offline applications where data imbalance often impacts policy performance in real-world scenarios.
- The paper is well-written, clear and easy to follow. 
- The authors apply their method to datasets collected on SMAC and MPE, two popular MARL environments, and apply it to behavior cloning (BC) and two modern offline MARL algorithms - OMIGA and CFCQL.
- The authors provide an ablation study to show the impact of different components of their MADiTS method.

### Weaknesses
Methodology:
- The authors provide details on how they generate the imbalanced dataset, using random perturbations on expert trajectories. However, it is not clear why this is better than using a dataset collected by mixed policies, e.g. taking medium and expert policies and combining their trajectories in a dataset. This appears to be more realistic and relevant to the problem of imbalanced datasets in MARL. A discussion on this choice would be relevant.
- Work such as [2,3] highlights the importance of diverse trajectories in offline MARL. This impact of MADiTS on the diversity of the trajectories is not discussed in the paper.  
- Clarity is needed regarding the computational cost of MADiTS. Details such as runtime and comparison with other trajectory augmentation methods (e.g., MA-MBTS or baseline models) would be relevant, especially since the text includes vague descriptors like “until a satisfactory trajectory is obtained.” Further, insights into how MADiTS scales with agent numbers or in larger MARL environments would enhance applicability.

Comparisons with Related Diffusion Models:
- In the appendix, the authors mention they use MaDiff [1] architecture for the diffusion model. However, the original MaDiff model is not included as a baseline in the main experiments, nor is Diffusion Offline Multi-agent Model (DOM2) [3], another relevant diffusion-based MARL trajectory augmentation approach. Furthermore, Shared Individual Trajectories (SIT) [2], another work that aims at helping with imbalanced datasets in offline MARL is only briefly mentioned in the appendix, and not mentioned in the main text.  A comparison with MaDiff (or clarification if “w/o dc + pn” in Figure 4a is equivalent to MaDiff) would strengthen the evaluation. Including DOM2 and SIT as baselines or discussing the differences would clarify MADiTS's unique contributions to diffusion-based MARL augmentation.

### Questions
1. Why does this approach generate an imbalanced dataset by perturbing expert trajectories? Why is this better than using a dataset collected by mixed policies and combine their trajectories in a dataset?
2. How does the proposed method impact the diversity of the trajectories in the augmented dataset? Do the dynamics constraints or behavior correction mechanism hurt the diversity of the trajectories?
3. What is the computational cost of the proposed method compared to the baselines? How does the proposed method scale with the number of agents, particularly with the integrated gradient computation?
4. How does MADiTS compare to standalone MaDiff, DOM2 and SIT? What are the key differences, and why were these methods not used as baselines in the primary experiments?

### Soundness
2

### Presentation
3

### Contribution
2
