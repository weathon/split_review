# Reasoning Elicitation in Language Models via Counterfactual Feedback

- Decision: Accept
- Scores: 6, 5, 8, 6

## Abstract
Despite the increasing effectiveness of language models, their reasoning capabilities remain underdeveloped. In particular, causal reasoning through counterfactual question answering is lacking. This work aims to bridge this gap. We first derive novel metrics that balance accuracy in factual and counterfactual questions, capturing a more complete view of the reasoning abilities of language models than traditional factual-only based metrics. Second, we propose several fine-tuning approaches that aim to elicit better reasoning mechanisms, in the sense of the proposed metrics. Finally, we evaluate the performance of the fine-tuned language models in a variety of realistic scenarios. In particular, we investigate to what extent our fine-tuning approaches systemically achieve better generalization with respect to the base models in several problems that require, among others, inductive and deductive reasoning capabilities.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper studies causal reasoning in LLMs through counterfactual question answering.

The authors propose a number of metrics: necessity inconsistency rate (N-IR), sufficiency inconsistency rate (S-IR), absent necessity inconsistency rate (AN-IR), absent sufficiency inconsistency rate (AS-IR), and the average of all those (Avg-IR). These go beyond simple accuracy by assessing the consistency between factual and counterfactual answers within a causal framework.

They perform a number of experiments where they finetune a small LLM (Phi-3 mini, 3.8B parameters) with SFT and DPO and present results on the extent to which their fine-tuning methods effect different generalization modes (common-cause, common-effect, inductive, deductive).

### Strengths
* Introducing more finegrained metrics: The proposed metrics for causal consistency are a valuable contribution, addressing a limitation of existing evaluation methods that focus primarily on accuracy.
* Generalization modes:  The proposed classes for generalization modes provide a structured framework for evaluating reasoning transfer.
* Experiments:  The paper includes a comprehensive set of experiments, including a hand-crafted puzzle and real-world problems.

### Weaknesses
 * The choice of a very small LLM (Phi-3 mini) with limited reasoning capabilities makes it difficult to draw any conclusions for stronger models that are more commonly used for reasoning tasks.  
* Clarity and Presentation:  While the paper focuses on an interesting problem and makes interesting suggestions, the presentation could be significantly improved. I found the formal definitions and descriptions of the methods a bit difficult to follow.
* Analysis of generalization: The analysis of the generalization results could be more in-depth.
* Comparison to CoT: The authors claim (in a footnote) that the effectiveness of CoT "can be attributed to
successful imitation of the provided examples". It would have been interesting to test that claim with the analytic tools they developed.

### Questions
1. Could you provide a more intuitive explanation of the inconsistency rate metrics in the paper?
2. Can you include the specific architecture and number of parameters of the Phi-3 mini model and discuss the limitations introduced by this choice? Can you include the Phi-3 mini performance on common reasoning benchmarks (compared to what top models are capable of)?
3. Have you considered comparing your methods with chain-of-thought prompting (see weakness above)?

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
This paper is interested in LLM's ability of doing causal reasoning (that follows Pearl's counterfactual methods). For this they propose novel metrics that balance accuracy in factual and counterfactual questions and then propose several fine tuning approaches and evaluate them using their proposed metrics with respect to several examples. They show that their fine tuning methods lead to better performance with respect to their proposed metrics.

### Strengths
Causal reasoning is an important problem and Pearl's approach of using counterfactuals to do causal reasoning is sound and well studied. There is indeed necessity of more fine grained metrics when evaluating reasoning ability of LLMs and the papers efforts towards that is a plus. 
The paper presents several fine tuning techniques and evaluate them using their proposed metrics with respect to several examples. The evaluations show that their fine tuning methods lead to better performance with respect to their proposed metrics.

### Weaknesses
The examples that are studied in the paper are very direct in terms of language and LLMs can translate them to a formal representation (LLMs are good at that) and then call a dedicated solver and thus achieve near 100% accuracy. What is the motivation then of doing it the way that is proposed in the paper?

