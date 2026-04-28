# Image and Video Tokenization with Binary Spherical Quantization

- Decision: Accept
- Avg Score: 5.75
- Scores: 6, 5, 6, 6

## Abstract
We propose a new transformer-based image and video tokenizer with Binary Spherical Quantization (BSQ).
  BSQ projects the high-dimensional visual embedding to a lower-dimensional hypersphere and then applies binary quantization. 
  BSQ is (1) parameter-efficient without an explicit codebook, (2) scalable to arbitrary token dimensions, and (3) compact: compressing visual data by up to 100$\times$ with minimal distortion.
  Our tokenizer uses a transformer encoder and decoder with simple block-wise causal masking to support variable-length videos as input.
  The resulting BSQ-ViT achieves state-of-the-art visual reconstruction quality on image and video reconstruction benchmarks with 2.4$\times$ throughput compared to the best prior methods.
  Furthermore, by learning an autoregressive prior for adaptive arithmetic coding, BSQ-ViT achieves comparable results on video compression with state-of-the-art video compression standards.
  BSQ-ViT also enables masked language models to achieve competitive image synthesis quality to GAN- and diffusion-based methods.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes a novel image and video tokenizer, BSQ-ViT, based on Binary Spherical Quantization (BSQ) integrated with a transformer architecture. The proposed method achieves state-of-the-art performance in image and video reconstruction with significant improvements in computational efficiency. It introduces a block-wise causal masking for video tokenization, supports variable-length videos, and delivers competitive results in visual compression against standards like JPEG2000 and H.264. BSQ-ViT also shows promising results in image generation.

### Strengths
1. The paper presents an innovative quantization method (BSQ) that addresses the limitations of existing vector quantization approaches by offering a more efficient and scalable solution.
2. Extensive experiments on benchmarks such as ImageNet and UCF-101 demonstrate that BSQ-ViT significantly improves reconstruction quality, outperforming prior methods in terms of speed and fidelity.
3. The methodology is clearly explained with detailed comparisons to related work, and the theoretical basis of BSQ is well-supported with mathematical derivations and experimental validation.
4. BSQ-ViT's ability to handle both image and video tokenization and perform well on diverse tasks such as compression and generation showcases its generalizability.

### Weaknesses
1. While the transformer architecture is explored, the paper does not demonstrate the effectiveness of  BSQ within a CNN-based model.
2. The paper provides limited comparative data in video reconstruction, reducing the robustness of the comparison. Additionally, while block-wise causal attention is noted to impact performance, the study lacks experiments on BSQ without this causal masking. 
3. The reported image and video compression results are better on MS-SSIM, potentially  due to the inclusion of perceptual losses like LPIPS and GAN loss in the loss function. However, the lack of subjective evaluation metrics limits the strength of the comparison.
4. When BSQ and VQ use the same number of indexes, BSQ performs less effectively, and codebook utilization decreases as the bits increase.
5. In the ablation experiments, the reproduction of the LFQ, which serves as the basis for this work, is too poor in terms of behavior and code usage. And it is premature to conclude that LFQ is less compatible with transformer-based codecs.

### Questions
see the weaknesses.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper propose a transformer-based image and video tokenizer with Binary Spherical Quantization, which projects the high-dimensional embedding to lower-dimensional hypersphere and applies binary quantization. BSQ is parameter-efficient without an explicit codebook, scalable to token dimensions and compact. The experiments show that the proposed method achieves comparable compression performance with JPEG2000/WebP for images and H.264/H.265 for videos. And it enables masked language models to achieve competitive image synthesis quality to GAN and diffusion methods.

### Strengths
The Binary Spherical Quantization seems to show more effective training of the qunatization bottleneck. Analysis shows that the proposed method can provide fast speed and good performance.

### Weaknesses
- Lack of comparison at different bitrate range for visual compression results. Table 4 only provides BPP, PSNR and MS-SSIM for one bitrate point. However, visual compression tasks usually require showing a Rate-Distortion curves and compare at different bitrate points. Your can use BD-Rate metric for more reasonable comparison and analyze the results at low bitrate and high bitrate.

- Test settings for ablation study. Please provide more experiment setting details. In Table 5, do VQ, LFQ and BSQ use the same tokenizers? I observed that the metrics vary significantly across different quantization methods. To alleviate the influence of training and focus on the quantization bottleneck, it is better to: 1. use the same tokenizer 2. freeze the other network parts and only train the information bottleneck parts.

- Complexity. It is better to provide the computation complexity and encoding/decoding time for comparison.

### Questions
See the weakness part

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
3

### Summary
The paper introduces a transformer-based image and video tokenizer that uses Binary Spherical Quantization (BSQ). By projecting high-dimensional visual embeddings onto a lower-dimensional hypersphere and applying binary quantization, BSQ achieves a bounded quantization error. The authors demonstrate that the proposed BSQ outperforms previous methods in image and video reconstruction, image generation, and compression tasks.

