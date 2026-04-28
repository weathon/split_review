# WILT: A Multi-Turn, Memorization-Robust Inductive Logic Benchmark for LLMs

- Decision: Reject
- Avg Score: 4.25
- Scores: 6, 3, 5, 3

## Abstract
While large language models (LLMs) have shown impressive capabilities across a wide range of domains, they still encounter significant challenges in reasoning tasks that require gathering evidence over multiple turns and drawing logical conclusions from this evidence. These challenges present significant obstacles for LLM chat user interfaces, which rely on multi-turn interactions to facilitate effective collaboration. This limitation leads to real-world issues; for example, service chatbots must gather necessary information from customers over multiple turns to diagnose and resolve problems effectively. Despite the multi-turn nature of many real-world LLM use cases, most existing benchmarks rely on carefully curated single-turn tests, which often blur the line between memorization and genuine reasoning. To address this, we introduce the \textbf{Wason Inductive Logic Test (WILT)}, a simple yet challenging multi-turn reasoning benchmark designed to resist memorization. WILT is inspired by the Wason 2-4-6 task \citep{wason1960failure}, where participants must infer a basic boolean function involving three variables (e.g., $x < y < z$) by proposing test cases (such as $(2, 4, 6)$). In WILT, each test starts from a clean slate, with only the initial instructions provided, preventing models from relying on pre-learned responses. Over several turns, models must interact with the environment by suggesting test cases to narrow the possible hypotheses and ultimately infer the hidden function based on the outcomes. Our findings reveal that LLMs struggle with this task, exhibiting distinct strengths and weaknesses: some are better at narrowing down the hypothesis space by proposing valuable test cases, while others are more adept at deducing the hidden function from observed cases. Despite these variations, the best-performing model achieves only 28\% accuracy, highlighting a significant gap in LLM performance on complex multi-turn reasoning tasks.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces WILT (Wason Inductive Logic Test), a new reasoning benchmark for LLMs to evaluate reasoning over multiple turns.

Inspired by the Wason 2-4-6 task, LLMs need to identify a function of three variables by proposing test cases and observing outcomes. 

The authors evaluate all the main state-of-the-art LLMs on WILT and find that they struggle with the task, achieving a maximum accuracy of only 28%. The authors also perform additional analyses, looking into hypothesis space reduction, response complexity, and test case novelty.

### Strengths
* Novel Benchmark: WILT addresses an important gap in LLM reasoning evaluation by focusing on multi-turn reasoning. This capability is important for real-world applications like chatbots.
* Synthetic examples: The design effectively prevents models from relying on memorized responses from training data.
* Broad Evaluation and interesting analysis: A wide range of LLMs is evaluated. Additionally, the authors provide a detailed analysis of their performance using multiple metrics, including accuracy, hypothesis space reduction, response complexity, and test case novelty. The analysis reveals interesting insights into the models' behavior.
* Reproducibility: The authors provide clear descriptions of the benchmark, experimental setup, and evaluation metrics, facilitating reproducibility (even if the code is not released, which they promise to do).

### Weaknesses
 * Limited scope of reasoning: The tests in the benchmark are limited to simple arithmetic and logical operations. Testing multi-turn reasoning on a wider range of reasoning tasks would be interesting.
* Lack of human baseline: It would be interesting to know how good humans are at this task.
* 'Approximately correct' metric: As far as I can tell, there is no clear definition of this metric.

### Questions
1. Can you provide more details on how the functions are generated?
2. An analysis by function type would be interesting.
3. Do you have an idea of how hard this task would be for humans? Did the authors try themselves on a subset?
4.  Can you provide a precise definition for the "approximately correct" metric?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper starts with pointing out that LLMs have trouble in reasoning tasks that require gathering evidence over multiple turns and drawing logical conclusions from this evidence.  The paper presents a benchmark, called WILT (Wason Inductive Logic Test), which the authors frame as a "multi-turn reasoning" benchmark, and which is supposed to be aimed at resisting memorization. In WILT, each test starts  with an initial instruction. Over several turns, models must interact with the environment by suggesting test cases to narrow the possible hypotheses and ultimately infer the hidden function based on the outcomes. The experiments done in the paper suggests that LLMs struggle with this task, with the best performing model achieving only 28% accuracy.

