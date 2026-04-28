# MetaAdapter: Leveraging Meta-Learning for Expandable Representation in Few-Shot Class Incremental Learning

- Decision: Reject
- Avg Score: 5.40
- Scores: 6, 5, 6, 5, 5

## Abstract
Few-shot class incremental learning (FSCIL) aims to enable  models to learn new tasks from few labeled samples while retaining knowledge of previously ones. This  scenario typically involves an offline base session with sufficient data for pre-training, followed by online incremental sessions where new classes are learned from limited samples. Existing methods either rely on a frozen feature extractor or meta-testing simulation to address overfitting issues in online sessions. However, they primarily learn feature representations using only the base session data, which significantly compromises the model's plasticity in feature representations. To enhance plasticity and reduce overfitting, we propose the MetaAdapter framework, which makes use of meta-learning for expandable representation. During the base session, we expand the network with pre-trained weights by inserting parallel adapters and employ meta-learning to encode generalizable knowledge into these modules. Then, the backbone is further trained on abundant data from the base classes to acquire fundamental classification ability.  In each online session, the adapters are first initialized with parameters from meta-training, and subsequently tuned to adapt to the new classes. Leveraging  meta-learning to produce initial adapters, MetaAdapter enables the feature extractor to effectively adapt to few-shot new classes, thus improving the generalization  of the model.  Experimental results on the mini-ImageNet, CUB200, and CIFAR100 datasets demonstrate that our proposed framework achieves the state-of-the-art performance.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces MetaAdapter, a framework designed to address challenges in Few-Shot Class Incremental Learning (FSCIL). By employing meta-learning, MetaAdapter initializes adapters that encode general knowledge, aiming to balance stability and plasticity during incremental learning. The training process involves three phases: meta-training adapters, applying a feature compactness loss to reserve space for future classes, and utilizing knowledge distillation during incremental sessions. The framework demonstrates state-of-the-art performance on benchmarks such as mini-ImageNet, CIFAR100, and CUB200.

### Strengths
1. **State-of-the-Art Performance:** MetaAdapter achieves competitive results on multiple FSCIL benchmarks, indicating its effectiveness in adapting to new classes with limited data.

2. **Comprehensive Framework:** The integration of meta-learning with feature compactness and knowledge distillation offers a holistic approach to incremental learning challenges.

3. **Well-Structured Presentation:** The paper is organized and clearly articulates the methodology, facilitating understanding.

### Weaknesses
1. **Limited Novelty in Meta-Learning Approach:** The application of meta-learning for adapter initialization resembles existing methods. Clarification on how this approach differs from established frameworks would strengthen the contribution. Specifically, the paper does not clearly articulate how the meta-initialization of adapters differs fundamentally from existing meta-learning techniques used in few-shot learning, where meta-learning is often used to learn initialization parameters or adaptation strategies. The paper should highlight the specific aspects of their meta-learning approach that make it novel in the context of FSCIL, beyond simply using it for adapter initialization.

2. **Training Complexity:** The three-phase training process, including feature compactness loss and sharpness-aware minimization, adds complexity. This may pose challenges for implementation in resource-constrained environments. The introduction of a feature compactness loss and sharpness-aware minimization, while potentially beneficial, increases the computational overhead. The paper should provide a more detailed analysis of the computational cost associated with each phase, particularly the added cost of SAM, and how this impacts the overall training time and resource requirements. This analysis should include a comparison with other methods to contextualize the added complexity.

3. **Base Task Performance:** The framework appears to underperform in base classification tasks compared to other methods using the same backbone. Understanding the reasons for this discrepancy is crucial, as base task accuracy is vital for incremental learning stability. The paper needs to investigate why the base task performance is not as strong as other methods, even with the inclusion of SAM and a prototype-based classifier. A detailed ablation study should be conducted to understand the impact of each component (e.g., SAM, feature compactness loss, prototype classifier) on base task performance. The paper should also explore if the optimization for incremental learning is somehow detrimental to the base task performance, and if so, how this trade-off is managed.

4. **Typographical Errors:** Minor errors, such as “rataining” in Line 012 and “minImageNet” in Line 448, detract from the paper's professionalism. A thorough review to correct these is recommended.

