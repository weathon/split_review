# ND-SDF: Learning Normal Deflection Fields for High-Fidelity Indoor Reconstruction

- Decision: Accept
- Avg Score: 7.50
- Scores: 8, 8, 8, 6

## Abstract
Neural implicit reconstruction via volume rendering has demonstrated its effectiveness in recovering dense 3D surfaces. However, it is non-trivial to simultaneously recover meticulous geometry and preserve smoothness across regions with differing characteristics. To address this issue, previous methods typically employ geometric priors, which are often constrained by the performance of the prior models. In this paper, we propose \textbf{ND-SDF}, which learns a \textbf{N}ormal \textbf{D}eflection field to represent the angular deviation between the scene normal and the prior normal. Unlike previous methods that uniformly apply geometric priors on all samples, introducing significant bias in accuracy, our proposed normal deflection field dynamically learns and adapts the utilization of samples based on their specific characteristics, thereby improving both the accuracy and effectiveness of the model. Our method not only obtains smooth weakly textured regions such as walls and floors but also preserves the geometric details of complex structures. In addition, we introduce a novel ray sampling strategy based on the deflection angle to facilitate the unbiased rendering process, which significantly improves the quality and accuracy of intricate surfaces, especially on thin structures. Consistent improvements on various challenging datasets demonstrate the superiority of our method.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper presents a pipeline for multi-view 3D reconstruction of indoor scenes. The pipeline is based on recently popular differentiable volume rendering methods using Signed Distance Functions (SDF), such as VolSDF and NeuS. To enhance reconstruction quality in indoor scenes, particularly in textureless regions, the paper introduces monocular priors for additional supervision, inspired by recent works like MonoSDF and NeuRIS.

A core contribution of this paper is the introduction of a normal deflection field, which helps the model identify and correct inaccuracies in reference normal images estimated from monocular models, such as the Omnidata model. Experimental results show that this deflection field aids in reconstructing fine geometric details, such as thin structures.

Additionally, the authors introduce techniques to further improve geometry reconstruction quality, including (1) an adaptive normal loss weight and (2) unbiased volume rendering on thin objects.

The experimental results are promising and include comprehensive ablation studies. Overall, the paper is well-argued and substantiated.

### Strengths
- The proposed normal deflection fields, which correct inaccurately estimated normals from normal maps, seem reasonable to me. 
- Table 6 and Figure 5 effectively showcase the contribution of the method's design through comprehensive ablation studies.
- The experimental results demonstrate that this proposed pipeline achieves state-of-the-art reconstruction quality in indoor scenarios.

### Weaknesses
 - Using unbiased volume rendering for thin structures seems reasonable. However, why not apply this unbiased volume rendering weight uniformly across all regions? The authors mention potential convergence issues with this approach, but it would be helpful if they provided a more in-depth analysis explaining the nature of these convergence issues and offered insights into why they occur.


### Questions
- In Line 280, is this a typo on $g(\theta)$? Looks like this is a missing $\Delta$.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper proposed a method to improve prior normal-guided neural SDF indoor scene reconstruction. Instead of supervising the normal uniformly across the whole domain, the author proposes to use a network to learn the deflect normal and desired adaptive angle prior to loss according to the deviation of the deflect normal to the prior normal. The intuition is that large deviation happens in complex structure areas where the normal prior in general is bad quality.  The author also proposes to use the re-weighted loss on normal, depth, and color rendering.  The experiments show the proposed method performs well qualitatively and quantitatively.

### Strengths
1. The paper is well-written and easy to follow. 
2. The normal deflection detection design is under reasonable assumptions and it offers a solution to deal with non-accurate normal prior.  
3. The angle deviation loss design fits the situation. 
4. The author provides complete experiments to show their method's performance. Including comparison with previous work quantitatively and qualitatively and ablation studies to show each module improves the results.

### Weaknesses
1. The bad quality normal prior problem seems only solved half. The author reduced the loss weight on the part that the normal prior is not accurate, but not the other half, what to do to improve the method itself performance in these areas.
2. Like the other prior-based methods, the quality of the prior matters. The author assumes smooth area the prior is relatively accurate. 
3. Like the other SDF-based methods, the reconstruction seems to still struggle with the thin structures.  
4. I noticed that in most cases the method outperforms previous methods, but sometimes it creates noise and artifacts.

### Questions
1. would it make sense to consider depth maps together to decide if the normal prior is accurate or not? For example, in most complex geometry areas such as thin structure areas, the depth is not continuous, and one may not be able to hope the normal is accurate there. 
2. what is the reason for the artifacts (which I mentioned in weakness 4), is that because without supervision the model struggles to recover the details?
3. to deal with 2, maybe add some smooth loss / geometric preserving loss on these areas that the normal prior is categorized as bad? 
4. I don't see a reason why this method only works indoor, has the author also tried it on outdoor datasets?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper proposes ND-SDF, which learns a normal deflection field to reduce the significant bias in monocular normal and depth priors. The normal deflection field can be rendered through volume rendering to further guide adaptive prior loss, ray sampling and unbiased rendering. The numerical and visualization results are compelling.

### Strengths
1. The inaccuracy and bias are widely existed in monocular depth and normal priors, therefore, the idea of exploring the uncertainty of monocular clues to improve the reconstruction performance is reasonable and valuable.
 2. The normal deflection field is effectively incorporated throughout the training process, enabling rendered deflected normal images to be supervised by estimated normals and adaptively applied in ray sampling, photometric loss, and unbiased rendering.
