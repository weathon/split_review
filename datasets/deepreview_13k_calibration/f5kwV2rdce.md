# Labits: Layered Bidirectional Time Surfaces Representation for Event Camera-based Continuous Dense Trajectory Estimation

- Decision: Reject
- Avg Score: 5.75
- Scores: 5, 6, 6, 6

## Abstract
Event cameras provide a compelling alternative to traditional frame-based sensors, capturing dynamic scenes with high temporal resolution and low latency. Moving objects trigger events with precise timestamps along their trajectory, enabling smooth continuous-time estimation. However, few works have attempted to optimize the information loss during event representation construction, imposing a ceiling on this task. Fully exploiting event cameras requires representations that simultaneously preserve fine-grained temporal information, stable and characteristic 2D visual features, and temporally consistent information density—an unmet challenge in existing representations. We introduce Labits: Layered Bidirectional Time Surfaces, a simple yet elegant representation designed to retain all these features. Additionally, we propose a dedicated module for extracting active pixel local optical flow (APLOF), significantly boosting the performance. Our approach achieves an impressive 49\% reduction in trajectory end-point error (TEPE) compared to the previous state-of-the-art on the MultiFlow dataset. The code will be released upon acceptance.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper tackles the representation problem of asynchronous indefinite-length event data feeding into modern networks. The authors propose Labits, a new representation based on a hierarchical bi-directional event surface, to better preserve the millisecond time information in the raw data. The authors conduct experiments on the continuous point tracking task and verify the performance benefits over other representations. However, from my perspective, the contribution is still insufficient, with only a new representation that has not been fully experimentally validated.

### Strengths
1. A new event representation Labits is proposed to preserve rich temporal information for motion-related downstream tasks.
2. The benefits of this new representation compared to the commonly used voxel grid are demonstrated on the nonlinear dense trajectory estimation task.

### Weaknesses
1. Experimental comparisons only on simulated data are not convincing, especially since the compared methods [1] already did some experiments on real data. At least qualitative or quantitative experimental comparisons should be done on a real collected event data, e.g., the optical flow estimation evaluation on DSEC in [1].

2. The new representations Labits presented in this paper are one of the core contributions, and it is necessary to apply this to multiple tasks (both motion-related and motion-irrelevant) and perform comprehensive evaluations, e.g., two-frame optical flow estimation, depth estimation, object detection, motion segmentation, etc. The authors only experimented with one task and mentioned that it could be used for other motion-related downstream tasks, but not actually provided.

3. ``Since the number of time bins in Labits can be freely adjusted by the user, maintaining a single-channel input increases flexibility.'' Does this indicate that the pretrained Labits-to-APLOF Net can adaptively handle different time bins set by the user? In addition, ablation experiments with a larger number of channels are necessary.

4. The differences between the dense tracking model and [1] need to be clarified.

### Questions
1. Table 1 indicates that the Voxel Grid discards polarity information. How does Labits handle this?
2. ``Labits is a synchronous event representation.'' Does it support online processing?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces Labits, a new representation method called "Layered Bidirectional Time Surfaces," designed for event cameras to enable precise dense trajectory estimation and optical flow calculation. Labits maximize the advantages of event cameras by capturing fine-grained temporal information, retaining stable 2D features, and maintaining consistent information density in spatiotemporal motion estimation. The authors also propose a specialized module, Labits-to-APLOF (Active Pixel Local Optical Flow), which uses Labits representations to enhance the accuracy of local optical flow estimation at active pixels. This paper demonstrates Labits' superior performance by reducing trajectory end-point error (TEPE) by 49% over previous state-of-the-art methods in the MultiFlow dataset, making it an effective and efficient tool for motion-sensitive tasks.

### Strengths
- The motivation is compelling, addressing the need for more accurate and dense event representations that fully exploit the unique properties of event cameras. This need is crucial in dynamic environments where event cameras can provide high temporal resolution.
- The paper is organized logically, with a clear distinction between the problem background, the proposed solution (Labits), and the experiments.
- Labits and the Labits-to-APLOF module demonstrate notable improvements in trajectory estimation accuracy. By leveraging bidirectional time surfaces, Labits successfully addresses temporal occlusion and provides a stable representation of movement information, which is particularly useful for complex tasks such as trajectory prediction, event-based video interpolation, and high-speed object tracking.

### Weaknesses
 - Some technical justifications for the Labits representation could be expanded. For example, while the use of bidirectional time surfaces is novel, more in-depth analysis of why this bidirectional approach provides such significant accuracy improvements over unidirectional methods could make the claims stronger.
