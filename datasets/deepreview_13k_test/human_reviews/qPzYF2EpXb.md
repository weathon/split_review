# GravMAD: Grounded Spatial Value Maps Guided Action Diffusion for Generalized 3D Manipulation

- Decision: Accept
- Scores: 6, 6, 6, 6

## Abstract
Robots' ability to follow language instructions and execute diverse 3D tasks is vital in robot learning. Traditional imitation learning-based methods perform well on seen tasks but struggle with novel, unseen ones due to variability. Recent approaches leverage large foundation models to assist in understanding novel tasks, thereby mitigating this issue. However, these methods lack a task-specific learning process, which is essential for an accurate understanding of 3D environments, often leading to execution failures. In this paper, we introduce \textbf{GravMAD}, a sub-goal-driven, language-conditioned action diffusion framework that combines the strengths of imitation learning and foundation models. Our approach breaks tasks into sub-goals based on language instructions, allowing auxiliary guidance during both training and inference. During training, we introduce \textbf{Sub-goal Keypose Discovery} to identify key sub-goals from demonstrations. Inference differs from training, as there are no demonstrations available, so we use pre-trained foundation models to bridge the gap and identify sub-goals for the current task. In both phases, \textbf{GravMaps} are generated from sub-goals, providing GravMAD with more flexible 3D spatial guidance compared to fixed 3D positions. Empirical evaluations on RLBench show that GravMAD significantly outperforms state-of-the-art methods, with a 28.63\% improvement on novel tasks and a 13.36\% gain on tasks encountered during training. These results demonstrate GravMAD's strong multi-task learning and generalization in 3D manipulation. Video demonstrations are available at: \url{https://gravmad.io}.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The paper proposes a pipeline of Grounded Spatial Value Maps-guided Action Diffusion (*GravMAD*), which is a subgoal-driven, language-conditioned action diffusion framework combining VoxPoser (Huang et al., 2023) with subtask imitation learning based on 3D Diffuser Actor (Ke et al., 2024). The idea is essentially to break tasks into sub-goals based on language instructions, allowing auxiliary guidance to help robots conceptually grasp tasks more accurately than directly using pre-trained foundation models.

The division of subtasks is conducted via Sub-goal Keypose Discovery, which is defined to happen when end effectors make contact or disengage with the objects. The proposed method uses pre-computed keyposes and touch&gripper change detection to segment subtasks for training epochs. During inference, the proposed method uses the LLM-based Planner and Composer from VoxPoser (Huang et al., 2023).

With the segmented subtasks, the proposed method first uses VoxPoser (Huang et al., 2023) to generate 3D value maps *GravMaps* and then uses 3D Diffuser Actor (Ke et al., 2024) to conduct subtask imitation learning and generate action sequences with the condition of tokens from *GravMaps*.

The authors test *GravMAD* on 20 RLBench (James et al., 2020) simulated tasks, including 12 original tasks selected from RLBench and  8 modified new tasks. Empirical results show that the proposed framework outperforms both VoxPoser and 3D Diffuser Actor in most seen and novel tasks, which validates GravMAD's superiority in both generalization and preciseness.

### Strengths
1. The paper is well-written, easy to follow, and presents its ideas clearly. 
2. The approach of combining VoxPoser's planning and perception ability with precise subtask imitation learning from 3D Diffuser Actor is well-motivated and clever to enhance the model’s long horizon task capability to achieve both VoxPoser's generalization and 3D Diffuser Actor's preciseness.
3. The reported scores are evaluated across 3 seeds, which are statically robust.

### Weaknesses
1. The proposed Sub-goal Keypose Discover method is kind of naive. The proposed method simply uses the change in the gripper’s open/close state and the change in touch force to segment a whole task, which could suit simple tasks like moving the chicken but might not work for tasks with longer horizons. This segmenting requires complex reasoning over the concrete task description and comprehensive understanding. During inference, foundation models like VoxPoser can be better at dividing subtasks due to the reasoning ability of LLM. However, for this proposed pipeline where different segmenting methods are used in training and testing, there could even be a domain shift for the subtasks' distribution itself due to unaligned segmenting.
2. The comparison and evaluation are limited. The selection strategy of the 12 tasks over 100 language-conditioned tasks from RLBench is not mentioned. The 8 modified tasks are not justified for their novelty, which might cause a doubt on opportunistic choices. 
3. Since both baselines of VoxPoser and 3D Diffuser Actor have conducted real-world evaluations, a real-world comparison for *GravMAD* will be more convincing.

Though conducted in an A+B paradigm on VoxPoser and 3D Diffuser Actor, this work's engineering contribution is solid and the idea of subtask imitation learning is novel. I will raise my score if more validations are provided.

### Questions
1. Can you provide more details on the selection strategy of the 12 tasks over 100 language-conditioned tasks from RLBench? Why do you choose 12 and why these 12? The currently designed novel tasks feature scenes and objects similar to those in the training tasks. Can you design more complex novel tasks?
2. Can you evaluate the performance of the proposed method in a real-world experiment? Most setups should be similar to 3D Diffuser Actor and not that hard.

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
This paper introduces GravMAD, a new approach that decomposes 3D manipulation tasks into key sub-goals, generates 3D spatial GravMaps to capture spatial relationships from these sub-goals, and employs an action diffusion policy to learn actions through imitation learning. This design aims to combine the precision of imitation learning with the generalization capabilities of foundation models. Extensive experiments conducted on RLBench show that GravMAD achieves improvements in both training tasks and novel tasks.

### Strengths
* The authors conduct extensive experiments, including comparisons with different types of baselines and a detailed ablation study.
* The authors provide diverse visualization in the paper and on the website, enhancing readers' understanding.
* The paper is well-organized and easy to comprehend.

### Weaknesses
* The novelty of the proposed method is limited, as it resembles a combination of previous works, Voxposer and 3D Diffuser Actor. Specifically, the authors use a similar approach to Voxposer by decomposing tasks and generating 3D spatial heatmaps for each sub-task, which are then integrated into the 3D Diffuser Actor architecture. The primary innovation appears limited to the proposed GravMAD framework.
* The comparison between GravMAD and 3D Diffuser Actor on training tasks indicates that, although the introduction of GravMap improves performance on most tasks, GravMAD's performance heavily relies on both the Detector and GravMap. If the Detector’s predictions lack precision, it can even degrade the method's performance, potentially compromising its robustness in scenarios where camera capture is unclear or ambiguous.
* In the ablation study w/o. Cost Map, it is surprising that the method achieves a zero score. Could the authors provide further explanation on why the predicted actions result in non-unit quaternions in this scenario? (This seems to conflict with the statement in Section 3.1, which mentions, "to avoid quaternion discontinuities, we use the 6D rotation representation.") Additionally, if the predicted quaternion is not-unit, we can normalize and convert it into a unit quternion. 
* It is advisable to conduct real-world experiments, as many related works, such as Voxposer and 3D Diffuser Actor, also include real-world demonstrations.

### Questions
* The use of a foundation model, such as GPT-4o, during inference might be time-consuming and could potentially hinder real-time responsiveness in robotic manipulation. Could the authors provide the average inference time for GravMAD at each sub-task stage?
* During training, why not generate GravMap in the same way as during inference? (One possible reason may be that the foundation model’s inference time is too lengthy?) The GravMap generated from demonstration ground-truths may differ in distribution from the GravMap produced by the foundation model, which could impact inference performance.

### Soundness
2

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
3

### Summary
This manuscript investigates 3D manipulation tasks through robot learning. Traditional imitation learning excels with familiar tasks but struggles with new, unseen ones. Recent approaches use large foundation models to mitigate this but lack task-specific learning, often leading to failures in 3D environments. To overcome this, the author introduces a novel framework termed Grounded Space Value Map-guided Action Diffusion (GravMAD). Due to its promising results, I am tentatively inclined to accept the paper. However, I find certain aspects unclear, especially the evaluation of design choices and overall performance. I am open to revising my evaluation if the authors can address these concerns comprehensively and convincingly detail the contributions of their work.

### Strengths
1. GravMAD shows strong generalization capabilities, achieving at least 13.36% higher success rates than state-of-the-art baselines on 12 base tasks encountered during training and surpassing them by 28.63% on 8 novel tasks.
  2. The manuscript is well-written with a clear structure, logical flow, detailed technical descriptions, and intuitive chart presentations.

### Weaknesses
- Insufficient argumentation
  1. The manuscript mentions in section 3.2 that different sub-goal keypose discovery rules were designed for different types of manipulation tasks, which seems to lack a reasonable explanation and generalizability.
  2. The manuscript does not adequately justify the exclusion of GravMap’s guidance in rotation prediction, stating that “rotation actions are difficult to be guided explicitly through value maps.”
- Inadequate Evaluation: 
  1.  Although it is claimed that this method is generalized, all experiments were conducted in the RLBench environment, and there is a lack of validation on other simulation environments or real robots.
  2. The main evaluation metric used is success rate, overlooking other important dimensions such as completion time, smoothness of action, etc.

### Questions
1. What are the specific criteria for “significant changes” in Sub-goal Keypose Discovery?
2. From Table 2, it is evident that the algorithm exhibits significant differences in performance on similar tasks, such as placing a cup and placing wine. Can you explain the reasons for this?

### Soundness
2

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
4

### Summary
This paper proposes a novel method for learning from demonstrations while incorporating knowledge from foundation models to tackle robotic manipulation. It learns to predict robot end-effector actions using a diffusion process and enhances the representation using 3D cost maps introduced in previous work. These cost maps are computed using heuristically extracted sub-goals during training, while foundation models are used instead at inference. In this way, the proposed method is able to combine strong generalisation capabilities from foundation models and learn precise robot actions from available demonstrations. The experiments show strong performance when compared to the considered baselines, while ablation studies provide valuable insights into different components of the method.

### Strengths
- The motivation of the paper is strong and well-explained.
- Figures (both in the main paper and the appendix) are clear and very helpful in understanding the proposed method.
- The technical challenge of integrating many components together in a unified framework is well-executed and appreciated.
- Ablation studies are well-executed and provide valuable insights into the method.
- Overall, utilising foundation models together with some demonstrations to achieve both, task generalisation and high precision seems like a great direction.

### Weaknesses
- Novelty and contribution claims are not very clear:
    - 1) Discovering sub-goals and predicting them to guide robot actions has been done before [1,2,3,4]. Is the novelty here mainly the 3D part combined with foundation models? Maybe the difference could be emphasised more.
    - 2) From the paper, it seems that GravMaps are Cost and Gripper openness maps used in VoxPoser, just renamed. Without properly explaining the difference, it shouldn’t be called a novel contribution.
    - 4) Claiming to design two types of tasks (line 124) and then using base tasks from RLBench for one type can come off as being disingenuous about the contribution claims. Rephrasing the 4th contribution to focus more on the evaluation rather than task design would be beneficial.
