# Action Typicality and Uniqueness Learning for Zero-Shot Video Anomaly Detection

- Decision: Reject
- Scores: 5, 3, 5, 5

## Abstract
Zero-Shot Video Anomaly Detection (ZS-VAD) is an urgent task in scenarios where the target video domain lacks training data due to various concerns, \emph{e.g.}, data privacy. The skeleton-based approach is a promising way to achieve ZS-VAD as it eliminates domain disparities in both background and human appearance. However, existing methods only learn low-level skeleton representation and rely on the domain-specific normality boundary, which cannot generalize well to new scenes with different normal and abnormal behavior patterns. In this paper, we propose a novel skeleton-based zero-shot video anomaly detection framework, which captures both scene-generic typical anomalies and scene-adaptive unique anomalies. Firstly, we introduce a language-guided typicality modeling module that projects skeleton snippets into action semantic space and learns generalizable typical distributions of normal and abnormal behavior. Secondly, we propose a test-time context uniqueness analysis module to finely analyze the spatio-temporal differences between skeleton snippets and then derive scene-adaptive boundaries. Without using any training samples from the target domain, our method achieves state-of-the-art results on four large-scale VAD datasets: ShanghaiTech, UBnormal, NWPU, and UCF-Crime. The Code will be publicly available.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This paper presents a novel Zero-Shot Video Anomaly Detection (ZS-VAD) approach that leverages action typicality and uniqueness learning. The proposed model incorporates two main components. First, a Language-Guided Typicality Modeling module projects skeleton snippets into a semantic space, learning typical behavior distributions (normal and abnormal) informed by experiential language model knowledge. Second, a Test-Time Uniqueness Analysis module examines spatio-temporal variations among skeleton snippets, establishing adaptive anomaly boundaries for diverse scenes.

### Strengths
This work is a good attempt at leveraging both typicality and uniqueness, offering a solution that utilizes large language models (LLMs) alongside test-time adaptability.

### Weaknesses
1. In reality, anomalies in many scenarios are distinguished by their deviation from the typical data for that specific scene. Without any normal data, it becomes challenging to define scene-dependent anomalies, reducing the task to change detection based on shifts in motion patterns and prior knowledge (or common sense) of a set of pre-defined actions. This approach risks misclassifying unusual but normal behaviors within a specific context as anomalies, since it lacks the ability to learn the nuances of what constitutes normal behavior within that scene. For instance, a person running in a normally quiet park might be flagged as anomalous, even if it's a regular occurrence during a specific time of day or for a particular event.
2. Besides, recognizing anomalies using only skeleton data loses the interaction information with the environment, which can hinder applications in real-world surveillance settings. The absence of contextual cues, such as interactions with objects or changes in the environment, limits the model's ability to detect complex anomalies. For example, a person picking up a prohibited item might be missed if the model only focuses on skeletal movements and not the object interaction itself.
3. Moreover, this method depends heavily on skeleton estimation and skeleton-based action recognition methods. If we already have a well-defined action recognition method and powerful LLM, identifying anomalies or normal behavior types could be achieved directly. Without these prerequisites, however, the necessity of using this approach for anomaly detection becomes less clear. A deeper explanation is needed to clarify the rationale behind the skeleton-text alignment, the selection of typicality knowledge, and the process for learning typicality distributions. The paper does not adequately address how the inherent uncertainty in skeleton estimation, especially in crowded or occluded scenes, impacts the overall anomaly detection performance. Furthermore, the reliance on pre-defined action categories might limit the model's ability to generalize to novel or unseen anomalous actions.

### Questions
Please refer to the Weaknesses. And the number of parameters, training and inference costs should be given.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper successfully implements zero-shot Video Anomaly Detection (VAD) by incorporating scene-related knowledge for the anomalous detection of human actions in videos, utilizing a Kinect-based large action classification dataset to train the skeleton encoder. It proposes a skeleton-based zero-shot video anomaly detection framework that can adaptively determine anomaly boundaries based on the scene.

### Strengths
1. The paper introduces the **Language-Guided Typicality Modeling module**, which maps skeleton snippets to a semantic space and computes KL divergence loss with features derived from a text encoder. Notably, during the alignment of skeletons and text, the authors innovatively incorporate a Large Language Model (LLM) for label classification (normal/abnormal), akin to how humans consider contextual factors when judging typical behavior distributions.
2. The analysis of skeleton snippets addresses temporal and spatial inconsistencies for cross-scene recognition. During the inference phase, the method filters results based on the proximity of spatiotemporal context graphs.
3. The authors achieve state-of-the-art (SOTA) performance on the ShanghaiTech, UBnormal, NWPU, and UCF-Crime datasets without using training data.

### Weaknesses
1. I have concerns regarding the Knowledge Collection section. Is it feasible to accurately classify action class texts using only a single prompt? What if the LLM considers a normal behavior in surveillance video, such as riding a bicycle, but it is classified as abnormal in the actual test set? This raises concerns about the robustness of the typicality scores derived from the LLM, especially if the LLM's understanding of 'normal' diverges from the ground truth in the target datasets. The reliance on a single prompt for such a crucial classification step seems overly simplistic and may not capture the nuances of real-world scenarios.
2. As noted by the authors in the limitations section of the appendix, the skeleton-based methods used in this study have limitations related to detectors and trackers, and they struggle to effectively handle single-person stable motion scenarios. This is a significant limitation, as many real-world anomaly detection scenarios involve single individuals exhibiting subtle deviations from normal behavior. The reliance on robust skeleton extraction and tracking also introduces a potential point of failure, as these methods are not always perfect and can be affected by occlusions, lighting conditions, and other environmental factors.
3. The **Uniqueness Analysis** in the inference phase seems applicable to any skeleton-based method, which raises questions about its originality. Specifically, the idea of filtering results based on the proximity of spatiotemporal context graphs is not novel in itself, and the paper does not adequately demonstrate how this particular implementation provides a unique advantage over existing approaches. The lack of novelty in this component undermines the overall contribution of the method.

