# BIG5-CHAT: Shaping LLM Personalities Through Training on Human-Grounded Data

- Decision: Reject
- Avg Score: 5.25
- Scores: 5, 6, 5, 5

## Abstract
In this work, we tackle the challenge of embedding realistic human personality traits into LLMs. Previous approaches have primarily focused on prompt-based methods that describe the behavior associated with the desired personality traits, suffering from realism and validity issues. To address these limitations, we introduce \bigfivechat{}, a large-scale dataset containing 100,000 dialogues designed to ground models in how humans \textit{express} their personality in text. Leveraging this dataset, we explore Supervised Fine-Tuning and Direct Preference Optimization as training-based methods to align LLMs more naturally with human personality patterns. Our methods outperform prompting on personality assessments such as BFI and IPIP-NEO, with trait correlations more closely matching human data. Furthermore, our experiments reveal that models trained to exhibit higher conscientiousness, higher agreeableness, lower extraversion, and lower neuroticism display better performance on reasoning tasks, aligning with psychological findings on how these traits impact human cognitive performance. To our knowledge, this work is the first comprehensive study to demonstrate how training-based methods can shape LLM personalities through learning from real human behaviors.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper tries to embed realistic human personality traits in LLMs.

1. The paper releases a dataset, Big5-chat, consisting of 100k synthetically generated dialogues.
2. The paper shows that it can outperform earlier prompting based personality induction techniques in personality assessment tests.
3. The paper shows interesting experiments correlating personality with reasoning capabilities.


I have the following questions and suggestions. I am open to modifying my review based on the authors' rebuttal:


1. Line 192 - Equation-1: This seems incorrect. In Line 196, it states "γ = 1 fully adopting the expert generator’s logits." I believe the equation either needs to be converted to the form γ*z_base and (1-γ)*z_expert, or Line 196 should be revised.

2. I could not understand the argument of Table-1. The classifier is trained on the PsychGenerator dataset. The generator too is trained on the PsychGenerator dataset. 

    a. The table shows that a classifier thinks that the generator (after training on the PsychGenerator dataset) is able to fool the classifier effectively. Isn't that expected? If the claim is that the generator has learned to generate text that can mimic different personalities, why not train the classifier on a different dataset and then demonstrate the generalization capabilities of the generator?

    b. Additionally, in Table-1, despite training on the same dataset, the accuracy difference is not substantial (1.7% difference between the base model and the trained one vs. 13.5% difference between real data and the trained generator).

    c.  Also, the PsychGenerator dataset is composed of Facebook posts, which severely limits the applicability of the claims made in the paper. Can the authors conduct or have they conducted any study to test the generalizability of the claims made in the paper (L96-L105) to domains other than Facebook?


3. L214-215 - I would like to understand if the method generates/extracts text with only one trait (e.g., neuroticism), or did the authors attempt to mix traits? While personality traits can appear independently, there is ample literature supporting the observation of mixed personality traits, such as agreeable and neurotic individuals.

4. Re L100 - Did the authors try experimenting with combining SFT (and DPO) with prompting to improve their scores further? 


5. Regarding Table-2 and Section 5.2:
    a. SFT and DPO are supervision-heavy techniques, whereas prompt-based methods require much less supervision. Given the data requirements, it is not surprising that they perform better than prompting. A better comparison would be to see if, after SFT/DPO, the trained models can outperform GPT/Claude. This would be similar to the experiments conducted in [1], where it was shown that fine-tuned models perform much better than closed-source models (and also their base models).
    b. Given that prompt-based techniques use much less data than SFT/DPO, can the authors try rotating the examples provided in the prompts? This might improve its performance relative to SFT. (If they have already done this, please indicate this to me.)

6. Regarding Line 457, "somewhat align": Can the authors compute the degree of alignment?

7. Regarding Section 5.3: I am unclear about the motivation for this experiment. The paper begins with a very useful and interesting motivation (Lines 31-36) of making LLMs output more authentic for conversational tools and addressing mental health problems, but this was not followed up in the subsequent sections. Section 5.3 is an interesting experiment, but what is its purpose as an evaluation? While reasoning (or other capabilities) may be correlated with personality traits, how can we utilize this? Additionally, why limit the evaluation to reasoning capabilities, and not extend it to other NLP benchmarks?


[1] Large Content and Behavior Models: https://openreview.net/forum?id=TrKq4Wlwcz

### Strengths
Indicated in the summary section

### Weaknesses
## Review

### summary:
 The paper tries to embed realistic human personality traits in LLMs.

