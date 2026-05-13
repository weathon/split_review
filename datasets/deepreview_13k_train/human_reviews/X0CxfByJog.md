# Breaking Class Barriers: Efficient Dataset Distillation via Inter-Class Feature Compensator

- Decision: Accept
- Scores: 3, 5, 6, 8

## Abstract
Dataset distillation has emerged as a technique aiming to condense informative features from large, natural datasets into a compact and synthetic form. 
While recent advancements have refined this technique, its performance is bottlenecked by the prevailing class-specific synthesis paradigm. 
Under this paradigm, synthetic data is optimized exclusively for a pre-assigned one-hot label, creating an implicit class barrier in feature condensation. 
This leads to inefficient utilization of the distillation budget and oversight of inter-class feature distributions, which ultimately limits the effectiveness and efficiency, as demonstrated in our analysis.
To overcome these constraints, this paper presents the Inter-class Feature Compensator (INFER), an innovative distillation approach that transcends the class-specific data-label framework widely utilized in current dataset distillation methods. Specifically, 
INFER leverages a Universal Feature Compensator (UFC) to enhance feature integration across classes, enabling the generation of multiple additional synthetic instances from a single UFC input.
This significantly improves the efficiency of the distillation budget.
Moreover, INFER enriches inter-class interactions during the distillation, thereby enhancing the effectiveness and  generalizability of the distilled data.
By allowing for the linear interpolation of labels similar to those in the original dataset, INFER meticulously optimizes the synthetic data and dramatically reduces the size of soft labels in the synthetic dataset to almost zero, establishing a new benchmark for efficiency and effectiveness in dataset distillation.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper first identifies two limitations of the current dataset distillation methods: inefficient utilization of the distillation budget and oversight of inter-class features. Based on this, this paper proposes to leverage a Universal Feature Compensator to enhance feature integration across classes.
Experiments demonstrate that the proposed INFER improves the storage efficiency and effectiveness of dataset distillation.

### Strengths
1. It analyses the limitations of the current optimization-based dataset distillation methods.
2. The proposed method can significantly reduce the storage.
3. The paper is well-written.

### Weaknesses
1. The authors claim that the existing dataset distillation methods focus on optimizing synthetic data exclusively for a pre-assigned one-hot label. However, RDED [1] introduces a non-optimization method that changes this paradigm. It is recommended that the authors analyze and compare their method with RDED.

2. In Table 1, lines 416-417, the authors claim that static labels perform better on small networks, while dynamic labels excel on large networks. However, in Table 2, static labels sometimes outperform dynamic labels on large networks and datasets, particularly when 
IPC=50 using ResNet-101. Why is this the case?

3. Additionally, in Table 4, the performance comparison between static and dynamic labels is inconsistent. Sometimes static labels are superior, other times dynamic labels are. What factors determine the choice between static and dynamic labels in real-world applications?

4. Analyzing computational cost is crucial in dataset distillation. It would be beneficial to compare both computation cost and peak memory usage against existing methods.

### Questions
1. The authors claim that the existing dataset distillation methods focus on optimizing synthetic data exclusively for a pre-assigned one-hot label. However, RDED [1] introduces a non-optimization method that changes this paradigm. It is recommended that the authors analyze and compare their method with RDED.

2. In Table 1, lines 416-417, the authors claim that static labels perform better on small networks, while dynamic labels excel on large networks. However, in Table 2, static labels sometimes outperform dynamic labels on large networks and datasets, particularly when 
IPC=50 using ResNet-101. Why is this the case?

3. Additionally, in Table 4, the performance comparison between static and dynamic labels is inconsistent. Sometimes static labels are superior, other times dynamic labels are. What factors determine the choice between static and dynamic labels in real-world applications?

4. Analyzing computational cost is crucial in dataset distillation. It would be beneficial to compare both computation cost and peak memory usage against existing methods. 

[1] Sun, Peng, et al. "On the diversity and realism of distilled dataset: An efficient dataset distillation paradigm." Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. 2024.

### Soundness
2

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
4

