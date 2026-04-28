# Decoding Reading Goals from Eye Movements

- Decision: Reject
- Avg Score: 5.75
- Scores: 8, 6, 3, 6

## Abstract
Readers can have different goals with respect to the text they are reading. Can these goals be decoded from the pattern of their eye movements over the text? In this work, we examine for the first time whether it is possible to decode two types of reading goals that are common in daily life: \emph{information seeking} and \emph{ordinary reading}. Using large scale eye-tracking data, we apply to this task a wide range of state-of-the-art models for eye movements and text that cover different architectural and data representation strategies, and further introduce a new model ensemble. We systematically evaluate these models at three levels of generalization: new textual item, new participant, and the combination of both. We find that eye movements contain highly valuable signals for this task. We further perform an error analysis which builds on prior empirical findings on differences between ordinary reading and information seeking and leverages rich textual annotations. This analysis reveals key properties of textual items and participant eye movements that contribute to the difficulty of the task. Data will be made publicly available.}

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
In their paper, the authors explore the option of predicting the goal of a person while reading a text. They distuingish between two different natural reading options. The first setting is a ordinary, general reading for pleasure, context, or prose. The second setting is a sharp turn, where the reader has a specfic goal in mind, answering in question, mimicing application scenarios for every person in daily life.

These are the two labels, for several binary classification models that try to distuingish, given the eye movements, and optionally the text, the goal of the reader. They also introduce a new way of interpreting the model's results using linear mixed models.

### Strengths
The paper was a pleasure to read. It introduces all relevant background regarding eye movements and reading, has a clear outline and follows a nice story.

Related work is exhaustive and paints a good picture of both machine learning models used in any kind of reading setting as well as eye-tracking-while-reading in general. They then introduce several machine learning models which consume either eye movements, the text that was read during the recording, or both.

### Weaknesses
The only true weakness is that the authors do not introduce a new model which exploits the eye movement while reading setting the authors investigate. 

Standard error not report, additionally, no statistical significance tests were done between trainable models, e.g. best model vs rest. The critical span (8./9. in the linear mixed effect model) for interpretability only works for already known texts. For binary classification AUROC would also be a great metric to report. 

Unfortunately, the anonymous repository is not accessible, as well as the data.

### Questions
- Why didn't you report AUROC?

### Soundness
3

### Presentation
4

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper explores a novel task of predicting reading goals - specifically distinguishing between information-seeking and ordinary reading - based on eye movement data. Utilizing an extensive dataset and advanced machine learning models, the authors demonstrate that eye movement patterns contain valuable signals for goal decoding. The study systematically evaluates several state-of-the-art models, including both eye-movement-only and multimodal (eye movements + text) approaches, and introduces an ensemble model that further improves prediction accuracy. The paper provides an in-depth error analysis, identifying key challenges in goal decoding and highlighting textual and participant-specific factors affecting classification difficulty.

### Strengths
Originality: The study introduces a novel problem - decoding reading goals from eye movements - that has not been widely explored. This new application area could encourage further research in cognitive science and multimodal data analysis.
Quality: The use of diverse models and a comprehensive evaluation protocol ensures the quality and reliability of the findings. The error analysis is particularly valuable, as it provides insights into the factors that influence classification success, such as the presence of critical spans and reading time.
Clarity: The paper explains the decoding task well and provides a logical flow of ideas. The inclusion of various model types and a mixed-effects model analysis demonstrates a comprehensive and thought-out approach.
Significance: This study lays a foundation for understanding goal-oriented reading behaviors. While applications are currently exploratory, the findings could aid cognitive science researchers and developers of educational tools who aim to personalize learning experiences based on user behavior.

### Weaknesses
Complexity in Model Descriptions: Some model descriptions lack clarity, especially in multimodal integration approaches. Providing visual diagrams or more intuitive breakdowns could make these sections more understandable. Specifically, the description of how eye-movement features are combined with text embeddings is vague. For instance, it is unclear whether the text embeddings are static or dynamically updated based on the eye-movement data, and what specific fusion techniques (e.g., concatenation, attention mechanisms) are employed. The paper would benefit from a more detailed explanation of the architecture, including the dimensions of the input and output layers, and the specific activation functions used in the multimodal models.

