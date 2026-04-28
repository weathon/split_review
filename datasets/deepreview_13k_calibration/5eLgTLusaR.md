# Loco3D: Indoor Multiuser Locomotion 3D Dataset

- Decision: Reject
- Avg Score: 4.50
- Scores: 5, 3, 5, 5

## Abstract
In the context of human-AI interaction, modeling human actions is a critical and challenging endeavor, with locomotion being a particularly fundamental behavior for AI agents to understand. Modeling human trajectories in complex indoor scenes, such as the home environment, requires an understanding of how humans interact with their surroundings and other humans. These interactions are influenced by a range of factors, including the geometry and semantics of the scene, the socio-cultural context, and the task each human needs to perform. Previous research has shared datasets containing human motion and scene structure in indoor scenes, but these datasets are limited in scale due to the difficulty and time required to collect data at different locations. To solve the scale problem, we propose to use a virtual reality (VR) system to build a human motion dataset. Specifically, we present Loco3D, a dataset of multi-person interactions in over 100 different indoor VR scenes, including 3D body pose data and highly accurate spatial information. The dataset can be used for building AI agents that operate in indoor environments, such as home robots, or to create virtual avatars for games or animations that mimic human movement and posture. With an initial evaluation, we demonstrate that models trained with our dataset have improved multi-person trajectory synthesis performance on real-world data.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes a novel indoor human motion forecasting dataset containing paired motion of two real persons in virtual environments. To address the proposed task of socially-aware trajectory forecasting the authors further propose a U-Net-style model for socially-aware trajectory forecasting.

### Strengths
Social interactions in 3D scenes is highly relevant but under-explored. The authors approach of utilizing VR to easily generated large variations of virtual worlds is clever.

### Weaknesses
The authors over-claim their contributions by saying that their dataset represents “real” social interactions: a better description would be “hybrid” or “mixed” as the scene is entirely virtual. Also, real social interactions require humans to see each others faces - for observing small social cues - which is not possible with VR headset. The authors should adjust the description of their method as “real” in Table 1 and tone down their claims of representing real social interactions.

There are two concerns with regards to the proposed U-Net:
First,  the U-Net in Section 4 is not well-described: 
* How is the scene sampled into an image?
* How is the heat map generated?
* How are past trajectories encoded?
* How is the goal encoded?
* How is the map encoded?
Second, the authors should have shown the effectiveness of their method on the experiments proposed in YNet.

### Questions
* What is part of the dataset? Will the authors make available the SMPL parameters at each frame as well?
* How does the speed of the person behaves after forecasting? Do they slow down when approaching the target? Is there a velocity “jump” when changing from past to future motion?
* Why is FDE not used in the experiments? 
* For completeness: The dataset contains personal information of the recorded subjects: did the subjects consent to the release of their trajectory and pose data?
* For completeness: where will the dataset be made available?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This manuscript presents Loco3D, a dataset of a pair of humans interacting with high-resolution indoor scenes in VR that includes detailed 3D body pose as well as detailed maps of the indoor environments. The dataset includes 7000 example trajectories across 130 scenes, and in addition to 3D body keypoints they provide semantic scene segmentation and scenes with photorealistic textures. They develop a UNet based path planner module that uses a path history, the goal location, and scene map to produce a probability map of trajectories. They consider three evaluation datasets – Loco3D, Loco3D-R which was collected in the real world, adn GIMO, a previously published dataset. They show improved performance compared to YNet on the Loco3D, but not GIMO datasets, and that training on Loco3D produced superior results. They show training with multi-person data is superior and give qualitative examples.

### Strengths
* The dataset is a contribution to the field and has several novel elements, including multi-person data, photorealistic textures, and semantic segmentation. I can see this experimental approach for generating training data to become common int he field. There is also a real-world test example. 

* There is a new U-Net based modeling format that incorporated multi-person data and evaluations show some modeling improvements with multi-person data. 

* The supplement and text are comprehensive and describe experiments well.

### Weaknesses
 * The contributions can be distinguished from other datasets and models for human trajectory synthesis but the advance seems somewhat incremental in comparison. In particular the contribution is more the dataset than the model and so I wonder whether ICLR is the right venue. Because the dataset does not open up a new field in learning representations, but more advances the existing field it may find a better home in a more specialized venue.

* The distinctions between the modeling component and existing literature are unclear. The approach seems novel but also related to approaches like YNet and the strengths and weaknesses could be more clearly elucidated in the text. Moreover I would like to see benchmarks with other approaches to improve the contribution of the new models, even if this means computing on single person trajectories alone. 

* There is not a robust comparison across standard benchmarks of the modeling component. It would be nice to know whether their proposed algorithm is SOTA and comparing its performance on a standard benchmark or whether the increase in performance is specific to the collected datasets. In fact the poor performance on GIMO is a limitation of the work in my opinion rather than just an endorsement of the value of the corpus.

* Table 1 category of ‘real/synthetic’ is a bit ambiguous here, since the scenes are synthetically rendered. 

* Units in Table 2?

* It is unclear how to interpret the poor performance on other datasets in Figure 4 and Table 2. The planner does not appear to work very well and it is unclear if this is just a domain gap? Moreover I was expecting to see comparisons training on the Loco3D corpus and testing on Loco3D-R

* Can YNet be extended to include multi-person trajectories? 

* Can you comment on domain gap with real scenes. Unclear how human interaction in freely moving VR different from real environments. Affects the scope and generality of the method.