5. **Limited Comparison with Recent Methods:** The paper compares MetaAdapter with only one method from 2024. Including a broader range of recent methods would provide a more comprehensive evaluation of its performance.

### Questions
Please refer to weakness

### Soundness
3

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
This paper proposes to use meta-adapter to address the few-shot class incremental learning problem. Additionally, a feature compactness loss is introduced to help the accommodation of new categories. By leveraging the generalization capabilities of meta-learning training methods, the proposed method enhances the performance of few-shot class incremental tasks.

### Strengths
1. The paper is well-written and easy to follow.
2. The figures in the paper are concise and clear.
3. The idea of feature compactness loss and adapter integration is impressive.
4. The ablation studies in Table 2 and Figure 4 are extensive.

### Weaknesses
1. Two highly related works are not compared [1,2], which have the same task setting.
2. Although the feature compactness loss (FCL) is impressive and shows good performance improvement, the analysis of FCL is insufficient:
    - Why don't more similar inter-class feature representations affect classification? Specifically, what is the trade-off between feature compactness and inter-class separability, and how does this affect the classification performance during both base and incremental learning phases?
    - Need further proof or experiment to demonstrate that more similar inter-class feature representations reserve embedding space. Additionally, will more similar inter-class feature representations possibly lead to the overall embedding space shrinking, similar to collapse in contrastive learning? It's crucial to understand if the FCL is truly reserving space or simply causing a contraction of the feature space that could be detrimental.
    - Need to prove that it is the reservation space that helps future tasks and not others. For example, reducing the number of novel categories in the few-shot adaptation task can also reserve space. Will this also improve performance? The paper needs to isolate the effect of space reservation from other potential factors that may influence performance.
    - The results using only FCL are missing in Table 2.
    - FCL is an interesting idea that I think needs further discussion.
3. It would be better to state how to expand $W_n^{t-1}$, Figure 2(b) only shows $W_n^{t}$. The description of how the weight matrix is expanded to accommodate new classes is unclear and requires more detail.
4. typo in L95: "using this knowledge to improve leanring efficiency"

### Questions
1. Please address the Weaknesses.
2. Since the ViT backbones are receiving more attention, I wonder if meta-adapter and FCL could be migrated to methods with ViT backbone?

### Soundness
2

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
This paper introduces a novel framework for few-shot class incremental learning (FSCIL) that addresses the challenges of plasticity and overfitting through meta-initialized adapters. The approach consists of three phases: meta-training adapters during the base session to obtain generalizable initial parameters, backbone pretraining with feature compactness loss to prevent feature space dispersion, and few-shot adaptation in incremental sessions where adapters are fine-tuned while preserving backbone knowledge. The framework demonstrates state-of-the-art performance across multiple benchmark datasets.

### Strengths
1. Novel architectural design that combines meta-learning with adapter modules in a way that enhances both plasticity and stability. 

2. Three-phase training strategy that systematically addresses key FSCIL challenges. The strategy integrates meta-learning for initialization, feature space management during pretraining, and adaptation during incremental sessions.

3. Thorough empirical validation across multiple benchmark datasets with ablation studies. The experimental results demonstrate consistent performance improvements across different scenarios and provide insights into the contribution of each component.

### Weaknesses
1. While the paper presents reproducible results across three datasets, some existing techniques implemented in the program are not mentioned in the manuscript. For example, the rotation technique utilized in the implementation appears to draw from previous work [1]. The authors should include all the implementation details in the paper and illustrate how these designs facilitate their method.

2. A more detailed discussion of the novelty in the existing techniques combination should be made (meta-learning [2], SAM [3], and feature compactness loss in FSCIL [4][5][6]...). The paper should elaborate on how the specific combination and adaptation of these techniques contribute to improved performance and reduced forgetting in the FSCIL context, for example, highlighting any unique modifications or interactions between these designs.

3. The benchmark comparisons should include detailed network architecture specifications for all compared methods. In addition, the model parameter size should also be listed since additional parameters are introduced in MetaAdapter. This additional information would facilitate a better understanding of the relative complexity and computational requirements across different approaches.

