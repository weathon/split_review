# One-Prompt-One-Story: Free-Lunch Consistent Text-to-Image Generation Using a Single Prompt

- Decision: Accept
- Avg Score: 7.40
- Scores: 5, 8, 8, 8, 8

## Abstract
Text-to-image generation models can create high-quality images from input prompts. However, they struggle to support the consistent generation of identity-preserving requirements for storytelling. Existing approaches to this problem typically require extensive training in large datasets or additional modifications to the original model architectures. This limits their applicability across different domains and diverse diffusion model configurations. In this paper, we first observe the inherent capability of language models, coined $\textit{context consistency}$, to comprehend identity through context with a single prompt. Drawing inspiration from the inherent $\textit{context consistency}$, we propose a novel $\textit{training-free}$ method for consistent text-to-image (T2I) generation, termed "One-Prompt-One-Story" ($\textit{1Prompt1Story}$). Our approach $\textit{1Prompt1Story}$ concatenates all prompts into a single input for T2I diffusion models, initially preserving character identities. We then refine the generation process using two novel techniques: $\textit{Singular-Value
Reweighting}$ and $\textit{Identity-Preserving Cross-Attention}$, ensuring better alignment with the input description for each frame. In our experiments, we compare our method against various existing consistent T2I generation approaches to demonstrate its effectiveness, through quantitative metrics and qualitative assessments.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper proposes a training-free method to enhance subject consistency in text-to-image models. This setting comprises an identity prompt describing the desired subject and a set of frame prompts describing the subject in different scenarios. The proposed method consists in concatenating the identity prompt and all frame prompts into a single, longer, consolidated prompt. Then, in order to generate images for each frame prompt, the consolidated prompt embeddings are reweighed accordingly. This improves identity preservation but harms text-image alignment, so authors propose a couple of techniques to mitigate it. First, the consolidated prompt embeddings are reweighed based on their singular values, which helps preventing information mixing from different frames. Second, the cross-attention between text embeddings and latent image features is modified to improve the subject's consistency. The proposed approach is evaluated on a proposed benchmark and compared against several existing methods, outperforming other training-free methods for identity preservation.

### Strengths
* The proposed method is training free and only increases inference-time compute moderately.
* The proposed method outperforms the considered training-free existing methods on prompt alignment and identity preservation.
* The ablation study confirms the effectiveness of singular-value reweighing and identity-preserving cross-attention.

### Weaknesses
 * Stable diffusion models use a CLIP text encoder, which is limited to 77 tokens. This severely constrains the number of frame prompts that can be used.
* Evaluating on a single benchmark of 200 examples seems insufficient. Additional benchmarks would be needed to verify the robustness of the results. Similarly, a human study on just 20 examples seems quite limited. I would suggest applying bootstrapping to obtain the sample variance.
* In figure 8 (right), applying the proposed method doesn't seem to have a big impact in terms of identity preservation.
* In figure 2, why doesn't P1 have the same text embedding for multi-prompt and single-prompt settings? I believe it should since the context is the same (`[[SOT]; P0]`) and CLIP's text encoder has causal attention.
* What do the shaded regions in figure 2 represent? How are they computed?
* Does changing the order of frame prompts affect results? For instance, always placing the frame prompt of interest at the end.
* In figure 3, I don't see the NPR results as incorrect since the background isn't specified in frame prompts 2, 3, 4 and 5.
* Why does the embedding of the [EOT] token belong to both the expressed and suppressed sets? Won't the effects cancel each other out?
* For prompt alignment evaluation, I would suggest using more recent metrics that are more correlated with human judgment, such as DSG [1] or VQAScore [2].

### Questions
* In figure 2, why doesn't P1 have the same text embedding for multi-prompt and single-prompt settings? I believe it should since the context is the same (`[[SOT]; P0]`) and CLIP's text encoder has causal attention.
* What do the shaded regions in figure 2 represent? How are they computed?
* Does changing the order of frame prompts affect results? For instance, always placing the frame prompt of interest at the end.
* In figure 3, I don't see the NPR results as incorrect since the background isn't specified in frame prompts 2, 3, 4 and 5.
* Why does the embedding of the [EOT] token belong to both the expressed and suppressed sets? Won't the effects cancel each other out?
* For prompt alignment evaluation, I would suggest using more recent metrics that are more correlated with human judgment, such as DSG [1] or VQAScore [2].

