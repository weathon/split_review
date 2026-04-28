# Implicit Neural Representations for Joint Sparse-View CT Reconstruction

- Decision: Reject
- Avg Score: 5.50
- Scores: 3, 5, 6, 8

## Abstract
Computed Tomography (CT) is pivotal in industrial quality control and medical diagnostics. Sparse-view CT, offering reduced ionizing radiation, faces challenges due to its under-sampled nature, leading to ill-posed reconstruction problems. Recent advancements in Implicit Neural Representations (INRs) have shown promise in addressing sparse-view CT reconstruction. Recognizing that CT often involves scanning similar subjects, we propose a novel approach to improve reconstruction quality through joint reconstruction of multiple objects using INRs. This approach can potentially utilize the advantages of INRs and the common patterns observed across different objects. While current INR joint reconstruction techniques primarily focus on speeding up the learning process, they are not specifically tailored to enhance the final reconstruction quality. To address this gap, we introduce a novel INR-based Bayesian framework integrating latent variables to capture the common patterns across multiple objects under joint reconstruction. The common patterns then assist in the reconstruction of each object via latent variables, thereby improving the individual reconstruction. Extensive experiments demonstrate that our method achieves higher reconstruction quality with sparse views and remains robust to noise in the measurements as indicated by common numerical metrics. The obtained latent variables can also serve as network initialization for the new object and speed up the learning process.\footnote{We have used ChatGPT provided by OpenAI to assist in writing. The language model was employed at the sentence level for tasks such as fixing grammar and rewording sentences. We assure that all ideas, claims, and results presented in this work are human-sourced.}

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper deals with the reconstruction of sparse-view CT images. The authors propose a novel Bayesian framework to jointly reconstruct multiple objects using implicit neural representations. The authors evaluate their method against other methods including FBP, iterative, and some joint reconstruction techniques using INRs.

### Strengths
The paper is generally well written, and the motivation is clear. Additionally, the literature review is exhaustive. The authors also provide some interesting ablation studies of their method.

### Weaknesses
 **Writing**

While the paper is well written and easy to read, some statements by the authors are somewhat misleading:
> Sparse-view Computed Tomography (CT) is favored over standard CT for its reduced [...] (Abstract)

suggests, that sparse-view CT would be common practice nowadays, which is -to the best of my knowledge- not the case.

>  While dense measurements typically yield accurate reconstructions, measurements are often intentionally limited to reduce ionizing radiation or cost, resulting in sparse data. (Introduction)

See above, to the best of my knowledge, sparse-view CT is not common in clinical practice. Also, can the authors clarify, how reducing the number of angles may reduce cost?

> While many approaches learn the mapping from sparse-view to dense-view images using supervised learning [...] they often necessitate extensive, domain-specific datasets which are difficult to obtain in practice. (Introduction)

Since full-view acquisitions are the de-facto standard in clinical CT and sparse-view datasets can easily be simulated from these data, such datasets are abundant (e.g., the LDCT Image and Projection data [1] contains over 300 full-view, full-dose acquisitions)

**Experiments**

I have several concerns regarding the experiments:

1. Comparison methods. Unfortunately, the authors do not compare their method against standard CNN-based methods (some of which are also mentioned in the introduction). In particular, the authors do not compare their method against approaches that implicitly (e.g., [2]), or explicitly (e.g., in the form of a DNN) incorporate prior knowledge. The authors also don't compare their method against other, previously proposed INR reconstructing techniques for sparse-view CT.
2. Missing error bars in Fig. 4, 5, & 6. In Tab. 1, over what is the mean $\pm$ standard deviation computed? Are the improvements statistically significant?
3. It is well known, that metrics such as SSIM and PSNR are often not in agreement with quality assessment by clinicians [3,4]. While I recognize that a thorough evaluation involving a reader study is beyond the scope of this work, I don't think the results in Tab. 1 justify the authors claim that their method 'sets a new standard in CT reconstruction performance' (Abstract). Upon visual inspection of Fig. 2 & 3, I find that the proposed method removes many anatomical details and I highly doubt that a clinician would find that reconstructions produced by INR-Bayes are significantly better than those produced by e.g. SingleINR.

**Computational complexity and real-world applicability**

What is the computational complexity of the method? Are all reconstructions performed for the main paper on single $512\times 512$ slices? The application to CBCT reconstructions shown in the appendix is on a much smaller (clinically unusable) image matrix. What would the computational cost for one full patient be compared to the other methods and a CNN-baseline?


