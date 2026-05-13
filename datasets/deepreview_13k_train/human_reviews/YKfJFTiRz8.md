# Pre-Training Graph Contrastive Masked Autoencoders are Strong Distillers for EEG

- Decision: Reject
- Scores: 6, 5, 3, 8, 3, 5

## Abstract
Effectively utilizing extensive unlabeled high-density EEG data to improve performance in scenarios with limited labeled low-density EEG data presents a significant challenge. In this paper, we address this by framing it as a graph transfer learning and knowledge distillation problem. We propose a Unified Pre-trained Graph Contrastive Masked Autoencoder Distiller, named EEG-DisGCMAE, to bridge the gap between unlabeled/labeled and high/low-density EEG data.
To fully leverage the abundant unlabeled EEG data, we introduce a novel unified graph self-supervised pre-training paradigm, which seamlessly integrates Graph Contrastive Pre-training and Graph Masked Autoencoder Pre-training. This approach synergistically combines contrastive and generative pre-training techniques by reconstructing contrastive samples and contrasting the reconstructions.
For knowledge distillation from high-density to low-density EEG data, we propose a Graph Topology Distillation loss function, allowing a lightweight student model trained on low-density data to learn from a teacher model trained on high-density data, effectively handling missing electrodes through contrastive distillation.
To integrate transfer learning and distillation, we jointly pre-train the teacher and student models by contrasting their queries and keys during pre-training, enabling robust distillers for downstream tasks.
We demonstrate the effectiveness of our method on four classification tasks across two clinical EEG datasets with abundant unlabeled data and limited labeled data. The experimental results show that our approach significantly outperforms contemporary methods in both efficiency and accuracy.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces a graph self-supervised learning framework, *EEG-DisGCMAE*, designed for pre-training models and transferring knowledge from high-density EEG data to improve classification performance on low-density EEG data. The framework combines *Graph Contrastive Learning(GCL)* and *Graph Masked Autoencoders(GMAE)* in a pre-training scheme that reconstructs contrastive samples and contrasts these reconstructions. With a novel *Graph Topology Distillation(GTD)* loss in the fine-tuning stage, the framework effectively transfers spatial knowledge from high- to low-density settings. This enables a lightweight student model to achieve enhanced classification performance with limited labeled data, showing potential for efficient and effective analysis in low-density EEG scenarios.

### Strengths
1. **Integration of Pre-train Methods from Original Perspective:** This paper proposes a novel approach that combines GCL and GMAE with the interpretation in relationships between node dropping and node masking, leading out a synergy of both self-supervised approach with unlabeled EEG data. This integration allows the model to achieve enhanced performance in scenarios with limited labeled data.

2. **Effective Knowledge Distillation in Spatial Connectivity:** By leveraging Graph Topology Distillation (GTD) Loss with contrastive distillation, the framework effectively distills the knowledge of teacher model from hard-to-obtain HD EEG data into a lightweight student model. This enables the student model to achieve robust performance even with only LD EEG data, making the approach more practical and accessible.

3. **Comprehensive Evaluation across Clinical EEG datasets:** The paper provides extensive experimental validation on four classification tasks across two datasets, demonstrating superior performance of EEG-DisGCMAE over existing methods and various baselines.

### Weaknesses
1. **Insufficient Evidence for Hypotheses:** The method relies on two key hypotheses: (1) that combining GCL and GMAE methods improves robustness in distillation, and (2) that jointly pre-training teacher and student models via mutual contrasting enhances distillation performance. However, these claims are not adequately validated in the current results. The paper would benefit from additional ablation studies and comparative evidence to clarify each component’s impact and substantiate these hypotheses. Specifically, the paper lacks a direct comparison of the proposed combined pre-training approach against using GCL or GMAE alone, each with and without the Graph Topology Distillation (GTD) loss during fine-tuning. This would isolate the effect of the combined pre-training and the GTD loss, clarifying their individual contributions. Furthermore, the benefits of mutual contrasting during pre-training are not clearly demonstrated against a baseline where GCL and GMAE are trained sequentially without this mutual contrastive component. 

2. **Lack of Clinical Interpretation:** While the paper includes visual assessments of EEG pattern reconstructions under various masking ratios, it lacks an analysis linking these patterns to clinically meaningful EEG features. Examining which EEG regions or connections contribute to classification tasks, and comparing these patterns with known clinical findings, would strengthen the study’s practical relevance. For example, the paper could explore whether the model highlights known biomarkers for specific conditions, such as the frontal theta activity in ADHD or the temporal lobe spikes in epilepsy. A more detailed analysis of the reconstructed EEG patterns, focusing on their clinical relevance, is needed to demonstrate the practical utility of the method.

