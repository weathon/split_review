# Fusion Is Not Enough: Single Modal Attacks on Fusion Models for 3D Object Detection

- Decision: Accept
- Avg Score: 6.25
- Scores: 5, 6, 6, 8

## Abstract
Multi-sensor fusion (MSF) is widely used in autonomous vehicles (AVs) for perception, particularly for 3D object detection with camera and LiDAR sensors. The purpose of fusion is to capitalize on the advantages of each modality while minimizing its weaknesses. Advanced deep neural network (DNN)-based fusion techniques have demonstrated the exceptional and industry-leading performance. Due to the redundant information in multiple modalities, MSF is also recognized as a general defence strategy against adversarial attacks. 
In this paper, we attack fusion models from the camera modality that is considered to be of lesser importance in fusion but is more affordable for attackers. We argue that the weakest link of fusion models depends on their most vulnerable modality, and propose an attack framework that targets advanced camera-LiDAR fusion-based 3D object detection models through camera-only adversarial attacks. 
Our approach employs a two-stage optimization-based strategy that first thoroughly evaluates vulnerable image areas under adversarial attacks, and then applies dedicated attack strategies for different fusion models to generate deployable patches. The evaluations with six advanced camera-LiDAR fusion models and one camera-only model indicate that our attacks successfully compromise all of them. Our approach can either decrease the mean average precision (mAP) of detection performance from 0.824 to 0.353, or degrade the detection score of a target object from 0.728 to 0.156, demonstrating the efficacy of our proposed attack framework. Code is available.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper studies the vulnerability of multi-sensor fusion to adversarial attacks in autonomous driving. The authors propose to leverage the adversarial patch to attack the camera modality in 3D object detection. Specifically, they propose an attack framework employing a two-stage optimization-based strategy that first evaluates vulnerable image areas under adversarial attacks, and then applies dedicated attack strategies for different fusion models to generate deployable patches.

### Strengths
- This paper studies an important concern in autonomous driving, i.e., the vulnerability of multi-sensor fusion to adversarial attacks.

- Multiple feature-level fusion models are considered in this paper.

- The performance of the proposed framework is evaluated through both simulated and real-world experiments.

### Weaknesses
 - This paper does not provide the threat model. What information is available to the attacker during the attack? How feasible is it for the attacker to access this information in a real-world setting? What are the attacker's capabilities?

- The practicality and generalizability of the proposed attack are limited due to its ineffectiveness on decision-level fusion models, which are widely used in many autonomous driving systems, such as Baidu Apollo. Although the proposed attack can alter camera inputs, it fails to affect the outputs of decision-level fusion models. Moreover, these models tend to depend more on LiDAR detection results, further diminishing the practicality of the proposed attack.

- I found it hard to understand the positioning of this paper. There are many existing works studying the attacks against camera-LiDAR fusion models [1,2]. These methods can be used to attack all three types of sensor fusion models including data-level fusion, feature-level fusion, and decision-level fusion. However, the method proposed in this paper can only be used to attack the first two types of fusion models. So, what is the major advantage of this work compared to those existing works? The authors should compare their method with existing attacks to demonstrate superiority of the proposed attack. 

- The practicability of the adopted adversarial patch is questionable. Table 7 shows that the minimum dimensions of the patch are 1 meter by 1 meter, and the patch is too large to be practical. How to place such a large patch on a pedestrian in the real world? In addition, it's impractical to place such a large patch on the back of a vehicle. The patch may hide the license plate of the vehicle, which is prohibited by the traffic law. 

- The real-world evaluation is weak. The authors propose to use a patch with a special color pattern to conduct the attack. Such a color pattern can be affected by many factors in the physical world such as light condition, the distance between the camera and the patch, as well as the view angle of the camera. However, the authors do not evaluate the impact of these factors in the real-world setting. 

- The impact of the proposed attack on the vehicle's motion remains unclear. Is the perception system of the vehicle consistently deceived by the attack? Is the vehicle's trajectory affected by the attack?

### Questions
- What is the threat model. What information is available to the attacker during the attack? How feasible is it for the attacker to access this information in a real-world setting? What are the attacker's capabilities?

- What is the major advantage of this work compared to existing attacks against camera-LiDAR fusion models?

- How to place the adversarial patch on a pedestrian in the real world (as shown in Figure 10)? How to place the patch on the back of a vehicle? Does the patch hide the license plate of the vehicle?

