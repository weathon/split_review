# KnowData: Knowledge-Enabled Data Generation for Improving Multimodal Models

- Decision: Reject
- Avg Score: 5.50
- Scores: 6, 5, 5, 6

## Abstract
In this paper, we introduce a framework to enhance the quality of synthetic image-text pairs for multimodal models such as CLIP. Our approach, named KnowData, integrates real-world knowledge explicitly into the generation of text descriptions. It combines structured knowledge from knowledge graphs like ConceptNet and unstructured knowledge extracted from Wikipedia, to ensure that the generated text descriptions are both contextually rich and accurately reflective of real-world knowledge. Additionally, we leverage Large Language Models for the expansion, summarization, and refinement of the text descriptions to ensure their coherence. These enriched texts are subsequently used to generate images through advanced text-to-image models like Stable Diffusion and DALLE-3. CLIP models are then fine-tuned with these synthetic image-text pairs for zero-shot classification tasks. Our experiments across 9 datasets demonstrate that CLIP models fine-tuned with our knowledge-guided synthetic datasets outperform state-of-the-art (SOTA) zero-shot CLIP methods (e.g., +11.23% on DTD and +4% on EuroSAT based on ViT-B/16 model; +11.47% on CIFAR-100 and +7.99% on DTD based on ResNet-50 model). These results showcase the improved out-of-distribution robustness and adaptability of our approach across a diverse set of data domains. We further substantiate the design of KnowData through ablation studies, revealing that the integration of knowledge not only enhances zero-shot performance but also contributes to the reliability, diversity, and detail-orientation of the generated synthetic images, thereby offering better data scaling laws for model performance.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes a novel method that use structured knowledge in ConceptNet and unstructured knowledge in Wikipedia to augment the synthetic image description with the help of LLMs. The synthetic data contains more informative contents and do not rely on crawling on the web. The resulted text descriptions are then fed to diffusion models to generate synthetic images.

### Strengths
1. A novel method to enhance the fine-tuning data of CLIP models
2. Circumvent the usage of crawling.
3. Good downstream task performance improvements

### Weaknesses
1. Limited comparison to other synthetic data methods. For example, are the wikipedia retrieval is necessary? Can this part be replaced by a strong LLM, where LLM can serve as a database?
2. A little unfair comparison with baselines. This method unfreezes part of the image encode but other methods only finetune the classification head. This could lead to unfair comparison.

### Questions
1. Could you clarify how you unfreeze part of the image encode when fine-tuning? Also can you compare your method with other baselines under the same fine-tuning budget?
2. See Weakness 1
3. Can your method be used to provide pre-training data for CLIP?
4. You have conducted scaling experiments on the image encoder and the fine-tuning dataset. Could you please also test whether your method is applicable to already strong CLIP-based pre-training models, like SynthCLIP [1]
5. Can you compare more fine-tuning baselines using synthetic data, such as LoGoPrompt [2], which shows greater performance.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper proposes a new technique to improve the zero-shot classification performance of vision-language models by incorporating factual knowledge data for the class descriptions. Specifically, KnowData starts from the class names of an image classification dataset, enriches them with ConceptNet relations, GPT-3.5, and RAG-retrieved Wikipedia knowledge, to create several detailed descriptions. These descriptions are then used to generate synthetic images with a text-to-image diffusion model. Finally, the synthetic dataset is used to fine-tune a vision-language model on the dataset-specific synthetic data.

### Strengths
- Incorporating facts from knowledge bases such as ConceptNet and Wikipedia is a reasonable approach to ensure correctness while obtaining a diverse set of novel class descriptions.
- The zero-shot classification results improve over previous works, especially for fine-grained classification datasets, such as DTD and EuroSAT.
- A comprehensive set of ablations studies evaluate the individual parts of KnowData, and further analyze the effect of the diffusion model, the scaling ability, and the VLM size.
- Zero-shot performance of the fine-tuned model on other downstream tasks (VQAv2, WinoGround) suggest that KnowData generalizes beyond image classification.

