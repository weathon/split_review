# Improving Gaussian Splatting with Localized Points Management

- Decision: Reject
- Avg Score: 5.33
- Scores: 5, 5, 6

## Abstract
\label{sec:abb}
Point management is a critical component in optimizing 3D Gaussian Splatting (3DGS) models, as the point initiation (e.g., via structure from motion) is distributionally inappropriate.
Typically, the Adaptive Density Control (ADC) algorithm is applied, leveraging view-averaged gradient magnitude thresholding for point densification, opacity thresholding for pruning,
and regular all-points opacity reset.
However, we reveal that this strategy is limited in tackling intricate/special image regions (\emph{e.g.}, transparent) as it is unable to identify all the 3D zones that require point densification, and lacking an appropriate mechanism to handle the ill-conditioned points with negative impacts (\eg, occlusion due to false high opacity).
To address these limitations, we propose a {\em\bf Localized Point Management} ({\shortname{}}) strategy, capable of identifying those error-contributing zones in the highest demand for both point addition and geometry calibration.
Zone identification is achieved by leveraging the underlying multiview geometry constraints, with the guidance of image rendering errors.
We apply point densification in the identified zone, whilst resetting the opacity of those points residing in front of these regions so that a new opportunity is created to correct ill-conditioned points.
Serving as a versatile plugin, {\shortname} can be seamlessly integrated into existing 3D Gaussian Splatting models.
Experimental evaluation across both static 3D and dynamic 4D scenes validate the efficacy of our \shortname{} strategy in boosting a variety of existing 3DGS models both quantitatively and qualitatively. 
Notably, \shortname{} improves both vanilla 3DGS and SpaceTimeGS to achieve state-of-the-art rendering quality while retaining real-time speeds, outperforming on challenging datasets such as Tanks \& Temples and the Neural 3D Video Dataset.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper introduces a point management method for 3D Gaussian Splatting, designed to improve point densification and correction. This approach leverages rendering errors in individual training views to identify 3D error zones by considering multi-view correspondences of 2D errors. Based on these detected error zones, point densification and opacity correction are applied to enhance the overall reconstruction quality. The results demonstrate promising improvements, with both quantitative and qualitative comparisons to the original 3D Gaussian Splatting and other prior methods.

### Strengths
The key contribution of the error-based point management technique sounds interesting and kind of novel, which seems naturally applicable to any GS-based representation and also leads to certain improvements over the standard technique used in 3DGS.

### Weaknesses
1. The method primarily relies on the assumption that regions with high errors require densification and correction. While this seems intuitively reasonable, it lacks a strong theoretical foundation, and many of the design choices appear ad-hoc without detailed mathematical explanations. Overall, the method shows some effectiveness, yet the mechanisms behind it remain unclear.

2. My main concern is on the quality. While the method offers some enhancement, the gains over standard 3D Gaussian Splatting appear incremental. Most quantitative results show PSNR improvements of less than 0.5 dB, with gains around 0.2 dB for static scenes, which is relatively marginal. Additionally, the visual comparisons reveal few notable differences, with only selected cropped examples—such as the truck windows—showing clearer improvement. These examples, however, are very few and appear carefully chosen. If the method specifically enhances quality in certain regions like transparent objects, this could be an interesting selling point, but a thorough explanation/evaluation, supported by more examples across various datasets, would be necessary to substantiate this claim.

### Questions
Overall, the method introduced in the paper has some novelty but I found it lacks a strong theoretical foundation. The quality improvement of 0.2~0.5db is also marginal. In general, while the approach offers an interesting advancement in point management for 3D Gaussian Splatting, it appears to be a relatively marginal step and still far from an optimal solution.

An additional comment: The paper "VET: Visual Error Tomography for Point Cloud Completion and High-Quality Neural Rendering" shares some similar insights with this work on leveraging visual errors for improvement in 3D point reconstruction and might be worth citing and discussing.

### Soundness
3

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
4

### Summary
This paper introduces a point management strategy for 3DGS to identify error-contributing zones. Specifically, they use LightGlue to provide pair correspondence, thus solving regions that are incorrectly located. Experiment results show that their strategy can be applied to different 3DGS methods and slightly improve the performance.

### Strengths
* The proposed method is a plug-in module. Although it takes additional computation to use LightGlue, the performance seems to have improved.
* The motivation of the proposed method is intuitive.

### Weaknesses
* One crucial weakness is that the performance improvement by introducing such a module is minor. In most experiments, the PSNR is only improved by 0.1~0.2 PSNR, and the improvements on other metrics are even less noticeable, like SSIM. This raises the question of whether introducing such a module together with LightGlue is a good solution. In addition, as the performance difference could be due to randomness, an error-bound analysis would be helpful.  
* Leveraging the pixel correspondence model may introduce additional errors since it may fail to find the correct correspondence. An analysis of such failure cases is helpful.

### Questions
* For 3D Gaussian splatting methods, the position of 3D Gaussians usually does not need to be perfect. Such flexibility allows the model to learn lightning and specular information. Thus, accurate 3D point management is less necessary, which may be the reason for the minor performance improvements in this paper. My question is whether this management helps more with the geometry modeling of 3DGS. Specifically, a quantitative comparison of surface modeling with 2DGS may help demonstrate its strength.

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
- This paper proposes a local point management (LPM) strategy to identify 3D regions that require point densification to alleviate the limitation of adaptive density control in 3D-GS.
- LPM can identify not only regions but also ill-conditioned points by leveraging multi-view geometric constraints and image rendering errors.
- LPM can be seamlessly integrated into existing 3D-GS-based methods. Experiments on static and dynamic scenes verify the proposed LPM's effectiveness.

### Strengths
1. The proposed LPM can identify 3D regions that cause incorrect rendering. For error regions, LPM densifies points or adds new Gaussians in these regions and resets the opacity of points in front of these regions.
2. By integrating LPM into existing 3D/4D GS methods, the rendering quality of static or dynamic scenes can be improved.

### Weaknesses
1. 3D zone identification requires the partial assignment predicted by LightGlue, which leads to some problems:
  - LPM cannot handle non-overlapping regions regions between two views.
  - Error and missing matches may harm LPM.

2. Although LPM is evaluated on Neural 3D Video dataset, for dynamic objects, the error region may move over time, and LPM lacks a mechanism to handle this situation. As shown in Figures 4 and 6, the improvement focuses on the static part. 

3. Lacking some details. For example,
  - As shown in L202, how are the paired region adaptive adjustments?
  - The details formula of rCone in L208
  - What is the interval for applying LPM? Is that apply LPM every 100 iterations just like the densified interval in 3D-GS?

4. Lacking discussion about limitations and failure cases.

### Questions
See `Weaknesses`.

### Soundness
3

### Presentation
3

### Contribution
3
