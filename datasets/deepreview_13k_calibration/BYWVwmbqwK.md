# Unpaired Single-Cell Dataset Alignment with Wavelet Optimal Transport

- Decision: Reject
- Avg Score: 5.00
- Scores: 5, 5, 5, 5

## Abstract
Aligning single-cell samples across different datasets and modalities is an important task with the rise of high-throughput single-cell technologies. Currently, collecting multi-modality datasets with paired samples is difficult, expensive, and impossible in some cases, motivating methods to align unpaired samples from distinct uni-modality datasets. While dataset alignment problems have been addressed in various domains, single-cell data introduce additional complexity including high levels of noise, dropout, and non-isometry between data spaces. In response to these unique challenges, we propose Wavelet Optimal Transport (WOT), a multi-resolution optimal transport method that aligns samples by minimizing the spectral graph wavelet discrepancies across datasets. Filters are incorporated into the optimization process to eliminate non-essential scales and wavelets, enhancing the quality of correspondences. We demonstrate the capacity of WOT in highly noisy and non-isometric conditions, outperforming previous state-of-the-art methods by significant margins, especially on real single-cell datasets.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The authors propose a new method, "Spectral Graph Wavelet Optimal Transport" (WOT), to align unpaired single-cell multi-omic datasets. To do so, they perform Gromov-Wasserstein OT alignment between two domains (-omic measurement types) but unlike existing methods, intra-domain distances are computed based on spectral graph wavelets in order to capture multi-scale structural information on the graphs constructed on each modality. They include scale-varying filters in their framework in order to filter out uninformative signals (or noise). There are two proposed strategies for choosing filters: (1) heuristically choosing them based on the entropy of the wavelets in each scale, as estimated based on kernel density estimation and (2) learned via an alternating optimization procedure, where the transport plan and the filters are alternatingly optimized via Sinkhorn iterations and stochastic gradient ascent, respectively. 

Overall, the approach is well-motivated and the proposed method is novel. While computational complexity is a challenge, experiments demonstrate the benefits in non-isometric and noisy settings. However, I have several remaining questions after reading the paper, especially around how these experiments and baselines are set up. Most importantly, the lack of sufficient information around the hyperparameter selection worries me about the fairness and quality of benchmarking experiments. My current score of 3 is mostly based on this. I am happy to update my score and recommend acceptance if the authors satisfactorily address this concern in the discussion period.

### Strengths
The paper is well-written (other than missing details) and easy to follow and the problem is well-motivated. Experimental section includes a number of simulated and real-world datasets that cover a mix of scenarios and the results are compared to relevant baselines.

### Weaknesses
 **Updated Review** After the rebuttal process, seeing the description of the unsupervised hyperparameter tuning procedure, I am updating my score from 3 to 5, as it partially addresses my concern from #1 below. Having said so, it appears that the hyperparameter tuning procedure does not account of hyperparameters like \rho, which will matter in real-world unpaired dataset integration, as these datasets tend to contain disproportionate cell type representation. Overall, while I think the authors make a contribution towards improving OT-based single-cell multi-modal data alignment (a challenge with scientific impact), I believe additional work needs to be done on **real-world unpaired datasets** before wrapping up this work. 
I keep my original review below for reference.

**1.** The largest concern I have with this submission is the lack of information around hyperparameter selection in benchmarking experiments. The proposed method has a high number of hyperparameters that require tuning: 
- (1) choice of k for the initial kNN graph, 
- (2) the bandwith \sigma for the RBF kernel that forms the weighted adjacency matrices, 
- (3) scale parameters [0...S], 
- (4) \epsilon for the entropic regularization of OT, 
- (5) choice of aggregation function {min, max, sum}, 
- (6) choice of wavelet generating function g {low-pass heat kernel, tight-frame Meyer kernel, ...}, 
- (7) the hyperparameters associated with the chosen g function,
- (8) threshold variable \delta for L-WOT, 
- (9) hyperparameters associated with KDE for E-WOT (bandwidth). 

The authors emphasize that the experiments are conducted in "fully unpaired scenario, where **we don't have validation data to conduct hyperparameter tuning**". Then, in Appendix C, they report different sets of hyperparameters for each dataset. If the experiments weren't conducted with default parameters (i.e. default changes based on dataset) but neither was any validation data was used, then how were different sets of hyperparameters chosen for each dataset? Is there a heuristic / self-tuning procedure to adopt hyperparameters to each dataset without tuning with validation data? This information is lacking. I looked at Appendix C1 on "Guidance on Choosing Hyperparameters" but it does not explain the experiments: it describes keeping aggregation function fixed as summation while reported hyperparameters use a range of aggregation function and secondly, the only heuristic described for self-tuning is from Demetci (2022b), which would only account for k and \epsilon, leaving many other hyperparameter to tune. If there was a self-tuning procedure used, this would be crucial to describe in the paper. The results they compare against uses default parameters for UnionCom, Pamona, MMD-MA, Seurat, bindSC and a self-tuning heuristic for SCOT, SCOTv2 and cross-modal AE. If hyperparameters of E-WOT and L-WOT were, in fact, tuned using data from the experiments, then the correct numbers to compare against would be Fig 2 results from Demetci (2022a):

