# Can Video LLMs Refuse to Answer? Alignment for Answerability in Video Large Language Models

- Decision: Accept
- Scores: 6, 6, 6, 6

## Abstract
In the broader context of deep learning, Multimodal Large Language Models have achieved significant breakthroughs by leveraging powerful Large Language Models as a backbone to align different modalities into the language space. A prime exemplification is the development of Video Large Language Models (Video-LLMs). While numerous advancements have been proposed to enhance the video understanding capabilities of these models, they are predominantly trained on questions generated directly from video content. However, in real-world scenarios, users often pose questions that extend beyond the informational scope of the video, highlighting the need for Video-LLMs to assess the relevance of the question. We demonstrate that even the best-performing Video-LLMs fail to reject unfit questions-not necessarily due to a lack of video understanding, but because they have not been trained to identify and refuse such questions. To address this limitation, we propose alignment for answerability, a framework that equips Video-LLMs with the ability to evaluate the relevance of a question based on the input video and appropriately decline to answer when the question exceeds the scope of the video, as well as an evaluation framework with a comprehensive set of metrics designed to measure model behavior before and after alignment. Furthermore, we present a pipeline for creating a dataset specifically tailored for alignment for answerability, leveraging existing video-description paired datasets. The code and the dataset will be publicly available.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces the concept of alignment for answerability in the context of video LLMs. Current models and data do not consider out-of-scope questions that a user might ask, and hence they don't recognize them as unanswerable. A definition and a metric to assess this phenomenon are presented. Furthermore, a new dataset is proposed containing unanswerable questions, and fine-tuning models on this dataset shows improved alignment towards recognizing unanswerable questions.

### Strengths
The paper is well-written and clearly introduces the concepts, definitions and metrics. The contribution is original as it formally recognizes a new problem, i.e. multimodal LLMs answering clearly unanswerable questions, and proposes solutions to it.
- The proposed problem framing and metric make intuitive sense. The definition takes into account the reasoning of why a question is unanswerable. The metric takes into account excessive refusal to answer which is a big problem with LLMs.
- A new dataset for alignment for answerability is presented. This is a valuable addition to the community as it creates out-of-scope QA pairs which we rarely see.
- The dataset creation process is simplistic, modifying a constrained set of objects and their relations, or changing object attributes. Furthermore, the evaluation dataset is verified manually. So, the dataset is likely dependable.
- Experimental results after fine-tuning on this dataset show clear improvements in alignment (Table 1), and the ablation study in Figure 5 outlines the drawback of an alternative.

### Weaknesses
The main weakness is that the proposed QAs in the dataset seem to be mostly geared towards detection capabilities without requiring much reasoning. This in turn makes the corresponding dataset construction, and improving model's capabilities on this axis rather easy. Some qualitative examples presented are "What breed is the cat in the video?", "What color laptop the presenter is holding?", "How many times does a person in gray shirt appear in the video?", etc. Recently, many reasoning based video-language benchmarks are proposed [1, 2] while this paper is more similar to older benchmarks [3].

Other notable weaknesses:
- The metric is rather complex. If we just want to detect unanswerable questions, and balance precision and recall, why not use F1-Score?
- The metric is defined between aligned model and unaligned model. However, if one wants to test the ability of a given model regarding unanswerable questions, the proposed metric cannot be used.
- Using LLM-in-the-loop to create the dataset may create some bias, hallucinations and incorrect QA pairs. 
- Human performance on the evaluation set is not presented.

### Questions
Can the authors provide more qualitative examples of unanswerable questions from the proposed dataset? Similarly, can we also get more qualitative examples of existing & aligned model's reactions to such questions?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper studies the phenomenon that some video language models can't refuse to answer a question when the question is irrelevant to the video. The authors first showcase such failure cases in existing VLLMs, then provide a method and metric to identify such case, and finally propose a dataset to finetune existing VLLMs to improve this issue.

### Strengths
- This paper executed a valid pipeline of improving VLLM on a task: identifying the problem, curating a dataset to fix the problem, and finetuning the model to show improvements. The paper shows a good practice on the task of introducing refusing to answer for VLLMs.

- The alignment score defined in section 4 makes sense to me.

- The authors conducted experiments on a variety number of VLLMs in Table 1.

### Weaknesses
 - My main feeling about reading this paper is I feel the problem of refusing to answer is a bit small and artificial. While showing the failure case in Figure 1, I feel it is also important to show if the problem can be migrated by explicit prompting, e.g., add to the prompt "Say 'can't answer' if you are not sure". Even though I believe the authors proposed method with finetuning on the curated dataset may still be better, I feel the problem is not as big as the author claimed.

