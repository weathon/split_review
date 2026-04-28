# ConcreTizer: Model Inversion Attack via Occupancy Classification and Dispersion Control for 3D Point Cloud Restoration

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 5, 5, 8

## Abstract
The growing use of 3D point cloud data in autonomous vehicles (AVs) has raised serious privacy concerns, particularly due to the sensitive information that can be extracted from 3D data. While model inversion attacks have been widely studied in the context of 2D data, their application to 3D point clouds remains largely unexplored. To fill this gap, we present the first in-depth study of model inversion attacks aimed at restoring 3D point cloud scenes. Our analysis reveals the unique challenges, the inherent sparsity of 3D point clouds and the ambiguity between empty and non-empty voxels after voxelization, which are further exacerbated by the dispersion of non-empty voxels across feature extractor layers. To address these challenges, we introduce ConcreTizer , a simple yet effective model inversion attack designed specifically for voxel-based 3D point cloud data. ConcreTizer incorporates Voxel Occupancy Classification to distinguish between empty and non-empty voxels and Dispersion-Controlled Supervision to mitigate non-empty voxel dispersion. Extensive experiments on widely used 3D feature extractors and benchmark datasets, such as KITTI and Waymo, demonstrate that ConcreTizer concretely restores the original 3D point cloud scene from disrupted 3D feature data. Our findings highlight both the vulnerability of 3D data to inversion attacks and the urgent need for robust defense strategies.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
ConcreTizer, a novel model inversion attack specifically designed for restoring 3D point cloud scenes from disrupted 3D feature data, is presented in this paper.  The unique challenges in 3D point cloud inversion, such as the inherent sparsity of the data and the ambiguity between empty and non-empty voxels after voxelization have been identified.  The authors address these challenges by incorporating two key techniques: Voxel Occupancy Classification (VOC) to distinguish between empty and non-empty voxels, and Dispersion-Controlled Supervision (DCS) to mitigate the dispersion of non-empty voxels across feature extractor layers. Evaluations on widely used 3D feature extractors and benchmark datasets demonstrate the effectiveness of ConcreTizer in restoring original 3D point cloud scenes.  This work highlighted the vulnerability of 3D data to inversion attacks.

### Strengths
The paper presents the first in-depth study of model inversion attacks for 3D point cloud data.  The proposed ConcreTizer appears to be novel, designed to tackle the unique challenges associated with 3D point cloud inversion.    

The paper is well-written with a clear and concise explanation of the problem, the proposed solution, and the experimental results. The experiments are comprehensive and well-designed, demonstrating the effectiveness of ConcreTizer across various datasets and 3D feature extractors.    

The findings of this paper have significant implications for the privacy and security of 3D point cloud data. The authors demonstrate that 3D data is vulnerable to inversion attacks, even when shared in the form of intermediate features.  This highlights the urgent need for robust defense strategies to protect sensitive information in 3D data. The proposed ConcreTizer method serves as a valuable tool for assessing the effectiveness of such defense strategies.

### Weaknesses
While the paper emphasizes the need for defense strategies, it only briefly explores the use of Gaussian noise addition as a potential defense mechanism.  A more in-depth investigation of various defense strategies, including their effectiveness and limitations, would further strengthen the paper's contribution.  For example, I would recommend exploring adversarial training, differential privacy, or feature obfuscation techniques. I would recommend an analysis of the trade-offs between privacy protection and utility preservation in these defense mechanisms.

ConcreTizer method is specifically designed for voxel-based feature extractors.  While these extractors are commonly used in autonomous vehicles, exploring the applicability of the method to other types of 3D feature extractors, e.g., point-based and graph-based would help broaden its scope and impact.   I recommend discussing how the key components of ConcreTizer (VOC and DCS) might need to be adapted for point-based or graph-based extractors, and highlight challenges they anticipate in extending the method to these architectures.

While the paper discusses the potential privacy risks associated with 3D point cloud data, it could benefit from a more detailed discussion of the real-world implications of these risks. This could include specific examples of how restored 3D scenes could be used to compromise privacy or security.  I also recommend the authors to provide concrete examples of privacy breaches that could occur with restored 3D scenes, such as identifying individuals, revealing sensitive infrastructure details, or inferring behavioral patterns. It's useful to discuss potential legal or ethical implications of these privacy risks in the context of autonomous vehicles and smart cities.