### Strengths
The paper presents an interesting task based on the task presentedd in Wason 1960, in  the Quarterly Journal of Experimental Psychology. 

The goal of that paper was to "examine the extent to which intelligent young adults seek (i) confirming evidence alone (enumerative induction) or (ii) confirming and disconfirming evidence (eliminative induction), in order to draw conclusions in a simple conceptual task. The experiments there were designed so that use of confirming evidence alone will almost certainly lead to erroneous conclusions because (i) the correct concept is entailed by many more obvious ones, and (ii) the universe of possible instances (numbers) is infinite."

In this paper, after discussing the dataset, various analysis of LLMs response to those tasks are discussed.

### Weaknesses
It is not clear why the presented task is important from the point of view of an LLM's reasoning ability, as  you claim?
Reasoning is a catch-all phrase, so it will be helpful to elaborate on the specific kind of reasoning that you are focussing on.

Does this task (and the reasoning ability that you are focusing on) have direct relationship with a task which we ask an intelligent agent to do?
In particular, please provide specific examples of real-world tasks that this benchmark relates to.

Also, how well do humans do with respect to the task presented in this paper?
Please include a human baseline in your experiments, and/or discuss existing literature on human performance on similar tasks.

Perhaps you can provide an analysis of the computational complexity for both the ideal solution and for the approach taken by LLMs. 
This would help contextualize the difficulty of the task.

It would be helpful to give a detailed transcript of an interaction of an LLM on one of the tasks. Please provide a 
few representative examples showing both successful and unsuccessful interactions, along with analysis of what led to 
success or failure in each case.

In the Caption of Figure 1, you say: "For each test, the test harness initializes a hidden rule, and participants propose up to 30 test cases for each hidden rule before making a final guess." Examples of Harness in figure 1 are given as: (x < y < z) 
and (x = y = z).

But the harness example in tables 7, 8, 9, 10 are just triplets of numbers. 

Please clarify the relationship between the hidden rules (like x < y < z) and the triplets of numbers shown in the tables 7-10.

### Questions
See the questions in the weakness part.

In the Caption of Figure 1, you say: "For each test, the test harness initializes a hidden rule, and participants propose up to 30 test cases for each hidden rule before making a final guess." Examples of Harness in figure 1 are given as: (x < y < z) 
and (x = y = z).

But the harness example in tables 7, 8, 9, 10 are just triplets of numbers. 

Please clarify the relationship between the hidden rules (like x < y < z) and the triplets of numbers shown in the tables 7-10.

### Soundness
3

### Presentation
2

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
This paper introduced a multi-turn inductive logic benchmark for LLMs. LLMs are supposed to interact with a black-box oracle by suggesting test cases. The oracle will provide the feedback on the outcome of the test cases. At the end, LLMs have to infer the hidden function based on all the test case outcomes. The paper found that LLMs still struggle with the proposed task with SoTA models achieving only 28% accuracy.

### Strengths
1. The paper is clearly presented and well written.
2. The benchmark is simple and easy to use for testing LLMs.
3. The authors conducted extensive ablations on hypothesis space reduction, inversion capability, and response complexity.

### Weaknesses
1. While the authors motivate the paper by claiming that LLMs struggle with multi-turn reasoning, there is no clear evidence presented to demonstrate that LLMs struggle more in the multi-turn cases than the single-turn scenarios.
2. The assumption that successful hypothesis space reduction will lead to a better chance of inferring the solution is not clearly established. In fact, Figure 2 shows quite the opposite, where all models converge to almost the same level of cumulative explorations after 10 attempts. 
3. The sample size of the benchmark is too small. In addition, we should have human baselines to highlight how challenging the task is to humans.
4. The results from swapped test cases in Figure 3 are very hard to explain. If all models end up at about the same level at reducing hypothesis space (Figure 2), then why do the test cases matter so much at the inference time for different models?

### Questions
The results from swapped test cases in Figure 3 are very hard to explain. If all models end up at about the same level at reducing hypothesis space (Figure 2), then why do the test cases matter so much at the inference time for different models?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces WILT as a new benchmark designed to assess LLMs in their ability to handle multi-turn reasoning tasks. Inspired by the classic Wason 2-4-6 task, WILT challenges models to deduce hidden rules by proposing test cases over several turns. Unlike typical single-turn benchmarks, WILT is structured to discourage simple memorization and requires genuine inductive reasoning by forcing models to iteratively narrow down possible hypotheses.

