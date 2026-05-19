### Summary

This paper presents a method for HDR reconstruction from casual videos captured with auto-exposure. The proposed method is a one-stage approach that jointly optimizes the HDR Gaussian Splatting representation, camera trajectory, exposure time, and camera response function. The authors claim that their method is robust to the varying exposure time and motion blur in casual videos. The experimental results show that the proposed method outperforms existing approaches in novel view synthesis, image deblurring, and HDR editing tasks.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

The proposed method is a one-stage approach that jointly optimizes the HDR Gaussian Splatting representation, camera trajectory, exposure time, and camera response function. This is different from existing methods that require multiple stages of optimization or manual tuning of exposure times.

The experimental results show that the proposed method outperforms existing approaches in novel view synthesis, image deblurring, and HDR editing tasks. The authors also provide a new dataset for evaluating HDR reconstruction methods.

### Weaknesses

#### Some Related Works


#### comment

The proposed method is a one-stage approach that jointly optimizes the HDR Gaussian Splatting representation, camera trajectory, exposure time, and camera response function. This is different from existing methods that require multiple stages of optimization or manual tuning of exposure times.

The experimental results show that the proposed method outperforms existing approaches in novel view synthesis, image deblurring, and HDR editing tasks. The authors also provide a new dataset for evaluating HDR reconstruction methods.

The proposed method is a one-stage approach that jointly optimizes the HDR Gaussian Splatting representation, camera trajectory, exposure time, and camera response function. This is different from existing methods that require multiple stages of optimization or manual tuning of exposure times.

The experimental results show that the proposed method outperforms existing approaches in novel view synthesis, image deblurring, and HDR editing tasks. The authors also provide a new dataset for evaluating HDR reconstruction methods.

### Suggestions

The paper introduces a one-stage approach for HDR reconstruction from casual videos, which is a notable departure from existing multi-stage methods. However, the paper could benefit from a more detailed analysis of the computational cost associated with this joint optimization. Specifically, the authors should provide a breakdown of the time complexity for each component of the optimization process, including the Gaussian Splatting representation, camera trajectory estimation, exposure time optimization, and camera response function fitting. This analysis should also compare the computational cost of the proposed method with existing approaches, highlighting the trade-offs between the unified optimization and the potential for increased computational burden. Furthermore, it would be beneficial to discuss the memory requirements of the proposed method, as this could be a limiting factor for processing high-resolution scenes or large video sequences. A clear understanding of the computational and memory requirements is crucial for assessing the practical applicability of the method.

While the paper claims robustness to varying exposure times and motion blur, it would be valuable to provide a more rigorous evaluation of the method's performance under different types of motion blur. The current evaluation seems to focus on general blur, but it is important to understand how the method performs under specific types of motion, such as rotational blur or out-of-focus blur. The authors should consider including experiments that specifically target these types of blur and analyze the method's performance in terms of both reconstruction quality and deblurring accuracy. Additionally, it would be helpful to investigate the sensitivity of the method to the severity of motion blur, i.e., how the performance degrades as the motion blur becomes more severe. This analysis would provide a more comprehensive understanding of the method's limitations and its applicability to real-world scenarios.

Finally, the paper introduces a new dataset for evaluating HDR reconstruction methods, which is a valuable contribution. However, the authors should provide more details about the characteristics of the dataset, such as the range of exposure times, the types of motion blur, and the scene complexity. It would also be beneficial to include a comparison of the dataset with existing HDR datasets, highlighting the unique aspects of the proposed dataset and its potential for advancing the field. Furthermore, the authors should discuss the limitations of the dataset, such as the size and diversity of the scenes, and how these limitations might affect the generalizability of the results. A thorough analysis of the dataset's characteristics and limitations is essential for ensuring the reproducibility and reliability of the results.

### Questions

See weakness.

### Rating

6

### Confidence

4

**********
