# LiveBench: A Challenging, Contamination-Free LLM Benchmark

- Decision: Accept
- Scores: 8, 8, 6

## Abstract
Test set contamination, wherein test data from a benchmark ends up in a newer model's training set, is a well-documented obstacle for fair LLM evaluation and can quickly render benchmarks obsolete. To mitigate this, many recent benchmarks crowdsource new prompts and evaluations from human or LLM judges; however, these can introduce significant biases, and break down when scoring hard questions. In this work, we introduce a new benchmark for LLMs designed to be immune to both test set contamination and the pitfalls of LLM judging and human crowdsourcing. We release \texttt{LiveBench}, the first benchmark that (1) contains frequently-updated questions from recent information sources, (2) scores answers automatically according to objective ground-truth values, and (3) contains a wide variety of challenging tasks, spanning math, coding, reasoning, language, instruction following, and data analysis. To achieve this, \texttt{LiveBench} contains questions that are based on recently-released math competitions, arXiv papers, news articles, and datasets, and it contains harder, contamination-free versions of tasks from previous benchmarks such as Big-Bench Hard, AMPS, and IFEval. We evaluate many prominent closed-source models, as well as dozens of open-source models ranging from 0.5B to 110B in size. LiveBench is difficult, with top models achieving below 65\% accuracy. We release all questions, code, and model answers. Questions will be added and updated on a monthly basis, and we will release new tasks and harder versions of tasks over time so that LiveBench can distinguish between the capabilities of LLMs as they improve in the future. We welcome community engagement and collaboration for expanding the benchmark tasks and models.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper introduces LiveBench, a new benchmark designed to evaluate LLMs in a way that mitigates common issues like test set contamination and biases introduced by human or LLM judges. LiveBench is continuously updated with new questions sourced from recent information, such as math competitions, arXiv papers, news articles, and datasets. This ensures the benchmark remains relevant and resistant to contamination by models trained on static datasets. Unlike many benchmarks that rely on subjective human or LLM judgments, LiveBench uses objective ground-truth values for scoring. LiveBench includes 18 tasks across six categories—math, coding, reasoning, language comprehension, instruction following, and data analysis. Each task is designed to be difficult, with top-performing models achieving less than 70% accuracy. The tasks are either based on recent real-world data or are harder versions of existing benchmark tasks. The paper evaluates dozens of LLMs, both proprietary and open-source. The benchmark provides detailed results across all six categories and highlights the strengths and weaknesses of each model. The authors plan to expand the benchmark with new tasks and models over time. They also plan regular updates to ensure the benchmark remains challenging as LLMs improve.

### Strengths
Originality:
This paper makes very well rounded verifiable benchmarks that cover a large number of tasks in different ways. This in itself is unique and a great contribution to LLM research.
While some of the tasks are inspired by existing benchmarks, some seem to be completely novel evaluation strategies (such as the proof reconstruction).

Quality:
The benchmark itself seems mostly well constructed and fair. The emphasis on task diversity and verifiability is commendable.

Clarity:
The methods are generally clear. Experiments are well explained. Benchmark tasks/evaluation are clear.

Significance:
This paper gives a useful benchmark for offline evaluation of LLMs. It has more task coverage than many other offline evaluation schemes. It also presented potential solutions to the benchmark contamination problem by making the benchmark “live”.

### Weaknesses
The core feature LiveBench claims to offer is being “contamination-free” However, it seems this claim rests upon two main assumptions that are never addressed:
1. The source data is not contaminated.
2. The data perturbations used to decontaminate or generate new data are actually sufficient to do so.

For (1): Consider the math category which utilizes questions from AMC12 2023, SMC 2023, AIME 2024, and IMO 2024. It seems likely these high quality data points would already be exploited by model developers for training models, intentionally or unintentionally. While the author’s do not directly discuss the implications of this, they do mention they do make some modifications to the questions. This leads to (2).

For (2): “Contamination-free” is a strong statement. **First and foremost, I recommend the authors define exactly what they mean by “Contamination-free”.** As a reader, my understanding of “contamination-free” is as follows: *Given I train my LLM on LiveBench up to month M, I will have no performance gain on the queries released in month M + 1.* Now, if the authors choose to run with this relatively strong definition of contamination-free, the authors should consider experimentally verify that training a model on prompts up to month M leads to negligible gains on prompts from month M + 1. Right now, I find this doubtful. For example, one of the author’s stated methods to change queries is through “modifying the prose and the answer order” (line 142). While it is likely that changing trivial sections of a query may decrease an overfit LLM’s performance slightly, the authors do not show that this fully mitigates contamination, or even to what extent it does (if not fully). Moreover, the authors suggest on line 303 that “many of the tasks are synthetic and therefore very fast and simple to create a new set of questions based on fresh data”. This raises the question: what is stopping an adversarial from generating, let’s say 1 million rows, of LiveBench data through this “fast and simple” process, training on it directly. Does this count as “contamination”? Would the release of 200 prompts in month M + 1 protect against this? Alternatively, let’s consider the instruction following summarization task: in this case, the update process presumably is to swap out the Guardian articles with new ones and change around the instructions selected from the 16 choices. However, how can the author’s be sure this meaningfully changes the task, especially because the article doesn’t even matter— the only thing the model needs to learn in order to overfit is the 16 different instructions that it will be checked on?