### Questions
Can the authors comment on how to improve the exploration of the defense strategies beyond what is done here? What are other directions and what are inherent challenges?

Any comments on whether the identified model inversion risks apply to point-based and graph-based feature extractors?

Any comments on how the identified privacy risks would compromise privacy or security in more concrete scenarios?  Why would anyone care about this?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper presents the first comprehensive study of model inversion attacks in 3D point cloud reconstruction tasks, introducing an attack method named ConcreTizer. ConcreTizer utilizes Voxel Occupancy Classification (VOC) to distinguish between zero-padded empty voxels and non-empty voxels containing valid points at the origin (0, 0, 0), along with Dispersion-Controlled Supervision (DCS) to enforce sparsity in the recovered 3D point cloud data. Extensive quantitative and qualitative experiments on open-source datasets, such as KITTI and Waymo, validate the effectiveness of this inversion attack and underscore the privacy vulnerabilities and the critical need for robust defenses in 3D point cloud data applications.

### Strengths
- ConcreTizer represents the first exploration of inversion attacks on 3D point cloud data, providing valuable insights and inspiration for further research.
- The paper demonstrates ConcreTizer’s effectiveness across various datasets and feature extractors, achieving impressive point cloud reconstruction results. The breadth and diversity of experiments enhance the credibility of the findings.

### Weaknesses
1. The attack scenario in this paper lacks practical significance. One of the core innovations proposed by the paper is the introduction of VOC to differentiate between empty voxels and those located at the (0,0,0), as they share the same representation. However, a simpler solution exists to address this issue, such as adding an "occupied" label when voxelizing the point cloud data, which would render the VOC setup unnecessary.
2. The paper contains some ambiguities in its expression, making it difficult to understand. See Question 1 for further details.

### Questions
There are ambiguities in the presentation. For instance, in Figure 2, the white areas, as suggested by the context, represent actual point cloud data, which decreases with increasing layer depth. However, the caption of Figure 2 states, “As the layer depth increases, the number of restored points increases rapidly, ...” which contradicts the visual representation and may confuse readers trying to align the illustration with the description.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper proposed the first study of model inversion attacks for 3D point cloud data. The primary contributions of our work include (1) identifying the challenges associated with the interaction between 3D point cloud characteristics and voxel-based feature extractors, (2) introducting ConcreTizer that utilizes Voxel Occupancy Classification (VOC) and Dispersion-Controlled Supervision (DCS) to restore original 3D point clouds from their voxel-based features. (3) Experiments demonstrate the superior performance of ConcreTizer compared to a traditional method and GAN-based method. The findings highlight the vulnerability of 3D point clouds to inversion attacks and underscore the need for enhanced defensive strategies in privacy-sensitive applications.

### Strengths
1.	Originality: The paper introduces ConcreTizer, the first approach to 3D point cloud restoration from voxel-based features, highlighting previously unexamined vulnerabilities. 
2.	Clarity: The paper is well-organized.
3.	Significance: By demonstrating the risks of model inversion attacks on voxel-based 3D features, this work has meaningful implications for privacy in applications like autonomous driving, emphasizing the need for robust defenses in this domain.

### Weaknesses
 1.	Focus on Voxel-based Features Only:
The paper’s focus is solely on voxel-based feature inversion, with no consideration for point-based or projection-based features. The justification for this narrow focus is not sufficiently strong, especially given the existence of other common 3D data representations. The paper should at least discuss the challenges and potential adaptations of ConcreTizer to these other feature types, or provide a more compelling argument for why they are out of scope. For example, point-based methods, while computationally intensive, are widely used and have different characteristics that could affect the performance of the proposed inversion attack. Similarly, projection-based methods, which transform 3D data into 2D representations, present another avenue for feature extraction that should be acknowledged.
2.	Limited Comparison Methods:
ConcreTizer is mainly compared with Point Regression and UltraLiDAR. While UltraLiDAR is a relevant baseline, the comparison lacks a thorough evaluation against other state-of-the-art inversion methods. Specifically, recent GAN-based or diffusion-based approaches, which have shown promise in generating high-quality 3D data, should be included to provide a more comprehensive assessment of ConcreTizer's performance. The absence of these comparisons makes it difficult to fully understand the strengths and weaknesses of the proposed method relative to the broader landscape of generative models.
3.	Limited Validation Scope:
a)	3D Object Detection Evaluation: Only PointPillar is used to assess detection on restored scenes. The choice of a single object detection model limits the generalizability of the findings. Testing with a more diverse set of models, such as CenterPoint, PV-RCNN, and Voxel R-CNN, is necessary to ensure that the conclusions are robust and not specific to the PointPillar architecture.
b)	Effect of DCS Instances in Ablation Study: The chosen values for DCS instances (1, 2, 4, 10) are limited and unevenly spaced. The lack of a more systematic exploration of the DCS parameter space makes it difficult to draw definitive conclusions about the optimal configuration. A more comprehensive ablation study, with a broader and more evenly distributed range of values, is needed to understand the sensitivity of the method to this parameter.
4.	Writing:
a)	Why the results for VoxelResBackbone with the Waymo dataset are not included?
b)	It’s unclear if "VOC alone" in the component-wise analysis ablation study refers solely to using the regression loss function. Explicit clarification would help.
c)	The phrase, “Since the restoration task does not require separate labeling, it is possible to train using open source datasets or self-collected data,” could be streamlined as the first part might appears redundant.

