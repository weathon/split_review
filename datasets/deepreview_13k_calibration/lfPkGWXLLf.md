# ForecastBench: A Dynamic Benchmark of AI Forecasting Capabilities

- Decision: Accept
- Avg Score: 6.67
- Scores: 5, 8, 8, 8, 6, 5

## Abstract
Forecasts of future events are essential inputs into informed decision-making. Machine learning (ML) systems have the potential to deliver forecasts at scale, but there is no framework for evaluating the accuracy of ML systems on a standardized set of forecasting questions. To address this gap, we introduce \textbf{\BenchmarkName}: a dynamic benchmark that evaluates the accuracy of ML systems on an automatically generated and regularly updated set of 1,000 forecasting questions. To avoid any possibility of data leakage, \BenchmarkName{} is comprised solely of questions about future events that have no known answer at the time of submission. We quantify the capabilities of current ML systems by collecting forecasts from expert (human) forecasters, the general public, and LLMs on a random subset of questions from the benchmark ($N=200$). While LLMs have achieved super-human performance on many benchmarks, they perform less well here: expert forecasters outperform the top-performing LLM (p-value $<0.01$).
We display system and human scores in a public leaderboard at \href{https://\BenchmarkURL}{\BenchmarkURL}.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
A dynamic dataset of forecasting qs about the future is aggregated and proposed as a benchmark for LLMs. Performance of a variety of LLMs is compared with human.

### Strengths
Interesting and useful benchmark, whose position in the landscape is clearly described. 
LLM evals are extensive.

### Weaknesses
 This is an interesting and useful dataset, but reads like a tech report or class assignment; the level of technical detail is superficial, and there is little to no exploration of what we learn about LLMs from this.

Detailed comments by section:

abs/intro/relwork
 - "necessary task" seems a bit overstated; if you want to make this claim it would be worth stating how exactly the referenced papers support that claim
- reasonably clear intro/positioning and motivation overall; a bit repetitive but lacking technical details (e.g. how are predictions elicited from humans? what kinds of mistakes do LLMs make?); it would be nice to mention that briefly 
- relwork: what is "statistically imprecise"?  - good lmeval section
preliminaries
 - unclear details about the nature of forecasts in the dataset; are they open-ended questions / natural language? are the possible outcomes enumerated in advance? is there a char limit? etc.  - unclear explanation of the Brier score; the Forecasting paragraph says forecasters "may" assign probabilities to possible outcomes; if they don't how do you assign f? How do you assign a 0/1 outcome to questions like "who will be the next US president?" - using the character f is confusing notation (f is almost universally a function) but not a huge deal - "strictly proper" and why we would care about that / why that incentivises truthfulness is not explained at all.  - 3 different methods of prompting/rag are not explained at all - "prompting" for the humans that are compared to the LLMS is not explained at all

sec 3 
 - does not seem necessary to have a flowchart here to say that everything goes to the question bank, and it takes a lot of space. It might be helpful to have one if it showed what are the different platforms and datasets, any pre-preprocessing that needs to be done, etc., but this is covered fine in Table 1.
 - Similarly for Fig 3; neither of these is contributing substantively to the paper; they could be moved to appendix to make space for more technical details.
 - it seems like the details in 3.2 contradict the "preliminaries" section
 
sec 5
- given the small dataset sizes here it would be interesting to explore exactly what LLMs do and don't get right

### Questions
The level of technical details and insight are the biggest things that would make me change my score.

Detailed comments by section:

abs/intro/relwork
 - "necessary task" seems a bit overstated; if you want to make this claim it would be worth stating how exactly the referenced papers support that claim
- reasonably clear intro/positioning and motivation overall; a bit repetitive but lacking technical details (e.g. how are predictions elicited from humans? what kinds of mistakes do LLMs make?); it would be nice to mention that briefly 
- relwork: what is "statistically imprecise"?  - good lmeval section
preliminaries
 - unclear details about the nature of forecasts in the dataset; are they open-ended questions / natural language? are the possible outcomes enumerated in advance? is there a char limit? etc.  - unclear explanation of the Brier score; the Forecasting paragraph says forecasters "may" assign probabilities to possible outcomes; if they don't how do you assign f? How do you assign a 0/1 outcome to questions like "who will be the next US president?" - using the character f is confusing notation (f is almost universally a function) but not a huge deal - "strictly proper" and why we would care about that / why that incentivises truthfulness is not explained at all.  - 3 different methods of prompting/rag are not explained at all - "prompting" for the humans that are compared to the LLMS is not explained at all

sec 3 
 - does not seem necessary to have a flowchart here to say that everything goes to the question bank, and it takes a lot of space. It might be helpful to have one if it showed what are the different platforms and datasets, any pre-preprocessing that needs to be done, etc., but this is covered fine in Table 1. 
 - Similarly for Fig 3; neither of these is contributing substantively to the paper; they could be moved to appendix to make space for more technical details.
 - it seems like the details in 3.2 contradict the "preliminaries" section
 
sec 5
- given the small dataset sizes here it would be interesting to explore exactly what LLMs do and don't get right

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper presents a sophisticated and automated benchmark for evaluating forecasts that improves over prior benchmarks in that it will not become stale and does not rely on assumptions about models (e.g., knowledge cutoffs). Using the benchmark, they find that interestingly, SOTA models are still short of expert forecasters.

### Strengths
- very well written--well motivated, structured, and polished overall
- addresses a key problem in prior benchmarks: benchmark staleness, which is obviously very important for the problem of forecasting, since the goal is to build/evaluate systems that can predict new events, not post-hoc. their approach is conceptually cleaner (imo) than relying on LLMs' knowledge-cutoffs, etc.
- overall interesting finding that at least in this setting, LLMs still quite lag behind experts, only matching the median of average people 
- the approach to building/generating the question set and the entire pipeline is very thoroughly thought out.

### Weaknesses
 - Table 2 is a bit big / dense and hard to parse. The paper could benefit from using more visual plots to convey the results

### Questions
- Is there anything easy (cheap) we can try to improve the capabilities of these models to forecasting beyond RAG-like things? I guess finetuning open-source models would be ideal but that is probably infeasible.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper introduces ForecastBench, a novel dynamic benchmark designed to evaluate the forecasting capabilities of AI systems, particularly large language models. In contrast to prior static benchmarks, ForecastBench continuously updates with new forecasting questions about future events that have no known answers at the time of submission, thereby eliminating concerns of data leakage or contamination. The study compiles a standardized set of 1000 forecasting questions sourced daily from nine data providers, including prediction markets, forecasting platforms, and real-world time series. To evaluate the accuracy, the authors assess the performance of 17 state-of-the-art LLMs on a subset of these questions, comparing their forecasts to those of expert human forecasters (superforecasters) and the general public, using the Brier score as the primary metric.

### Strengths
- A sophisticated evaluation framework that incorporates multiple forecasting dimensions, including:
    - Selection of questions from high-liquidity market sources,
    - Temporal sampling methodology for question release,
    - Granular analysis of model and human performance across varying time horizons.
    - Comprehensive assessment of instruction-following chat models through six distinct evaluation methodologies (Section 5.1), including zero-shot prompting, scratchpad reasoning prompting, and news-augmented generation.
- Implementation of diverse temporal resolutions for forecasting questions, spanning from week-long to decade-scale predictions, enabling robust evaluation across different time scales.
- Novel incorporation of combination questions for assessing model performance on higher-complexity tasks, revealing significant human performance advantages and highlighting current limitations in model capabilities.
- The development of a daily question-release mechanism featuring 1000 forecasting queries, which:
    - Mitigates potential gaming of the leaderboard system,
    - Generates an expanding dataset of resolved predictions enabling model training and calibration of future forecasting systems.

### Weaknesses
 - The evaluation of unresolved questions relies on comparisons with crowd predictions, potentially complicating future assessments of whether models outperform the crowd baseline.
- The number of expert predictions was limited, with only 39 experts contributing, leading to an average of 8 expert predictions per question. This relatively small sample size may affect the robustness and generalizability of the evaluation results.

### Questions
- Have you investigated the impact of the prompt date on model predictions? Specifically, could questions asked further in advance of the resolution date introduce greater uncertainty in LLM predictions, potentially affecting prediction accuracy?
- How is the quality of questions released for evaluation determined?
- Have you considered evaluating model predictions by examining the logits of the answer tokens? Although this may be more feasible with open-source models, some providers do offer token-level logit outputs. Incorporating logits could provide insights into model calibration and further enhance prediction reliability.

### Soundness
3

### Presentation
4

### Contribution
4

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper proposes a forecasting benchmark for evaluating LLM's forecasting capability. The benchmark is carefully constructed to avoid potential data leakage. The benchmark results indicates with statistical significance that even the SOTA LLMs nowadays cannot beat human experts in this task.

### Strengths
1. The forecasting problem studied in this paper is both very interesting and practical. Forecasts on macroeconomic problems such as presidential election is both complicated and impactful to real-world scenarios. Hence it can serve as a good benchmark for evaluating LLM's capability.
 
2. The benchmark design considers data leakage, which improves the reliability of the benchmark.

3. The benchmark results indicates some areas where LLMs still have inferior performance compared to top human, revealing potential future research directions.

4. Code is provided for better reproducibility.

### Weaknesses
1. It may be worth justifying the adopted method in this benchmark for LLM to make forecasts, since LLM reasoning methods (e.g. RAG, etc.) can have great influence on the final performance

### Questions
1. What if we allow LLMs to access different tools to actively acquire relevant information in a feedback loop? In this way the LLM may construct more context for more accurate answer.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This work presents a benchmark for evaluating how well LLMs predict future events, curating questions about current events and corresponding answers. A set of state-of-the-art LLMs are then prompted to predict the probability of future events. The prediction accuracy is then compared against expert and non-expert human forecasters, ultimately finding that the LLMs generally perform similarly to average forecasters but worse than expert forecasters.

### Strengths
This paper has many strengths:
* Dynamic benchmarks are needed and event forecasting seems like a sensible LLM use to evaluate, likely interesting members of the research community
* This paper seems to describe a mature and already-used system that could elicit some interesting use
* The finding that LLMs can forecast events similarly to average forecasters is interesting, and the fact that experts are still better is a promising sign that this area deserves further attention
* The use of real human experiments is a big strength

### Weaknesses
This paper could be strengthened by addressing the following weaknesses:
1. The main weakness of this work is the limited experiment section. Given the main contribution is the curation of a new dataset and resultant evaluation, it is unsatisfying that the result is only one page of experiments with minimal interpretation. The result is it's unclear if this benchmark is useful beyond this experiment. Relatedly, it's never really shown why it's important for this to be a "dynamic" benchmark, despite this being a key selling point. Avoiding data leakage is indeed important, but it's surprising that this doesn't allow for any dedicated experiment or discussion around how often questions are resolved during the benchmarking. For example, it would be beneficial to see an analysis of how the performance of models changes as the benchmark evolves over time, or a comparison of model performance on static vs dynamic versions of the benchmark. Without such experiments, the claims about the necessity of a dynamic benchmark remain unsubstantiated.
2. The method development is described without many details, especially explanations of design decisions and their impact. Instead, most of Section 3 simply states what was done. It's not clear that future researchers could improve on this work if there's no explanation of what alternatives exist and why they are insufficient. This isn't inherently a major concern, but the main contribution of the work appears to be the dataset development, so defending these decisions would help the reader gain confidence in the resulting data and findings. For instance, the paper lacks a discussion of alternative methods for question selection, or how the choice of sources impacts the diversity and difficulty of the questions. A more thorough discussion of these design choices would strengthen the paper.
3. The paper is hard to follow, with many details sprinkled throughout various sections and the reader is left to hunt them down. It could help to include more details on the forecasting problem and summaries of exactly what's provided in Section 3.

### Questions
Answers to the following questions would help me better calibrate my review:
1. Is there intuition for why the LLMs would perform better on average for the questions sampled for humans? It seems like there's a consistent drop in the Brier Score.
2. How do LLM and human questions differ? Could these differences explain any differences in accuracy? Maybe this relates to L265---what's different about their information-availability?
3. What is "News with freeze values"?

### Soundness
3

### Presentation
1

### Contribution
3

---

## Human Reviewer 6

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper introduces ForecastBench, a dynamic benchmark for evaluating the forecasting capabilities of both human and machine learning systems. This benchmark continuously updates with new forecasting questions, addressing the limitations of static benchmarks. The paper includes comprehensive experiments comparing the performance of various LLMs and human forecasters.

### Strengths
Interesting paper and relevant problem statement. Human annotated data generation in a streamlined manner is a challenge and the methodology proposed in the work can be used for updating the evaluation set for LLMs with time.
The work also discusses the evaluation on complex questions comprising of simple questions.

Paper is well-written.

### Weaknesses
Overall concerns-
Forecasting based on questions is a highly subjective problem. The questions and their respective responses could vary depending on the demographics, education background, understanding of the domain, etc of the forecasters. Does the authors have any openly accessible user-study report highlighting the biases and how they are being addressed. This follows for both - human forecasters as well as "superforecasters"

I'm wondering how does the 1000 questions designed for evaluation covers forecasting of an open world set? Or is it only targeted to a few domains?

The question examples shown in Figure 4&5 seem at a very high-resolution. Although, it is appreciated that the source of the questions is provided, but "is 2024 going to be hotter than 2023" - What parameter is being considered here for comparison? is it mean temperature? Can LLMs infer these for a new undefined concept?

Methodology relies on online links and APIs, thus limited in its coverage of questions.

Reproducibility is missing; validation is difficult.

User -study report should be provided publicly. What's the demographics of the human forecasters?

Reliability and risks associated with the methodology - Is stress test performed on the methodology for use in real-world? What are the metrics?

### Questions
Questions in Weakness Section.

### Soundness
2

### Presentation
3

### Contribution
3
