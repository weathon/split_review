# Size-Generalizable RNA Structure Evaluation by Exploring Hierarchical Geometries

- Decision: Accept
- Scores: 6, 6, 8, 6

## Abstract
Understanding the 3D structure of RNA is essential for deciphering its function and developing RNA-based therapeutics. Geometric Graph Neural Networks (GeoGNNs) that conform to the $\mathrm{E}(3)$-symmetry have advanced RNA structure evaluation, a crucial step toward RNA structure prediction. However, existing GeoGNNs are still defective in two aspects: 1. inefficient or incapable of capturing the full geometries of RNA; 2. limited generalization ability when the size of RNA significantly differs between training and test datasets. In this paper, we propose EquiRNA, a novel equivariant GNN model by exploring the three-level hierarchical geometries of RNA. At its core, EquiRNA effectively addresses the size generalization challenge by reusing the representation of nucleotide, the common building block shared across RNAs of varying sizes. Moreover, by adopting a scalarization-based equivariant GNN as the backbone, our model maintains directional information while offering higher computational efficiency compared to existing GeoGNNs. Additionally, we propose a size-insensitive $K$-nearest neighbor sampling strategy to enhance the model's robustness to RNA size shifts. We test our approach on our created benchmark as well as an existing dataset. The results show that our method significantly outperforms other state-of-the-art methods, providing a robust baseline for RNA 3D structure modeling and evaluation.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper proposes EquiRNA, a hierarchical equivariant neural network designed to evaluate RNA 3D structures and generalize across varying RNA sizes, along with a new benchmark dataset rRNAsolo. The key strength is its practical approach to scaling equivariant neural networks for RNA data through multi-level equivariant message passing and size-insensitive k-NN sampling. Additionally, the paper introduces a new curated RNA dataset for structure fitness prediction task which is an important contribution given the scarcity of RNA datasets. However, the choice of E(3) over SE(3) equivariance ignores molecular chirality, the subunit and nucleotide level message-passing mechanisms lack clear motivation, and the empirical validation would benefit from multiple dataset splits given the relatively small number of samples in the datasets.

### Strengths
1. The paper tackles important practical limitations of the scalability of equivariant neural networks applied to real biological data.
2. The paper focuses on RNA which is a much less saturated domain compared to other biomolecular modalities such as proteins. Extending a machine learning toolkit for RNA analysis is an important contribution.
3. The paper introduces a new dataset rRNAsolo. Authors make great effort in collecting the data and purifying it on multiple levels. This is an important contribution given the scarcity of RNA datasets for machine learning.
4. The subunit-level message passing is novel and the ablation study underlines its importance for the fitness prediction task.
5. The k-NN sampling strategy is a simple approach for that potentially robustifies a model against an input size distribution shift.

### Weaknesses
1. The method focuses on E(3)-equivariance while in reality SE(3)-equivariance is the most relevant due to the molecular chirality. The E(3)-invariant/equivariant method does not discriminate between RNA molecules and their reflection which often comes with drastically different properties. This severely limits the practical applicability of the proposed method. Authors may consider the method presented in [1] (Eq.6-7) as a relatively easy way to break the symmetry to reflections and achieve SE(3)-equivariance.
2. The size generalization problem requires further elaboration. RNAs of different lengths usually correspond to different types, and hence different functions and structures. With this, it is hard to see how a network could generalize to another type of RNA with possibly completely different biological function/structure without observing it during training. The paper does not adequately address the fundamental challenge that RNA structure and function are highly correlated with length, and therefore, training on shorter RNAs may not provide sufficient information to generalize to longer, functionally distinct RNAs.
3. The subunit-level message passing (lines 273-300) is not explained clearly, and the particular form of message-passing in equation (2) is not well-motivated. Without this clear motivation, I fail to see why this form of message-passing will bring any advantage compared to a simple EGNN-like message-passing scheme. The use of attention weights, while potentially useful, lacks a strong justification in the context of RNA structure. It is unclear why a learned attention mechanism is superior to a simpler, geometrically-motivated approach for capturing interactions between subunits.
4. Similarly, the particular form of nucleotide-level message passing is not well-motivated. The framework of learnable templates and matrix-valued message function in Eq. 3 appears as unnecessary over-complication. I am wondering why the simplest approach of averaging the nucleotide coordinates (similar to how it is done with invariant nucleotide features) is not enough here. At least, I would expect an ablation study with respect to simple averaging. The use of learnable templates and matrix-valued functions introduces unnecessary complexity, and the paper fails to provide a clear rationale for why this approach is superior to a simpler, more direct method of aggregating atomic information within each nucleotide.
5. The experiments are performed only on one split of the datasets. Given the relatively small number of samples in the datasets, it is good to run the methods over several splits and provide mean and standard deviation results. Further, the benchmarking on the proposed rRNAsolo dataset will be much more reliable if the dataset comes with several provided train\val\test splits. This will significantly increase the weight of the rRNAsolo contribution.
6. The related work on Geometric GNNs misses elaboration on recent scalable equivariance methods: [2,3,4], etc. This is important since the paper claims to tackle the practical limitations of the scalability of equivariant neural networks