### Questions
The experiment configurations intra-patient and 4DCT violate the conditional independence assumption. Does this influence reconstruction quality?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposes a method to implicit neural representation learning (INR) for joint sparse-view CT reconstruction, which means that to reconstruct several CT images at the same time. The proposed method is evaluated on different CT image datasets and shows better performance compared with previous meta-learning based INR methods.

### Strengths
- The proposed method may investigate an interesting research question that how to incorporate population priors in INR learning. Although I do have quite a few concerns and questions about the proposed method as below, the proposed INR-Bayes method may be a potential way by introducing latent variables so that it may be possible to make it as a generative model from some prior distribution in some way..
- The paper validates the proposed method on different CT image datasets with different CT configuration or settings, and compares them with different baselines. The experiments about adaptation on new patients using priors learned from other patients are an interesting setting, but may also be questionable as follows.

### Weaknesses
 - The motivation for conducting joint CT reconstruction. From the perspective of clinical applications, I do not see any reason why we want to do joint CT reconstruction. To my best knowledge, there are no such settings and needs from current clinical protocol. Can we imagine that in a scenario, after one patient is scanned, we do not do the reconstruction right after the scanning but wait until there are 5-10 patients’ scans, then we want to do the reconstruction together? I cannot think about some applications that require such needs, maybe the author can explain more or give some specific examples.  
- What is the physical meaning of the learned priors? This prior is learned from 10 slices (which mimics 10 different patients). From this setting, I guess the prior may be some “average” CT image across these 10 images including mostly low-frequency signals. This guess is also supported by the illustration of learned prior in Figure 13 and 15, which is somewhat the general structure of the sliced anatomic structure. But why should this prior be helpful to reconstruct higher quality of CT for new patients? In the sparse-view CT reconstruction, due to the sparse sampling, what is always missing is the high-frequency signal in the detailed structure. Why does such an “average” image should be helpful to improve the final reconstruction image quality to get sharper and fine structures?
- How to choose these 10 patients to get the prior? If we consider a setting to use the learned prior for new patients’ reconstruction, how shall we choose the 10 different patients to get the prior? Such as healthy patients or abnormal patients? For example, if there are some patients with tumors, does the learned prior also include such prior in the latent variables and indicate that in the new patients’ reconstruction? Shall there be any relationship between the new patients and prior patients? How can we know if the new patient is normal or abnormal before we get the CT image reconstructed?
- How does the method deal with registration problems in CT imaging? The validated datasets in the paper seem to be already registered. If we consider the real CT scanning in practice, for different patients, the patient’s positions will always be different. How can this method deal with the position shift when learning the prior from different patients?
- In the motivation as well as experiments, one important baseline that the paper compares with is MAML [1]. As the author also mentioned, [1] learned an initialization from multiple objects in order to speed up optimization process while cannot achieve better optimization results from the learned initialization. The proposed works share a lot of similarity with [1] while using a different way to formulate and parametrize the learned prior, why the proposed method would achieve better optimization results while [1] not. The results in Table 1 also support these where the scores for these two methods are quite comparable. Besides, does the INR-Bayes and MAML use the same encoding function, embedding size and backbone network structure in this comparison?
- In the previous works, the paper mentioned “Lastly, while alternative joint CT reconstructions like (Shen et al., 2022) [2] use priors from pre-reconstructed images, and (Reed et al., 2021) [3] relies on finding a template image from 4DCT; their practical limitations led to their exclusion from our comparative analysis.” First, to my understanding, these two works are not doing the joint CT reconstruction as claimed in this paper. [2] is doing the CT and MRi reconstruction through INR by using a full-sampled prior image of the same patient as prior embedding, which is a very common setting for patients’ longitudinal study in clinics. [3] is doing dynamic CT reconstruction where different frames share some similarity while maintaining deformable motion, which is also very common in 4DCT setting with motion. Second, I do not see what is the “practical limitations led to their exclusion from our comparative analysis”, since these two papers’ setting may be more reasonable from practical applications. And their goal is to achieve better reconstruction results instead of fast convergence as [1], so I think these two papers may even be more important to be  compared with to demonstrate the superiority of the proposed method.
- In the setting of “Applying to Unseen Data using Learned Prior”, how are the patients chosen to learn the prior? Would different prior patients influence the reconstruction for the same new patient? Would different number of prior patients influence the reconstruction for the same new patient? When adapt the new patients, will the latent variable also adapt to the new patient?
Computational efficiency. Based on Algorithm 1, it seems that multiple networks are maintained and trained simultaneously for different patients. Also it needs to iterate through all patient, all time steps, with three loops interleaved. This algorithm looks very costly for memory and time efficiency. Can the paper report the memory and time used in training and testing with comparison of baseline methods?
- Using some framework figure may be better to illustrate the whole framework.

