# OmniPhysGS: 3D Constitutive Gaussians for General Physics-Based Dynamics Generation

- Decision: Accept
- Scores: 6, 6, 6, 6, 8

## Abstract
Recently, significant advancements have been made in the reconstruction and generation of 3D assets, including static cases and those with physical interactions. To recover the physical properties of 3D assets, existing methods typically assume that all materials belong to a specific predefined category ($\textit{e.g.}$, elasticity). However, such assumptions ignore the complex composition of multiple heterogeneous objects in real scenarios and tend to render less physically plausible animation given a wider range of objects. We propose $OmniPhysGS$ for synthesizing a physics-based 3D dynamic scene composed of more general objects. A key design of $OmniPhysGS$ is treating each 3D asset as a collection of constitutive 3D Gaussians. For each Gaussian, 
its physical material is represented by an ensemble of 12 physical domain-expert sub-models (rubber, metal, honey, water, etc.), which greatly enhances the flexibility of the proposed model. In the implementation, we define a scene by user-specified prompts and supervise the estimation of material weighting factors via a pretrained video diffusion model. Comprehensive experiments demonstrate that $OmniPhysGS$ achieves more general and realistic physical dynamics across a broader spectrum of materials, including elastic, viscoelastic, plastic, and fluid substances, as well as interactions between different materials. Our method surpasses existing methods by approximately 3% to 16% in metrics of visual quality and text alignment.  The code and data will be made publicly available.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The paper presents a framework for text-driven physical parameter learning for 3DGS-reconstructed objects. Compared to previous methods, the main novelty lies in making discrete constitutive model types learnable based on given text prompts. For each particle, the physics-aware decoder predicts a material type from 12 predefined material classes. The simulated and rendered results are fed into a pretrained text-to-video diffusion model to evaluate SDS for guiding both material class and material parameter learning. Efficiency enhancements are also proposed, including optimizing the long sequence in chunks.

### Strengths
- The overall presentation of the framework is clear.
- Comparisons and ablations are extensive.

### Weaknesses
 - The controls of the scene—such as initial velocity and external forces—are not learnable parameters. For this reason, the paper is best summarized as a framework for learning physical parameters, where interactions between objects remain fixed and are not directly controllable. Consequently, text descriptions must be crafted based on these known, predefined interactions.
- In reality, objects cannot be both elastic and sandy. The physical plausibility is questionable. With such heuristic blending of materials within a single object, the dynamics may conform to unrealistic motions encoded in the video model that is impossible in reality.

### Questions
- How is the physical-aware decoder trained? The material classes are discrete and the sampling of $j_i, k_i$ in Eq.6 is non-differentiable. How does the model learn to change material class? This is the key novelty of the paper, a detailed discussion is needed.

- The following references are highly related, which also design learnable constitutive models:
    - Nagasawa, Kentaro, et al. "Mixing sauces: a viscosity blending model for shear thinning fluids." ACM Trans. Graph. 38.4 (2019): 95-1.
    - Su, Haozhe, et al. "A generalized constitutive model for versatile mpm simulation and inverse learning with differentiable physics." Proceedings of the ACM on Computer Graphics and Interactive Techniques 6.3 (2023): 1-20.
   

- Warp can create arrays from Torch tensor without copying. I am wondering why it consumes much more memory than implementing MPM in Pytorch.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes a physics-based dynamics generation method that includes different physical material properties. The authors model the object as constitutive 3D Gaussians that exhibit multiple physical material properties by an ensemble of physical domain-expert sub-models. The dynamics can be described and input as a user prompt, the learnable constitutive models would be optimized by a pre-trained video diffusion model with SDS loss. The authors designed a 3D feature extractor and physical-aware decoder to model ordinary Gaussians to constitutive Gaussians. Due to the limited generation length of existing video diffusion models, the authors designed two training strategies, grouping and multiple mini-batch training to allow the training on MPM simulation steps.

### Strengths
1. This approach uses 3D Gaussians as constitutive models, enabling the representation of diverse physical material properties. It facilitates the optimization of these properties via a learnable MPM simulation, which integrates video SDS loss.

2. Domain-expert constitutive models are incorporated to steer the learning process across various materials, functioning similarly to a Mixture of Experts methodology.

3.  Two training strategies are introduced, grouping and multi-mini-batch training, to address the challenges posed by numerous MPM simulation steps and the limited number of frames produced by video diffusion models,

