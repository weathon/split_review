# Reconstruction of Cortical Surfaces with Spherical Topology from Infant Brain MRI via Recurrent Deformation Learning

- Decision: Reject
- Scores: 5, 3, 3

## Abstract
Cortical surface reconstruction (CSR) from MRI is key to investigating brain structure and function. While recent deep learning approaches have significantly improved the speed of CSR, a substantial amount of runtime is still needed to map the cortex to a topologically-correct spherical manifold to facilitate downstream geometric analyses. Moreover, this mapping is possible only if the topology of the surface mesh is homotopic to a sphere.  
Here, we present a method for simultaneous CSR and spherical mapping efficiently within seconds. Our approach seamlessly connects two sub-networks for white and pial surface generation. Residual diffeomorphic deformations are learned iteratively to gradually warp a spherical template mesh to the white and pial surfaces while preserving mesh topology and uniformity. 
The one-to-one vertex correspondence between the template sphere and the cortical surfaces allows easy and direct mapping of geometric features like convexity and curvature to the sphere for visualization and downstream processing. We demonstrate the efficacy of our approach on infant brain MRI, which poses significant challenges to CSR due to  tissue contrast changes associated with rapid brain development  during the first postnatal year. Performance evaluation based on a dataset of infants from 0 to 12 months demonstrates that our method substantially enhances mesh regularity and reduces geometric errors,
outperforming state-of-the-art deep learning approaches, all while maintaining high computational efficiency.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposed a recurrent deformation learning method for cortical surfaces reconstruction. The validation on the BCP dataset shows the good performance.

### Strengths
The results show improvement over the competing methods.

### Weaknesses
1.The details of the proposed mehthod are not clearly.
2. The topology correction is not validated.
3. The time consuming should be given.
4. The segmentation performance also should be given.

### Questions
1.The details of the proposed mehthod are not clearly.
2. The topology correction is not validated.
3. The time consuming should be given.
4. The segmentation performance also should be given.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a recurrent method for cortical surface reconstruction by deforming a sphere template.

### Strengths
1. Utilize a general sphere template as the starting shape for the reconstruction task.
2. Utilize a recurrent method. 
3. The presentation is clear and the experiments and visualization are sound.

### Weaknesses
1. This work is an incremental work based on the previous CSR methods, like CortexODE, Vox2Cortex, etc. Instead, this work utilized a more general sphere template, while other methods get the template from a mean shape or topology correction. Even though the author mentions that the sphere template is beneficial for spherical mapping, for the cortex reconstruction task, I don't see the advantage of using a sphere template for CSR. The use of a sphere as the initial template introduces a significant deformation challenge, as it is topologically and geometrically distant from the target cortical surfaces. While the authors claim it simplifies spherical mapping, the core reconstruction task becomes more complex, potentially negating the benefits. The paper lacks a clear justification for why a sphere is superior to other initialization methods for the *reconstruction* itself, given the increased difficulty of the deformation. 
2. The recurrent framework is not novel, as it has been applied to medical image registration for a long time. Even though it might be the first time introduced into the CSR, it is not novel enough for ICLR. The recurrent approach, while potentially useful, doesn't introduce a fundamentally new concept to the field. The core idea of iterative refinement is well-established, and its application here, while perhaps novel in the specific context of CSR, doesn't represent a significant conceptual leap. The method appears to be a straightforward application of a known technique to a new problem, rather than a novel methodological contribution.
3. The proposed framework: template -> white surface -> pial surface, is pretty similar to CortexODE, with the change of using a sphere template and multiple-step surface reconstruction. The multi-step approach, while common in traditional methods, doesn't offer a substantial innovation in this deep learning context. The paper doesn't provide a strong rationale for why this specific sequence is superior to other possible strategies, or why it represents a significant advancement over existing deep learning-based CSR methods.

### Questions
The proposed method contains limited innovation and is mainly incremental work. Even though the author wants to emphasize the benefit of spherical mapping, from the CSR point of view, the method is not novel enough for ICLR.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
Neuroanatomical studies of populations often perform analyses on the cortical surface of the brain (imaged by MRI), with the brain represented by a mesh (or a mesh-inflated-to-a-sphere) enabling the study of local cortical shape thickness. Submission 6817 presents a framework for the fast extraction of cortical surfaces using supervised learning to match the performance of a conventional solver. 