### Questions
Please see weakness for the details of questions.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces a new method for improving the reconstruction quality of sparse-view CT scans using implicit neural representations (INRs). Addressing the challenges posed by undersampled data in Sparse-view CTs, this paper advocates for joint reconstruction of multiple objects/subjects, capitalizing on the shared information (statical regularities in the paper) often found in similar subjects. Central to their approach is an INR-based Bayesian framework that incorporates latent variables to discern inter-object relationships. These variables serve as a dynamic reference during the optimization process, ensuring enhanced reconstruction quality. This work achieves good results and promises to open source the code.

### Strengths
1. Novelty. I like the proposed approach to modeling shared information in a "nerf-in-the-wild" setting. It effectively extracts maximal shared information across different subjects and demonstrates its utility. This setting is new, at least to me. While some works have applied INRs to sparse-view CT challenges, this paper slightly sets it apart by jointly reconstructing multiple objects. Also, the incorporation of multiple latent variables in the Bayesian framework is a thoughtful addition, further enhancing the originality of the approach.

2. The paper is well-structured and offers an intuitive flow, making it easy to read and follow.

3. The tackled problem, sparse view CT reconstruction, holds its own significance in "AI+Med". The paper provides some extra (toy) examples in the appendix, which is appreciated.

### Weaknesses
1. Small improvement. While the proposed method is conceptually appealing, the performance improvement appears to be minimal. As illustrated in Table 1, the gains, though in the positive direction, are relatively slight. Such incremental progress might raise questions about the practical implications and advantages of adopting this new approach over existing methods. The reported PSNR improvements, while positive, are on the order of 0.5-1.5 dB, which may not be substantial enough to justify the added complexity of the proposed approach, especially when considering the computational overhead of training implicit neural representations. A more thorough analysis of the practical significance of these gains, perhaps through visual inspection of reconstructed images or other metrics beyond PSNR, would be beneficial. Furthermore, the consistency of these gains across different datasets and noise levels should be investigated to better understand the robustness of the method.

2. Non-principled static-transient decomposition. From what I understand now, the current model seems to hinge on a static branch that remains uniform across all subjects, irrespective of their position in the 3D volume. While this might be appropriate in a NeRF-in-the-wild setting, given the fixed positioning of structures like buildings in the real world, its direct application to varied anatomical structures in the abdominal region seems problematic. Every patient's anatomy, although structurally similar, is unlikely to occupy the same 3D space due to innate variations (rigid/deformable transformations). Hence, applying this method without a template registration step appears misguided. The static branch, as currently implemented, assumes a shared coordinate space across all subjects, which is a strong assumption that does not hold true for anatomical data. This could lead to suboptimal performance, especially when dealing with significant inter-subject anatomical variations. A more principled approach would involve incorporating a mechanism to account for these variations, such as learning deformation fields or using a canonical space for reconstruction.

### Questions
1. Increasing the number of nodes doesn't help much for almost all methods. Do the authors have any insights into this?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a novel approach to improve reconstruction quality in Sparse-view Computed Tomography (CT) using Implicit Neural Representations (INRs) with a Bayesian perspective. The method incorporates latent variables to capture inter-object relationships and sets a new standard in CT reconstruction. The authors utilize three CT datasets and a natural image dataset to evaluate the generalizability of their approach. The proposed INR-based Bayesian framework enhances individual reconstructions and shows notably better metrics compared to other methods.

### Strengths
- Novel approach to improve reconstruction quality in sparse-view CT with INR, enhancing reconstructions.
- Extensive experiments and comparisons with other methods, to evaluate various facets of reconstruction performance
- Clear and detailed explanation of the methodology, including the EM algorithm and the alternating E and M steps used in the approach
- Results are well explained, each demonstrating the efficiency of including Bayesian framework.
- Well-designed and well-executed study that makes a significant contribution to the field of medical imaging.

### Weaknesses
No significant weakness in the paper.

### Questions
- For Figure 4b, there is a discussion that MAML might struggle to capture the shared features when many nodes are participating. Could you give bit detailed explanation? Also, which dataset are used for Figure 4? Was it 4DCT?
- Why would MAML fail to learn meaningful prior in Supplementary Figure 10?
- How does the proposed framework compare to other state-of-the-art methods in terms of computational efficiency?

nitpicks:
- Missing bold text in 5th row of Table 3.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
