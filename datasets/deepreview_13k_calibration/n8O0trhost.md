# cryoSPHERE: Single-Particle HEterogeneous REconstruction from cryo EM

- Decision: Accept
- Avg Score: 6.67
- Scores: 6, 8, 6

## Abstract
The three-dimensional structure of a protein plays a key role in determining its function. Methods like AlphaFold have revolutionized protein structure prediction based only on the amino-acid sequence. However, proteins often appear in multiple different conformations, and it is highly relevant to resolve the full conformational distribution.
Single-particle cryo-electron microscopy (cryo EM) is a powerful tool for capturing a large number of images of a given protein, frequently in different conformations (referred to as \textit{particles}). The images are, however, very noisy projections of the protein, %and recovering the full distribution over conformations is extremely challenging. 
and traditional methods for cryo EM reconstruction are limited to recovering a single, or a few, conformations.
In this paper, we introduce cryoSPHERE, a deep learning method that takes as input a nominal protein structure, e.g. from AlphaFold, learns how to divide it into segments, and how to move these as approximately rigid bodies to fit the different conformations present in the cryo EM dataset. This formulation is shown to provide enough constraints to recover meaningful reconstructions of single protein structures. This is illustrated in three examples where we show consistent improvements over the current state-of-the-art for heterogeneous reconstruction.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The authors introduced a new method, cryoSPHERE, that resolves the continuous heterogeneity problem in cryo-EM reconstruction. Similar to some other methods, cryoSPHERE uses an atomic model as the input, makes segmentations, and uses the results as the regularization in finding the flexible movement in the cryo-EM dataset.

### Strengths
Instead of finding the deformation for each residue, cryoSPHERE learns a segmentation of the amino acid or nucleotide chains and deforms the segment to fit the heterogenous cryo-EM data. This is indeed a valid assumption in many cases especially for large complexes  like the spliceosome (EMPIAR-10180).

### Weaknesses
Major:
1. CryoSPHERE uses an atomic model as the reference and formulates the conformational heterogeneity in cryo-EM data as the deformation of segments of the reference model. The approach to finding optimal segments is similar to that used in e2gmm, where a Gaussian Mixture Model (GMM) with N_{segm} components is fitted. This segmentation is then used in a cryoSTAR/DynaMight-like setting, replacing regularization losses and computing predicted projections for comparison with particle images. The authors should provide a more detailed comparison with other similar methods, including DynaMight, e2gmm, and 3DFlex, discussing the specific differences in methodology and outcomes, rather than just stating they are similar.

2. Density maps are crucial for evaluating the validity of cryo-EM results. The authors only present density maps for one synthetic dataset. Given the hypothesis that heterogeneity is modeled as deformations of a canonical density, it is essential to demonstrate that the reconstructed canonical density is free from artifacts, especially for real datasets. The absence of such analysis for real data is a significant weakness.

3. The FSC comparison in Sec. 5.2 between cryoSPHERE and cryoDRGN and cryoSTAR is potentially misleading. CryoSPHERE's density is reconstructed under the assumption of a canonical density, while cryoDRGN does not make this assumption, and cryoSTAR explicitly avoids it to reduce bias. A more appropriate comparison would be against methods like DynaMight and 3DFlex, which also model deformations of a reference structure. The current comparison does not fairly assess the method's performance against relevant alternatives.

4. The lack of an ablation study is a significant oversight. The authors should investigate and discuss how N_{segm}, a key hyperparameter controlling the degrees of freedom in segmentation, affects the results on both synthetic and real data. This analysis is essential for understanding the method's sensitivity to parameter choices and its robustness.

5. The authors compare cryoSPHERE to cryoDRGN and cryoSTAR, but the experiments do not clearly demonstrate the advantages of cryoSPHERE. The only apparent advantage is an increase in FSC resolution, but this is only shown for one synthetic dataset. It is unclear what unique benefits cryoSPHERE provides over existing methods, especially given the limitations of the comparison.

Minor:
1. The sequence of Fig.6 and Fig.7 in the paper is reversed.
2. In the related works, e2gmm should also be considered as a method using deep learning.
3. In the FSC comparison, if not comparing two half maps, the cutoff of 0.5 should be used, and 0.143 is not meaningful. See [1] appendix for the reason (and also why 0.143 is the number widely used for half maps comparison). Therefore, the discussion at the end of Sec. 5.2 about 0.5 and 0.143 cutoff improvement is not very correct.
4. The writing could be better polished.
5. I do not think the "Ethics Statement" content is proper as it lacks evidence.

### Questions
Can the authors elaborate how the density maps (volumes) are reconstructed in cryoSPHERE (like in Fig. 6)? I understand how backprojection in cryo-EM works, but still find it difficult to understand how this is performed exactly.