1. The paper releases a dataset, Big5-chat, consisting of 100k synthetically generated dialogues.
2. The paper shows that it can outperform earlier prompting based personality induction techniques in personality assessment tests.
3. The paper shows interesting experiments correlating personality with reasoning capabilities.


I have the following questions and suggestions. I am open to modifying my review based on the authors' rebuttal:


1. Line 192 - Equation-1: This seems incorrect. In Line 196, it states "γ = 1 fully adopting the expert generator’s logits." I believe the equation either needs to be converted to the form γ*z_base and (1-γ)*z_expert, or Line 196 should be revised.

2. I could not understand the argument of Table-1. The classifier is trained on the PsychGenerator dataset. The generator too is trained on the PsychGenerator dataset. 

    a. The table shows that a classifier thinks that the generator (after training on the PsychGenerator dataset) is able to fool the classifier effectively. Isn't that expected? If the claim is that the generator has learned to generate text that can mimic different personalities, why not train the classifier on a different dataset and then demonstrate the generalization capabilities of the generator?

    b. Additionally, in Table-1, despite training on the same dataset, the accuracy difference is not substantial (1.7% difference between the base model and the trained one vs. 13.5% difference between real data and the trained generator).

    c.  Also, the PsychGenerator dataset is composed of Facebook posts, which severely limits the applicability of the claims made in the paper. Can the authors conduct or have they conducted any study to test the generalizability of the claims made in the paper (L96-L105) to domains other than Facebook?


3. L214-215 - I would like to understand if the method generates/extracts text with only one trait (e.g., neuroticism), or did the authors attempt to mix traits? While personality traits can appear independently, there is ample literature supporting the observation of mixed personality traits, such as agreeable and neurotic individuals.

4. Re L100 - Did the authors try experimenting with combining SFT (and DPO) with prompting to improve their scores further? 


5. Regarding Table-2 and Section 5.2:
    a. SFT and DPO are supervision-heavy techniques, whereas prompt-based methods require much less supervision. Given the data requirements, it is not surprising that they perform better than prompting. A better comparison would be to see if, after SFT/DPO, the trained models can outperform GPT/Claude. This would be similar to the experiments conducted in [1], where it was shown that fine-tuned models perform much better than closed-source models (and also their base models).
    b. Given that prompt-based techniques use much less data than SFT/DPO, can the authors try rotating the examples provided in the prompts? This might improve its performance relative to SFT. (If they have already done this, please indicate this to me.)

6. Regarding Line 457, "somewhat align": Can the authors compute the degree of alignment?

7. Regarding Section 5.3: I am unclear about the motivation for this experiment. The paper begins with a very useful and interesting motivation (Lines 31-36) of making LLMs output more authentic for conversational tools and addressing mental health problems, but this was not followed up in the subsequent sections. Section 5.3 is an interesting experiment, but what is its purpose as an evaluation? While reasoning (or other capabilities) may be correlated with personality traits, how can we utilize this? Additionally, why limit the evaluation to reasoning capabilities, and not extend it to other NLP benchmarks?


[1] Large Content and Behavior Models: https://openreview.net/forum?id=TrKq4Wlwcz

### soundness:
 3

### presentation:
 3

### contribution:
 2

### strengths:
 Indicated in the summary section

### weaknesses:
 Indicated in the summary section

### questions:
 Indicated in the summary section.

### flag_for_ethics_review:
 ['No ethics review needed.']

### rating:
 5

### confidence:
 4

### code_of_conduct:
 Yes

### role:
 Review

### Questions
Indicated in the summary section.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper tackles the problem of embedding personality traits into LLMs. To this end, the authors propose: 
- A novel large-scale dataset, BIG5-CHAT, of 100000 dialogues which grounds real human personalities in text. To generate the dataset they combine controllable text generation models with a domain-specific, personality-annotated dataset. They propose a classification-based evaluation to address to which extent the proposed generation framework is capable of embedding the personality traits within the text.
- The authors test the BIG5-CHAT over two instruction-based models, i.e. Llama-3-8B and Llama-3-70B under three main learning strategies: traditional prompting techniques (zero-shot and few-shot), Supervised Fine Tuning (SFT), and Direct Preference Optimization (DPO).
- The authors provide a comprehensive empirical investigation into how personality traits affect performance in both social reasoning and general reasoning tasks testing the different model’s configurations over ad-hod benchmarking datasets.
	
