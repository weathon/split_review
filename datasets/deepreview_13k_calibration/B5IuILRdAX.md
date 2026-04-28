# One-step Flow Matching Generators

- Decision: Reject
- Avg Score: 5.00
- Scores: 6, 3, 6, 5

## Abstract
In the realm of Artificial Intelligence Generated Content (AIGC), flow-matching models have emerged as a powerhouse, achieving success due to their robust theoretical underpinnings and solid ability for large-scale generative modeling. These models have demonstrated state-of-the-art performance, but their brilliance comes at a cost. The process of sampling from these models is notoriously demanding on computational resources, as it necessitates the use of multi-step numerical ordinary differential equations (ODEs). Against this backdrop, this paper presents a novel solution with theoretical guarantees in the form of Flow Generator Matching (FGM), an innovative approach designed to accelerate the sampling of flow-matching models into a one-step generation, while maintaining the original performance. On the CIFAR10 unconditional generation benchmark, our one-step FGM model achieves a new record Fréchet Inception Distance (FID) score of 3.08 among all flow-matching-based models, outperforming flow matching models that use 50 generation steps. 
Furthermore, we use the FGM to distill the Stable Diffusion 3, which is a leading text-to-image flow-matching model. The resulting model named the MM-DiT-FGM demonstrates outstanding industry-level performance as a novel transformer-based one-step text-to-image generator.  When evaluated on GenEval benchmark, MM-DiT-FGM has delivered remarkable generating qualities, rivaling other multi-step models in light of the efficiency of a single generation step. We will release our one-step FGM text-to-image model with this paper.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces the **Flow Generator Matching (FGM) objective** for distilling a one-step generator from pretrained flow-matching models. It provides theoretical guarantees that the proposed objective yields the same gradient, with respect to the parameters of the one-step generator, as the standard flow-matching loss. The paper demonstrates competitive and, in some cases, superior results in both unconditional generation on CIFAR-10 and large-scale text-to-image generation, achieved by distilling Stable Diffusion 3 (SD3).

### Strengths
1. The paper is well-written and easy to follow.
2. The proposed algorithm is elegantly designed, alternating the optimization of the parameters of the one-step generator, $\theta$, and an auxiliary flow model, $\psi$. The correctness and effectiveness of the algorithm are supported by Theorems 4.1 and 4.2.
3. The paper conducts thorough empirical evaluations of the proposed method across various tasks, including unconditional generation on CIFAR-10 and large-scale text-to-image generation, demonstrating superior results.

### Weaknesses
1. The proposed method requires training an auxiliary flow model with parameters $\psi$, designed to generate the implicit flow determined by the one-step generator. The paper does not clearly state whether this auxiliary model is discarded after training or if it plays a role in the final generation process. The necessity of training this additional model raises concerns about the overall complexity and resource consumption of the method.
2. The paper lacks a thorough discussion of training efficiency and speed, particularly in comparison to existing distillation techniques. While the paper mentions the number of optimization steps, it does not provide a clear analysis of the computational cost per step or the total training time. A comparison with methods like Consistency Flow Matching (Yang, Ling, et al., "Consistency Flow Matching: Defining Straight Flows with Velocity Consistency") is crucial to understand the practical advantages and disadvantages of the proposed approach. The absence of such a comparison makes it difficult to assess the real-world applicability of the method, especially in resource-constrained environments.

### Questions
Please see weaknesses part.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes extending score implicit matching from diffusion to flow matching, which is called FGM. The method seems to work well on text-to-image and unconditional generation.

### Strengths
1. The paper is well-written and easy to follow.
2. The paper extends the score implicit matching to a flow matching generator.

### Weaknesses
1. The novelty of the paper is limited. Since flow matching can be considered a special form of diffusion model, score-based diffusion and flow matching are equivalent. Therefore, rawly extending the implicit score matching for the flow matching model should work well.
2. The evaluation for the text-to-image section should include FID, Recall, ClipScore, Image Reward, PickScore, and AES score. These metrics are often used as standard metrics to evaluate generative models.
3. Since this method is closely related to implicit score matching, the author should include a background section for implicit score matching.

### Questions
My biggest concern is the novelty and originality of this paper's idea. There is a list of works working on score implicit models, such as [1,2,3]. Extending the framework from diffusion to flow matching is not interesting and does not introduce something new. 

[1]: Diff-Instruct: A Universal Approach for Transferring Knowledge From Pre-trained Diffusion Models

[2]: One-Step Diffusion Distillation through Score Implicit Matching

[3]: Score identity Distillation: Exponentially Fast Distillation of Pretrained Diffusion Models for One-Step Generation

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces Flow Generator Matching, an innovative distillation framework for pre-trained flow-matching models. The framework is designed to accelerate sampling by constructing a one-step generator. To achieve this, the authors define a noise-to-image mapping $g_\theta(z)$, and optimize the distance between the vector field of the pre-trained flow model, and the vector field implicitly derived from the one-step generated images and the online flow model. By leveraging a theoretical approximation of this optimization using the flow product identity, the authors develop a fast and efficient one-step flow generator.

### Strengths
- Theoretical justification: The proposed distillation formulation is both intuitive and novel in the context of flow matching. Although optimizing $L_{FM}$ directly with respect to $\theta$ is non-trivial, the authors introduce an innovative alternative whose gradient remains aligned with the original objective.

