# GUI-World: A GUI-oriented Dataset for Multimodal LLM-based Agents

- Decision: Accept
- Scores: 5, 6, 8, 6

## Abstract
Recently, Multimodal Large Language Models (MLLMs) have been used as agents to control keyboard and mouse inputs by directly perceiving the Graphical User Interface (GUI) and generating corresponding commands. However, current agents primarily demonstrate strong understanding capabilities in static environments and are mainly applied to relatively simple domains, such as Web or mobile interfaces. We argue that a robust GUI agent should be capable of perceiving temporal information on the GUI, including dynamic Web content and multi-step tasks.  Additionally, it should possess a comprehensive understanding of various GUI scenarios, including desktop software and multi-window interactions. To this end, this paper introduces a new dataset, termed GUI-World, which features meticulously crafted Human-MLLM annotations, extensively covering six GUI scenarios and eight types of GUI-oriented questions in three formats. We evaluate the capabilities of current state-of-the-art MLLMs, including Image LLMs and Video LLMs, in understanding various types of GUI content, especially dynamic and sequential content. Our findings reveal that vision LLMs struggle with dynamic GUI content without manually annotated keyframes or operation history. On the other hand, video LLMs fall short in all GUI-oriented tasks given the sparse GUI video dataset. Therefore, we take the initial step of leveraging a fine-tuned video LLM as a GUI agent based on GUI-World, demonstrating an improved understanding of various GUI tasks. However, due to the limitations in the performance of base LLMs, we conclude that using video LLMs as GUI agents remains a significant challenge. We believe our work provides valuable insights for future research in dynamic GUI content understanding.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The paper presents GUI-World, a dataset designed to enhance understanding with dynamic GUIs. It includes 12,379 GUI videos spanning six key scenarios (e.g., desktop, websites, mobile) and diverse tasks. The authors train and test a video model GUI-Vid on GUI-World, showing moderate performance gains and highlighting the challenges in dynamic GUI understanding.

### Strengths
This paper is novel in video understanding for GUIs, an area with limited research so far.

The dataset is large-scale and spans a wide range of GUI scenarios.

### Weaknesses
The main weakness is that the paper does not clearly demonstrate how much this dataset contributes to actual GUI agent tasks. From the examples provided, it seems more beneficial for GUI understanding rather than addressing high-level agent tasks.

### Questions
Can you show more experiments to address the issue in Weakness? Is it possible to demonstrate the capability of the model on traditional GUI grounding and agent benchmarks?

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper presents a new dataset called GUI-World for GUI understanding tasks. The datasets consists primarily of ~12k videos, with extracted keyframes corresponding to various actions across multiple platforms and scenarios including various software packages, websites, and operating systems. The dataset also supplies human+llm generated captions for UI actions and multiple choice questions for a variety of UI understanding tasks. One main contribution of this dataset over existing datasets is a greater focus on "dynamic environments" i.e. tasks that require understanding of a sequence of views of a user interfaces. 

The paper also presents GUI-vid. A version of the *VideoChat2* model from Li et al. that has been finetuned on GUI-World and demonstrates improved performance on the eval set of GUI-world that the original model and is preferred by humans in side by side comparisons. The authors note that however GUI-Vid does not outperform pre-trained frontier Vision LLMs such as GPT.

### Strengths
1. The scope of the dataset collected, both in terms of number of videos but also the annotations and task generation presented alongside. Relatively few UI understanding datasets are video based and this additional focus on the dynamic aspect of UI transitions will likely be useful to others working on this problem.
2. The evaluation of a number of contemporary multimodal large models on this dataset and insight into performance gaps.
3. The authors also go an extra step to demonstrate that GUI-world can be used to improve UI understanding capabilities via a fine-tuning experiment, though I do find this experiment somewhat limited and will comment on that below. 

Overall I lean towards accept and am open to raising my score but have a few concerns regarding presentation of the dataset and results that are detailed below.

### Weaknesses
 - **Uneven presentation of results/tasks:** The dataset can be partitioned along a number of axes, but that partitioning is not very consistent throughout the paper. The leaves certain results 'missing' given the design considerations and experimental setup presented.
	- Here are some different categorizations of tasks/queries I saw
		- Prediction, Reasoning, Captioning (Fig 3)
		- Static, Sequential, Prediction, Conversation, Reasoning, (Figure 5)
		- Free form, MCQA, Conversation (Table 2)
		- Detailed and Summarized Captioning, Static GUI content, Dynamic and Sequential GUI content (L253-L263)
		- Caption, Complex Tasks, Conversation (Table 5)
	- While i do think it is useful to have a number of orthogonal categorizations of queries in the dataset, many of these all of these are not well described/defined and having so many different ways of describing splits made it hard to follow and map these back onto results. It would be helpful if the authors had a table with definition for the major categorizations they would like readers to know about in this dataset.
	- The categorizations used should hopefully be mirrored in the metadata associated with the videos. It would be helpful for the authors to include an example metadata record (or at least the schema) for one or more videos in an appendix.
	- A gap this work is trying to address is that of dynamic environments/tasks. Yet I find the presentation of the performance difference between static vs dynamic content a bit unclear. It is presented in Table 5, but its not clear to me why "Complex Tasks" is the only thing where there is a split between Static and Dynamic (its also not very clear what "Pred" is as a category not what Complex Tasks includes). Why does Table 5 not have results for MCQA tasks? Could the authors shed a bit more light on their choices for how to organize these results?