Minor:
- line 346 typo: size-generation -> size-generalization

### Questions
I suggest authors address weaknesses for the rebuttal.

### Soundness
3

### Presentation
3

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
The paper introduces EquiRNA, a model which has three-level hierarchical architecture—atom-level, subunit-level, and nucleotide-level—inspired by the biological composition of RNAs. The model is designed to efficiently model RNA structures while handling RNAs of varying sizes, referred to as the size generalization problem in the paper. The paper introduces a new dataset curated from public database and benchmarks the proposed model against this dataset and an existing ARES dataset outperforming existing methods for the task of predicting RMSD between candidate and native structures, used for scoring and ranking all candidates to identify the one most
closely matching the native structure.

### Strengths
1. The paper proposes three-level E(3)-equivariant message-passing design for modeling RNA 3D structures that captures atom, subunit, and nucleotide interactions effectively. This is inspired by the biology of RNA and sensible contribution.
2. The paper showcases an application of EGNN architecture to model the interactions within different levels of RNA. Although it is a straightfoward application of EGNN, I find it addresses a meaningful modeling aspect respecting the prior knowledge from biology. Size-insensitive K-nearest neighbor sampling is also intended to boost the model’s performance on varied RNA sizes, addressing a common challenge in RNA modeling.
3. Introducing rRNAsolo benchmark is useful for future development in this area.
5. The paper is well-written for most parts, with ideas explained in a structured manner.

### Weaknesses
Although the paper tackles an important problem, there exist several avenues for improvement. 
1. Given that the paper is meant to address the size generalization aspect of RNA structure evaluation, the experiments are carried out mostly on relatively smaller RNA sequences (~200 nucleotides). In most practical applications, the RNA sequences can easily range from hundreds to even thousands of nucleotides. To strengthen the claim that the proposed model can generalize to larger size RNAs, is it possible to showcase performance on larger RNA sizes or to discuss any technical limitations that prevented testing on very large RNAs?

2. Though the K-nearest neighbor sampling helps, there might still be overfitting to smaller RNAs, as training primarily relies on these samples. It is possible that I may have misunderstood but I am not sure how K-nearest neighbor sampling strategy guarantees the size generalization of the model. Given that this is claimed as the core contribution of the paper, it is remarkably brief and covered within 1 small paragraph. A detailed explanation around this will help improve readability. 

3. The design, being based on EGNN, might face issues with large RNAs common in drug discovery due to increasing complexity in both memory and computation. Famously, SE(3)-Transformer (Fuchs et al., 2020), Equiformer (Liao et al., 2022) has been utilized for modeling large molecules such as proteins in models such as AlphaFold, there also have been recent works such as SE(3)-Hyena (Moskalev et al. 2024) using long-convolutional models for equivariant modeling of large-scale systems. Such architectures may directly model all-atom resolution thus providing an alternative to hierarchical modeling at backbone level as described in the paper. Potentially, the authors may consider an ablation study comparing their hierarchical approach to an all-atom model for the largest RNAs in their dataset or may provide a complexity analysis comparing their approach to SE(3)-Transformer, Equiformer and SE(3)-Hyena for large RNA modeling to justify architectural choice.

