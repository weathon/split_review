# Learning Epipolar Feature Fields for Multi-Image Super-Resolution

- Decision: Reject
- Scores: 1, 8, 3, 6

## Abstract
Multi-image super-resolution (MISR) allows to increase the spatial resolution of a low-resolution (LR) acquisition by combining multiple images carrying complementary information in the form of sub-pixel offsets in the scene sampling, and can be significantly more effective than its single-image counterpart. Its main difficulty lies in accurately registering and fusing the multi-image information. Currently studied settings, such as burst photography, typically involve assumptions of small geometric disparity between the LR images and rely on optical flow for image registration.
We study a MISR method that can increase the resolution of sets of images acquired with arbitrary, and potentially wildly different, camera positions and orientations, generalizing the currently studied MISR settings. Our proposed model, called EpiMISR, moves away from optical flow and explicitly uses the epipolar geometry of the acquisition process, together with transformer-based processing of radiance feature fields to substantially improve over state-of-the-art MISR methods in presence of large disparities in the LR images.

## Human Reviews

## Human Reviewer 1

### Rating
1

### Rating Number
1

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
A method for multi-image super-resolution (SR) is proposed where the input multi-images which provide the extra subpixel information are captured from a wider baseline rather than a video or very small baseline. These kind of images are typical in structure from motion settings where epipolar geometry is used to accumulate the extra information from all the images. The solution framework is divided into three main blocks. The first block does standard single image pre-existing super-resolution (stopped at feature level output and not full RGB output) followed by capture for epiploar information with reference image being one single image which needs to be super-resolved and epiploar images being all other images. The epiploar information is encoded in 4D tensor. Lastly the epiploar tensor matrix is passed through a transformer (encoder-decoder) architecture to learn a delta image which when linearly added to already existing single image super resolved image will improve it even further. Many relevant metrics are shown in results to show that the proposed multi-image super resolution outperforms SOTA in single image SR and burst SR.

