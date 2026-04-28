# CtrlSynth: Controllable Image Text Synthesis for Data-Efficient Multimodal Learning

- Decision: Reject
- Avg Score: 5.00
- Scores: 6, 3, 6, 5

## Abstract
Pretraining robust vision or multimodal foundation models (\eg, CLIP) relies on large-scale datasets that may be noisy, potentially misaligned, and have long-tail distributions. Previous works have shown promising results in augmenting datasets by generating synthetic samples. However, they only support domain-specific ad hoc use cases (\eg, either image or text only, but not both), and are limited in data diversity due to a lack of fine-grained control over the synthesis process. 
    In this paper, we design a \emph{controllable} image-text synthesis pipeline, \sys, for data-efficient and robust multimodal learning. The key idea is to decompose the visual semantics of an image into basic elements, apply user-specified control policies (\eg, remove, add, or replace operations), and recompose them to synthesize images or texts. The decompose and recompose feature in \sys allows users to control data synthesis in a fine-grained manner by defining customized control policies to manipulate the basic elements. \sys leverages the capabilities of pretrained foundation models such as large language models or diffusion models to reason and recompose basic elements such that synthetic samples are natural and composed in diverse ways. \sys is a closed-loop, training-free, and modular framework, making it easy to support different pretrained models. With extensive experiments on 31 datasets spanning different vision and vision-language tasks, we show that \sys substantially improves zero-shot classification, image-text retrieval, and compositional reasoning performance of CLIP models.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors propose a controllable image-text generation pipeline that can augment data to improve CLIPs image retrieval, classification, and compositional performance. Specifically, they leverage strong vision models to tag images with objects and attributes, use the knowledge in language models to create new variations of the captions, and use diffusion models to generate images based on the new captions as prompts.

### Strengths
- The pipeline can be thought of as a way to distill knowledge from the language models and stable diffusion models to augment the dataset of CLIP. This is an interesting way to inject new information in synthetic data. 

- The results are good, demonstrating improvements over CLIP while maintaining the amount of data it sees since the fix the number of iterations and just change the proportions of real vs their synthetic data.

### Weaknesses
 -  They say that the language model takes an instruction on how to generate a caption given the visual tags. They show some examples in Appendix A1. The instructions don't mention any editing, it mostly just says to describe the image better. In that case, do the gains come from some hallucination in the LLM caption that makes varied images?

- Have the authors tried any other variation of editing instructions? Is there any analysis on the kinds of image editing prompted by the text that improve performance more? Are there specific prompts that serve as better negatives when tuning the CLIP contrastive loss?

- There are other works that edit images based on text instructions like instruct pic to pic, magic brush etc. It might have been nice to see to see if editing certain things in images based on the LLM prompts is better than just using SD to generate since SD can often lack accuracy in generating the correct attribute object relation compositions. 

