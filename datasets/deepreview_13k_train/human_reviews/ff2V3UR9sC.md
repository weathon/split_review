# Teaching Human Behavior Improves Content Understanding Abilities Of LLMs

- Decision: Accept
- Scores: 8, 8, 5, 6

## Abstract
Communication is defined as ``\textit{Who} says \textit{what} to \textit{whom} with \textit{\textbf{what} effect}.'' A message from a communicator generates downstream receiver effects, also known as behavior. Receiver behavior, being a downstream effect of the message, carries rich signals about it. Even after carrying signals about the message, the behavior signal is often ignored while training vision language models. We show that training VLMs on receiver behavior can actually help improve their content-understanding abilities. We demonstrate that training VLMs to predict receiver behaviors, such as likes, comments, and replay graphs, which are available at scale, enhances the VLM's performance across a broad range of downstream content understanding tasks. We show this performance increase over 6 types of behavior, 46 different tasks covering image, video, text and audio over 26 benchmark datasets across both 0-shot and fine-tuning settings, outperforming many supervised baselines on diverse tasks ranging from emotion recognition to captioning by upto 150\%. We note that since receiver behavior, such as likes, comments, and replay graphs, is collected by default on the internet and does not need any human annotations to be useful, the performance improvement we get after training on this data is essentially free-lunch. We also release BLIFT, our Behaviour-LLaVA IFT dataset comprising of 730k images and videos with their receiver behavior collected from multiple platforms on which we train our models to achieve this.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper proposes that using user behavior data collected from Reddit and YouTube helps large vision and language models achieve better performance across a wide range of language and visual content understanding tasks. The gains are especially more salient on the higher-level tasks such as emotion recognition, persuasion strategy classification, and question answering than the lower-level tasks like action and object
recognition. Furthermore, the ablation study demonstrates the importance of behavior data and instruction fine-tuning on behavior data.

### Strengths
1. The paper is well-motivated, highlighting the importance of leveraging user behavior data for content-understanding tasks.
2. It contributes a large-scale dataset BLIFT, consisting of 400k images and 330k videos, along with their receiver behavior, which is beneficial for research about vision language models.
3. The proposed training method has gained significant performance on a variety of vision-language tasks, which shows the effectiveness of the method.

### Weaknesses
More details of the training process can be provided for reproducibility, e.g. the average length of the text input, and how to deal with extremely long ASR results.

### Questions
NA

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
Communication consists of not only the message but also the effects it has on the receiver. However, receiver behavior is commonly ignored when training vision language models. This paper shows that training VLMS on receiver behavior such as likes, comments and replay graphs improves their performance across 46 diverse tasks. Moreover, this data is commonly collected by default (through user interactions on Reddit and YouTube) and hence does not require additional annotation. They collect and release a large scale 730k-sample dataset containing this data.

### Strengths
1.	This proposed idea of using receiver feedback relating to images/videos is novel to the best of my knowledge (which should been taken with a pinch of salt since the reviewer mostly work on text-only alignment) and is certainly worthwhile exploring since the cost of using these receiver-behavior is essentially zero compared to how much it would cost for post-collection expert human annotations.
2.	The data collection and preprocessing from Reddit and YouTube are detailedly described and carefully thought-out. I’m especially impressed by the extensive data cleaning done by the authors as well as the multitude of ways that the content behavior data can be converted to instruction tuning data.
3.	The training setup designed by the authors seem reasonable, with well-designed ablations such as matching for additional data (Ad-LLaVA) 
4.	The evaluation is done rigorously with 46 different tasks and general improvements across many of these metrics, in relation to strong baselines.

### Weaknesses
1.	The introduction claims that “behavior data is considered noise and is ignored while training large language models” (Line 50). However, this statement ignores the substantial work done in harnessing receiver-generated behavior data especially on online forums such as Reddit (through upvotes and comments), which have been used by many works including [1] and [2]. Nonetheless, I have not heard of VLMs using organic/behavioral feedback data so I would suggest the authors to acknowledge that prior work have been done for text-only settings and only claim that this is done in this paper for VLMs, which is more appropriate to the remainder of the paper.
2.	The organization for Section 3 Results and Discussion can be improved. Currently, it’s not easy to follow the main areas of improvement of the proposed methods. Because there are 46 evaluation metrics, it might be easier to follow if the results section starts with one table that shows the average gain in each task category e.g. VQA, which can be done by normalize all scores for a baseline model (e.g. LLaMa-Vid) to 100%, with the raw metrics in appendix. I would also recommend that the discussion is organized more clearly (i.e. each paragraph has one main point summarized as the paragraph heading) as it currently reads as simply describing the results and it’s hard for readers to follow along on the main insights arising from the results.

### Questions
To the best of my knowledge, platforms such as YouTube and Reddit have stringent Terms of Use requiring how such behavioral data can be used and released as a dataset. How did the authors work together with the platform to ensure that collecting and releasing this data does not breach their terms of use?