Contributions include

1. A New Benchmark: WILT is specifically designed to test LLMs on tasks that require gathering information from previous context and adjusting responses across multiple turns. This makes it relevant for real-world applications where models engage in human-robot interactions.

2. Highlighting Multi-Turn Challenges in LLMs: The authors tested a range of current LLMs on WILT, finding that even the best models achieved only limited performance. This low performance emphasizes that many models struggle with reasoning tasks that span multiple interactions, showing a significant gap between single-turn and multi-turn capabilities.

3. Insights into Model Strengths and Weaknesses: The paper reveals interesting model-specific strengths; some models are better at generating test cases that effectively reduce the hypothesis space, while others are better in drawing conclusions from the evidence once it’s gathered.

### Strengths
*Originality*: WILT shifts from traditional single-turn benchmarks to a more complex multi-turn setting by drawing inspiration from the Wason 2-4-6 task, which is an original task design.

*Quality*: The benchmark aligns with research questions through clear test cases and thoughtful metrics. The analysis on model behaviors (e.g., strengths in hypothesis reduction vs. deductive reasoning) adds depth to the findings.

*Clarity*: The use of illustrative examples of WILT’s structure, including failure modes (e.g., “doom loops”), aids in understanding the benchmark design.

*Significance*: By identifying limitations in current LLMs' multi-turn reasoning capabilities, this paper raises an important point: strong single-turn performance does not ensure multi-turn effectiveness. This is crucial for applications requiring iterative evidence gathering and hypothesis testing, marking a step forward in aligning LLM capabilities with practical, interactive use cases.

### Weaknesses
1. Limited Novelties in Benchmark Design: WILT essentially reconfigures a classic logic game, the Wason 2-4-6 task, into a format for LLMs. This design, though interesting and original, does not present sufficient novelty. Designing benchmarks based on one specific task is completely acceptable, but the selected task should at least offer unique insights, constraints, requirements that other tasks could not provide. But in this case, WILT is based on one logic puzzle and could be replicated with many other similar logic games that require inductive reasoning abilities, e.g. any tasks that require pattern abstraction could also be applicable like 20-question game, word puzzle, MasterMind etc. At least, a Motivation section should be included to justify the choice of Wason 2-4-6 task instead of others. WILT’s setup may thus be perceived as overly simplistic and lacks the depth or adaptability that would make it a significant advance over existing reasoning tests. A more comprehensive testbed with several such tasks could lead to much more convincing results.

2. Limited Insights into Model Behaviors: The paper offers insights into why models perform poorly on WILT, but does not provide practices or recommendations on potential improvements. Without deeper analysis of why specific failure modes (e.g., “doom loops”) occur or how multi-turn reasoning could be enhanced, WILT risks being seen as a "toy" benchmark, yielding performance metrics without furthering understanding. Including more potential training data augmentations or improved training techniques to counteract these limitations would add more value.

3. Inadequate Justification of Real-World Relevance: The authors justify WILT by referencing real-world multi-turn interactions, as in “mirroring real-world tasks like debugging code or reasoning over time”, yet the benchmark itself does not closely simulate real-world tasks. In actual applications, multi-turn conversations often involve at least two subjects, rich context, existence of ambiguities,varying user intentions, etc. which are not addressed by a task as simple as deducing a hidden function. WILT’s game-like setup may fail to reflect the practical challenges models encounter in real-world inductive reasoning. Incorporating richer,or contextualized scenarios, reasoning tasks could make WILT more aligned with actual LLM use cases.

### Questions
1. The results suggest that models struggle with “doom loops” and “confirmation bias”, yet the analysis does not explore the underlying causes. Could the authors clarify any insights of model design issues (e.g., training data) that may lead to these failure modes?
2. “We release two test suites: a lite split, with 10 very easy tests and a canonical full split with 50 moderately difficult tests”. How were the specific rules selected? How do you define the “difficulty” of these rules? Why are the test samples so few?

### Soundness
2

### Presentation
2

### Contribution
2
