# MLE-Bench: Evaluating Machine Learning Agents on Machine Learning Engineering

- Decision: Accept
- Avg Score: 8.00
- Scores: 8, 8, 10, 6

## Abstract
We introduce MLE-bench, a benchmark for measuring how well AI agents perform at machine learning engineering. To this end, we curate 75 ML engineering-related competitions from Kaggle, creating a diverse set of challenging tasks that test real-world ML engineering skills such as training models, preparing datasets, and running experiments. We establish human baselines for each competition using Kaggle's publicly available leaderboards. We use open-source agent scaffolds to evaluate several frontier language models on our benchmark, finding that the best-performing setup — OpenAI's o1-preview with AIDE scaffolding — achieves at least the level of a Kaggle bronze medal in 16.9\% of competitions. In addition to our main results, we investigate various forms of resource-scaling for AI agents and the impact of contamination from pre-training.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper introduces MLE-bench, which is a benchmark consisting of 71 Kaggle competitions for measuring how well AI agents perform at machine learning engineering. The benchmark includes human baselines using the publicly-available Kaggle leaderboards. The paper also includes benchmarking with various scaffolds and foundation models, as well as some analysis of possible issues like contamination from pre-training.

### Strengths
Originality. To my knowledge, this benchmark is the first that is designed to evaluate ML engineering capabilities of AI agents. 

Quality. The paper has done a good-faith effort to benchmark using relevant models and mitigate potential issues (e.g., contamination and plagiarism). I liked the transparent discussion of limitations and potential issues. 

Clarity. I found the paper generally easy to follow. 

Significance. The introduction of this benchmark is quite timely given the interest in developing high-quality software engineering agents.

### Weaknesses
1. There seems to be an issue with Figure 2. I can only see a small snippet of the figure. 

2. I am concerned about the accessibility of this benchmark. As stated in section 6, it is a resource-intensive benchmark to run. If I understand the cost breakdown correctly, a single seed costs over $2500 to run (for the current prices of o1-preview). This is simply not feasible to university labs. I would suggest the authors provide two versions of the benchmark: one that is more accessible and one that is less accessible.

3. Given that the main contribution of this work is the benchmark, I think some of the experiments could be pushed to the appendix, whereas more details about the benchmark could be in the main body. For example, I’d like to see a more clear setup and rules section to make using the benchmark as easy as possible.

4. Given that this is a datasets and benchmarks submission, I wish the anonymized codebase was made available during submission. As a result, I am also reducing my confidence score.

5. There was a lot of discussion about splitting the competitions based on complexity, but I don’t see any presentation of the agent scores as a function of complexity. It feels strange to have this decomposition without using it in the later analysis.

6. Some of the selection criteria is clear (e.g., completed competition), but others are more qualitative (e.g., well-specified description), so it would be nice to see something a bit more detailed and systematic for those.

7. Some of the choices are not super clear. For example, what does “where sensible, we maintain the train/test split ratio” mean? (L157-158). Similarly, why was the headline metric chosen that way? Is this standard for Kaggle competitions? 

8. I would have liked to see examples of the generated code, potentially with an additional quality analysis. This analysis need not be extensive, even conducting the analysis on a randomly-selected output for one task would be interesting.

### Questions
1. Could the authors please clarify how the complexity for each competition was derived? A common way to do this would be calculate Cohen’s kappa on independently labeled by annotators. Is there a computed agreement score? (L145-149). I feel like this part could be more clear and principled.

2. How were the 7 development competitions chosen? (L150-152).

3. Are the restrictions in Section 3 a part of the benchmark? For example, the time limit of 24 hours? (L243).

4. Is the plagiarism checker provided as a part of the benchmark for free? (L229-233).

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
This paper introduces a new benchmark, “MLE-Bench”, with the goal of assessing AI agent’s abilities at machine learning engineering (MLE) tasks. The benchmark consists of 71 hand-selected Kaggle competitions from domains including image classification (38%), text classification (14%), and tabular tasks (13%) at a variety of difficulty levels. For each task, the agent is provided with a description of the task and a dataset. The agent is prompted to solve the task by writing code which is executed and evaluated analogously to the process of evaluating human Kaggle contestants’ submissions. Each agent is given up to 24 hours to iteratively improve its solution before evaluation.

The authors use MLE-Bench to evaluate several combinations of agent scaffolds and base language models,

- AIDE (with o1-preview, gpt-4o, llama-3.1-405b, claude-3-5-sonnet),
- ResearchAgent from MLAgentBench (with gpt-4o),
- CodeActAgent from OpenHands (with gpt-4o),

and compare the performance of these agents with a baseline derived from the performance of human Kaggle contestants. The evaluation metric is the percentage of tasks in which the agent would have received a Bronze, Silver, or Gold medal, had it actually participated in the respective Kaggle competition.

The authors show that both the choice of agent scaffold as well as the choice of language model has a significant effect on performance, and show that the best agent receives a medal in 17.3% of tasks.

