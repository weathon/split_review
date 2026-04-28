# Data Attribution for Multitask Learning

- Decision: Reject
- Avg Score: 5.50
- Scores: 5, 6, 6, 5, 6, 5

## Abstract
Data attribution quantifies the influence of individual training data points on machine learning models, aiding in their interpretation and improvement. While prior work has primarily focused on single-task learning (STL), this work extends data attribution to multitask learning (MTL). Data attribution in MTL presents new opportunities for interpreting and improving MTL models while also introducing unique technical challenges. On the opportunity side, data attribution in MTL offers a natural way to efficiently measure task relatedness, a key factor that impacts the effectiveness of MTL. However, the shared and task-specific parameters in MTL models present challenges that require specialized data attribution methods. In this paper, we propose the **MultiTask Influence Function** (**MTIF**), a data attribution framework tailored for MTL. MTIF leverages the parameter structure of MTL models to derive influence functions that distinguish between within-task and cross-task influences. Our derivation also sheds light on the applicability of popular approximation techniques for influence function computation, such as EK-FAC and LiSSA, in the MTL setting. Compared to conventional task relatedness measurements, MTIF provides not only task-level relatedness but also data-level influence analysis. The latter enables fine-grained interpretations of task relatedness and facilitates a data selection strategy to effectively mitigate negative transfer in MTL. Extensive experiments on both linear and neural network models show that MTIF effectively approximates leave-one-out and leave-one-task-out effects while offering interpretable insights into task relatedness. Moreover, the data selection strategy enabled by MTIF consistently improves model performance in MTL. Our work establishes a novel connection between data attribution and MTL, offering an efficient and scalable solution for measuring task relatedness and enhancing MTL models.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper introduces a novel method called the MultiTask Influence Function (MTIF) for data attribution in multitask learning (MTL) settings, which extends data attribution from single-task learning to MTL, addressing both the opportunities and challenges that come with MTL.
﻿
1. **Novel Connection**: It establishes a new connection between data attribution and MTL, showing that data attribution can be used to efficiently measure task relatedness, a critical factor in MTL.
﻿
2. **MTIF Proposal**: The authors propose MTIF, a data attribution method designed for MTL. MTIF leverages the structure of MTL models to estimate the impact of removing data points or excluding tasks on the predictions of specific target tasks. It provides both data-level and task-level influence analysis.
﻿
3. **Efficiency and Scalability**: MTIF offers an efficient and scalable solution for data attribution in MTL by approximating leave-one-out and leave-one-task-out effects without the need for model retraining.
﻿
4. **Practical Usefulness**: MTIF can be used for practical applications such as data selection, which results in consistent performance improvements over baselines and helps mitigate negative transfer effects in MTL.
﻿
In summary, the paper presents an advancement in the field of multitask learning by introducing a method that enhances model interpretability and performance through efficient data attribution.

### Strengths
### Originality
﻿
1. **Innovative Approach to Data Attribution in MTL**: The paper introduces the MultiTask Influence Function (MTIF), which is a novel method for data attribution in multitask learning (MTL). This extends the application of data attribution beyond single-task learning, representing a creative advancement in the field.
   
2. **New Perspective on Task Relatedness**: By proposing a method to measure task relatedness in MTL, the paper offers a fresh metric for understanding task interactions, which is an original contribution to the understanding and optimization of MTL models.
﻿
### Quality
﻿
1. **Thorough Experimental Validation**: The paper provides a rigorous experimental framework, testing MTIF on both linear and neural network models, which speaks to the high quality of the research and its findings.
﻿
### Clarity
﻿
1. **Clear Problem Formulation**: The paper clearly defines the problem of data attribution in MTL, making it accessible to readers who may not be experts in the field.
﻿
2. **Detailed Methodological Explanation**: The step-by-step explanation of the MTIF methodology, including the mathematical derivations, enhances the clarity and understandability of the paper.

### Weaknesses
### Specificity in Application Domains

1. **Limited Domain Diversity**: The paper primarily focuses on synthetic and neural network models. While this provides a solid foundation, expanding the experiments to include a broader range of real-world datasets and application domains could strengthen the claims of generalizability. Specifically, the current evaluation lacks diversity in data modalities and task types. For example, the inclusion of datasets from areas such as natural language processing, time-series analysis, or computer vision beyond basic image classification would provide a more comprehensive assessment of the method's applicability. The reliance on synthetic data, while useful for controlled experiments, does not fully capture the complexities and nuances of real-world scenarios, potentially limiting the practical impact of the findings.

### Depth of Negative Transfer Analysis

