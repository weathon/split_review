# How to Catch an AI Liar: Lie Detection in Black-Box LLMs by Asking Unrelated Questions

- Decision: Accept
- Scores: 8, 6, 5, 8

## Abstract
Large language models (LLMs) can ``lie'', which we define as outputting false statements despite ``knowing'' the truth in a demonstrable sense. LLMs might ``lie'', for example, when instructed to output misinformation. %
Here, we 
develop a simple lie detector that requires neither access to the LLM’s activations (black-box) nor ground-truth knowledge of the fact in question. The detector works by asking a predefined set of unrelated follow-up questions after a suspected lie, and feeding the LLM’s yes/no answers into a logistic regression classifier. Despite its simplicity, this lie detector is highly accurate and surprisingly general. When trained on examples from a single setting---prompting GPT-3.5 to lie about factual questions---the detector generalises out-of-distribution to (1) other LLM architectures, (2) LLMs fine-tuned to lie, (3) sycophantic lies, and (4) lies emerging in real-life scenarios such as sales. These results indicate that LLMs have distinctive lie-related behavioural patterns, consistent across architectures and contexts, which could enable general-purpose lie detection.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper provide a definition for a language model lie based on consistency: an LM lies if it gives an incorrect answer to a question, but would answer correctly if the question is given in a standard question-answering format. The authors propose to detect this kind of lies by observing how the LM behaves on a fixed, specifically curated set of unrelated question. The authors train a logistic regression classifier to detect lies using outputs from a GPT 3.5 *that’s prompted specifically to lie*, which manages to generalize very well to new models, new tasks, and several other aspects. The results seem to suggest that lying—a type of inconsistency as defined by the paper—is surprisingly consistent across many language models.

### Strengths
The findings of this paper are somewhat surprising and definitely interesting. The authors also did a great job on ablations, e.g., spurious correlations that might exist in the experiments but not in general. The idea of using unrelated questions to establish a behavioral baseline is smart. And since the set of elicitation questions are particularly optimized for lie detection, this opens up a lot of follow-up work.

### Weaknesses
Nothing in particular. This paper seems well executed and the results are worth sharing with the ICLR audience.

### Questions
The lying behavior studied in this paper can be seen as a special case of sycophantic behavior, where the LM model does something like "there is a lie in the context (that I can detect), so I should be consistent and keep lying". Would it be interesting to study whether this effect will be diluted by longer context, e.g., with a long and truthful prefix before the lie?

### Soundness
4 excellent

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces a lie detector designed to determine whether a Language Model (LLM) is providing deceptive answers to questions. First, it provides an overview of the latest advancements and studies in the field, focusing on two main areas: 'Distinguishing Lies from Other Falsehoods' and 'Building Lie Detectors'. The authors developed a simple yet effective black-box lie detector, which operates by posing a predefined set of unrelated follow-up questions after a suspected lie, and then feeding the LLM’s yes/no answers into a logistic regression classifier. The experimental setup of the paper is meticulously explained, detailing how to generate lies with the LLM and how to conduct black-box lie detection using elicitation questions. Finally, an analysis of the lie detection results is presented.

### Strengths
In the case of a black box scenario, the lie detector proposed in this paper is capable of rendering a verdict solely through a series of yes/no questions answered by the LLM, with the responses then fed into a binary classifier. This approach represents a substantial innovation and carries two significant implications.

- This approach eliminates the need for access to the LLM’s activations, allowing researchers to investigate lie detection in advanced models while having only limited API access.

- Some approaches depend on assistant LLMs to validate claims made by potentially deceptive LLMs. This method might fail if the assistant possesses less knowledge than the deceptive LLM. In contrast, the lie detector proposed here requires no ground truth knowledge about the statement under evaluation. In addition, the paper has developed a dataset of 'synthetic facts'—questions for which the model has not encountered the answers during pre-training, but to which it provides the correct answers in the prompt.

The appendix of this paper is highly detailed, encompassing the dataset, specifics of the experimental setup and lie generation, elicitation questions for the lie detector, additional lie detection results, details on specific generalization experiments, prompts, and real-life role-playing scenarios for goal-directed lying. This comprehensive coverage makes it easy for readers to follow and understand the experiment.

