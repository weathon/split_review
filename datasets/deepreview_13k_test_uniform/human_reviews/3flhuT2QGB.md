# Towards Synergistic, Generalized, and Efficient Dual-System for Robotic Manipulation

- Decision: Reject
- Scores: 6, 6, 3, 6

## Abstract
The increasing demand for versatile robotic systems to operate in diverse and dynamic environments has emphasized the importance of a generalist policy, which leverages a large cross-embodiment data corpus to facilitate broad adaptability and high-level reasoning. 
However, the generalist would struggle with inefficient inference and cost-expensive training. 
The specialist policy, instead, is curated for specific domain data and excels at task-level precision with efficiency. Yet, it lacks the generalization capacity for a wide range of applications. 
Inspired by these observations, we introduce \modelname, a synergistic dual-system that supplements the merits of both generalist and specialist policy. 
A diffusion transformer-based specialist is devised for multi-step action rollouts, exquisitely conditioned on the high-level task understanding and discretized action output of a vision-language-action (VLA) based generalist. 
Compared to OpenVLA, \modelname achieves 26.7\% improvement in real-world setting and 12\% gain on CALVIN by introducing a specialist policy with merely 20M trainable parameters. It maintains strong performance with  5\% of demonstration data only, and enables a 3.8$\times$ higher control frequency in real-world deployment. Code would be made publicly available. Our project page is hosted at~\url{https://opendrivelab.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper investigates a pertinent question in imitation learning: how to combine the generalization capability of models like OpenVLA with the accuracy and task-specific precision of methods such as ACT or Diffusion Policy. To address this, the authors propose a novel framework, RoboDual, which uses the intermediate tokens in OpenVLA to condition a modified Diffusion Policy. Through simulation and real-world experiments, the proposed method demonstrates substantial performance improvements over both generalist and specialist baselines.

### Strengths
- **Effective Synergy**: The RoboDual framework innovatively combines a generalist and specialist model, leveraging OpenVLA’s generalization and Diffusion Policy's efficiency. This approach addresses a gap in imitation learning by merging generalist adaptability with specialist precision.
- **Experimental Results**: Both simulation and real-world experiments show significant performance gains over state-of-the-art baselines in generalization and task-specific adaptation, highlighting RoboDual's potential in practical settings.
- **Well-Written and Accessible**: The paper is clear, well-organized, and easy to understand, making the novel approach and its implications accessible.
- **Open-Source Commitment**: The authors promise to release the code, which could foster further research and replication.

### Weaknesses
1. **Limited Real-World Experiments on Generalization** Although the framework shows promise, its real-world experiments, particularly those evaluating generalization capabilities, remain limited. Conducting additional experiments—such as testing with a wider variety of novel objects (beyond just banana to eggplant), introducing more distractors at varied locations, using diverse language instruction templates, varying lighting conditions, or providing more detailed descriptions of the existing experiments—would significantly bolster the case for RoboDual’s practical applicability.

2. **Insufficient Introduction to the CALVIN Dataset** Including illustrative images in Section 4.2 to showcase the training and test settings of the CALVIN dataset would enhance readers' understanding of the experiment RoboDual run in simulation.

3. **Improved Color Differentiation in Bar Charts** The colors representing Octo, OpenVLA, and Ours (single/multi) in the bar figures are difficult to distinguish. Selecting more visually distinct colors would improve clarity and make comparisons easier.

4. **Failure Analysis** It is hard to tell which part is the bottleneck for the current method. A failure analysis will be helpful.

### Questions
### Questions
1. From the current experiments, this method does not seem to solve problems beyond what Robot-Moo or RoboPoint achieve. Any thoughts on how this method could outperform approaches based on explicit representations like bounding boxes or points?
2. It would be easier to understand if the conditioning feature were illustrated in Figure 2.
3. The authors claim that OpenVLA and Octo serve as generalist models, but they do not generalize effectively in all cases. For instance, the OpenVLA paper mentions challenges with out-of-distribution (OOD) cases, reflective surfaces, unseen action spaces, and actions along the depth axis. Given this, OpenVLA may not be an ideal generalist. Does this imply that RoboDual’s generalization is limited by OpenVLA’s capabilities?
4. In Figure 3, OpenVLA outperforms RoboDual in the "Knock down object" task. Can the authors explain why this is the case?
5. Additional real-world experiments on generalization ability would be beneficial. Including a baseline setting where Diffusion Policy/OpenVLA performs reasonably well would also help clarify RoboDual's improvements, given the claim that OpenVLA mainly provides generalization ability in this setup.
6. Perhaps I missed it, but is the Diffusion Policy baselines in your experiments the modified versions (specialist only), or the originals? This distinction is important, as a significant improvement from switching the transformer backbone to DiT may impact the novelty.
7. Is the OpenVLA in your experiments the same model used as the generalist in RoboDual (generalist only)?

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
3

### Summary
This paper introduces a new method for solving language-conditioned, robotic manipulation tasks.  The proposed method, RoboDual, combines an vision-language-action (VLA) model for high-level task understanding and long-horizon reasoning with a low-level policy to handle spatial reasoning and precise movements.  The two models are integrated together by passing discretized action predictions and latent representations from the generalist model to the specialist model.  A key benefit of their approach is the ability to run at higher control frequencies (20Hz), which is necessary for many dynamic manipulation skills, since they do not rely on the generalist to make predictions at every time step.  RoboDual is evaluated on a suite of challenging manipulation tasks in simulation and the real-world, where it outperforms all baselines in terms of success rate and shows strong robustness to across task variations.  RoboDual also outperforms baselines even in settings where the amount of data is significantly reduced.

### Strengths
- The paper proposes a scheme for combining a generalist VLA model with a specialist low-level policy model, via conditioning on latent representations and discretized actions.  This approach relies on the low-level policy to process non-vision-language inputs (like depth, proprioceptive, or tactile info), so the VLA does not need to be fine-tuned extensively.
- RoboDual can be trained much faster than a fully generalist approach, since the action predictions of an under-trained VLA model are refined by the specialist model that trains quickly.
- The experiments in Section 4.4 show that RoboDual is very sample efficient, achieving 73.3% success rate at 5 demos on real-world tasks.  This indicates that the coarse action predictions of the generalist are helpful and enable the specialist to refine the actions with limited data.-
- RoboDual can be run at 15Hz at inference, compared to 4Hz for openVLA.  This difference is significant, since jumpy movements of the robot prevent it from solving tasks that require precision.

### Weaknesses
- The ablation study needs some work.  Please switch to a different color map so that it is easier to distinguish the bars and read the legend.   The axis range makes it look like the ablations have a substantial impact on model performance, even though the difference in performance is minimal.  There should be error bars, otherwise it is difficult to determine whether a 0.03 increase in average time is significant.  The discussion of these results should also be changed to better reflect the actual results.  For instance, it is not true that "each conditioning source from the generalist model plays an **essential** role in ... enhancing overall performance" [emphasis mine] if removing the conditioning decreases average length by at most 4%.   
- There are some instances where the wording could be improved.   In Figure 1 caption: "the fast specialist policy *obsesses* ..." (achieves?). Top of page 2, "The *yielding* policy" (The resulting policy).  Bottom of page 2, "We bring in a novel approach" (We introduce? a novel approach).  Beginning of Section 3.3, "Disparate from" (Unlike?).
- The first contribution says, "Our methodology ... paves the way for the practical application of VLA models".  This is quite a broad claim.  I believe you are hinting at the computational efficiency of the dual-system.  Perhaps modify this to say "practical application of VLA models to higher-frequency control tasks".

### Questions
- In Table 3, it is interesting that transferring to an unseen background (checkered to solid-white tablecloth) results in 30% or greater drop in performance for all models.  Do you have a hypothesis for why this is the case?  One would expect the generalist models and RoboDual to be more robust to background texture.  
- What was the reason for choosing joint space control over end-effector control?
- In Section 3.3, it says that the specialist model is trained for "one hour" but in Section 4.4 it says "one hour of training on a node equipped with eight A100 GPUs".  Is this the same "one hour"?  If so, updating Section 3.3 to "8 gpu-hours" would be more accurate.
- It seems that fine-tuning the generalist policy to predict discretized actions in a specific robot's action space makes it no longer "generalist".  Have you thought of other ways to condition the low-level policy that might allow one to deploy the system on different robot types?

Typos: Figure 6a legend: (w/o Action L**e**tent).

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper introduces RoboDual, a dual-system framework combining generalist and specialist policies for robotic manipulation. RoboDual leverages both i) a generalist’s broad generalization capabilities with ii) a specialist’s task-specific precision and efficiency. The generalist is a large-scale pretrained vision-language-action model which provides high-level guidance, while the specialist is a diffusion policy which facilitates rapid, precise control.

