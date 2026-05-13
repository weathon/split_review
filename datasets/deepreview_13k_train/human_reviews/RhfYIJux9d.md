# Video2Policy: Scaling up Manipulation Tasks in Simulation through Internet Videos

- Decision: Reject
- Scores: 3, 6, 5, 8

## Abstract
Simulation offers a promising approach for cheaply scaling training data for generalist policies. To scalably generate data from diverse and realistic tasks, existing algorithms either rely on large language models (LLMs) that may hallucinate tasks not interesting for robotics; or digital twins, which require careful real-to-sim alignment and are hard to scale. To address these challenges, we introduce Video2Policy, a novel framework that leverages large amounts of internet RGB videos to reconstruct tasks based on everyday human behavior. Our approach comprises two phases: (1) task generation through object mesh reconstruction and 6D position tracking; and (2) reinforcement learning utilizing LLM-generated reward functions and iterative in-context reward reflection for the task. We demonstrate the efficacy of Video2Policy by reconstructing over 100 videos from the Something-Something-v2 (SSv2) dataset, which depicts diverse and complex human behaviors on 9 different tasks. Our method can successfully train RL policies on such tasks, including complex and challenging tasks such as throwing. Furthermore, we show that a generalist policy trained on the collected sim data generalizes effectively to new tasks and outperforms prior approaches. Finally, we show the performance of our policies improves by simply including more internet videos. We believe that the proposed Video2Policy framework is a step towards generalist policies that can execute practical robotic tasks based on everyday human behavior.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper proposed a method to reconstruct objects and their poses from videos in order to re-create a real-world environment in a simulator. A policy is then trained with LLM-generated reward functions inside the simulator. Experiments were run on videos from the Something-Something dataset and showed that the reconstructed environment can be used to achieve good manipulation performance (inside the simulator). The policy's performance also scales with the number of LLM-generated tasks.

### Strengths
- Leveraging in-the-wild video for robotic manipulation is an important task.
- The reconstructed scenes are pretty consistent with the original scenes but this is achieved with some assumptions.

### Weaknesses
 - The proposed method doesn't handle material and physical properties such as surface roughness, center of mass, density, weight etc. These are crucial information without which a policy cannot transfer from sim to real. The lack of these properties makes the simulation unrealistic, limiting the policy's applicability to real-world scenarios. For example, a policy trained on a simulated object with incorrect mass distribution might fail when interacting with the real object.
- The environment is assumed to be a flat table top surface, which is a big assumption. It's unclear how the method can be applied to complicated real-world scenarios. This significantly restricts the complexity of the environments that can be handled, and it's not clear how the method would generalize to non-planar surfaces or cluttered environments. The assumption of a flat surface simplifies the reconstruction and policy learning, but it does not reflect the complexities of real-world manipulation tasks.
- There's no real-world evaluation at all. Therefore, calling the learned policy a "generalist policy" is a massive overclaim. I can't really see how the proposed method can benefit real-world manipulation problems. The absence of real-world validation makes it difficult to assess the practical utility of the proposed method. The claim of a 'generalist policy' is not supported by the experimental results, as the policy is only evaluated in simulation.
- The technical contribution and the novelty of the paper is unclear. Essentially what the paper proposes is a method to reconstruct a 3D scene from a video, which is a well-established task in computer vision literature. The authors used off-the-shelf method including InstantMesh, FoundationPose to obtain the geometry and 6DoF poses of the objects in a scene. The paper also uses GPT-4o for code and reward generation which is also a well-explored task. I fail to see what the contribution of the paper is compared with prior works. The combination of existing techniques does not constitute a significant contribution without a novel approach or substantial improvement over existing methods.
- Since the paper essentially proposes a 3D/4D reconstruction framework, the title video2policy seems quite inappropriate. Besides, the policy learned from the framework likely cannot generalize back to the scene in the original video. The title is misleading as the core contribution is the reconstruction framework, not a novel policy learning approach. The learned policy is not designed to generalize back to the original video, which further highlights the disconnect between the title and the actual method.

