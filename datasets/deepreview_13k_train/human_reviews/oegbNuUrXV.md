# Generalizable Dynamic Radiance Field in Egocentric View

- Decision: Reject
- Scores: 5, 3, 3, 5, 5

## Abstract
We present a novel framework for generalizable dynamic radiance field in egocentric view. Our approach can predict a 3D representation of the physical world at a given time based on a monocular video without test-time training. To this end, we use a contracted triplane as the 3D representation of physical world in an egocentric view at a specific time. To update the explicit 3D representation, we propose a 4D-aware transformer module to aggregate features from monocular videos. Besides, we also introduce a temporal-based 3D constraint to achieve better multiview consistency. In addition, we train the proposed model with large-scale monocular videos in a self-supervised manner. Our model achieves top results in novel view synthesis on dynamic scene datasets, demonstrating its strong understanding of 4D physical world. Besides, our model also shows the superior generalizability to unseen scenarios. Furthermore, we find that our approach emerges capabilities for geometry and semantic learning. We hope our approach can provide preliminary understanding of the physical world in first-person view and help ease future research in computer vision, computer graphics and robotics.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper describes an approach for novel view rendering given dynamic egocentric video inputs. The approach is feedforward without optimization at inference time, and is trained to generalize to unseen scenes. The approach uses a triplane as scene representation, which is subsequently updated with a transformer to incorporate the input frames as well as camera parameters. Qualitative and quantitative evaluation provides evidence of the performance and generalizability of the approach.

### Strengths
Significance: As the authors rightly point out, existing solutions for dynamic NVS generally can not generalize to novel scenes, limiting their practical use scenarios. Therefore, a solution for generalizable, dynamic NVS given first-person video frames can be significant. 

Originality: Though none of the building blocks are new, the technical solution of a triplane representation for dynamic NVS and the refinement of the representation with frame features through a "4D-aware transformer" is sound and novel. 

Clarity: Though missing some details (explained in the next section), the paper is overall well-written, conveys the main ideas well, and is easy to follow.  

Quality: The results are generally consistent with the authors' claim. It is particularly helpful that authors make clear distinctions between dynamic and static scene components, in-domain and out-of-domain samples in the experiments, and also conduct ample ablation studies.

### Weaknesses
I think a major weakness is in the evaluation of the approach, particularly regarding generalization.

Results in Sec.4.1.1 are not quite helpful since the approach is behind a few competing methods and the testing scenes are already seen during training. While no per-scene optimization is needed at inference time, it's possible the network can memorize the scenes to some extent via training.

