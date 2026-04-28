# $\texttt{NAISR}$: A 3D Neural Additive Model for Interpretable Shape Representation

- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 6, 6, 8

## Abstract
Deep implicit functions (DIFs) have emerged as a powerful paradigm for many computer vision tasks such as 3D shape reconstruction, generation, registration, completion, editing, and understanding. However, given a set of 3D shapes with associated covariates there is at present no shape representation method which allows to precisely represent the shapes while capturing the individual dependencies on each covariate. Such a method would be of high utility to researchers to discover knowledge hidden in a population of shapes. For scientific shape discovery, we propose a 3D Neural Additive Model for Interpretable Shape Representation (\texttt{NAISR}) which describes individual shapes by deforming a shape atlas in accordance to the effect of disentangled covariates. Our approach captures shape population trends and allows for patient-specific predictions through shape transfer. \texttt{NAISR} is the first approach to combine the benefits of deep implicit shape representations with an atlas deforming according to specified covariates. We evaluate \texttt{NAISR} with respect to shape reconstruction, shape disentanglement, shape evolution, and shape transfer on three datasets: 1) \textit{Starman}, a simulated 2D shape dataset; 2) the ADNI hippocampus 3D shape dataset; and 3) a pediatric airway 3D shape dataset. Our experiments demonstrate that \texttt{NAISR} achieves excellent shape reconstruction performance while retaining interpretability.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a 3D Neural Additive Model for Interpretable Shape Representation (NAISR) which describes individual shapes by deforming a shape atlas in accordance to the effect of disentangled covariates. The proposed approach captures shape population trends and allows for patient-specific predictions through shape transfer. Moreover, NAISR is the first approach to combine the benefits of deep implicit shape representations with an atlas deforming according to specified covariates. Sufficient experiments demonstrate that NAISR achieves excellent shape reconstruction performance while retaining interpretability.

### Strengths
1. The idea is ok
2. This paper is well-written and easy to follow
3. The experiment is sufficient

### Weaknesses
 1. The research survey on the investigated model is relatively limited.
2. The construction details of the algorithm need to be improved.

### Questions
1. It would be better if the authors give more details of how to train the additive model $g_i$?
2. Does the inclusion of group structure contribute to the improvement of model performance? Please refer to the Group Sparse Additive Model (Yin et al 2012; Chen et al 2017).

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes a data model for representing shapes in a shape dataset as a function of given co-variates (i.e., age, weight, sex, etc.). It uses deep implicit representations to learn templates and deformations of shape specific to each co-variate whereas both the templates are deformations are not available apriori. The authors evaluated their method in terms of various shape analysis tasks (shape reconstruction, transfer, disentanglement, and evolution) by applying them to one simulated and two real human organ shape datasets. The experimental results support the claim of uniqueness and usefulness of the work.

### Strengths
+ The paper is a very good-read and tells a story in an elegant manner. It touches upon a new and potentially very impactful area of research in the domain of shape analysis of medical data. 

+ The method is reasonable and the proposed claims are backed up by quantitative and qualitative evidence as experimental results

+ All the related works and their limitations have been comprehensively mentioned. The differences and similarities between the related works and the proposed work are clearly intelligible.

### Weaknesses
 - The loss function is made up of 6 components, each associated with a scalar co-efficient to constitute the final loss. Though an ablation study on the loss components is presented in the supplementary table S.12 and S.13, they do not clearly discuss the effects of these co-efficients on the final result and what should be a reasonable set of values for them. Specifically, the interplay between the different loss terms and how the coefficients affect the trade-offs between reconstruction accuracy, shape disentanglement, and transfer performance is not well-explained. It's unclear how sensitive the model is to these hyperparameter choices and if the reported results are optimal or just a local optimum found by the specific parameter setting.

- Some of the limitations (invertibility problem) should be mentioned in the main manuscript instead of the supplementary. Ending the conclusion of the paper with a reference to the supplementary does not seem like a good approach to me.

- In Section 3.2, the authors simply mentioned that they used SIREN as the backbone of their template and deformation prediction network. I think a little bit more details on SIREN method needs to be added here. For instance, the specific architecture of the SIREN network, the number of layers, and the number of neurons per layer, and how these choices impact the learning of implicit representations are missing. The initialization strategy of the weights and biases, which is crucial for the convergence of SIREN, should also be discussed in more detail.



### Questions
- All the shapes in the dataset seem to be pre-aligned and centered. Is it a requirement that the shapes need to be pre-aligned and centered? In such a case, it should be clearly mentioned in Problem Description (Section 3.1)

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes a concept disentangled deep implicit representation learning method for 3D shapes, with a focus on medical imaging application. Given a set of shapes from the same class represented by a point cloud, the proposed method identifies a template, and learns a set of displacement maps with respect to both known and unknown covariates.  

The technique is compared to five other implicit shape representations (based on implicit functions), and qualitatively and quantitatively outperforms the best competitor A-SDF (Mu 2021), which also learns disentangled implicit shape representation. 

Experiments are conducted on Starman, a simulated 2D shape dataset (5041 training + 4966 testing shapes), ADNI hippocampus 3D shape dataset (1632 hippocampus shapes segmented from magnetic resonance images (MRI)), and pediatric airway 3D shape dataset (357 airway shapes segmented from computed tomography (CT)). Qualitative and quantitative results conducted using shape reconstruction, transfer, disentanglement and evolution experiments and demonstrate competitive performance.

EDIT: I have updated my rating after reading authors' comments.

### Strengths
The paper is well-written and easy to follow. Experiments are thorough and conducted with well-established metrics (Chamfer distance (CD), Earth mover’s distance (EMD), Hausdorff distance (HD)), all established metrics for evaluating 3D shape methods. Code is provided in supplementary materials.