### Questions
Please refer to the weaknesses of the paper.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
Pointing out the heavy reliance on a feature extractor trained only on the base session, this paper leverages meta-learning to effectively adapt to new classes. Specifically, the proposed method first constructs a meta-learning scenario using the dataset from the base session and trains an adapter with Reptile, one of the meta-learning algorithms. Then, MetaAdapter trains a backbone network with a feature compactness loss to reserve feature space for future new classes. Finally, MetaAdapter updates the adapter using few-shot new-class data. The authors evaluate the proposed method on the CIFAR-100, miniImageNet, and CUB-200 datasets.

### Strengths
The authors address one of the key challenges in Few-Shot Class Incremental Learning (FSCIL): the lack of plasticity caused by the heavy reliance on the encoder trained during the base session. To overcome this, they propose leveraging a meta-learning approach and tackle several challenges that arise when applying meta-learning in the context of FSCIL.

### Weaknesses
1) Unclear descriptions of the proposed method.

The meaning of 'c_pseudo,' mentioned in lines L223-L224, is difficult to understand, and a formal definition would be helpful. Additionally, in Equation 4, the dimension of 'p_concat' is unclear. It appears that 'c_batch' has a shape of B x C x d, while 'p' has a shape of B x d, where B, C, and d represent the batch size, the number of base classes, and the feature dimension, respectively. If this is the case, concatenation would be impossible; if not, further clarification from the authors on the structure of 'p_concat' is necessary. Specifically, it is unclear how the prototypes for unseen classes, 'c_pseudo', are derived and incorporated into the loss calculation. The lack of clarity regarding the dimensions of the concatenated feature representation makes it difficult to assess the validity of the proposed approach. Furthermore, the paper does not explicitly state whether the prototypes are class-specific or instance-specific, which is crucial for understanding the loss function.

Furthermore, Section 3.5 is challenging to interpret. Figure 2 is particularly difficult to follow, especially in relation to the adapter’s structure. It seems that the adapter may share convolutional layers with the backbone model, as indicated by the gray and sky-blue colors. However, the gray coloring appears to make this unclear. Additionally, the number of channels between the adapter convolutional layer (shown in red) and the backbone convolutional layer (in sky-blue) seems to differ. Yet, in Equation 13, these two layers are simply added, which would not be feasible with different channel numbers. The paper lacks a clear explanation of how the adapter's output is integrated with the backbone's features, especially when the channel dimensions do not match. The description of the adapter architecture is vague, making it hard to understand the precise mechanism of few-shot adaptation. A more explicit explanation of the adapter architectures, including the specific kernel sizes and padding used, would be beneficial.

These issues make it challenging to understand the few-shot adaptation phase. A more explicit explanation of the adapter architectures would be beneficial.

2) Motivation of the feature compactness loss (FCL)

In L211-L215, the authors argue that traditional optimization during the base session results in a dispersed embedding space that does not accommodate future new classes. To address this, they propose Feature Compactness Loss (FCL), which compacts the feature space to reserve space for future new classes.
With similar motivation, many existing works on Few-Shot Class Incremental Learning (FSCIL) have aimed to maximize the margin between classes in the feature space. While FCL appears to share this motivation, it takes the opposite approach: rather than maximizing the margin, it reduces the overall feature space. To validate FCL, the authors should provide additional analysis to explain why compacting the feature space is more effective than maximizing class margins in preserving space for new classes. The paper does not provide a theoretical justification for why reducing the feature space would be more effective than maximizing inter-class separation. The lack of analysis makes it difficult to assess the validity of the proposed approach. The reviewer encourages the authors to refer to [3], which proposes reducing inter-class distance to improve representation learning in FSCIL and provides an analysis on its implications.

3) Fairness issue

In Appendix A, the authors state that they use ResNet-12 for both mini-Imagenet and CIFAR-100 experiments.
However, several existing methods like FACT and ALICE adopt ResNet-18 for miniImageNet experiments.
Thus, the comparison with these methods is unfair and may not demonstrate the effectiveness of the proposed method.

