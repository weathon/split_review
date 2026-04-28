# Improving the Convergence of Dynamic NeRFs via Optimal Transport

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 6

## Abstract
Synthesizing novel views for dynamic scenes from a collection of RGB inputs poses significant challenges due to the inherent under-constrained nature of the problem. To mitigate this ill-posedness, practitioners in the field of neural radiance fields (NeRF) often resort to the adoption of intricate geometric regularization techniques, including scene flow, depth estimation, or learned perceptual similarity. While these geometric cues have demonstrated their effectiveness, their incorporation leads to evaluation of computationally expensive off-the-shelf models, introducing substantial computational overhead into the pipeline. Moreover, seamlessly integrating such modules into diverse dynamic NeRF models can be a non-trivial task, hindering their utilization in an architecture-agnostic manner. In this paper, we propose a theoretically grounded, lightweight regularizer by treating the dynamics of a time-varying scene as a low-frequency change of a probability distribution of the light intensity. We constrain the dynamics of this distribution using optimal transport (OT) and provide error bounds under reasonable assumptions. Our regularization is learning-free, architecture agnostic, and can be implemented with just a few lines of code. Finally, we demonstrate the practical efficacy of our regularizer across state-of-the-art architectures.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work presents a regularizer for dynamic NeRFs to improve the rendering quality. Specifically, it is based on the hypothesis that the pixel intensity distribution of a scene, which is rendered from a specific fixed camera view, should remain consistent within short time intervals. Then, this work uses the dissimilarity measure between pixel intensity distributions as the alternative to the pixel-to-pixel distance function to formulate the problem as an Optimal Transport (OT) problem. Additionally, this work employs a sliced-Wasserstein approximation to reduce the OT computation complexity from O(n^3) to O(nlogn), making the proposed regularizer more lightweight as compared to baselines. The experiments on 3 dynamic scene reconstruction datasets valide that the proposed regularizer can further improve SOTA dynamic NeRF models' rendering quality.

### Strengths
> + Well-Motivated: I think the central hypothesis, i.e., the pixel intensity distribution of a scene should remain approximately consistent within short time intervals, is valid for most cases and existing dynamic scene datasets unless scenes with objects in very high-speeds. Also, the related works are discussed in an organized way. Specifically, the regularizers in static NeRF as disentangling camera motion from object motion inherently constitute an ill-posed problem, and existing regularizers in dynamic NeRFs with DNN-based solutions are costly and face the domain gap issue. Thus, a lightweight regularize for dynamic NeRF is highly desirable.

> + Interesting problem formulation: I am not familiar with optimal transport (OT) problems, but this work seems to be the first one to formulate the dynamic NeRF regularization as an OT problem and further optimize the corresponding computation complexity in OT to make it lightweight.

> + Solid experiments: the experiments consider 3 dynamic NeRF datasets and 5 dynamic NeRF models, showing impressive improvement across different datasets.

### Weaknesses
 > + Discussion on Failure Cases: Since the hypothesis of this work is that the pixel intensity distribution of a scene should remain approximately consistent within short time intervals, failure cases may happen when some high-speed objects appear in the scene. However, the limitation section did not add sufficient details about it. It would be better if the author could provide some analysis or experimental results to provide a more direct way to show when the hypothesis will be invalid (e.g., under what speed or in some specific scenes). Specifically, the paper lacks a quantitative analysis of the temporal window within which the intensity distribution consistency assumption holds. It's unclear how the chosen time interval for calculating the sliced-Wasserstein distance relates to the actual speed of objects or camera motion. The authors should provide a more rigorous treatment of the temporal sensitivity of their method, perhaps by showing performance degradation as the time interval increases for a fixed scene or by analyzing how the method performs with different motion magnitudes.

