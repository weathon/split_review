# RNA FrameFlow: Flow Matching for de novo 3D RNA Backbone Generation

- Decision: Reject
- Avg Score: 5.60
- Scores: 6, 6, 6, 5, 5

## Abstract
We introduce \textsc{RNA-FrameFlow}, the first generative model for 3D RNA backbone design. We build upon $SE(3)$ flow matching for protein backbone generation and establish protocols for data preparation and evaluation to address unique challenges posed by RNA modeling. We formulate RNA structures as a set of rigid-body frames and associated loss functions which account for larger, more conformationally flexible RNA backbones (13 atoms per nucleotide) vs. proteins (4 atoms per residue). Toward tackling the lack of diversity in 3D RNA datasets, we explore training with structural clustering and cropping augmentations. Additionally, we define a suite of evaluation metrics to measure whether the generated RNA structures are globally self-consistent (via inverse folding followed by forward folding) and locally recover RNA-specific structural descriptors. The most performant version of \textsc{RNA-FrameFlow} generates locally realistic RNA backbones of 40-150 nucleotides, over 40\% of which pass our validity criteria as measured by a self-consistency TM-score $\geq0.45$, at which two RNAs have the same global fold.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper introduces a generative model for designing the tertiary structure backbone of RNA, offering a novel approach to structure-based RNA design. The authors establish a set of evaluation metrics to assess the designability and rationality of the generated structures. Experimental results demonstrate that the proposed model can successfully generate reasonable designs for RNA of a certain length.

### Strengths
1.	This is the first generative model specifically proposed for RNA 3D backbone design.
2.	A comprehensive set of evaluation metrics is defined to assess the quality of generated RNA structures.
3.	The flow matching technique, originally applicable only to proteins, is extended to RNA, contributing at the engineering level.
4.	The proposed model demonstrates successful design outcomes on several common RNA types.
5.	The writing logic of the paper is clear and straightforward, making it easy to follow.

### Weaknesses
1.	The paper employs gRNAde for inverse folding to verify the quality of RNA backbone generation from a self-consistency perspective. However, the inherent capabilities and errors of gRNAde may significantly impact this evaluation metric. This should be thoroughly explained and discussed in the paper. Specifically, the paper should discuss the limitations of gRNAde in handling complex RNA structures, its known biases towards certain sequence motifs, and how these limitations might affect the interpretation of the self-consistency results. A more detailed analysis of gRNAde's performance on diverse RNA structures, including those with pseudoknots or non-canonical base pairings, is needed to contextualize the results.
2.	Unlike the protein field, RNA structure prediction accuracy is relatively low, with many challenges remaining. Relying solely on RhoFold for RNA structure prediction may introduce bias. It would be more comprehensive and reasonable to incorporate additional structure prediction models, such as trRosettaRNA and Alphafold3, to demonstrate performance. The paper should acknowledge that RhoFold, while a reasonable choice, may have limitations in accurately predicting certain RNA structural features, such as complex tertiary interactions or flexible regions. Comparing the results with other state-of-the-art methods would provide a more robust assessment of the generated structures.
3.	For the Earth Mover's Distance (EMD) in Table 1, the results of the 50/50 split of the training set should be included as a reference for the numerical scale. The numerical range of EMD varies greatly and is easily influenced by hyperparameter settings. Without this reference, it is difficult to assess the significance of the reported EMD values. The paper should also discuss the sensitivity of EMD to different structural features and how this might affect the interpretation of the results.
4.	From an RNA biology perspective, the current diversity metric is relatively meaningless. A more effective approach might be to explore whether the generated structures encompass diverse RNA types or families (e.g., by calculating structural or sequence similarity), rather than focusing on the most common tRNA and rRNA. The paper should consider using metrics that quantify the structural diversity based on known RNA families or structural classifications, such as those found in the RNA STRAND database, to provide a more biologically relevant assessment of the generated structures.
5.	The current quality assessment of the generated structure includes both global and local geometry, which can be further enhanced by further checking whether the generated RNA structures contain some common tertiary interaction motifs, such as pseudoknots and base multiplets, rather than just base pairing and stacking. The paper should incorporate metrics that specifically assess the presence and quality of these tertiary interactions, as they are crucial for RNA function and stability. This could involve adapting existing tools for identifying such motifs or developing new metrics tailored to the generated structures.
6.	For the case where clashes appear in the generated 3D backbones, there is a lack of quantitative metrics to illustrate the frequency of this phenomenon, such as the average proportion of nucleotides with clashes in RNA. The paper should provide a detailed analysis of the types and locations of clashes, as well as the average number of clashes per generated structure, to better understand the limitations of the method in producing physically realistic structures.

