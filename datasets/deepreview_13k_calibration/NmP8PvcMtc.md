# Efficient Multi-Level Learning for Dense Object Detection

- Decision: Reject
- Avg Score: 4.00
- Scores: 3, 5, 5, 3

## Abstract
Dense object detection is crucial and favorable in the industry and has been popular for years with the success of the multi-level learning framework. By delivering the learning of objects into a multi-level feature pyramid, such a divide-and-conquer solution eases the optimization difficulty. However, this learning paradigm has a major shortcoming left behind. The shallow levels take tons of computational burden due to their high resolutions of the feature maps, heavily slowing down the inference speed. In this paper, we aim for minimal modifications to exchange a better speed-accuracy trade-off. The outcome is SlimHead, a very simple, efficient, and generalizable head network, which further unleashes the potential of multi-level learning for dense object detectors. It operates in two stages: Slim and Fat, initially plugging interpolator before the head network functions to "slim'' the feature pyramid, and then recovering the features to original solution space by "fatting'' the feature pyramid. Thanks to its flexibility, operations with higher computational complexity can be easily integrated to benefit accuracy without loss of inference efficiency. We also extend our SlimHead to multiple high-level vision tasks such as arbitrary-oriented object detection, pedestrian detection, and instance segmentation. Extensive experiments on PASCAL VOC, MS COCO, DOTA, and CrowdHuman demonstrate the broad applicability and the high practical value of our method.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper proposes a 'slim' and 'fat' strategy to reduce the computational burden of high-resolution features in multi-level object detection. The 'slim' step reduces the feature resolution by interpolation, and the 'fat' step recovers the original resolution. By incorporating DCN, the resulting model achieves slightly better accuracy and inference speed than the baseline model. The paper also presents experimental results on pedestrian detection and instance segmentation.

### Strengths
1. The writing and presentation are good, especially the figures in the paper.
2. Extensive experiments were conducted to analyze the effectiveness of the proposed method.

### Weaknesses
1. Limited novelty. The proposed method is simple, and the performance improvements are minimal. It appears to be more of an engineering technique than a sufficient method for publication at ICLR.

2. Multiple alternative approaches can achieve similar improvements. An intuitive and simpler method would be to reduce the channels of low-resolution features. The paper already presents this result in Figure 8. The model with half the channels at P3 and P4 achieved comparable results to the proposed method (AP 39.3 vs. 39.4, FPS 39.9 vs. 40.2). This approach adds 2M parameters, but this is negligible compared to the entire model. Why not adopt this approach to achieve similar results?

3. Improving the inference speed of the detection head has less impact when using a larger backbone. The results in Table 9 illustrate this (when using Swin-L as the backbone, FPS 6.6 vs. 6.7). With the rapid development of LLMs, such an improvement becomes less significant.

4. Another way to enhance detection accuracy with minimal computational cost is to apply DCN only on high-level features, as DCN mainly benefits large objects (Table 4). This may be a more cost-effective solution than the proposed method, offering similar detection accuracy with faster inference speed.

In summary, there are many engineering techniques that can achieve similar results to the methods in the paper. The proposed method offers no clear advantages over these alternatives.

### Questions
See the weaknesses.

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
The paper proposes a generic head module named SlimHead to reduce the heavy computational cost of dense object detectors at shallow feature levels by reducing the spatial size by a factor of r. Experiments are conducted on COCO, DOTA, and PascalVOC datasets and on different detectors such as TOOD, Faster-RCNN, and Phase-shifting coder.

### Strengths
The paper proposes an efficient head module to improve the speed-accuracy trade-off for dense object detection architectures. Experiments are conducted across different datasets.

### Weaknesses
 - The comparison methods in Tab. 5 for object detection on MS COCO val2017 are outdated.
- More real-time methods should be included for comparison.
- Given that the main technical contribution is to achieve a better speed-accuracy trade-off for object detection, the current results are insufficient to demonstrate this.

### Questions
Will the method work if you finetune only the head layers from pretrained models using a subset of data? It can then apply to a broader class of models. 

Inaccuracy in Table 5: TOOD paper has different values than reported in Table 5. 42.5 (original) vs 42.3 (here). Can the authors explain the discrepancy?

In general, the speed only improves marginally (< 1 FPS) for all the models shown. How does it compare with efficient backbones such as efficientnetv2 or efficientvit? Since, the paper deals with efficiency it should compare against these baselines.
Further, how does it compare with quantization methods that do not require retraining or pruning methods [1,2]?

