# TOWARDS LAYER-WISE PERSONALIZED FEDERATED LEARNING: ADAPTIVE LAYER DISENTANGLEMENT VIA CONFLICTING GRADIENTS

- Decision: Reject
- Avg Score: 4.75
- Scores: 3, 5, 6, 5

## Abstract
In personalized Federated Learning (pFL), high data heterogeneity can cause significant gradient divergence across devices, adversely affecting the learning process. This divergence, especially when gradients from different users form an obtuse angle during aggregation, can negate progress, leading to severe weight and gradient update degradation. 
To address this issue, we introduce a new approach to pFL design, namely Federated Learning with Layer-wise Aggregation via Gradient Analysis (FedLAG), utilizing the concept of gradient conflict at the layer level.
{Specifically, when layer-wise gradients of different clients form acute angles, those gradients align in the same direction, enabling updates across different clients toward identifying client-invariant features. 
Conversely, when layer-wise gradient pairs make create obtuse angles, the layers tend to focus on client-specific tasks.
In hindsights, FedLAG assigns layers for personalization based on the extent of layer-wise gradient conflicts. Specifically, layers with gradient conflicts are excluded from the global aggregation process.}
The theoretical evaluation demonstrates that when integrated into other pFL baselines, FedLAG enhances pFL performance by a certain margin. Therefore, our proposed method achieves superior convergence behavior compared with other baselines. Extensive experiments show that our FedLAG outperforms several state-of-the-art methods and can be easily incorporated with many existing methods to further enhance performance.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper presents a layer disentanglement mechanism to achieve personalized federated learning. Specifically, the paper distinguishes between personal layers and global layers by examining the conflicts in local model gradients. Consequently, the model can adaptively separate the model parameters into personal and global components. Experimental evaluations demonstrate performance improvements compared to baseline models.

### Strengths
S1: This paper focuses on an important issue in the federated learning, i.e., build layer-wise personalized federated optimization framework to solve the data heterogeneity challenge.

S2: The idea is meaningful that the system can disentangle the personalized parameters by monitoring the gradient conflict.

S3: Experimental and theoretical analysis demonstrate the effectiveness of the proposed method.

### Weaknesses
W1: Compared with common layer-wise personalized federated learning framework, the proposed method has a higher communication overhead. Common layer-wise methods upload partial layers to the server for global aggregation and keep other parameters as personal component locally. However, the proposed method demands clients to upload full model parameters to the server for distinguishing gradient conflict, which increases the communication burden, especially with large models and numerous clients. This is a significant drawback compared to methods that selectively communicate only a subset of parameters.

W2: The proposed method incurs high computational costs due to the need to calculate the parameter correlations between any two users. Specifically, calculating the gradient conflict score, which involves comparing parameters across all clients, requires a pairwise comparison. This operation scales quadratically with the number of clients, making it computationally expensive for large-scale federated learning scenarios. The paper does not provide sufficient analysis on the computational complexity and scalability of this step.

W3: The presentation is poor and there are many confusing clarifications, please refer to section "Questions" for details.

### Questions
Q1: What is the meaning of vertical axis in Figure 2(a)?

Q2: Does the conclusion of Figure 2(b) contradict the textual interpretation in main text?

Q3: Is it necessary to re-compute the conflict layer in each computation round?

Q4: What is the purpose of the experiments in Section 7.2.5?

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper focuses on enhancing model performance in personalized federated learning (FL).  Recent pFL's methods usually face the problem of selecting which layers of the neural network to be personalized. To this end, the authors propose FedLAG to adaptively personalize layers whose gradients exhibit large conflicts across different clients.  Comprehensive theoretical and empirical results confirm the advantage of the proposed method in terms of accuracy.

### Strengths
**S1**. The authors provide a thorough theoretical analysis to show the strength of FedLAG in convergence and model performance.

**S2**.  Experimental results show that FedLAG outperforms baselines in terms of accuracy and convergence time, especially under high data heterogeneity and low user participation.

**S3**. The proposed method is simple bug effective and can be easily integrated into existing methods.

