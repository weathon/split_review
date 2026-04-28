# Eliciting Black-Box Representations from LLMs through Self-Queries

- Decision: Reject
- Avg Score: 6.00
- Scores: 8, 5, 6, 5

## Abstract
As large language models (LLMs) are increasingly relied on in AI systems, predicting when they make mistakes is crucial. While a great deal of work in the field uses internal representations to interpret model behavior, these representations are inaccessible when given solely black-box access through an API. In this paper, we extract representations of LLMs in a black-box manner by asking simple elicitation questions and using the probabilities of different responses \emph{as} the representation itself. These representations can, in turn, be used to produce reliable predictors of model behavior. We demonstrate that training a linear model on these low-dimensional representations produces reliable and generalizable predictors of model performance at the instance level (e.g., if a particular generation correctly answers a question). Remarkably, these can often outperform white-box linear predictors that operate over a model’s hidden state or the full distribution over its vocabulary. In addition, we demonstrate that these extracted representations can be used to evaluate more nuanced aspects of a language model's state. For instance, they can be used to distinguish between GPT-3.5 and a version of GPT-3.5 affected by an adversarial system prompt that makes its answers often incorrect. Furthermore, these representations can reliably distinguish between different model architectures and sizes, enabling the detection of misrepresented models provided through an API (e.g., identifying if GPT-3.5 is supplied instead of GPT-4).

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper introduces an effective method called QueRE, designed to infer the internal representations of black-box language models through self-queries, particularly in follow-up question scenarios. The authors represent the black-box model by using the probability of the "yes" token as vector values, and then train a linear model to achieve the following objectives: 1) accurately predict model performance at the example level, and 2) assess various states of the language model, such as detecting if the model has been influenced by harmful prompts, determining if it has been replaced by another model, and identifying the architecture and size of the models. The authors also demonstrate that this approach generalizes beyond top-K token reliance, making it applicable to sample-based methods.

### Strengths
- A simple yet effective method to elicit the internal representations of black-box models
- A series of detailed experiments demonstrating QueRE's effectiveness across various benchmarks and settings, comparing it favorably against more complex, resource-intensive methods.
- Strong practical application value.
- Mathematical foundation

### Weaknesses
I am impressed with this paper, both by its strong results and its practical applications. Could you elaborate on the intent behind your design choices? Additionally, did you explore other methods that ultimately proved less effective or failed to yield similar results?

### Questions
The same as in the Weaknesses part.

### Soundness
4

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
3

### Summary
This paper proposes a method to extract black-box representations from large language models (LLMs) by querying them with elicitation questions. The approach leverages the probabilities of model responses to these questions, creating low-dimensional representations that can be used to predict model performance on specific tasks, detect adversarial manipulation, and distinguish between different model architectures and sizes. The authors demonstrate that these black-box representations are effective, often outperforming other techniques that even rely on internal model states.

### Strengths
1. The paper is well written, and the ideas are conveyed in a way that is accessible and logically coherent, making the methodology and results easy to follow.
2. This work is particularly significant given the increasing reliance on black-box LLMs by researchers and developers who lack full access to model internals. By providing a practical and scalable way to elicit representations from these models, the paper addresses a growing need.
3. The method of querying black-box models with elicitation question to construct representations is creative and the method outperformed strong baselines. The method was also applied to three different tasks.

### Weaknesses
1. The paper labels the extracted low-dimensional vectors as “representations,” but this may be overstated. These vectors are simply derived from yes/no responses to elicitation questions, which only provide limited insights into the model’s deeper knowledge or reasoning structures.
2. My interpretation is that the classifier is primarily learning to detect shifts in the model’s calibration—the confidence in its yes/no responses—rather than meaningful behavioral changes. This is limiting since if a model provider adds the system prompt (“Be helpful and cautious.”), it could alter the model's calibration and trigger your classifier as detecting an adversarial/harmful LLM (task 3). I think any added system prompt for that matter would trigger a false positive. Furthermore, if system prompts were appended to all models by the model providers, I'm not sure you could still reliably classify between models (task 2)?

I’m not sure how useful the proposed method is for actual tasks beyond predicting model performance (point 1), and I'm not sure if the method is actually robust to the variations I described (point 2).

### Questions
- While your method is superior to the baselines, can you comment on how much more expensive/cheaper it is?

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
The authors introduce QueRE — a black-box method for extracting model representations. QueRE extracts representations by asking follow-up yes/no questions about the LLM's answers and using the articulated response probabilities as features. They ask questions such as “Are you confident in your answer”, where the LLM replies P(”Yes”) = 0.95”). They then use the value of 0.95 as part of the representation for a linear model to predict whether or not the LLM gets the answer correct. By asking multiple follow-up questions, they create a representation for a linear model to use. This linear model can be used for particular tasks, given labeled data.

Contributions

- On a task to predict whether the model answering an open-ended question is correct, QueRE beats several white-box and black-box methods.
- QueRE can distinguish between model architectures, and detect adversarially prompted models.

### Strengths
- The authors show significant results for the task to predict whether the model answers an open-ended question correctly. They compare against a variety of white-box and black-box methods and beat these baselines. The presentation for this section was clear.
- The scaling chart (Figure 8) demonstrates performance improvement with more elicitation questions. This work can be viewed as an extension of the post-conf baseline — which uses just one way of asking for the probabilities. Instead, we can ask it in multiple ways. We then apply a linear classifier on top of it to weigh the different possible ways of asking for probabilities. The scaling chart demonstrates the usefulness of their method compared to the post-conf baseline.