|   |SCOTv2 | SCOT | UnionCom | Pamona | MMD-MA | Cross AE | BindSC | Seurat |  
| ---- |  ----  |  ----  |  ----  |  ----  |  ----  |  ----  |  ----  |   ----  |  
**SNARE-seq** | 0.927 | 0.982 | 0.423 | 0.686 | 0.942 | 0.689 | 0.734 | 0.684 |  
**scGEM**      | 0.643 | 0.576 | 0.582 | 0.651 | 0.588 | 0.523 | 0.449 | 0.423 |  

**2.** (Minor point) I think the discussion of previous methods not explicitly reducing noise is not entirely accurate: "[previous methods] do not explicitly reduce dataset-intrinsic noise or signal". E.g. UnionCom, Pamona, SCOT, SCOTv2 all use kNN graphs (using only connectivity or Euclidean distance between PCs) on dimensionality-reduced data, which would reduce noise, albeit in a much more naive way than the proposed method here. Cross-modal autoencoders align datasets in a smaller latent space learned by autoencoders, which would be expected to have lower noise level, as well.  

I have other questions and comments below, but the major questions I have are in point #1 above.

### Questions
**1.** How were the hyperparameters of SCOT, SCOTv2, UnionCom and Pamona chosen for the SHREC20 experiments? What were these hyperparameters? 
**2.** What does "Multiple" mean for "Wavelet" parameter in Appendix C? How do you choose the set of scales?
**3.** When computing the kNN graph, what representation of data is used for single-cell datasets? Is it the raw gene expression data, normalized data, or some dimensionality-reduced version of the data? If it's dimensionality reduced, is it based on PCA, LDA, tSNE etc? Do you consider Euclidean distances or correlation or a different 
**4.** What discrepancy measure do you use for L in Equation 4?
**5.** For the GW baseline used in bifurcation matching experiments, how are the intra-domain distances computed (i.e. what is the choice of d_A and d_B used from Eq 1 for this experiment)? Why are single-cell alignment baselines excluded from this experiment?
**6.** Have you attempted to compare methods in settings with validation data? Is the advantage from having a better self-tuning procedure or do you also outperform existing methods when validation data is available?

These are less major questions than the ones in weaknesses section but answers to 1-5 would be good to include in the paper for completeness and replicability.

### Soundness
2

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
The authors present Wavelet Optimal Transport (WOT) based on spectral graph wavelets to align different single-cell datasets, which can be challenging due to noise, dropout, and batch effects. By introducing two versions of WOT, namely L-WOT and E-WOT, the authors demonstrate that these methods are collectively better the the state-of-the-art methods on two simulation and two real single-cell datasets.

### Strengths
The authors address important problem of aligning unpaired single-cell datasets, which seems to not have been addressed in the literature previously. While many unpaired methods exist in different applications, such as image-to-image translation as the authors rightly point out, single-cell context requires additional careful considerations. The mathematical details are thorough and the algorithm itself is familiar to the literature, as it relies on projected gradient descent and/or alternating minimization schemes. I think when the paper is put in right format and much more user-friendly writing style, it will be a great contribution to the community

