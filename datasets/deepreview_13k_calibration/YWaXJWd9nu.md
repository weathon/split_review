# What should an AI assessor optimise for?

- Decision: Reject
- Avg Score: 4.50
- Scores: 5, 5, 5, 3

## Abstract
An AI assessor is an external, ideally independent system that predicts an indicator, e.g., a loss value, of another AI system. Assessors can leverage information from the test results of many other AI systems and have the flexibility of being trained on any loss function: from squared error to toxicity metrics. Here we address the question: is it always optimal to train the assessor for the target loss? Or could it be better to train for a different loss and then map predictions back to the target loss? Using ten regression problems with tabular data, we experimentally explore this question for regression losses with monotonic and nonmonotonic mappings and find that, contrary to intuition, optimising for more informative losses is not generally better. Surprisingly though, some monotonic transformations, such as the logistic loss used to minimise the absolute or squared error, are promising.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper explores the efficacy of training assessor models, which are predictive systems designed to estimate the performance of other models (base systems) on various metrics before deployment. The authors question the common assumption that directly optimizing assessors for a specific validity metric always leads to the best outcomes for that metric. They investigate this through a series of experiments involving regression problems, comparing the performance of assessors trained on different error metrics, including absolute error, squared error, and logistic error. The results reveal that optimizing for a proxy metric can sometimes outperform direct optimization for the target metric, with logistic error frequently yielding the best performance.

### Strengths
1. **Innovative Approach:** The paper addresses a critical gap in the understanding of how assessors can be trained, providing a fresh perspective on the relationship between the optimization of assessor models and the performance metrics of interest.
2. **Comprehensive Experimental Design:** The authors conduct several experiments that systematically evaluate the impact of different training metrics on assessor performance, leading to insightful findings.
3. **Interesting Findings:** The consistent superiority of logistic error in various situations prompts further investigation into the characteristics of error distributions, which is a valuable contribution to the field.

### Weaknesses
1. **Limited Metric Scope:** While the paper examines several regression metrics, it may benefit from a broader exploration of other types of metrics across different applications, such as classification or ranking tasks, to enhance the generalizability of the findings. Specifically, the paper does not address scenarios where the base model's output is a probability distribution, which is common in many machine learning tasks. The current scope limits the applicability of the findings to scenarios where the base model outputs a continuous value, neglecting a significant portion of practical use cases.
2. **Theoretical Foundation:** The paper would be strengthened by a more robust theoretical explanation of why certain metrics outperform others in the context of assessor training, particularly for the surprising results related to logistic error. The lack of theoretical justification makes it difficult to understand the underlying mechanisms and limits the ability to predict when the observed trends will hold in different settings. A deeper analysis of the properties of the error functions and their interaction with the assessor training process is needed.
3. **Clarification Needed on Assessor Application:** The practical applications of assessors in real-world scenarios could be discussed in greater detail, including how to implement these findings in various domains, such as healthcare or autonomous systems. The paper lacks concrete examples of how the proposed approach can be integrated into existing workflows and what challenges might arise in real-world deployments. More specific guidance on how to select the appropriate error metric for a given application would be beneficial.

### Questions
- Can the authors elaborate on the specific characteristics of the logistic error that made it the most effective metric across the experiments?
- How might the findings change if applied to more complex models or different domains? Are there limitations in the current experimental setup that could affect generalizability?
- It would be beneficial for the authors to provide concrete examples of how their findings could inform the design of assessor models in practice.

### Soundness
3

### Presentation
2

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
The paper studies the effects of training different prediction models on proxy assessors instead of the target metric. The study focuses on regression problems and tabular features. Results show that training for more informative losses is not always better. In addition, the paper provides a decomposition of results on different directions of pairwise combinations of loss functions.

### Strengths
S1: The exploration of what loss functions are most effective for a target lost is generally important and can be informative if best choices are known and documented for practitioners.

S2: The work uses a variety of tabular models and datasets.

### Weaknesses
W1: The work engages only with regression models, which makes the scope somewhat narrow.

W2: The work does show some interesting outcomes, with some of them summarized in Figure 8. The results are however exclusively explained from an empirical perspective only. There is no theoretical discussion about for example how ML optimization and different optimization algorithms may interfere and interact with the results. For example, the fact that signed simple error -> signed squared error is green (proxy easier), may be explained by optimization difficulties. For this one in particular, it would be useful to experiment with different optimization algorithms and settings of such algorithms. It would also be useful to understand whether things like learning rate etc have an impact on results.

### Questions
Q1: Are the artifacts of this work going to be made available to the public (e.g. code)?