### Questions
- Why use only 60 videos? The methods mentioned in the framework seem all pretty fast and there are an abundant amount of videos in something-something v2. Why not apply the method to all videos in the dataset?
- How does the performance scale with the number of videos? The paper claims "This generalist policy scales favorably with the number of videos used for task generation.", where is the supporting experiments? Is it Figure 5? Calling a video a task is misleading. Task and reward feel very similar to me. A manipulation task can be described by a reward in RL so if the author is referring a video as a task, I suggest using a different term.
-

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes a strategy to automatically generate tasks with corresponding data from real world videos via 3d reconstruction and tracking. Then, to enable agents to learn the task, they generate task codes and train RL policies, where reward functions are generated by novel methods of using LLMs. Finally, to enable a more generalist agent, they propose using the data generated along with the policies learned to generate expert trajectories to train a BC model on several tasks. Evaluation is performed on 9 tasks from the SSv2 dataset, and 3 tasks on a self-collected dataset, with ground truth evaluation functions. 
Overall, the method is interesting and has the potential to scale up learning from real world datasets. If clarifications are made regarding the questions/weaknesses, the rating can be increased.

### Strengths
1. The paper is well-written and easy to follow
2. The experiments performed on the generalist policy are a promising direction towards behavior cloning without human collected datasets.
3. The method is evaluated on several different tasks and on real world videos
4. Several ablations are performed to understand the importance of each component
5. Experiments are performed to show the scalability of the method, which means that it could have a larger impact

### Weaknesses
1. The way a task code is defined is novel, so its important to include some examples of the task codes that are generated and what each of the 6 components (described in Sec 4.2) look like. Specifically, the exact structure of the JSON representation, the format of the reset function (including how it interacts with the environment's reset), the success function (including the specific conditions and how they are evaluated), the format of the additional observations, and the reward function (including how it evolves over iterations) should be detailed. Without this, the points made in Sec 4.2 are somewhat abstract and hard to understand.
2. How can we verify the iterative reward function is improving the policy overtime and a necessary part of the pipeline? A graph with the iteration vs success rate for the tasks is good to include for this. X-axis would be the iteration number, and the y-axis would be the success rate. Furthermore, it's unclear how the reward function is initialized and what the initial reward signal looks like before the iterative process begins. How does the reward function change between iterations, and what are the criteria for determining if a reward function is 'better' than the previous one?
3. Line 275 in Section 4.2 discusses how GPT-4o can generate additional observations necessary such as distance between objects. However, there is not much subsequent discussion about when/what GPT-4o generates these in the experiments that are performed. Furthermore, how does GPT-4o know what additional observations to generate (there are no iterative updates for generating this part right)? Only the reward and success functions are generated with CoT so there is some learning about the environment that can be seen? It is unclear what prompts are used to generate these observations, and how the model ensures that the generated observations are relevant and useful for the task at hand. The paper should also clarify if these observations are generated once or if they are re-generated at each iteration of the reward function refinement.

### Questions
Questions that should be addressed:
1. Is it possible that the reset functions that are generated by V2P end up allowing the success state to be more easily reachable than the hard coded reset states that other methods such as CoP, Eureka, or RoboGen have? This could be like a form of reset cheating. A good way to verify this is to compare the reset functions that are generated for each baseline. Maybe one method of comparison is to check qualitatively they all reset to very different states that are equally ‘hard’ or ‘easy’ to achieve success form there
2. How precise does the tracking of the objects have to be? There are several off-the-shelf models chained together which gives lots of room for failures. So what success/failure rate did you notice during the experiments if the 6D position for example is way off? 
3. How do you evaluate the validity of a generated task code? How often does hallucination occur when generating child success/reset functions using Chain-of-thought? (Brief mention of this in line 280-282, but using GPT to evaluate still seems like there is lots of room for error).
4. ‘Task code’ is a relatively unknown term. You define this in parts, but just making this term bolded and clearly stating what this means at the end of paragraph 2 of the introduction (somewhere around line #050) would make the paper much clearer. 
5. Figure 3 shows some task codes, but please add what the task description is and the goal of these tasks are to the figure.


Minor Comments:
1. L70-82 gives a lot of related work that seems misplaced/breaks the flow of the contribution description. Preferably condense into a few lines and move the rest to the related works section
2. Line 268/269 are unclear. What is the ‘parent’ reset function vs the ‘children’ reset functions? Please clarify this.

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a method to leverage internet videos for training generalist policies. Instead of performing sim2real by creating digital twins, it only utilizes video data to extract task-relevant information, such as object assets and scene layouts. It then uses VMLs to take the video, video captions, object meshes, sizes, and 6D pose tracking to produce codes for the simulated scenes. Instead of simply cloning the trajectory in the video, the proposed leverages VLM to write the task code iteratively generates reward functions, and trains a policy to produce more training data. The reconstruction includes three steps: 1) object segmentation 2) mesh reconstruction, and 3) 6D pose tracking. The evaluation focuses on tabletop tasks using IsaacGym, which reconstructs 60 videos on 9 distinct tasks from the dataset in total and demonstrates a certain level of generalization to self-collected videos.

