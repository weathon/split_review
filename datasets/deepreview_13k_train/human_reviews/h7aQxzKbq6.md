# HAMSTER: Hierarchical Action Models for Open-World Robot Manipulation

- Decision: Accept
- Scores: 5, 8, 6, 5

## Abstract
Large models have shown strong open-world generalization to complex problems in vision and language, but they have been relatively more difficult to deploy in robotics. This challenge stems from several factors, the foremost of which is the lack of scalable robotic training data since this requires expensive on-robot collection. For scalable training, these models must show considerable transfer across domains, to make use of cheaply available "off-domain" data such as videos, hand-drawn sketches, or data from simulation. In this work, we posit that hierarchical vision-language-action models can be more effective at transferring behavior across domains than standard monolithic vision-language-action models. In particular, we study a class of hierarchical vision-language-action models, where high-level vision-language models (VLMs) are trained on relatively cheap data to produce semantically meaningful intermediate predictions such as 2D paths indicating desired behavior. These predicted 2D paths can serve as guidance for low-level control policies that are 3D-aware and capable of precise manipulation. In this work, we show that separating prediction into semantic high-level predictions, and 3D-aware low-level predictions allows such hierarchical VLA policies to transfer across significant domain gaps, for instance from simulation to the real world or across scenes with widely varying visual appearance. Doing so allows for the usage of cheap, abundant data sources beyond teleoperated on-robot data thereby enabling broad semantic and visual generalization. We demonstrate how hierarchical architectures trained on this type of cheap off-domain data can enable robotic manipulation with semantic, visual, and geometric generalization through experiments in simulation and the real world.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces a hierarchical model for robotic manipulation using Vision-Language Models (VLMs) to generate intermediate 2D waypoints, which then guide a low-level control policy. The idea is to leverage high-level VLM-based planning to produce simple 2D paths, using less specific and more accessible data sources like videos or simulations. This approach aims to make manipulation models more generalizable across different environments without requiring extensive, robot-specific training data.

### Strengths
- The hierarchical approach has a nice structure, separating high-level VLM predictions from low-level control, which could allow for integration of varied data sources in future applications.
- The focus on using general, “cheap” data sources is interesting and relevant, as scaling data collection in robotics is always a challenge. This could be an efficient way to sidestep the need for large, domain-specific datasets.
- The generalization goal aligns well with current interests in making robotic systems more adaptable to diverse environments and tasks, and this modular setup has potential.

### Weaknesses
 - The paper doesn’t seem to address some core challenges in using VLMs for manipulation, such as understanding 3D spatial relationships. VLMs trained on language and images aren’t inherently equipped for the depth of 3D reasoning required for more complex manipulation. Specifically, the model does not account for occlusions, changes in viewpoint, or the complex geometry of objects, which are critical for robust manipulation.
- The tasks used are relatively simplistic and limited mostly to pick-and-place scenarios, which doesn’t fully showcase the potential of this approach. Although these tasks have merit, it’s unclear how well the model would handle more challenging or continuous tasks that require a stronger 3D understanding. For example, tasks involving deformable objects, precise alignments, or multi-step manipulation sequences are not explored, leaving the generalizability of the approach uncertain.
- In terms of novelty, the approach doesn’t seem to introduce significant improvements over existing methods for VLM-based waypoint generation. While the structure is clear and modular, there’s limited demonstration that it extends much beyond what current methods already accomplish. The paper lacks a detailed comparison against state-of-the-art VLM-based manipulation methods, making it difficult to assess its true contribution.
- A primary limitation is that the model relies only on 2D waypoints generated from single-view images, which restricts the range of tasks it can realistically handle. For tasks that require nuanced 3D spatial awareness, like pushing or rotating objects, the 2D-only input may limit its applicability. The model's inability to perceive depth directly from the input images could lead to inaccurate path planning and failed manipulations in complex scenarios.
- While the system’s hierarchical design has promise, the 2D waypoint restriction means it may not leverage the full potential of VLMs in manipulation tasks, and this makes it less flexible for more sophisticated, real-world interactions. The lack of 3D input limits the VLM's ability to reason about the environment, and the 2D waypoints may not provide sufficient information for the low-level controller to perform complex manipulations effectively.

### Questions
- How would the model perform on tasks requiring intricate 3D manipulation, like pushing or rotating objects? Given its current reliance on 2D waypoints, would extending this approach to more complex, spatially-aware tasks be feasible?
- Why were primarily pick-and-place tasks chosen? It would be insightful to see how the model handles a more varied set of challenges to get a clearer sense of its adaptability.
- Since VLM-based waypoint generation has been explored in past work, could the authors clarify how this approach differs from or improves upon those existing methods?
- Are there future plans to incorporate 3D input or multi-view data into the model? This could help address some of the limitations around spatial understanding and potentially broaden the approach’s applicability.

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
4

