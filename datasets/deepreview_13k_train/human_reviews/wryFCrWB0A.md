# A Spark of Vision-Language Intelligence: 2-Dimensional Autoregressive Transformer for Efficient Finegrained Image Generation

- Decision: Accept
- Scores: 6, 6, 6, 8, 5

## Abstract
This work tackles the information loss bottleneck of vector-quantization (VQ) autoregressive image generation by introducing a novel model architecture called the 2-Dimensional Autoregression (DnD) Transformer. The DnD-Transformer predicts more codes for an image by introducing a new autoregression direction, \textit{model depth}, along with the sequence length direction. Compared to traditional 1D autoregression and previous work utilizing similar 2D image decomposition such as RQ-Transformer, the DnD-Transformer is an end-to-end model that can generate higher quality images with the same backbone model size and sequence length, opening a new optimization perspective for autoregressive image generation. Furthermore, our experiments reveal that the DnD-Transformer's potential extends beyond generating natural images. It can even generate images with rich text and graphical elements in a self-supervised manner, demonstrating an understanding of these combined modalities. This has not been previously demonstrated for popular vision generative models such as diffusion models, showing a spark of vision-language intelligence when trained solely on images.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper addresses the problem of image modeling and generation using discrete latent representations and autoregressive (AR) sampling. The authors note that larger codebooks are need to improve visual quality but scaling up the codebook directly is difficult. They suggest a using multiple codes per token and adopt residual vector quantization (RVQ or just RQ) based on an earlier model called the RQ-Transformer.

They then present a creative approach for predicting the residual codes by adding a prediction head between different layers within the normal multi-layer transformer. This approach adds only a trivial amount of extra parameters and computational cost, and requires only minor changes to existing LLMs. Contrast with the RQ-Transformer that adds a new (albeit small) transformer, which is harder to integrate into existing LLM code. Through empirical validation, the authors show that their "DnD-Transformer" yields good generation results compared to RQ-Transformer, LlamaGen, and other methods.

Using RVQ to decompose a large codebook is not new, but adding prediction heads between the layers of the LLM transformer is. The authors show that this approach outperforms parallel prediction and vertical prediction (visualized in Fig. 5), two other approaches for predicting multiple codes from a single forward pass.

In addition to generation on ImageNet-256 evaluated using standard metrics (gFID, IS, etc.), the authors also introduce rOCR that evaluates an autoencoder in terms of how well text in a reconstructed image can be recognized. They show that larger depth values (more residual codes) improves this metric, as expected (see Table 1b). For generation, they measure perplexity using Qwen2.5-72B over text extracted with Qwen2-VL-72B and show that their approach performs better that a diffusion-based baseline (Fig. 6b). They argue that AR prediction is better suited to generating images of text compared to the "simultaneous" generation of diffusion models. This is where the "spark of vision-language intelligence" comes from: the DnD-transformer is trained on images of text and can then generate images of text with a few recognizable words and short phrases (see Fig. 7).

### Strengths
The main strength of the paper is the authors' creative solution to predicting multiple codes per token in an efficient and effective manner.  The approaches used in other works all have significant drawbacks:
 - use more tokens, which is computationally expensive
 - use a second transformer as in RQ-Transformer, which complicates the model, especially if you're building on top of an existing LLM
 - grow the codebook, which is memory-limited for VQ (though not FSQ or binary quantization as in MagVit v2 and MaskBit) and makes prediction more difficult
 - use multiple codes and predict them in parallel, which doesn't work very well (also discussed in this paper).

### Weaknesses
I see two main weaknesses in the paper. First, I'd like to see more evaluation of the DnD-Transformer in terms of sensitivity to layer indexes for the prediction heads both within an otherwise fixed architecture (e.g., stick with DnD-Transformer-XXXL and vary the indexes) and for smaller/larger models (e.g., if #heads == #layers, the smallest option, does the approach still work?). While the layer indexes are "just" a hyperparameter, it would be quite interesting to know if the approach is relatively robust to the layer choices or if there's a pattern. For example, for a fixed number of layers (and thus compute), you can ask how that compute should be used: do you want more layers before the first code is predicted? An even distribution across codes? Maybe the first code is relatively easy and you need successively more compute for later codes.

