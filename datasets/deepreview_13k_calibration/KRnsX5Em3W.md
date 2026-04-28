# LLMs Know More Than They Show: On the Intrinsic Representation of LLM Hallucinations

- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 6, 6, 8

## Abstract
Large language models (LLMs) often produce errors, including factual inaccuracies, biases, and reasoning failures, collectively referred to as ``hallucinations''.
Recent studies have demonstrated that LLMs' internal states encode information regarding the truthfulness of their outputs, and that this information can be utilized to detect errors.
In this work, we show that the internal representations of LLMs encode much more information about truthfulness than previously recognized.
We first discover that the truthfulness information is concentrated in specific tokens, and leveraging this property significantly enhances error detection performance.
Yet, we show that such error detectors fail to generalize across datasets, implying that---contrary to prior claims---truthfulness encoding is not universal but rather multifaceted.
Next, we show that internal representations can also be used for predicting the types of errors the model is likely to make, facilitating the development of tailored mitigation strategies.
Lastly, we reveal a discrepancy between LLMs' internal encoding and external behavior: they may encode the correct answer, yet consistently generate an incorrect one.
Taken together, these insights deepen our understanding of LLM errors from the model's internal perspective, which can guide future research on enhancing error analysis and mitigation.%
\footnote{Our code is available in \repo.}

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper examines the internal representations of large language models (LLMs) to understand how they encode truthfulness and produce hallucinations—errors such as factual inaccuracies and reasoning failures. Through an approach involving probing classifiers, the authors identify truthfulness signals in specific tokens, particularly in exact answer tokens. Experiments across multiple LLMs reveal that truthfulness is task-specific, with signals varying by the nature of the task. Additionally, the study develops a taxonomy of error types, finding that LLMs may encode the correct answer internally while producing an incorrect one externally, suggesting areas where error mitigation could be applied.

### Strengths
- By probing specific tokens associated with “correct” answers, the authors highlight underexplored dimensions of LLM truthfulness encoding. This approach captures nuanced error signals that extend beyond surface-level accuracy. 

- The paper demonstrates robustness by testing the approach on a variety of LLM architectures (e.g., Mistral-7b, Llama3-8b). This extensive model comparison strengthens the study’s findings by showing consistency in truthfulness encoding patterns across different architectures. 

- The detailed taxonomy of error types, including categories like “two competing answers” and “consistent incorrectness,” could help model developers diagnose and prioritize error types during model fine-tuning. 

- The study’s finding that truthfulness encoding is not universal but rather task-specific introduces an important consideration for cross-task applications.

### Weaknesses
 - While probing classifiers show strong results, the interpretability of their outputs remains unclear. For example, understanding how specific probing layer choices affect error predictions or how developers might interpret these signals is crucial for practical adoption but is not fully addressed. Including examples of how different layers and token choices impact classifier predictions would clarify the interpretability of this approach. A case study showing how interpretability of classifier outputs could inform model improvements would also be beneficial. 

- The error taxonomy could be more robust if supported by quantitative analyses on how consistently each error type appears across varying prompts or domains. Currently, it is unclear if the identified error types remain stable under different experimental conditions or across datasets. Conducting further experiments to determine if error types remain consistent under prompt variation or across domains (e.g., factual vs. commonsense tasks) could enhance the reliability of the taxonomy. These results would provide stronger support for the taxonomy as a practical tool. 

- The framework’s token-level focus may overlook broader context, potentially missing how errors manifest within larger segments of generated text. For tasks like long-form QA or summarization, this might limit the approach’s utility by not capturing interactions between tokens. Testing whether incorporating context windows around answer tokens, or analyzing sentences rather than isolated tokens, would improve accuracy could make the approach more adaptable to contextually rich tasks. Including examples where broader context improves error prediction would also strengthen this aspect. 

- Practical guidance on integrating these insights into model development workflows is limited. Developers may find it challenging to apply these techniques without clear implementation guidelines.

### Questions
1. Have the authors tested if the taxonomy of error types is consistent across various domains or tasks, and if not, would this be feasible in future work? 

2. Could the authors explain why certain model layers are more effective for probing in error detection? A discussion on this might enhance understanding of how internal representations encode truthfulness.

3. Have the authors considered using a context window around answer tokens to improve detection accuracy, especially for tasks that involve longer responses or require more context? 

4. Given the diversity in model architectures tested, are there certain architectures where the probing method performs noticeably better or worse?

### Soundness
2

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
This paper proposes that the internal representations of LLMs' responses are predictive of error patterns. Unlike previous approaches focusing on representations of last token or averaged representations, this paper focuses on representations of exact answer tokens.

### Strengths
- This paper interprets halluciantions from the perspective of token representations, particularly the exact answer tokens, which provides a relatively new perspective.
- This work demonstrates that the internal representations of LLMs' responses are skill specific rather than universal.
- The paper is well-structured and the experiments are comprehensive to demonstrate the validity of the findings.

### Weaknesses
This paper has generated some interesting findings. However, the method is hardly to be taken as general.

- This approach could be only applicable to QA tasks. For open-ended questions, can it be applied? It would be better to provide performance on these kinds of tasks as well.
- The results in table 1 show that the AUC of last generated almost match that of exact answer tokens with TriviaQA. Does this imply that actually the representations of last token and answer exact token are almost the same, especially for more general hallucinations rather than specific factual ones such as math problems? Besides, the result of Mistral is worse than that of LLaMA 3.1. Is it because the answer of Mistral involves less explanations to the question than that of LLaMA 3.1? The results in table 2 seems also demonstrate that answer exact tokens are barely better than last tokens when it comes to more generic tasks?

