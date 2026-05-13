# GUNet: A Graph Convolutional Network United Diffusion Model for Stable and Diversity Pose Generation

- Decision: Reject
- Scores: 3, 3, 3

## Abstract
Pose skeleton images are an important reference in pose-controllable image generation. In order to enrich the source of skeleton images, recent works have investigated the generation of pose skeletons based on natural language. These methods are based on GANs. However, it remains challenging to perform diverse, structurally correct and aesthetically pleasing human pose skeleton generation with various textual inputs. To address this problem, we propose a framework with \textbf{GUNet} as the main model, \textbf{PoseDiffusion}. It is the first generative framework based on a diffusion model and also contains a series of variants fine-tuned based on a stable diffusion model. PoseDiffusion demonstrates several desired properties that outperform existing methods. \textit{1) Correct Skeletons.} GUNet, a denoising model of PoseDiffusion, is designed to incorporate graphical convolutional neural networks. It is able to learn the spatial relationships of the human skeleton by introducing skeletal information during the training process. \textit{2) Diversity.} We decouple the key points of the skeleton and characterise them separately, and use cross-attention to introduce textual conditions. Experimental results show that PoseDiffusion outperforms existing SoTA algorithms in terms of stability and diversity of text-driven pose skeleton generation. Qualitative analyses further demonstrate its superiority for controllable generation in Stable Diffusion

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper proposes a diffusion model-based framework for the task of generating diverse and skeletally structurally stable 2D human pose skeletons (text2pose). The propose model is called PoseDiffusion, a denoising model that incorporates graphical conv networks and learns the spatial relationships of the human skeleton. During training, it represents 2D skeletons as heatmaps (one per keypoint) and add noise to the heatmap. The denoising process is managed by a model called GUNet—a U-Net-like structure based on graph neural networks (GNNs) with graph convolutional layers—to utilize the graph-like nature of human keypoints.

### Strengths
- Novelty. The model takes advantage of the inherent graph structure of human keypoints, allowing it to better capture spatial relationships and dependencies among keypoints. To my knowledge, GNN is not used in human-specific diffusion-based generation yet.

### Weaknesses
 - Motivation. The introduction suggests that the motivation behind PoseDiffusion is to improve the quality of 2D pose skeleton images for controllable human image generation. However, the experiments section does not provide sufficient evidence to substantiate this motivation, as the quantitative evaluation is performed only at the heatmap level. It remains unclear if improvements at the heatmap level translate to better final image generation. The paper lacks a clear demonstration that the proposed method's heatmap outputs lead to superior performance in downstream tasks like controllable image generation, which is the stated motivation.
- Performance. The superiority of this method is not convincing to me through the qualitative results.
  - In the qualitative results (Figure 5) it is unclear whether the proposed method is better than baselines. For example, I think SD 1.5 T2P has more reasonable generation than GUNet. The visual quality of the generated poses from GUNet does not consistently outperform the baseline, and in some cases, the baseline appears to produce more coherent and realistic poses.
  - In Figure 7, it seems that the proposed method does not differentiate between left vs right keypoints. The generated skeletons sometimes appear flipped or mirrored, indicating a potential issue with the model's understanding of spatial orientation and left-right distinctions.
- Evaluation protocol. 
  - Line 455 “we generated 10 pairs of human posture skeletons for the natural language descriptions in the validation set with these models and then compared the coordinates of each keypoint of the generated posture skeletons with the corresponding ground truth to calculate MSE”. How can you compare to the GT since this is a generation task and the generations may be different each time? The use of MSE to compare generated poses with ground truth poses in a generative setting is problematic because it penalizes valid variations in pose. The evaluation protocol should account for the inherent variability in pose generation.
  - In Table 2 the authors use HPSV2 as a quantitative metric. I am not sure if it’s a valid metric since the paper is generating 2d keypoint heatmaps instead of natural images. The author should explain how they apply this metric in detail. The application of HPSV2, a metric designed for evaluating natural images, to keypoint heatmaps is questionable and requires a detailed explanation of how it is adapted for this purpose. It is not clear how the aesthetic score of a natural image can be derived from keypoint heatmaps, and this needs to be clarified.