The authors could potentially address this in 2 ways:
1. Experimentally show how much training (with a reasonable setup) on M affects M + 1.
2. Establish a very weak definition of “Contamination-free” (e.g. the exact prompt is not seen in M + 1). However, there are no guarantees that training on M will not help M + 1. (Note that this heavily decreases the significance of the benchmarks as “contamination-free”)

**Bottom Line: In its current implementation, this paper has little evidence that its current query perturbation/generation process has any effectiveness against contamination. The authors should first define contamination, then defend that their benchmark sufficiently protects against this definition of contamination.**


The “live” aspect of the benchmark is powered by brute force, and is not necessarily automatic in any sense: It is not entirely clear how LiveBench is significantly more “update-able” than existing static and verifiable benchmarks, such as MMLU or IFEval. The author’s pledge to keep updating the benchmark monthly does not seem like a sufficient novel contribution to benchmark construction in general. The authors should document the update plan for every single fine-grain task. They should explain the estimated time and monetary cost to update this specific task. They should detail any optimizations in task design to ensure it is easy to update, if any. This would be a great table for the appendix and would make it clear what the paper contribution on this front is.


**Ablations on LLM-Judgments are insufficient, and potentially misleading:**
The experiments to show “LLM judges cannot accurately evaluate challenging math and reasoning questions” are not enough to address the scope of the claim.
In particular:
1. Only GPT-4-Turbo was tested as judge
2. GPT-4-Turbo was mainly judging itself, which is already likely worst case scenario
3. Only 2 models total were judged
4. Only 4 benchmarks tested
5. Subpar judge prompt
	a. No reference answer (generally these judges have either pairwise comparisons, or some form of reference answer)
	b. No rubric for judging

Possible ways to strengthen the experiment to adequately support the claim are as follows:
1. Utilize more LLMs as judges
2. Use the LLM to judge more models
3. Judge with a reference answer, and/or use a more updated judge prompt, such as the judge prompt from Arena-Hard-Auto or Alpaca-Eval 2.0.
4. Show accuracies on all tasks


**Insufficient comparisons to other benchmarks or “ground truth” evaluations:**
The authors compare LiveBench to Chatbot Arena and Arena-Hard. They hypothesize that the differences in rankings are mainly due to style or self-bias. If the authors suspect style to be a large factor in ranking difference they should compare LiveBench taking to style controlled Chatbot Arena rankings, proposed in the blog https://blog.lmarena.ai/blog/2024/style-control/. Note that Arena-Hard also has style control implemented. The authors should provide a table showing the correlation between the benchmarks. There are also Chatbot Arena categories, such as Math or Instruction following, which would provide more informative correlations to the respective LiveBench tasks.

### Questions
On line 214, the author suggests that LLMs are commonly used to perform table joins. Can they elaborate on this? This does not seem like a common real-world use case.


On line 299, the authors suggest they will release 200 prompts per month, but it seems in lines 307-311 they released significantly less than 200 prompts per month. Could the authors clarify what the plan for questions releases is?


On line 331, the authors suggest they use FastChat chat templates. Why is FastChat used over the explicit template provided in model tokenizers or readmes? FastChat is not necessarily guaranteed to be maintained to be constantly up to date for this purpose. Not all models are implemented in FastChat.


On line 363-365, the authors suggest that the zebra puzzles are too hard such that top models do not perform better than random chance. If this is the case, is there anything that can be done to make this category more relevant? E.g, making it slightly easier? Adding this noise into a benchmark seems unnecessary.


On line 402-407, the authors color outliers in red. However, outlines that are far below the line (large negative residual) are not colored. Why were some points determined as outliers but others not? This is true for both graphs.  Moreover, on the left plot, o1-preview is shown as an outlier, but the point next to Phi-3.5-mini-instruct is not shown as an outlier, even though the latter is even farther from the line of best fit.


On lines 438-445, the authors show Starling-LM-Beta on their graph, presumably to show the large differential between Chatbot Arena score and LiveBench score. However, Starling-LM-Beta is notably missing from Figure 5 which is described to show “all models”.  It is also missing from Table 3. Starling appears again in Figure 6… then it is gone again in Table 7… then back again in Table 9. Why is this the case? (I think Open Hermes and a couple other models also appear and disappear).