### Questions
Please refer to the details in Weaknesses.

1.	Could you elaborate on the limitations and potential errors of gRNAde that might impact the self-consistency evaluation of backbone generation? How do these factors influence the reliability of your results?
2.	Consider incorporating results from multiple structure prediction models to provide a more comprehensive evaluation of your method's performance.
3.	Include the results of the 50/50 split calculation of the training set as a reference to provide a clearer understanding of the EMD's numerical scale.
4.	Explore whether the generated structures include diverse RNA types or families by calculating structural or sequence similarity to enhance the diversity metric's biological significance.
5.	Enhance the quality evaluation by checking for common tertiary interaction motifs to provide a more comprehensive evaluation of the generated RNA structures.
6.	How frequently do the generated 3D backbones exhibit clashes, and what is the average proportion of nucleotides involved in these clashes?

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper presents RNA-FrameFlow, a novel generative model tailored to design de novo 3D RNA backbones. Building on SE(3) flow matching methods developed for protein backbone modeling, the authors introduce an adapted framework to accommodate RNA’s structural flexibility, characterized by 13 backbone atoms per nucleotide versus the typical four in proteins. They establish a protocol for handling RNA-specific challenges like limited 3D structural data, which they address with structural clustering and augmentation. Evaluation includes newly defined metrics for assessing the self-consistency and structural fidelity of generated RNA backbones. RNA-FrameFlow outperforms baselines like MMDiff in validity, diversity, and sampling efficiency, showing potential in RNA structural modeling.

### Strengths
1. Adapting the SE(3) flow matching approach to RNA is novel and technically complex. The model navigates challenges in structural flexibility and the need for RNA-specific design by introducing RNA-tailored frame parameters and torsion-based atom placement.

2. Development of comprehensive evaluation protocols for RNA backbone generation, including both local and global structural metrics.

3. Figures, particularly those explaining the RNA frame, frame transformations, and evaluation metrics, effectively illustrate the approach and results. The structural consistency and Ramachandran-like angle plots are insightful, showing the model’s fidelity in RNA structural features.

### Weaknesses
1. The model’s training set, derived from a limited pool of 3D RNA structures, restricts RNA-FRAMEFLOW’s generalization to less frequent RNA folds. While clustering and cropping augmentations aim to mitigate this, they lead to a decrease in sample validity. Additionally, over-represented lengths like those common to tRNA and 5S rRNA may cause the model to rely on memorized structural features, limiting its novelty in unseen scenarios. The cropping augmentation, in particular, may introduce unrealistic structural contexts at the cut points, further hindering the model's ability to generalize to novel folds. This is because the local geometry at these cut points may not be consistent with the global fold, potentially leading to the generation of structures with physically implausible conformations.

2. The evaluation pipeline uses RhoFold for forward folding, but RhoFold’s length bias favors structures with specific lengths, potentially skewing evaluations for other sequence lengths. The reliance on scTM and pdbTM as primary evaluation metrics may thus disproportionately favor over-represented sequence lengths, and alternative, less biased evaluation methods could improve fairness. The use of scTM and pdbTM, which are alignment-based metrics, may also not fully capture the structural diversity and novelty of the generated RNA backbones, as they are more sensitive to global structural similarity rather than local variations or novel folds.

### Questions
1. How might explicit modeling of RNA base pairing and stacking interactions (e.g., incorporating hydrogen bonding) impact RNA-FRAMEFLOW’s ability to produce realistic structures?

2. Given the length bias of RhoFold, do the authors have plans to explore alternative evaluation tools that might yield less length-biased results?