2. **Analysis of Negative Transfer**: While the paper mentions the mitigation of negative transfer, a more in-depth analysis of how MTIF specifically addresses and quantifies negative transfer effects could be beneficial. The current analysis does not provide a clear understanding of the mechanisms through which MTIF identifies and mitigates negative transfer. A more detailed investigation into the types of negative transfer scenarios that MTIF is effective against, and those where it might struggle, would be valuable. Furthermore, the paper should include a more granular analysis of how the influence scores correlate with the actual performance changes observed when negative transfer is mitigated.

### Comparative Analysis

3. **Lack of Comparative Analysis with Other Attribution Methods**: The paper could benefit from a comparative analysis with other existing data attribution methods in MTL to better highlight the advantages and potential limitations of MTIF. The absence of a direct comparison with other attribution techniques makes it difficult to assess the relative performance and novelty of MTIF. A comparison with methods adapted from single-task learning or other related techniques would help to establish the unique contributions of MTIF and clarify its position within the existing landscape of data attribution methods. This comparison should include both quantitative and qualitative aspects, highlighting the strengths and weaknesses of MTIF relative to other approaches.

### Robustness and Generalization

4. **Robustness Across Different Model Architectures**: More extensive testing of MTIF across different model architectures and complexities could provide a clearer picture of its robustness and generalization capabilities. The current evaluation does not explore the sensitivity of MTIF to variations in model architecture. Testing MTIF with a wider range of architectures, including both shallow and deep models, and different types of layers (e.g., convolutional, recurrent, transformer), would provide a more robust understanding of its generalization capabilities. This analysis should also consider the computational cost associated with applying MTIF to different model architectures.

### Questions
1. Given that the paper primarily focuses on synthetic and neural network models, how might the findings differ if a broader range of real-world datasets and diverse application domains were included in the experiments? What steps could be taken to test the generalizability of the results in these different contexts?
﻿
2. The paper touches on the mitigation of negative transfer but lacks an in-depth analysis of MTIF's effectiveness in this regard. What specific methodologies or metrics could be employed to better quantify and analyze the negative transfer effects mitigated by MTIF? How would such an analysis strengthen the overall claims of the paper?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes the MultiTask Influence Function (MTIF) by extending data attribution techniques for single-task learning (STL) to the context of multitask learning (MTL). The authors identify new challenges in data attribution in MTL which stems from task interdependencies and the need to balance shared and task-specific parameters. The proposed MTIF method approximates the impact of individual data points or entire tasks on other tasks’ performance, enabling both data-level and task-level influence analysis without the need for retraining. The authors validate MTIF’s effectiveness in approximating data-level and task-level influences through experiments on linear models and shallow neural networks, by demonstrating positive correlations with an oracle influence estimation from extensive computations.

### Strengths
**An important extension of data attribution problem and method for STL to the context of MTL:** A key contribution of this work is its formulation of data attribution specifically for MTL, highlighting the need to quantify data influence not just within tasks, but across multiple related tasks that share parameters. 

**Clear presentation and justification of the proposed method:** The authors describe MTIF’s construction and rationale with clarity, particularly regarding its approach to handling shared and task-specific parameters in MTL. By leveraging the influence function (IF) approach, which uses first-order approximations to model parameter changes, MTIF mitigates the computational burden of retraining, which is commonly associated with data attribution methods.

**Preliminary yet convincing experimental results:** The experiments clearly demonstrate MTIF’s ability to approximate leave-one-out (LOO) and leave-one-task-out (LOTO) influences and to be employed in the downstream task after estimating data influences, although the setups are simplistic.

### Weaknesses
 **No computational complexity analysis:** Although the major challenge of data attribution in MTL is computational complexity, the paper lacks explicit theoretical or empirical analysis of MTIF’s computational complexity. Given that influence functions and Hessian computations are generally costly, a complexity analysis would have been useful in understanding the method’s scalability, particularly for large-scale MTL applications.

**High computational cost of calculation of Hessian:** Despite MTIF’s efficiency improvements, Hessian computations remain costly, which could hinder the method’s application to high-dimensional models or a large number of tasks. The paper could benefit from discussing any further optimizations or Hessian approximations to address this issue.

**Limited experimental scope:** The experiments are conducted on simple models, including linear models and shallow neural networks, which may not fully showcase MTIF’s potential in realistic MTL scenarios. Evaluation on more sophisticated architectures, such as deep neural networks or transformer-based models, and larger datasets would provide a more comprehensive assessment.

**Lack of comparison with existing baselines:** The paper does not compare MTIF to simple methods for estimating task relatedness, such as cosine similarity of gradients, which are often used in MTL, although they are tailored for only estimating task-level influences. Additionally, incorporating heuristics based on gradient similarity could serve as promising baselines even for data-level influences, e.g., cosine similarity between the gradient of an individual data point and the average gradient.

### Questions
Please address the aformentioned weaknesses.

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
4