### Summary
The proposed method, as shown in Fig.1 and 2, leverages the advantages of imitation learning and VLA models to increase generalization ability. It distills knowledge of the task by visual path representation with VLA and uses dataset/task-specific models to deal with the lower-level controls.

### Strengths
1. The baseline comparisons are fair and detailed. More convincing with human evaluation.
2. As stated in the summary, HAMSTER leverages the advantages of imitation learning and VLA models to increase generalization ability. It distills knowledge of the task by visual path representation with VLA and uses dataset/task-specific models to deal with the lower-level controls.

### Weaknesses
1. Notations of proprioception are used differently (s and p, line 336 and 234). It confuses and breaks the whole problem statement.
2. There are no (a), (b), and (c) Fig. 5.
3. The system still requires human-engineered prompts for the VLM and other efforts such as "Conditioning on Paths" (page 7) and running the Ramer-Douglas-Peucker algorithm.

Minor:
1. missing period in line 215.
2. i.e -> i.e., (line 231).

### Questions
1. What is the use of the intermediate representations $l_i$ of the hierarchical VLM?
2. In the fine-tuning phase, are the outputs of VLM normalized across datasets? For instance, the pixel locations are normalized to $[0, 1]$ or not?
3. What is the length of the output of the Ramer-Douglas-Peucker algorithm?
4. Which part of the system has the 3D knowledge of the world? Does VLA project 3D paths in the real world to images or does the policy deal with it?
5. Please unify the notations in the problem formulation, e.g., proprioception vs. path-labeler and proprioception vs. states. Formally define and explain why they share the same notations if you have to use them repeatedly.

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors in this work propose a hierarchical action model consisting of a high-level vision-language model (VLM) and a low-level imitation learning policy. These two components communicate via a 2D path representation on the image that is predicted by the VLM and used to guide low-level imitation learning. The major advantage of such a design is to enhance the generalization of manipulation tasks by utilizing abundant "off-domain" data for VLM fine-tuning and reducing the requirement of massive amount of "in-domain" on-robot data required by the monolithic action models. Both simulated and real-robot experiments have been conducted to verify the claimed improved generalization performance against the other baselines.

### Strengths
- The target problem is important in enhancing the scalability and generalization of robot action models. The proposed idea of using 2D path intermediate representation to bridge the VLMs and low-level action models is neat and sensible;

- The presentation is in general good to follow and clear to understand. 

- The idea of using "off-domain" data to fine-tune VLM and consequentially benefit the low-level policy learning is inspiring.

- The experiments include results from both the simulation and the real robot, indicating the workload and applicability of the proposed method.

### Weaknesses
 - The foremost concern from my perspective is the mismatch between the technical contribution and the way to sell the claimed idea of hierarchical action models. Technically, this work fine-tunes an open-source VLM with easy-to-collect and "off-domain" data for 2-D path/trajectory prediction, which is used to train a low-level imitation learning policy for task execution. The purpose of the authors to enhance the impact of the work is understandable. The current technical and experimental investigation seems insufficient for this purpose. I would suggest the authors either refine the selling points (e.g., "fine-tuning cross-domain VLM for 2D path-guided imitation learning") and switch to more concrete and matched contents for presentation or include more experiments with a special focus on the idea of the hierarchy mechanism itself (detailed below).
  
- For a more focused investigation of the hierarchy mechanism, if I understand correctly, the first key factor of this idea is the intermediate representation. This key factor has a large impact on the claimed advantage, namely the possibility of utilizing the abundant off-domain training data for fine-tuning. The authors propose to use 2D-path and discuss other alternatives such as 3D-path and key-point representation. It's fine to leave the 3D version for future work. However, the key-point representation can be easily obtained by extracting the start and ending points of the 2-D path. To enhance the focus on the hierarchy mechanism, it would be informative to conduct experiments on this. On the other hand, other related work [1] demonstrates accurate key-point prediction based on open-sourced foundation models without fine-tuning.

- The second key factor in the hierarchy idea is the low-level action models. There are two points on this aspect. The first one is the way to condition the predicted intermediate representation in getting the low-level actions. Though the authors argue that overlapping the 2-D path on the existing images is a good and convenient way, it can help the community to get more insights into this "augmentation" if other ways, like concatenation, can be examined and analyzed both experimentally and empirically. The second one is about the choices of the low-level action model, [1] has demonstrated strong performance without using an imitation learning policy. Why do we need such a policy in this mechanism, which still has to be trained based on a few "in-domain" data? If yes, what's the difference between using a 2D and 3D policy? The investigation done in this work is insufficient.     

- There is no explicit empirical evidence for this claim of "drastically reducing the number of demonstrations needed for learning downstream tasks." In real-robot experiments, the better performance after being trained with the same amount of path-augmented images couldn't verify this claim. Having a quantitative experiment on how much data has been saved with the 2D-path guidance would be much more informative. For example, comparing learning curves with different amounts of training data to check if the augmented path can facilitate training efficiency.

