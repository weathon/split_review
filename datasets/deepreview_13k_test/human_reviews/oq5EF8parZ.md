# Sparkles: Unlocking Chats Across Multiple Images for Multimodal Instruction-Following Models

- Decision: Reject
- Scores: 5, 6, 5, 6

## Abstract
Large language models exhibit enhanced zero-shot performance on various tasks when fine-tuned with instruction-following data. Multimodal instruction-following models extend these capabilities by integrating both text and images. However, existing models such as MiniGPT-4 and LLaVA face challenges in maintaining dialogue coherence in scenarios involving multiple images. A primary reason is the lack of a specialized dataset for this critical application. To bridge these gaps, we introduce \textbf{\OurData{}}, the first machine-generated dialogue dataset tailored for word-level interleaved multi-image and text interactions. Furthermore, we construct \textbf{\OurEval{}}, a GPT-assisted benchmark for quantitatively assessing a model's conversational competence across multiple images and dialogue turns. We then present \textbf{\OurModel{}}, a multimodal instruction-following model for open-ended dialogues across multiple images. Our experiments validate the effectiveness of training \OurModel{} with \OurData{} based on MiniGPT-4 and LLaVA-v1.5, which enhances comprehension across multiple images and dialogue turns, and does not compromise single-image understanding capabilities. Qualitative evaluations further demonstrate \OurModel{}'s generality in handling real-world applications.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work introduces SparklesChat, a multimodal instruction-tuned model designed to effectively engage in dialogues that encompass multiple images. Additionally, the constructed multi-image dialogue dataset and an evaluation benchmark are introduced.

### Strengths
This work focuses on a new scenario that is not well-explored by current large multimodal models, i.e. multi-image multimodal dialogue. 

This work propose new training data, evaluation benchmark, and model for this scenario, which exhibit better performance than MiniGPT-4.

### Weaknesses
**1. The data construction process seems too trivial and not sound.** 

In the data construction process to generate visual dialogue with multiple images, you provide multiple image-text pairs and ask GPT-4 to link them together, which I think is the simplest way to construct multi-image dialogues. 

Besides, this simple approach fails to yield effective samples. In Figure 3, the response from GPT-4 seems too naive, *i.e.*, in image #1, we see ..., in image #2, we witness..... This is just a concatenation of descriptions of two images.

**2. Insufficient experiments.**

I think current experiments cannot form a strong foundation to support the effectiveness of your model and training data.

* Baselines. You compare your method only with MiniGPT-4, which in my understanding is an embarassingly weak and simple model & dataset. More comparisons are definitely needed.

* Evaluation benchmarks. You use three benchmarks for evaluation, BISON, NLVR2, and your own evaluation data. Among them, BISON and NLVR2 are not commonly used benchmarks now. Besides, on your own evaluation data, you claim your performance apporach GPT-4. However, your self-constructed training data could share similar distribution to you eval data. To this end, I think this claim cannot well establish.

### Questions
More solid experiments could be helpful.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper presents SparklesChat, a multimodal instruction-following model for open-ended dialogues across multiple images. It introduces SparklesDialogue, a specialized machine-generated dialogue dataset, and achieves superior performance compared to MiniGPT-4 on vision-language benchmarks. SparklesChat's effectiveness is further demonstrated by its high score on SparklesEval, a benchmark for assessing conversational competence across multiple images and dialogue turns.

### Strengths
1. The paper addresses a key limitation in the field by introducing SparklesChat, a multimodal instruction-following model that integrates multiple images at the word level. This fine-grained integration of images and text is a novel approach that mimics natural human communication more closely.

2. The paper presents SparklesDialogue, the first machine-generated dialogue dataset designed for word-level interleaved multi-image and text interactions. The dataset is constructed from different image and description sources, ensuring greater robustness and diversity. Additionally, the paper introduces SparklesEval, a comprehensive scoring system that quantitatively evaluates the model's conversational competence in multimodal, open-ended dialogues.

3. The SparklesEval benchmark shows that SparklesChat's conversational competence significantly surpasses MiniGPT-4 and approaches the performance of GPT-4. These results highlight the potential of SparklesChat in real-world scenarios.

### Weaknesses
Considering the current status of single-image comprehension, which still requires further advancements, it appears that addressing scenarios involving multiple images may not be an immediate priority. Additionally, when considering the data construction approach described in the paper, it becomes evident that the model's capabilities are still constrained by the limitations of single-image understanding.

In my personal opinion, focusing on improving single-image comprehension would be more beneficial at this stage. Once single-image understanding is well-established, the demonstrated ability to handle multiple images, as showcased in the paper, should not pose significant challenges. It is crucial to ensure a solid foundation in single-image comprehension before delving into more complex scenarios involving multiple images.

