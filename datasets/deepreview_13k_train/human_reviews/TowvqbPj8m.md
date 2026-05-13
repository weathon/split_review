# Content-style disentangled representation for controllable artistic image stylization and generation

- Decision: Reject
- Scores: 5, 5, 5, 6

## Abstract
Controllable artistic image stylization and generation aims to render the content provided by text or image with the learned artistic style, where content and style decoupling is the key to achieve satisfactory results. However, current methods for content and style disentanglement primarily rely on image information for supervision, which leads to two problems: 1) models can only support one modality for style or content input;2) incomplete disentanglement resulting in semantic interference from the reference image. To address the above issues, this paper proposes a content-style representation disentangling method for controllable artistic image stylization and generation. We construct a WikiStyle+ dataset consists of artworks with corresponding textual descriptions for style and content. Based on the multimodal dataset, we propose a disentangled content and style representations guided diffusion model. The disentangled representations are first learned by Q-Formers and then injected into a pre-trained diffusion model using learnable multi-step cross-attention layers for better controllable stylization. This approach allows model to accommodate inputs from different modalities. Experimental results show that our method achieves a thorough disentanglement of content and style in reference images under multimodal supervision, thereby enabling a harmonious integration of content and style in the generated outputs, successfully producing style-consistent and expressive stylized images.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper collects a new dataset WikiStyle+ and proposes to learn decoupled content-style representations with conventional VLM pre-training losses, which are injected into the diffusion models via cross-attention layers for stylized image generation.

### Strengths
1. A new dataset with multimodal annotations of both style and content is collected.

2. Conventional VLM pre-training losses are adopted in the scenario of diffusion model based stylized image generation.

### Weaknesses
1.The qualitative results are not convincing. For example, DeaDiff and InstantStyle  better follow the input styles than the proposed method in Fig.1 and Fig.5 respectively.

2.The authors should discuss the differences between WikiStyle+ and the existing WikiArt dataset [A] (e.g., image data overlap). Moreover, the authors do not clarify that whether the dataset will be released in the future.

[A] Recognizing image style.

3.The pipeline in Fig.4 is not consistent with the descriptions in Sec.4.2. For example, (L308-310) the style embeddings are expected to be injected into the diffusion model via multi-step cross-attention layers but in Fig.4, the style embeddigns are injected into the midlle block only and the time embedding is missing as input to the multi-step cross-attetion layers; (L312-313) the content embeddings are expected to be concatenated with the text embeddings from the text encoder but the content embeddings are fed into the cross-attention layers in Fig.4.

4.The ablation study in Sec.5.4 is not sufficient for the missing discussions about the effect of each item in Eq.(1).

### Questions
1.How many images in WikiStyle+ overlap with WikiArt dataset? Will the dataset be released?

2.How does each item in Eq.(1) affect the final results?

3.Dose the multi-step cross-attention layers accept the modulation from the time step?

--------Response on Dec 4th----------

Thanks the authors for the further response after the rebuttal period. Two main concerns are still not addressed:

1.The authors claim that “The single reference image is not the only color source for the generated results; the model also utilized color usage patterns embedded in the pre-trained dataset. ” But OOD evaluation is not included in the paper (which I have pointed out during the rebuttal period and the related details are not clarified in the paper as well), where the reference style/artist is not included in the pre-training dataset.

2.The authors claim that “The style of an image should be reflected in the artist's color usage habits rather than the specific colors present in that particular image. These habits encompass commonly used tones (e.g., bright, soft, or dark), color schemes (e.g., complementary, analogous, or monochromatic), as well as attributes like saturation and contrast.” However, the adopted style similarity metric in this paper lacks persuasiveness for comparions among all the competing methods. Also, the metric subjective preference should be disentangled into different aspects (e.g., tones, color schemes, etc).

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a content-style representation disentangling method for controllable artistic image stylization and generation. The proposed method employs contrastive learning tasks to learn disentangled content and style representations, which then guide a diffusion model to generate stylized images.

### Strengths
1. The proposed method accepts inputs from different modalities as control conditions.
2. This paper provides a new dataset consists of artworks with corresponding textual descriptions for style and content.
3. Both qualitative and quantitative experiments are conducted to evaluate the performance of the proposed method.