> + Comparision with the Strongest Baseline: From Table 1, HexPlane seems to be the strongest baseline, but it was not listed in Tab. 2 and Fig. 3. Could the author add more details about it? It is important to understand why the method was not compared against this baseline, especially given its strong performance. The authors should clarify if this is due to implementation difficulties or if there are fundamental reasons why their method might not be directly comparable. A more thorough analysis of the baseline's performance, even if it's not directly comparable, would be valuable.

> + Comparison of Efficiency Metrics: The author claimed that their proposed regularization is more efficient. It could be more solid to add the training time to better verify it. The claim of efficiency is currently not well supported by empirical evidence. While the authors mention the computational complexity of the optimal transport calculation, this does not directly translate to training time. The authors should provide a detailed breakdown of the computational cost, including the time spent on the sliced-Wasserstein calculation, backpropagation, and other relevant steps. This would allow for a more accurate comparison with existing regularization methods.

### Questions
Minor question: this regularizer seems to be compatible with all dynamic NeRF models because it is defined in the pixel space. Currently, there are more dynamic NeRF models based on Gaussian Spatting (e.g., https://arxiv.org/abs/2308.09713 or https://arxiv.org/abs/2310.08528), will such a new representation cause new challenges in applying the proposed regularize from the optimization side?

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
This paper proposes a regularization method to enhance the quality of novel view synthesis for dynamic NeRFs. The regularization is based on the notion that the light intensity distribution should remain approximately constant from a fixed camera view within short time intervals. Specifically, the method implements distance metrics such as sliced-Wasserstein and serves as a robust plug-in to improve the quality for several state-of-the-art methods across multiple dynamic scene view synthesis benchmarks.

### Strengths
- The intuitive idea of exploiting light distribution consistency.
- The proposed regularization is easy to implement and can be integrated into various methods.

### Weaknesses
 - Baseline comparison. Previous literature, including random background compositing [2], additional metric depth supervision [3] from iPhone sensor, and surface sparsity regularizer [4], presents more advanced regularization techniques. Quantitative results reported in Table 3 and Figure 10 in [1] suggest that the baseline methods Nerfies and HyperNeRF gain a significant performance boost from these techniques. The paper does not provide a direct comparison of the proposed regularization against these existing methods. It is unclear how well the proposed regularization performs in terms of quantitative metrics such as PSNR, SSIM, and LPIPS when compared to these established techniques. A thorough quantitative and qualitative comparison would help to establish the effectiveness of the proposed method.

- Robustness in combination with other regularizations. The paper does not explore the potential benefits of combining the proposed regularization term with those mentioned above [1,2,3]. It is uncertain whether these regularization terms are complementary or if they might interfere with each other. An ablation study investigating the performance of the proposed method in conjunction with other regularization techniques would provide valuable insights into its robustness and general applicability.

- Efficiency. The paper lacks data points illustrating the speed and memory usage of the proposed method. While the intuitive idea suggests potential computational benefits, the actual computational overhead introduced by the proposed regularization is not quantified. Providing data on training time, inference time, and memory footprint would allow for a more comprehensive evaluation of the method's practicality.

### Questions
- How does the proposed method compare to more recent regularization techniques?
- Can the proposed method be combined with existing regularization techniques?
- Do we need to compromise performance (reduce batch size to fit into GPU memory) and/or speed (increase per-iteration time) to enable the proposed method?

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces a regularization method for dynamic view synthesis by reformulating the regularization task to an optimal transportation problem. The paper assumes that, for a fixed camera pose, the intensity of the pixel of images within a small interval should be constant. Hence, the authors propose to minimize the divergence metric of two distributions at two times. The method is architecture-agnostic, simple and can be easily integrated into existing frameworks. The experiments show that the proposed regularization improve the performance of different frameworks.

### Strengths
1.	The work reformulates the problem of regularization of dynamic nerf based on the assumption proposed by the paper. The Fig 1 clearly shows the difference between the proposed method and the simple metrics (like L2 distance).
2.	The proposed method seems technically sound with the theory of optimal transportation.
3.	The unbiased estimator is a clear advantage over existing regularization, like depth and optical flow.

### Weaknesses
1.	I am not the expert of the optimal transportation area. I cannot judge the novelty of the designed method, including the proposed theorem 1, and the sliced-Wasserstein approximator. It seems that the optimal transport method proposed here is not original and lack novelty. But again, I am not an expert for this area, and I would be open mind for other reviewers’ opinions for this part.
2.	The proposed regularizations only based on 2D distributions and cannot regularize 3D deformation directly. For me, it is equal to the idea that keep the image as static as possible. Is it true that the improvement of the regularization come from the improvement of the static background of the images, which are not related to the dynamic objects? The chichchicken video in supp supports this point.
3.	This method does not have much effect when the performance of the framework is above the certain level.
4.	This method could not deal with scenes with high frequency details, as such situation could break the assumption of the paper.
5.	There should be more visual results, especially for videos. Combine the two videos side by side in one video would be much helpful for comparison.

### Questions
1.	What are the settings of the baseline methods? Do you remove all other losses and only use the photometric loss, or you use all the proposed losses of the original papers.

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposed a regularization method for dynamic NeRFs using the optimal transport of pixel values at two different time steps, exploiting consistent structures between the video frames at different time steps. Although they assumed smooth motions without abrupt scene dynamics, they showed consistent results for iPhone and HyperNeRF interpolation datasets applying to various dynamic NeRFs.

### Strengths
- A simple yet effective regularization for dynamic NeRFs. 

- Thank you for the neat presentation of your work in the code of Alg. 1.

### Weaknesses
 - As the authors mentioned, this method asserted smooth motions without abrupt scene dynamics in the dynamic scene. The proposed method is rather an ad-hoc method for a subset of dynamic scenes. The authors may introduce a method to determine whether a given scene is appropriate to apply this method before full training and evaluation. This limitation is significant because many real-world dynamic scenes contain non-smooth motions, such as sudden object movements or occlusions. The method's reliance on consistent pixel structures across time steps will likely fail in such scenarios, leading to artifacts or inaccurate reconstructions. A more robust approach would ideally incorporate mechanisms to detect and handle these discontinuities, or at least provide a clear indication of when the method is likely to be ineffective.

 - In Tbl. 1. Hexplane w/ Reg on the Block scene had a significant gain while deteriorating the other scenes (i.e., Paper windmill, Teddy, Wheel in PSNR). The inconsistent performance of Hexplane with the proposed regularization across different scenes raises concerns about its general applicability. The fact that the regularization improves performance on one scene while degrading it on others suggests that the method may be sensitive to specific scene characteristics or model biases. This behavior needs further investigation to understand the underlying reasons and to determine the conditions under which the regularization is beneficial or detrimental. Without a clear understanding of this behavior, it is difficult to recommend the method for general use.

 - In Sec. 3.1, the theoretical statement makes the paper unnecessarily complicated. And I do not follow why Thm. 1 is necessary for the argumental context. The theoretical justification provided in Section 3.1, particularly Theorem 1, appears to be disconnected from the practical application of the method. The theorem's relevance to the overall argument is unclear, and the added complexity may not be necessary to understand the core contribution of the paper. The authors should clarify the practical implications of the theorem and explain why it is essential for the validity of their approach. Without a clear connection to the method's practical performance, the theoretical section may be seen as an unnecessary distraction.

### Questions
- Q1. In Tbl. 1. Hexplane w/ Reg on the Block scene had a significant gain while deteriorating the other scenes (i.e., Paper windmill, Teddy, Wheel in PSNR). How do you speculate on this result?

- Q2. In Sec. 3.1, the theoretical statement makes the paper unnecessarily complicated. And I do not follow why Thm. 1 is necessary for the argumental context.

- Q3. In Fig. 1, how do you decide which metric is the best in the manner of quantitativeness?

- Minors:
  - In Sec. 2, Related works -> Related work
  - In Sec. 3.1, from an images -> from images
  - The caption of Tbl. 5 goes beyond the content boundary of the bottom.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
