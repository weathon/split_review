# VD3D: Taming Large Video Diffusion Transformers for 3D Camera Control

- Decision: Accept
- Avg Score: 6.20
- Scores: 8, 3, 6, 8, 6

## Abstract
Modern text-to-video synthesis models demonstrate coherent, photorealistic generation of complex videos from a text description.
However, most existing models lack fine-grained control over camera movement, which is critical for downstream applications related to content creation, visual effects, and 3D vision.
Recently, new methods demonstrate the ability to generate videos with controllable camera poses---these techniques leverage pre-trained U-Net-based diffusion models that explicitly disentangle spatial and temporal generation.
Still, no existing approach enables camera control for new, transformer-based video diffusion models that process spatial and temporal information jointly.
Here, we propose to tame video transformers for 3D camera control using a ControlNet-like conditioning mechanism that incorporates spatiotemporal camera embeddings based on Plucker coordinates.
The approach demonstrates state-of-the-art performance for controllable video generation after fine-tuning on the RealEstate10K dataset.
To the best of our knowledge, our work is the first to enable camera control for transformer-based video diffusion models.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper presents a camera control method for transformer-based video generation models that enhances control while ensuring visual quality. The proposed approach aligns the video perspective with predefined camera trajectories, improving controllability. The authors claim this is the first study to employ ControlNet-like guidance for global spatiotemporal transformer video generation models, in contrast to the more commonly used U-Net architecture. Moreover, the evaluation demonstrates that both the video quality and adherence to the input camera trajectories are state-of-the-art.

### Strengths
Camera control during the video generation process is a significant issue. As more foundational models adopt transformer architectures, exploring control mechanisms for these models becomes crucial. This paper is the first to investigate how to better utilize camera trajectory parameters for transformer-based video generation models, using SnapVideo as the foundational model. The design is well thought out, and the evaluation is rigorous. The strengths of the paper are as follows:

- Unlike the spatiotemporal decoupling generation of U-Net structures, transformer-based video generation considers spatiotemporal video tokens globally, which means it cannot directly leverage the advantages of spatiotemporal decoupling. This paper overcomes this limitation by being the first to explore control specifically for spatiotemporal transformers. This shift in foundational model structure is critical and provides a solid engineering foundation for future work.
  
- The authors use Plücker embeddings to convert camera intrinsic and extrinsic parameters into pixel-level controls, which match the shape of video tokens. This information is then introduced through read cross-attention layers. While this approach is a straightforward combination of existing methods, it has been validated as effective for transformer-based video generation models, providing valuable experimental insights.
  
- The paper includes comprehensive evaluations and ablation studies, conducting both qualitative and quantitative experiments regarding video content quality and camera control, with well-defined criteria. The evaluation of baseline models is fair, making the transition to the new foundational model structure more convincing.

### Weaknesses
 - While camera control is the central problem addressed in this paper, the camera trajectories used primarily come from the RealEstate10K dataset, which, as observed in the visual results, mostly follow smooth, straight lines. There is a lack of consideration and experimentation with trajectories of varying difficulty, such as those involving significant directional changes. This raises some questions regarding the trajectory settings.
  
- There have been several prior works in the 3D multi-view generation field that focus on similar camera control issues, such as the referenced *Cat3D*, which also employed Plücker embeddings and attention calculations. The distinction between spatiotemporal decoupling and other network characteristics is a design feature intrinsic to the architecture. In exploring DiT-based generation, there have also been multiple studies investigating spatiotemporal decoupling, such as *Latte: Latent Diffusion Transformer for Video Generation*. Therefore, the novelty of this work lies more in applying existing designs to spatiotemporal transformers rather than presenting a technological innovation. However, the state-of-the-art results under the new configuration indeed serve as an important engineering reference for future directions.

### Questions
- Have there been additional relevant experiments regarding camera trajectories, such as comparisons of control quality for generated trajectories of varying complexity?

At this time, I have no further questions.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The method proposes a controlnet-like architecture for a private video diffusion model by including plucker coordinates as camera control.

### Strengths
- The proposed controlnet design outperforms other model variants designed by the authors. The evaluations are thoroughly conducted for the design choices. Detailed ablations are provided.

### Weaknesses
 - The proposed framework overfits on the trajectories that are seen during training. Though the authors provide quantitative comparisons in Tab. 8, no visual comparisons are provided. 
- Though the performance is impressive, the technical contribution is limited in the proposed framework. Training a ControlNet for diffusion transformer is not new, as shown in [1]. Using Plucker coordinates for camera control is not new, as shown in CameraCtrl (He et al., 2024a). The core novelty of the method, the projection mechanism, is not clearly defined and its difference from a standard ControlNet is not well explained. The authors claim a novel projection mechanism, but it is unclear if this is simply a single linear layer for projection instead of multiple layers, which is not a significant contribution. Furthermore, the paper claims that the proposed approach has an extra level of complexity due to the spatio-temporal nature of the transformer, but the method simply concatenates the camera information along the extra dimension, which is a standard approach. The evaluation on SnapVideo is also questionable, especially given that the vanilla DiT version performs better, raising questions about the purpose of building on top of SnapVideo. The paper does not clarify if the baselines (MotionCtrl and CameraCtrl) are also implemented using a vanilla DiT for a fair comparison. The implementation details of the CameraCtrl baseline are also unclear. It is not clear if the authors are fine-tuning a camera encoder trained from AnimateDiff or if they are implementing a SnapVideo version of CameraCtrl using zero-convolution plus a copy of SnapVideo layers. The paper also does not clarify if all CameraCtrl variants mentioned in the paper are implemented the same way. Finally, the reliability of Particle-SfM results when evaluating videos without translation is not discussed.

