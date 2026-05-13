# TopoSD: Topology-Enhanced Lane Segment Perception with SDMap prior

- Decision: Reject
- Scores: 6, 5, 5, 5, 5

## Abstract
Recent advances in autonomous driving systems have shifted towards reducing reliance on high-definition maps (HDMaps) due to the huge costs of annotation and maintenance. Instead, researchers are focusing on online vectorized HDMap construction using on-board sensors. 
However, sensor-only approaches still face challenges in long-range perception due to the restricted views imposed by the mounting angles of onboard cameras, just as human drivers also rely on bird's-eye-view navigation maps for a comprehensive understanding of road structures.
 To address these issues, we propose to train the perception model to "see" standard definition maps (SDMaps). We encode SDMap elements into neural spatial map representations and instance tokens, and then incorporate such complementary features as prior information to improve the bird's eye view (BEV) feature for lane geometry and topology decoding. Based on the lane segment representation framework, the model simultaneously predicts lanes, centrelines and their topology. To further enhance the ability of geometry prediction and topology reasoning, we also use a topology-guided decoder to refine the predictions
 by exploiting the mutual relationships between topological and geometric features. We perform extensive experiments on OpenLane-V2 datasets to validate the proposed method. The results show that our model outperforms state-of-the-art methods by a large margin, with gains of +6.7 and +9.1 on the mAP and topology metrics. Our analysis also reveals that models trained with SDMap noise augmentation exhibit enhanced robustness.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper integrates SDMap information to complement limitations of on-board cameras for map construction. To enhance the ability of geometry prediction and topology reasoning, , they propose a topology-guided decoder. The proposed method achieves state-of-the-art results on OpenLaneV2, demonstrating that incorporating SDMap yields a significant improvement in accuracy.

### Strengths
1. The approach encodes geometry and road types from SDMap into features and integrates these into BEV features for use in the decoder, which improves performance.

2. To explore the mutual influence of topology and geometry, this work introduce a topology-guided self-attention mechanism to aggregate vicinity lane features.

### Weaknesses
1. *Performance Drop in Model Combination*: Combining LaneSegNet with P-MapNet results in decreased performance, which is unexpected and requires clarification. An explanation for this discrepancy, particularly given that P-MapNet also employs a cross-attention mechanism, would provide valuable insight into the interaction between the two models. The comparison is not entirely fair since the authors use a 200x100 resolution for their method, while P-MapNet uses a 50x25 resolution for both BEV and SDMap features. This difference in resolution significantly impacts the comparison, and the performance decrease may be primarily due to this lower resolution.

2. Limited Novelty in SDMap Encoding and Fusion: The methods used for map tokenization and fusion lack significant novelty, with SDMap encoding resembling SMERF’s approach and the fusion method similar to P-MapNet, both of which utilize cross-attention. Specifically, the spatial fusion process, which sums SD features and BEV features before applying a cross-attention mechanism, is similar to P-MapNet's approach, which also uses cross-attention for feature integration.

### Questions
1. Task Choice:

> Instead, researchers are focusing on online vectorized HDMap construction … However, sensor-only approaches still face challenges for long-range perception due to the limited field of view of camera, … 

The paper’s abstract suggests a focus on addressing challenges in long-range perception due to camera field-of-view limitations. Given this:

  a. Why does this work emphasize the Topology task for incorporating SDMap rather than focusing on an HDMap task?

  b. For topology reasoning, why was the OpenLaneV2 **lane segment** task selected over the OpenLaneV2 **lane centerline** task?

2. Decoder Analysis

In the ablation study (Table 3, last two rows), the authors compare the performance impact of using the Topo-Guided Decoder based on an SDMap incorporation baseline. Have the authors considered evaluating the Topo-Guided Decoder on a baseline without SDMap integration? It would be helpful to understand whether this module maintains effectiveness in the absence of SDMap incorporation.

3. Generalizability of SDMap Fusion Method:

While the paper aims to leverage SDMap to address sensor limitations, it is unclear whether the proposed SDMap encoding and fusion method can also enhance performance in other BEV map-based tasks beyond the current setup.

Given that the combination of P-MapNet with LaneSegNet lowers LaneSegNet’s original performance (Table 1), additional experiments on other tasks would clarify the versatility and potential trade-offs of this fusion approach.

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
4

