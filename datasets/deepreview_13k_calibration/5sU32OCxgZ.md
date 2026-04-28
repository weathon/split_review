# TTVD: Towards a Geometric Framework for Test-Time Adaptation Based on Voronoi Diagram

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 6

## Abstract
Deep learning models often struggle with generalization when deploying on real-world data, due to the common distributional shift to the training data. Test-time adaptation (TTA) is an emerging scheme used at inference time to address this issue. In TTA, models are adapted online at the same time when making predictions to test data. Neighbor-based approaches have gained attention recently, where prototype embeddings provide location information to alleviate the feature shift between training and testing data. However, due to their inherit limitation of simplicity, they often struggle to learn useful patterns and encounter performance degradation. To confront this challenge, we study the TTA problem from a geometric point of view. We first reveal that the underlying structure of neighbor-based methods aligns with the Voronoi Diagram, a classical computational geometry model for space partitioning. Building on this observation, we propose the Test-Time adjustment by Voronoi Diagram guidance (TTVD), a novel framework that leverages the benefits of this geometric property. Specifically, we explore two key structures: 1) Cluster-induced Voronoi Diagram (CIVD): This integrates the joint contribution of self-supervision and entropy-based methods to provide richer information. 2) Power Diagram (PD): A generalized version of the Voronoi Diagram that refines partitions by assigning weights to each Voronoi cell. Our experiments under rigid, peer-reviewed settings on CIFAR-10-C, CIFAR-100-C, ImageNet-C, and ImageNet-R shows that TTVD achieves remarkable improvements compared to state-of-the-art methods. Moreover, extensive experimental results also explore the effects of batch size and class imbalance, which are two scenarios commonly encountered in real-world applications. These analyses further validate the robustness and adaptability of our proposed framework.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper introduces a novel Test-Time Adaptation (TTA) method using Voronoi Diagrams, termed TTVD. The manuscript highlights the integration of cluster-induced Voronoi Diagrams with Power Diagrams, marking their inaugural application in the TTA domain. This combination aims to ensure both flexibility and robustness within the method. Based on the experiments presented, TTVD demonstrates a clear reduction in errors, which is commendable. The writing is clear, the methodology sound, and the experimental outcomes show significant improvement. However, the manuscript does raise concerns about its level of innovation, primarily since it builds upon pre-existing methodologies without introducing novel concepts.

### Strengths
1. The proposed TTVD method is presented as both simple and rational, making it easily understandable.
2. The experimental performance of the TTVD method is impressive and showcases the method’s efficacy.

### Weaknesses
1. The main innovation of TTVD appears to be the combination of existing methods (Cluster-induced Voronoi Diagram and Power Diagram), which might not sufficiently fulfill the criteria for substantial novelty. The application of Voronoi diagrams, while novel in the context of TTA, leverages well-established geometric constructs. The core contribution seems to be in the specific combination and application rather than the introduction of fundamentally new theoretical concepts or algorithms. This raises concerns about the depth of the contribution to the broader field of machine learning.
2. The manuscript lacks a comprehensive discussion and validation of parameter settings, such as \gamma, \eps, and \tau, which are crucial for the reproducibility and understanding of the research. The absence of a sensitivity analysis for these parameters makes it difficult to assess the robustness of the method. The choice of \gamma, in particular, seems arbitrary without a clear justification of its impact on the Voronoi diagram's influence function. Similarly, the role of \eps in the log function needs more rigorous explanation beyond simply avoiding log(0) errors, as this could be addressed in other ways. The lack of detailed exploration of these parameter choices limits the practical applicability and reproducibility of the method.
3. The comparative analysis primarily focuses on methods proposed up to and including 2023. Given the rapid advancements in the field, incorporating more recent methodologies (from 2024) could provide a more current understanding of TTVD's positioning. The field of test-time adaptation is rapidly evolving, and the absence of comparisons with state-of-the-art methods from the current year limits the assessment of the proposed method's competitive edge.

### Questions
1. The parameter gamma seems to be a critical aspect of TTVD; however, its determination and impact on algorithm performance are not thoroughly discussed in the manuscript. Could you provide a detailed explanation on how gamma values are selected and their influence on the method's efficacy?
2. Regarding the introduction of parameter eps in equation (3) to avoid the log0 issue, the justification seems unclear. The rationale that including eps prevents log0 errors in equation (3) is not compelling, as the log0 problem might not arise even without eps. Could you elaborate on the necessity of eps in this context?
3. The manuscript assumes the Voronoi sites are pre-determined without detailing the process of converting Xtest into Voronoi sites. For clarity and completeness, please provide a comprehensive description of how Xtest data are transformed into Voronoi sites.

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper uses a combination of different variants of Voronoi Diagrams in test-time adaptation. The proposed method combines original Voronoi Diagram, Cluster-induced Voronoi Diagram, and Power Diagram. The proposed method outperforms a collection of relevant baselines under 4 benchmarking datasets.

### Strengths
- The proposed method is novel, seems to be the first working applying Voronoi Diagram in test-time adaptation, although there are works (e.g. T3A, AdaNPC) share similar intuitions. 
- The author choose very appropriate baselines: all of them are highly relevant and shares similarities to the proposed method. The proposed method has strong performance.

### Weaknesses
 - The algorithm part seems unfinished and lacks many details. For example, the paper only include how to compute the soft prediction $\hat{y}$ for VD, but not for CIVD and PD. Also, it is not introduced how these three components are combined and whether there are additional hyper parameters or flexibilities. 
