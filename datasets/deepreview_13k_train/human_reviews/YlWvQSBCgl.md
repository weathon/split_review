# Image Generation with Channel-wise Quantization

- Decision: Reject
- Scores: 5, 3, 5, 3

## Abstract
We present a novel image generation model with channel-wise quantization. Our method quantizes image feature along channel into discrete codes. Then based on the learned codes, our approach adopts masked-prediction paradigm for image generation. Compared with widely used spatial tokenizers, our channel-wise tokenizer has an efficient modeling for image structure and strong representational capacity. Besides, the codebook usage of our tokenizer can reach 100\% under different codebook size. Using the channel-wise tokenizer, our generation framework achieves competitive performances on various benchmarks of image generation. In particular, on ImageNet 256x256 benchmark, our method significantly improve baseline by improving Frechet inception distance (FID) to 1.87. Furthermore, we also validate the effectiveness of our proposed method on text-to-image generation.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper provides an interesting perspective on image compression through learning a vector quantized autoencoder. Typically, we tokenize images spatially. That is, every (i,j) for i over h and j over w within an hxwxc latent space, each position is mapped to a token in a learned codebook. In contrast, this paper proposes to tokenize along the channel dimension of the latent space within the AE. This results in tokens that capture the global image along a latent channel dimension. Results are conducted on class conditional and text conditional image synthesis with various ablations and analysis.

### Strengths
- The paper tackles an interesting approach to tokenize along the channel dimension within a VQ AE for images.
- The paper is well-structured and written.
- The approach is easy to understand and to follow.
- Comparison against many relevant models (albeit not exactly fairly if I understood correctly; see below for details).

### Weaknesses
My main concerns are regarding fair evaluation wrt compression ratios, more analysis on various token dimensions and exploration of usage of channel wise tokenization in downstream diffusion and AR tasks.

- Since each token in channel space captures complete global information, configurations such as [4,64,64] result in only four tokens of size 64x64 each, rather than 64x64 tokens of size 4. This impacts discussions on code embedding size and codebook use, which are misleading because they affect the compression ratio. I suggest comparing against a fixed compression budget with various compression ratios rather than focusing solely on code embedding sizes (which does not give the full picture).
- Adding to the above, the token count in Table 5 is potentially misleading, as the models use different compression ratios. If I understand correctly, the comparison is between VQAN using 4x16x16 tokens (4x256) and the proposed model with 256x16x16 tokens (256x256). The comparison is not apples to apples given the different number of tokens, and thus different compression ratios.
- The ablation study for token dimensions is incomplete. Experiments within the range [8, 256] are needed to understand scaling behavior better. It is unclear how the performance changes with varying token dimensions, and whether there is an optimal range.
- Tokenizing *global information* along the channel dimension implies a significant correlation among tokens, meaning each image is learned as a whole rather than in parts. Consequently, *C* tokens per image are kind of memorized, making it difficult to repurpose tokens for other images due to global encoding. This also explains the high overall usage of the codebook, as tokens are not easily reusable. The claim that tokens are not reusable needs further investigation and clarification.
- Adding codebook size, embedding dimensions, and compression ratios to the tables would improve comparability. The current tables lack crucial information for a complete understanding of the experimental setup and results.
- In Table 5, why is rFID significantly better while PSNR is worse, even though SSIM is better? I would expect a consistent trade-off between perceptual- and pixel-wise metrics. This discrepancy raises questions about the evaluation methodology and the interpretation of the results.
- Exploring channel-wise quantization in autoregressive (AR) or diffusion tasks could be insightful. I assume it may not perform as well for AR tasks, as the AR function would need to predict the entire global image in one step rather than progressively building it up from parts. The potential limitations of this approach in AR tasks should be explored.
- The claims regarding low similarity between channel tokens, efficient modeling of image structure, and strong representational capacity lack clear definition and verification. These claims need to be supported by more rigorous analysis and experiments.
- I have ignored going into details regarding quantitative results mainly because the issue of fair evaluation is not cleared yet. As of now, sometimes the model is better, sometimes worse, and it is unclear why and when one would want to choose this method over the spatial tokenization.

### Questions
NA

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper presents an alternative to standard VQ-VAE, which typically quantizes each spatial position as a token. Instead, this work quantizes image features along the channel dimension into discrete codes.

For comparison, in a standard VQ-VAE with a final feature dimension of C*H*W, there would be H*W tokens, whereas this work produces C tokens.

Advantages:
1. The paper is clearly written and easy to understand
2. The metrics appear reasonable

Disadvantages:
1. Channel-wise quantization lacks theoretical justification and Intuitive rationality.
   Without spatial-based quantization, the model training appears to lose its causal nature
2. As the model scales up, the number of tokens would need to increase, potentially making learning more difficult
3. The resulting tokenizer becomes incompatible when image resolution changes

I believe the motivation behind this idea is fundamentally flawed, which leads to several issues:
- Limited generalizability
- Sequence length problems
- Modeling methodology concerns

Therefore, I lean towards a negative assessment of this work.

### Strengths
Advantages:
1. The paper is clearly written and easy to understand
2. The metrics appear reasonable