### Weaknesses
1. The authors limit their comparisons to the same object modeled with vastly different materials. This approach is less persuasive because altering materials in PhysGaussian [1] is straightforward, whereas optimizing appropriate physical parameters is challenging. More convincing evidence would come from showing varied parameter results within the same material. I will elaborate on this point in the questions section.

2. The collision experiments appear to lack physical contact, consistently showing a gap between the colliding objects, whereas collisions modeled in PhysGaussian [1] are depicted as more substantial. The overall visual quality of the experiments still falls short of what is achieved with PhysGaussian.

### Questions
The experiments primarily compare the same object using two distinctly different materials, such as rubber versus sand or jelly versus fluids. However, in practical applications, it is unusual to utilize the same object with radically different materials. Moreover, modifying the material type in PhysGaussian [1] is relatively straightforward, requiring changes to only three fields in the configuration file: the material itself, Young’s modulus, and Poisson’s ratio. This simplicity contrasts sharply with the complexity of optimizing a model using video diffusion models for similar tasks. From my perspective, it is beneficial to explore the optimization of physical parameters for a single type of material. For instance, metals like gold exhibit high plasticity, whereas aluminum alloys display low plasticity. Similarly, wood varieties may vary significantly in flexibility. As demonstrated in Figure 6 of PhysGaussian [1], jelly can show varying degrees of stiffness and volume preservation by adjusting Young's modulus and Poisson's ratios. These parameters are challenging to adjust manually and merit further exploration for optimization via video diffusion models.

As stated in line 234 by the authors, “Unlike previous works (Zhang et al., 2024b; Liu et al., 2024; Huang et al., 2024) that maintained fixed constitutive models, Constitutive Gaussians allow the model to capture diverse material behaviors, encompassing both elastic and plastic deformations, thus offering a more dynamic and comprehensive representation of material properties.” Additionally, Equation 4 highlights that the hyperelastic energy density function, the plasticity return function, and the physical parameters are all learnable parameters within the constitutive models. Therefore, as the authors assert, this approach should facilitate the optimization of material properties within the same material category.

I am eager to see experimental results that demonstrate this capability of the model. For instance, comparing a "hard rubber bear" with a "stretchy rubber bear," or a "hard metal can" with a "soft metal can" would illustrate the model’s effectiveness. Presenting such results would prompt me to raise my score.

[1] Xie, T., Zong, Z., Qiu, Y., Li, X., Feng, Y., Yang, Y., & Jiang, C. (2024). Physgaussian: Physics-integrated 3d Gaussians for generative dynamics. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (pp. 4389-4398).

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper focuses on generating dynamic 3D objects with physics-based simulation. The paper aims to relax the assumption of fixed constitutive models from previous works such as PhysGaussian and PhysDreamer. In particular, this paper introduces the OmniPhysGS framework with the learnable Constitutive Gaussians at the core. The main technical idea is to decompose an object into many small particle groups and use SDS optimization to assign a particular material to each group. The material assignment is a classification process that selects one of twelve predefined constitutive models with learnable physical parameters. Experiments are performed on a set of simple synthetic objects, showing that the proposed approach can generate different types of material dynamics.

### Strengths
- The problem is relevant and important. Current methods (e.g., PhysDreamer, Physics3D) are very much limited to elastic objects due to fixed constutive model. The proposed approach adds the flexibility of choosing from different materials.
- The experiment results of generating different types of material dynamics for a single input are interesting.
- Implementing a memory-efficient MPM solver is useful.

### Weaknesses
 - There is no real experiments such as the ones in PhysDreamer and Physics3D.
- Some experiment results look weird, such as in 0:49 of the video, the can hit by the toy duck. It looks like the can has a very weird material (it does not look like metal at all), such that it keeps shrinking after being lightly hit by a toy.
- The metrics (e.g. CLIP similarity score) applying to videos do not seem to be very convincing to me. I'm not sure if CLIP score can be used to measure motion quality. I think the motion realism would be better judged by human preference.
- I'm a bit concerned about the technical design of dividing an object into small particle groups and allowing them to have different predefined constitutive models. That may not align with real-world physics. For example, it may give arbitrary material prediction in the interior of an object. I think the can example is one illustration of generating unreasonable results. Would this give reasonable results all the time?
- It is not clear to me why a neural network is needed at all. It seems there is no training, but per-scene test-time optimization. So there is no generalization issue. Then one may simply optimize a 12-way one-hot softmax vector for the material classification. What's the advantage of having to train a scene-specific neural network?
- Some notations are confusing, e.g., in L207, the physical parameters are denoted as a single real scalar value, yet the supplementary material says it includes Young’s modulus and Poisson’s ratio.