### Weaknesses
This paper uncovers a number of interesting properties. However, providing a more detailed and intuitive explanation of the thought process that inspired the methods proposed in this article, as well as a deeper analysis and insight into the underlying mechanisms of the discovered properties, would greatly aid in enhancing the reader's understanding of this intriguing issue.

There is room for improvement in the organization and presentation of the article. For instance, the caption in Figure 4 is placed below, while the caption in Figure 5 is placed above.

### Questions
If feasible, it would be beneficial to include comparative experiments in order to demonstrate that the method proposed in this paper offers more advantages than alternative approaches.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes a lie detector for LLMs that works by answering unrelated follow-up questions and requires no access to internals. This is an interesting topic that relates to hallucinations but still has not received a lot of attention on its own. The author's method strikes through simplicity, which is a positive aspect. However, the paper is a tough read due to a confusing structure and lack of proper formalization (pseudocode, definitions). Furthermore, the scenario and evaluation appear insufficient. I hope that the detailed comments help the authors to improve their manuscript.

Detailed:
* Large language models (LLMs) can “lie”, which we define as outputting false
statements despite “knowing” the truth in a demonstrable sense.
 -> this is fuzzy definition. Say a model is prompt sensitive (non-robust) and output the wrong reply for a slighlty modified prompt, according to this definition, this would be lying. A formal treatment of lying (or deceiving)  that might help in a proper definition can be found, e.g., in
 Schneider, J., Meske, C., & Vlachos, M. (2020). Deceptive AI explanations: Creation and detection. arXiv preprint arXiv:2001.07641.
* After reading the intro the question arises: Could not lying be directly detected from the prompt? I am aware that this might not cover all scenarios covered in the paper, but it appears obvious for some that are discussed.
* Also the scenario is unclear and to what I understood there are direct lie instructions "Lie when answering the following question". I think a liar should be instructed to lie consistently (A system prompt like. "Lie to the first question and then treat the answer as truthful to avoid lie detection"). Such approaches should be evaluated. Furthermore there are different kinds of lies and different lying approaches. The paper discusses this only on a shallow level.
* The intro is very short. Crisp is good, but the balance between Abstract and intro is poor - Make the abstract shorter and prolong the intro. Also the contribution section discusses more what is actually done (and should go into the intro main part) than the contribution. Contributions are typically a short list of key points. Overall this structure should be altered.
* The paper jumps right into the experiment section without clearly describing the method (pseudocode etc.)

### Strengths
see above

### Weaknesses
 The paper proposes a lie detector for LLMs that works by answering unrelated follow-up questions and requires no access to internals. This is an interesting topic that relates to hallucinations but still has not received a lot of attention on its own. The author's method strikes through simplicity, which is a positive aspect. However, the paper is a tough read due to a confusing structure and lack of proper formalization (pseudocode, definitions). Furthermore, the scenario and evaluation appear insufficient. I hope that the detailed comments help the authors to improve their manuscript.

Detailed:
* Large language models (LLMs) can “lie”, which we define as outputting false
statements despite “knowing” the truth in a demonstrable sense.
 -> this is fuzzy definition. Say a model is prompt sensitive (non-robust) and output the wrong reply for a slighlty modified prompt, according to this definition, this would be lying. A formal treatment of lying (or deceiving)  that might help in a proper definition can be found, e.g., in
 Schneider, J., Meske, C., & Vlachos, M. (2020). Deceptive AI explanations: Creation and detection. arXiv preprint arXiv:2001.07641.
* After reading the intro the question arises: Could not lying be directly detected from the prompt? I am aware that this might not cover all scenarios covered in the paper, but it appears obvious for some that are discussed.
* Also the scenario is unclear and to what I understood there are direct lie instructions "Lie when answering the following question". I think a liar should be instructed to lie consistently (A system prompt like. "Lie to the first question and then treat the answer as truthful to avoid lie detection"). Such approaches should be evaluated. Furthermore there are different kinds of lies and different lying approaches. The paper discusses this only on a shallow level.
* The intro is very short. Crisp is good, but the balance between Abstract and intro is poor - Make the abstract shorter and prolong the intro. Also the contribution section discusses more what is actually done (and should go into the intro main part) than the contribution. Contributions are typically a short list of key points. Overall this structure should be altered.
* The paper jumps right into the experiment section without clearly describing the method (pseudocode etc.)

