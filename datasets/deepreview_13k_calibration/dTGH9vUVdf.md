# FreeVS: Generative View Synthesis on Free Driving Trajectory

- Decision: Accept
- Avg Score: 5.80
- Scores: 6, 6, 6, 8, 3

## Abstract
Existing reconstruction-based novel view synthesis methods for driving scenes focus on synthesizing camera views along the recorded trajectory of the ego vehicle. 
Their image rendering performance will severely degrade on viewpoints falling out of the recorded trajectory, where camera rays are untrained.
We propose \methodnamenospace, a novel fully generative approach that can synthesize camera views on free new trajectories in real driving scenes. 
To control the generation results to be 3D consistent with the real scenes and accurate in viewpoint pose, we propose the pseudo-image representation of view priors to control the generation process.
Viewpoint transformation simulation is applied on pseudo-images to simulate camera movement in each direction.
Once trained, \methodname can be applied to any validation sequences without reconstruction process and synthesis views on novel trajectories.
Moreover, we propose two new challenging benchmarks tailored to driving scenes, which are novel camera synthesis and novel trajectory synthesis, emphasizing the freedom of viewpoints.
Given that no ground truth images are available on novel trajectories, we also propose to evaluate the consistency of images synthesized on novel trajectories with 3D perception models.
Experiments on the Waymo Open Dataset show that \methodname has a strong image synthesis performance on both the recorded trajectories and novel trajectories.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors present FreeVS -- a Video Stable Diffusion-based generative view synthesis method for driving scenes that can synthesize high-quality camera views both on and beyond recorded trajectories. 

The key innovation is using pseudo-images created by projecting colored point clouds as a unified representation for view priors. As opposed to recent contenders that rely on gaussian splatting or nerfs to represent the scene, the authors train a diffusion model on colored LiDAR point clouds.

The authors introduce two new benchmarks to evaluate the generated images that are far from the original poses. The method outperforms previous approaches for both traditional and newly proposed benchmarks on the Waymo dataset.

### Strengths
### Novelty
Clever use of pseudo-images obtained through colored point cloud projection as a unified representation for all view priors, simplifying the learning objective for the generative model.
### Evaluation
Introduces two new challenging benchmarks - novel camera synthesis and novel trajectory synthesis.

### Efficiency
The authors claim it takes less computational resources at inference time compared to splatting-based models.

### Performance
Better performance versus contenting methods, especially on poses far away from the original camera poses.

### Weaknesses
### Novelty
Engineering work -- it boils down to an addon for Video Stable Diffusion that has colored LiDAR point features concatenated.


### Different type of artfacts
The method trades the gaussian and nerf artifacts with the diffusion ones. While there is no denying that FreeVS works better than the previous attempts from novel views, for single front view, splatting still yields significantly better results (Table 3, front view).

### Evaluation
A single dataset is benchmarked (Waymo Open Dataset).

### Paper quality
Some tables missing numbers -- Table 3, reconstruction time.

### questions:
 1. Why is there no ablation study for **no priors**? This should be as close as possible to the vanilla Video Stable Diffusion.
2. Have you experimented with LiDAR noise / pseudo lidar from MDE methods or maybe a mesh-based method? Otherwise this pipeline is bound to an expensive data acquisition pipeline.
3. Training/inference times are unclear. How can it be that your method is faster than splatting-based methods at 0.9 FPS? The training time should also be discussed but it's not.
4. Could moving objects benefit from a special treatment? I.e, tracking/ inpainting. It doesn't look like the method handles well uncertain areas.

### Questions
1. Why is there no ablation study for **no priors**? This should be as close as possible to the vanilla Video Stable Diffusion.
2. Have you experimented with LiDAR noise / pseudo lidar from MDE methods or maybe a mesh-based method? Otherwise this pipeline is bound to an expensive data acquisition pipeline.
3. Training/inference times are unclear. How can it be that your method is faster than splatting-based methods at 0.9 FPS? The training time should also be discussed but it's not.
4. Could moving objects benefit from a special treatment? I.e, tracking/ inpainting. It doesn't look like the method handles well uncertain areas.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper approaches the task of novel view synthesis of outside-trajectory viewpoints on driving videos. It does so by training a conditional video diffusion model on outside-trajectory views created through projection of existing 3D point clouds. It evaluates generated images outside trajectories using off-the-shelf models. Compared to baselines StreetGaussian, EmerNeRF and 3D-GS, it shows superior results on novel camera synthesis, multi-view novel frame synthesis, and outstanding results on novel trajectory synthesis. Qualitative video results show a significant improvement over baselines.

