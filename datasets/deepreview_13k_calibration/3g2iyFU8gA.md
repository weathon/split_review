# Learning Fused State Representations for Control from Multi-View Observations

- Decision: Reject
- Avg Score: 4.50
- Scores: 5, 5, 5, 3

## Abstract
In visual control tasks, leveraging observations from multiple views enables Reinforcement Learning (RL) agents to perceive the environment more effectively. However, while multi-view observations enrich decision-making information, they also increase the dimension of observation space and introduce more redundant information. Thus, how to learn compact and task-relevant representations from multi-view observations for downstream RL tasks remains a challenge. In this paper, we propose a Multi-view Fusion State for Control (MFSC), which integrates a self-attention mechanism with bisimulation metric learning to fuse task-relevant representations from multi-view observations. To foster more compact fused representations, we also incorporate a mask-based latent reconstruction auxiliary task to learn cross-view information. Additionly, this mechanism of mask and reconstruction can enpower the model with the ability to handle missing views by learning an additional mask tokens. We conducted extensive experiments on the Meta-World and Pybullet benchmarks, and the results demonstrate that our proposed method outperforms other multi-view RL algorithms and effectively aggregates task-relevant details from multi-view observations, coordinating attention across different views.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a method that combines a bisimulation-based approach with masked representation learning for multi-view reinforcement learning. The core idea is that to enable task-relevant multi-view fusion, it is essential to align the integration process closely with the specific objectives of the task. In other words, when fusing information from multiple views, the task’s specific goals (Equation 8) must be considered. The authors have evaluated their method on two visual control environments, including Meta-World and PyBullet, demonstrating significant performance improvements over baseline methods.

### Strengths
- The paper is clearly written and easy to understand.
- The proposed method that integrates bisimulation metric learning into the fusion process of multi-view states is reasonable.
- The authors have provided extensive experimental results, covering various visual RL environments, to validate the effectiveness of the method. The paper also includes experiments with missing views as well as additional visualizations to interpret the effectiveness of the method.

### Weaknesses
•	A few formula faults are discovered in the paper.
•	Evaluation Metrics: The evaluation metrics used in the experiments could be more comprehensive. Currently, the focus appears to be on task performance, but including metrics that assess representation quality (e.g., reconstruction loss) would provide a fuller picture of the model’s effectiveness.
•	Generalization to Other Tasks: The experiments are primarily conducted on Meta-World. To evaluate the generality of the approach, the authors should consider applying MFSC to other control tasks or environments. This would help demonstrate the versatility and broader applicability of the proposed method.
•	Limitations Discussion: The paper should include a dedicated section discussing the limitations of the proposed method. Identifying potential weaknesses and suggesting avenues for future work would add depth to the contribution.

### Questions
I recommend the authors systematically compare the similarities and differences between their method and Seo et al.'s masked multi-view RL approach within the main text.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes the Multi-view Fusion State for Control (MFSC), which integrates a self-attention mechanism and bisimulation metric learning to fuse task-relevant representations from multi-view observations, and incorporates a mask-based latent reconstruction auxiliary task to obtain more compact fused representations and handle missing views.

### Strengths
1. The writing is relatively clear.

2. The performance of the proposed method is validated on Meta-World and Pybullet benchmarks.

### Weaknesses
1. The author incorporates bisimulation principles by integrating reward signals and dynamic differences into the fused state representation to capture task-relevant details. As I am aware, [1] also acquires representations for control with bisimulation metrics. Additionally, the author employed a Mask-based Latent Reconstruction strategy, which is analogous to that in [2]. Does this similarity suggest a deficiency in significant innovation or does the author offer additional components or enhancements that differentiate it from the existing strategies in [1] and [2]? Furthermore, it is essential to determine whether appropriate credit and comparison with the prior works in [1] and [2] have been adequately accounted for.

[1] Learning invariant representations for reinforcement learning without reconstruction.

[2] Mask-based Latent Reconstruction for reinforcement learning。

3. Missing many recent visual RL baselines: the baselines used in the paper are all old methods and a large body of the recent methods developed on visual reinforcement learning are ignored [1][2].

[1] TACO: Temporal Latent Action-Driven Contrastive Loss for Visual Reinforcement Learning.

[2] Mastering Diverse Domains through World Models.

4. Whether this method is only useful for robot control tasks needs to be further verified on more types of environments, such as Carla, atari, etc.

