# GRAM: Generalization in Deep RL with a Robust Adaptation Module

- Decision: Reject
- Scores: 6, 6, 6, 6

## Abstract
The reliable deployment of deep reinforcement learning in real-world settings requires the ability to generalize across a variety of conditions, including both in-distribution scenarios seen during training as well as novel out-of-distribution scenarios. In this work, we present a framework for dynamics generalization in deep reinforcement learning that unifies these two distinct types of generalization within a single architecture. We introduce a robust adaptation module that provides a mechanism for identifying and reacting to both in-distribution and out-of-distribution environment dynamics, along with a joint training pipeline that combines the goals of in-distribution adaptation and out-of-distribution robustness. Our algorithm GRAM achieves strong generalization performance across in-distribution and out-of-distribution scenarios upon deployment, which we demonstrate on a variety of realistic simulated locomotion tasks with a quadruped robot.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The authors propose a novel method (GRAM) to learn RL policies that exhibit both adaptive and robust behavior through a unified training pipeline, specifically in the context of deployment environments that vary in dynamics at test time. GRAM employs context-conditioned policies where the context is automatically learned through a history of past observations and actions. Crucially, when the history falls OOD or is unable to provide context point estimates, the learned context converges to a special null context vector, so that robust behavior is triggered.

### Strengths
- The manuscript is extremely well written and provides clear statements to understand the proposed method.
- The authors demonstrate a successful implementation of recently introduced Epistemic Neural Networks for a relevant and important open problem in robot learning (i.e. generalization over unobservable environment contexts)

### Weaknesses
 - Missing recent related works: the authors should consider citing and discussing recent works [1] and [2] as they present themselves as state-of-the-art methods in Robust RL and Domain Randomization as of 2024. Specifically, DORAEMON [2] tackles the same problem setting as in this work where privileged information is available at training time, and a history of previous observations and actions is used to allow implicit system identification at test time and promote adaptive behavior.

- Limited experimental evaluation:
  - While Domain Randomization is an extremely popular baseline for learning robust/adaptive behavior in sim2real settings, the authors provide little information to the implementation of this baseline and no comparison of GRAM vs. DR in fig. 4 and 5. The lack of detail makes it difficult to assess the validity of the comparison.
  - Implementation details of DR: I highly suggest the authors to compare GRAM against a DR baseline which also uses a history of previous state and actions, as this is the notorious way to implement DR [3]. Furthermore, DR may and should also leverage privileged information at training time, by using the notorious asymmetric actor-critic paradigm [2, 3, 4]. Conditioning the critic on the known context often drastically affects the results of DR methods vs. unprivileged critics, and does not require further assumptions. The current DR implementation seems underpowered and does not represent the state-of-the-art.
  - The analysis is carried out on locomotion environments only, and simulated environments only. The generalization problem under unobservable dynamics is likely exacerbated and more challenging for manipulation and contact-rich settings, which would make the experimental evaluation more significant and relevant. The lack of real-world experiments also limits the impact of the work.

### Questions
- Why is the performance of all baselines better in Fig. 3 (right) for the "Base ID + frozen joints" vs. the "Base ID" counterpart?

- Regarding the statement at the end of Sec. 5 "as the goal is to train the epinet in (5) to output estimates with low variance in ID contexts and high variance in OOD contexts.". Does GRAM promote the learned encoder to output high variance in OOD contexts at training time? Judging from Eq. (7) alone, it seems to me that the encoder is only trained to provide low variance on ID contexts, whereas a higher OOD variance is a spontaneous effect that occurs at test time only.

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
The paper develops an approach for generalization in reinforcement learning by tackling the problems of in-distribution generalization through contextual RL, and out-of-distribution generalization through robust RL. The authors develop a unified approach, called "Robust Adaptation Module" that relies of teacher-student training for tackling these challenges of generalization. The teacher policy is trained through RL in simulation by using privileged information of the environment that is not accessible at deployment. The student policy is trained to imitate rollouts from the teacher policy and leverage an adaptation module that predicts "context" from history of interactions. Experiments with a simulated quadruped robot in fixed velocity locomotion demonstrates the applicability of the approach in generalizing to different dynamics variations like mass and friction.

### Strengths
- The paper is interesting and the key ideas of adaptive RL and robust RL are easy to follow 

- To the best of my knowledge the robust adaptation module relying on context identification from history and epistemic uncertainty of the policy is novel in the context of generalization in RL. 

- The use of a teacher-student training paradigm is nice, and since the student doesn't require privileged information, the approach can be potentially scaled to real world tasks via sim2real. 

- The experiments are on a non-trivial simulated quadruped locomotion task and the generalization to dynamcis variations corresponds to a practical use-case in controls and robotics.

### Weaknesses
 - It is unclear how general is the proposed approach in dealing with different types of variations. The paper is motivated from the perspective of very generic generalization in RL but the experiments are limited to a single task/environment and correspond to only dynamics variations. What about variations in visual scenes? generalization to different tasks with the same robot?

- The in-distribution and out-of distribution generalization motivation is a bit confusing in the introduction. The authors should clarify scenarios where out-of-distribution generalization is possible without in-distribution generalization. The approach is based on the former not necessarily implying the latter and so this is important to motivate and explain with concrete examples.

- It is a bit confusing that context prediction module is only trained from on-policy data. Can't off-policy and generic offline data with the same robot/agent be used for learning this context prediction? This could potentially alleviate some of the challenges with out-of-distribution generalization as well and remove the need for the second part of the module.

- Some prior works that also do context prediction and demonstrate real-world quadruped locomotion through student-teaching training are not cited and discussed. For example the RMA paper below:

