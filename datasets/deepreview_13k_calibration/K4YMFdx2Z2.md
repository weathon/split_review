# Unsolvable Problem Detection: Evaluating Trustworthiness of Large Multimodal Models

- Decision: Reject
- Avg Score: 5.67
- Scores: 6, 5, 6

## Abstract
This paper introduces a novel and well-defined challenge for Large Multimodal Models (LMMs), termed Unsolvable Problem Detection (UPD). UPD examines the LMM's ability to withhold answers when faced with unsolvable problems. UPD encompasses three problems: Absent Answer Detection (AAD), Incompatible Answer Set Detection (IASD), and Incompatible Visual Question Detection (IVQD), covering unsolvable cases like answer-lacking or incompatible choices and image-question mismatches. In this paper, we introduce the MM-UPD Bench, a benchmark for assessing performance across various ability dimensions. Our experiments reveal that even most LMMs, which demonstrate adequate performance on existing benchmarks, struggle significantly with MM-UPD, underscoring a novel aspect of trustworthiness that current benchmarks have overlooked. To deepen the understanding of the UPD, we explore various solutions, including chain of thought, self-reflection, and instruction tuning, and demonstrate each approach's efficacy and limitations. We hope our insights, together with future efforts within the proposed UPD settings, will enhance the broader understanding and development of more practical and reliable LMMs.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces Unsolvable Problem Detection (UPD) as a framework to evaluate Large Multimodal Models (LMMs) on their capacity to identify and manage unsolvable problems. This framework consists of three main challenges: Absent Answer Detection (AAD), Incompatible Answer Set Detection (IASD), and Incompatible Visual Question Detection (IVQD), to address scenarios involving insufficient, mismatched, or incompatible information. To support evaluation, the authors present the MM-UPD Bench, a benchmark consisting of 2k questions derived as a subset of MMBench, to measure LMM performance in these areas. The paper evaluates several LMMs using the MM-UPD Bench and provides an analysis based on open-source versus closed-source models, as well as detailed question types.

The experimental results reveal that even state-of-the-art LMMs, which perform well on conventional benchmarks, encounter difficulties when assessed with the MM-UPD Bench. Additionally, generic existing approaches were tested to address UPD but proved ineffective, which underscores the challenge of UPD.

### Strengths
1. The paper is well-written and easy to follow. The definitions of the problems and evaluation criteria are clearly presented, and the visualizations of examples and results enhance the readers' understanding.
2. The paper conducts comprehensive and detailed experiments to analyze where and how LMMs struggle with UPD. It further evaluates the effectiveness of existing methods in addressing UPD, which offers valuable insights for future researchers aiming to tackle these challenges.

### Weaknesses
 1. The paper's strategy for filtering image-agnostic questions (line 207) to ensure that problems truly rely on the image modality seems problematic. Specifically, the method filters questions from MMBench that can be answered correctly using text-only GPT-4 and manually reviews the remaining questions. This approach risks excluding genuinely image-dependent questions that GPT-4 might answer correctly by chance, or due to biases in its training data, rather than true understanding of the image. As shown in Table 1 IVQD, there is a possibility that GPT based model attempts to answer questions that require image information but lack relevant image input. This could lead to false exclusions, and introduce bias into the dataset and impact the evaluation of GPT-based models.