- It seems like this paper changes the way of doing inference (from simple linear layer to a combination of three types of Voronoi Diagrams). However, the TTA process is still just entropy minimization, like a simpler version of SHOT. Given this similarity, it is highly unsure why the proposed method can solve the challenges in introduction, and how. 
- [Minor] The format of references may need to be updated. There are many places where the author use \cite, while it should be \citep. Please correct it in the next version.

### Questions
- For the Voronoi Diagram method in Section 3.1, Is it true that the Voronoi sites won’t be updated once initialized? Since in Algorithm 1, it is not adapted. 
- How to get the soft prediction based on $F$ in formula (4) and (6)? How three diagrams are combined? 
- What is the purpose of Lemma 3.1? Is it how the $v_k$s are initialized?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper targets the challenge of test-time adaptation (TTA) in deep learning models. The authors propose a framework, TTVD (Test-Time adjustment by Voronoi Diagram guidance), which leverages the geometric properties of Voronoi Diagrams to adapt models online during inference. The paper introduces two key geometric structures: Cluster-induced Voronoi Diagram (CIVD) and Power Diagram (PD), to enhance the robustness and adaptability of models facing distributional shifts. Extensive experiments on benchmark datasets like CIFAR-10-C, CIFAR-100-C, ImageNet-C, and ImageNet-R demonstrate the effectiveness of TTVD against state-of-the-art methods.

### Strengths
1. The paper offers a fresh perspective on TTA by employing Voronoi Diagrams, which is a significant departure from traditional approaches and shows promise in handling distributional shifts.
2. The authors provide a rigorous experimental evaluation, demonstrating TTVD's superiority over existing methods on multiple benchmark datasets, which strengthens the credibility of their approach.
3. Leveraging Voronoi Diagrams for TTA enhances model interpretability, allowing for clearer visualizations and understanding of partition boundaries, which is a valuable asset in deep learning.

### Weaknesses
1. While the paper discusses the benefits of TTVD, it lacks a detailed discussion on the computational overhead introduced by the geometric structures, which could be a concern for real-time applications.
2. While experimental results are promising, it would be valuable to see a comparison with theoretical bounds or guarantees, if available, to understand the limits of TTVD.
3. Some sections, particularly the methodology, could benefit from more detailed explanations or pseudo-code to aid reproducibility.
4. The performance of geometric structures like CIVD and PD may be sensitive to hyperparameters. The paper could provide more insights into hyperparameter tuning and the robustness of these parameters.

### Questions
See weaknesses.

### Soundness
2

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
3

### Summary
This paper presents the Test-Time adjustment by Voronoi Diagram (TTVD) framework by leveraging geometric principles, particularly the Voronoi Diagram (VD) and its extensions: the Cluster-induced Voronoi Diagram (CIVD) and the Power Diagram (PD). TTVD addresses the limitations of current test-time methods by using these geometric structures to improve feature alignment and sample filtering. CIVD enhances robustness by considering clusters rather than individual prototypes, while PD allows flexible boundaries to better handle noisy samples near decision boundaries. The proposed TTVD demonstrates substantial improvements over state-of-the-art TTA methods on several corrupted datasets, showing its effectiveness in real-world distribution shift scenarios.

### Strengths
- By introducing geometric frameworks like VD, CIVD, and PD, TTVD leverages computational geometry to improve the alignment of test-time features with training distributions. This approach provides a mathematically grounded and visually interpretable solution to feature adaptation in TTA.
- TTVD shows consistent improvements over existing methods across multiple datasets, reducing classification error rates and enhancing model calibration as indicated by lower Expected Calibration Error (ECE) scores. The inclusion of diverse corruption types in the evaluation (e.g., noise, blur, and weather-based distortions) demonstrates the framework’s adaptability to real-world conditions.

### Weaknesses
 - Both CIVD and PD are well-established geometric structures, raising questions about the novelty of TTVD’s core contributions. The first two contributions mainly apply these established methods to the TTA setting, which may limit the originality of the approach.
- The distinction between “test-time training” (TTT) and “test-time adaptation” (TTA) is somewhat blurred. According to the TENT framework, TTA excludes access to source data, while TTT can include self-supervised losses on source data. TTVD’s reliance on pre-computed Voronoi sites calculated during pre-training suggests it should be categorized as TTT rather than TTA. This distinction impacts baseline comparisons, as the current baselines primarily include TTA methods, potentially leading to an unfair performance comparison.
- The paper claims that TTVD extends VD from a point-to-point structure to a cluster-to-point influence mechanism, but it’s unclear why distances in standard VD (calculated by $\mu_k$) would not already reflect cluster-to-point relationships. A clearer explanation of this transition’s significance would be beneficial.
- The method lacks details on integrating VD, CIVD, and PD into a single loss function. Questions remain regarding whether the label y is generated by substituting $d(\cdot)$ in Equation 3 with $F(\cdot)$, how the components are balanced, and whether this balance is sensitive to different datasets.
- The paper lacks computational details on estimating key parameters ($\mu, C, and~ v$) in the TTVD framework. More clarity on these calculations would enhance understanding of the implementation and reproducibility of TTVD.

### Questions
The reviewer may have limited familiarity with the Voronoi Diagram, which could have led to some misunderstandings. The authors are encouraged to provide additional explanations during the rebuttal to clarify above points, especially the contributions of the paper and the assumptions between TTT and TTA.

### Soundness
3

### Presentation
3

### Contribution
2