### Questions
1. How do the Dialogue Demonstrations contribute to the data quality and diversity?
2. Considering the impressive performance of GPT-4 with ground truth (gt) annotation, could the authors provide a baseline using a strong caption model with an instruction-tuned Language Model to address the challenges raised in the paper?
3. Does the model in the paper have the capability to handle scenarios with more than two images, considering that the paper only showcases examples with two images?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper introduces SparklesChat, a multimodal instruction following model for open-ended dialogues across multiple images. This is MiniGPT4 fine-tuned on the machine-generated dialogue dataset released in the paper called SparklesDialogue. This contains word-level interleaved multi-image and text interactions with up to 3 images during the first turn and 1 image during the second turn. SparklesDialogue consists of two subsets: 1) SparklesDialogueCC which contain images from CC3M and captions generated by MiniGPT4 2) SparklesDialogueVG which contain images from Visual Genome and descriptions from GPT-4, based on human-annotated captions, objects, and regions. SparklesEval is a new GPT-assisted benchmark with 150 dialogs, introduced to assess conversational competence across multiple images and dialogue turns, through criteria such as Image Understanding & Reasoning, Cross-Image & Cross-Turn Coherence, and Relevance & Completeness of Responses. SparklesChat outperforms MiniGPT-4 and gets marginally close GPT-4 on binary image selection task and the NLVR2 visual reasoning task. The paper contains ablation study on the effect of dialog turns and SparklesDialogue subsets during training.

====

Updated final rating form 3 to 5 due to demonstration of improvement on LLaVA as well. The experiments section and total contributions are still weak.

### Strengths
1.	New dataset SparklesDialogue for word-level interleaved multi-image and text interactions
2.	New benchmark SparklesEval for word-level interleaved multi-image and text interactions
3.	Demonstration of improved performance over MiniGPT4

### Weaknesses
1.	SparklesDialogue contains subset SparklesDialogueVG, which was generated using GPT-4. The paper compares with performance of GPT-4 (method used to create the data set is also being evaluated on), while still performing worse although SparklesChat uses much richer image embedding. 
2.	No contribution in terms of novelty architecture. Main contribution is in the data set. 
3.	Only two turns per sample in the dataset. Longer sessions are probably more practical than more images per turn and limiting to just 2 turns. Dataset (that too, machine-generated) being the highlight of this paper, would have expected more.
4.     Not clear how this extends to other approaches such as LLaVA. Results are shown only for Min-GPT4 extension.

### Questions
Q1) Section 5.2 mentions, SparklesDialogueVG and SparklesEval use the same sources of images and captions. This is suspected to be one of the reasons why model trained on SparklesDialogueVG performs better than model trained on SparklesDialogueCC. Isnlt this a serious issue, especially since SparklesDialogueVG is claimed to be the high quality subset?

Minor typo
1.	Table 2: Column title should be A2 under “Turn two”

### Soundness
2 fair

### Presentation
3 good

### Contribution
1 poor

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work studies the open multimodal dialogue following user instruction in the conversations of multiple turns with multiple images. This work achieves this from three directions by proposing a model (SparklesChat), a dataset (SparklesDialogue), and a benchmark (SparklesEval). It also performs experiments on SparklesEval, the BISON binary image selection, and the NLVR2 visual reasoning task, on which SparklesChat outperforms MiniGPT-4 significantly.

### Strengths
1. This is one of the first works that studies multiple turns with multiple images for the open multimodal dialogue. Thus, it can additionally evaluate cross-image and cross-turn coherence and completeness of responses.

2. It contributes a novel dataset named SparklesDialogue leveraging GPT-4.

3. This work also proposes GPT-assisted evaluation named SparklesEval that can automate quantitative evaluation of a model’s conversation across multiple images and dialogue turns.

4. The Appendix and the supplementary material is helpful and very thorough.

### Weaknesses
1. It only consider two images per context, which could be too structure with little diversity.

2. The SparklesChat model is not novel in that it is just an instruction tuned miniGPT-4. It could be removed from contributions. 

3. As described in Table 1, SparklesDialogue is not large-scale. 

4. Each conversation seems to have a very typical pattern with two images as described in section 2.  
“In the first turn, the user initiates a reasonable and creative message regarding some images. In response, the assistant generates detailed answers that include comprehensive reasoning regarding the visual content. In the second turn, the user introduces a new image for further discussion, referencing both the new and previous images.”

5. Only the miniGPT-4 is compared as a baseline.

### Questions
1. Why only the two datasets - BISON and NLVR2 are chosen? Is there any other dataset to use?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