Results in Sec.4.1.2 provide some insights regarding generalization, but are very limited. Table 2 only shows comparisons with single-view methods on a single dataset. To demonstrate generalization capability, the authors should consider:
* Analyzing results across more diverse testing datasets and scenes;
* Comparison with other multi-view approaches (even if they're static or optimization-based);

Also regarding experiments, it would be valuable to show:
* more distinct views from input views to better understand the limitations
* results and comparisons regarding first-person vs other types of samples.

The paper does not have any analysis nor comparisons regarding latency and speed. This would make clear the efficiency advantage over optimization-based approaches.

Some closely related literature on Gaussian Splatting (GS) is not mentioned, namely
* 4D GS: 
    - 4D Gaussian Splatting for Real-Time Dynamic Scene Rendering
    - Spacetime Gaussian Feature Splatting for Real-Time Dynamic View Synthesis
    - Motion-aware 3D Gaussian Splatting for Efficient Dynamic Scene Reconstruction
    - 3D Geometry-aware Deformable Gaussian Splatting for Dynamic View Synthesis
    - Dynamic Gaussian Marbles for Novel View Synthesis of Casual Monocular Videos
* Feedforward GS: 
    - MVSGaussian, GS-LRM, MVSplat, etc. 

Last but not least, the paper lacks clarity on some key concepts that should be better defined, e.g. 
* How is the initial triplane learned/initialized?
* The concept of feature "similarity" is used in a few places but is not properly defined. 
* "epipolar feature" appears to be simply projected pixel features. If so, the use of term "epipolar" is uncommon and confusing.  
* "time bias" on L200 is not defined.

### Questions
Please see the suggestions made in the section above, regarding results, analysis, and clarity. Most critically, I think a more thorough experimental analysis of the generalization capability can significantly improve the paper.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes a generalizable dynamic radiance filed in an ego-centric view. Differing from the common NeRF literature, which requires test-time optimization and object centric-view, the method predicts a neural representation from ego-centric image sequence without test-time training. For this purpose, the paper newly proposes a 4D-aware transformer consisting of a View-Attention Module, Axis-Attention Module, and Plane-Attention Module. Using the method, the paper trains a model on a number of training datasets (NVIDIA Dynamic Scenes, EPIC Fields, and nuScenes) and tests on nuScene (test) and RealEstate 10K. However, the performance does not outperform previous related works, and the method has a number of questions in terms of generalization and dynamic representation.

### Strengths
S1. The paper proposes a 4D-aware transformer consisting of a View-Attention Module, an Axis-Attention Module, and a Plane-Attention Module.

### Weaknesses
W1. The design philosophy of the proposed framework for generalization.

* The paper conducts generalization experiments by training the triplane on several training datasets (NVIDIA Dynamic Scenes, EPIC Fields, and nuScenes) and testing on nuScene (test) and RealEstate 10K.
However, it is questionable whether the proposed framework is suitable for dynamic radiance field generalization.
Originally, the learnable triplane aimed to learn three feature planes to embed the target scene context and its temporal change.
However, if the target training set gets diverse, the target of the learnable triplane is unclear. 
In the current training scenario, what is the learning goal of the learnable triplane, and what do they learn? Specifically, how does the triplane representation adapt to different scene geometries and dynamic elements when trained across such varied datasets? The paper lacks a clear explanation of how the shared triplane representation can effectively capture the nuances of both indoor and outdoor environments, as well as the diverse dynamic motions present in the training data. The concern is that the triplane might be learning a generic representation that is not specific enough to handle the complexities of individual scenes, thus hindering its generalization capabilities.

* Also, it would be great to discuss whether the current framework is suitable for dynamic radiance field generalizatoin. 
The current frameworks seem unsuitable for radiance field generalization to handle totally unseen and out-of-distribution domain data, such as mountains, caves, or endoscopes. The method's reliance on datasets with relatively similar scene structures (e.g., indoor and common outdoor scenes) raises concerns about its ability to generalize to truly novel environments with drastically different geometric and textural characteristics. The paper should address how the proposed approach would perform in scenarios where the underlying scene structure and dynamic patterns differ significantly from the training data.

W2. Performance improvement is not significant.

* In novel view generation in both the seen and unseen domains, the proposed method doesn't outperform the pseudo-generalized methods MonoNeRF Tian et al. (2023) and PGDVS Zhao et al. (2024).

* Also, the paper uses nuScene (test) and RealEstate10K datasets as unseen datasets. However, in terms of domain gap, the training set already includes nuScene (training) and common indoor and outdoor scenes. So, the network is already aware of similar structures, such as the common load scenario and indoor building scenario. The domain gap between the training and testing (unseen) dataset is quite small. If the method is truly generalizable, it should be tested with totally out-of-distribution data. The choice of evaluation datasets does not adequately demonstrate the generalization capabilities of the proposed method. The 'unseen' datasets share significant similarities with the training data, making it difficult to assess the method's ability to handle truly novel scenarios. A more rigorous evaluation would require testing on datasets that exhibit substantial differences in scene geometry, texture, and dynamic patterns compared to the training data.

W3. Novelty in terms of generalization and dynamics representation

* The paper insists that it proposed a generalizable dynamic radiance field estimation framework. For this purpose, the paper proposes a new 4D-aware transformer consisting of a View-Attention Module, an Axis-Attention Module, and a Plane-Attention Module. However, their strength in terms of generalization and dynamics representation is unclear.
It would be great to prove the proposed 4D-aware transformer's effectiveness in both generalization and dynamics representation by comparing it to previous methods. For instance, compared to previous dynamic content embedding methods (Li et al. (2023); Tian et al. (2023)), is the View-Attention Module superior to representing dynamic content? The paper needs to provide a more detailed analysis of how each module contributes to the overall performance, particularly in terms of handling dynamic scenes and generalizing to unseen views. It is not clear how the proposed attention mechanisms specifically address the challenges of dynamic scene representation, and the paper lacks a comparative analysis to demonstrate the superiority of the proposed approach over existing methods.

### Questions
Please answer the weakness part.

### Soundness
2

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
The paper proposes a framework for creating generalizable dynamic radiance fields from first-person (egocentric) views, enabling view synthesis of dynamic scenes without test-time training. Using a 4D-aware transformer with dedicated attention modules for understanding temporal, spatial information with regard to the camera parameters, the model aggregates features from monocular videos to form a 3D triplane representation, achieving robust generalization across diverse, unseen scenes.

### Strengths
- This paper introduces a 4D transformer, that can be generally used in view synthesis.
- This paper conducted extensive experiments on various datasets, to demonstrate the effectiveness and generalizability of the proposed method.

### Weaknesses
 - The methodology part is not straightforward to understand.
- The methodology is not aligned to the title or motivation of this paper, focusing on 'egocentric views'
- Experimental results are far from 'comparable' to the previous approaches. I understand that previous algorithms optimize view synthesis scene-wise, so the state-of-the-art performance is not expected. However, showing mid-low performance on PSNR and SSIM metrics in table 3, while calling it 'on-par' is not agreeable.
- This paper includes shallow ablation study. Only module-wise plug-in-plug-out ablation is not enough to fully demonstrate the motivation and effectiveness of the suggested modules. This is where the authors can truly argue that their 4D transformer is actually valid in understanding 4D scene information, even though it lacks performance compared to previous algorithms with scene-specific training.
- Overall qualitative results are not curated well to present the effectiveness of the proposed method.

### Questions
- Can you explain what exactly the suggested attention modules in 4D transformer are trying to 'learn'? For example, what is 'axis-attention', implicitly? What does it mean, and how does it help to understand 4D scene?
- Can you explain how the suggested modules are specifically designed for 'egocentric' views?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper proposes a generalizable dynamic radiance field by using attention across view, axis and plane.

### Strengths
Propose a attention-based attention to improve triplane for generalizable task.

### Weaknesses
The generalizability is tested on only one dataset. While the main focus is on generalizability, the primary results table (Table 1) does not reflect this aspect.

The performance of the proposed method, as presented in Table 1, appears limited when compared to other methods. This is particularly concerning given that the model is trained on a diverse set of scenes from NVIDIA, EPIC, Plenoptic, and nuScenes. The discrepancy between the training data diversity and the achieved performance raises questions about the effectiveness of the proposed approach in fully leveraging the available data. It is unclear why the model's performance does not scale with the breadth of the training data.

Missing reference: 
DynPoint: Dynamic Neural Point For View Synthesis
NeuPhysics: Editable Neural Geometry and Physics from Monocular Videos

### Questions
Could the algorithm be evaluated on additional datasets to assess its generalizability?

Additionally, in Table 1, it states, "Our model is trained on scenes from NVIDIA, EPIC, Plenoptic, and nuScenes (train set)" (Line 370). Why does the performance remain limited compared to other methods?

Missing reference: 
DynPoint: Dynamic Neural Point For View Synthesis
NeuPhysics: Editable Neural Geometry and Physics from Monocular Videos

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper studies the generalizable model for dynamic scene rendering. It uses triplane as scene representation, and proposes view-attention, axis-attention and plane-attention modules to optimize the triplane features. Experimental results on RealEstate10K and Nvidia Dynamic Scene datasets show the proposed method achieves comparable results without any finetuning on dynamic scenes compared to other methods that all require per-scene optimization.

### Strengths
It could achieve good dynamic scene rendering performance without flow and depth supervision.
It achieves better generalization ability compared to MonoNeRF and PGDVS.

### Weaknesses
After carefully reading the method section, I'm still confusing how the proposed method processes dynamic scenes over time. Line 139 says that the model could render novel views at target time $t_1$, but does not mention how $t_1$ is determined and introduced into the model. Figure 1  does not present how the model could generate novel views of dynamic scenes at different timestamps either.

Besides, since this paper uses 3D triplane representation without a time axis and uses all the video frames to train the 3D representation, the time-variant motion features may be mixed into one triplane representation, which is quite confusing to use the model to render novel views at different timestamps.

The paper claimed that it could learn semantic information with the proposed pipeline, but it only tests its image encoder performance on image classification tasks, which is somehow weak. Semantic learning of dynamic scenes should be demonstrated by challenging semantic tasks like segmentation, tracking, completion, and generalization in Semantic Flow [1] paper.

The paper uses many non-egocentric view datasets for evaluation. It is weird to conduct experiments on these dataset as the goal of the paper is to build generalizable dynamic radiance fields in egocentric view. I want to know why.

### Questions
Some citation formats in this paper seem wrong. Please double-check citation formats.

### Soundness
2

### Presentation
3

### Contribution
2
