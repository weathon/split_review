# GVFi: Learning 3D Gaussian Velocity Fields from Dynamic Videos

- Decision: Reject
- Avg Score: 5.25
- Scores: 6, 6, 3, 6

## Abstract
In this paper, we aim to model 3D scene geometry, appearance, and physical information just from dynamic multi-view videos in the absence of any human labels. By leveraging physics-informed losses as soft constraints or integrating simple physics models into neural networks, existing works often fail to learn complex motion physics, or doing so requires additional labels such as object types or masks. In this paper, we propose a new framework named **GVFi** to model the motion physics of complex dynamic 3D scenes. The key novelty of our approach is that, by formulating each 3D point as a rigid particle with size and orientation in space, we choose to directly learn a translation rotation dynamics system for each particle, explicitly estimating a complete set of physical parameters to govern the particle's motion over time. Extensive experiments on three existing dynamic datasets and two newly created challenging synthetic and real-world datasets demonstrate the extraordinary performance of our method over baselines in the task of future frame extrapolation. A nice property of our framework is that multiple objects or parts can be easily segmented just by clustering the learned physical parameters. Our datasets and code will be released at https://github.com/

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces GVFi, a novel approach for modeling 3D scene geometry, appearance, and dynamics from multi-view images without the need for human annotations, such as bounding boxes or segmentations. The authors highlight that previous 3D Gaussian Splatting models struggled to capture the underlying motion physics of dynamic scenes. In contrast, GVFi treats 3D points as particles in space, each with a learnable size and orientation, enabling the model to learn particle rotation and translation to represent a dynamic system effectively. Experimental results on three diverse datasets show that GVFi significantly outperforms prior 3D Gaussian Splatting models on both interpolation and extrapolation tasks.

### Strengths
1. It is novel to represent the 3D points as particles, which is a well-established concept in robotics. This representation could open up further research topics to improve dynamics modeling.
2. This model does not rely on human annotations for motion estimation. It can autonomously group meaningful objects based on motion patterns without requiring any labeled data.
3. The authors provide both quantitative and qualitative results across multiple datasets, demonstrating GVFi’s improvements in both interpolation and extrapolation tasks.

### Weaknesses
1. This model builds upon DefGS (Yang et al., 2024), with its main contribution being the translation-rotation dynamics system module. However, the novelty of this addition may be somewhat limited, as it appears to be a relatively straightforward extension of existing techniques. The core idea of representing 3D points as particles with learnable translation and rotation is not entirely new, and it's unclear if the specific implementation provides significant advantages over other possible dynamics models.
2. The performance of DefGS (Yang et al., 2024) and GVFi is quite similar, and there appears to be no significant visual difference between the outputs of the two models. The authors should clarify specific scenarios where the translation-rotation dynamics system module leads to performance improvements, particularly in cases where the motion is more complex than simple translation or rotation. It is not clear if the model can handle non-rigid deformations or more complex motion patterns.
3. There are no quantitative results for object segmentation. It is crucial to evaluate the model's ability to segment objects based on their motion patterns, and compare it to models that rely on human annotations. Without this, it's difficult to assess the practical utility of the learned motion parameters for tasks beyond novel view synthesis.

### Questions
1. The performance and visual results of DefGS and GVFi appear very similar. Could the authors specify scenarios where the translation-rotation dynamics module offers clear advantages?
2. Could quantitative results for object segmentation be provided, and how does GVFi compare to models that rely on human annotations for this task?
3. Could the authors highlight the novelty compare to DefGS?

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
The authors extend multi-view dynamical scene modeling by predicting motion physics parameters without additional supervision. Specifically, they directly predict a translation rotation dynamics system for each 3D particle, which gives the model capabilities in future predictions of trajectories and rigid part discovery via clustering. Quantitative and qualitative results show superior performance against prior arts on three existing and one proposed benchmarks.

### Strengths
[+] The paper is well-organized.

[+] The proposed methodology of predicting translation rotation dynamics is straight-forward and well-presented.

[+] The emerged behavior of rigid parts through motion clustering is interesting and show be highlighted further.

[+] Extensive empirical evaluation on multiple benchmarks demonstrates superior performance, along with proper ablation study and demo video in supplementary.

