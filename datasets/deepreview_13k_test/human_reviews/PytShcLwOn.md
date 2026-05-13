# SIGHT: Single-Image Conditioned Generation of Hand Trajectories for Hand-Object Interaction

- Decision: Reject
- Scores: 6, 3, 3, 6

## Abstract
We introduce a novel task of generating realistic and diverse 3D hand trajectories given a single image of an object, which could be involved in a hand-object interaction scene or pictured by itself. When humans reach for an object, appropriate trajectories naturally form to manipulate it for specific tasks in our minds. Such hand-object interaction trajectory priors can greatly benefit applications in robotics, embodied AI, augmented reality and related fields. To tackle this challenging problem, we propose the SIGHT-Fusion system, consisting of a carefully curated pipeline for extracting features at various levels of hand-object interaction details from the single image input, and a conditional motion generation diffusion model processing the extracted features. We train our method given video data with corresponding hand trajectory annotations, without supervision in the form of action labels. For the evaluation, we establish benchmarks utilizing the FPHAB and HOI4D datasets, testing our method against various baselines and metrics. We also introduce task simulators for executing the generated hand trajectories and reporting task success rates as an additional metric. Experiments show that our method generates more natural and diverse hand trajectories than baselines and presents promising generalization capability on unseen objects. The accuracy of the generated hand trajectories is confirmed in a physics simulation setting, showcasing the authenticity of the created sequences and their applicability in downstream uses.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The paper introduces the task of generating 3D hand trajectories given a single image of an object, in two settings: (a) the object depicted by itself, and (b) the object being interacted with by a human hand. The authors set up comprehensive benchmarks for the new task, including various baselines and evaluation metrics. They propose a task success rate metric using physical simulation for evaluation. The paper develops SIGHT-Fusion, a novel pipeline designed to extract hand-object interaction features from a single image input and generate hand trajectories using a conditional diffusion-based model.

### Strengths
1. The paper proposes a challenging problem of generating plausible interaction trajectories from a single image. This problem is both interesting and important, as it addresses a critical gap in the field of 3D hand trajectory generation.
2. Using the success rate in a simulation environment as an evaluation metric is a reasonable approach, and this design is meaningful. It provides a clear and objective way to assess the performance of the proposed method.
3. The authors propose SIGHT-Fusion, which learns to generate realistic and diverse 3D hand trajectories conditioned on a single image. This is a novel and effective approach that addresses the challenges of the proposed task.

### Weaknesses
1. In Figure 2, when using conditions, either CLIP features or averaged features can be used. Do the authors have any experimental findings on when to use which type of condition? This design is very interesting because it can guide us on whether we should incorporate more global conditions or local conditions.
2. How does the paper handle articulated objects? Are they considered alongside rigid bodies? Articulated objects are clearly very difficult to learn with their interactive joints given an image. I noticed that HOI4D contains a large number of articulated objects, but I did not see results or visualizations regarding this aspect in the paper.
3. The paper only tests the success rate in a simulation environment on four simple tasks. I believe this evaluation metric should serve as a general metric; why not calculate the average success rate across all tasks as a quantitative measure?

### Questions
This paper presents a meaningful and challenging problem. However, there are still some design aspects that I am unclear about. Mainly, these concerns are related to the method of conditional injection, the handling of articulated objects, and the evaluation metrics used in the simulation environment. If the authors can address these concerns, I would be very willing to increase my score.

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
5

### Summary
This paper introduces SIGHT that generates realistic and diverse 3D hand trajectories from a single image of an object, either being interacted with or standalone. The authors propose SIGHT-Fusion, a diffusion-based conditional motion generation system that processes visual features extracted from egocentric videos of object manipulation. The method is evaluated on FPHAB and HOI4D datasets using comprehensive metrics including accuracy, diversity, and fidelity, as well as physical plausibility through MuJoCo simulation. The results demonstrate superior performance then other related works.

### Strengths
1. Methodology performance: The proposed SIGHT-Fusion system effectively combines advanced feature extraction techniques with a diffusion-based motion generation model, leading to improved performance over existing baselines.

2. Evaluation detail: The authors conduct extensive experiments using multiple metrics on well-established datasets and further validate their results through physics simulations. This experiment adds credibility to the physical plausibility of the generated motions.

### Weaknesses
The datasets used (FPHAB and HOI4D) may not include a wide variety of real-world objects and interactions, which could limit the generalization ability of the proposed method to more complex or diverse scenarios encountered in the real-world. Though authors provided the unseen testing experiment on MDM dataset, it seems also limited, compared to category-agnostic [1] or stable-diffusion-based generation method [2].
[1] HOLD: Category-agnostic 3D Reconstruction of Interacting Hands and Objects from Video, CVPR 2024.
[2] DreamFusion: Text-to-3D using 2D Diffusion, ICLR 2023.

