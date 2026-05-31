## Human Reviewer 1

### Summary
The paper presents Contact-VLA, a novel framework for zero-shot planning and control in contact-rich manipulation tasks. It integrates Vision-Language-Action (VLA) systems with a reactive motion controller, leveraging Large Language Models (LLMs) for high-level planning, strategy formulation, and online adaptation. The core idea is to combine the broad understanding of VLAs/LLMs with the precision and robustness of reactive control for dynamic, contact-heavy robotic interactions. The authors claim that Contact-VLA significantly outperforms prior state-of-the-art methods on various manipulation tasks, validated through experimental comparisons, ablation studies, and robustness analysis. The framework's ability to perform zero-shot tasks and recover from failures is a key contribution.

### Strengths
1.  The paper addresses a significant challenge in robotics by proposing a unified framework that combines the semantic understanding of LLMs/VLAs with the fine-grained control needed for contact-rich manipulation. The framework demonstrates promising zero-shot planning and control, reducing the need for extensive task-specific data and potentially enabling rapid deployment in new scenarios.
2. The inclusion of mechanisms for online adaptation and LLM-driven failure analysis and refinement (e.g., modifying cost functions, adjusting penalties) significantly enhances the system's robustness to uncertainties and unexpected events during execution.
3. The comparative results against state-of-the-art baselines (e.g., OpenVLA-OFT on the LIBERO benchmark) show a clear performance advantage for Contact-VLA in terms of success rate and completion time. The ablation studies provide insights into the contributions of key components, such as the LLM-guided contact strategy, which helps validate design choices.

### Weaknesses
1. The paper acknowledges computational latency as a limitation. While a common issue, more discussion on specific strategies to mitigate this for real-time robotic applications, beyond general statements, would be beneficial.
2. The reliance on LLMs for strategy formulation, while enabling zero-shot capabilities, raises questions about the consistency, optimality, and safety guarantees of these generated strategies across a truly diverse and potentially adversarial set of contact scenarios.
3. The effectiveness of the reactive control and adaptation hinges on an accurate internal world model and physical parameter estimation. More details on how these are learned, maintained, and their potential failure modes would strengthen the paper.

### Questions
1. Could the authors provide more specifics on the prompt engineering or fine-tuning techniques used to guide the LLM for generating cost functions, refining strategies, and performing failure analysis? How sensitive is the system to variations in these prompts?
2. What is the end-to-end latency of the Contact-VLA system, from visual input to motor commands, particularly when the LLM is involved in an online adaptation or failure recovery loop?
3. Are there any formal guarantees or theoretical bounds on the stability and safety of the reactive controller when its parameters and objectives are dynamically modulated by an LLM?
4. How does Contact-VLA handle situations where the LLM's generated strategy is suboptimal, unsafe, or leads to unexpected physical interactions not covered by its training data?
5. Can the authors elaborate on the Internal World Model and Physical Parameter Estimation? How are these models learned, updated, and how robust are they to novel object properties or environmental changes?
6. What is the current compute cost (e.g., GPU hours, energy consumption) for training and deploying Contact-VLA, especially considering the LLM components?
7. Beyond the tasks presented, what are the current limitations of Contact-VLA in terms of object complexity, number of contact points, or task duration?
8. Can the authors provide specific examples of how Contact-VLA offers improved explainability compared to other end-to-end learning systems for manipulation?

### Soundness
2

### Presentation
3

### Contribution
2

### Rating
2

### Confidence
4

---

## Human Reviewer 2

### Summary
The method has not been evaluated on a real-world robotic platform, which undermines the claims regarding contact-rich manipulation, as simulators often struggle to accurately model physical contact dynamics.

### Strengths
The authors address the problem of explainability in VLA systems, which is a highly relevant topic for the research community. The proposed method demonstrates superior performance compared to baseline approaches on the evaluated tasks. Furthermore, the authors provide the implementation code.

### Weaknesses
The paper exceeds the 9-page limit and, in accordance with the ICLR submission guidelines, should therefore be desk rejected. It also contains several formatting issues, most notably in Figure 3. Furthermore, the plan component in *Equation (1)* is not clearly defined.

The method has not been evaluated on a real-world robotic platform, which undermines the claims regarding contact-rich manipulation, as simulators often struggle to accurately model physical contact dynamics.

Beyond the separation of the VLA into distinct vision and language modules and the introduction of a Memory Unit, the novelty of the contribution appears limited.

### Questions
See Weaknesses.

### Soundness
2

### Presentation
1

### Contribution
2

### Rating
2

### Confidence
2

---

## Human Reviewer 3

