# SparseDFF: Sparse-View Feature Distillation for One-Shot Dexterous Manipulation

- Decision: Accept
- Scores: 6, 6, 6, 6

## Abstract
\vspace{-6pt}
Humans demonstrate remarkable skill in transferring manipulation abilities across objects of varying shapes, poses, and appearances, a capability rooted in their understanding of semantic correspondences between different instances. To equip robots with a similar high-level comprehension, we present \method, a novel \ac{dff} for 3D scenes utilizing large 2D vision models to extract semantic features from sparse RGBD images, a domain where research is limited despite its relevance to many tasks with fixed-camera setups. \method{} generates \textbf{view-consistent} 3D \acp{dff}, enabling efficient \textbf{one-shot} learning of dexterous manipulations by mapping image features to a 3D point cloud. Central to \method{} is a feature refinement network, optimized with a contrastive loss between views and a point-pruning mechanism for feature continuity. This facilitates the minimization of feature discrepancies \wrt end-effector parameters, bridging demonstrations and target manipulations. Validated in \textbf{real-world} scenarios with a dexterous hand, \method{} proves effective in manipulating both rigid and deformable objects, demonstrating significant \textbf{generalization} capabilities across object and scene variations.
\vspace{-6pt}

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The broader goal of the paper is to enable the transfer of robotic dexterous grasps from one object to a similar object (which can happen with understanding the inherent similarities of the 3D shape instances despite the variations in appearances, poses, or categories). More precisely, given a source scene, source hand-object grasp and a target scene, what could be the target grasps.
To do so, they leverage 2D vision models (namely DINO) to learn features in 2D space and then distill or back-project those features in 3D. The similarly of features in 3D space allows transfer of grasps from one object to another.
Compared to prior works, which leverage dense multi-view images to infer dense 2D features for each three 3D point and simply average the multi-view features, the paper operates in sparse view setting. Rather than simply out the point features from multiple view, the paper paper learns a feature refinement network on each point features and defines a contrastive learning approach to bring points closer to each in 3D other more closer in feature space and points farther from each other in 3D space more farther in feature space.
Finally, leveraging the projected and refined 3D features from sparse views, the paper performs the task mentioned in first bullet, mapping source grasp (on sourc e scene) to target scene.

### Strengths
Writing is good, and the paper is easy to follow.
The motivation of creating a generalized robotic manipulator and leveraging 3D priors for that, seems exciting and promising.

### Weaknesses
[Novelty Issue] Lack of any exciting factor or in some sense novelty: The difference from prior work in DFF (distill feature field) is that the paper operates in sparse view setting, where simple fusion of features from multiple views doesn’t perform best. To overcome this loss of views from prior work, they refine the point features baed on the insight that points close in 3D, should have similar features. This seems a very natural and obvious technique of pruning or refining points which have incorrect feature consistency w.r.t 3D consistency.

[Assumptions on GT depth and camera pose] Secondly, following up on the novelty part, the paper makes the assumption of having GT depth maps and also GT camera poses. Errors in either of them will make the above refinement step tricky.

[Additional experimental comparison] Experimental Comparison against baselines like (Neural descriptor fields and follow-up) where the goal is similar but rather than using the large vision model, an object category specific feature descriptor is learned.

[Less Relevant] Newer papers like Lseg, Conceptfusion have projected LLM/ vision-LLM features on the 3D scenes, comments on using them as feature backbones will be appreciated.

[Less Relevant] Papers learning joint hand object poses, leaning visual affordances from images, also seem to be relevant related works, comparison against them in related work would be appreciated (Affordance Diffusion: Synthesizing Hand-Object Interactions, papers on hand-object interaction: HOI etc).

### Questions
I would like authors to address the points raised in weaknesses section. 
1. What happens when there is noise in pose and/or depth? How will that impact refinement module?
2. How does the method compare with baselines like neural descriptor fields and follow up works?

### Soundness
3 good

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
To mitigate the dense view requirement in the distilled feature field (DFF) for the application of one-shot dexterous manipulation, the authors introduce sparseDFF, which utilizes a sparse collection of RGB-D scans of a scene. Feature points are reprojected using depth, followed by a feature refinement process on these reprojections. Contrastive loss and point pruning are employed to enhance feature consistency within each local neighborhood, and an energy function is formulated to aid in reducing feature discrepancies. Performance on grasping benchmarks demonstrate the proposed methods surpasses DFF while significantly outperforms UniDexGrasp++.