[1] Cho, Jaemin, et al. "Davidsonian Scene Graph: Improving Reliability in Fine-grained Evaluation for Text-to-Image Generation." The Twelfth International Conference on Learning Representations.
[2] Lin, Zhiqiu, et al. "Evaluating text-to-visual generation with image-to-text generation." European Conference on Computer Vision. Springer, Cham, 2025.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The goal of this article is pretty similar to Cosistory, but it proposed a new training-free method which focus on how to leverage prompts better. This article first proposes Naive Prompt Reweighting which rescaling the embeddings of the other frame prompts by a reduction factor. Then, it proposes  Singular-ValueReweighting+&- which perform a SVD decomposition and Identity-PreservingCross-Attention(IPCA) which enhance the identity similarity between images generated from the concatenated prompt.

Work is relatively well done, simple and effective, but not very innovative(Reweight and Identity-Preserving or their similar ideas have appeared in previous articles, this artivle just use them into the enhancements of prompts)

What's more, I wonder the quality and improvements for multi-IDs, because nowadays the consistency works  can  generally do well with multiple IDs.

### Strengths
1. Drawing, good.
2.Focus on the enhancements of prompts and make it effectiveinstead of focus on images.
3.Proposed different reweightmethods： NPR and SVR+-, make the article more solid.

### Weaknesses
1. Reweight and Identity-Preserving or their similar ideas have appeared in previous articles, this artivle just use them into the enhancements of prompts(I remember Reweight is used in video, the extent how a prompt or ref img affects different frames is reweighted. )(Identity-Preserving--like [1] which operate on the modality of images)
2. The improvements for multi-IDs are NOT mentioned, which is always talked in recent works like StoryDiffusion(The example of a man and a dog).

### Questions
1. Prove your novelty (I know it's a little hard for training-free methods in this field)。
2. Show results on milti-IDs.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper introduces a novel training-free approach for generating subject-consistent images using text-to-image models. The method concatenates prompts for different frames into a single prompt to achieve consistency, while utilizing two key innovations: singular-value reweighting and identity-preserving cross-attention techniques. These techniques effectively mitigate interference between frames and enhance consistency. Through comprehensive experiments, the authors demonstrate their method achieves superior performance in terms of text-image alignment and subject consistency, compared with both training-required and training-free competitors.

### Strengths
- The paper is well-written, and the results are nicely presented.
- The proposed method is simple yet effective. The paper demonstrates its effectiveness by comparing it with multiple training-required and training-free methods, along with the user study and the ablation study.
- Due to its simplicity, the proposed method should be able to easily be adapted to T2I models with different architectures and sampling strategies.

### Weaknesses
 - Long prompts might pose a challenge to the applicability of the proposed method due to the limit of number of tokens (e.g., M=77 for SDXL by default). Nevertheless, this appears to be a solvable issue.

 - For the experiment in Section 3.1.1, it seems that the t-SNE visualization is conducted for only a single set of prompts. It would benefit the clarity if more details can be provided.
- Instead of the proposed Identity-Preserving Cross-Attention technique, is it possible to improve the consistency by performing SVR on $[c^{P_0}, C^{EOT}]$?
- Does the proposed method affect the visual quality/image realism? How is it compared with other methods?

### Questions
- For the experiment in Section 3.1.1, it seems that the t-SNE visualization is conducted for only a single set of prompts. It would benefit the clarity if more details can be provided.
- Instead of the proposed Identity-Preserving Cross-Attention technique, is it possible to improve the consistency by performing SVR on $[c^{P_0}, C^{EOT}]$?
- Does the proposed method affect the visual quality/image realism? How is it compared with other methods?

### Soundness
4

### Presentation
4

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
The paper proposes a training-free approach for consistent character generation. In particular, given a descriptive prompt of  the main character, followed by frame-specific prompts, the goal is to generate images that faithfully depict each frame, while maintaining a consistent visual appearance of the main character. 

The main observation of the paper is that when combining all frame-prompts with the character description prompt, then the character embedding in each-frame prompt is more consistent. The authors introduce two additional enhancements for their final method.

[1] Singular Value Reweighting (SVR): combining all frame-prompts leads to information blending from different frames. To avoid this, during the generation of frame i (i.e., based on prompt p_i), the authors use SVD to increase p_i contribution to the generation by enhancing the leading singular value of prompt p_i. The authors also suppress the contribution of other other prompts j != i in a similar manner. Here, the authors also take into consideration the end token (EOT), as it contains significant semantic information as well. 

[2] Identity-Preserving Cross-Attention: SVR alone handles intra- fame information blending, although the identity consistency may still be affected. The authors propose to concatenate the k/v- projections in which the token features corresponding to each prompt pi, i in [1,N] are zeroed out. 

Minor:
L 353 (K, V) notations are different from those used later in the paragraph. Since this is a paper on consistency, please maintain consistent notations :-)

