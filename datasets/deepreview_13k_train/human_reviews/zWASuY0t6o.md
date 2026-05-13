# Focus On This, Not That! Steering LLMs With Adaptive Feature Specification

- Decision: Reject
- Scores: 5, 3, 5, 8

## Abstract
Despite the success of Instruction Tuning (IT) in training large language models (LLMs) to perform arbitrary user-specified tasks, these models often still leverage spurious or biased features learned from their training data, leading to undesired behaviours when deploying them in new contexts. In this work, we introduce \emph{Focus Instruction Tuning} (FIT), which trains LLMs to condition their responses by ``focusing on'' specific features whilst ignoring others, leading to different behaviours based on what features are specified. Across several experimental settings, we show that focus-tuned models can be adaptively steered by focusing on different features at inference-time: for instance, robustness can be improved by focusing on task-causal features and ignoring spurious features, and social bias can be mitigated by ignoring demographic categories. Furthermore, FIT can steer behaviour in new contexts, generalising under distribution shift and to new unseen features at inference time, and thereby facilitating more robust, fair, and controllable LLM applications in real-world environments.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces Focus Instruction Tuning, a finetuning strategy for focusing LLMs on specific features.  The method is applied to classification settings with spurious correlations.  Results shown on three tasks indicate for potential to mitigate bias over traditional finetuning.

### Strengths
- The proposed work targets improving robustness to spurious correlations. Improving robustness to spurious correlations is an important problem  that has been well studied in classification problems and is also important to study for more recent LLMs.  
- The paper is overall well-written.  I appreciate the authors have highlighted the key takeaways one act experiment.

### Weaknesses
 - The experiments for the paper consider older tasks including NLI and sentiment.  These datasets are old, and there are already many existing approaches for reducing bias in these datasets which the authors have not considered in this work.  I recommend the authors to compare against existing approaches for example: https://aclanthology.org/2020.acl-main.769/ and https://aclanthology.org/2022.acl-long.190.pdf.  Further the author could consider more recent benchmark tasks that the models are typically evaluated on as even the included QA dataset is a few years old (2022).
- The proposed method is limited to classification in the experiments, however there are also many tasks these LLMs are capable of including general QA, MCQ, generation, etc. which may have bias and also important to study.
- The evaluations that are done do not seems to be consistent with prior works as they separate based on the label for computing accuracy.  Could the authors also include the full accuracy on the datasets for comparison with prior work?

### Questions
- Can the authors clarify on the difference between FIT and IT? More specifically how is the $I_{focus}$ included in the data? Is this included for the IT comparison, or is the data left out? I believe including this data as part of $x$ would be a necessary comparison as well.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
In this paper, the authors propose an instruction fine-tuning method called Focus Instruction Tuning (FIT), designed to guide large language models (LLMs) to prioritize causal features while disregarding spurious ones. Specifically, the authors construct an instruction fine-tuning dataset based on Equations (1) and (2), categorizing the desired output labels into four groups. The concurrence rate between spurious features and labels is adjusted at various levels to control the difficulty of the test set. In the experiments, the authors evaluate the model’s focus instruction capability, denoted as $\hat{y}\sim p_{\theta}(y|I,I_{text},x)$, representing the probability of predicting the label given the focus instruction. The metric $A_{focus}$ is used to compare different methods.

### Strengths
This paper is well written and easy to follow.

### Weaknesses
I have several concerns about this paper:

1. It appears that both training and evaluation require prior knowledge of spurious features (relative to a given model), which may be challenging in practical applications.

2. This approach primarily enhances instruction-following in a narrow domain — specifically, where the model learns to "focus on X while ignoring Y" — rather than truly mitigating spurious correlations. After training, the model still relies on "focus and ignore" instructions to control its output.

  According to my experiment, part of the spurious correlation problem originates from the supervised fine-tuning (SFT) data itself, highlighting the importance of data quality and diversity, as emphasized in technical reports for models like LLaMA and Nemotron. For instance, Nemotron achieves this by applying a Cartesian product over task diversity (e.g., open Q&A, writing), topic diversity (e.g., STEM, humanities), and instruction diversity (e.g., JSON output, yes-or-no answers). FIT seems to add only a single dimension of variation ("focus and ignore") to the SFT data.