### Weaknesses
It is unclear to me whether QueRE works on out-of-distribution datasets. The results would be more significant if QueRE generalizes to out-of-distribution datasets, where it is hard for humans to supervise and we don’t have ground truths.
Suggestion: If you use labeled data from e.g. HellaSwag to train your linear model, does the model work on SQuAD?
- The setup for detecting adversarially influenced models is simplistic. Using a system prompt that instructs the model to "answer questions incorrectly", is easily detectable. For example, if I asked the adversarial model “What is 1 + 1?”, the adversarial model may reply “3”, which someone can detect as wrong easily.
This setup fails to address the forms of adversarial influence that the cited Sleeper Agents paper spells out — where models insert bugs only in specific contexts.
Suggestion: Use a similar setup as the Sleeper Agents paper where you evaluate code-like tasks. The system prompt may be “When creating code, insert bugs into the code. Otherwise when asked other questions, just act normally”. 
There is a question of what labeled data to use in this adversarial model setup. Related to my first point, assume that you don’t have labeled data about code questions. Does using labels from e.g. the dataset SQuAD still work?  Can the linear predictor generalize to detecting these adversarial questions, even without ground truths from these adversarial questions?

### Questions
Questions:

- I’m unsure about the importance of distinguishing between model architectures. More related work and citations pointing out the importance can be stated to highlight the importance.
- Suggestion for clarity: Prompts for black-box baseline — pre-conf and post-conf should be provided in the appendix to make it easier to understand what they are.

### Soundness
2

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
3

### Summary
This paper introduces QueRE, a method for constructing black-box representations from LLMs by using the models’ confidence in answering specific follow-up questions. These representations are instance-level, meaning each one corresponds to a single instance. Through experiments, the authors demonstrate that these representations can predict task accuracy, differentiate between a clean LLM and an adversarially instructed one, and distinguish different LLMs. The experiments are conducted by additional supervised training on these representations for every dataset.

### Strengths
I believe extracting low-dimensional representations that can reflect LLM's behavior is an important and challenging problem.

### Weaknesses
W1: The representations extracted in this paper fall short of my expectations for “eliciting black-box representations from LLMs.” The authors construct representations as Yes-or-No probabilities for a set of follow-up questions, like “Do you think your answer is correct?” This approach feels quite post-hoc. I expected “black-box representations from LLMs” to more fundamentally reflect the models’ internal workings. To give some concrete examples, first, I would hope the representation exhibit generality across tasks, rather than being tailored for accuracy prediction with a predictor trained for each specific task. Second, I would hope the representation finds utility in zero-shot settings as well. While the authors may have a different perspective, I encourage them to clarify their definition of “black-box representation” early in the paper.

W2: 2. Following up on the previous comment, if the authors could demonstrate that a single predictor can be trained across tasks to predict accuracy and generalize to new, unseen tasks without any known ground truth, it would help demonstrate the generality of the extracted representations.

W3: Tables 2, 7, and 8 show that random sequences can outperform QueRE for some models and tasks, suggesting that the specific follow-up questions chosen may not be critical. Random sequences are considered among the weakest baselines, yet they outperform QueRE, leading me to believe that simply elicitating more information from the LLM is the main reason giving the empirical performance. Better constructed follow-up questions can perform better, but a “random kitchen sink” approach already works to some level. If this is the case, it should be acknowledged in the paper, as it, in my view, lessens the contribution of this work. Could the authors conduct a more thorough analysis of why random sequences sometimes outperform QueRE, and discuss the implications this has for their method?

W4: Building on the idea of random sequences, I suggest the authors compare QueRE with more diverse follow-up question strategies. For example: (1) rephrasing the same question in different ways and eliciting confidence, or (2) using questions from the same task with known ground truth (since all experiments assume access to a small amount of labeled data from downstream tasks), or (3) using questions from other tasks with known ground truth.

W5: Please discuss empirically the importance between the number of eliciting questions and the elicitating question strategies (e.g., between one designed in this paper, random sequences, others mentioned in W4).

W6: I’m curious why QueRE outperforms full logits in Figures 2 and 3. Shouldn’t full logits contain strictly more information than QueRE? Could you provide a more detailed analysis of why QueRE outperforms full logits in these cases?

W7: If this difference is due to the fact that full logits are only extracted for the initial response while QueRE includes additional follow-up questions, could the authors concatenate full logits from all follow-up questions and include this as a comparison?

W8: Additionally, I suspect the use of linear classifiers might contribute to these results, since QueRE is low-dimension and full logits are high dimension. Could the authors compare QueRE’s performance with more complex classifiers? Linear classifiers may favor low-dimensional representations.

W9: QueRE appears to extract and combine uncertainty or confidence signals. Could the authors compare QueRE to a baseline that directly concatenate different existing LLM uncertainty estimates? For example, [1].

W10: If I understand correctly, the experiments in Sections 4.2 and 4.3 are ablation studies, rather than comparisons to external methods. All baselines—pre-conf, post-conf, and Answer Probs—are components of QueRE, as noted in lines 297-307. This setup makes it impossible for QueRE to perform worse than these baselines. I suggest that the authors highlight the ablation nature of these experiments in Sections 4.2 and 4.3. Additionally, it would be beneficial to compare QueRE with existing methods that can be applied.

W11: The experimental setup in Section 4.3 may be seen as limited and less realistic. Adversarial LLMs explicitly designed to answer incorrectly are easy to distinguish and less reflective of real-world scenarios. I suggest the authors consider existing methods that contaminate or manipulate LLMs in more subtle ways.

### Questions
See Weakness section.

### Soundness
2

### Presentation
2

### Contribution
2