4. The paper does not seem to explore cases where EquiRNA performs poorly or where errors arise, missing an opportunity to analyze model limitations and provide insights into potential biases or weaknesses in real-world RNA structures. Can the authors provide specific examples where EquiRNA performs poorly compared to other methods or any patterns in the types of RNA structures or features that lead to higher errors?

5. The use of learned atom and nucleotide templates is innovative, but I wonder if this can also hamper generalizability. I imagine that generalizability is partly tied to specific template choices, which might not always capture structural diversity in RNAs. If new RNA structures or variations appear, the model may not capture these well unless it’s retrained or the templates are updated. If the model is reliant on pre-learned templates, it may struggle with RNAs that exhibit novel conformations or atypical atom interactions.

6. Experimental mehods like cryo-EM, X-ray crystallography, or NMR spectroscopy—for obtaining RNA structures—can produce data with resolution limits. This has mentioned in the introduction but I seem to have missed how the model performance changes when applied to   more/less noisy data (in terms of structural resolution).

### Questions
I have posed my questions/concerns in the weaknesses section already. Here is a summary and few suggestions which may help address some of my concerns.
1. Can the authors show how does the model handle variations in RNA structures due to experimental noise or biological variability (performance with different structural resolutions)? Also since noise is common in experimental structure determination/sequencing, can we consider testing the model's performance on RNA structures with simulated noise or structural variability to assess its robustness?
2. How sensitive is the model’s performance to the choice of templates? Is there a risk that template selection introduces bias or limits the generalizability of the model?
3. Has the model been evaluated on a variety of RNA structures, particularly those with unusual or rare structural motifs, to ensure generalizability? 
4. Is it possible to run experiments showcasing the model's ability to truly generalize on large RNA sequences common in drug discovery (many hundreds to thousands of nucleotides), such as those derived from high-throughput sequencing or large RNA viruses?
5. I am not sure how K-nearest neighbor sampling strategy guarantees the size generalization of the model. Can this section be expanded upon?
6. Is it possible to showcase some error cases where the model fails and if that reveals some insights?
7. For the model to be usable and further developments to happen in this space, releasing code and curated datasets will be useful. Can the authors release them?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper presents EquiRNA, a hierarchical Geometric Graph Neural Network model designed for size-generalizable RNA structure evaluation. Addressing challenges in capturing full RNA geometries and generalizing across different RNA sizes, EquiRNA uses a three-level architecture—atom, subunit, and nucleotide—to model RNA’s structural complexity effectively. It introduces a size-insensitive K-nearest neighbor sampling strategy to enhance robustness when generalizing from small to large RNAs, and a new dataset, rRNAsolo, for thorough evaluation. Experimental results show EquiRNA outperforms SOTA methods, providing a robust new baseline for RNA 3D structure prediction and evaluation.

### Strengths
1.	Hierarchical Architecture for Size Generalization: By modeling RNA structure at atom, subunit, and nucleotide levels, EquiRNA effectively captures detailed RNA geometries and adapts well to RNAs of varying sizes, addressing the common challenge of generalizing from small to large RNAs.  

2.	Innovative Sampling Strategy: The size-insensitive K-nearest neighbor sampling enhances robustness by exposing the model to diverse structural variations, allowing better generalization to larger RNAs not seen during training.  

3.	Comprehensive New Dataset: The rRNAsolo dataset, covering a broader range of RNA sizes and types, provides a more rigorous benchmark for size generalization, demonstrating EquiRNA’s superior performance over state-of-the-art methods in real-world scenarios.

### Weaknesses
See Questions.


### Questions
1.	Better to have a figure when explaining the graph structrure in 3.1
2.	In line 53, what’s the definition of “resolution”? Is it the threshold of deciding if there is an edge between two atoms?
How and why to select “resolution higher than 2 A”?
3.	Why don’t use average for $\overrightarrow{\boldsymbol{X}}^{l+2} \in \mathbb{R}^{3 \times\left(N_r+N_b\right)}$, instead of a concatenation?

4.	For atom-level and subunit-level layers, do they apply only on 4 types of nucleotides (AUGC), or each nucleotide respectively?

