# CameraCtrl: Enabling Camera Control for Text-to-Video Generation

- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 6, 8, 6

## Abstract
Controllability plays a crucial role in video generation since it allows users to create desired content. 
However, existing models largely overlooked the precise control of camera pose that serves as a cinematic language to express deeper narrative nuances. 
To alleviate this issue, we introduce \method, enabling accurate camera pose control for text-to-video~(T2V) models. 
After precisely parameterizing the camera trajectory, a plug-and-play camera module is then trained on a T2V model, leaving others untouched. 
Additionally, a comprehensive study on the effect of various datasets is also conducted, suggesting that videos with diverse camera distribution and similar appearances indeed enhance controllability and generalization. 
Experimental results demonstrate the effectiveness of \method in achieving precise and domain-adaptive camera control, marking a step forward in the pursuit of dynamic and customized video storytelling from textual and camera pose inputs. Our project website is at: \href{https://hehao13.io/projects-CameraCtrl/}{https://hehao13.io/projects-CameraCtrl/}.
  \keywords{Camera control \and Video generation}

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
CameraCtrl enhances video generation by enabling precise camera pose control in video diffusion models, preserving narrative nuances through cinematic language. This approach integrates a plug-and-play camera pose control module and demonstrates improved controllability and generalization, with experimental results showcasing its effectiveness across different models.

### Strengths
The motivation is clear.

The results appear promising and solid.

The experiments are thorough.

The writing is easy to follow.

### Weaknesses
Applying a controlnet-like network to incorporate control signals into video diffusion isn’t particularly novel, though the use of Plücker embeddings adds a degree of originality.

Since the RealEstate10K dataset mainly features static videos with few moving objects, could this lack of motion introduce a bias that undermines the base model’s natural grasp of object motion? The foreground objects in the examples provided show limited movement.

There is a need for comparisons and discussion with recent camera control methods, such as VD3D.

### Questions
Please see the weakness part.

### Soundness
2

### Presentation
2

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
This paper proposes a plug-and-play module for control of camera pose. This module can be integrated to various video diffusion models. This module leverages Plücker embeddings to encode camera movements, offering detailed spatial representation compared to traditional numerical values (e.g., extrinsic matrix).

### Strengths
* This is one of the early works that enables adding camera control to existing video models. I believe it will have a positive impact on various downstream tasks.
* While the way of achieving camera control itself isn't technically very novel, the paper presents an intuitive design and provides extensive experimental comparisons on various conceivable design choices (e.g., where to inject the control and different camera representations).
* It is interesting that camera control can be achieved with a lightweight additional adapter without further tuning the video model.

### Weaknesses
 * Since it is fine-tuned on static scene data, it tends to show somewhat reduced ability in generating dynamic motions compared to the original video diffusion baseline (as shown in ODD). But, it shows better performance compared to other methods.
* In object-centric video generation, it appears that the movement of the object is minimal compared to the background. Ideally, models fine-tuned on Objaverse or MVImgNet should be able to generate camera trajectories covering 360 degrees of the object. I'm curious if this model can effectively generate videos when provided with such camera trajectories as input (e.g., generating a video from a frame showing the front of a person to one showing the back).


### Questions
* Why are static scene video datasets mainly used without general video datasets? (For example, one could use general video datasets for training along with estimated camera trajectories from various models like particleSFM.)
* This didn't affect my rating, but I'm curious about the authors' opinions on whether this method can be generally applied to DiT-based methods that do not separate temporal and spatial aggregation.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The authors explore the problem of conditioning a pretrained video generation model on a desired camera motion. The problem is of high relevance not only to the video generation community, but also in 3D and 4D generation. The authors propose the use of a frozen video generation backbone, coupled with a camera encoder block, injecting camera information into the backbone. The method is simple, sound, clearly written and accompanied by a comprehensive evaluation validating the importance of each of the main components: camera embeddings, encoder architecture, feature injection, and training datasets.

### Strengths
- The problem treated in the paper is of high significance to video generation, and 3D/4D generation.
- The paper is very clearly written. Every section of the paper was easy to follow and it appears the information in the paper would be sufficient to replicate the presented method and results. In addition, code is available.
- I appreciate the simplicity of the method. The authors identified the most crucial components to enable camera control: use of Plucker embeddings, camera encoder architecture, how to couple the encoder to the retrained backbone, and training data recipe. Without adding bells and whistles, the authors show good camera control performance.
- Evaluation is solid and informative. Every of the most critical design dimensions (use of Plucker embeddings, camera encoder architecture, how to couple the encoder to the retrained backbone, and training data recipe) is validated in a respective ablation, providing useful insights. The model is demonstrated on diverse video generation backbones
- Qualitative evaluation is rich. Limitations are shown and highlighted

### Weaknesses
 - Discussion of the camera representation could be strengthened by an accompanying figure.
- While Plucker embeddings were found more effective than a set of straightforward alternative representations, their properties do not appear to be completely aligned to the nature of the proposed approach. See questions.

### Questions
- The choice of the Plucker representation appears effective when compared to Euler angles, quaternions and raw values, though some properties of the Plucker representation appear suboptimal for the purpose of achieving camera control. In particular, the set of points along a certain camera ray will have a constant embedding. Sitzmann (2021) introduces the use of Plucker coordinates in the context of LFNs, for which this property is well justified and beneficial. In the context of the current paper, though, Plucker embeddings appear to obscure the camera origin, a fundamental information for the model. With each Plucker embedding defining a set of points along a ray, the only way for the model to recover the camera origin is to solve a system of equations involving multiple rays. This is a necessary, but likely difficult task for the model to perform. Why is this property desirable for this work? Did the authors experiment with alternative representations not suffering from this drawback such as (o, d) or (normalized_o, d) (for some choice of normalization for o) which would make the camera origin readily available to the model?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces a general-purpose encode for a moving camera that can be used to add camera conditioning to different video generator architectures. The paper considers three technical problems: representing the camera, injecting the representation in a video generator, and developing training data sufficient for learning the model. The camera encoding is based on Plucker rays, it is injected in a video generator via cross-attention layers added to the temporal self-attention of the video generator, and the training data combines synthetic and real-life datasets of static contest where the camera is known.

Empirically, the new module is integrated AnimateDiff and in and Stable Video Diffusion (SVD), two different video generators prompted using text. Compared to alternative like MotionCtrl, the approach has better metrics in terms of camera reconstruction and image quality.

### Strengths
* The problem considered by the paper is practically important: camera control is an important feature in many potential applications of video generation

* The approach is technically simple. The architecture design is reasonably well motivated. The performance is shown to be better than close competitors.

* Several applications beyond text-to-video generation with camera control are demonstrated, showing that the method successfully combines with other control types.

### Weaknesses
I remain unconvinced about the formulation of the problem (which is a limitation shared by prior works).

The paper aims at controlling camera motion accurately, but camera motion can only be interpreted in *relation* to the content generated in the video, and this relationship is not well defined in this work. This has several manifestations, discussed next.

First, there is the issue of scale: how a particular value for the camera translation should be interpreted depends on the scale of the generated scene, which is unknown and/or arbitrary. For example, a translation of one meter to our right is entirely negligible if we are looking at the sun, but if we are looking at the chair in front of us it is sufficient to take the object out of view entirely. There is no indication on whether the model is learning a "metric" (or canonical) interpretation of scale; this seems in fact unlikely given the nature of the training datasets which do not posses a well defined scale. The appendix briefly mentions scale as an issue of COLMAP, which requires scale normalisation for evaluation. But this is not a minor issue compared to the  much more serious concern that we cannot assume that the scale of the training data is know. Even if it has "some" value, the latter is often arbitrary and inconsistent (many real-life datasets like MVImageNet use COLMAP for camera annotation; synthetic ones like Objaverse have arbitrary scale).

Even if the training data was "metric", so that one could at least attempt to learn a meaningful canonical notion of scale, and thus interpret camera translation accordingly, this would still be difficult to do for a model. This is a reflection o the fact that very similar content can exist at different physical scales in the world (e.g., model of a city vs city), so learning  a canonical reference scale, insofar as one can be defined, is difficult.

Second, along with scale there is the issue of framing and aligning content and camera motion. Suppose you wanted to move the camera around an object. You could specify a camera trajectory that pivots around a given arbitrary physical point in front of you, in a turn-table-like fashion. Whether the network decides to place an object in correspondence of the pivot point, thus obtaining a turn-table-like effect, is not clear. Camera motion is only useful when its relation to the content is meaningful, so that the subject of the video is framed in the intended way.

Thirdly, there is the issue of the intrinsic parameters of the camera. It is not clear how these are handled in the paper. Specifically, the Plucker ray should be able to encode any camera model/focal length, but it is not obvious whether the authors train the model with different sets of cameras, and if the model is accurate enough to capture focal length correctly. Note that focal length would affect the apparent size of an object in an image, so this also has a strong effect in attempting to learn a canonical/metric interpretation of scale, which seems necessary in this formulation of the problem (see above).

Note that the issue of scale trickles down to evaluation. Even if the content of the video is not well matched to the camera motion (i.e., the framing and/or scale is not what one would expect), the model can still generate a video with the prescribed camera motion. The latter can then recovered using, e.g., COLMAP and compared to the input camera up to scale (for the translation component). The latter is described in appendix, but evaluation of camera reconstruction has been considered extensively int he literature; why not using one of the many standard scale-invariant metrics instead of proposing a new one (line 990)?

More worryingly, the authors state (line 983) that they manually discard badly generated videos where COLMAP fails in their evaluation (line 983). This can very well introduce a selection bias, where their method is favoured by simply discarding difficult videos more liberally than for others. While it is difficult to compare video generators directly due to the aleatoric nature of their task, nevertheless the authors should consider a metric that would at least remove this problem. For example, they could measure success rate, as in the percentage of generated videos where the camera is reconstructed at different levels of accuracy, generating corresponding curves. By prompting different models with the same textual prompts and the same camera motions, such curves would at least be more comparable.

The novelty of the paper is reasonable, but not outstanding. A very similar problem is considered in MotionCtrl and the paper is mostly an iteration that innovates on the three technical components discussed above (better camera encoding, better camera injection, and better data). There is nothing wrong with it, and the results are a bit better, but the conceptual innovation does not run very deep.

# Minor issues

* Line 195: the sentence structure is broken

* Line 460: Do you mean that COLMAP cannot reconstruct the generated videos? Is this an issue with COLAMP or with the quality of generation?

### Questions
* How is scale handled by your model? For example, what is the meaning/effect of translating the camera by, say, one unit to the right? What about two units?

* How do you make sense of the camera motion if you don't know what is going to be generated in the video?

* Does the choice of focal length (camera intrinsics) affect the generated video?

* Can you comment on the potential issues on the evaluation discussed above?

### Soundness
2

### Presentation
3

### Contribution
3
