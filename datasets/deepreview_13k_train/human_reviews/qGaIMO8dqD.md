# Explaining the Complex Task Reasoning of Large Language Models with Template-Content Structure

- Decision: Reject
- Scores: 3, 5, 6

## Abstract
The continuous evolution of pre-trained large language models with ever-growing parameters and corpus sizes has augmented their capacity to solve complex tasks. This ability, which obviates the necessity for task-specific training or fine-tuning, relies on providing the model with a language description or some task exemplars---referred to the *prompt*---that guide the desired autoregressive generation. Despite the remarkable success, the underlying mechanisms that facilitate such exceptional generalization abilities remain an open question. In this paper, we present a novel framework that formally conceptualizes answer generation for complex natural language tasks as a hierarchical *''template-content''* structure. According to our modeling, there exist pre-trained models that can automatically decompose tasks into constituent steps during autoregressive generation, through language modeling on a sufficiently large corpus, thereby solving them. Our framework offers an explanatory tool for the complex reasoning abilities of large language models from the perspective of modeling autoregressive generation tasks. Our experiments show that real-world models exhibit distinct behaviors for ''template'' and ''content'', providing support for our modeling.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a framework to explain language model's ability to solve complex reasoning tasks as parsing the input and generating the output in a "template-content" structured way. The paper theoretically formalizes this framework, and extends the framework to the hierarchical version to explain why models can solve arbitrarily complex tasks. Finally, the authors used the last-letter-concatenation task to show their T-C framework can help explain models' reasoning abilities in practice.

### Strengths
- The proposed template-content framework is interesting, and the extension to the hierarchical version is also more flexible in explaining model's abilities in solving complex reasoning tasks.

### Weaknesses
This paper made many simplified (possibly unrealistic) assumptions in its proposed theoretical framework and misses the connection to real-world tasks.
- For example, the paper assumes a model is "well trained", meaning the model can memorize all answers perfectly. The authors claimed that this assumption is "not challenging for the prevailing LLMs with a huge amount of parameters", but many existing work has shown that even the largest models could struggle with tail knowledge [1]. This assumption is particularly problematic because it sidesteps the core challenge of generalization, which is the ability to perform well on unseen data, not just memorized instances. The framework should explicitly address how the model handles novel combinations of templates and content, rather than assuming perfect memorization.
- The hierarchical extension assumes a model can decompose complex tasks well into sub-template and sub-content. But as the sub-template and sub-content can have many different combinations (especially if they are in slightly different forms as defined in Appendix A.1, based on label consistency), it is unrealistic to assume that the model is able to search in this combinatorial space efficiently and find the right template/content combination, especially when the task is very complex. The paper does not provide a mechanism for how the model navigates this combinatorial space, nor does it address the possibility of multiple valid decompositions, each with varying degrees of memorization. Thus the presented theory in its current form, doesn't seem to be sufficient in explaining model's ability to solve very complex tasks.

In addition, the experiments are rather weak and do not support the theoretical part very well.
- The two tasks used are very simple tasks, last-letter-concat and SingleEQ. In order to support the authors' claim on the *flexibility* and *generalizability* of this framework, a slightly more complex task should be presented as well. For example, on slightly more difficult algorithmic reasoning tasks like GSM8K or AQuA, can the hierarchical T-C be used to explain model's reasoning?
- The results on T/C classification is a bit ad-hoc. Based on Figure 4 right, 1) as the authors mentioned, some green bars are too short to see, so it is unclear which model "exhibits the clearest T/C distinction"; 2) can the authors provide more quantitative analysis on the ratio between the green/blue bars? from the 2nd figure and the 3rd figure, the ratios seem not very significantly different, so I'm not sure if one can indeed judge a model has a better "reasoning capability" from those ratios.
- In Figure 5, even on the simple SingleEQ task, the proposed classification already conflicts with the human intuition, so I'm not sure if this can be used in practice, especially for more complex reasoning tasks. Also on this task, the authors define content as "names, objections, and Arabic numbers", this also seems very ad-hoc and how can one apply this in general for any tasks?

Missing references, the following paper also discusses how text (similar to the "content" part defined in this paper) and patterns (similar to the "template" part defined in this paper) affect reasoning performance in language models:
- Text and Patterns: For Effective Chain of Thought, It Takes Two to Tango. Madaan et al. 2022.

### Questions
- Can the authors provide more quantitative analysis on the ratio between the green/blue bars in Figure 4?
- How can one define template/content in general for any tasks?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper aims to show the existence of the template-content decomposition of complex natural language tasks. The paper first provides proof for the UAT of casual transformers, and then proves the existence of template transformers and content transformers. The paper is not easily readable. Even though the existence of the transformers model is proved, it is not clear the implication of the theorem. This is because the Transformers function $f_T$ and $f_C$ could be much more complex than a single transformer model. Also, there is no experimental result showing such decomposition benefits the tasks either in computation efforts or task performances.

### Strengths
* Provide proof of the existence of template transformers and content transformer functions for the template-content decomposition

### Weaknesses
 * The importance of the existence of template-content decomposition is unknown. While the paper proves the existence of template and content transformers, it does not sufficiently explain why this decomposition is significant for practical applications. The paper lacks a clear explanation of how this theoretical decomposition translates to tangible benefits in NLP tasks. The theoretical results are not connected to practical implications, leaving the reader to wonder about the value of the decomposition.
* The paper does not address the complexity of the template and content transformers. The functions $f_T$ and $f_C$ could be more complex than a single transformer model, potentially negating the benefits of decomposition. The paper does not provide any analysis of the computational cost or model size of the decomposed transformers, which is crucial for understanding the practical feasibility of the approach. It remains unclear whether the decomposed models are more efficient or easier to train than a single monolithic model.
* There is no experimental result showing such decomposition benefits the tasks either in computation efforts or task performances. The paper lacks empirical validation of the proposed template-content decomposition. Without experimental results, it is difficult to assess the effectiveness of the approach. The paper does not demonstrate whether the decomposition leads to improved performance or reduced computational costs in practical NLP tasks.

### Questions
* Can $f_T$ and $f_C$ be more complex than a single transformer model? In other words, to decompose tasks that can be handled by an LLAMA 7B model, will the $f_T$ and $f_C$ be an LLAMA 70b function?

* Will such model decomposition benefit the tasks either in computation efforts or task performances? Also, will such decomposition work for more general NLP tasks such as summarization, translation, or LLM benchmark tasks including [HELM](https://crfm.stanford.edu/helm/latest/) or [lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness)

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors present a structured framework in this paper to elucidate the workings of language models, emphasizing a template-task structure for answer generation. The paper is articulate and well-structured. I do have some inquiries concerning its content

### Strengths
The explanations in the paper are clearly written in simple terms.

### Weaknesses
The authors present a structured framework in this paper to elucidate the workings of language models, emphasizing a template-task structure for answer generation. The paper is articulate and well-structured. I do have some inquiries concerning its content

The authors frequently relegate crucial details to the appendix, disrupting the continuity of the reading experience.

It would be valuable to examine cases with misclassification errors to assess the robustness of the proposed model.

### Questions
Are there alternative explanation models in the existing literature? A detailed comparison, possibly supplemented with numerical experiments, would be beneficial.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