### Questions
In summary, I find this paper has notable merits, including the innovative introduction of LLM for scene-related anomaly detection and the fine-tuning of the encoder. However, I remain skeptical about whether this straightforward approach can effectively address cross-scene challenges and generalize to more scenarios in a zero-shot manner. Additionally, I believe the **Uniqueness Scores** could offer insights applicable to any skeleton-based method.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper addresses zero-shot skeleton-based video anomaly detection. During training, the choice of a human behavior dataset is commendable, as it deviates from the commonly used datasets for Video Action Detection (VAD). The methodology of first learning visual features of skeletal points through an encoder and then extracting these features for input into a classifier (NF) is innovative. This approach avoids the previous practice of directly using skeletal point coordinates as classifier input to determine normality or abnormality.

### Strengths
The computation of two graphs, as seen in many papers, is well-executed here. One graph captures the motion relationships between adjacent individuals within the current data segment, while the other graph represents the motion state of the same individual across different data segments. This dual-graph approach provides a comprehensive understanding of human motion.

The model learns high-level semantic features, which enables a better representation of the data. This leads to improved performance in various tasks.

By utilizing an action recognition dataset, the model can learn a wider range of behavior categories, allowing for better generalization across multiple scenarios.

### Weaknesses
This paper lacks innovation. Language-guide action learning is a common technique in zero-shot action recognition, such as [1,2], and the author merely applied it to anomaly detection. The method presented is primarily based on STG-NF [3], which can be regarded as an extension of STG-NF incorporating language-guided and zero-shot capabilities.

The backbone of the method is the multi-scale CTR-GCN, while the backbone of STG-NF is ST-GCN. Therefore, it is unfair to compare the experimental results of this paper directly with those of STG-NF. I would like to know how the author's method performs on the popular setting of VAD.

The model struggles with anomaly detection when the motion trajectory becomes stable. This highlights a potential weakness in the model's ability to handle certain types of data patterns.

The visualization results in Figure 4 and Figure 6 are ugly. The font size used to represent the anomaly score is too large.

### Questions
N/A

### Soundness
2

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
3

### Summary
This paper proposes a new method for zero-shot video anomaly detection. Specifically, it first utilizes a module to align the skeleton and text for generalizable skeleton representations among normal and abnormal behaviors. Secondly, the high-confidence skeleton samples are selected to learn distributions. Then, the cross-person and self-inspection graphs are designed to calculate the uniqueness score for test-time adaption. Extensive experiments show the superior performance of the proposed method.

### Strengths
1. The experimental results achieve the sota.
2. The insights in test-time uniqueness analysis should be appreciated.
3. The experiments are comprehensive and solid.

### Weaknesses
1. The paper is not well-written. Some symbols and details are not described well.

2. What does the $T$ in line 197 denote? The decompose process should be described in detail. What are the $g_i, g_j$ refer? And what are the $i$ and $j$ denote? They should be described clearly.

3. For typicality knowledge distillation, if I am not wrong, the equation seems to select one skeleton sequence with the most similar text label in each category, so how does this equation address the challenges proposed in Lines 225-227?

4. In line 281, how does the $A_i$ is associated with the person graph $p_i$ and timestamp $t_i$. The subscript can be denoted as the spatial index and temporal index concurrently. I am confused about that; it should be introduced clearly. The symbols in Eqa (8) and Eqa (9) are unclear; the subscripts for the person and timestep indexes are the same.

5. I am confused about the uniqueness scores. The uniqueness score is also high if the different normal actions exhibit low similarity/distance in different timesteps. So how do we ensure the high distance means anomaly accurately?

6. In the training phase, the dataset used is inconsistent with the previous methods. How does the author ensure the equability with other sota methods?

### Questions
1. What does the $T$ in line 197 denote? The decompose process should be described in detail. What are the $g_i, g_j$ refer? And what are the $i$ and $j$ denote? They should be described clearly.
2. For typicality knowledge distillation, if I am not wrong, the equation seems to select one skeleton sequence with the most similar text label in each category, so how does this equation address the challenges proposed in Lines 225-227?
3. In line 281, how does the $A_i$ is associated with the person graph $p_i$ and timestamp $t_i$. The subscript can be denoted as the spatial index and temporal index concurrently. I am confused about that; it should be introduced clearly. The symbols in Eqa (8) and Eqa (9) are unclear; the subscripts for the person and timestep indexes are the same. 
4. I am confused about the uniqueness scores. The uniqueness score is also high if the different normal actions exhibit low similarity/distance in different timesteps. So how do we ensure the high distance means anomaly accurately?
5. In the training phase, the dataset used is inconsistent with the previous methods. How does the author ensure the equability with other sota methods?

### Soundness
3

### Presentation
1

### Contribution
2