The paper also includes experiments on the effect of hardware provided to the agents (0-2 GPUs) and the amount of time available to agents (up to 100 hours per task). Further, the authors evaluate whether the agent’s potential familiarity with a task (i.e. inclusion in its training data) affects performance. Finally, they analyze the agent’s code outputs for potential rule violations and plagiarism.

### Strengths
The experimental results presented in the paper are interesting and provide a clearer picture on current AI agent’s abilities for MLE. The benchmark will be a useful contribution to future work on agent scaffolds and LLMs, as well as for evaluating current systems from AI safety and preparedness perspectives.

Some strengths worth highlighting:

1. The proposed benchmark is comprehensive, and covers many parts of ML engineering (preprocessing, model training,...) and task domains (image, text, tabular,..).
2. The main experiments are rigorous and demonstrate the usefulness of the proposed benchmark.
3. The evaluation protocol seems generally sensible and the reported metrics are useful for understanding the results, although some improvements could be made (see below).

### Weaknesses
Please see the following suggestions that, in my opinion, would significantly improve this paper. Given some updates to the paper and clarifications to the questions in the next section, I would be happy to increase the score.

1. The authors acknowledge that their benchmark is very resource-intensive to run, requiring 1704 GPU-hours and >100M LLM tokens for a single seed (see Sec 6./Accessibility). Given that their main results used 16 and 36 seeds, this is clearly inaccessible to a large fraction of the research community. The paper would be improved if the authors could provide a lighter version of the benchmark (e.g. a subset of 5-10 tasks that reflect the main challenges of MLE) along with the metrics on this subset. This would not require running any additional experiments.
2. The aggregated results (across tasks, seeds, and time steps) provided in the paper are useful, but do not provide a full picture of the remaining open challenges in MLE and why the agents achieve good/bad levels of performance. It would be great if the authors could include more detailed and also qualitative results. In particular:
    1. A clearer analysis of which kinds of tasks agents perform well or badly on (e.g. split scores by complexity level and by task domain).
    2. The paper mentions raw per-task scores (Sec 2.2), although these do not seem to be included in the paper.
    3. The paper mentions that the authors analyzed agent transcripts/logs. It would be useful if these transcripts were provided (not necessarily in the paper, but in an external source)


### Questions
1. In Section 3.3, the authors show that the number of GPUs (0-2) provided to the agent does not significantly affect performance. This is a surprising result as, in contrast, I would expect this to make a substantial difference for human data scientists/MLEs. Could you share any insights regarding this? How often/rarely are agents using a GPU if it is provided? Does the majority of medals come from tasks where no GPU is necessary?
2. The paper uses Bronze/Silver/Gold medals to evaluate performance, which quantizes the leaderboard ranking into top-40%/top-20%/top-10% buckets (with varying thresholds as described in Sec. 2.2). Why did you choose this evaluation over using the leaderboard ranking directly (normalized into [0, 1])? That would likely give more fine-grained performance information.
3. In Figure 5, you use the “score normalized between the sample submission score and the gold medal score for that competition”. Why did you use this new metric instead of either the fraction of medals across seeds (as in other experiments) or the leaderboard ranking?
4. Depending on the agent, in 20% or more cases the agent is unable to make any valid task submission. What are generally the reasons for this? Including these reasons in the paper could support future work on improving these agents.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
10

### Rating Number
10

### Confidence
4

### Summary
The authors present MLE-bench, a benchmark designed to evaluate AI agents’ capabilities in machine learning engineering. This benchmark is constructed from publicly available Kaggle challenges, with AI agent performance assessed based on the percentage achieving medal-level scores comparable to real human submissions. The paper releases the benchmark’s data and code, includes three open-source agents as baselines, and evaluates state-of-the-art foundational models using the AIDE agent.

### Strengths
1. Given recent advancements in AI agents for coding, engineering, and scientific discovery, the proposed benchmark serves as a highly valuable testbed for evaluating foundational models and agents in real-world machine learning engineering contexts.
1. The paper is clearly written and easy to follow, providing necessary details on both the dataset and technical implementation.
1. The study includes solid empirical evaluations across different agents, foundational models, scaling factors, and contamination issues, offering valuable insights into AI agents’ current capabilities and limitations in the field.
1. The authors provide a thorough discussion of the benchmark’s limitations and ethical considerations.

### Weaknesses
### Accessibility of the Benchmark

As discussed by the authors in Section 6 L505, the benchmark is costly to run. Based on my estimates, using the authors’ cost descriptions and current rates on OpenAI and Lambda Cloud, a single full evaluation with AIDE and o1-preview would require approximately 4,000 USD (around 2,600 USD for API queries and 1,300 USD for an A10 GPU server). Considering the costs for development and extensive experiments would be substantially higher than a single evaluation, this benchmark may be inaccessible to small to medium-scale academic labs.