### Weaknesses
 **W1** . It is quite weird that the modern neural network ResNet9 can only achieve at most 97% testing accuracy on MNIST across all the methods and some results are even lower than 90% in Table 2 (e.g., PerAvg and FedPAC). A simple LeNet-5 model can already achieve 90% testing accuracy on MNIST by FedAvg even in the case of extremely non-i.i.d. partition (e.g., one label per client) [a]. In addition, the performance of FedAvg on MNIST-Dir(0.5) is lower than its performance on MNIST-Dir(0.1), which is also strange since a higher degree of data heterogeneity leads to a better performance for a non-personalized method. These factors make the experimental results less convincing. Please explain the potential reasons for these anomalous results. The use of pFLlib does not fully explain the low accuracy, as the framework itself should not inherently limit the achievable performance of a ResNet9 on MNIST. The discrepancy between the reported results and expected performance raises concerns about the experimental setup or potential implementation issues within the framework. The lack of a clear explanation for this discrepancy undermines the validity of the experimental comparisons.

**W2**. There may be some typo errors. For example, in the first line of Sec. 7.1.1, the α in the sentence "We assess at two heterogeneity levels, i.e., α = 0.1, 1."  is inconsistent with α 's values in Table 2.  In the Sec. 6.2, the method name GBFL (Zhang et al., 2023c) should be GPFL. Please correct these issues and check over the manuscript.

**W3** Some works related to leveraging gradient conflicts in FL [b][c][d] were missing. More discuss on how the approach relates to or differs from the gradient conflict handling methods is needed. One highly related baseline [e] similarly tackling the layer personalization problem in FL was also ignored. Please compare with this method in the experiments. While the authors claim that their method adaptively determines layers for personalization based on gradient conflicts, a comparison with [e], which uses a learning-based approach for layer selection, is crucial. The absence of this comparison makes it difficult to assess the true advantage of the proposed gradient-conflict-based approach over other layer-wise personalization mechanisms. The authors should also clarify how their method addresses the challenge of selecting layers for personalization, which is a key aspect of [e], and provide a rationale for why their approach is superior or complementary.

### Questions
Please see the weakness.

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
4

### Summary
This paper proposes a novel layer-wise personalized federated learning (PFL) method called FedLAG, which uses the divergence of client gradients as a criterion for selecting personalized layers. Experimental results demonstrate the effectiveness of this approach.

### Strengths
1. The paper is well-written, and the main claim is easy to understand.
2. Using gradient divergence as a criterion for selecting personalized layers seems reasonable.
3. Extensive experiments demonstrate the effectiveness of FedLAG.

### Weaknesses
1. Although gradient conflict is easy to understand, how gradient alignment specifically influences collaboration effectiveness in federated learning remains unclear. For instance, how large of an angle actually affects performance? Is an angle greater than 90 degrees necessarily detrimental? The paper primarily tunes the hyperparameter  \xi  to identify a threshold, but exploring the relationship between angle and performance further, along with providing a guideline for adjusting  \xi , would greatly enhance the quality of the work.
2. From the results in Tables 1 and 7, the performance improvement of FedLAG over the SOTA methods appears limited, with gains of less than 1%. Moreover, existing methods can already decouple the learning of personalized and generic knowledge in each parameter [1], I suggest that the authors compare FedLAG to this method.
3. As shown in Table 3, FedLAG appears highly sensitive to the hyperparameter  \xi . Combined with the results in Table 1, FedLAG requires very careful tuning of  \xi  to achieve performance superior to SOTA, which limits its usability.

### Questions
Section 3:

1. In Question 3.2, the authors state that “the density of conflicting gradients among clients does not progressively increase from the input layer to the output layer.” However, from Fig. 2(b), it appears that deeper layers have higher conflict scores. Could the authors clarify this discrepancy? I suggest that the authors provide a quantitative analysis of the trend in conflict scores across layers, rather than relying on a visual inspection of the figure.
2. In Section 4.1, why is FedLAG considered communication-efficient?

Section 7:

1. In 7.1.1, the authors mention “with improvements ranging from an average of 5–7% to 15%.” How was this calculated? From Table 1, it seems that FedLAG does not exceed the performance of the best method by more than 1% in most cases.
2. In 7.2.2, what would happen if  K  layers were randomly selected instead?
3. Which layers does FedLAG typically select for personalization?

### Soundness
3

