# LocoVR: Multiuser Indoor Locomotion Dataset in Virtual Reality

- Decision: Accept
- Avg Score: 5.80
- Scores: 3, 6, 8, 6, 6

## Abstract
Understanding human locomotion is crucial for AI agents such as robots, particularly in complex indoor home environments. Modeling human trajectories in these spaces requires insight into how individuals maneuver around physical obstacles and manage social navigation dynamics. These dynamics include subtle behaviors influenced by proxemics - the social use of space, such as stepping aside to allow others to pass or choosing longer routes to avoid collisions. Previous research has developed datasets of human motion in indoor scenes, but these are often limited in scale and lack the nuanced social navigation dynamics common in home environments. 
To address this, we present LocoVR, a dataset of 7000+ two-person trajectories captured in virtual reality from over 130 different indoor home environments. LocoVR provides full body pose data and precise spatial information, along with rich examples of socially-motivated movement behaviors. 
For example, the dataset captures instances of individuals navigating around each other in narrow spaces, adjusting paths to respect personal boundaries in living areas, and coordinating movements in high-traffic zones like entryways and kitchens. Our evaluation shows that LocoVR significantly enhances model performance in three practical indoor tasks utilizing human trajectories, and demonstrates predicting socially-aware navigation patterns in home environments.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces a dataset for multi-user indoor navigation collected in a Virtual Reality (VR) environment. The dataset includes 7,071 trajectories with 2.5 million frames across 131 scenes. Baseline methods, such as A* and U-Net, are used to demonstrate and analyze the proposed dataset.

### Strengths
+ The dataset is based on real human subject studies, and the use of VR environments facilitates data collection efforts.

+ This open-source dataset could benefit the research community focused on social navigation.

### Weaknesses
 - Novelty and contributions are key concerns. Although the human subject studies require significant time and the dataset a reasonable sample size, the dataset has not been demonstrated, for example, to train state-of-the-art neural network models. The demonstrated methods are relatively simple. The dataset is also limited to two-person navigation scenarios.

- Given that the objective of the dataset is to estimate user trajectories and goal positions, without addressing the estimation of human body motions, why is VR more advantageous than an overhead camera with a bird-eye view?

- How are real human full-body motions in the physical world synchronized with the virtual environment?

-  Research (e.g., in human-robot interaction) has shown that humans respond differently to virtual agents compared to physical agents. The authors are encouraged to provide a study and analysis on whether this difference exists and, if so, how significant it is.

- The work mentions robotics as a motivation and application scenario; however, related research on social robot navigation is not well reviewed.

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
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces LocoVR, a virtual reality dataset that captures approximately 7,000 two-person trajectories across 130 indoor home scenes. The authors demonstrate the utility of LocoVR through three applications: global path prediction, trajectory prediction, and goal area prediction. The model trained on this dataset exhibits socially and geometrically aware navigation patterns within indoor scenes.

### Strengths
1. The extensive collection of two-person human trajectory (with motion capture) data in indoor scenes, is a valuable resource for the community.
2. Utilizing virtual reality for data collection is a promising approach, allowing more diverse 3D scenes when resources are limited.
3. The data and code will be released.

### Weaknesses
1. While using VR to collect human trajectory data is helpful, this paper would benefit from a discussion in the related works section about VR and human motion. For instance, referencing works like "QuestEnvSim: Environment-aware Simulated Motion Tracking from Sparse Data" in SIGGRAPH 2023 [1] which uses VR for motion tracking and "Strategy and Skill Learning for Physics-based Table Tennis Animation" in SIGGRAPH 2024 [2] which involves interaction between human and humanoid agents.
2. I notice authors utilize motion capture to provide whole body motion, and I wonder the reason to consider only experiments of path, trajectory and goal prediction. The occasionally unnatural motion observed in the video could be explained, particularly in the context of the inverse kinematics (IK) system used. A more detailed description of the motion capture setup and its limitations would be valuable.
3. The use of A* baselines seems inappropriate for two-person interaction scenarios. I notice this dataset mainly focuses on obstacle avoidance. There appears to be a lack of interactive behaviors between the two persons. It may not be enough if two persons just operate independently and avoid the other person within the same space. I think it doesn't reflect scenarios often seen in real life. Can the authors provide more information on the distribution of action types within the dataset? Given this is a dataset paper, more statistics and descriptions would be beneficial, such as the distribution of different interaction types, including but not limited to avoidance, following, and leading behaviors. Metrics like average and minimum separation distances, relative velocities, and frequency of direction changes could provide a quantitative characterization of the dataset's diversity.

### Questions
The paper seems to focus on locomotion. Without interactions like sitting on a sofa or standing up from a chair, does the goal prediction remain compelling?
With many figures presented in 2D planes, would a bird's eye view semantic map provide enough information for the prediction tasks? What's the importance of 3D geometry?

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
1) LocoVR introduces a large dataset with 7000 two-person interactions across 130 diverse indoor environments in VR -- includes full body pose data and spatial information. 
3) LocoVR improves model performance in 3 indoor tasks including human trajectories and predicting socially aware navigation patterns in home environments.

### Strengths
1) LocoVR’s large, indoor locomotion dataset records two-person interactions across 130 diverse indoor environments 
2) Introduction of motion proxemics in a large-scale dataset which is useful for downstream tasks such as studying human-human interactions and potentially human-robot interactions
3) Rigorously quantitatively evaluated against strong baselines; baseline configurations and settings are fair and well-documented 
4) Data of two-person trajectories is useful to study motion proxemics 

The authors introduce an exciting/ relevant problem. The problem is well-motivated while the execution and evaluations are strong. I see many potential downstream applications and I believe that this will make a huge impact in the robotics field.

