# Lumina-mGPT: Illuminate Flexible Photorealistic Text-to-Image Generation with Multimodal Generative Pretraining

- Decision: Reject
- Scores: 6, 8, 6, 5, 5

## Abstract
We present \ours, a family of multimodal autoregressive models capable of various vision and language tasks, particularly excelling in generating flexible photorealistic images from text descriptions. Unlike existing autoregressive image generation approaches, \ours employs a pretrained decoder-only transformer as a unified framework for modeling multimodal token sequences. Our key insight is that a simple decoder-only transformer with \textit{\textbf{m}ultimodal \textbf{G}enerative \textbf{P}re\textbf{T}raining} (mGPT), utilizing the next-token prediction objective on massive interleaved text-image sequences, can learn broad and general multimodal capabilities, thereby illuminating photorealistic text-to-image generation. Building on these pretrained models, we propose \textit{Flexible Progressive Supervised Finetuning} (FP-SFT) on high-quality image-text pairs to fully unlock their potential for high-aesthetic image synthesis at any resolution while maintaining their general multimodal capabilities. Furthermore, we introduce \textit{Ominiponent Supervised Finetuning} (Omni-SFT), transforming \ours into a foundation model that seamlessly achieves omnipotent task unification. The resulting model demonstrates versatile multimodal capabilities, including visual generation tasks like flexible text-to-image generation and controllable generation, visual recognition tasks like segmentation and depth estimation, and vision-language tasks like multi-turn visual question answering. Additionally, we analyze the differences and similarities between diffusion-based and autoregressive methods in a direct comparison.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This work presents Lumina-mGPT, a series of autoregressive models for multimodal understanding and generation. With a pre-trained decoder-only transformer, Lumina-mGPT allows for a unified framework for multi-model modeling. The work shows that multimodal generative pretraining is the key towards general multimodal capabilities. Furthermore, flexible progressive supervised fine-tuning, as proposed by the work, allows high-aesthetic image generation at flexible resolutions. Finally, omnipotent supervised fine-tuning enables Lumina-mGPT to achieve task unification in visual generation and understanding.

### Strengths
* The proposed Unambiguous image Representation, when used with Flexible Progressive Supervised Finetuning (FP-SFT), allows the method to generate images of varying resolutions.
* While prior method Chameleon can only perform vision-language and text-only tasks, Lumina-mGPT achieves visual recognition tasks (e.g., segmentation, depth prediction) and controllable generation as well as image editing, which makes Lumina-mGPT a unified model for various downstream applications.
* The performance on VQA benchmarks significantly improves over baseline Chameleon, demonstrating the effectiveness of the proposed model.

### Weaknesses
 * The contributions of this work is not clearly described. While the work claims mGPT to be a key insight, the importance of mGPT is not discovered by the work, as the mGPT model is adapted from Chameleon. The difference is that Lumina-mGPT performs fine-tuning on Chameleon.
* The proposed Unambiguous image Representation (Uni-Rep) is only applied at the supervised fine-tuning stage. This creates gaps between the image representation in pre-training and fine-tuning. Specifically, the pre-training of the sequence model is done with fixed image resolution, while UniRep is introduced only during fine-tuning to allow for variable image resolutions. This discrepancy introduces a potential domain shift that could negatively impact performance. An ablation study is needed to quantify the impact of this gap by comparing the performance of a model trained with and without UniRep for fixed resolution generation.
* The method claims that baseline Chameleon shows degraded visual quality compared to diffusion methods (L242-244). However, this work does not perform quantitative evaluations on the quality of the generated images to illustrate whether the method is able to overcome this limitation. Metrics such as FID and/or results on benchmarks such as T2I-CompBench [1] are needed to show the performance improvements against other related works.
* No comparisons are provided with text-only LLMs on text-only benchmarks such as MMLU. The example dialogues are insufficient in evaluating the model's capabilities in text-only tasks.
* No human evaluation is performed to assess the quality of multi-modal generation.

### Questions
The comparisons and evaluations are insufficient for the work. Specifically, a few questions are still to be addressed:
* How does Lumina-mGPT compare with diffusion-based methods in terms of image generation?
* How does Lumina-mGPT perform on text-only tasks, comparing with other text-only LLMs?

### Soundness
2

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
This paper introduces Lumina-mGPT, a multimodal autoregressive model that excels in generating photorealistic images from textual descriptions, as well as performing a variety of other vision and language tasks. Built on a pre-trained decoder-only transformer architecture, the model adeptly processes multimodal token sequences. Key innovations of Lumina-mGPT include Effective Multimodal Generative Pretraining (mGPT) using extensive interleaved text-image datasets, Flexible Progressive Supervised Fine-tuning (FP-SFT), and Omnipotent Supervised Finetuning (Omni-SFT). These developments enable the model to produce images of varying resolutions and accommodate a broad spectrum of vision-language tasks, marking a notable advancement in flexibility and task integration over traditional autoregressive approaches.

