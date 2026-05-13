# Subject-Diffusion: Open Domain Personalized Text-to-Image  Generation without Test-time Fine-tuning

- Decision: Reject
- Scores: 6, 5, 6, 3

## Abstract
Recent progress in personalized image generation using diffusion models has been significant. However, development in the area of open-domain and test-time fine-tuning-free personalized image generation is proceeding rather slowly. In this paper, we propose Subject-Diffusion, a novel open-domain personalized image generation model that, in addition to not requiring test-time fine-tuning, also only requires a single reference image to support personalized generation of single- or two-subjects in any domain. Firstly, we construct an automatic data labeling tool and use the LAION-Aesthetics dataset to construct a large-scale dataset consisting of 76M images and their corresponding subject detection bounding boxes, segmentation masks, and text descriptions. Secondly, we design a new unified framework that combines text and image semantics by incorporating coarse location and fine-grained reference image control to maximize subject fidelity and generalization. Furthermore, we also adopt an attention control mechanism to support two-subject generation. Extensive qualitative and quantitative results demonstrate that our method have certain advantages over other frameworks in single, multiple, and human-customized image generation.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors have introduced "Subject-Diffusion," an innovative approach for personalized image generation that doesn't require test-time fine-tuning and only needs a single reference image. They created a large dataset and a unified framework that combines text and image information. The results show Subject-Diffusion outperforms other methods in generating single-subject, multi-subject, and customized images, marking a significant advancement in this field.

### Strengths
1.	They develop an automatic pipeline for constructing a substantial and well-organized training dataset, consisting of 76 million open-domain images and 222 million entities.
2.	Their work introduces a pioneering framework for personalized image generation, addressing the challenge of simultaneously generating open-domain personalized images for both single and multi-concept subjects, all without requiring test-time fine-tuning. This framework relies solely on a single reference image for each subject.
3.	The experimental results, both quantitative and qualitative, showcase the exceptional performance of their framework when compared to other state-of-the-art methods, confirming its effectiveness in personalized image generation.

### Weaknesses
1.	While the authors have access to a substantial training dataset containing subject information (segmentation, text descriptions, and bounding boxes), it appears that the method may not introduce sufficiently novel or distinctive techniques compared to previous approaches. Instead, it seems to be a combination or integration of existing methods. Specifically, the paper lacks a clear explanation of how the combination of these existing techniques leads to a synergistic effect that significantly surpasses the capabilities of the individual components. The novelty seems to stem primarily from the scale of the dataset rather than a fundamental algorithmic breakthrough.
2.	The training mechanism leverages multiple concept information from a single image, which is indeed a notable feature of the proposed model. However, it doesn't provide a detailed explanation or evidence to support the claim that this single-reference image approach can consistently yield better results compared to fine-tuning methods with access to multiple subject images. The paper does not adequately address the potential limitations of relying on a single reference image, such as the inability to capture variations in appearance or pose that might be present in a multi-image dataset. Furthermore, the paper does not explore the trade-offs between fidelity and diversity when using a single reference image.

### Questions
See the weakness section.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes Subject-Diffusion, an open-domain personalized text-to-image generation model that can support single- or multi-subject personalization using a single reference image without test-time model fine-tuning. The authors develop an automatic data labeling tool and construct a large-scale dataset that comprises 76M open-domain images and 222M entities. They introduce a unified framework that combines text and image semantics by incorporating coarse location and fine-grained reference image control. The authors design the prompt format and employ a trainable text encoder, as well as insert an adapter between each self- and cross-attention block, encoding dense patch features of the segmented objects and their corresponding bounding box information. The framework also adopts an attention control mechanism to support multi-subject generation. Experiments demonstrate the advantages of the proposed method over state-of-the-art baselines.

### Strengths
- The paper is generally well-written. The symbols, terms, and concepts are adequately defined.

- Sufficient details are provided to explain the proposed method. The framework shows some advantages over existing baselines.

- The relevant literature is well-discussed and organized.

### Weaknesses
 - The reviewer's primary concern is the actual experimental performance. In many results generated by Subject-Diffusion (e.g., Figure 1), the subjects lack diversity/identity variation. This suggests that Subject-Diffusion may have limited creative generation capability and generalizability. Some results are akin to image composition.

- Apart from the quantitative results, presenting additional qualitative results of the ablation studies would strengthen this paper further.

