# Predictive Inverse Dynamics Models are Scalable Learners for Robotic Manipulation

- Decision: Accept
- Avg Score: 7.50
- Scores: 8, 8, 8, 6

## Abstract
Current efforts to learn scalable policies in robotic manipulation primarily fall into two categories: one focuses on "action," which involves behavior cloning from extensive collections of robotic data, while the other emphasizes "vision," enhancing model generalization by pre-training representations or generative models, also referred to as world models, using large-scale visual datasets. This paper presents an end-to-end paradigm that predicts actions using inverse dynamics models conditioned on the robot's forecasted visual states, named Predictive Inverse Dynamics Models (PIDM). By closing the loop between vision and action, the end-to-end PIDM can be a better scalable action learner. In practice, we use Transformers to process both visual states and actions, naming the model Seer. It is initially pre-trained on large-scale robotic datasets, such as DROID, and can be adapted to real-world scenarios with a little fine-tuning data. Thanks to large-scale, end-to-end training and the continuous synergy between vision and action at each execution step, Seer significantly outperforms state-of-the-art methods across both simulation and real-world experiments. It achieves improvements of 13% on the LIBERO-LONG benchmark, 22% on CALVIN ABC-D, and 43% in real-world tasks. Notably, it demonstrates superior generalization for novel objects, lighting conditions, and environments under high-intensity disturbances. Code and models will be publicly available.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper introduces an end-to-end framework, Predictive Inverse Dynamics Models (PIDM), which predicts actions using inverse dynamics models conditioned on the robot’s forecasted visual states. By integrating vision and action in a closed-loop system, the end-to-end PIDM serves as a scalable and effective action learner. The approach demonstrates improved performance over state-of-the-art methods, both in simulations and on a real robot.

### Strengths
1. Thorough ablation studies and experiments that demonstrate the effectiveness of jointly predicting forward and inverse dynamics as a pre-training task for robot learning
2. Evaluation in both simulation and in real on the effectiveness of the method
3. Shows scalability of the proposed method by pre-training on DROID.

### Weaknesses
1. Learning inverse dynamics models from visual inputs has been explored in the past (i.e. [1,2]). It would be good to discuss these papers in the context of this paper. 
2. The paper shows scalability in the direction of pre-training and finetuning data. To fully demonstrate scalability, it would be good to demonstrate the scalability in the model capacity axis as well.
3. The current formulation of the model does not seem to take account of the history (past observations). This makes it challenging to extend to more complex environments where stronger task planning is needed.

### Questions
1. The joint prediction of inverse dynamics (actions) and forward dynamics (next observation) reminds me of RPT [1], where it performs random masking of action and latent representations of observations and pre-trained via mask reconstruction. The key difference between this approach and RPT is that RPT doesn’t predict exact forward dynamics due to the random mask pattern, so it can learn shortcuts by copying from other future frames. Is there some way to evaluate the importance of predicting forward dynamics? Specifically, for table 3(b): is it possible to pre-train with only inverse dynamics?
2. For finetuning the model, are all weights considered, or is LoRA applied to the model? It would be interesting to know how this method's performance scales with the amount of parameters used for fine-tuning. 

[1] Radosavovic, Ilija, Baifeng Shi, Letian Fu, Ken Goldberg, Trevor Darrell, and Jitendra Malik. "Robot learning with sensorimotor pre-training." In Conference on Robot Learning, pp. 683-693. PMLR, 2023.

[2] Hu, Edward J., Yelong Shen, Phillip Wallis, Zeyuan Allen-Zhu, Yuanzhi Li, Shean Wang, Lu Wang, and Weizhu Chen. "Lora: Low-rank adaptation of large language models." arXiv preprint arXiv:2106.09685 (2021).

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper proposes an end-to-end Predictive Inverse Dynamics Model (PIDM) paradigm, to integrate vision and robot actions in a closed loop for a scalable policy for robotic manipulation. They introduce the Seer model, designed to leverage visual, temporal, and action features for large-scale pretraining, effectively combining the advantages of vision and action in policy formulation. The model is structured around two key components: Conditional Visual Foresight and Inverse Dynamics Prediction.

