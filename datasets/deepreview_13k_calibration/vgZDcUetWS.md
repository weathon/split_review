# Neural Approximate Mirror Maps for Constrained Diffusion Models

- Decision: Accept
- Avg Score: 6.67
- Scores: 6, 6, 8

## Abstract
Diffusion models excel at creating visually-convincing images, but they often struggle to meet subtle constraints inherent in the training data. Such constraints could be physics-based (e.g., satisfying a PDE), geometric (e.g., respecting symmetry), or semantic (e.g., including a particular number of objects). When the training data all satisfy a certain constraint, enforcing this constraint on a diffusion model not only improves its distribution-matching accuracy but also makes it more reliable for generating valid synthetic data and solving constrained inverse problems. However, existing methods for constrained diffusion models are inflexible with different types of constraints. Recent work proposed to learn mirror diffusion models (MDMs) in an unconstrained space defined by a mirror map and to impose the constraint with an inverse mirror map, but analytical mirror maps are challenging to derive for complex constraints. We propose \textit{neural approximate mirror maps} (NAMMs) for general constraints. Our approach only requires a differentiable distance function from the constraint set. We learn an approximate mirror map that pushes data into an unconstrained space and a corresponding approximate inverse that maps data back to the constraint set. A generative model, such as an MDM, can then be trained in the learned mirror space and its samples restored to the constraint set by the inverse map. We validate our approach on a variety of constraints, showing that compared to an unconstrained diffusion model, a NAMM-based MDM substantially improves constraint satisfaction. We also demonstrate how existing diffusion-based inverse-problem solvers can be easily applied in the learned mirror space to solve constrained inverse problems.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper proposes neural approximate mirror maps for constraint data generation with diffusion models. Compared to typical mirror diffusion models, the mirror map is parameterized by the gradient of ICNN and learned via penalizing the differentiable constraint distance, thereby being applicable to general non-convex constraints. The forward and inverse mirror maps are learned by a combination of cycle consistency loss, constraint loss and regularization loss. Experiments in several settings ranging from physics-based to semantic demonstrate the effectiveness on constraint satisfaction, training efficiency and constrained inverse problem solving.

### Strengths
- The method is applicable to more general constraints than previous works.
- The cycle-consistency loss tailored for mirror maps and diffusion models is sound.
- The experiments are conducted on diverse settings, including constrained DPS.
- The ablation studies are comprehensive.

### Weaknesses
 - The experiments are primarily toy. It is not clear whether the proposed method can scale to high dimensions and apply to domains such as images.

 - The regularization loss is introduced to ensure a unique solution according to the paper. What is the meaning of unique? As the mirror map is parameterized as the gradient of ICNN, the reversibility is already ensured.
- Is the method scalable? For example, can it be applied to the image settings in Reflected Diffusion Models?

### Questions
- The regularization loss is introduced to ensure a unique solution according to the paper. What is the meaning of unique? As the mirror map is parameterized as the gradient of ICNN, the reversibility is already ensured.
- Is the method scalable? For example, can it be applied to the image settings in Reflected Diffusion Models?

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
This paper presents neural approximate mirror maps (NAMMs) to enforce soft constraints for diffusion models (DMs). NAMMs employ two neural networks to learn a mirror map that maps constrained points into the mirror space, and its inverse that transforms data back to the constraint set. A mirror diffusion model (MDM) can be trained in the learned mirror space, and its generated samples can be mapped to the constraint set via the inverse map. This method is tested on five benchmark problems, ranging from physics-based, geometric to semantic constraints, and the results show the proposed method improve constraint satisfaction compared to a vanilla unconstrained DM. And, this paper also demonstrates NAMMs leads to less constraint violation when solving constrained inverse problems.

### Strengths
1. NAMMs generalize the concept of true mirror maps to learn approximate mirror maps to handle non-convex constraints.
2. NAMMs can handle physics-based, geometric and semantic constraints, while existing methods are restricted in the types of constraints they can handle.
3. NAMMs not only help diffusion models, but also help VAEs to improve constraint satisfaction, showing the potential to be compatible for other generative models. And NAMMs are also helpful to diffusion-based inverse-problem solvers for solving constrained inverse problems.

