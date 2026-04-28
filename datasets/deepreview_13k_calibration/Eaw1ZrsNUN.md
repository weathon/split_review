# USDC: A Dataset of $\underline{U}$ser $\underline{S}$tance and $\underline{D}$ogmatism in Long $\underline{C}$onversations

- Decision: Reject
- Avg Score: 6.25
- Scores: 6, 8, 6, 5

## Abstract
Although prior studies have explored Stance and Dogmatism in user conversations, their datasets are constructed at the post level, treating each post as independent and randomly sampling posts from conversation threads. Thus, Stance and Dogmatism labels in these datasets cannot capture the user's opinion fluctuations expressed throughout the entire conversation context. However, identifying user's opinion fluctuations in long conversation threads on various topics can be extremely critical for enhanced personalization, market research, political campaigns, customer service, conflict resolution, targeted advertising, and content moderation. Hence, training language models to automate this task is critical. However, to train such models, gathering manual annotations has multiple challenges: 1) It is time-consuming and costly; 2) Conversation threads could be very long, increasing chances of noisy annotations; and 3) Interpreting instances where a user changes their opinion within a conversation is difficult because often such transitions are subtle and not expressed explicitly. Inspired by the recent success of large language models (LLMs) for complex natural language processing tasks, we leverage Mistral Large and GPT-4 to automate the human annotation process on the following two tasks while also providing reasoning: i) User Stance classification, which involves labeling a user's stance of a post in a conversation on a five-point scale; ii) User Dogmatism classification, which deals with labeling a user's overall opinion in the conversation on a four-point scale. The majority voting on zero-shot, one-shot, and few-shot annotations from these two LLMs on 764 multi-user Reddit conversations helps us curate the USDC dataset. USDC is then used to finetune and instruction-tune multiple deployable small language models for the 5-class stance and 4-class dogmatism classification tasks. Additionally, human annotations on 200 test conversations achieved inter-annotator agreement scores of 0.49 for stance and 0.50 for dogmatism, indicating a reasonable level of consistency between human and LLM annotations. We make the code and dataset publicly available [https://anonymous.4open.science/r/USDC-0F7F].

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces a dataset for detecting stance and dogmatism in each turn of a conversation.
The dataset is based on Reddit conversations, where each turn is a reply within a thread.
To label the stance and dogmatism of each speaker—a task with inherent subjectivity—the authors use multiple prompting schemes across different models, finalizing each label through majority voting.

### Strengths
The dataset provides valuable insights into stance and dogmatic expressions in Reddit conversations, contributing a unique resource for analyzing opinion and belief expression in online discourse.

### Weaknesses
1. Moderate Inter-Annotator Agreement: The inter-annotator agreement between human and LLM annotations could be improved.

2. Fragmented Conversations: By selecting only the top two authors’ comments, the dataset lacks conversational continuity. The two selected authors’ comments are scattered across the thread, rather than forming a cohesive conversation.

### Questions
1. The observed inter-annotator agreement between LLM-human and human-human highlights the subjectivity of this task. If these labels are treated as ground truth in experiments, might this reduce the robustness of the results?

2. Are there any qualitative examples demonstrating cases with high, moderate, and low inter-annotator agreement? These could provide insight into where the labeling approach is most and least effective.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
It is very costly to have humans annotate Reddit threads with multiple posts to label the stances and dogmatism of multiple users. 
Previous work considers posts independently, however, that is not the nature of the interaction. 

This paper looks at if LLMs can encapsulate the nuances to understand user opinions and whether their opinions shift through the conversation. 

LLMs are used to classify (1) user stances and (2) user dogmatism and express their reasoning for their classification. Every sample is annotated six times (two models x zero-shot, one-shot, and few-shot) and then the majority vote is taken. 

The paper introduces the USDC dataset that includes 1528 dogmatism samples (user-level) and 9618 stance samples. It is able to capture contextual and opinion shifts. As such it can be used as an instruction-tuning dataset or evaluation benchmark. The authors also instruction-tune and fine-tune LLMs on the dataset.

### Strengths
1. The paper is well-motivated and easy to read. 
2. The approach is straightforward and makes sense. 
3. The added qualitative analysis is very important and nice to read.

### Weaknesses
1. The majority voting conflict makes me wonder why Mistral is used at all if, in cases of conflict, the decision maker is GPT4 (which is quite a costly model)? 
2. Majority voting labels are used as ground-truth. It would be good to add experiments on what would happen if we train on unaggregated labels, as subjectivity is important in such a task.

### Questions
Why is it the case that instruction-tuning is better for stance and fine-tuning better for dogmatism?

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
3

### Summary
In this paper, the authors introduce a new dataset, named USDC.  It is as a dataset focusing on user stance and dogmatism in long conversations. Different from the previous methods based on labeling individual posts, this dataset can track changes in user opinions throughout the entire conversation, making it particularly useful for user personalization, market research, political campaigns, and content moderation. However, this paper lacks of more llms to be involved, only using Mistral Large and GPT-4, making the dataset has risk to be restricted by the knowledge in Mistral Large and GPT-4.

### Strengths
1. The article is well-written and easy for readers to understand.  

2. It contributes a novel dataset, which is a unique collection focusing on user stance and dogmatism in long conversations.  

3. Extensive experiments demonstrate that the annotations generated by LLMs are comparable to those generated by humans.  

4. Fine-tuning and instruction-tuning multiple small language models and proved the effectiveness.

### Weaknesses
1. What I am particularly concerned about is that you only used two LLMs for data annotation, which poses a risk of missing knowledge from other regions and fields, especially knowledge that other models might possess.  
2. I am also worried that in some cases, the system prompts may not be clear enough, leading to confusion in the large language models during annotation, such as inaccuracies in recognizing the author's stance.  
3. Furthermore, the models face difficulties in identifying intermediate positions and ambiguous attitudes, which can easily lead to misunderstandings of user opinions. These issues will be even more pronounced in machine-annotated data, as you may not be able to provide sufficient information.

### Questions
Please use more experiments to convince me that the weaknesses not exist.

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
Previous datasets on stance and dogmatism in user conversations are constructed at the post level. However, these datasets fail to capture fluctuations in users' opinions throughout entire conversational contexts. This paper introduces USDC, a dataset focused on user stance and dogmatism in long conversations. Inspired by the recent success of large language models (LLMs) in complex natural language processing tasks, the authors leverage Mistral Large and GPT-4 to annotate the training data for USDC. To ensure data quality, they manually labeled 200 test conversations for evaluation. They also conducted experiments to assess the performance of different models on the test set.

### Strengths
1. This paper introduces a novel dataset, USDC, which focuses on user stance and dogmatism in multi-user conversations.
2. It leverages large language models (LLMs) for efficient, scalable annotation of complex conversational data.
3. Extensive experiments are conducted using a variety of small language models.

### Weaknesses
In the experimental section of the paper, the authors often merely list the results without providing in-depth analysis of the underlying reasons. For more details, refer to the "Questions".

Q1: Line 407 "2) For both tasks, the majority voting labels as ground truth has a relatively high performance, scoring above 50% weighted F1-score across several models." This expression is not very accurate. As shown in Table 1, for the Dogmatism Classification task, only 2 out of 14 models achieved an F1-score above 50% when using majority voting labels as ground truth. In contrast, when GPT-4 FS labels were used as ground truth, 11 out of 14 models outperformed the corresponding F1-scores obtained with majority voting labels. To enhance clarity and accuracy, I recommend that the authors revise these statements to reflect the results more precisely.

Q2: Line 410 "4) For GPT-4 annotations, in most cases, SLMs finetuned with few-shot annotations outperform those trained with zero and one-shot annotations. For Mistral Large annotations, SLMs finetuned with one-shot annotations perform the best." For the Mistral Large annotations, why do SLMs fine-tuned with one-shot annotations outperform those fine-tuned with corresponding few-shot annotations? Could the authors provide a hypothesis that  might explain this counterintuitive result?

### Questions
Q1: Line 407 "2) For both tasks, the majority voting labels as ground truth has a relatively high performance, scoring above 50% weighted F1-score across several models." This expression is not very accurate. As shown in Table 1, for the Dogmatism Classification task, only 2 out of 14 models achieved an F1-score above 50% when using majority voting labels as ground truth. In contrast, when GPT-4 FS labels were used as ground truth, 11 out of 14 models outperformed the corresponding F1-scores obtained with majority voting labels. To enhance clarity and accuracy, I recommend that the authors revise these statements to reflect the results more precisely.

Q2: Line 410 "4) For GPT-4 annotations, in most cases, SLMs finetuned with few-shot annotations outperform those trained with zero and one-shot annotations. For Mistral Large annotations, SLMs finetuned with one-shot annotations perform the best." For the Mistral Large annotations, why do SLMs fine-tuned with one-shot annotations outperform those fine-tuned with corresponding few-shot annotations? Could the authors provide a hypothesis that  might explain this counterintuitive result?

### Soundness
3

### Presentation
3

### Contribution
2
