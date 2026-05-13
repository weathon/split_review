# RTMPose: Real-Time Models for Multi-Person Pose Estimation

- Decision: Reject
- Scores: 3, 5, 8

## Abstract
Recent studies on 2D pose estimation have achieved excellent performance on public benchmarks, yet its application in the industrial community still suffers from heavy model parameters and high latency. To bridge this gap, we empirically explore key factors in pose estimation including paradigm, model architecture, training strategy, and deployment, and present a high-performance real-time multi-person pose estimation pipeline, RTMPose. Our RTMPose-m achieves 75.8% AP on COCO with 90+ FPS on an Intel i7-11700 CPU and 430+ FPS on an NVIDIA GTX 1660 Ti GPU, and RTMPose-x achieves 65.3% AP on COCO-WholeBody. To further evaluate RTMPose's capability in critical real-time applications, we also report the performance after deploying on the mobile device. Our RTMPose-s model achieves 72.2% AP on COCO with 70+ FPS on a Snapdragon 865 chip, outperforming existing methods used by industrial companies.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper presents RTMPose, which is fast on mobile device and accurate at the same time. It explores five influencing factors to the performance and latency of multi-person pose estimation. By exploring the factors, RTMPose have a good balance between speed and performance.

### Strengths
1. Experiments are extensive. The five factors are thoroughly discussed and verified.
2. Results achieve nice balance between speed and performance, also on mobile devices.

### Weaknesses
1. The presentation of the paper is not good. There are a lot of typos and repetitive references. e.g., UDP (Huang et al., 2020), Crowdpose (Li et al., 2018);  Typos: Table 3.1?
2. Although experiments are extensively done, there is no interesting insight into the five factors, which seems hyper-parameter tuning to me.
In general, I don't think this paper is ready to be accepted.

### Questions
Please see weaknesses

### Soundness
3 good

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper aims at real-time multi-person pose estimation. It empirically explores key factors in pose estimation including paradigm, model architecture, training strategy, and deployment, and presents a high-performance, real-time multi-person pose estimation pipeline. Experimental results show that the proposed method achieves an excellent balance between performance and complexity. It can also be deployed on various devices (CPU, GPU, and mobile devices) for real-time inference.

### Strengths
-The proposed method empirically integrates key modules or factors in existing methods that contribute to real-time pose estimation, and an ablation study of each improving factor is given.

-The experimental results are impressive, demonstrating the high performance and efficiency of the proposed method.

### Weaknesses
1. Despite its high performance and efficiency, the proposed method is an integrated engineering framework of existing methods and training tricks, lacks its original methodological contributions, and is not suitable for top academic conferences like ICLR.

2. The writing can be improved. For example, 1) some symbols in Equations 1 and 2 are not defined, which should not be ignored for an academic paper; 2) some references have no journal or conference information (e.g., Huang 2020c, Li 2021c, Lyu 2022, etc.).

3. Typos. On page 4, "Table 3.1" should be "Table 1".

### Questions
Please see the weaknesses.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors present a high-performance real-time multi-person pose estimation model, which can achieve real-time inference speed on CPU, GPU, and mobile devices. This article may provide guidelines and references for designing future industrial-oriented pose estimation algorithms.

### Strengths
- The paper is well-written and easy to follow. The authors provide clear explanations of the paradigm, backbone network, localization method, training strategy, and deployment. 
- The paper conducts comprehensive inference speed validation on commonly used deployment frameworks and hardware platforms in the industry.
- The paper also includes helpful visualizations and figures to illustrate the key concepts.

### Weaknesses
 - Table 4 has a lot of content, but the analysis of the results is very thin.
- The author did not analyze why Large Kernel Convolution works. Some heat maps may be helpful for analysis.
- The author did not analyze why NVIDIA GeForce GTX 1660 Ti GPU and Intel I7-11700 CPU were chosen. Has the author tried other devices?

### Questions
Please refer to the Weakness above.

### Soundness
4 excellent

### Presentation
3 good

### Contribution
3 good