### Questions
Please refer to the weakness part.

### Soundness
2

### Presentation
3

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
The paper highlights the growing privacy concerns surrounding the use of 3D point cloud data in autonomous vehicles due to the sensitive information it contains. While model inversion attacks have been well-studied in 2D data contexts, their application to 3D point clouds has largely been unexplored. To address this, the authors present an in-depth study of model inversion attacks aimed at reconstructing 3D point cloud scenes. They identify challenges such as the inherent sparsity of 3D data and the ambiguity between empty and non-empty voxels after voxelization, which is worsened by voxel dispersion across feature extractor layers. To tackle these issues, they introduce ConcreTizer, a model inversion attack specifically designed for 3D point cloud data, incorporating Voxel Occupancy Classification and Dispersion-Controlled Supervision. Experiments on popular 3D feature extractors and datasets like KITTI and Waymo demonstrate ConcreTizer's effectiveness in restoring disrupted 3D point cloud scenes, underscoring the vulnerability of 3D data to such attacks and the urgent need for robust defense strategies.

### Strengths
1.Good writing. This paper is well-written and easy to understand for even outliers like me, since I am not an expert in the research domain of model inversion attacks.

2.Nice figure presentations. The nice figures including Figures 1-3 make the paper more clearly and visually pleasing.

3.Well-motivated scheme. The authors have justified the motivation and key intuition behind proposed research problem and solution.

### Weaknesses
1.More analysis about the failures of existing inversion attacks are needed. In the Introduction section, Lines 71-72, the authors just demonstrated that conventional attacks failed, however, the authors did not provide more insights behind this phenomenon. A detailed explanation will help us get a better understanding of the reason why the proposed attack is effective.

2.Limited scope of proposed attacks. The authors said that, "we delve into the phenomena that arise when the voxel-based feature extractors handle 3D point cloud scenes", however, not all point cloud networks need to realize voxelization during feature extracting [1]. Therefore, it seems that the first challenge cannot represent the majority point cloud inversion attack scenes, limiting the effectiveness scope of the proposed attack scheme.

3.I encourage the authors to conduct more experiments to make results more convincing, since the page limit is 10 in ICLR 2025, providing enough space to demonstrate more results. For instance, the authors are supposed to employ more 3D point cloud datasets (which may not only focus autonomous driving datasets)

4.More defense baselines are supposed to be used for evaluation. Many recent works about point cloud adversarial attacks [2-4] have  employed  popular defense schemes like random 3D data augmentations, SOR, and SRS to evaluate the point cloud attack scheme's robustness. Thus, I will appreciate it if the authors can provide more results about defense evaluations.

### Questions
As a minor suggestion, the authors could revise the statement in Line 47 to make this claim “However, efforts to protect raw data have primarily focused on 2D domains, rather than 3D data.“ more accurate. Since recently there is already some parallel studies that mainly focus on protecting 3D raw data privacy against unauthorized training [5], the authors can revise this sentence to suggest the difference between existing 3D works and this paper's concentration view and the importance of studying model inversion attacks in 3D point clouds.

[5] Unlearnable 3D Point Clouds: Class-wise Transformation Is All You Need. NeurIPS 2024

### Soundness
3

### Presentation
3

### Contribution
3
