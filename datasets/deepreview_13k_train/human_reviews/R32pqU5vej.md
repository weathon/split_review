# DH-Fusion: Depth-Aware Hybrid Feature Fusion for Multimodal 3D Object Detection

- Decision: Reject
- Scores: 5, 5, 5, 5, 5

## Abstract
State-of-the-art LiDAR-camera 3D object detectors usually focus on feature fusion. However, they neglect the factor of depth while designing the fusion strategy. In this work, we for the first time point out that different modalities play different roles as depth varies via statistical analysis and visualization. Based on this finding, we propose a Depth-Aware Hybrid Feature Fusion (DH-Fusion) strategy that guides the weights of point cloud and RGB image modalities by introducing depth encoding at both global and local levels. Specifically, the Depth-Aware Global Feature Fusion (DGF) module adaptively adjusts the weights of image Bird's-Eye-View (BEV) features in multi-modal global features via depth encoding. Furthermore, to compensate for the information lost when transferring raw features to the BEV space, we propose a Depth-Aware Local Feature Fusion (DLF) module, which adaptively adjusts the weights of original voxel features and multi-view image features in multi-modal local features via depth encoding. Extensive experiments on the nuScenes and KITTI datasets demonstrate that our DH-Fusion method surpasses previous state-of-the-art methods. Moreover, our DH-Fusion is more robust to various kinds of corruptions, outperforming previous methods on nuScenes-C w.r.t. both NDS and mAP.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper is based on the observation that LiDAR points on a target decay more significantly with distance compared to camera pixels, leading to information loss at greater distances in LiDAR data. Consequently, in multi-modal detection, more emphasis should be placed on camera data to compensate for this loss. Unlike traditional transformer-based methods, this paper introduces a novel approach to "explicitly" leverage distance information, enhancing cross-attention between modalities. The proposed method discretizes target distance and uses positional encoding within a transformer framework to incorporate this information into both global and local feature fusion. Experimental results on the KITTI and nuScenes datasets demonstrate that the proposed approach outperforms baselines with comparable backbones.

### Strengths
- The paper offers a clear, statistically grounded analysis that highlights the disparity in information decay between camera pixels and LiDAR points, justifying the architectural adjustments. The experimental validation supports the efficacy of the proposed solution, making the paper well-structured and cohesive.
- The figures in the paper effectively clarify the architecture, aiding in the comprehension of the proposed methodology.
- The proposed approach achieves superior results on both KITTI and nuScenes datasets, surpassing baselines with similar backbones.

### Weaknesses
 - Although the paper focuses on using positional encoding to make LiDAR query features aware of target distance from the ego vehicle, similar methods (e.g., BEVDet, BEVFormer) have already employed positional encoding. The main novelty here is its application in multi-modal detection for autonomous driving, which limits its originality.
- For a paper emphasizing depth encoding in multi-modal detection, exploring additional variations of positional encoding, such as incorporating learnable parameters or different encoding functions (e.g., sinusoidal vs. radial basis functions), would provide more comprehensive contributions to the field. The current approach, while effective, feels somewhat limited in its exploration of encoding possibilities.
- There is a lack of analysis on whether existing methods implicitly utilize depth information through learned feature representations and why the explicit use of distance, as proposed, might be preferable. A more thorough comparison, perhaps through ablation studies or feature visualization, would strengthen the justification for the proposed method.
- Excessive detail on model structure, particularly the specifics of the transformer layers and attention mechanisms, detracts from the primary novelty of the proposed method, which is the distance-aware fusion. This level of detail could be streamlined to better highlight the core contribution.
- It is unclear how much additional computation the method requires to achieve improved performance over the baseline. The paper should include a detailed analysis of the computational overhead, including parameters, FLOPs, and inference time, to provide a complete picture of the method's practical implications.

### Questions
Further exploration of positional encoding, particularly by incorporating multi-modal detection priors, would enhance the paper's novelty. Expanding the method to address a more general problem would also be beneficial.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The paper proposes a depth-aware LIDAR-Camera fusion method, including a depth-aware glocal feature fusion (DGF) module and a depth-aware local feature fusion (LGF) module,  for 3D object detection. Extensive experiments were conducted to validate the effectiveness of the proposed method on both the nuScenes and KiTTI datasets. The core contribution is injecting the depth information into the process of cross-modal feature fusion.

### Strengths
1. The presentation, including the writing and figures, is clear.

2. The motivation and the way to inject depth information are straightforward, easy to understand.

3. Extensive experiments and analyses were conducted to show the effectiveness of each component.

### Weaknesses
1. The ablation study on the effectiveness of depth encoding is conducted separately on DGF and DLF, but a lower baseline might yield larger gains. Could you provide results for the entire model without depth encoding, i.e., DH-Fusion-base without depth encoding?

