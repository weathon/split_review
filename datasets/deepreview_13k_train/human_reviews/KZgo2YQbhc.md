# PaRa: Personalizing Text-to-Image Diffusion via Parameter Rank Reduction

- Decision: Accept
- Scores: 8, 6, 8, 8

## Abstract
Personalizing a large-scale pretrained Text-to-Image (T2I) diffusion model is challenging as it typically struggles to make an appropriate trade-off between its training data distribution and the target distribution, \ie, learning a novel concept with only a few target images to achieve personalization (aligning with the personalized target) while preserving text editability (aligning with diverse text prompts).  
  In this paper, we propose \textbf{PaRa}, an effective and efficient \textbf{Pa}rameter \textbf{Ra}nk Reduction approach for T2I model personalization by explicitly controlling the rank of the diffusion model parameters to restrict its initial diverse generation space into a small and well-balanced target space. Our design is motivated by the fact that taming a T2I model toward a novel concept such as a specific art style implies a small generation space. To this end, by reducing the rank of model parameters during finetuning, we can effectively constrain the space of the denoising sampling trajectories towards the target.
  With comprehensive experiments, we show that PaRa achieves great advantages over existing finetuning approaches on single/multi-subject generation as well as single-image editing. Notably, compared to the prevailing fine-tuning technique LoRA, PaRa achieves better parameter efficiency ($2\times$ fewer learnable parameters) and much better target image alignment.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper proposes a framework for T2I model personalization called PaRa (Parameter Rank Reduction). It introduces an innovative approach to control the rank of diffusion model parameters, thereby constraining the initially diverse generation space to a smaller, more balanced target space. This enables the generation of personalized concepts and single-image editing. Furthermore, multiple individually fine-tuned PaRa modules can be combined to achieve the fusion of multiple personalized concepts. The framework also demonstrates higher parameter efficiency and better alignment with target images, with experimental results validating its effectiveness.

### Strengths
1. This paper is well-structured and easy to understand.
2. The idea of achieving T2I model personalization by controlling the rank of diffusion model parameters is highly innovative. Additionally, detailed explanations are provided for the introduced learnable low-rank parameters.
3. The experimental section is well-designed with sufficient data, demonstrating the effectiveness of PaRa in single/multi-subject generation and single-image editing, as well as its compatibility with other modules.

### Weaknesses
1. The methodology section includes extensive explanations of the mathematical principles behind PaRa but lacks an organized overview of the model’s framework. From the subsequent experimental section, it is evident that the approach also utilizes text embeddings, among other elements. While these are not the main focus of the methodology, they should be appropriately explained, specifically how the introduced [V] tokens interact with the text embeddings. Additionally, adding some visualizations in the methodology section, such as a diagram illustrating the data flow and parameter interactions within the PaRa module, would make the concepts more intuitive.
2. In the last part of the introduction (lines 110–111), it states that "PaRa achieves state-of-the-art performance in personalized single/multi-subject generation." However, the experiments do not provide sufficient comparisons to support this claim. Firstly, there is no comparison with encoder-based personalization methods mentioned in the introduction. Secondly, the fine-tuning-based personalization methods used in the experiments are not the latest approaches in this field, such as methods that incorporate more advanced regularization techniques or adaptive learning rates, which weakens the persuasiveness of the results.
3. In section 3.1, it is mentioned that “B is initialized to zero and fine-tuned with a few text-image pairs.” The experimental section should clarify the scale of the data used, the fine-tuning time, the specific optimizer used, and the learning rate schedule. Additionally, to support the claim of higher parameter efficiency, a computational efficiency analysis should be provided, including the number of FLOPs and memory usage compared to other methods.
4. From the image editing results, it appears that introducing PaRa may result in some loss of texture information, particularly in fine details. The analysis and interpretation of the experimental results are insufficient, and a more detailed discussion of the trade-offs between editability and texture preservation is needed.