### Soundness
2

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
4

### Summary
- The authors propose a VAE and GMM-based approach to atomistic heterogeneous Cryo-EM reconstruction
- The GMM part learns how to divide the amino acid chan in segments
- The VAE learns how to encode images into latent variables and decode these variables along with the GMM output into segment-wise conformational changes
- The authors claim that their method overcomes current challenges that atomistic models face, while also achieving improved interpretability by learning these segments (that ideally correspond to domains in the biological sense)

### Strengths
The work is of high quality and overall very well-written. I’d like to highlight the following strong points of the paper:
- The authors seem very well aware of the difficulties atomistic models have in terms of the optimisation landscape and address the problem adequately by regularising while keeping sequential information intact
- The authors give useful biological remarks such as that their methods seems to recover domains, which is useful to know as a practitioner
- The authors show that their method works on real data, which is actually the first time I’ve read this for atomistic models

### Weaknesses
There is one main weak point in the paper in my regard:
- The authors do not address limitations of their method very thoroughly:
    - whether or not their method is able to overcome poor initialisation of the initial structure S_0. This is one of the major risks of working with (pseudo)-atomistic models as shown in works such as DynaMight (Schwab et al. 2024) 
    - Whether or not local physical information such as bond lengths between atoms at the boundaries of the segments is preserved. This might be challenging

### Questions
Questions for clarification 
- In section 3.6 the authors say “Similar to Li et al. (2023), instead of using a mean squared error loss between the predicted and ground truth image, we use a correlation loss between the true and predicted image”. However, they do not motivate this choice. Would you please care to elaborate?
- In section 5.1 the authors write “Testing the segment decomposition, we then run cryoSPHERE by requesting division into Nsegm = 4. The program learnt a first and third segment with 0 residues, a second segment with 1353 residues and a fourth segment with 157 residues (Figure 5). Thus, cryoSPHERE learnt segments according to the ground truth.” Is there a reason why we should expect that the model prefers to learn two segments?

Additional feedback
- It reads as if equation 7 is the only loss that is being used. I assume that the VAE latent distribution is also trainable? It would benefit the readability if the authors clarify whether the loss is just the decoder loss or the whole loss.“
- In section 5.3 the authors write “The first two principal components explain more than 96 percent of the variance.” In general, I would be very reluctant to make any claims about PCA in the latent space as you could come up with a transformation that scrambles the latent space and still gives the same decoding, but covers much less variance. I can imagine that Figure 7 is a nice illustration, but I would recommend to leave it with that.

### Soundness
3

### Presentation
3

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
This paper introduces cryoSPHERE, a deep learning model that uses nominal protein structures (e.g., from AlphaFold) to break proteins into segments and fit these segments to various conformations in cryo-EM data.

### Strengths
1. The approach of learning to decompose the protein’s amino acid chain into segments to represent various conformations is novel.
2. The interpretability of moving part is highly beneficial for practitioners, offering a clearer understanding of conformational dynamics.

### Weaknesses
1. No meaningful improvements were observed over CryoStar
    - Figures 3, 12, 13: It’s unclear what meaningful differences exist compared to CryoStar. The FSC curves appear very similar, and the visual differences in the fitted structures are not substantial enough to justify the method's complexity. A more rigorous quantitative analysis of the fitted structures, beyond FSC, is needed to demonstrate any advantage.
    - Figures 14, 21: There doesn’t appear to be a significant difference between CryoStar and CryoSphere (CryoStar may even appear better). The slight variations in the fitted structures could be due to random initialization or optimization artifacts rather than a genuine improvement in fitting accuracy. It is crucial to show statistically significant improvements, perhaps through multiple independent runs and reporting of standard deviations.
    - Figure 29: It would be great to compare CryoStar with CryoSphere rather than with CryoDRGN. The comparison with CryoDRGN is not directly relevant since CryoDRGN is a different type of method, and the goal here is to assess the improvement over the most similar method, CryoStar.
2. Should change Figure 6:
    - Instead of showing only CryoDRGN results and G.T, a comparison with CryoSTAR or Dynamight would be more appropriate (perhaps include Figure 32 and the CryoSphere result, as there are no CryoSphere results with SNR 0.001). The current figure does not provide a fair comparison with other structure fitting methods. It's important to show how CryoSphere performs against the state-of-the-art methods in the low SNR regime, which is a critical test for any cryo-EM structure fitting algorithm.

### Questions
Could you include additional comparisons with methods like CryoSTAR, or Dynamight (e.g., computational cost, novelty, etc)

### Soundness
3

### Presentation
2

### Contribution
3