### Presentation
3

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
This paper presents a novel layer-wise aggregation method for personalized federated learning, named FedLAG. By analyzing gradient conflicts, FedLAG dynamically determines which layers should undergo global aggregation (GAL) and which should be personalized (PL) to mitigate the negative impact of data heterogeneity on federated learning. FedLAG adapts to the personalized needs of the data, reducing the reliance on prior knowledge that traditional methods require, thereby enhancing model convergence and adaptability. Experimental results indicate that FedLAG outperforms existing baseline methods across multiple datasets.

### Strengths
1)Innovation: This paper addresses a key challenge in personalized federated learning, specifically, how to implement layer-wise model partitioning under data heterogeneity, and introduces an innovative method based on gradient conflict analysis.
2)Theoretical Rigor: The paper provides a theoretical analysis demonstrating the convergence advantages of FedLAG and includes mathematical proofs to validate the effectiveness of its gradient conflict-based layer separation.
3)Comprehensive Experimental Design: The experiments encompass various datasets of data heterogeneity, with results affirming FedLAG's strengths in both accuracy and convergence speed.

### Weaknesses
1)Gradient Conflict Concept Insufficiently Explained: Although the paper defines gradient conflict, it lacks examples or illustrations to show how gradient conflicts are detected and quantified in practice, especially in the context of layer separation. Specifically, the paper does not clarify how the cosine similarity between gradients is computed across different clients for a given layer, nor does it explain how this similarity measure translates into a practical conflict score. Furthermore, the choice of the gradient conflict threshold, as well as its impact on model performance, is not clearly explained. The paper merely describes conflict-based layer separation without providing an intuitive example. Supplementary examples or visual aids are recommended to enhance reader comprehension.

2)Inadequate Ablation Studies: While the paper compares the performance of fixed layers, it does not explain why certain layers are more suitable for personalization than others. This section lacks theoretical support or empirical evidence, rendering the rationale for layer selection ambiguous. For example, the paper does not explore whether layers closer to the input or output are more prone to gradient conflicts, or how the depth of a layer influences its suitability for personalization. Further experiments or analyses could substantiate the impact of layer choice on model performance, strengthening the logic behind model design.

3)Inaccurate Terminology: The paper states that “existing methods require extensive fine-tuning to determine which layers should be used for global aggregation and personalization” characterizing a limitation of existing methods. However, the term “fine-tuning” is inappropriate in this context. References [1] and [2] emphasize the role of prior knowledge in layer separation, and clarifying this terminology would help prevent potential misunderstandings.

4)Ambiguous Notation: Several notations in Section 2 are unclear, such as the definition of global communication rounds. This paper uses “each round” to describe this symbol, which may confuse readers regarding whether it refers to global communication rounds or local iteration rounds. Furthermore, in the “Layer Disentanglement” section, the complex and nested notation complicates the reader's understanding of the hierarchical structure. A clearer description of the relationships among symbols is recommended, along with a well-organized explanation of global and personalized layers. Visual aids, such as diagrams, could also serve as useful tools to help readers intuitively grasp the layered model structure.

5)Insufficient Discussion on Limitations and Future Directions: The paper does not discuss the limitations of the proposed approach or provide insights into future research directions in the conclusion. It is recommended to analyze the limitations, such as the uncertain performance on more complex types of heterogeneous data (e.g., feature distribution skewed datasets) or potential applications in NLP and time-series analysis. Future research directions could also include exploring the method on multi-type heterogeneous datasets to enhance generalizability.

6)Lack of In-depth Analysis of Experimental Results: Table 1 and Figures 6 and 7 demonstrate FedLAG's performance across various datasets, but the analysis of performance differences is not sufficiently in-depth. For instance, FedLAG's substantial improvement over other methods on CIFAR-10 and CIFAR-100 is not explained in terms of potential causes or contributing factors. A detailed analysis of these phenomena would increase the paper's credibility and persuasive power. For example, it would be beneficial to analyze if the performance gain is consistent across different levels of data heterogeneity or if specific types of heterogeneity benefit more from FedLAG.

7)Insufficient Validation of Gradient Conflict Distribution: Although a 2D toy dataset experiment was conducted in Section 3, there is insufficient evidence to demonstrate the consistency of gradient conflict distribution across different datasets. The paper does not provide any analysis on how the distribution of gradient conflicts varies across different layers or datasets, which is crucial for understanding the generalizability of the proposed method.

### Questions
See the weakness.

### Soundness
3

### Presentation
1

### Contribution
2
