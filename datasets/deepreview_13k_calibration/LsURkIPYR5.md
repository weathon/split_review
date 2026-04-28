# LaneSegNet: Map Learning with Lane Segment Perception for Autonomous Driving

- Decision: Accept
- Avg Score: 6.00
- Scores: 8, 5, 5, 6

## Abstract
A map, as crucial information for downstream applications of an autonomous driving system, is usually represented in lanelines or centerlines. 
However, existing literature on map learning primarily focuses on either detecting geometry-based lanelines or perceiving topology relationships of centerlines. 
Both of these methods ignore the intrinsic relationship of lanelines and centerlines, that lanelines bind centerlines. 
While simply predicting both types of lane in one model is mutually excluded in learning objective, we advocate \textit{lane segment} as a new representation that seamlessly incorporates both geometry and topology information.
Thus, we introduce \textbf{\algname}, the first end-to-end mapping network generating lane segments to obtain a complete representation of the road structure. 
Our algorithm features two key modifications.
One is a lane attention module to capture pivotal region details within the long-range feature space. 
Another is an identical initialization strategy for reference points, which enhances the learning of positional priors for lane attention.
On the OpenLane-V2 dataset, \algname outperforms previous counterparts by a substantial gain 
across three tasks, \textit{i.e.},
map element detection ($+4.8$ mAP), centerline perception ($+6.9$ DET$_l$), and the newly defined one, lane segment perception ($+5.6$ mAP).
Furthermore, it obtains a real-time inference speed of $14.7$ FPS.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The work presents a lane-segment based approach for map constructions. The goal is to generate a comprehensive representation [ Map elements and centerline combined] of the lanes within the map. The results are competitive with previous approaches with a single model generalizing to multiple lane based tasks. The method achieves non-marginal results on different tasks.

### Strengths
- The paper is well-written. Detailed explanation of each component. Starting from the introduction to a comprehensive related work review. Then section 3.2 details the approach. 
- Experiments are comprehensive, and non marginal improvments in the evaluation metrics can be seen
- Ablation study for the different choices of attention mechanism and other design choices validating the model architecture is available. 
- The regression in AP_div is discussed in section 4.3

— 
I increased my score after taking a look into rebuttal and other reviewers. The work is sound in terms of value and a novelty of the concept. It’s true that the new concept is having a form of disadvantage but the results are promising. The results indeed generalize to other datasets as shown in the rebuttal.

### Weaknesses
 - It seems there is only one dataset that contains all of the tasks. What about the performance on other datasets where such tasks individually are available. 
- No ablation on the choice for the BEV encoder.

### Questions
It would be nice to see the impact of such a map on downstream tasks such as motion planning/prediction.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes LaneSegNet to annote lane segment for online end-to-end map learning. The network leverages both geometry and topology. It introduces a lane detection module with heads-to-regions for long range attention and identical initialization of reference points to stablize the training.

### Strengths
1. The results look strong. 
2. Abalation studies were conducted to compare different choices of attentions and initialization.

### Weaknesses
1. The model uses one-to-one optimal assignment between predictions and ground truth with the Hungarian algorithm, which is usually slow and unstable and difficult to train, particularly in the beginning. 
2. While metrics look promising, the metrics are still pretty low. It would be more interested in showing what type of lanes the model can do  so well that it can be used for autonomous driving.

### Questions
1. How long is each lane segment ?
2. For a lane segment {A_left, A, A_right}, each appears in 3 lane segments, how to combine them to get final result for e.g. A ?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work introduces LaneSegNet for predicting lane segments from multi-view camera images.  
They propose a new representation for lane segments and develop two new techniques for map-prediction architectures.  
Their lane attention module is an alternative to deformable cross-attention that aims to better capture long-range interactions, and their reference point initialization is a way to better capture spatial priors of map elements.
They perform experiments on the OpenLane-V2 dataset and show improvements on map detection, centerline prediction, and lane segment segmentation.

### Strengths
* Strong results on the new OpenLane-V2 dataset. Numbers are solid and their tiny model outperforms  the other baselines.
* I like the general trend of work that directly predicted structured representations for mapping.

### Weaknesses
 * Motivation for a new task - I'm not convinced this task is necessary. Can the authors elaborate why this is a more suitable representation as opposed to the representations in VectorMapNet, MapTR, others? The paper does not sufficiently justify why predicting lane segments, with explicit left and right boundaries, is superior to existing methods that predict centerlines and associated attributes. The redundancy in representing lane boundaries (e.g., V1_right and V2_left) raises concerns about the efficiency and necessity of this approach. A more thorough discussion of the limitations of existing representations and the specific advantages of the proposed approach is needed.