5.	Line 878 shows the number of layers for both datasets are 3. If I stack Eq. 1, Eq.2, and Eq.3, are they together 1 layer or 3 layers?
6.	Equation 4 is confusing, and I’m not clear with the overall task.  

(1)	The task is to predict RMSD between candidate and native structures. So on RNAsolo’s website (https://rnasolo.cs.put.poznan.pl), the provided structures are ground-truth (native) structures, right? Then what’s the candidate structures and how did you get them? Based on my understanding, there are multiple 3D strucure prediction tools for one RNA sequence, then what are the prediction tools? And, how many candidate structures are compared to the ground-truth structure?  

(2)	In Eq.4, is $\hat{\boldsymbol{h}}_i^{l+3}$ the ground truth label for each nucleotide? How did you get that? I understand the ground truth structure is given by a PDB file, but how was it converted into the ground truth for each nuclotide?   

(3) Why is $\hat{h}_i$ ground truth? Isn't it the feature? If it is ground truth here, then the notation is duplicated.  

(4) Why to use features h to predict final RMSD? Why not X? What’s the function of row 3 in Eq.3 if X is not used?  

I'd appreciate it if the authors can describe the overall task, candidate structures, ground truth labels comprehensively.

7. Eq. 1 and Eq.2 have the similar form with EGNN. The difference is just on different levels (atom level, sub-unit level). Is there any intuition why to use RBF?

8.	Code is not available.

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
4

### Summary
The paper introduces a three-level hierarchical equivariant graph neural network (EquiRNA) designed to efficiently capture the geometries of RNA, enabling it to generalize effectively across a wide range of RNA sizes. EquiRNA demonstrates promising results in evaluating RNA 3D structures.

### Strengths
1.	The proposed hierarchical equivariant graph for RNA structures is novel.
2.	The results on the size generalization dataset are compelling.

### Weaknesses
1.	The paper presents comparisons with several models, but there are other models, such as SphereNet[1], Equiformer[2], MACE[3], and ProNet[4], that show better performance. A more extensive comparison with existing methods would enhance the paper. Although the experimental results highlight the proposed method's effectiveness, a more thorough comparison with other leading models could further substantiate the paper's claims.
2.	A detailed explanation of the implementation of several baselines is needed. For example, RDesign was originally developed for RNA inverse folding tasks and only includes backbone atoms. How was RDesign adapted for RNA structure evaluation in this paper?
3.	While EquiRNA performs well on datasets of RNAs with unseen sizes, its performance on the datasets splitting irrespective of size remains unclear. Furthermore, the method used for splitting the data into training, validation, and test sets is not clearly defined, particularly regarding how structural similarity is handled to prevent data leakage between sets. This lack of clarity makes it difficult to assess the true generalization capability of the model.

### Questions
1.	The paper presents comparisons with several models, but there are other models, such as SphereNet[1], Equiformer[2], MACE[3], and ProNet[4], that show better performance. A more extensive comparison with existing methods would enhance the paper. Although the experimental results highlight the proposed method's effectiveness, a more thorough comparison with other leading models could further substantiate the paper's claims.
2.	A detailed explanation of the implementation of several baselines is needed. For example, RDesign was originally developed for RNA inverse folding tasks and only includes backbone atoms. How was RDesign adapted for RNA structure evaluation in this paper?
3.	The author emphasizes the importance of the size-generalization task but should include an experiment that evaluates dataset splitting independent of size.

[1] Liu, Yi, et al. "Spherical message passing for 3d molecular graphs." International Conference on Learning Representations (ICLR). 2022.
[2] Liao, Yi-Lun, and Tess Smidt. "Equiformer: Equivariant graph attention transformer for 3d atomistic graphs." arXiv preprint arXiv:2206.11990 (2022).
[3] Batatia, Ilyes, et al. "MACE: Higher order equivariant message passing neural networks for fast and accurate force fields." Advances in Neural Information Processing Systems 35 (2022): 11423-11436.
[4] Wang, Limei, et al. "Learning hierarchical protein representations via complete 3d graph networks." arXiv preprint arXiv:2207.12600 (2022).

### Soundness
4

### Presentation
3

### Contribution
3
