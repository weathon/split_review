# Towards Off-Road Autonomous Driving via Planner Guided Policy Optimization

- Decision: Reject
- Avg Score: 4.00
- Scores: 6, 1, 3, 6

## Abstract
Off-road autonomous driving poses significant challenges such as navigating diverse terrains, avoiding obstacles, and maneuvering through ditches. Addressing these challenges requires effective planning and adaptability, making it a long-horizon planning and control problem. Traditional model-based control techniques like Model Predictive Path Integral (MPPI) require dense sampling and accurate modeling of the vehicle-terrain interaction, both of which are computationally expensive, making effective long-horizon planning in real-time intractable. Reinforcement learning (RL) methods operate without this limitation and are computationally cheaper at deployment. However, exploration in obstacle-dense and challenging terrains is difficult, and typical RL techniques struggle to navigate in these terrains. To alleviate the limitations of MPPI, we propose a hierarchical autonomy pipeline with a low-frequency high-level MPPI planner and a high-frequency low-level RL controller. To tackle RL's exploration challenge, we propose a teacher-student paradigm to learn an end-to-end RL policy, capable of real-time execution and traversal through challenging terrains. The teacher policy is trained using dense planning information from an MPPI planner while the student policy learns to navigate using visual inputs and sparse planning information. In this framework, we introduce a new policy gradient formulation that extends Proximal Policy Optimization (PPO), leveraging off-policy trajectories for teacher guidance and on-policy trajectories for student exploration. We demonstrate our performance in a realistic off-road simulator against various RL and imitation learning methods.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper presents an approach to learn policies for off-road autonomous driving on diverse and challenging terrains. The authors try to tackle the problems of model-based control (MPPI) only approaches and RL-only based approaches and combine the two methodologies to get a low-frequency high-level MPPI planner and a high-frequency low level RL controller. 

They extend the PPO (proximal policy optimization) algorithm to enhance targeted exploration. They introduce a teacher-student paradigm where the planning information is distilled from the teacher policy (trained using dense planning information from MPPI) and the student policy learns the off-road traversal. They call this extended algorithm Teacher Action Distillation Policy Optimization (TADPO). 

The paper compares this algorithm with other on-policy and off-policy algorithms using success rate, completion percentage and mean speed and the evaluation metrics. TADPO outperforms SOTA RL baselines methods in terms of learning to navigate in a diverse set of off-road terrains.

### Strengths
- The authors did a good elaborate comparison of why some of the existing algorithms (IL, vanilla PPO, on-policy, off-policy) might not be good for traversal in diverse terrains that helps in getting a good contrastive contribution of the presented work.

- The algorithm helps in improving the policy (in policy gradient methods) over other better state distributions (using the teacher demonstrated trajectories).

- The framework allows for faster and less frequent planning at the time of deployment.

- The paper designs the algorithm to make it capable of real-time execution.

### Weaknesses
 - The pipeline is not able to adapt to different domains, hence generalizability is a problem for now.

 - The work seems to be not ready for real-world deployment and is best suited for simulation based research.

 - The authors have presented why other IL methods, on-policy methods and off-policy methods might not perform well for off-road terrain considering the diverse scenarios; but it would be good to have some contrastive quantitative metrics to present how TADPO is trying to resolve those challenges, for example handling diverse scenes.

### Questions
- Nit: Line 141: There is no A_cap in equation 2.

- Nit: Line 704: β_{i} = (w^{0}_{i,t}, w^{1}_{i,t}) - here the second `w` can be made bold?

- Nit: Line 752: the symbols used to represent action space in this line are overloaded in the paper. Can we try to use something else here?

- Can we have any specific ablations or experiments to justify or get some research direction that the presented framework is not robust to domain shifts?

- Orthogonal direction: Can this hierarchical framework be applied to more structured observation spaces like unban autonomous driving environments and how good or bad can it be considering that this frame tries to alleviate the exploration problem in policy gradient methods and covariate shifts in imitation learning and other off-policy methods?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
1

### Rating Number
1

### Confidence
4

### Summary
In this paper, the authors consider a hierarchical framework of a sparse global MPPI planner and a dense local MPPI planner setting waypoints tracked by low-level RL control policies. As the dense local planner has high inference costs, the approach tries to amortize the computational costs. An objective called TADPO, which is a reformulated PPO object, distills the knowledge of a teacher, who has access to the dense planner, to a student, who has only access to the sparse planner. The empirical results show that the sparse MPPI planner combined with the low-level student policy performs significantly better than RL or IL methods learned from scratch.

### Strengths
- Novel Idea and Setup: The idea of distilling the teacher into the student via PPO is interesting and the problem of off-road driving seems to be challenging.

### Weaknesses
 - Correctness: The description of MPPI seems to be wrong, different to eq. (7), MPPI uses importance sampling to average between all sampled trajectories.
