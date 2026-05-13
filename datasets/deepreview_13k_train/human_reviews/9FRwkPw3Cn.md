# Inverse Constitutional AI: Compressing Preferences into Principles

- Decision: Accept
- Scores: 6, 8, 5, 8

## Abstract
Feedback data plays an important role in fine-tuning and evaluating state-of-the-art AI models. Often pairwise text preferences
    are used: given two texts, human (or AI) annotators select the ``better'' one. Such feedback data is widely used to align models to human preferences (e.g., \emph{reinforcement learning from human feedback}), or to rank models according to human preferences (e.g., \emph{Chatbot Arena}). 
    Despite its wide-spread use, prior work has demonstrated that human-annotated pairwise text preference data often exhibits unintended biases. 
    For example, human annotators have been shown to prefer \emph{assertive} over \emph{truthful} texts in certain contexts. 
    Models trained or evaluated on this data may implicitly encode these biases in a manner hard to identify.
    In this paper, we formulate the interpretation of existing pairwise text preference data as a compression task: the \emph{Inverse Constitutional AI} (ICAI) problem.
    In constitutional AI, a set of principles (or \emph{constitution}) is used to provide feedback and fine-tune AI models.
    The ICAI problem inverts this process: given a dataset of feedback, we aim to extract a \emph{constitution} that best enables a \emph{large language model} (LLM) to reconstruct the original annotations. 
    We propose a corresponding initial ICAI algorithm and validate its generated constitutions quantitatively based on reconstructed annotations.
    Generated constitutions have many potential use-cases---they may help identify undesirable biases, scale feedback to unseen data or assist with adapting LLMs to individual user preferences. 
    We demonstrate our approach on a variety of datasets: (a) synthetic feedback datasets with known underlying principles; (b) the AlpacaEval dataset of cross-annotated human feedback; and (c) the crowdsourced Chatbot Arena data set.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces the Inverse Constitutional AI (ICAI) problem, which seeks to generate a set of principles from a given feedback dataset. These principles serve as a concise and human-readable representation of the feedback dataset, potentially aiding in identifying annotation biases and scaling up feedback annotation. The authors propose an initial ICAI algorithm and evaluate it on four different feedback datasets. Results indicate that the summarized principles can assist large language models in reconstructing the feedback annotations.

### Strengths
1. The paper introduces a new problem, named Inverse Constitutional AI (ICAI), which aims to compress human or model feedback into principles that can help uncover biases in data annotation, enhance understanding of model performance, scale feedback to unseen data, and adapt large language models to individual or group preferences.

2. The paper proposes a straightforward method to address ICAI problems and conducts extensive experiments across four different feedback datasets to validate its approach.

3. The authors present a method to evaluate the effectiveness of the generated principles by inputting them into an LLM and requiring the model to reconstruct the original feedback datasets, with the agreement serving as an evaluation metric for the summarized principles.

### Weaknesses
1. The experimental results would be more convincing if the authors demonstrated the application of ICAI. For instance, providing experimental evidence of ICAI’s potential in addressing annotation biases and scaling up annotation would strengthen the paper. While the authors claim their algorithm can help discover annotation bias in the feedback dataset, the experiments focus solely on reconstructing the original feedback without analyzing bias discovery and annotation scaling. 

2. The proposed method has inherent limitations: (1) In the first step, the LLM generates principles based on single feedback, but some annotation biases and principles require synthesis from multiple feedbacks. (2) In the second step, K-means clustering is used to group the generated principles, which requires specifying the number of clusters in advance. In real-world scenarios, the exact number of principles is usually unknown.

3. The experimental results could benefit from deeper analysis: (1) In Section 4.2, it is unclear why GPT-3.5-Turbo’s performance does not surpass random choice. Is this due to the quality of the generated principles, or does it reflect limitations in the model’s ability to reconstruct feedback from constitutions effectively? (2) In Sections 4.1 and 4.2, the default annotator cannot achieve better agreement than random choice. This requires further explanation. Does this suggest a bias in the preference data itself, or might the model be inherently biased?