### Strengths
+ Omni-SFT within Lumina-mGPT effectively unifies a diverse array of tasks within a single model framework, demonstrating its extensive multitasking capabilities across various complex applications such as text-to-image synthesis, image captioning, image editing, spatial-conditional image generation, and more.
+ The use of mGPT for initial training, followed by sophisticated fine-tuning strategies like FP-SFT and Omni-SFT, establishes a solid foundation for generating high-quality, photorealistic images while adeptly handling a wide range of multimodal tasks.
+ Lumina-mGPT exhibits exceptional flexibility in generating images across different resolutions and aspect ratios—a significant advantage over many existing models.
+ By effectively bridging the gap between autoregressive and diffusion methods, Lumina-mGPT achieves remarkable visual aesthetics and detailed image rendering without the need for cascading models,
+ The paper ingeniously integrates various advanced concepts from the literature and existing models to enhance the training and inference capabilities of Lumina-mGPT. This includes adopting classifier guidance from diffusion models and stabilization techniques used in large language models, which collectively contribute to the robustness and efficiency of the framework.

### Weaknesses
 - The paper falls short in providing comprehensive comparative metrics, such as FID scores, with only limited comparisons featured in Table 2 against the Chameleon model. A more extensive range of benchmarking against current state-of-the-art (SoTA) models is essential to objectively evaluate the model’s performance and its advancements over existing methodologies. Including a broader set of metrics would significantly clarify the model's positioning and contribution within the broader field.
- Although the paper showcases zero-shot capabilities in enhancing visual details, it only offers qualitative results. Incorporating quantitative evaluations would provide a more robust comparison against other models and substantiate the claimed improvements. Specifically, metrics such as PSNR or SSIM on the reconstructed images would be beneficial.
- While Omni-SFT demonstrates the model's capability to handle diverse tasks, the absence of quantitative results in a controlled evaluation test limits the understanding of its performance, especially in comparison to specialized models. Providing such data, perhaps using established benchmarks for tasks like image captioning or editing, would help gauge the effectiveness of Omni-SFT and its relative performance across different tasks.
- The paper highlights the performance benefits of Omni-SFT fine-tuning on top of the Lumina model but lacks a comparative analysis with scenarios where Omni-SFT is fine-tuned starting from the initial mGPT. A direct comparison would help validate the advantage of transitioning from Lumina to Omni for task unification, ensuring that this methodological choice yields tangible benefits.

### Questions
- In the appendix, you observe that *"with the CFG increasing, the quality of generated images improves, proving the effectiveness of the classifier-free guidance in this context."*. This finding appears to contrast with typical outcomes in diffusion models, where increasing the CFG beyond a certain threshold often results in diminished image quality. Could you elucidate the reasons behind this differing impact of CFG in your model compared to traditional diffusion models?

### Soundness
3

### Presentation
4

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
The paper "Lumina-mGPT" introduces a multimodal autoregressive model designed for flexible, photorealistic image generation from text, leveraging a decoder-only transformer and multimodal Generative PreTraining (mGPT). Lumina-mGPT unifies text and image processing within a single framework, using Flexible Progressive Supervised Finetuning (FP-SFT) for high-resolution, flexible-aspect image synthesis, and Omnipotent Supervised Finetuning (Omni-SFT) for a wide range of vision-language tasks, including segmentation and multiview generation. The model’s novel unambiguous image representation enhances its ability to generate variable-resolution images, and extensive multimodal pretraining enables impressive zero-shot capabilities across visual tasks.

### Strengths
The paper presents a systematic approach to fine-tuning through Flexible Progressive Supervised Fine-Tuning (FP-SFT) and Omnipotent Supervised Fine-Tuning (Omni-SFT). These methods are well-supported by empirical results, demonstrating that Lumina-mGPT generates high-quality, high-resolution images across various aspect ratios. Additionally, an extensive evaluation of zero-shot performance and attention visualizations offers insights into the model's generalizability and internal mechanisms.

The paper is well-organized and clearly articulates its goals, methodology, and findings. The authors effectively communicate complex technical concepts, ensuring that each design choice—such as the unambiguous image representation—is both motivated and illustrated, enhancing readability. While certain sections, such as the detailed explanations of supervised fine-tuning processes, may require technical background to fully appreciate, the overall clarity remains high.

Lumina-mGPT's primary contribution lies in bridging the gap between autoregressive (AR) models and diffusion-based image quality, with its open-source release further amplifying its impact.

### Weaknesses
The introduction and abstract emphasize the decoder-only architecture for text and image as a novel contribution, which is strange, given that several prior works—some even cited in this paper—have already employed similar architectures.

The effectiveness of Flexible Progressive Supervised Finetuning (FP-SFT) would benefit from more detailed analysis, especially around why certain parameter settings or resolution stages were chosen. Currently, the progressive finetuning approach appears somewhat arbitrary, and an ablation study exploring different finetuning configurations or showing specific benefits per stage would substantiate these choices.