- Adding to the above point, the authors only evaluated relatively small VLLMs in Table 1 (Video-LLaVA/ VideoChat2/ LLaMA-VID), while skipping the more recent SOTA VLLMs like Qwen2-VL, LLaVA-OneVision, and GPT-4o or Gemini 1.5. I am expecting these more well instruction-tuned models may have less answerability issues.

- If I understand correctly, the authors propose to solve the problem by finetuning the VLLM on a dataset. A clear shortcoming is that the models might drop performance on other tasks, which is not desirable. Please provide some discussion on this.

### Questions
- Overall, I feel this paper propose a valid solution to a small problem. The solution might have issues on overfitting the model on the particular task, and the problem may not exist on more modern VLLMs. My current rating is a week reject. I am happy to raise my rating if the authors address my concerns in the rebuttal.

### Soundness
3

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
4

### Summary
The paper aims to improve Video-LLMs’ capabilities of differentiating visually-unaligned questions, while maximally retain the performance on answering common answerable questions.
Specifically, the paper first defines a suite of metrics to evaluate alignment for answerability. It then collects data for both training and evaluation. The experiments show that existing Video-LLMs almost cannot refuse to answer unaligned questions. While SFT and DPO can effectively improve the overall performance, DPO significantly outperforms SFT in maintaining the models’ original performance while handling unaligned questions.

### Strengths
1.	The work is overall well-developed and shows the authors’ insights in the problem.
2.	The constructed benchmark could be valuable, with dedicated evaluation metrics and annotations (reason for unanswerable).
3.	The paper implements both SFT and DPO for improving existing Video-LLMs with the training data and shares helpful insights.

### Weaknesses
1.	The paper neglects to discuss many existing works that study the unanwerability of (V)QA models (see my attached references).

2.	It would be better to conduct more in-depth analysis to help understand what kinds of unanswerable QA are more challenging to resolve in videos: static objects/attributes/relations vs. dynamic actions.


### Questions
see weakness.

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
This paper addresses the issue of "answerability" in Video Large Language Models (Video-LLMs). Current Video-LLMs excel at answering questions directly related to the content of a video, but struggle with questions that go beyond the video's scope, often hallucinating plausible but incorrect answers. The authors propose a framework called "alignment for answerability" to train Video-LLMs to recognize and refuse to answer such unanswerable questions.

This framework involves:
- Alignment:  Training Video-LLMs to assess the relevance of a question to the video content and respond with "unanswerable" when appropriate.  They formally define this alignment process and associated scoring functions.
- Evaluation Metrics:  Beyond simple accuracy, the authors propose a set of metrics to comprehensively evaluate the alignment process. These include measuring how often the model refuses to answer valid questions (Excessive Refusal), how often it correctly answers previously refused questions (Permissiveness), and how well it identifies and declines truly unanswerable questions (Discretion).
- Dataset Creation (UVQA): The authors created a new dataset, UVQA, specifically for training and evaluating answerability.  They leverage existing video-description datasets, altering the descriptions to generate questions that are unanswerable based on the accompanying video.  They further categorize these questions based on the type of mismatch (object, attribute, or relationship).

Experiments demonstrate that models trained with this framework and the UVQA dataset significantly improve their ability to handle unanswerable questions. The authors also explore an alternative approach based on decomposing questions into multiple existence-based sub-questions (inspired by the POPE approach for image-based LLMs), but find it less effective and computationally more expensive than their proposed framework.

### Strengths
- The paper tackles an important yet often overlooked issue of answerability in Video-LLMs.
- The paper defines sound metrics and data generation pipeline.
- The results on the in-domain evaluation set are convincing, notably with a positive comparison against the POPE baseline.

### Weaknesses
 - The evaluation set is curated from the same distribution as the training set, which may overestimate the benefits and results of the alignment procedure. It would be great to see the results on a fully human-annotated set, ideally on videos from a different distribution (e.g. using videos from MSR-VTT).
- Having results on academic VideoQA benchmarks (e.g. the full Activitynet-QA evaluation set) would enable to double check the absence of accuracy degradation compared to the state of the art. Has any trade-offs between answerability performance and standard VideoQA performance been observed?

### Questions
- The approach could be extended to images in future work. Is there any challenge the authors anticipate in doing so?

### Soundness
3

### Presentation
4

### Contribution
3