- Does the proposed attack maintain its effectiveness under varying light conditions in the real world?

- The impact of the proposed attack on the vehicle's motion remains unclear. Is the perception system of the vehicle consistently deceived by the attack? Is the vehicle's trajectory affected by the attack?

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a new approach to attacking fusion models from the camera modality, which successfully compromises advanced camera-LiDAR fusion models and demonstrates the weaknesses of relying solely on fusion for defence against adversarial attacks. The proposed attack framework is based on a novel PointAug method that perturbs the point cloud data and generates realistic-looking adversarial examples. The experiments conducted in both simulated and physical-world environments show the practicality and effectiveness of the proposed approach.

### Strengths
1.Sophisticated Camera-LiDAR Fusion Model: The proposed methodology exemplifies a commendable synthesis of advanced camera-LiDAR fusion models. This amalgamation not only taps into the inherent strengths of individual modalities but also crafts a synergistic fusion, ensuring that the combined system is more robust and efficient than its constituent parts in isolation.
2.Efficacy of PointAug in Generating Adversarial Samples: An intrinsic highlight of the paper is the PointAug method, which adeptly fabricates realistic-looking adversarial examples. Such capability is pivotal, particularly in the realm of robust machine learning, as it enables researchers to thoroughly evaluate the resilience of models against potential adversarial threats.
3.Rigorous Experimental Validation in Diverse Environments: The rigorousness and diversity of experiments set this work apart. By conducting evaluations in both simulated and real-world environments, the paper fortifies the assertion of the proposed approach's practicality and efficacy. This dual-pronged validation underscores the method's adaptability and reliability in a wide range of scenarios.

### Weaknesses
1.Limited Fusion Model Efficacy: The methodology, while promising, seems to be narrowly tailored for a specific set of fusion models. This raises concerns about its universality. An in-depth exploration into its effectiveness against a broader spectrum of fusion models, particularly those employing decision-level fusion, would have provided a more comprehensive perspective, allowing for a holistic understanding of its potential and pitfalls. The current focus on data-level and feature-level fusion leaves a gap in understanding how the proposed attack would perform against models that fuse information at a later stage, potentially limiting the practical applicability of the findings.

2.Data Dependency and Generalizability Concerns: The experiments, predominantly based on a circumscribed dataset, cast doubts on the model's capacity to generalize across diverse scenarios. The exclusive reliance on a limited dataset, even if it contains diverse driving conditions, can inadvertently introduce biases, thereby undermining the robustness of the approach when deployed in novel, real-world situations. The lack of evaluation on datasets with different sensor configurations, environmental conditions, or object types raises questions about the generalizability of the attack.

3.Inadequate Security Analysis and Potential Resource Constraints: While the paper delves into several aspects of the proposed approach, it seems to sidestep a comprehensive analysis of its security implications, particularly concerning the specific threat model and attacker capabilities. Given the pivotal role of security in such contexts, a detailed discourse would have been invaluable. Furthermore, the potentially substantial computational overhead required to generate adversarial samples, especially in real-time scenarios, may render the approach untenable for resource-constrained environments. The paper's omission of a thorough dissection of its inherent limitations, including the specific hardware requirements and time costs, further obscures the potential challenges one might encounter in its adoption.

### Questions
1.Comparison with Pre-existing Methodologies: Given the emergence and evolution of methodologies targeting fusion models, how does the proposed approach position itself relative to these existing strategies? An analytical juxtaposition against established techniques would elucidate its uniqueness, advantages, and potential shortcomings.
2.Defensive Countermeasures against the Approach: While the paper sheds light on an innovative adversarial approach, it begs the question: What are the viable defensive strategies that can be deployed to counteract its effects? Unveiling potential countermeasures not only underscores the resilience of the approach but also aids in the development of more robust fusion models.
3.Extension and Scalability Concerns: Fusion models are diverse and multifaceted. How malleable is the proposed approach in its application to other fusion model variants? A deeper dive into its adaptability would provide insights into its scalability and flexibility across various fusion paradigms.
4.Implications for Autonomous Vehicle Security: Given the pivotal role of fusion models in autonomous vehicle systems, the proposed adversarial approach inevitably raises safety and security concerns. How might these attacks compromise the integrity and reliability of autonomous driving systems? A comprehensive discussion on this would be crucial for stakeholders in the autonomous vehicle domain.

