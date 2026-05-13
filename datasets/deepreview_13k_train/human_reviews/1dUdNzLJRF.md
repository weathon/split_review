# TICKing All the Boxes: Generated Checklists Improve LLM Evaluation and Generation

- Decision: Reject
- Scores: 5, 6, 5, 6

## Abstract
Given the widespread adoption and usage of Large Language Models (LLMs), it is crucial to have flexible and interpretable evaluations of their instruction-following ability. 
Preference judgments between model outputs have become the de facto evaluation standard, despite distilling complex, multi-faceted preferences into a single ranking. 
Furthermore, as human annotation is slow and costly, LLMs are increasingly used to make these judgments, at the expense of reliability and interpretability.
In this work, we propose \textbf{TICK} (\textbf{T}argeted \textbf{I}nstruct-evaluation with \textbf{C}hec\textbf{K}lists), a \textit{fully automated, interpretable} evaluation protocol that structures evaluations with LLM-generated, instruction-specific checklists. 
We first show that, given an instruction, LLMs can reliably produce high-quality, tailored evaluation checklists that decompose the instruction into a series of \texttt{YES/NO} questions. 
Each question asks whether a candidate response meets a specific requirement of the instruction. 
We demonstrate that using TICK leads to a significant increase (46.4\% $\to$ 52.2\%) in the frequency of exact agreements between LLM judgements and human preferences, as compared to having an LLM directly score an output.
We then show that \textbf{STICK} (\textbf{S}elf-\textbf{TICK}) can be used to improve generation quality across multiple benchmarks via self-refinement and Best-of-N selection. STICK self-refinement on LiveBench reasoning tasks leads to an absolute gain of $+$7.8\%, whilst Best-of-N selection with STICK attains $+$6.3\% absolute improvement on the real-world instruction dataset, WildBench. In light of this, structured, multi-faceted self-improvement is shown to be a promising way to further advance LLM capabilities. Finally, by providing LLM-generated checklists to human evaluators tasked with directly scoring LLM responses to WildBench instructions, we notably increase inter-annotator agreement (0.194 $\to$ 0.256).

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The authors propose TICK, a method that uses LLMs to decompose instructions into checklists composed of several YES/NO choices to address limitations in standard evaluation metrics like Elo rating and direct scoring. This approach provides a more interpretable evaluation by breaking down instructions into specific criteria. They further introduce STICK, which refines LLM responses using self-assessment based on these checklists, achieving substantial improvements compared to traditional refinement methods. Experiments demonstrate that using LLMs for checklist generation is feasible and reliable. Also, using checklists for evaluation aligns with human annotations. Based on TICK, STICK enhances the quality of LLM outputs beyond vanilla-refinement approaches. Additionally, the authors find that using checklists in human annotation significantly increases inter-annotator agreement, making the evaluation process more consistent and reliable.

### Strengths
- The automatic evaluation method using LLMs as judges is novel and significant. The authors present an effective and interpretable protocol for evaluating and refining generated text.
- Comprehensive experiments and detailed analyses are provided to support the effectiveness of the proposed methods.
- The paper is well-written and easy to follow, making it accessible to a broad audience.

### Weaknesses
1. Leveraging LLMs with simple prompts to generate checklists is a straightforward approach. Previous work has also used decomposition techniques to evaluate responses across multiple dimensions, similar to step-by-step verification of LLMs' instruction-following abilities. While this method has been applied to various evaluation metrics, to my knowledge, this is the first time it has been specifically focused on instruction-following.
2. The construction details and statistics of the Internal dataset are not sufficiently explained, which reduces confidence in the reliability of the results when using LLMs for checklist generation.
3. When evaluating the generated checklists against gold labels, the authors use metrics like ROUGE and BLEU. However, these metrics are less effective in knowledge-intensive contexts, suggesting a need for additional manual annotation or alternative metrics. However, the human annotation results are missed.
4. The preference labeling approach of annotators does not fully align with the checklist-based method for evaluating instruction-following capabilities. Human annotation will consider the quality of the response while TICK only considers instruction-following ability.
5. The low inter-annotator agreement for direct scoring raises concerns, as the authors only demonstrate TICK's effectiveness through pairwise correlation with human annotations. If the inter-annotator agreement for pairwise scoring is similarly low, it might undermine the validity of this correlation.
6. The comparison of TICK to other evaluation methods is limited to direct scoring and an ablated version (Check-then-Score). This restricts the scope of the comparison. Evaluations with fine-tuned models or well-established frameworks could provide a fairer assessment.
7. In self-refinement experiments, the baseline comparison is limited to vanilla self-refinement, which is insufficient. Incorporating additional strong baselines would provide a more comprehensive understanding of STICK's effectiveness.

### Questions
1. The caption for Figure 3(a) appears to be out of sequence or unclear. Could the authors clarify or reorder the content for better coherence?
2. The self-refinement process using STICK results in a minor decline in the last iteration, could the authors make a further explanation?

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper aims to measure and enhance LLM performance in instruction-following tasks by leveraging a powerful model to generate checklists based on the given instructions. 
The key contributions include: 
1. Proposing a prompt to generate checklists for each instruction. 
2. Validating the high similarity between checklists generated by advanced LLMs and those created by humans across several benchmarks. 
3. Showing that the judge score derived from aggregating checklists yields a pass ratio that closely aligns with human scores, highlighting the potential of using the checklist to improve the performance of LLM-as-judge. 
4. Showcasing that self-refinement guided by the generated checklists leads to higher performance improvements compared to unstructured feedback. 
5. Allowing human annotators to reference the model-generated checklists results in enhanced inter-annotator agreement.