- Some parts of the method and design choices need to be better explained:
    - How GravMap tokens are used in the network architecture is not described in the main text of the paper.
    - Explaining in more detail why sub-goals are extracted differently during training and inference would greatly benefit the clarity of the paper. It becomes obvious while reading the paper, but initially, it can cause confusion.
    - It is not clear why rotation maps from VoxPoser are not used. Justifying it would make the overall approach clearer.
    - GravMap Synthesis during Inference is not explained clearly. Lines 305-309 are very dense with information, but it’s very difficult to understand how the sub-goals are actually extracted. If it is done just using existing methods, then contribution claims should be adjusted accordingly. 
- It is not clear if the proposed sub-goal keypose discovery is actually needed. There are no experiments using keyposes, without filtering them. If there are other reasons to filter keyposes, they should be explained.
- Overall, sub-goal keypose discovery seems very tailored towards specific types of tasks. Limitations of it (and how they could be lifted) are not discussed.
- What are 3 random seeds used for? Are the models re-trained using different seeds or just to change object poses and the stochastic diffusion process? If it’s the latter, then it is the same as having 3x episodes and the reported statistics don’t hold a lot of value.
- GravMAD (Manual) seems like an unfair comparison to the baselines. Maybe providing the same ground truth object pose information to other methods would be more valuable for such comparison.
- Given that the proposed method uses sub-goals to guide the diffusion process, selected baselines are not the most appropriate. Better baselines would be ChainedDiffuser [3] and/or Hierarchical Diffusion Policy [4].
- There are some contradictory and not complete claims in the paper:
    - Line 144 - Described methods already leverage demonstration data.
    - Line 205 - Quaternions, although they have the double cover property, are continuous unless additional restrictions are imposed (e.g. by requiring that the scalar part w≥0).
    - Line 206 stated that 6D rotation representation is used, but line 510 states that the model can predict non-unit quaternions. How is this possible?
    - What are “3D tasks”? Tasks that involve 3D observations or 6D manipulation? It is not a very clear term.
