# 3D-SPATIAL MULTIMODAL MEMORY

- Decision: Accept
- Avg Score: 6.50
- Scores: 8, 6, 6, 6

## Abstract
We present 3D Spatial MultiModal Memory (M3), a multimodal memory system designed to retain information about medium-sized static scenes through video sources for visual perception. By integrating 3D Gaussian Splatting techniques with foundation models, M3 builds a multimodal memory capable of rendering feature representations across granularities, encompassing a wide range of knowledge. In our exploration, we identify two key challenges in previous works on feature splatting: (1) computational constraints in storing high-dimensional features for each Gaussian primitive, and (2) misalignment or information loss between distilled features and foundation model features. To address these challenges, we propose M3 with key components of principal scene components and Gaussian memory attention, enabling efficient training and inference. To validate M3, we conduct comprehensive quantitative evaluations of feature similarity and downstream tasks, as well as qualitative visualizations to highlight the pixel trace of Gaussian memory attention. Our approach encompasses a diverse range of foundation models, including vision-language models (VLMs), perception models, and large multimodal and language models (LMMs/LLMs). Furthermore, to demonstrate real-world applicability, we deploy M3’s feature field in indoor scenes on a quadruped robot. Notably, we claim that M3 is the first work to address the core compression challenges in 3D feature distillation.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The article proposes a novel approach for video memory combining structural information from Gaussian Splatting with semantic information gathered from foundation models. The main challenge in this approach is the high-dimensionality of the semantic features for encoding in Gaussian splats. This has been addressed in the literature by feature distillation, but the authors argue that this leads to inefficient misaligned distilled features. 
The authors proposed a novel attention approach to extract so-called Principle Scene Component. Experiments on a number of datasets appear to show that the proposed approach compares well in terms of fidelity and efficiency with the state-of-the-art, supporting the authors' claims.

### Strengths
- The efficient integration of structural and semantic features is an important problem for AI, and the proposed method is an interesting contribution. 
- The method appears to perform well on a broad range of measures and experiments. 
- The robotic application is a nice addition.

### Weaknesses
 - The Gaussian Memory Attention component is a central contribution of the paper but is rather briefly discussed in the paper. It would be good to provide a clearer rationale for why this method was chosen and why it achieves the claimed result? How does it compare to standard memory mechanisms (such as in transformers), and what could be the alternative implementations. Specifically, the paper lacks a detailed explanation of how the Gaussian Memory Attention (GMA) module's design choices impact its performance. The rationale behind using a weighted sum of principal scene components based on similarity scores, and how this relates to the knowledge space of the original foundation models' embeddings, needs further clarification. The paper should also discuss the potential limitations of the GMA module, such as its sensitivity to the choice of similarity metric or the potential for information loss during the weighted sum operation.
- Similarly, the article contains an extensive ablation study of the foundation models, but no analysis of the impact of this specific component on performance. It would be good to provide some evidence of that as an ablation study (eg, Gaussian Memory attention vs other attention implementation). This would provide valuable insight into the component's impact on overall performance. The absence of an ablation study for the GMA module makes it difficult to isolate its contribution to the overall performance gains. It is unclear whether the observed improvements are solely due to the GMA module or if other factors, such as the choice of foundation model, play a more significant role. A comparative analysis with other attention mechanisms, such as those used in transformers, would provide a more comprehensive understanding of the GMA module's effectiveness.
- The robotic experiment is interesting but it is unclear how informative it is about real-world applicability. It would be good to discuss possible challenges in scaling the approach to more complex/realistic environments and tasks, and to clarify the limitations of the current implementation as well as the future work that would be required for a real-world application. The current robotic experiment seems to be limited to a controlled tabletop environment. The paper should address the challenges of deploying the proposed method in more complex and dynamic real-world scenarios, such as those involving cluttered environments, occlusions, and moving objects. Furthermore, the paper should discuss the computational cost of the proposed method and its suitability for real-time robotic applications.

### Questions
See the questions above in the weaknesses section, in summary: 
- Can you provide a rationale for Gaussian Memory Attention component and a comparison to standard approaches? 
- Can you provide an ablation study to evidence the impact of this novel component on the system's performance? 
- Can you provide a discussion of the limitations of the approach in the robotic scenario and the outstanding questions and limitations to be overcome for real-world application.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces MultiModal Memory (M3), an integration of 3D Gaussian Splatting (GS) techniques with features from 2D Foundation Models (FMs) that replace standard feature distillation pipelines. The authors introduce two new concepts: a) principal scene components (PSC) which reduces the dimensionality of the FM features without sacrificing quality, thus reducing computational resources for training and storing features, and b) gaussian memory attention (GMA) which proposes to learn queries to memory as gaussian attributes (and not
the FM features themselves), thus dealing with the issue of misalignment between distilled and raw features of previous methods. The proposed memory can store features from multiple FMs, thus allowing a single GS structure to reconstruct multiple different features and solve many vision-language downstream tasks. The authors compare the quality of reconstructed features vs previous approaches in 4 scenes, do ablations in another 2 robotic-related scenes, provide comparisons with downstream tasks for 1 scene, and also provide a
demonstration with a mobile robot.