- Showing the stated claims: From my understanding the experiments in Table 1 do not validate the modified PPO objective over a simple BC loss. Apart from MPPI + Teacher and TADPO all other methods seem to not use the sparse MPPI planner during testing. Thus, in that sense, only the tracking formulation with the MPPI planner is validated, but not whether training the student requires the TADPO objective and a simple BC loss would not work.
- Missing related work (or even important baselines): A comparison to [1] would be interesting where MPPI is accelerated by rolling out trajectories with an RL policy. I think this idea should be compared to the algorithm presented in this work. Another direct competitor could be variants where the terminal value function is learned, thus significantly improving the convergence of MPPI [1, 5, 6].  Another research line very related to the objective presented in this work is guided policy search as defined in [2].  Also, a potentially important related paper could be [3] where a reference generated by a high-lvl MPC planner is tracked by a low level RL policy.
- Writing: The description and notation of the algorithm could be improved. It is unclear to me which dynamics model the authors are using for the sparse MPPI or the dense MPPI planner. Further, it was not completely clear, whether the baselines use the MPPI planner or not.

[1] Y. Qu et al, "RL-Driven MPPI: Accelerating Online Control Laws Calculation With Offline Policy," in IEEE Transactions on Intelligent Vehicles, vol. 9, no. 2, pp. 3605-3616, Feb. 2024.
[2] S. Levine and V. Koltun, "Guided Policy Search," in Proceedings of the 30th International Conference on Machine Learning, 2013.
[3] F. Jenelten et al, "DTC: Deep Tracking Control—A Unifying Approach to Model-Based Planning and Reinforcement Learning for Versatile and Robust Locomotion," arXiv preprint arXiv:2309.15462, Jan. 2024.
[5] N. A. Hansen, H. Su and X. Wang, "Temporal Difference Learning for Model Predictive Control," in Proceedings of the 39th International Conference on Machine Learning, 2022.
[6] K. Lowrey  et al, "Plan Online, Learn Offline: Efficient Learning and Exploration via Model-Based Control", in Proceedings of the 7th International Conference on Learning Representations, 2019.

### Questions
- Instead of greedily selecting the most cost-efficient trajectory, one could average via the importance sampling scores like in MPPI or use a Cross-Entropy Planner [4]. Do you think this would help the planner to converge more stably?

[4] M. Kobilarov, "Cross-entropy Motion Planning," The International Journal of Robotics Research, vol. 31, no. 7, pp. 855-871, 2012.

Overall:
- The paper would benefit from more clarity: One should state more clearly what the novel key algorithmic contributions are and why they offer an improvement over the related work mentioned above. I further think that a more detailed analysis of the altered PPO objective would significantly improve the paper!

Further Remarks:
- Notation in equation (1) does not make sense, on the right side the argmax returns a function, and on the left side, a probability density is evaluated.
- Are you using the generalised advantage estimator for PPO. In the Appendix there is a hyperparameter suggesting so, but from the notation in the main paper it was not clear to me !?
- The introduction is rather lengthy and would benefit from shortening.
- Figure 5 scaling is off. 
- On page 9, a formulation in the paragraph SAC+Teacher describes putting the trajectories into the replay buffer as being simplistic. However, it is not described whether this approach was used in the end. 
- In Figure 1, the proposed method is called MPPI + TADPO, whereas in Table 1, it is called TADPO. This could lead to potential confusion.
- In Appendix A.3.2 it should be a student policy, not a teacher policy.
- There are a lot of figures not cited in the text: Figure 2, 3 and 5.

### Soundness
1

### Presentation
1

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper proposes a hierarchical approach for off-road autonomous driving that combines model predictive path integral (MPPI) and reinforcement learning (RL). The high-level MPPI planning provides dense waypoints for exploration, while the low-level RL learns to navigate based on both visual and proprioceptive inputs. Extensive experiments in BeamNG simulations show the approach’s improved performance over several baseline RL and imitation learning methods especially in obstacle-dense, off-road terrains.

However, TADPO’s reliance on dense teacher guidance raises concerns about generalizability, particularly in dynamic or unfamiliar environments where such detailed waypoints may be unavailable. Additionally, while the model performs well in simulations, its adaptability to real-world conditions with diverse terrains, unpredictable weather, and lighting changes remains untested and uncertain. Broader comparisons with end-to-end DRL models could also help clarify the strengths and limitations of the hierarchical framework, especially for real-world applications.

### Strengths
The combination of high-level MPPI planning with a low-level RL controller creates an efficient approach for off-road autonomous driving.

The low latency of the RL controller allows for real-time decision-making, making the framework well-suited for off-road applications.