Kumar, Ashish, Zipeng Fu, Deepak Pathak, and Jitendra Malik. "Rma: Rapid motor adaptation for legged robots."

### Questions
Refer to the weaknesses above. 

- It is unclear how general is the proposed approach in dealing with different types of variations. What about variations in visual scenes? generalization to different tasks with the same robot?

- The in-distribution and out-of distribution generalization motivation is a bit confusing in the introduction. What are examples of scenarios where out-of-distribution generalization is possible without in-distribution generalization?

- It is a bit confusing that context prediction module is only trained from on-policy data. Can't off-policy and generic offline data with the same robot/agent be used for learning this context prediction?

### Soundness
3

### Presentation
2

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
This paper proposes a new method for robust in-context adaptation in reinforcement learning. To remedy the OOD context distribution in the inference, the GRAM method proposes to adapt the the latent vector with a pre-trained context encoder that estimate the uncertainty of the context and bias the latent context into a confident region (i.e., 0). Empirical results show that the adaptation yields robust performance w.r.t. other baselines in the frozen joint OOD test cases.

### Strengths
1. The method is simple, novel and easy to understand. It does not involve too much code change with vinilla in-context adaptation.
2. The empirical results is comprehensive in quadraped OOD generalization case, which is persuasive.

### Weaknesses
1. The paper does not consider other easy to implement baselines, e.g. domain invariance prediction, adding noise to the context, or use a larger replay buffer for the context encoder training. I think to show that this specific design is useful, one should also consider other easy-to-implement baselines.
2. GRAM biases towards 0, which is the mean at the beginning of the training. It is unclear if this is the best choice. How about bias toward the mean at the end of the training of the context encoder?

### Questions
See the two points in weakness.

### Soundness
3

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
3

### Summary
This paper introduces GRAM (Generalization in Deep RL with a Robust Adaptation Module), a deep RL framework designed to enhance generalization performance in both in-distribution (ID) and out-of-distribution (OOD) scenarios. GRAM aims to unify both generalizations within a single architecture.

The core of GRAM is the robust adaptation module. This module utilizes an epistemic neural network to estimate the current context and the uncertainty associated with that estimation.  This uncertainty measure allows the system to identify OOD situations.  When high uncertainty is detected, the module defaults to a pre-defined "robust" latent feature, triggering a robust control policy specifically trained for such scenarios. This module is trained by teacher-student distillation. A "teacher" policy is trained with access to contextual information, learning to adapt to different environments.  A "student" policy then learns to mimic the teacher's behavior based only on observed history, enabling deployment without needing explicit contextual data. 

GRAM's training pipeline also combines standard data collection for ID adaptation with adversarial training for OOD robustness.  An "adversary" agent introduces disturbances during training, forcing the robust policy to learn to handle unexpected perturbations. 

Experiments conducted on simulated quadruped robot locomotion tasks demonstrate GRAM's effectiveness.  Compared to traditional contextual and robust RL methods, GRAM achieves stronger performance in both ID and OOD environments.  It demonstrates adaptive behavior in familiar terrains while maintaining robust locomotion in challenging, unseen terrains like rough surfaces.  The experiments also confirm that GRAM effectively identifies OOD situations, automatically adjusting its behavior based on the uncertainty level of its context estimation.

### Strengths
- GRAM tackles an important challenge of generalization in deep RL by proposing a unified architecture that effectively combines adaptation and robustness. This is an important perspective as previous methods often focused on one at the expense of the other.

- The introduction of the robust adaptation module with its integrated epistemic neural network is a novel mechanism. It allows the system to not only adapt to different contexts but also quantify the uncertainty of its estimations, enabling switching between ID and OOD modes.

- The paper is well-written and easy to follow.

### Weaknesses
### Major

- The assumption underlying this paper is notably strong. While assuming access to context variable values within the simulation environment is reasonable, *assuming the knowledge of which parameters constitute the context is a strong assumption*. In their experiments, contexts include friction, added base mass, motor strength, and joint angle bias - effectively acknowledging a priori which parameters will vary in test environments. This raises the question: if these variation sources are known beforehand, why not just randomly sample these parameters from a wider range during training? The selection of these specific parameters as contexts, rather than others, implies a prior understanding of which factors are most relevant to the task, which is a form of domain knowledge that limits the generality of the approach.

- The adversary policy design similarly relies on prior knowledge. In their experiments, the adversary policy applies external forces to the robot's body. This is clearly tailored to address specific anticipated environmental variations. Such an adversary policy would be useless if the primary differences between training and test environments involved different factors, such as lighting conditions or camera poses. The effectiveness of the robust policy is therefore tied to the specific type of adversarial training used, which may not generalize to other types of perturbations.

- It seems the motivation of this paper is to deploy deep RL policies in real-world settings reliably (the 1st sentence in abstract). However, alll experiments are conducted in simulation.  While simulation allows for controlled experiments and extensive testing, demonstrating GRAM's effectiveness on real-world hardware is crucial for validating its practical applicability.  Real-world deployments often introduce unforeseen challenges that simulations may not fully capture.


### Minor

- The OOD experiments primarily focus on variations in terrain roughness and robot parameters. While relevant, exploring a wider range of OOD scenarios, such as unexpected obstacles or changes in task objectives, would provide a more comprehensive evaluation of GRAM's robustness.

- The paper mentions fine-tuning the parameters for the uncertainty hyperparameter ($\alpha_t$) but doesn't provide a detailed analysis of its sensitivity.  Understanding how different threshold values impact performance in various ID and OOD scenarios would be beneficial.



### Questions
- It is still unclear to me why the $z_{rob}$ is set to 0. Why should it output 0 for context embedding if uncertainty is high?

### Soundness
3

### Presentation
3

### Contribution
2
