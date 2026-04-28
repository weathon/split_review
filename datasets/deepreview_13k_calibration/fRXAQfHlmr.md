# studentSplat: Your Student Model Learns Single-view 3D Gaussian Splatting

- Decision: Reject
- Avg Score: 4.25
- Scores: 3, 5, 6, 3

## Abstract
Recent advance in feed-forward 3D Gaussian splatting has enable remarkable multi-view 3D scene reconstruction or single-view 3D object reconstruction but single-view 3D scene reconstruction remain under-explored due to inherited ambiguity in single-view. We present studentSplat, the first single-view 3D Gaussian splatting method for scene reconstruction. To overcome the scale ambiguity and extrapolation problems inherent in novel-view supervision from a single input, we introduce two techniques: 1) a teacher-student architecture where a multi-view teacher model provides geometric supervision to the single-view student during training, addressing scale ambiguity and encourage geometric validity; and 2) an extrapolation network that completes missing scene context, enabling high-quality extrapolation. Extensive experiments show studentSplat achieves state-of-the-art single-view novel-view reconstruction quality and comparable performance to multi-view methods at the scene level. Furthermore, studentSplat demonstrates competitive performance as a self-supervised single-view depth estimation method, highlighting its potential for general single-view 3D understanding tasks.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper introduces studentSplat, a single-view 3D Gaussian splatting (3DGS) aimed at scene-level reconstruction from a single image. Recognizing challenges in single-view reconstruction, such as scale ambiguity and context extrapolation, the authors propose a teacher-student architecture. Here, a multi-view teacher (pre-trained feed-forward Gaussian Splatting Model (e.g., MVSplat)) provides geometric supervision to a single-view student model during training, addressing scale ambiguity and encouraging geometrically valid reconstructions. Additionally, the model uses an extrapolation network to adaptively fill missing scene context through GANs, improving the novel-view reconstruction quality.

### Strengths
- The overall paper is well-written with the architectural designs mentioned in detail making the readers easy to understand the training procedure and contributions of the work.
- Although the task being challenging, the proposed method shows strong performance, achieving state-of-the-art in multiple datasets.
- The proposed method is efficient in terms of the model parameters and the number of Gaussians compared to previous methods.

### Weaknesses
 - Mitigating the use of camera poses : The authors mention that the camera pose of a single image can be defined as the identity matrix, mitigating the use of camera poses of multi-view images. However, during the teacher-student geometric supervision, as MVSplat[1] has been trained on both RealEstate10K and ACID using SfM Camera poses, this supervision guides studentSplat to learn this SfM Camera Pose scales which enables the photometric loss of $L_{photo}$ with a specific relative camera pose $[R|t]$. As a result, I strongly believe that the current training scheme cannot be claimed as mitigating the camera pose.
- Performance contribution of extrapolator : As the evaluation is currently done with 2 novel views outside and one novel view inside the context frustums, I agree that the extrapolation performance of StudentSplat is superior than other methods and the teacher MVSplat. However there is no qualitative or quantitative results of the performance of studentSplat without the extrapolator which makes it hard to fairly compare with other methods.

### Questions
- As mentioned in the weakness section, training the student network in the same dataset with the teacher network cannot be claimed as fully mitigating the camera pose constraint. Can the model be trained in a new dataset the teacher has not been trained on? Or can the student network be trained with the rendered results of the teacher instead of ground truth images?
- To fully understand the performance of StudentSplat without the extrapolator, can the authors provide qualitative and quantitative results without the extrapolator?
- Extended from the previous question, I am concerned that the performance of studentSplat without the extrapolator is similar to the performance of MVSplat with Gaussians from one context images. As a result, can the authors show the performance of MVSplat (one view) + extrapolator?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces studentsplat. Inspired by some recent feed-forward 3D Gaussian Splatting methods with multi-view or single-view inputs, studentsplat combines two settings and uses multi-view model (teacher) to improve the performance of single-view model (student). An extrapolation network (GAN) is used to complete missing scene context and thus facilitates training. The idea is straightforward and the performance is better than recent methods in single image rendering and monocular depth quality.

### Strengths
The idea of distilling knowledge from multi-view model to single-view model is simple and makes sense. 

The paper is clearly written.

Studentsplat outperforms recent methods in single image rendering and monocular depth. 

The ablation study in main paper and supplementary is thorough.

### Weaknesses
I felt the evaluation is not very convincing. In single image setting, it is not surprising that pixelsplat and mvsplat perform worse since they rely on feature matching across different views, which is unavailable with single image (or let’s say two same images with baseline=0). For the evaluation with single image, my concerns mainly come from Fig. 3, 4, 7, 8. In these images, we can find that the viewpoints of target views and input context view are similar (i.e. the baseline between input view and target view is small). In some cases, I think directly copying the input image as output would provide nice rendering metrics as well. Therefore, I think evaluation with large baseline between input context view and target view should be included. 

In Fig. 11, seems the rendered depth from studentsplat is usually oversmoothed. Additionally, since the authors also mentioned Depth Anything (the student model also has similar structure as Depth Anything, i.e. DINOv2 + DPT), comparison with Depth Anything on depth quality can be included.

L90: The claim ‘Propose the first single-view 3D scene Gaussian splatting model’ is not convincing. Though SplatterImage (CVPR 2024) mainly focused on object-level scenes in the paper, the results in Table. 1 show that SplatterImage perform relatively well on large scenes (a little worse than the proposed method). 

Can you show some visualization of extrapolation with MI-GAN? 

