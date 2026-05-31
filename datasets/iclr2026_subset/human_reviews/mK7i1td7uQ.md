## Human Reviewer 1

### Summary
The paper modifies Uni-Mol by retraining the model without “flat” structures (molecules with all Z coordinates set to zero), finding minimal impact on performance; introducing a contrastive learning objective to align embeddings across multiple 3D conformations, though the novelty over Uni-Mol’s existing contrastive loss is unclear; and exploring the use of the Organic Molecules (OMol) dataset instead of the original Uni-Mol dataset, which did not lead to significant improvements. Overall, the method consists of incremental adjustments rather than a fundamentally new approach.

### Strengths
The paper is detailed and uses domain-specific terminology appropriately.

### Weaknesses
Overall, the paper reads more like a technical report on modifications to Uni-Mol rather than presenting a strong methodological contribution.

- **Modification of Uni-Mol:**
   - The authors identified that the original Uni-Mol model included “flat” structures (atoms with Z = 0) in ~9% of the training data and retrained the model without them, finding negligible performance degradation.
While this is a useful insight, it is minor. The original design helps Uni-Mol generalize to molecules with incomplete 3D information or planar molecules (e.g., aromatic rings, graphene fragments). Showing that removing this feature has little effect is interesting but not a major contribution.
  - The paper proposes a contrastive learning objective to align embeddings across multiple conformations. However, Uni-Mol already applies contrastive learning across conformations, where positive pairs are conformations of the same molecule and negatives otherwise.
It is unclear how the proposed contrastive loss differs from the original Uni-Mol approach, and this should be clarified.
  - The exploration of the Organic Molecules (OMol) dataset instead of the original Uni-Mol dataset did not lead to noticeable performance improvements.
- The authors do not include a baseline using only graph data (without 3D information). Without this, the effectiveness of 3D conformations cannot be properly evaluated, especially when some works has shown that using RDKit-generated 3D coordinates can even lead to degrade performance (RDKit is not very accurate in this task).
- **Terminology and ML Understanding:** 
  - The manuscript misuses some CS/ML terminology. For example, “retrain” is incorrectly used where “fine-tune” is meant (e.g., abstract: *current approaches require retraining the entire model for each prediction task, using published weights only as initialization* → this is actually fine-tuning).
  - Moreover, the statement *current approaches require retraining the entire model for each prediction task, using published weights only as initialization* is inaccurate at a deeper level: pretrained models can be used as feature extractors to train other models for downstream tasks. This is one of the main motivations of the paper, undermining the importance of the actual problem they are trying to solve. Overall, this suggests a weak understanding of ML concepts.
  - The claim *from a physical point of view, molecular graphs do not exist* is unconvincing as an argument against this datatype. Many representations (FASTA sequences, DNA sequences, or even text) do not physically exist in the same sense, yet are useful abstractions. This argument does not support the proposed approach.
  - The claim *structural formulas work well for the chemistry of organic molecules, but for more complex compounds* is misleading. The sentence implies that *more complex compounds* (such as organometallics) are not organic molecules, which is not entirely accurate. Moreover, I think this work focuses on building models for representing organic compounds.
  - The term *task-agnostic* in the abstract is an overstatement, since the authors still fine-tune their models on downstream tasks.

### Questions
How does your use of contrastive learning differ from that in Uni-Mol?

### Soundness
2

### Presentation
2

### Contribution
1

### Rating
2

### Confidence
4

---

## Human Reviewer 2

### Summary
This paper proposes a pretraining strategy that incorporates conformational information to enhance molecular representation learning. The authors argue that modeling 3D space is essential for capturing molecular properties. While the motivation is sound, the manuscript suffers from several critical issues that undermine its contribution.

### Strengths
The topic of incorporating 3D information is well-motivated.

### Weaknesses
1. **Misrepresentation of Prior Work**  
   The authors claim that “no chemical embedding model capturing the diversity of 3D molecular conformations has yet been published.” This statement overlooks a substantial body of literature on conformer-aware pretraining. Several existing models explicitly incorporate 3D conformational diversity, and the lack of engagement with these works raises concerns about the novelty and scholarly rigor of the paper.