3. While FIT demonstrates an improvement in the model's ability to follow "focus and ignore" instructions, this is expected given that the model is specifically trained on such patterns. However, it is unclear how this affects other instruction-following abilities — do they remain stable, or do they degrade? Can author demonstrate that?

### Questions
See my comments on the weakness

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper introduces Focus Instruction Tuning (FIT), a method designed to guide Large Language Models (LLMs) in emphasizing specific features or disregarding others during task execution. FIT addresses limitations in traditional Instruction Tuning (IT) by training LLMs to avoid spurious correlations and biases, thereby enhancing model robustness and fairness. This approach enables adaptive focus on task-relevant features, leading to improved performance in scenarios involving distributional shifts and unfamiliar contexts. Empirical evaluations across multiple NLP tasks demonstrate FIT's effectiveness in managing various spurious and causal features and in mitigating biases.

### Strengths
1. **Originality**: FIT's feature-based focus approach offers flexibility in controlling LLM responses based on specified attributes, advancing traditional instruction tuning techniques. However, this technique in my opinion can be viewed as a variant of context distillation, which limits the originality of this paper. 
2. **Quality**: The experiments are comprehensive, encompassing various LLM models, datasets, and evaluation conditions. The robustness of FIT against spurious correlations and distribution shifts is well-documented, establishing the method's adaptability and efficacy.
3. **Clarity**: The methodology is detailed and clear, with illustrative examples and visualizations that support understanding of FIT’s impact. However, further contextualization of feature selection strategies could enhance comprehension.
4. **Significance**: FIT’s potential to mitigate biases and enable feature-based focus presents meaningful advancements in applying LLMs in ethically sensitive areas, such as fair NLP applications and explainable AI.