### Weaknesses
1. The proposed method is not well-explained. What are the outputs and training objectives of the Content and Style Disentangled Network (CSDN)? What is its structure, specifically the image encoder and the Q-Former? The paper states, 'The image-grounded text generation loss involves training a model to generate descriptive text that corresponds to a given input image.' To whom does the 'model' refer in this context? Additionally, what is the 'two-class linear classifier' mentioned in the image-text matching loss, and where does it come from? How are the image and text embeddings used in the contrastive learning tasks, and what are the specific loss functions used for each task (ITC, ITM, ITG)?

2. The claims regarding the quality of the proposed method in the text-to-image stylization task appear to be overstated. While its visual quality is comparable to that of other methods, it is challenging to identify instances where the proposed method demonstrates significant superiority. In fact, the stylized images produced in this paper always exhibit noticeable deviations in style (such as color) when compared to the reference style images. The method seems to struggle with accurately transferring fine-grained stylistic details, often resulting in a generalized style rather than a precise replication of the reference.

3. Some state-of-the-art text-to-image stylization methods are not compared in this paper, such as StyleDrop [1] and DreamStyler [2]. 
[1] StyleDrop: Text-to-Image Generation in Any Style. NeurIPS 2023. 
[2] DreamStyler: Paint by Style Inversion with Text-to-Image Diffusion Models. AAAI 2024.

4. The style similarity metric used in this paper lacks persuasiveness. Why not employ CLIP to directly assess the similarity between the generated images and the reference images? Alternatively, Gram loss is also a widely used metric to evaluate style similarity between two images. The current metric, which involves generating descriptive text from the reference image and then comparing it to the generated image, introduces an unnecessary layer of abstraction and potential information loss. How is the descriptive text generated, and what ensures its faithfulness to the original style?

5. This paper only conducted quantitative experiments in the text-to-image stylization task, while no quantitative experiments were performed in the stylized text-to-image generation and collection-based stylization tasks. This lack of comprehensive quantitative evaluation across all tasks makes it difficult to assess the generalizability of the proposed method.

6. I am curious about the inference speed of the proposed method. Is it comparable to or superior to that of previous methods? What is the computational overhead of the CSDN and the diffusion process?

### Questions
Please see **Weaknesses**.

### Soundness
2

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
3

### Summary
This paper presents an innovative approach to controllable artistic image stylization and generation by addressing the challenges of content and style disentanglement. By constructing the WikiStyle+ dataset, which includes artworks with corresponding textual descriptions, the authors enable a more comprehensive disentanglement of content and style. Their proposed model utilizes Q-Formers and learnable multi-step cross-attention layers within a pre-trained diffusion model, allowing for inputs from different modalities. The experimental results demonstrates that the method achieves thorough disentanglement and harmonious integration of content and style. This work represents a significant advancement in the field.

### Strengths
- This paper creatively proposes the use of a Q-Former to disentangle content and style features, achieving more fine-grained control in generation and yielding excellent results. 
- The paper conducts thorough comparisons, surpassing baseline methods on multiple metrics, and provides ample visual analyses to support its main conclusions. 
- The writing is fluent, the expressions are clear, and the logic is easy to follow. 
- The primary research problem of this paper—disentangling content and style features—offers valuable insights for the development of related fields.

### Weaknesses
Some of the description of the methods is unclear:

- MCL is mentioned in Line 251 but is not further elaborated upon. Specifically, it is unclear how the multi-step cross-attention layers are implemented and how they interact with the diffusion model's denoising process. The mechanism by which style embeddings are 'injected' requires more detail.
- In Eq 3, the specific workings of the binary classification network are not described, including its specific inputs. It is unclear how the cosine similarity between image and text embeddings is transformed into a matching probability and what specific layers are used for this transformation. The inputs to the binary classifier, specifically whether they are the raw embeddings or some transformed version, are not specified. Furthermore, the distinction between content and style inputs ($I_c$, $T_c$) and ($I_s$, $T_s$) is not clearly explained in the context of the equation.
- The text generation model used in Eq 4 is not introduced in the text or figures. The architecture of this decoder is completely absent, making it difficult to understand how the model generates text from the image embeddings. The specific layers, activation functions, and the process of mapping hidden states to vocabulary logits are not described.

