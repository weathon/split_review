# Robust Representation Consistency Model via Contrastive Denoising

- Decision: Accept
- Avg Score: 6.25
- Scores: 3, 6, 8, 8

## Abstract
Robustness is essential for deep neural networks, especially in security-sensitive applications. To this end, randomized smoothing provides theoretical guarantees for certifying robustness against adversarial perturbations. Recently, diffusion models have been successfully employed for randomized smoothing to purify noise-perturbed samples before making predictions with a standard classifier. While these methods excel at small perturbation radii, they struggle with larger perturbations and incur a significant computational overhead during inference compared to classical methods. To address this, we reformulate the generative modeling task along the diffusion trajectories in pixel space as a discriminative task in the latent space. Specifically, we use instance discrimination to achieve consistent representations along the trajectories by aligning temporally adjacent points. After fine-tuning based on the learned representations, our model enables implicit denoising-then-classification via a single prediction, substantially reducing inference costs. We conduct extensive experiments on various datasets and achieve state-of-the-art performance with minimal computation budget during inference. For example, our method outperforms the certified accuracy of diffusion-based methods on ImageNet across all perturbation radii by 5.3\% on average, with up to 11.6\% at larger radii, while reducing inference costs by 85x on average.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper presents the Robust Representation Consistency Model (rRCM), an approach to improve robustness in deep neural networks by leveraging contrastive denoising within diffusion models. Instead of standard generative denoising, the authors reframe denoising as a discriminative task in latent space, enabling implicit one-step classification with reduced computational overhead. The authors perform experiments on datasets like ImageNet and CIFAR10 and investigate the method’s certified accuracy and scalability across perturbation radii, claiming a notable reduction in inference costs.

### Strengths
- The paper introduces a structured noise schedule for diffusion-based Randomized Smoothing, reformulating de-noising from a generative to a discriminative task. This is an interesting idea, especially in adversarial robustness, where noise schedules and latent consistency are less commonly used.
- The authors perform a thorough evaluation of their approach, comparing it against multiple state-of-the-art methodologies, in terms of certified accuracy and inference time.

### Weaknesses
 - Motivation: the main idea of Carlini et al. (2022) is to utilize an existing diffusion model for de-noising, thus getting randomized smoothing "for free", without needing to fine-tune the base classifier. This work reformulates the diffusion process to be more aligned in the latent space, but in the end, we get a classifier that's trained from scratch, with a diffusion-like objective. Why do all that and not just train a classifier on noisy images (since we're going to train in any case)? What is the benefit? The motivation of the approach is not very clear to me. In particular, I cannot follow the diffusion formulation and motivation precisely. 
- Presentation: related to the above, the methodology section of the paper is not easy to follow, e.g. there are various details where I don't fully understand how it all comes together (normalization, consistency loss, etc.). It would help if the authors (1) state the high-level motivation of their approach, (2) add clean pseudo-codes showing how the overall process works. Also, figure 2 would benefit from further elaborations.   
- Complexity: the approach is technically complex (structured noise schedule, alignment with PF ODE trajectories) which could hinder it's extension in other setups. 
- Some things, like e.g. the 46x speed improvement are over-claimed, for instance this holds only for a particular case. On average, the approach is faster than e.g. the Gaussian baseline or Carlini et al. (2022), but not by that much. Also, the reported 41% accuracy of the Gaussian baseline at radius 0 seems surprisingly low, raising questions about the fairness of the comparison.

### Questions
My questions are mainly related towards addressing the weaknesses mentioned before:
- Can the authors clearly motivate the methodology, why this particular approach and not something else? Why e.g. not just train a ViT on a lot of noisy samples?
- Can the presentation be improved so that readers can easily see the overall motivation, and follow along with the details?
- Despite the complexity overhead, does the approach generalize on other e.g. models or datasets, and how easily?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes a new method to improve the robustness of deep neural networks against adversarial perturbations. By reformulating the generative task in consistency models as a discriminative task in latent space, the authors use instance discrimination to ensure consistency of noisy samples along PF-ODE trajectories. This approach enables one-step denoising and classification, reducing computational overhead while achieving a balance between robustness and efficiency across different perturbation radii. Experiments show that the method performs well on large-scale datasets like ImageNet and significantly reduces computational costs compared to traditional methods.