- The reviewer is interested in the accuracy of the automatic data labeling tool. Providing more evaluation and analysis of the tool to demonstrate its merits is beneficial.

- The presentation of this paper could be improved. Most images in the figures of the paper are too small, which requires careful zooming in to check details. Besides, the layout of some sections, especially the experiments, is a bit messy.


### Questions
- About the proposed framework, what is the intuition of fixing the image encoder while training the entire text encoder?

- Will the authors release the proposed SDD dataset? It is very useful if the dataset will be made publicly available. Also, the code should be made publicly available to ensure reproducibility.

- The limitation and failure case discussions are missing, which are highly recommended to be included.

- The last line of Page 1 has an Appendix reference error. This also applied to other places referring to the Appendix.

- Regarding the quantitative results in Table 1, some results are borrowed from BLIP-Diffusion while others are tested. It would be useful if the authors could provide more details on the test settings to ensure a fair comparison.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper introduces "Subject-Diffusion," a novel approach for open-domain personalized image generation that doesn't require test-time fine-tuning. The model only needs a single reference image to support personalized generation of single or multiple subjects in any domain. The authors constructed a large-scale dataset with 76M images and their corresponding subject detection bounding boxes, segmentation masks, and text descriptions. The proposed framework combines text and image semantics, incorporating location and fine-grained reference image control to maximize subject fidelity and generalization. The results indicate that the method outperforms other state-of-the-art frameworks in various image generation tasks.

### Strengths
- Introduces a new approach that doesn't require test-time fine-tuning, addressing a significant challenge in the field.
- Utilizes a single reference image, making it more user-friendly and versatile.
- Incorporates a comprehensive dataset with 76M images, enhancing the model's training and performance.
- Combines text and image semantics, leading to high fidelity and generalization in generated images.
- Demonstrates superior performance compared to other state-of-the-art methods when generating multiple objects

### Weaknesses
 - The construction of the large-scale dataset might have biases or inconsistencies that could affect the model's performance.

### Questions
None

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes to learn subject-driven image generation from training adapter layers for diffusion model, on a large-scale subject-related image generation dataset. Moreover, this paper designs the model architecture to take control signals such as bounding box, segmentation mask to supplement its model training for fidelity and faithfulness. Using this model, the paper claims that it can perform single subject image generation, multi-subject image generation, as well as human subject generation.

### Strengths
1. The recipe of adapting pre-trained diffusion model into subject-driven image generation is novel and interesting. 
2. The trained model is capable of doing multiple subject-related text-to-image generation tasks, via careful prompting the model, which is nice.
3. The quantitative results look strong to all the methods the authors have compared with. 
4. The ablation study looks comprehensive.

### Weaknesses
 - The paper is emphasizing that they have outperformed state-of-the-art in single subject generation, which is not supported by its results. Particularly, the comparison in Table 1 is intentionally ignoring the state-of-the-art results from SuTI (Chen et. al. 2023). I have found neither comparison nor discussion to justify this ignorance. Additionally, it would also be important to do qualitative side-by-side comparison with SuTI to understand the quality of generation.
  - IMO, a great paper could be one without the state-of-the-art performance, but should not be one that claims to be state-of-the-art without comparing to the actual state-of-the-art method.
- The reproducibility of the paper is questionable, given that the model training is relying on a large private dataset (at least the labels, masks, and grounding). While the dataset is being argued as one of this paper's main contribution, there is no discussion on quality of the data (not a lot examples in main paper or appendix), no discussion on how bias/privacy is protected, no plan or discussion on releasing the data.
- The image resolution provided in the paper is quite small (even counting the ones in the supplementary). Having high-resolution image generation is quite important to assess the quality of model in the field of image generation. Looking at figure 6 (when zooming in ), I could find a lot of artifacts in the interpolated results, the face is losing details, the cat face is weird, the lion looks more like a horse to me. Similarly, figure 5 also seems to have a lot of artifacts from my perspective.

### Questions
- During the inference on single-subject / multi-subject generation, do you provide those auxiliary information to the model? 
  - If the mask  / segmentations are available for the subject-diffusion only during the inference, what would be the performance if they are removed during the inference? Also how faithful is the model's generation to those control signal? 
  - the mask  / segmentations are not available in inference, would the model's performance improve given those controls signal?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