### Weaknesses
Disadvantages:
1. Channel-wise quantization lacks theoretical justification and Intuitive rationality. Without spatial-based quantization, the model training appears to lose its causal nature. Specifically, the channel-wise quantization approach does not inherently preserve the spatial relationships within the image, which are crucial for many image generation tasks. The lack of spatial awareness in the quantization process could lead to difficulties in generating coherent and spatially consistent images. Furthermore, the channel-wise approach may not effectively capture local texture and patterns, which are often encoded in the spatial arrangement of features.
2. As the model scales up, the number of tokens would need to increase, potentially making learning more difficult. This is because the number of channels in a feature map is typically fixed, and increasing the number of tokens would require a more complex codebook and potentially a larger model. This could lead to increased computational costs and training instability. The fixed number of channels also limits the model's ability to adapt to different levels of detail, as it cannot dynamically adjust the number of tokens based on the complexity of the input image.
3. The resulting tokenizer becomes incompatible when image resolution changes. This is a significant limitation as it requires retraining the tokenizer for each new resolution, making it less flexible and adaptable than spatial tokenizers. The inability to generalize across different resolutions hinders the practical applicability of the method, as it cannot be easily applied to a wide range of image datasets or real-world scenarios where images may have varying resolutions.

I believe the motivation behind this idea is fundamentally flawed, which leads to several issues:
- Limited generalizability
- Sequence length problems
- Modeling methodology concerns

Therefore, I lean towards a negative assessment of this work.

### Questions
see above

### Soundness
1

### Presentation
3

### Contribution
1

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
In this paper, the authors propose a new image tokenization method called channel-wise quantization, which quantizes image feature along channel. Then, based on the learned tokenizer, the authors use masked-prediction paradigm similar to MaskGIT to generate images. Experiments show that the proposed method achieves competitive performances compared to other image tokenizers and generative models. Besides, the proposed method can reaches 100% codebook usage under different codebook size.

### Strengths
+ The writing is clear and easy to follow.
+ The idea of channel-wise quantization is novel and interesting.
+ The reconstruction ability (especially rFID and SSIM) is greatly improved compared to spatial tokenizers.

### Weaknesses
 - The motivation of proposing channel-wise quantization is not very strong to me. While spatial tokenizers often suffer from low codebook usage and reduced code embedding dimension limits expressive ability, it's unclear how these issues lead to the design of channel-wise quantization.

- The paper lacks a detailed analysis of how the channel-wise tokenizer behaves differently from spatial tokenizers. For example, the authors claim that channel-wise tokens capture both global structures and local details, but there are no direct experiments to support this. It would be interesting if the authors could visualize the learned channel-wise tokens and discuss each channel's representation, so that we can have a deeper understanding of the channel-wise tokenizer.

- The authors attribute the 100% codebook usage to the nature of channel-wise quantization. However, I note that entropy regularization, which is known to be helpful for increasing codebook usage, is adopted in codebook learning. Additionally, the compared method LlamaGen did not use entropy regularization. Thus, I'm not sure if channel-wise quantization is the main factor behind high codebook usage.

### Questions
+ As mentioned in weaknesses part, will the channel-wise quantization still reach 100% codebook usage without entropy regularization?

+ What does a channel token typically represent? Is it possible to visualize the learned channel tokens?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This work presents a novel image generation model that utilizes channel-wise quantization to convert image features into discrete codes along the channel dimension, adopting a masked prediction paradigm for image generation. This approach offers efficient modeling of image structures and strong representational capacity, outperforming or matching state-of-the-art methods on the ImageNet benchmark. The authors also performed the text-to-image generation and demonstrated transferability to text-to-image generation on the COCO dataset. The contributions of this work include a simple yet effective visual tokenizer with 100% codebook usage and a generation framework based on channel-wise quantization for image generation tasks.

### Strengths
This paper is easy to follow and includes comprehensive experiments to demonstrate the effectiveness of the proposed method. It proposes novel channel-wise quantization, which offers efficient modeling of image structures and strong representational capacity. It also proposed a simple yet effective tokenizer with 100% codebook usage. These features enable the whole image generation framework to achieve superior or comparable performance to state-of-the-art methods across various image generation tasks.

### Weaknesses
1) This paper's biggest contribution is proposing a channel-wise quantization for image generation. However, channel-wise quantization is widely used in various applications, such as classification [a], LLM compression [b], and super-resolution [c]. The novelty of applying channel-wise quantization to image generation is not sufficiently justified, especially considering its existing use in similar contexts where the goal is to reduce redundancy in feature maps.

2) The paper lacks a comparison with the Stable Diffusion (SD) series, such as SD1.5, SDXL and SD2.1. These models represent state-of-the-art in image generation and should be included for a comprehensive evaluation. The absence of this comparison makes it difficult to assess the true performance of the proposed method relative to established benchmarks.

3) The experimental results are limited to a maximum resolution of 512x512. More experimental results about high-resolution image generation (e.g., 1024x1024 or higher) should be provided to demonstrate the effectiveness of the proposed method in generating high-fidelity images. The current results do not fully explore the method's capabilities in high-resolution scenarios.

4) The authors did not evaluate the text-image alignment between the text prompts and the synthesized images. This is a critical aspect of text-to-image generation models and should be assessed using appropriate metrics.

5) The proposed channel-wise tokenizer is limited to one specific image resolution, which restricts its general applicability. A more versatile tokenizer algorithm that can be adapted to various image resolutions would significantly enhance the contribution of this work. The current design limits the practical use of the method.

6) The authors only conducted experiments on MS-COCO and ImageNet datasets with the image resolution 256*256. This limited dataset scope restricts the generalizability of the findings and does not fully validate the method's robustness.

7) Marginal performance. Compared with VAR, the proposed method only shows very marginal performance improvement (or even a slight performance drop) under the same experimental setting: similar network parameters and inference step from Table 2.

Minor issues:

1) The best results under the same setting in Table 2 should be bold. 

2) Figure 2 is a little blur and seems that some parts are screenshots of other images.

### Questions
What is the purpose of the image generation? 

Only evaluating the image quality of the synthesized images based on evaluation metrics like FID, SSIM and PSNR is not enough. Can the synthesized images promote the downstream visual perception performance such as classification?

### Soundness
2

### Presentation
2

### Contribution
2
