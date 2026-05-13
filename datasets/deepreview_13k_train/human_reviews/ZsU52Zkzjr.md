# PvNeXt: Rethinking Network Design and Temporal Motion for Point Cloud Video Recognition

- Decision: Accept
- Scores: 6, 8, 6

## Abstract
Point cloud video perception has become an essential task for the realm of 3D vision. Current 4D representation learning techniques typically engage in iterative processing coupled with dense query operations. Although effective in capturing temporal features, this approach leads to substantial computational redundancy. In this work, we propose a framework, named as PvNeXt, for effective yet efficient point cloud video recognition, via personalized one-shot query operation. Specially, PvNeXt consists of two modules, a Motion Imitator and a Single-Step Motion Encoder.  The former module, the Motion Imitator, is designed to capture the temporal dynamics inherent in sequences of point clouds, thus generating the virtual motion corresponding to each frame. The Single-Step Motion Encoder, is tasked with performing a one-step query operation from points to their corresponding virtual frames with motion. Through the integration of these two modules, PvNeXt enables personalized one-shot queries for each frame, effectively eliminating the need for frame-specific looping and intensive query processes.  Extensive experiments on multiple benchmarks demonstrate the effectiveness of our method, with significantly cheaper training costs. Notably, PvNeXt gains a $1.95$ accuracy increase with $23$x inference speedup on the widely used point cloud video recognition benchmark MSR-Action3D compared to PST-Transformer, while the latter takes over $60$x larger parameters. Codes will be available soon.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces a novel framework, PvNeXt, designed for efficient point cloud video recognition. PvNeXt leverages a personalized one-shot query mechanism to significantly reduce computational redundancy by avoiding frequent inter-frame queries, commonly seen in traditional methods. The framework incorporates two key modules: the “Motion Imitator” and the “Single-Step Motion Encoder,” which capture temporal dynamics effectively across point cloud sequences. Experimental results show that PvNeXt achieves high accuracy and significantly improved inference speed and memory efficiency on MSR-Action3D and NTU-RGBD datasets.

### Strengths
1. Efficiency: PvNeXt uses a one-shot query operation that eliminates complex looping and dense queries, achieving a 23x speedup in inference compared to other methods, which greatly reduces computational costs.

2. Low Resource Usage: The model requires only 0.72M parameters, reducing the parameter count by almost 98% compared to traditional methods, making it suitable for deployment on resource-constrained devices.

3. Innovative Design: The introduction of the “Motion Imitator” and “Single-Step Motion Encoder” modules enables effective temporal and spatial modeling of dynamic information within point cloud sequences.

### Weaknesses
1. Lower Accuracy: PvNeXt shows lower recognition accuracy compared to pose [1], RGB [2] and depth-based [2] modalities, highlighting the limitations of using only the point cloud modality for capturing complex dynamic information.

2. Limited Applicability: The model is primarily optimized for action recognition in point cloud videos and lacks validation for other tasks, such as object recognition or scene understanding [3], limiting its generalizability.

3. Potential Difficulty in Capturing Fine-Grained Motion: The one-shot query mechanism, while efficient, might struggle to capture very subtle or intricate motions across frames, which could impact performance in scenarios requiring high precision for small movements.

### Questions
1. Could you clarify the practical significance of using point cloud video for action recognition, especially considering that RGB, depth, and pose data have demonstrated better performance?

2. Please update Table 10 to include comparisons with more recent methods, and add efficiency evaluation metrics such as FLOPs and Params.

### Soundness
3

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
5

### Summary
The article proposes a point cloud video classification framework, rethinks the core issues of framework design and provides reasonable solutions. The article uses two key modules, Motion Imitator and the Single-Step Motion Encoder, to significantly accelerate the classification efficiency of point cloud videos. The authors also verified the effectiveness of this scheme on two human datasets.

### Strengths
1. The problem of understanding point cloud videos is very important. This article rethinks the key challenges and network design in this field, providing inspiration for progress in this direction.
2. The article points out two core challenges of current networks in terms of computational overhead, the need to traverse all frames and the overlap of local point cloud patches. This observation is reasonable.
3. The article found that effective feature extraction can be achieved by only performing one-step queries between local regions between adjacent frames, which is an interesting discovery.
4. This experimental finding also shows that we need more new 4D tasks, in addition to classification, there are also segmentation, prediction, etc.
5. The previous method proposed to reduce the range of the receptive field in the spatial dimension. This article proposes to reduce the receptive field in the temporal dimension and achieve good performance.

### Weaknesses
1. Motion imitator implicitly performs point tracking to learn the adjacent frame correlation of dense points. The single step motion encoder learns motion information to encode features based on the learned correlations. If I understand correctly, how does the author measure the correlation learned by the motion imitator? Because this correlation is easy to learn on the human body, it becomes significantly more difficult when other objects or backgrounds are included.
2. The author can calculate calculate the distance between the predicted human point cloud and the GT point cloud to evaluate the ability of the motion imitator. I think this link is easy to learn on the human dataset, and can even be calculated manually by some methods, but when it includes occlusion problems, scene backgrounds, and interactive objects, can it still be learned? This conclusion is very important for the design of future 4D networks because it determines whether we need to perform point tracking explicitly or implicitly.
3. Because NTU-RGBD contains background scene information, its results are not better than the baeline of PST-Transformer, which may also confirm the limitations of the method when the motion imitator is difficult to learn.
4. This paradigm of the article is only experimented on human point cloud recognition. Can this method be extended to point cloud video action segmentation tasks such as HOI4D action segmentation task, because these tasks require predicting a label for each frame and are more relevant to robotics or AR/VR applications. I am very curious whether the article method is effective in this dense prediction task.

### Questions
I think the article proposes a very interesting perspective to redesign the network architecture of point cloud videos, and this research is inspiring. However, some conclusions are still unclear, such as how to evaluate the learning performance of the motion imitator, whether point tracking is still easy to learn in other scenarios, and how this method performs on dense prediction tasks like HOI4D action segmentation task. The author can try to explain these key concerns, and I am very willing to improve the score.

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
Considering traditional method capture temporal features effectively but at a high computational cost. The paper addresses the computational challenges in point cloud video perception by introducing PvNeXt, an efficient framework for 3D video recognition. PvNeXt introduces a more efficient approach through two main modules: the Motion Imitator models temporal dynamics by generating virtual motion for each frame and the Single-Step Motion Encoder captures motion cues and temporal dynamics in a single step.

### Strengths
1. PvNeXt reduces computational redundancy by replacing iterative, dense query operations with a one-shot query mechanism, enabling faster inference and lower training costs.
2. In experiment, the PvNeXt achieve SOTA especially in flops and parameters.
3. In experiment, the paper provide comprehensive ablation studies and discussion.

### Weaknesses
The conclusion is too short, lack of analysis of network limitations and discussion of application scenarios since the network is lightweight. Are there particular types of limitations you think should be discussed? Or specific application areas where the lightweight nature could be especially impactful?

### Questions
Can the method proposed in the paper still effectively solve the problem of longer time-series data or very fast high-speed motion?

### Soundness
3

### Presentation
3

### Contribution
3