### Weaknesses
[-] My main concern about this work is the assumption made (L219) that "there is no additional force involved after $t=0$." Although the author give a justification that "a rolling ball suddenly exploding is not learnable," I am not sure if the scope of the research is sufficiently broad given this constraint:
- First, while some moveable objects cannot move of their own volition, many dynamical (interesting) objects do have the ability to move on their own (e.g. humans, vehicles, animals, etc). By assuming no additional forces after $t=0$, the formulation appears to limit the model to scenarios where objects are only influenced by initial conditions, neglecting the continuous application of forces that drive the motion of self-propelled objects. This significantly restricts the applicability of the method to a subset of dynamical scenes, and it's unclear how the model would handle objects that change their motion due to internal forces. The examples provided, such as the whale, skater, and van, seem to contradict this assumption, unless the model is only capturing short time windows where no additional forces are applied, which should be clarified.
- Second, due to the strict assumption made about applied forces, the dynamical scene valid for this method would be rather simple and cannot contain more complex motion with evolving accelerations. The method, as described, appears to be limited to modeling constant or near-constant accelerations, which is a significant limitation when dealing with real-world scenarios where objects often exhibit complex, non-uniform motion patterns. For example, a bouncing ball or a car accelerating and decelerating would not be accurately modeled by this approach. The authors should elaborate on the types of motion that can / cannot be handled by GVFi, specifically detailing the limitations imposed by the constant acceleration assumption.
- Finally, since I do not work on this topic, I am not sure how significant is my concern above and I am happy to change my recommendation as I await to read other reviewer’s comments and the author's response to my review.

### Questions
Please refer to weaknesses above.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper introduces GVFi, a framework for modeling the motion physics of complex dynamic 3D scenes using multi-view RGB videos without requiring additional annotations such as object shapes, types, or masks.
Building on Deformable3DGS, GVFi incorporates constraints based on the laws of classical mechanics to guide motion predictions, ensuring that the Gaussian deformation estimated by the MLP aligns more closely with physical principles. By assuming that motion adheres to the laws of classical mechanics and explicitly learning the associated motion parameters, GVFi is capable of performing effective extrapolation rendering, allowing it to predict frames beyond the observed time span. Experimental results show that GVFi significantly outperforms existing methods, particularly excelling in future frame extrapolation tasks.

### Strengths
1. Modeling the motion of Gaussians through a Translation Rotation Dynamics System grounded in classical mechanics, resulting in a concise and conceptually elegant framework with solid mathematical and physical foundations.
2. Introducing an effective method to train the motion parameters of the Translation Rotation Dynamics System, enabling the accurate estimation of translation and rotation dynamics for each particle in the scene.
4. By explicitly learning motion parameters under classical mechanics, enabling effective extrapolation to unobserved frames and presenting potential for generation tasks that require plausible future frames in dynamic 3D scenes.
3. The proposed approach is validated on two tasks, demonstrating superior performance compared to previous methods, highlighting its effectiveness in modeling motion dynamics in 3D scenes.

### Weaknesses
1. The contributions of this work are somewhat incremental, as most of the methodological design heavily overlaps with the baseline method, Deformable3DGS [1]. The key difference lies in the incorporation of dynamical principles, primarily to enable extrapolation capabilities rather than introducing fundamentally novel approaches. The core idea of modeling Gaussian motion through a Translation Rotation Dynamics System, while conceptually elegant, is built upon existing Gaussian Splatting techniques, which limits the novelty of the approach. The method's reliance on a relatively simple motion model, where each Gaussian is treated as an independent rigid particle undergoing constant acceleration, does not fully capture the complexities of real-world dynamic scenes.

2. The proposed motion modeling framework is overly restrictive, relying on an strong assumption of no external forces, disregarding energy transfer processes, and lacking the ability to handle non-rigid or nonlinear motion. These limitations significantly reduce the model’s applicability to real-world physics. The assumption of constant acceleration for each Gaussian primitive, while simplifying the motion model, is a strong constraint that may not hold true in many real-world scenarios. This simplification limits the model's ability to capture complex interactions between objects and their environments, such as collisions, friction, or other external forces that cause non-constant accelerations or non-rigid deformations.

3. Due to its reliance on idealized assumptions and limited scope, the model struggles to handle complex, real-world motion dynamics where varied forces, interactions, and non-rigid behaviors are prevalent, limiting its utility for practical applications in diverse environments. The datasets used, with only 60 frames in total, limit the complexity and extent of motion, which makes it difficult to evaluate the model's ability to handle more complex and realistic scenarios. The lack of evaluation on more challenging datasets with more complex motion patterns and longer time spans raises concerns about the method's robustness and generalizability.