- **The generation process for QA pairs in the dataset was not clear to me**. Could the authors briefly elaborate on Section 2.3 and  L1119-L1127 in appendix A.3. and give a step-by-step list of the process?
- **Mismatch between tabular results and conclusions for keyframe selection experiment:** It is possible I missed something so the authors should feel free to clarify, but I don't think the statement in L426-L431 *"Across both basic tasks such as captioning and more complex tasks like prediction and reasoning, significant variations are evident among keyframe selection methods. As shown in Table 22 and Table 24, GPT-4V and Gemini significantly benefit from using human-selected keyframes..."* match the results presented. 
	- As far as I can tell neither Table 22, Table 24, Table 2, nor Table 5 present Human selected keyframes with Gemini-Pro 1.5 as stated in the text. What is this referencing?
	- The random keyframe condition seems best for gemini-pro in all the tables referenced. And also for Qwen-VL-Max and GPT-4V in Table 2 and Table 21. And for GPT4V in table 24.
	- Why refer to table 22 and table 24 rather than Table 2 (or 21)?
	- Am I missing something?
- Because of the flow of the paper the impression I took away from section 3 is that GUI-vid was finetuned only on GUI-world, however from Table 12 it looks like around half of the data for stage 1 finetuning came from MetaGUI and OmniAct. It would be better to move some of this information about training datasets used up into the main body of the paper.
- No details about the evaluation protocol/setup whose results are detailed in Table 8 are given. This result is likely quite interesting to readers in addition to just the benchmark scores. It would be helpful if the authors provided some information to contextualize what prefers means in this context and how it is measured.

### Questions
- Are any parts of this dataset derived from existing datasets? The caption for Table 2 says *"For Android, we select videos from Rico"* (L162), but this wasn't really mentioned in the  data collection portion of the paper. So I just want to clarify my understanding? 
- What is the "Textual information" that is referred to in L461-462 that references Table 5. What data in the table should we be looking at to understand the conclusion in this section.
- I couldn't find Table 4 referenced anywhere in the text. Two of the conditions in this have no visual input and its not clear why. I'm not sure what the purpose of this table is? Could the authors say a bit more about what readers should take away.
-  For conversational queries, what task are the models asked to do? How are they prompted to complete this task? The example in Figure 5 doesn't make it very clear what to me what the model is supposed to do when presented with this as a query, in that example, is the model supposed to predict the User's next question? 
- L115-L1117 say that an LLM is used to reduce errors made by human annotators. What kind of errors were you seeing that needed fixing?

### Soundness
2

### Presentation
1

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper argues that "existing works" for evaluating multi-modal language models' (MMLMs') ability to perform vision-dependent tasks with graphical user interfaces (GUIs) are limited in their evaluative characteristics. To remedy this problem, the authors introduce three key contributions: 1) GUI-World,  a comprehensive GUI dataset comprising 12,379 videos specifically designed to assess and improve GUI-oriented capabilities of MLLMs, spanning a range of categories and scenarios, including desktop, mobile, and eXtended Reality (XR), and representing the first GUI-oriented instruction-tuning dataset in video domain; 2) GUI-Vid, a GUI-oriented video LLM with enhanced capabilities to handle various and complex GUI tasks;, and 3) a series of experiments that demonstrate how existing MLLMs struggle with GUI-oriented tasks and suggest that improvements in vision perception, along with an increase in the number of keyframes and higher resolution, can boost performance in GUI-oriented tasks.

### Strengths
I'd like to express my thanks to the authors. The paper was an enjoyable and thorough read.

## Overview of Strengths
- Manuscript and appendix very well-written and thorough.
- Problem is important to several areas machine learning and adjacent areas of science (e.g., human-computer interaction)
- Multiple contributions (i.e., large dataset, model, and new knowledge from several experiments)
- Comprehensive and rigorous in experimental breadth.

### 1. Manuscript Quality
The manuscript is extremely well-written and thorough in its objective. The appendix is *incredibly* thorough, and I found it challenging to identify gaps in aspects of the paper that weren't communicated in some capacity or another. I have no qualms about the paper's writing quality, though there are areas where specific phrases and word choices could be revised.