### Strengths
Learning from video or leveraging real-world demonstrations to train robot policies that can generalize is an essential topic. The proposed pipeline is an attempt in this direction. It uses existing components, for example, DINO grounding, sam-based segmentation, and object reconstruction and pose tracking. These components have shown good generalization to the real world, even though not perfect. The two-level learning framework is also a commonly used one, i.e., reward level tuning with LLMs and then policy training with RL on refined reward function. Given these, the replicability of the proposed should be good, and also, there are no constraints on applying the proposed to more diverse videos and tasks.

### Weaknesses
The study of the robustness of the proposed pipeline is limited.
For example, what is the performance of the DINO grounding, and how does the detection or segmentation affect the trained policy, in which sense? Also, how does the reconstruction quality affect the generalization? Especially, why is the reconstruction performed with only one image? Why not use more images for a better reconstruction? 
The proposed use of an off-the-shelf component UniDepth for size estimation, since there is much noise, is there any study showing how the noise affects the final performance?
I am confused with the design logic of the 6 components in the task code generation module. Any discussion on the why and why such a design is efficient?
Moreover, the efficiency of the training pipeline is unclear, since it involves multiple rounds of the reward reflection. Is there any metric on the efficiency of this part? Again, given that some baselines do not utilize the reflection, how do you ensure fairness?
Furthermore, the reconstruction does not include any scene information, how do you guarantee, it can be generalized to more complex scenes? Do you have some studies on the effect?
Again, since there is no limitation of applying the proposed to more videos, why not include videos from a much larger dataset to verify the benefits of the pipeline?
With that being said, I would like to see a more detailed discussion as well as more evidence of the effectiveness not just the better performance on simple tabletop scenarios and tasks.

### Questions
Most of the questions are listed above, one extra question, why do you need 6D pose tracking? And how does it relate to policy training? You are not imitating the estimated trajectory from the video right?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The Video2Policy framework offers a scalable solution for training generalist robotic policies by using internet videos of everyday human tasks. It overcomes the high cost and complexity of traditional data generation by leveraging RGB videos for task reconstruction in two phases: (1) task generation via object mesh reconstruction and 6D position tracking, and (2) reinforcement learning with reward functions generated by large language models (LLMs). It potentially overcome the hallucination of LLMs when generating the tasks, and also provide useful information (relative 6D position) in the training process.

### Strengths
1. It utilizes human videos to initiate task and reward generation, overcoming challenges typically difficult for LLMs to address.

2. It incorporates 6D relative poses of multiple objects within the scene to enhance the reward generation process, effectively harnessing critical information from the videos.

3. The experiments are thorough, yielding policies from the collected data that generalize effectively across tasks.

### Weaknesses
1. The generated tasks remain limited to simple tabletop scenarios; incorporating more complex or long-horizon tasks would enhance the framework's versatility.

2. This work primarily constructs a pipeline by integrating previous works as components, but it doesn't address technical challenges through unique design innovations.

3. No real-world experiments were conducted to validate the approach.

### Questions
1. In the object reconstruction phase, generating accurate reconstructions from masked images can be challenging due to limited pixel data for each object. With low-resolution images, tools like InstantMesh often struggle to produce high-quality results. Has this limitation been encountered in this work, and if so, what solutions have been implemented to address it?

2. In the pipeline, the 6D pose is provided in camera coordinates. It's difficult to position the camera identically to the original video. How does the framework address this issue? I assume only relative 6D poses are utilized, but I would like clarification on how GPT leverages these relative poses within the reward generation process.

3. Given the focus on data collection, comparing only success rates may not provide a fair assessment. Factors like the time-intensive iterative reward design process in this framework should be considered. A more meaningful comparison might be the time required to generate a successful trajectory.

### Soundness
3

### Presentation
3

### Contribution
2
