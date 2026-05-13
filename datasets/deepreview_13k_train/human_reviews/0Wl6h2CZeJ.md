# RealTracker: Simpler and Better Point Tracking by Pseudo-Labelling Real Videos

- Decision: Reject
- Scores: 6, 5, 6, 5

## Abstract
Most state-of-the-art point trackers are trained on synthetic data due to the difficulty of annotating real videos for this task.
However, this can result in suboptimal performance due to the statistical gap between synthetic and real videos.
In order to understand these issues better, we introduce \method, comprising a new tracking model and a new semi-supervised training recipe.
This allows real videos without annotations to be used during training by generating pseudo-labels using off-the-shelf teachers.
The new model eliminates or simplifies components from previous trackers, resulting in a simpler and often smaller architecture.
This training scheme is much simpler than prior work and achieves better results using 1,000 times less data.
We further study the scaling behaviour to understand the impact of using more real unsupervised data in point tracking.
The model is available in online and offline variants and reliably tracks visible and occluded points.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes a simpler and better point tracking approach by pseudo-learning real videos. Specifically, the proposed approach allows real videos without annotations to be used during training by generating pseudo-labels using off-the-shelf teachers. The proposed approach explores to use real video for training point tracking models w/o annotations. Moreover, the authors also study the scaling law to understand the impact of using more real training videos.

### Strengths
- The paper focuses on an interesting problem in the community, i.e., aiming to explore to train TAP models w/ real videos w/o annotations, since the previous approaches mainly focus on learning w/ synthetic datasets;
- The proposed RealTracker shows that a simpler architecture and training protocols can outperform SOTA trackers like BootsTAPIR and LocoTrack;
- The paper is well written and organized;

### Weaknesses
 - Using pseudo-labels for training trackers is well explored, e.g., for some online learning-based trackers like Dino-Tracker, it uses pre-computed optical flow which provides the pseudo ground truth pixel-level correspondences for online training the tracker. For DinoTracker3, pseudo-labelling is explored. Please illustrate more differences with these trackers for better highlighting the contributions;
- Are there any specific concerns for choosing a teacher model for pseudo label generation? Does the better teacher model with higher tracking performance commonly lead to better tracking performance? Can a single teacher model well support the tracker learning?
-  In Table 2, the time of the per frame and per tracked point is shown. For the online variant, what’s the overall tracking speed (i.e., fps) given an online testing video?
- Missing Refs for discussion. For completeness, please include more pseudo-label based tracker training approaches [1,2,3,4] for discussion in the related work.

### Questions
Overall, I think this is an interesting paper that focuses on an essential problem in the community, i.g., enabling existing TAP trackers to leverage real videos w/o annotations for training. The idea is somewhat incremental but effectively addresses an essential problem in a simple yet effective way. Thus my current rating is ``accept''. I would like to see more author rebuttal in terms of differences w/ existing pseudo label based approaches as mentioned above.

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
3

### Summary
1. The authors address the redundancy in modules of various existing point tracking models and propose RealTracker, a network with simplified architecture that achieves better performance and faster processing speed.

2. The authors leverage existing models to generate pseudo-labels for real video data, enabling effective utilization of unlabeled videos for network fine-tuning, which further enhances performance.

3. The authors analyze the impact of real data scale on the network model's performance, providing insights into the relationship between dataset size and tracking effectiveness.

### Strengths
1. The paper's motivation is well-justified, particularly in its approach to eliminate model redundancies, resulting in a more lightweight yet powerful architecture.
2. The paper demonstrates effective utilization of unlabeled real-world datasets for training, achieving significant performance improvements through this approach.
3. The experimental analysis is comprehensive, and the visualization results are particularly impressive in demonstrating the model's capabilities.

