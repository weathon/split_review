# Meissonic: Revitalizing Masked Generative Transformers for Efficient High-Resolution Text-to-Image Synthesis

- Decision: Accept
- Scores: 6, 6, 6

## Abstract
We present Meissonic, which elevates non-autoregressive masked image modeling (MIM) text-to-image to a level comparable with state-of-the-art diffusion models like SDXL. By incorporating a comprehensive suite of architectural innovations, advanced positional encoding strategies, and optimized sampling conditions, Meissonic substantially improves MIM's performance and efficiency. Additionally, we leverage high-quality training data, integrate micro-conditions informed by human preference scores, and employ feature compression layers to further enhance image fidelity and resolution. Our model not only matches but often exceeds the performance of existing models like SDXL in generating high-quality, high-resolution images. Extensive experiments validate Meissonic's capabilities, demonstrating its potential as a new standard in text-to-image synthesis. We release a model checkpoint capable of producing $1024 \times 1024$ resolution images.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
- The paper presents Meissonic, a high-resolution, non-autoregressive masked image modeling (MIM) approach for text to image generation. 
- It introduces architectural innovations to elevate MIM’s performance to rival diffusion models like SDXL. 
- Its key advancements include a multi-modal transformer architecture, Rotary Position Encoding (RoPE), feature compression layers, and micro-conditions based on human preference scores. 
- It enables high-fidelity image generation at 1024×1024 resolution on 8GB VRAM. 
- The model is trained on high-quality datasets and achieves state-of-the-art results on various benchmarks.

### Strengths
- The integration of multi-modal transformers with single-modal refinements optimizes MIM for high-resolution synthesis and addresses the historical gap in resolution and quality compared to diffusion models.
- The model's efficiency is notable as it requires only 48 H100 GPU days which is far less than other high-resolution models like SDXL while achieving comparable performance.

### Weaknesses
 - Using CLIP text encoder makes Meissonic potentially less adept at handling complex text prompts compared to models using larger language models like T5 which could impact its effectiveness in scenarios demanding high text comprehension. e.g. generating images with visual texts.
- The reliance on high-quality datasets may limit the model's generalization in open-domain applications.

### Questions
Since Meissonic uses a CLIP text encoder, which might limit its effectiveness in scenarios demanding high text comprehension (e.g. generating images with visual texts), could the authors provide examples comparing Meissonic's performance on complex prompts versus simpler prompts? Also, would there be noticeable performance degradation if the model were applied to open-domain data?

### Soundness
3

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
5

### Summary
The paper scales up a masked image modeling (MIM) framework for professional-quality image generative model comparable to the diffusion-based SDXL. The key problems the authors have find in MIM framework is its low resolution constraint and persisting performance gap. The newly proposed model, Meissonic model incorporates efficient text encoder, mixed single-modal and multi-modal transformer backbone using rotary positional encoding, and curated training datasets. The final model performs comparable to SDXL in quality and exceeds efficiency in inference time and memory requirement.

### Strengths
- The presented method is lightweight, in terms of the number of parameters and the training time, lowering production cost of large scale image generative models.
- The model also have reduced inference time with lower GPU memory cost compared to SDXL.
- The training procedure is opened with transparency as shown in Figure 15.
- The model supports masked image editing and inpainting.

Overall, the proposed method in this manuscript can be regarded as a good industrial image generative model with production-ready quality.

### Weaknesses
The main concerns are in the presentation of the material. Although the model at this reported performance can contribute to the generative AI community, the current form of manuscript seems more like an industrial technical report than an academic article.

