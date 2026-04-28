# Point Cluster: A Compact Message Unit for Communication-Efficient Collaborative Perception

- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 8, 6, 6

## Abstract
The objective of the collaborative perception task is to enhance the individual agent's perception capability through message communication among neighboring agents. A central challenge lies in optimizing the inherent trade-off between perception ability and communication cost. To tackle this bottleneck issue, we argue that a good message unit should encapsulate both semantic and structural information in a sparse format, a feature not present in prior approaches. In this paper, we innovatively propose a compact message unit, namely point cluster, whose core idea is to represent potential objects efficiently with explicitly decoupled low-level structure information and high-level semantic information. Building upon this new message unit, we propose a comprehensive framework CPPC for communication-efficient collaborative perception. The core principle of CPPC is twofold: first, through strategical point sampling, structure information can be well preserved with a few key points, which can significantly reduce communication cost; second, the sequence format of point clusters enables efficient message aggregation by set matching and merging, thereby eliminating unnecessary computation generated when aligning squared BEV maps, especially for long-range collaboration. To handle time latency and pose errors encountered in real-world scenarios, we also carefully design parameter-free solutions that can adapt to different noisy levels without finetuning. Experiments on two widely recognized collaborative perception benchmarks showcase the superior performance of our method compared to the previous state-of-the-art approaches.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
1

### Summary
This paper presents a new message unit, the "point cluster," to improve collaborative perception efficiency in multi-agent systems. Unlike existing message units such as raw point clouds, bounding boxes, or BEV maps, the point cluster format minimizes bandwidth usage while retaining essential structural and semantic information. Representing objects with point coordinates, a cluster center, and semantic features, this approach allows efficient inter-agent information exchange, enhances object alignment, and preserves object structure for more accurate detection. A new framework, CPPC, combines point packing and aggregation modules, addressing issues like bandwidth constraints, time delay, and pose errors, and achieves state-of-the-art performance on several benchmarks.

### Strengths
1. **Bandwidth Efficiency**: The proposed "point cluster" message unit significantly reduces communication bandwidth by capturing only essential foreground object information in a sparse format, making it highly efficient compared to dense representations like raw point clouds and BEV maps.

2. **Enhanced Object Detection Accuracy**: By preserving detailed structural and semantic information, the point cluster improves object detection accuracy, especially in complex multi-agent scenarios, demonstrating superior performance on established collaborative perception benchmarks.

3. **Robustness to Real-world Challenges**: The CPPC framework includes robust mechanisms for handling pose errors and time delays, crucial for real-world applications. Parameter-free solutions for pose and latency issues make it adaptable to various levels of noise without additional tuning.

4. **Clear and Effective Writing**: The paper is well-written, with a clear explanation of the proposed methods and thorough descriptions of experiments, which makes the complex technical content accessible and supports the credibility and reproducibility of the research findings.

### Weaknesses
In terms of methodology, there is a noticeable reliance on FSD, which slightly reduces the originality. However, overall, the approach is still reasonable.

### Questions
No questions.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper proposes a novel message exchange unit called point cluster for collaborative perception. Point clusters can efficiently and compactly represent an object's location, structure, and semantic information. The proposed CPPC framework includes point cluster-based encoding, packing, exchange, and integration methods. CPPC improves both communication efficiency and perception accuracy while being robust to various real-world noises. Experimental results on various benchmarks demonstrate that CPPC significantly outperforms existing methods.

### Strengths
This paper systematically analyzes the advantages and disadvantages of existing collaborative perception methods (early, intermediate, late collaboration) and proposes a rational solution considering the inherent trade-off between communication efficiency and perception performance. 
The proposed point cluster is a compact message unit that selectively combines the strengths of existing methods and efficiently represents both structural and semantic information of objects. 
CPPC introduces parameter-free approaches to handle pose error and time latency issues encountered in real-world scenarios, ensuring robustness to various noise levels. 
This paper clearly identifies the current challenges and limitations in the field of collaborative perception and demonstrates how the proposed method can rationally solve them.
Through clear problem formulation, the collaborative perception problem is mathematically defined, and based on this, the motivation and principles of the proposed method are lucidly explained.

### Weaknesses
Based on the proposed technique, the amount of data that can be transmitted is limited. Therefore, it is crucial to prioritize foreground objects and bring them in a sparse manner to distinguish the overall shape, rather than bringing only a few parts. Regarding this aspect, I wonder if there are any criteria or tendencies for determining which points should be selected and what rules should be followed. Additionally, I am curious about the extent of performance degradation when background information is included instead of solely focusing on the foreground.