2. Following the previous point, the paper states in line 996 that 13% of the original questions are removed as image-agnostic. This suggests that the initial GPT-based filtering only marginally reduces manual effort. Given this, why not manually filter all image-agnostic questions to ensure greater accuracy and consistency? The relatively small reduction in manual effort raises concerns about the efficiency of the GPT-4 filtering step and whether the potential for introducing bias outweighs its benefits.
3. The use of Dual Accuracy as the primary metric (line 252) may not fully capture the intended evaluation properties of the benchmark. Dual Accuracy is defined as *the accuracy on standard-UPD pairs, where success is counted only if the model answers both the standard and UPD questions correctly.* However, as illustrated in Figure 2's examples, a model might correctly refuse to answer absurd questions even if it is not capable of answering the standard version. This coupling of general VQA ability and the capacity to reject unanswerable questions could skew comparisons across models. To better assess the models' capability in detecting unsolvable questions, it may be more informative to compare success rates on questions where the model correctly answers the standard version. This ensures both text and image are understood, and evaluates if the changes that make the question becomes unanswerable are detected. (Mathematically, it's similar to divide Dual Accuracy by Standard Accuracy). This would provide a more isolated measure of the model's ability to identify unsolvable problems, independent of its general VQA performance.
4. The distribution of question types appears skewed and inconsistent across AAD, IASD, and IVQD, as shown in Table B (line 1042). For instance, in AAD and IASD, the three most common question types (#2, #17, and #3) account for 30% of the questions, whereas in IVQD, the most common types (#2, #7, and #9) account for 44%. Could this affect the analysis of UPD performance? Additionally, six question types have no representation in IVQD. While it is understandable that certain types need to be removed to evaluate IVQD, if the distribution matters (as stated in the previous point), could it be more beneficial to modify these questions and make them less general rather than remove them? This inconsistency in question type distribution across the different UPD challenges could lead to skewed performance evaluations and limit the generalizability of the findings.
5. Table 4 reports performance following UPD-specific training. The paper notes that such training may degrade performance on general tasks. However, the performance under the *Orig* condition remains the same as indicated in Table 1. To provide a complete analysis, it would be helpful to re-evaluate the *Orig* condition after fine-tuning to observe any potential impacts. This would help determine if the fine-tuning process has any unintended consequences on the model's original capabilities, even when not directly evaluated on the UPD tasks.

### Questions
1. Please refer to the concerns raised in Weaknesses 2 and 4.

2. In addition to the three challenges defined in the paper, have the author considered an additional challenge of *incompatible question detection*? This would involve scenarios where the image and answer set align, but the question itself is incompatible with both the image and the answer. For example, replacing the original question in an image-question-answer set with an unrelated one. This condition appears aligned with how the proposed challenges are structured. Would it be necessary to incorporate this condition, or is this concept already encompassed by the current challenges defined?

### Soundness
3

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
4

### Summary
This paper addresses a challenge in multimodal large language models (MLLMs): Unsolvable Problem Detection (UPD). The authors conceptualize UPD through three distinct tasks: Absent Answer Detection (AAD), Incompatible Answer Set Detection (IASD), and Incompatible Visual Question Detection (IVQD). To systematically evaluate MLLMs’ capabilities in addressing UPD, they introduce a benchmark, MM-UPD (derived from MMBench), and assess both open-source and closed-source models on this benchmark. The evaluation reveals that current models exhibit substantial difficulty in handling UPD tasks. To mitigate these limitations, the authors propose a series of enhancement strategies, including chain-of-thought prompting, self-reflection, and instruction tuning, aimed at improving MLLMs' effectiveness in detecting unsolvable problems.

### Strengths
1. The authors investigate the important issue of Unsolvable Problem Detection (UPD) and provide an in-depth analysis of this challenge within the context of multimodal large language models (MLLMs). 

2. To evaluate MLLMs' effectiveness in handling UPD, they develop a benchmark that incorporates diverse evaluation settings, examining various scenarios and testing a range of both open-source and closed-source MLLMs. The findings, particularly those outlined in Section 5.2, offer valuable insights into current MLLMs limitations.

3. To address the UPD challenge, the authors propose several practical strategies, including chain-of-thought prompting (CoT), self-reflection, and instruction tuning, which show promise in mitigating the difficulties MLLMs face in detecting unsolvable problems.

### Weaknesses
1. **Narrow Definition of Unresolvable Problem Detection**: The proposed definition of Unresolvable Problem Detection (UPD) is limited, focusing solely on multiple-choice problems. This approach overlooks other open-ended multimodal question-answering scenarios, which are prevalent and significant in real-world applications. The restriction to multiple-choice questions limits the assessment of a model's ability to identify unsolvable problems in more complex, free-form contexts. For instance, a model might correctly identify an unsolvable multiple-choice question by eliminating options, without truly understanding the underlying issue. Expanding the scope to include open-ended scenarios would provide a more comprehensive understanding of UPD, reflecting real-world challenges where answers are not constrained by predefined options.

2. **Anticipated Poor Performance of Existing MLLMs**: The observed poor performance of existing multimodal large language models (MLLMs) in handling UPD is not unexpected. This is likely due to the absence of specific instruction-tuning datasets during the visual instruction fine-tuning stage. While the proposed solutions, such as chain-of-thought prompting, self-reflection, and instruction tuning, are steps in the right direction, they appear somewhat straightforward. The use of chain-of-thought, while helpful, is a well-established technique and its application here doesn't represent a significant methodological leap. Similarly, self-reflection and instruction tuning are common practices, and their implementation in this context lacks novel technical depth. More sophisticated and innovative approaches are needed to effectively address the complexities of UPD, such as incorporating adversarial training or more advanced reasoning mechanisms.

3. **Limited Benchmark Diversity**: The benchmark used for evaluating MLLMs' capability in handling UPD lacks diversity, relying solely on MMBench, which comprises 2,095 questions. This limited dataset may not provide a comprehensive evaluation. The exclusion of other datasets like MMMU and MathVista, based on their low standard accuracy, may not be a sufficiently robust justification. The argument that low standard accuracy invalidates a dataset for UPD evaluation is not entirely convincing, as these datasets might still offer valuable insights into how models handle unsolvable problems in more challenging scenarios. Incorporating a variety of datasets, including those with lower standard accuracy, would enhance the evaluation's robustness and offer a more thorough assessment of MLLMs' performance in UPD tasks, potentially revealing different failure modes and limitations.

### Questions
1. **Manual Dataset Curation Standards**: The benchmark dataset involves certain manual efforts, such as eliminating image-agnostic questions and removing ambiguous questions. Could the authors clarify the criteria used for these removals? What standards were applied to ensure consistency and objectivity in these decisions?

2. **Alternative Solutions for UPD**: Are there potentially more advanced or effective solutions for addressing the challenges of Unsolvable Problem Detection (UPD) beyond those proposed? If so, what approaches could further improve MLLMs' performance in handling UPD scenarios?

3. The error analyses in section 6.2 is insightful, could you do the same analyses for open-source MLLMs?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper introduces a new challenge for LMMs, termed Unsolvable Problem Detection (UPD) which examines the LMM’s ability to withhold answers when faced with unsolvable problems. Then, a benchmark is introduced to assess the performance across various ability dimensions and some solutions are explored to understand UPD. It can enhance the development of more practical and reliable LMMs.

### Strengths
It first introduces a new challenge for LMMs, termed Unsolvable Problem Detection (UPD).
It constructs a benchmark to assess the performance across various ability dimensions.
It evaluates state-of-the-art LMMs on the UPD problem with the benchmark.

### Weaknesses
The dataset in the paper is constructed based on existing datasets, and there is no comparative analysis of data size, distribution, and comprehensiveness, etc.

### Questions
What is the difference between the exsiting definition of unsolvable problems and the definition in this paper?
What is the difference in the design of Table 3 and Table 4, and why not merge them？

### Soundness
2

### Presentation
2

### Contribution
2