3. **Limited Comparison with Recent SSL Methods:** The comparison primarily includes pre-2023 graph SSL methods, omitting recent graph SSL approaches [1, 2, 3, 4] and other EEG-specific SSL [5, 6] advancements that incorporate contrastive, generative, or both types of methods. Analyzing how the proposed approach differs from these recent methods would provide a clearer benchmark and better contextualize its contributions. For instance, the paper does not compare against recent methods that use graph masking for self-supervised learning or those that combine contrastive and generative approaches, which could provide a more comprehensive evaluation of the proposed method's novelty and performance.

### Questions
1. Hypothesis 1 suggests that combining GCL and GMAE results in a more robust distiller than using each method independently. However, it seems that when GCL or GMAE is used alone for pre-training, knowledge distillation is not applied during fine-tuning. Is this correct? To validate this hypothesis, ablation studies similar to Table 4 that compare the fine-tuning performance of GCL and GMAE with and without GTD in distillation cases would be beneficial. Furthermore, if there are prior works supporting this hypothesis, referencing them would strengthen the argument.

2. In Table 3, does "Seq. Comb." refer to first performing GCL, then GMAE? If so, what is the performance when GCL and GMAE are jointly trained without mutual contrasting using teacher and student keys, followed by distillation fine-tuning? If this setup improves performance over single pre-training methods and further enhances distillation fine-tuning with mutual contrasting, it could provide validation for both Hypotheses 1 and 2.

3. Is there a particular reason for using DGCNN as the backbone for the student model instead of Tiny G-Former? Given that the Tiny DGCNN  and the Tiny G-Former  have similar parameter counts (Table 7), and that G-Former generally performs better (Figure 2), G-Former might yield better results as the student model.

4. According to Appendix A, a learning rate of 0.0002 was used uniformly across pre-training methods during fine-tuning. While a common learning rate may work well for similar model architectures, if GCL and GMAE were validated only on G-Former, it’s possible that the selected learning rate might favor DGCNN. Additionally, each SSL pre-trained model may require an optimal learning rate suited to the specific starting representation, suggesting a need for more extensive hyperparameter ablation study in fine-tuning.

5. Using the same samples from the EMBARC and HBN dataset for both pre-training and downstream tasks raises potential data leakage concerns. Even with different window sizes, the model may still encounter similar information, which could lead it to memorize dataset-specific features instead of learning generalizable patterns. To better evaluate generalizability, pre-training on the larger HBN dataset and fine-tuning on EMBARC would provide a clearer measure of robustness across datasets.

Minor Comments:
1. Figure 1 appears to need revision. Although “Frozen” and “Tuned” are noted, the corresponding symbols are not visible. Additionally, the “GNN2GNN Distill Loss” in the figure is not referenced in the main text; does this term refer to the Graph Topology Distillation Loss? Consistent terminology would improve clarity.
2. In Equation 11, what is the meaning of the second $∣∣$ following the KL divergence? Does it function as a conditional mask using an indicator? If this notation is standard, could a reference be provided?

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
3

### Summary
The paper proposes a graph-based pretraining method for EEG data using contrastive learning and masked autoencoder. The pretrained model can be combined with distillation to improve the downstream performances on both low-density and high-density data.

### Strengths
- The proposed pretraining and fine-tuning method improves the preformance on multiple tasks of EEG data.

- The experiments are comprehensive. The paper compares with multiple baseline methods and conducts ablation studies.

### Weaknesses
 - The goal and contributions of the paper are ambiguous. The paper proposes two things. First, pretraining combines contrastive learning and reconstruction. Second, the large model can used for training a tiny model from distilluation. The first part is not quite novel. For the second part, it's also unclear how does distillation help the model than just using the large model?

- Equation (11) and (12) are confusing. What does "||" before P_ij means in Equ (11). In Eq (12), it is also not clear that why the distillation loss is defined like this. Is there any maths interpretation on what a sum of KL div over a sum of some other KL div means?  How are L^{logits}_{Dis} and L^{CE}_{Dis} defined and how are they implemented together with GTD loss? I believe the sample used in each batch are different. so it's unclear how these two losses can be summed during trainiing for a batch?