### Questions
- Can this intermediate representation limit the versatility of the low-level motions? How do we express the versatility of the motions with the 2D path? On the other hand, the key-point representation can mitigate this constraint. For example, the authors can discuss or empirically evaluate specific types of motions or tasks that might be challenging to represent with 2D paths. 

- As mentioned in the experiment part, the number of points of the 2D path can be controlled. How would performance change if we vary the number of points?

- The idea enhances the generalization by using a large VLM for 2D path guidance. Does this increase the computation requirement? Is it worthwhile?

---------------------------------- Post Review ---------------------------------------

I appreciate the efforts of the authors to address my concerns and am pleased to increase my score.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes a two-level hierarchical approach to solving robotic manipulation tasks.  Given an image and a language prompt, a vision-language model (VLM) predicts a 2D gripper trajectory in image space.  Then, a low-level policy generates end-effector motions conditioned on the 2D gripper trajectory.  The authors show that the VLM can be trained using large-scale, offline datasets without expensive, on-robot data.  The low-level policy is trained via imitation learning with small on-robot datasets.  The proposed method, called HAMSTER, is empirically evaluated on a range of real-world and simulated robot manipulation tasks.  HAMSTER outperforms baselines when generalizing to different language prompts, spatial rearrangements, or objects.  The 2D gripper trajectory predictions of HAMSTER's VLM is evaluated based on human evaluations of their accuracy, and it is shown to produce better predictions than the baselines.

### Strengths
- The paper demonstrates that a VLM can be trained on offline, cheap datasets to produce 2D gripper trajectories to solve a range of robotic manipulation problems not seen during training.  A human evaluation study shows that the proposed training scheme produces trajectory predictions that are better ranked than baselines.
- The proposed method, HAMSTER, combines this pre-trained VLM with a low-level policy to solve language-conditioned, long horizon manipulation tasks.  This hierarchical approach is shown to significantly outperform non-hierarchical baselines on real-world tasks, especially on variations not seen during training.
- HAMSTER leverages a large VLM in a way that is still efficient at inference time.  The VLM is queried once at the start, and then only the lighter-weight, low-level policy is used.

### Weaknesses
 - The authors do not discuss common failure modes of the proposed approach.  It is written, "We refer readers to
the supplementary website for additional details on the failure modes and evaluation conditions."  This discussion is important for understanding the limitations of the approach and should be included in the main paper.  For instance, how often does the VLM produce infeasible paths? Does the low-level policy ever mess up a grasp but still follow the 2D trajectory? It would be beneficial to understand if failures are primarily due to the VLM's trajectory prediction, the low-level policy's ability to follow the trajectory, or the low-level policy's action execution.
- The results in the simulation evaluation are not compelling.  On average, HAMSTER outperforms 3D-DA by only 8%, even though HAMSTER's VLM was trained on RLBench (what Colleseum was built upon).   The discussion of this experiment is very brief so it is difficult to gain any insights.  For instance, why does HAMSTER have lower performance and much higher variance on the "no variation" task?  Is there a reason why one would expect the VLM to be especially helpful on tasks like "man obj size" or "tab col"?  Why did the authors switch from RVT-2 to 3D-DA for this setting? It's unclear why 3D-DA is used as a baseline in simulation, given that RVT-2 was used in the real-world experiments. This makes it difficult to compare the performance of the proposed method across different settings and baselines.
- It is not clear why human ranking was used as an evaluation metric for the VLM's 2D trajectories.  No information is provided in the Appendix about how the participants were instructed to rank the trajectories, whether these participants were familiar with robot arms, nor how many participants were included.  Is there a reason that the 2D trajectories could not be evaluated based on mean squared error on a set of expert robot trajectories? It's unclear how the human evaluators were qualified to assess the quality of 2D robot trajectories, and whether their subjective rankings accurately reflect the performance of the VLM.

### Questions
- It's not clear how 'time' is encoded in the 2D trajectory image.  It is written "we use a color gradient to indicate progression through time."  Is this based on an absolute or relative scale?  Would two trajectories of different lengths end at the same color?  Can this approach encode the speed that the gripper should be moving?
- How was it decided that the VLM should generate 2D trajectories in image space **and** gripper apertures?  Given that the low-level policy has to predict 6DoF end effector motions, it does not seem unreasonable that it could also predict gripper motion? Alternatively, why not train the VLM to predict the rotation of the gripper (this information would be available in the Robot Simulation Data and the Real Robot Data)?  
- Why do you only use the `front_cam` view in RLBench, as stated in Appendix A?  Given that the objective is to train a VLM that is robust to changes in view, it seems like the model would benefit from training on all camera views in RLBench.  
- Most of the images of the experiments in the main paper show the a similar camera view (camera pointing toward robot base).  Did you evaluate the model on different camera views?  Do you have evidence or ideas on how HAMSTER would perform on different views?
- Why do you think 3D-DA performed worse when the language prompts were removed?

Minor typo: Missing period at bottom of page 4 "is similar An illustrative"

### Soundness
2

### Presentation
3

### Contribution
2
