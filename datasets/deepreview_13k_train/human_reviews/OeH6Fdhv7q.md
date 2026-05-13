# TapMo: Shape-aware Motion Generation of Skeleton-free Characters

- Decision: Accept
- Scores: 6, 6, 6, 8

## Abstract
Previous motion generation methods are limited to the pre-rigged 3D human model, hindering their applications in the animation of various non-rigged characters. In this work, we present TapMo, a \textbf{T}ext-driven \textbf{A}nimation \textbf{P}ipeline for synthesizing \textbf{Mo}tion in a broad spectrum of skeleton-free 3D characters.
    The pivotal innovation in TapMo is its use of shape deformation-aware features as a condition to guide the diffusion model, thereby enabling the generation of mesh-specific motions for various characters.
    Specifically, TapMo comprises two main components - Mesh Handle Predictor and Shape-aware Diffusion Module. Mesh Handle Predictor predicts the skinning weights and clusters mesh vertices into adaptive handles for deformation control, which eliminates the need for traditional skeletal rigging. Shape-aware Motion Diffusion synthesizes motion with mesh-specific adaptations. This module employs text-guided motions and mesh features extracted during the first stage, preserving the geometric integrity of the animations by accounting for the character's shape and deformation.
    Trained in a weakly-supervised manner, TapMo can accommodate a multitude of non-human meshes, both with and without associated text motions. We demonstrate the effectiveness and generalizability of TapMo through rigorous qualitative and quantitative experiments. Our results reveal that TapMo consistently outperforms existing auto-animation methods, delivering superior-quality animations for both seen or unseen heterogeneous 3D characters. The project page: \url{https://semanticdh.io/TapMo}.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The main contribution of this paper is a motion diffusion model that can take shape-deformation features as inputs to generate shape-aware motions. This function is desirable in the computer animation, which can save a lot of efforts in the animation production. The proposed pipeline has two components: mesh handle predictors to predict skinning weights and underlying skeletons and shape-aware motion diffusion models that can synthesizes motion with mesh-specific adaptations.

### Strengths
1.  the generated animations for a variety of 3D characters are impressive. The structure of the 3D meshes are well recognized when associating it with the animations. 

2. The application of shape deformation feature in animation is nice.

### Weaknesses
There are still penetrations between foot and ground in the generated animations, which downgrade the animation quality.

### Questions
Please clarify how the adversarial loss is trained in the rebuttal.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
TapMo is a text driven motion synthesis framework for skeleton-free 3D characters. Addressing limitations of relying on pre-rigged character models, TapMo introduces the Mesh Handle Predictor and the Shape-aware Motion Diffusion. These components enable the framework to generate motions of skeleton-free characters using text descriptions. Specifically, Mesh Handle Predictor predict the skinning weights and can clusters mesh vertices into adaptive handles. Then the Shape-aware Motion Diffusion takes mesh deformation feature and output handles' motion. Trained in a weakly-supervised manner, TapMo demonstrates its performance in generating animations for novel non-human characters.

### Strengths
The research addresses an interesting and promising problem, as far as I know it is the first attempt to enable text-driven motion synthesis for skeleton-free characters.

Comprehensive experiments are conducted, yielding impressive results across diverse shapes. Supplementary videos and a user study further validate the naturalness of the generated results.

The combination of diffusion-based motion synthesis and skeleton-free mesh deformation is interesting and novel.

### Weaknesses
Some details are not clearly explained, such as the mesh deformation feature, what exactly is f_ and how it's obtained, and its dimensions, which are not reflected in the main text. From the appendix, it seems to be a 512-dimensional vector. Further explanation from the authors is desired. And how does mesh-specific adaptation affect the vertices, it is not included in the equations. How is the Discriminator implemented? Are the two modules trained jointly or separately?

What are the visualization and qualitative results for Handle-FID? Specifically, what are the two SMPL human models and what do the results look like? On the other hand, are two models enough? Why don't authors try MGN ("Multi-garment net: Learning to dress 3d people from images") which includes clothed human models and can use SMPL pose parameter to drive.

I recommend the authors discuss the following skeleton-free papers: "Zero-shot Pose Transfer for Unrigged Stylized 3D Characters" and "HMC: Hierarchical Mesh Coarsening for Skeleton-free Motion Retargeting". The self-supervised shape understanding method in the former could potentially strengthen handle prediction including mesh deformation feature extraction.

The authors could try using the PMD metric in SfPT and the previous works, which allows for direct comparison with ground truth vertices and can judge both motion and mesh quality, this is suitable for SMPL-based models.

Can the authors provide qualitative results before and after Motion Adaptation Fine-tuning? The post-process usually results in big differences in naturalness.

Compared to Eq1 in SfPT, if we ignore the global translation and rotation of the root, authors added $\tau^{l}_k$ and $h_k$, which seems different from SfPT Eq1. Could the authors explain the purpose of this?

For local translations and local rotations, their first dimension is K. Does this include the root (first) handle? Is k=1 represent root handle in Eq. 3? Or there are K-1 local translations/rotations from k=2 to k=K.

In Eq.7, defining handle adjacent handles is required, is this something that needs to be done separately for each character? For instance, shapes with large differences as in Figure 6. Is this only necessary during training or during inference? And how many characters need to be specifically defined?

In the first paragraph of the Method section, does "skinning weight s of the handle" refer to the skinning weights of the vertices?

### Questions
Compared to Eq1 in SfPT, if we ignore the global translation and rotation of the root, authors added $\tau^{l}_k$ and $h_k$, which seems different from SfPT Eq1. Could the authors explain the purpose of this?

For local translations and local rotations, their first dimension is K. Does this include the root (first) handle? Is k=1 represent root handle in Eq. 3? Or there are K-1 local translations/rotations from k=2 to k=K.

In Eq.7, defining handle adjacent handles is required, is this something that needs to be done separately for each character? For instance, shapes with large differences as in Figure 6. Is this only necessary during training or during inference? And how many characters need to be specifically defined?

In the first paragraph of the Method section, does "skinning weight s of the handle" refer to the skinning weights of the vertices?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work focuses on an interesting research topic - synthesizing motions for skeleton-free 3D characters, with two main modules: 1. Mesh Handle Predictor, and 2. Shape-aware Motion Diffusion Module.  In addition, this work utilizes the shape deformation-aware features as a condition to guide the motion generation for specific character models. The proposed method could show impressive generated animations for both seen and unseen characters.

### Strengths
1. it is good to study generating shape-aware motions, especially for non-humanoid 3D characters.
2. The proposed method seems to be reasonable and might be promising to generate motions for unseen characters.

### Weaknesses
1. The proposed mesh handle predictor is simple and straightforward, but it is not clear how the proposed method resolves different characters that have different topologies with different semantics.  Currently, the manuscript mentions that "each handle is dynamically assigned to vertices with the same semantics across different meshes", but it is not clear how the method will select those handles. Also, it is unclear how the method will choose the number of handles since different topologies tend to have different numbers of handles. It is unclear how the proposed method could achieve training with different numbers of handles.

2. The proposed Shape-aware Motion Diffusion seems to be simple modifications for existing methods (e.g., MDM), but the current presentation makes it overcomplicated, and difficult for readers to get the key designs that could highly improve the motion generation quality. I am not sure if considering the character shapes is the major factor that improves the quality, and the others could make further improvements.

3. The experiments seem to be insufficient.  HumanML3D dataset is the only benchmark that is used to report quantitative comparisons.  However, recent methods, such as MotionDiffuse[1], ReMoDiffuse[2], and T2M-GPT[3] have not been discussed.

### Questions
The authors could answer my questions asked in the weakness section first.
Besides, I would like to suggest the authors could improve its readability and also highlight the key design.
For the experiments, I would like to see more generated motions, especially for non-humanoid characters and unseen characters.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper (TapMo) tackles text-guided character motion generation in a skeleton-free manner. It can be thought of as the intersection of  MDM (a human-specific motion generation method) and SfPT (a category-agnostic per-frame pose transfer method). Combining the two enables new capabilities -- text-guided motion generation for generic shapes.

Method-wise, instead of simply combining the two prior works, TapMo made innovations on (1) modeling root movement by an additional root handle (2) taking shape into account when generating handle movements (3) introducing a delta term to account for motion that cannot be explained by a fixed number of handles.

The video nicely demonstrates the capability of motion generation beyond human characters.

### Strengths
**Significance**
- The paper is a nice first step toward motion generation for generic characters. 

**Quality**
- The method is sound and relatively simple.
- The motion generation results are impressive, especially for the walking hand and animals. 

**Presentation**
- The visual illustrations are well done, and the paper is easy to follow. I enjoyed reading them.

### Weaknesses
 **Data**
- The metrics are reported on a human dataset (HumanML3D), which does not show off the cross-category generation ability of the proposed method. Evaluating the method on a dataset with characters beyond humans would be beneficial, such as deforming things 4D [A]. The lack of evaluation on non-human datasets makes it difficult to assess the true generalization capability of the method, especially given the claim of handling diverse shapes. The current evaluation primarily focuses on motion quality within a single category, rather than demonstrating the method's ability to adapt to different morphologies and motion styles.

**Method**
- Driving signal. The driving signals seem to be limited to text in the current form. However, there are motions that cannot be described purely by natural language, such as body gestures, facial expressions, hair movements, etc. This is not necessarily a weakness, as the paper already made the setup clear. The reliance on text input limits the expressiveness of the system, potentially missing out on nuanced motion cues that are not easily captured by language. For instance, subtle shifts in weight, momentum, or anticipation are difficult to articulate textually, which could limit the system's ability to generate highly realistic and complex movements.
- Representation. To generalize to fine-grained motion, such as cloth deformation and hair, the handle-based deformation with a limited number of handles (K=30) seems not enough. The use of a fixed number of handles may struggle to capture complex deformations, especially in areas with intricate details or highly dynamic motion. This limitation could lead to artifacts or a loss of fidelity in the generated animations, particularly for characters with complex geometries or clothing.

### Questions
1. The model is trained on text-motion pairs of human motion but seems to be able to generalize to other categories like quadruped animals. This is interesting. Is the text description transferable over bipeds and quadrupeds? Has the model seems quadruped motion before? 

2. The methods use both diffusion-based reconstruction loss and GAN loss. In which case is the GAN loss necessary/complementary to diffusion loss? What happens if GAN loss is removed?

3. In Table 1, the TapMo variants have a much higher Diversity metric than top rule methods. Is there an explanation? Additionally, the Multimodal Dist and Multimodality results are not explained in the paper. Explanations on why certain method performs better/worse would be useful.

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good