### Weaknesses
 - Improvements on ImageNet, although better than previous work, are rather marginal.
- The selection of fine-grained datasets is rather slim and could be extended. Cited works such as [He et al., 2023] evaluated on many more datasets.
- The CLIP fine-tuning is not entirely clear. Is a randomly initialized classification head added on top of the CLIP vision features, i.e. linear probing, or are the text embeddings of the base prompt used for classification during fine-tuning? If it is the former, how does the generalization in Tab. 7 work, i.e., how does KnowData ensure that the fine-tuned model is still compatible with the text encoder embeddings?
- Some additional ablations could help better understand all components of the method:
  * With vs. without few-shot demonstrations for Sec. 3.2 description summarization and refinement.
  * With vs. without CLIP filtering in Sec. 3.3 image generation.
  * Training only a classification head vs. multiple layers in addition. This would create a fair comparison to "Synthetic".
- Tab. 7 already suggests this generalizes beyond the specific use case of image classification. This paper would have been more impactful, if it fully embraced this direction to improve all vision-language capabilities of CLIP, e.g. text/image retrieval, instead of focusing mainly on image classification.
- While the idea to incorporate factual knowledge is novel, it is a rather incremental improvements over previous approaches that also used external knowledge. I see this as a minor weakness.

### Questions
Please address the points raised in the Weaknesses section. Here are additional relevant questions/comments:
- L. 185: How do you choose the N structured knowledge descriptions when there are more than N? What do you do when there are less than N?
- Tab. 3 shows CLIP scores, but it is not clear which text embedding is used for each row. A fair comparison would use the base prompt for each row. Please clarify.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This work proposes a data augmentation methodology called KnowData. It basically consists of four main components/procedures: (1) structured knowledge generation to obtain schema-based knowledge, (2) LLM-aided summarization and refinement for the previously obtained structured knowledge, (3) generating images from the crafted/refined prompts from step (2), and finally (4) finetuning multimodal models from the augmented data obtained from step 1 to 3.
The authors then demonstrate the effectiveness of the proposed method on numerous datasets compared to baselines such as the vanilla CLIP and some of its zero-shot enhanced variants.

### Strengths
- The paper is quite clearly written, easy to follow, and well-illustrated.
- The proposed data augmentation method improves the zero-shot performance quite significantly, where comprehensive experimental results are shown.
- The retrieve and summarize idea is neat.

### Weaknesses
 - The CLIP score is a holistic score, what about finer-granularity of details that are suboptimal but decisive for recognition?
- The proposed data-augmentation method is supposedly generalizable, yet the paper only tests its effectiveness on one multimodal model, that is CLIP. The method should be further justified by more advanced multimodal LLM-based models in a controlled (few-shot) setting.
- The proposed method is rather incremental, and there is no direct evaluation applicable (in the paper) to quantify how and where the generated prompts are better than normally collected ones. Ablations needed compared to web-crawled image captions in addition to self-ablations in Table 5.
- The proposed method needs to be tested on datasets that are much more challenging, especially ones that contain sufficiently confusing class-pairs, such as iNaturalist (Horn et al.).

### Questions
- What is the performance between confusing pairs? I.e., when we plot the confusion matrix, and select the top-2 (or K) confusing class-pairs, how much does the proposed model improve?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper proposes a data augmentation method called KnowData, which leverages text-to-image generation models to synthesize text-image pairs. Compared to traditional data augmentation methods, this approach incorporates structured knowledge from ConceptNet, covering taxonomy, relationships, and attributes, as well as unstructured sources like Wikipedia and Retrieval Augmented Generation (RAG) to enhance contextual and background details. GPT-3.5 is used to generate coherent sentences, and a text-to-image generation model creates diverse images, from which high-quality images are selected. The resulting dataset is used to fine-tune models. Experimental results show that this data augmentation method significantly enhances CLIP’s performance on image classification tasks.