L1009-1015: The visualization looks wrong. The input images and target image are from different scenes.

Typo: L237: compositing-> composition

### Questions
L90: The claim ‘Propose the first single-view 3D scene Gaussian splatting model’ is not convincing. Though SplatterImage (CVPR 2024) mainly focused on object-level scenes in the paper, the results in Table. 1 show that SplatterImage perform relatively well on large scenes (a little worse than the proposed method). 

Can you show some visualization of extrapolation with MI-GAN? 

L1009-1015: The visualization looks wrong. The input images and target image are from different scenes.

Typo: L237: compositing-> composition

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The paper presents a pioneering method for single-view 3D Gaussian splatting, addressing challenges in scene reconstruction from single images. The authors introduce a teacher-student architecture, where a multi-view teacher model provides geometric supervision, mitigating scale ambiguity. Additionally, an extrapolation network enhances scene context completion, leading to high-quality reconstructions. The proposed method achieves state-of-the-art results in single-view novel-view reconstruction and demonstrates potential in self-supervised depth estimation, broadening the applicability of 3D Gaussian splatting models​.

### Strengths
* The approach of leveraging geometric priors from multi-view reconstruction methods to enhance single-view reconstruction is intriguing, and the authors have experimentally demonstrated significant improvements in the perspective extrapolator through multi-view distillation.
* The authors present a simple yet effective method for extrapolating when computing the novel view reconstruction loss.
* The paper is well-written and easy to follow.

### Weaknesses
 * **3D Consistency**: In the unseen regions when extrapolating new views, the rendered results depend on the 2D generative model MI-GAN. Therefore, I am skeptical about the model's ability to generate extrapolated continuous new views with 3D consistency. Specifically, the reliance on a 2D generative model for extrapolation raises concerns about the geometric plausibility of the generated content. While the method may produce visually appealing novel views, it's unclear if the extrapolated regions maintain accurate 3D structure, potentially leading to inconsistencies when viewed from significantly different angles. The lack of explicit 3D constraints during the extrapolation process could result in artifacts such as incorrect object shapes or misaligned surfaces in the extrapolated regions. I recommend that the authors supplement the discussion with relevant visual results or theoretical analyses, particularly focusing on the geometric fidelity of the extrapolated regions.
* **Overclaim**: The authors state in the contributions section that they "propose the first single-view 3D scene Gaussian splatting model that does not require relative camera poses during inference." However, to my knowledge, there exists a single-view 3DGS-based method, Flash3d [1], which can achieve much of what this work does without needing camera poses. I recommend that the authors explicitly address how their method compares to Flash3D and explore the differences in their approach. Additionally, if feasible, including comparative experiments in their analysis would enhance the robustness of their claims. The current claim is misleading given the existence of alternative approaches that also operate on single images without requiring camera poses during inference.

### Questions
* Given the model's relatively low parameter count and the use of a lightweight generative model, does this method offer any advantages in terms of training time and inference speed compared to other single-view methods?
* Is the generative model MI-GAN fixed or fine-tuned during training? Could the authors provide more detailed experimental settings and analyses regarding MI-GAN?
* The authors propose a method for refining student output in Appendix D. Can this method be utilized during the training process of the student or teacher models as a form of self-supervised approach to enhance multi-view consistency?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper proposes a single-view 3D scene reconstruction method. While single view reconstruction suffers from unknown scale and regions unobserved, the authors introduce two techniques. The first solution is introducing a teacher-student architecture where multi-view model acts as a teacher model to provide supervision to student model. The second solution is introducing an extrapolation network that helps to extrapolate. The method is evaluated on ACID and RE10k, and ablation studies are conducted to support author's design choices.

### Strengths
1. Clear writing
2. Experiments are conducted with large-scale datasets, and compared with existing SOTAs.

### Weaknesses
1. In page 1, line 38, why is it the first single-view 3D gaussian splatting method? I recall flash3D [1], the paper written by the same first author of the splatterimage,  has already publicly available since June 2024, which is hard to miss. I understand that the paper seems to be yet published to any conferences or journals, but this does not mean that the authors can simply ignore this already existing paper and claim author's paper as the first approach. I recommend the authors to cite this paper, as well as provide some comparisons to them. I find that their code implementations are also available.

2. From the listed contributions in Line 90~96 at page 2, none of the list points are actually this paper's contributions. For example, the first approach for single-view 3D scene GS model is achieved by Flash3D, extrapolation issue is an apparent issue that comes with single view reconstruction, which many other works also address. Finally, It is questionable whether expanding the applications of 3D Gaussian splatting model is also one of the contributions. Since there have been many attempts trying to distill the knowledge learned from multi-view images to single-view model, and the applications the authors show are not really new. Single-view depth estimation is, NVS, Text-to-3D are all already existing applications if depth/3DGS is available. 

3. It is difficult for me to find technical contributions as well. Distillation from teacher to student is commonly adopted in the community and extrapolation module is simply learning from novel views, which have already been done in flash3d. 

4. Finally, I believe single-view reconstruction is practically close to impossible in "estimation" tasks, where 3D geometry dominates. It is possible in "generation" tasks, but since we never know what is beyond the single view observation, I personally believe this task is ambiguous in current state. Unless the authors provide convincing arguments that justify the need of this task and the feasibility of extrapolating better than the generation model, I doubt this work will deliever a valuable message to the community.

### Questions
Please see the weaknesses above.

### Soundness
2

### Presentation
3

### Contribution
1