Q2: Are there any findings or insights that are specific to some of the datasets or do all results apply to all datasets individually? It would be useful to have some breakdown per datasets and see if there are any characteristics of the data that strengthen the results (or otherwise make them less applicable).

Q3: Which optimization algorithms did you use?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
In this paper the authors investigate the question as to whether assessor models should be trained using a proxy metric rather than the metric of interest. In doing so, they find mixed results. They also demonstrate that training assessors using more informative losses is not always better than training with uninformative versions.

### Strengths
I think the paper has several strengths:
1. The explanations of concepts and methodology is quite clear. I like the use of diagrams such as Figures 1, 3, 4 and 8.
2. The number of datasets used is quite commendable. 10 seems like a sufficient number to generate some useful trends if there was a large effect at play.
3. The subject matter is of interest although I think the focus on tree-based methods restricts the utility of the paper.

### Weaknesses
I do not think this paper is sufficiently novel and broadly applicable in order to warrant publicaton in ICLR.

I believe there are several weaknesses:
1. Unless I missed something, I believe all models used in the training set for the assessors are tree-based and are not neural networks. I know that tree-based methods can be better for tabular data but the most interesting application of assessors (to me at least) is neural networks. The most interesting assessor models are the ones that produce scaling laws. The lack of exploration into neural network base models severely limits the impact of the findings, particularly given the current focus on deep learning in the field. The paper does not address whether the observed trends hold for more complex model architectures, which is a significant gap.
2. The results of the paper do not seem particularly surprising. We know that changing the geometry of the loss landscape by using a different loss function can sometimes improve pefromance in regression. I don't think applying this logic to assessor models is paticularly interesting especially given the limited scope of exploration of the paper to tree based methods and the lack of mathematical theory. The paper's findings essentially demonstrate that optimizing for a proxy metric can sometimes yield better performance on the target metric, which is a well-established concept in machine learning. The application of this idea to assessor models, without a deeper theoretical justification or exploration of more complex models, does not provide substantial new insights.
3. Outside of intuition, there is no theory developed to explain the results. It seems that for a paper at ICLR, I would have expected more here. The lack of a theoretical framework makes it difficult to generalize the findings beyond the specific experimental setup. Without a formal analysis, it's unclear why certain loss functions perform better for assessor training and whether these results are specific to the datasets and models used.

### Questions
There may be some assumptions in my review which are incorrect. Please correct me if I am wrong but I am assuming that:
1. There are no neural network models which the assessors are applied to but neural networks are used to do asessing.
2. There are no proofs or more formal justifications for the relationships observed

I have a few other questions / requests:
1. Could the authors replace the figures with PDFs or SVGs intead of what is currently being used (easier to zoom in on)?
2. Do the authors think that there might be different relationships in the case of assessors applied to predicing things about over-parameterised models?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper investigates the question of what an AI assessor should optimize for. Specifically, could it be better to use something other than the target loss for the assessor. The question is considered empirically in the domain of tabular data using regression methods with a variety of methods of parameter optimization.

### Strengths
- The paper is generally clearly written.
- A fair number of experiments are conducted.

### Weaknesses
 - The big weakness of the paper is that it is framed around assessing AI systems, but focuses on regression with tabular data. I don't see how the latter is relevant to the former.

 - Given the generality of the question, why are we focusing on tabular data?
- Line 39: please introduce the variable v. 
- Line 47 "routing(Hu" missing space. 
- I don't understand what Figure 1 is intended to illustrate. On the picture there are "target assessor" and "proxy assessor" but the caption text doesn't clearly define these. It would be helpful to see an example that illustrates the notion of better that the authors appear to be aiming for? Also, when might this be true?  
- Why are the six losses chosen the right ones? 
- If we are interested in AI broadly, why are we using decision trees, Random forests, etc for parameter optimization? 
- It seems likely that they heuristic methods used for hyper parameter optimization or tabular data or regression might really be more of the story here than anything about AI.

### Questions
- Given the generality of the question, why are we focusing on tabular data? 
- Line 39: please introduce the variable v. 
- Line 47 "routing(Hu" missing space. 
- I don't understand what Figure 1 is intended to illustrate. On the picture there are "target assessor" and "proxy assessor" but the caption text doesn't clearly define these. It would be helpful to see an example that illustrates the notion of better that the authors appear to be aiming for? Also, when might this be true?  
- Why are the six losses chosen the right ones? 
- If we are interested in AI broadly, why are we using decision trees, Random forests, etc for parameter optimization? 
- It seems likely that they heuristic methods used for hyper parameter optimization or tabular data or regression might really be more of the story here than anything about AI.

### Soundness
2

### Presentation
2

### Contribution
2