### Strengths
Impressive results on a challenging task
- Results are clearly better than baselines in novel camera synthesis, multi-view novel frame synthesis, and significantly better in novel trajectory synthesis (FID drops by towards 75%)
- Qualitative comparisons clearly back these results
- Video results show impressive generation well outside input trajectory, while other methods have severe artifacts / fail entirely

Creative use of 3D and off-the-shelf models to enable a non-conventional setup
- Novel View Synthesis is so often limited to input trajectories. In the case of cars, this makes the task fairly straightforward and limited due to constraints on using positions connected to the car.
- Instead, this work approaches prediction several meters away from car trajectories. It does so by utilizing colored LiDAR across multiple views to create point clouds it can project into pseudo-images. This is a nontrivial trick to implement effectively. This work shows it can be useful for training a generative model!
- Evaluation is also tricky in the pseudo-image setting, but FID and 3D Detection mAP are suitable metrics; while of course qualitative results are most important.


***Post-Rebuttal Update*** I leave my score at 6. The reviewers did a good job of addressing my concerns and I feel the paper should be accepted as it offers good contributions in 3D and video generation to yield an effective method. See my response to the rebuttal for more detail.

### Weaknesses
Could use clearer argument for method leading to performance gain
- Numbers in the ablations table do not match that in comparisons to baselines. Why not?
- Ablations show little impact on performance. When the FID of this method is less than a third of that of baselines, surely more than 10% of performance can be explained by choices. For example, how does training data impact performance? What about pretraining or architecture? If these are important, it feels the architecture should be described in more detail. 
- I infer a lot of the performance is coming from training data, yet the main paper has little information about this. How big is the train set in terms of sequences, if they are chosen from WOD? 
- The alternative explanation I fear is most of the performance is coming from Stable Video Diffusion. It should be very clear how strong this baseline is without the proposed contributions

### Questions
See Weaknesses

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This work focus on novel view synthesis on extrpolated view (i.e. rendered views are far away from source training views).
The authors propose to use reprojected colored lidar points as condition, using a freezed diffusion decoder to achieve high quality synthesized images.
Experiments are conducted on Waymo, demonstrating way better results over other 3d-optimization based approaches (emernerf, streetgaussian)

### Strengths
1. Much better (more robust) results over 3D-optimization based approaches (EmerNerf, streetgaussian) on far-away novel veiws, because they typically have overfitting issues.
2. A combination of 3D informtion and 2D diffusion  model that provides both controllability and decent rendering results.

### Weaknesses
1. The rendering speed is very slow,  while 3DGS which can render at real time (50+fps), this hinder the downstream applications that requires realtime efficiency.
2. Inconsistency results because of using large decoder
3. Worse performance compared to 3D-optimization approaches if the novel view are close to source views;

### Questions
This idea is quite similar to Free View Synthesis which both project source views into target view, you may consider add it as a baseline, at least cite it.