### Soundness
3 good

### Presentation
4 excellent

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
This paper proposes an adversarial attack method, which could attack multi-modal 3D object detection methods from the image input, making the attack easy to implement.
It first recognizes the proper attack type and proposes different methods for each type.
Experiments are conducted with multiple popular multi-modal detectors, showing promising performance.

### Strengths
- The motivation that attacks from image input is reasonable, which is practical real world.
- The proposed method overall makes sense.
- Authors provide a demo, which makes the application of the proposed method more clear.
- Authors conducted extensive experiments with many SOTA the art detectors, making the results convincing.

### Weaknesses
 - Attack from only the image side has limited application. In particular, some methods do not conduct feature-level fusion between image and LiDAR like [1][2]. The two modalities are decoupled in these methods. Even if the image modality is totally failed, they can output reasonable results. For instance, in data-level fusion models, a failure in the image modality might not completely compromise the system's ability to generate reasonable outputs, especially if the LiDAR data remains unaffected. This is particularly relevant in scenarios where the image data is used to augment or enhance the LiDAR data, but the core object detection or scene understanding relies more heavily on the latter.
- The writing is not clear, especially in page 4 and page 5. There are very long paragraphs and many notations without clear organization, making it hard to follow the detailed method. For example, the description of the sensitivity distribution recognition and the subsequent attack strategy selection process lacks a clear, step-by-step explanation. The notations, such as those used in the optimization process, are introduced without sufficient context, making it difficult to understand their significance and how they relate to each other. I list some detailed questions in the following question box.
- The method is not well-motivated. The proposed method seems to be a general attacking method. The paper does not sufficiently elaborate on what specific challenges are faced when the attack is limited to the image modality, especially in the context of autonomous driving. Are there any special designs to solve problems in image-only attacking or autonomous driving scenes? What is the difficulty of image-only attacks? For instance, it is unclear whether the sensitivity distribution recognition algorithm is specifically tailored for image-only attacks or if it is a general technique applicable to other modalities as well. Furthermore, the paper does not discuss how the proposed method addresses the unique challenges of autonomous driving scenes, such as varying lighting conditions, weather, and the presence of dynamic objects.

### Questions
- In attack strategies, is the noise patch shared by the whole dataset? I saw the patch keeping changing in object-level attacks but remaining unchanged in scene-level attacks.
- Is the mask in Sensitivity Distribution Recognition shared by the whole dataset?
- I do not understand the form of the proj_x in Eq. 6 and why it is necessary.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The author proposes a two-stage optimization strategy for camera-LiDAR fusion models via using adversarial patches in camera images. The paper explores single-modal attack on fusion models, an interesting yet under-explored problem.

### Strengths
* The paper is well-written and explores an interesting topic. 
* The proposed method can decrease the model performance by a large margin, showing the possibility of dramatically deteriorating the system performance by only attacking single-modality.

### Weaknesses
 * The effectiveness of the proposed two-stage optimization approach needs further justifications. Only showing the performance drop on fusion models is not enough. Comparisons with other single-stage attacks are also needed to demonstrate the effectiveness. Without proper benchmarks and comparisons with other SOTA algorithms, it is hard to justify the effectiveness of the technical contributions. Specifically, the paper lacks quantitative comparisons demonstrating the advantage of the two-stage approach over a single-stage optimization in terms of attack success rate and perturbation magnitude. The current evaluation only shows that the two-stage approach can lead to performance degradation, but does not show it is superior to a single-stage approach, especially considering the increased complexity.
* How to ensure the feasibility of the adversarial patches? Since the gradient optimization may find patches in the undeployable areas e.g., sky, can the proposed approach ensure the attack is feasible in the real physical world? Also in the paper, the author assumes the lidar data would not be changed. Since the patch may influence the lidar intensity or introduce extra points, please provide justifications for this assumption. The paper needs to address how the patch is designed to avoid influencing the lidar data, such as through material selection or specific placement strategies. Furthermore, a more detailed explanation is needed regarding the projection of the patch onto the 3D scene to ensure that it is physically plausible and does not introduce unrealistic artifacts in the scene geometry.

### Questions
* What is the sensitivity of single-modal methods vs multi-modal (LiDAR/camera) methods?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
