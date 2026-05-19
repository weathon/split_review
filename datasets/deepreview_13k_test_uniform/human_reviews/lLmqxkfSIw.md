# Grounding Multimodal Large Language Models to the World

- Decision: Accept
- Scores: 8, 6, 8, 6

## Abstract
We introduce \our{}, a Multimodal Large Language Model (MLLM), enabling new capabilities of perceiving object descriptions (\eg, bounding boxes) and grounding text to the visual world.
Specifically, we represent refer expressions as links in Markdown, \ie, ``\texttt{[text span](bounding boxes)}'', where object descriptions are sequences of location tokens.
Together with multimodal corpora, we construct large-scale data of grounded image-text pairs (called \textsc{GrIT}) to train the model.
In addition to the existing capabilities of MLLMs (\eg, perceiving general modalities, following instructions, and performing in-context learning), \our{} integrates the grounding capability into downstream applications.
We evaluate \our{} on a wide range of tasks, including (i) multimodal grounding, such as referring expression comprehension, and phrase grounding, (ii) multimodal referring, such as referring expression generation, (iii) perception-language tasks, and (iv) language understanding and generation.
This work lays out the foundation for the development of Embodiment AI and sheds light on the big convergence of language, multimodal perception, action, and world modeling, which is a key step toward artificial general intelligence.
Code and pretrained models are available at \url{https://aka.ms/kosmos-2}.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper introduces "KOSMOS-2", a Multimodal Large Language Model (MLLM) that has the ability to perceive object descriptions, such as bounding boxes, and ground textual content to the visual world. This is achieved by representing specific text spans, like referring expressions and noun phrases, as links in Markdown format, connecting the text to location tokens that denote the object's position. A significant dataset called GRIT, consisting of grounded image-text pairs, is constructed to train the model. This dataset is built using subsets from previous image-text pair datasets, namely LAION-2B and COYO-700M. Experimental results demonstrate KOSMOS-2's leading performance in grounding and referring tasks, as well as competitive results in traditional language and vision-language tasks. This grounding capability allows KOSMOS-2 to be used in various applications, such as grounded image captioning and grounded visual question answering. The study underscores the convergence of language, multimodal perception, and world modeling, a vital progression toward artificial general intelligence.

### Strengths
The core innovation is the method to link text spans in image captions to spatial coordinates of the objects or regions in the image. These coordinates are converted into location tokens and attached to the text span, forming a "hyperlink" that connects the image's objects or regions to its caption. When trained, KOSMOS-2 can link these text spans in generated text to specific image regions, resulting in more accurate and comprehensive vision-language predictions. The model can also identify and refer to objects using pronouns, enhancing its reasoning capabilities. 

Besides that, the paper is well written and clearly presented.

### Weaknesses
The GRIT dataset is trained on Grit together with text to image instructional dataset, and the work claims that the model maintain the conventional multimodal capability. It is important to evaluate the model on more multi understanding tasks to validate the modeling approach. The model is only evaluated on Flickr30k and VQAv2, a more comprehensive evaluation is lacking.

### Questions
Is there data cleaning process to make sure that training dataset do not contain any image from evaluation dataset?

For table 5, what's the training cost of LLM, Kosmos-1 and Kosmos-2. If LLM is trained longer and match the gpu hours of kosmos-2, will that change the results in table 5.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper presents a way to allow multimodal language models to refer to and ground objects in images. Grounded text spans are represented as [text span](bounding boxes), and similarly one could use such formats to input and output bounding boxes. A separate grounding model is used then to annotate boxes for web image-text data and Kosmos-2 is pre-trained on such image-grounded text data. Evaluation shows that the model archives zero/few-shot performance comparable to previous supervised grounding / grounded understanding models.

### Strengths
- The idea is simple and effective. Using such markdown-like formats allows the model to easily take boxes as input or output grounding boxes. The authors also spend time discussing the details in converting image-text data into such grounded data, including how to extract the correct noun chunk (Section 2), and how to convert boxes into a markdown-like format (Section 3.1), which is welcomed.

- The evaluation shows the model can handle diverse tasks: 1) accepting a phrase and outputting boxes; 2) accepting boxes and outputting descriptions; 3) classical VL tasks such as VQA and language understanding tasks.

### Weaknesses
1. Limited methodology innovation

    There is no significant methodology improvement, as outputting bounding boxes as discrete tokens has been extensively studied in prior work such as [1]. 

    [1]. OFA: Unifying Architectures, Tasks, and Modalities Through a Simple Sequence-to-Sequence Learning Framework. Wang et al., 2022.

2. Ablation study

     While the evaluation is extensive, there is no ablation study or discussion of key design choices or error analysis. Thus it is hard to draw further insights from the experiments. Below I just list a few questions that I have but I would encourage the authors to include ablation study / error analysis.

     a. How much impact does the data cleaning process (Section 2) have on the final performance? 

     b. Where does the in-context learning ability come from? Is it solely from interleaved image-text data or are in-context grounded data specifically included?

     c. Can we fine-tune Kosmos on downstream grounding tasks? If so, will the system match previous fine-tuned models?

     d. Few-shot in-context prompting results are shown only for RefCOCOg. Could we also do few-shot prompting for grounding tasks such as Flickr30K?

### Questions
Will some of the grounded data (converted from public data) be made public?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes Kosmos-2, a Multimodal Large Language Model (MLLM) that can not only do vision-language tasks based on image inputs, but also enables both inputting and outputing bounding box regions. The authors first introduce how to construct a training dataset of grounded image-text pairs, then illustrate how they enable the model to do grounding and referring by using bounding box representation as a hyperlink. The experimental results demonstrate the new grounding and referring capabilities of the model, and also comparable image understanding ability with other MLLMs.

