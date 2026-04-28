# Relative Drawing Identification Complexity is Invariant to Modality in Vision-Language Models

- Decision: Reject
- Avg Score: 4.00
- Scores: 5, 3, 3, 5

## Abstract
Large language models have become multimodal, and many of them are said to integrate their modalities using common representations. If this were true, a drawing of car as an image, for instance, should map to the similar area in the latent space as a textual description of the strokes that conform the drawing. To explore this in a black-box access regime to these models, we propose the use of machine teaching, a theory that studies the minimal set of examples a teacher needs to choose so that the learner captures the concept. In particular, we apply this to GPT-4V, a multimodal version of GPT-4 that includes support for image analysis, to evaluate the complexity of teaching a subset of objects in the _Quick, Draw!_ dataset using two presentations: raw images as bitmaps and trace coordinates in TikZ format. The results indicate that image-based representations generally require fewer segments and achieve higher accuracy when compared to coordinate-based representations. But, surprisingly, for concepts recognized by both modalities, the teaching size ranks concepts similarly across both modalities, even when controlling for (a human proxy of) concept priors. This could also suggest that the simplicity of concepts is an inherent property that transcends modality representations.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper investigates whether MLLMs, specifically GPT-4V, truly understand common representations. The authors leverage machine teaching, a framework focused on identifying the minimum number of teaching cases necessary for a model to learn a concept. They apply this to GPT-4V to assess the complexity of teaching drawing object recognition with two different representations: bitmap images and trace coordinates in TikZ format. The findings show that image-based representations generally require fewer examples and achieve higher accuracy than coordinate-based representations.

### Strengths
- The evaluation protocol is technically sound.
- The findings are interesting.

### Weaknesses
 - The testing model and dataset are limited: in the experiment, only GPT-4V is considered as the model for testing, and the test set is limited to 20 concepts from a specific dataset. Given the variety of multimodal LLMs, including both open-source and proprietary models, the reviewer suggests testing additional models, especially advanced open-source models, to further verify the findings and demonstrate the effectiveness of the proposed protocol. The lack of diverse model testing limits the generalizability of the conclusions, as performance could vary significantly across architectures and training datasets. Furthermore, the reliance on a single dataset with only 20 concepts raises concerns about the robustness of the findings. The concepts themselves might be too simplistic or specific to this dataset, potentially not reflecting the complexities of real-world object recognition tasks. A more comprehensive evaluation would involve a wider range of concepts and datasets.

- Potential applications and impact are unclear: Based on the experimental results shown in this paper, the reviewer is concerned about the potential applications of this work. The experiment tests very simple sketch bitmap images, which is a limited. Also, the discussion of potential applications and impact of this work will be appreciated. The current study focuses on a narrow task of recognizing simplified sketches, which does not directly translate to practical applications. The lack of discussion on how this work could be extended to more complex scenarios, such as real-world images or more intricate drawings, makes it difficult to assess its practical value. The paper would benefit from a more thorough exploration of potential use cases and the broader impact of the findings.

Minor comments:

- The paper's writing should focus more on the motivation. The detailed descriptions of each module are overwhelming for the reader. The reviewer suggests revising the paper in a more concise and precise manner.

### Questions
- Line 270 states that the data is not part of the GPT-4V training data. How was this verified?

- When prompting GPT-4, did the authors include the list of concepts in the prompt for GPT-4 to select from?

- Once the teaching size was confirmed, how did you prompt GPT-4 with the instances in the teaching set? Could you please provide more implementation details on how GPT-4 was prompted.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
In this paper, the authors have explored the relative complexity of concept identification across different modalities (bitmap images and coordinate representations) in current large multi-modal models: gpt-4v. The authors introduce machine teaching framework focusing on the minimum information required for identifying concepts in image and coordinate formats. The results suggest that bitmap images are generally more efficient for concept identification than coordinate-based representations.

### Strengths
The approach of machine teaching to explore modality-invariant concept complexity is interesting, particularly in comparing GPT-4V's handling of bitmap and coordinate-based representations.

### Weaknesses
Most importantly, the practicality of understanding concepts explored in this paper cannot be generalized into the real-world settings, and the findings are not insightful beyond the concept understanding comparison between the image representation and stroke coordinates.

### Questions
What are the take-away insights through the analyses and results from the comparison between the bitmap and coordinate-based representations? The current LLMs implicitly learn the concepts for the given explicit supervision: next-word prediction, while the visual perception capabilities are mainly coming through from the pre-trained vision encoder. Can this study partially related with the more real-world scenarios (the way of how the model learns the concepts)?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper studies GPT4-V (a multimodal LLM) for the drawing identification task. Specifically, they compare identification accuracy for inputs that vary in terms of complexity (number of drawing strokes) and modality (visual bitmap vs. textual coordinates). For their evaluation, they select a subset of 20 concepts each with 50 associated drawings from the Quick, Draw! dataset. They find that the relative ordering of concept complexity is largely preserved across modalities.