2. **Limited Novelty**  
   The proposed techniques—pretraining on conformers and freezing the backbone while fine-tuning only the final MLP layer—are well-established practices in molecular machine learning. The manuscript does not present sufficient innovation beyond these standard approaches.

3. **Underwhelming Performance**  
   As shown in Tables 1 and 2, the model's performance falls short of state-of-the-art methods across multiple benchmarks. The results do not convincingly demonstrate that the proposed approach yields meaningful improvements in molecular representation quality.

### Questions
**Questionable Embedding Behavior**  
   Figure 5 presents a pair of conformers with substantial geometric differences. If ConforFormer-OMol had truly learned a robust understanding of 3D molecular structure, the cosine similarity between these embeddings should be significantly lower. This example casts doubt on the model’s ability to distinguish conformational nuances.

### Soundness
1

### Presentation
2

### Contribution
1

### Rating
2

### Confidence
3

---

## Human Reviewer 3

### Summary
This paper explores the use of advanced contrastive learning techniques to enhance molecular representation learning. By introducing the ConforFormer framework, the authors aim to develop conformation-invariant molecular embeddings that capture 3D geometric information without relying on explicit molecular graphs. Although the idea is conceptually interesting and relevant to modern chemical foundation models, the method shows limited novelty beyond existing architectures such as Uni-Mol, and several claims lack sufficient experimental or theoretical support.

### Strengths
Using advanced contrastive learning to improve molecular representation learning is an interesting research topic.

### Weaknesses
1. The presentation of the paper is poor, making it difficult to understand the research problem and motivation it aims to address. In the abstract, the authors argue that existing methods using published weights only as initialization have certain limitations.  
I do not think this is a real limitation, since most approaches intentionally leverage pretrained foundation models to support various downstream tasks. In the introduction, the authors claim that real-world datasets are often too small to allow stable retraining, which is also not accurate, as many domain adaptation techniques—such as few-shot learning and data augmentation—can effectively address this issue.  

2. The proposed method lacks novelty. The so-called *“new weakly supervised contrastive learning objective”* is essentially the standard contrastive loss without any additional innovation. The authors claim to propose a novel structure called **ConforFormer**, but it is architecturally identical to **Uni-Mol**, except for the added contrastive learning objective.  Also, some other paper already has used Contrastive Learning for 3D molecular representation learning, see [1]

3. Some claims in the paper lack sufficient evidence. For example, the paper mentions *“a benchmark evaluating the model's ability,”* but there is no open-source release or supporting evidence provided to describe the benchmark in detail.  

[1]Qin, Jiayu, et al. "A probability contrastive learning framework for 3D molecular representation learning." Advances in Neural Information Processing Systems 37 (2024): 58058-58076.

### Questions
What are the detailed definitions of the loss terms in the total loss (e.g., L_token, L_coord, L_distance)?  
How were these terms computed, and how were the coefficients (5, 10, 2) determined — empirically or theoretically?

### Soundness
2

### Presentation
1

### Contribution
1

### Rating
2

### Confidence
4

---

## Human Reviewer 4

### Summary
This paper proposes ConforFormer, a Transformer-based molecular representation model that aims to learn conformation-invariant molecular embeddings through contrastive learning across different 3D conformers of the same molecule. The goal is to obtain general molecular representations that capture structural consistency without requiring task-specific fine-tuning.

### Strengths
1. The paper targets a meaningful and relevant problem, how to build robust molecular representations that account for 3D conformational variability.
2. The proposed framework is conceptually clear and easy to follow, with a reasonable motivation and solid experimental setup.
3. The introduction of the PharmIsomer benchmark provides an interesting way to evaluate whether models can distinguish between conformers and isomers. The writing and figures are clear, making the overall presentation accessible.

### Weaknesses
1. Limited technical novelty: The approach mainly extends existing ideas from contrastive learning and 3D molecular representation (e.g., Uni-Mol) without introducing substantial methodological innovation.
2. The results do not show clear or consistent improvements over strong baselines such as Uni-Mol; in some benchmarks, performance is even slightly worse. This weakens the paper’s contribution, since if training the baseline is not computationally expensive, practitioners would still prefer to fine-tune an existing model rather than use ConforFormer’s frozen representation.

### Questions
Please refer to the cons

### Soundness
2

### Presentation
3

### Contribution
2

### Rating
4

### Confidence
3