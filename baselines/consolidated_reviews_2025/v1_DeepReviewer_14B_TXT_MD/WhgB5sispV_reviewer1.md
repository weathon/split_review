### Summary

This paper proposes a 4D Gaussian Splatting representation for dynamic scenes. The 3D Gaussian from previous work is reinterpreted as a spatial marginalization of the 4D Gaussian proposed in this work. The 4D Gaussian is parameterized by anisotropic ellipses that can rotate arbitrarily in space and time, as well as view-dependent and time-evolved appearance represented by the coefficient of 4D spherindrical harmonics. The optimization of the 4DGS is highly efficient and the novel view rendering can be done in real-time. The experiments across various monocular and multi-view scenarios demonstrate the superior performance of 4DGS in both rendering quality and speed.

### Soundness

4 excellent

### Presentation

4 excellent

### Contribution

3 good

### Strengths

The paper is well-written and easy to follow.
The idea of 4D Gaussian Splatting is well-motivated and technically sound. The 4D rotation is a novel contribution.
The rendering quality and speed are significantly improved compared to previous methods.

### Weaknesses

#### Some Related Works


#### comment

The failure cases are missing. It is unclear what kind of scenes this method can fail to represent. For example, the Plenoptic Video dataset contains a lot of thin structures and small textures, like the books in the bookstore and the windows in the hotel room. It is unclear if the proposed method can handle these cases well or not. Specifically, the method's ability to capture high-frequency spatial details and rapid temporal changes in these complex regions needs further investigation. The paper should include a discussion of the limitations of the method, including specific types of scenes or motions that may cause it to fail.

The quantitative results are a little bit suspicious. For example, in Table 2, the LPIPS of the proposed method is significantly lower than other methods, which is surprising. The large improvement in LPIPS, particularly compared to methods where it was previously a weakness, warrants further scrutiny. It is important to understand if this improvement is due to the method's inherent capabilities or if there are other factors at play. The paper should provide a more detailed analysis of the LPIPS results, including a discussion of why this metric shows such a significant improvement.

The densification and pruning strategy is not explained in detail. The densification and pruning strategy from 3DGS is applied to 4DGS with some minor modifications. However, the details of the modifications are not provided. The paper should provide a more detailed explanation of how the densification and pruning strategies are adapted for the 4D Gaussian representation, including the specific modifications made and the rationale behind them. Without these details, it is difficult to assess the effectiveness of the method.

### Suggestions

The paper would benefit from a more thorough analysis of failure cases. The authors should include a qualitative discussion of scenarios where the 4DGS method struggles, such as scenes with very thin structures, high-frequency textures, or extremely rapid motion. For example, it would be useful to see how the method performs on scenes with complex occlusions or sudden changes in lighting. The authors could also investigate the impact of different types of motion, such as rotational versus translational motion, on the quality of the reconstruction. Including these failure cases would provide a more complete picture of the method's limitations and help guide future research.

To address the concerns about the LPIPS results, the authors should provide a more detailed analysis of why their method achieves such a significant improvement. It would be helpful to include a breakdown of the LPIPS scores per scene or per type of scene complexity. This would help to identify if the improvement is consistent across all types of scenes or if it is more pronounced in certain scenarios. Furthermore, the authors should investigate whether the improved LPIPS score is correlated with improvements in other metrics, such as PSNR or SSIM. This would provide a more comprehensive understanding of the method's performance and help to validate the LPIPS results. It would also be beneficial to analyze the per-pixel errors and identify any patterns or biases in the reconstruction.

The paper should include a more detailed explanation of the densification and pruning strategy for 4DGS. The authors should provide a step-by-step description of how the 3D densification and pruning methods are adapted for the 4D case, including the specific modifications made and the rationale behind them. For example, how are the splitting and pruning thresholds determined in the 4D case? How does the method handle the temporal dimension during densification and pruning? The authors should also discuss the computational cost of these operations and how they impact the overall efficiency of the method. Providing these details would make the method more reproducible and allow for a more thorough evaluation of its effectiveness.

### Questions

What is the training time of the proposed method compared to 3DGS?
How does the number of Gaussians of the proposed method compare to 3DGS?

### Rating

6: marginally above the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
