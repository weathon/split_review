# MMR: A Large-scale Benchmark Dataset for Multi-target and Multi-granularity Reasoning Segmentation

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6

## Abstract
The fusion of Large Language Models (LLMs) with vision models is pioneering new possibilities in user-interactive vision-language tasks. A notable application is reasoning segmentation, where models generate pixel-level segmentation masks by comprehending implicit meanings in human instructions. However, seamless human-AI interaction demands more than just object-level recognition; it requires understanding both objects and the functions of their detailed parts, particularly in multi-target scenarios. For example, when instructing a robot to "turn on the TV," there could be various ways to accomplish this command. Recognizing multiple objects capable of turning on the TV, such as the TV itself or a remote control (multi-target), provides more flexible options and aids in finding the optimized scenario. Furthermore, understanding specific parts of these objects, like the TV's button or the remote's button (part-level), is important for completing the action. Unfortunately, current reasoning segmentation datasets predominantly focus on a single target object-level reasoning, which limits the detailed recognition of an object's parts in multi-target contexts. To address this gap, we construct a large-scale dataset called Multi-target and Multi-granularity Reasoning (MMR). MMR comprises 194K complex and implicit instructions that consider multi-target, object-level, and part-level aspects, based on pre-existing image-mask sets. This dataset supports diverse and context-aware interactions by hierarchically providing object and part information. Moreover, we propose a straightforward yet effective framework for multi-target, object-level, and part-level reasoning segmentation. Experimental results on MMR show that the proposed method can reason effectively in multi-target and multi-granularity scenarios, while the existing reasoning segmentation model still has room for improvement.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper provides a large multi-target and multi-granularity reasoning segmentation benchmark. Based on this benchmark, this paper designs a baseline model trained on it while evaluating public datasets to present the effectiveness of both the benchmarks and the baseline. Experiments demonstrate that the proposed baseline outperforms LISA and other representative approaches.

### Strengths
1. The distinguishing characteristic of the proposed benchmark is clear, which includes multi-granularity and more images.
2. Multi-target and multi-granularity reasoning segmentation is a valuable research topic.
3. The overall writing is fluent.

### Weaknesses
1. This paper provides few comparisons on the proposed benchmark. It is not clear whether the proposed baseline model outperforms other MLLMs on multi-target and multi-granularity reasoning segmentation. Specifically, the paper lacks a thorough comparison against other state-of-the-art models designed for similar tasks. The absence of such comparisons makes it difficult to ascertain the true effectiveness and novelty of the proposed baseline.
2. The major contribution lies in the benchmark, while this benchmark is auto-annotated based on the existing dataset PACO-LVIS, which hurts the contribution. The reliance on auto-annotation, even if based on an existing dataset, raises concerns about the quality and potential biases introduced during the annotation process. This approach might limit the benchmark's ability to capture the nuances of human-level reasoning.
3. According to Table 1, MMR offers both object-level and multi-target annotations, making it more comprehensive than ReasonSeg and MUSE. This paper could include zero-shot evaluations on these two benchmarks to further demonstrate effectiveness. The lack of zero-shot evaluations on ReasonSeg and MUSE limits the assessment of the benchmark's generalizability and its ability to handle diverse reasoning scenarios.

### Questions
Please refer to the weaknesses.

### Soundness
3

### Presentation
3

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
This paper introduces a dataset named MMR, designed for multi-target and multi-granularity reasoning segmentation tasks. The goal is to address challenges in reasoning across multiple targets and different levels of granularity. The dataset comprises complex and implicit question pairs, covering both object-level and part-level reasoning. Additionally, the paper proposes a baseline model, M2SA, to achieve multi-target, object-level, and part-level reasoning segmentation.

### Strengths
1. **Clear Writing**: The paper is well-organized and easy to understand.

2. **Significant Contribution of the Dataset**: The MMR dataset contains 196K samples. Although it was generated using large models, a rigorous filtering process was employed to ensure data quality.