- Nit: There are several works that either generate synthetic images based on the dataset they want to target (https://arxiv.org/pdf/2406.05184), or for cross domain retrieval (https://arxiv.org/pdf/2401.00420). A discussion for comparison could be nice.

### Questions
See above.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper proposes CtrlSynth, a controllable image-text synthesis pipeline for data-efficient multimodal training. Addressing limitations in existing large-scale datasets that are often noisy and misaligned, CtrlSynth enables fine-grained control by decomposing images into basic elements and applying user-specified modifications to synthesize new data. This training-free and flexible pipeline can work with different models and supports closed-loop synthesis (image to text and vice versa). The proposed method also boosts the performance of multimodal model training.

### Strengths
- The paper focuses on noise and misalignment in the large-scale image-text datasets, which is a critical challenge in multimodal learning.
- The paper introduces an innovative approach that emphasizes fine-grained control, utilizing generative models to decompose and refine images and texts at a detailed level. Notably, it is training-free and suited for integration with different pre-trained generative models.
- The experiments presented in the paper show that the proposed method improves downstream performances of multimodal models.

### Weaknesses
The paper, while contributing valuable ideas, has several notable weaknesses that are significant and need to be addressed.

### Methodological Weaknesses
- The proposed pipeline shares significant similarities with GenArtist[1] on image editing. The paper does not clearly demonstrate the differences between this work and GenArtist. It is important for the authors to specify these distinctions and highlight the novelty of their approach.  Additionally, a thorough comparison should be incorporated into the experimental section to strengthen the evaluation.
- While fine-grained control is presented as the main contribution, represented by the text and image controllers in the pipeline, the design is inadequate and lacks clarity. The design of the pipeline does not effectively demonstrate how the editing condition is provided to the generative model in a fine-grained manner. The text controller relies solely on prompt concatenation, making the mapping between visual tags and policies unclear and limiting precise control. Additionally, the paper does not address how to maintain image consistency after editing, which is essential for practical use. These shortcomings contribute to potential inconsistencies and an insufficient explanation of how fine-grained control is maintained. The image controller exists the same problem.

### Experimental Limitations
- The datasets used (CC3M and CC12M) are relatively small, with no experiments conducted on larger datasets such as LAION-400M or LAION-5B.
- The paper only tests a limited range of multimodal model structures, lacking experiments on models like BLIP and CLIP of different ViT models.
- The study does not address data-efficiency validation. Existing data-efficiency-focused works, such as SemDeDup[2], Filter-&-Align[3], and Sieve[4], refine or filter datasets for better performance. The paper should include comparisons with these approaches in terms of model performance and the amount of training data.

### Questions
Refer to the Weakness.

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
This paper introduces a multimodal data synthesis pipeline called CtrlSynth. Specifically, CtrlSynth includes a vision tagging model to extract key objects, attributes, and relations from an image, which can then optionally be combined with the original text for a language model to generate new image descriptions. Finally, the newly generated image caption is input into a text-to-image model to generate an image. The authors have demonstrated the effectiveness of their pipeline by comparing it with CLIP pretraining data. Overall, the enhanced dataset appears to be superior to the original one.

### Strengths
1. The idea is clear and effective: by combining multiple expert models, we can obtain fine-grained image tags, captions, and synthetic images, which together help to create a high-quality synthetic dataset.

2. The modularized pipeline is flexible, as each model can be replaced without affecting the performance of the other components.

3. Experiments are comprehensive. Compared to the baseline CLIP, the improvements from CtrlSynth are evident.

### Weaknesses
1. Practical concerns: By using several models, such as the vision tagging model, LLM, and diffusion model, the proposed method might not be efficient for scaling up to larger datasets, particularly considering the time cost associated with image synthesis.

2. The assumption behind CtrlSynth is based on a fixed number of data samples, where the method helps a model achieve better performance than training on the original dataset. However, given the recent trends in LLM and multimodal LLM research, where pretraining data continues to scale up, the proposed method may not be scalable for very large datasets. While this is a challenge, under the current setting in the paper, CtrlSynth is indeed effective.

### Questions
Can the authors provide details on the overall efficiency of the proposed pipeline? For example, how long does it take to generate 1 million images along with their captions? It would also be good to know the time cost at each component, e.g. vision tagging, caption generation, image generation. A more complete picture of the efficiency in the pipeline would better help to assess the value of this work.

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
4

### Summary
This paper introduces CtrlSynth, a controllable pipeline for generating synthetic image-text data to improve multimodal models. By allowing fine-grained control over data synthesis, CtrlSynth decomposes and recomposes visual semantics using pretrained models, enhancing diversity and alignment of generated samples.

### Strengths
- Introduces a new controllable synthesis pipeline (CtrlSynth) that allows fine-grained data manipulation, enabling user-defined policies for image-text synthesis.
- Achieving significant performance improvements across diverse tasks such as zero-shot classification, retrieval, and long-tail recognition is inspiring.
- Clearly explains the methodology with diagrams and examples, easy to understand the synthesis process and its components.

### Weaknesses
1. In the ablation experiments, it was observed that the performance improvement brought by CtrlSynth-img alone is minimal. Would it be possible to completely remove the generation of synthetic images and focus resources on improving the diversity and quality of synthetic text? Would this lead to consistent performance improvements across all tasks?

2. The paper mentions that CtrlSynth uses a self-filtering mechanism to improve the quality of synthetic data, but it lacks detailed explanations about the implementation, such as how the alignment threshold for visual tags is selected.

3. The paper does not explain in depth how CtrlSynth fundamentally differs from other caption augmentation methods like VeCLIP and LaCLIP. It is necessary to provide a clearer comparison, clarifying whether the increased diversity brought by the decomposition of visual tags and user control strategies is more important, or whether it is the generation of more fine-grained semantic captions that matters.

4. The experiments may be limited to a few selected models (e.g., Mistral-Nemo and Qwen2-7B). Would using larger LLMs lead to better results?  

5. A drawback of this method is that the data generation pipeline involves multiple different models and is not end-to-end in training, requiring substantial resources and time for building the synthetic data in the early stages.

### Questions
See weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3