### Strengths
+ The overall structure and writing approach of the paper are well-organized and clear.
+ Combining consistency model with robust representation learning is interesting and novel to me. The use of PF-ODE to build a consistent relationship between clean data and perturbed data has a theoretical basis.
+ The proposed method is significantly more time-efficient than previous diffusion-based methods, both theoretically and practically..

### Weaknesses
 - Some details of the method are unclear; it would be helpful to provide the complete loss function formula used in the approach, along with a detailed explanation. Specifically, the interplay between the consistency loss and the contrastive loss needs further clarification. It's not immediately obvious how these two losses are balanced, or if they are weighted differently during training. The paper should also specify how the instance discrimination is implemented in the latent space, including the choice of similarity metric and the sampling strategy for negative examples.
- The improvements in Certified Accuracy shown in Table 1 are marginal, suggesting limited gains in robustness compared to prior methods. The reported improvements, while present, do not seem substantial enough to justify the complexity of the proposed approach. A more thorough analysis of the performance gains across different perturbation radii and datasets is needed. It would be beneficial to see a comparison with more recent state-of-the-art methods, especially those that also leverage consistency models or related techniques.

### Questions
- What are z_0 and z_1 in Algorithm 1? More explanation and a detailed description of the proposed method are needed.
- It is still unclear what the upper limit of this method is. I hope the authors can explain this and clarify why the method has or has not reached this limit if applicable.
- It appears that this method relies on the consistency model to denoise perturbed data. My question is why the consistency model can recover perturbed data to the corresponding original data. Although this is not the main contribution claimed by the paper, I still hope the authors can provide a reasonable explanation for this.

### Soundness
2

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
4

### Summary
This paper proposes to incorporate a new diffusion trajectory based consistency loss to the self-supervised pretraining of vision transformers for robust representation learning. The resulting model can be utilized directly in the randomized smoothing framework for certified adversarial robustness, removing the need of pretrained diffusion models employed by prior works. The proposed method, rRCM, is competitive with prior art at low perturbation radii with lower latency, while outright exceeding previous state of art performance at larger perturbation radii.

+++++++++++++++++++++++++++++++++++++++++++++++++++++

Post rebuttal edit:

Most of my concerns regarding clarity and presentation have been addressed in the revision. I think the paper is in solid shape and hence would recommend accepting for publication.

### Strengths
1. The proposed method makes sense intuitively and seems like a novel way to bake adversarial robustness into representation learning pipelines
2. Experimental evaluations are fairly thorough and the performance improvements over prior methods are quite large.

### Weaknesses
1. I can’t quite understand what is the message behind the image generation experiment in section 4.5. Is the diffusion model trained on actual images in CIFAR10? If so, then regardless of whether the conditioning encoder extracts meaningful semantic representations, the diffusion model will produce images that resemble CIFAR10 images.

2. Overall, writing could use some polish. Some examples:
  * Line 42 “While empirical defenses train DNNs to be robust to known adversarial examples (Madry et al., 2017) during training”
  * Line 305 “... . And we…”
 * Line 315 “During pre-training, we adopt the settings of the diffusion model in EDM”. Which settings are you adopting?