The performance improvement is mainly observed across medium and large-scale objects. Why do they improve when you only modify the shallow features (for small objects)? Is there a trade-off between the different feature scales?

The claim of a generic module is not supported by comprehensive experiments: Experiments are shown with only the ResNet-50 backbone. Further, Table 9 shows that the performance improvement with larger models like Swin-L is small (even with 2x schedule) across both speed and accuracy. So, additional experiments with ResNet101 backbone and other architectures like RetinaNet are needed to claim it is a generic module. 

The configuration of Slimhead is not uniform and is engineered for different tasks and datasets (Sections 4.3, 4.4, 4.5) as DCN is used for the first two layers for object detection and in all layers, for instance segmentation. How to choose the configurations, does it require extensive hyperparameter tuning? Can it be automated with Neural Architecture Search?

For the alternatives, have the authors considered reducing both spatial and channel dimensions? Have you considered residual connections in SlimHead?

Minor: 
The writing of the paper can be improved further – e.g., sub-figures are denoted as figure3Right with Right in caps. Figure 3 can be improved with marked arrows.
Typo in L214 – “dimention”

[1] Molchanov et. al. Pruning convolutional neural networks for resource efficient inference, ICLR 17
[2] He et. al., Channel pruning for accelerating very deep neural networks. ICCV 17

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces SlimHead, a head network that optimizes speed and accuracy with minimal modifications. SlimHead processes feature pyramids in two stages—first "slimming" and then "fatting" the features—allowing for complex operations without sacrificing inference efficiency. This adaptable design improves accuracy across tasks like object and pedestrian detection and instance segmentation, as shown through extensive experiments on datasets such as PASCAL VOC, MS COCO, DOTA, and CrowdHuman.

### Strengths
- The paper is clearly written.
- The ablation study sufficiently demonstrates the effectiveness of each component.
- Several instance-level perception tasks are performed.

### Weaknesses
 * The novelty is limited. It seems the method only applied an interpolator&inversed interpolator into layers to change the size of feature map. In my opinion, it's just an engineering trick.
* The experiment are seriously out of date. The method achieves 43.2 on MS COCO2017. But according to the [leading board](https://paperswithcode.com/sota/object-detection-on-coco-minival), the detectors now can achieve over 65.9 now. Even taking into account the small backbone network chosen for the experiment, the results are only comparable to the level of research conducted a few years ago. I don't think a small boost is enough in such a weak experimental setup: for example, according to Table 6, the proposed method only improves 0.4 on the Faster R-CNN.
* The comparison is problematic. It seems the performance of other works is much lower than the official report. For example, in Table 5, GFocalV2 achieves 41.1 on the COCO 2017 val set, but according to the [official paper](https://github.com/implus/GFocalV2), GFocalV2 with the R50 backbone performs 44.3 test set. Although there are differences between the two datasets, there is generally not such a large performance loss.

### Questions
Please see the above weaknesses.

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
5

### Summary
In this paper, the authors aim for minimal modifications to exchange a better speed-accuracy trade-off. The outcome is SlimHead, a very simple, efficient, and generalizable head network, which further unleashes the potential of multi-level learning for dense object detectors.

### Strengths
* The method is easy to understand.

### Weaknesses
* The novelty is limited. It seems the method only applied an interpolator&inversed interpolator into layers to change the size of feature map. In my opinion, it's just an engineering trick.
* The experiment are seriously out of date. The method achieves 43.2 on MS COCO2017. But according to the [leading board](https://paperswithcode.com/sota/object-detection-on-coco-minival), the detectors now can achieve over 65.9 now. Even taking into account the small backbone network chosen for the experiment, the results are only comparable to the level of research conducted a few years ago. I don't think a small boost is enough in such a weak experimental setup: for example, according to Table 6, the proposed method only improves 0.4 on the Faster R-CNN.
* The comparison is problematic. It seems the performance of other works is much lower than the official report. For example, in Table 5, GFocalV2 achieves 41.1 on the COCO 2017 val set, but according to the [official paper](https://github.com/implus/GFocalV2), GFocalV2 with the R50 backbone performs 44.3 test set. Although there are differences between the two datasets, there is generally not such a large performance loss.

### Questions
The authors may:

1.  Applied their method on the latest works and dig further into the innovations of the methodology.
2. Explain why the performance of other works in the Table 5 is lower than the official results.

### Soundness
2

### Presentation
2

### Contribution
2