### Strengths
- The necessity of as few as 4 views for transferring manipulation skills is noteworthy, as this method can be readily generalized to novel scenes.
- Point feature refinement, the minimization of feature discrepancies using an energy function, and point pruning are specifically designed for applications with RGB-D scans as input.
- Utilizing DINO feature distillation for diverse downstream grasping tasks markedly outperforms the previous baseline (DFF) and UniDexGrasp++.

### Weaknesses
**[Clearance]** 
- The authors are encouraged to establish connections regarding why distilling DINO features is advantageous and elucidate its applications in downstream tasks. Specifically, the manuscript should detail how the semantic understanding provided by DINO features translates into improved performance for dexterous manipulation, going beyond a general statement about inter-scene correspondences. It would be beneficial to provide a concrete example of how a specific DINO feature helps in a grasping scenario.
- The definition of **one-shot** should be explained in the manuscript (abstract or introduction). The current usage is ambiguous and could refer to different aspects of the learning process. A clear definition is needed to avoid misinterpretations.
- The input should accurately be described as "multi-view RGB-D scans" rather than "Given a 3D point cloud X", in the method section. And the dimension of the variable should be added. It is important to specify the number of views, the resolution of the RGB-D images, and the format of the point cloud data (e.g., organized or unorganized).
- Regarding the motivation of using DINO, while the authors have highlighted, "This field offers semantic understandings for inter-scene correspondences that transcend geometric descriptors", how does it contribute specifically to image matching deep models like LOFTR? The authors should clarify why DINO features are preferred over other feature extractors, especially in the context of establishing correspondences between different views. A comparison of the feature matching performance of DINO versus other methods would be beneficial.

**[Method]** 
The authors propose "discard the 20% of points that accumulate the fewest votes.".How was this hyper-parameter for the pruning ratio determined? Were multiple-stage or iterative pruning strategies considered? The manuscript should provide a more detailed explanation of the hyperparameter selection process, including any sensitivity analysis performed. It is also unclear what constitutes a 'vote' in this context and how these votes are accumulated. 

**[Experiments]** 
- How did the inference performance compare with baseline methods? The authors should provide a quantitative comparison of the inference time of the proposed method with the baseline methods. This is crucial for understanding the practical applicability of the method.
- Was depth information also utilized by DFF?

### Questions
See the raised questions in Weaknesses.

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work applies 3D feature fields for manipulation. The key contribution lies in introducing a sparse view setting, where unlike previous works that use dense RGB views, this work uses sparse RGB-D views. A point-based sparse 3D feature field construction method is introduced to improve the 3D information aggregation quality and the grasping task performance.

### Strengths
The introduction of sparse RGBD camera setting.
The method of sparse DFF to reconstruct 3D feature fields from sparse RGBD inputs.
Reasonable experiment design and analysis.

### Weaknesses
There are existing sparse-view NeRF methods (e.g., [1,2]) that applies similar ideas as the sparse DFF, some of which are not extremely hard to apply to the normal DFF (e.g,, [1]). It is fairer to allow baselines to also utilize the depth information introduced in this work (e.g., introducing depth supervision similar as [1] in DFF).

### Questions
N.A.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper presents an innovative method to obtain view-consistent 3D DFFs from sparse RGBD data, enabling one-shot learning of complex manipulations that can be adapted to unfamiliar settings. The key contribution of SparseDFF comprises a lightweight feature refinement network, optimized using a contrastive loss applied to pairs of views after projecting image features onto the 3D point cloud. Furthermore, by establishing consistent feature fields in both the source and target scenes, they design an energy function that simplifies the process of minimizing feature differences with respect to the end-effector parameters between the demonstration and the target manipulation.

### Strengths
This paper presents a captivating approach to 3D feature learning, involving the creation of a point-cloud-based 3D representation and the utilization of the DINO feature extractor. This 3D representation based on point clouds can enable one-shot dexterous manipulation. As demonstrated by the experimental results, the proposed method exhibits robust performance across various settings.

### Weaknesses
In light of the experimental findings presented in this paper, it is respectfully suggested that the method described may not be particularly captivating. For a more comprehensive critique, kindly refer to the Questions section.

### Questions
### Question 1:
In the contrast learning process, a distance of 1cm is set as the threshold to distinguish between similar and dissimilar parts. Can the authors provide clarification on how they precisely define this distance?
### Question 2:
Is distance truly an effective criterion for distinguishing between similarity and dissimilarity?
### Question 3:
Is there a typographical error in Equation (3)? Why does it contain both an equation symbol and an inequality symbol?
### Question 4:
Additionally, is the pruning process defined in Equation (3) considered reasonable?
### Question 5:
Could this pruning process potentially lead to the removal of critical edge information?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
