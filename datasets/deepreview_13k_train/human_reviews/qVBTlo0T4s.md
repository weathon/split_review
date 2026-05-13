# AutoNeRF: Training Implicit Scene Representations with Autonomous Agents

- Decision: Reject
- Scores: 3, 5, 6, 5

## Abstract
\noindent
Implicit representations such as Neural Radiance Fields (NeRF) have been shown to be very effective at novel view synthesis. However, these models typically require manual and careful human data collection for training. In this paper, we present AutoNeRF, a method to collect data required to train NeRFs using autonomous embodied agents. Our method allows an agent to explore an unseen environment efficiently and use the experience to build an implicit map representation autonomously. We compare the impact of different exploration strategies including handcrafted frontier-based exploration, end-to-end and modular approaches composed of trained high-level planners and classical low-level path followers. We train these models with different reward functions tailored to this problem and evaluate the quality of the learned representations on four different downstream tasks: classical viewpoint rendering, map reconstruction, planning, and pose refinement. Empirical results show that NeRFs can be trained on actively collected data using just a single episode of experience in an unseen environment, and can be used for several downstream robotic tasks, and that modular trained exploration models outperform other classical and end-to-end baselines. Finally, we show that AutoNeRF can reconstruct large-scale scenes, and is thus a useful tool to perform scene-specific adaptation as the produced 3D environment models can be loaded into a simulator to fine-tune a policy of interest.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces a method, AutoNeRF, that enables an embodied agent to autonomously collect the necessary data to train Neural Radiance Fields (NeRF), thereby removing the need for manual and tedious data collection. The authors compared various exploration strategies including frontier-based, end-to-end and modularized approaches which consist of trained high-level planning and traditional path followers. The evaluation is based on four downstream tasks - rendering, map reconstruction, planning, and pose refinement. The results reveal that NeRFs can be efficiently trained using actively acquired data from an unseen environment, and that these can be used for different robotic tasks. Furthermore, they also show that modularly trained exploration models are superior to classical and end-to-end strategies.

### Strengths
1. The proposed autonomous approach for embodied agents collecting NeRF visual training data greatly reduces human intervention.
2. The authors conduct a comprehensive evaluation assessing the quality of the reconstructed scene produced by four different autonomous data collecting approaches. The assessment is carried out by evaluating each approach based on four downstream tasks which indicates the actual performance on follow-up applications.

### Weaknesses
1. The scientific contribution of this paper is unclear. Although the authors conduct a comprehensive evaluation of the designed autonomous approaches, it does not point out their core contributions to this field. The proposed autonomous exploration strategy is straight-forward, and could not be considered as main contribution of this paper. Additionally, the absence of a comparison between their methods and existing techniques in autonomous visual exploration—which could have been utilized for collecting NeRF training data—is missing. The experimental evidence alone does not constitute significant scientific contribution.
2. The claims are backed by empirical results, but the lack of theoretical analysis or concrete mathematical justifications for the algorithm.

### Questions
Did you evaluate the end-to-end based and modularized based method on completed unseen (or largely different) scenario? I am curious about the actual performance in such scenarios. While the rule-based method, i.e., the frontier-based exploration, did not outperform learning-based methods (such as end-to-end based and modularized methods) in your experiments, it demonstrated fairly consistent results across the majority of scenes, regardless of whether they were familiar or unfamiliar scenarios.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper discusses the key considerations when employing NeRF for map construction and semantic segmentation in the context of autonomous embodied agents exploring previously unseen environments. Utilizing modular exploration policies that take into account four types of intrinsic rewards (exploration area, obstacle coverage, semantic object coverage, and viewpoint coverage), the agent initially learns how to explore through self-supervised learning. Subsequently, the agent trains a Semantic Nerfacto by collecting valuable data during its exploration. The quality of the Nerfacto is assessed across four distinct tasks: rendering, metric map estimation, planning, and pose refinement. The authors propose reward types that enhance NeRF training and present a diverse set of evaluation tasks to expand the application of NeRF in the field of environment exploration.

### Strengths
The authors correctly emphasize the need for more realistic tasks when evaluating NeRF in navigation scenarios. Furthermore, they have introduced effective rewards that yield improved NeRF results in the various suggested tasks.

### Weaknesses
As the authors attempt to cover a wide range of tasks, the presentation of results lacks organization, making it challenging for readers to interpret and examine the outcomes. Specifically, the paper jumps between different evaluation metrics and tasks without a clear narrative, making it difficult to compare the performance of different reward policies across the board. Furthermore, the lack of a baseline comparison for the Semantic Nerfacto model, particularly against a vanilla Semantic NeRF, makes it difficult to assess the true impact of the proposed exploration strategy. The claim that the vanilla Semantic NeRF produces a higher quality mesh is not supported by quantitative evidence, relying solely on a qualitative assessment of 'holes and irregularities'. This makes it difficult to objectively evaluate the claim. Finally, the implications of the experiments in Table 1 are not fully explained, leaving the reader to guess the significance of the results in the context of the overall contribution.