Results show that:
- The dataset produced using controllable text generation not only achieves a higher average accuracy score but also provides a more balanced performance across all five personality traits.
- For Llama models both prompting and training techniques (SFT, DPO) successfully reflect the personality traits in their responses. However, training-based methods indicate more personality traits than prompting techniques. 
- When testing the reason capabilities of the models, SFT consistently outperformed or matched DPO, and both training methods outperformed prompt-based approaches.
- LLMs trained with higher levels of conscientiousness and agreeableness excel in various reasoning tasks, while models with lower extraversion and neuroticism performed better at all reasoning tasks.

### Strengths
The paper is well-written, clear and easy to follow.

The literature review is comprehensive of both studies from cognitive science and computer science and provides a complete and clear picture of the state of the art, and the limitations that the current NLP field is facing in the paper’s domain. 

The authors propose a novel dataset and creation strategy that can be beneficial not only in the field of persona-based LLMs but can also be applied to other fields, for the creation of ad-hoc data that need to embed specific characteristics in the generation.

Moreover, the evaluation proposed both for the quality assessment of the dataset and the experiments proposed is solid and comprehensive, by taking into account not only different training strategies but also assessing the model’s capabilities over a wide range of reasoning tasks.

### Weaknesses
The description and discussion of the results should be more detailed and closely tied to the data presented in the tables. For instance, statements such as “When comparing trait levels, models with higher conscientiousness and agreeableness generally outperformed those with lower levels” or “indicating that certain personality trait levels can improve performance in reasoning tasks” are either difficult to verify directly from the provided data or are too vague. To address this, I recommend emphasizing the specific results that illustrate these points by using bold text or guiding the reader to the relevant findings within the tables. Additionally, the authors offer a more comprehensive analysis of Llama-3-8B in the Appendix compared to Llama-3-70B in the main text.

Besides these, I will list hereafter small changes that I believe would benefit the paper:

- [Figure 1] Add a reference to the Figure within the text and detail the caption with a brief description of the modules depicted.
- [Section 4.2] Token analysis: missing description of the tokenization process. What were the token units employed? Words, or LLM 
tokens? Which tokeniser did you use for the analysis?
- [Section 4.3, line 300] In context-examples: how were they chosen and how many were used? Which prompt was employed? While the prompt provided in Appendix B.3 might address some of these questions, it is not referenced within the main text. Additionally, this appendix section appears somewhat disorganized, lacking clear references to the main text and presenting prompts in a different order. I suggest restructuring this appendix section for better clarity.
- [Table 3] The arrows in the header are all in the same direction. Consider providing more details in the caption in order to better interpret the Table and the results.
- [Appendix B.4] The first part of the section is confusing and there are repeated concepts. Maybe some draft sentences were not commented out. (e.g., “We follow lm harness and Deepseek for their implementations of evaluation on the general benchmarks and social benchmarks.”, followed by “We followed the evaluation frameworks established by the Language Model Evaluation Harness (lm-eval-harness) and DeepSeek for assessing performance on general and social benchmarks. Our evaluation pipeline utilized the following key parameters”).

Moreover, the authors did not provide references (and descriptions) for “Language Model Evaluation Harness” and “DeepSeek”.  
[Appendix D.3 and D.4] Consider incorporating some of these findings into the main body of the paper to provide the reader with a comprehensive overview of the LLMs’ capabilities for both models under analysis. Additionally, ensure that the main text offers the same level of detailed description for Llama-3-70B as it does for the other models.

### Questions
[Appendix B.1] “We structure the labels for the expert generator training data into three equidistant thresholds”. The process is not very clear. How did you pick the thresholds? Did you discard the data whose value was in the middle? I believe more details would be beneficial for the reader, and maybe also an example.

In Table 1, the authors evaluate the quality of the generated dataset using their proposed framework against two other prompted LLMs. The average performance shows that the Generator method outperformed the others and provides more balanced performance across different traits. However, for individual traits like Extraversion, Agreeableness, and Neuroticism, the two prompted models outperform the Generator. How can you explain these results? Did you perform an empirical evaluation of the generation to better understand the reasons for this behaviour?

### Soundness
3

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
5

### Summary
Challenges:
1. Existing methods rely on prompting models with descriptions of behaviors associated with personality traits. These behavioral descriptions are nonsensical for text-based LLMs, failing to ground their personality in realistic patterns of how humans’ personality is expressed in text.
2. The scarcity of large-scale, human-generated datasets annotated with personality traits has hindered the exploration of training-based approaches, limiting most prior research to prompting-based methods.

To address these challenges, this paper introduces BIG5-CHAT, a large-scale dialogue responses dataset that is designed to capture Big Five personality traits within diverse social interactions. Also, leveraging the dataset, this work empirically investigates if training-based methods benefit in grounding in real human data compared to traditional prompting methods.

