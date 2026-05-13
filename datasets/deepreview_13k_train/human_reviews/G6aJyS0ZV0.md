# 3D StreetUnveiler with Semantic-aware 2DGS - a simple baseline

- Decision: Accept
- Scores: 8, 3, 6, 8

## Abstract
Unveiling an empty street from crowded observations captured by in-car cameras is crucial for autonomous driving. However, removing all temporarily static objects, such as stopped vehicles and standing pedestrians, presents a significant challenge. Unlike object-centric 3D inpainting, which relies on thorough observation in a small scene, street scene cases involve long trajectories that differ from previous 3D inpainting tasks. The camera-centric moving environment of captured videos further complicates the task due to the limited degree and time duration of object observation. To address these obstacles, we introduce StreetUnveiler to reconstruct an empty street. StreetUnveiler learns a 3D representation of the empty street from crowded observations. Our representation is based on the hard-label semantic 2D Gaussian Splatting (2DGS) for its scalability and ability to identify Gaussians to be removed. We inpaint rendered image after removing unwanted Gaussians to provide pseudo-labels and subsequently re-optimize the 2DGS. Given its temporal continuous movement, we divide the empty street scene into observed, partial-observed, and unobserved regions, which we propose to locate through a rendered alpha map. This decomposition helps us to minimize the regions that need to be inpainted. To enhance the temporal consistency of the inpainting, we introduce a novel time-reversal framework to inpaint frames in reverse order and use later frames as references for earlier frames to fully utilize the long-trajectory observations. Our experiments conducted on the street scene dataset successfully reconstructed a 3D representation of the empty street. The mesh representation of the empty street can be extracted for further applications.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper introduces StreetUnveiler, a method to reconstruct empty street scenes from crowded video captured by moving vehicles. The key challenge is removing temporarily static objects (like parked cars and pedestrians) while maintaining temporal consistency over long trajectories. The main contributions are: 1) adapting 2DGS with hard-label semantic for scalable scene representation with explicit object removal, 2) using rendered alpha map to classify areas as fully observed, partially observed, or unobserved for creating inpainting masks, and 3) a time-reversal inpainting framework that maintains temporal consistency by using future frames to condition earlier frames. The paper shows better inpainting results compared to other off-the-shelf methods.

### Strengths
- I particularly like the idea of time-traversal inpainting. While single-image inpainting has been extensively explored, video-based inpainting (where temporal consistency is required) remains relatively understudied. Although the overall process isn't completely novel, I appreciate that the method is specifically tailored for driving videos with predominantly forward motion. Reference-based inpainting shows great promise for many applications and seems like a valuable direction to pursue.

- The paper is well-written, with clear motivation. The process, insights, and technical details are thorough and convincing. I especially appreciate the comprehensive related work section, which is very helpful for readers who don't necessarily work in inpainting or neural scene representation.

- The results are impressive, with both quantitative and qualitative improvements over baseline inpainting methods. The method appears to handle challenging cases well, particularly in maintaining consistency across long sequences.

### Weaknesses
 - My only concern is that while the ultimate goal is temporally-consistent inpainting, the authors chose a more complex approach going through neural scene representation (2D/3DGS) and using rendered alpha masks to identify different region types (observable/unobservable) for generating inpainting masks. While this is interesting in principle, I wonder if a simpler pipeline could achieve similar goals - for example, establishing object correspondences across the video frames and then applying LeftRefill. I also note that LeftRefill is missing from the quantitative comparisons.

### Questions
I think the paper is well-written with a good application as it proposed an inpainting method that seems to work well to maintain temporal consistency.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This work aims to remove static movable objects (e.g., parked vehicles) in street view data for 3D reconstruction (e.g., 3DGS). The authors propose two main improvement to achieve better inpainting results: better inpainting mask, better reference for image inpainting.

Experiments conducted on Waymo and PandaSet datasets demonstrate better performance compared to image/video inpainting methods and other 3D inpainting approaches.

### Strengths
1. Clear writing and presentation, with a well-designed supplementary website
2. Two novel and effective design elements:
   * An improved method for generating inpainting masks that incorporates observations from other frames
   * Time-reversal inpainting that utilizes future frames as references

### Weaknesses
1. The contribution seems somewhat limited. While the two major contributions are effective, they appear to be incremental rather than groundbreaking. The work could serve as a baseline, but not much more that.

2. The performance metrics are not entirely convincing. Table 1 doesn't demonstrate significant advantages over other baselines. The video in the supplementary materials appears noticeably inferior to other NVS methods on Waymo (e.g., EmerNeRF, StreetSurf, StreetGaussian).

3. The benchmark methodology raises some questions (please correct me if I'm mistaken, as I haven't encountered this benchmark setting before). What are the ground truth images used for LPIPS? If all rendered images lack vehicles while the ground truth images typically include them, is this an appropriate measurement for LPIPS/FID?