### Soundness
4

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper demonstrates hat training VLMs to predict receiver behaviors, such as likes, comments, and replay graphs, which are available at scale, enhances the VLM’s performance across a broad range of downstream content understanding tasks. Next, this paper constructs a behavior-LLaVA instruction fine-tuning dataset, and obtain the fine-tuned Behavior-LLaVA and AdLLaVA. The experiments on the fine-tuned VLMs demonstrate the effectiveness of content and behaviour, and study the different effect of perception and action behavior.

### Strengths
1. The constructed dataset could be very helpful for VLM researches.
2. The fine-tuned VLMs show improvement across various tasks.

### Weaknesses
1. The idea of the connection between VLM performances and fine-tuning on behavior data, upon which the paper is built, is questionable. The authors try to draw some analogy from relevant studies in human behavior, but fail to make a clear point with the work done in this paper (fine-tuning VLMs on behavior datasets). Also, the logic in this paper lacks clear or formal theoretical analysis on why fine-tuning VLMs on behavior datasets could improve performance, but rather just some abstract references to some concepts in the human behavior research. In this respect, the logic foundation of this paper is questionable and unconvincing.
2. The study of the connection between LLM/VLM foundation models and human behaviors is not novel. In fact, many researches [1][2][3] have been performed from various different perspectives, such as social behavior and trust behaviors. If we are to view the study on the connection of behavior with VLMs as a contribution in this paper, there are already many researches delivering similar and more comprehensive conclusions on this topic. In this sense, the authors should clearly position this paper along the research line and clearly state the difference between other related works.
3. The conclusion that learning behavior leading to learning content better is quite trivial and might not be very useful. In fact, adding more fine-tuning data of any types could lead to performance improvement on some relevant tasks. If the authors really want to make this point, they should curate the same dataset without explicitly telling VLMs what the behavior is and explore the performance of the VLM fine-tuned on this dataset.

### Questions
Any analysis on the harmfulness/trustworthiness/bias on the generated content from behavior LLaVa? The collected dataset could contain these harmful content.

### Soundness
3

### Presentation
2

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
1. This paper proposes the use of behavioral data training to enhance the content understanding capabilities of multimodal models and has collected a cross-modal dataset called BLIFT.

2. Building on LLaMA-Vid, this paper applies two different instruction fine-tuning strategies, Behavior-LLaVA and Ad-LLaVA, on the BLIFT dataset. The Behavior-LLaVA strategy leverages behavioral data, making it stronger than the Ad-LLaVA strategy, and demonstrates superior performance compared to baseline models across multiple multimodal downstream tasks.

### Strengths
1. The paper presents an innovative perspective by examining large models' understanding of data through the lens of human behavioral performance.

2. The authors have compiled a substantial multimodal dataset and fine-tuned the model from the perspective of behavioral performance, demonstrating impressive results in downstream tasks.

### Weaknesses
1. Lacks sufficient information on data collection, processing, and distribution. The description of the data collection and filtering process lacks logical coherence. The filtering appears to be largely empirical, and there is no thorough analysis of the feature distribution of the collected data, such as the distribution of topics, emotions, or object categories present in the images and videos, and how these distributions compare to the distributions in the comments. This lack of analysis makes it difficult to assess the potential biases in the dataset and their impact on the model's performance.

2. The paper fails to provide information about the specific experimental details used for instruction tuning (including in the appendix) and does not compare the changes in time efficiency resulting from tuning with additional commentary data versus without. The absence of details regarding the instruction tuning process, such as the specific prompts used, the number of training steps, and the learning rate schedule, makes it difficult to reproduce the results and evaluate the effectiveness of the proposed approach. Furthermore, the lack of a time efficiency comparison between training with and without behavioral data makes it hard to assess the practical trade-offs of the proposed method.

3. The paper states that sensor data is inferior to behavioral data based on the insufficient quantity of sensor data. It could be argued that sensor data is challenging to collect; however, comparing the quality of sensor data requires more substantial evidence. The claim that sensor data is inferior is not adequately supported by empirical evidence or a rigorous analysis of the inherent differences between sensor and behavioral data. The paper needs to provide a more nuanced discussion on the potential benefits and limitations of each data type.

4. In this paper, "Ad-LLaVa" sometimes appears as "AdLLaVa." Please ensure consistency in spelling.

### Questions
1. Did the authors consider the issue of distributional bias during data collection, and how might this impact the downstream tasks? The extent of data acquisition is also an important aspect of quality assessment. While collecting large-scale data, it's essential to consider the characteristics of the data being collected. Besides YouTube or Reddit, have other data sources been considered? In addition, please address the legality of your data acquisition and processing.

2. Please provide more experimental details, including experimental design and setup. Additionally, only the source code for llama-vid is provided—have any model improvements beyond fine-tuning been considered? The supplementary materials only include the llama-vid code, with the only visible data being a small amount of Reddit data.

### Soundness
2

### Presentation
3

### Contribution
3
