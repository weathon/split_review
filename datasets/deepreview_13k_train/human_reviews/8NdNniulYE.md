# STAMP: Scalable Task- And Model-agnostic Collaborative Perception

- Decision: Accept
- Scores: 3, 8, 8, 6, 6

## Abstract
Perception is a crucial component of autonomous driving systems. However, single-agent setups often face limitations due to sensor constraints, especially under challenging conditions like severe occlusion, adverse weather, and long-range object detection. Multi-agent collaborative perception (CP) offers a promising solution that enables communication and information sharing between connected vehicles. Yet, the heterogeneity among agents—in terms of sensors, models, and tasks—significantly hinders effective and efficient cross-agent collaboration. To address these challenges, we propose STAMP, a scalable task- and model-agnostic collaborative perception framework tailored for heterogeneous agents. STAMP utilizes lightweight adapter-reverter pairs to transform Bird's Eye View (BEV) features between agent-specific domains and a shared protocol domain, facilitating efficient feature sharing and fusion while minimizing computational overhead. Moreover, our approach enhances scalability, preserves model security, and accommodates a diverse range of agents. Extensive experiments on both simulated (OPV2V) and real-world (V2V4Real) datasets demonstrate that STAMP achieves comparable or superior accuracy to state-of-the-art models with significantly reduced computational costs. As the first-of-its-kind task- and model-agnostic collaborative perception framework, STAMP aims to advance research in scalable and secure mobility systems, bringing us closer to Level 5 autonomy. Our project page is at \href{https://jocular-manatee-91cad0.netlify.app/}{https://jocular-manatee-91cad0.netlify.app} and the code is available at \href{https://anonymous.4open.science/r/STAMP-id}{https://anonymous.4open.science/r/STAMP}.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper presents a framework for collaborative perception that is argued to be salable, tasks-independent and model agnostic, which is also argued to be capable of dealing with heterogeneity in the agents and enhancing flexibility and security.

### Strengths
+ Heterogeneity in collaborative agents, especially in robotics outside of collaborative driving, is an important problem.

+ The proposed method is straightforward, and the writing is easy to follow.

### Weaknesses
 - Novelty is a key concern. The proposed method is based on BEV representations and performs intermediate fusion using the BEVs. Each component also uses or marginally extends existing methods, and the novelty of each component is not well justified. For example, Collaborative Feature Alignment (CFA) simply uses the BEV from each agent and projects it to a unified feature space.

- The paper argues that the proposed approach can address heterogeneity in the agents; however, the solution is simply based on the BEV representation that is assumed to be computed by each agent.

- Similarly, the claim that the proposed method is model-agnostic is also an overstatement, primarily due to its reliance on the BEV representation.

- Why is the proposed method secure? The method uses a set of neural networks, so how can we ensure that the use of these networks is secure?

- What is the coordinate frame of the BEV representation used by each vehicle? If the BEV is ego-centric for each vehicle, how can the correspondence of street objects between agents be found?

### Questions
See above.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper introduces STAMP (Scalable Task- and Model-Agnostic Collaborative Perception), a framework designed to enable efficient, secure, and scalable multi-agent collaborative perception (CP) in autonomous driving systems. Recognizing the challenges posed by heterogeneous agents—such as varying sensors, models, and tasks—STAMP employs lightweight adapter-reverter pairs to align Bird’s Eye View (BEV) features to a unified protocol, allowing agents to collaborate without sharing model details. The framework is validated on simulated (OPV2V) and real-world (V2V4Real) datasets.

### Strengths
1. STAMP initiates the first study of task-agnostic and model-agnostic collaborative perception, and verifies the effectiveness of the proposed method in connected and autonomous driving scenarios.

2. STAMP introduces a unique adapter-reverter mechanism to bridge heterogeneity gaps in multi-agent collaboration.

2. STAMP addresses a critical need in autonomous driving by enabling heterogeneous agents to collaborate effectively, setting a foundation for more secure, scalable CP frameworks applicable to various downstream tasks.

### Weaknesses
1. While the proposed method claims scalability, the experiments include only three agents, which limits the demonstration of scalability in larger, more complex multi-agent systems. The evaluation does not explore how performance degrades with increasing agent numbers or communication overhead, which are critical factors in real-world deployments.

