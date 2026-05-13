# 3D Perception with Differentiable Map Priors

- Decision: Reject
- Scores: 3, 6, 5, 3

## Abstract
Human drivers rarely navigate where no person has gone before. After all, thousands of drivers use busy city roads every day, and only one can claim to be the first. The same holds for autonomous computer vision systems. The vast majority of the deployment area of an autonomous vision system will have been visited before. Yet, most computer vision systems act as if they are encountering each location for the first time. In this work, we present Differentiable Map Priors, a simple but effective framework to learn spatial priors from historic traversals. Differentiable Map Priors easily integrate into leading 3D perception systems at little to no extra computational costs. We show that they lead to a significant and consistent improvement in 3D object detection and semantic map segmentation tasks on the nuScenes dataset across several architectures.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper presents an approach to learn spatial priors from geolocations. Specifically, the global map is represented as a multi-resolution hap map, which can be incorporated into an existing 3D detection architecture. Experimental results on the nuScenes dataset are reported.

### Strengths
The proposed map prior leads to slightly better 3D object detection results on the nuScenes dataset.

### Weaknesses
1. The motivation of this paper is to use the historical traversals of autonomous vehicles to improve the 3D scene understanding task (line #16, line #33, etc). The proposed approach, however, does not use the historical information at all. It simply uses the geolocation within the global map to learn point-wise embeddings. More elaborations are needed here.

2. The comparison with the prior work NMP is problematic. The motivation of NMP is to use the historical information to improve the downstream task. The learned prior serves as an external memory module, which can be learned and applied to both training and inference stages separately. Using the training prior during evaluation breaks the setting of NMP and makes it unnecessarily ineffective. And in the NMP paper, no 3D object detection experiments are conducted. It is not clear how it is adapted to such a task in this paper.

3. The introduction is incredibly short. It is not clear how the proposed approach is different from previous approaches. As a result, it is hard to comprehensively gauge the significance of the proposed approach. A significant revision of the paper is needed.

### Questions
1. Why can the proposed map prior improve the object detection? Intuitively, it only learns prior knowledge based on the geolocation only. Why can it be useful? Showing more analysis and discussions would be very useful.

2. How is NMP adapted for the object detection task? And how can the proposed approach work for map segmentation?

3. In line #40, it is claimed that the authors "incorporate DMP into three distinct multi-view perception stacks". What does "stacks" means here?

### Soundness
1

### Presentation
1

### Contribution
1

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The manuscript proposes to leverage the fact that autonomous vehicles (AV) will be deployed in areas that are and will be extensively observed during previous trips. That information is available during training and should allow learning priors over the map that can be leveraged during inference when the vehicle is deployed. The idea is to learn a world-aligned sparse, multi-resolution feature representation of the environments during training time by simply backpropagating into those features during normal training. During inference the learned features are retrieved given the vehicles location and fed into the 3D perception system as priors. Two key architectures are investigated: BEV-based systems and DETR-style Transformer detectors. Both show improvement in their performance when map prior information is available. Encouragingly the more traversals have been observed during training the better the performance increase during inference.

### Strengths
- The key idea of learning a spatial priors for AVs is simple and powerful. It is great to see this work execute on this idea. The proposed approach is elegant and straight forward to add to existing systems. This enhances potential impact.
- The manuscript is well written and the illustrations are high quality and support the written text well.
- The experiments are illustrative especially the ablation with respect to number of traversals in training set and performance at different distances. Both of those support the claim that a map prior is learned by showing that (1) when more prior observations exist the learned prior leads to a higher performance boost and (2) when sensor observations are weak (because things are far away) the learned prior can compensate and lift performance substantially. 
- The baseline experiments with NMP shows clearly the benefit of end-to-end learning the map prior during training with the model in the loop.

### Weaknesses
 - A slight weakness is that the improvements of adding the map prior seem to be relatively minor in the overall evaluation. Likely this is due to the observations at close range providing sufficient information to not really need the learned prior (as shown in Fig8). I do wonder what happens if the image information provided to the model gets degraded in some way. Like downscaling significantly or blacking-out chunks of the images, or dropping out all but one frame? A limit experiment would be to provide NO image information to understand how much the models can do without any observations only given the prior?
- The sparse voxel hashmap representation for the prior is a great choice for a scalable representation. It would be good to add some statistics into the paper as to the required memory footprint per distance traveled (for example). This would (1) give the reader a better sense for actual practical memory footprints of the map and (2) support the claim that the prior map is represented in a scalable way.
- The paper lacks a strong baseline comparison for the map prior. The current baseline only uses the network without the learned prior. It would be beneficial to compare against a more traditional map prior, such as using a pre-existing map like OpenStreetMap, or even a simple aggregated RGB map from previous traversals. This would help to isolate the benefit of the learned features compared to simply having a map.

### Questions
- It was not that obvious upon a first read how the sparse voxel datastructure is setup: 
    - Is it 3D or only 2D (I assumed 2D but the word voxel was used?)? 
    - How are the 4 levels spaced in voxel resolution 0.5m, ?, ?, 25m? 
    - Am I right to assume that T=2^16 means that each side of the 2D grid is 2^8=256 pixels/voxels wide? so the highest resolution layer is 0.5m*256 = 128m wide?
- How does the approach handle dynamic objects?

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
This paper introduces map priors for 3D object detection. To obtain multi-scale map representation, this paper utilizes techniques like InstantNGP to encode the map as a hash map. Further, this paper presents a prior fusion module to fuse the map priors into 3D perception models, like BEVDet, BEVFormer. Experimental results demonstrate the effectiveness of the design.

### Strengths
- This paper introduces map information as the prior of the 3D perception model. The idea is interesting.

- Main experiments in Table 1 demonstrate improvements. Experiments in Figure 6 are interesting, and demonstrate that map priors help multi-traversal circumstances.

### Weaknesses
1. Map representation. 

- The paper introduces the map priors for 3D perception. It is unclear how the map prior is represented, and whether it is an HD-map or not. If the map prior is derived from an HD-map, then the cost of this method will be a significant issue, both in terms of storage and access. Furthermore, relying on HD-maps limits the applicability of the method to only areas where such maps are available, which may limit the potential of this method. Even if the map representation is learned, the limited driving region problem still exists, as the method would only be applicable in areas where sufficient training data for the map representation is available. The paper should clarify how the map representation is obtained and address the limitations of this approach.

- Ablation studies related to map representation and final NDS performance are also required. Whether SD map can also bring such performance improvements?

2. Comparisons with prior works related to map segmentation.

- How about the method compared to other end-to-end driving methods, especially the overall performance on 3D object detection? like UniAD [1] or VAD [2]? This method also introduces map segmentation as an auxiliary supervision.

- Comparisons with NMP in Table 2. I am not sure about the motivation of this experiment. Whether it is used to show the prior fusion technique is more advanced compared to the one in NMP or not? I think there is a gap between the setting of NMP and DMP, which are used to update the online map, while another is proposed to utilize the map.

[1] Planning-oriented Autonomous Driving

[2] VAD: Vectorized Scene Representation for Efficient Autonomous Driving

3. Missing related papers. Some papers share similar ideas with the paper, and detailed comparisons are suggested. Some discussions related to the key similarities and differences are required.

- Mind the map! Accounting for existing maps when estimating online HDMaps from sensors.

- P-MapNet: Far-seeing Map Generator Enhanced by both SDMap and HDMap Priors

### Questions
See weakness.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper introduces Differentiable Map Priors (DMP), a framework aiming at enhancing 3D perception systems in autonomous vehicles by leveraging historical traversal data. Specifically, the prior knowledge is represented as a differentiable map that can be directly learned from training data. The learned spatial prior features can be fused with features from the current observations, which leads to improved object detection and semantic segmentation performance on the nuScenes dataset.

### Strengths
1. Integrating historical data is a promising practice for equipping autonomous vehicles with a more robust perception ability, especially when the onboard observation is less reliable (e.g. bad weather or long-range perception).

2. Maintaining a learnable map prior offers a flexible solution to use the historical information according to training data and target tasks. In addition, the map prior is built on a multi-resolution hash table, which is compact and memory-efficient for real-world applications.

3. The proposed map prior can be effortlessly incorporated with current detection and segmentation frameworks by feature fusion.

### Weaknesses
1. The novelty of this paper is unclear: The idea of integrating historical data with onboard data for autonomous vehicles has already been explored in works like HINDSIGHT[1] and NMP[2]. The Neural Map Prior proposed in NMP, although not in the form of hash tables, shares a similar design and usage as the Differentiable Map Prior in this work. The major difference is that NMP uses GRU updating and the Differentiable Map Prior in this work can be directly optimized, which does not form enough novelty from my point of view.

2. The presentation of this paper can be improved: Some figures, tables, and descriptions are not informative and clear enough. For example, Figure 1 and Figure 5 both show examples from the nuScenes dataset to illustrate the large portion of overlapping traversals, which could be redundant to each other. In Figure 2, it is confusing what “global map” represents, is it a traditional map, or the differentiable map priors? Table 1 could also be improved. Firstly, it is unclear what bold numbers represent. Secondly, the table arrangement makes it very hard to tell the improvement brought by DMP, calculating delta values may help. Besides, the in-text citation style needs refinement for better readability.

3. Experimental results do not demonstrate consistent and strong improvement: From Table 1, it is observed that incorporating DMP does not always lead to better results. For example, for BEVDet, mASE and mAOE is better without DMP. For DEVFormer, mASE, mAAE and mAVE do not improve with DMP.

4. Ablations are not adequate: The ablation experiments currently presented do not cover the core of the method. For example, the Differentiable Map Prior itself is not ablated. In addition, the fusion between prior features and sensor features is not ablated.

### Questions
1. Building Differentiable Map Prior with a multi-resolution hash map, how to avoid hash collision for finer resolutions? More specifically, if the number of grid points is larger than the number of entries in the hash table, how to assign entries to grid points?

2. The paper mentions that at inference, the map prior will only be used if it is available. For the scenes that have never been traversed, the method will fall back to the baseline algorithm. How does the method get to know when to fall back to the baseline and when to use the map prior? Does it mean DMP explicitly keeps track of the positions that have been visited?

3. Following the previous question, is Differentiable Map Prior available for all locations or just for the ones that have been visited? What embedding will be retrieved if a novel location is input?

4. When training, are DMP and detectors trained together? Are all components in detectors trainable or not? If both DMP, detector encoder and decoder are trained together, how to make sure DMP is not bypassed?

5. For the comparison with NMP, can you provide more details on how you modify it to use training prior during evaluation? From my point of view, NMP does not use separate priors for training and testing, and its original setting should be comparable with this paper. Results for original NMP should be included for a complete comparison.

6. In Table 2, while NMP* and DMP have similar NDS and mAP, DMP shows a much higher mIoU. Can you provide mIoU for individual classes and explain this performance gap?

### Soundness
2

### Presentation
1

### Contribution
2
