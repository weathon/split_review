## Human Reviewer 1

### Summary
This paper evaluates the capabilities of (multimodal) LLMs to produce fine-grained concept annotations. Prior work either relied on human evaluations or used downstream performance as a proxy. The key idea of this paper is that if annotations are sufficient, a LLM should be able to infer the correct class from the annotation alone (Definition 3.1).

The authors investigated concept annotations of (multimodal) LLMs through several stages of annotation refinements (l. 234-240). A so-called fast mode, where the model directly predicts the class from the input image (like in standard object recognition). In the so-called slow mode, the model progressively predicts concept annotations from coarse (e.g., background or superclass) to fine-grained levels (e.g., visual attributes such as the shape or color of bird’s wing).

The experiments show that (multimodal) LLMs generally fail to produce concept annotations that are sufficiently accurate or informative to enable correct class inference from them.

### Strengths
* S1: The finding that using more fine-grained annotations (slow mode) hurts the correct class inference for fine-grained data like CUB is surprising and interesting.

* S2: The concept annotation sufficiency definition is quite interesting. It captures well what we want concept annotations to look like.

### Weaknesses
* W1: A core issue with the evaluation framework is that a LLM is used to infer the class. There’s no guarantee that this LLM is good in inferring the correct class from the annotations.

* W2: The claim that “strong performance in downstream tasks may not correlate with adequate conceptual supervision” (l. 462/463) is too strong. Also, I’d like to note that these models often weigh the concepts or only use a subset of them on a per-instance basis. Thus, the conclusion seems not warranted. It’d be more meaningful to take, say, the top-5 concepts per image and try to see if models can infer the correct class.

* W3: The finding that (multimodal) LLMs work not that well to capture fine-grained details is well-known. The paper doesn’t provide a novel insight regarding this point.

* W4: The paper’s writing could overall be improved for clarity.

### Comments

* C1: The explanation of “utility-as-proxy assumption” is very unclear and would be good to refine for better clarity.

* C2: Comparing the 0-shot classification performance to the concept annotation is likely not that fair. Because, for example, these models might have seen the dataset, so the fast-mode numbers might be therefore a too optimistic estimate. However, I understand that this might be hard to control for the authors and, thus, only listed it here as a comment.

### Questions
* Q1: Limiting the number of classes to four plus the correct class seems very constraining. Why did the authors choose this setting?

* Q2: How would concept annotators that also include distinguishing similar classes compare? The prompts (Appendix B) don’t focus on this aspect and therefore the models might yield annotations that can be confused with other classes.

* Q3: Regarding Fig. 3: What makes post-hoc textual annotations so much stronger than visual-grounded annotations?

* Q4: How do models compare on ImageNet in Tab. 3?

### Soundness
2

### Presentation
2

### Contribution
2

### Rating
2

### Confidence
4

---

## Human Reviewer 2

### Summary
This paper investigates whether large language models (LLMs) and vision-language models (VLMs) can serve as reliable automated annotators for concept-based explainable AI (XAI) systems. 
The work introduces the Fast and Slow Effect (FSE) framework, which evaluates the sufficiency of concept-class annotations without human supervision. 
FSE models the annotation process as a continuum from a fast (opaque, intuitive) mode to a slow (explicit, conceptual reasoning) mode, and introduces a new metric, the Class Representation Index (CRI), to quantify whether generated concepts adequately represent the target class.
Through experiments on fine-grained and general vision datasets (e.g., CUB-200, Cars-196, CIFAR-100), the authors find that current LLM-generated annotations are often insufficient, particularly in fine-grained classification. 
Surprisingly, “slow” conceptual reasoning frequently underperforms the “fast” intuitive mode, suggesting that models possess implicit visual knowledge they struggle to express explicitly. 
The paper also critiques the “utility-as-proxy” assumption, that higher downstream accuracy implies better annotation quality, showing this correlation breaks down under FSE analysis.

### Strengths
- The FSE framework is an original and well-motivated contribution that systematically examines annotation sufficiency, filling a notable gap in XAI evaluation methods.

- The paper offers a convincing empirical analysis revealing a consistent gap between intuitive inference and explicit conceptual reasoning, raising important questions about the interpretability of LLM-driven explanations.

- The paper is well-organized, clearly written, and transparent about procedures, datasets, and metrics, which enhances reproducibility and conceptual clarity.

### Weaknesses
- The definition of sufficiency is somewhat circular and lacks grounding in formal interpretability theory. It might mistake a good result for true understanding.

- The five-stage annotation process (Background, Superclass, Salient, Detailed, Auxiliary) may heavily influence results. The robustness of findings to prompt variations or alternative hierarchies is unexplored.

- Although the paper critiques “utility-as-proxy,” its proposed CRI metric is still accuracy-based, measuring recoverability of class labels rather than interpretive richness or human-understandable sufficiency.

- The current research strictly limits its focus to image data. Therefore, its effectiveness is uncertain for other forms, such as text, tabular data, time series, or mixed-media reasoning.

### Questions
- How can CRI or FSE be extended to capture human interpretability, not just internal consistency?

- Would the same phenomena occur in text-only domains (e.g., sentiment analysis explanations) or multimodal reasoning tasks beyond classification?

- Can fine-tuning LLMs explicitly for conceptual disentanglement improve slow-mode sufficiency, or is this limitation architectural?

- Is there empirical evidence that higher CRI correlates with human trust or usability of explanations? Without this, the framework’s practical XAI relevance remains uncertain.

### Soundness
3

### Presentation
3

### Contribution
3

### Rating
6

### Confidence
3

---

## Human Reviewer 3

### Summary
This paper investigates the problem of explainable AI in deep learning, whether large language models (LLMs) and vision-language models (VLMs) can generate reliable concept-based annotations. While previous studies have shown that LLMs can produce plausible annotations, the semantic adequacy of these annotations is unclear. To address this, the paper introduces the Fast and Slow Effect (FSE) framework, an autonomous self-evaluation methodology. FSE transitions annotation from a fast mode to a slow mode and evaluates each stage using a Class Representation Index (CRI) metric, which measures how well accumulated concepts represent their target classes. Experiments conducted on various visual classification datasets demonstrate that current annotations generated by LLMs lack sufficiently conceptual depth and need more effective and transparent strategies.

### Strengths
1. The paper is well written, and its motivation is clear.
2. This paper proposes a new explanatory framework that can automatically evaluate annotation sufficiency without human intervention. 
3. The paper conducts experiments on fine-grained and common datasets with various model families and further re-examines the utility-as-proxy evaluation.

### Weaknesses
1. The paper initially discusses annotations for both LLMs and VLMs; however, the proposed methodology and experiments focus only on the explanation of vision tasks with VLMs, without evaluating textual explanation tasks or reporting results for LLMs.
2. The reliability of the concept-chain gathering process and the CRI metric as accurate measures of “semantic sufficiency” remains unclear, as they have not been rigorously validated through human evaluation.

### Questions
1. How sensitive is the prompt design to different vision tasks? The current five-stage refinement process is evaluated only on general-domain datasets. How well does this template perform in generating visual concepts for more specialized domains, such as medical imaging?
2. The concept generation process follows a hierarchical structure, for example, from background to detailed features. How does the order or number of steps in this concept chain influence the final results?

### Soundness
3

### Presentation
3

### Contribution
3

### Rating
6

### Confidence
3