- Since the authors have claimed for supporting inpainting, outpainting, mask-free editing, and masked editing, there should be a comparison in both quantitative and qualitative way for each of the task in the manuscript. For now, the article only contains EMU-Edit scores with reduced number of columns--the original EMU-Edit contains five algorithmic ratings (CLIP_dir, CLIP_im, CLIP_out, L1, DINO) and two human ratings (Text Alignment, Image Faithfulness), measured in two different test sets (Emu Edit / MagicBrush). Also, the qualitative comparison is not shown in the paper, showing only the proposed method in Figure 6 and 7. Overall, this writing style makes the article more of an well-written industrial technical report than an academic paper. As a recommendation, there are many well-established detailed quantitative metrics such as masked image preservation and text alignment (e.g., PSNR/LPIPS/MSE as in BrushNet, Table 2), and overall generation quality (e.g., FID as in Table 2 of PQDiff), which can be applied to compare with, for example, SDXL.
- Maybe it is due to the intrinsic characteristics of MIM framework, but the inpainting in Figure 7 seems to change the non-masked regions of the image. This deformation should be measured in quantitative metrics such as in BrushNet.
- It would be better to have plots depicting how the generated quality changes by changing the number of iterations in the inference, or at least a recommendation of the number of inference steps of using the pre-trained model.
- I believe image demonstration from page 20 to the end is unnecessary and carry little information about the model. It is not bad to have a lot of demonstration images in a technical report, but there should be at least qualitative comparison between other models in order to have persuasive narrative. For example, generating random 5-16 images from the same text prompt without curation and show the diversity and the point of breaking (e.g., broken hands or limbs) can be visually compared with other large scale generative models such as SDXL-base, which is quoted multiple time throughout the manuscript.
- I would like to recommend adding details about training and inference algorithms. For example, the explanation of “micro controls” and architectural detail of “feature compression layers” is not described in appropriate level of details (what is chosen, how's the size of this controls, and how each component benefits the training, etc.). Moreover, even if the original idea is borrowed from previous papers, such information should be contained in the paper for completeness, e.g., how is 1D RoPE encoding used in this specific 2D MIM Transformer block?

### Questions
These are questions that are minor enough that do not count in the final scores.

- Does this model architecture supports DreamBooth-type fine-tuning for practical application?
- The success of U-Net-based architecture (e.g., SD, SDXL) partially relies on the strong controllabiliy gained from ControlNet. However, such I do not want to require the authors to provide the experimental results or detailed idea, but I wonder if they are planning to develop in this direction.
- I believe it would be great to have Figure 11 in the main manuscript, since this shows justification of changes made during the development of the proposed model.

### Soundness
3

### Presentation
3

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
The paper explores Masked Image Modeling (MIM), an non-autoregressive technique, and propose a new model named Messonic. Messonic poses a promising enhancement on MIM compared to its auto-regressive and diffusion-based counterparts. The keys to the improvement of Messonic are enhanced transformer architecture, advanced positional encoding and adding masking rate as a condition. The authors conduct extensive evaluations on Messonic to demonstrate its superiority.

### Strengths
### Motivation
- The paper shows a good motivation - MIM shows the potential capability to unify the language and vision modalities, and the paper attempts to bridge the gap between MIM and other popular image generation fashions. 
- The paper shares several interesting observations on the current MIMs, including architecture design, positional encoding, and masking rate as a condition. It then starts from those insights and implement effective components to gain improvement. 

### Method
- The proposed pipeline is straight-forward and seems effective. 
- It is an interesting finding that embedding original image resolution, crop coordinates, etc would be helpful for the stability of the training, as mentioned in Line 229 - Line 232. 
- The decomposition of training stages (Section 2.5) makes sense to me. It could work as a new procedure for other or future model training. 

### Experiments/Results
- The authors conduct extensive experiments and evaluations to demonstrate the performance of Messonic. 
- Messonic shows superiority on HPS benchmark, GenEval benchmark, and MPS scores. It shows competitive results with SDXL, while has a 2x smaller model size and transparent training costs (Table 1).
- Messonic also shows an economic expense of VRAM (i.e., 8GB). This demonstrates a promising value for customer level usage. 
- Messonic shows a good performance in Zero-shot I2I task, as shown in Table 6 and Figure 5.

### Writing/Delivery
The paper is well-written. The technical parts are clear and easy to understand.

### Weaknesses
I do not see a critical weakness from this paper. Some minor points:
- Messonic seems to be designed to match the auto-regressive manner in language models. The authors indicates it aims to unify language-vision models (Line 014). However, I do not see a strong evidence to show the current Messonic achieves this goal in the paper.
- The proposed approach is more driven from an "add-on" manner, where most of the components in Messonic are "borrowed" from other works. For example, multi-modal transformer backbone from the ADD paper, RoPE from Roformer, tokenization from VQVAE. The core contribution of the paper, therefore, seems to be a practice of choosing these components and empirical trials.

### Questions
1. It is interesting that the diverse micro conditions (Line 229 - Line 232) are helpful for the training stability (Line 134). From a high level perspective, why would these conditions help with the stability?
2. It is interesting to see that you choose to use a "lightweight" text encoder, CLIP (Line 210), instead of using LLM encoders or a mixed way like in SD3. Is there a reason or a hypothesis behind this choice, not just a "trial-and-error" experience?

### Soundness
3

### Presentation
4

### Contribution
2