### Strengths
1. The proposed data augmentation method addresses the limitations of existing text-image pairs that contain only class names or superficial or short descriptions. By incorporating structure and unstructure knowledge from knowledge bases and knowledge graphs, the resulting text descriptions are rich and reliable, thereby enhancing CLIP’s perception and cognition. This finding will encourage further studies on synthetic data that integrates real-world knowledge from knowledge bases or knowledge graphs.
2. The paper conducts extensive experiments, demonstrating the method's advantages from various perspectives. This paper also provides valuable insights and experience that benefit the community’s exploration in this area.
3. The study validates an interesting insight: longer, knowledge-rich textual descriptions do not limit image diversity in image augmentation. Instead, they may increase it. This finding can offer confidence for similar applications in long-text-to-image data synthesis, particularly for entity-centric data.

### Weaknesses
1. The experimental setup is inaccurately categorized. Although the paper frequently mentions a focus on zero-shot image classification, the augmented textual descriptions begin with class names derived from the training set used in the evaluation tasks. As a result, the final augmented image-description pairs are essentially a fine-grained version of the training set. While the KnowData-enhanced CLIP model was not directly fine-tuned on the original training set, the augmented data is an extension of the training data, which does not meet the criteria for zero-shot learning.
2. The paper contains numerous writing issues, primarily with the overly broad title and unclear focus, as well as some inaccurate statements.  I hope you can revise it in the future. If the revision results in a version that is clearer and more accurate, it will deserve a score above the borderline. 
3. Some citations are missing or inappropriate. While the authors have generally identified relevant papers, certain sources are incorrectly cited multiple times throughout the paper.

### Questions
I. Title and Focus are Inappropriate

-- 1. The paper’s focus is too broad, which leads to confusion about the specific model and task under study. For example, in the first paragraph, it may not be suitable to discuss both vision-language pre-trained models and diffusion models, like Flamingo and DALL-E 3, together. Flamingo is a vision-language pre-trained model, while DALL-E 3 is a diffusion model. The broad scope introduces unrelated topics, such as automatic content generation, auxiliary techniques, and image-text retrieval. It is suggested to narrow the focus to Contrastive Language-Image Pre-training (CLIP).

-- 2. The broad focus results in certain claims that cannot be sufficiently supported by experiments on CLIP alone, such as in lines 97-98, “enhancing the learning efficacy and application potential of multimodal models.” However, the study only tests CLIP without exploring other models.

-- 3. It is suggested that the title be narrowed down, for instance, to "Knowledge-Enabled Data Generation for Long-Tail Entity Image Classification," as focusing solely on class names, knowledge graphs, and Wikipedia descriptions with images is inadequate for constructing datasets for more complex tasks. Lines 96-97 mention “domain-specific insights into the text generation process,” yet “domain-specific” does not apply to data synthesis methods for tasks beyond classification.

-- 4. While Table 7 extends beyond image classification to VQA and image-text matching, it remains uncertain if such improvements are consistently present. KnowData’s generated text-image pairs are entity-centric and cater to less common entities that benefit from additional background knowledge. However, VQA and Winoground require inference and compositional generalization, which are not covered by entity image-description pairs. Perhaps you could further explain why domain-specific entity knowledge leads to improvements in VQA and compositional generalization tasks.

II. Citation Issues

-- 1. Due to the overly broad focus in the first two paragraphs of the introduction, related work citations are insufficient. Each category or application is cited with only one reference, which is not necessarily the latest or most representative.

-- 2. Line 44 cites Radford et al. (2021) as mentioning that CLIP uses noisy image-text pairs from the internet. However, this does not support the claim that traditional dataset collection methods compromise contextual richness and accuracy due to noisy internet data. Instead, Radford et al. (2021) demonstrates that CLIP’s effectiveness surpasses that of previous models using a large and noisy internet-based image-text dataset. It is suggested to add additional references on “contextual richness” and “accuracy” which are impacted by “noisy data”.