4. I have reservations about the task itself: Is it truly necessary to remove static components from the scene? Static elements (e.g., trees, traffic signs, rubbish bin) are integral parts of the environment. Even if removal is desired, wouldn't it be more efficient to accomplish this through multi-pass data collection?

### Questions
please address the concern in the weakness session

### Soundness
3

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
3

### Summary
The paper presents StreetUnveiler for reconstructing an empty street from in-car camera videos. It uses hard-label semantic 2DGS for representation, divides the scene into regions located by an alpha map, and introduces a time-reversal inpainting framework. Experiments show its effectiveness in reconstructing the empty street for autonomous driving applications.

### Strengths
- The use of 2D Gaussian combined with semantic information is reasonable. It allows for better identification and removal of objects by injecting semantic labels into 2D Gaussians.
- Experiments on street scene datasets demonstrate the effectiveness of the method.
- The proposed time-reversal framework inpaints frames in reverse order and uses later frames as references for earlier frames. This enhances the temporal consistency of the inpainting results, making the reconstructed street more realistic and consistent across different views.

### Weaknesses
 - The 2DGS reconstruction and optimization processes might be computationally complex and costly, especially for large-scale street scenes, leading to long training and inference times. The author may consider other faster reconstruction baselines.
- The method has limited ability to handle dynamic objects. Although some approaches for simple dynamic cases are proposed, more improvements are needed for complex dynamic scenes.

### Questions
In fact, there are many methods that directly predict the masks of dynamic objects, and these are usually more reliable than the masks obtained by optical flow. Additionally, in many complex situations (such as vehicles driving sideways at an intersection), can the prior advantage of time-reversal inpainting still be maintained?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
The paper presents StreetUnveiler, a method based on semantic 2DGS to achieve the empty street scene reconstruction. 
StreetUnveiler first utilizes the rendered alpha map to locate unobservable regions with the aid of distortion loss and shrinking loss.
Then a time-reversal inpainting framework is introduced to optimize temporal consistency by leveraging later frames as references for earlier ones. 
Experiments are conducted on Waymo and Pandaset to demonstrate the effectiveness of StreetUnveiler for the empty street reconstruction.

### Strengths
1. The writing of the paper is clear and easy to follow.
2. The task of empty street scene reconstruction is interesting. The limitations discussed in the introduction are well studied in the following section. 
3. The proposed method is evaluated on two datasets. Many quantitative and qualitative experiments are conducted to demonstrate the effectiveness of this method.

### Weaknesses
1. Lack of Quantitative Metrics for Mesh: While the authors discuss the differences in problem formulation between StreetSurf and StreetUnveiler, a quantitative comparison of mesh reconstruction is still lacking. StreetSurf uses point clouds as ground truth to calculate Chamfer Distance as a metric. Could a point cloud derived from Structure from Motion (SfM) be used as a ground truth for evaluating StreetUnveiler’s performance? Even relative values across different baselines could provide meaningful insight. Specifically, it's unclear how the observed geometry of StreetUnveiler compares to methods like StreetSurf, even if the unobserved geometry is the primary focus. A comparison of the observed regions using metrics like Chamfer Distance or F-score, with appropriate masking to isolate the observed portions of the mesh, would be beneficial.
2. Limitations in Semantic Label Supervision: Current semantic supervision seems limited to common objects like vehicles, yet street environments also include pedestrians and less common obstacles. Could expanding the range of semantic (instance) labels improve the model’s robustness across diverse urban scenes? Furthermore, the robustness of the method to noisy semantic segmentation is not discussed. The performance of StreetUnveiler may be highly dependent on the quality of the semantic segmentation. If the segmentation contains noise, how does this impact the final reconstruction?

### Questions
1. Applications of Unveiled Street Scene Reconstruction: The task of reconstructing an unveiled street scene is indeed challenging and engaging. However, real-world street environments include more than just vehicles, and vehicles can often obscure parts of other objects, such as the lower half of a road sign. Would it be more practical to first apply 2DGS to separate scenes based on specific requirements, then proceed with targeted inpainting? This approach could provide more utility by selectively reconstructing essential scene elements.
2. Potential to Build on Existing 3DGS Street Scene Reconstruction Methods: Current methods, such as Street Gaussians[1] (using 3D box-based scene decomposition) and S3Gaussian[2] (self-supervised scene decomposition), aim to separate scenes into dynamic and static components. Could integrating these approaches enhance StreetUnveiler’s ability to more effectively distinguish between removable objects and essential scene elements? This could potentially improve the precision in identifying and preserving critical components.

[1]Yan Y, Lin H, Zhou C, et al. Street gaussians for modeling dynamic urban scenes[J]. arXiv preprint arXiv:2401.01339, 2024.
[2]Huang N, Wei X, Zheng W, et al. $\textit {S}^ 3$ Gaussian: Self-Supervised Street Gaussians for Autonomous Driving[J]. arXiv preprint arXiv:2405.20323, 2024.

### Soundness
4

### Presentation
4

### Contribution
4