The paper lacks an in-depth qualitative analysis of the failure cases or challenging scenarios where the proposed method might not perform well. Especially, I think it would be helpful if authors could add qualitative examples such as objects with complex shapes or scenarios with occlusion. Such analysis could provide valuable insights into the limitations and potential areas for improvement.

No discussion for previous similar literature such as [3], which is generating hand-object interactions. Though their input is different while I think the method could be trivially extends to the intended scenario.
[3] Text2HOI: Text-guided 3D Motion Generation for Hand-Object Interaction, CVPR 2024

The qualitative results do not clearly demonstrate the improvements of the proposed method. Especially, in Figure 4, a comparison between the current SOTA method and the proposed approach, it is difficult to find which result shows better quality on the figure. I request authors to have some pointers to indicate where to see.

The evaluation metrics only address limited cases. This paper addresses Hand-Object Interaction, but it does not consider any metrics to assess interaction results, such as "hand-object contact" measure. This raises concerns that the evaluation may be overly restricted to limited cases.

### Questions
I request authors to answer concerns raised in weakness section.

### Soundness
1

### Presentation
2

### Contribution
1

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
They proposed a model that estimates the trajectory of the hand conditioned on a single image of hand-object interaction.

Various experiments were conducted by comparing it with models that estimate hand trajectories based on text.

### Strengths
They propose a model that generates the trajectory of the hand even from a single image.

The superiority of the proposed model is demonstrated through simulations.

Highly informative features are extracted by considering the contact areas between the hand and the object.

### Weaknesses
1. It does not consider the object's trajectory (rotation and translation), making the application of this technique seem unpractical.

2. It appears that the hand's translation is not generated separately, which also seems to be a practical issue. It seems like the fingers move and hand rotates in place.

3. The approach does not account for the interaction between the object and the hand, which makes it seem inadequate. For example, it does not consider a loss that considers actual 3D contact with objects. Also, it does not use 3D point cloud information of the object. This could prevent the network to learn generalizability to unseen objects.

4. There is no metric evaluation involving the 3D object. As HOI4D includes 3D object meshes, it seems unfortunate that there are no metrics for contact or penetration between hand the object.

### Questions
1. How can we confirm that the generated hand trajectory properly interacts with the object corresponding to the image? Specifically, does the part of the hand grasping the object match exactly as shown in the image? For instance, in Figure 1, the bottom of the milk carton is being grasped in the input image, but the motion generated in 3D shows that the hand is grasping the top of the milk carton.

2. Does the generated hand motion vary significantly even when the same image is used as the condition image, as shown in Figure 1?

3. What is the P model? Is it different from M? It seems to be a model not described in the Method section. From the caption of Table 3, it seems to be an other version M that uses the part features. Additionally, O is described as the interacting object in L219, but in the caption of Table 3, it is referred to as a model.

4. Is there a specific reason for not using object features and part features together?

5. Does the model perform well even in situations where there are only a few part features before averaging due to a small object in the image? In other words, I am curious if the model's performance varies significantly depending on the size of the object in the image and the number of part features.

6. Is there a reason why ours, part experiments were not conducted for unseen objects in Table 2? It would be helpful to test ours, part as well to understand hand interactions with unseen objects.

7. In the simulation examples, are the objects shown in the result images the same as those in the condition image? It would be clearer if the condition (input) images were also displayed.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This work propose a new task of generating hand trajctories based on a single image. And design a method called SIGHT-Fusion which is able to extract visual features and leverage diffusion-based generation model to diffuse motions. The results demonstrate well performance against baselines.

### Strengths
Generating hand trajectories can benefit various fields, such as VR/AR and robotics. The authors’ use of diffusion for trajectory generation is a reasonable approach to alleviate ambiguity. I also appreciate the considerable amount of video results, especially the application to dexterous hands.

### Weaknesses
- Most results show that the trajectory attempts to grasp a single object, which raises doubts about whether the methods have truly learned a grasp/manipulation prior. Examples such as throwing a ball or placing a pencil could better address this issue.

- Line 208 states that it focuses solely on right-hand motion, while existing hand motion generation papers, such as [1], already generate motions involving both hands. 

- The architecture of SIGHT-Fusion is quite similar to MDM, while MDM achieves two-hand motions with a broader range motions.


[1] Text2HOI: Text-guided 3D Motion Generation for Hand-Object Interaction

### Questions
- The main question is why generating hand motions from a static image is considered valid. There could be many plausible motion trajectories that correspond to a given static image, such as moving a bottle up or down.

- What is the performance on deformable objects, such as pulling out a tissue or handling cloth?

- How can the 2.5-second SIGHT-Fusion motions be retargeted to approximately 25-second motions in the simulator? Providing more details would help readers reproduce the results.

### Soundness
3

### Presentation
2

### Contribution
3
