# Ctrl-V: Higher Fidelity Video Generation with Bounding-Box Controlled Object Motion

- Decision: Reject
- Scores: 5, 5, 3, 3

## Abstract
Controllable video generation has attracted significant attention, largely due to advances in video diffusion models. In domains such as autonomous driving, it is essential to develop highly accurate predictions for object motions. This paper tackles a crucial challenge of how to exert precise control over object motion for realistic video synthesis. To accomplish this, we 1) control object movements using bounding boxes and extend this control to the renderings of 2D or 3D boxes in pixel space, 2) employ a distinct, specialized model to forecast the trajectories of object bounding boxes based on their previous and, if desired, future positions, and 3) adapt and enhance a separate video diffusion network to create video content based on these high quality trajectory forecasts. Our method, \textbf{Ctrl-V}, leverages modified and fine-tuned Stable Video Diffusion (SVD) models to solve both trajectory and video generation. Extensive experiments conducted on the KITTI, Virtual-KITTI 2, BDD100k, and nuScenes datasets validate the effectiveness of our approach in producing realistic and controllable video generation.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper presents a controllable video generation pipeline for autonomous driving, where bounding boxes are first generated and then used as conditions for video generation. Experiments on various driving datasets are conducted to evaluate the pipeline's capabilities.

### Strengths
* The paper introduces a novel diffusion-based approach for generating 2D/3D bounding-box trajectories at the pixel level.
* This paper proposes a two-part controllable video generation method that first generates trajectories and then uses these trajectories to condition video generation, achieving solid performance in autonomous driving scenarios.
* The experiments cover multiple autonomous driving datasets and provide sufficient quantitative and qualitative results, effectively validating the model’s applicability in autonomous driving contexts.

### Weaknesses
 * The primary distinction of the proposed two-part method from one-stage generation is the additional step of bounding-box trajectory generation. However, the paper does not discuss the specific advantages of this intermediate trajectory generation step. Including a comparison would help clarify the benefit of this two-part method. For instance, it's unclear if generating trajectories first allows for better control over object motion or if it improves the overall quality of the generated video compared to directly generating video with bounding box conditions.
* While AP is used to assess bounding-box generation location accuracy, this paper lacks evaluations of trajectory smoothness, rationality, and temporal consistency. These aspects are important in assessing the realism of generated motion trajectories. For example, are the generated trajectories free of abrupt jumps or unrealistic changes in direction? Are the speeds of the objects consistent with real-world driving scenarios? The lack of these evaluations makes it difficult to assess the quality of the generated trajectories.
* Methods compared in the paper, such as Boximator, are designed for general scenarios, while this paper only concentrates on driving scenes, making it difficult to ensure fair comparisons. The paper does not clarify whether the proposed method could work in broader contexts beyond autonomous driving. It would be useful to see how the method performs on datasets that are not related to driving, to understand its generalizability.
* In Table 1, the Teacher-forced method performs worse than the BBox-Generator-and-Box2Video-combination method on KITTI and BDD datasets. Does this imply that the Box2Generator model is not optimal? Discussion on this phenomenon would be valuable. It raises questions about the effectiveness of the teacher-forcing approach in this specific context and whether the model is learning the underlying dynamics of the bounding box trajectories effectively.

### Questions
* It would be helpful to see more ablation studies, such as whether using the bounding box of the last frame is necessary and the role of the adapter layer.
* More specific visualizations or numerical results would be valuable for cases involving occluded objects or objects that appear midway, as mentioned in the model.
* Discussion on failure cases is insufficient.
* The two-stage generation method involves two diffusion forward processes. However, there is a lack of discussion regarding the computational overhead and parameter cost associated with this approach.
* It would be insightful to explore whether the model can handle more control information.

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
2

### Summary
This paper presents an approach to generating driving scene videos by utilizing existing pre-trained image-to-video diffusion models, Stable Video Diffusion. Notably, all the bounding box conditionings are encoded into RGB (in contrast to feature representations), and the off-the-shelf VAE is used to render the conditionings to latent representation. The proposed method first interpolates bounding boxes placed on the first frame and the last frame (and optionally other frames?) to generate a sequence of bounding conditionings, and then realistic driving videos are generated with a control-net-based conditioning mechanism. The authors demonstrate reasonable generated quality.

### Strengths
- The authors demonstrate that bounding box conditioning can be encoded with the off-the-shelf VAE, which is interesting.
- Investigating the ability to generate driving scene videos with existing image-to-video diffusion models (i.e., SVD) is interesting. 
- The quality of generated videos seems to be reasonable although the authors did not provide the sample of generated videos (in a video format) in the supplemental materials.