### Weaknesses
1. Theoretically, NAMMs lack the guarantee of the existence and uniqueness of the mirror maps when applied to non-convex problems. This is a significant limitation, as the method's success relies on the assumption that a suitable mirror map can be learned, which may not always be the case for complex, non-convex constraints. The lack of theoretical grounding makes it difficult to predict when the method will succeed or fail.

2. The proposed method is validated on five benchmark problems in the main experiments to show the superiority of applying NAMMs to diffusion models in generating constrained data. However, in the experiments to solve inverse problems, ablation experiments, and the experiments applied to VAE, this method is only carried out on partial problems and does not fully demonstrate its performance on the three types of constraints mentioned. This inconsistent evaluation across different experimental settings makes it difficult to assess the method's generalizability and robustness.

3. Finetuning is an important part of the proposed method introduced in section 3. But, it is mentioned in subsection 4.1 that “We show results from a finetuned NAMM, but as shown in Section 4.3, finetuning is often not necessary”. Moreover, in the ablation studies of constraint loss and mirror map parameterization, and experiments about the VAE, fine tuning is not used. This inconsistency in the application of fine-tuning raises questions about its actual contribution and necessity, and the lack of a clear guideline for when to use it.

4. The basic unconstrained model is used for comparison, but the comparison with another existing methods dealing with constraints is lacking. This makes it difficult to assess the relative performance of the proposed method compared to state-of-the-art constraint-handling techniques.

### Questions
1.	In this paper, the robustness of the model is enhanced by introducing noise into the mirror space. What does robustness mean here, and are there any experimental results that support the robustness of the method?
2.	In order to fully demonstrate the performance of the method, it is necessary to supplement its experiments on five benchmark problems and an additional baseline model.
3.	If fine-tuning is considered to be one of the important components of the method and one of the contributions of this paper, more experimental support is needed.
4.	On line 1097, there is a clerical error, “a la”.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper proposes a technique to learn a mirror map for general constrained diffusion generation. The resulting neural approximate mirror map transforms the constrained problem domain to an unconstrained space, where the diffusion model is trained. The training loss encourages that the inverse of the mirror map lies within the constraint set. Numerical experiments on various problems demonstrate the efficacy of the proposed technique in enforcing the constraints.

### Strengths
- The method is well motivated. Proper constraint satisfaction is challenging in diffusion generation, limiting many important applications in engineering, physics and computer vision. 

- The proposed approach is sensible, and to the best of my knowledge novel. It improves the flexibility of mirror diffusion models by obviating the need for analytical mirror maps.

- The experimental results are promising on a wide array of problems. 

- The paper overall is well-written and easy to follow.

### Weaknesses
 - It is unclear how complex of a constraint the proposed method can handle, as the gap between NAMM and the baseline is less significant for the semantic problem. It would be beneficial to see results on more complex constraints, such as those involving non-convex or discontinuous regions, to fully assess the method's capabilities. The current experiments, while diverse, do not fully explore the limits of the approach in terms of constraint complexity.
- It is unclear if there is a systematic way to tune the introduced hyperparameters, and how sensitive the performance is in higher dimensions to $\sigma_{max}$. The paper lacks a detailed analysis of how the choice of $\sigma_{max}$ and $\lambda_{constr}$ affects the trade-off between constraint satisfaction and sample quality, especially in higher-dimensional spaces. The current discussion on hyperparameter tuning is limited, and a more thorough investigation is needed to provide practical guidance for users.


### Questions
- It appears in Fig. 6 that constraint distance is fairly sensitive to $\sigma_{max}$ and $\lambda_{constr}$. Can authors propose systematic ways to tune the hyperparameters? How does the sensitivity depend on the dimensionality of the problem or the complexity of the constraint?
- Minor comment: the citations in Section 2.1 take up a large portion of the paragraph somewhat reducing readability (top of page 3).
- Minor comment 2: Fig. 2 is never directly referenced in the text.

### Soundness
3

### Presentation
3

### Contribution
3
