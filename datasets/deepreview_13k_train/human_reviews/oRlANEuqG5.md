# Track-On: Transformer-based Online Point Tracking with Memory

- Decision: Accept
- Scores: 5, 8, 5, 6

## Abstract
In this paper, we consider the problem of long-term point tracking, which requires consistent identification of points across multiple frames in a video, despite changes in appearance, lighting, perspective, and occlusions. We target online tracking on a frame-by-frame basis, making it suitable for real-world, streaming scenarios. Specifically, we introduce Track-On, a simple transformer-based model designed for online long-term point tracking. Unlike prior methods that depend on full temporal modeling, our model processes video frames sequentially without access to future frames, leveraging two memory modules —spatial memory and context memory— to capture temporal information and maintain reliable point tracking over long time horizons. At inference time, it employs patch classification and refinement to identify correspondences and track points with high accuracy. Through extensive experiments, we demonstrate that Track-On sets a new state-of-the-art for online models and delivers superior or competitive results compared to offline approaches on TAP-Vid benchmark. Our method offers a robust and scalable solution for real-time tracking in diverse applications.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper introduces Track-On, a transformer-based online long-term point tracking model designed for real-time point tracking in video streams. Track-On leverages two memory modules—spatial memory and context memory—to capture temporal information and maintain reliable point tracking over extended video sequences. Unlike methods relying on iterative updates and full temporal modeling, Track-On employs patch classification and refinement for identifying correspondences and tracking points with high accuracy. Extensive experiments demonstrate that Track-On sets a new state-of-the-art for online models and delivers superior or competitive results compared to offline approaches on the TAP-Vid benchmark.

### Strengths
The dual memory module design effectively handles long video sequences in an online setting while addressing feature drift.

Track-On demonstrates fast inference speeds while maintaining high accuracy, a significant advantage in real-time tracking systems.

The model establishes a new benchmark for online models on the TAP-Vid benchmark and shows competitive performance against offline methods.

### Weaknesses
The paper mentions potential precision loss when tracking thin surfaces or instances with similar appearances, indicating limitations in handling certain visual effects. 

The model may struggle to establish correct correspondences in complex scenes with high visual similarity, affecting tracking accuracy.

While the model is memory-efficient, there is a trade-off between memory module size and inference speed, which may require balancing in practical applications.

### Questions
There are too few datasets for comparison, I hope to supplement the experiments.

Are there common patterns or specific scene characteristics in the cases where the model fails?

There are other transformer-based tracking methods mentioned, such as SpatialTracker and CoTracker. How does Track-On differentiate itself from these methods?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper proposes a long-term point tracking framework focused on online, frame-by-frame tracking. The framework leverages spatial and context memory modules to reliably track points over extended time horizons. It achieves state-of-the-art results for long-term point tracking in the online setting. Additionally, the framework is capable of real-time tracking.

### Strengths
- The paper is well-written and easy to follow, with extensive experiments that clearly demonstrate the performance improvements contributed by each module. 
- The authors propose an effective approach using patch classification, rather than regression, to predict each point location; while patch classification was mentioned in the PIPs paper, it was previously used only to accelerate convergence by supervising score maps.
- The authors propose 2 memory modules that effectively improve the tracking performance.

### Weaknesses
 - line 289: I think you meant $\gamma^s$ not $\gamma^q$ which does not appears in eq.8.
- Table 1: the authors should show the backbone used in each approach for easier comparison. If possible, the methods should be compared on the same backbone. However, this is alleviated by table 3 where the authors have show the effectiveness of the memory modules.

### Questions
It would be interesting if the authors can show that this method can be used on much longer videos from recent datasets such as PointOdyssey or Tapvid3D.

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
In order to make point tracking methods more suitable for the real world, the author proposes a new frame by frame online tracking method. The author designed a spatial memory module and a content memory module to capture temporal information and maintain reliable point tracking over a long period of time. Finally, the author uses a coarse to fine manner to predict the final output.

### Strengths
1.The author designed two memory modules to mine spatio-temporal information and use coarse to fine manner for more accurate point prediction. 

2.Experiments demonstrate the effectiveness of the method proposed by the authors and obtain the SOTA performance of the online point tracking method.

### Weaknesses
1.Experiments were inadequate. The designed analysis and the layer number ablation analysis of each modules are not enough, including several decoders, the number (4) of level of similar map used for patch classification, etc.

2.The figures in the paper are not clear enough. For example, in the left of Figure 5, the input qinit does not understand what it means, because q has no subscript and does not specify its meaning. In additional, the title of Figure 5 should go from left to right when introducing the content.

3.Does online point tracking just require that the model does not see the next frame during testing? I think the authors should add the speed of testing like SOT, as the authors said, to be more adaptable to the real world applications.

4.Although your online method is the best, it does not outperform the offline method in the DAVIS data set. What is the reason? Apart from the characteristics of the two type methods.

5. Although the author analyzed the causal processing method in the relevant video field, the analysis of the online method in point tracking is not sufficient, and it does not see the advantages of the proposed method in online methods.

### Questions
1.Although the authors demonstrated many visual maps to demonstrate the effectiveness of the method, a quantitative ablation analysis of the critical modules is lacking, for example, the layer number analysis of query decoder.

2.Many writing details should be noted by the author, including the expression of the picture content, the color of the formula and other details.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The paper proposes a simple yet effective framework, named Track-On, for Tracking Any Point (TAP) task. 

Track-On employ a coarse-to-fine mechanism, where they first find the most match patch feature, and then predict an offset relative to the center of the most matched patch to obtain a more fine-grained prediction.

To tackle the issue of feature drifting in long-term situation, Track-On further proposes the Spatial Memory as well as Context Memory. Spatial Memory utilize deformable attention to flexibly select the most-relevant features in the last frame, to provide a more reliable and latest feature as a reference to help the prediction of current frame. While Context Memory maintains a FIFO queue to store the latest K frames' decoder outputs, to provide a larger context.

Extensive experiments are conducted. The performance on TAP-Vid benchmark shows their superiority, especially on Kinetics and RGB-Stacking subsets. The thorough ablation studies and supplementary materials make the paper looks solid.

### Strengths
1. The paper proposes a simple yet effective transformer-based framework for tracking any point task, named Track-On. Track-On employs the coarse-to-fine strategy. Track-On utilize the DINOv2's feature to help find the most matching feature patch to provide a coarse prediction. After that, Track-On predict a local offset to obtain a more fine-grained prediction. The coarse-to-fine strategy looks reasonable.

2. The paper proposes the Spatial Memory and Context Memory to handle the long-term tracking situation. Spatial and Context Memory provides complementary information for each other, improving their performance significantly.

3. Extensive experiments and ablation studies are conducted, showing their superiority and the effectiveness of each module.

### Weaknesses
I think there is no fatal weaknesses, but there are some concerns:

1. There are some designs that are similar with previous works. For example, in TAPIR, they also use coarse-to-fine strategy, in TAPTR, they also utilize the initial feature to alleviate error propagating. It is better to cite these paper during your description.

2. Some points are over-claimed. Actually, the Spatial/Context Memory can not "address" tracking drifting. There are more metric or experimental evidence to support the claims in L78-L87.

3. Since the positional embedding are learned during training process, how to guarantee the continuity of the embeddings? If the continuity can not be guaranteed, how to ensure the "inference-time memory extension"? What if just ignore the positional embedding?

### Questions
1. I wonder how the Fig. 4 is obtained. By sampling on each frame based on the gt position and then calculate the similarity?

2. It seems a typo in L289, what is the r^q?

### Soundness
3

### Presentation
3

### Contribution
3
