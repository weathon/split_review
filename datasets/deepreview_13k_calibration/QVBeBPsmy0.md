# Mitigating Compositional Issues in Text-to-Image Generative Models via Enhanced Text Embeddings

- Decision: Reject
- Avg Score: 4.50
- Scores: 5, 5, 3, 5

## Abstract
Text-to-image diffusion-based generative models have the stunning ability to generate photo-realistic images and achieve state-of-the-art low FID scores on challenging image generation benchmarks. However, one of the primary failure modes of these text-to-image generative models is in composing attributes, objects, and their associated relationships accurately into an image. In our paper, we investigate this compositionality-based failure mode and highlight that imperfect text conditioning with CLIP text-encoder is one of the primary reasons behind the inability of these models to generate high-fidelity compositional scenes. In particular, we show that (i) there exists an optimal text-embedding space that can generate highly coherent compositional scenes showing that the output space of the CLIP text-encoder is sub-optimal, and (ii) the final token embeddings in CLIP are erroneous as they often include attention contributions from unrelated tokens in compositional prompts.  Our main finding shows that the best compositional improvements can be achieved (without harming the model's FID score) by fine-tuning only a simple and parameter-efficient linear projection on CLIP's representation space in Stable-Diffusion variants using a small set of compositional image-text pairs. This result demonstrates that the sub-optimality of the CLIP's output space is a major error source.  We also show that re-weighting the erroneous attention contributions in CLIP can lead to slightly improved compositional performances.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper investigates why early versions of stable diffusion (v1.4 and v2) are bad at composition. The authors found two sources: 1) CLIP text embeddings have wrong attentions between words, 2) the CLIP text embeddings fail to fully drive the UNet to generate compositional images. The authors propose two patches for the two sources, respectively: 1) zero-shot attention reweighting, 2) adding a linear projection layer to the CLIP text embeddings to make it drive the UNet more accurately.

### Strengths
1) The proposed methods are simple and easy to implement.
2) The proposed method are validated to be effective in experiments.

### Weaknesses
1) Training a linear projection layer on top of CLIP text embedding seems ad-hoc. Especially, the authors focused on a few types of attributes:  color, texture, shape. However, in practice, we cannot limit compositional prompts to these few types. If we want the projection layer to handle more types, we need to train the layer on more diverse instances, which demand increasing manual efforts.

2) The newer models, e.g., SDXL, SD 3.5, and FLUX, have been much better at composition. This indicates that the source of bad composition is the SD1.4/2.0 models were not well designed or well trained. Therefore, systematic solutions like redesigning and retraining the model should be our main pursuit for solving compositionality. **Patching a bad model** could work as a temporary solution to some degree, but I'm not sure if this direction is worth investing significant amount of time and efforts.

### Questions
N/A

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper aims to mitigate the compositional issues in recent CLIP-based diffusion models, such as Stable Diffusion. Specifically, the authors first show that the output space of the CLIP text encoder is sub-optimal. Then, they propose to fix it by using a window-based linear projection for text embeddings from the CLIP model. Experiments have demonstrated the effectiveness of their approach.

### Strengths
1. The idea is easy to understand. The CLIP model may not capture some key concepts or attributes in a prompt. Thus, applying a window-based linear projection could help reweight the text embeddings, which improves prompt alignment in text-to-image generation.

2. The proposed window-based linear projection brings a clear improvement in terms of color, texture, and shape, as demonstrated in Table 1.

3. This paper is easy to follow. Figures have well demonstrated their core idea.

### Weaknesses
1. There exist some training-free approaches to reweight the text embedding for better prompt alignment, such as enhancing the attention on a few words, e.g., (tuxedo) or (tuxedo:1.21) in stable-diffusion-webui, where the number indicates the strength of word embedding. This approach reweights the text embeddings from CLIP encoder, in a way that it slightly changes the overall text condition signals for the subsequent diffusion process. Compared to it, the introduced WiCLP in this paper trains an additional layer which achieves something similar but may specifically target one model only. As the aforementioned approach has been widely adopted in the text-to-image generation community, the authors are encouraged to add a brief discussion with it [A].

2. Practical concerns. This approach requires training an additional linear projection, which could be impossible if we only have the released model weights and cannot access the pretraining dataset. According to Section D.1, the training cost is also not negligible (25K steps on one RTX A5000 GPU). It would be good to know if the trained linear projection can be generalized to other diffusion models as well, such as those finetuned/stylized diffusion model [B,C].

### Questions
Please see the weakness.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper investigates compositionality-based failure modes in text-to-image generative models, identifying imperfect text conditioning with the CLIP text encoder as a key factor hindering the generation of high-fidelity compositional scenes. To address this, the authors propose a simple yet effective baseline, WiCLP, which fine-tunes a linear projection within CLIP's representation space. WiCLP achieves superior performance on compositional image generation benchmarks while maintaining a low FID score across a wide range of clean prompts.

