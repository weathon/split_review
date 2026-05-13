# ImageFolder: Autoregressive Image Generation with Folded Tokens

- Decision: Accept
- Scores: 5, 6, 6, 8

## Abstract
Image tokenizers are crucial for visual generative models, \eg, diffusion models (DMs) and autoregressive (AR) models, as they construct the latent representation for modeling. Increasing token length is a common approach to improve the image reconstruction quality. However, tokenizers with longer token lengths are not guaranteed to achieve better generation quality. There exists a trade-off between reconstruction and generation quality regarding token length. In this paper, we investigate the impact of token length on both image reconstruction and generation and provide a flexible solution to the tradeoff. We propose \textbf{ImageFolder}, a semantic tokenizer that provides spatially aligned image tokens that can be folded during autoregressive modeling to improve both generation efficiency and quality. To enhance the representative capability without increasing token length, we leverage dual-branch product quantization to capture different contexts of images. Specifically, semantic regularization is introduced in one branch to encourage compacted semantic information while another branch is designed to capture the remaining pixel-level details. Extensive experiments demonstrate the superior quality of image generation and shorter token length with ImageFolder tokenizer.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
- This paper presents a semantic image tokenizer that provides better token representations for visual autoregressive modeling, with improved generation quality and efficiency. 

 - The authors leverage product quantization and semantic regularization for a more compact representation. Extensive experiments demonstrate the advantage of the proposed tokenizer over previous ones.

### Strengths
- This paper targets learning more semantically compact and disentangled image token representations, which leads to better autoregressive modeling with improved performance and shorter token length. The issue of information density(token length) and the explanation of previous image tokenizers have been hindering the performance of visual autoregressive modeling.

  - Compared to previous work on image tokenizers, this work investigates product quantization to separate different information about images. With the proposed muti-scale RQ, semantic regularization, and quantizer dropout, the representation of image tokens is enhanced.

 - Extensive experiments on autoregressive modeling and visualization demonstrate the superiority of ImageFold.

### Weaknesses
 - Several important components in this work have been investigated in previous works, including adopting semantic regularization, multi-scale RQ, and parallel decoding has been explored in earlier works. 

 - This work lacks either enough theoretical or empirical discussions about product quantization.  Additional details, such as more visualization and discussion as in Fig. 8, should be provided to validate the "disentangled" nature of the obtained image tokens.  (see Questions)

 - This work missed some important references. Although product quantization has been rarely discussed in image tokenizers. Previous works[1] on tokenizing other modalities such as audio have adopted relevant strategies.

### Questions
- To better understand the method, the authors should add more analysis about the proposed tokenizer, such as the perplexity (codebook usage) with different techniques.

 -  Although this work primarily experiments with autoregressive modeling, the tokenizer does not seem to be particularly designed for AR modeling. How would this tokenizer perform on other generative schemes, such as diffusion, and non-autoregressive modeling?

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
This paper proposes a novel method to solve the problem of how to improve image quality under finite length tokens, and proposes a semantic tokenizer, which realizes good image quality under smaller length tokens through Product Quantization.

### Strengths
1. The idea of this paper is novel. Through Product Quantization, token processing is carried out in smaller spaces, and good performance is achieved under fewer tokens.
2. The logic of this paper is rigorous, the argumentation is clear, the method is fully explained, and the experimental setting is rigorous.

### Weaknesses
Although this paper has reached an acceptable level, there are still several small problems that need to be worked on.
1. The description of performance indicators in the article is not in place. Tables 1, 2 and some later tables do not give a simple indication of superior performance represented by high or low indicators.
2. In Formula 4, the description of several hyperparameters and their Settings is missing.

### Questions
Please solve the problem I mentioned above

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces a novel image tokenizer called ImageFolder, which addresses the trade-off between image reconstruction quality and generation quality in visual generative models, such as diffusion models and autoregressive (AR) models. The key contributions of the paper can be summarized as follows: 1. The proposed tokenizer provides spatially aligned image tokens that can be folded during autoregressive modeling, resulting in a shorter token length without compromising reconstruction or generation quality. The experiments demonstrate that folded tokens outperform unfolded ones in terms of generation performance, even when the overall token count remains the same. 2. The paper explores the use of product quantization within the image tokenizer. It introduces semantic regularization and quantizer dropout to enhance the representational capability of the quantized image tokens by separately capturing semantic information and pixel-level details. 3. Extensive experiments are conducted to investigate the relationship between token length, generation quality, and reconstruction quality, providing deeper insights into the image generation process in AR modeling.

### Strengths
1.The ImageFolder tokenizer achieves better generation performance by effectively folding tokens, which enhances the efficiency of the autoregressive modeling process.

2.Despite reducing token length, the proposed method does not sacrifice the quality of image reconstruction, making it a balanced solution for generative tasks.

3.By leveraging product quantization and introducing mechanisms like semantic regularization and quantizer dropout, the tokenizer captures richer semantic and pixel-level information, leading to more accurate image representations.

4.The paper provides extensive experimental results that validate the effectiveness of the proposed method, offering a solid foundation for its claims and demonstrating its superiority over existing tokenizers.