### Questions
1. What are the distinctions between “best”, “medium”, and “worst” constitutions mentioned in Appendix H?

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper proposes a novel and interesting problem, namely, inverse constitutional AI (ICAI) problem which aims to reconstruct the preference data based on some principles that are in reverse concluded from the preference data. 

As an initial algorithm, the ICAI method involves prompting the LLM to generate the principles that summarize the preference patterns within the data. These principles are cleaned via clustering, deduplication, and testing by reconstruction loss, relevance, as well as credit ordering, 

The experiments on diverse tasks and settings demonstrate its effectiveness.

### Strengths
- Very interesting and well-defined research problem.
- The ICAI method is simple and effective.
- The experiments cover various settings, including population preference, persona-based preference, and even personalized preference.

### Weaknesses
1. Static principles (with limited quantity) may lead to some information loss for summarizing the preference patterns. The number of patterns does matter. For example, in the paper of PopAlign[1], the authors have investigated the so-called elicitive contrast for preference data synthesis, which involves generating good v.s. bad principles for each instruction as the thoughts for contrastive response generation. Such dynamic (or instruction-dependent) principles may benefit from the unlimited expressivity. Thus, as one more baseline, can the author add the elicitive preference annotation method, which involves generating principles for each instruction in an online manner as the thoughts for feedback labeling (instead of generating limited principles in an offline manner)?
2. The comparison between default feedback annotators and constitution-based feedback annotators on the unaligned settings may be unfair. Since default annotators are prompted to label the normal feedbacks, while the constitution-based annotators are prompted to label the special feedbacks. Do you prompt the default annotators to flip the feedbacks?
3. Once again, principles (in natural language) may lead to some information loss for summarizing the preference patterns. In contrast, a reward model can capture the preference patterns in an implicit “language” (i.e., model parameter) form. Can the authors add a reward model such as a fine-tuned PairRM[2] as one additional baseline?

### Questions
1. Rule-based reward models are proven to be quite useful for the safety aspect [3]. Can the author compare the effects of the ICAI methods on different aspects? For example, helpful v.s. harmless?
2. Typos:
    - line 1088: the word “is” is redundant.