### Strengths
- The premise of the paper, or the idea of comparing how vision-language models process analogous image vs. text inputs, is quite interesting and novel.

### Weaknesses
 - I would like to see some discussion of data filtering / quality checking of the evaluation set, given that RDP is an automated algorithm.
    - Is it possible to conduct an experiment without any RDP simplified images, e.g., for a given concept simply sampling drawings with different numbers of segments from the Quick, Draw! dataset?
- The paper mainly studies the identification accuracy of GPT4-V stratified by different factors (e.g., concept class, modality, level of complexity, relative ranking). It would be nice if it included other lines of inquiry.
    - It would be nice if the study includes additional models or some justification of why GPT4-V is sufficiently representative of “vision-language models” as described in the title. Specifically, it would be nice if the paper included an open-source model, because many aspects of GPT4-V are unknown.
    - It would be nice if the hypothesis in L15 were explored in the paper, i.e., analogous images and textual descriptions “should map to the similar area in the latent space.”

**1. Limited data filtering / quality checking of the evaluation set.**

**It is unclear whether humans can even classify some of the drawings in the evaluation set, which has been automatically generated via RDP.** While the authors note that the data has been automatically filtered by a neural network trained on the Quick, Draw!, I raise this concern due to the examples shown in Table 6 of the Appendix. Specifically, RDP can modify the images so drastically that the simplified images are indistinguishable from other class categories (e.g., the simplified "Computer" and "Door" look almost identical).

I also made the concrete suggestion that the authors conduct an experiment without any RDP generated images, to account for this potential limitation, which was not addressed. While I understand that the authors are trying to "reflect the inherent variability in the dataset while ensuring robust comparisons," I think it is still possible to conduct a reasonable evaluation by selecting a smaller subset of images per class, reducing the number of classes, or using a coarser bin width for this specific ablation.

**2. Focus is too narrow.**

While I understand that the authors have the objective of conducting a "detailed analysis with a single model to ensure clarity and depth," **its focus on identification accuracy of GPT-4V stratified by different factors seems to be narrow to provide broad impact or new insights for the ICLR community.** In particular, the name of the paper suggests that the result applies broadly to "Vision-Language Models," when given the stated research objective it should be revised to "GPT-4V". I do not understand why it would hurt the clarity or depth of the paper to include evaluations on these additional models, as it is common practice to compare against other models as a baseline or study multiple models to observe common trends in a single paper.

### Questions
- Below are a few suggested revisions to improve clarity.
    - In Figure 2, the caption could be revised to explain key terminology, e.g., the “teaching size” (also called “simplicity” / “complexity” of the image) is measured in terms of the number of segments, which is varied by the RDP algorithm.
    - I wish there was an illustration of the input and output to GPT4-V, which showcases the core details of the experiment. For example, the figure could show the input as a bitmap expressed in varying numbers of segments and the output the identification accuracy. Initially, the term “teaching size” made me think there was some learning algorithm at play (e.g., in-context examples).

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This work investigates the complexity of teaching visual concepts to large multimodal language models, focusing on how different representations affect the model's ability to learn and identify concepts. The authors assess how efficiently GPT-4V learns objects using machine teaching. The results reveal that image-based representations are generally more effective, requiring fewer segments and yielding higher accuracy. However, the relative ranking of concept complexity remains consistent across both modalities, suggesting that certain concepts are inherently easier or harder to teach, regardless of how they are represented.

### Strengths
1. The overall idea of investigating the invariance and complexity of concept representations across modalities is very interesting.
2. The experiment setting is well-presented and easy to understand
3. The description of the experiment setting and research method is very detailed

### Weaknesses
1. The experiment is only carried out on GPT-4V, which raises the question of whether the conclusion is specific to the mentioned model or the Vision-Language Models in general. A broader investigation of models such as Gemini, LLaVA, and CogVLM might strengthen the conclusion of the paper.
2. The experiment uses basic prompts to ask for recognition results without constraining the answering format. The author may consider using constrained decoding or a prompt template with a pre-defined concept set. I believe the concern of the attempts research question can simplify the experiment quite a lot (i.e. no need for finding hyponyms) without sacrificing the recognition capacity.
3. Some of the simplified sketches are not very obvious for human recognition (i.e. the simplest car in Fig 2 does not look like a car; the envelope in fig6 looks like just a square). The experiment only considers basic prompt as a zeroshot inference, which can be challenging for VLM. Something like In-context learning might be helpful to teach the concept to models.

### Questions
I'm a bit confused about why GPT4V is called learner. In the experiment, the VLM is presented with sketch and tikz code with fewer segments without an obvious "teaching" process. It looks like a zero-shot inference to me. I would appreciate it if the authors could clarify if I have any misunderstandings about the settings.

In general, I think the idea is very interesting, but the empirical result is a bit weak. In particular, about the number of models tested and the prompt used and inference strategy, such as constrained decoding, pre-defined prompt templates, and in-context learning.

### Soundness
2

### Presentation
3

### Contribution
2
