# Transfusion: Predict the Next Token and Diffuse Images with One Multi-Modal Model

- Decision: Accept
- Avg Score: 7.60
- Scores: 8, 6, 8, 8, 8

## Abstract
We introduce Transfusion, a recipe for training a multi-modal model over discrete and continuous data.
Transfusion combines the language modeling loss function (next token prediction) with diffusion to train a single transformer over mixed-modality sequences.
We pretrain multiple Transfusion models up to 7B parameters from scratch on a mixture of text and image data, establishing scaling laws with respect to a variety of uni- and cross-modal benchmarks.
Our experiments show that Transfusion scales significantly better than quantizing images and training a language model over discrete image tokens.
By introducing modality-specific encoding and decoding layers, we can further improve the performance of Transfusion models, and even compress each image to just 16 patches.
We further demonstrate that scaling our Transfusion recipe to 7B parameters and 2T multi-modal tokens produces a model that can generate images and text on a par with similar scale diffusion models and language models, reaping the benefits of both worlds.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper proposes a multi-modal transformer model where text tokens are sampled auto regressively and image "tokens" are diffused in a VAE latent space.

### Strengths
- problem is well motivated
- method is simple and clear
- results are good
- abalations cover most of my questions

### Weaknesses
the method relies on a pre-trained VAE. It would have been nice to see an ablation done in pixel space or with some type of co-training scheme to avoid a 2-stage training process.

### Questions
The structure of the UNet is unclear to me. the paper says "since U-Net blocks contain bidirectional attention within, independent of the transformer’s attention mask, this gap is less pronounced when they are applied." What U-Net architecture uses bidirectional attention? Is the UNet applied to each patch independently, or is patching done after the U-Net?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper proposes Transfusion, a unified model for joint understanding and generation. During training, it incorporates CE loss for text learning and diffusion loss for image learning. In inference, it uses casual attention for autoregressive text generation and bidirectional attention for parallel image generation. Compared to Chameleon, Transfusion attains good performance for visual understanding and generation.

### Strengths
1. This paper verifies the feasibility combining different learning targets with one framework for respective understanding and generation.

2. It reveals the scaling performance comparing Transfusion and Chameleon, providing good insights for future works.

3. It provides detailed ablation study and analysis to demonstrate the effectiveness of each component.

### Weaknesses
-The comparison with previously published works only covered text-only & text-to-image tasks and didn't include their performances on image comprehension tasks(e.g. image captioning). 
An additional comparison for these tasks with previous multi-modal LLMs that process images differently(e.g. input-only with an external encoder like LLaVA, or image quantization like Chameleon) would support the effectiveness of Transfusion's approach.

-The paper lacks a detailed explanation of how the timestep embedding is incorporated into the denoising process, making it difficult to fully understand the implementation. This is crucial for reproducibility and further research.

-The training process involves calculating both AR loss and diffusion loss in a single forward pass using noised image latents alongside text tokens. This introduces a discrepancy, as the model infers with clear latents, which may lead to suboptimal performance, especially in image understanding tasks. The paper does not adequately address this training-inference discrepancy.

### Questions
See weakness

### Soundness
3

### Presentation
3

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
The paper introduces Transfusion, a novel approach for training a single unified model capable of understanding and generating both discrete and continuous modalities. The authors demonstrate that by combining the language modeling loss function (next token prediction) with diffusion, they can train a transformer model over mixed-modality sequences. This method allows for seamless integration of discrete text tokens and continuous image data, without the need for information loss through quantization.

### Strengths
1. Originality: The paper introduces a unique approach by combining language modeling and diffusion objectives over shared data and parameters. This method allows for the seamless generation of discrete and continuous modalities.

2. Quality: The paper demonstrates the effectiveness of the Transfusion model through extensive experiments and comparisons with existing methods. 

3. Clarity: The paper is well-structured, with clear explanations of the Transfusion method, its architecture, and the training objectives. 

4. Significance: The paper addresses a critical challenge in handling both discrete and continuous data modalities.

### Weaknesses
#### More experiments are encouraged.
1. Results on multimodal Understanding tasks are limited. For example, VQA, Summarization, VideoQA and etc.
2. I encourage the authors to scale up the model parameters or training data size (Scaling Law on Transfusion is very important), but I understand the computation resources on scaling law are huge. Thus, this is a minor issue.

#### Compare the technical differences of several recent works (e.g., Show-o, MIO, Emu3).

### Questions
As shown in Weaknesses.

### Soundness
4

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
The paper introduces Transfusion, a novel approach for training multi-modal models that effectively handle both discrete (text) and continuous (image) data. By combining next token prediction for text and diffusion for images within a single transformer architecture, Transfusion eliminates information loss associated with traditional quantization methods. The model was pretrained on a balanced dataset of text and images, utilizing modality-specific encoding and decoding layers to optimize performance. Experimental results demonstrate that Transfusion outperforms existing methods like Chameleon in various benchmarks, achieving significant efficiencies in both text-to-image and image-to-text generation tasks. The study concludes that Transfusion represents a significant advancement in creating integrated multi-modal generative models.

### Strengths
1. Innovative Framework: Transfusion introduces a novel approach that seamlessly combines text and image modalities, achieving impressive results in image generation and editing.
2. Robust Comparative Experiments: The paper includes comprehensive comparative analyses and detailed ablation studies that examine various dimensions, such as model architecture and parameters, providing strong evidence for the framework's effectiveness.
3. Clear and Fluid Writing: The writing is clear and the structure of the paper is well-organized, making it easy to follow the authors' arguments and findings.

### Weaknesses
Lack of demonstration of multi-modal understanding capabilities: While the paper focuses on image generation and editing capabilities, it does not present extensive benchmarks for the model’s general visual question answering (VQA) abilities. It would be beneficial to include benchmarks related to image understanding, such as VQAV2, SEED Bench and MMMU.

### Questions
same as weakness

### Soundness
3

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
4

### Summary
This paper explores how to bridge the modality gap to inject continuous image generation ability into discrete text-based LLMs by proposing a single transformer model trained with autoregressive modeling and diffusion loss simultaneously. This method of Transfusion avoids image discreteness and still enables input and output-level image tasks. By carefully designing attention masks and input formation, the transformer models text data by AR modeling with causal masking and generates images by denoising with bidirectional attention.

Compared to injecting image comprehension/generation ability by introducing discrete image tokens(Chameleon), the authors demonstrated their approach performs better in various scales in text-to-image generation, image captioning, and even text-only tasks. The large-scale model of Transfusion showed comparable performance to previously published large image generative models.

### Strengths
-They suggested a novel training and inference pipeline for a transformer that allows performing both AR and diffusion modeling with shared parameters.

-The manuscript contains extensive controlled experiments and ablation studies.

### Weaknesses
-The comparison with previously published works only covered text-only & text-to-image tasks and didn't include their performances on image comprehension tasks(e.g. image captioning). 
An additional comparison for these tasks with previous multi-modal LLMs that process images differently(e.g. input-only with an external encoder like LLaVA, or image quantization like Chameleon) would support the effectiveness of Transfusion's approach.

### Questions
-How does Transfusion take the embedding of noise timestep in the training/inference of image latent denoising process?

-In the training phase, the model calculates the AR loss and diffusion loss in one forward pass using text tokens and 'noised' image latent, which introduces unavoidable discrepancy when the model inference with clear latent. Wouldn't it be more accurate to calculate AR and diffusion loss separately in two model passes?


-Is there a reason that the COCO FID scores of StableDiffusion models are not in Table 6?

### Soundness
2

### Presentation
3

### Contribution
4