2. Based on the analysis in Lines 044–053 of the introduction, it seems that the detector should focus more on LiDAR features at close range and on image features at longer range. However, in the proposed method, the output of the depth encoder is multiplied by LiDAR BEV features in DGF and by cross-modal instance features in DLF. Is this design consistent with the findings mentioned above? Additionally, Section 4.6 visualizes the attention weights in DGF, but not the output of the depth encoder or the feature multiplied by it. How can the attention weights applied to the image BEV features in the DGF module support the analysis in Lines 044–053?

3. Why not compare with more recent works from ECCV? For example, SparseLIF achieves better results, with 77.0% NDS on the nuScenes validation set. The submission deadline for ICLR is after the ECCV conference.

### Questions
See the weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper presents a method that uses depth information to enhance the fusion of LiDAR and camera data in 3D object detection. The author proposes to adaptively adjust the fusion weights of the two modalities based on object depth, addressing limitations in prior methods that overlook depth variations. This approach integrates depth-aware fusion at both global and local levels, preserving critical details and improving detection accuracy. Experiments demonstrate that DH-Fusion outperforms existing methods on multiple datasets and shows greater robustness to data corruption.

### Strengths
The paper introduces a novel depth-aware fusion approach for 3D object detection that outperforms existing methods on multiple datasets and shows greater robustness to data corruption.

Extensive experimental design with extensive benchmarks on multiple datasets supports its effectiveness. Ablation studies clearly validate the contributions of each module.

The paper is generally well-organized with helpful visual aids, though some mathematical sections could be simplified for accessibility.

### Weaknesses
1. While DH-Fusion introduces a depth-aware module in fusion weights, it applies a similar strategy across the entire depth range, which might not be optimal. Objects at very close or far distances likely require different levels of emphasis on specific feature types (e.g., closer objects may benefit from high geometric fidelity in LiDAR, while far objects may rely more on image data). Specifically, the method does not account for the varying reliability of depth estimates themselves; at longer ranges, depth estimates become less precise, and relying on them to modulate fusion weights might introduce noise rather than signal. A more nuanced approach would consider the uncertainty of depth measurements when adjusting fusion parameters.

2. While the method offers some contributions, its overall originality appears moderate, as it primarily builds upon established approaches such as LoGoNet and IS-Fusion, with the addition of a depth-guided weighting mechanism for fusion. This depth-aware module, while beneficial, seems to be an incremental improvement rather than a fundamental shift in how multimodal 3D object detection is approached. The core architecture still relies heavily on existing fusion strategies, and the depth-aware weighting could be seen as a relatively straightforward extension of existing techniques.

3. The paper includes a comparative analysis of speed, showing that DH-Fusion achieves relatively high efficiency. However, the reason behind this speed advantage is unclear, as the authors have not provided an in-depth breakdown of how DH-Fusion’s architecture contributes to these performance gains. The paper lacks a detailed computational complexity analysis, making it difficult to understand whether the speed improvements are due to architectural choices or implementation details. A more detailed analysis of the FLOPs and memory access patterns would be necessary to substantiate the claims of efficiency.

4. Additionally, in Table 9, it would be valuable to see a more comprehensive comparison of the model’s performance on smaller, more distant objects, where the benefits of depth-aware fusion are likely to be more pronounced. The current analysis does not provide a granular enough view of performance across different object sizes and distances, which is crucial for evaluating the effectiveness of the proposed depth-aware fusion strategy. A breakdown of performance by object size and distance would allow for a more thorough assessment of the method's strengths and weaknesses.

### Questions
Please refer to the weakness.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper tackles the challenge of effectively combining information from LiDAR and camera data for 3D object detection, which is crucial for applications like autonomous driving. Traditional fusion methods often overlook depth, despite its importance in balancing the strengths of both LiDAR and RGB image data at different ranges. To address this, the authors introduce a Depth-Aware Hybrid Feature Fusion (DH-Fusion) method, which leverages depth encoding to dynamically adjust the contributions of LiDAR and camera features.

The fusion is done on two levels: globally, where the depth-aware model prioritizes different features depending on the object's distance, and locally, through a Depth-Aware Local Feature Fusion (DLF) module. The DLF module specifically enhances details in local regions by balancing original voxel data and multi-view image features, guided by depth encoding. This approach not only boosts detection accuracy but also improves robustness across varying conditions, as demonstrated in experiments on challenging datasets.

### Strengths
1. Examining image and point cloud information variability across different depth layers offers valuable insights and may inspire future research. To this end, the paper introduces a novel approach to 3D object detection by incorporating depth information into the fusion of LiDAR and camera features—a crucial but often overlooked factor in previous fusion methods. This depth-aware approach enables more adaptive and accurate fusion, particularly enhancing the detection of objects at varying distances.  