### Strengths
Originality: This paper analyzes the quality of checklists generated by advanced LLMs and how they can be used to improve LLM-as-judge and high-quality instruction selection. It can provide experiment results for practitioners who want to use these checklists to enhance the performance of LLMs as judges, offering valuable insights.

Quality: The overall experimental analysis is thorough, including validation of LLM-generated checklists to human-generated checklists. It also features corresponding analyses on the use of checklists for self-refinement and their application as the reference for human annotators.

Clarity: The paper is written clearly, making it easy to follow and understand.

Significance: The topic of LLMs as judges is highly relevant, and the findings of this study may offer significant insights for the industry.

### Weaknesses
Novelty: Given multiple works on using checklists to enhance the performance of LLMs as judges, this paper’s contribution lies in enabling LLMs to generate their own checklists and validating their feasibility. The approach involves introducing a specific prompt to elicit the checklist from the LLM. However, this requires the LLM to first follow a complex set of instructions to generate the checklist, which places even higher demands on the model’s capabilities than the instruction-following task itself.

Experimental Limitations: From an experimental perspective, the study could benefit from considering a wider range and a larger scale dataset. Currently, it only examines three benchmarks: Internal, InfoBench, and WildBench. 

Expense: The existing design is computationally expense during inference time since it requires a large number of tokens and multiple generations during the self-refinement stages. How to distill this ability or reduce this expense can be a good direction.

### Questions
1. For table 2, why don't you consider the semantic similarity metrics such as scores generated by natural language inference models? BLEU and Rouge style metrics sometimes can be unreliable.

### Soundness
3

### Presentation
4

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
To evaluate the instruction-following capabilities of large language models (LLMs), this paper introduces a method called TICK (Targeted Instruct-evaluation with ChecKlists). TICK leverages the in-context learning abilities of LLM to break down complex instructions into a series of yes/no questions, forming a checklist. The LLM is then used to score this checklist. Initially, the paper demonstrates the advantages of the TICK assessment method through extensive human consistency experiments. Subsequently, the effectiveness of the TICK method is validated through experiments involving self-refinement, Best-of-N selection, and assistance with human annotations.

### Strengths
1. TICK enhances the transparency and interpretability of the evaluation process by breaking down the assessment task into a series of specific YES/NO questions. This fine-grained evaluation approach helps to more accurately identify the strengths and weaknesses in the model's output.

2. This paper conducts extensive automated and manual consistency experiments to quantify and demonstrate the advantages of the TICK evaluation method.

### Weaknesses
1. The core of the proposed method in this paper lies in using in-context learning to break down instructions into a checklist for self-validation and refinement, as well as for best-of-N selection. However, employing decomposed checklists for instruction evaluation ,validation and refinement is not new, as seen in work like FollowBench, InfoBench, and Self-Contrast. The fundamental differences and substantive contributions of this work compared to existing approaches, particularly in terms of evaluation methods and self-improvement strategies, need to be more clearly defined.

2. There is a lack of in-depth discussion regarding the efficiency of the proposed evaluation method.

### Questions
1. Although checklists introduce a certain level of structure, they typically only express parallel relationships. When the content to be verified involves more complex logical relationships, such as selective, chain relationships, or their combinations (for example, tasks in ComplexBench), how can the effectiveness of checklists be ensured?

2. A notable feature of instruction-following tasks is that verification points are directly reflected in the instructions (such as text style, word count limits, etc.), making it relatively easy to break down the task into different verification points and generate checklists. However, for a wider range of task types, especially in fields involving symbolic reasoning like mathematics and programming, how can the application methods and advantages of checklists be demonstrated?

3. For models with different capability levels, particularly some weaker or smaller-scale language models (LLMs), how do they perform in terms of decomposing checklists and accurately scoring?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper explores developing an automated evaluation benchmark to assess the instruction-following ability of large language models. Their study is based on the idea that asking LLMs to evaluate response qualities with a set of detailed requirements provides more reliable assessments than asking LLMs to provide a holistic evaluation directly, as proposed by InfoBench. The major finding of this paper is that LLMs can also prepare the decomposed questions (i.e., the checklist) for arbitrary user prompts, scaling up this framework to the next level of automation. Also, they find that the LLM-generated checklist could further help LLMs to provide self-refined responses.

### Strengths
1. This paper removes the major constraint of manually constructing checklists of prior works, significantly improving the scalability of automated instruction-following benchmarks.
2. It is interesting that the checklist can help LLMs refine their initial responses.
3. The paper is well-written and well-organized.

### Weaknesses
1. The metrics to evaluate the similarities between the human-crafted and LLM-generated checklists can be improved. In particular, those lexical-matching metrics (i.e., BLEU and ROUGE) should be replaced with more semantic ones. For example, [1] evaluates the quality of LLM-generated rubrics versus to human-crafted ones with BERTScore. Further reporting the percentage of recalled human-crafted check items and the percentage of precise LLM-generated check items will be better. 

2. This paper fails to discourse the details of human study. In this paper, many experiments are conducted with human annotators. The authors should discuss some basic information about the annotations, such as the statistics of their demographic information, the training procedures for the annotators, and the internal agreement among the annotators.

### Questions
Please see the suggestions in Weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3