### 2. Problem Significance
The paper argues that "existing works" for evaluating multi-modal language models' (MMLMs') ability to perform vision-dependent tasks with graphical user interfaces (GUIs) are limited in two ways: (1) an inability to handle dynamic environments that involve sequential operations and (2) significantly limited support for scenarios beyond web-based environments (e.g., web browsers). An alternative (and arguably simpler) framing of the tackled problem is that current evaluation datasets fail to evaluate MMLMs in a comprehensive and robust fashion. Generally speaking, the problem is one that is recognized as being significantly important to the broader ML community.

### 3. Scope of Contributions
The paper frames its contributions around a dataset, a model trained on the dataset, and a series of experiments with the trained model. Generally speaking, I believe that the work is significant and contributes new knowledge that would be valuable not only to ICLR's community, but certainly more broadly (e.g., to the field of human-computer interaction). The work's comprehensive nature is broad in several ways (e.g., data collection, task type, evaluation, etc.). The originality and significance of these contributions is somewhat of an open question, which I discuss under Weaknesses.

### 4. Experimental Rigor
The paper employs approaches and methods that are both well-motivated and well placed in the literature for ICLR's standards. Most of the paper's methodological novelty stems from dynamic and sequential GUI content, which I find to be generally well-grounded as they're supervised, validated, and refined by human annotators. I'd argue that the data collection process itself is quite rigorous in its approach and can be viewed as a standard baseline for collecting such data. There's sufficient detail to *mostly* replicate the methodology with some exceptions.

### Weaknesses
There are two high-level weaknesses with the manuscript:
- Novelty of contributions needs clearer articulation
- Details aren't sufficiently clear for reproducibility.

## 1. Novelty of Contributions
The paper's magnitude of contributions make it challenging to assess significance and contribution as clearly as I'd like to for several reasons. 
1. The differentiation between contributions from existing literature and the trifecta of three primary contributions presented in this manuscript (i.e., dataset, model, and experiments) are simply not well articulated. The authors repeatedly use phrases such as "take the first step to". It's unclear if this is said with respect to this being the first step in accomplishing their goal within the scope of their paper or in a larger context (i.e. within the scope of the entire research community).
2. There are similar works that aren't included that are more narrow than GUI-World, but certainly have overlap with portions of the GUI-World dataset (e.g. [1]). It's unclear how GUI-World is substantially different for these areas of overlap.
There are a large family of prior works that predate MLLMs but fundamentally operate on the same basis of data collection + practical application (e.g., [2,3,4,5]). The authors should clarify their contributions in the scope of this prior work *and* integrate these clarifications into their paper.
3. The manuscript has a plethora of smaller contributions that come in the form of "small findings". For example, the notion that programmatic extraction of keyframes is disadvantageous for MMLMs is a *stellar* finding that's buried by the emphasis on other contributions more aligned to #1. I'd like to see the authors elevate their contribution clarity by surfacing these smaller findings at greater detail.
4. It's unclear if the data collection methodology itself (i.e. Steps 1 and 2 in the pipeline) should be viewed as a contribution.

[1] Chen, Wentong et al. “GUICourse: From General Vision Language Models to Versatile GUI Agents.” ArXiv abs/2406.11317 (2024): n. pag.
[2] Li, Gang, and Yang Li. "Spotlight: Mobile ui understanding using vision-language models with a focus." arXiv preprint arXiv:2209.14927 (2022).
[3] Wang, Bryan, et al. "Screen2words: Automatic mobile UI summarization with multimodal learning." The 34th Annual ACM Symposium on User Interface Software and Technology. 2021.
[4] Wang, Bryan, Gang Li, and Yang Li. "Enabling conversational interaction with mobile ui using large language models." Proceedings of the 2023 CHI Conference on Human Factors in Computing Systems. 2023.
[5] Li, Yang, et al. "Widget captioning: Generating natural language description for mobile user interface elements." arXiv preprint arXiv:2010.04295 (2020).

### 2. Detail Clarity and Reproducibility
The paper's claims hinge on methodological details that aren't well articulated. I view this as a problem that stems from the paper's scope being so incredibly large, but its a problem that must be remedied nonetheless. The following provides several pointers to areas where I needed more information to understand how the methodology should be reproduced:
1. The reliability of the LLM-as-a-Judge method is not detailed in any capacity. It is unclear how rigor and reliability were established with the method, if at all, for the scope of the authors' task.
2. The design of the process followed by student workers is not detailed. The paper states that students were provided with a "specific software task", but the set of "software tasks" is not explained in any capacity.
3. The manuscript's paragraph on YouTube Video data collection should specifically include portions of the content in A.3. that detail the search + collection process used by human collectors. Otherwise, readers would be misled to believe that the collection process was targeted at collecting videos of "specific software tasks" rather than collection tutorial videos without a specific task in mind.