- Limitations of the proposed method are only superficially discussed.

[1] Black, Kevin, et al. "Zero-shot robotic manipulation with pretrained image-editing diffusion models." arXiv preprint arXiv:2310.10639 (2023).

[2] Kang, Xuhui, Wenqian Ye, and Yen-Ling Kuo. "Imagined subgoals for hierarchical goal-conditioned policies." CoRL 2023 Workshop on Learning Effective Abstractions for Planning (LEAP). 2023.

[3] Xian, Zhou, et al. "Chaineddiffuser: Unifying trajectory diffusion and keypose prediction for robotic manipulation." 7th Annual Conference on Robot Learning. 2023.

[4] Ma, Xiao, et al. "Hierarchical Diffusion Policy for Kinematics-Aware Multi-Task Robotic Manipulation." Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. 2024.

### Questions
- Some are raised in the Weaknesses section.
- What is the difference between GravMaps and the cost maps described in VoxPoser? Is it the downsampling part?
- Why are rotation maps from VoxPoser not used?
- Do you have any intuition on how well your proposed method would scale with more data? Would Imitation Learning catch up at some point (with a lot of training data)?
- Could you expand a bit more about the limitations of your proposed method?
- GravMaps are just an overparameterization of sub-goals at a high level. The fact that the ablation variant (w/o. GravMap) performs so poorly is not very intuitive. Could you provide more details about this ablation variant and maybe you have some intuition about its performance?

### Soundness
3

### Presentation
2

### Contribution
2
