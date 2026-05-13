# Gaussian Head & Shoulders: High Fidelity Neural Upper Body Avatars with Anchor Gaussian Guided Texture Warping

- Decision: Accept
- Scores: 6, 6, 5, 6, 8

## Abstract
The ability to reconstruct realistic and controllable upper body avatars from casual monocular videos is critical for various applications in communication and entertainment. By equipping the most recent 3D Gaussian Splatting representation with head 3D morphable models (3DMM), existing methods manage to create head avatars with high fidelity. However, most existing methods only reconstruct a head without the body, 
substantially limiting their application scenarios.
We found that naively applying Gaussians to model the clothed chest and shoulders tends to result in blurry reconstruction and noisy floaters under novel poses. This is because of the fundamental limitation of Gaussians and point clouds -- each Gaussian or point can only have a single directional radiance without spatial variance, 
therefore an unnecessarily large number of them is required to represent complicated spatially varying texture, even for simple geometry.
In contrast, we propose to model the body part with a neural texture that consists of coarse and pose-dependent fine colors. To properly render the body texture for each view and pose without accurate geometry nor UV mapping, we optimize another sparse set of Gaussians as anchors that constrain the neural warping field that maps image plane coordinates to the texture space. We demonstrate that Gaussian Head \& Shoulders can fit the high-frequency details on the clothed upper body with high fidelity and potentially improve the accuracy and fidelity of the head region. We evaluate our method with casual phone-captured and internet videos and show our method archives superior reconstruction quality and robustness in both self and cross reenactment tasks. To fully utilize the efficient rendering speed of Gaussian splatting, we additionally propose an accelerated inference method of our trained model without Multi-Layer Perceptron (MLP) queries and reach a stable rendering speed of around 130 FPS for any subjects.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes a method to reconstruct upper body avatars from videos based on 3D Gaussian Splatting. The method models head and shoulders separately, i.e., heads by 3D Gaussians anchored on 3DMM template, and shoulders by Anchor Gaussians and neural textures. The paper proposes a Neural Texture strategy to model shoulders with less 3D Gaussians. The authors evaluate their methods on different experimental datasets and human subjects.

### Strengths
The paper has a clear structure, and it‘s easy to follow.
The idea of modeling the head and shoulder separately is interesting. The neural texture strategy can model the shoulders efficiently with less 3D Gaussians.
The pipeline is verified on different human subjects.

### Weaknesses
The method models head and shoulders separately, i.e., different Gaussian representations and different tracking approaches. This causes a limitation, i.e., the head and shoulders are misaligned for some relatively big body movements. 

It seems that the Anchor Gaussian only supports relatively simple should motions. It’s not verified that the proposed method can model pose-dependent wrinkles for the shoulders in the paper. The body movements in the supplementary demo are too simple, and I cannot observe that the clothing wrinkles vary with poses.

### Questions
Considering the 3DMM parameters and landmarks of the shoulder are acquired separately, is there a method to unify the two tracking results? It seems that the head and shoulder are misaligned in some frames.

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
3

### Summary
This paper proposes a Gaussian splatting based deformable avatar method with a specific focus on modelling shoulders with a high fidelity. The head is represented by a set of 3D Gaussians while the shoulders are represented by a neural texture map. The gaussians on the head are deformed from the canonical space using Linear Blend Skinning while the texture-map for the shoulders are warped using a pose dependent MLP. Once in the deformed space, both the neural textures and the gaussians are rendered to yield the final image. The properties of the gaussians and the warpings are learnt through a set of RGB and deformation based losses. The neural texture warping is specifically constrained through an anchor loss defined using a set of Gaussians learnt on the shoulders. Both quantitative and qualitative show improvements over prior work.

### Strengths
1) The paper is well written and easy to follow
2) The use of a neural texture map to model the shoulders is well motivated and intuitive
3) The additional loss terms introduced are well ablated in both the main paper and the supplementary
4) The proposed method both qualitatively and quantitatively outperforms prior work

### Weaknesses
1) There are no significant out-of-plane view synthesis results that are shown in the results to demonstrate whether or not the learn texture map is able to generate novel renders of the shoulders in a geometrically consistent way or it just renders them as a plane 

2) This paper is, I believe, a little out of scope of ICLR and is more suited at a vision or graphics conference. However, I will defer to other reviewers and the AC for that before I consider it as a strong weakness.

3) There is no ablation of exactly how robust the proposed method is to shoulder movement in the capture video. Understanding this would help evaluate the method more throughly (I do grant that prior work does not even address this problem, but I believe this is important to make the paper more complete.)

4) Any reason why Splatting-avatar results are so much worse compared to the other methods?

### Questions
1) As mentioned above, I’m curious to see novel out-of-plane renders of the shoulders themselves to see how geometrically accurate they are. 

2) There is no ablation of exactly how robust the proposed method is to shoulder movement in the capture video. Understanding this would help evaluate the method more throughly (I do grant that prior work does not even address this problem, but I believe this is important to make the paper more complete.)

3) Any reason why Splatting-avatar results are so much worse compared to the other methods?

### Soundness
3

