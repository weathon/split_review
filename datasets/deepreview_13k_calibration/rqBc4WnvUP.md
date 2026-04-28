# Multi-view Object-Centric Learning with Identifiable Representations

- Decision: Reject
- Avg Score: 3.50
- Scores: 5, 3, 3, 3

## Abstract
Modular object-centric representations are key to unlocking human-like reasoning capabilities. However, addressing challenges such as object occlusions to obtain meaningful object-level representations presents both theoretical and practical difficulties. We introduce a novel multi-view probabilistic approach that aggregates view-specific slots to capture *invariant content* information while simultaneously learning disentangled global *viewpoint-level* information. Our model resolves spatial ambiguities and provides theoretical guarantees for learning identifiable representations, setting it apart from prior work focusing on single-view settings and lacking theoretical foundations.  Along with our identifiability analysis, we provide extensive empirical validation with promising results on both benchmark and proposed large-scale datasets carefully designed to evaluate multi-view methods.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes a multi-view probabilistic approach that aggregates view-specific slots to capture invariant content information while learning disentangled global viewpoint features, advancing modular object-centric representations for human-like reasoning. The model addresses spatial ambiguities and provides theoretical guarantees for identifiable learning, outperforming prior single-view methods lacking theoretical support. The authors also present an identifiability analysis and extensive empirical validation, demonstrating strong performance on both benchmark datasets and newly designed large-scale multi-view datasets.

### Strengths
1. The paper provides identifiability guarantees specifically for multi-view scenarios, addressing a limitation in existing work that mainly focuses on single-view setups. This broadens the applicability of object-centric representations to more complex settings.
2. The proposed model is viewpoint-agnostic, requiring no additional view-conditioning information. This design improves the model's robustness and makes it adaptable across various viewing conditions without extra supervision.
3. The authors empirically validate the model’s scalability by testing it on large-scale datasets and using complex decoders, such as transformer-based decoders. This shows the model’s capacity to handle increasing data volume and decoder complexity effectively, which is crucial for practical applications.

### Weaknesses
1. The use of the Expectation-Maximization (EM) algorithm for fitting the GMM in Figure 2 is mentioned, but it’s unclear how this fits into the broader model architecture. Is this process repeated for each view, or is it a one-time initialization? Including a step-by-step outline or flowchart for the EM algorithm application might make this more transparent. Specifically, it's unclear if the GMM parameters are learned jointly across views or independently for each view, and how the learned GMMs are then used in the subsequent stages of the model. This lack of clarity makes it difficult to assess the computational implications and the overall coherence of the approach.
2. The description of viewpoint-specific slots and how they are represented as GMMs (Gaussian Mixture Models) in the multi-view context is technical but could benefit from more details. For instance, how are these slots initialized, and does the model assume independence between slots? Additionally, it would be helpful to discuss the computational implications of fitting GMMs for each view, especially in large-scale settings. It is not clear how the parameters of these GMMs are updated during training, and whether the updates are performed in a batch-wise manner or individually for each view, which can significantly impact the model's performance and scalability. Furthermore, the assumption of independence between slots needs to be justified, given that slots might represent related object parts.
3. The explanation lacks details on the computational complexity of the aggregate GMM model, particularly as it scales with the number of views and components. It would be useful to discuss how computational tractability is ensured and any potential limitations in terms of scalability, given large datasets or high-dimensional view spaces. Specifically, the paper should address the computational cost of merging GMMs from different views, and how this cost scales with the number of views and the number of components in each GMM. This is crucial for understanding the practical applicability of the proposed method.
4. Some expressions and details need further refinement to ensure clarity. For instance, in line 214, "...parameters described in 6" should refer to Equation 6 and should be written as "...parameters described in Equation 6."

### Questions
Please see weakness.

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
4

### Summary
This paper extends PSA to multi-view scenes and proposes a multi-view object-centric learning model (MVPSA) using identifiable representations. By aggregating all object representations in all multi-view scenes, identifiable representations across multi-view scenes are obtained. In addition, this paper proposes some theoretical proofs of recognizability. Experimental results on several synthetic datasets demonstrate that the model can achieve recognizable object-centric representations without relying on additional viewpoint information.

### Strengths
1.	This paper extends PSA from a single-view setting to a multi-view setting and provides certain theoretical guarantees.
2.	This paper verifies the performance and robustness of the proposed method in multi-view scenarios on multiple datasets.

### Weaknesses
1.	This paper seems to simply apply the PSA framework to multi-view scenarios through a Hungarian matching module and lacks innovation in both motivation and methodology.
2.	Some of the theoretical proofs and theorems are difficult to understand. It would be beneficial for the authors to provide more detailed explanations or examples to improve the readability of these proofs.
3.	Based on the visualization results presented in Appendix F, the segmentation and reconstruction performance of the proposed method appears to be less than expected, which raises concerns about the overall effectiveness and significance of the method. Specifically, the segmentation masks in Figure 9 of Appendix F often only capture parts of objects or merge multiple objects into a single segment, indicating poor performance in complex multi-view scenes.
4.	Some important works are missing for comparison (see Q5)
5.	The paper lacks a detailed description of how viewpoint representations are learned and used. The method models viewpoint information, but it's unclear how this information contributes to object-centric representation learning. The absence of visualization results for scene images generated through viewpoint interpolation and sampling further weakens the validation of the learned viewpoint representation.