### Weaknesses
1) Potential Overfitting to VR-Specific Biases:
I am curious what the authors have done to further minimize the gap between real-world scenes vs VR scenes. Are there any obstacle perception features e.g., vibrational feedback when participants bump into objects in the scene?

2) *Qualitative results: ‘as the trajectory progresses, the probability distribution of the goal area narrows down near the true goal object’*
I think that it is reasonable to assume that humans narrow the probability distribution in LocoVR closer to the true goal object. However, I would like to understand exactly why this observation arises from LocoVR’s dataset. Is it merely the size of the dataset or is it the difference in data collected in LocoVR vs the other datasets? Are the authors claiming that this is a strength as it mimics the probability distribution of human trajectories better? If so, I would like to see analysis of this phenomenon in the different datasets.

3) Cultural/ societal biases of motion proxemics:
Since motion proxemics is influenced by cultural norms, authors should show aggregated user demographics. It would also be interesting to see motion proxemics based on the aggregated clusters of people.

### Questions
See weaknesses.

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
LocoVR is a virtual reality-based dataset aimed at improving the modeling of human locomotion in complex indoor environments. This dataset specifically focuses on multi-user indoor navigation, capturing over 7,000 two-person trajectories within more than 130 different home-like scenes. The main goal of the LocoVR dataset is to enhance the ability of AI systems, like home robots, to understand and predict human movement patterns that incorporate both spatial and social navigation dynamics.

### Strengths
By using VR, the dataset captures detailed spatial data and full-body motion in diverse home environments. The VR setup enables controlled capture of social navigation behaviors, such as maintaining personal space and avoiding collisions in shared spaces like entryways.

The dataset is well evaluated. The paper evaluates the dataset on three trajectory-based tasks—global path prediction, trajectory prediction, and goal prediction. The results show that models trained on LocoVR outperform those trained on other datasets, particularly in predicting realistic, socially aware navigation paths in complex environments.

I can see implications of this work not just for virtual agents, games etc, but also as we move to further robotic presence in our homes this type of dataset can help train their trajectories.

### Weaknesses
I m not sure about the Non-Verbal Social Cues: such as gaze direction or facial expressions—that influence social navigation.

The two agent approach perhaps limits also its scope in multi-user indoor scenarios common in real homes with multiple occupants.

### Questions
I would like future work to discuss how this type of work can be merged with other approaches like weighted interpolations to define trajectories of avatars indoors: https://www.microsoft.com/en-us/research/publication/avatarpilot-decoupling-one-to-one-motions-from-their-semantics-with-weighted-interpolations/

### Soundness
3

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
4

### Summary
This paper focuses on understanding human locomotion behaviors in indoor environments, with the specific scenario of two persons walking two separate goals in an indoor room. The main contribution is a new dataset LocoVR capturing sequences of two persons walking to their goal locations in 3D indoor rooms. To overcome the high cost of capturing locomotion in physical scenes, this paper proposes a VR-based solution where the subjects wear a VR device and navigate through a virtual 3D room displayed in VR. The human locomotion trajectories are tracked using VR devices. This VR capture solution scales up locomotion capture to 130+ scenes. The authors then conducted experiments validating that the collected LocoVR dataset outperforms existing datasets in three tasks: global path prediction, trajectory prediction, and goal prediction.

### Strengths
1. The proposed VR capture solution eliminates the high cost of physically setting up indoor scenes and capturing human movements, which facilitates scaling up locomotion capture to many more scenes compared to previous datasets.

2. This paper captures two-person goal-reaching motions which include the social navigation behaviors such as adjusting the path to respect personal boundaries or side steps to give way to another person. Such social navigation behavior is not covered in most previous datasets and is important for understanding multi-human social navigation and potential human-robot interactions.

3. Experiments on three navigation-related tasks show that models trained on the LocoVR dataset consistently outperform models trained on existing datasets when tested on a real-world two-person locomotion test set.

### Weaknesses
1. Although this paper claims to provide full body pose data (L20), the human motion capture is far from realistic according to the supplementary video (0:00-0:30). If aiming for capturing full body poses, it may be necessary to change from the HTC VIVE tracking to marker-based motion capture as in CIRCLE (Araujo et al., 2023). With the current presented results, I recommend removing the claims of full body pose data since all experiments only use trajectory data. The provided full-body pose data appears to be a rough estimation derived from sparse trackers, rather than a high-fidelity capture of human movement. This discrepancy between the claim and the actual data quality should be addressed by either improving the capture method or reframing the dataset as primarily a trajectory dataset with auxiliary, low-fidelity pose information.

2. The VR capture system is limited to simple behaviors assuming a flat floor scene and no contact-based close object interactions. It can only capture locomotion or reaching behaviors as in CIRCLE (Araujo et al., 2023). The VR capture system can not work for behaviors like lying on a sofa or walking up stairs. When the humans try to do such interactions in VR, they are actually interacting with air in the real world and will fall. This virutal-real inconsistency can also cause the subjects to slightly walk into obstacles as discussed in paper.

3. This paper only focus on a very simple social navigation scenario of two persons avoiding each other. However, the social navigation behaviors can be much more complex. For example, humans do not only avoid each other but also collaborates and coordinates, consider the cases where one person is leading the way and other persons follow the leading one, and two persons walk to each other to talk. It is also necessary to include social scenarios with more than two persons.

### Questions
1. In appendix H, why are time windows and intervals set as the presented numbers? Are there any motivation or empirical study?

2.L860, figures should be tables?

### Soundness
3

### Presentation
3

### Contribution
3
