# Why Do You Answer Like That? Psychological Analysis on Underlying Connections between LLM's Values and Safety Risks

- Decision: Reject
- Avg Score: 4.67
- Scores: 6, 5, 3

## Abstract
The application scope of Large Language Models (LLMs) continues to expand, leading to increasing interest in personalized LLMs. However, aligning these models with individual values raises significant safety concerns due to harmful information correlated with certain values. In this paper, we identify specific safety risks in value-aligned LLMs and investigate the psychological principles behind these challenges. Our findings reveal two key insights. First, value-aligned LLMs are more prone to harmful behavior compared to non-fine-tuned models and exhibit slightly higher risks in traditional safety evaluations than other fine-tuned models. Second, these safety issues arise because value-aligned LLMs genuinely understand and act according to the aligned values, which can amplify harmful outcomes. Using a dataset with detailed safety categories, we find significant correlations between value alignment and safety concerns, supported by psychological hypotheses. This study offers insights into the ``black box'' of value alignment and proposes enhancing the safety of value-aligned LLMs by corresponding in-context alignment methods.
Warning: This paper contains contents that may be offensive or upsetting.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The article evaluates the safety of LLMs fine-tuned using three kinds of datasets. The main purpose is to evaluate the effect of fine-tuning to personal values of users on the models' safety. Traditional NLP tasks (Samsum and Grammar) as well as instruction fine-tuning (Alpaca and Dolly) are used as control groups to contrast the value-aligned LLMs. The safety is evaluated using four datasets. The article shows that different values have different effects on the safety dimensions. The article points out that correlations between values and safety dimensions confirm or are confirmed by the accepted psychological theories. The authors argue that the reason for certain safety violations is the value alignment. To support this claim value-based prompts are proposed which instruct the LLM not to consider the values. Additional standard mitigations are also evaluated and shown to slightly decrease the safety risks.

### Strengths
* Model safety is an important issue, and personalization is an essential context for this work. 

* The authors validate their results using established psychological theories.   

* All the main claims are backed by the results and are properly discussed

### Weaknesses
 * Minor clarity issues

In the first contribution, it is not clear whether existing theories support the value-dependent degradation or value-independent degradation of safety.

The paper shows that correlations of values with particular misbehaviors correspond to the correlations reported in psychological theory. Since the objective of the paper, as expressed in the title, is explaining "why do they answer like that," it is important to show and explain the causal relationships between the variables and not just correlations.



* Value fine-tuning is not followed/accompanied by safety rewards

LLM training methodology includes safety rewards as an integral part of the task-specific rewards. According to the standard forgetting phenomenon, fine-tuning the models on specific tasks naturally drags the model away from the preciously learned state, including stepping away from the safety optima. It may be the case that if the fine-tuning was accompanied by safety rewards, then there would be no difference between value-aligned LLMs and instruction-aligned LLMs.  


* The basic LLMs are trained to perform various tasks. If the models used were already trained with the data used as the control, then it would explain the lower impact of these data sets on safety. 

* Statistical significance is not reported for results in Tables 2 and 3.

### Questions
How can the correlation analysis show that value causes misbehavior and that the shown correlations are not a result of a confounding factor? 

Is it more challenging to keep the models within the safety boundaries while finetuning for personal values than while other domain adaptations?

Are you sure that the LLMs were not previously trained on the non-value alignment datasets used in the study? 

Is the difference between the safety degradation of Touch´e23-ValueEval and the safety degradation due to other datasets statistically significant?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper explores the relationship between value alignment and possible harms that might emerge in LLMs under psychology lens.

### Strengths
- Interesting take on value alignment in LLMs, well grounded in psychology. I particularly enjoyed reading about psychology and the results of this part.
- The experiments are extensive

### Weaknesses
 - The paper's flow is a little bit broken so it is hard to follow at certain points. The results in the middle in particular feels parachuted and out of context, while the end is what holds the essence of the paper. 
- The methodology is hard to accept and follow as it is just a list of choices without justification. It would be helpful to know why the datasets were chosen and the personalization techniques were selected, especially in the context of linking the safety alignment tasks to psychology. Maybe also adding some examples would be helpful?
- Some techniques are mentioned without explanation (e.g., VIM). VIM is a key technique in the paper, and yet, no citation or explanation provided... 
- The results in Fig 2 do not seem important enough to make the conclusions of the paper. The absolute values of the coefficients are very small, ranging from 0.01 to 0.03, which raises concerns about their practical significance. Given the potential range of coefficient values, these small magnitudes suggest that the relationships identified may not be robust or meaningful enough to support the paper's claims.

### Questions
1) Please justify the methodology: The choice of Schwartz theory, the choice of the safety tasks with respect to the psychology analysis. 
2) Please clarify the methodology
3) Please provide examples in each value rather than just numerical values, it would make the paper more solid

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper investigates the safety implications of value alignment in LLMs by analyzing how models fine-tuned to align with specific human values might exhibit increased safety risks. The authors identify certain values as being more correlated with certain categories of harmful behavior and also propose some prompt-engineering strategies to help mitigate the challenge.

### Strengths
This paper is the first comprehensive study to examine the relationship between value alignment and safety risks in LLMs, and applies psychological analysis to model output analysis. By correlating model behavior with the psychological theory of basic human values, the authors explore how aligning models with values like hedonism or power might influence their likelihood of generating particular types of unsafe responses. The correlation analysis is quite novel. The overall paper flow is clear and easy to follow.

### Weaknesses
- The entire section 4.2 is based on analysis of 2 datasets and only of 1 model and its fine-tuned versions. Therefore, it is unclear how this generalizes to different models/ datasets with more fine-grained or different harmfulness categorization.
- The paper analyzes model behavior based on psychological theories of humans, but it is unclear the validity of analyzing AI behavior through human behavior perspectives. 
- The prompt-engineering mitigation strategies are not realistic. The authors discussed that they select extreme distributions (which may not reflect actual human value system and realistic prompts to begin with). However, if this is to be incorporated in real-world systems, there needs to first be a value detector, which is non-trivial to implement with high detect accuracy. 
- The paper attributes the safety difference to value alignment, but does not include enough ablations to disentangle confounding variables. For example, the difference could be impacted by the size of the benign fine-tuning dataset, the fine-tuning method etc. These warrants more detailed study. 
- The proposed strategies also does not guard against prompt injection or other optimization based jailbreking strategies, which has a more direct impact on safety. 
- It is unclear how the psychological analysis could be incorporated from a practical standpoint for improving model safety in the real world.

### Questions
How exactly is the distribution sampling done? More explanation and detail are needed.

What about the performance of more recent models like Llama-3-8B, or other larger models? With better alignment processes and more parameters, are they better at balancing value customization and safety risks?  

What exactly does VIM entail? Does it mean value alignment via fine-tuning, specifically with the Touche23-ValueEval dataset? (the acronym was never explained in the paper either).

### Soundness
2

### Presentation
2

### Contribution
2