### Weaknesses
The biggest weakness of this paper is the **presentation**. I read it through multiple times and it was still quite confusing and not sure who the audience is. This is clearly not going to be the computational biology practitioners as the paper is too technical without providing connections and insights sufficiently to the single-cell applications. It felt as though the authors had the idea of WOT on spectral graph wavelets first and then tried to find for some relevant applications afterwards, which led to awkward connections. The experiments felt a bit rushed in that the main highlights (Section 4.3) are only dedicated half a page, without clear and thorough investigations on why the WOT algorithms might be performing better (I also didn't like the practice of "taking" the numbers from other papers).

- It was not clear what alignment of "unpaired" single-cell dataset would actually mean. What would be the use case for this, how would biologists benefit from such alignment for scientific research? For image-to-image translation, yes there are clear reasons, but for alignment of single-cell dataset, it was not so clear from the paper
- The authors need to keep referring back & connecting to the single-cell example/application throughout the presentation of the algorithm. Section 3 is almost entirely separated from the single-cell application, and it is unclear how these two are related. For instance, the "scale" is discussed a lot in the algorithm, but what does scale actually mean in single-cells? The wavelets can provide a basis for decomposition in spectral & temporal domain, but what does it actually mean for single-cell images?
- I think the experimental results are not presented in reader-friendly manner. The evaluation metrics keep changing (geodesic, label transfer accuracy), which the practitioner not familiar with them would have hard time understanding - What do each of these metrics really tell you? Wouldn't it be also important to discuss what filters are used and learned for L- and E-WOT in these real-world examples? What do each of baseline in real-world example do (SCOT, UNIONCOM, etc..) and how/why WOT methods are better as we see in the table?
- "L-WOT performs much better than E-WOT and existing methods on the scGEM while the inverse is seen in SNARE-seq. A potential reason for this difference is that scGEM profiles cells in dedifferentiation, so the boundaries of cell types are not as clear as those of SNARE-seq ~" => This feels like scratching the surface and not really getting at the reason why one might perform better than the other
- Some illustrative (quantiative and qualitative) figure on the experiment results for 4.3 would be informative.

All in all, the authors should focus much less on the mathematical underpinnings but focus more on biological aspect for this to be a valid contribution to the community.

### Questions
- The simulation dataset seems to have dimension of from 1,000 to 2,000, but the real-world single-cell datasets remain at 10~30. Could you explain if this is common combination and how this might affect the algorithm?

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper introduces the Wavelet Optimal Transport (WOT) method, a framework for aligning unpaired single-cell datasets from different modalities. WOT leverages spectral graph wavelet coefficients to capture multi-scale relationships within data and improve alignment robustness against noise, dropout, and non-isometric between data spaces. The authors present two implementations: E-WOT, using entropy heuristics to filter out irrelevant scales, and L-WOT, which dynamically learns the filters to improve alignment adaptivity. Experiments further demonstrate the WOT's superiority in both simulated and real scenarios.

### Strengths
1. Empirical Effectiveness. WOT consistently outperforms SOTA methods in high-noise scenarios, non-isometric conditions, and dropout cases across synthetic and real single-cell multi-omic datasets.
2. Theoretical Novelty. Using spectral graph wavelets for multi-resolution dataset alignment offers a novel view, and further theoretical rigor by generalizing GW-OT and ensuring robustness.
3. Flexibility. WOT allows different filters and optimization strategies to enhance performance based on dataset-specific characteristics.

### Weaknesses
1. Few misspellings in the main text (e.g., in line 012, 'throughput' should be 'throughout').
2. Figure 1 lacks clarity in illustrating both the task and framework.
3. Lack of comparisons with more recent single-cell paired alignment methods such as Harmony and scDML. They are the most common methods for single-cell alignment and deserve to be discussed. Additionally, the description of the weakness of related works in Section 2.1 remains for more detailed analysis about these methods.
4. The study lacks a broader range of experimental scenarios involving real single-cell multi-omic datasets. Results would be more convincing with diverse single-cell multi-omic datasets from different tissues and sequencing technologies, to demonstrate the method's effectiveness across various empirical conditions.
5. The proposed method is designed for two datasets' alignment, which restricts its applicability when aligning multiple datasets simultaneously. In fact, alignment of multiple samples may be a more common scenario.
6. The fixed hyperparameter setting is limited in applicability across real scenarios. Although the authors provide some advice in hyperparameter selection, utilizing an adaptive strategy is encouraged. Furthermore, even if it is difficult to give an adaptive strategy, sensitivity analysis of hyperparameters should be provided to show that this method can achieve good performance in most cases.

### Questions
1. In Sections 4.1 \& 4.2, task-specific baseline methods should be included.
2. How does your framework handle high-dimensional single-cell datasets? Common single-cell dataset dimensions are above 20K. Even if feature selection is performed, the most common input is 1-3K genes.
3. In Figure. 8, I can see that this method can keep the cell types separate. But I am more confused whether the SNARE-seq and ATAC-seq data have been mixed together successfully (need to color based on the dataset).
4. It seems to me that this method is generally applicable, and I wonder why it should be limited to the alignment of single cells? In fact, I think that if this method cannot effectively solve the problems unique to single-cell alignment, such as alignment of high dimensions and multiple datasets, it would be better to use public datasets for comparison and emphasize the general applicability of this method.

### Soundness
3

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
3

### Summary
This paper introduces Wavelet Optimal Transport (WOT) for aligning unpaired single-cell datasets across different modalities. The core contribution lies in using spectral graph wavelets to decompose dataset signals into multiple scales and using filters during optimal transport. The authors propose two variants: E-WOT (entropy-based filtering) and L-WOT (learned filtering). This framework is claimed to generalize Gromov-Wasserstein and shows better performance on noisy data alignment tasks. Various experiments are performed on synthetic data, shape correspondence tasks, and real single-cell multi-omics datasets.

### Strengths
S1: The paper addresses a well-motivated problem (dataset alignment in single cell technologies). The proposed method outperforms many baselines in several setups.

S2: Multi-scale aggregation is a valid approach which has connections to Gromov-Wasserstein under specific conditions (Remark 1). The framework itself is general enough to allow a broad design space with many things to tune for improved performance (kernels, filter, scale aggregation, graph construction...)

### Weaknesses
W1: From a high-level perspective, the method combines established concepts (SGW and Gromov Wasserstein with filtering approaches). While the combination is novel, there appears to be limited theoretical development to help understand why and when the approach works well. Additionally, there are multiple moving parts that would benefit from a more detailed ablation study to shed light on different design choices. For instance,

a) Comparing at multiple scales is the primary motivation for this approach. I think it would be helpful to show (e.g., in experiments) which scales are most relevant and how much they contribute to performance. This is particularly important given the non-negligible performance variability between different WOT variants. In some experiments, E-WOT and L-WOT show varying performance (sometime underperforming some baselines). Without understanding this variability, it is challenging to predict when WOT will outperform existing methods or which variant to use.