### Weaknesses
Overall, paper clarity is lacking, and significant revision might be needed to meet the standard conference paper quality. Since I am not specifically an expert in driving video generation, it was difficult for me to precisely understand the technical contribution and soundness of the paper. (Hence, I set the confidence score as 3.)
Here are some suggestions to improve clarity:
- Generated videos (in a video format) are not provided in supplementary materials. Since this paper works on video generation, it is important to provide samples of generated videos in a video format.
- The figure of the overall framework (Figure 2) is not referred to in the paper. Since there is no explanation related to this figure (for instance what is c', k?), it is difficult for me to judge the correctness.
- Some equations are missing. For instance, the authors mentioned Equation 3.3, but the equation does not exist in the paper.
-  I would suggest defining all the notations in the authors' papers instead of directing the readers to other papers for the definition of notations (for instance, in section 3.1).
- In section 4.2, the authors set up baselines but it is not clear to me exactly what these baselines are. For instance, what is "Teacher-forced Box2Video generation"? Exactly how it is different from the proposed approaches. I would appreciate it if the authors could explain all the baselines in detail. 
- The motivation of input conditioning seems unclear. Could the authors provide reasons for why the authors experiment with first/last frame conditioning, 2D/3D conditioning, and first/three frame conditioning, trajectory conditioning in the last frame?
- Are there indeed no baselines from previous works that can be compared with the authors' works? How is the authors' method superior to relevant works? Since I am not familiar with driving scene generation, I will rely on other reviewers' judgments for this. But in general, I would like to see how relevant baselines (even if they are not directly applicable to your problem setting) are inferior to your approach.

### Questions
I would appreciate it if the authors could revise the paper to improve clarity. Please see above for some suggestions.

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper presents a bounding-box (bbox) controllable video generation method called "Ctrl-V." Ctrl-V employs a two-stage pipeline: it first generates a bbox sequence based on both the first and last frames, and then the diffusion model Box2Video generates a video conditioned on the sequence of generated bboxes. To evaluate the performance of this new problem formulation, a new benchmark has been introduced.

### Strengths
This paper proposes an innovative video generation method that involves generating a sequence of bounding boxes. Compared to other approaches, it demonstrates superior generation quality.

### Weaknesses
1. The figures in the paper require significant improvement. The references to the figures are unclear. For Figure 1, the information presented is sparse. Figure 2 is difficult for readers to interpret due to unclear connections. Additionally, Figure 3's purpose is not well-defined within the context of the paper.
2. The experimental section lacks validity. For Table 1, there is no information regarding the last column for Multi-view on the nuScenes dataset. The meaning of "Ctrl-V + BBox Generator + Box2Video" is ambiguous, as it appears that Ctrl-V is already integrated with the BBox Generator and Box2Video.

### Questions
Where is the corresponding description for the figures in this paper?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper proposes Ctrl-V, a method for bounding box controlled video generation. The proposed method is split into two parts. The first part is a generator that synthesizes images of bounding box sequences. The second part takes the bounding boxes images as an input to condition a pre-trained video model. The results demonstrate that the bounding boxes images can be used as a ControlNet style conditioning signal for video generation.

### Strengths
- Writing: The paper is well written and easy to follow.
- Simple approach: The proposed two-stage method seems simple and easy to implement. Moreover, the method is generally sound.

### Weaknesses
 -  No video results: There is no supplementary website with video results. This makes the submission incomplete, as the most important part of a video generation work are the video generations. It’s impossible to judge the results at all, especially regarding temporal consistency.
- Generalizability: The method is trained on driving data and evaluated on that, even though the method is using a pre-trained video model trained on diverse data. It’s not clear how well this method generalizes, especially because the denoising U-Net is fine-tuned. All previous works demonstrate generalizability to any input, which is a clear advantage over the proposed method.
- Missing comparisons: Why does Tab. 2 with the bounding box control metrics not include other trajectory-conditioned video generation methods? It’s not clear why there is only this one made up baseline instead of adapting previous trajectory-conditioned video generation approaches to the same setup.
- Unclear metric scores: The average precision scores in Tab. 3 are not clear. The caption says that prior works don’t evaluate driving datasets. So are these methods adapted to these datasets or do the test datasets differ here? Because it sounds like different evaluation sets were used for different methods.
- No insights provided: The approach is very simple. Create bounding box images with one network, then do ControlNet to condition the generation with these bounding box images. If an approach is that simple without some interesting twist or super convincing results, the paper needs insights. There is no ablation in the paper. For example: How important is it to use bounding boxes images? What happens if just the coordinates and sizes are used as conditioning? There is no clear motivation why the proposed method is the best way to solve this issue.

### Questions
I currently rate this paper below the acceptance threshold. Video results are missing, hence it’s impossible to judge the results. Furthermore, only driving datasets are shown while all previous works show generalizability to any kind of scene.

I would like authors to address following questions:
- Why are there no video results?
- Does the method transfer bounding box conditioning to OOD prompts?

I am open to adjusting my rating based on the rebuttal.

### Soundness
2

### Presentation
2

### Contribution
2