### Weaknesses
1. **Lack of Targeted Design in the Baseline Model**: The baseline model (Early Local Feature Fusion and Multi [SEG] Tokens) does not incorporate specific structures to effectively address the multi-target and part-level reasoning required by the MMR dataset. The use of multiple [SEG] tokens, while allowing for multiple outputs, does not inherently enforce relationships or dependencies between these outputs, which is crucial for multi-target reasoning. Similarly, early local feature fusion, while preserving spatial information, may not be sufficient to capture the complex hierarchical relationships between objects and their parts. As a result, it lacks novelty, leading to underwhelming performance in Table 3.

2. **Limited Performance in Table 3**: The comparison methods in Table 3 are not sufficiently recent. The authors did not include comparisons with more relevant multi-target approaches, such as GSVA [1] or GLaMM [2]. This limits the impact of the proposed approach, as the results are not very competitive. The evaluation in Table 3 focuses on referring expression segmentation, which is a simpler task than the multi-target, multi-granularity reasoning segmentation that the MMR dataset is designed for. This makes the comparison less meaningful for evaluating the core capabilities of the proposed model.

3. **Insufficient Comparisons in Table 2**: The methods compared in Table 2 are too limited. I strongly recommend including more methods that could be adapted for the MMR task to facilitate meaningful comparisons for future research.

### Questions
1. Will the proposed dataset be made publicly available?
2. The paper mentions the use of 4 A6000 GPUs. How long does it take to train the proposed model on the MMR dataset?

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
5

### Summary
This paper introduces a novel dataset, MMR, the first part-level dataset for the reasoning segmentation tasks. In addition, a new network framework is proposed to leverage low-level fine-grained information and to address the limitation of the existing LISA model, which can only segment a single object. The authors conduct experiments to evaluate the performance of existing methods on the proposed MMR dataset and demonstrate the advantages of the proposed network framework.

### Strengths
1. This paper is well written and easy to follow. 
2. The proposed MMR dataset is highly valuable to the research community, as part-level reasoning segmentation is crucial in real-world applications, such as robotic control. However, there is currently a lack of available datasets for research in this area.
3. A detailed analysis is provided to thoroughly present the characteristics of the MMR dataset.

### Weaknesses
1. The contributions of the proposed M2SA network framework are incremental. The early local feature fusion appears to be only a minor structural modification, lacking a clear demonstration of significant novelty or impact on performance compared to existing methods. Additionally, the strategy of employing multiple [SEG] tokens has already been introduced in earlier methods, such as [a]. The authors should clarify the specific differences between their approach and [a] in terms of how the [SEG] tokens are utilized and what unique information they encode, beyond simply segmenting multiple objects.
2. This paper could benefit from more thorough experiments based on the characteristics of the dataset. For instance, the analysis of the long-tail phenomenon should not only consider the performance difference between frequent and infrequent categories, but also include a detailed analysis of the types of errors made by the model on infrequent categories. This would provide a more nuanced understanding of the model's limitations. Additionally, the paper lacks a comprehensive evaluation of the model’s open-vocabulary performance. While the authors mention the potential for open-vocabulary evaluation, they do not provide any concrete results or analysis in this area. The absence of such results limits the assessment of the model's generalization capabilities.
3. More examples of the image-question-answer triplet in the MMR dataset could be presented in the paper to enable readers to understand the characteristics of the dataset more quickly and intuitively. The current examples are insufficient to fully grasp the complexity and diversity of the reasoning tasks involved.

### Questions
1. Why did you remove the generated questions that contain explicit target coordinates or strong hints? I think training with such data would enhance the model’s ability to handle target-specific inputs. For example, if an image contains two different animals, a fish and a cat, users could indicate the coordinates of the animal they are interested in and ask, “Which part of this animal [coordinates] uses its sense of smell?” The model could then segment either the nose or the fish’s gills depending on the coordinates provided. This could be quite interesting.

### Soundness
3

### Presentation
4

### Contribution
3