### Questions
- This approach could be only applicable to QA tasks. For open-ended questions, can it be applied? It would be better to provide performance on these kinds of tasks as well.
- The results in table 1 show that the AUC of last generated almost match that of exact answer tokens with TriviaQA. Does this imply that actually the representations of last token and answer exact token are almost the same, especially for more general hallucinations rather than specific factual ones such as math problems? Besides, the result of Mistral is worse than that of LLaMA 3.1. Is it because the answer of Mistral involves less explanations to the question than that of LLaMA 3.1? The results in table 2 seems also demonstrate that answer exact tokens are barely better than last tokens when it comes to more generic tasks?

### Soundness
4

### Presentation
4

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
This paper presents a novel approach to investigating hallucinations in LLMs by using probing classifiers to analyze their internal representations. The approach involves analyzing internal model representations to determine how LLMs handle factual versus hallucinatory information. The proposed approach is evaluated through multiple experiments on various LLMs and datasets, offering new insights into understanding and mitigating hallucinations in these models.

### Strengths
- The paper is well-structured, and the motivation is clearly communicated.
- The experiments effectively demonstrate how probing classifiers reveal the internal mechanisms of LLMs.
- The results highlight significant discrepancies between internal representations and generated outputs, offering a deeper understanding of how hallucinations manifest and potential ways to mitigate them.

### Weaknesses
 - It would be better to clarify the specific model used for the probing classifier and provide more details on the training setup (e.g., hyperparameters, optimizer, detailed dataset split information).
- From the experimental results presented in Section 4, it seems that the generalization ability of the probing classifier across different tasks is relatively limited. For instance, many AUC scores are in the range of 0.5 to 0.6, which suggests that the classifier's performance is only slightly better than random guessing. Could you elaborate on possible reasons for this limited generalization, and suggest any potential ways to enhance it?
- Have you considered conducting generalization tests across different LLMs, in addition to testing across different datasets? For instance, how would a probing classifier trained on output generated by Mistral-7b perform when tested on Llama3-8b? This approach could provide better insight into whether the probing classifier remains effective when applied to activation states across different LLMs.

### Questions
- It would be better to clarify the specific model used for the probing classifier and provide more details on the training setup (e.g., hyperparameters, optimizer, detailed dataset split information).
- From the experimental results presented in Section 4, it seems that the generalization ability of the probing classifier across different tasks is relatively limited. For instance, many AUC scores are in the range of 0.5 to 0.6, which suggests that the classifier's performance is only slightly better than random guessing. Could you elaborate on possible reasons for this limited generalization, and suggest any potential ways to enhance it?
- Have you considered conducting generalization tests across different LLMs, in addition to testing across different datasets? For instance, how would a probing classifier trained on output generated by Mistral-7b perform when tested on Llama3-8b? This approach could provide better insight into whether the probing classifier remains effective when applied to activation states across different LLMs.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper conducts extensive experiments and verifies through probing that LLMs possess an implicit understanding of truthfulness within their hidden representations. However, due to certain calibration issues, even though the model "knows" the truth, it can still produce incorrect outputs. Additionally, further experiments show that probing is not a general-purpose tool for detecting hallucinations; it is task-specific.

### Strengths
- Originality: The understanding of hallucination is accurate, and the exploration of the model’s self-knowledge capabilities provides deeper insights. Perspective of shifting focus from human-centric to model-centric is pinpoint and insightful.
- Quality: The experiments are thorough and well-executed.
- Clarity: The paper is structured clearly, making it easy to follow.
- Significance: This work is valuable for future research, especially for studies focusing on how models internally grasp factuality.

### Weaknesses
 - **On the definition of hallucination**: The paper's definition of hallucination remains somewhat vague. As discussed in [this paper](https://arxiv.org/abs/2407.14507), hallucination can be understood as *inconsistency* between a model’s expression and world knowledge it has learned from its training corpus.

- **Missing experiments**: On p.6, the paper states that “the primary conclusion is that information about truthfulness is highly localized in specific generated tokens.” Given this claim, I believe an additional experiment is necessary: measuring the accuracy of the model when prompted to produce exact answers under restricted conditions. This would provide more direct evidence supporting the localization of truthfulness in generated tokens. Specifically, the paper should evaluate the probe's performance when the model is constrained to generate short, factual answers, as this would more directly test the claim of localized truthfulness encoding. The current experiments, while thorough, do not isolate this aspect sufficiently.

- **Lack of clear direction for next steps**: The paper does not explicitly outline what future steps can be taken. If we now accept that "the model latently and task-specifically knows what truthfulness is," how can we leverage this finding to help a general-purpose LLM handle unpredictable tasks? Or, how can this work help researches avoid futile efforts? The practical applications of these insights are not clearly addressed.

### Questions
- **On p.3, Section 3.1**: Which model, $M$, did you use to generate responses when constructing the triplet dataset?
- **On p.5**: What is the accuracy of Mistral-7b-Instruct when extracting the exact answer token? Or did you assume that all extracted tokens are correct without further validation?
- **On p.5, fig. 2**: The statement “Middle to later layers typically yield the most effective probing results” seems inaccurate. The figure does not show a clear pattern supporting this claim.
- **On p.8**: Why were the error patterns not designed to be orthogonal? Could you provide a definitive reason for this decision?
- **On p.10, fig.5**: What do the different colored bars represent in the figure? Please clarify the meaning of the different colors.

### Soundness
4

### Presentation
4

### Contribution
3