### Questions
Please see weaknesses above. I'm open to change my mind if there are evidences to rebut my points, though.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
In this work, the authors propose omniphysgs, a novel method for creating physics-based 3D dynamic scenes with diverse objects by modeling each asset as collections of 3D Gaussians and using multiple material sub-models. This method allows for complex material compositions, enhancing realism and flexibility in physical interactions. Experimental results show omniphysgs outperforms existing methods in visual quality and text alignment.

### Strengths
1. Performance: The proposed method omniphysgs achieves state-of-the-art results. The experiments well validate the effectiveness of the proposed methods.

2. Clarity: The paper is well-written and clearly structured, making the methodology and results easy to understand and follow.

3. Technical Novelty: The main contributions of this paper are twofold: 1) They propose a novel framework, which models each 3D asset as a collection of 3D Gaussians and represents physical materials using an ensemble of 12 domain-specific sub-models. This design significantly enhances the flexibility and realism of the synthesized dynamic scenes. 2) They define a scene by user-specified prompts and use a pretrained video diffusion model to supervise the estimation of material weighting factors, enabling the synthesis of more general and physically plausible interactions across a diverse range of materials.

### Weaknesses
Figure 1 is unclear regarding the material properties of the objects. It is confusing when the mountain is depicted as non-elastic while the duck toy is elastic, but the mountain collapses after the duck toy falls, which seems inconsistent with the assigned material properties.

### Questions
I am curious about how this method handles interactions between a single object and an entire scene, as opposed to interactions between two objects. Additionally, it would be better to understand the method's performance and behavior in scenarios involving more than two objects.

### Soundness
3

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
The OmniPhysGS framework can simulate general physics-based 3D dynamics. It works with many types of materials like elastic, plastic, and fluid. Authors use Constitutive Gaussians and video diffusion models to make more realistic animations. It uses MPM for accurate physics simulation. The paper shows better results than PhysDreamer, Physics3D, and DreamPhysics.

### Strengths
This is the first method to use learnable constitutive models in Gaussian Splatting. It makes material simulation more flexible.

It supports many different materials. Other methods usually focus on one type.

The method uses text prompts and video diffusion models. It is very user-friendly and simple to use.

### Weaknesses
The quality depends on pre-trained diffusion models. This could make it difficult to simulate new materials or very specific materials. The method's reliance on diffusion models, which are trained on existing datasets, inherently limits its ability to generalize to materials or scenarios not well-represented in those datasets. This is a significant limitation when attempting to simulate novel or highly specialized materials with unique constitutive properties.

The method might lack robustness when dealing with more complex or unusual physical scenarios, especially when the guidance models do not adequately capture the specific material properties. The reliance on diffusion models for guidance introduces a potential bottleneck in the simulation pipeline. If the diffusion model's understanding of a particular physical scenario is limited, the simulation may produce inaccurate or unstable results. This is especially concerning for complex interactions involving multiple objects or extreme deformations, where the diffusion model's guidance might be insufficient or even misleading.

It is not clear what they assume about materials in each Gaussian particle. Would the proposed method be able to do material mixture as in this paper?

### Questions
A discussion comparing the method to 'A generalized constitutive model for versatile MPM simulation and inverse learning with differentiable physics.' [2023] would be good. This would provide more context on how OmniPhysGS performs in comparison to recent advancements in MPM simulation and the capabilities of inverse learning. Authors should say more about the limits of the constitutive models. It is not clear what they assume about materials in each Gaussian particle. Would the proposed method be able to do material mixture as in this paper?

In experiments, it would be good to say how OmniPhysGS parameters are chosen. This is not clear for multi-object scenes where material differences are important.

More explanation needed about permanent deformation. How does OmniPhysGS handle it for viscoelastic or plastic materials? Would there be failure during training? For example, a bad parameter causes a 3D model to break down to pieces. The optmization may get stuck, right?

In Figure 3, could add some notes. Use a scene with multiple model categories, and show how the classification decoder assigns constitutive models to different areas of the scene. 

The wolf on water scene, how is the shape of the water container specified in the pipeline?

### Soundness
3

### Presentation
3

### Contribution
3