b) This may be a minor point, but there are limited discussions of when to use which aggregation method (sum, max, potentially other weighting schemes) and how this choice affects results. The paper lacks a clear rationale for choosing between sum and max aggregation, and it's unclear how these choices interact with the filtering approach and scale selection. For example, does max aggregation emphasize the most informative scale, or does it introduce instability by focusing on a single scale? A more thorough investigation into the impact of different aggregation methods is needed.

The overall impression is that there are many tunable components (scale selection, filtering approach, aggregation method, kernel choice) without sufficient guidance or understanding of their interactions.

W2: a) L-WOT may require some discussion on when or whether it converges at all. The optimization landscape for L-WOT is complex, involving a bilevel optimization with non-convex inner and outer loops. The paper lacks a discussion on the convergence properties of the learned filters, and it's unclear if the reported results are stable or sensitive to initialization. b) Is entropy always a good heuristic to emphasize informative scales? Using KDE with tunable bandwidth seems to introduce further complexity (in the Appendix, the authors report fixing Gaussian KDE bw at 0.4; have the authors considered adaptive bandwidth like Scott's or Silverman's?) The choice of a fixed bandwidth for KDE is not well-justified, and it's unclear how sensitive the entropy calculation is to this parameter. The paper should explore the impact of different bandwidth selection methods on the performance of E-WOT.

W3: It is not clear whether the experiments exclusively use the Chebyshev polynomial approximation. The paper would be strengthened if there is some analysis/comparison between the Chebyshev approximation vs the exact computation to provide some understanding of the trade-off between speed and performance. The paper should provide a more detailed discussion on the accuracy of the Chebyshev approximation, especially when using a limited number of polynomial terms. It would be beneficial to see a comparison of the computational cost and accuracy between the approximation and the exact computation to better understand the practical implications of this choice.

W4: I think that runtime/memory benchmarking for all methods should be discussed more thoroughly (beside what is provided in Appendix E). What are the runtime for each method in each experiment? Moreover, constructing large, fully-connected graphs is expensive. It helps to understand the computational/memory cost when evaluating different methods for practical applications. The paper should provide a breakdown of the computational cost for each step of the algorithm, including graph construction, wavelet decomposition, and optimal transport. This would help to identify the bottlenecks and provide a more comprehensive understanding of the method's scalability.

### Questions
Q1: Why is this work not positioned as a general framework for handling noisy, non-isometric spaces (many of which the authors leave as future directions)? Are there inherent limitations to it when applied to other domains? It is true that single-cell data provides an important application, but if the method is more general then I think it may be a good idea to broaden the experiment settings to truly evaluate its effectiveness against other baselines.

Q2: The authors state they cannot conduct hyperparameter tuning due to the unpaired setting (with some related details in Appendix C), is this a standard practice to pretend we don't have ground truth for tuning in these domains? Since there are many things to tune, how practical is the approach compared to the baselines? If we would like to avoid falling back to using heuristics, then how common is prior scale knowledge in practical settings? (In the paper, the authors cite Deutsch et al. (2016) but it seems generic and is not clear what scale is considered noise since there are no relevant experiments)

### Soundness
2

### Presentation
2

### Contribution
2