-- 3. The paper does not adequately explain the necessity and challenges of the proposed method. Lines 50–52 in the second paragraph should focus more on this, given the prevalence of synthetic data in image classification and other multimodal tasks. The paper only lists one related work, but several studies are relevant, such as Synthetic (He et al., 2023) and Diversity (Shipard et al., 2023). To strengthen credibility, more relevant works should be cited here. Additionally, while DALL-E 3’s caption construction method may have inspired this work, it does not effectively demonstrate the need for the proposed method.

-- 4. Line 189 references GPT-3.5 incorrectly with (Brown et al., 2020). (Brown et al., 2020) is related to GPT-3. The appropriate citation for GPT-3.5 is the paper of InstructGPT.

III. Writing Issues

-- 1. Line 110-111, “This study aims to set a new benchmark and ignite further research into knowledge-guided approaches for multimodal learning.” The paper presents a dataset construction process, which results in a training set, not a benchmark.

-- 2. Separate different conclusions. For instance, “Our extensive experiments demonstrate that CLIP models fine-tuned with our knowledge-guided, synthesized dataset outperform those trained with state-of-the-art (SOTA) data generation approaches or other zero-shot techniques,” represents two conclusions.

-- 3. Line 173-174, the mention of ATOMIC (Hwang et al., 2021) providing commonsense knowledge around human events seems unnecessary.

-- 4. Line 293 mentions “robustness and adaptability”; however, robustness was not evaluated, so “robustness” should be removed.

-- 5. Line 330-331, “P denotes the use of pre-trained models” should clarify which pre-trained models are meant. Is this referring to CLIP? If so, consider rephrasing to “P denotes the use of only CLIP.”

-- 6. Line 428, directly linking the appendix figures in the main text could be avoided; Figure 2 is sufficient, even though I reviewed figures 6 and 8 in the appendix.

-- 7. Line 469, the claim “KnowData enables better data scaling law” is typically about the trend in model performance with an increase in training data scale. However, for highlighting KnowData’s effectiveness over basic prompt usage, “KnowData utilizes data more efficiently” may be more appropriate.

IV. Inaccurate Statement of Experimental Setup

-- 1. The paper does not constitute a zero-shot setting. This paper says that “as no original training data is used in our framework, our evaluation belongs to the zero-shot setting.” However, in the experimental setup, “We generate 480k synthetic images based on ImageNet class names to fine-tune the downstream models and then evaluate the fine-tuned models on ImageNet test data and its out-of-distribution variants. We generate about 60k images for other datasets with fewer categories, including CIFAR100, DTD, and EuroSAT.” Although not the original training set, the similar training data and augmented descriptions (with labels) & images are used. Therefore, this setting does not meet the criteria for zero-shot. Similarly, the title “KnowData improves CLIP’s zero-shot performance” in line 368 is also inaccurate.

[Optional] V. Experimental Results Needing Further Explanation （Further details could enhance the story, but their absence is not critical）

-- 1. Why does the KnowData augmentation method underperform compared to the OpenAI-version CLIP on ImageNet-A? The paper does not explain this, so a definite or plausible explanation would be helpful.

-- 2. In text-to-image generation, DALL-E 3 often surpasses Stable Diffusion v1.5 in image quality. Yet, in Table 4, DALL-E 3 performs similarly to or worse than Stable Diffusion v1.5 on several datasets. This could result from the more realistic nature of Stable Diffusion v1.5 images or its closer alignment with test distribution on simple, single-object images. Additional explanations are expected. 

-- 3. In Table 5, the CN+WRAG+GPT+Div setup greatly improves DTD and EuroSAT while offering a smaller boost for ImageNet. This may be domain-specific. Given the high training cost (140k image-text pairs), can the study identify which classes benefit more from knowledge and diversity enhanced prompts? Additionally, are there classes where basic prompts are sufficient?

-- 4. The effect of diversity trick (with different guidance scales) is unclear. “Diversity in knowledge and diversity in images both matter” in Line 482 lacks direct experimental evidence. Table 5 does not include a diversity score. Is it possible that CN+WRAG+GPT alone (without the diversity trick) could improve diversity scores?

### Soundness
2

### Presentation
2

### Contribution
3
