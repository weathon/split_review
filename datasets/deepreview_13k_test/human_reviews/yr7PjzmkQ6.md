# On the utility of Equivariance and Symmetry Breaking in Deep learning architectures on point clouds

- Decision: Reject
- Scores: 5, 5, 6, 6

## Abstract
This paper explores the key factors that influence the performance of models working with point clouds, \edit{across different tasks of varying geometric complexity.} In this work, we explore the trade-offs between flexibility and weight-sharing introduced by equivariant layers, assessing when equivariance boosts or detracts from performance. It is often argued that providing more information as input improves a model's performance. However, if this additional information breaks certain properties, such as $SE(3)$ equivariance, does it remain beneficial?  We identify the key aspects of equivariant and non-equivariant architectures that drive success in different tasks by benchmarking them on segmentation, regression, and generation tasks across multiple datasets with increasing complexity. We observe a positive impact of equivariance, which becomes more pronounced with increasing task complexity, even when strict equivariance is not required.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This work investigates the utility of imposing equivariant constraints in models that perform point cloud processing. To study the effects of the application of different equivariant constraints, the authors propose a scalable architectural desing that allows for easily incorporating varying degrees of equivariance. They evaluate this architecture on different point cloud processing tasks, incorporating different levels of equivariance or symmetry-breaking factors that break the network's symmetry constraint. Experimental results are used to accept or reject a set of hypotheses regarding the effects of equivariant constraints on model performance and generalization. Specifically, this work analyzes the effects of equivariance when modifying the size of the model, the size of the dataset, the complexity of the task, or when allowing symmetry breaking by providing pose dependent information (that is not available in the typical equivariance case).

### Strengths
- This work provides a detailed description of the most commonly used equivariant architectures for point-cloud processing.
- Additionally, the clear definition of the hypotheses that the authors aim to investigate allows for the explicit design of experiments that can be used to test them, facilitating the reader's understanding of the conclusions drawn from the experimental observations.
- The extensive experimental evaluation across diverse point-cloud tasks provides convincing evidence of the effect of difference levels of equivariance on the proposed Rapidash model, showing the influence of the dataset size and task complexity on these effects.

### Weaknesses
- This work lacks sufficient attribution to prior work that has investigated hypotheses similar to the ones tested here. For example, hypothesis 5, on the effect of symmetry breaking in equivariant neural networks, has already been studied in prior works, such as :

	[1] Marc Finzi, Gregory Benton, Andrew Gordon Wilson "Residual Pathway Priors for Soft Equivariance Constraints"

	[2]  Mircea Petrache, Shubhendu Trivedi, "Approximation-Generalization Trade-offs under (Approximate) Group Equivariance"

	[3] Stefanos Pertigkiozoglou, Evangelos Chatzipantazis, Shubhendu Trivedi, Kostas Daniilidis , "Improving Equivariant Model Training via Constraint Relaxation"
- The experimental evaluation is limited to examining the effects of the equivariant constraints on a single architecture. While it is shown that these effects generalize across tasks it is not clear how they generalize across different model architectures. 
- In the experimental results, no error bars are provided. As a result, it is hard to assess the significance of the observations that are used to accept or reject the various hypotheses.

### Questions
- Providing a more detailed discussion on how the proposed hypotheses have also been investigated in prior works would improve the completeness of this work.
- Why is it reasonable to expect that the experimental observations generalize across different model architectures?
- Including error bars and variances of the reported numbers, given the randomness of the model's initialization and training, would allow for easier verification of the significance of the reported observations.

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
2

### Summary
Summary
This paper examines the role of equivariance and symmetry breaking in deep learning architectures for point clouds, focusing on the influence of additional input information and SE(3) equivariance on model performance. Through a series of experiments on various tasks and datasets (e.g., Shapenet 3D, QM9, and CMU Motion Capture), the authors compare the effects of equivariant and non-equivariant layers, exploring the advantages of equivariance as task complexity increases. Results show that equivariance offers significant benefits for small datasets and geometrically complex tasks, though this advantage diminishes in large-scale data regimes.

Strengths

Weaknesses

