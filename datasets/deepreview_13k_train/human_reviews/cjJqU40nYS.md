# Occlusion-aware Non-Rigid Point Cloud Registration via Unsupervised Neural Deformation Correntropy

- Decision: Accept
- Scores: 5, 6, 6, 6

## Abstract
Non-rigid alignment of point clouds is crucial for scene understanding, reconstruction, and various computer vision and robotics tasks. Recent advancements in implicit deformation networks for non-rigid registration have significantly reduced the reliance on large amounts of annotated training data. However, existing state-of-the-art methods still face challenges in handling occlusion scenarios. To address this issue, this paper introduces an innovative unsupervised method called Occlusion-Aware Registration (OAR) for non-rigidly aligning point clouds. The key innovation of our method lies in the utilization of the adaptive correntropy function as a localized similarity measure, enabling us to treat individual points distinctly. In contrast to previous approaches that solely minimize overall deviations between two shapes, we combine unsupervised implicit neural representations with the maximum correntropy criterion to optimize the deformation of unoccluded regions. This effectively avoids collapsed, tearing, and other physically implausible results. Moreover, we present a theoretical analysis and establish the relationship between the maximum correntropy criterion and the commonly used Chamfer distance, highlighting that the correntropy-induced metric can be served as a more universal measure for point cloud analysis. Additionally, we introduce
locally linear reconstruction to ensure that regions lacking correspondences between shapes still undergo physically natural deformations. Our method achieves superior or competitive performance compared to existing approaches, particularly when dealing with occluded geometries. We also demonstrate the versatility of our method in challenging tasks such as large deformations, shape interpolation, and shape completion under occlusion disturbances.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
Authors proposed a new approach to non-rigid point alignment using implicit deformation networks. Solving non-rigid point alignment using implicit deformation is attractive as it is self-supervised can generalize to well to unknown categories. There is specific focus is on how best to handle occlusion using such networks. The authors propose a maximum correntropy criterion. They argue that it effectively avoids collapsed, tearing, and other physically implausible results – leading to substantially better results than current state of the art.

The authors also demonstrate impressive results on a variety of benchmarks including 4DMatch and OpenCAS. One concern, however, with the approach is that it is essentially a well documented loss function, and well known regularizer applied to the problem of non-rigid point alignment. There is no real explicit handling of occlusion, it is instead handled implicitly through the loss function and regularizer. Also, there needs to be further ablation  into how the network architecture itself regularizes the solution. This seems to have been discarded as a minor detail in Sec 4.3. As it stands, I am on the fence with the paper. The results are good, but the motivation, ablation and new ideas are lacking. 

One major concern I have is the proposed objective seems quite similar to classical robust error functions used for decades within robotics and computer vision literature. It would be good if the authors could relate their loss function to these other methods. My initial feeling is that they would almost get identical results, but happy to hear back from the authors about why I am wrong.

Most famously the Huber loss function, 

- P. J. Huber, “Robust Estimation of a Location Parameter,” The Annals of Mathematical Statistics, vol. 35, no. 1, pp. 73–101, 1964.

Huber loss functions and their variants have been used for decades in both 3D point and image alignment problems to deal with occlusion and outliers. A great example can be found in:-

- A. W. Fitzgibbon, “Robust registration of 2D and 3D point sets,” Image and Vision Computing, vol. 21, no. 13-14, pp. 1145–1153, 2003.    

Subsequent works have evaluated broad families of robust error functions. 

One notable example includes:-

- B. Theobald, I. Matthews, and S. Baker. “Evaluating error functions for robust active appearance models,” in IEEE International Conference on Automatic Face and Gesture Recognition, 2006.

### Strengths
- The results are impressive compared to current state of the art (especially in the presence of significant occlusion), and the authors do a good job of applying their approach across a number of application domains.
- I especially like use of LLR in the method, using classical work from Roweis and Saul (’00). The Application of the LLR regularization loss is critical to the success of the propose approach. However, it does lead to questions of where does the regularization of the method is stemming (implicitly from the network, all solely through the LLR loss). 
- Authors do a good job on the ablation of their method, especially with respect to the number of neighbors and bandwidth (see Appendix C).
- The evaluation and visualization of results are compelling.

### Weaknesses
 - In general I do have some concerns over novelty. At the end of the day the authors are proposing an existing loss, and regularizer to a new problem. The novelty is really in how well it works for the problem of non-rigid point alignment. 
