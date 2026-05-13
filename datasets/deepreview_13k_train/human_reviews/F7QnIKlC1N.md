# GTMGC: Using Graph Transformer to Predict Molecule’s Ground-State Conformation

- Decision: Accept
- Scores: 8, 8, 3

## Abstract
The ground-state conformation of a molecule is often decisive for its properties. However, experimental or computational methods, such as density functional theory (DFT), are time-consuming and labor-intensive for obtaining this conformation. Deep learning (DL) based molecular representation learning (MRL) has made significant advancements in molecular modeling and has achieved remarkable results in various tasks. Consequently, it has emerged as a promising approach for directly predicting the ground-state conformation of molecules. In this regard, we introduce GTMGC, a novel network based on Graph-Transformer (GT) that seamlessly predicts the spatial configuration of molecules in a 3D space from their 2D topological architecture in an end-to-end manner. Moreover, we propose a novel self-attention mechanism called Molecule Structural Residual Self-Attention (MSRSA) for molecular structure modeling. This mechanism not only guarantees high model performance and easy implementation but also lends itself well to other molecular modeling tasks. Our method has been evaluated on the Molecule3D benchmark dataset and the QM9 dataset. Experimental results demonstrate that our approach achieves remarkable performance and outperforms current state-of-the-art methods as well as the widely used open-source software RDkit.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces a novel graph transformer specifically designed for 3D ground state prediction. Notably, the proposed architecture is versatile and applicable to a wide range of 3D supervised tasks. The key contributions of this work include:

A novel architectural proposal that elegantly extends the classical attention mechanism to 3D molecular graphs. This extension incorporates edge and interatomic distances as biases for the attention mechanism, enhancing its capabilities.

A successful demonstration of the effectiveness of this architecture in the realm of 3D ground state prediction, as well as its application to predict various other 3D molecular properties.

### Strengths
Originality:
Despite numerous unsuccessful attempts to construct graph transformers using principles akin to the original transformer, this work stands out as it elegantly achieves the intended goal with minimal architectural complexity. This work avoids unnecessary biases that often detract from the model's effectiveness, making it easier for most researchers to apply their existing intuitions from sequence transformers to this novel architecture.

Quality:
The architectural design and its application in ground state conformation prediction are well executed, as reflected in the results, solidifying its position as a favorable solution compared to alternative methods. The iterative refinement of $G_{cache}$ within the decoder represents a notable innovation that enhances model performance in conformer prediction. Ablation studies further clarify the significance of each component within the network, facilitating an understanding of their contributions to this specific modeling task.

Clarity:
The paper is well-written and maintains a high level of clarity, making it easily comprehensible for readers.

Significance:
While predicting the ground state of a molecule remains relatively underexplored due to its limited relevance in specific applications, this work serves as a foundational step that can be extended to tackle the broader challenge of full conformer generation. Such an extension holds are very significant, especially in the context of drug discovery.

### Weaknesses
The assertion regarding the innovative utilization of the MoleBERT Tokenizer might be overstated, especially in light of the results presented in Table 2. Previous molecular graph papers, such as the MolGPS paper, have explored various atomic featurizations that could potentially outperform the approach presented in this work. Specifically, the use of simple atomic IDs as input features, while computationally efficient, may not capture the full complexity of atomic interactions and chemical properties that more sophisticated featurizations could offer. The paper should include a more thorough comparison with other featurization methods, including those that incorporate learned embeddings or physicochemical properties, to justify the choice of the MoleBERT tokenizer.

To allocate more space for related works and experiments, it would be beneficial to consider shortening or omitting certain sections, such as those in the introduction (implementation) and preliminary sections (multi-head and transformer). The current introduction, while providing context, could be more concise, focusing on the specific challenges of 3D molecular graph modeling rather than general transformer concepts. The preliminary sections on multi-head attention and transformers, while necessary for completeness, could be shortened or moved to an appendix, given that these are well-established concepts.

The related work should be integrated into the main text rather than relegated to the appendix. It is crucial to comprehensively cover the various attempts to construct graph transformers and elucidate why they are ill-suited for the tasks at hand. This discussion should include a detailed analysis of the architectural choices made in previous attempts and why the current approach is superior. A more in-depth analysis of the limitations of existing graph transformer architectures, particularly in the context of 3D molecular data, is needed to fully appreciate the novelty of the proposed method.

