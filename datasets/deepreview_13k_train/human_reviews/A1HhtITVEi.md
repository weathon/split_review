# CheapNet: Cross-attention on Hierarchical representations for Efficient protein-ligand binding Affinity Prediction

- Decision: Accept
- Scores: 5, 8, 5, 6, 6

## Abstract
Accurately predicting protein-ligand binding affinity is a critical challenge in drug discovery, crucial for understanding drug efficacy. While existing models typically rely on atom-level interactions, they often fail to capture the complex, higher-order interactions, resulting in noise and computational inefficiency. Transitioning to modeling these interactions at the cluster level is challenging because it is difficult to determine which atoms form meaningful clusters that drive the protein-ligand interactions. To address this, we propose CheapNet, a novel interaction-based model that integrates atom-level representations with hierarchical cluster-level interactions through a cross-attention mechanism. By employing differentiable pooling of atom-level embeddings, CheapNet efficiently captures essential higher-order molecular representations crucial for accurate binding predictions. Extensive evaluations demonstrate that CheapNet not only achieves state-of-the-art performance across multiple binding affinity prediction tasks but also maintains prediction accuracy with reasonable computational efficiency.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a new solution to the protein-ligand binding problem, namely modeling molecules and proteins at a higher level than the atom (cluster level). This motivation comes from the fact that modeling only at the atomic level can easily lead to computational burden and reduced accuracy. Experiments on the ligand affinity prediction and ligand efficacy prediction tasks demonstrate the effectiveness of proposed method.

### Strengths
1. The motivation is reasonable, and it is possible to enhance the generalization of the model by trying to model at levels other than atoms.

2. The proposed method is simple and easy to understand.

3. Code is provided and is executable.

4. The experimental results are satisfactory in terms of both accuracy and computational efficiency.

### Weaknesses
1. The writing logic of the article is not smooth, making it less readable. Two examples: (1) In the first paragraph in Introduction, a better presentation would be to first introduce the task, then talk about the wet lab approach and limitations, and finally analyze the challenges of deep learning models in solving this problem. Then, the purpose of the sentence describing DTI is also unclear and can be deleted. (2) Why does line 047 begin with "however"? Didn't you just talk about the limitations of atom-level modeling?

2. The motivation is reasonable, that is, the entire functional group may interact with a certain protein region. However, the pooling method used does not seem to guarantee this. Can the author consider, at least, adding additional loss to ensure that clusters represent the functional group?

3. The significance of hierarchical representation is usually to allow the model to adaptively learn and select features from different information channels. I also agree that some interaction cases come from the entire functional group rather than the atom, but this is not absolute. Therefore, I prefer dual awareness at the atom-level and cluster-level. Although cluster-level representations are derived from atom encoders, this only complies with the strong assumption that individual atoms do not participate in interactions. The framework I suggest is to use atom selectors (such as attention selection or gating algorithms) to filter important atom representations to merge with cluster representations.

4. Let's analyze the title. This paper's greatest contribution seems to be to propose a specialized adaptive attention mechanism for hierarchical representation learning. However, the proposed cross-attention algorithm seems to be only for the cluster level. In addition, if this is the case, what is the difference between the proposed method and directly adopting the cross attention module in [1]?

5. This is a point I would like to discuss with the author. In this paper, the author allows complex input, but only uses this information in atom embedding computation. Perhaps there is a more explicit way to use this information. Since we already know the rough range of where the interaction occurs, why not use it to guide the coefficient of cross attention. For example, assuming that cl:1 and cp:2 are clusters of ligand and protein at the interface, the correlation coefficient between cl:1 and cp:2 should be much higher than the others.

### Questions
1. How to determine the number of clusters for ligand and protein?

2. In fact, the proposed method still needs to learn effective atom-level representation to obtain pooling results and cluster representation. What is the advantage in computational efficiency?