### Summary
The paper proposes a method for contact-rich manipulation by leveraging foundation vision models and large language models in a zero-shot manner. Specifically, given a task, the method first uses LLMs to propose contact plans and cost functions, which are then used for planning with MPPI. To model environment dynamics, physical parameters are initially estimated by the LLM and subsequently updated during plan execution. Based on the rollouts, both the plans and physical parameters are iteratively refined until the task is completed. Experiments demonstrate the effectiveness of the method on six manipulation tasks in the LIBERO environment.

### Strengths
1. The paper is easy to read. 
2. The idea of using LLM to write cost functions for MPPI is interesting. 
3. Experiments have shown the effectiveness of each module.

### Weaknesses
1. The tasks considered are very simple, only covering short-horizon basic manipulation (pushing / grasping / pivoting) of simple shapes, and it seems the method assumes access to a list of motion primitives, instead of directly doing joint position / torque control. This further simplifies the problem.
2. The authors assume that all the objects considered have known geometry. This is a strong assumption and greatly limits the generalizability of the method. How can the method generalize to unknown objects or non-rigid objects?
3. The applicability of the physical parameter estimation part is questionable. The authors assume that only 2 values — mass and friction — of a single object need to be estimated. This is another strong assumption: the difficulty of physical parameter estimation grows combinatorially with number of objects or degrees of freedom. Even for the simple case discussed in the paper, there seem to be no physical parameter variations for each task. This does not systematically show the effectiveness of the module. On the other hand, in the real world, online adaptation might be infeasible for hard-to-reset or safety-critical scenarios. 

Overall, the method relies on several strong assumptions about the task and environment, but the tasks demonstrated are still relatively simple. Thus I believe it is not meeting the bar of the venue.

### Questions
1. In Section 3.2, where do the successful experience episodes come from?
2. What is the prompt for generating the initial cost function and contact strategy?
3. How are the baseline models finetuned on the LIBERO dataset before testing?
4. What is the action space MPPI works on? From the provided code implementation, it seems the method assumes a list of motion primitives to be given for each task. How are they constructed?

### Soundness
2

### Presentation
2

### Contribution
2

### Rating
2

### Confidence
3

---

## Human Reviewer 4

### Summary
This work proposes a modular robotic system built with a combination of LLMs, VLMs, pose estimators and motion planners for manipulation task. Unlike what title may imply (VLAs), the modular system does not require demonstrations for imitation learning. Instead, it first uses perception modules such as FoundationPose to estimate poses of the objects and use VLMs for physical parameter specification, which get converted into a physics-based model (the simulator). LLM is used to provide/refine task-specific cost functions. Leveraging the model and the inferred cost functions, an MPC algorithm (MPPI) is used to generate robot actions. The proposed method is evaluated in Robosuite and compared against the OpenVLA and pi-0.5 baselines. Ablation experiments are also done to highlight the importance of the various components of the method.

### Strengths
- Leveraging the knowledge of foundation models in a reactive MPC formulation is an interesting and promising direction that bypasses the requirement for extensive demonstration data compared to imitation learning based approaches.
- The tasks demonstrated in this work, albeit in simulation, involve contact-rich interactions which are impressive to achieve without task-specific demonstrations.

### Weaknesses
- The term “real world” or “physical world” are mentioned several places in the paper. However, this is an incorrect claim as experiments are only done in simulation. This is particularly relevant in the context of this work, where high fidelity model is often required for such contact-rich reasoning, which often induces a notable gap between simulation and the real world (for both real2sim reconstruction and sim2real transfer). While it is fine to only demonstrate simulation results and state its limitations, leaving the incorrect impression that the proposed method works in the real world is certainly a over claim.
- Additionally, the method is named as “Contact-VLA”, which is also inaccurate. VLAs typically refer to end-to-end models finetuned from VLMs to directly produce actions. However, in this work, it is a modular approach that leverages a combination of VLMs and LLMs. As a result, it would also easily lead to incorrect expectation of the work.
- Since the approach involves using MPPI for planning and is demonstrated only in simulation, it is unclear whether MPPI uses the same simulation environment as that being used for evaluation. If so, it would not establish a fair comparisons to OpenVLA or pi-0.5 since they do not assume access to the environment models.
- The approach also appears to rely on a text-only LLM for specifying contact strategies and cost functions. This appears to be very challenging since it’s unclear how LLMs can specify these given no visual input (or even coordinate frame). The provided appendix also does not seem to provide sufficient details. For example, does it rely on task-specific prompt that is manually refined by the developer?

### Questions
See the weaknesses section.

### Soundness
2

### Presentation
2

### Contribution
3

### Rating
4

### Confidence
4