Why is your approach preferable to using a formal representation and a dedicated solver?

That motivation must match with the way the examples and evaluation data are presented and studied.

### Questions
1. See the question in the weakness part.

2. Are the examples that are studied in the paper original to this paper?  (If so, they are a good contribution.) Or are they published in some other papers cited in this paper. 

3. In the Introduction you say: "When the goal of fine-tuning is specifically to improve reasoning, a unique problem arises in evaluating the fine-tuned LLMs: we cannot just measure performance for a held-out set of test samples within the same reasoning task. If we do, it would be impossible to tell whether the LLM actually learned to reason or whether it is still recalling the demonstrations we have made during fine-tuning.*2* "

*2* For instance, chain-of-thought prompting aims to improve reasoning by providing examples of how a problem can be solved in smaller steps. While such prompting is effective, its effectiveness can be attributed to successful imitation of the provided examples and is not necessarily the result of true reasoning (Wei et al., 2022).

In Page 3 you say: "Modes of Generalization. As we have discussed in the introduction, an in-domain evaluation is not sufficient alone to assess the success of fine-tuning for reasoning."

I am a bit confused by these. Consider an analogy. Say I have examples of how to multiple 
2, 3, and 4 digit numbers and using that a model learns to be able to multiple 5, 6, 7 ... digit numbers. Is that a good generalization?

Similarly your model may learn from a few examples and if it is able to address causality in new examples with a much more complicated graph, and more variables, will that not be a good generalization?

Kindly clarify the distinction you are making between in-domain evaluation and generalization, and how your approach differs from the type of generalization mentioned above.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper presents a method for fine-tuning large language models by means of counterfactual feedback. The authors present four categories of causal reasoning (common-effect, common-cause, inductive, and deductive). They also propose two new metrics to measure necessity and sufficiency under a reasoning framework (these metrics measure necessity and sufficiency inconsistency rates), by first presenting an example justification of these metrics. They then introduce three methods for fine-tuning LLMs with counterfactual feedback: supervised, preference-based and causal consistency feedback.

### Strengths
I see a lot of strengths in this paper, including: 

- The paper presents an interesting framework for fine-tuning LLMs with counterfactual feedback, which is highly relevant and original. 
- The quality of the paper is very good: it is very well structured, organized, and it integrates a multiplicity of concepts, scenarios and metrics for the problem at hand. In this sense, the paper is beyond complete. 
- The significance of the paper appears to be very relevant for researchers in causal reasoning (with or without LLMs).

### Weaknesses
I see very few weaknesses in this paper. Here is a couple of things I would improve:

- Organization of the paper: the placement of related work is a bit odd - perhaps moving it to the end of the paper would help.
- Conclusion: the limitations in the conclusion feel a bit 'incomplete', in the sense that these leave room open for further research of non-binary representations of causes and effects. Can you give some hints on how the proposed method could be adapted in this case?
- There is a typo in line 144 of the paper: "interesting" --> "interested"

### Questions
- Can you give some hints on how the proposed method could be adapted to the case of non-binary representations of causes and effects?

### Soundness
4

### Presentation
4

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
This paper explores the potential of fine-tuning language models (LLMs) to improve their causal reasoning abilities, particularly through counterfactual feedback. Standard LLMs exhibit a discrepancy between their strong recall abilities and their limited reasoning abilities. The authors propose a framework that incorporates new metrics (necessity and sufficiency inconsistency rates) to assess reasoning more comprehensively. They explore fine-tuning methods, including supervised and preference-based approaches, to improve understanding of causal dependencies and generalization across tasks. The study finds that fine-tuning is more effective at improving reasoning in inductive scenarios than in deductive ones, suggesting different patterns of generalization in reasoning tasks. Also, the paper suggests that using factual and counterfactual reasoning examples together can lead to better reasoning abilities in models.

### Strengths
The authors present a framework for fine-tuning based on causal reasoning, which provides a structured approach to understanding how reasoning can generalize across different problems. They formally categorize this generalization into four distinct types: common-effect, common-cause, inductive, and deductive reasoning, which helps to better understand reasoning in LLMs. This classification provides a systematic way to analyze and apply causal reasoning to different tasks. 