5.The investigation into the trade-off between generation and reconstruction quality with respect to token length contributes to a better understanding of the dynamics involved in image generation, which can inform future research in the field.

### Weaknesses
1.The training is based on the tokenizer from LlamaGen. Is it possible to train one from scratch to better demonstrate its effectiveness?

2.How is the token length of 265 derived from the residual scales [1, 1, 2, 3, 3, 4, 5, 6, 8, 11]? The paper should clarify the exact calculation and rationale behind this specific token length, as it is not immediately obvious how these scales translate to the final token count. A more detailed explanation of the relationship between the residual scales and the resulting token length is needed to fully understand the design choices.

3.Are there other length design comparisons for token length, such as 265, 430, etc., to better validate the results? The paper should include a more comprehensive ablation study on token length, exploring a wider range of values beyond the single point comparison. This would help to understand the sensitivity of the proposed method to token length and identify the optimal configuration.

### Questions
1.The training is based on the tokenizer from LlamaGen. Is it possible to train one from scratch to better demonstrate its effectiveness?

2.How is the token length of 265 derived from the residual scales [1, 1, 2, 3, 3, 4, 5, 6, 8, 11]?

3.Are there other length design comparisons for token length, such as 265, 430, etc., to better validate the results?

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
4

### Summary
The paper is well-structured, comprehensive, and easy to understand, making the proposed concepts accessible. It presents a novel approach to decoupling features using separated quantizers and manages both the separated quantizers and input features through product quantization. Overall, the paper offers valuable insights and design strategies for quantizer development, contributing to advancements in feature token quantization.

### Strengths
1. The paper is well-structured, comprehensive, and easy to understand, making the proposed concepts accessible.

2. It presents a novel approach to decoupling features using separated quantizers and manages both the separated quantizers and input features through product quantization.

3. This approach effectively mitigates the performance drop observed in previous work caused by incorporating semantic features.

4. The model achieves comparable performance to state-of-the-art (SOTA) methods, demonstrating the efficacy of the proposed method.

5. Overall, the paper offers valuable insights and design strategies for quantizer development, contributing to advancements in feature token quantization.

### Weaknesses
1. The results section lacks a comprehensive comparison with a broader range of current state-of-the-art VAE and autoregressive (AR) token quantizers. Including such comparisons, particularly with methods that utilize different quantization strategies or loss functions, would provide stronger validation of the method’s performance. Specifically, a comparison against models using vector quantization or other learned quantization techniques would be beneficial.

2. In the main paper, the VAR model training has not reached final results, only intermediate outcomes are presented. Showing the final results, including convergence metrics and final performance scores, would strengthen the evaluation and allow for a more thorough assessment of the method's capabilities.

3. In terms of ablation studies, the paper would benefit from additional experiments that test the model with only the semantic branch or only the detail branch under the same experimental setting. Additionally, showing results where only a single branch incorporates semantic information, while the other branch operates without semantic input, would provide a more complete analysis of the method’s effectiveness and the contribution of each branch. This would help to isolate the impact of the semantic information.

4. Finally, presenting quantizer dropout—a popular regularization technique—as a primary contribution does not seem particularly solid. While dropout can be effective, it is not a novel technique in itself, and its application here, while potentially beneficial, does not represent a major conceptual advancement.

### Questions
Q1: In Table 1, does “tokens” refer to the number of input tokens or codebook tokens?

Q2: The symbol “L” in “247 quantizer drop” can be confusing as it is also used for patch size in the previous context. Additionally, in Table 3, patch size is denoted as  K=1, which adds to the confusion. Could you clarify this section further? Also, please consider refining the symbol definitions.

Q3: In Figure 5, should the grid size double after each downsampling? Currently, it shows 1x1 to 2x2 to 3x3—how should this be understood? Why does the grid increase with the step size? Also, why does resolution increase from left to right? Is this sequence reversed? Normally, the input has the highest resolution, which decreases as the step deepens.

Q4: In line 273, is dropout necessary for a simple semantic quantizer? Is it possible to dropout only one branch during training, so that we may know which branch will be impacted much more?

Q5: Has contrastive loss been considered using CLIP’s prompt or image features to create a more robust text-image pre-trained model? The paper mentions that DINO’s semantic-rich feature isn’t suitable for image generation. Would using models like CLIP potentially alleviate this issue, making a separate semantic quantizer branch unnecessary?

Q6: In AR modeling, does dividing one token into two sub-tokens and computing losses for each mean we are increasing the token count without lengthening the token length? Line 408, mentions increasing the token count without enlarging the token length, yet line 340 states that a shorter token length benefits quality while keeping the token count the same. Could you clarify this part?

Q7: A smaller patch size ( k=1 ) impacts performance significantly. Is this necessary, and have you tried other designs or experiments around patch size?

Q8: Could you add a comparison of different tokenizer performances for better illustration, such as comparisons with different VAEs and token quantizers?

Q9: In the 4-branch quantizer, how is the contrastive loss applied? Does this only worsen gFID in your results?

### Soundness
3

### Presentation
3

### Contribution
2
