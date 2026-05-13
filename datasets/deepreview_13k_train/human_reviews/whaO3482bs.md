# ChroKnowledge: Unveiling Chronological Knowledge of Language Models in Multiple Domains

- Decision: Accept
- Scores: 6, 6, 6, 6

## Abstract
Large language models (LLMs) have brought significant changes to many aspects of our lives.
However, assessing and ensuring their chronological knowledge remains challenging.
Existing approaches fall short in addressing the \rebuttal{temporal adaptability} of knowledge, often relying on a \rebuttal{fixed} time\rebuttal{-point view}. 
To overcome this, we introduce \textsc{\textbf{ChroKnowBench}}, a benchmark dataset designed to evaluate chronologically accumulated knowledge across three key aspects: multiple domains, time dependency, temporal state.
Our benchmark distinguishes between knowledge that evolves (e.g., \rebuttal{personal history,} scientific discoveries, amended laws) and knowledge that remain constant (e.g., mathematical truths, commonsense facts). 
Building on this benchmark, we present \textbf{\textsc{ChroKnowledge}} (Chronological Categorization of Knowledge), a novel sampling-based framework for evaluating LLMs' non-parametric chronological knowledge.
Our evaluation led to the following observations: 
(1) The ability of eliciting temporal knowledge varies depending on the data format that model was trained on.
(2) LLMs partially recall knowledge or show a cut-off at temporal boundaries rather than recalling all aspects of knowledge correctly.
Thus, we apply our \textsc{ChroKnowPrompt}, an in-depth prompting to elicit chronological knowledge by traversing step-by-step through the surrounding time spans.
We observe that it successfully \rebuttal{recalls objects across both} open-source \rebuttal{and} proprietary LLMs, \rebuttal{demonstrating versatility, though it faces challenges with dynamic datasets and unstructured formats

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces CHROKNOWBENCH, a benchmark used to evaluate chronological knowledge in LLMs by distinguishing between evolving and static information. The authors also introduce a sampling-based prompting technique to improve LLMs’ recall of time-dependent knowledge across multiple domains. Their approach enables effective temporal non-parametric knowledge updates, even in proprietary models, showing some improvement in biomedical and general knowledge accuracy.

### Strengths
- The paper is very well written, and most of the claims are well-motivated and justified. 
- The benchmark covers various domains and temporal knowledge dimensions. 
- The authors transform the problem into both open generation and MCQ tasks.

### Weaknesses
W1: The overall results appear incomplete across the dataset's various dimensions. A table summarizing average results for each benchmark dimension—Domain, Format, Temporal State, and Time Dependency—would help clarify performance. Currently, it’s unclear whether the performance limitations stem from temporal aspects or the models' domain-specific capabilities.

W2: The proposed prompting method does not clearly demonstrate its effectiveness. Section 5.1 shows stable performance in the biomedical domain, while Section 7.1 suggests the prompting method mainly improves results for biomedical questions, which were not influenced by dynamic changes. How do the authors justify these outcomes as evidence of the prompting method’s efficiency?

W3: In Line 313, the authors state that "GPT-4 performs best in generation tasks." Do they provide any rationale for this observation?

W4: To strengthen the analysis, the paper would benefit from more detailed error analysis and examples. In which cases does the model fail to generate correct answers, and are there discernible patterns in these errors?

### Questions
Q1: What is the evaluation score for the "Generation" experiments in Figures 2 and 3? How do you extract the answer from the model output? Is it an exact match?

Q2: You mention that you use the original MMLU prompting strategy (Hendrycks 2021). Is this with the 5-shot setting or with the zero-shot and Chain-of-Thought generation?

Q3: Are the results for the "Time Invariant" data being reported?

### Soundness
3

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
3

### Summary
This paper investigates how well large language models recall chronological knowledge. The paper makes several contributions. First, the authors describe a new benchmark dataset covering different domains (e.g., biomedical, legal) and different types of time dependency and temporal state. Then, the authors benchmark several LLMs (both open-sourced and closed-sourced) and show that LLMs have varied abilities to elicit temporal knowledge. Finally, the authors present a prompting method to elicit chronological knowledge.

### Strengths
* The studied problem is important and interesting.
* The authors build a benchmark for evaluating LLM and propose a method for recalling/editing knowledge?

### Weaknesses
 * The authors evaluate whether LLM can track `object changes`. This problem formulation may not capture the `accumulative nature of knowledge` as discussed in the paper. For example, one drug may have multiple side effects, each of which was identified at different times. I am unsure how the proposed benchmark and evaluation strategy addresses this accumulative nature. For example, a model that always generates the old knowledge will be considered `correct` based on the definition in Table 1.
* The result sections are hard to follow: it is very difficult to understand how their results support these statements in Section 5 (Figures 2, 3).
* The proposed prompting strategy seems to be disconnected from the benchmark sections. For example, the authors show that the proposed prompting strategy improves in the biomedical domain, whereas results in Section 5 and Figure 3 show little variability across times. Any intuitive explanations of why?

### Questions
* The ChroKnowBench considers only changes on `object` while keeping `subject` and `relation` unchanged. How does it capture the change of `relation` between the `subject` and `object`? For example, `Zidane` was a `player` at `Real Madrid` in 2001, then became `coach` in 2010.
* Figures 2 and 3: It is hard to interpret these results; suggest using the same y-axis range
* Section 5.1: `In dynamic datasets, models show reduced knowledge in multiple-choice question answering (MCQA) settings, highlighting the impact of formatting and prompting on temporal abilities.` What does this mean?
* Section 5.1: `models fail to track recent updates between 2022 and 2023`; `Static datasets remain consistent, reflecting the stable nature of scientific knowledge` suggest clarifying what these statements mean

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes a new aspect of evaluating Large Language Models, which focuses on chronologically accumulated knowledge. The authors set up a new benchmark, ChroKnowBench, for chronological knowledge evaluation across three dimensions: time dependency, domain difference, and temporal state. They also put forward a novel evaluation framework called ChroKnowledge, and a novel prompting technique called ChroKnowPrompt, which aims to improve the model’s performance using temporal neighboring data.

### Strengths
The paper targets a novel field, which studies how language models learn and adapt to knowledge in different time spans. Previously, not many researchers formalized and paid attention to the question. The authors did well in defining the key aspects of testing and evaluating chronological knowledge in large language models, including putting forward a comprehensive dataset and benchmark that covers a variety of time ranges and domains, as well as developing novel prompting techniques. They also conducted fairly comprehensive experiments to demonstrate their claims.

### Weaknesses
1. Results in section 7 does not necessarily support the soundness and validity of the ChroKnowPrompt framework, but instead hints at the deficiency in the ChroKnowledge dataset. There is another possible explanation to the large amount of performance increase in the biomedical section of the dataset: domain-specific data are more static / less dynamic than general data, and your method on distinguishing dynamic and static knowledge needs to be updated to a more fine-grained extent. For example, over the span of 10 years, some data might changed 5 to 6 times, but there could be other data that only changed once. I currently don’t see that taken into account. The improvement from the “dynamic” portion of your results could be over-exaggerated.
2. The figures need more work. For figure 2 and 3, I understand that the authors are trying to demonstrate the relationship between time and model performance, but the graph needs some extra work on clarity to deliver the message. Figure 4 and 5 in section 6 also needs more work. The most useful explanations for Figure 4 are in the appendix, making the figure a little confusing. Figure 5 needs more clear textual hints on the overall framework of ChroKnowPrompt. The figure itself is not illustrative enough for the entire framework.

### Questions
1.	Why would you include Legal data? The rest of the data are of the same type in format and structure, but only legal is unstructured and of a different type.
2.	For your results in section 4, is it possible that the quality of your collected data in different time points is a more influential factor? 
3.	Suggestions for the weaknesses mentioned above: 
a.	Do more fine-grained classification of the “static” and “dynamic” data.
b.	Update Figure 2 and 3 for more clarity.
c.	Move some information from the appendix to section 7, including the extra descriptions for ChronoPrompt and some extra summaries for the algorithm.

### Soundness
3

### Presentation
3

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
This paper introduces CHROKNOWBENCH, a benchmark dataset designed to evaluate chronologically accumulated knowledge across three key aspects: multiple domains, time dependency, and temporal state. Besides, the authors develop CHROKNOWPROMPT, an in-depth prompting to elicit chronological knowledge by traversing step-by-step through the surrounding time spans. The motivation behind this work is clear, however, the paper majorly lacks in the quality of the experiments and its setup.

### Strengths
This work addresses the sensitivity of LLM to time dependencies and constructs dynamic and static datasets for evaluation.
This paper introduces an iterative approach to integrate knowledge across different temporal spans, enabling dynamic knowledge updates.

### Weaknesses
The paper mentions evaluating knowledge across multiple domains; however, it only introduces knowledge from the medical and legal domains, where changes of knowledge along the timeline are relatively subtle.
This paper aims to explore the ability of LLMs to capture temporal dependencies within knowledge. However, the constructed benchmark dataset and evaluation methodology do not effectively demonstrate this capability of the models in an intuitive manner.
Although the paper divides knowledge into dynamic and static datasets, the knowledge within these datasets may have already been learned by LLMs. As a result, the benchmark evaluation results are likely to primarily reflect the memory capacity of the LLM regarding this knowledge, rather than its ability to handle time dependencies.
For the dynamic dataset, this paper essentially transforms knowledge into a temporal knowledge graph (TKG). However, there are established benchmarks in TKGs. The authors should consider providing comparisons with these benchmarks and clarifying the specific improvements made.

### Questions
See weakness.

### Soundness
3

### Presentation
4

### Contribution
3