[3] Rule Based Rewards for Language Model Safety, OpenAI, [cdn.openai.com/rule-based-rewards-for-language-model-safety.pdf](https://cdn.openai.com/rule-based-rewards-for-language-model-safety.pdf)

### Soundness
2

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
Paper proposes a framework for interpreting preference datasets used to align large language models (LLMs) with human-like decision-making. ICAI inverts the process of constitutional AI. Rather than using a predefined constitution to guide model behavior, ICAI attempts to derive such principles from preference data. They tested constructed principles by reconstructing preference annotations.

### Strengths
1. Developing constitutional principles from feedback data is an important research problem to build an interpretable preference learning framework. 

2. This alogrithm is tested on four datasets with synthetic setting, human annotated data, individual user preferences and group preferences.

### Weaknesses
1.  Without establishing causality between the principles and annotator rationale, the framework risks over-simplifying or even misrepresenting the underlying preferences. For example, it is possible that the principles reflect incidental biases of the model or dataset rather than genuine human values. This could lead to misleading interpretations and false assumptions about user or demographic intentions.

2. ICAI's approach inherently admits multiple valid constitutions for the same dataset, depending on clustering and sampling choices. This non-uniqueness implies that each run could yield different principles that still achieve similar reconstruction accuracy. This hurts interpretation. Also ICAI seems to be influenced by initial prompt or clustering parameters as well, making it more unstable.

3. The paper primarily focuses on preference reconstruction, yet practical applications, such as bias detection, model debugging, or customization, are only discussed in passing without concrete evidence of their effectiveness. There is no emperical evidence of ICAI's practical application

4. This framework may amplify biases present in the training data by distilling these biases into high-level principles. The paper does not discuss or test for scenarios where harmful biases (such as gender or racial biases) could be encoded into the constitution, which may reinforce harmful stereotypes or skewed preferences.

### Questions
See weaknesses

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
It introduces a novel approach for understanding and interpreting pairwise preference data used in training and evaluating AI models. Traditional methods often use feedback data like pairwise text preferences to align models with human preferences, but they do not explain why one model is preferred over another. This gap in interpretability poses challenges, particularly when biases in human feedback influence model training and evaluation.

To address this, the authors propose the Inverse Constitutional AI (ICAI) problem, which involves extracting a set of natural language principles (a "constitution") from existing feedback data. This set of principles is intended to help a large language model (LLM) reconstruct the original annotations, effectively compressing complex preference data into an interpretable and concise format. The ICAI method could help reveal underlying annotator biases, provide a clearer understanding of model behaviors, and facilitate the creation of customized models aligned with individual or group preferences.

The paper outlines an ICAI algorithm with five main steps: generating candidate principles, clustering similar principles, deduplicating principles, testing principles for their effectiveness in reconstructing feedback, and filtering out less effective principles. The method is tested on synthetic datasets, human-annotated AlpacaEval data, user-specific data from Chatbot Arena, and demographic group data from the PRISM dataset. The experiments show that the generated constitutions can effectively compress and explain preference data, revealing biases and guiding models toward interpretable decision-making.

### Strengths
1. One of the standout strengths of the ICAI approach is its ability to convert complex, often opaque preference data into a set of clear, natural language principles. This enhances the interpretability of AI training and evaluation processes, allowing researchers and practitioners to understand the rules and biases underlying model behavior. Such transparency is especially valuable when assessing why certain outputs are favored, which can inform better decision-making and trust in AI systems.

2. The method provides a powerful tool for detecting potential biases embedded in human-annotated feedback. By distilling preferences into principles, ICAI helps identify systematic biases (e.g., preferences for assertiveness over truthfulness) that might not be evident from raw data alone. This can lead to more balanced and fair training processes and better-aligned models.

3. The algorithm's ability to scale feedback data into concise, human-readable principles means it can be adapted for various use cases, including creating personal or group-specific constitutions. This adaptability supports the customization of LLMs to align with individual user preferences or demographic group values, potentially improving user satisfaction and model alignment in diverse contexts.

4. The paper demonstrates that ICAI is applicable to a range of datasets, from synthetic data with known rules to complex, real-world datasets like AlpacaEval, Chatbot Arena, and PRISM. This versatility shows that ICAI can work in controlled experiments as well as in more unpredictable, user-driven scenarios.

### Weaknesses
1. One inherent limitation of the ICAI method is that it simplifies complex human annotations into a smaller set of principles, which can result in a lossy representation. This simplification means that the constitution may not fully capture the nuances of the original data. For example, subtle contextual dependencies or complex interactions between different factors influencing human judgment might be lost when distilling preferences into a concise set of rules. This could lead to a situation where the reconstructed preferences, while broadly aligned, fail to accurately reflect the full spectrum of human decision-making, especially in edge cases or when dealing with ambiguous scenarios.

2. The effectiveness of ICAI heavily depends on how well an LLM can interpret and apply the generated principles. The reliance on an LLM introduces a layer of variability, as the interpretation of the principles can differ based on the specific LLM used, its training data, and its inherent biases. If the LLM struggles to consistently apply the principles, the reconstructed annotations may diverge from the original data. This dependence on the LLM's ability to generalize and apply the principles consistently is a potential bottleneck, particularly when dealing with complex or nuanced principles.

3. The generated principles, while human-readable, may be ambiguous or open to interpretation. This ambiguity can lead to inconsistent applications of the principles, especially when dealing with edge cases or scenarios that the principles do not explicitly address. For instance, a principle like 'prefer responses that are helpful' can be interpreted differently depending on the context and the specific criteria used to define 'helpful.' This lack of precision in the principles can make it difficult to ensure consistent and reliable reconstruction of the original annotations.

### Questions
1. How well do the principles generated by ICAI transfer across different models and datasets? Can the constitutions created for one dataset be adapted effectively for use with other types of preference data?

2. How effective is ICAI at identifying subtle or less obvious biases in preference data? What specific types of biases are more likely to be detected with this approach, and which may be missed?

3. How might ICAI be extended to work with multimodal data (e.g., combining text with images or audio) or more complex preference structures beyond pairwise comparisons?

### Soundness
3

### Presentation
3

### Contribution
4