- In Sec 4.3, the authors use a SIREN style implicit neural function (INF) using sinusoid activations. This departs quite heavily from the NSFP work of Li et al. which use ReLU activations. One motivation in NSFP for ReLU is that it leverages the inherent spectral bias of ReLU to find low-frequency (i.e. smooth) solutions. By using SIREN style INFs the authors would kill this property. It seems this would be an additional motivation for the LLR regularization. Some sort of ablation on the role of activation with the LLR would be useful, as they seem to both be regularizing the solution.   
- There seems to be a number of mistakes in the Lemma and Definitions, they also seem quite trivial and do not add much to the paper. 
- The authors report timing information for their method in Table 2. NSFP is currently considered quite slow for an INR method. Approaches like Li et al. “Fast Neural Scene Flow” (ICCV’23) show a 30 times speedup with almost no loss in performance. It would be useful for the authors to discuss this, and talk about how feasible such a strategy would be to their method.
- See my other concerns in the summary concerning the relation of the author's loss function with classical robust error functions (e.g. Huber loss).
- The role of correntropy (i.e. MCC) is overblown. The title, abstract and introduction of the paper make a significant deal about correntropy. However, the central utility of the approach is around the LLR regularization. Since MCC is such a significant part of the narrative of the paper it seems inappropriate for this discussion to be hidden in the appendix. A generic robust-error function will likely work just as well, and there would be little sensitivity to threshold and kernel size selection (removing the central advantages of the MCC measure that the authors have noted).

### Questions
- In Definition 1, why are the authors referring to bandwidth? It seems the statement is quite generic (covering all kernels that satisfy Mercer’s theorem). Kernels like Gaussian have bandwidth, but that seems much more restrictive. 
- Lemma 1 seems wrong. The authors have not defined the kernel, and just said that it needs to satisfy Mercer’s theorem. It is trivial to show that if k(x,y) = ||x – y||, then it would not be L2 close, L1 as they get apart, and L0 far apart. It seems this statement should be dependent upon the type of kernel used? For example, for the specific case of a Gaussian kernel I would believe such a statement. 
- Eq. 2 seems to have a mistake. They use k(x – y), but I suspect it should be k(x,y)?

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
3

### Summary
This paper proposed a novel method for non-rigid registration between two point clouds under partial occlusion. The core idea of the proposed method is to use the Maximum Correntropy Criterion (MCC) to measure the similarity between two point clouds. By the combination of MCC and implicit neural representations, efficient unsupervised point cloud registration algorithm can be developed. Furthermore, a local linear reconstruction (LLR) formulation has been utilized to regularize the deformation of occluded region of point cloud. Experiment on the Open-CAS liver and several self-built dataset shows that the proposed method achieves impressive result under occlusion and large deformation.

### Strengths
1. Although the MCC is an existing metric, but its usage in the framework of implicit neural deformation optimization is simple, elegant and effective
2. The experiment result is impressive, the proposed method consistently outperforms competing approaches by large margin on Open-CAS liver dataset
3. The proposed LLR has demonstrated its effectiveness in ablation study, especially in high level of occlusion
4. The presentation is clear and easy to follow, and the result is reproducible with source code

### Weaknesses
1. There is no ablation study on the use of MCC and Chamfer distance for registration. As Proposition 1 says that the Chamfer distance is a special case of MCC induced metric, it would be good to see how the generalization of the MCC induced metric works on real-world point cloud registration, for example, with different level of occlusion, deformation, or even registration in same-class level, not same-instance level. It would also be good to see the comparison on computational efficiency
2. Table 4 is in appendix, not in the main text
3. The shape completion task in section 5.7 requires a complete source mesh model as template, which may not be available in practical scenarios. It would be good to see whether a 'mean' shape mesh model could serve as the template and achieve good mesh hole filling result.

### Questions
1. In Fig.6 shape interpolation experiment, what the timestamp t means? is it some mixture ratio between two shapes? it would be good to briefly describe the settings for shape interpolation

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
The paper proposes an unsupervised method for deformable point cloud registration, aiming to handle the case where parts of the point cloud are missing due to occlusions. Prior works have mainly used the Chamfer Distance to measure the similarity between the registered point clouds, which does not account for occlusion. In contrast, the proposed method utilizes the correntropy-based metric. This metric includes a decaying kernel function that reduces the influence of the occluded region on the deformation result and enables the registration of point clouds with occlusion. To accommodate the deformation of the occluded parts, the authors include a linear reconstruction regularization term to preserve the original point local structure in the deformed point cloud. The point deformation field is parametrized as a coordinate-based neural network, where the network's parameters are optimized subject to the correntropy and regularization term. The method is applied to several point cloud benchmarks with occlusion, as well as for shape interpolation and completion applications, and demonstrates favorable performance.

