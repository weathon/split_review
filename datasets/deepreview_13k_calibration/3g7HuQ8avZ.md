# OmniContrast: Vision-Language-Interleaved Contrast from Pixels All at once

- Decision: Reject
- Avg Score: 5.50
- Scores: 5, 5, 6, 6

## Abstract
In this work, we present OmniContrast, a unified contrastive learning model tailored for vision, language, and vision-language-interleaved understanding within multi-modal web documents. Unlike traditional image-caption data with clear vision-language correspondence, we explore a new contrastive fashion on maximizing the similarity between consecutive snippets sampled from image-text interleaved web documents. Moreover, to enable CLIP to handle long-form text and image-text interleaved content from web documents, OmniContrast unifies all modalities into pixel space, where text is rendered visually. This unification simplifies the processing and representation of diverse multi-modal inputs, enabling a single vision model to process any modality. To evaluate the omni-modality understanding of OmniContrast, we design three consecutive information retrieval benchmarks AnyCIR, SeqCIR, and CSR. Extensive experimental results demonstrate that OmniContrast achieves superior or competitive omni-modality understanding performance to existing standard CLIP models trained on image-text pairs. This highlights the potential of multi-modal web documents as a rich and valuable resource for advancing vision-language learning.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposed OmniContrast, a unified contrastive learning model that processes multi-modal web documents by transforming all modalities, including text, into pixel space for a single vision model to handle. It achieves competitive or superior performance compared to standard CLIP models, demonstrating the value of multi-modal web data for advancing vision-language learning.

### Strengths
1. OmniContrast is among first to explore vision-language correspondence on image-text interleaved web documents in CLIP-style.
2. Authors propose three consecutive information retrieval benchmarks, including AnyCIR, SeqCIR, and CSR to o facilitate the evaluation of omni-modality understanding.
3. The effectiveness is validated by experimental results.

### Weaknesses
I am concerned about the motivation with the single modality in the pixel space. I believe it is limited in a few ways.

1. It is ture that "image-text interleaved content is natively present in visual formats such as screenshots". Screenshot is a scenario, however, in more cases, such as the very rich html format image-text interleaved data (much richer than screenshots), images and texts are naturally presented in different modalities. 

2. Is it really practical unifying them into pixels? In many cases, we have seperated texts and images, where we have to re-organize them in the form of "screenshots" to use the model. It can be redundant. And organizing them in the form of "screenshots" itself can involve some issues, such as the limitation from the resolution, etc. I agree that CLIPPO (Tschannen et al., 2023) demonstrates that the vision encoder can learn meaningful textual representation directly from pixels, however, "it is feasible to do so" does not mean it is a good solution in different scenarios. I am looking for a strong motivation to do so.

3. In Tab. 6, simple alternatives like CLIP-V+T, and UniIR-CLIP are very effective when compared to Omni. That is also why I am considering if unifying them into pixels is a good solution and well-motivated.

### Questions
### Reply (Post Rebuttal)

I do not think my comments have the inconsistencies mentioned by the authors.

> You correctly acknowledge that unifying information into a single modality simplifies the model structure and improves handling image-text interleaving data (e.g., screenshots).

These are two separate points. The authors mention two advantages: the first is simplifying the structure, and the second is the use case for screenshots. I acknowledge its usefulness for screenshots but do not consider "simplifying the structure" to be a clear benefit. These two points are entirely unrelated, so the inconsistencies claimed by the authors do not exist.

1. The reason I don’t view "simplifying the structure" as a clear benefit has already been explained: *"The text encoder in CLIP is also quite simple, and I feel this is more of a design choice between single-tower and two-tower architectures rather than a significant advantage."* While a single-tower model does eliminate the text encoder in a two-tower architecture, does removing a CLIP text encoder offer any clear advantage in most scenarios? That is the question I raised. We all know that removing a text encoder reduces the number of parameters, but if this is being presented as a major contribution and clear advantage, the authors need to demonstrate why removing a text encoder is crucial in their application context. I did not see this importance addressed in either the paper or the rebuttal.

2. The authors argue that *"we address cases where text extraction is complex or difficult, like image-text interleaving formats like screenshots."* However, recognizing printed text from screenshots is straightforward as I know.

I remain concerned about unifying text into the pixel space, where sentences are treated as a bag of words literally. And it is more concerning when the authors emphasize long-form text, where contextual dependencies are likely more important.

### Soundness
2

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
3

### Summary
This paper develops OmniContrast to unify vision-language modeling from image-text interleaved web data. To evaluate such a unified model, the authors develop the AnyCIR and SeqCIR benchmarks. These two benchmarks focus on evaluating the relevant snippet retrieval ability of the model.