- What is the different between GTD loss and some self-distillation method for SSL like DINO? Why it is not used in PT part but the FT part?

- Figure 4 shows that training may not be enough after 400 epoch. How about validation loss?

- Figure 1 is unclear. What is shown in (a), HD or LD performance? In (b), how can a student model be large? plots AUC v.s. ACC, but they are highly correlated. Instead of size of circle, it might be more straight forward to put size on y-axis. In the caption, not sure what does it mean by "’L’ denotes large-size models." How was large-size models defined? What does ours-tiny/large in (a) coresponds to in (b)?

- The experiments lack important details on other baselines - are they trained on HD or LD or both datasets? The comparison might not be fair if they are trained with different data from the proposed method. 

- More explanations are necessary to help understanding what the colors and shapes in Figure 3 mean.

### Questions
See weakness. Please considering clarify the main contribution of the paper, as the goal of the paper is hard to follow in the version. 
Also, more details are need for method details. Please decribe the pipeline of the method - what data is used at which stage for both baseline and the proposed method? What is the purpose of some design choices? These will be helpful for the reasoning of the paper.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
In this paper, the authors integrate contrastive learning and knowledge distillation (KD) for EEG classification tasks. Specifically, they utilize contrastive learning between high-density EEG graphs and low-density EEG graphs to improve performance on limited labeled data. Additionally, they propose a Graph Knowledge Distillation approach with a Graph Topology Distillation loss to boost the performance of low-density EEG models when applied to high-density EEG data.

### Strengths
1. The description of the method is clear and easy to understand.
2. The authors' proposed method is technically sound.
3. Experiments are comprehensive.

### Weaknesses
1. The experimental results suggest that the proposed method offers only a marginal improvement, and due to the typically small size of medical datasets, the performance gains are not convincing for me.
2. The methods of comparison experiment are outdated, e.g.,  GMAE(Hou et al., 2022), GPT-GNN (Hu et al., 2020).
3. The method is incremental. The method designed in this paper is primarily a combination of existing approaches. In graph learning, both contrastive learning and knowledge distillation have been extensively studied, and contrastive learning across different data views, such as high-level and low-level representations, is also a common practice.

### Questions
1. Assumption1 and Assumption 2 seem too strong and lack explanations and empirical support.
2. As for Assumption 2, the assumption fails to specify how positive and negative pairs are selected.
3. As for Assumption 1, there may be instability in the training process or architectural differences between GCL and GMAE that could affect the effectiveness of joint pre-training.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper proposes a new approach, EEG-DisGCMAE, to address the challenge of enhancing low-density EEG analysis by leveraging high density EEG data. The authors used a graph-based transfer learning approach and considered this as a knowledge distillation problem. They introduced a unified pre-training framework that combines Graph Contrastive Learning (GCL) and Graph Masked Autoencoder (GMAE) methodologies. Their hybrid design captured robust features by reconstructing contrastive samples and contrasting the reconstructions, which enables both generative and contrastive pre-training. Their main contributions are as follows:

1.	EEG-DisGCMAE integrates GCL and GMAE pre-training to better leverage unlabeled data, optimizing the learning of robust features by combining generative and contrastive methods.
2.	The Graph Topology Distillation (GTD) loss function facilitates knowledge distillation from a complex HD EEG model (teacher) to a lightweight LD EEG model (student), enabling the student to handle missing electrodes through contrastive distillation.
3.	By jointly pre-training teacher and student models through contrastive querying, the framework enhances the distillation robustness, enabling strong transfer performance across downstream tasks.
4.	The authors validated EEG-DisGCMAE on two clinical EEG datasets, demonstrating its ability to outperform existing models in both accuracy and efficiency, even with reduced parameter sizes.

### Strengths
1. The paper introduces a novel unified framework combining Graph Contrastive Learning and Graph Masked Autoencoders, along with a specialized Graph Topology Distillation (GTD) loss for HD to LD EEG data distillation.

2. The methodology is solidly backed by theoretical foundations, with comprehensive experiments and ablations on two EEG datasets validating each component’s effectiveness.

3. The paper clearly explains complex ideas with well-structured sections, helpful figures, and strong contextualization within EEG and graph learning research.

4. The framework advances portable EEG diagnostics and has broader implications for graph-based learning, offering lightweight, high-performance solutions.