### Strengths
1. The idea of projecting high-dimensional visual embeddings onto a lower-dimensional hypersphere is straightforward yet effective.

2. The motivation is clear, and the overall presentation is coherent and easy to follow. The experiments are comprehensive and provide convincing evidence to support the approach.

3. The BSQ-ViT model achieves competitive performance in diverse tasks such as image/video reconstruction, generation, and compression.

### Weaknesses
1. This method uses a transformer encoder and decoder, which limit the flexibility in resolution. How do the authors address this issue? Specifically, the fixed patch size and the global nature of the self-attention mechanism in the transformer architecture pose challenges when dealing with varying input resolutions. The authors should clarify how the model handles inputs that are not exact multiples of the patch size, and whether any padding or resizing is performed. Furthermore, the computational cost of the self-attention mechanism scales quadratically with the number of patches, which may become a bottleneck for high-resolution images or videos.

2. For image and video compression results, it would be beneficial to include an LPIPS comparison to assess perceptual performance. While PSNR and SSIM are useful metrics, they do not always correlate well with human perception of image quality. LPIPS, on the other hand, is designed to measure perceptual similarity between images, and would provide a more comprehensive evaluation of the compression method's performance. The lack of LPIPS results makes it difficult to assess the perceptual quality of the compressed images and videos.

3. There are a few minor issues. 1) In Eq. (7), $\hat{q}(c|u) = \frac{\exp(\tau c^{T}u)}{\sum_{c \in C_{BSQ}} \exp(\tau c^{T}u)}$ might need to be revised to $\hat{q}(c|u) = \frac{\exp(2 \tau c^{T}u)}{\sum_{c \in C_{BSQ}} \exp(2 \tau c^{T}u)}$ ? The current formulation might not be optimal for the binary spherical quantization. 2) On page 16, line 837, $\frac{e^{\tau u_d \hat{c}_d}}{e^{\tau u_d \hat{c}_d} + e^{\tau u_d \hat{c}_d}}$ should be corrected to $\frac{e^{\tau u_d \hat{c}_d}}{e^{\tau u_d \hat{c}_d} + e^{-\tau u_d \hat{c}_d}}$. This appears to be a typo in the denominator. 3) On page 3, line 118, it would be clearer to use different symbols for the downsample factor $q$ and the bottleneck module $q$. The use of the same symbol for two different concepts can lead to confusion.

### Questions
1. For image compression, why not use arithmetic coding to improve compression performance? Is intra-frame information used for video compression? If not, why not?

### Soundness
3

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
4

### Summary
This paper proposes a visual tokenizer based on a Vision Transformer and Binary Spherical Quantization (BSQ).   
The Transformer-based encoder-decoder leverages a block-wise causal mask and uses only visual tokens from the current or past timestamps for reconstruction.  
BSQ first projects the high-dimensional visual embedding of the encoder to a lower-dimensional hypersphere and then applies binary quantization.   
The transformer encoder, decoder, and BSQ are seamlessly integrated into the VQ-GAN framework and trained end-to-end.  

The proposed visual tokenizer has several advantages in trading off  visual reconstruction quality and computational efficiency and supporting variable-length input. Experiments on visual reconstruction and compression are conducted to verify the performance.

### Strengths
Visual tokenizers are critical for visual modeling. The proposed Binary Spherical Quantization (BSQ) for unified image and video tokenization is novel and important.  

Theoretical contribution is good. It is proved that the proposed BSQ has bounded quantization error.    

The manuscript is well written. BSQ is well placed agains previous VQ and LFQ.  

Extensive experiments on visual reconstruction, compression and generation show the better performance of BSQ.

### Weaknesses
My major concern is the fair comparison with VQ and LFQ. Though the ablation study is provided in  tab 5 with image reconstruction task on imagenet-1k, the resolution is only 128, and more tasks should be tested:     

It seems to me the results on image is not as obvious as video. For example, in image reconstruction (tab 1), the proposed method has best image quality, but the parameter number is also larger. It is better to add Ours-VQ for better comparison, as done in tab 2 for video reconstruction.  

In image compression, no VQ or LFQ based method is compared.     

For image generation in tab 3, more steps are used for BSQ, what if we use the same steps as VQ and LFQ?   

In L389, we get a direct comparison between VQ and BSQ, BSQ has more bits (18 vs 14) and the video quality is only comparable with VQ.   



Minor  
The derivation for eq. 13 is not given. Please provide a proof or give a reference here.  
There exist some typos in the derivations.  
In Line 878, the p shuld be Q.   
In line 886, the p should be q^hat.

### Questions
My major concerns in the weakness part can be summarized as the direct comparison between BSQ, VQ and LFQ on representative image and video tasks are not adequate. As a general tokenizer for image and video, it is important to make direct comparisons with strictly controlled variables.

### Soundness
3

### Presentation
3

### Contribution
3