5.  The paper lacks sufficient ablation experiments. The author only ablated MFSC without bisimulation constraints ('MFSC w/o bis') and MFSC without Mask and Latent Reconstruction ('MFSC w/o res'), but not more detailed parts like the Self-Attention Fusion Module.

6. The author claims that MFSC can be seamlessly integrated into any existing downstream reinforcement learning framework to enhance the agent's understanding of the environment. However, there are no relevant experiments to verify this claim.

### Questions
Please see the weaknesses.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper presents a novel architecture called Multi-view Fusion State for Control (MFSC), designed to learn compact and task-relevant representations from multi-view observations in reinforcement learning (RL). This approach integrates a self-attention fusion module with bisimulation metric learning to aggregate information from different views, while also using a mask-based latent reconstruction auxiliary task to promote cross-view information aggregation.  Experiments conducted on Meta-World and Pybullet demonstrate the superiority of MFSC over other methods.

### Strengths
1.	The paper addresses the challenging and significant problem of learning task-relevant fused state representations from multi-view observations, which is a crucial aspect of multi-view reinforcement learning. 
2.	The integration of a mask-based latent reconstruction task enhances the model’s ability to learn cross-view information. The proposed approach, combining self-attention and bisimulation metrics, offers an effective solution.
3.	This paper demonstrates the effectiveness of MFSC across multiple challenging benchmarks, including robotic manipulation tasks in Meta-World and control tasks in Pybullet.

### Weaknesses
1.	This paper does not include comparisons with approaches tailed for visual RL, such as [1-2], particularly multi-view visual RL method like [3]. Evaluating MFSC against such baselines would provide a more accurate assessment of its effectiveness and novelty.
2.	How does the computational complexity of MFSC compare to baseline approaches in terms of training time, inference time, and resource requirements?
3.	This paper does not provide sensitivity analyses of MFSC with respect to different hyperparameters, such as the weight of fusion loss and the weight of reconstruction loss.
References
[1] Hafner et al. Mastering diverse domains through world models. arXiv preprint   arXiv:2301.04104, 2023.
[2] Seo et al. Masked world models for visual control. CORL, 2023.
[3] Seo et al. Multi-view masked world models for visual robotic manipulation. ICML, 2023.

### Questions
Please see weakness section.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper introduces a novel approach named Multi-view Fusion State for Control(MFSC)，which ingrates a self-attention mechanism with bisimulation metric learning to fuse task-relevant representation from multi-view observation. Additionally, the paper also incorporated a mask-based latent reconstruction auxiliary task to learn cross-view information in order to foster more compact fused presentation. In this paper, two major problems were solved : First is Higher data dimensions and more redundant information , and Informative aggregation of representation from various views.

### Strengths
1.	Clear statements and good structure. The paper is well-structured, and viewpoints was stated logically. The introduction provides a good overview of the challenges in the multi-view representation learning task and approach to address them relatively.  Also illustrate provided along with methods made it easy and vivid.
2.	Sufficient and solid proof in major conclusions. Problems were clearly defined and followed by mathematical formulations with clear explanation and ended with a solution with validate experiments. 
3.	Comprehensive experiment and supportive solution ,also contributions made by this method were shown vividly and clearly through several comparative illustrate shown in the part of Experiments.  
4.	Reproductive experiment with project code and data shared.  Experiments  result can be verified personally by readers with resources provided in this paper.

### Weaknesses
•	A few formula faults are discovered in the paper.
•	Evaluation Metrics: The evaluation metrics used in the experiments could be more comprehensive. Currently, the focus appears to be on task performance, but including metrics that assess representation quality (e.g., reconstruction loss) would provide a fuller picture of the model’s effectiveness.
•	Generalization to Other Tasks: The experiments are primarily conducted on Meta-World. To evaluate the generality of the approach, the authors should consider applying MFSC to other control tasks or environments. This would help demonstrate the versatility and broader applicability of the proposed method.
•	Limitations Discussion: The paper should include a dedicated section discussing the limitations of the proposed method. Identifying potential weaknesses and suggesting avenues for future work would add depth to the contribution.

### Questions
Overall, while the MFSC architecture presents a promising direction for multi-view reinforcement learning, addressing the outlined weaknesses and incorporating the suggested improvements will significantly enhance the paper's clarity, depth, and impact in the field.

### Soundness
3

### Presentation
3

### Contribution
2