### Strengths
1. The motivation is promising and important. By enabling MLLM to do grounding and referring, it brings more flexibility to the model and enables it to do a lot more fancy things. We can imagen how convenient it will be if users can specify a region when querying a MLLM. The paper makes a first step towards building such a model together with a training dataset.
2. Experimental results show that the model is comparable with previous MLLM on various traditional vision-language tasks, while shows new capabilities for grounding and referring.

### Weaknesses
I don't see a big weakness here. One thing is that the proposed model achieved much worse performance than the previous grounding & referrring models. Ideally, with language model's stronger language capabilities, the model should achieve better performance on these tasks. Therefore, there are still rooms here for improvements.

### Questions
I am curious about the performance of integrating an object-detection model with Kosmos-2. Say, if we provide the location of the objects for VQA tasks, what performance can the model achieve?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces Kosmos-2, a multimodal LLM-based architecture pretrained to perform object localization along standard (image-grounded) text generation. Object localization is also framed as text generation by converting bounding box coordinates to discrete tokens that are added to the language vocabulary. The pretraining data is obtained through an automatic pipeline that extracts phrase–bbox from existing large-scale image caption data. Evaluation on localization-based tasks (phrase grounding, referring expression comprehension/generation) shows that the model acquires strong zero-shot and few-shot learning abilities, while maintaining, while maintaining similar performance on other multimodal and text-only tasks as Kosmos-1 (from which the model is initialized).

### Strengths
1. The proposed pipeline to transform image captions into phrase–bbox pairs is interesting, and it holds promise for further development of data manipulation techniques to improve model performance.
2. The proposed model modifications to use the newly generated data consolidate and effectively extend previous approaches that aimed at grounding LMs by adding object location in text.
3. The resulting model obtains strong zero- and few-shot performance on grounding tasks (Sec 4.1 and 4.2), whilst generally maintaining the performance of the model it was initialized from (Kosmos-1)
4. The paper is generally well-written and easy to follow

### Weaknesses
1. While generally clear, I do not think I would be able to reproduce the pipeline of Figure 2. The submitted code does not seem to include the steps required to obtain data similar to what is in GrIT. This heavily limits the applicability of the proposed method and future comparisons that aim at improving data manipulation strategies.
2. My main concerns are related to some of the evaluation methodology and claims made in the paper. 
- (2a) While results are indeed strong for grounding and referring expressions, I disagree that “Kosmos-2 achieved impressive results on language and vision-language tasks”. The model achieves competitive performance with its baseline. 
- (2b) Using Flickr30K as captioning benchmark is suboptimal due to the small number of images (1K) – I encourage the authors to report performance on COCO, which most work uses as benchmark for captioning. 
- (2c) While the authors claim that “grounding capability born with KOSMOS-2 enables it to be applied to more downstream tasks, such as grounded image captioning, and grounded visual question answering” no such tasks are tested. An evaluation on a dataset like “VizWiz-VQA-Grounding” [1] would be appreciated towards grounding these claims. Likewise, claims about better action modeling (Conclusion) are unrelated to the proposed model.
- (2d) In Section 4.4, the authors state that “KOSMOS-2 demonstrates new capabilities when achieving comparable performance on language tasks.” This is after showing similar performance on most tasks, worse performance on CV and better performance on BoolQ and COPA. What kind of text-only capabilities are achieved by Kosmos-2? Are there patterns that allow us to pinpoint why the model performs better in these two tasks? And what about performance on CB, the drop is much larger (14.2pp) than any (or even the sum) of the gains on BoolQ and COPA.
3. Another concern that I have is about the unnecessarily claims towards world modeling and AGI. I agree that (better) grounding LLMs to vision goes towards these goals, however, I do not think this should be stressed in the title and abstract (which I invite the authors to consider modifying). While adding additional visual grounding abilities, this approach does not ground “models to the world” in a much more significantly extended way than concurrent work. This can mislead the readers, and given the increased interest in our field from the general public, I believe we researchers should not make claims stronger than needed. The paper proposes good contributions to improve visual grounding, and I think they should be framed as such.
4. The Related Work section needs substantial expansion. Discussion on models like PEVL [2] and X-VLM [3] that pretrain VLMs with object detectors are missing, as well as some of their capabilities [4]. There is also no mention of other approaches towards data curation that can improve model performance, including work like BLIP [5], VSG [6] and other relevant work in NLP [eg, 7].

---
[1] Chen et al. Grounding Answers for Visual Questions Asked by Visually Impaired People. CVPR’22.

[2] Yao et al. PEVL: Position-enhanced Pre-training and Prompt Tuning for Vision-language Models. EMNLP’22.

[3] Zeng et al. Multi-Grained Vision Language Pre-Training: Aligning Texts with Visual Concepts. ICML’22.

[4] Bugliarello et al. Measuring Progress in Fine-grained Vision-and-Language Understanding. ACL’23.

[5] Li et al. BLIP: Bootstrapping Language-Image Pre-training for Unified Vision-Language Understanding and Generation. ICML’22.

[6] Bugliarello et al. Weakly-Supervised Learning of Visual Relations in Multimodal Pretraining. arXiv 2305.2305.

[7] Lee et al. Deduplicating Training Data Makes Language Models Better. ACL’22.

### Questions
1. Can you identify any specific abilities of Kosmos-2 that lead to improvement in BoolQ and COPA? And what about systematic failures in CB?
2. In Sec 4.1.2, does the input sequence also include the token “<grounding>” after “</p>”? If not, why? If I understood well, having the token “<grounding>” would better resemble the pretraining GrIT data format.
3. Will you open-source the code to reproduce the pipeline of Figure 2 to produce dataset?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
