# Samba: Synchronized Set-of-Sequences Modeling for Multiple Object Tracking

- Decision: Accept
- Scores: 6, 8, 8

## Abstract
Multiple object tracking in complex scenarios - such as coordinated dance performances, team sports, or dynamic animal groups - presents unique challenges. In these settings, objects frequently move in coordinated patterns, occlude each other, and exhibit long-term dependencies in their trajectories. However, it remains a key open research question on how to model long-range dependencies within tracklets, interdependencies among tracklets, and the associated temporal occlusions. To this end, we introduce Samba, a novel linear-time set-of-sequences model designed to jointly process multiple tracklets by synchronizing the multiple selective state-spaces used to model each tracklet. Samba autoregressively predicts the future track query for each sequence while maintaining synchronized long-term memory representations across tracklets. By integrating Samba into a tracking-by-propagation framework, we propose SambaMOTR, the first tracker effectively addressing the aforementioned issues, including long-range dependencies, tracklet interdependencies, and temporal occlusions. Additionally, we introduce an effective technique for dealing with uncertain observations (MaskObs) and an efficient training recipe to scale SambaMOTR to longer sequences. By modeling long-range dependencies and interactions among tracked objects, SambaMOTR implicitly learns to track objects accurately through occlusions without any hand-crafted heuristics. Our approach significantly surpasses prior state-of-the-art on the DanceTrack, BFT, and SportsMOT datasets.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The paper introduces SambaMOTR for multiple object tracking in videos. This method aims to improve tracking by utilizing temporal information about object movements to model historical object data, and occlusions, thereby modeling long-range dependencies, implicit motion, and appearance between tracklets.

### Strengths
- Overall, the experiments are extensive with different alterations in modeling provided in the main paper and appendix.

### Weaknesses
 - Visual comparisons show that the Samba autoregressive model performs better than memory/motion models should be provided to substantiate the claims.
- The interpretations of system $\mathbf{A}$ and control $\mathbf{B}$ matrices in the context of object tracking are unclear. Providing clearer definitions of notations would be helpful.
- I understand the intention to separate two paradigms tracking-by-detection (TBD) and tracking-by-propagation (TBP), but the difference is subtle as the TBP still needs bounding boxes to initiate the states, and needs a detector to recognize newly appearing objects. Then, propagation alone is simply not practical in this problem of multiple object tracking.
- Then it should be fair to compare with TBD methods, and the performance still falls short behind classic motion models as reported in Table A.
- While I value the effort in development, the innovation in the method appears to be limited, as it essentially represents a straightforward combination of MOTR and Mamba and the motivation is not really compelling.

### Questions
- Just to confirm, does the state space model operate on the coordinate domain (bounding boxes) or the visual domain (pixel values)? If it does operate on the coordinate domain, how can the auto-regressed output boxes be refined to fit the subjects without looking at visual features?

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper introduces the novel SAMBA model architecture for multi-object tracking. It takes a unique approach to tracking in a tracking-by-propagation framework, building on top of selective state-space models captured by Mamba models. Additional self-attention is used to model dependency between tracks. The method is evaluated on three tracking datasets, and it demonstrates a new state-of-the-art performance.

### Strengths
(1) The presented method achieves strong performance.

(2) the reason to integrate SSMs into a tracking-by-propagation framework is well motivated.

(3) The ablation studies conducted verified the introduced modifications.

(4) The paper is well written; the provided illustrative examples showcase strong results.

### Weaknesses
(1) There is a lack of qualitative comparison between prior works and the proposed method. It is helpful to see qualitative differences between methods' outputs to highlight what improvements in the models' output are contributing to the improvement in the performance. Specifically, visualizations showing how the proposed method handles occlusions, missed detections, and ID switches compared to existing methods would be beneficial.

(2) On L137, it is stated that  SambaMOTR has "the same GPU memory requirements". However, the paper lacks any measurements to back up this claim. Overall, there is emphasis placed on efficiency in the paper, so it would be good to include some measurements and comparisons to show these points. For example, including peak memory requirements and FLOPS would illustrate this point. Furthermore, a breakdown of memory usage by different components of the model (e.g., Mamba blocks, attention layers) would provide a more granular understanding of the model's efficiency.

(3) While the method shows strong results, chiefly due to architectural modifications, it is worth asking whether efficiency gains enable larger (higher capacity) models, which lead to improvements or whether the SSMs formulation provides better biases for the tracking problem. While it might be difficult to disentangle such factors, the paper could help guide future research in this area by reporting some (albeit not great) proxies, such as learnable parameter counts, the number of FLOPs per frame, and the size of the hidden state, to better understand the trade-offs between model size, computational cost, and performance.

### Questions
(1) Would it be possible to include a comparison of SambaMOTR on top of YOLOX-X to have an apple-to-apples comparison with prior tracking-by-detections works?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper introduces a tracking-by-propagation framework, SambaMOTR, which wanna tackles the question of how to model long-range dependencies within tracklets, interdependencies among tracklets, and the associated temporal occlusions. The core function of the  SambaMOTR is the Samba module, a novel linear-time set-of-sequences model designed to jointly process multiple tracklets by synchronizing the multiple selective state-spaces used to model each tracklet.  SambaMOTR is evaluated on DanceTrack, BFT, and SportsMOT datasets and achieves the state-of-the-art performance.

### Strengths
1. SambaMOTR introduces the novel linear-time set-of-sequences model designed to jointly process multiple tracklets by synchronizing the multiple selective state-spaces used to model each tracklet.
2. SambaMOTR achieves good tracking results on DanceTrack, BFT, and SportsMOT datasets.

### Weaknesses
1. The authors are advised to analyze the computational complexity, specifically detailing the time and space complexity of the proposed Samba module in both training and inference phases. It is crucial to understand how the linear-time claim scales with the number of tracklets and the length of the sequences, and to compare this with the complexity of other tracking methods.
2. The authors are advised to analyze why Samba is suitable for trajectory modeling and compare it with xLSTM, other SSMs, and RRNs. A more in-depth analysis is needed to justify the choice of the Samba module over other sequence modeling techniques, including a discussion on the specific properties of trajectories that make Samba a good fit. This should include a theoretical comparison of the representational power and inductive biases of these models.
3. The authors are advised to provide some tracking cases of SambaMOTR to demonstrate its superiority in trajectory modeling. It would be beneficial to see specific examples where SambaMOTR excels, particularly in challenging scenarios such as occlusions, long-term tracking, and complex motion patterns. These examples should be accompanied by a qualitative analysis of why SambaMOTR performs better in these cases.

### Questions
see Weaknesses.

### Soundness
4

### Presentation
4

### Contribution
3
