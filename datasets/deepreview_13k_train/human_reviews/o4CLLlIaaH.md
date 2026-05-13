# Learning Robust Generalizable Radiance Field with Visibility and Feature Augmented Point Representation

- Decision: Accept
- Scores: 8, 6, 6, 6

## Abstract
This paper introduces a novel paradigm for the generalizable neural radiance field (NeRF). Previous generic NeRF methods combine multiview stereo techniques with image-based neural rendering for generalization, yielding impressive results, while suffering from three issues. First, occlusions often result in inconsistent feature matching. Then, they deliver distortions and artifacts in geometric discontinuities and locally sharp shapes due to their individual process of sampled points and rough feature aggregation. Third, their image-based representations experience severe degradations when source views are not near enough to the target view. To address challenges, we propose the first paradigm that constructs the generalizable neural field based on point-based rather than image-based rendering, which we call the Generalizable neural Point Field (GPF). Our approach explicitly models visibilities by geometric priors and augments them with neural features. We propose a novel nonuniform log sampling strategy to improve both rendering speed and reconstruction quality. Moreover, we present a learnable kernel spatially augmented
with features for feature aggregations, mitigating distortions at places with drastically varying geometries. Besides, our representation can be easily manipulated. Experiments show that our model can deliver better geometries, view consistencies, and rendering quality than all counterparts and benchmarks on three datasets in both generalization and finetuning settings, preliminarily proving the potential of the new paradigm for generalizable NeRF.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a novel paradigm for constructing a generalizable neural field based on point-based rendering, which addresses the challenges of occlusions, distortions, and degradation in image-based representations. The proposed approach combines geometric priors and neural features to eliminate occlusions in feature-fetching, and a nonuniform log sampling strategy and a learnable kernel spatially augmented with features for improved rendering speed and reconstruction quality. The authors demonstrate the effectiveness of their approach on a variety of datasets, showing improved generalization and robustness to occlusions and distortions compared to previous methods. Overall, the paper presents a promising approach for learning robust and generalizable radiance fields.

### Strengths
Overall the paper is nicely presented and introduce several novel components including: 

- The proposed approach combines geometric priors and neural features to eliminate occlusions in feature-fetching explicitly in the rendering process, which is a novel contribution to the field.
- The authors introduce a nonuniform log sampling strategy and a learnable kernel spatially augmented with features, which is a novel approach to improving rendering speed and reconstruction quality.

The method is properly evaluated with some ablation study.

### Weaknesses
The paper proposed a new pipeline with several novel designs over the existing methods, however many of the designs are not validated and some of the claims are not strongly backed by their existing experiments:
1. The exact definition of convergence speed is vague in Table 2, and is not explained in details. Making the results in this table questionable. The reported convergence speed lacks a clear definition, making it difficult to interpret the results. It's unclear what metric is used to measure convergence, and how it relates to the overall performance of the model. A more rigorous definition and explanation are needed to validate the claims made in Table 2.
2. Separating low level and high level features sounds intuitive but however is not validated and the necessity of such design is thus questionable. The paper lacks a thorough ablation study to justify the separation of low-level and high-level features. While the intuition is that low-level features capture color and edges and high-level features capture semantic information, this is not explicitly validated. The necessity of this separation is not clear, and it's possible that a single feature encoding could achieve similar or better results. An ablation study comparing different feature encoding strategies is needed.
3. No quantitative validation on claims such as "better geometry" and "occlusion awareness". The paper claims better geometry and occlusion awareness, but lacks quantitative metrics to support these claims. There is no comparison of depth maps or other geometric metrics with existing methods like MVSNeRF and NeuRay. Without quantitative validation, these claims are not strongly supported by the experiments.