3. The method in this paper does not seem to be limited to processing protein and ligand interactions, but can also handle protein-protein related tasks (please correct me if I am wrong). If the authors can perform additional experiments such as protein-protein interaction, protein-protein docking or protein-protein interface prediction, it will further prove the scope of the proposed method.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
Predicting protein-ligand binding affinity is essential for drug discovery. Due to the complexity of protein-ligand interactions, traditional prediction models, which mainly rely on the atom-level interactions, are often computational intensive and unable to capture the complex and higher-order interactions. This paper proposes a deep learning-based model, CheapNet, for protein-ligand binding affinity prediction. CheapNet uses a cross-attention mechanism on hierarchical representations to capture intricate molecular interactions while maintaining computational efficiency.

### Strengths
1. CheapNet integrates both atom-level and cluster-level representations of protein-ligand complexes, this can significantly enhance the model's ability to predict protein-ligand binding affinity. The idea is novel and meaningful。

2. CheapNet employs the DiffPool method to cluster atoms in both the protein and ligand, reducing complexity while retaining the critical protein-ligand interaction patterns. The use of the cross-attention mechanism between protein and ligand clusters highlights the most relevant inter-molecular interactions, filtering out less impactful interactions and reducing the computational costs.

3. The authors utilized the PDBbind and  CSAR NRC-HiQ datasets to benchmark CheapNet against different types of protein-ligand binding affinity prediction models, They evaluated the model performance on ligand binding affinity and ligand efficacy prediction using different performance metrics. Subsequently, ablation studies were conducted to evaluated the model's effectiveness, focusing on adaptability of cluster-attention, hierarchical representations and attention mechanism, and cluster size. The experiments are comprehensive, and demonstrate CheapNet's superior performance.

### Weaknesses
1. CheapNet relies on high-quality three-dimensional structural data. However, many proteins lack experimentally crystallized structures, which limits CheapNet's ability to make predictions for proteins without available three-dimensional structural data.

2. In the section 'Permutation Invariance of Clusters for Cross Attention', the authors demonstrate that CheapNet’s cross-attention mechanism ensures permutation invariance for protein and ligand cluster-level representations. However, in protein-ligand interactions, three types of symmetries—translation, rotation, and permutation—should be considered. In my opinion, discussing whether and how the model achieves rotation and permutation invariance in local coordinates, as well as translation, rotation, and permutation equivariance in global coordinates, is essential. Only focusing on discussing the permutation invariance is insufficient.

3. While the cluster-attention mechanism is beneficial for filtering out irrelevant protein clusters, the approach also clusters the atoms of the ligand. Given that ligands are typically small molecules with relatively few atoms, some even fewer than 20, there's a concern that crucial molecular information might be lost during the clustering process. This could potentially limit CheapNet's applicability, particularly for very small ligands where atom-level details are critical for accurate binding affinity prediction.

### Questions
1. Discuss how to deal with the proteins which do not have the experimentally crystallized structures. For instance, combine some AI protein prediction models, or use alternative representations for the proteins without three-dimensional structures

2. Extend the discussion on whether and how CheapNet handle the symmetries of protein-ligand complexes. If CheapNet is not able to address other types of symmetries,  then discuss howthis might impact the model's performance or generalizability, and the further improvement.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The authors developed a novel interaction-based model (called CheapNet) that combines atom-level representations with hierarchical cluster-level interactions using a cross-attention mechanism to predict binding affinity tasks. The authors showed that CheapNet can effectively capture key higher-order molecular representations necessary for accurate binding predictions. They also performed extensive evaluations to show that CheapNet can deliver state-of-the-art performance in various binding affinity prediction tasks while maintaining efficiency in computation.

### Strengths
-Used both local and global information to predict the binding affinity. The idea is relatively novel.
-Compared the performance of the proposed approach to that of many baseline approaches.
-Demonstrated the model interpretability.

### Weaknesses
-The model performance representation can be further improved, such as using p-values to evaluate whether the proposed approach is significantly better than the baselines? the authors claimed "significantly outperforming all baselines", but there are no metrics to support the conclusion.
-It is not clear whether all the comparisons in the results tables are fair comparisons. For example, all these baselines are based on the same data evaluation strategy as the proposed approach (or the same set of training, validation and test sets) ? If the baseline results are from the original papers, how can we make sure the performance evaluations are fair?