Visualizations are very clear, and lots of additional details are provided in supplementary material.

### Weaknesses
It is not clear how SD based techniques will be beneficial for medical images. Majority of medical imaging techniques use voxel-based representations. The proposed implicit shape representation (as other baselines) smoothed out details (compare ‘’gold standard’’ to all methods in Figure 2, for instance) and it not clear why a method with such artifacts would be beneficial in practice? Authors should provide more clear motivation of why the proposed method will be useful for medical imaging. Specifically, the smoothing effect observed in the reconstructions, while potentially reducing noise, also eliminates fine-grained anatomical details which are often crucial for diagnostic purposes. The paper needs to clarify how this trade-off between smoothing and detail preservation is addressed and why the level of smoothing is appropriate for the intended medical applications. For example, in the context of airway analysis, subtle variations in bronchial structure can be clinically significant, and it is not clear if these variations are preserved by the proposed approach.

As described in Section 3.1, it is assumed that “the overall displacement field is the sum of displacement fields that are controlled by individual parameters”, plus there is a contribution of the unknown covariate (z) which cannot be controlled. However, it isn’t clear what happens if a key covariate is unknown (e.g., not provided in metadata) or a not useful covariate is present? The authors should clearly explain implications of such assumptions. For instance, if a critical factor like a specific genetic marker influencing shape is not included as a covariate, how does the model account for this variability? Does it get absorbed into the latent variable z, potentially confounding its interpretation? Furthermore, the impact of including irrelevant covariates (e.g., a patient's shoe size) needs to be discussed. Will this introduce noise into the model or will the model effectively learn to ignore it?

There are several weaknesses in related work:

* Relationship to other methods (Mu 2021) is not clearly described. What is the methodological advantage that the proposed technique brings? It is not clear how the proposed method improves upon A-SDF, particularly in terms of the disentanglement of shape variations. The paper should provide a more detailed comparison of the architectural differences and how these differences lead to better performance. For example, what specific limitations of A-SDF are addressed by the additive deformation model in NAISR?
* Related work is limited to representations focusing on implicit functions. There is other work in allowing parametrized shape editing, e.g., see for instance: Learning to Infer Semantic Parameters for 3D Shape Editing (Wei, 3DV 2020)

### Questions
In section 4.2, authors describe experiments with shape reconstruction, and indicate that the the proposed method and other SDF techniques can help complete shapes. It isn’t clear whether the technique is trained for shape completion, and if so, where do the partially complete shape come from? Does the fact that a shape is partial negatively influence method training?

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper introduces NAISR, a 3D neural additive model that aims to provide an interpretable shape representation. This approach combines deep implicit shape representations with an atlas that deforms in response to specified covariates. The utility of NAISR is demonstrated through evaluations on simulated and real medical datasets. The paper discusses the advantages of NAISR over other shape representation methods, particularly in capturing individual covariates' effects on shapes, shape transfer capabilities, and the ability to generate shapes based on extrapolated covariates.

### Strengths
- The paper is well-structured, making it easy to follow. The flow of content is logical, facilitating a clear understanding of the proposed model and its implications.

- The paper tackles a significant gap in the shape modeling field: quantitatively capturing shape changes concerning problem-specific covariates. This is a significant contribution to the domain of shape representation and analysis.

- Leveraging neural additive deep implicit for shape representation offers interpretability and shape reconstructions that are resolution agnostic.

- The proposed approach's efficacy is showcased on both simulated data and medical datasets.

- The paper compares NAISR with existing state-of-the-art implicit shape representation methods, further establishing its superior performance and potential for broader applications.

### Weaknesses
 - The paper assumes the given population to be unimodal and representable fully by a learned atlas. However, the methodology's ability to handle multimodal distributions and topological variations remains unclear. Specifically, the approach relies on deforming a single template shape, which may not be adequate for populations exhibiting significant topological differences or multiple distinct modes of variation. For example, in a dataset with both healthy and diseased shapes, the learned atlas might represent an average that does not accurately capture either subpopulation.

- The experiments do not adequately demonstrate the model's performance under limited training sample sizes, a typical scenario in medical shape analysis. The paper should include a more thorough evaluation of the model's performance with varying sample sizes, especially in the low-data regime, which is common in medical imaging. This would provide a better understanding of the model's robustness and applicability to real-world scenarios.

- While deformations from the learned atlas provide a means to statistical shape analysis, the paper does not evaluate or showcase the learned models' statistical aspects. This omission limits the paper's depth and breadth in understanding the model's holistic performance. For example, the paper does not discuss the statistical properties of the learned latent space, such as its dimensionality or the distribution of the latent codes. A deeper analysis of these aspects would be beneficial.

- The paper does not discuss the sensitivity of the proposed model to hyperparameters, which could be crucial for replication and application in various contexts. The lack of a hyperparameter sensitivity analysis makes it difficult to assess the robustness of the model and its applicability to different datasets. It is important to understand how the performance of the model changes with different choices of hyperparameters, such as learning rates, regularization parameters, and network architectures.

Minor: Authors provide a discussion of limitations in the supplementary material, however this should be part of the main paper.

### Questions
- It is unclear how the atlas is initialized. It would be very helpful to show the learned atlas across epochs.

- The paper does not discuss the computational complexity and runtime for various processes, including training, inference, shape transfer, evolution, and disentanglement. Given that neural implicit representation works at the point coordinate level, understanding these metrics is crucial.

-  What are the computational and time requirements to reconstruct a full shape using the proposed implicit representation?

- The paper does not adequately justify the use of a non-amortized latent code, particularly the latent code encapsulating shape parameters not observed or captured by the covariate. The latent code is being optimized during training and inference as opposed to using a neural network to estimate such latent codes.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good