### Questions
See Weaknesses.

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
A diffusion based image personalization method is presented via a parameter rank reduction technique. Particularly, the proposed method controls the rank of the diffusion model parameters to restrict the generation space into a small and well-balanced target space, achieving trade-off between the training data distribution and the target distribution. The motivation of the method lies in two main aspects. Firstly, this paper assumes that taming a T2I model toward a novel concept implies a small generation space. Secondly, the rank of matrix is important for parameter efficient fine-tuning. In this case, by reducing the rank of model parameters during finetuning, the proposed method is proven to achieve advantages over existing finetuning approaches on single/multi-subject generation and single-image editing.

### Strengths
1. Solving personalisation from matrix decomposition is a reasonable and good idea.
2. Combing rank with edibility, especially diversity of the generated image is proven effective in this paper.
3. The experiments are convincing in explaining the superiority of the proposed solution.

### Weaknesses
1. Matrix decomposition is proven to be effective in parameter efficient fine-tuning tasks, e.g. image editing. Although the difference between the proposed solution to Lora is clear. As both methods are based on matrix decomposition, it's not clear what are the foundational differences, and how the authors come up with the current solution.
2. SSIM is used in this paper for image diversity evaluation. I'm not quite sure whether SSIM is the best one, as SSIM focuses on pixel-level difference instead of semantic level difference. e.g. position difference of the same instance may contribute more to SSIM than than an extra accessory. 
3. Writing should be improved to highlight the contributions, especially how the solution is formed, and how it is different from the existing techniques.

### Questions
1. One important motivation of the paper is that taming a T2I model toward a novel concept implies a small generation space, making it possible to perform one-shot training for the low-rank parameter B. I'm curious about the relationship between edibility and the optimal rank of B. Is it always possible to learn a good low-rank B to perform reasonable editing in one-shot manner? It's just an open question. Please share your experiences.
3. As a one-shot training techniques for image editing, how the model perform with different one-shot pairs? Please explain robustness of the model.
4. Both numbers and visualisation are good in explaining the superiority of Para compared with existing techniques. Then, what are the limitations of Para? Please provide a rough failure case analysis.

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
4

### Summary
This work aims to balance personalization and text editability by reducing the rank of model parameters, effectively narrowing the generation space to better align with target concepts. This method is more parameter-efficient and achieves better target image alignment than existing techniques like LoRA. It also supports combining multiple personalized models and facilitates stable single-image editing without additional noise inversion processes. The paper shows PaRa’s effectiveness through comprehensive experiments on single and multi-subject generation tasks.

### Strengths
1. The proposed Parameter Rank Reduction (PaRa) method is a creative solution to the challenge of T2I model personalization, offering a new perspective on controlling the generation space.
2. PaRa demonstrates significant parameter efficiency, requiring 2× fewer learnable parameters compared to existing methods like LoRA.
3. The paper provides extensive experimental results showing PaRa’s advantages in single/multi-subject generation and single-image editing and shows better results than LoRA.
4. The paper is very well written and presented.

### Weaknesses
1. The authors have not compared their method with SOTA such as LyCoris, DiffuseKronA, etc. Including these results would provide a better comparison of the method.

### Questions
The only concern is insufficient comparisons to SOTA, adding which would allow a better comparison.

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
This paper proposes a new method to personalizing diffusion model with few samples, which is to reduce the rank of the original weights in diffusion models. This method allows the finetuned model to have smaller diversity and better alignment with the training data. This paper conducts extensive experiments on various generation task including single subject, multi-subject generation and editing. The paper is well written and easy to understand.

### Strengths
1) This paper provides a very interesting ideas to personalize diffusion model by reducing the rank of the weights. 
2) The proposed finetuning method is simple, effective and show good flexibility.

### Weaknesses
1) Different hyper-parameters may affect the alignment of the previous methods, such as the Rank of LoRA and fine-tuning steps. Authors may need to provide more clarification on how these hyper-parameters are chosen for the compared methods to make sure they achieve good enough alignment in the experiments.

### Questions
Please refer to the concerns in the Weakness.

### Soundness
3

### Presentation
3

### Contribution
3