### Weaknesses
1. While the paper demonstrates effectiveness on specific EEG classification tasks, testing on a broader range of EEG applications (e.g., seizure detection, cognitive state classification) could further validate generalizability. The current evaluation is limited to datasets focused on relatively similar classification tasks, and it is unclear how the method would perform on tasks with different underlying signal characteristics and noise profiles, such as those encountered in seizure detection or cognitive load assessment. This lack of diversity in evaluation limits the conclusions about the model's robustness and applicability.

2. The paper focuses on graph-based methods, but comparing with non-graph EEG models (e.g., CNNs or RNNs used for EEG analysis) could provide a fuller picture of the proposed approach’s advantages and trade-offs. The current evaluation lacks a direct comparison to established non-graph based methods, making it difficult to assess whether the graph-based approach offers a significant advantage over more traditional methods, such as convolutional neural networks (CNNs) or recurrent neural networks (RNNs), which have been successfully applied to EEG analysis. A direct comparison would help clarify the specific benefits and drawbacks of the proposed method.

3. The explanation of the GTD loss function is complex and could benefit from additional breakdown or intuitive examples to clarify how positive and negative pairs are selected. The description of the Graph Topology Distillation (GTD) loss function is not sufficiently clear, particularly the mechanism for selecting positive and negative pairs. This lack of clarity makes it difficult to fully understand the loss function's behavior and its impact on the model's performance. More intuitive examples or a step-by-step breakdown of the selection process would be beneficial.

4. While low-density EEG is addressed, more evidence on the performance of the model at very low-density settings (e.g., <16 channels) would strengthen the claim that the model is effective for portable and affordable EEG setups. The paper does not provide sufficient evidence to support the claim that the model is effective for very low-density EEG setups. The performance of the model at extremely low channel counts, such as 8 or fewer, is not adequately explored, which is critical for assessing its applicability to portable and affordable EEG devices. More detailed results at these very low densities are needed to validate this claim.

5. Although ablations cover essential components, including more details on varying the depth of GCL-GMAE integration (e.g., testing contrastive-only or generative-only pre-training) would offer deeper insights into the contributions of each part of the pre-training framework. The ablation studies do not fully explore the individual contributions of the Graph Contrastive Learning (GCL) and Graph Masked Autoencoder (GMAE) components. Specifically, the paper lacks a detailed analysis of the performance when using only GCL or only GMAE for pre-training, and how varying the depth of integration between these two components affects the overall performance. This analysis would provide a more nuanced understanding of the framework's behavior.

### Questions
1. How does the framework perform on EEG tasks beyond classification, such as seizure detection?

2. Have you compared your model against non-graph EEG methods like CNNs or RNNs?

3. Can you clarify the selection process for positive and negative pairs in the GTD loss?

4. Have you tested your model at very low-density EEG settings (e.g., <16 channels)?

5. Could you provide more ablation results showing the impact of using only GCL or only GMAE in pre-training?

6. What is the potential of your model for real-time EEG applications in terms of computational efficiency?

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper proposes a pre-training framework for resting-state Electroencephalography (EEG), a crucial tool for understanding neural dysfunctions. First, EEG data is represented as graph data, and Graph Neural Networks (GNNs) are employed to capture both the intricate features and topological structures of the EEG data. Due to the difficulty of acquiring labeled EEG data, the authors propose leveraging large amounts of unlabeled EEG data to improve performance on tasks with limited labeled data. Specifically, they introduce a self-supervised pre-training strategy, which combines Graph Contrastive Pre-training (GCL-PT) and Graph Masked Autoencoder Pre-training (GMAE-PT), allowing for efficient learning from the unlabeled data. To further enhance the model's performance on high-density EEG data, the authors design a Graph Topology Distillation (GTD) loss function, enabling a lightweight student model to learn from a more complex teacher model trained on high-density EEG data. The proposed framework is evaluated on real-world EEG datasets, and the contributions of each component are analyzed through extensive ablation studies.

### Strengths
· The paper proposes a framework to capture intricate features in EEG data, which is crucial for diagnosing clinical brain disorders.

· Given the scarcity of labeled EEG data, the authors formalize an effective transfer learning strategy that pre-trains on large unlabeled datasets and fine-tunes on limited labeled data.

· The paper introduces a novel knowledge distillation objective function that allows models trained on low-density EEG data to handle missing electrodes, effectively enhancing model performance.

### Weaknesses
· The rationale behind the different components is unclear. It is not evident how the model handles the heterogeneous unlabeled EEG graphs. Specifically, the paper does not clarify how the model accounts for the variability in signal characteristics across different subjects and conditions when pre-training on a combined dataset of diverse EEG recordings.