### Strengths
The paper is very well written (infact I didn't find any grammatical mistakes which is rare in my experience), easy to understand and all concepts are clearly explained with sufficient literature review. The results analysis is also good. The paper addresses an almost unexplored territory of wide base line multi-image super resolution. The analysis is Section 4.6 is very good to relate newer concepts like attention with more traditional vision analysis.

### Weaknesses
1. One of the missing parts in the results section is what happens when the selection of multi-view images involves widening the baseline between images, while keeping the number same. In other words if the selected images are more spread out, then how does the method perform. This result would have been like a test of breaking point of the method with respect to distribution of the camera locations. Like in Figure4, the images are wide baseline but not too wide.

2. Another thing to put would be more visual results. Figure 2 just shows one result. Typically 4-5 results with challenging scenes should have been shown as SR is a very visual problem.

3. The paper doesn't talk about failure cases. Its hard to believe that there were no cases where the proposed method outperformed all SOTA in all test images.

4. I also couldn't find any numbers on run-time for training and inference.

### Questions
Kindly look at the weakness section and address it.

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
4 excellent

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper proposed a novel MISR technique by employing epipolar constraints in classical multi-view geometry. There were similar MISR tasks where the multiple images were obtained from adjacent frames in video, burst images, and stereo images, which means that the multiple images have small disparity. The authors claim that the proposed methods can super-resolve images with potentially wider disparity. They provided few output results and quantitative results.

### Strengths
- Overall, it is a well-written and easy to read paper. 
- The authors clearly differentiated the proposed work compared with existing MISR works about the definition and technical novelty. 
- They also provided experimental results of the existing SOTA methods. 
- They also provided degree of disparity in the experimental images (a.k.a. parallax angle)
- Technical novelty is on applying epipolar constraint to the learning models, since to the deep network, information which doesn't satisfy the epipolar constraint can be regarded as noise to the problem setting.

### Weaknesses
The paper already provides contents that I was about to challenge. But I suggest that, as it is image related works, the authors could provide more qualitative results (sample images).

### Questions
No questions

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper introduces a method, known as EpiMISR, for multi-image super-resolution by integrating complementary elements from multiple neighboring images. EpiMISR leverages the epipolar geometry inherent in the image acquisition process and employs transformer-based processing of radiance feature fields. This approach improves the performance of MISR methods, particularly when dealing with large disparities in low-resolution images. Once the super-resolution model is trained, it can be applied to a new scene with an arbitrary number of views. However, the method does not have the capability to render novel views.

### Strengths
+ The paper proposes a novel method for multi-image super-resolution.
+ The paper is articulated in a clear and concise manner, making the method straightforward to comprehend.

### Weaknesses
1. Novelty: While the use of epipolar geometry is not new and has been widely used in light field super-resolution [1] and generalizable NeRF [2], the main pipeline of this paper appears to be a combination of single-image super-resolution methods and light field neural rendering [3]. The paper’s primary contribution is unclear.
[1] Zhang, Shuo, Song Chang, and Youfang Lin. "End-to-end light field spatial super-resolution network using multiple epipolar geometry." IEEE Transactions on Image Processing 30 (2021): 5956-5968.
[2] Suhail, Mohammed, et al. "Generalizable patch-based neural rendering." European Conference on Computer Vision. Cham: Springer Nature Switzerland, 2022.
[3] Suhail, Mohammed, et al. "Light field neural rendering." Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. 2022.

2. View Consistency: View consistency is indeed crucial for multi-image super-resolution, differing from single-image super-resolution. If the method can ensure consistency among all super-resolution images, it would be beneficial for downstream tasks such as novel view synthesis and 3D reconstruction. However, the paper does not evaluate the consistency of the produced super-resolution images.

3. More Datasets: The paper claims that the method can be used for an arbitrary scene with an arbitrary number of views with an arbitrary geometry. However, only 9 scenes in the DTU dataset are tested, which may not be sufficient to demonstrate the method’s effectiveness, especially in super-resolution tasks. IBRNet[1] has collected multiple multi-view datasets, which contain more than 1000 scenes. Testing on this dataset would provide more convincing results.
[1] Wang, Qianqian, et al. "Ibrnet: Learning multi-view image-based rendering." Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. 2021.

4. Occlusion: The method’s direct fusion of multi-view features in the MIFF module may introduce artifacts due to occlusions. It’s unclear how the method deals with occlusion problems. While the occlusions in DTU scenes are not complex, allowing the method to outperform some single-image super-resolution methods, it’s uncertain whether it can be applied to complex scenes and achieve similar performance, such as the fern scene in the LLFF dataset.
5. Missing a reference. 
Huang, Xin, et al. "Local implicit ray function for generalizable radiance field representation." Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. 2023.

### Questions
I hope the author can address my concerns mentioned in the weaknesses. Additionally, I have a few more questions and suggestions:

1. Is it possible to apply epipolar geometry to dynamic scenes? Additionally, epipolar geometry is dependent on pose calibration. Could you clarify why methods based on epipolar geometry are considered superior to flow-based methods?

2. Is the method dependent on bicubically downsampling? If given low-resolution images captured by a camera as input, can the method produce super-resolution images?

3. The caption of the pipeline could be more detailed for better understanding.

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
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The author proposed a multi-image super-resolution algorithm. The algorithm can handle input images with large parallax by combining neural processing and epipolar geometry. The proposed method achieves promising numerical and visual results.

### Strengths
The overall pipeline of multiple image SR with large parallax is reasonable.

The method achieved SOTA scores on objective metrics and the result is visually promising.

### Weaknesses
* Novelty:
I don't agree with the statement in 2.2 “this is the first work tackling the problem of generic multi-image super-resolution”. In paper [1], the framework of multi-image fusion has been proposed, and the example in section 4.1 shows the super-resolution application. 

Registration and fusion neural features along the epipolar line can also be found in [1, 2, 3].

So this novelty of the proposed method is compromised. The authors should properly cite the relevant papers, make comparisons and rephrase the contributions. Will re-evaluate the novelty based on the revision.

* The description of CAP module in section 3.1.1 is ambiguous. I suggest illustrating the process with diagrams.

* The experiment section only visualizes one result in Fig. 2. To avoid the impression of handpicking, more results should be demonstrated.

* The experiments were only carried out on one dataset, so it is difficult to analyze the generalization ability of the model to other data. This is important especially in case the proposed method was claimed to be generic. The authors are suggested to evaluate the model on other data if possible.

[1] Huang, Qian, Minghao Hu, and David J. Brady. "Array Camera Image Fusion using Physics-Aware Transformers." Journal of Imaging Science and Technology 66 (2022): 1-14
[2] He, Yihui, et al. "Epipolar transformers." Proceedings of the ieee/cvf conference on computer vision and pattern recognition. 2020.
[3] Wang, Xiaofeng, et al. "MVSTER: Epipolar transformer for efficient multi-view stereo." European Conference on Computer Vision. Cham: Springer Nature Switzerland, 2022.

### Questions
P = 256 in experimental setting 4.1. But sometimes epipolar line can intersect with more than 256 pixels when the image resolution is 400x300. Please elaborate on how 256 points are sampled under this situation.

The parallax in NERF dataset may be extreme since the occlusions between the camera views are magnified. How does the model perform in regions with substantial occlusions?

Why do you use BRISQUE scores when you have GT and you cannot justify it?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
