# Knowledge Manipulation in Language Models

- Decision: Accept
- Scores: 6, 6, 8, 6

## Abstract
Language models can store vast factual knowledge, yet their ability to flexibly use this knowledge for downstream tasks (e.g., via instruction finetuning) remains questionable. This paper investigates four fundamental knowledge manipulation tasks: \textbf{retrieval} (e.g., "What is person A's attribute X?"), \textbf{classification} (e.g., "Is A's attribute X even or odd?"), \textbf{comparison} (e.g., "Is A greater than B in attribute X?"), and \textbf{inverse search} (e.g., "Which person's attribute X equals T?").

We show that language models excel in knowledge retrieval but struggle even in the simplest classification or comparison tasks unless Chain of Thoughts (CoTs) are employed during both training and inference. Moreover, their performance in inverse knowledge search is virtually 0\%, regardless of the prompts.
Our primary contribution is a \emph{controlled, synthetic experiment} that confirms these weaknesses are \emph{inherent} to language models: they cannot efficiently manipulate knowledge from pre-training data, even when such knowledge is perfectly stored in the models, despite adequate training and sufficient model size. Our findings also apply to modern pretrained language models such as GPT-4, thus giving rise to many Turing tests to distinguish Humans from contemporary AIs.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper investigates the fundamental knowledge manipulation abilities of language models, particularly in logical reasoning tasks that require combining multiple pieces of knowledge rather than finding direct answers in training data. Using a controlled biography dataset, the study examines four key reasoning abilities—retrieval, classification, comparison, and inverse search—that broadly cover real-world scenarios. Results reveal that while models perform well in basic knowledge retrieval, they struggle with tasks requiring partial extraction or retrieving multiple attributes. Classification and comparison tasks, especially those involving attribute comparisons, are challenging without the use of Chain of Thought (CoT) techniques. Additionally, the models are particularly weak in inverse search tasks, such as identifying a person based on attribute values, underscoring the limitations of current language models in more complex knowledge manipulation.

### Strengths
1. The experiments are well-controlled, focusing on minimizing extraneous variables, which allows the study to provide numerous insights (Results 1-8). Unlike most research on LLM knowledge, which often lacks such control and tends to use pre-trained LLMs, this study stands out as an important contribution.

### Weaknesses
1. The paper includes four knowledge manipulation tasks, but the reason for putting all four together in this single paper is not entirely clear. While the performance of each individual task is shown and discussed, it would be helpful if the authors discussed the overall implications of these results, i.e., what can be concluded when combining these findings.
2. While performance for each manipulation task is discussed, there is no analysis on why the results are as they are. For instance, why can the model perform full retrieval but perform worse in partial retrieval? Why does the performance improve when CoT is used? Although it may be challenging to fully explain these observations, the paper would be more insightful if it included some hypotheses and experiments to verify these hypotheses.
3. The paper explores limited variations in querying knowledge for LLMs, relying solely on the question forms + fine-tuning. But, other query methods, such as cloze-style prompting (with next-word prediction, which is closer to the pretraining objective), or zero-shot and few-shot prompting, could also be explored. It would be beneficial to see whether these alternatives could improve performance on manipulation tasks. This should lead to more robust conclusions about the challenges language models face with knowledge manipulation tasks. If one wants to claim that something does not work, as many solutions as possible need to be tested.

### Questions
1. Regarding Weakness 1, what are the overall implications of the results? Could you clarify the broader conclusions/impacts that can be drawn from the current results?
2. For Weakness 2, are there any possible experiments that could provide further insights, or is this beyond the scope of the current study?
3. For Weakness 3, would conducting additional experiments with varied settings yield valuable insights, or are the current experiments sufficient to reach definitive conclusions?

### Soundness
2

### Presentation
2

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
This paper examines the knowledge manipulation capabilities of LLMs, such as knowledge retrieval, classification, comparison, as well as inverse search. Through controlled experiments on models like GPT2 and Mistral, the authors reveal substantial limitations in these models' ability to perform even basic manipulations, such as identifying a person’s birth year, unless that information is directly present in the model's training data or using advanced prompting methods like CoT.

### Strengths
1. The flaws of LLMs highlighted in this work are fundamental and significant. The testbed and methodology presented here could serve as a valuable benchmark for future generations of LLMs, potentially marking a clear boundary between AI systems that possess system II reasoning capabilities and those that do not.

2. The evaluation is reasonably thorough, including various types of knowledge manipulation tasks and examining both open and closed-source LLMs.

### Weaknesses
1. It's not a new finding that LLMs struggle to retrieve and apply stored knowledge effectively for solving reasoning tasks [1, 2]. However, the author doesn't cite these existing work.