### Questions
1. Based on the methodology, there seem to be three possible approaches for interpolation rendering: (1) directly using $f_{defo}$ to predict the deformation at the given time $t$, (2) progressively calculating the Gaussian deformation at the given time $t$ from time 0 using the motion parameters predicted by $f_{trd}$, or (3) following the steps described in lines L261-L269. Which approach was used in the experiments? Are the results consistent across these three methods?
2. For extrapolation rendering according to lines L261-L269, it seems feasible to use either the second or third approach from question 1. Which method was actually used by the authors? If the third approach was used, how does it perform over longer extrapolation periods? Could the authors provide visual results for extrapolations that extend beyond the time span covered in the dataset?
3. The choice of baseline methods for comparison appears limited. For a comprehensive evaluation, it would be beneficial to compare against state-of-the-art methods in dynamic scene reconstruction, such as 4D-GS[2] and more recent work like E-D3DGS [3], which both have architectures similar to Deformable3DGS but differ in their motion representation. Could the authors verify if the proposed Translation Rotation Dynamics System can be integrated into these methods and whether it would yield similar performance gains?
4. The authors claim that their framework is a general approach for modeling motion physics in complex dynamic 3D scenes. However, the datasets used, with only 60 frames in total, limit the complexity and extent of motion. Could the authors validate this claim by testing on more challenging synthetic and real-world datasets, such as the ParticleNeRF and PanopticSports datasets, to provide a more comprehensive evaluation of the framework’s effectiveness on complex scenes?
5. In the ablation study, the authors provide a rationale for their choice of $\delta t$, which is somewhat reasonable. However, this conclusion is based on results from only one dataset, which may not be sufficient, as each dataset could exhibit different motion characteristics. Could the authors clarify how to select an appropriate $\delta t$ in practice across diverse datasets?
6. The experimental details are insufficient, particularly regarding training time, required resources, storage size, and rendering speed. Could the authors provide more comprehensive information on these aspects?
7. Please ensure that all abbreviations and technical terms are clearly defined, with full explanations and necessary citations. In the related work section, it would be helpful to explicitly clarify the differences from relevant works wherever possible.

[2] Guanjun Wu, Taoran Yi, Jiemin Fang, Lingxi Xie, Xiaopeng Zhang, Wei Wei, Wenyu Liu, Qi Tian, and Xinggang Wang. 4d gaussian splatting for real-time dynamic scene rendering. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), 2024.

[3] Jeongmin Bae, Seoha Kim, Youngsik Yun, Hahyun Lee, Gun Bang, and Youngjung Uh. Per- gaussian embedding-based deformation for deformable 3d gaussian splatting. In Proceedings of the European Conference on Computer Vision (ECCV), 2024.

### Soundness
2

### Presentation
2

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
Paper proposes a method "GVFi"  tackles the problem of estimating dynamic 3D scenes.

Broadly speaking, GVFi
 - Uses an off the shelf method (3DGS) to compute gaussian splats in a canonical frame
 - Uses an off the shelf method ("Deformable 3D Gaussians for High-Fidelity Monocular Dynamic Scene Reconstruction" Yang et al., CVPR 2024) to estimate a deformation field over position, rotation, and scale of each gaussian as a function of time
 - Uses these as inputs to then estimate the 3D gaussian's motion 

Importantly, these gaussians are parameterized as rotation around a moving rotation centerpoint, and this centerpoint's motion is described entirely by an initial position, velocity, and acceleration estimate. These estimates are then optimized against the flow field as noisy ground truth and training observation reconstruction losses.

### Strengths
- Method at its core is quite simple (this is a good thing)
   - Learning a second order taylor series expansion of the full trajectory
 - The quantitative results seem good, even if only minor improvements in a number of cases

### Weaknesses
 - Second order taylor series expansion seems quite limiting for arbitrary motion, or motion over non-trivial time horizons
 - Assuming I am interpreting the paper correctly, experiments seem to be only over short (~1 second) time horizons, which don't seem like they would challenge this assumption
 - Presentation quality is *extremely* poor
   - Core concept is quite simple, but it's heavily obfuscated for no apparent reason. It could be explained in 1 paragraph.
   - Core concepts seem poorly motivated; physics priors are common, but why only a second order expansion? Is this really a reasonable assumption in practice? There needs to be more motivation to this choice and more careful analysis of its limitations
   - Figure 1 and 2 are almost the same thing but not very informative. A better figure would be demonstrating the taylor series expansion of a single gaussian's trajectory
   - The math in section 3 does not feel like it was put there to be informative, but instead to intimidate the reader; after climbing through the notation its basically just saying to compose offsets together to estimate motion. If the authors feel this notational exercise is needed (don't think it is), it should go in the appendix and the main paper should have far more explanatory figures.
 - Ablations do not seem to address the core contribution, which is the assumption of the second order expansion --- what if you only do a first order expansion? Can you attempt to extend this to third order? They briefly mention replacing it with an MLP, but minimal details are provided.

I'm of the opinion that the paper has a neat idea but its presentation needs to be dramatically overhauled --- its assumptions need to be clearly stated and examined as reasonable or not, and it needs to have experiments where the method is pushed. Looking at the qualitative results, these datasets are very simple partwise rigid motion and the taylor series expansion is a nice trick to force smooth non-shattering motion, but it comes at the cost of generality --- nowhere does this seem to be addressed, considering the sometimes marginal performance improvements over far more flexible prior methods.

Nit:
"Cononical" -> Canonical misspelling is rampant

### Questions
- How long are each of the datasets scenes? Are they really long enough to meaningfully challenge the assumption of second order expansion?
- The NVIDIA Dynamic Scene Dataset (Yoon 2020) contains many dynamic scenes in the 2020 paper, but this paper claims "it consists of two real-world dynamic 3D scenes", what are those scenes?

### Soundness
3

### Presentation
2

### Contribution
3