### Questions
Please refer to the weakness part.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper tackles the problem of Few-Shot Class Incremental Learning (FSCIL). The authors propose enhancing model plasticity during incremental learning stages by integrating and updating adapters within the backbone network. To simulate the testing scenario, the Reptile algorithm is employed to meta-learn the adapter, facilitating better initialization using data from the base session. Afterward, the adapters are frozen, and the backbone is fine-tuned on the base classes using a novel Feature Compactness Loss (FCL), complemented by a strategy to promote Flat Local Minima (FLM). The objectives of FCL and FLM are to reduce inter-class distances within the base classes, thereby preserving feature space capacity for future incremental classes. During incremental sessions, the adapters are updated and merged into the backbone through a running average. The approach demonstrates superior performance across three standard benchmarks.

### Strengths
1.	Enhancing model plasticity through the insertion of adapters while maintaining stability by freezing the backbone is a sound technical approach for FSCIL.
2.	Preserving feature space for future incremental classes is an effective strategy for improving overall performance.
3.	The proposed method demonstrates superior performance across three standard benchmarks.

### Weaknesses
Major:

1. The primary motivation of this paper is that previous methods do not update the learned representation during incremental sessions, thereby compromising model plasticity. However, the authors have not sufficiently explored related work in the field of continual learning. There is a considerable body of research that focuses on balancing model stability and plasticity during incremental sessions while also updating the backbone, not limited to FSCIL. The absence of a discussion on these relevant works is a notable gap. Even within FSCIL, prior works such as MetaFSCIL provide a relevant comparison. MetaFSCIL is a meta-learning-based method that not only learns meta-representations using base session data but also updates the backbone representation during incremental sessions. The meta-learning strategy employed in offline training mimics the meta-testing scenario while also balancing stability and plasticity as the backbone is updated. Conceptually, MetaFSCIL is closely aligned with the idea of meta-learning adapters proposed in this paper. However, the authors have misinterpreted MetaFSCIL’s approach in L60-63 and L113-115.
2. The concept of feature compactness loss, aimed at reducing excessive dispersion among base classes, is conceptually similar to the forward compatibility strategy introduced in FACT, which ensures sufficient feature space is reserved for future classes. However, the authors did not provide a discussion or comparison with FACT, despite the conceptual overlap. Including such a comparison would have strengthened the paper’s positioning and clarified its contributions relative to existing approaches.

3. The training sequence, where adapters are trained before fine-tuning the backbone, appears non-intuitive. In the first phase, the adapters are trained while the backbone remains frozen, causing the adapters to rely heavily on the backbone’s fixed knowledge. As a result, the adapters are meta-learned to operate on top of this frozen representation. However, in the second phase, the backbone undergoes fine-tuning, altering its parameters. This shift may create incompatibility between the previously trained adapters and the newly updated backbone, potentially undermining the synergy between the two components.


Minor:

1.	It is inaccurate to state “randomly initialize the adapter parameters for the j-th task,” as mentioned in L197-198. This phrasing implies that the adapters are randomly initialized for each task, which is misleading. In reality, the adapters should be updated iteratively using Eqs. (1) and (2) to build on previously learned knowledge rather than restarting with random parameters for every task.
2.	Eq. (4) appears somewhat unclear. If the goal is to bring feature vectors closer together, it would imply that Eq. (4) encourages a more uniform probability distribution. However, it is unclear how the information is concatenated into P_{\text{concat}} . What is the dimensionality of P_{\text{concat} ? If the concatenation occurs along the embedding dimension, the resulting output of the cosine similarity would be a scalar. Applying softmax to a scalar value does not seem meaningful, so additional clarification on the concatenation process is needed.
3.	The objective of the feature compactness loss and sharpness-aware minimization is to reduce the distances among base classes. However, it is unclear whether this operation could negatively impact the model’s performance on the base classes. If such degradation occurs, it is important to discuss how this issue could be mitigated to maintain performance on the base classes.

### Questions
1. How is the knowledge encoded in the adapters ensured to be task-agnostic, as claimed in L67? This concept is introduced in the paper’s introduction but is not elaborated upon in subsequent sections. A more detailed explanation is necessary to clarify how the adapters generalize across tasks without being biased toward specific ones.
2. How are pseudo-targets generated? The paper lacks details on the process used to obtain these pseudo-targets. Providing a clear description of the method for generating pseudo-targets is essential for understanding the approach and evaluating its effectiveness.

### Soundness
2

### Presentation
2

### Contribution
1