### Questions
1.	In Appendix C.2, it mentions that each scene has 5 viewpoints and 24 frames. What is the difference between viewpoints and frames?
2.	The formula in Line 213 of the main manuscript appears to have a typo. Are the brackets incomplete?
3.	The proposed method specifically models viewpoint information but does not seem to be used for object-centric representation learning. This makes one question the point of modeling perspective representation.
4.	How do the authors ensure that the Hungarian algorithm can correctly match all objects across viewpoints without falling into local optimality during training?
5.	Can the authors provide experimental results comparing the proposed method with other object-centric methods based on multi-view scenarios, such as SIMONe[1], OCLOC[2], etc.?

[1]	Kabra R, Zoran D, Erdogan G, et al. Simone: View-invariant, temporally-abstracted object representations via unsupervised video decomposition[J]. Advances in Neural Information Processing Systems, 2021, 34: 20146-20159.

[2]	Yuan J, Chen T, Shen Z, et al. Unsupervised Object-Centric Learning From Multiple Unspecified Viewpoints[J]. IEEE Transactions on Pattern Analysis and Machine Intelligence, 2024.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper proposes a multi-view object-centric learning model (MVPSA) using identifiable representations, addressing challenges with occlusion and viewpoint ambiguities. MVPSA extends PSA into multi-view setting, aggregates content across views while separating viewpoint information. Theoretical guarantees for identifiability are provided, alongside extensive empirical results on synthetic datasets, demonstrating the model's ability to achieve identifiable object-centric representations without relying on additional viewpoint information.

### Strengths
1.	The paper introduces an object-centric learning method to address occlusion and spatial ambiguity in multi-view settings without relying on viewpoint conditioning, extending identifiability guarantees from single-view setups to multi-view settings.
2.	Both theoretical and empirical analyses are provided to support the model's identifiability claims. The extensive experiments conducted on multiple synthetic datasets, including the newly introduced MV-MOVI-C and MV-MOVI-D, validate the model's performance and robustness in various scenes.

### Weaknesses
1.	The approach is primarily based on the PSA framework, which lacks sufficient innovation, even though it extends the single-view method to a multi-view setting. The core mechanism for aggregating information across views, which appears to be a simple convex combination of view-specific slot representations, does not introduce significant novelty. The method seems to rely heavily on the existing PSA architecture, with the multi-view aspect being a relatively straightforward extension rather than a fundamental rethinking of the problem.
2.	The text in the figures is too small, making it difficult to read and comprehend the information presented.
3.	The related work section lacks recent methods for object-centric representation learning in multi-view settings, such as SIMONe[1] and OCLOC[2]. This omission makes it difficult to assess the novelty and performance of the proposed method in the context of the current state-of-the-art.
4.	The proposed dataset has only 3,000 scenes, which raises questions about calling it "large-scale." Compared to existing datasets like MOVi-C and MOVi-D, the number of scenes and object diversity appear limited, which could restrict the generalizability of the findings.

### Questions
1.	The proposed dataset has only 3,000 scenes, which raises questions about calling it "large-scale." Why it is considered large-scale compared to other datasets?
2.	I have tried extracting object representations from each viewpoint image using a single-view model, and I found that using Hungarian matching directly can lead to errors if an object is heavily occluded or completely hidden from one viewpoint. Does the model in this paper face this issue, and how might it be addressed?
3.	Judging from the visualization results in Appendix F, the segmentation and reconstruction effects of the proposed method are defective. Can the author analyze the reasons for the inferior results?
4.	Could the authors explain the purpose of the following proposed method in modeling viewpoint information separately?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper introduces a novel approach to learning object-centric representations that can handle challenges such as object occlusions. The proposed, theoretically guaranteed multi-view probabilistic method could jointly capture invariant content information and disentangled global viewpoint-level information. Experiments are conducted to justify the effectiveness of the proposed method.

### Strengths
- The paper addresses an important topic of multi-view object-centric representation learning.
- The theoretical justification of the proposed method is solid and easy to follow.

### Weaknesses
There are no concerns regarding the theoretical justification of this paper. However, due to the extremely poor empirical validation, the effectiveness of the proposed method cannot be justified. The authors only test their models on very simple scenes such as CLEVR or MOVi. In these scenarios, given multi-view images, it would be intuitive to leverage unposed 3D object-centric learning methods (e.g., [1]) or use few-view calibration methods like DUSt3R [2] to calibrate these scenes and then apply 3D object-centric learning methods (e.g., [3, 4, 5]) to extract per-object representation and obtain highly accurate object segmentation results. However, the authors did not provide a comparison between the proposed method and these previously established approaches, all of which fall under the category of direct inference. Furthermore, if per-scene optimization is permitted, one could even employ few-shot NeRF and Gaussian Splitting methods to first build a scene representation and then use segmentation models (e.g., [6]) to learn per-object representation and achieve scene segmentation.

Although the authors claim that the problem they tackle, namely multi-view object-centric learning, is a step forward, they overlook the internal difficulty of single-view object-centric learning, which is handling occlusion between objects. This paper sidesteps this challenge by utilizing multi-view information. While this is acceptable, as previous literature [1, 6] also considers multi-viewpoint setups, those works focus on real-world, in-the-wild scenes, unlike the simple synthetic scenes considered in this paper. Unsupervised object-centric representation learning on multi-view CLEVR or MOVi datasets is nearly a solved task [4, 5], so it is strongly recommended that the authors consider more complex datasets, such as Kitchen-Shiny [5], OCTScenes [8], or ScanNetv2 [9]. Thus, transitioning from single-view to multi-view settings while keeping the evaluation datasets the same might be considered a step backward.

### Questions
See the weaknesses section. The reviewer believes the experiments of this paper cannot verify the effectiveness of the proposed method and strongly recommends the authors include experiments on more complicated, in-the-wild scenes, as mentioned above.

### Soundness
2

### Presentation
3

### Contribution
2