### Questions
Can the authors please comment on the above-mentioned weaknesses?

### Soundness
2

### Presentation
2

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
This paper provides a method for adding the control of camera movements to video diffusion transformers. The core idea is to represent camera conditions as pixel-level ray condition with Plucker embeddings. A ControlNet inspired module is used to process the camera condition. The model is finetuned on RealEstate10k and is compared to two similar methods both qualitatively and quantitatively.

### Strengths
- paper is easy to follow
- the proposed design including the Plücker embedding is reasonable and effective
- comprehensive experiments are conducted and presented in the main manuscript and appendix
- supplemental materials contain video samples to demonstrate the effectiveness

### Weaknesses
 - The proposed method has been evaluated only on one video diffusion transformer, which raises some concerns on whether its performance can generalize to other pretrained video diffusion transformers.
- I'm curious about the distribution of camera movements evaluated in the experiments, in terms of its diversity and similarity to natural camera movements.
- The novelty is slightly limited, as the task is not new, and ControlNet-like module as well as Plücker embedding have been explored and used before.

minor:
- CameraCtrl was appeared on arXiv in April 2024, which should not be considered as a concurrent work.

### Questions
Overall I think this paper provides an effective solution to amend video diffusion transformers with camera control. See weaknesses for questions and discussion.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper proposes a first method to condition spatio-temporal transformer-based video diffusion models on camera poses (previous methods focused on pre-trained U-Net-based diffusion models). To this end, they propose a ControlNet-like block that conditions the model on camera embeddings that are based on Plucker coordinates. The paper evaluates the choices made and demonstrates good results, both qualitatively and quantitatively.

### Strengths
The paper presents a nice idea on to enable spatio-temporal transformer-based video diffusion models with camera control. It is the first to do so by using a ControlNet-like block in combination with Plucker coordinates, and presents a nice contribution. I value the ablation studies in the paper and the reasoning as to how they arrived at this particular architecture. The paper is quite well-written overall. It's easy enough to follow and appreciate the contribution.

### Weaknesses
While I'm positive overall, there are a few weaknesses.

A criticism that could be made is that this paper is a bit of an A+B paper, where A is the ControlNet block and B is the Plucker coordinates. I don't think that's a useful criticism, because at the end of the day it's a sensible thing to do and the authors demonstrate that you need to do a few things to make it work (Table 2).

The paper reads well overall, however, I'm not a fan of Figure 3. It's hard to interpret what goes where, and how this relates to the formulas. I'd suggest to clearly delineate what are the video patch tokens vs. the plucker patch tokens, maybe add the variables from the formulas to the appropriate boxes, and overall structure the figure so that the separate blocks are clearly separate.

Finally, in terms of results, I would have liked to see more examples of the same scenes with different camera control (there are only three examples). Furthermore, most examples use input camera trajectories from scenes that are completely unrelated to the target scene. It be nice to see some that are related -- makes it easier to judge if the generated camera path is good or not.

### Questions
Nothing crucial.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper presents a novel approach to incorporating camera movement control into Transformer-based video diffusion models. While camera control has been extensively studied in UNet-based video diffusion models, this area remains largely uncharted for Transformer architectures. The author introduces an additional ControlNet-like network to inject tokenized Plücker embeddings, demonstrating that this design enhances both visual quality and controllability.

### Strengths
1. The authors made an important step forward in camera control for the Transformer-based video diffusion model, which is unexplored by previous research;
2. The visual quality and motion dynamics of the generated videos are excellent;
3. The methodology is clearly explained and easy to understand.

### Weaknesses
1. The main components of the method have been validated by previous works, for instance, the Plucker embedding as camera representation (CameraCtrl), and training on RealEstate10K(MotionCtrl, CameraCtrl);

2. As mentioned in 1., I would say the specified designs for Transformer architecture are the major contribution of the paper. However, SnapVideo's architecture is not a typical DiT (it has the "read" operation, and the attention is not performed on the actual tokens). It's not clear how to extend the proposed method for a standard video DiT and how the performance would be.

3. For the MotionCtrl baseline, the visual quality degrades when the base model is fine-tuned. Would it be better to freeze the backbone?

4. Would be better to also provide the trainable parameter scale of the two baselines and the proposed method.

### Questions
1. Line 272, R_1, t_1 can be interpreted as the original extrinsic or the extrinsic after normalization. It would be better to use R'_1, and t'_1 to represent the extrinsic after normalization;

2. I am not quite clear about the baseline implementation details. From my understanding, for MotionCtrl, one additional learned token is concatenated to the video patch tokens, while for CameraCtrl, the camera encoder produces additional latent tokens. Is that correct?

3. While previous works sacrifice motion dynamics when training on RealEstate10K (mostly static scenes), the video in the supplementary material exhibits better and larger motions. What would be the possible reasons for the difference?

### Soundness
3

### Presentation
3

### Contribution
3