### Questions
1. Could you please share the results of the vanilla Semantic NeRF model mentioned in Figures 9 and 10? While it is claimed to deliver superior results compared to Semantic Nerfacto, there is a lack of supporting evidence.
2. It appears that the four types of rewards exhibit different strengths. Are there any criteria or trends that can assist researchers in selecting the most appropriate reward type for specific tasks? For instance, is there a reason why the policy with the obstacle coverage reward performs better than others in the rendering task?

3. Could you provide a more detailed explanation of the experiments featured in Table 1 and elaborate on their implications?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper introduces AutoNeRF, a method enabling autonomous agents to collect data for training NeRF without human intervention. It proposes various exploration strategies for efficient environment exploration. These strategies are evaluated based on downstream tasks like viewpoint rendering, map reconstruction, planning, and pose refinement. Results demonstrate that NeRFs can be trained from a single episode in an unknown environment and applied to diverse robotic tasks.

### Strengths
1. The paper explores multiple exploration policies for collecting training samples for a scene NERF, which provides a comprehensive analysis of the community.
2. The policies are further evaluated using different downstream robotic tasks, which is beneficial to related researchers.
3. The experimental results are comprehensive and solid.
4. The paper is well-written and easy to follow.

### Weaknesses
1. The novelty of the paper is limited. The idea of using Nerf for scene construction in SLAM is not new. The authors also adopted an off-the-shelf NERF module. The main contribution of this paper lies in validating the effect of different exploration policies during image collection on downstream robotics tasks.

### Questions
1. How many images are used to train the NERF model? In task specification it says "The agent can navigate for a limited number of 1500 discrete steps", does it mean to capture 1500 images for NERF training?

### Soundness
3 good

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper targets an important problem of autonomous NeRF construction through active exploration. The solution is straightforward: A conventional modular learning of online exploration is first deployed, followed by an offline semantic NeRF construction. It should be noted that the two types of scene representations are adopted for these two problems. Multiple downstream tasks are conducted given the batch-learned NeRF.

### Strengths
+ The paper is well-organized and clearly presented. The motivation is clear and the problem setting is practical for the NeRF community.
+ Multiple downstream tasks given the trained NeRF are tested.
+ The utilization of a NeRF model as a simulation environment for finetuning navigation policy is interesting.

### Weaknesses
1. The major concern lies in the two-phase fashion:
- The input of the system is unclear. For exploration, RGB frames along with the depth maps are required (Sec. 4 Task Specification), while for NeRF training, the depth information is not leveraged. It is highlighted in Sec. 4.2 that 'no depth information is required for reconstruction' is an important property. From the reviewer's perspective, this is merely the characteristic of NeRF itself. For the proposed AutoNeRF, the depth information is essential for the proposed exploration module to update the 2D top-down map.
- How the automatic process helps the downstream tasks is unclear. It is known that a trained NeRF can be applied for these four tasks (as also mentioned in the Related Work section). The paper directly adopts the methods without further modification, and the NeRF training does provide any feedback to the exploration policy training. Moreover, the exploration phase already builds a 2D map online that can be used for Task 2&3. The benefit of involving an extra NeRF training phase for these two tasks should be further elaborated.

2. Insufficient experiments.
- Though the paper conducts thorough experiments on multiple tasks, merely 5 Gibson scenes are evaluated. It should be noted that the methods of [Chaplot et al., 2020a] and [Ramakrishnan et al. (2021)] are evaluated on Matterport3D besides the Gibson datasets. As the paper targets an AutoNeRF problem, the method is expected not to be limited by the data-driven exploration policy. The generalization ability of the proposed modular learning strategy should be discussed compared to the relevant one-phase works of A-C.
- The technical contributions seem to be the different reward signals in Sec. 4.1. Detailed ablation studies should be conducted to validate the efficacy and the benefits arising from these terms.

### Questions
Though the automatic reconstruction of the implicit neural field is of great importance, the current version seems inconsistent and disintegrated. Multiple aspects are integrated into the system directly without clear connections. The author is expected to stress the following questions in a more unified and valid manner:
1. What is the major focus of the paper? A. If the paper targets an automatic reconstruction of the neural radiance field, there are only minor contributions to the reward design of the exploration policy. The author should further evaluate how these rewards lead to a better radiance field (but not a better exploration strategy). The limitations of this modular learning strategy should also be discussed (especially the generalization ability). B. If the paper targets a better exploration policy with additional NeRF training, how NeRF affects the exploration policy (but not the pointGoal policy provided in Tab. 1) should be elaborated. Nevertheless, it seems that the construction of NeRF does not affect the exploration policy in this modular fashion. C. If the paper aims to stress the advantages of a well-trained NeRF given sufficient observations on the downstream tasks, the experiments should clearly explain how the compared exploration strategies (Frontier, E2E) fail that leads to performance degradation, and how the designed reward functions help to solve the problem. 
2. What is the role of semantic reasoning? Seemingly the semantic cues are not the best reward for exploration, and semantics are not a prerequisite for the 'AutoNeRF' setting. The subtasks of semantic rendering and object-goal navigation can be removed without hurting the central contribution. The role of semantics should be better demonstrated.
3. Does the training of NeRF lead to a better BEV map? The exploration phase already obtains a 2D metric-semantic map on the fly that can be applied for exploration and point/object-goal navigation. The map should be added to Fig. 10 for a better understanding of how the performance can be affected with a follow-up NeRF model.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