### Strengths
- The paper is clearly written and easy to understand.
- Background section is thorough and well-written that helps the reviewers to understand more deeply about the domain and the current challenges.

### Weaknesses
 - **Although the motivation for the work is convincing, contribution is comparatively trivial.** Much of their dataset and framework are adopted from previous works, with only slight change. Also, the necessity of conducting alignment comparison experiment only on their dataset is unclear. Is there a specific reason or intention as to why the authors did not experiment on existing datasets?
- **The argument that BIG5-CHAT captures personality traits better than other datasets is not convincing.** In line 265, the authors argue their dataset captures personality and nuances better than other datasets. However, the provided table (Table 8) does not demonstrate the argument. Human evaluation, or at the very least, case study for comparing BIG5-CHAT over other datasets is required. Also in experiments, the authors did not conduct experiments on other datasets, leaving the validity of the dataset in question.
- **This work fails to capture all traits comprehensively.** The proposed method, DExperts, induces each personality trait in a response. However, in reality, the personality of a human is very complex and comprehensive. It is doubtful that their approach, as opposed to their statement of “capturing nuanced expression of personality traits”, can truly reflect human personality more elaborately. 
- **Related work section could include more works.** Although a considerable portion of the work deals with alignment methods, review on works that concerns effectiveness of training-based methods in inducing personality, or let alone works on alignment, are nowhere to be seen.

### Questions
- line 363-367: Does this mean that personality traits are evaluated by humans using questionnaires? If so, the authors should provide details on evaluator recruitment. 
- (Related to third weakness) Have the authors considered combining all traits in a single response, like combining all five expert logits into one combined logit (in Equation 1)? 
- line 420: The authors said that they excluded results for instruction-based prompting on Llama-3-8B-Instruct. However, Table 2 reports Prompt-Inst and excludes Prompt-Demo. Which is correct? There must be a clarification on this.
- Experiments: In my opinion, experimenting SFT, DPO and prompting on other datasets (the ones that you mentioned as failing to ground human personality realistically) is necessary to prove the effectiveness of training-based methods for inducing personality traits. In that case, the authors will be able to demonstrate the effectiveness of training methods, as well as excellence of their dataset over others.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The paper presents BIG5-CHAT, a dataset of 100,000 dialogues for simulating realistic human personality traits. The authors leverage two datasets, PsychGenerator and SODA, to generate BIG5-CHAT with DExperts framework and train LLMs on realistic personality patterns. The experiments show that training-based methods outperform prompting methods on personality assessments. Other experiments also reveal the personality traits of LLMs have influence on behaviors in various reasoning tasks, which align with human cognitive tendencies observed in psychology.

### Strengths
Originality: The BIG5-CHAT dataset is novel and represents a valuable resource for advancing human-like LLM research.

Quality: The experiments are well-designed and comprehensive. The results on several benchmarks are also aligned well with psychology researches.

Clarity: The paper is easy to follow, with clear explanations of the methods and concepts.

Significance: The paper provides a new dialogue dataset with personality traits. Some findings show the impacts of personality traits in different benchmarks.

### Weaknesses
Absence of Human Evaluation: To enhance the validity of personality alignment claims, human evaluations are recommended. A suggested methodology is to have a panel of human raters assess a sample of dialogues from BIG5-CHAT, scoring them on each of the Big Five traits (Openness, Conscientiousness, Extraversion, Agreeableness, Neuroticism). The human ratings can then be compared to the intended trait levels to verify if the model successfully conveys the intended personality traits.

Limited Novelty: Although this paper introduces the BIG5-CHAT dataset and applies training methods like SFT and DPO for personality alignment, prior work has shown that it is possible to train LLMs to exhibit specific personality traits, e.g., https://arxiv.org/pdf/2312.12999. In this paper mentioned above, they collected data of different MBTI types and trained 16 agents. These agents can chat in the way of certain personality trait and have the ability to pass the MBTI test. Additionally, the method of generating personality-aligned responses is adapted from DExperts. To strengthen the novelty, it would be helpful if the authors provided a clearer comparison to existing work, particularly in how their dataset creation or methodology differs. Emphasizing unique aspects, such as the integration of PsychGenerator and SODA datasets or specific adjustments to the DExperts framework for personality traits, would clarify the innovative contributions of this study.

### Questions
Question 1: How do you interpret the results of Table 1, in which the proposed method is not as effective as two baseline models in "Agreeableness" and "Neuroticism"? What makes the difference between these traits?

Question 2: How do you determine the scaling factor \gamma? How much does this factor influence the generated results?

### Soundness
3

### Presentation
4

### Contribution
2
