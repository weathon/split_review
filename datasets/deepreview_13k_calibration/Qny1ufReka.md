# Refusal Tokens: A Simple Way to Calibrate Refusals in Large Language Models

- Decision: Reject
- Avg Score: 4.20
- Scores: 6, 3, 3, 6, 3

## Abstract
A key component of building safe and reliable language models is enabling the models to appropriately refuse to follow certain instructions or answer certain questions.
We may want models to output refusal messages for various categories of user queries, for example, ill-posed questions, instructions for committing illegal acts, or queries which require information beyond the model's knowledge horizon.
Engineering models that refuse to answer such questions is complicated by the fact that an individual may want their model to exhibit varying levels of sensitivity for refusing queries of various categories,
and different users may want different refusal rates. 
The current default approach involves training multiple models with varying proportions of refusal messages from each category to achieve the desired refusal rates, which is computationally expensive and may require training a new model to accommodate each user's desired preference over refusal rates.
To address these challenges, we propose refusal tokens, one such token for each refusal category or a single refusal token, which are prepended to the model's responses during training. 
We then show how to increase or decrease the probability of generating the refusal token for each category during inference to steer the model's refusal behavior.  Refusal tokens enable controlling a single model's refusal rates without the need of any further fine-tuning, but only by selectively intervening during generation.\makeatletter
\let\@makefnmark\relax
\footnotetext{$^\dagger$ Work completed during Capital One Internship; Correspondence to $<$njain17@umd.edu$>$}
\makeatother

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
- This paper introduces refusal tokens as meta-tokens to control language model’s refusal levels. They fine-tune models with [REFUSE] and [RESPOND] tokens prepended to the messages. They also propose variants with multiple tokens per category (e.g. safety, queries related time after cutoff date etc). 

- Once a model is trained with these tokens, they can control the probability threshold to produce this token and therefore can control the probability of refusal. 

- Interestingly, they also find this approach improves actual scores of models in standard LM benchmarks.

### Strengths
Strengths:

- This paper is almost complete. It introduces a simple idea and performs extensive analysis on its effects on the language models.
- With the threshold sweep, they can find a good true positive rate without many false positives.
- The results in Tables 2 and 3 are surprising: they can improve the task-accuracy of the model after training with these tokens.

### Weaknesses
Weaknesses:
- It’s not clear Table-2 and 3 results are significant? I cannot see any error analysis.-

- Some experiments are distractive: Figure-5. Given all other plots why this another way of thresholding interesting? Why don't you present the best method and put small variants and analysis related to them to the appendix.

### Questions
- Can Table-4 can be a heat map as in a confusion matrix plots?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper introduces refusal tokens as a way to enable refusal behavior in LLMs at test time, and enable fine-grained threshold refusal by using the softmax probability of the new introduced token. Experiments show the effectiveness of the method.

### Strengths
- Training LLMs to refuse improper query is an important and interesting topic.

### Weaknesses
 - The authors claim that their method requires no retraining, while it does require training the model with a modified dataset (adding [refusal] and [respond] token to examples).
- Adding tokens in front of reponse to control the behaviour of LM has been explored a lot in controlled text generation works, for example, Quark (Lu et al., 2022) [1], Prefix-Tuning (Li & Liang, 2021) [2], CoCon (Chan et al, 2020) [3]. I'm a bit concerned about the novelity, as this work can be viewed as a specific version of Quark or Prefix-Tuning.

[1] Quark: Controllable Text Generation with Reinforced Unlearning

[2] Prefix-Tuning: Optimizing Continuous Prompts for Generation

[3] CoCon: A Self-Supervised Approachfor Controlled Text Generation

### Questions
- In introduction, F1 score is improved on which dataset? Even though it is clarified in the later section, it's not clear in the introduction.
- Some expression in intro is vague, what does "refine the token’s effectiveness" mean exactly? Is token effectiveness a widely used definition? Can it be quantitively measured?
- SFT seems to have similar performance with DPO in figure 2, can you explain why DPO is necessary if SFT also performs well? What causes the gap between SFT and DPO?

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces "refusal tokens," a method for dynamically calibrating refusal behavior in LLMs without retraining, offering control over how models respond to queries requiring refusal. The authors address challenges like over-refusal and user preference variability by training models with special tokens, which the model associates with refusal messages. At test time, refusal probabilities are adjusted using softmax thresholds, allowing nuanced control over refusal types and improving F1 scores. Experiments on UltraChat, Coconot, and Alpaca datasets show that refusal tokens enhance model consistency and safety while enabling user-specific refusal rate customization.

### Strengths
1. The paper addresses an important and timely issue by proposing a simple yet powerful method for calibrating refusal behavior in language models, which is crucial for improving model safety, reliability, and user trust.

2. It provides a thorough and comprehensive analysis of the refusal token approach, experimenting with various settings, datasets, and hyperparameters. This includes using multiple thresholding strategies and testing across distinct refusal categories, demonstrating the method’s versatility and effectiveness across different configurations.

### Weaknesses
1. The paper suffers from organization and clarity issues, making it difficult to discern the primary contributions and understand the flow of the proposed methodology.

2. It overlooks a highly relevant related work, *Refusal in Language Models Is Mediated by a Single Direction*, which explores a similar concept, potentially missing critical comparisons or distinctions with this study.

3. The paper omits evaluation on the important *XSTest* dataset (Röttger et al., NAACL 2024), which specifically benchmarks exaggerated refusal behaviors. This omission limits the analysis of the method’s effectiveness in controlling over-refusals.

