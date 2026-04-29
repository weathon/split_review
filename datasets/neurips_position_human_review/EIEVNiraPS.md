# Spiral Evolution of Visual World Model: Reclaiming Autoregression from the Diffusion Era

- Decision: Reject
- Scores: 8, 4, 3

## Abstract
Recent advances in video generation have been dominated by diffusion-based models, which produce high-quality, prompt-faithful sequences through holistic denoising. While this paradigm has achieved striking visual fidelity, it falls short for real-time, interactive applications that require frame-level responsiveness and causal coherence—cornerstones of practical world modeling. In this position paper, we advocate for a strategic return to autoregressive generation as the foundational architecture for building interactive world simulators. We argue that beyond offering faster inference, autoregressive models bring critical structural advantages: they naturally support predictive compression, enable causal disentanglement, and offer a more responsive mechanism for integrating control signals in dynamic settings. Unlike language-conditioned diffusion models, autoregression flexibly accommodates frame-wise control inputs such as camera motion and joint actions, making it ideally suited for agent-centric simulation. We further highlight emerging techniques and promising directions—including selective denoising, adaptive resolution, and postdictive coding—that address historical limitations of autoregression and unlock new levels of interactivity. We contend that embracing autoregression will be essential for developing practical, controllable, and truly intelligent world models.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper argues for a renewed focus on autoregressive architectures as the future of video generation and world modeling. The paper argues that while current diffusion models excel at visual fidelity and prompt adherence, their reliance on global optimization and heavy compute resources makes them unsuitable for real-time applications that demand fast, coherent, and causal generation. In contrast, the paper proposes that the research community revisit autoregressive architectures. These models offer more efficient underlying representations that support better temporal coherence and allow for fine-grained control during the generation process. Finally, the authors show that this approach could serve as a more viable path forward for building interactive, visual artificial intelligence systems in the future.

### Strengths
I think one of the core strengths of this paper is that it is structured very well – the paper introduces the concept of world models and then guides the reader through the history of autoregressive model architectures followed by the recent advances made in video diffusion models. This cohesive flow, coupled with strong literature references, allows the paper to develop its position supporting the revival of the autoregressive architecture by demonstrating to the readers why current approaches fall short and how recent developments can make these autoregressive architectures both viable and more powerful. Furthermore, I strongly believe that this perspective can be very useful to the computer vision community at NeurIPS, particularly in scaling future world/video models more efficiently.

### Weaknesses
One very minor weakness I’d like to point out is that, while the paper mentions postdictive coding—which involves refinement through revision—it may be somewhat confusing to readers. This is because it could be interpreted as endorsing bidirectional (temporal) interactions between representations, which appears to contradict traditional autoregressive architectures that strictly avoid relying on future representations. Some clarification on this point would be great.

### Questions
I think another interesting (though slightly tangential) question to consider is how switching to an autoregressive model architecture would affect model size compared to traditional diffusion models?

### Presentation
4

---

## Human Reviewer 2

### Rating
4

### Rating Number
4

### Confidence
4

### Summary
The paper advocates for a revival of autoregressive models in video generation, particularly for interactive world modeling, contending that while diffusion models achieve impressive visual fidelity and global coherence, they are ill-suited for real-time, control-intensive applications. Autoregressive approaches, with their sequential generation, provide several key advantages: they ensure causal coherence by aligning with natural temporal dynamics, enable fine-grained control and deliver real-time responsiveness—a critical requirement for embodied agents operating in dynamic environments. By leveraging these strengths, the authors argue that autoregressive models are better positioned to meet the demands of interactive and responsive world simulation compared to their diffusion-based counterparts.

### Strengths
- The paper presents a valid argument for revisiting autoregressive models in video generation, particularly for world modeling. This contrasts with the current dominance of diffusion models, offering a fresh perspective that aligns with the needs of real-time, causally coherent applications.

- The authors provide a thorough historical overview of video generation paradigms, from ConvRNNs to diffusion models, and critically evaluate their limitations. This contextual grounding strengthens their argument for an autoregressive renaissance.

### Weaknesses
While the advantages of autoregressive approaches are well-articulated, the discussion overlooks key innovations that have significantly improved diffusion models in the very areas where they were previously weak. For example: 

- real time models: techniques like latent consistency models (LCMs) [1] and distillation methods now enable near real-time generation without sacrificing quality.

The arguments for autoregressive models are valid, but the paper would benefit from an up-to-date comparisons with modern diffusion techniques.


[1] https://arxiv.org/abs/2310.04378#

### Questions
Please see weakness.

### Presentation
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper advocates revisiting the autoregressive paradigm as a foundation for building interactive world models. This paper summarizes some technical directions in the field of video generation from past ConvRNNs to nowadays diffusion models. By demonstrating some disadvantages of diffusion models for interactive video generation, this paper advocates that the research community should focus on autoregressive generation. Several advantages of autoregressive generation are analyzed to support the paper's position.

### Strengths
- This paper considers a widely-discussed problem, whether to use autoregressive or full-sequence generation in the context of interactive video generation. This topic is important and valuable to the research community.

### Weaknesses
- The figures used in this paper are borrowed from other papers, such as Figures 2~4, which raises concerns regarding the originality of the visual content.
- The evidence provided to support the paper's position is not sufficient or strong. This paper claims that autoregressive generation is better suited for interactive generation due to the time efficiency, while diffusion models require more time. However, for generating a long video, a diffusion model with a faster sampling technique (e.g., fastvideo) can surpass autoregressive generation, especially when a frame requires lots of tokens to reconstruct. The advantages of autoregressive generation demonstrated in section 5 should be further highlighted, and it should be explained clearly why other approaches fail to do so.
- The paper's position and writing are not clear. While criticizing diffusion models in the introduction section, the authors propose to leverage diffusion for next-frame prediction in section 6.1.
- No novel directions or insights are provided in this paper. All the discussed points have been mentioned in previous research, at least for me.

### Questions
The compounding error in autoregressive generation still poses a challenge for high-quality generation. Do you have any idea for addressing it?

### Presentation
2