### Summary
This paper focuses on the task of online map generation. In order to improve the performances of online map construction, the authors adopt SDMaps as prior to enhance BEV feature. To incorporate the SDMaps prior with BEV-based framework, the authors introduce two distinct encoding methods: (1) spatial map encoding and (2) map tokenization. The spatial map encoding is added into the initial BEV query and the SDMaps tokens are used as key and values in the cross attention of BEV encoder. Additionally, to improve the performances of topology prediction, the authors proposes a topology-guided self attention mechanism to aggregate features of predecessor and the successor. The proposed method achieve state-of-the-art performance on the OpenLaneV2 benchmark.

### Strengths
1. The writing and presentation of this paper is good.
2. The authors provide detailed ablation studies to show how the proposed SDMap prior fusion and topology-guided decoder improve the performances.
3. The authors recognize the noise issue in SDMap and mitigate the performance degradation through data augmentation during training.
4. The proposed method achieves high performance compared to recent state-of-the-art methods.

### Weaknesses
1. The SDMap Prior Fusion section lacks technical innovation. The authors combine two SDMap representation methods to achieve better results, but both methods are derived from previous works: spatial map encoding from P-MapNet and map tokenization from SMERF. The author should explain the differences between the proposed fusion method and the simply combination of P-MapNet and SMERF (for example: (1) using both spatial map encoding and map tokenization as key\values in cross attention; (2) concat or add spatial map encoding with BEV features and using map tokenization as key\values in cross attention. Specifically, the authors should clarify why their approach of adding spatial encoding to the BEV query and feature, while using map tokens as keys/values in cross-attention, is superior to other combinations. The current justification lacks a detailed analysis of the design choices and their impact on performance.
2. Some minor writing errors:
(1) In Table 1, Ours-2 achieves lower AP_ped compared to Ours-1. However, the improvement of Ours-2 is 7.2 while Ours-1 is 7.0.
(2) A period is missing before "Similarly" in Line 259.

### Questions
1. The authors should explain the technical contributions of their proposed SDMap Prior Fusion and provide a detailed discussion and comparison with P-MapNet and SMERF in the rebuttal. As shown in Table 3, the most significant improvement of SDMap Prior Fusion actually comes from jointly applying Spatial Encoding and Tokenization. I will consider improve my rating if the authors can address my concern.
2. Is separating predecessor and successor in the Topology-guided Self Attention Mechanism the key factor for performance improvement? The author can prodive ablation study through comparing the proposed method with simply aggregating features by adj. matrix without separate predecessor and successor information.

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
5

### Summary
This work proposed an online mapping method named TopoSD, which enhances lane segment perception capabilities with SDMap priors. Concretely, SDMap elements are encoded into spatial map representations with CNN and instance tokens with transformer encoder and fused with BEV features at different stages. The design mainly lies in the fusion of SDMap priors, while the main structure still follows LaneSegNet. Multiple heads are concatenated to enable the model to simultaneously predict various elements that are required by the online road map. Experiments are conducted on the OpenLane-v2 dataset and demonstrate a significant performance gain compared to baselines. Besides, TopoSD also shows robustness to SDMap noises, which enhances its real-world application values.

### Strengths
- SDMap is a much more easily accessible map prior compared to HDMap and shows the basic structures of a road network. The introduction of it is intuitive and of great practical value.
- The fusion of BEV feature and SDMap priors at different levels is simple but effective, leading to a significant performance gain, as demonstrated in the experiments.
- The study on the effect of mis-aligned SDMap is novel, which is a common case due to the SDMap collection methods.

### Weaknesses
 - Although the metrics have been elevated greatly in OpenLane-V2, the generated online map still seems very terrible and contains **lots of** significant errors, overlaps, and wrong detections, as displayed in the qualitative results on Page 9. It prevents TopoSD from being put into real use.
- Although the study on the influence of SDMap error is novel, the experimental results seem contradictory to the claims TopoSD proposes, which makes this section of study ill-defined. Since the TopoSD is robust to the influence of SDMap deviation or rotation, how much SDMap contribute to the perception result of TopoSD? Besides, there seems no specific design to rectify the SDMap prior errors in your model design.
- As shown in Table 4, the performance of TopoSD trained with SDMap noise is even worse than the baseline LaneSegNet without any SDMap priors. Such a kind of robustness is far from satisfactory.

### Questions
- Why is SDMap’s range $\pm100m \times \pm50m$ while the perception range still remains $\pm50m\times\pm25m$? As far as I am concerned, to truly reflect model’s long range perception performance, the perception range should also be extended to the same range as SDMap’s. Could you also provide experiment results under this setting?
- Could you also provide the results of TopoSD with ResNet-50 backbone, which is the original setting of LaneSegNet and more commonly compared with in the context of online mapping?

### Soundness
3

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
4

### Summary
This paper proposes a novel method called TopoSD to enhance the online generation of high-definition maps (HDMaps) using prior knowledge from standard definition maps (SDMaps). The model processes perspective images captured by cameras arranged in a surround-view configuration, augmenting the online prediction capabilities of the long-range HDMap with locally aligned SDMaps.

### Strengths
1. The paper is well-structured, demonstrating strong logical coherence, and the definitions of geometric and topological tasks are presented clearly and comprehensively. 
2. Quantitative experiments conducted on the OpenlaneV2 dataset demonstrate significant performance improvements and provide valuable insights for result interpretation. 
3. The framework exhibits superior real-time performance while constructing a map at a distance, outperforming related works.

### Weaknesses
1. The definition of SDMap in the article and its acquisition method during the experiment are overly concise and ambiguous. Further clarification regarding the application of SDMap within the framework is necessary. 
2. Section 4.3 lacks comprehensive error analysis in practical scenarios. For instance, when generating an SDMap, in addition to positional offsets, the article should consider other potential inaccuracies, such as variations in road width, lane markings, and the presence of occlusions or temporary road constructions that might not be reflected in the SDMap. 
3. The article does not provide a detailed analysis of the performance enhancements attributable to SDMap in the modeling process. It is unclear how much of the improvement comes from the SDMap itself versus other components of the model. A more granular analysis, perhaps through ablation studies focusing on different aspects of the SDMap integration, would be beneficial.

### Questions
1. Could you offer a clearer and more comprehensive definition of SDMap along with its specific application within the framework? Why not use some open-source maps like OpenStreetMap?
2. Does the framework require addressing the alignment of structured information in contiguous areas of SDMap before it is input into the network? If so, what methods are employed in the framework to achieve this?

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
As annotating HD maps is expensive for real-world applications, researchers have started generating mapping elements based on onboard sensors on self-driving vehicles. The authors propose a method to integrate SD maps as prior knowledge for better generation performance. The contribution of this paper is threefold: (1) two complementary SD maps encoding methods are introduced; (2) a Topology-Guided Decoder is proposed to better leverage geometrical and topological features; (3) achieving SOTA performance on the OpenLane-V2 dataset. The two  SD map encoding methods refer to [spatial map encoding] processing SD map elements drawn on various canvases via CNN and [map tokenization] encoding SD map elements via one-hot encoding and Transformer. The Topology-Guided Decoder (TGD) refers to modifying deformable attention modules to let predicted topology information influence the prediction of geometric information. Experimentally, the proposal method achieves better performance than the baseline method, LaneSegNet, and some other methods, like SMERF and P-MapNet.

### Strengths
- The authors conduct detailed ablation studies to demonstrate the effectiveness of the proposed modules.
- Concerning real-world applications, the authors conduct analysis on the effect of noisy SD map data on model performance.

### Weaknesses
 - In line 15, the authors state that '... long-range perception due to the limited field of view of cameras.' This should refer to the distance a camera can 'see'. The norn of 'field of view' should refer to the angular extent of the camera. The authors should rephrase this sentence for clarity.
- Grammar errors are common, such as 'surround view' -> 'surrounding view' in line 175, 'local aligned' -> 'locally aligned' in line 175,  'forms, i.e.' -> ' forms, i.e.' in line 177, etc. The authors should use tools like Grammarly to complete a grammar check.
- The first two contributions of the paper are limited. The proposed modules to encode SD map information are straightforward and commonly seen, such as in UniHDMap [1] and MapVison [2]. The TGD module depends on the learning results of the deformable attention mechanism.

### Questions
- Please carefully check grammar.
- To verify the novelty of the SD map encoding modules, it is suggested that the proposed method should be compared to other encoding methods, both theoretically and experimentally.
- To verify the novelty of the TDG module, it is suggested that ablation studies on the design choice be done and that the proposed method be logically compared to other design choices.

### Soundness
2

### Presentation
1

### Contribution
2