In Conditional Visual Foresight, Seer generates future RGB image predictions conditioned on specified goals (such as language instructions or robot states) and recent observations (previous RGB images and robot states), allowing the robot to anticipate and guide its actions. The Inverse Dynamics Prediction module then takes two consecutive observations—the current state and the visually predicted future state—to infer the required action sequence to achieve the anticipated outcome. This allows Seer to dynamically adjust its actions based on updated visual predictions, maintaining adaptability and responsiveness.

They performed extensive experiments in simulations and the real world, demonstrating the generalization capabilities and robust performance of the proposed method, underscoring its potential in advancing scalable, closed-loop policy solutions for robotic manipulation.

### Strengths
- Effective Pre-training Objectives: The paper emphasizes the importance of pre-training the entire policy rather than just visual components, leading to significant performance improvements. The conditional visual foresight objective encourages the model to learn from the future, while the inverse dynamics prediction objective helps it understand the relationship between actions and their visual consequences.
- End-to-End Training: Both the visual prediction and inverse dynamics modules are trained together, enabling the model to effectively utilize visual, temporal, and action information from large datasets. Seer uses Transformers to process visual states and actions, making it scalable.
- Unidirectional Attention: The model uses a unidirectional attention mask in the Transformer encoder, allowing the action prediction module to integrate past and future information for better decision-making.
- Extensive Results: The paper provides extensive experimental results on both simulated and real-world benchmarks. Seer consistently outperforms state-of-the-art baselines on tasks involving long-horizon planning, generalization to unseen scenes, and robustness to disturbances.

### Weaknesses
 - Generalization across embodiment: While this paper proposes a generalizable ene-to-end pre-training paradigm for robotic manipulation policy, the proposed Seer model is pre-trained on the DROID [1] dataset, which only involves the Franka Panda robot. Training on the dataset across different embodiments such as Open-X [2] might improve generalization capability. Specifically, the lack of variation in robot morphology and kinematics during pre-training could limit the model's ability to adapt to robots with different degrees of freedom, joint configurations, or end-effector designs. This is a critical limitation, as real-world robotic applications often involve a variety of robot platforms.

- In the real-world evaluation, they selected dataset DROID, which contains demonstrations of Franka robots executing various tasks in diverse scenes. It is likely to overfit the dataset for policies for different tasks. The dataset's focus on a single robot type and a specific set of tasks might lead to a model that is highly specialized to those conditions, rather than a generalizable policy. This raises concerns about the model's ability to perform well in novel environments or with tasks that differ significantly from those in the DROID dataset.

[1] Khazatsky, Alexander, et al. "Droid: A large-scale in-the-wild robot manipulation dataset." arXiv preprint arXiv:2403.12945 (2024).

[2] O.-X. E. Collaboration, A. Padalkar, A. Pooley, A. Jain, A. Bewley, A. Herzog, A. Irpan, A. Khazatsky, A. Rai, A. Singh, et al., “Open x-embodiment: Robotic learning datasets and rt-x models,” arXiv preprint arXiv:2310.08864, 2023.

### Questions
- Generalization Across Embodiment: The model is pre-trained on the DROID dataset, limited to the Franka Panda robot. How does this impact its generalization to different robot types? Would you please discuss the possibility of training on a more diverse dataset, like Open-X, to improve adaptability?

- Real-World Evaluation: The real-world evaluation uses the DROID dataset, with only Franka robots in varied tasks. Is there a risk of overfitting, potentially limiting performance in broader tasks? Would you please discuss task generalization?

- Regarding the OpenVLA baseline, which specific checkpoint version was used? OpenVLA has multiple versions fine-tuned on LEBERO, and their performance varies across different tasks.

- Typo: Line 067 using Inverse Dynamics Models (IDM) conditioned on the robots’. There is an extra "'".

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
The paper presents an approach for end2end learning of action and image predictions for imitation learning - termed Predictive Inverse Dynamics Model. The authors present a Transformer architecture that takes in language, observation history, and robot state, and predicts both actions and images in tandem (the action predictions are conditioned on the image predictions). The authors conduct experiments in simulation (LIBERO and CALVIN) and on real-world tasks pretrained on DROID to showcase the benefits of the proposed pretraining approach.