2. Although the method is presented as task-agnostic, generalizing to untrained downstream tasks may prove challenging, suggesting that the adaptability across broader task domains could benefit from further validation. The paper lacks a clear definition of 'task-agnostic' and does not demonstrate how the learned feature representations can be effectively utilized for diverse, unseen tasks without significant retraining or fine-tuning of the adapter-reverter pairs.

3. The writing needs to be polished. The main paper contains numerous intricate details that might be better suited for the appendix, and the main figure contains redundant information that could be streamlined for clarity. The current presentation makes it difficult to quickly grasp the core contributions and technical novelty of the proposed approach.

4. The framework focuses on vehicle-to-vehicle communication, which may narrow its broader impact within the ICLR community. Expanding the scope or exploring applications outside autonomous driving could increase its relevance. The current scope limits the applicability of the framework to a specific domain, potentially overlooking broader applications of collaborative perception.

5. The paper could benefit from a more comprehensive literature review, as some highly relevant works on efficient and scalable collaborative perception are missing [1-7]. Including a broader range of recent studies would provide a stronger context for the contributions and better situate the proposed framework within the current state of research.

### Questions
Could the authors illustrate task-agnostic collaborative perception more (especially the difference compared to the prior work [1])? As this prior work can be trained without knowing downstream tasks. However, the proposed framework in this paper seems to be trained on some specific tasks and is hard to generalize to novel downstream tasks. The authors are suggested to illustrate the limitations and setups clearly.  

[1] Yiming Li, Juexiao Zhang, Dekun Ma, Yue Wang, and Chen Feng. Multi-robot scene completion: Towards task-agnostic collaborative perception. In Conference on Robot Learning, pp. 2062–2072. PMLR, 2023c. 3, 5

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This work focuses on collaborative perception for heterogeneous agents and proposes a task- & model- agnostic framework that is scalable, efficient & secure. The framework involves learning a shared latent representation space, referred to as the protocol feature, using BEV features from LiDAR input. For each agent, a learned local adapter and reverter modules are used to map the agent-specific BEV features to the protocol feature space and vice versa. The protocol feature space is learned jointly across agents and tasks, while the local adapters and reverters are trained separately. Since the protocol feature space is learned once and adapter-reverter modules are lightweight, the proposed framework is scalable and efficient. Moreover, using a shared feature space prevents the need to share information about modalities & models from different agents, thus improving security. Extensive experiments on OPV2V and V2V4Real datasets show the effectiveness of the proposed framework in various scenarios.

### Strengths
- This work studies collaborative perception for heterogeneous agents and focuses on efficiency, scalability & security, which is important from a practical perspective.
- The shared latent representation space only needs to be learned once and the adapter-reverter modules are lightweight (~1MB), thereby reducing computational overhead (7.2x saving) and improving efficiency.
- Using a shared feature space avoids sharing information about the sensors, models & tasks, making it task-& model-agnostic and secure.
- The ideas are intuitive and the paper is well written & easy to follow.
- Experiments in both simulated (OPV2V) and real (V2V4Real) scenarios show the effectiveness of the proposed framework over several baselines in terms of detection performance (Tab.2,3), scalability (Fig.2), efficiency (Fig.2), better robustness to noise (Tab.1), being task-agnostic (Tab.4) & model-agnostic (Tab.4).
- Ablation study on different architectural components (Fig.3,4) and visualization of features & outputs (Fig.5) help to the capabilities of the proposed framework.

### Weaknesses
 - The protocol feature space is learned using BEV features from LiDAR data. Is there a way to extend this to incorporate other modalities like RGB as well since dense semantic features from RGB complement sparse geometric features from LiDAR. It would also enhance the modality-agnostic aspect of the proposed framework and might scale better to real-world datasets.
- In the current experiments, the model- and task- agnostic setting is considered on the simulated OPV2V dataset. Is there any reason why this cannot be extended to real-world datasets like nuScenes? This would be helpful to verify if the trends hold on real-world datasets as well. This is not required for rebuttal but additional clarifications would be helpful.
- For multi-group collaborative systems, it seems like the agents might need to share extra information to form groups, e.g. which is the weaker modality. This might affect the modality agnostic or security aspects of the proposed framework. It'd be useful to provide some more insights into this.

### Questions
Some aspects need clarification, which are mentioned in the Weaknesses above.

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
4

### Summary
The manuscript proposed a collaborative perception framework for heterogeneous agents, highlighting its feature of task- and model-agnostic. The framework contains a lightweight adapter-reverter pair, transforming the features between agent-specific domains and a shared protocol domain. The framework is tested on both simulated(OPV2V) and real-world (V2V4Real) datasets.

