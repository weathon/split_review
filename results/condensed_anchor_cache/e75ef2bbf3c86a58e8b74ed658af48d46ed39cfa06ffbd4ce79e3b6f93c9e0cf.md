- Decision: Reject
- Scores: 3, 3, 6

## Merged Review

### Summary
This paper tackles model editing (structured pruning and class unlearning) for deep neural networks in a data-free regime, where training data and loss functions are unavailable. The authors propose identifying "HiFi components" – a small subset of channels per layer whose input contributions strongly correlate with the layer’s output feature map. Identifying these components is formulated as an expected reconstruction error problem, solved via a heuristic called RowSum. To recover accuracy after editing, they derive an upper bound on the post-editing loss in terms of changes in BatchNorm (BN) statistics and propose BNFix, an algorithm to update BN statistics using distributional access. Two algorithms, CoBRA-P (pruning) and CoBRA-U (unlearning), are introduced. Experiments on CIFAR-10/100 and ImageNet with ResNet architectures show reductions in FLOPs/parameters and forget-class accuracy, with claims of competitive performance.

### Strengths
- **Data-free model editing setting**: The paper addresses a timely problem of editing models without access to training data, for both structured pruning and class unlearning (Reviewer 1, 2, 3).  
- **Interesting conceptual insight**: The idea of identifying HiFi components via correlation between input contributions and output feature maps is novel and compelling (Reviewer 1). The distributional viewpoint rather than sample-wise sensitivity is a key strategy that may extend to continual learning, explainability, and other areas (Reviewer 2).  
- **Theoretical contribution on BN statistics**: A novel theoretical analysis characterizing post-editing model performance via an upper bound on the loss using changes in BN statistics is provided (Reviewer 3). Note: Reviewer 1 found the bound potentially loose due to reliance on the largest Hessian eigenvalue, while Reviewer 3 viewed this analysis as a strength.  
- **Potential wide applicability**: The distributional approach could be applied beyond pruning/unlearning to other problems where controlled model editing is needed (Reviewer 2).

### Weaknesses
- **Limited technical novelty of core components**:  
  - The RowSum heuristic is a simple correlation measure between input contributions and output feature maps, lacking deeper theoretical justification for why this specific correlation reliably identifies crucial components (Reviewer 1, 2). The paper does not prove that distributional similarity implies retention of learned knowledge, nor does it rule out alternative causes (e.g., random initialization artifacts) (Reviewer 2).  
  - The BNFix algorithm is similar to existing methods for adjusting BN means/variances; the differences and advantages over prior work are not adequately highlighted (Reviewer 1).  
  - The theoretical bound uses the largest eigenvalue of the Hessian, which can be loose for deep networks, and no empirical evidence is provided to assess its tightness (Reviewer 1).

- **Limited applicability of the method**:  
  - The core theory and algorithms rely heavily on BatchNorm statistics, which are absent in many modern architectures (e.g., Vision Transformers). This significantly limits the impact compared to model editing work that is architecture-agnostic (Reviewer 3). The authors do not clarify whether the HiFi concept can be adapted to models without BN (e.g., LayerNorm-based networks) (Reviewer 3).  
  - The evaluation is restricted to ResNet architectures on CIFAR-10/100 and ImageNet. Generalizability to other tasks, datasets, and architectures (including transformers) is not demonstrated (Reviewer 1, 3).

- **Insufficient empirical validation**:  
  - The number of baseline methods is limited, especially for the unlearning task. Data-free baselines (e.g., task arithmetic-based unlearning) and non-data-free methods (e.g., gradient-based unlearning) are missing, making it hard to assess relative performance (Reviewer 3).  
  - The claimed trade-off between accuracy and efficiency is not convincingly shown: the method often does not achieve competitive accuracy, and efficiency gains are not strong enough to justify the added complexity (Reviewer 3).  
  - The reliance on external data (even from a similar distribution) weakens the practical data-free claim. An ablation study on the size and quality of the external dataset is absent (Reviewer 3). More datasets with varying characteristics should be tested (Reviewer 1, 3).

- **Poor presentation and writing quality**:  
  - Many grammar errors, missing spaces, inconsistent citation formatting, and unpolished sentences (e.g., missing CNN full name, line 47; inconsistent parentheses spacing; missing commas) (Reviewer 2).  
  - Figures are too small to read, especially Figure 2 (key assumption on reconstruction error) and appendix figures (Reviewer 1, 2, 3).  
  - Incorrect labeling of Assumption 5 (line 328); equations (e.g., Eq. 3) exceed text width; notations are unclear (e.g., lines 177–178) (Reviewer 2, 3).  
  - The connection between HiFi component identification and BNFix is not clearly established; the flow between sections is disjointed (Reviewer 1). The paper lacks an intuitive explanation of how RowSum leads to HiFi components and how these are used in pruning/unlearning (Reviewer 1).

- **Unclear theoretical and conceptual foundations**:  
  - It is not explained why retaining/discarding HiFi components preserves or forgets specific learned knowledge, nor how distributional similarity guarantees that components encode the model’s crucial features (Reviewer 2).  
  - Assumptions, equations, and notations (e.g., the definition of B in the model editing formula) are ambiguous or inconsistent, making it difficult to follow the theory (Reviewer 2, 3).  
  - The paper does not explore how different types of knowledge (general vs. specific) might map to HiFi components (Reviewer 2).  
  - Several questions from reviewers correspond to missing experiments or ablations:  
    * How to compute Figure 2 in detail? (Reviewer 1)  
    * Why only BN statistics need fixing? (Reviewer 1)  
    * Is additional information stored during training? (Reviewer 1)  
    * Could insights be extended to non-BN models? (Reviewer 3)  
    * Ablation on external dataset size (Reviewer 3)  

- **Minority reviewer contrast**: One reviewer (score 6) was notably more positive about the theoretical analysis and the overall approach, but still raised significant weaknesses regarding limited applicability, insufficient validation, and presentation issues, echoing the other two reviewers (scores 3) on many points.