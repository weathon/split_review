# Uncovering Overfitting in Large Language Model Editing

- Decision: Accept
- Avg Score: 7.33
- Scores: 8, 8, 6

## Abstract
Knowledge editing has been proposed as an effective method for updating and correcting the internal knowledge of Large Language Models (LLMs). However, existing editing methods often struggle with complex tasks, such as multi-hop reasoning. In this paper, we identify and investigate the phenomenon of \textbf{Editing Overfit}, where edited models assign disproportionately high probabilities to the edit target, hindering the generalization of new knowledge in complex scenarios. We attribute this issue to the current editing paradigm, which places excessive emphasis on the direct correspondence between the input prompt and the edit target for each edit sample. To further explore this issue, we introduce a new benchmark, \thebench (EValuation of Editing Overfit in Knowledge Editing), along with fine-grained evaluation metrics. Through comprehensive experiments and analysis, we demonstrate that Editing Overfit is prevalent in current editing methods and that common overfitting mitigation strategies are of limited effectiveness in knowledge editing. To overcome this, inspired by LLMs’ knowledge recall mechanisms, we propose a new plug-and-play strategy called Learn to Inference (LTI), which introduce a Multi-stage Inference Constraint module to guide the edited models in recalling new knowledge similarly to how unedited LLMs leverage knowledge through in-context learning. Extensive experimental results across a wide range of tasks validate the effectiveness of LTI in mitigating Editing Overfit.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
In this paper, the authors focus on investigating parameter-modifying knowledge editing methods and find that existing parameter-modifying knowledge editing approaches exhibit overfitting. Specifically, when questions related to the edited subject and relation arise, the model tends to respond with the edited object, regardless of whether that object is a reasonable answer to the question.

Based on this finding, the authors propose the EVOKE benchmark to assess the degree of overfitting in previous parameter-modifying knowledge editing methods and to evaluate the effectiveness of past techniques designed to mitigate overfitting. They discover that, with the exception of Specificity Augmentation, most methods show limitations.

To address the overfitting issue, the authors introduce a plug-and-play strategy called LTI. Experimental results demonstrate that LTI is highly effective in alleviating overfitting.

### Strengths
- The overfitting issue in parameter-modifying knowledge editing methods identified by the authors is an interesting finding.

- The proposed benchmark contributes to a more comprehensive analysis of the effectiveness of knowledge editing methods.

- The authors provide extensive experimental results, conducting a detailed analysis of previous parameter-modifying knowledge editing methods and testing various previously suggested mitigation techniques.

- The LTI method proposed by the authors is a plug-and-play solution, making it convenient to integrate with previous methods for enhanced performance.

### Weaknesses
 - The proposed LTI method relies on the model's in-context learning capability. This approach requires the unedited model to generate correct answers based solely on the context of the new knowledge, thereby providing an accurate representation and output distribution constraint for the editing process. This implies that for smaller models less proficient in in-context learning, or for models particularly rigid regarding certain facts, the constraints provided by the LTI method may negatively impact editing performance.

### Questions
- I am curious whether the representation and output distribution of the unedited model are computed only once. If so, I wonder whether applying Paraphrase Augmentation to this new knowledge would improve performance. The final loss could potentially be adjusted to compute the average KL divergence across different paraphrases. The paper mentions that Paraphrase Augmentation can actually exacerbate overfitting in knowledge editing methods. Therefore, would applying Paraphrase Augmentation to the new knowledge enhance the quality of the constraint, or would it ultimately reduce the effectiveness of the edit?

### Soundness
3

### Presentation
3

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
The paper investigates the phenomenon of Editing Overfit within large language models. Editing Overfit occurs when edited LLMs assign disproportionately high probabilities to the edit target, which negatively impacts the model's generalization ability, particularly in complex reasoning tasks. The authors introduce a new benchmark, EVOKE, designed to assess overfitting in LLMs across several challenging scenarios. To address the Editing Overfit problem, the authors propose a strategy, Learn to Inference (LTI), which encourages LLMs to recall edited knowledge in a manner more consistent with their natural inference mechanisms.