### Questions
1. Provide explicit statements that indicate the significance of each of your contributions (e.g., "We are the first to do X, Y, and Z").
2. Clarify whether the data collection pipeline itself is a contribution.
3. Add appropriate citations for relevant work that you are building on *and* explicitly state how the methodology presented here is different.
4. Add additional commentary on the "smaller contributions" that as noted under "Weaknesses".
5. Incorporate all cited works mentioned in weaknesses to broaden the scope of cited prior work.
6. Include more information about the LLM-as-a-Judge method's reliability in your pipeline. (Note: To be clear, I am not looking for citations from other studies. I am seeking more data to understand that the LLMaaJ method works with your specific prompts.)
7. Replace "existing works" in the Introduction with text that is more explicit in its meaning.
8. Clearly describe and detail the process followed by student works including the specific set of tasks that were used.

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
3

### Summary
This paper introduces gui-world, a GUI-oriented dataset designed for multimodal large language model (LLM)-based agents, encompassing six distinct GUI scenarios that include videos, human-annotated keyframes, detailed captions, and a variety of question-and-answer types. The scenarios span a range of multimodal GUI environments such as desktop operating systems, mobile platforms, websites, software applications, and extended reality (XR) platforms. To handle the dynamic, sequential tasks within these environments, the authors created a pipeline for human-annotated keyframes and captioning, along with diverse Q&A generated through human-LLM collaboration. Extensive experiments demonstrate that videoChat2, trained with a two-stage training architecture, surpasses multiple existing visionLLM and videoLLM models in performance. Lastly the authors provide a number of insights that can inspire future work.

### Strengths
- Strong motivation behind the dataset collection effort, underscoring the significance of the topic.
-  A comprehensive new dataset, developed with a unique construction pipeline, to evaluate and enhance GUI-oriented capabilities in MLLMs.
-  A method aimed at improving model perception of GUI elements.
-  Thorough experiments and detailed result analysis.

### Weaknesses
1) Unclear Novelty of the Model: The novelty of the model is not well established. Although VideoChat2 is used for experiments, it’s unclear which aspects of the model or pipeline method are innovative. The model seems to closely resemble the approach in Li et al. (2023b), and the construction method appears similar to that in Lai et al. (2024). Greater justification of the model’s novelty and a clear rationale for selecting VideoChat2 would be valuable. Additionally, training and comparing models other than VideoChat2 in the same way could strengthen claims of improved GUI perception abilities in Section 3.

2) Low Clarity and Unclear Descriptions:
2-1)Table 1: While Table 1 uses check marks to indicate inclusion, more detailed quantitative and qualitative comparisons across each category would enhance clarity. For instance, some existing datasets also include websites, as indicated in Table 1, but it’s unclear how the quantity or quality of the proposed dataset compares with those.
2-2)Table 3 Results: The results in Table 3 seem selectively presented, as data for "H" in Gemini-Pro-1.5 and "R" and "E" for GPT-4o are missing. Without these results, it’s challenging to assess whether the performance gains are mainly due to human annotations or if GPT-4o is inherently a strong model without them.
2-3)Score Analysis: The authors report accuracy using the LLM-as-a-Judge approach, but score variations appear minor. Applying statistical tests could clarify which scores in the table are significantly higher.

3) Low Presentation Quality: The paper’s readability and flow could be improved to enhance presentation quality.
3-1)	Figure 2: Currently, Figure 2 lacks contextual information. Moving it to the evaluation section, along with relevant text from line 96, could make it more informative.
3-2) Mixed Results, Implications, and Limitations in Section 4.2: Separating results, implications, and limitations in Section 4.2 could improve readability. Specifically, a distinct discussion of limitations and implications would help to inspire and guide future research more effectively.

### Questions
1) Could the authors provide further justification for the novelty of the model and training method?
2) Could the authors include the missing results in Table 1, specifically"H" for Gemini-Pro-1.5 and "R" and "E" for GPT-4o?
3) Could you report which scores in the results are statistically significantly higher than others?
4) It’s unclear in the paper whether the dataset will be made publicly available. If so, could the authors specify when it will be accessible?
5) Many references include only titles without complete publication details, such as conference or journal venues, page numbers, and publication years.
6) How were keyframes randomly selected for the "Random" condition? Table 3 presents results for Random selection, but it’s not clear which method was used. Was an established random selection method applied, or was a new tailored method developed for this study?
7) In Line 205, it’s noted that “they typically underperform…” How did the authors address this limitation? If GUI-Vid exhibits this issue, an example would be helpful to illustrate.
8) The data collection reportedly covers a wide range of software and websites, but the quantity of data collected isn’t specified. To assess balance in data collection, it would be useful to include the number of samples by software and websites, such as in Figures 9 and 10.

### Soundness
2

### Presentation
2

### Contribution
3