### Weaknesses
  **Generalization to Real-World Conditions**: This approach has shown strong performance in simulation, but its ability to generalize to real-world off-road environments with diverse terrains and unpredictable elements is unclear. Real-world variability, such as changes in weather, lighting, and unexpected obstacles, could significantly impact its effectiveness. Specifically, the simulation environment may not capture the complexities of real-world sensor noise, varying soil conditions (e.g., mud, sand, gravel), and the presence of vegetation that could occlude sensors or affect vehicle dynamics. The lack of robustness to these factors raises concerns about the practical applicability of the method.

  **Reliance on Dense Teacher Guidance**: The teacher-student setup assumes access to densely planned waypoints for training, which may not be feasible in all scenarios. This dependency could hinder generalizability, especially in dynamically changing or unknown environments. The requirement for dense waypoints from MPPI implies a need for a highly accurate model of the environment, which may not always be available or computationally feasible to obtain in real-time. This reliance on a precise model for generating the teacher signal limits the adaptability of the approach to situations where the environment is not well-defined or changes rapidly.

  **Exploration Limitations**: While TADPO leverages the MPPI teacher for exploration guidance, the DRL student policy may still face challenges with effective exploration in complex terrain. The end-to-end navigation policy has limited learning benefits from the MPPI teacher, making it unclear if the proposed method resolves the exploration limitations inherent to PPO. The method does not explicitly address how the student policy can learn to recover from situations where the teacher guidance is suboptimal or unavailable, such as when encountering novel obstacles or terrain features not present in the training data. This lack of explicit recovery mechanisms could limit the robustness of the approach.

### Questions
**Ensuring Safety in High-Risk Environments**: Since TADPO uses an end-to-end DRL approach, how does it ensure safe navigation, especially in challenging off-road conditions where mistakes could lead to accidents or costly damage? What specific measures are in place to guarantee safety throughout the process?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper presents a novel approach for off-road autonomous driving by integrating a Model Predictive Path Integral (MPPI) planner with a reinforcement learning (RL) controller. The authors propose a teacher-student framework to address exploration challenges in RL, utilizing a new policy gradient formulation called Teacher Action Distillation with Policy Optimization (TADPO) extended from Proximal Policy Optimization (PPO).

The contribution of this paper can be summarized as follows:

1. The authors combine MPPI and RL in a teacher-student framework to handle long-horizon planning and real-time execution in challenging terrains.

2. The authors extend Proximal Policy Optimization (PPO) with Teacher Action Distillation (TADPO) to leverage off-policy trajectories for better training efficiency.

3. The authors conduct experiments on an offroad driving simulator to demonstrate the advantage of their proposed method over other RL and imitation learning methods.

### Strengths
The strengths of the paper are twofold.

1. The integration of MPPI with RL in a teacher-student framework to tackle off-road driving challenges is innovative. The hierarchical framework is well-motivated and addresses key limitations of both techniques.

2. The experiments conducted in a realistic off-road simulator demonstrate the effectiveness of the proposed method compared to various baselines, highlighting its potential for real-world applications.

### Weaknesses
The weaknesses of the paper is as follows:

1. **Selection of Baseline Methods:** The selection of baseline methods is not comprehensive. The baselines consist solely of learning-based planning approaches, specifically imitation learning and reinforcement learning. As stated by Dauner et al. in their CoRL 2023 paper, *Parting with misconceptions about learning-based vehicle motion planning*, traditional planning methods often outperform many learning-based planning methods in on-road autonomous driving. This conclusion may also apply to off-road scenarios. Therefore, it would be beneficial to include one or two traditional planning methods as baselines, such as the MPPI algorithm mentioned in the paper, or other Model Predictive Control (MPC) algorithms or sampling-based motion planning techniques. The absence of these comparisons makes it difficult to assess the true performance gain of the proposed method against established techniques. For instance, a comparison with a well-tuned MPC controller, which can handle constraints and optimize for specific cost functions, would provide a more rigorous evaluation of the proposed method's strengths and weaknesses.

2. **Complexity Analysis:** A complexity analysis of the proposed method is necessary, as efficiency is one of the advantages claimed by the authors. Specifically, the paper should include the inference time of the proposed method and a comparison with the baseline methods to demonstrate that the authors' approach is capable of real-time planning and is more efficient than previous approaches. The paper lacks a detailed analysis of the computational cost associated with the proposed method. This includes the time required for policy evaluation, gradient computation, and action selection. Without this information, it is difficult to assess the practical applicability of the method, especially in real-time scenarios where computational resources are limited. Furthermore, a comparison of the computational complexity with the baseline methods is essential to support the claim that the proposed method is more efficient.

### Questions
In addition to the questions raised in the weaknesses, I have one more question regarding the rationale for choosing MPPI. Is MPPI the only state-of-the-art (SOTA) traditional planning method for off-road autonomous driving? If that is the case, it would be helpful for the authors to clarify this in the introduction. If there are other methods available, a brief review of existing SOTA traditional planning methods for off-road autonomous driving could provide valuable context, along with an explanation of why MPPI was chosen to be combined with reinforcement learning.

### Soundness
3

### Presentation
3

### Contribution
2