* Table 1. Table caption should appear on top of table. Ties should be highlighted (SmoothAdv at r=2.5)
*There is a lot of empty space around figures and some sections in the text that could be removed (such as that on image generation) to make space for a method figure in the main text (but leave out the patch illustration as I think most audiences are familiar with how ViTs work).
* Figures 1,3,4,5 have “classification accuracy” on y-axis, should this be “certified accuracy”?
* Figure 3 is never mentioned in text. Captions or legends in figures 3,4, and 5 should indicate which dataset the evaluation is from.
3. Writing in the method section in particular lack clarity in several places:
* a. While I understand the idea the authors are attempting to convey with equation 6 and 7, their presentation diminishes the rigor of the paper as the equality constraint between $f(x_*)$ in 6 and the dot product being equal to 1 are strong statements. It would be more appropriate to instead state, for instance, that you intend to minimize the differences between two $f(x_*)$ , i.e. $\min_\theta ( f_\theta (x_*) - f_\theta (x_**) )$. As a side note, one clearly does not intend to have equation 6 hold all the way to $t_N$, as the marginal of the PF-ODE at $t_N$ attains a standard Gaussian distribution, such that all trajectories are indistinguishable in distribution at this time step, thereby forcing f to loose all discriminative power.
* b. How is teacher-student training actually related to your proposed method? Is it just the use of the ema weights in the contrastive loss? This seems like a weird point of emphasis as even the SimCLR paper doesn’t consider itself an example of knowledge distillation. The paragraph on teacher-student learning in related works feels similarly ill-named.
* c. In Algorithm 1, it is not clear whether mlp(g( , )) corresponds to the linear head or the non-linear projector head. It is also not clear what ct_loss and cnsis_loss meant (also, there’s a typo “cnsis_loss” becomes “cnsis” on the next line)
* d. Line 247-line 253 cites SimCLR but there doesn’t seem to be any statement in SimCLR that supports the statement of line 247-line 253
* e. Line 255-line 272 was very confusing until I read line 273 stating that you use contrastive loss in addition to the PF-based consistency loss. It would have been much more clear to state that these two losses were used before going into details such as which samples are augmented and the bottleneck layer. Furthermore, an expression of the consistency loss should be included in the methods section for completeness.
* f. There is no subsection on finetuning?
* g. Why the obsession with comparisons to MoCo-V3 but not have it in the main results tables?

### Questions
1. Please address my concerns in the weaknesses section. I think the technical content of the paper is great but the presentation of the paper requires significant work.
2. On what hardware configuration and at what batch size are the latency number obtained?
3. What are the “raw” classification accuracies of rRCM-B-Deep on Imagenet at various perturbation radii? (the numbers in bracket in Carlini2022’s table 1 and 2)

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The authors propose a novel defense method for image classifiers utilizing contrastive denoising. Experimental results indicate that their approach significantly enhances the model's robustness while reducing inference latency.

### Strengths
The authors present strong empirical results, claiming that their method outperforms existing methods in the literature by as much as 5.8% while reducing inference costs by 46 times on ImageNet. The concept of training a robust model using the contrastive denoising method has the potential to benefit adversarial defense society and inspire future research.

### Weaknesses
Honestly, I’m not familiar with the denoising-based adversarial defense literature, so my concerns mainly focus on the experimental settings and results.

1. In Figure 1. The authors compare their method with others from the literature. While their method achieves competitive accuracy, the model structure (number of parameters) differs from those used in other studies. It is unclear whether the reduction in inference latency is due to a smaller model size, a high-performance deep learning toolkit (Footnote 5), or advancements in the proposed method. What is the adversarial accuracy of the methods from the literature when using the same models as those employed by the authors in this paper?

2. Line 228-229. Could author further clearify what is role of the teacher model, in the teacher-student training paradigm they used in the paper?

3. What is $Z_1$ and $Z_2$ in the pseudocode of algorithm 1?

4. Line 255-264. Why can a trainable MLP be considered a data augmentation method? Setting data augmentation aside, I still cannot agree with the claim that adding a trainable MLP can "ensure" the model captures meaningful representations. It would be helpful if the authors could provide more evidence to support this statement.

5. In Figure 3, the authors compare their results with those of MoCo V3. However, the accuracy of MoCo V3 is significantly lower than what is reported in the original paper when the radius is set to zero, raising concerns about the correctness of the implementation and the fairness of the comparison.

6. Line 466. Minor: It seems it should be Figure 3 rather than Figure 4.

7. NOT A WEAKNESS (CONCERN). I’m just curious—since the paper is focusing on the defense method, could the authors provide further explanation of the motivation behind Section 4.5, "Image Generation"?

### Questions
Please see the weaknesses section.

### Soundness
3

### Presentation
4

### Contribution
3