### Presentation
1

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces a method to create a high-fidelity head avatar.
This method maps intricate texture to the image plane through a sparse set of anchor Gaussians driven by 3DMM, not only reconstructs the head, but also the upper body parts.
In addition, this paper also proposes a method to use Gaussian spraying to speed up rendering.

### Strengths
- This paper uses neural textures to model body parts simultaneously, instead of just the head.
- The paper proposes a method to accelerate reasoning, so that the rendering speed can reach 130 frames per second.

### Weaknesses
 - This paper lacks comparisons with some methods in terms of head reconstruction quality, including [1, 2].
- The head part of this method is similar to the theory of existing methods (PSAvatar).
- The tracking results given in Figure 11 are not convincing. In many body tracking projects, some scenes containing half of the body can still produce reasonable results. For example, One-Stage 3D Whole-Body Mesh Recovery with Component Aware Transformer. The paper should describe in more detail the methods used for tracking and why they were failed, otherwise I don't see the point why not using the upper body SMPL model.


### Questions
- Since the modeling of the body parts starts from a canonical frame/space, will the selection of this canonical frame significantly affect the reconstruction quality?
- I still have doubts about how this method drives the reconstruction of the upper body of the character for unseen self-driving frames and cross-driving frames. From the visual results, it seems that the upper body is not aligned with the driving frame.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper addresses the challenge of creating realistic upper body avatars from monocular videos. Existing methods focus on head avatars and struggle with detailed body textures, resulting in blurry reconstructions. The proposed solution uses neural textures guided by sparse Gaussians to improve fidelity and speed, achieving up to 130 FPS, and excels in both self and cross-reenactment tasks.
Contributions:
1. It uses anchor Gaussians to effectively model detailed upper body textures.
2. It eliminates MLP queries for faster speeds, reaching about 130 FPS.

### Strengths
1. This method effectively models detailed upper body textures.
2. This paper combines 3DGS and neural fields to construct head and body textures, showcasing technical novelty.
3. Experimental results demonstrate that this method has significant advantages in rendering accuracy and inference speed while using a smaller number of 3D Gaussians.

### Weaknesses
1. The article lacks some clarity in its writing. For example, it does not explain what texture space is in the introduction.
2. The article could include additional baselines, such as Gaussian Avatars and Gaussian Head Avatar.
3. Regarding the rendering formula in Section 3.5, the coefficient for the third term, body texture, is the product of the opacities of the first two terms. Wouldn't this cause most of the pixels' colors in the third term to be overridden?

### Questions
1. FlashAvatar is motivated by inference acceleration. Has this paper calculated its FPS?

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This work present the way of rendering shoulders in addition to the human faces. In general, the author propose the following methods:
(1) to use anchor gaussians to represent the shoulder region only.
(2) use neural texture to refine the shoulder represent and make it robust to body motions including translation, rotation, and depth-based motions;
(3) Leverage 3D-to-2D correspondence mapping as the regularization of the shoulder learning.
(4) an option without using MLP for fast rendering

The author conducts many experiments to validate their method.

### Strengths
The overall writing is easy to following and well-written.

It seems like compared with conventional method, which ignore the shoulder but only focus on face, this model presents better performance and more robust to shoulder renderings (like compare with PointAvatar and GS*)

### Weaknesses
Concerns of Comparisons:

1. Some works already tries to explore the joint face and shoulder rendering including:
   a. Real3D-Portrait, which uses FOMM for the shoulder motion reenactment and finally merge the face motion and shoulder motion together.
  b. StyleAvatar, a 2D human face rendering technique which includes the face, shoulder and background together

The author did not include these two into the comparison. Is it possible to compare with this pipepile with FOMM/TPS-based methods used in Read3D-Portrait / Torso NeRFs used previously in GeneFace to see whether this method is more effective? Specifically, a comparison focusing on the shoulder region's rendering quality and motion fidelity would be beneficial. In addition, using neural texture as an whole image enhancement method is also covered in StyleAvatar, but slightly different: this work tries to enhance the shoulder only while StyleAvatar's neural texture is for the whole image. It will be good if the authors can present very strong argument regarding this given my evaluation might be partially wrong.

Data:
The videos in the supplementary material do not present very large shoulder motions. I am not quite sure whether the model is robust in rendering the shoulder. However, I do see for slight shoulder motions, the model's performance is good.

Experiment:
I did not see the ablations for the main method part. The proposed methods include introducing the anchor gaussians for shoulder only, the 3d-2d correspondence, the neural texture compared with the baseline GS and PointAvatar. I will defer this part in the questions.

### Questions
1. Can the authors provide the novel view synthesis for rendering the shoulder and also present the volumetric representation of the shoulder areas to let readers know how robust the model is for shoulder rendering?

2. What exactly each module brings or benefits for the shoulder rendering? I think the following are possible ablations: 
(a) completely remove anchor gaussian and the 3D-2D correspondence, only relying on neural texture like in StyleAvatar
(b) exclude Neural texture, use anchor gaussian only

3. For the anchor gaussian, how the deformation achieved? If it is relying on LBS, due to that LBS is based on flame mesh that only contains the head and neck, there does not exist a real LBS for the shoulders. How should we understand the relationship between the deformation of shoulder gaussian point and neural texture? Is it a refinement of potential noisy deformed gaussian points?

### Soundness
2

### Presentation
3

### Contribution
2