### Questions
See weakness

### Soundness
2

### Presentation
3

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
This paper proposes a method to make language models refuse answering (abstain) by fine-tuning them with [response] / [refuse] tokens. It furthers considers multiple [refuse] tokens, one per category, and using contrast data where a model should not refuse. Experiments show this technique is effective on both a dataset containing multiple refusal categories and on temporal refusal, where a model should not answer questions about material after its training cutoff date.

### Strengths
- Important problem: learning to refuse to answer 
- Technically simple solution 
- Experiments show mostly effective results 
- The related work section is comprehensive and informative, and table 1 is useful. It would also be good to add a sentence to the first paragraph placing the current work in the context of the prior work mentioned in that paragraph.

### Weaknesses
 - Out-of-distribution generalization is not sufficiently explored
- Effects in the multi-category case are mixed; see below
- Some experimental issues and analyses are not clear; see below

I'd be willing to revise my evaluation depending on answers to the issues mentioned below.

### Questions
1. Probably the first work to use special tokens to affect generation according to some constraint is Sennrich et al., "Controlling Politeness in Neural Machine Translation via Side Constraints", 2016. 
2. Using the softmax probability as a measure of confidence assumes that the model is calibrated. Has that been tested?  It is known from the GPT4 paper that instruction-tuning hurts model calibration in terms of next-word prediction, but I wonder how that plays with refusal calibration. 
3. I'm confused about the "Coconot Experimental Setting". Is the training on UltraChat or on Coconot or both? It seems like the training is on UltraChat but the contrast data comes from Coconot. Can you clarify?
4. Validity of response/refusal cases in the temporal setting: How can we be certain when a model should respond or refuse? In the temporal setting, the model's training data cutoff date serves to choose which questions a model should answer or refuse. However, the fact a question is about an event that occurred prior to the cutoff date does not necessarily mean the model knows the answer. Perhaps the answer was mentioned in the training data but the model did not memorize it? Perhaps the answer was not in the training data even though it's about material before the cutoff date? 
5. Evaluation with LLM as a judge: I appreciate the decision to use the open-source Llama-3.1-70B. It's also great that the effectiveness was manually verified. Can you provide more details on this manual verification? 
6. The analysis in figure 3 of suppressing specific categories is interesting, but not so clear. First, what is the base refusal rate without any refusal tokens to compare with? Also, "humanizing" is not the only category that isn't affected; the "safety" pink bar is about as high in the safety category as in the other categories. 
7. Figure 4, right: why doesn't the false positive rate decrease below ~0.35? 
8. Figure 5: Is sum thresholding preferable to using a single refusal token? 
9. The analysis in figure is interesting. It's especially clear that training on refusal data (with or without refusal token, with or without contrast data) has only a small effect on another dataset, TriviaQA. Is this desired? Maybe we should want the model to learn to refuse on another dataset? Are there examples in TriviaQA where we actually expect the model to refuse? More generally, the question of generalization of the refusal training to other dataset seems important to study in greater breadth.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper proposes a method of refusal tokens. By incorporating refusal tokens into this framework, the model learns the relationship between the tokens and the corresponding behaviors during training. Then, during inference, the probability of the refusal tokens is used to guide the model's refusal behavior.

### Strengths
1. By adding refusal tokens, the language model is equipped with the ability to issue refusal messages.
2. Different categories of refusal tokens improve the normativity and interpretability of the refusal behavior, making it clearer why a refusal is issued for certain types of queries.

### Weaknesses
1. Lack of Comparative Baseline: The paper does not provide a baseline for comparison, making it difficult to evaluate the effectiveness of the refusal token method relative to other approaches. I suggest that the authors reference the methods presented in the survey article by Wen et al. (2024) as comparison benchmarks, particularly the Alignment Stage Approaches and Input-processing Approaches mentioned in the paper.

Wen, B., Yao, J., Feng, S., Xu, C., Tsvetkov, Y., Howe, B., & Wang, L. L. (2024). The art of refusal: A survey of abstention in large language models. 

2. Risk of Exploitation and Jailbreak Attacks: The proposed refusal tokens may be susceptible to exploitation or jailbreak attacks, where adversaries manipulate the tokens to circumvent the intended refusal mechanisms. Have the authors tested the performance of refusal tokens against adaptive attacks, such as backdoor attacks and jailbreak attacks? Additionally, have any mitigation strategies been considered, such as automatically removing response tokens from the input?

### Questions
If the authors can address my concerns, I will consider raising my score:
1. Can Refusal Tokens Appear within Generated Text, Not Just at the Beginning? In longer outputs, some portions may be harmful while others are safe. Could the proposed Refusal Tokens be improved to address such cases by refusing part of the content and generating a safe response? For example, could the system be designed to remove the content between the Refusal Token and the next Response Token?
2. What Are the Advantages of Using Refusal Tokens over Directly Training a Classifier? Could the authors design experiments to compare these two approaches?
3. Could the Proper Use of Response Tokens Improve the Harmlessness of Model Outputs? For inputs that do not meet the refusal threshold, is there a significant difference in the outputs when a Response Token is added versus when it is not?
4. Could Users Exploit the Model by Inserting Response Tokens in Their Inputs for Jailbreaks or Other Backdoor Attacks? I recommend that the authors discuss how they prevent or mitigate such exploitation. For instance, have they considered methods for detecting and filtering user-inserted tokens in the input?

### Soundness
2

### Presentation
3

### Contribution
2