### Strengths
1. The idea of using an adapter-reverter pair in collaborative perception system for heterogeneous agents is intuitive. The design of the adapter & reverter is light-weight and does support solving most of the issue caused by heterogeneous encoders, such as resolution feature dimension. 

2. The experimental results validate the effectiveness of the framework and prove it is task- and model-agnostic. More surprisingly, the training efficiency is significantly higher than the existing methods.

3. The manuscript organizes very well and the visualization is clear and easy to understand.

### Weaknesses
In the methodology section, the authors propose using the L2 norm as the training loss to align the agent-specific features with the protocol features. However, to fully understand this approach, more information on the architecture and capability of the protocol model is needed. Knowledge-distillation designs like this can sometimes risk alignment failure if there is a significant capability gap between the models. This may also explain the limitation noted in A.3, where the system performance is constrained by the weakest agent. 

This reviewer is concerned that this may pose a drawback, as finding a suitable protocol model that meets the requirements of various modern encoders could be challenging. To address this concern, it would be helpful if the authors can provide more details about criteria of the protocol model selection, the current protocol model architecture, model size and its capabilities like task performances, as well as the comparison with those of the agent models.

### Questions
1. Following the weakness section, have authors considered the risk of alignment failure when there are significant capability differences between models? How do you pick the protocol model to maintain the robustness of the framework?

2. Another follow-up to the weaknesses section, this reviewer noticed that, in the experimental setup, all encoders are CNN-based. Has the author tried different combinations of protocol models and agent encoders, such as using a transformer-based protocol model while allowing agents to have either CNN-based or transformer-based encoders or other combinations.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper proposes STAMP, a task- and model-agnostic collaborative perception framework. The core idea is to first obtain a protocol BEV feature space, then align other local models' BEV features to this space using a simple DNN projection to achieve model agnosticism. A simple DNN is also used to map the aligned BEV features to a specific decoder and task head, achieving task agnosticism. Finally, experiments were conducted on OPV2V and V2V4Real.

### Strengths
1. This paper proposed a task- and modal-agnostic CP framework, which is new and the first work to address heterogeneous modalities, heterogeneous model architectures or parameters, and heterogeneous downstream tasks simultaneously.
2. The writing is good and fluent.

### Weaknesses
1. On line 227, the authors claim that the protocol model is not limited to any specific architecture or downstream task, making it a task- and model-agnostic framework. However, I disagree. The framework is task- and model-agnostic because it allows newly added agents to use different models or tasks, rather than due to the flexibility of the protocol model itself.
2. I think the author should compare more baseline methods, such as HM-ViT, DiscoNet, V2VNet, V2X-ViT, Where2comm, When2com, and What2com, not just compare with HEAL. I know your idea comes from HEAL, but comparing with other methods is necessary.
3. In Tab.2 and 3, I observe that STAMP achieves the best performance. However, I have some concerns about E2E training. The E2E training supposes to be the best, since it has the entire parameters to adapt the domain gap, which STAMP just use two projection DNN to adapt the features between different modalities and models, which is not make sense.
4. In Tab. 4, I find that the STAMP just has very little improvement even degradation. I don’t think there is much significance. 
5. On line 52, the authors claim that this framework is robust against malicious agent attacks. However, they haven't proven this or conducted even a single experiment to support it. Moreover, I believe this claim is questionable. Although an attacker might not know the other agents' models, they could still inject malicious information into the protocol BEV features to attack the ego vehicle.

### Questions
1. In experiment, why use AP@30 and AP@50 rather than AP@50 and AP@70? I think AP@30 is not usually used in detection task.
2. Why not conduct experiments about the communication efficiency.
3. Since the task is different, how to align the decision space with different tasks (GT) in Sec. 3.3
4. For the feature space alignment, I don’t think it always works, some times it may has negative influence, because the BEV feature distribution is different across different agent. From Figure 5, we can see that the styles of different agents’ feature are not the same. As a result, just simply forcing the features to be same is not a good idea.
5. The current trend in autonomous driving models is towards increasing model size and vehicle computational power. Additionally, there is a shift towards end-to-end models, significantly enhancing the autonomous capabilities of individual vehicles. Given these advancements, how much market potential remains for multi-vehicle cooperative perception based on intermediate BEV feature communication? How does the author view this issue?

### Soundness
3

### Presentation
3

### Contribution
2