3. Could the clustering and cropping data augmentation methods be adjusted to avoid introducing invalid folds? How might alternative data augmentation methods improve diversity without sacrificing validity?

### Soundness
3

### Presentation
4

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
This paper proposes RNA-FrameFlow, a flow matching framework for RNA backbone generation. The authors utilize three key atoms to determine the frame of each nucleotide, and leverage the FrameFlow[1] method with proper auxiliary losses to generate 3D backbone structures. The authors establish a generation pipeline for benchmarking the performance of RNA generation models, and results demonstrate the proposed models' capability to yield valid backbone structures with specific lengths.

[1] Yim, Jason, et al. "Fast protein backbone generation with SE (3) flow matching."

### Strengths
1. This paper focuses on a novel problem of RNA backbone generation, and is the pioneer to represent RNA structures as frames.
2. The experiments are thorough. Notably, the paper provides a detailed exploration of the limitations, offering insightful analyses and preliminary solutions. This openness about current challenges reflects a constructive effort toward advancing the field, even if these issues remain to be fully resolved.

### Weaknesses
1. For the evaluation pipeline, self-consistency scores could be affected by cumulative errors introduced by the inverse folding and structure prediction models. To better understand the potential limitations, it would be helpful to estimate an upper bound for this pipeline. One approach could involve sampling a similar distribution of structures from the test set and computing self-consistency scores using the inverse folding–structure prediction pipeline.
2. As the model may exhibit bias toward common patterns in the training set (tRNAs or 5S ribosomal RNAs), it would be beneficial to provide the training distribution and compare it with the TM-score distribution across different sequence lengths for better analysis.

### Questions
1. Does the selection of frame atoms involve some rigid assumptions? If so, how do these assumptions impact the results, and are there comparisons with other possible selections?
2. Could you provide the average scTM for each method in addition to the validity metrics? The validity may be sensitive to the chosen threshold (0.45).

### Soundness
4

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
4

### Summary
This paper is the first to apply frameflow for RNA backbone generation, designing the structure of RNA. It also provides comprehensive experiments and reasonable analysis.

### Strengths
This is the first paper to utilize frame flow for designing the RNA backbone. It also includes a complete experimental section.

### Weaknesses
Main Weaknesses:

1. The innovation in the methodology section is limited. It applies frame flow to the backbone design of RNA. However, the application of frame flow to RNA design, in my view, lacks novelty, as frame flow is a model for generating frames (although the authors only provide experiments with proteins), and RoseTTAFoldNA has already offered a method to represent RNA as frames. Therefore, applying frame flow to RNA seems like a combination and does not appear to be a significant enough contribution to serve as the primary innovative point for a top-tier conference paper; it could only be considered a minor innovation and a baseline. However, this paper presents it as the main innovation. I think this paper needs to highlight some other insights, such as what problems arise when applying frame flow to RNA and how they should be addressed. The paper does indeed point out some insights, like how to address the issue of insufficient data and how to represent RNA as frames. However, I have questions about these insights. First, the lack of 3D structural data for RNA is a well-known problem [1], and it is not an insight. To solve this problem, the authors propose data augmentation methods, such as Structural clustering and Cropping augmentation. But these Structural clustering[3] and Cropping augmentation[2] are very common [2,3] and cannot be considered major insights or innovations.

[1] RDESIGN: HIERARCHICAL DATA-EFFICIENT REPRESENTATION LEARNING FOR TERTIARY STRUCTURE-BASED RNA DESIGN

[2] AlphaFold3 & AlphaFold2

[3] SE(3) diffusion model with application to protein backbone generation

2. Another innovation in the methodological part is their proposal of a way to characterize RNA backbones as frames. However, I find this questionable. First, in RoseTTAFoldNA, a method to characterize RNA backbones as frames has already been proposed, and it is highly similar to the one presented in this paper. Therefore, this paper is not the first to propose such a method. Second, while RoseTTAFoldNA constructs frames based on the phosphate group (P, OP1, and OP2), this paper bases its construction on C3′−C4′−O4′. However, the authors do not provide compelling reasons or experimental results to demonstrate that choosing C3′−C4′−O4′ is a superior option. The authors do mention in the paper that C3′−C4′−O4′ is more centrally located. Nevertheless, even so, I do not think this would lead to a significant improvement in model performance, as it essentially just adds a fixed offset to the RNA, and neural networks should be capable of fitting this offset. Thus, I do not consider this a valid innovation. If, however, the authors can provide experimental results showing that using C3′−C4′−O4′ over P, OP1, and OP2 significantly enhances the model's performance, along with a compelling analysis of the underlying reasons, I would be willing to regard this as a major innovation.