### Strengths
- Clear presentation.

- The evaluation of different methods on AnyCIR and SeqCIR seems sound.

- The method is also straightforward, only a unified model saves the memory.

### Weaknesses
 - The reviewer appreciates the development of benchmarks like AnyCIR and SeqCIR. One pitty is that the results of baselines are all reproduced by the authors. No third-party baselines are provided.

- No results on common benchmarks are provided. In this case, the reviewer may think that OmniContrast is only developed for CIR, this specific task. It may discount the contribution of this work.

- Another question is, why we would choose OmniContrast when there are many next-token-prediction VLMs? For example, the Emu series. Such VLMs may be the mainstream now. The reviewer thinks these VLMs can also do what OmniContrast can do. Relevant discussions/comparisons are required.

### Questions
- In Section 5.2, do the authors only use the vision encoder of CLIP/OpenCLIP for evaluation? Why not use the full CLIP/OpenCLIp model? 

- Could the authors provide results on common benchmarks like MS-COCO (text-to-image retrieval), Flickr30k (text-to-image retrieval), and GLUE benchmark? Like what CLIPPO [1] did. The reviewer thinks this can better figure out what can/cannot OmniContrast do. 
    - As said in the  Weaknesses, all results of baselines are reproduced by the authors. Comparisons on common benchmarks make the evaluation more strong.

- Another question is, why we would choose OmniContrast when there are many next-token-prediction VLMs? For example, the Emu series[2]. Such VLMs may be the mainstream now. The reviewer thinks these VLMs can also do what OmniContrast can do. Relevant discussions/comparisons are required.


[1] https://arxiv.org/pdf/2212.08045

[2] https://github.com/baaivision/Emu

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper presents the OmniContrast model, which unifies vision and text into a pixel space for web document retrieval and understanding. Moreover, this paper presents three new information retrieval benchmarks (AnyCIR, SeqCIR, and CSR) to evaluate the ability of the model to retrieve continuous information in complex multi-modal documents.

### Strengths
- The model performs excellently, achieving outstanding results in multiple baselines.
- Good writing and detailed experiments.
- A novel and useful approach for transforming interleaved data into pixel space.

### Weaknesses
 - I'm not sure if I'm misunderstanding the model, but I think there is a lack of comparisons on some baselines, such as VQAv2 and GLEU like the comparisions in CLIPPO.
- I think there is a lack of further discussion on the necessity and effectiveness of unifying text and images into pixel space, as well as a comparison of the differences between interleaved data and text-image pairs in this unified pixel space.

### Questions
I believe that the handling of interleaved data is a significant distinction between OmniContrast and CLIPPO. 

Therefore, I'm curious about the differences in the model's performance when using interleaved data compared to image-text pairs.

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
OmniContrast, a unified contrastive learning model for understanding vision, language, and vision-language interactions within multi-modal web documents. Unlike traditional models, OmniContrast:

- Explores a new contrastive approach to maximize similarity between consecutive snippets from image-text interleaved web documents.
- Unifies all modalities (text, images) into pixel space, rendering text visually, simplifying processing and representation.
- Enables a single vision model to process any modality.

### Strengths
1. Excellent ablation study demonstrating the necessity of including each modality in the proposed pipeline (Table 1).
2. Clearly outperforms baseline methods, allowing the model to work in different modality settings.

### Weaknesses
1. Despite the proposed method outperforming CLIPPO in terms of average scores, it seems that the baseline method is capable of handling all modalities in OmniContrast. Clarification on the contribution is needed.

2. Data augmentation of the training data is a crucial part of the pipeline, but it is not well-documented, raising concerns about synthesizing low-quality training samples.

3. Figure 2: The images and fonts are extremely small, making it difficult to understand. The caption fonts also appear too small.

4. The concept of omni-modality seems odd from a reading perspective, as it appears the authors are solving vision-language problems.

5. In the abstract, "OmniContrast unifies all modalities into pixel space, where text is rendered visually" was difficult to understand until reading the entire introduction and related work section. The term "rendering" suggests high-resolution 3D scenes, whereas simple text copying and pasting is not truly rendering.

### Questions
1. Does training a model in this omni-style make it easier or harder to converge?
2. Related to Q1, do the authors believe that adding modalities helps the model learn each modality better, or does it make the training problem more complicated?
3. What would happen to OmniContrast if there were abundant data in three modalities but limited data in the fourth modality?

### Soundness
3

### Presentation
2

### Contribution
3