### Summary
In general, dataset distillation methods employ a class-specific synthesis paradigm, each synthetic instance has one label. This work suggests two limitations that these "one label per instance" approaches do not utilize the budget efficiently and fails to adequately reflect inter-class features. To overcome these limitations, this work introduces a new approach, Inter-class Feature Compensator (INFER), for “one instance for all classes” framework by utilizing Universal Feature Compensator (UFC). Experimental results show the effectiveness of the proposed framework.

### Strengths
1. This manuscript is well written and easy to follow along with their reasoning.
2. The idea of UFC is simple and easy to adapt.
3. The motivations of this work, inefficient budget utilization and oversight of inter-class features, are straightforward and novel. The proposed method aligns with these motivations.

### Weaknesses
1. The calculation of utilized budget of INFER is unclear. Some components in INFER seem to be consist of several vectors which have same size with original natural instance. However, in the manuscript, there is explicit description of utilized budget of INFER. Therefore, it is essential to clearly specify how the budget used by INFER is calculated and how it is set to ensure a fair comparison with prior studies.

2. There is insufficient baseline used for performance comparison. Although many dataset distillation methods are recently proposed to enhance the performance and budget efficiency, this work only compares INFER to some (possibly outdated) studies. Additionally, comparing INFER’s performance with recent methods raised doubts about its effectiveness. For example, DATM [1], which also address the feature redundancy as the manuscript said (Line 238-240), achieves higher performance than INFER in many settings: 47.2% (IPC=10), 57.5% (IPC=100) for CIFAR-100 and 31.1% (IPC=10). 39.7% (IPC=50) for Tiny-ImageNet.

3. One of the component in INFER, $P^k$, is consist of real instances. Storing real instances can be a drawback in tasks where privacy issues are crucial (e.g., continual learning). Continual learning is one of the primary applications of dataset distillation.

### Questions
1. How to calculate the utilized budget of INFER? According to Algorithm 1, it seems that $P^k$, $U^k$, and $Y^k$ are stored in budget after training. $P^k$ consists of instances equal to the number of classes $C$ (Line 263), and $U^k$ consists of $M$ instances (Line 269). Since there are a total of $K=\text{IPC}$ (Line 261) sets of $P^k$ and $U^k$, the total number of instances in $P$ and $U$ amounts to $\text{IPC} \times (C + M)$, which already exceeds the budget of $\text{IPC}×C$ used by conventional methods. If my understanding is incorrect, please clarify the budget utilized by INFER.

2. Is there a reason for learning $U^k$ independently for each $k$? Learning $U^k$ independently for each $k$ aims to capture the inter-class features of $P^k$. This approach seems to capture only local inter-class features, which may be suboptimal. Introducing a single $U$ could potentially be beneficial for obtaining global inter-class features. Are there experimental results using a single $U$?

3. In Algorithm 1, all $u_j \in U^k$ are initialized with zero vector and independently optimized with same ingredient. This suggests a risk that all instances of $u_j$ may converge to the same optimal value. I am curious about how different values of the optimized $u_j$ actually are. Additionally, I am interested in the rationale for initializing with a zero vector rather than a random noise vector, as well as the resulting performance when using the latter.

4. In general, data factorization methods generate more instance than IPC under same budget. Given this characteristic, feature duplication may present a greater limitation in data factorization methods. Does feature duplication occur in data factorization as well? If it does, is there an improvement in performance when combining INFER with data factorization methodologies?

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
4

### Summary
This paper presents a novel dataset distillation (DD) method, INFER (Inter-Class Feature Compensator), which explores the potential of leveraging inter-class features to significantly enhance distillation performance. In addition, it addresses a critical challenge faced by decoupled DD methods (e.g., SRe2L), where soft labels require nearly 30 times more storage than images. To overcome this limitation, the proposed method introduces a static labelling strategy that not only retains competitive performance but also dramatically reduces storage requirements, making it a more efficient and scalable solution.