### Questions
-	In Figure 7, why are the human generations from GUNet sometimes flipped? Shouldn’t the model differentiate left vs. right keypoints  which determines whether the person is facing the camera?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper introduces GUNet, a key component of the PoseDiffusion framework, which generates diverse and structurally stable 2D human pose skeletons from text descriptions. GUNet combines graph convolutional networks with U-Net to capture spatial relationships in human poses, addressing challenges in pose skeleton generation. The framework outperforms existing methods in terms of stability and diversity, offering correct skeletons and enhanced controllability in pose generation.

### Strengths
The paper presents GUNet within the PoseDiffusion framework, an original approach that combines graph convolutional networks with U-Net for text-driven 2D human pose skeleton generation, showcasing creativity in integrating spatial information into the model.

### Weaknesses
1. The manuscript would benefit from a thorough language revision to enhance clarity and readability. The current phrasing is in need of refinement to better convey the research's contributions and methodology.

2. The presentation of the experimental results, particularly the visualizations, falls short of the standards expected for a top-tier conference. There is a need for more compelling and clear visual representations that effectively communicate the outcomes of the research.

3. The novelty of the proposed model, as it stands, is insufficient to distinguish it from existing work in the field. The manuscript should either provide a more detailed justification for the model's innovative aspects or align its claims with the actual contributions to avoid overstatement.

4. Given the current state of the manuscript, with its language, visualization, and novelty issues, it may not be suitable for publication in a top conference. Considerable improvements are necessary to meet the high standards of such venues.

### Questions
Please refer to the weakness part.

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
This paper introduces PoseDiffusion, which uses a diffusion model to generate 2D human pose skeletons from text descriptions. Their denoising model GUNet uses a graph convolutional neural network (GCN) to capture the joint connections within the human skeleton. This results in better-generated poses than those by the Wasserstein GAN with LP normalization.

### Strengths
The approach of using a GCN, connecting joints by the human skeleton seems reasonable, although needs to be compared to a pure transformer-based approach. 

Considers downstream applications such as using the generated keypoints to control generate images with ControlNet.

### Weaknesses
The description of what the baselines are, especially SD1.5-T2P and PoseAdapter, is insufficient to figure out what these models are. It is mentioned that a pose coding layer is added to either just PoseAdapter or both but does not describe well enough what the pose coding layer is and to what part of the model the layer is added. 

UNet-T2H is GUNet without the graph convolutional layer so it is an ablation, not a baseline. 
The remaining baselines are based on WGAN-LP, a 2018 paper.
This is not to say there are no works to compare against with pose generation. One such work is "Adversarial Synthesis of Human Pose From Text" by Yifei Zhang and colleagues. 

Figure 7 and table 2 both claim that a measure of the quality of the generated poses can be measured by the quality of the ControlNet-generated image conditioned on the generated 2d pose. While this is an interesting approach to evaluating generated poses, ControlNet might have its own biases in the images that it can generate that would not help reflect whether or not a conditioned pose is viable. Also, the qualitatives for the ControlNet evaluation do not look convincingly better than the baselines. It would be beneficial to show quantitative improvement, either in FID, Clip-Image similarity or a cycle consistency error on the pose using an off-the-shelf pose detector on the generated images. 

I dont see any viable comparisons in this paper and as a result, I cannot recommend this paper as an accept. In order for me to change my review I need to see comparisons against recent work specifically designed to do text to pose estimation. This can include papers that project from 3d to 2d.

### Questions
I would like to see some discussion and maybe include a baseline for the benefits of graph convolution over a masked transformer architecture.

I would like to see more evaluations that measure the quality of estimated poses using established evaluation metrics. I would also like to see a better argument for why the ControlNet evaluation proposed in the paper is an effective way of evaluating generated poses, and if so, I would like to see qualitatives on this evaluation. 

I would also like to see evaluations against more recent pose generation works.

### Soundness
1

### Presentation
3

### Contribution
1