### Summary
This paper focuses on data-attribution and task-attribution in multitask learning. The authors propose a novel multitask influence function that efficiently estimates the impact of removing data points or excluding tasks on specific target task predictions, offering interpretable data-level and task-level influence analysis.

### Strengths
- This paper targets a meaningful problem in machine learning. In practice, interpretable data-level and task-level influence analysis is crucial in multitask learning.

- The motivation is stated clearly. The authors argue that re-training-based data attribution methods greatly increase computation cost, and that existing IF-based methods in single-task learning face computational challenges from complex optimization objectives. To address these issues, the authors propose a multitask influence function (MTIF).
- The experiments on multiple benchmark datasets validate the effectiveness of the proposed method compared with the baseline models.

### Weaknesses
 - **The key differences between single-task IF and the proposed multitask IF should be clarified.** According to my understanding,  it seems the authors apply the idea of the IF-function (Koh & Liang, 2017) to multitask learning, handling more complex differential operations.

- **More empirical results are necessary.** On one hand, since the authors claim that the proposed method can enhance computational efficiency in the motivation, the efficacy analysis (such as memory usage, training/inference time, flops) also is crucial.  On the other hand, it is not convincing that the authors just select re-weighting-based method as competitors. The empirical results of directly transferring IF-based methods in STL to MTL need further analysis.

-  In the related work, the authors overlook several work [1,2,3] on addressing the ”negative transfer“ issue in multi-task learning.
- The authors should provide citations for each method in Tab. 3.

### Questions
Please see the above weakness.

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
4

### Summary
This paper proposes the MultiTask Influence Function (MTIF), a novel data attribution method for multitask learning (MTL). By extending influence function-based approaches to MTL, the authors aim to quantify data and task importance within MTL frameworks, offering insights into task relatedness and the impact of individual data points on model performance. The method shows promise in improving model efficiency and interpretability within MTL.

### Strengths
1. This paper introduces data attribution to the field of multitask learning (MTL) for the first time, analyzing data importance across multiple levels. This is a meaningful contribution, as understanding the significance of individual data points in MTL could greatly enhance the interpretability and performance of MTL models. The proposed work provides an efficient approach to quantify task relatedness, which is essential in MTL since task interactions often drive overall performance improvements.

2. The authors effectively extend the influence function (IF) to MTL through the proposed MultiTask Influence Function (MTIF), enabling both data-level and task-level attribution analysis. By circumventing the computational expense of retraining models, MTIF approximates leave-one-out (LOO) and leave-one-task-out (LOTO) effects, demonstrating efficient computational performance with strong interpretability, as supported by the experimental results.

### Weaknesses
1. Many conclusions in this paper are based on the assumptions in Equation 1; however, a detailed derivation for this equation is missing. This absence may impact readers’ confidence in the method’s validity. Specifically, the paper should clarify the assumptions under which the influence function can be extended to the multitask setting, and whether these assumptions hold in practical MTL scenarios. A rigorous derivation would help readers understand the limitations of the method and its applicability to different types of MTL problems.

2. The derivation of Equation 6 relies on partial derivatives with respect to \(\sigma\), which, in turn, depend on the local properties of the parameter \(\theta\). These local properties may change across different training stages, and the importance of specific samples and tasks may shift as training progresses. For example, while derivatives may tend toward zero after convergence, this is not necessarily the case in earlier training stages. The paper should discuss how the method accounts for the dynamic nature of the loss landscape during training, and how the influence scores are interpreted when the derivatives are not stable. It is crucial to understand how the method’s estimates of influence evolve over the course of training, and whether the method can be used to identify samples and tasks that are important at different stages of the learning process.

3. The paper does not sufficiently detail the sample selection process (e.g., whether samples are chosen randomly or deterministically), which may lead to a significant influence from randomness. Providing more detailed descriptions of the experimental setup, including criteria for selecting tasks and samples and data partitioning methods, would enhance the reproducibility and reliability of the results. For example, the paper should specify whether the same samples are used across different experiments, and how the selection of samples might affect the observed influence scores. The paper should also discuss the potential for bias in the sample selection process and how this bias might affect the conclusions.

4. The experiments predominantly use simpler datasets, with much of the analysis focusing on cases of local properties (e.g., \(\sigma=1\) or \(0\)). For more complex datasets, substantial variations between discrete values may emerge, potentially challenging the evaluation methods used. The paper should provide a more comprehensive evaluation of the method on complex datasets, and discuss the limitations of the method when applied to high-dimensional data and complex task relationships. It is important to understand how the method scales with the number of tasks and the complexity of the data, and whether the method can be used to analyze real-world MTL problems.

