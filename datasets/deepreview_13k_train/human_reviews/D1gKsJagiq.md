# Dual-Stream Adapters for Anomaly Segmentation

- Decision: Reject
- Scores: 6, 5, 3

## Abstract
Anomaly segmentation aims to identify pixels of objects not present during the model’s training. Recent approaches address this task using mask-based architectures, but these methods have high training costs due to the large transformer backbones involved. While vision adapters can help reduce training costs, they are not specialized for this task, leading to inferior performance. In this work, we propose Dual-Stream Adapters (DSA), a vision adapter tailored for anomaly segmentation. DSA extracts both in-distribution and out-of-distribution features via (i) an anomaly prior module that produces separate initial embeddings for the two streams; and (ii) a dual-stream feature refinement that implicitly guides the separation of in-distribution from out-of-distribution features. We train DSA using a novel hyperbolic loss function that provides supervised guidance for differentiating in-distribution and out-of-distribution features. Experiments on various benchmarks show that dual-stream adapters achieve the best results while reducing training parameters by 38\% w.r.t. the previous state-of-the-art.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces a ViT adapter designed specifically for anomaly detection in semantic segmentation. The approach begins by extracting multi-scale features using a ResNet convolutional stem. Two distinct sets of learnable encodings are added to these features to specialize them for in-distribution (ID) and out-of-distribution (OOD) learning. These initial features are then fused with ViT backbone activations through a series of cross-attention layers and feed-forward networks, maintaining separate streams for ID and OOD features throughout the entire downstream path. The model is trained using an uncertainty-based hyperbolic loss function, where features are projected into hyperbolic space: OOD features are attracted towards the origin of the Poincaré ball, while ID features are repelled away from it.

The authors evaluate their dual-stream adapter on road-driving anomaly detection benchmarks, comparing its performance to other ViT adapters and alternative outlier detection methods. Additionally, they conduct an ablation study to assess the impact of individual components of their proposed method.

### Strengths
1) Method is simple and more parameter efficient than existing outlier detection methods.
2) The method preserves ID performance well.

### Weaknesses
1) Mixed results in terms of OOD detection on different datasets, both in comparison to fully fine-tuned models, but also different adapter types.
2) I do not agree that using void/background class makes this training self-supervised, as there is explicit supervision in terms of labelling pixels into this additional class. Furthermore, the method could not be used on datasets that do not have ignore regions. It would maybe be better to follow the convention of using the term "auxiliary data". It  would be useful if this was reflected in the organization of Table 3.
3) Missing methods in ood-detection tables. e.g. [a] is the current leader on SMIYC-RA
4) Some things about the method are still not clear -> see questions.

### Questions
1) How are the encoder and adapter features integrated before being passed to the decoder as described in Equation 3?
2) Is the background class utilized in the computation of L_{mask} and L_{class}​?
3) Is the convolutional module within the anomaly prior module also fine-tuned? Was it pretrained, and if so, how? What specific ResNet variant is used?
4) Can you provide detailed specifications of the Cross-Attention and Feed-Forward Network (FFN) modules used in the adapters?
5) How is the void/background class incorporated into L_{ubhl}? At what stage is the ground truth label applied?

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
The paper aims to reduce the high training cost of the transformer-based anomaly segmentation model. The authors introduce the Dual-Stream Adapter (DSA) to tackle this issue, specifically designed for anomaly segmentation tasks. The DSA comprises two main components: an anomaly prior module and a dual-stream feature refinement module. The anomaly prior module is responsible for learning both in-distribution and out-of-distribution features through separate feature-level encodings. Meanwhile, the dual-stream feature refinement module enhances and integrates these features with the robust representations derived from a frozen Vision Transformer backbone. Additionally, the architecture employs a hyperbolic loss function to guide the learning process effectively. The authors carried out extensive experiments across five datasets, demonstrating their proposed model's effectiveness.

### Strengths
+ The paper is clearly structured, featuring well-organized paragraphs and accessible figures that enhance comprehension.
+ The design of the proposed Dual-Stream Adapter is sound and well-motivated.

### Weaknesses
 - The experiments conducted were compared to several competitors; however, the values reported in Table 3 do not align with those in the original publications. This inconsistency raises questions about the validity of the experimental outcomes. It is highly advisable for the authors to verify the accuracy of the reported experiments to ensure reliable results.

- It appears that there is an inconsistency between Figure 3 and equations (6) and (7). It would be beneficial to verify their accuracy.

- It would be interesting to analyze the amount of training time that can be saved due to the reduction in trainable parameters. Specifically, a comparison of the training time with and without the proposed adapter would be beneficial to quantify the actual speedup achieved. This should include not only the total training time but also the time per epoch, to understand the computational efficiency gains.

- There are some related papers [A-B] that have not yet been cited in the current version.

### Questions
This paper is well-structured and has a clear motivation. However, a significant concern arises from the experiments reported, as the values presented appear inconsistent with those in the original publications. At this stage, I prefer to take a cautious approach to the rating and await the author's response before reaching a final conclusion.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces a novel adapter architecture for anomaly segmentation. The architecture incorporates two key architectural components: anomaly prior modules and dual-stream feature refinement tailored to improve anomaly segmentation. The anomaly prior
module learns to extract the initial ID and OOD features that are refined and improved by passing through a set of dual-stream feature refinement blocks. It introduces an uncertainty-based hyperbolic loss to explicitly learn the ID and OOD features. The results on several datasets in terms of some metrics show the effectiveness.

### Strengths
+ a novel adapter architecture for anomaly segmentation. It designs anomaly prior modules and dual-stream feature refinement tailored to improve anomaly segmentation. 
+ The results on several datasets in terms of some metrics are the SOTA.

### Weaknesses
 - The definaton of this task is unclear. How to define the Anomaly regions. For example, I put the first input of Fig. 5 into the ChatGPT and ask it to indicate the abnormal regions. It responses: "
From the image, it appears to show a traffic checkpoint or roadblock scene with a few police officers, some cones marking the road, and vehicles either being stopped or passing through the checkpoint. To analyze any potential abnormal regions, I would need specific criteria for identifying abnormalities, such as:
Traffic flow: Are there any unusual movements or traffic behavior?
Objects: Are there any misplaced cones, vehicles, or people?
Security concerns: Is there anything out of place, like suspicious behavior or unmarked vehicles?
If you're looking for more detailed insights, could you clarify what type of abnormality you're focused on—whether it's safety, traffic irregularities, or something else?"
This answer is more reasonable, since the anomaly regions can be different in different settings.

-The above example gives another question. The current multimodal large language model already achieves better responses.

- The preposed method lacks novelty, and it is mainly combined by Vit adaptors with cross-attention.

### Questions
Based on the above the weaknesses, I have the following questions: 

- What are the key criteria or benchmarks used to evaluate anomaly detection in your scenario?
Defining the task clearly with precise criteria is critical. How do you plan to measure the model's success in detecting abnormal regions?

- What are the distinguishing features of your method compared to existing multimodal models?

- How does the model handle the contextual differences in anomaly definitions?
Since anomalies are highly context-dependent, is your model trained to recognize such context? How does it deal with shifting or ambiguous definitions of normalcy versus anomaly?

- Are there plans for improving the generalization and adaptability of the model?
For instance, using domain adaptation techniques or fine-tuning the model on specific datasets related to the task could improve its performance in different scenarios.

### Soundness
2

### Presentation
3

### Contribution
1