The second weakness deals with evaluation of generation results as a function of depth. If I'm interpreting the paper correctly, the ImageNet results in Table 2 use depth=2 (see the caption for Table 2), and the text-image generation results use depth=1 (see Section 4.4). Note that depth=1 is the baseline where no residuals are used (i.e., it's just an standard next-token predictor with one code per token). These low depth values seem to undermine the core contribution of the DnD-Transformer.

Note that the "Generation Results on arXiv-Image" sub-section does say that an "8-layer visual tokenizer and corresponding DnD-transformer..." If that means that depth=8, then I'm less concerned. Nonetheless, I'd like to see a chart showing gFID vs. depth (much like other VQVAE-based papers show gFID vs. codebook size). Figure 1b has the right structure, but it shows *reconstruction* metrics, which should always improve as depth increases. This does not always translate to generation quality.

### Questions
I'm not sure how to interpret the code usage reported in Table 1a vs. Figure 4a. The table shows 100% usage up to depth=8, but the chart shows code usage falling off with depth. Is this a mistake or are they showing something different?

A minor point (that's not actually a question): In Section 2.1 the paper says "each code has log N bits [of] information". It should be "log_2 N bits" or "log N nats".

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This work addresses the information loss bottleneck in vector-quantized (VQ) autoregressive image generation by introducing a novel model architecture, the 2-Dimensional Autoregression (DnD) Transformer. The DnD Transformer is an end-to-end model capable of generating higher-quality images while maintaining the same backbone model size and sequence length, presenting a fresh optimization perspective for autoregressive image generation. Experiments on ImageNet and rich-text images demonstrate that the DnD Transformer successfully generates detailed, high-quality images, highlighting its potential for advancing vision-and-language models with a new approach.

### Strengths
It’s intriguing to see the potential for training a vision-and-language model solely on images. When training such models using textbooks or other materials, preprocessing to associate images with the relevant text is often challenging. Training an LMM purely on images might offer a more principled and human-like learning approach.

### Weaknesses
#1. Compared to the RQ-Transformer paired with RQ-VAE, what are the benefits of this work? The proposed method appears largely similar, with no observed improvements over RQ-VAE.

#2. I believe the manuscript requires extensive revision. Some references are incomplete, with some citing Wikipedia, which is not a valid source. Furthermore, the comparison between DnD-Transformer and existing approaches, especially RQ-Transformer, lacks clarity and is not fully convincing.

#3. I believe many experiments in this paper may lead to misinterpretation, as the comparisons are not conducted under fair conditions. I suggest that the authors address my questions in #5 and #8 to ensure a more accurate comparison.

### Questions
#1. I'm not trying to pinpoint this assertion, but I don't personally buy this argument, since autoregressive image generation research was already very popular before the release of ChatGPT. Additionally, by 2022, the research community had already shifted to diffusion models. GLIDE (2021), Latent Diffusion (2022), DALL-E 2 (2022), and Imagen (2022) were all published before ChatGPT.

#2. The claim in the phrase “a spark of vision-language intelligence for the first time” appears to be overstated, especially given the limited scope of the experiments conducted. It is notable that AR-based image generation demonstrates strong performance in text rendering, particularly for documents, compared to diffusion models. However, can this really be considered a spark in vision-and-language intelligence?"

#3. How is the ICR of JPEG computed? Additionally, it would be preferable to include a proper reference from a primary source or technical documentation rather than Wikipedia.

#4. In section 2.2, the authors discuss the differences between the proposed approach and RQ-VAE, but I find the explanation somewhat unconvincing. Could you elaborate on the distinctions and explain why the newly proposed component might be expected to outperform RQ-VAE?

#5. In Table 1(a), code usage is reported at 100%. Did you apply any specific techniques to enhance code usage, such as restarting dead codes or similar methods?

#6. In Table 1(b), SDXL and SD3 are trained on ImageNet and should be considered zero-shot tokenizers. However, this isn’t indicated in the table, which leads to misinterpretation of the results.

#7. As I understand it, unlike RQ-Transformer, DnD-Transformer predicts codes along the depth dimension simultaneously. However, HQ-Transformer, a follow-up to RQ-Transformer, also explores predicting codes in this way. If my understanding is correct, it might be beneficial to include HQ-Transformer as a baseline for comparison.

#8. Regarding Figure 3, which dataset was used for the tokenizer in SD3? Did you use the original SD3 tokenizer? If so, I question whether this is a fair comparison, as open-source image generation models generally do not include OCR images in their datasets. If the claim is that DnD-Transformer performs well in generating rich-text images, it would be more appropriate to train a tokenizer specifically on rich-text images. I suggest training an LDM, including a tokenizer (such as continuous VAE f8), on rich-text images and then comparing DnD-Transformer with LDM under these conditions. In that case, I am not certain that DnD-Transformer would outperform LDM.

### Soundness
2

### Presentation
2

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
In this work, the authors introduce DnD Transformer, which predicts discrete image tokens in both sequence and depth direction. In sequence direction, the model is trained to generate tokens one by one as standard AR. In depth direction, the model generate one complete token in a residual-quantized manner. Experiments on ImageNet show competitive performance against baseline AR models. The model also show promising results on text-heavy image generation tasks.

### Strengths
1. The work investigates an interesting problem about improving autoregressive image generation on discrete tokens. 
2. The model achieves competitive performance on standard ImageNet benchmark. 
3. The model demonstrates capability of generating images with rich text and graphical elements.

### Weaknesses
1. Some implementation details are missing which affect the evaluation of proposed method.
2. Some baselines are missed on standard ImageNet generation tasks.
3. The model claims it shows a spark of vision-language intelligence by showing results on the rich-text image generation. However, it's a bit unclear to me whether these results lead to actual language understanding. It may beyond the scope of this work but it would be interesting to see how it performances in vision-language understanding tasks. The authors may consider being careful about the claim.



### Questions
1. It's not very clear about the gain from depth-wise autoregression. It would be good to have results with depth 1 or 3 on ImageNet reported as well. Also on rich-text image generation, DnD is trained with depth 1. How would the performance change if more depths are applied?
2. There're some AR-based image generation tasks that are not included in ImageNet256 benchmark. For example, VAR [1] curates a resolution-changing tokenizer for image generation. 
3. For rich-text image generations, how is SD3 implemented? Is it re-trained on tokenizer trained on rich-text datasets or finetuned with its original tokenizer? More details would help understand the performance gap between SD3 and DnD. 
4. Also, are there quantitative evaluations for rich-text image generation, like the rOCR used in evaluation of reconstruction performance?
5. The tokenizers are trained separately for ImageNet and rich-text datasets. Will tokenizers trained on merged datasets hurt the performance on either side?

References: 

[1] Visual Autoregressive Modeling: Scalable Image Generation via Next-Scale Prediction, https://arxiv.org/abs/2404.02905

### Soundness
2

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
The paper proposes a 2-Dimensional Autoregressive Transformer (DnD-Transformer) which, essentially, adds iterative refinement to visual token generation in the autoregressive regime. This iterative refinement is reminiscent of diffusion model inference (but not the same).

### Strengths
We know that iterative refinement is currently key in methods to generate images. For example, diffusion and rectified flow models which are SoTA have this iterative refinement quality. Embedding iterative refinement in the AR transformer block is a very interesting idea. Further, the paper presents ablations that show monotonically improving FID and other scores when the depth is higher, which is consistent with this claim. Also, they present results that rival SoTA diffusion models for class-to-image generation, which is very promising. The images they show in the paper are also convincing, with very high quality - and the interesting phenomenon of coherence in text generation even when trained without text-labels. Overall it's an interesting paper with a strong directive idea.

### Weaknesses
1. The paper needs objective data on FLOPs, training time, and inference speed. This is very important since adding the DnD-Transformer layers increases all of these. It needs comparisons to SoTA diffusion, rectified flow, and AR models. This is very important for judging the paper since increasing computation has to be balanced out by increased performance - and both need to be presented, not just one.
2. Only explores class-to-image and unconditional image generation.

### Questions
- My biggest question is on computational complexity. We need more clarification on the additional compute needed for different depths of DnD-Transformer layers, for both inference and training, and comparisons to other work.
- Is there any reason text-to-image is not explored?
- Can the method generalize to higher resolutions without exploding complexity?

My final score will depend on these clarifications.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces DnD aimed at addressing information loss in vector quantization decoder for AR transformer. 

The DnD-Transformer incorporates an additional depth dimension and extends sequence length, enabling it to predict a greater number of image encodings, which in turn leads to the generation of higher-quality images.

To my knowledge, it looks like introducing simplified diffusion-like process for each token while keep the AR schedule for the whole token sequence. 

The experimental results demonstrate the effectiveness of the proposed method.

### Strengths
1. The motivation behind DnD is well-founded, as addressing the effects introduced by VQ can lead to improvements in generation quality.
2. The author provides ablation studies to demonstrate the effectiveness of the proposed architecture.
3. DnD (almost) does not introduce an increase in the number of parameters compared to conventional architectures.

### Weaknesses
I still have the following concerns regarding this work:

1. The paper’s theoretical analysis is significantly lacking. The author’s explanation of how the depth dimension is used for prediction remains unclear. While the author attempts to explain the work through the lens of RQ, I find this explanation insufficient. Specifically, the paper does not adequately justify why a single transformer, as opposed to RQ's two independent modules, is sufficient for multi-depth code prediction. The lack of a clear rationale for this architectural choice is a significant gap in the theoretical underpinning of the work.

2. The experimental setup for the arxiv-images presented by the author raises some confusion. What exactly can similar experiments demonstrate? I had anticipated that **DnD would, through these experiments, show that the text in the generated images is coherent and carries semantic meaning.** However, based on the examples provided, the content appears to remain **disorganized**, with improvements observed only in terms of fidelity. The claim of achieving 'Vision-Language Intelligence' is not substantiated by the presented results, as the text within the generated images lacks semantic coherence and meaningful structure. The experiments do not demonstrate that the model understands or generates text with any level of contextual understanding.

3. Additionally, I find the decision to fine-tune models like SDXL or SD3 for **unconditional** generation tasks unclear. Why didn’t the author employ models like SiT or DiT to validate DnD’s effectiveness? This choice makes it difficult to isolate the impact of DnD, as the fine-tuned models may already possess strong generative capabilities. Using models specifically designed for unconditional generation would provide a more direct assessment of DnD's contribution.

4. I did not find sufficient evidence in the experiments to convincingly show a reduction in VQ loss. While there is an improvement in generation quality, it appears that this improvement is not solely attributable to VQ. The paper does not provide a clear comparison of reconstruction quality against baselines like RQ or VQ, making it difficult to assess whether the proposed method truly reduces VQ loss or simply benefits from the increased depth of the model. The repeated references to the 'DnD tokenizer' in Section 2.2 also raise questions about whether the method is actually improving the tokenizer itself, which is not clearly addressed in the experiments.

The following are some comments that do not influence my overall assessment:
1. In comparison to other contemporary works, e.g. [1], the author’s approach seems to represent a particular case.
2. I know it would be tough but could the author provide reconstructed results to better illustrate that the VQ loss has been significantly reduced?

### Questions
see weakness

In summary, I find this paper to be more focused on practical engineering experience. DnD enhances the performance of generative models with relatively low computational cost. However, there are notable issues regarding the theoretical analysis and clarity of the writing. As a result, my rating is a marginal rejection.

### Soundness
3

### Presentation
3

### Contribution
2