The mathematical expressions and symbols are ambiguous:

- In Eq(2), the subscripts c and s on the vectors I and T previously indicated different feature types, but in the equation, i is used to denote the sample index. This creates a conflict in notation and makes it difficult to understand which features are being used in the equation. The use of $i$ as a sample index is also not standard in this context, as sample indices are typically denoted by $n$ or $k$.
- The symbol T has multiple meanings: in Figure 4, it represents the total number of forward pass steps; in Eq 2, it denotes text features; and in Eq 4, it indicates text length. Similarly, t has multiple meanings, referring to both timestep and text sequence index. This overloading of symbols makes the equations and figures difficult to interpret and understand.
- Image features are denoted as z in Fig 4, but as F_I in the text. This inconsistency in notation between the text and figures creates confusion and makes it harder to follow the methodology.

There are noticeable typos in the keywords:

- Line 251: "Mlti-step Cross-attention Layers" should be "Multi-step Cross-attention Layers."
- Line 337: "learning rate of 51e-5" should be corrected.
- Fig 4: "Detangle Loss" should be "Disentangle Loss."

### Questions
- What are the differences between CSDN and MCL? Does CSDN refer to the entire generation framework or specifically to the cross-attention part?
- Could you provide a more detailed analysis of the roles of each component in the disentanglement loss function, such as through mor ablation experiments?

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper addresses the challenge of artistic image stylization by decoupling content and style representations. The authors propose a new approach using a multi-modal dataset, WikiStyle+, and a disentangled content-style diffusion model guided by Q-Formers and multi-step cross-attention layers.

### Strengths
1. **WikiStyle+**: The introduction of the WikiStyle+ dataset is a meaningful contribution, particularly as style-content disentanglement is a growing area of interest in this research community. By providing a dataset with artwork images and descriptive text, the authors provide a resource that could aid further research into artistic stylization.

2. **Performance**: The qualitative results appear more nuanced compared to previous methods (e.g. as shown in Figure 1). For instance, in the stylization of Van Gogh’s Starry Night, the proposed method captures broader brushstroke techniques of the artist rather than simply replicating signature swirling patterns in that specific art piece. This suggests that the model emphasizes general stylistic elements of artist and it better suited for general style adaptation.

### Weaknesses
1. **Dataset**: The style descriptions in WikiStyle+ appear to rely on existing tags from WikiArt. This raises concerns about their expressiveness, as a simplistic style caption may not sufficiently capture the nuances of lesser-known artistic styles. Notable styles such as Van Gogh’s may embed effectively even with a very general description since the pre-trained model already have seen this artwork in their training. On the other hand, other (non-famous) styles might benefit from more detailed descriptors, such as specific brushstroke techniques or color tones, to improve style expressiveness.

2. **Novelty**: Although the authors have made commendable efforts in curating WikiStyle+, both the dataset and model contributions feel incremental. While disentangling content and style is valuable, a deeper exploration of style elements (e.g., brushstroke and color) could enhance the study’s impact (as I said in above). Similarly, the reliance on Q-Formers for modeling feels more like a marginal improvement than a breakthrough innovation.
3. **Related Works**: Recent studies e.g. StyleDrop and DreamStyler address content-style disentanglement by incorporating context prompts alongside style replication and they achieve the reduction of content leakage. Although these approaches differ in specifics, they share similarities in the goal of style-context disentanglement. A direct comparison or inclusion of these models in the discussion would clarify the unique advantages of this paper’s method. For example, it would be informative to analyze how the model performs when relying solely on style-content descriptions or to provide ablation studies to pinpoint effective components.
4. **Analysis**: It would be valuable to examine how the level of detail in content and style descriptions affects disentanglement performance. For instance, analyzing whether a minimal description results in poorer disentanglement could yield insights into the robustness of the method.

### Questions
Please see the weakness. I am curious on how the style replication performance varies when the details of style-content prompt differ.

### Soundness
3

### Presentation
3

### Contribution
2