### Questions
* Table 1 category of ‘real/synthetic’ is a bit ambiguous here, since the scenes are synthetically rendered. 

* Units in Table 2?

* It is unclear how to interpret the poor performance on other datasets in Figure 4 and Table 2. The planner does not appear to work very well and it is unclear if this is just a domain gap? Moreover I was expecting to see comparisons training on the Loco3D corpus and testing on Loco3D-R

* Can YNet be extended to include multi-person trajectories? 

* Can you comment on domain gap with real scenes. Unclear how human interaction in freely moving VR different from real environments. Affects the scope and generality of the method.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper introduces a human behavior data collection system that utilizes VR to get a multi-person trajectories dataset, Loco3D, across 130 complex indoor settings. Additionally, the authors propose a human trajectory prediction model consider the multi-person scenario. Experimental outcomes indicate that in multi-person scenarios, both the Loco3D dataset and the proposed methods enhance trajectory synthesis outcomes.

### Strengths
* Leveraging VR to collect the multi-person trajectory is a compelling approach, considering the time cost and complexity to set up cameras or environments in the real world. The advantage is that although the scene is some scan-reconstructed, the human trajectory is real.
* The Loco3D dataset includes much more scenes then previous multi-person real dataset. The high diversity in the layouts can support more work focusing on trajectory synthesis in multi-person scenario.
* Their experiments demonstrate that the collected data can be used to improve the performance of the models, and the scale of the data is important.
* Their methodology takes into account multi-person trajectories, yielding enhanced results in comparison to prior research.

### Weaknesses
 * Regarding the dataset statistics, there's an absence of comparisons concerning the number of trajectories in each scene, as well as their length and complexity. In Table 2, prior multi-person trajectory datasets, such as JRDB, contained approximately 20K frames for each scene. In contrast, Loco3D offers only 7.7K frames. It remains ambiguous whether this frame count pertains to a single trajectory or multiple ones. Additionally, the variation in the number of individuals across datasets is not clearly demonstrated.
* For the comparison with prior dataset, the most related prior dataset shold be the JRDB ones, which also contains the multi-person data. Current comparison is hard to see if the improvement is from the data scale or from different task settings.
* For the proposed method, the structure seems that it can only work for a fixed number of people. This limit the generality the proposed methods. It’s also hard to see if the proposed method can still be adapted to the single-person scenario and what the performance will be.
* For the qualitative results, treating the overlapping of the trajectory as a judgement is not proper. The trajectory also involves the time, two people may not go to a near position at each time step even if their trajectories overlap.

### Questions
* For the Loco3D dataset, does it also include the first-person view frames? Then how to deal with the gap between the rendered images using a scan-reconstructed dataset (HM3D) and the real world? 
* The motivation mentions the human trajectory should consider if the other human is watching TV. However, based on the paper data collection process, all humans can only walk around, lack of the diversity in different social scenario. So what’s the actual social constraints covered in the dataset, instead of only collision avoidance between people?
* Does the dataset only contains two people scenario and why the design is like this?
* For the proposed method, is there some solution to make it adapt to scenarios with different number of people?
* Why not comparing the results with JBDR to see if the improvement really comes from different scenes or just different number of trajectories?

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper presents a new multi-human-scene interaction dataset collected using a VR system with motion capture. This work also proposes a UNet-based model for human trajectory prediction and demonstrates its effectiveness on the proposed Loco3D dataset.

### Strengths
1. The idea of collecting human-scene interaction datasets using VR is great. It enjoys the benefit of real human behavior, scene diversity, and low cost (with scalability).
2. The Loco3D dataset seems a good contribution to the community and would interest multiple fields.
3. The idea of incorporating human-human interactions is well-motivated.

### Weaknesses
The main weakness of this work is that the current experimental analysis fails to align with the main characteristic of the dataset, making the motivation for creating the dataset less convincing.
- (motion) The dataset features locomotion (3D body motions), but the experiments are only on the trajectories. The experiments should leverage the full 3D motion capture data, including joint angles and body poses, instead of just 2D or 3D trajectories. This limits the evaluation of the dataset's potential for tasks like full-body motion prediction or synthesis.
- (scene-affordance) The dataset contains rich indoor 3D scenes with diverse objects and affordances, but the experiments contain only 'binary maps as scene maps' as scene representations, which cannot reflect the meaningful scene surroundings for human behaviors. The use of binary maps severely limits the ability to model the influence of scene affordances on human behavior. The experiments should incorporate more sophisticated scene representations, such as 3D meshes, point clouds, or semantic scene graphs, to capture the spatial and semantic relationships between objects and humans.
- (interaction) The motivation behind the dataset contains social interactions (e.g., social etiquette in section 1 paragraph 2), but the interactions in the experiments only involve collision avoidance and do not address the mentioned TV scenario. The experiments do not fully explore the social interaction aspect of the dataset. The current experiments only focus on collision avoidance, which is a basic interaction. The dataset should be used to evaluate more complex social interactions, such as following, leading, or collaborative tasks, which are more aligned with the initial motivation.

### Questions
- Could the author discuss more details on the VR mocap data collection protocol? e.g. the real and virtual space could be unaligned (e.g., a wall in the real world but not in the virtual and vice versa), how to mitigate the issue?
- More interaction types could be explored in the data collection process (e.g., two people need to accomplish certain tasks together).

Minor issues:
- Section 2.2 HUMANIZE -> HUMANISE
- [b] CIRCLE: Capture in Rich Contextual Environments needs to be cited and discussed.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
