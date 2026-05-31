## Human Reviewer 1

### Summary
This paper focused on a shape-adaptive guidance signal for promptable segmentation of cortical sulci. The authors proposed a curvature-aware encoding of user clicks that can provide the underlying cortical geometry. The results show improving labeling accuracy with minimal user prompts. The proposed method highlights the spherical representation; the surfaces are mapped to the unit sphere with neuroimaging pipelines. Then it includes an interactive framework and a shape-adaptive guidance signal.

### Strengths
- The design of the simulated guidance signal for prompt segmentation is new and attractive for sulci analysis.
- The promptable segmentation for cortical surface segmentation is critical as interactive analysis for subregions are demanding in the domain. 
- The results show improved accuracy for tiny structures in the challenging sulci.

### Weaknesses
- The design of curvation estimation can be more clarified. Such as the curvature estimation on discrete meshes can be noisy in shallow sulci. The errors could affect the propagation speed function and mislead the signal.
- The segmentation can only provide prompt-based binary segmentation right? No multi-label, semantic differentiations?
- In limited regions, the method could be more validated beyond the LPFC patterns.
- The real cortical surface segmentation data is hard to get, but the studies used in this work is relatively too small. In the future, a larger cohort evaluation might be needed.

### Questions
Questions and suggestions are associated with the weakness section. Thanks.

### Soundness
3

### Presentation
3

### Contribution
3

### Rating
6

### Confidence
5

---

## Human Reviewer 2

### Summary
This paper introduces a novel shape-adaptive guidance signal for interactive segmentation of cortical sulci, particularly focusing on small and shallow sulci in the lateral prefrontal cortex. The authors leverage spherical convolutional neural networks and propose a curvature-aware encoding scheme based on the eikonal equation, which incorporates mean curvature to guide segmentation more effectively than traditional equidistance-based methods. The method is validated on a dataset of 72 subjects with 17 manually labeled sulci, showing that even a single user click using the proposed guidance signal significantly improves segmentation accuracy compared to fully automatic methods and simpler interactive schemes.

### Strengths
1. The paper is well-motivated by the challenges in labeling shallow sulci and the limitations of automatic methods.

2. The method requires minimal user input and shows promise for reducing annotation effort in large-scale studies.

3. The paper provides a thorough mathematical formulation of the guidance signal encoding.

4. The use of mean curvature in the eikonal equation to encode user clicks is a novel approach that adapts to the anatomical structure of cortical folds.

### Weaknesses
1. The method is evaluated only on LPFC sulci, and its generalizability to other cortical regions is not explored. Moreover, the segmentation is binary per sulcus, which may be inefficient when labeling multiple sulci simultaneously.

2. Although the method is interactive, its performance likely depends on the quality and location of user clicks. The paper does not report real-world user studies to validate the simulated click strategy.

3. The performance of WGDT is sensitive to parameters such as $\sigma$ and $k$, requiring empirical tuning to select optimal values. This may limit out-of-the-box usability for new datasets.

4. While visual comparisons are included, the paper lacks discussion of user interface design and real-time feedback, both of which are important for practical deployment.

### Questions
1. The method is evaluated only on LPFC sulci. Have you tested it on other small or shallow sulci out of the box? Since the segmentation is binary per sulcus, this should be conceptually straightforward, similar to SAM.

2. Why were only fully automatic methods used as baselines? Could other interactive segmentation approaches—such as SAM-based projections—be adapted for comparison?

3. Were the automatic baselines retrained or fine-tuned on the same dataset, or were they used as-is?

4. The paper mentions tuning $\sigma$ and $k$ for WGDT. Is there a principled way to select these parameters, or is tuning entirely empirical?

5. How sensitive is the WGDT signal to inaccuracies in curvature estimation? Could noise or bias in curvature maps degrade propagation quality?

6. Is the curvature-based speed function empirically justified beyond visual inspection? Have you compared it with other geometric cues, such as sulcal depth or convexity?

7. Is the model capable of providing real-time feedback during annotation yet? If not, how close is it to achieving this? Please specify the latency and computational requirements per user click.

8. Is there a point of diminishing returns in accuracy after a certain number of clicks? How does performance after saturation compare to expert annotations?

9. How does the model perform on atypical brains (e.g., pediatric or pathological cases)? Is the curvature-based propagation robust to such anatomical variability?

### Soundness
2

### Presentation
2

### Contribution
3

### Rating
4

### Confidence
4

---

## Human Reviewer 3

### Summary
The work proposes an improvement to interactive segmentation methods for cortical sulcal labeling. Given user clicks, it proposes a new prompting strategy in which click signals are propagated along surface curvature maps. This provides sulcal context to the segmentation model. The authors compare the shape-guided representation to simpler encoding methods (disk and radial distance–based) and benchmark against automatic cortical segmentation baselines. They demonstrate improved performance over simple encodings and standard baseline segmentation methods.

### Strengths
The paper tackles an important challenge. Registration-based cortical parcellations often lack accuracy, while newer learning-based surface segmentation methods lack substantial training data to support generalization across diverse folding patterns. This work explores an interactive improvement that reduces manual labeling effort, enabling larger and more detailed shallow sulcal parcellation maps to support better cortical analysis tools.

The motivation is clear and the proposed method is straightforward. Overall, the text is easy to follow.

### Weaknesses
The method is trained and evaluated on the same subset of 17 labels. Generalization to new tasks is key in interactive segmentation methods, but the paper does not evaluate performance for previously unseen regions.

For interactive tools, efficiency is also an important consideration. Yet no runtime or real-use performance stats are provided.

The baseline setup in Section 4.2 is unclear on whether these methods are retrained on the same 17 labels and data splits outlined in Section 3.3, or if they are used off the shelf. While no prior interactive sulcal-surface labeling baselines exist, numerous interactive image segmentation tools do. A comparison against a universal model such as SAM, using planar projections of sulcal and curvature maps as input, would help clarify whether a specialized approach is necessary.

The paper suggests that the chosen $\sigma$ values for the ADT and disk-based guidance signals are sufficiently small to capture fine-grained sulcal branches. However, many interactive segmentation methods perform well using single-pixel click encodings. It is not convincing that the selected $\sigma$ values are small enough, as Figure 4 shows continued improvement as ADT $\sigma$ decreases.

The introduction provides a solid overview but is overly long. The contribution could be presented far more quickly, with background details moved to a structured Related Work section.

Figures also need attention. The plots in Figure 4 are hard to interpret (some x-axis labels are missing, the scaling is not optimal, improvements are masked by stacked bars). Figure 2 introduced negative clicks, but there is no in depth methodological or experimental discussion of this.

Overall, while the problem is important, the focus on shallow sulcal regions gives the work a relatively narrow scope. Many cortical labeling tasks involve regions that span multiple sulci or gyri or rely on feature maps other than the three considered here.

### Questions
Line 335: "To ensure labels were constrained to sulcal regions, outputs with negative curv values were discarded" Could the authors clarify this step? It seems important but is not clearly explained

Since the same targets are used for evaluation, how does the model perform without any signal guidance at all (i.e. when trained directly for multiclass segmentation)?

In Figure 6, it seems that manual labels closely follow sulcal map borders. Instead of solving the eikonal equation with a speed function, why not simply mask the ADT or disk signal using the positive sulcal map?

### Soundness
2

### Presentation
2

### Contribution
2

### Rating
2

### Confidence
4