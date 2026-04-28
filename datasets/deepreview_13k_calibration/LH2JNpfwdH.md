# Towards 4D Human Video Stylization

- Decision: Reject
- Avg Score: 5.67
- Scores: 6, 6, 5

## Abstract
We present a first step towards 4D (3D and time) human video stylization, which addresses style transfer, novel view synthesis and human animation within a unified framework. While numerous video stylization methods have been developed, they are often restricted to rendering images in specific viewpoints of the input video, lacking the capability to generalize to novel views and novel poses in dynamic scenes.
To overcome these limitations, we leverage Neural Radiance Fields (NeRFs) to represent videos, conducting stylization in the rendered feature space. Our innovative approach involves the simultaneous representation of both the human subject and the surrounding scene using two NeRFs. This dual representation facilitates the animation of human subjects across various poses and novel viewpoints. Specifically, we introduce a novel geometry-guided tri-plane representation, significantly enhancing feature representation robustness compared to direct tri-plane optimization.
Following the video reconstruction, stylization is performed within the NeRFs' rendered feature space. Extensive experiments demonstrate that the proposed method strikes a superior balance between stylized textures and temporal coherence, surpassing existing approaches. Furthermore, our framework uniquely extends its capabilities to accommodate novel poses and viewpoints, making it a versatile tool for creative human video stylization.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes editing videos using the 4D NeRF representation. The video is firstly reconstructed as the static background NeRF plus a Neural Avatar. For style transfer, it uses the feature from the NeRF backbone and projects it to the stylized space.  With this canonical representation, it can generate consistent results when editing viewpoint, human pose, and style.

### Strengths
The overall idea is technically sound. Using NeRF-like canonical representation can solve video editing problems in a unified framework.

### Weaknesses
(1) Limited technical novelty. The NeRF reconstruction part is almost identical to NeuMan except that it uses a tri-plane representation, which has also been exploited widely. This choice is straightforward. The style transfer part follows AdaAttn without any modification. So the main paper is a straightforward combination of two existing works.


(2). The overall visual quality is low, as shown in the paper and supplement material. Editing viewpoint and human pose is not new as this part is almost identical to the NeuMan.  But for stylization, compared to existing baselines, the qualitative experiments are not enough, just less than 5 style transfer results are shown. 

(3). The comparison to existing baselines is not fair. This paper stylizes foreground and background separately while baseline methods are applied in a foreground-agnostic manner. I believe it is easy to extend existing work to be segmentation-aware. 

(4). Lacking comparison with other video editing baselines which also exploited a layered and canonical representation. e.g.,
Layered Neural Atlases for Consistent Video Editing, SIGGRAPH Asia 2021,
This baseline can be easily extended using AdaAttn by optimizing the canonical atlas.

(5) Minor wriring issues
In Equ.5. \mathcal{E}(x) should also depends on frame indices.

### Questions
Please address the weakness (1),(2),(3) and optionally (4)

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes a novel method for human video stylization that leverages 2 NeRFs to represent backgrounds and the human body separately. 
It introduces a geometry-guided tri-plane representation to learn the 3D scene more efficiently and effectively. The proposed method can accommodate novel poses and viewpoints, making it a versatile tool for creative human video stylization.

### Strengths
The paper proposes a novel method for human video stylization that leverages 2 NeRFs to represent backgrounds and the human body separately. 
The proposed geometry-guided tri-plane representation enhances feature representation robustness compared to direct tri-plane optimization by introducing a geometric prior on the tri-plane. This geometric prior is achieved by discretizing the 3D space as a volume and dividing it into small voxels, with sizes of 10 mm × 10 mm × 10 mm. Voxel coordinates transformed by the positional encoding are mapped onto three planes to serve as the input to the tri-plane.

### Weaknesses
The proposed contributions are trivial besides the two Nerf ideas.
The AdaAttN, loss functions are all borrowed from existing methods.
The demo results didn't show large angles of novel views from the backgrounds.

### Questions
Have you thought of using DeamFusion-like models to generalize on the background scene generation? Maybe this can help with adding information to your 3D scene.

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper desribes a NeRF based video stylization methods. The authors propose to split human action and background scenes into two different NeRF to synthesis novel views and a novel geometry-guided tri-plane representation to enhanced feature representation robustness and synthesis quality. The stylization is then performed within the NeRFs’ rendered feature space. Both qualitative and quantitative experiments have been conducted to demonstrate that the proposed method outperforms existing approaches.

### Strengths
1.By spliting human gesture and background scene into two different NeRF branches, the proposed method can effective synthesis novel views and animated human.
2.The proposed geometry-guided tri-plane representation can effectively stablize image synthesis and improve result quality.
3.Compared to previous methods, the generated samples have better visual quality

### Weaknesses
1.While there are plenty of video stylizatio works, in the experiment section, the authors only compare the proposed method with 3 exsisting methods, which seems to be not adequate.

2.In both qualitative comparison (table2) and user study (Figure 5), the advantage of proposed method over previous seems not very obvious. Especially in user study, the proposed method only have obvious advantage over CCPL but received similar evaluation compared to LST and AdaAttN

3.The authors are putting "4D" in the title, trying to emphesize the contribution on video stylizaiton. Personally I don't think it's proper to regard the video stylization as a main contribution of this paper, as the proposed method directly apply stylization on the NeRF rendered feature space and doesn't have any mechanism for inter-frame stablizaiton. Also, the novel view synthesis / human animation function and stylization seems to have little connection.

### Questions
The stylization is directly applied on the NeRF rendered feature space, and seems to have littile connection to the proposed geometry-guided tri-plane representation and two branch NeRF for human and background scene. Also, in the METHODOLOGY section, the authors are repeatedly mentioning that many components of the framework are motived by previous methods. How could authors persuade reviewers the proposed the framework is innocative instead of an incremental work with the combination of previous works?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
