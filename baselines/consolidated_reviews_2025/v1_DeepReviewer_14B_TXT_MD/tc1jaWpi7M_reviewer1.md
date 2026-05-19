### Summary

This paper introduces an iterative method, named MaskComp, for object completion. The proposed method relies on an alternating optimization between generating complete objects and refining object masks. To complete the partial objects, the authors adopt ControlNet, where they input the partial object images and the corresponding partial object masks. To refine the masks, the authors leverage the off-the-shelf segmentation model, SAM, to obtain the object masks from the generated complete objects. The whole iterative object completion and mask refinement process is stopped by the mask voting technique. The authors demonstrate the effectiveness of the proposed MaskComp in object completion via two datasets, AHP and DYCE.

### Soundness

2 fair

### Presentation

3 good

### Contribution

2 fair

### Strengths

* The authors address the object completion problem by iteratively generating complete objects and refining the object masks. The proposed method is simple and intuitive. 
* The authors demonstrate the effectiveness of the proposed MaskComp on two datasets, AHP and DYCE.

### Weaknesses

#### Some Related Works


#### comment

 * The proposed method is based on the simple and intuitive idea of iteratively generating complete objects and refining the object masks. 
* The ablation study does not include the effects of the number of iterations and the number of sampled images. 
* The authors do not provide the comparison of the proposed method with the state-of-the-art methods, such as ControlNet, Kandinsky 2.1, and Stable Diffusion 2.1, in terms of the runtime.

### Suggestions

The core idea of iteratively refining object completion through alternating generation and mask refinement is indeed intuitive, but the paper could benefit from a more rigorous analysis of the method's limitations and potential failure modes. For instance, the paper should explore scenarios where the initial mask is significantly inaccurate or when the object has complex occlusions. It would be beneficial to analyze how the iterative process behaves in these challenging cases, and whether the method can recover from poor initializations. Furthermore, the paper should investigate the sensitivity of the method to the choice of the object encoder and decoder. A more detailed analysis of the impact of different encoder/decoder architectures on the quality of the completed objects would strengthen the paper. The authors should also consider exploring alternative mask refinement techniques beyond the voting method, as this could potentially lead to further improvements in the quality of the completed objects.

Regarding the ablation study, it is crucial to provide a more comprehensive analysis of the impact of the number of iterations and the number of sampled images. The current study only shows the performance at a specific iteration and with a fixed number of sampled images. A more detailed analysis should include a plot showing the performance (e.g., FID score) as a function of the number of iterations. This would help to understand the convergence behavior of the proposed method and to determine the optimal number of iterations. Similarly, the ablation study should explore a wider range of the number of sampled images and analyze its impact on the performance and computational cost. It is important to understand the trade-off between the number of sampled images and the quality of the completed objects. The authors should also provide a more detailed analysis of the computational cost of the proposed method, including the runtime of each component (e.g., ControlNet, SAM) and the overall runtime. This would help to understand the efficiency of the proposed method and to compare it with other state-of-the-art methods.

Finally, the paper should include a more thorough comparison with state-of-the-art methods, such as ControlNet, Kandinsky 2.1, and Stable Diffusion 2.1, not only in terms of the runtime but also in terms of the quality of the completed objects. The current comparison only focuses on the runtime, but it is important to compare the proposed method with other state-of-the-art methods in terms of the quality of the completed objects (e.g., FID score, user study). The authors should also consider comparing the proposed method with other object completion methods, if available. This would help to understand the advantages and disadvantages of the proposed method compared to other existing approaches. The paper should also discuss the limitations of the proposed method and potential directions for future research. This would help to understand the scope of the proposed method and to identify areas for further improvement.

### Questions

* The proposed method is based on the simple and intuitive idea of iteratively generating complete objects and refining the object masks. 
* The ablation study does not include the effects of the number of iterations and the number of sampled images. 
* The authors do not provide the comparison of the proposed method with the state-of-the-art methods, such as ControlNet, Kandinsky 2.1, and Stable Diffusion 2.1, in terms of the runtime.

### Rating

5: marginally below the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