### Questions
Was molecular property prediction approached as a single-task or multi-task endeavor?

Could you clarify the rationale behind placing the molecular property prediction results in the appendix, especially considering that they do not outperform SOTA across the board?

It could be valuable to assess the scalability of your architecture across various graph sizes, thereby determining where it potentially outperforms existing methods.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work proposes GTMGC, a graph transformer model for ground-state molecular conformation prediction. GTMGC uses a novel self-attention module to achieve effective molecular structure modeling. Experiments show that the proposed GTMGC model achieves state-of-the-art performance in ground-state molecular conformation prediction benchmarks.

### Strengths
Originality: The proposed graph transformer model is novel, with many novel technical contributions in effectively capturing spatial structures by self-attention mechanism.  
Quality: The effectiveness has been effectively demonstrated by experiments.  
Clarify: The writing and presentation of this paper is good and well-organized.  
Significance: The contribution of this work is very useful and meaningful to chemical and molecular biological science fields as the proposed method can significantly accelerate the computation of finding ground-state molecular conformations.

### Weaknesses
There are actually many prior studies about formulating the mapping from 2D molecular graphs to 3D molecular conformations as a generative problem. Though they are different from the problem studied in this work, these models can be trained on the used Molecule3D datasets and evaluated by generating only one molecular conformation. However, authors do not compare with any of these methods. Authors are recommended to compare with at least one molecular conformation generation method, such as [1].

[1] Torsional Diffusion for Molecular Conformer Generation. NeurIPS 2022.

### Questions
No additional questions.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes GTMGC, a transformer-based architecture for end-to-end prediction of 3D groundstate molecules' conformations from their 2D graph.

The method makes use of MoleBERT for initial embedding as well as LPE for positional encoding.
The inputs are then processed by a Transformer-based model, where the self-attention modules are augmented with the adjacency matrix and learned/predicted atomic distance matrix in a weighted sum fashion. 

The loss is augmented by a regularization of the middle distance matrix prediction.,

### Strengths
1. The paper is very clear and pleasant to read.
2. The integration of various existing frameworks for the task of molecules' ground state conformation is original to some extent.
3. The performances compared to the baselines are significant.

### Weaknesses
I believe there are two main weaknesses:

1. Novelty: There are plenty of previous works (not cited) implementing Transformer architectures that implement the elements of the proposed self-attention, e.g., [1] uses the adjacency matrix, [2] makes use of the distance matrix (even cited in the manuscript), while the weighted summation is ubiquitous in many fields using Transformers [3]. The initial encoding is obviously not a technical contribution.

Thus, the contribution may be summarized as the integration of existing methods/approaches, augmented with the regularization loss on the distance matrix (the \beta seems to bring very minor improvement).

2. Strange results: I may be wrong, but according to Table 3 (ablation study) a *simple Transformer* architecture without any addition to the self-attention reaches 0.4395 (MAE) which is already better than all the other baselines. This is problematic. Also, the final improvement is only ~1%. Finally, the reported results seem to take the best-ablated model results for each metric, which is wrong.

Moreover,  we have:

3. The advantage of MoleBert over the standard atomic encoding is extremely shallow or even worse.
4. Lack of comparison with other Transformer based methods.

### Questions
Currently, it seems the proposed contributions don't bring any advantage over a simple (large) transformer model.

1. One needs to know the capacity of the model in order to assess the origin of the good performance. 
According to weakness 2, it seems the good performances are obtained *almost solely* from a large/powerful standard Transformer model. From Table 5, the model seems much bigger than other methods. Also, the discrepancies between the tables are disturbing (one single metric should be used for the model validation).

2. Ablating the initial LPE. 

3. It would be beneficial to have a comparison performance with (at least one) other molecule transformer-based methods such as [4,5,6] or others at a similar capacity.

4. It would be interesting to look at the learned weighting parameters (\gamma) of the self-attention to better understand the contribution of each (maybe even adding a weighting to the global attention).


[4] Relative molecule self-attention transformer.

[5] 3dtransformer: Molecular representation with transformer in 3d space.

[5] Geometric transformer for end-to-end molecule properties prediction.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
