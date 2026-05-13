# DexTrack: Towards Generalizable Neural Tracking Control for Dexterous Manipulation from Human References

- Decision: Accept
- Scores: 8, 3, 6, 8

## Abstract
We address the challenge of developing a generalizable neural tracking controller for dexterous manipulation from human references. This controller aims to manage a dexterous robot hand to manipulate diverse objects for various purposes defined by kinematic human-object interactions. Developing such a controller is complicated by the intricate contact dynamics of dexterous manipulation and the need for adaptivity, generalizability, and robustness. Current reinforcement learning and trajectory optimization methods often fall short due to their dependence on task-specific rewards or precise system models. We introduce an approach that curates large-scale successful robot tracking demonstrations, comprising pairs of human references and robot actions, to train a neural controller. Utilizing a data flywheel, we iteratively enhance the controller's performance, as well as the number and quality of successful tracking demonstrations. We exploit available tracking demonstrations and carefully integrate reinforcement learning and imitation learning to boost the controller's performance in dynamic environments. At the same time, to obtain high-quality tracking demonstrations, we individually optimize per-trajectory tracking by leveraging the learned tracking controller in a homotopy optimization method. The homotopy optimization, mimicking chain-of-thought, aids in solving challenging trajectory tracking problems to increase demonstration diversity. We showcase our success by training a generalizable neural controller and evaluating it in both simulation and real world. Our method achieves over a 10% improvement in success rates compared to leading baselines. The project website with animated results is available at  [DexTrack](https://projectwebsite7.github.io/gene-dex-manip/).

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper proposes an approach for training generalizable neural tracking controllers from human reference trajectories for dexterous manipulation tasks with robot hands. The approach consists of three steps: The first step involves using reinforcement learning to successfully track single, per-task trajectories for a subset of tasks. These policies are then distilled into a single policy using imitation learning. Next, a dataset of trajectories is sampled from the remaining tasks. The trained IL policy is now used to generate reference policies and residual RL is used to improve per-trajectory tracking. The best tracking results are used to re-train the IL policy. To enhance the diversity of trajectories tracked, a homotopy optimization scheme is introduced to facilitate “chain-of-thought” learning of the tracking controller over the set of related tasks. Once a sufficient set of high-quality tracking trajectories is generated, a conditional diffusion model is trained to serve as a homotopy generator. Finally, RL, the trained tracking and the trained homotopy generator are used to curate a final set of demonstrations and optimize the tracking controller.

### Strengths
- Meticulous and concise description of the details of the proposed algorithm.
- Tackles an important problem of learning a tracking controller for dexterous manipulation that is often overlooked, but could have significant impact as our data collection devices continue to improve with the rapid rise of AR/VR.
- Thorough evaluations of the proposed method in simulation as well as real-world setup.
- Paper provides useful insights into the importance of high-quality demonstration data for dexterous manipulation, and outlines a procedure for curating it from existing datasets.

### Weaknesses
 - Approach relies on the presence of object states in the dataset which are difficult to obtain and are limited to very few datasets. It could be useful to investigate the effectiveness of this dataset without using object states, especially given the relatively small performance gap with the `(w/o data)` ablation. Based on the current results, it is unclear to me that the use of object state data, which is especially hard to come by in real-world datasets is significantly useful to the proposed approach.
- In the same vein, it might be insightful to present results with the `Ours (w/o data)` ablation in the real-world experiments to better understand the effectiveness of data when crossing the significant domain gap between simulation and real-world.


### Questions
- How does a simple open loop baseline perform? I would be interested in the authors’ experience with sampling a reference trajectory from the dataset based on a simple heuristic to determine a nearest neighbor trajectory. 
- With human-object interaction, the trajectory of the object is generally the main variable of interest. Given the significant morphology gap between human hands and the robot hands used in this work, the error in position and orientation of the wrist as well as the robot hand fingertips can be a noisy signal resulting from artifacts in the trajectory retargeting scheme. I would like the authors to reflect on the relative weighting schemes attempted and any related conclusions that informed their design of the reward function as well as metrics.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The authors propose a neural IK controller for controlling dexterous robot hands. The results are validated in both simulated environments and the real world. The authors claim the proposed IK controller can achieve better tracking results than existing approaches.

### Strengths
- **Real-world experiments are valuable**. I appreciate the authors' efforts to conduct real-world validations of their approach.
- **Baseline comparisons add value**. I appreciate the authors' efforts to compare against DGrasp and PPO baselines.

### Weaknesses
 **A. Presentation**.

The paper's presentation is substantially below the ICLR standard in figure and writing. I had a very difficult time understanding the paper.

The teaser figure is confusing. First, it is too dense for the readers to quickly catch what the paper is doing. There are simply too many display items in the teaser figure, and the readers could be overwhelmed. More importantly, **I could not comprehend the input and output behavior of the work from the teaser figure**. I scrolled to the method section just to understand what the paper is tackling.

Now, the second figure of the method is just as dense. I don't know what viewing order the authors want to present, but it left me confused about the most essential input and output behavior of the method.

Regarding writing, the authors had trouble situating their contribution and the problem they are solving using the conventional language in robotics. **The authors could have communicated very clearly that they were building an inverse kinematics controller that takes Euclidean space coordinates as input and outputs joint space position-based commands, in just a few sentences in the abstract, introduction, and figures.**

Next, there is a mixture of overuse and incorrect usage of terms from deep (reinforcement) learning, multi-body dynamics, control theory, and robotics in general. This leads me to question the credibility of this work.

I already provided one example of the authors' clarity in communicating their input-output behavior.  Another example I will give is the use of "robustness of tracking controller" by the authors. It can be easily confused with robustness analyses from control theory in the context of trajectory tracking and IK, e.g., using toolsets from Lyapunov Analysis. This, in my view, irresponsible use of terms is also evidenced in line 176, when the authors casually throw out words like "adaptability," "generalizability," and "robustness" without grounding these properties in any computational ways, leaving the readers to interpret themselves. These terms should not be easily thrown into publications without computational interpretations. Another example - what are the "hard-to-track" trajectories mentioned in Figure 2 vs. the "Parent" trajectory? Can the authors computationally state what makes them hard to track?

Whether the approach can handle second-order transients is also not communicated effectively. The proposed approach seems to eventually use a PID-like controller to command the included robotic systems. I could not assess this part due to a lack of descriptions. Can the system perform torque-level control, which is crucial for contact-rich manipulations?

**B. Confusing related work section, Missing critical experiments**.

I am currently unconvinced and cannot fully assess the performance of the work. The related work section mentions the sample inefficiency problem of RL. Yet, the evaluation protocol doesn't ablatively analyze how the proposed approach can generalize other than a very fuzzy success rate criterion in Figure 5.

I am worried that this work will not inform the community why the proposed approach brings benefits. The proposed approach is a very complicated pipeline, piecing together existing toolsets. First, tracking is a highly continuous task and should not be solely evaluated in a single scalar of success rate when the authors want to show that their approach is more "sample-efficient." Together with the presentation issues I have listed above, I could not understand the take-home message of the work to the robotics community. What limitations of existing controllers (e.g., OmniGrasp & DGrasp) are addressed by this pipeline?

### Questions
Please see my comments in the weakness section. Thanks.

### Soundness
2

### Presentation
1

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
This paper presents DexTrack, a generalizable neural tracking controller for dexterous manipulation, trained on large-scale robot tracking demonstrations based on human-object interactions. The method integrates reinforcement learning, imitation learning, and homotopy optimization to improve controller performance, diversity, and adaptivity in dynamic environments. DexTrack achieves over 10% higher success rates than leading baselines in both simulation and real-world tests, demonstrating robust manipulation capabilities across various objects and tasks.

### Strengths
Originality: The method is original, and combining RL and IL makes perfect sense for training a controller with high-quality demonstrations. I especially like the use of homotopy optimization as a path generator to enhance data quality.

Quality: The experimental results are thorough and solid, both qualitatively and quantitatively. A substantial number of simulation experiments are conducted, and I appreciate the inclusion of real-world results as well.

Clarity: The paper is clear, well-written, and easy to understand.

Significance: This work represents a solid advancement toward solving the challenging task of dexterous hand manipulation, which is a significant objective in robotics.

### Weaknesses
The real-world robot results are not very impressive, as the grasp does not appear to be consistently robust, which may limit the method’s applicability in practical settings. It’s understandable, however, that real-world evaluations can be influenced by various factors, such as hardware limitations, sensor noise, and environmental variability, all of which can impact performance. The paper also does not fully explore the limitations of the homotopy generator beyond its speed. While speed is certainly a factor, there may also be other limitations, such as the generator’s ability to generalize across a diverse range of objects and trajectories. It would be valuable to understand if the homotopy generator maintains high performance across these variations or if specific configurations present challenges. The paper would benefit from a more detailed analysis of the failure cases of the homotopy generator and how these failures impact the overall performance of the tracking controller.

### Questions
Are there any limitations to the proposed homotopy generator beyond its speed? While speed is certainly a factor, there may also be other limitations, such as the generator’s ability to generalize across a diverse range of objects and trajectories. It would be valuable to understand if the homotopy generator maintains high performance across these variations or if specific configurations present challenges.

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The authors proposed a neural tracking controller that integrates the reinforcement learning and imitation learning by iteratively improving the controller and generating demonstrations in simulation. Specifically, they proposed a per-trajectory tracking scheme to generate diverse and high-quality tracking demonstrations through a homotopy optimization framework. The authors further show qualitative and quantitive results to evaluate their proposed method.

### Strengths
This work has solid contributions including novel approach and substantial experimental results. The work is well-motivated to present a generalizable tracking controller (policy learning) especially that can tackle dexterous manipulation. The framework the authors proposed was well-formulated. The experiments are thorough and results are well-presented and analyzed.

### Weaknesses
I found the method section was hard to follow and understand, and I would suggest to improve the writing.
1) It would be great to clearly define each terminology at the beginning such as for kinematic reference trajectory, expert trajectory, baseline trajectory, kinematic reference sequence, tracking prior and etc and use them consistently through the paper.
2) I found the pipeline in section 3.3 helpful for me to understand the whole framework, so I would suggest to move it to the beginning of the section 3. 
3) Figure 2 has a lot information, but it was hard for me to find a proper order to read it. Maybe it can be improved with a more clear flowchart. It would be great to use consistent icons (multiple different ones for object) or remove redundant icons (such as what is the magnifying glass icon?)

Typo in section 4.1 Metric: racking -> tracking

### Questions
1) In section 3.1 Imitation Learning: Does expert state-action trajectory come from human demonstration? If so, how to address the kinematic and dynamic gaps here?

2) In section 3.2 Finding effective homotopy optimization paths: Could the authors clarify “better baseline trajectory” in the sentence “For a specific task, we consider a neighbor that provides … parent task."?

3) The real-world deployment seems impressive. I wonder beyond grasping, have the authors tried in-hand manipulation on real-world robot or were there any failure cases?

### Soundness
3

### Presentation
2

### Contribution
3