Limited Scope of Goal Types: The study only explores two reading goals (information seeking and ordinary reading). Extending this research to other goals (e.g., skimming, proofreading) could make the findings more broadly applicable. The current binary classification limits the practical utility of the model. For example, in real-world scenarios, readers may engage in a variety of reading strategies, such as scanning for specific keywords or reading for comprehension. The model's inability to distinguish between these nuanced goals restricts its applicability in diverse reading contexts. Furthermore, the paper does not discuss how the current model could be adapted to accommodate additional reading goals, which is a crucial consideration for future research.

### Questions
Could the authors clarify how reading goal classification would perform in real-world applications where eye-tracking calibration is variable, such as web-based eye tracking?
Have the authors considered testing whether other task-specific goals (e.g., skimming) could also be accurately predicted using these models?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper adopts an existing dataset and existing methods to test reading goal prediction, which consists in predicting if a human is performing ordinary reading or information seeking (binary classification task). In addition to testing existing methods, the authors introduce a model ensemble which shows improved performance, highlighting that different models capture different information. Finally, the authors study how different trial features affect the model's prediction. Reading time before/after critical span, critical span length and paragraph position seem to be the most crucial features.

### Strengths
Originality. The paper proposes an interesting research question, i.e. if one can distinguish between two reading tasks based on eye movements (+ text). This can be seen as an extension of previous work, in particular [1]. The authors suggest that their paper has broader scope and ecological validity than [1]. While this represents an important and valid extension, it is not particularly stark in originality. The methodologies are all adapted from previous works, as well as the data. While taking a different perspective, the conceptual framework is almost identical to previous work [1,2].

Quality. The methods used are appropriate and the analysis performed is appropriate, well presented, and interpreted. The authors released their code, which together with the implementation details provided in the paper should make the results reproducible.

Clarity. The paper is well written and exhaustively reports implementation details. To further improve clarity, I would add a more clear explanation of the difference between the proposed task (reading goal classification) and reading comprehension. 

Significance. The paper represents an interesting contribution to the field of psycholinguistics, exploring a new task. The analysis in Section 6 highlights important features to consider when studying eye movements on text. 

[1] Hollenstein, Nora, et al. "ZuCo 2.0: A Dataset of Physiological Recordings During Natural Reading and Annotation." Proceedings of the Twelfth Language Resources and Evaluation Conference. 2020.
[2] Shubi, Omer, et al. "Fine-Grained Prediction of Reading Comprehension from Eye Movements." arXiv preprint arXiv:2410.04484 (2024).

### Weaknesses
- As discussed above, the paper is an interesting extension of previous work but does not particularly shine in terms of originality.

- The authors do not discuss limitations of current methods or dataset. The authors briefly mention the need for different tasks and datasets in Section 8, but I believe a more structured and systematic discussion of limitations is necessary. For example:
  - The paragraphs considered in the study are all short. Do the findings generalise to longer text? 
  - Being taken from newspaper articles, all the paragraphs are expository - they provide information. Do the authors expect to find similar results for, e.g., narrative texts written to entertain? 
  - There are differences between different reading comprehension tasks [1]. For example, students that read a text when doing an exam have likely a different behaviour than students that read just to understand the text. Are these differences relevant to this paper?  

- The scientific implications of the authors’ findings can be better discussed. Based on their findings, how can we improve current methods? How can we fully exploit the potential of eye movements for such a task? 

- While the authors state that reading is an ubiquitous and essential skill, the paper lacks an explanation of why reading goal prediction is an important task to study and which are the applications or areas that will benefit the most from that. 

- Overall, this paper presents interesting research in psycholinguistics. However, I believe its contributions are not strong and original enough to be published at ICLR. In addition, the topic would probably fit better a psycholinguistics or computational linguistics venue.

### Questions
see above

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors investigate automatic classification of reading behaviour into information seeking and "ordinary reading". They recorded a new eye tracking dataset for this task and evaluated several relevant approaches.

### Strengths
The article is very well written and easy to follow.
The experiments are extensive, sound, and deliver some meaningful insights.
The dataset can be a valuable resource for the community.

### Weaknesses
The novelty is limited: the author conduct a number of evaluations of existing methods an a new dataset.
The novelty of the task is also very marginal and incorrectly portrayed as the authors miss highly relevant previous work. Xiuge et al. (2023) distinguished deep from skim reading using eye tracking, which is very similar to what the authors claim as novelty.

Further relevant previous work that should be discussed is by Kunze et al. (2013) who distinguished different document types.
It would also be meaningful to compare the reading goal recognition task to similar tasks that were investigated with eye tracking data. One example is informational versus navigational intent classification (Sharma et al., 2023).

### Questions
no questions

### Soundness
3

### Presentation
3

### Contribution
2