The authors may consider providing a lighter dataset split to improve accessibility, similar to the approach in SWE-Bench.

### Evaluation Reliability and Contamination

One particular challenge in benchmarks for AI agents is establishing reliable detection for potential cheating behaviors (e.g., hacking the evaluation function or accessing private test data). I appreciate the authors for addressing this with a tool designed to flag such behaviors. However, Table 6 in Appendix A.3 indicates a high false positive rate, which may hinder practical reliability. The rate is sufficiently high that manually checking all flagged submissions would be demanding.

Additionally, while the authors provide a thorough discussion and empirical analysis of contamination issues, this remains a critical limitation for this and other similar benchmarks. For instance, Figure 5 shows GPT-4o familiarity scores above 0.4 across all problems. Does this suggest that these problems are included in the model’s training set? Also, the conclusions drawn from the correlation between familiarity and performance could be significantly impacted by confounders, such as problem difficulty. Furthermore, while the obfuscated dataset and plagiarism detection tools are commendable efforts, foundational models could still potentially recognize rephrased questions and apply high-level strategies from their memories, making such behaviors difficult to detect.

More discussions on those concerns could be helpful. However, it is worth noting that these issues reflect broader challenges in the field, and it would be unreasonable to expect any single paper to fully resolve them. The paper has made valuable contributions with its detailed discussions and insightful empirical results on these challenges.

### Comparison Between Human Medal Results

As noted by the authors in Section 6 (L497), the train-test splits used in MLE-bench differ from the original splits in Kaggle competitions. The authors state that they “ensure that the distributions… are similar by checking that the example submission scores similarly on both sets” (L156). However, it is unclear how these example submissions were created. If the same model training pipeline were applied to both the original training set and the modified training set (a subset of the original), one would typically expect lower performance on the latter due to reduced training data. Could the authors clarify the configuration of the example submission, and specifically, what comparisons were made and under which settings?

### Additional Questions

### Questions
1. Would the authors consider discussing related works on AI agents, AutoML, and automated scientific discovery in the Related Work section? These areas seem relevant to the benchmark’s objectives.
1. Regarding the difficulty estimation in L145, how reliable is the human estimation process? Could the authors provide additional details on the setup and methodology for these annotations?
1. In L300, the authors note that “agents would execute commands that overload the machine’s disk or RAM, resulting in their process getting killed and their run finishing early.” Do the tested agents incorporate any error-handling or reflection mechanisms for such situations?
1. Are the three results in Table 3 statistically different from one another? It would be challenging to interpret the higher performance of the extra GPU setting if the second GPU was not utilized, which might suggest that differences could arise merely from noise.
1. In Figure 3, it might be useful to further scale o1-preview, as the curve does not yet appear to have plateaued.

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper constructs a benchmark for evaluating the capabilities of LLMs in automated data science tasks based on Kaggle competitions. This paper presents MLE-bench, consisting of 71 competitions covering diverse data modalities and task complexities. Rule-breaking detection and plagiarism detection are provided to prevent LLMs from generating undesired behaviors. Evaluations are conducted on both closed-source and open-source LLMs.

### Strengths
1. The proposed benchmark is quite challenging for current LLM agents.

2. A lot of factors are considered in the benchmark, such as time constraint, computation resource, etc.

3. The empirical evaluation is comprehensive.

### Weaknesses
1. My major concern lies in the test splits used in this benchmark, which cannot guarantee alignment with the private leaderboard score and thus leads to unfair comparison with data scientists from Kaggle. I checked several Kaggle competitions used in this benchmark and found that they supported “late submission” to provide the leaderboard score. Why MLE-bench does not choose to fully leverage this feature? Could you check whether the test splits used in MLE-bench align with the realistic leaderboard via this feature? If not, I think MLE-bench can only provide comparison among LLM agents rather than human data scientists from Kaggle.

2. As discussed in Line 501-504, there is an obvious discrepancy on available machine learning techniques between past Kagglers and modern LLMs. I suspect that the capabilities of LLM agents for winning a medal in MLE-bench also correlates to the year of the Kaggle competition. As such, the evaluation metric solely relying on whether an LLM agent can win a medal may lead to biased conclusion. Could you present complete results to show the effect of the competition starting year for the performance?

3. Also, could you provide empirical analyses on the effect of the competition complexity (as labeled high/medium/low) for the agent performance?

4. Could you present some successful cases and failed cases of o1-preview in MLE-bench?  The trajectories shown in Figure 2 are not complete enough to derive insightful findings.

5. How does plagiarism detection work? If the current competition is A, the plagiarism is detected in terms of merely notebooks in A or all the notebooks in competitions from MLE-bench?

6. As discussed in Line 505-509, I also think the current benchmark is too heavy for potential future research purposes. Maybe a light-weight version of MLE-bench can be considered as future work.

### Questions
See weaknesses

### Soundness
3

### Presentation
3

### Contribution
3