Minor Weaknesses:
To my knowledge, the reliability of RNA structure prediction results is not as high as that of protein structure predictions. As a result, although the experimental outcomes have some reference value, they are not very precise. Of course, I understand this is a difficult issue to resolve, and my evaluation of this paper does not hinge on this point. This issue has a minimal impact on my rating of the paper, and the authors can disregard it. I am merely pointing out this objective fact in the interest of rigor. It would be better if the authors could provide additional experimental data, such as some molecular dynamics software that can now estimate RNA energy, which would also serve as a helpful evaluation tool.

### Questions
See weaknesses

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper introduces RNA-FRAMEFLOW, a novel generative model designed for de novo 3D RNA backbone generation. The model adapts SE(3) flow matching, previously used for protein backbone design, to handle RNA's structural complexities. RNA-FRAMEFLOW represents RNA backbones using rigid-body frames and leverages auxiliary losses to enhance training effectiveness. The model incorporates several evaluation metrics to ensure self-consistency and structural realism. Additionally, it introduces novel data preparation strategies to enhance both the diversity and novelty of generated RNA structures.

### Strengths
1.	Successfully adapts SE(3) flow matching to RNA, addressing RNA’s complex and flexible conformations.
2.	It achieves a validity rate of 41%, indicating good global and local structural accuracy.
3.	Implements techniques like structural clustering and cropping augmentation to enhance training diversity, partially addressing the scarcity of 3D RNA datasets.
4.	Compared to diffusion models like MMDiff, RNA-FRAMEFLOW generates RNA backbones more quickly, making it more efficient in practical applications.

### Weaknesses
1.	The cropping strategy, meant to increase dataset diversity, can introduce unrealistic subsequences that may not fold correctly, reducing the validity of generated structures. Specifically, the arbitrary cropping of RNA sequences might disrupt essential long-range interactions necessary for proper folding, leading to structures that are not physically plausible. This is a significant concern as it undermines the reliability of the generated structures.
2.	The reliance on folding and inverse-folding models, which have their own biases,  affects RNA-FRAMEFLOW’s overall performance and the validity of generated designs. The inherent limitations and biases within these models, such as the tendency to favor certain conformations or misinterpret specific sequence patterns, can propagate through the generation process, leading to inaccuracies in the final RNA structures. This dependence introduces a potential source of error that needs careful consideration.
3.	It would be beneficial to include more detailed results on the generation process (see Q1). For example, the analysis of the convergence of the flow matching process and the distribution of generated structures would provide valuable insights into the model's behavior and reliability.
4.	Further ablation studies could be conducted to evaluate the impact of the proposed auxiliary losses on model performance (see Q2). Specifically, a more granular analysis of how each loss term contributes to the overall validity, diversity, and novelty of the generated structures is needed. This would help in understanding the relative importance of each loss and potentially lead to further optimization.
5.	The scTM only reflect the self-consistency of C4’ atoms, other atoms should be also compared (see Q3). The current metric does not fully capture the rotational and angular accuracy of the generated structures. A more comprehensive evaluation should include the analysis of the relative positions of all backbone atoms.

### Questions
1.	As the number of timesteps increases, the performance in terms of validity, diversity, and novelty decreases. Could you analyze how the number of sampling steps impacts the quality of the generated samples?
2.	Could you conduct ablation studies to demonstrate how the added auxiliary losses contribute to performance improvements?
3.	The C3’ atom primarily reflects the accuracy of translational performance, while the aspects of rotations and angles are not assessed by the current validity metric. Could you compute the RMSD between the generated structure and the folded structure for a more comprehensive evaluation?

### Soundness
3

### Presentation
3

### Contribution
3
