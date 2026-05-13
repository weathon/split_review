# Peering Through Preferences: Unraveling Feedback Acquisition for Aligning Large Language Models

- Decision: Accept
- Scores: 8, 6, 6, 6

## Abstract
Aligning large language models (LLMs) with human values and intents critically involves the use of human or AI feedback. While dense feedback annotations are expensive to acquire and integrate, sparse feedback presents a structural design choice between ratings (e.g., score Response A on a scale of 1-7) and rankings (e.g., is Response A better than Response B?). In this work, we analyze the effect of this design choice for the alignment and evaluation of LLMs. We uncover an \textit{inconsistency problem} wherein the preferences inferred from ratings and rankings significantly disagree $60\%$ for both human and AI annotators. Our subsequent analysis identifies various facets of annotator biases that explain this phenomena such as human annotators would rate denser responses higher while preferring accuracy during pairwise judgments, for a particular comparison instance. To our surprise, we observe that the choice of feedback protocol has a significant effect on the evaluation of aligned LLMs. In particular, we find that LLMs that leverage rankings data for alignment (say model X) are preferred over those that leverage ratings data (say model Y), with a rank-based evaluation protocol (is X/Y's response better than reference response?) but not with a rating-based evaluation protocol (score Rank X/Y's response on a scale of 1-7). Our findings thus shed light on critical gaps in methods for evaluating the real-world utility of language models and their strong dependence on the feedback protocol used for alignment.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper studied the two kinds of protocols used for collecting preference data: ratings and rankings. The authors found an inconsistency problem where in the preferences inferred from ratings and rankings significantly disagree 60% for both human and AI annotators. Their subsequent analysis identifies various facets of annotator biases that explain this phenomena such as human annotators would rate denser responses higher while preferring accuracy during pairwise judgments, for a particular comparison instance. Finally, they also found that the choice of the feedback protocol has a sharp influence on the evaluation of the aligned LLMs in the form of evaluation inconsistency. This highlights a challenge in designing robust evaluation protocols that mirror real-world performance.

### Strengths
- This paper studied an interesting question: the significance of Ratings versus Rankings in collecting and evaluating preference feedback. To me, this represents an essential and timely investigation.
- The findings in the paper could shed light on this question and stimulate further research.
- The paper is well structured and written. The experiments are extensive and carefully designed.

### Weaknesses
I liked this paper a lot but I do have several comments:  

- In Table 2, the authors showed that when converting the rating to ranking, there is a huge disagreement between the two different protocols. One flaw is that a proper baseline is missing here. For example, if you annotate the same examples using another batch of human or sample from the same model (GPT-3.5-Turbo) using different temperature, what would be the disagreement? I would be curious to see such a baseline as it also correlates with the main conclusion of this paper.

- This is not necessarily a weakness but given what observed in the paper, it would be great to see if the authors could take one step further to verify the root cause of the difference and try potential ways to combine the advantages of the two annotation protocols. To me, Figure 3 shows that the ranking-based protocol is more effective and robust (it yield better win rate with ranking-based evaluation protocol and smaller gap when changing the evaluation protocol). This makes sense, as in the rating protocol, the model/human only see each individual answer thus the rating is likely to be less calibrated. Also, seen from the examples in section H, the ranking protocol is likely to introduce some systematic biases. Here is my proposal: can we try the third protocol that instruct the model/human to give both ratings and rankings for either a pair of responses or a list of responses. My guess is that rating annotated in such a way will be better calibrated and the rankings will less likely to be biased.

### Questions
see weaknesses

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
This work provides an intriguing analysis of the issue of the feedback inconsistency problem, where human or model-generated evaluations can be inconsistent across different evaluation protocols (e.g., output A is better than B in pairwise evaluation while if the rating of A is lower than the rating of B). They collect 6k human feedback data under the ratings and rankings protocols, as well as model-generated feedback. They found that inconsistencies are prevalent both in human and AI evaluations. They further conduct quantitative and qualitative analyses to understand the potential factors of these inconsistencies. While such preference or rating data is essential for recent RLHF approaches as well as evaluation for open-ended generations, it is still unclear whether such data is reliable or what kind of factors affect the overall rating. This work provides an interesting analysis of this important area, and sheds light on several underexplored issues. I have several questions and concerns (e.g., inconsistencies from prior findings, validity of the final experimental), overall it has positive and good scientific contributions to ICLR.

### Strengths
- This paper provides an in-depth analysis of feedback acquisition by humans and AI, based on 6,000 human ranking and rating annotations for model responses, as well as model predictions. 
- Their analysis reveals the prevalence of feedback inconsistency issues and also provides an in-depth analysis of why it arises.
- They also found that which type of feedback data a model is trained on has strong effects on the evaluation.

### Weaknesses
I found this paper quite interesting, but the paper reports a set of many different findings, and sometimes their findings are inconsistent with the previous work. Having more detailed discussions on key findings can make this paper stronger (detailed below). I am also not fully convinced by the results of Section 5. Below, I detailed those points. 