### Strengths
1. Combining a high-level generalist and a low-level specialist model is a compelling paradigm to enable broader generalization while maintaining more fine-grained control.

2. RoboDual achieves higher performance with fewer demonstrations and limited computational requirements.

### Weaknesses
1. A bi-level policy increases model complexity and therefore inference time, which may affect performance in low-latency tasks.

### Questions
1. How does the performance vary with different sensory input combinations, and could simpler setups still achieve competitive results while offering advantages in runtime efficiency?

2. How well does RoboDual perform in more dynamic or even user-interactive settings (e.g. moving an object while a trajectory is being executed)?

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
To enable efficient fine-tuning and inference of VLA models, while not compromising generalisability, the article presents RoboDual, a dual-system approach that combines generalist and specialist policies to enhance robotic performance in dynamic environments. The generalist offers adaptability, while the specialist ensures efficient task execution. This synergy results in significant improvements in both real-world and benchmark tasks, offering strong performance with minimal data and higher control efficiency.

### Strengths
- The figures in the paper are thoughtfully designed and highly informative, significantly aiding readers in understanding the proposed methods and results.

- The dual-system approach aligns well with principles from cognitive science, making its application to embodied manipulation both insightful and innovative. Implementing this concept in robotics is a valuable contribution to the field.

- The extensive experimental results provide strong evidence of the model's advantages in achieving generalizable real-world manipulation. *RoboDual* outperforms both generalist and specialist-only models, demonstrating superior training and data efficiency, which highlights its practical value for broader real-world applications.