3. The numerical and visualization results are attractive and impressive, which highly demonstrate the effectiveness of the proposed method.
4. The ablation studies are thorough, clearly showcasing the effectiveness of each proposed module.

### Weaknesses
1. Lack of citation. A similar approach of learning rotated normals to mitigate the bias between normal priors and ground truth normals was first proposed in NC-SDF[1]. While I know that NC-SDF has not released the source code so it’s difficult to directly compare with it, an appropriate clarification is necessary to distinguish the proposed idea from NC-SDF.
2. Lack of quantitative comparisons with DebSDF. DebSDF also predicts the uncertainty of monocular priors and is able to reconstruct details such as chair legs. The numerical result of DebSDF is included in the table but visual comparison with DebSDF is absent, which is insufficient.

### Questions
See weakness.

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
5

### Summary
This paper introduces ND-SDF and proposes to learn a Normal Deflection field to represent the angular deviation between the scene normal and the normal prior.

The paper also additionally introduces a ray sampling strategy based on the deflection angle to improve the surface quality further. The paper also proposes to use an unbiased function inspired by TUVR.

### Strengths
1. The paper writing is easy to follow.

2. The experiment covers lots of different dataset for a comprehensive comparison, like Scannet, TanksandTemples, Scannet++, Replica.

3. The ablation study indicates the effectiveness of the deflection field and adaptive angle prior when compared to its base model.

### Weaknesses
Major weakness:

1. Although the dataset included is various, the compared methods are not so much comprehensive(except the Scannet). The quantitative comparison on TanksandTemples, Scannet++, Replica only includes three works in 2022(NeuRIS, MonoSDF, VolSDF) and one work in 2021(Unisurf). This leads to an insufficient experiment. For example, what about the comparison with HelixSurf, TUVR, DebSDF, H2OSDF on TanksandTemples, Scannet++, Replica? The reviewer thinks the comparison without newer baselines is insufficient on TanksandTemples, Scannet++, Replica. Although Table 1 includes most newer baselines, usually only 4 scenes in Scannet are used for indoor scene reconstruction experiments. This is why the reviewer thinks that more quantitative experiments are required here.

Details: The reviewer understands that it's not necessary to run all previous baselines in all datasets. But just place here as an example. Since the unbiased weight technique is used, the reviewer thinks **at least** TUVR(CVPR2023) is a newer baseline that should be included in both the quantitative and qualitative comparisons on TanksandTemples, Scannet++, Replica datasets. (But more comparison with other newer methods will enhance the paper's experiment part.)

2. The qualitative comparison is also insufficient (only compared with older baselines). It's better to include the qualitative comparison with newer baselines in Figure 4, Figure 11, Figure 12, Figure 13.

3. Some works have both pure MLP version and hash grid version (like MonoSDF). The performance and efficiency of different versions have some differences. Since ND-SDF includes instant-NGP in its implementation, it's better to clearly indicate the version to compare within the table. (For example, "MonoSDF(mlp)", "MonoSDF(grid)".)

Minor weakness:

4. For Section 3.4, similar ideas of better ray sampling strategy have been investigated in some previous work. Like edge-aware sampling in EaNeuS[1], GaussianRoom[2], and uncertainty-aware sampling in DebSDF. Please consider adding a brief discussion about these previous methods.

5. In Figure 2, "GT depth" and "GT Normal" should be changed to "depth prior" and "normal prior".

6. The number of selected scenes in each dataset for the experiment has not been reported.

7. The dataset conducted in the ablation study has not been reported.

### Questions
1. For Figure 3, what about the comparison with unbiased density function in NeuS, TUVR, DebSDF, HF-NeuS[3], and NeuRodin(optional, because NeuRodin is the concurrent work)[4]? These works also propose an unbiased density strategy. (visual comparison is better for good understanding)

2. In Figure 7, The deflection angle map appears to have a higher value at complex structural regions. What's the visual comparison between edge mask(EaNeuS), NCC mask(Equation 6 in NeuRIS), and uncertainty-aware mask(DDPNeRF[5], DebSDF, H2OSDF)?

3. For Equation 12 of this paper, it seems that when $\hat{\mathbf{N}}^d(\mathbf{r})$ and $\hat{\mathbf{N}}(\mathbf{r})$ perfectly fits the prior $\mathbf{N}(\mathbf{r})$, then this loss will become a perfect zero. The reviewer is concerned that this situation that causes zero loss doesn't seem to be in a good state. Is there a more comprehensive explanation about this training objective and why this training objective will work to help solve the concerns above?

4. Does the proposed normal deflection field have some advantages over the normal uncertainty field, like in DebSDF and H2OSDF?

Reference:

[3] HF-NeuS: Improved Surface Reconstruction Using High-Frequency Details. Wang et al. (Neurips 2022)

[4] NeuRodin: A Two-stage Framework for High-Fidelity Neural Surface Reconstruction. Wang et al. (Neurips 2024)

[5] Dense Depth Priors for Neural Radiance Fields from Sparse Input Views. Roessle et al. (CVPR 2022)

### Soundness
2

### Presentation
3

### Contribution
3