### Weaknesses
1. The methodology appears to be more engineering-oriented rather than theoretically innovative, primarily consisting of combinations and modifications of existing methods. The pseudo-label fine-tuning approach, while effective, lacks novelty, as it is a relatively common technique in deep learning. Given this is a **deep learning conference**, the technical contributions seem somewhat limited, particularly in the absence of a novel loss function, optimization strategy, or architectural component that significantly advances the field.
2. As acknowledged in the limitations section, the model's improvement of performance is heavily dependent on the teacher model's capabilities. This strong reliance on existing methods' performance creates a ceiling effect where the training results are constrained by the teacher model's performance limits, potentially reducing the method's generalizability. The paper does not explore methods to mitigate this dependency, such as using an ensemble of diverse teacher models or incorporating techniques to reduce the impact of inaccurate pseudo-labels.
3. The authors aim to bridge the domain gap using real-world dataset training. However, the paper lacks substantial technical innovation in terms of cross-domain adaptation techniques. The approach merely relies on real-data fine-tuning and teacher model voting effects for enhanced robustness, neither of which represents a significant contribution to the field of domain adaptation. The paper does not explore more advanced techniques such as adversarial domain adaptation, domain-invariant feature learning, or discrepancy-based methods, which could have provided a more robust solution to the domain shift problem.

### Questions
1. The terminology "self-supervised fine-tuning" is indeed questionable in this context. Using state-of-the-art models from the same domain to generate pseudo-labels for supervision is more aligned with teacher-student learning or pseudo-labeling approaches rather than traditional self-supervised learning, where the supervision signals are typically derived from the data itself without external models.

2. The incorporation of domain adaptation strategies during the fine-tuning process would have significantly enhanced the paper's contribution. This could have included techniques specifically designed to address domain shift and better align feature distributions between source and target domains.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
the approach leverages other point trackers to produce training data  for their point tracker.  Supposedly less additional training data is required compared to other point trackers.   The biggest contribution is that the other trackers use real data and not synthetic data for training.   Other approaches in the past have typically used point data for tracking.

### Strengths
The paper incrementally builds upon point trackers by producing a better approach that leverages other point trackers to produce supervised training data.  In the past other trackers have used synthesized data however this is all based on real data.  The results seem to better than other point trackers.

### Weaknesses
It is not clear on what type of motions were tested, if parallax for motion is required, what about zooming like motions with no parallax, does the method work.
What % of occlusion in terms of coverage of the object and in terms of time occluded were not clearly tested.
The limitations and failure cases of the algorithm were not explored.

From Table 2, it appears that the training set does matter in the results, The methods training with Kub+15M performed on average better than the methods trained with Kub, please explain and elaborate.  What is the difference?
Why does the offline method perform better than the online method, Intuitively I would assume the opposite?
Table 6, why does SIFT turn on the best results?

### Questions
From Table 2, it appears that the training set does matter in the results, The methods training with Kub+15M performed on average better than the methods trained with Kub, please explain and elaborate.  What is the difference?
Why does the offline method perform better than the online method, Intuitively I would assume the opposite?
What are the limitations and failure cases?
Table 6, why does SIFT turn on the best results?

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
This paper introduces the RealTracker, a point tracker that combines several ideas from other related trackers but eliminates some components and simplifies others. RealTracker also designes a semi-supervised training protocol, where real videos are annotated utilizing several off-the-shelf trackers. With this protocol, RealTracker can achieve encouraging results on the Kinetics, RGB-S, and DAVIS datasets.

### Strengths
1. RealTracker combines valuable ideas from the recent state-of-the-art point trackers and eliminates some unimportant modules.
2. RealTracker proposes a simple semi-supervised training protocol and achieves better results on several public datasets compared to state-of-the-art trackers.
3. RealTracker explores the training scaling low via its proposed training protocol.

### Weaknesses
1. The idea of using trackers to annotate unlabeled datasets, such as [1], is not new.
2. The authors should use the Kub+15M data to train the CoTracker and TAPTR and verify the proposed method's effectiveness.
3. To prove the effectiveness of the RealTracker, it is suggested that confidence and visibility be visualized.
4. More ablation studies are suggested to verify that eliminating some modules in the listed trackers and simplifying some modules is useful, including the computation cost and tracking performance.

### Questions
Please follow the weakness. If the issues are addressed,  I will improve the rating.

### Soundness
3

### Presentation
3

### Contribution
3