* Writing - the majority of Section 3 (method) was not detailed enough. Section 3.3 (training loss) in particular describes several losses very briefly and with no citations. The descriptions of the loss functions (e.g., segmentation loss, regression loss) lack sufficient detail. The paper mentions these losses but does not describe their specific formulations, hyperparameters, or how they are weighted during training. The absence of citations makes it difficult to understand the origins or specific implementations of these losses.
* Comparison with prior work - OpenLane-V2 is relatively new and baseline numbers are from authors implementations. It would help calibrate numbers if they applied their architecture to the original tasks conducted in nuScenes. The lack of comparisons on established datasets like nuScenes makes it difficult to assess the generalizability of the proposed method. The reported improvements on OpenLane-V2 are difficult to interpret without a comparison against existing methods on a more established benchmark.
* Figures should be more informative - Figure 2 looks like a generic map prediction architecture and Figure 3 does not help illustrate the lane attention module. Figure 2 provides a high-level overview of the architecture, but it does not highlight the specific novel contributions of the proposed method. Figure 3, intended to illustrate the lane attention module, is too abstract and does not clearly show how the attention mechanism operates or how it differs from other attention mechanisms.

### Questions
* Take for example a simple road with two lanes (V1, V2 from left to right) - with the proposed representation, this would be represented as V1 = {V1_left, V1_center, V1_right} and V2 = {V2_left, V2_center, V2_right}.  
How is the consistency of V1_right and V2_left enforced?  
It seems redudant to regress additional left/right lanes instead of simply regressing centerline + adding left/right lane id attributes.

* Why is Argoverse 2 mentioned on page 7?

* Metrics: it would be helpful to readers to define the acronyms for OLS and DET

### Soundness
3 good

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presents a novel approach to map learning for autonomous driving systems by utilizing the commonly used PV2BEV feature transformation. In contrast to existing methods, this approach introduces a new representation called "lane segment," which incorporates both geometry and topology information. The proposed model is built upon the BEVFormer architecture and incorporates two key modifications: a lane attention module and an identical initialization strategy for reference points, aimed at enhancing the model's prediction capabilities. The prediction branches of the model consist of multiple MLPs, which collectively generate the final predicted lane segment, including the centerline, laneline, laneline type, and adjacent matrix for the lane topology. The effectiveness of the proposed method has been demonstrated through validation on the OpenLaneV2 dataset, showcasing a significant improvement over other existing approaches.

### Strengths
1. This paper introduces an innovative end-to-end approach to jointly predict the centerline and laneline scheme, which is a unique contribution compared to existing methods.
2. In contrast to MapTR, which employs hierarchical queries for map element prediction, this method utilizes a single query for both centerline and laneline prediction. The authors propose a heads-to-regions mechanism and distribute reference points evenly within a lane segment, thereby enhancing feature aggregation for both long-range and local image features.
3. By employing an identical initialization strategy, the model achieves remarkable performance on the OpenLaneV2 dataset, demonstrating its effectiveness and high accuracy.

### Weaknesses
1. The definition of "long range" is not clearly defined in the paper. The authors mention that the OpenLaneV2 dataset is reannotated using the proposed lane segment manner, resulting in lanes being broken into multiple segments. By using shorter lane segments, I don't think "long range" is a challenge. The paper does not provide a clear quantitative definition of what constitutes 'long-range' in the context of lane segments. The claim that the model addresses long-range dependencies is not sufficiently supported by the experimental setup, especially since the lane segments are shorter than the original lane annotations in the OpenLaneV2 dataset. The lack of a clear definition makes it difficult to assess the significance of this contribution.
2. Additionally, manually dividing a lane into segments without any visual cues may introduce unnecessary challenges for the model's prediction, whichi is also not critical for autonomous driving systems. The manual segmentation process, particularly without clear visual cues, could introduce artificial discontinuities and inconsistencies in the data. This raises concerns about whether the model is learning genuine lane structure or adapting to arbitrary segmentation boundaries. The justification for this segmentation approach and its relevance to real-world autonomous driving scenarios is not sufficiently addressed.
3. In the context of map learning, the novelty of topology prediction in this paper is limited. The paper's approach to topology prediction does not introduce any novel mechanisms or architectural components. The performance gains may simply be a byproduct of the lane segment representation, rather than a significant advancement in topology learning itself. The paper does not adequately discuss how the proposed method compares to more sophisticated topology prediction techniques.

### Questions
1. MapTRV2 is a stronger baseline but the relative results are not compared in the experiment section.
2. How to innitialized multiple reference points uniformly inside a lane segment through positional query is not discussed detaily.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