### Strengths
1. The paper provides a detailed analysis of CLIP text embeddings, examining the response and alignment between tokens, which accurately pinpoints the root of compositionality issues in SD 1.5 and SD v2.
2. The experimental results convincingly demonstrate the effectiveness of the proposed improvement, providing clear evidence of its advantages over existing methods.

### Weaknesses
1. My primary concern is the limited innovation. The proposed solution merely involves a projection fine-tuning of CLIP text embeddings, with WiCLP simply aggregating information from neighboring tokens. Ultimately, the method only fine-tunes text embeddings on a selected dataset using Stable Diffusion, lacking sufficient technical novelty. The core idea of fine-tuning a linear projection is not new, and the paper does not adequately justify why this specific approach, compared to other possible fine-tuning strategies, is the most effective for improving compositional understanding. The aggregation of neighboring tokens, while intuitive, lacks a deeper theoretical justification or analysis of its impact on the learned representations.

2. The paper includes limited comparisons. There are no qualitative results of other baselines such as SDXL, nor comparisons with recent compositional generation methods such as RPG[1], Realcompo[2]. The baselines provided seem somewhat outdated, and the absence of recent methods makes it challenging to gauge the true impact of the proposed approach. The lack of comparison with SDXL is a significant oversight given its widespread use and improved architecture. Furthermore, the absence of comparisons with methods like RPG and Realcompo, which explicitly tackle compositional generation, makes it difficult to assess the relative merit of the proposed approach.

3. The experiments are limited. By fixing the U-Net and text encoder and only fine-tuning the text embeddings, the paper restricts itself, as fine-tuning any component on the selected data might yield compositional improvements. A comparison with alternative fine-tuning approaches would help validate whether adjusting the text embeddings specifically yields the best results, rather than gains simply from better-selected samples. The paper does not explore the impact of fine-tuning other components, such as the U-Net, which could also contribute to improved compositional understanding. This lack of exploration limits the conclusions that can be drawn about the specific effectiveness of fine-tuning the text embeddings.

4. Limited impact. The baseline used is Stable Diffusion v2, which is outdated, and the approach centers around fine-tuning the CLIP text encoder. However, most modern generative models, like SD3 and Flux, now use T5-based encoders. Thus, it is uncertain if the proposed method would have practical utility in today’s models. The focus on CLIP encoders, while understandable given the paper's analysis, limits the practical applicability of the proposed method to newer architectures that have moved away from CLIP. This raises questions about the long-term relevance of the work.

5. Poor presentation. The paper has significant issues in its writing: quotation marks are inconsistently formatted, Figure 5 lacks labels on the left, making it hard to interpret, and Figure 7 is very low resolution.

### Questions
1. I am curious whether fine-tuning other parts of Stable Diffusion could achieve similar improvements. It would be beneficial to evaluate which component adjustments yield the most effective or efficient results.

2. How would the proposed method be adapted for T5-based diffusion models, such as Pixart-Alpha? Is it likely to produce comparable results in these architectures?

### Soundness
2

### Presentation
1

### Contribution
1

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a fine-tuning approach to address the compositionality issue of text-to-image diffusion models. Specifically, it first identifies one of the major sources of the problem is that the attention module in text encoder tend to assign wrong attention of unintended tokens to other tokens, resulting in distorted representation. Then it proposes a window-based projection layer - by learning to aggregate information of tokens within a local window for a new representation. Experimental results show that the proposed method have better compositional alignment with respect to the text description without harming the model's FID score.

### Strengths
1. The paper is well motivated, as correctly composing the object / attribute relations in text-to-diffusion models is a very important problem.
2. The paper makes the observation that one source of wrong composition is in the attention assignment operation within the text encoder, which makes intuitive sense and is supported by experimental results. 
3. The paper proposes to add a window-based linear projection layer on top of the text embedding for fine tuning, showing better compositionality alignment, while maintaining FID values.

### Weaknesses
1. The window-based projection design is based on the assumption that tokens with close semantic relations occur within a local window. However, this is not necessarily the case in more complex sentence, in which semantically related words have longer distance than the length of window, e.g. "three cubes, the color of which are red, green, blue".  So the proposed solution might not fundamentally address the attention assignment issue, which requires a more general sentence parsing method.
2.  There are no failure case visualizations showing under what situations will the proposed method fail to capture the correct relations in the text description. Furthermore, the method seems to struggle with numerical compositionality, often generating the correct attributes but the wrong number of objects, even for simple prompts like "one A one B". This suggests the proposed method may not be fundamentally addressing the token attention assignment problem, and the locality constraint may be too simplistic to capture complex relationships.

### Questions
1. As mentioned in weaknesses, it would be better to show more generated samples under complex descriptions, to see whether the proposed design is generally applicable. (Specifically, complex in the sense that semantically related words have distance longer than the length of the window)
2. Whether there are examples in the tested datasets that the proposed method failed to generate the expected compositions?

### Soundness
2

### Presentation
3

### Contribution
2
