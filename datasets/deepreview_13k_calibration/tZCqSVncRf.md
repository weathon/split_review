# MIRAGE: Evaluating and Explaining Inductive Reasoning Process in Language Models

- Decision: Accept
- Avg Score: 6.00
- Scores: 5, 6, 8, 5

## Abstract
Inductive reasoning is an essential capability for large language models (LLMs) to achieve higher intelligence, which requires the model to generalize rules from observed facts and then apply them to unseen examples. We present {\scshape Mirage}, a synthetic dataset that addresses the limitations of previous work, specifically the lack of comprehensive evaluation and flexible test data. In it, we evaluate LLMs' capabilities in both the inductive and deductive stages, allowing for flexible variation in input distribution, task scenario, and task difficulty to analyze the factors influencing LLMs' inductive reasoning. Based on these multi-faceted evaluations, we demonstrate that the LLM is a poor rule-based reasoner. In many cases, when conducting inductive reasoning, they do not rely on a correct rule to answer the unseen case. From the perspectives of different prompting methods, observation numbers, and task forms, models tend to consistently conduct correct deduction without correct inductive rules. Besides, we find that LLMs are good neighbor-based reasoners. In the inductive reasoning process, the model tends to focus on observed facts that are close to the current test example in feature space. By leveraging these similar examples, the model maintains strong inductive capabilities within a localized region, significantly improving its deductive performance.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper evaluates and analyzes LLM's ability for inductive reasoning. Compared to previous works in inductive reasoning, it adopts a new setting, which is to compare the performance of LLMs under two settings: (1) specific --> general --> specific, and (2) specific --> specific.
It is interesting to see that the performance of LLMs under the two settings is comparable. The result indicates that setting (2) will have a better performance, even though traditionally we think a general rule is important to make further inferences to unseen specific examples.

As for results, the main findings of this paper are that 
(1) setting (2) outperforms setting (1);
(2) many techniques such as self-consistency can't improve performance in the proposed task; and 
(3) in-context demonstrations that are closer to the input can help more in terms of the accuracy of output.

### Strengths
1. The main finding is insightful, that setting (2) outperforms setting (1), which can bring in more discussions on how LLMs perform inductive reasoning.
2. The analysis in terms of neighbor-based reasoning, especially the investigation into the scope is also interesting. However, it might not be surprising, since the similarity of in-context demonstrations has been discussed extensively in previous papers.

### Weaknesses
1. The writing is not clear. Specifically,
a). what does the "substitution" in line 414 and line "443" mean?
b). after finding IF, CF, and OF, how are they used?
c). what is the metric in Table 1?

2. The claim "We prove that LLM is a poor rule-based inductive reasoner" is too strong and unacceptable. What is the definition of "poor"? And have the authors proved it mathematically?

3. "We prove that LLM is a neighbor-based inductive reasoner.": Have the authors proved it mathematically? When LLM is a neighbor-based inductive reasoner?

4. Although the performance that setting (2) outperforms setting (1) is provided. There might lack of a more in-depth analysis of when LLMs use neighbor-based reasoning, and when LLMs use the general pattern thinking? Or is it that LLMs can purely do neighbor-based reasoning, and never use the general pattern thinking at all? It seems that although each experiment is interesting, but I don't know what is the takeaway knowledge from this paper.

### Questions
See above

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
This paper presents a new dataset for evaluating the induction and deduction ability of LLMs. The authors provide a very detailed explanation of the generation method of the dataset and make extensive experiments to evaluate current state-of-the-art models. The authors also propose two hypotheses about LLMs' reasoning behaviours, and the experiments are designed to verify these hypotheses. Detailed explanations and discussion are provided, and the supplementary material also gives good support to the conclusion.

### Strengths
- The paper covered a broad range of related works and provided another valuable benchmark for evaluating LLMs' reasoning power. The tasks has been formulated in four representations to ensure the diversity.
- The authors make two interesting hypotheses on LLM's behaviour, and carefully designed several experiments to verify them.
- In order to evaluate LLMs' behaviours, the authors designed several metrics specifically, most of which make sense to me. Detailed discussions are provided, and all the charts and tables are explained well.

