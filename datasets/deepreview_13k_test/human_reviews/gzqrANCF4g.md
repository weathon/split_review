# Language Model Beats Diffusion - Tokenizer is key to visual generation

- Decision: Accept
- Scores: 8, 8, 8

## Abstract
\vspace{-3mm}
While Large Language Models (LLMs) are the dominant models for generative tasks in language, they do not perform as well as diffusion models on image and video generation.
To effectively use LLMs for visual generation, one crucial component is the visual tokenizer that maps pixel-space inputs to discrete tokens appropriate for LLM learning.
In this paper, we introduce \modelname{}, a video tokenizer designed to generate concise and expressive tokens for both videos and images using a common token vocabulary.
Equipped with this new tokenizer, we show that LLMs outperform diffusion models on standard image and video generation benchmarks including ImageNet and Kinetics. 
In addition, we demonstrate that our tokenizer surpasses the previously top-performing video tokenizer on two more tasks: (1) video compression comparable to the next-generation video codec (VVC) according to human evaluations, and (2) learning effective representations for action recognition tasks.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes a novel visual tokenizer based on lookup-free quantization (LFQ). With the growth of the vocabulary size LFQ consistently improve both reconstruction and generation quality, which is in stark contrast with Vector Quantization (VQ) where an increased vocabulary size reduces reconstruction error but hurts generation results. The tokenizer can be integrated with MAGVIT and achieves state-of-the-art performance on video generation. The tokenizer can also improve video compression and video recognition.

### Strengths
1. Starting from an interesting finding that enlarging the vocabulary improves reconstruction quality but hurts generation results, the paper proposes solutions (LFQ) to tame both reconstruction and generation simultaneously.

2. A detailed study of architecture modifications that improves up MAGVIT supported by extensive ablations. 

3. The tokenizer is proved to benefit video generation, compression and recognition. It will potentially have a huge impact on the general audience of video understanding.

### Weaknesses
1. For video compression results, it would be better if there is a PSNR/LPIPS/MS-SSIM-bpp curve comparing the performance across different bpps.

2. In the video recognition setup, it seems unnecessary to detokenize the visual tokens back to pixels since BEVT and BEIT can work with tokenized input. I understand one of the main reasons is that the underlying recognition model is the ViViT which takes raw pixels as input (as stated in the draft). However, you may also have a comparison with BEVT.

### Questions
See weakness.

### Soundness
3 good

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper focuses on learning a video / image tokenizer to discretize video / images so that they can be modeled using a Language Model. They specifically introduce one innovation in this setting: A lookup free quantizer. They show that in this limit of using a large vocabulary and no lookup, the tokenizer reconstruction and LM generation quality both increase with vocabulary size. The authors also show that the learned tokenizer performs very well as a compression scheme.

### Strengths
The paper does a good job of motivating the core thesis of the paper: How to design a tokenizer for image / video? The authors also do a good job of presenting this idea to the uninitiated. It is also pretty clear that the work is significant to academia and industry given that it helps unify image generation with image understanding and natural language generation and understanding techniques. The ideas in the paper are well explained. The authors also do a thorough job of running experiments to substantiate many claims including numerous ablations. Some of the important technical insights like the lookup free quantizer (and in general lower dimensional code words) helping in generation quality are substantiated by experimental results

### Weaknesses
My main concern is the completeness of the exposition in the paper. The authors assume that the reader is familiar with the state of the art in video tokenization and details do get rather buried in the many “deltas” relative to the baseline. I do understand the space limitations but it might be helpful if the authors try to make the core system / model design more explicit. Lot of the ideas like factorization of the output space in the decoder (and associated weight tying) for example are just mentioned in passing.

### Questions
* The question “Why masked LM and not AR LM for image / video generation?” for evaluating the tokenizer was not clearly answered.
* No explicit definition of the objective for training the tokenizer (loss function)
* No mention of decoder in VQ-VAE and VQ-VAE loss used when we use no lookup
* More motivation needed on why the authors choose to use a causal encoder for tokenizer when doing masked LM for image / video generation
* It’s not clear why the authors tackle video generation if the aim was to understand the fundamentals of tokenization. It may be desirable for them to clearly motivate why they study videos and not images alone?
* It may be interesting for the reader to understand the computational complexity of both the tokenizer (encoder) and the detokenizer (decoder) and how they compare with video or audio codecs

### Soundness
3 good

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces a novel visual tokenizer designed to enhance large language models in producing high-quality images and videos. Experimental results show that, when integrated with the proposed tokenizer, LLM surpasses diffusion models in standard benchmarks such as ImageNet, UCF-101, and Kinetics-600. Additionally, the paper presents promising results in video compression and representation learning.

### Strengths
1.	This paper presents the first evidence of large language models surpassing diffusion models on the ImageNet benchmark.
2.	The paper proposes a novel lookup-free quantization approach, providing a promising direction for expanding vocabulary size in LLM-based visual generation.
3.	The motivation is clear, and the overall presentation is coherent and easy to follow.
4.	Good results on visual generation video compression, and video representation learning.

### Weaknesses
1.	While the presented method is tailored for masked LM, many of the prevailing and powerful LLMs, such as LLaMA [A], employ an autoregressive approach. Incorporating results from AR-LM would greatly enhance the paper's relevance to the community.
2.	In Table 4, despite the good action recognition performance showcased by the proposed method, it doesn't conclusively establish its efficacy as a viable self-supervised pre-training target. Notably, some pivotal baselines, like pixel colors and the image descriptor from MaskFeat [B], are missing.

[A] Touvron, H., Lavril, T., Izacard, G., Martinet, X., Lachaux, M. A., Lacroix, T., ... & Lample, G. Llama: Open and efficient foundation language models. arXiv preprint arXiv:2302.13971.

[B] Wei, C., Fan, H., Xie, S., Wu, C. Y., Yuille, A., & Feichtenhofer, C. Masked feature prediction for self-supervised visual pre-training. In CVPR 2022.

### Questions
1.	In Figure 1, it's highlighted that the VQ generation FID sees a pivotal change at a vocabulary size of 2^14, while the LFG generation FID consistently improves. I'm curious to understand how the LFG generation FID would respond to even larger vocabulary sizes.
2.	Regarding Table 3, what could be the reason behind the proposed method's PSNR and MS-SSIM values being inferior to those of the standard video codec?

### Soundness
3 good

### Presentation
3 good

### Contribution
4 excellent