### Weaknesses
1. **Overlap with Context Distillation**: FIT shares similarities with context distillation methods, potentially limiting its distinctiveness and raises the question of where FIT truly diverges from established context distillation approaches. For instance, studies such as Snell et al. (2022) on learning by distilling context (https://arxiv.org/abs/2209.15189) explore related concepts. I first saw context distillation in Anthropic’s first paper: https://arxiv.org/abs/2112.00861 So I think it’s probably fairly well-known at this point. Additional comparisons with established context distillation methods could clarify FIT’s unique contributions. The authors may benefit from clarifying these distinctions to strengthen the paper's contributions and make its novel aspects more apparent.
2. **Dependence on Human Guidance**: FIT relies on human intervention to determine which features are task-relevant or spurious, which may not be feasible in highly dynamic or uncertain domains. Automation in identifying these attributes would improve applicability.
3. **Generalization Challenges**: The model's ability to generalize across unseen, highly overlapping features is noted as a limitation. More discussion on addressing this would help clarify FIT’s potential for broader generalization.

### Questions
1. Could the authors provide more insight into automating feature selection for focus tuning? How does FIT handle feature ambiguity in complex datasets?
2. How does FIT compare empirically with existing context distillation methods, and what unique improvements does it provide over these methods?
3. Are there additional strategies the authors could explore to enhance FIT’s generalization on overlapping features, especially in high-dimensional feature spaces?

### Soundness
3

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
Motivated by the observation that instruction-tuned LLMs tend to overly rely on spurious features, this paper proposes a new method, FIT, for instruction tuning LLMs while focusing on or ignoring certain features in the input. The method is a simple, intuitive modification to standard instruction tuning to include an additional focus instruction, such as "Direct your attention solely to X" or "Exclude Y entirely from your evaluation." Models trained with FIT can then be flexibly guided to focus on or ignore certain features at inference time, by modifying the prompt in a similar way. The authors evaluate FIT on three models across three datasets, presenting promising results for reducing over-reliance on spurious correlations and mitigating bias involving demographic attributes. The authors also show that models trained with FIT can also generalize to focus prompts other than those in the training data.

### Strengths
- FIT is a simple, intuitive, and effective idea.
- The paper is well-written and clear. The diagram in fig 1 and the remaining figures are clearly presented.
- Over the three models and three evaluations presented, FIT appears to be effective (though see my questions below), showing an improvement over the standard IT baseline.
- The paper presents reasonably thorough evaluations. Manipulating the extent of the spurious correlation, and which label it is correlated with, is a particularly nice addition.
- Fine-tuning to actively focus on the spurious feature and ignore the causal feature provides an interesting control and highlights the flexibility of the method.
- The ablations in section 5 demonstrate that the model does not overfit to the specific focus prompts used during training.

### Weaknesses
There are a number of weaknesses that at the very least warrant some discussion.
1. Training using FIT requires access to ground-truth information about which features are spurious and which are causal, or group attributes in a fairness setting. These are often unavailable, or undesirable to collect. How do the authors expect FIT to perform if, for example, trained on a dataset where y_spurious is available, but tested in a different setting where unavailable? It would be helpful if the authors could discuss this in their limitations section. Furthermore, the method's reliance on explicit spurious feature labels during training raises concerns about its applicability in real-world scenarios where such labels are difficult or impossible to obtain. The paper should discuss the potential for using proxy labels or automated methods for spurious feature detection, and how these might impact the effectiveness of FIT. The current framing assumes a level of annotation that is often not feasible, and this needs to be addressed more thoroughly.
2. The work is restricted to classification settings, rather than open-ended generation. This is a reasonable assumption but also significantly limits the applicability of the approach. This should be discussed in the limitations section, if not earlier. The restriction to classification and multiple-choice question answering (MCQA) tasks limits the scope of the method. While MCQA can be viewed as a form of classification, the paper does not explore the more complex challenges of open-ended text generation, where controlling for spurious features is arguably more difficult. The authors should discuss the potential challenges and adaptations required to extend FIT to generative tasks, such as summarization or dialogue generation.
3. While the evaluations are reasonably comprehensive, the paper would benefit greatly from an explicit test of out-of-distribution generalization w.r.t. training domain. For example, how well would a model trained to follow instructions on SS be able to follow instructions on SMNLI without training?

To my eyes, this paper presents a flexible method for specifying which features should be used and which ignored at inference time. Yet, the authors consistently frame the paper in terms of spurious or causal features. In practice, it is often unclear whether a feature is actually casual. I wonder if the paper might benefit from framing similar to "core vs. spurious", or "intended vs. unintended", rather than "spurious vs. causal"?

**Minor**: The final section of the related work, on refocusing LLMs, is a little confusing in light of the broader arc of the paper. After reading, I half expected the authors to introduce something akin to LlamaGuard, rather than a new instruction fine-tuning method. I wonder if this could be relegated to a broader related work section later in the paper, for the sake of narrative clarity.

### Questions
1. I find it surprising that certain models able to follow Focus(C) + Ignore(S) instructions even under vanilla SFT, across all test conditions on the SS dataset (e.g. fig. 2, Mistral, SFT)? Could the authors elaborate on this, and possibly temper the claims in lines 360--362 as a result?
2. Similarly, could the authors elaborate how FIT can improve accuracy on the null focus instruction set (e.g. fig 4., Mistral, SFT vs. FIT)? I would have imagined there should be no change here?
3. Could the authors clarify at which stage FIT is applied? Is it used in place of existing instruction tuning, or a second stage after standard instruction tuning? As a broader question, do the authors have any intuition about a) whether FIT could be applied to downstream chat tuning, or b) whether chat tuning might undo some of the success of FIT?

### Soundness
3

### Presentation
3

### Contribution
3