@article{riegler2020free,
  title     = {Free View Synthesis},
  author    = {Gernot Riegler and V. Koltun},
  journal   = {European Conference on Computer Vision},
  year      = {2020},
  doi       = {10.1007/978-3-030-58529-7_37},
  bibSource = {Semantic Scholar https://www.semanticscholar.org/paper/49fae04a4e9383080788759f63dba75c86bd21b0}
}


You may also want to cite magicDrive and MagicDrive3D, as both work on generative driving scenes.

### Soundness
3

### Presentation
3

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
The paper introduces FreeVS, an approach to view synthesis for driving scenes that overcomes limitations of existing methods, which primarily focus on synthesizing camera views along pre-recorded vehicle trajectories. Traditional methods tend to degrade in performance when synthesizing viewpoints deviate from the recorded trajectory, as these viewpoints lack of groundtruth data. 

To ensure that the generated images remain consistent with the 3D structure of the scene and accurate in terms of viewpoint pose, the authors introduce a pseudo-image representation of view priors based on LiDAR. This representation controls the generation process and allows for the simulation of viewpoint transformations, enabling the model to mimic camera movement in different directions.

The authors proposed two benchmarks for evaluating novel camera synthesis and novel trajectory synthesis. The proposed method is evaluated on Waymo Open Dataset.

### Strengths
- The paper is well motivated, shows great potential for the real-application of autonomous driving simulation.
- Proposed a "psuedo LiDAR controlnet" for SVD, which is easy yet effective.
- The experimental results and demo video demonstrate the effectiveness of the proposed method.

### Weaknesses
 - The evaluation is not very comprehensive. The baseline methods are not *specifically* designed for the similar purpose of the paper. 3D-GS is the basic method, EmerNeRF and StreetGaussian are more for the dynamic NeRF/3DGS. There are works that use virtual warping for improving the novel view quality such as [1] [2], that might be better for the baselines. Specifically, the baselines lack methods that explicitly address view synthesis from novel viewpoints, which is the core contribution of this paper. The comparison should include methods that leverage similar input data (LiDAR) and aim at generating novel views, not just general NeRF or 3DGS methods.
- The benchmark of novel trajectory synthesis looks interesting to me, however, the authors only show the FID results, while FID is well-known for its instability and unreliability by changing the resolutions, etc. This reminds me of the existing novel trajectory synthesis benchmark [3], the authors should test their methods on such a dataset and demonstrate the *absolute* performance gain using the metrics of PSNR, SSIM, etc. The reliance on FID alone makes it difficult to assess the actual quality of the synthesized images, as FID is more indicative of distribution similarity rather than pixel-level accuracy. A more comprehensive evaluation should include metrics that directly measure the fidelity of the generated images.
- I would like to further know the zero-shot generalization of the trained SVD, since the Waymo Open dataset is quite clean for its camera/LiDAR extrinsic calibration, and the number of LiDAR beams is relatively high, it is interesting to show the results of genelizating it to other scenes or datasets, and how the SVD benefits the downstream 3DGS reconstruction. The paper does not address how the method would perform on datasets with different sensor configurations or calibration qualities. It is crucial to evaluate the robustness of the approach to variations in input data.
- What are the results of applying the proposed methods on dynamic scenes? The paper does not provide sufficient detail on how dynamic objects are handled, and it is unclear how the method would perform in complex scenes with moving vehicles or pedestrians.

### Questions
See above. I personally like the idea of the paper, but I still have many concerns and would provide a final rating based on the authors' responses.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper addresses the free-view synthesis problem by training a diffusion model conditioned on synthetic images through point cloud projection. During training, it project colored LiDAR points from nearby views into the reference view as a condition image, and finetune a diffusion model so that it can generate the reference view. During inference, condition image can be synthesized for a novel view, which is taken by the diffusion model to generate a realistic image of that view.

### Strengths
The paper is easy to read and the idea is clear.

The method is solid and reasonable, potentially showing good generalizability without training very big models (e.g. video foundation model). Conditioning on pseudo-images can help improve 3D consistency.

### Weaknesses
1. the proposed method seems too normal, and I read tons of paper doing similar things -- fine-tune the result based on a synthesized image. The authors also mentioned several such works in the related work. The only difference seems to be that they deal with objects while the authors deal with the driving scene.

2. it seems that the paper did not seriously consider temporal information. There is no way to ensure temporal consistency. Also, it seems that moving objects can cause inconsistency and troubles during pseudo image synthesis while the authors only have one sentence discussing how to address it. I believe it can cause a lot of troubles.

3. There is no discussion about the requirement of the pseudo images. For examples, if the novel view is far from captured views, it surely can cause problems.

### Questions
See weakness.

### Soundness
3

### Presentation
3

### Contribution
2