In current literature, a popular approach is to train a supervised UNet-style network output multiple deformation fields that iteratively warp a template mesh into the desired ground truth cortical surface (with the ground truth obtained by FreeSurfer or similar). Submission 6817 follows this approach but instead uses a recurrent UNet instead of an unrolled UNet. Experimentally, it focuses on supervised infant cortical surface extraction using data from the Baby Connectome Project.

### Strengths
- The proposed “adaptive edge length loss” is an interesting and intuitive approach to dealing with the dramatic volume changes in the brain in the first year of growth.
- Using multi-modal T1w & T2w MRI as inputs for all considered methods is a nice touch as infant surface extraction has lower contrast and thus benefits from inter-modality differences.

### Weaknesses
### No methodological or implementation details provided:
As presented, this paper is unreproducible and hard to evaluate as no implementation and low-level modeling details are provided. For example, there’s no network architecture, no code, no details regarding dataset preprocessing (crucial to CSR), no details about data augmentation, how baselines were tuned, etc. The short implementation subsection lists learning rates, number of iterations, and loss weights, but spends the other half of its space describing instance normalization. 

**Suggestion:** As the submitted paper doesn’t make it to the ICLR page limit (and there’s unbounded supplementary space), please actually describe the framework and its details and also share code if possible.

### ODE and iterative deformation contributions presented as novel:
Section 3.2 presents the proposed ODE-based deformation formulation which is framed as a contribution. However, this appears to be the same formulation as used in most previous work on CSR (e.g., CortexODE, CortexFlow, etc.) with the only distinction being that a recurrent UNet is used instead of an unrolled UNet. 

**Suggestion:** Please detail how this specific contribution is non-trivially different from previous work and describe any specific innovations.

### Baseline performance does not match trends reported in previous work:
The experiments show the proposed method widely outperforming well-established baseline methods such as Vox2Cortex and CorticalFlow++. However, these experimental trends are highly unexpected as previous work also on infant data show that the differences between methods are in the order of 0.01 mm whereas this paper reports differences of 1mm or more (for example, see table 1 in CoTAN, MICCAI’23 https://arxiv.org/pdf/2307.11870.pdf). 

How were these baselines implemented? Were their hyperparameters tuned on validation data ? If so, please add supplementary plots supporting this. Crucially, several of these methods start from an initial template cortical surface and not a sphere as in this method - were proper initial templates when these methods were run, or was a sphere used? If the latter, published hyperparameters for these methods will no longer transfer to the setting of this paper and need significant reworking for fair comparison. 

**Suggestion:** Please clarify these experimental differences w.r.t. other published work and describe in detail how the baselines were implemented and tuned.

### Only a single dataset
The paper presents itself in the context of infant brain surface extraction which does not have many public datasets associated with it. However, none of the proposed methods in the submission are specific in any way to infants and could be directly applied to adults (in datasets such as HCP or ADNI) or neonates (e.g., the dHCP dataset). To actually evaluate the generalizability of the method, please include experiments on atleast one more dataset as is common in most papers in the subfield. 

**Suggestion:** If experimenting on another dataset is not possible, please explain why the method is specific to infants in the 0-8 mo. age range.

### Overstretched claims
The paper makes some claims that are not well supported. For a few examples,
- The introduction (para. 3) claims that papers based on graph convolutions such as Hoopes, et al and Bongratz, et al. do not generate topologically valid surfaces and require topology correction. This is untrue as both methods perform the same topologically-valid approach as the submission (deforming a template to a target) and do not require correction. 
- The paper claims that infant brain myelination (“tissue contrast changes”) poses a significant challenge to cortical surface reconstruction because of poor segmentation. However, this is only true in the unsupervised setting (e.g., using EM-style methods). As the paper trains its segmentor in a fully supervised manner, tissue segmentation is no more challenging than it is in adult brains as evidenced by all the work using the iSeg dataset.

**Suggestion:** Please temper these claims.

### Questions
Please see above, all of my suggestions to focus the rebuttal are highlighted in bold.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