### Weaknesses
 - First of all, all the experiments are behavioural studies and empirical evaluations, and there is no mathematical evidence about LLM's induction/deduction power. IMHO, if there is no mathematical proof, then claims such as "we prove that LLMs are poor in inductive reasoning" would be too strong.
- It is fine to evaluate the models' induction ability by using the designed tasks. However, I wouldn't call the other task as "deduction" since the rules are not provided. From the definition from logic, a deductive inference needs both input facts and the logic rules for deducing the outputs.

### Questions
Please see above.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper investigates the inductive reasoning abilities of LLMs, introducing Mirage, a synthetic dataset designed to comprehensively evaluate LLMs' inductive and deductive reasoning from various perspectives. Using Mirage, the authors demonstrate that LLMs are weak at rule-based reasoning but perform well with neighbor-based reasoning. These findings suggest that LLMs' deductive reasoning can be enhanced by leveraging similar examples to support a robust inductive reasoning process.

### Strengths
Strengths:
- Present a synthetic data generation framework to evaluate inductive and deductive reasoning processes. The authors provide clear steps detailing the data generation process, specifically outlining the rule generation and question generation procedures.
- Various advanced prompting techniques, including SR and HR, along with the latest LLMs, are tested in the experiments.
- The effective scope analysis for neighbor reasoning supports the claim that LLMs are effective neighbor-based reasoners.

### Weaknesses
Weaknesses:
- In the section on neighbor reasoning, the authors use the term "Feature Space" to denote the space of observed facts and test samples. However, it’s unclear where the features in this space originate, specifically how these features are extracted or represented from the raw input data, and whether they are hand-engineered or learned.
- The data setting may lack sufficient complexity to effectively demonstrate inductive reasoning capabilities in real-life scenarios. The synthetic nature of the data, while allowing for controlled experiments, might not capture the nuances and complexities present in real-world datasets, such as noise, ambiguity, and a wider range of rule types.

### Questions
Questions:
- Could the authors offer additional insights or empirical evidence on the model's performance with real-world datasets or in less controlled environments?
- Additionally, could the authors also check if fine-tuning over the synthetic data helps the inductive reasoning of LLMs?

### Soundness
3

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
2

### Summary
Authors created a synthetic dataset MIRAGE to evaluate the reasoning ability of LLMs, with two conclusions: (1) LLMs are not good at deductive reasoning, (2) LLMs are good at performing inference based on neighborhood information, thus, they are "neighbor-based inductive reasoner". 

Authors try to distinguish the ability of deductive reasoning from the ability of inductive reasoning. The missing experiment(s) is/are to distinguish the ability of reasoning from the ability of pattern matching. For example, it is necessary to show the so-called "neighbor-based inductive reasoner" is the ability of reasoning, instead of the ability of pattern-matching.

### Strengths
A new synthetic dataset is created and contributed to the reasoning evaluation of LLMs. 
Authors conclude that LLMs are poor in rule-based reasoning, and good at neighbor-based reasoning.

### Weaknesses
Authors created a synthetic dataset MIRAGE to evaluate the reasoning ability of LLMs, with two conclusions: (1) LLMs are not good at deductive reasoning, (2) LLMs are good at performing inference based on neighborhood information, thus, they are "neighbor-based inductive reasoner". 

Authors try to distinguish the ability of deductive reasoning from the ability of inductive reasoning. The missing experiment(s) is/are to distinguish the ability of reasoning from the ability of pattern matching. For example, it is necessary to show the so-called "neighbor-based inductive reasoner" is the ability of reasoning, instead of the ability of pattern-matching.

It is not surprising that LLMs are good at "predicting" based on neighborhood context, as this is one of the important methods to train them.

Authors coined the nice term "neighbor-based reasoning". But, is it reasoning or just pattern-matching? I am afraid there is no term of "neighbor-based inductive reasoning" in the literature of logic or psychology.

### Questions
1. why do you only mention inductive reasoning in the title? you also report experiments on deductive reasoning of LLMs. 

2. do you assume any causal relations between the input and the output of rules, or just associative relations? If only associative relations, how do you distinguish deductive from inductive reasoning?

### Soundness
2

### Presentation
3

### Contribution
2