### Strengths
- The paper clearly identifies Editing Overfit as a pervasive issue within existing LLM editing methods, providing evidence through extensive experimentation and analysis. The identification of this new key problem is one of the major contribution of this paper. 
- Besides identifying the problem, the paper also introduces the EVOKE benchmark with fine-grained evaluation metrics, allowing for a more systematic and comprehensive evaluation of the Editing Overfit problem.
-  The paper also carefully analyzes different potential solutions and proposed the Learn to Inference (LTI) approach, an effective plug-and-play module that is highly adaptable for integration with existing knowledge editing methods. The authors also provide a detailed evaluation across multiple LLMs and editing methods, showing that LTI effectively reduces Editing Overfit without compromising editing success.

### Weaknesses
 - It seems that LTI is only applicable in cases where the edited knowledge can be explicitly represented as knowledge triples (s, r, o, o*). However, more complex or nuanced knowledge editing tasks may not fit into this structured format, potentially limiting LTI's applicability in real-world scenarios. 
- The phenomenon of Editing Overfit and the proposed LTI approach are only tested on small-scale LLMs such as GPT-J and GPT-2. Extending the analysis to larger models, such as LLaMA-2/3 or other larger models, would provide a more comprehensive understanding of LTI’s effectiveness at scale.

### Questions
- Does knowledge editing on larger models, such as LLaMA-2/3, still suffer from the problem of Editing Overfit? How would the proposed LTI strategy perform on these larger models? 
- Are there specific types of facts or domains (e.g., factual knowledge vs. commonsense reasoning) where the problem of Editing Overfit is more severe? Likewise, is there any specific types of knowledge where LTI may be less effective?

### Soundness
3

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
The paper explores the issue of "Editing Overfit" in knowledge editing for large language models (LLMs), where edited models disproportionately favor edit targets, especially in complex tasks like multi-hop reasoning. To investigate this, the authors introduce EVOKE, a benchmark designed to assess overfitting in knowledge editing, and evaluate existing mitigation strategies, finding them insufficient. They propose a novel approach, Learn to Inference (LTI), which uses multi-stage constraints to guide models in recalling new knowledge similarly to unedited models, thus mitigating overfitting.

### Strengths
1. The paper's exploration of the overfitting problem in knowledge editing is both highly interesting and valuable, and the design of a dedicated benchmark provides an effective way to investigate it in depth.

2. The work is highly comprehensive, identifying an unexplored issue, evaluating it within multi-hop reasoning, and proposing a plug-and-play solution based on observed phenomena.

3. The writing is very clear, and the experimental design is comprehensive and well-aligned with the motivation.

### Weaknesses
1. I believe Section 5 may not be essential to the overall paper.  While it contributes some useful experimental insights with basic mitigation techniques, it does not appear closely aligned with the paper's primary contributions.  Instead, it occupies space that could be better devoted to the LTI section, which I consider more significant.

2. I understand that this work focuses on the overfitting issue in model editing.  However, to my knowledge, model editing itself performs poorly on multi-hop editing tasks, likely due in large part to the overfitting phenomenon discussed.  I suggest that the authors consider addressing this perspective in the paper.

3. I strongly recommend that the authors include a description of in-context editing approaches in relevant sections, such as Related Work or the Baseline. Compared to model editing, these methods are potentially better suited for handling multi-hop editing tasks. Additionally, relevant citations are missing, such as [1][2][3].

### Questions
1. How do the authors view the development of model editing versus in-context editing for the knowledge editing community, given that model editing presents challenges such as training overhead and overfitting?

2. I am very curious about the performance of the proposed LTI on more recent models, such as LLaMA, Mistral, and larger-scale models.

### Soundness
3

### Presentation
4

### Contribution
4