### Strengths
Strengths:
* The general problem of learning action/image prediction models or world models is of interest to the community.
* The problem is well-motivated and the literature review does a good job of contextualizing the paper in prior work.
* The paper is strong, well-written and easy to follow.
* The figures are informative and effectively illustrate the benefits of the proposed approach.
* The experiments consider both simulation and real robot evaluation, as well as an ablation study, demonstrating the proposed method's superior performance as compared to the considered baselines.

### Weaknesses
 * The authors may consider adding the following relevant works to the literature review.
  * Gen2Act: Human Video Generation in Novel Scenarios enables Generalizable Robot Manipulation
  * This&That: Language-Gesture Controlled Video Generation for Robot Planning
  * VideoAgent: Self-Improving Video Generation
  * IGOR: Image-GOal Representations Atomic Control Units for Foundation Models in Embodied AI
* My biggest concern with the paper is the low number of experimental trials in certain settings (e.g., 20) and the lack of indication whether the results are statistically significant. At these lower trial numbers, it would not be unexpected that some of the performance difference is not statistically significant.
* In line 71, it is stated that this approach is the first to optimize vision and action prediction synergistically. However, does the GR-1 paper not do the same high-level goal?
* The limitations of the approach are missing from the paper.
* Line 267 - vanilla typo.

### Questions
1. Are the predicted actions at the same frequency as the prediction images? This point was confusing as the actions were referred to as intermediate actions throughout the paper.
2. How many frames of observation history are used as input? How many frames are predicted?
3. Did rolling a chunk of action predictions not work for inference (it seems like only one was rolled out)? Did you end up using a temporal ensemble? How many predictions were in the ensemble?

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
4

### Summary
This paper presents a unified approach to combine visual sub-goal prediction and action prediction into a single predictive inverse dynamics model (PIDM). 

1. The proposed framework achieves impressive results on LIBERO-LONG and Clavin, two long-horizon manipulation benchmarks. 
2. The proposed framework is pretrained on DROID datasets, which shows the potential scalability of PIDM. 
3. The authors also evaluate the proposed method with a real robot and conduct ablation studies on the contribution of pretraining, the choices of pre-training, and fine-tuning loss functions.

### Strengths
1. This work studied an important problem: improving the data scalability of robot manipulation policies. 
2. The idea makes sense. The proposed PIDM combines sub-goal prediction and action prediction. The former, as a vision task, is more generalizable and naturally benefits the latter task. The data efficiency study in Fig.3 is convincing. 
3. The results of CALVIN look very impressive. 
4. The writing is easy to follow.

### Weaknesses
1. The authors did not discuss the limitations of the proposed method at all, while there obviously are. For example, it could be difficult to apply this method in high-frequency control tasks, such as ALOHA. Moreover, the experiments focus on easy manipulation tasks that do not require rich contacts or high precision, such as insertion, screwing, etc.  A thorough discussion of limitations is necessary, especially given the claim that PIDM is a scalable policy.

2. The central idea is not novel. Bringing sub-goal prediction into manipulations has been recently explored by many existing works, such as [1][2][3], especially in the direction of using video generation models for robot tasks. 

3. The authors did not explain the network architectures clearly. Some descriptions are in the supplementary, but they are unclear, and there is no figure.

4. When comparing with existing work, the authors only report success rates (or alike), but not network sizes and MACs (number of multiply-additions). It becomes unclear whether the performance gain comes from a larger network or a better method.

### Questions
In addition to the weakness section: 

1. Could you compare SEER with the existing works that use sub-goal prediction? I am looking for a clear explanation of the essential differences in the method level. 

2. In Table 3, how does the finetuning/pretraining work if both the loss functions are not used? 

3. How much GPU resources are required during pre-training and fine-tuning? 

4. How are sub-goals selected when you prepare the training set? 

5. Does this framework work for tasks of more precision or contacts? This is the key issue of using video prediction models in robotics, as these methods sometimes lack the required precision when generating sub-goal videos.  CALVIN has long horizons but very simple manipulation tasks. The LIBERO also seems only have pick and drop, push and pull tasks on relatively large objects.

In general, I appreciate the quality of the idea and result of this work. I rate this paper a borderline accept at this moment, but I have many concerns. Please address them.

### Soundness
3

### Presentation
3

### Contribution
3