2. The author reports a new finding that LLMs trained with CoT are not better at knowledge manipulation. However, examining the training samples (L360-362) reveals that the CoT format used is incomplete as it includes only intermediate answers without the full reasoning chain, which may have hindered the effect.

3. The author trains the models on synthetic biography data. It's well motivated as it allows the authors to assess knowledge manipulation without data contamination risks. However, it’s uncertain whether fine-tuning on this synthetic data might lead to catastrophic forgetting in the models, affecting their understanding of concepts like "even" or their general manipulation capabilities.

### Questions
1. I think your work is also related to those work on assessing the self-consistency of LLMs.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
Pre-trained Language Models (PLMs) are widely recognized for encoding extensive knowledge during pre-training. However, their effective utilization of this knowledge remains uncertain. This paper examines knowledge manipulation capabilities across four tasks: retrieval, classification, comparison, and reverse search.

To isolate these factors, the authors emphasize the need for a controlled setting where the model’s responses reflect actual knowledge manipulation rather than simple recall of training data. Given that recent Large Language Models (LLMs) are trained on expansive internet datasets, achieving such control is challenging. Consequently, the authors re-train several models (GPT-2, LLaMA, and Mistral) on synthetic datasets, including biographical datasets (bioS, bioR) and Q&A datasets for either pretraining or fine-tuning.

Results reveal that while LLMs perform well in knowledge retrieval, they struggle with partial knowledge extraction (e.g., identifying only the birth month instead of the full birth date), knowledge comparison (e.g., determining if a birth month is even), and reverse search (e.g., identifying a person by their birth date). The authors further observe that performance improves significantly with Chain of Thought (CoT) prompting, suggesting that LLMs benefit from generating intermediate reasoning steps (e.g., “He was born in December, which is the 12th month and therefore even”).

Finally, the authors extend their study to larger production models, such as GPT-4o and LLaMA-3-405B, revealing similar limitations, underscoring this as an area for improvement in future model iterations.

### Strengths
- The paper is thorough and self-contained, re-explaining key concepts, which enhances readability and makes the study easy to follow.
- The writing is clear, and methodological points are frequently illustrated with examples, adding clarity to the analysis.
- The use of synthetic datasets to examine LLMs within a controlled environment is a valuable and relevant methodological choice. 
- By testing multiple models, including recent versions like GPT-4o, the paper strengthens the generalizability of its findings.
- Overall, the paper addresses a crucial issue in model capabilities that warrants broader attention.

### Weaknesses
Figures 3, 4, and 6 are challenging to interpret, particularly due to the color coding and the distinctions between various lines (e.g., bioS multi5 + permute vs. bioS multi5 + permute + fullname) and the variations in behavior among them. Reducing the number of results displayed and focusing on a deeper analysis of selected findings could enhance clarity. The current presentation makes it difficult to discern the key trends and the relative performance of different model configurations. Furthermore, the specific reasons for the performance variations between the different training setups (e.g., bioS vs. bioR) are not sufficiently explored, leaving the reader to speculate on the underlying causes. The analysis would benefit from a more in-depth discussion of these differences, possibly including ablation studies or more granular performance breakdowns.

### Questions
1) Could the reliance on Chain of Thought prompting be due to the fact that this approach effectively enables the model to “think” more deeply, performing additional steps or calculations that might not otherwise be possible? 
2) What methods would you consider to address this limitation of LLMs?

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper investigates the ability of large language models (LLMs) to manipulate stored factual knowledge through various tasks such as retrieval, classification, comparison, and inverse search. The authors argue that while LLMs like GPT-4 excel in knowledge retrieval, they struggle with classification and comparison tasks unless trained and tested with Chain of Thought (CoT) reasoning. Inverse knowledge search is highlighted as a critical limitation, with performance remaining near-zero across different datasets, architectures, and model sizes. The paper utilizes synthetic biographical datasets to conduct controlled experiments, confirming these weakness of LLMs and revealing the need for enhanced training strategies to improve LLMs’ knowledge manipulation abilities.

### Strengths
* This paper focus on knowledge manipulation addresses a vital challenge in NLP, with implications for retrieval-based tasks.
* The paper Introduce inverse knowledge search as an evaluation criterion adds a new dimension to LLM evaluation.
* The synthetic biography datasets and the four well-designed tasks are valuable assets for future researchers.
* The paper is well-organized and presented clearly.
* The paper offers detailed analyses and experimental results, contributing meaningfully to understanding LLM limitations.

### Weaknesses
Recent studies have extensively explored the challenges of LLMs in reasoning and manipulating knowledge from pre-training data. It would strengthen the paper if the authors discussed potential solutions based on their findings.

### Questions
None

### Soundness
3

### Presentation
4

### Contribution
3