### Questions
See Weakness

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors extend influence functions to the multitask learning setting. Due to the fact that there are multiple sets of task-specific parameters, if done naively the Hessian of the loss with respect to the full set of parameters would be very large and thus difficult to invert. The authors circumvent this issue by using the block structure of the Hessian. On both synthetic and real datasets, the influence function values correlate strongly with the difference in validation loss attained by leave-one-out retraining. Moreover, removing the most problematic examples and retraining yields consistent performance improvements on the CelebA dataset.

### Strengths
* The work is well-motivated and tackles the important problem of data attribution in multitask learning.
* The novelty is significant, since influence functions have not yet been extended to this setting.
* The empirical side of the work is strong, since the task-level influence is correlated to the LOTO effect across three datasets.
* The authors take it a step further and demonstrate a concrete benefit of their work; performance on CelebA improves across the majority of tasks by removing the most problematic examples as measured by the task-level influence.

### Weaknesses
 * There is no baseline to compare against in the results in Table 1 and 2, which makes the numbers difficult to interpret. I.e. is 21% correlation high or low? I understand that this is a new approach and there may not be existing methods to compare against. However there should be at least some kind of (perhaps trivial) baseline to compare against.


### Questions
* Include some kind of baseline for the correlation between task-level influence and LOTO effect.
* Can you report the data selection results (Table 3) on the synthetic and human action recognition datasets as well? It would be good to see that this yields consistent improves across multiple datasets, not just one.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 6

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper extends traditional data attribution techniques from single-task learning to multi-task learning (MTL), addressing the interference caused by cross-task parameter sharing on sample gradients. By analyzing task relatedness, the paper introduces a novel approach to data-level analysis, offering a novel perspective for enhancing MTL.

### Strengths
1. The paper provides a novel perspective for modeling task relatedness in multi-task learning by investigating the influence of individual samples on other tasks. This fine-grained analysis helps elucidate the interference caused by cross-task sharing.

2. The data selection method, realized through data-level influence analysis in Section 5.2.2, presents a unique and valuable application for MTL, distinguishing this work from existing approaches.

### Weaknesses
 1. The main contribution of the paper lies in applying influence functions to MTL in the form of Leave-One-Out (LOO) and Leave-One-Task-Out (LOTO) analyses, a conceptually straightforward extension. The key distinction from single-task learning is the influence of the task-sharing quantity $\Omega_k$ in Eq. 5. However, under the assumption of a convex combination of tasks, this influence is relatively easy to analyze and does not provide a particularly challenging technical novelty. The adaptation of single-task influence functions to the multi-task setting, while practically useful, lacks significant theoretical depth. The core idea of using the Hessian to measure influence is well-established, and the extension to MTL, while requiring some algebraic manipulation, does not introduce fundamentally new concepts in optimization or statistical learning theory. The paper does not adequately address the computational challenges associated with calculating the Hessian in high-dimensional MTL models, which is a significant practical concern.

 2. The work lacks direct baselines, resulting in insufficient comparison. For instance, in Tables 1 and 2, the experiments are only compared with the ground truth LOTO scores, making it difficult to assess the performance of the method quantitatively. This is especially concerning given the unsatisfactory correlation coefficient results in Table 2. The absence of comparisons with other data attribution methods, even those adapted from single-task learning, makes it difficult to assess the relative merits of the proposed approach. Without these comparisons, it is unclear whether the proposed method offers any advantage over existing techniques or if it simply replicates known results in a multi-task setting. The correlation results, particularly on the CelebA dataset, are quite low, raising questions about the reliability of the method in more complex scenarios.

 3. While this may be a somewhat harsh critique, it is worth noting that traditional MTL methods are rapidly being supplanted by more advanced models. Recent work in MTL since 2022 increasingly leverages cutting-edge techniques such as multi-modal models (e.g., CLIP) or fine-tuning large language models (LLMs) via LoRA (both included in the Related Work section). In contrast, the experimental setup and models employed here appear overly simplistic, serving more as illustrative case studies than as a demonstration of broader applicability or superiority in real-world scenarios. The use of linear models and relatively shallow neural networks in the experiments does not reflect the current state of the art in MTL, where deep, complex architectures are more common. This raises concerns about the practical relevance of the findings and limits the impact of the paper.

### Questions
1. Would it be feasible to adapt existing single-task attribution algorithms to provide additional baselines for the experiments presented in Sections 5.1.2 and 5.2.1? This would improve the rigor of the empirical evaluation and provide more meaningful comparisons.

2. In Section 5.2.2, the authors report significant improvements in MTL performance by removing certain negative samples. However, is this approach entirely justified? Many recent MTL methods address conflicting gradients by adjusting only the conflicting components (e.g., gradient surgery and its variants), preserving parts of the conflicting samples that are beneficial to their respective tasks. Could the proposed algorithm be extended to provide insights or improvements to these gradient-based optimization techniques?

### Soundness
2

### Presentation
4

### Contribution
3