On lines 324-329, the authors cite various models they use. However, the citations for the remaining models are not present anywhere else. I find it strange that some models are chosen to be cited properly and others are not.


It seems the authors commonly use **answer ** to make the LLM generated answer parsable for verification. Why was ** chosen here, when it is also a common markdown symbol? Wouldn’t a less common symbol make sense here, like “{{answer}}” as one example. Peaking at the code, which seems to take the last bolded text as the final answer, it is conceivable that a markdown heavy model could have some extra bolding after the answer and get penalized for this. Think of something like “... **Final Answer: ** **X **\n\n **Additional Considerations: ** …” It is important to note that adding any bolded content after the final answer seems to not be explicitly warned against in the prompt to the LLM.


On lines 914-917, the authors show the judge prompt used for the LLM judge, which outputs a numerical score 1-5. However, it is unclear how this score is turned into a binary label used to calculate the error rates seen in Table 2.

### Soundness
2

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
3

### Summary
The paper presents LiveBench, a benchmark designed to evaluate LLMs while avoiding data contamination and biases associated with LLM and human judges. LiveBench includes frequently updated, diverse tasks across categories such as math, coding, reasoning, and data analysis, scoring responses based on ground-truth answers to ensure objectivity. With new, harder tasks released monthly, LiveBench aims to accurately assess LLMs as they improve over time.

### Strengths
- The benchmark addresses a prevalent issue in LLM evaluation.
- The paper is well-written, clearly explaining both the motivation and the implementation.
-  LiveBench scores models against objective ground-truth answers, not relying on possibly-biased LLM-judges.
- Tasks presented are very diverse.

### Weaknesses
 - Some models' performance in evaluations are very close. It's hard to say how similar they are without a significance test / stds.
- As LLM developers may train their models to excel on specific benchmarks, frequent updates could eventually lead to overfitting to LiveBench’s task formats, even with the regular introduction of new content. This could incentivize models to optimize for LiveBench-specific tasks rather than improving general capabilities. This can be solved with the introduction of more types of tasks and the contribution of the community, but it's also worth thinking about refreshing existing tasks' formats.

### Questions
Why did you not evaluate with some randomness to obtain significance over noise?

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper presents LiveBench, a new benchmark for evaluating LLMs designed to avoid common issues such as test set contamination and biases from LLM or human judging. LiveBench achieves this by (1) frequently updating questions with information from recent sources, (2) employing automated scoring against objective ground-truth values, and (3) covering a wide range of challenging tasks in areas such as math, coding, reasoning, language, instruction following, and data analysis.

The authors evaluated multiple prominent closed-source and open-source LLMs, showing that even top-performing models struggle to achieve over 70% accuracy, highlighting the benchmark’s difficulty.

### Strengths
1. This paper provides a dynamic, comprehensive and challenging benchmark that stays current with LLM development.
2. The benchmark’s monthly updates and open access to questions, code, and model answers contribute to high reproducibility and transparency.

### Weaknesses
1. The paper fails to analyze the quality of the questions used for evaluation, particularly those manually constructed or adjusted for model testing. This includes a lack of discussion on potential biases introduced during the manual creation or modification of questions, such as ensuring that the questions are not inadvertently designed to favor certain types of solutions or models. A more rigorous analysis of the question generation process is needed to understand the potential impact on the benchmark's validity.
2. The paper seems to employ a regular expression matching approach against ground truth to evaluate model outputs, a method which can introduce evaluation bias, especially for models with weaker instruction-following abilities. While the paper mentions potential biases from using large language models as evaluators, it neglects to analyze how regex-based matching could exacerbate evaluation inaccuracies. Specifically, the paper does not address the potential for models to produce correct answers that are not captured by the regex patterns, leading to false negatives. This is particularly concerning for tasks where the answer can be expressed in multiple valid ways, or where the model might use a different but semantically equivalent phrasing.

### Questions
1. Are all tasks' ground truths unique and definitive? How do you ensure that there is no ambiguity in the ground truth for each task?
2. In line 509, you mentioned that "In Srivastava et al. (2024), the authors modify the original MATH dataset (Hendrycks et al., 2021) by changing numbers in the problem setup, leading to significant declines in model performance across all LLMs, including the leading ones." Given this, do the tasks generated in this benchmark, such as the Typos task, also face similar issues due to using updated data sources under the same modification rules?
3. Could you provide a statistical table that clearly presents the number of questions, tasks, sources, and other relevant information for each category? This would enhance clarity and help readers understand the distribution and characteristics of the tasks more effectively.

### Soundness
3

### Presentation
3

### Contribution
4