### Strengths
The paper is well-written and easy to understand. The method is technically sound, can be applied to various applications, and improves over the compared alternatives. That said, important evaluations and comparisons are missing.

### Weaknesses
The method is evaluated quantitatively on the Open-CAS, 4DMatch, and 4DLoMatch, and several shapes from the TOSCA dataset. Still, a major dataset in the non-rigid deformation literature is SHREC’19 [1]. The shape completion application hints that the method can handle human body non-rigid matching and an evaluation on this dataset can further demonstrate the method's utility. Additionally, the evaluation on partial animal shapes should be done with the common SHREC'16 benchmark [2] instead of several selected shapes from TOSCA.

Comparison:
There are prior works that use an implicit field [3] or self-supervision [4] for non-rigid partial shape registration. Such works should be discussed and compared. Specifically, the implicit field methods often demonstrate superior performance in handling topological changes and large deformations, which are relevant to the problem of occlusions. The self-supervised methods, while requiring training data, can learn more robust feature representations that could potentially improve the registration accuracy, especially in the presence of significant occlusions. A thorough discussion of the advantages and disadvantages of these alternative approaches is necessary to properly contextualize the contribution of the proposed method.

I think the paper passes the acceptance threshold, though adding the missing evaluations and comparisons can strengthen the submission much further.

### Questions
Please address the concerns raised in the "weakness" section.

### Soundness
3

### Presentation
3

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
In this paper, the authors propose an occlusion-aware non-rigid point cloud registration method based on cross correntropy between deformed source shape $T(Y)$ and occluded target shape $X$.  The paper argues that the main failure reason of previous non-rigid point cloud registration methods is that most of them are based on the standard Chamfer Distance (CD), which can lead to collapsed or physically implausible results. To overcome the limitation, the paper demonstrates theoretical analysis between maximum correntropy criterion (MCC) and CD and concludes that the standard CD is a special case of MCC and MCC is more robust in occluded regions. Furthermore, the paper proposes a regularization based on locally linear reconstruction (LLR) inspired by local linear embedding (LLE) to regularize the deformation smoothness of unmatched points and experimentally demonstrate the superior performance of LLR compared to as-isometric-as-possible (AIAP). In the experiment part, the paper conducts extensive experiments under different settings (e.g. medical data, human, animal, different level of occlusions) and demonstrates the superior performance of the proposed method compared to prior works, including both axiomatic and learning-based methods.

### Strengths
1. The paper conducts exhaustive experiments in different scenarios ranging from medical data to animal and humans and demonstrates superior performance of the proposed method compared to both axiomatic and learning-based method. 
2. The idea of using maximum correntropy criterion (MCC) and local linear reconstruction (LLR) for non-rigid point cloud registration is novel and technically sound. In the ablation study, the paper also demonstrates the superior performance of LLR in comparison to as-isometric-as-possible (AIAP) regularization, which is commonly used in previous methods.

### Weaknesses
1. In the experiment part, the paper only demonstrates rather synthetic point cloud datasets in the context of occlusion ratio as well as point cloud sampling density. When it comes to more challenging dataset like 4DMatch and 4DLoMatch with less overlap and large motions. The proposed method needs to use the pre-trained geometric feature descriptor Lepard. Meanwhile, it would be better to shortly describe how to incorporate the pre-trained feature descriptor into the proposed method. 
2. The motivation of using neural implicit representation is not well illustrated. To my understanding, the proposed regularization can also be directly used to optimize the deformation field defined on each point in the point cloud. 
3. It would be better to conduct an ablation study, which replaces MCC with standard Chamfer Distance to better demonstrate the effectiveness of MCC.
4. In the literature of point cloud completion, some works also propose variants of CD to address the problem of occlusion, it would be better to also compare MCC with their proposed variants, e.g.
T. Wu, et al.: Density-aware Chamfer Distance as a Comprehensive Metric for Point Cloud Completion (NeurIPS 2021)
F. Lin, et al.: Hyperbolic chamfer distance for point cloud completion (ICCV 2023)

### Questions
1. In Eq.3, the definition of $\tilde{y}_{i}$ should be  $T(Y)$ rather than $Y$?
2. More details of Lemma 1 should be provided, since it is the crucial difference between MCC and standard CD.

### Soundness
3

### Presentation
2

### Contribution
2