- The paper introduces the Labits-to-APLOF network as a lightweight and adaptable feature. However, additional evidence supporting its adaptability, such as visual examples of Labits in various scenarios, would clarify its generalizability.
- While Labits achieves efficiency gains, it is slower than simpler methods like the Voxel Grid. Additional experiments demonstrating the trade-off between computational cost and accuracy gains in real-time settings would strengthen the justification for using Labits in time-sensitive applications.
- The evaluation of Labits is confined to a single dataset (MultiFlow), limiting insight into its performance across different event-based vision tasks and datasets. Exploring Labits in various contexts and testing it on multiple datasets would offer a more comprehensive assessment of its versatility and robustness, providing a promising direction for future research.

### Questions
- The authors claim that the bidirectional time surface design enables Labits to reduce estimation error significantly. Could they provide additional analysis or visualizations to show why this bidirectional approach better captures motion density and consistency compared to unidirectional methods?
- Could the authors clarify the Labits layer's adaptability? Specifically, how does Labits handle scenarios with minimal event data where forward and backward time data might be sparse?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
They introduced Labits, a novel event representation that simultaneously retains fine-grained temporal information, meaningful 2D visual patterns, and local speed cues. They also developed the Labits-to-APLOF net, which accuratelyconverts Labits into active pixel local optical flows. The results high-light that, beyond model architecture, event representations also have a transformative impact onthe final outcomes.

### Strengths
1. a novel synchronous event representation that is aware of event camera's asynchronous characteristic and keeps rich local movement trend information

2.They achieved the SOTA performance on event-based dense trajectory estimation task.

3.trained a corresponding active pixel local optical flow estimator based on Labits layers, which significantly benefits movement-sensitive tasks.

### Weaknesses
1.In Figure 4, there is less difference between (d) and (e). What’s the influence of APLOF? Could you give explanation for this phenomenon?

2.In Table3, you already give the model size and other metrics. Could you please compare your model with others in FLOPs and total parameters to demonstrate your model’s efficiency?

### Questions
See weakness above.

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
4

### Summary
This paper introduces a simple and elegant representation to preserve fine-grained event features for event-based continuous dense trajectory estimation. Experiments conducted on the MultiFlow dataset demonstrate the effectiveness of the proposed solution. Extensive analyses and visualizations are presented. The source code will be provided to foster future research.

### Strengths
1. A novel and effective synchronous event representation aware of the event camera's asynchronous characteristics is presented.
2. The paper is overall well-written and nicely structured.
3. The source code will be provided to foster research in this direction.
4. Rich interesting visualization results demonstrate the effectiveness of the proposed solution.

### Weaknesses
1. If it is possible, it would be nice to investigate the potential of the proposed representation for optical flow estimation or mesh flow estimation.
2. In addition to the MultiFlow dataset, it would be nice to experiment on another dataset to show the generalization capacity of the proposed solution.
3. If it is possible, please consider presenting analyses to directly show the dense time-continuous prediction results by visualizing the results in different time steps within a sample window of the MultiFlow dataset.
4. More detailed ablation studies and parameter analyses could be conducted. For example,  the numbers of the TORE volume, the voxel grid, the Labits, and time bins could be experimented for analyzing the best parameter settings or helping understand the effects of different parameters.

### Questions
1. Would you consider discussing some limitations of the presented work and pointing out some future research directions?
2. Would you consider directly comparing the proposed representation against some existing event representations to verify the superiority of your solution?
3. In Table 1, it is indicated that the voxel grid discards the event polarity. However, voxel grids actually contain the accumulation of event polarity information. Could you explain this?
4. Actually, for voxels, they can also support the training of a voxel-to-APLOF network by computing a voxel active event mask and computing voxels with accumulative time spans, similar to the unified voxel grid of EVA-Flow. Could you explain this?
5. What is r_start in equation(5)(6)? Does O(x) indicate the optical flow speed or displacement? Then how did you compute Or(x), Or+(x_start), and Or-(x_start)? This is somewhat misleading.
6. It is claimed that "Labits is well-suited for local motion-sensitive tasks and has the potential to standard". However, only the last two rows in Table 2 indicate the results of Labits. It would be nice to add more results to verify the superiority of Labits, e.g., by testing DCT-RAFT with Labits and by testing with Unified Voxel Grid.
7. While the proposed method achieves high accuracy on MultiFlow, it is a synthetic dataset. It would be nice to offer results on a real-world dataset like DSEC-Flow to verify the generalization capacity of the proposed method.

### Soundness
3

### Presentation
3

### Contribution
3