### Questions
see above

### Soundness
3 good

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors propose a simple methodology to detect whether an LLM’s response is a lie (an answer that is false, even though the model can produce the correct answer). Authors use a set of fixed elicitation questions to probe a model and only use the responses to these followup questions to predict whether an LLM lied. The results demonstrate that this methodology is surprisingly accurate and has intriguing generalization properties.

### Strengths
1. The problem definition is strong and seems impactful. That is, the concept of lying for an LLM is formalized as LLMs producing a false statement while being able to accurately produce the correct statement. The toolbox proposed in the paper contributes to having practical reliability safeguards for existing LLMs.

2. I am surprised and excited to see that the lie detector generalizes to different architectures and distributions of input text, which further adds to the value of the proposed methodology. Specifically, this allows the design of general-purpose lie detectors that are cheap to implement across a variety of settings. 

3. I am also very curious about the underpinnings of the observed behavior, which is very novel and not have been discussed before to the best of my knowledge. Specifically -- what are the mechanisms that relate the lying behavior to the answers to seemingly unrelated questions? Although the paper does not provide concrete explanations as to why the classifiers surprisingly work very well, these properties motivate several interesting questions to pursue for future work.

4. The authors did extensive evaluations to make sure that the results were not due to spurious correlations, such as simply picking up on the repeated lying behavior, but have more going on (i.e. the fact that responses to ambiguous questions can also predict the lying behavior).

### Weaknesses
1. (Lack of Descriptive Discussion) I would have loved to see more on what the classifier may be picking on; or what the suggested inductive biases may be. As it stands, it is rather a mysterious result. However, I do not find this to be a significant limitation, as the results are thorough, and future work can further investigate this phenomenon.

2. (Labeling for Correctness) The way authors labeled an answer as correct/incorrect appeared slightly brittle to me (in that the correctness of a model’s response is defined as whether an LLM’s response contains the ground truth entity). For instance, a response could still mention the ground truth entity and be wrong. For example, if the ground truth is "Paris" and the model responds "The capital of France is not Paris", the response would be labeled as correct, which is incorrect. This approach also does not account for cases where the model might provide a synonym or a more descriptive answer that is still factually correct but does not contain the exact ground truth entity. However, I acknowledge that evaluating natural language generations is challenging and still an open research area, thus this limitation is hard to address.

3. (Lack of ablation) I would also be curious to see how redundant the set of 48 questions is, the set of questions and the number of questions is somewhat arbitrary and I’m curious how the authors reached this number. Can we achieve the same performance with only 2 ambiguous elicitation questions? What happens if the authors just keep the top 2 questions with the largest weights? What does that imply? It is unclear if all 48 questions are necessary or if a smaller subset could achieve comparable results. The lack of ablation studies on the number and type of elicitation questions makes it difficult to assess the robustness and efficiency of the proposed method.

4. (Presentation) There is a lot to unpack, and I had a bit of a hard time following Sections 4 and 5. I think one factor was that the presentation of the dataset is rather scattered (4.1, 4.2), and the methodology is rather scattered (4.3, 5.2). There are also quite a bit of details deferred to the Appendix (e.g. finetuning details), which makes reading very nonlinear.


Minor

1. There are a lot of numerical data in the paper that are inline, which makes it a bit hard to see when one needs to recall previous related results. I’d appreciate having most of the results contained in tables in the main text, however, I can also see that the space is a limiting factor.

### Questions
1. Regarding W3: Have the authors performed any ablations for the number of questions? Otherwise, how did the authors reach the number 48 / other more granular numbers for each of the factual / ambiguous questions?

2. Similar to Q1: I’d be curious to see a study around performing lasso/feature selection experiment to see how far this number can be reduced or is saturated.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good