### Questions
I am curious whether the author can apply the trained models to predict real-world cases involving known disease-causing proteins. Can the models identify compounds from a large library, such as ZINC250K, that are likely to bind to these proteins? Since the authors have emphasized the model's strong interpretability, I would appreciate seeing how the model’s functions are used to interpret the prediction results in this case.

### Soundness
3

### Presentation
2

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
The manuscript proposes a cross-attention method based on atom clustering for protein-ligand affinity prediction. This approach employs a soft-assignment method to separately cluster atoms in the protein and ligand, followed by a cluster-level attention mechanism to facilitate information exchange between the two. The model demonstrates significantly improved performance over baseline methods, and ablation studies indicate that integrating both clustering and cross-attention mechanisms into existing methods enhances prediction accuracy.

### Strengths
The method is innovative. By clustering atoms separately within the protein and ligand, it effectively improves affinity prediction performance.

### Weaknesses
1. The method’s details are not clearly explained. For example, how are the numbers of clusters for protein and ligand selected? Additionally, the process for initializing the representations of the protein and ligand is unclear.

2. While the method is interesting, the reasoning behind the clustering and cross-attention mechanisms' positive impact on model performance is not fully explained. Further analysis would provide valuable insights. For instance, although a soft clustering method is applied, this component is not explicitly supervised in the loss function. Why does such a soft clustering approach improve the model's performance?

### Questions
1. How the numbers of clusters for protein and ligand selected?

2. Is there any experimental evidence explaining why the clustering method enhances model performance?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
Summary:  The paper introduces CheapNet, a novel model designed for protein-ligand binding affinity prediction. Focusing on efficiency, CheapNet employs a cross-attention mechanism on hierarchical representations to address limitations of traditional atom-level methods, which often capture noise by treating all atom interactions equally. By integrating differentiable pooling, CheapNet selectively forms clusters of atoms that are relevant to binding interactions, reducing computational complexity and improving accuracy. Experimental results demonstrate CheapNet’s competitive, state-of-the-art performance across multiple datasets.

### Strengths
1.The paper is clearly written, the authors focus on a critical issue in drug discovery for which they proposed a solution and demonstrated by well designed experiments, that their proposed solution works well.
2.The main idea of using cluster-based, attention-guided binding predictions is well-motivated and aligned with current needs in efficient, scalable drug discovery models.
3.CheapNet achieves state-of-the-art performance across multiple datasets, showcasing its ability to balance accuracy and computational efficiency effectively.

### Weaknesses
1.The application of clustering and cross-attention is not novel for this field, as clustering is used in models like GemNet, Equiformer, and LEFTNet. Although CheapNet integrates these methods, it does not introduce substantial methodological innovations.

2.The paper lacks a discussion of relevant clustering methods and does not provide sufficient analysis of different clustering approaches. This omission makes it difficult to assess the comparative advantages of CheapNet’s differentiable pooling mechanism.

3.The comparison lacks depth with state-of-the-art methods, including GemNet, Equiformer, and LEFTNet, all of which employ unique strategies for interaction prediction that CheapNet could be benchmarked against more thoroughly.

4.Equation 2’s category count (number of clusters) is unclear. It would be beneficial to specify whether it is a predefined constant or dynamically determined based on molecular size or complexity. This information is crucial for assessing how different molecular structures might impact CheapNet’s clustering performance.

5.The authors should review and discuss the relevance of clustering methods used by existing models like LEFTNet, which employs a layered approach to handle structural hierarchies. Additionally, the work should compare or at least mention methods from “Generalist Equivariant Transformer Towards 3D Molecular Interaction Learning” to position CheapNet’s approach among recent advancements.

### Questions
See in weakness.

### Soundness
2

### Presentation
3

### Contribution
2