· The authors do not discuss when Assumption 1 is valid and do not provide sufficient evidence to support the claim that combining GCL and GMAE results in a more robust distillation process. The paper lacks a theoretical justification or empirical analysis demonstrating that the combination of these two pre-training methods offers a synergistic effect, rather than simply adding complexity without clear benefits. Furthermore, the specific conditions under which this combination is most effective are not explored.


· The strategy of randomly dropping nodes and edges to generate query and key graphs raises concerns. As mentioned in line 037, EEG data has complex inherent structures, and randomly removing nodes or edges could disrupt the graph's topology, potentially undermining graph learning and making contrastive learning less effective. The authors do not address the potential for this random dropout to remove critical connections or introduce spurious relationships in the graph, thus hindering the model's ability to learn meaningful representations.


· The experimental setup is limited. The authors do not provide sufficient details about the graph data (e.g., the number of nodes and edges), making it difficult to assess the model’s generalization capabilities. The lack of detail regarding the specific graph construction process, such as the criteria for edge creation and the handling of varying channel densities across different datasets, makes it difficult to reproduce the results or evaluate the model's robustness.


· The paper is not well-written and is difficult to follow. For instance, the motivation behind proposing graph topological distillation is not clearly explained, leading to confusion. The paper lacks a clear articulation of the problem that GTD is intended to solve, and the connection between the proposed method and the specific challenges of EEG data analysis is not well-established.


· The paper is not well-written and hard to following. For example, it is quiet confusing that why the graph topological distillation is proposed

### Questions
· Could the authors provide more discussion on when Assumption 1 is valid?


· Would randomly dropping nodes and edges destroy important structures in the input EEG graphs?


· Regarding the contrastive learning framework, what is the rationale for using query and key graphs during contrastive learning? How does this approach aid in model pre-training? Why is the key sample pool beneficial?


· Could the authors provide more details on how topological information is preserved within the knowledge distillation framework?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 6

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
To fully leverage the extensive unsupervised data, this paper proposes a pretraining and fine-tuning paradigm for EEG representation learning, where GNN is applied as the backbone. To further enhance the learning of low-density data, this paper proposes a teacher-student distillation method to enrich the information from high-density data. Experiments are conducted on two datasets and four classification tasks, and the results demonstrate performance improvements over conventional GNN-based learning frameworks.

### Strengths
This paper formulates two important questions in EEG representation learning, 1) how to leverage unsupervised data, 2) how to distill knowledge from rich (high-density) EEG data. With incorporation of those external knowledge, the performance on various datasets and tasks has shown significant improvements. Overall, this paper is well structured. The insights are straightforward and the solution is clear.

### Weaknesses
Though the questions tackled are significant, the technique designed lacks some novelty. [1] tackles the similar problem in EMR representation learning for clinical prediction, and the solution is also very similar (using pretraining on large data volume and fine-tuning on small targets, and distill knowledge from datasets with rich features). There are some differences in detailed design according to the problem setting, but the core ideas seem identical.

Below are some technical issues:

0. In graph construction stage: There seems too much information loss during node representation construction. Why not consider using a time-series embedding model (transformer-based or lightweight RNN-based) to capture more high-order information in the EEG time series of every single channel as the node representation?

1. In GNN pretraining stage: How to ensure the representation spaces of teacher and student models can be inherently “alignable” when using different model architectures (Graph transformers v.s. GCN)? As GCNs are spectral-based GNN, while Graph transformers are spatial-based. The basic hypothesis behind those architectures is different, thus the alignment of their representation spaces cannot be directly ensured. It is more reasonable to use models in different sizes under the same architecture.

2. In GNN pretraining stage: The adjacency matrix A is dynamic during training. How to ensure the training stability? Moreover, GCN is a transductive GNN method, how to make it suitable for dynamic adjacency matrices?

3. In Fine-tuning stage: Z in Eq.(11) seems like a likelihood score according to Eq.(8). Then how to conduct KL between two scores in Eq.(11) , as they are not distributions?

4. In experiments: Maybe incorporate some other transfer learning/distillation methods for comparison?

Finally, I suggest supplementing a notation table of all the variables introduced in Chapter 3, as there are too many symbols and readers may easily get lost.

### Questions
See Weaknesses.

### Soundness
2

### Presentation
2

### Contribution
2