### Strengths
1. The introduction of Gaussian Memory Attention (GMA) is a novel and interesting way of linking Gaussian \ Splatting techniques with feature distillation. Previous works learn downsampled versions of the target features to reduce memory footprint, and decode them back with MLPs. The downsampled feature is the learned attribute in GS. With GMA, the learned attribute is a query to a memory, which can hold features from multiple foundation models. This allows a single trained GS to reconstruct features from many possible \ foundation models, instead of one GS per foundation model.

2. The introduction of Principal Scene Components (PSC) and the similarity reduction algorithm seems to be able to provide a good balance between memory footprint (#degrees stored in memory) vs. reconstruction quality, according to Table 1.

3. The authors integrate generative foundation models (Llama3v etc.) with their approach, while previous works only consider discriminative features (CLIP, DiNov2 etc.). The authors claim that the reconstructed features can be used directly as visual context to LLMs for generative tasks such as image captioning, which is I believe a great advancement of the distilled feature fields work, although they did not provide demonstrations for such applications.

### Weaknesses
1. The paper misses implementation details and qualitative results for downstream task applications. How to use the reconstructed FM features to do the tasks you show in your Fig.2, namely: image captioning, language grounding and retrieval? Please share some explanation of which feature is used for what task, and how, and provide qualitative comparisons with previous works F-3DGS and F-splat.
 
2. Lacking quantitative comparisons with baselines for downstream tasks. Only Table 4 contains comparisons for 1 scene with grounding task but lacks comparison with F-Splat baseline. I believe the authors need to perform more experiments for downstream tasks for more scenes and compare with both baselines, so the final performance-efficiency tradeoff from the introduction of PSC and attention memory can be appreciated.

 3. Also, currently the paper only shows reconstructed features from their M3 method. I believe the paper would benefit from a comparison of reconstructed features between previous approaches and M3, in order to appreciate qualitatively the effect of introducing the PSC method for reducing feature dimensionality and Gaussian Memory for decoding back the original feature.

 4. There is some confusion regarding the inclusion of the temporal aspect in the memory. The authors name their structure video memory and say that it holds medium-time video clips for static scenes. However, from the method and experiments, it seems that the temporal aspect has not been a focus of the paper, as the scenes are static, and the downstream tasks are only at the image or pixel level (captioning, grounding, etc.). Do the authors mean that the video contains the multi-view collection trajectory of an agent? If that is the case, I believe it should not claim to be a video memory and model the temporal aspect, as the temporal dimension in the video is just the dimension of new views of the same static scene.

 5.  I believe the paper would benefit from better clarity when presenting the method. The authors introduce many concepts by naming them (VG, KS, V) but do not provide input domains for such concepts therefore lacking precision. For example, in line 189, the authors write for a view V ∗ ∈ V, its V ∗ = {v 1 , v 2 , ..., v n }. What is the domain of V and V*? What are the intermediate segments vi? Later, in line 200, they write F ∗ (V) = {E 1 , E 2 , ...E n } for the foundation model features of a scene and say that n is the number of views. This seems a bit contradicting to me, as before they mentioned V* as a particular scene, and n the number of multi-granularity segments of that scene. Which one is it, n is a number of scenes or a number of segments inside a scene? 

MINOR:
 - (line 250) as shown in?
 - Table 4 is mentioned before Tables 2 and 3. Maybe rename?
 - (line 062): [...] may not be be inherently 3D-consistent [...]
 - (line 064): [...] knowledge embbeded in [...]
 - (line 080): [...] outperforms what?

### Questions
1. How to use the reconstructed FM features to do the tasks you show in your Fig.2, namely: image captioning, language grounding, and retrieval? Please share some explanation of which feature is used for what task, and how, and provide qualitative comparisons with previous works F-3DGS and F-splat.

2. Can the authors provide qualitative examples comparing the reconstructed features of M3 with those from previous methods, such as F-3DGS and F-Splat? This would help assess the quality improvement gained through PSC and GMA.

3. Could the authors clarify if the term "video memory" implies the storage of multi-view data in static scenes or if there is an intention to extend this framework to dynamic scenes? If the latter, would the temporal dimension in the memory structure require additional model adjustments?

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper presents a method for integrating foundation model knowledge into a structural representation of the scene (here Gaussian Splatting). The approach is capable of integrating several foundation models' knowledge into Multimodal Memory. To this end, the authors propose Principal Scene Components, i.e. a method of feature reduction based on the assumption that multiple views of the scene contain redundant information. The paper evaluates the performance on a low level in feature space, and on a high level - through a downstream task, including robot deployment.

### Strengths
I believe that the authors of the paper correctly identified the drawbacks of 3D feature supervision through 2D feature maps (i.e. potential loss of information with dimensionality reduction). To this end, the paper proposes a compression scheme for extracted features named principal scene components (PSC). I believe this idea to be sound and interesting. I appreciate that the idea includes a flexible parameter of similarity threshold allowing the user to decide on memory/knowledge trade-off. In principle, the method seems to be trained in a similar way to prior works, making me believe that the proposed memory module can be used interchangeably to prior works, and could be applied to an arbitrary 3DGS work. Another benefit is a significant speed-up with respect to F-3DGS. Qualitative results seem convincing. I believe the use of robot manipulation as the downstream task is a good demonstration of the capabilities of the proposed approach.

### Weaknesses
While I believe the authors propose an interesting method, I see some weaknesses in the paper. Firstly, there are some drawbacks to the experimental setup:
- F-3DGS evaluated their approach through the task of novel view semantic segmentation. I see no reason why this could not be used in this paper as the experiment. This makes comparison between the two methods harder. Similarly, both F-3DGS and F-Splat do language-guided editing. Direct feature comparison is interesting and meaningful, however, we should also adhere to previously used evaluation protocols in order to facilitate fair comparisons.
- Similar to the previous point, I believe it would be beneficial to have some datasets between the proposed method and prior work in common. 
- Further, the paper claims memory efficiency as a part of the method's benefits. Therefore an ablation and comparison to prior work from the memory perspective would be useful.
- There should be a study on whether there exists a correlation between performance, training time, and memory footprint (e.g. quantitative metrics for similar training time to F-3DGS - does M3 reach the same performance or does it plateau; also a comparison between models for the same feature size, etc.).

### Questions
- Do all the methods in comparison use the same underlying 3DGS model?
- Lines 48-49 mention both static scenes and time windows, could you explain that?
- Do you train reconstruction together, or do you start training with colour loss only? Alternatively, is the method sensitive to initialisation? With poor initialisation, the first iteration may be very noisy and rendered features very poor.
- Could you pinpoint the exact component that makes M3 training so much faster than F-3DGS?

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper introduces 3D Spatial MultiModal Memory (M3), a video memory system aimed at retaining visual perception information over medium temporal and spatial scales. M3 employs 3D Gaussian splatting and incorporates multiple foundation models to create a multimodal memory capable of spanning visual details and encompassing a broad knowledge range. The authors address two primary limitations of prior feature splatting methods: high computational demands for storing dense features in each Gaussian primitive and misalignments with foundation model knowledge. M3 innovatively introduces principal scene components and Gaussian memory attention mechanisms to improve the efficiency of storage, training, and inference within the Gaussian Splatting Model. Evaluated across various foundation models, including vision-language and self-supervised models, M3 demonstrates robust performance, with successful deployment on a quadruped robot for grasping tasks, showcasing its practical viability in real-world applications.

### Strengths
The idea is interesting and novel, and this direction is promising for diverse robotic tasks.
The method design makes sense. The figures and algorithm flowchart make the paper easy to understand.
The authors provide comprehensive coparisons in evaluation on M3 features (table 1, 2, 3, 4).

### Weaknesses
My concerns mostly lie on real robot experiments. I think one of the advantage of such feature field (also claimed in paper) is for various downstream robotics manipulation tasks. While, this paper shows a simple example in grasping a duck on the table. It could make this paper much stronger if the authors can demonstrate the promising potential of this study in various practical downstream tasks.
Some example downstream tasks:
1. Geometry-based or semantic-part-based tasks using DINO or diffusion features, such as geometry-based object retrieval/grasping[1, 2], planning objects to the goal configuration[3].
2. Language-guided tasks using CLIP feature, such as like "pick up the red cube and place it on the blue book." (example references: [4, 5])
3. A multi-step task that combines different features, such as "navigate to the kitchen, locate the mug with a cat design, and bring it to the living room table." These examples would showcase how M3 can leverage different types of features for more complex robotic applications.

Some typos: for example, in figure 5, dinov->dinov2. In line 350&351, there are missing parts after `as shown in'.

### Questions
Please see weakness.

### Soundness
3

### Presentation
3

### Contribution
2