2. The study of robustness to data corruption is particularly compelling. The proposed DH-Fusion method is rigorously evaluated against various types of corruption, demonstrating improved resilience compared to previous models. This robustness makes the model more suitable for real-world applications, where data quality often fluctuates due to environmental factors like weather conditions and sensor noise.

### Weaknesses
1. The novelty in the fusion strategy is marginal.   The proposed Depth-Aware Hybrid Feature Fusion (DH-Fusion) strategy, while unique in its dual-level (global and local) application, still follows the intermediate fusion trend that has been widely adopted. Intermediate fusion methods, which integrate LiDAR and image data at the feature level, have become mainstream. The specific structure of DH-Fusion, including using transformer-based encoders for feature interaction, is similar to other recent methods, such as BEVFusion and TransFusion, which also use transformers or other deep networks to perform feature alignment and fusion. The learned nature of these works indicates that the optimal fusion strategy is learned from data. That means that they can find a fusion mechanism that treats of variability of point clouds and image information across different depth layers if that information is critical. Thus it is unclear how much the explicit introduction of depth information can boost learning particularly when there is sufficient data.  

2. The performance improvement is modest. As shown in Table 4, the gains range from only 1 to 2 percent, indicating that depth guidance may not be a decisive factor in enhancing this fusion approach. Interestingly, the improvements in corrupted data (Table 3) are more pronounced. However, the paper does not thoroughly explore why the introduced fusion strategy is particularly effective in this context.

3. Limited exploration of depth information usage. While the paper applies depth encoding to adjust feature weights, its approach is straightforward, relying on sine and cosine functions for positional representation. Other potential methods for encoding depth, such as adaptive or learning-based encoding techniques, are not investigated. Additionally, to better understand the fusion mechanism, it would be helpful to visualize the fusion weights through case studies, demonstrating how image and LiDAR features are combined. Such visualizations could provide stronger support for the motivation behind the proposed approach.

### Questions
1. How does depth-guided fusion contribute to performance improvement compared to other learning-based fusion mechanisms without depth?   What are the unique advantages over existing learning-based fusion techniques where the fusion weights are learned from data? 
2. Was there any experiments with alternative depth encoding methods, and if so, what were the results? Could learning-based or adaptive depth encoding improve performance? 
3.  Was there any investigation into early or late fusion methods in combination with depth encoding? How would these methods impact the overall model’s effectiveness?
4. Could depth guidance be especially beneficial in scenarios with environmental noise (e.g., fog or rain)? What are the specific scenarios where depth guidance provides the most benefit? What is the reason behind this? 
5. Visualizations of the fusion weights in different scenarios (e.g., near vs. far objects) offer additional insights. How do these weights change under different environmental conditions? 
6. Were there any limitations observed when applying DGF and DLF across different object sizes or distances? For instance, does depth-aware fusion perform equally well for small or partially occluded objects?

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
4

### Summary
The paper proposes DH-Fusion, a depth-aware feature fusion strategy for LiDAR-camera 3D object detection, which dynamically adjusts modality weights using depth information at both global and local levels. By incorporating depth encoding, the method balances the contributions of point cloud and RGB image data, improving detection accuracy and robustness against data corruptions. Extensive experiments on datasets like nuScenes and KITTI demonstrate that DH-Fusion outperforms state-of-the-art methods.

### Strengths
1)The proposed Depth-Aware Hybrid Feature Fusion (DH-Fusion) strategy is well justified, using statistical analysis to show the varying roles of modalities across different depths. This is meaningful to the field of multimodal 3D object detection.
2)This paper includes comprehensive experiments on nuScenes, KITTI, and nuScenes-C datasets, which provide effective evidence of the method’s effectiveness and robustness.

### Weaknesses
1)The proposed fusion method depends on BEV features, which is not general for some point-based, voxel-based in 3D features.
2)The explanation of why depth encoding is more effective for local features could be more comprehensive. The authors should consider adding a theoretical rationale or hypothesis to elucidate why local features exhibit heightened sensitivity to depth variations.
3)It would be important to discuss any potential limitations or key differences compared to existing methods. Additionally, since the method is considerably more complex than BEVFusion, providing metrics on computational efficiency(parameters, GFLOPs, latency) and accuracy would strengthen the evaluation and offer a clearer understanding of the trade-offs involved.
4)The ablation study results are informative; however, more detailed experiments would be beneficial. For instance, assessing the performance of each component under diverse weather conditions in the nuScenes-C dataset could yield deeper insights into the robustness and adaptability of DH-Fusion.
5)The application of the proposed method to the KITTI dataset needs further clarification. Specifically, the baseline used should be explicitly identified, and the improvements brought by each proposed module should be clearly quantified and discussed.

### Questions
See the weaknesses

### Soundness
2

### Presentation
3

### Contribution
2