### Questions
The Large World Model (LWM) paper introduces a multimodal autoregressive model capable of processing extensive sequences of video and book data, with a context length of millions of tokens. This enables it to perform tasks such as language understanding, image analysis, and video generation. In contrast, the Lumina-mGPT model is focused specifically on photorealistic text-to-image generation. Is this understanding accurate? Based on reading both papers, LWM appears to use a less effective VQ-VAE compared to Lumina-mGPT's VQ tokenizers; does this difference explain the variation in visual quality? Could the authors provide an analysis to identify the areas contributing the most to these performance gains?

While Lumina-mGPT demonstrates impressive performance across various tasks, additional examples in less conventional vision-language settings would help illustrate its adaptability and generalization. Could the authors provide results or comparisons on more challenging benchmarks or diverse vision-language tasks (e.g., object counting, spatial reasoning) that may better highlight Lumina-mGPT's strengths and weaknesses across the multimodal spectrum?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper proposes to finetune an autoregressive decoder-only model (initialized from Meta's Chameleon model) for image generation based on multimodal inputs. For this the paper initializes their model from the Chameleon checkpoint and finetunes the model for image generation and also adds additional multimodal tasks (e.g.,image editing, dense predictions like segmentation maps, spatial conditions, VQA, etc) to the training. The resulting model can generate photorealistic images in various aspect ratios and can also perform the multimodal tasks it was finetuned on.

### Strengths
The paper finetunes the Chamaleon model to add image generation and other multimodal tasks to the model. The original Chameleon model can also do this but the image generation model was not publicly released.
The paper also proposes a simple representation of the images to support various aspect ratios by adding information about height and width, as well as end-of-line tokens after each row of (latent) pixels.
The finetuning on multimodal tasks shows that the training approach also generalizes to tasks besides image generation.

### Weaknesses
There is limited novelty in the paper. Most of the work seems to come from the original Chameleon checkpoint with the image training being a relatively straight-forward finetuning approach.

The finetuning with multimodal tasks is also a relatively straight forward extension and other works have already shown that AR vision models can handle many different tasks and also can perform in-context learning (e.g., Sequential Modeling Enables Scalable Learning for
Large Vision Models, CVPR 2024).

Overall it's not clear to me what exactly is novel and different from Chameleon or other large VLMs.

### Questions
What exactly is different about Lumina-mGPT from other large VLMs? Is the training different? Is there some novelty in how the training is done?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces a large multimodal autoregressive model, Lumina-mGPT, with a particular focus on its text-to-image (T2I) generation capability after fine-tuning. The model leverages pre-trained token representations from Chameleon 7B and 30B (Meta) and incorporates two fine-tuning techniques—Flexible Progressive Supervised Fine-tuning (FP-SFT) and Omnipotent Supervised Fine-tuning (Omni-SFT)—to adapt the model for T2I tasks and multiple vision and language tasks.

Overall, I think this paper has both clear strengths and limitations, which I will detail in my comments below.

### Strengths
- The proposed model achieves very good image generation results on the T2I task in the AR paradigm, as stated as one of the main contributions.
- The paper presents a rather detailed discussion of the implementations and fine-tuning recipes, including failure cases, which is appreciated.
- This work is open-source, with the promise to release the model checkpoints and codes, thus, it may be of interest to the researchers in the open-source community on large models.

### Weaknesses
 - While this may sound like a platitude, I must note that there is limited novelty in this work. As the authors acknowledge, a well-trained token representation for multimodal data is crucial in this setting, motivating their choice of Chameleon. The proposed fine-tuning techniques, however, follow commonly used methods and widely accepted design choices. Overall, the work reads very much like a technical report to me. However, I recognize that both intellectually novel approaches and engineering-heavy work have their place in the community. That being said, I am fine with either as long as the design choices are well-justified. 
- A more concerning issue is the claim of the “emergent zero-shot capabilities.” While zero-shot is indeed becoming something of a buzzword, I don’t believe the observed reconstruction ability within the VQ-VAE module qualifies as true “zero-shot.” This term should be defined and examined rigorously, with careful attention to the training and inference data at different stages, especially within complex frameworks that combine multiple large models. The observation that the model's reconstruction sometimes surpasses the original VQ-VAE reconstruction is interesting, but it is not unique to this model and has been observed in other generative models using discrete representations. This phenomenon likely stems from the properties of the VQ-VAE latent space itself, rather than any specific innovation in the proposed model architecture or training method. The claim of zero-shot capability is therefore misleading and should be removed or significantly rephrased to reflect the existing literature on VQ-VAE and similar models.
- While I appreciate the discussion on failure cases, Figure 6 actually highlights that this work does not address the fundamental challenges in generative modeling—specifically, the limitations in distribution learning with limited data. In other words, much of the performance boost appears to come from improved pre-trained data representations and high-quality, sufficient data during fine-tuning, rather than advancements in the model’s actual ability to learn distributions.

### Questions
Please see the questions from my review comments above. Overall, my preliminary rating is based on the pros and cons of the current work.

### Soundness
2

### Presentation
3

### Contribution
2