### Weaknesses
- When considering the system from another perspective: viewing the generalist as a vision-language model (VLM) and the specialist model as an action head, RoboDual can be seen as an asynchronous variant of Octo (Ghosh et al., 2024). This diminishes the novelty of the proposed approach, as the heterogeneity between the two systems mainly lies in the data and model scale, which impacts generalizability. It raises the question of whether scaling up the training data for the specialist model might yield comparable performance to the RoboDual system in terms of both computational efficiency and generalizability. Given that DiT is a scalable architecture, and considering the limited dataset used for experiments in Figure 5 (CALVIN), it would be valuable to explore this.


    One way to better distinguish these two systems is to draw more deeply on cognitive science concepts, such as viewing one system as responsible for reasoning (akin to System 1) and the other for actuation (akin to System 2). For example, in a task like "write down the answer of 1 + 1 on the blackboard," the reasoning required to determine the answer is challenging for the specialist system alone. Highlighting such distinct roles could provide a more fundamental differentiation between the two systems.

> Dibya Ghosh, Homer Walke, Karl Pertsch, Kevin Black, Oier Mees, Sudeep Dasari, Joey Hejna, Tobias Kreiman, Charles Xu, et al. Octo: An open-source generalist robot policy. arXiv preprint arXiv:2405.12213, 2024.

- The experiments on training efficiency could be improved. The use of DistillBERT might not be sufficient for capturing the semantics of actions and target objects from language instructions. I would suggest adding two additional baselines:

    1. Using T5 to encode language for the specialist-only model to ensure sufficient semantic extraction. Since language encoding is performed once per rollout, T5-xxl might be a suitable choice.

    2. GPU hours may not be the best metric for measuring efficiency, as it does not account for the number of parameters. I recommend switching the x-axis metric to FLOPs for a more accurate representation of computational efficiency.

### Questions
- **Line 26**: Could you clarify why "with" is italicized?

- **Line 268**: The description of the shifted-window conditioning mechanism is somewhat unclear. Why are only $k_g - \tau_s$ generalist actions sampled as conditioning rather than using the entire chunk of $k_g$ actions?

- **Line 197**: There appears to be a duplicated closing parenthesis in ")), \etc". Could you confirm if this is an error?

- In the experiment described in Figure 5, is the generalist model in the dual approach frozen? If it is frozen, are the weights solely from OpenVLA, or has it been further fine-tuned on CALVIN?

- Is the VLA model strictly necessary as the generalist model? If a vision-language model (VLM) were used to extract conditions instead, would this achieve comparable performance to RoboDual?

### Soundness
3

### Presentation
2

### Contribution
3