### Strengths
[1] The paper is well written and the quantitative and qualitative comparisons are well carried. 

[2] I find the main observation of the paper to be very novel and might have broader implications to other tasks. In particular, exploiting the context consistency of language models for the purpose of character consistent generation. The paper analysis of this observation clearly motivates the rest of the paper. 

[3] Using SVR for prompt-specific enhancement/suppression rather than simple reweighing is interesting.

[4] The visual quality of the generated outputs is good. 

[5] The method is fairly simple and doesn’t complicated procedures

### Weaknesses
[1] In the Identity-Preserving Cross-Attention module, the authors zero-out features of all frame-prompts p_i. It is not clear why not completely removing these features, instead of zeroing them? As zeroing out the features may affect the attention scores, because of the normalization. Also, why the remaining features (i.e, in this case P0 features and EOT features) are enough to enhance consistent identity among frames ? Effectively, this new module (IPCA) biases queries to attend to P_0 and EOT token features. Furthermore,  P_0 and EOT embeddings are different for different frames (because of the asymmetric nature of SVR), hence the additional K/V matrices that are concatenated for different prompts are different as well, hence this means that P_0 and EOT should maintain similar embeddings for different frame-generations, which is not clear from the paper.

[2] The authors claim their method to be memory-efficient compared to existing methods. I think it is nice to know the memory complexity of the proposed method compared to existing ones.

### Questions
Following my points raised in the weakness section, can you please consider answering the following ?

[1] Can you please confirm that you simply zero-out the token features of all prompts P_i, i \in [1,N] ,except for P_0 and EOT ?

[2] What is the rationale behind zeroing out features of frame-prompts p_i rather than removing them entirely? How does this affect attention scores and normalization?

[3] How do the P_0 and EOT features alone enhance identity consistency across frames? Given that P0 and EOT embeddings may differ across frames due to SVR, how does your method ensure consistent embeddings for different frame generations?

[4] Can you please provide further motivation to the KV extension and why this generates more consistent characters. To me this is similar to the KV sharing used in Consistory, but here the the KV-extension only biases the queries to attended PO and EOT (which can be different for different frames due to the SVR procedure).

[6] Can you provide memory complexity comparison between your method and existing approaches.

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper introduces a novel, training-free approach called 1Prompt1Story to address the character consistency issue in storytelling. By concatenating all prompts into a single input, 1Prompt1Story preserves character identities from the start. The generation process is further refined using two innovative techniques: Singular-Value Reweighting and Identity-Preserving Cross-Attention. Comparative experiments demonstrate that 1Prompt1Story improves identity consistency and alignment with input descriptions, outperforming existing methods both quantitatively and qualitatively. Further experiments also show that 1Prompt1Story supports ControlNet.

### Strengths
- The authors' observation of inherent context consistency in text, along with their proposed NPR method, is particularly insightful. It offers a direct and elegant solution for maintaining consistency in text-to-image generation, making a meaningful contribution to the field.
- The paper is well-written, clearly structured, and easy to follow.
- The quantitative analysis of context consistency, particularly through t-SNE visualizations and text-prompt distance metrics, is sound and convincing.
- The authors employ a comprehensive set of metrics to demonstrate the advantages of their method, providing a robust evaluation that underscores the effectiveness of their solution.

### Weaknesses
 - The Prompt Consolidation method concatenates all text prompts into a single input before feeding it to the text encoder. However, in my view, this approach faces a significant limitation for generating longer stories due to the token length restrictions of the diffusion model’s text encoder. In contrast, other training-free personalized storytelling methods do not encounter this issue, which limits the broader applicability of the proposed method. It would be helpful if the paper explicitly addressed the length limitation of the 1Prompt1Story approach. Additionally, are there any potential solutions to mitigate this constraint? Or will you compare the practical story length capabilities of your method versus other training-free approaches?
- The handling of the EOT tokens in lines 290-322 appears somewhat unclear. Could you further clarify why the EOT needs to be initially expressed and then suppressed? Additional explanation of this process would enhance understanding. Will you provide a brief explanation of the role of EOT tokens in the model?
- The user study sample size of 20 participants seems relatively small, which may limit the generalizability of the findings.

### Questions
Please the first and second point of the weaknesses section.

### Soundness
3

### Presentation
4

### Contribution
3