### Questions
1. Visualize the test PSNR curve instead of just stating "Convergence Speed" as in Table 2 would be more convincing, intuitive and easier to follow.
2. Some modules are not well ablated and analyzed - \eg high-low-level feature encoding.
3. It would be nice to present some metric and quantitatively prove the quality in geometry (esp. occlusion awareness). At least depth error should be compared with MVSNeRF and NeuRay.
4. In related works, Generalizable Neural Field. section: "All the above can be seen as image-based neural rendering". I think this might be inaccurate- I believe the finetuned/unfinetuned MVSNeRF / GeoNeRF / NeRFusion can aggregate multi view information and do not require original images for further use (though MVSNeRF fetches image color for rendering in some versions). Could you clarify on this? Also I believe the section is not extensive enough. The authors should also talk specifically about other point-based neural rendering methods, maybe in a dedicated section.
5. Maybe: considering other point-based methods as ft baselines and include in the main paper.
6. Typos and minor fixes:
  - Table 2: Convergeuce -> Convergence; Missing/misplaced underline under 1.04s
  - Citation format should be fixed throughout the paper.

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
The work propose a generalizable point-based NeRF for novel-view synthesis tasks. The point cloud is first initalized from classical MVS technique. A U-Net is trained to extract feature for the input views, which is aggregated into the points in a visibility-aware and learnable manner. To do volume rendering, query coordinates are sampled per the point density to improve efficiency. The query coordinates search K-nearest neighbor from the feature point cloud to form the query point feature, which is then map to density and color for volume rendering.

### Strengths
The quantitative improvement is solid. I believe many of the proposed modules can be plug into point-based rendering system to boost results.

### Weaknesses
The visibility score in Eq4 is not well designed. The score actually decay more quickly for point ahead of the depth ($P_z < D_{i,xy}$). Consider two points with $P_z^{(back)} = D_{i,xy} + \epsilon$ and $P_z^{(front)} = D_{i,xy} - \epsilon$, their scores are:
- $score^{(back)} = 1 - \frac{|D_{i,xy} + \epsilon - D_{i,xy}|}{D_{i,xy} + \epsilon} = \frac{D_{i,xy}}{D_{i,xy} + \epsilon}$
- $score^{(front)} = 1 - \frac{|D_{i,xy} - \epsilon - D_{i,xy}|}{D_{i,xy} - \epsilon} = \frac{D_{i,xy} - 2\epsilon}{D_{i,xy} - \epsilon}$

When $\epsilon > 0$, $score^{(front)} < score^{(back)}$. In addition, the score is claimed to be naturally constrainted in range of 0 and 1, but it is not the case when $P_z < 0.5 D_{i,xy}$ (become negative).

I found some qualitative results from the baseline is better. In Fig3, the head of the ship and the sea in the ship scene, the table of the durian scene are better recovered by ENeRF. In Fig4, the reconstructed ground dirt in the BlendedMVS is overly smooth while the baseline ENeRF can recover more detail texture. What would be the reason of these? Is it because the dependent MVS point cloud?

Is the proposed method sensitive to the initial points?

Paper proofread:
- Missing parentheses for the $\exp$ in Sec3.3 last paragraph.
- The reference to the Figure in Sec.4.2's 5th sentence is missing.

### Questions
I found some qualitative results from the baseline is better. In Fig3, the head of the ship and the sea in the ship scene, the table of the durian scene are better recovered by ENeRF. In Fig4, the reconstructed ground dirt in the BlendedMVS is overly smooth while the baseline ENeRF can recover more detail texture. What would be the reason of these? Is it because the dependent MVS point cloud? 

Is the proposed method sensitive to the initial points?

Paper proofread:
- Missing parentheses for the $\exp$ in Sec3.3 last paragraph.
- The reference to the Figure in Sec.4.2's 5th sentence is missing.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper presents a novel paradigm in generalizable Neural Radiance Field (NeRF) research by introducing the Generalizable Neural Point Field (GPF). Unlike traditional NeRF methods that utilize image-based rendering, this work focuses on point-based rendering. The paper claims to address several prevalent issues with the existing image-based methods, including occlusion-related problems, artifacts, and performance drop-offs with varying view distances.