### Strengths
a. The authors present an innovative analysis of existing class-specific dataset distillation methods. This work distinguishes itself from prior research by proposing the Universal Feature Compensator (UFC), which enhances inter-class feature integration, resulting in a more efficient dataset distillation framework. Relevant related works are appropriately cited. b. The submission is technically sound, with thorough evaluations and comparisons. c. The paper is clearly written and well-organized, making the content easy to follow and understand. d. This work addresses two key limitations of class-specific dataset distillation methods and achieves SOTA performance. Moreover, the proposed static labelling strategy reduces storage requirements by 99.3%.

### Weaknesses
 a. The compensator is denoted by $\mu$ in Fig. 2, but by $u$ in Fig. 3. Maintaining consistent notation across the figures would improve clarity and help avoid potential confusion.
b. Some results fall short of SOTA benchmarks, and it would be helpful if the authors provided a discussion of potential reasons for this discrepancy.
c. The current evaluation only focuses on same-architecture distillation performance for ConvNet and ResNet18 on CIFAR and tiny-ImageNet. A broader cross-architecture evaluation would offer better insights into generalization. 
d. While the static labelling approach effectively reduces storage requirements and, in some cases, even outperforms the dynamic method, the paper does not explore whether these benefits extend to other decoupled DD methods, such as SRe2L.
e. I have a question regarding the IPC used in the experiments, which refers to the number of images per class. If the authors apply the augmentation approach described in Equation 2, the final number of distilled images per class becomes IPC \times \left(1 + \frac{M}{{class number}}\right) . This seems to differ slightly from the IPC used in other comparison methods. While this difference might have minimal impact on large datasets with many classes, it could be more influential for smaller datasets. Have the authors accounted for this adjustment to ensure a fair comparison?

### Questions
e. I have a question regarding the IPC used in the experiments, which refers to the number of images per class. If the authors apply the augmentation approach described in Equation 2, the final number of distilled images per class becomes IPC \times \left(1 + \frac{M}{{class number}}\right) . This seems to differ slightly from the IPC used in other comparison methods. While this difference might have minimal impact on large datasets with many classes, it could be more influential for smaller datasets. Have the authors accounted for this adjustment to ensure a fair comparison?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The authors highlight that the “one label per instance” paradigm reduces intra-class diversity and amplifies inter-class differences within the distilled dataset. These limitations hinder the efficient use of the distillation budget and lead to poorly defined decision boundaries. To overcome these challenges, the authors propose a novel “one instance for all classes” approach, incorporating a Universal Feature Compensator (UFC). This method enhances class overlaps and ambiguities, improving representation quality and achieving state-of-the-art performance across a variety of datasets and architectures.

### Strengths
- The analysis of the two limitations in class-specific dataset distillation is insightful.
- The proposed Inter-class Feature Compensator is novel and improves the utilization of the distillation budget by leveraging inter-class features.
- To assess the size of the final distilled dataset, the authors introduce a compression ratio, in addition to the commonly used IPC metric, providing a fairer comparison with methods that utilize soft labels.
- The paper is well-written and well-structured.
- It offers extensive validation experiments across multiple datasets and architectures, reinforcing the reliability of the proposed approach.

### Weaknesses
 - [1] explores inter-class and inter-class relations in dataset distillation, introducing a class centralization constraint to tighten within-class clustering and improve class discrimination. While both methods report significant performance improvements, the conclusions appear to contrast with those of this paper. Could the authors elaborate on this discrepancy?
- [2] also employs multiple backbone architectures for dataset distillation. It would be helpful if the authors discuss how their approach aligns with or differs from this.
- Since the optimizable parameter is not the entire distillation budget but only the M compensators, will this speed up the distillation or synthesis phase?
- How did the authors accurately calculate the compression ratio in Table 2? Additionally, how did the author estimate the size of soft labels?
- Does the compensator consume the IPC budget in the experiments? If yes, according to the design of compensator, the IPC values should not be integers.
- Including comparisons with recent state-of-the-art dataset distillation methods extended from SRe2L [3, 4] would provide a more comprehensive evaluation.
- There are some typos; for example, in line 401, “Our INFER also employ the soft labels” should be corrected to “Our INFER also employs the soft labels.”

### Questions
please see the weakness part.

### Soundness
3

### Presentation
3

### Contribution
3