If we follow the logic mentioned above, I wonder if we can expect sufficient performance improvement in early or late collaboration by only bringing foreground information and adjusting it according to the available bandwidth.

- In Figure 4(a), there is a section where the performance of the proposed method rises sharply. I am curious about the reason behind this phenomenon and how the performance of the proposed method would differ from existing technologies if the communication volume is lower than this point.
- On Page 7, Line 373, it is mentioned that the proposed method shows improvements of 5.7%, 7.3%, and 12.8%, but it is unclear which methods are being compared. 
- On Page 7, Line 377, the term "late collaboration" is used. I am curious about which specific technique this refers to.

If we assume some objects are moving at high speeds, I think the errors caused by delay would vary for each object. It seems this aspect might not be covered, does the proposed method handle this problem?

### Questions
If we assume some objects are moving at high speeds, I think the errors caused by delay would vary for each object. It seems this aspect might not be covered, does the proposed method handle this problem?

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces a communication-efficient collaborative perception (CPPC) framework for vehicle-to-everything autonomous driving. Unlike previous methods that mainly rely on BEV features, the CPPC framework leverages point clusters to control its computational complexity and alleviate issues like high-level information loss. Specifically, the CPPC framework consists of a point cluster picking module, a pose alignment and latency compensation module, and a point cluster aggregation module to generate cluster features for subsequent predictions. The CPPC framework outperforms existing BEV-based methods on three public datasets, including V2XSet, OPV2V, and DAIR-V2X-C.

### Strengths
\+ This paper is written well and the motivation behind the proposed method is easy to follow.

\+ The proposed method is a systematic solution for multi-agent perception, which exploits point clusters as the intermediate representation with controllable communication costs, to balance efficiency and effectiveness. 

\+ The proposed method outperforms several previous methods on three public datasets consistently. The extensive experimental results validate the effectiveness of the proposed modules.

### Weaknesses
 - There are four thresholds used in the proposed method, which may be hard to choose in complex or unseen scenarios.

- The proposed method mainly considers BEV-based methods for comparisons, however, it is unclear how significant its technical contributions are compared with previous point-cloud-based methods (e.g., Cooper, F-cooper). I am concerned about this because the techniques used in the main components of the proposed method, including point cluster picking, pose correction, and the SD-FPS, are quite common in the research communities of point cloud processing. Specifically, the point cluster picking seems to rely on simple distance-based clustering, which might not be robust in scenarios with varying point densities or occlusions. The pose correction module, while necessary, appears to use standard ICP or similar techniques, lacking novelty. Furthermore, the SD-FPS, while incorporating semantic information, is still fundamentally a sampling method, and its contribution over existing sampling techniques is not clearly demonstrated. The paper needs to better articulate the novelty of combining these existing techniques in the context of collaborative perception.

### Questions
My current concerns are mainly about the technical contributions of the proposed method. I may change my rating after reading other reviewers' comments and the authors' rebuttal. Here are some questions I wish could be addressed:

Q1: In the proposed SD-FPS method, how to balance the weights of semantic and spatial distances ($\lambda_s$ and $\lambda_d$)? How will they affect the performance of the proposed method?

Q2: Does the proposed method perform well in a crowded environment where many objects are exhibited?

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper proposes to use Point Cluster as the message unit for collaborative perception. Previous intermediate methods use BEV map as the message unit, which suffer from weak object features, inefficient message aggregation and vague boundary. The proposed point cluster-based framework can solve these problems well. Extensive experiments on V2XSet, OPV2V, and DAIR-V2X-C demonstrate the effectiveness of the proposed method.

### Strengths
1. Using point cluster as an intermediate message unit is novel and well-motivated.
2. The proposed CPPC framework, as well as the PCE, PCP and PCA modules are solid.
3. State-of-the-art performance on mainstream benchmarks.

### Weaknesses
My main concerns are about the effectiveness and efficiency of the proposed method, for which I think more ablation studies are required.
1. Ablation studies on PCP, PCA, pose correction and latency compensation are required.
2. The authors claim the BEV representation is inefficient during aggregation. Is there any comparison between BEV and Point Cluster-based methods?

### Questions
In section 3.5, can the authors detail "spatial cluster matching"? If the pose between two agents is not accurate, how to match point clusters from different agents into a single object?

### Soundness
3

### Presentation
3

### Contribution
3