### Strengths
- Originality: The Generalizable Neural Point Field (GPF) is a fresh perspective in NeRF research, emphasizing point-based over image-based rendering.
- Quality: The proposed methods exhibit high-quality research and innovation, from the nonuniform log sampling strategy to the feature-augmented learnable kernel.
- Clarity: The paper's overall structure is clear, presenting a logical flow of ideas and discussions.
- Significance: If the claims are validated further, this research could serve as a benchmark in the NeRF domain.

### Weaknesses
 - Lack of Detailed Explanations: Some sections, especially the technical components, could use more in-depth explanations or visual aids.
- Dependency on Other Technologies: The initial dependency on PatchmatchMVS might limit the paper's approach from being a standalone solution.
- Limited Experimentation: Testing on only three datasets might not showcase the full potential or limitations of the method.
- Complexity: The approach's intricate nature might pose scalability or efficiency challenges that haven't been addressed comprehensively.

### Questions
- Could the authors expand on the visibility-oriented feature fetching, possibly with diagrams, for better clarity? Figure (b) alone is not clear enough.
- Given the reliance on PatchmatchMVS for the initial point scaffold, how does this affect the scalability or deployment of GPF in diverse scenarios? The authors also mention in the limitation section that they want to propose a NeRF-based initialization module that can be trained from scratch. Please comment on how you plan to achieve this.
- Can the authors comment on potential efficiency challenges due to the method's complexity? For example, compare the rendering speed with E-NeRF.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes to construct the generalizable neural field, called the generalizable neural Point Field (GPF), based on point-based rendering. This approach explicitly models by geometric priors and augments it with neural features to eliminate occlusions in feature-fetching. A nonuniform log sampling strategy is proposed to improve both rendering speed and reconstruction quality. Moreover, this paper presents a learnable kernel spatially augmented with features for feature aggregations, mitigating distortions at places with drastically varying geometries. Experiments show that the proposed model can deliver better geometries, view consistencies, and rendering quality on three datasets in both generalization and finetuning settings.

### Strengths
This paper proposes a Generalizable neural Point Field (GPF) for building generalizable NeRF based on point-based neural rendering. This paradigm outperforms existing image-based benchmarks and yields state-of-the-art performance on generic reconstructions.

This method explicitly models the visibilities by geometric priors and augments it with neural features, which are then used to guide the feature fetching procedure to better handle occlusions.

A nonuniform log sampling strategy is proposed based on the point density prior, and perturbations to sampling parameters are imposed for robustness, which not only improves the reconstructed geometry but also accelerates the rendering speed.

A spatially feature-augmented learnable kernel as feature aggregators is presented, which is proven to be effective for generic abilities and geometry reconstruction at drastically shape-varying areas.

### Weaknesses
This reviewer has the following concerns.

The primary contribution claimed by this paper is the introduction of the first generalizable NeRF based on point-based neural rendering. An existing point-based method is PointNeRF, which is a per-scene optimization method.
Section F.1 discusses the comparison between GPF and PointNeRF, which is helpful. What does the entry "Ours" represent in the table below Figure 17? If it refers to the model after fine-tuning, what are the results without fine-tuning?

Upon closer examination of the comparison with PointNeRF, this paper states that the improvement is attributed to hierarchical fine-tuning strategies. I am wondering about the runtime required for fine-tuning. PointNeRF can be optimized from scratch in approximately 40 minutes. Additionally, is pretraining of the generalizable NeRF necessary? It seems that the primary advantage of this method over PointNeRF lies in its superior fine-tuning strategy.

The log sampling strategy is simply a handcrafted sampling distribution around the surface, which may not be considered a significant technical contribution. This strategy can only be applied if the depth prior is known.

It is important to discuss the comparison between the proposed method and the recently introduced efficient Gaussian-splatting representation. What are the advantages of the proposed method?

### Questions
Please clarify the comparison with PointNeRF and explain the key factors that make this method superior to PointNeRF.

Please discuss the comparison between this method and Gaussian-splatting.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