**Lack of detailed discussions on findings and detailed annotation setup** 

Particularily Section 3 and 4 report various interesting phenomena, but some of them lack detailed explanations. For instance, 

- Section 3.1 length distributions: despite multiple papers reporting length of responses has a positive correlation with rating, the authors claim there's no difference ("we find that there is no discernible difference between the average length and average number of unique tokens of the preferred and unpreferred response in the rankings feedback collected from the humans and AI."). I wonder if the authors have any insights into this. 
- Section 4.2 Qualitative analysis: the authors say that they sampled a few inconsistent instances and asked annotators to provide explanations for the inconsistencies. I think this is an important and inconsistent analysis and the annotation protocols should be precisely documented. If the claim "the differences in the preferences of the humans while annotating for different feedback protocols played a significant role in their decision making" is based on 2-3 instances, the claim may not be fully satisfied. 

**The findings of "Alignment and Evaluation" section**

I think the findings of Best-of-n policies outperform SFT have been already reported in prior work, and evaluation inconsistency is somewhat predictable given the discussion of inconsistencies. While the second part (inconsistencies) can be novel, I am confused about the descriptions of the results. To my understanding, the finding is if we use a ranking model for Best-of-n ranking we can get higher rates when the same ranking protocol is used during evaluations. For me, it's not really surprising as the reward model is trained on the feedback data and reranks n responses at inference time, so if a model is trained on pairwise feedback data it learns to choose the response preferred in the pairwise setup. It'd be interesting if you could use the feedback data during training (e.g., PPO) and see if the trends remain as well. Yet, I am overall confused with the descriptions in these paragraphs and feel free to correct me if

### Questions
- Could you prvovide the details of human annotation process of Qualitative analysis?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper investigates two feedback protocols (rating and ranking) for the alignment and evaluation of LLMs. It collects AI feedback based on these two settings and uses them to train reward models. The reward models and the LLMs with the best-of-n policies are then evaluated on the annotations of humans and ChatGPT. It conducts a detailed analysis of the characteristics of the collected annotations. It reveals evaluation inconsistencies in which feedback protocols used in alignment algorithms have an advantage over other feedback protocols during evaluation.

### Strengths
* This paper draws attention to feedback inconsistency where the ratings and rankings disagree with each other for the 60% comparison in both humans and AI.
* This paper investigates the influence of different feedback protocols on reward functions. It sheds light on how we should collect feedback.
* This paper collects human feedback and AI feedback and conducts a detailed analysis from different aspects.

### Weaknesses
 * This paper does not explore the influence of feedback protocols on common alignment methods (such as RLHF[1], RRHF[2], RLAIF[3], etc.). The alignment in this paper just applies the reward models to select the best out of n generation, which is only affected by the performance of reward models.
* The evaluation inconsistency seems straightforward: the performance of reward models will be affected by the format of input data. It is better to convert the rating feedback to the ranking format first and then use it to train an NLL reward model (just like the ranking feedback) and then compare the performance.

### Questions
* Can you explore how the feedback protocol affects the reinforcement learning finetuning for model alignment, such as RLHF?
* Will the collected feedback be released?
* Is there any calibration on the rating scores? For example, detail the meaning of each score (1-7) in the prompt for AI feedback and instruction for human annotation to make sure that the annotators can fully understand the principle of evaluation.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies the two types of feedback, collecting ratings versus rankings, from both human annotators and AI as an annotator. The authors analyzed both types of collected feedback, observing general inconsistency, and also used them to train reward models, finding that the choice of feedback protocol affects the effectiveness of the reward model (where the trends hold across both human and AI feedback).

### Strengths
- This paper studies an important problem of understanding the effect of different kinds of human feedback and how they can be used in the training pipeline. 
- The findings, which apply to both human and AI annotations could be useful for informing how people design feedback protocols in the future.

### Weaknesses
In general, the specific details surrounding experimental design were not as well justified, making it difficult to assess the applicability of the findings more broadly. For example, 
- Why were Dolly, User-orient, and SuperNI selected as the tasks of interest? 
- What was the prompt provided for AI annotation? Given the subjectivity of the task, what instructions were given to the crowdworkers when asked to provide ratings / rankings? This is important to justify because the text mentions that crowd workers perceived a response to be “dull”, though it’s not clear what kind of metric crowd workers are / should be using.
- Additionally, the generalizability of the results may be limited by the choice of model in the various experiments: (1) only Alpaca-7b was tested in terms of generating candidate responses, (2) only GPT-3.5-Turbo was evaluated as an AI annotator, (3) only LORA Alpaca-7b was selected as the reward model, and (4) win-rate was computed only against DaVinci-003. It would be helpful for the authors to clarify why those models were selected in each part of the paper.

### Questions
- How would results in Figure 3 differ across tasks?
- In Section 2.2 and 2.3, it would be helpful for authors to add references for each to help the reader get a sense of where the protocols and models have been used in prior work.
- Some typos, e.g., missing link in the first paragraph of Section 3 and “the humans 6k instances of annotations”.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good