### Strengths
Novel Research Problem: The paper presents several hypotheses regarding the impact of equivariant vs. non-equivariant architectures, particularly on tasks of varying complexity. This is a novel and relevant problem, providing new insights into geometric deep learning for point cloud data.
Comprehensive Experimental Design: The authors conduct extensive experiments across multiple datasets, thoroughly evaluating the performance of different architectures, thus providing strong support for the effectiveness of equivariance.
Modular and Scalable Architecture: The proposed Rapidash architecture is extensible, supporting various forms of equivariance, and provides an efficient platform for testing, which is beneficial for future research.
Clear and Substantiated Conclusions: The experiments confirm the advantages of equivariance in geometrically complex tasks and quantify the impact on different data scales, offering practical guidance for model selection and design.

### Weaknesses
Limited Discussion on Symmetry Breaking: Although the paper addresses symmetry breaking by incorporating global coordinates, it lacks a detailed analysis of how this affects performance across different tasks. Additional theoretical insights or quantitative results would strengthen this discussion.
Insufficient Evaluation of Model Complexity and Computation Costs: While Rapidash shows promise for high-complexity tasks, the paper provides limited discussion on computational costs and scalability in practical applications, which may impact its usability for large-scale deployment.
Limited Benchmark Comparisons: While some baseline methods are included, the paper does not cover all recent benchmarks. Broader comparisons with state-of-the-art equivariant and non-equivariant methods would enhance the persuasiveness of the findings.
Lack of Practical Application Discussion: Although theoretically relevant, the paper does not discuss the potential impact of equivariance and symmetry breaking on real-world point cloud applications (e.g., 3D reconstruction or object detection), potentially limiting its practical value.

### Questions
see Weaknesses

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper explores the key properties of deep learning networks on 3D point clouds, especially focusing on SE(3) equivariance. It conduct extensive experiments to test the initial hypothesis of the trade-offs between flexibility and weight-sharing introduced by equivariant layers. Based on the experimental results, a scalable network called Rapidash is introduced to facilitate the comprehensive testing of the hypothesis.

### Strengths
1. Clear motivation and insightful key idea.   
2. The paper writing quality is very high, with explicit statements and clear logic links.   
3. The code is provided in the supplementary material.   
4. The analysis and theoretical conclusion may bring future insight to 3D point cloud learning.

### Weaknesses
1. The major concern lies in the dataset. ShapeNet is a synthetic dataset. However, one important key challenge of modern 3D point cloud networks is their real-world performance on real-world data. Thus, whether the raised hypothesis can also be accepted in real-world 3D data needs to be explored.   
2. Although this paper verified the three important hypotheses, a **solution** derived from hypotheses such as some network design ideas or even *engineering tricks/techniques* (e.g., how to revise the current point convolution operation) should be further discussed and evaluated based on the extensive analysis of the paper, which will benefit the network design of future point cloud learning methods.  
3. The reviewer believes that some extra figure illustrations should be provided to better intuitively understand the proposed theoretical hypotheses.

*Conclusion*:   
The current version of the paper is theoretically important, but need more pilot studies to provide the **practical** values.

### Questions
1. Some pilot studies (no need too much) should be conducted on real-world datasets, or at least some robustness point cloud datasets. For example, ScanObjectNN for point cloud classification, or ModelNet40-C for robustness point cloud recognition.
2. Some "solutions" should also be provided and evaluated (some pilot studies are enough).

If these two questions can be addressed well, the reviewer may consider raising the rating.

### Soundness
3

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
3

### Summary
This paper studies the impact of additional input information and SE(3)  equivariance on the performance of models processing point cloud data.  They present a series of hypotheses to  study different aspects of equivariant neural networks and symmetry breaking. Extensive experiments have been conducted on segmentation, regression, and generation tasks to verify the applicability and superiority of equivariant networks.

### Strengths
1. Detailed introduction to previous work.
2. The relationship between task complexity and equivariance was studied, and it was found that the equivariant method has more obvious advantages in tasks that require strict equivariance. It is demonstrated that providing explicit geometric information can improve performance even in the case of symmetry breaking.

### Weaknesses
1.There are so many contents from previous works that I can hardly tell the novelty. From my point of view, only Formulas 8 and 9 are new, but it is still quite easy to prove.

2.Although the paper proposes that symmetry breaking may be beneficial, it provides insufficient explanation of the mechanism behind it.

### Questions
None

### Soundness
2

### Presentation
3

### Contribution
2