- Specialized distillation methods for flow matching: Given the widespread use of flow matching in various state-of-the-art large-scale generative models (e.g., Movie Gen), effective sampling acceleration is critical. This paper offers a promising approach to address this important contemporary challenge.

- Experiments: Comprehensive empirical evaluations, including unconditional, conditional, and text-to-image experiments, support the effectiveness of the method. The approach demonstrates competitive performance with other flow distillation techniques, achieving lower NFE.

### Weaknesses
 - Writing & Notations: The connection between the derivations and practical implementations is difficult to follow. For instance, while FGM relies on the online flow model parameterized by $\psi$, as outlined in Algorithm 1, $\psi$ is notably absent in Section 4, despite being a crucial component. Additionally, there is no explanation or justification for the phrase "stop the $\theta$-gradient" mentioned in Line 250, which is a critical implementation detail. From my understanding, FGM is conceptually similar to distribution matching distillation, where both the generator $\theta$ and an online critic $\psi$ are updated alternately. However, this understanding comes from Algorithm 1 rather than the main text. The authors should provide a clear and theoretically grounded explanation of "stop gradient" and revise the derivations to explicitly incorporate the online flow model $\psi$. Moreover, some important information are provided in appendix without pointers, e.g.   model parameterization in L952. Detailed pointers in the main paper would be appreciated.

- Novelty: As previously mentioned, FGM shares significant technical similarities with existing diffusion distillation methods. This overlap may diminish the novelty of the approach and, consequently, inherit some of the limitations of these existing methods, such as reliance on a potentially sub-optimal online flow model. Furthermore, the authors' claim that flow matching does not imply explicit modeling of probability density, unlike diffusion models, is not entirely accurate. Flow-based generative models can indeed recover the ODE structure in the form of denoisers and generalize probability path definitions [1,2]. This distinction is crucial for establishing the novelty of the approach, and requires further clarification.

- Qualitative Results: Although FGM demonstrates better quantitative performance compared to other flow distillation methods, the generated images appear overly "synthetic" and color-saturated (e.g., the rightmost images in Lines 54 and 488), while i admit that this may vary based on human perception. This could be potentially attributed to the image-data-free property proposed as limitations by the authors.

### Questions
Overall, the paper is well-structured and presents promising results. However, the derivations and notations could be refined to enhance clarity and facilitate faster understanding. Below are some questions for consideration:

- Ablation Study on Generator Initialization: The generator is initialized with pre-trained flow models, which may be crucial for warm-up and accelerating convergence, especially given that FGM does not utilize real-image datasets. This initialization might also mitigate the OOD gap for pre-trained flow models trained on real images. Conducting an ablation study or providing further analysis could improve understanding and highlight the significance of this choice.

- Bypassing Equation 4.11: Although Equations 4.11 and 4.12 both originate from the FGM loss, the authors opt not to use Equation 4.11, as mentioned in Line 368. This decision represents a significant bypass. Additional analysis, discussion, and empirical evidence are needed to justify this choice. Could the authors elaborate on why Equation 4.11 is deemed unnecessary in practice?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper introduces Flow Generator Matching (FGM), a method for to distill a pretrained flow-matching model into a single-step model. Specifically, the paper proposes a data-free distillation approach to match the implicit vector field of the student model $v_{\theta, t}$ with the pretrained vector field u_t, where u_t can be regarded as the teacher. Experiments are carried out on CIFAR-10 and paired text-image dataset, which demonstrate the effectiveness.

### Strengths
1. The paper proposes a novel method to distill a flow-matching model based on the property of its vector field from a probabilistic standpoint, which represents a good contribution.
2. Experiments show effectiveness of the appraoch.

### Weaknesses
1. My biggest concern is the clarity of the paper.
    - Algorithm 1 is not clear to me and hard to understand. What is the online flow model $v_\psi$? It gets introduced nowhere in the entire Section 4 except the Input field of Algorithm 1. Does it represent the implicit vector field? If yes, why shall we have another notation of $v_{sg[\theta], t}$ in 4.11 and 4.12? If not, then what does the online model do and how could we use $\theta$ to parameterize both the generator and the implicit vector field? Also in 4.12, there're both $u_t(x_t)$ and $u_t(x_t | x_0)$, yet $x_t$ is only sampled from $x_t | x_0$ ~ $q_t(x_t | x_0)$, then why do we have different notations here? This is the core of the paper which concretizes the theory into algorithm, and it shall be presented as clear as possible. Specifically, the role of $v_\psi$ as an approximation of the generator's vector field is not well-motivated, and the distinction between $u_t(x_t)$ and $u_t(x_t | x_0)$ needs further clarification in the context of the loss function.
    - in line 203, there's an abuse of notation where using $x_0 = g_\theta(z)$ instead of $x$ could make the notation more consistent with the latter integral.
2. The one-step results seem to have checkerboard artifact. When zoomed in Fig.1, most samples show the pattern. It also appear in the 2nd sample of Figure 3 while SD3-28 steps have much smoother texture. The quality degradation is still a concern. The presence of these artifacts suggests potential issues with the training process or the model's ability to capture the underlying data distribution in a single step.
3. There's missed reference in Table 2 for StyleGAN2 + Smart.
4.  How do we find the t* in 5.1? The ablation study is not presented. The lack of a clear methodology for selecting $t^*$ and the absence of an ablation study make it difficult to assess the robustness of the proposed approach.

### Questions
Please refer to weakness.

### Soundness
2

### Presentation
1

### Contribution
3