The authors propose new metrics-Necessity Inconsistency Rates (N-IR) and Sufficiency Inconsistency Rates (S-IR)-for evaluating reasoning in large language models (LLMs) based on causal principles. They also introduce absent necessity and absent sufficiency to capture cause-effect relationships beyond traditional necessity and sufficiency. These metrics provide a more detailed framework for evaluating causal reasoning in LLMs.

The authors fine-tuned the models by including the counterfactual information with the factual information, which proved useful in improving the model's understanding of causal dependencies. This focus is consistent with human reasoning processes, where understanding "what-if" scenarios often plays a critical role in causal inference. Preference training using DPO was also used in the paper, which showed that learning from comparative feedback can be more effective than standard supervised approaches in some cases.

### Weaknesses
My main concern with the paper relates to the way the experiments are conducted. The paper claims that using factual and counterfactual examples leads to a performance gain compared to the base model or the model trained only on factual examples of counterfactual examples. However, this could be due to the increased number of training examples, which leads to an increase in overall performance. 
In addition, a model tuned with both factual and counterfactual examples tends to perform well on metrics that measure both properties compared to either one. This may simply be due to an over-fitting of causal specific patterns. In addition, the experiments are limited to one model and one synthetically generated dataset, and the results are difficult to generalize across models and datasets. The other datasets used later are missing all the training/test splits used and how the model was trained. Section 6.3 is hard to understand because it lacks information on the number of samples used. 

**Actionable Suggestion** : It would be great to see an experiment where you randomly sample equal number of factual and counterfactual examples and fine-tune the model and compare it with the individual factual and counterfactual only models. That would be a fair comparison.

The experiments also lack deeper analysis to better understand where fine-tuning fails. For example, a breakdown of errors by task type, complexity, or specific reasoning challenge (e.g., false sufficiency vs. false necessity errors) would provide insight into model weaknesses. The errors for which the model struggles to perform well need to be analyzed, and this is not discussed in the paper. 

**Actionable Suggestion:** Please provide the task specific error categories that provides deeper insights into the models' strengths and weaknesses.

Finally, the approach of using counterfactual reasoning to improve model performance in reasoning tasks is not new and has been studied previously by https://arxiv.org/abs/2307.02477 and https://aclanthology.org/2022.lrec-1.229/. 
The novelty of this paper lies in the way the two metrics are proposed to understand causal reasoning in LLMs. However, due to the weaker experiments, it is not clear why this paper stands out. It is similar in many ways to papers suggesting that more data can improve reasoning (such as from https://arxiv.org/abs/2309.12284).

### Questions
Section 6.3 lacks any information about the real-world data used. It is important to discuss the training and test data used and how many samples were rejected due to incorrect or unclear counterfactuals. It is mentioned at the end of the paper *Note that not all generalization modes were tested for each problem due to differences in causal structures, so the average scores were calculated using only the problems that were tested for each generalization mode.* which needs to be discussed. 
**Provide a table summarizing the datasets used, including sample sizes, data sources, and which generalization modes were tested for each problem.** This will clear the confusion in this section. 

Authors need to provide a discussion section where the type of error each type of fine-tuned model makes is discussed. Currently, just from the numbers, it is hard to understand what are the errors made by each model and how preference tuning can solve some of them. **Some error analysis examples or visualizations that would illustrate the different types of errors made by each model and how preference tuning addresses them would be helpful here**.

Some results need to be discussed more like statements like: *However, with common-cause/effect and deductive demonstrations, they no longer show the same reasoning improvements as observed in the in-domain setting.*  Inductive vs. Deductive results are not clear and need to be discussed why one approach performs better than the other. 

Finally, the most important result to discuss is the data imbalance between the factual or counterfactual training set alone and a combination of the two. Both experiments need to be balanced for a fair comparison, otherwise it could just be the additional data points that lead to improved performance.

### Soundness
2

### Presentation
3

### Contribution
2
