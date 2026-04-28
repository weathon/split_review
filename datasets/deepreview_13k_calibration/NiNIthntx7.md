# RefactorBench: Evaluating Stateful Reasoning in Language Agents Through Code

- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 8, 6, 6

## Abstract
Recent advances in language model (LM) agents and function calling have enabled autonomous, feedback-driven systems to solve problems across various digital domains. To better understand the unique limitations of LM agents, we introduce RefactorBench, a benchmark consisting of 100 large handcrafted multi-file refactoring tasks in popular open-source repositories. Solving tasks within RefactorBench requires thorough exploration of dependencies across multiple files and strong adherence to relevant instructions. Every task is defined by 3 natural language instructions of varying specificity and is mutually exclusive, allowing for the creation of longer combined tasks on the same repository. Baselines on RefactorBench reveal that current LM agents struggle with simple compositional tasks, solving only 22\% of tasks with base instructions, in contrast to a human developer with short time constraints solving 87\%. Through trajectory analysis, we identify various unique failure modes of LM agents, and further explore the failure mode of tracking past actions. By adapting a baseline agent to condition on representations of state, we achieve a 43.9\% improvement in solving RefactorBench tasks. We further extend our state-aware approach to encompass entire digital environments and outline potential directions for future research. RefactorBench aims to support the study of LM agents by providing a set of real-world, multi-hop tasks within the realm of code.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces a novel benchmark, RefactorBench, designed to evaluate the limitations of LM agents in complex, multi-file code refactoring tasks within open-source repositories. RefactorBench consists of 100 handcrafted tasks, each defined by 3 natural language instructions that vary in specificity, requiring agents to explore dependencies across multiple files to complete tasks successfully. Initial experiments demonstrate that current LM agents struggle  with these compositional tasks, solving only 18% compared to human developers, who achieve 87% under short time constraints. Through trajectory analysis, the authors identify distinct failure modes, particularly the agents' difficulty in tracking past actions. To improve this, the authors propose to adapt baseline agents to condition on state representations which improves performance by 40.4%. The study positions RefactorBench as a critical tool for advancing the  development of LM agents in code-related environments.

### Strengths
* RefactorBench is a novel benchmark to evaluate LLMs in the complex multi-file code refactoring tasks, which can isolate unique language agent behaviors compared with similar benchmarks like SWE-bench.
* The benchmark construction process is technically sound, with unit tests included to ensure rigorous correctness assessment. The experiments provide insightful analysis of how current LM agents perform on this new task. Furthermore, rather than simply discussing the results, the authors go a step further by proposing enhancements based on their findings, achieving a 40.4% improvement in performance over baseline agents.

### Weaknesses
A key weakness of this work is its narrow focus on GPT-4o and SWE-Agent for evaluation, omitting other closed models like Claude, as well as open-source models and other LM agent frameworks. For a benchmark paper, evaluating a broader range of baselines would provide a more comprehensive view of existing LLM performance and help new models or LM agents identify their relative strengths and weaknesses. Additionally, a wider evaluation would allow for assessing whether the observed results generalize across different models, strengthening the benchmark’s robustness and relevance to the broader field.

### Questions
See the above weakness.

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
3

### Summary
RefactorBench introduces a new benchmark for evaluating LM agents on performing a variety of multi-file "refactoring" tasks. For instance, one task may involve adding new arguments to a class with sensible default values and updating dependent / affected components throughout the code base. There seem to be other diverse tasks. The authors show that these tasks, while seemingly straightforward for human programmers (most being solvable within 5 minutes by humans), can still be a challenge for existing agents when evaluated on AST-based unit tests against reference solutions. They provide a few evaluation settings, such as having a `lazy`, `standard`, and  `descriptive` version of each task and provide analysis of the dataset and model performance. Finally, state-aware interfaces for LM agents are proposed as an improvement over a simple SWE-agent baseline agent, which includes providing LMs a summary of code changes made overtime, that is demonstrated to improve performance.

### Strengths
- RefactorBench introduces a practical setting that remains relatively difficult for LM agents.
- The data quality seems fairly high based on my manual inspection.
- The three-tiered instruction approach (lazy, standard, descriptive) offers valuable insights into agent capabilities.
- The proposed improvements to SWE-agent and agent architectures in general represent meaningful advances.
- Provides thorough analysis.

### Weaknesses
 - The term `pseudo-task` is used in the abstract but doesn't seem to be used or elaborated on explicitly in the main text. I recommend using a more common term in the abstract, especially if it isn't defined elsewhere.
- Tractability is first used in Section 3.1 but is not defined until a bit later in section 3.2. I recommend pointing to this in the text in 3.1 when it is first used or cite a work that introduces this term. It doesn't seem conventional enough to use without definition.
- Figure 1 lacks substance and could be more much informative.
- With 100 instances the benchmark remains a bit small - however it may be understandable provided that there may a fair bit of human labor involved in creating instances.
- The lack of a train or, more importantly, a development set may limit the useful lifetime of this benchmark. Test-split only benchmarks encourage overfitting when they require some upfront system design (like agent systems). This may also have been a problem in the development of the agent systems presented in this paper.
- The writing is acceptable but could be slightly simplified or reorganized for greater clarity.

### Questions
- Line 162: can you clarify what you mean by design principle?
- Seems to be a mistake on line 415: Perhaps you mean a 40.4% relative improvement in performance?

### Soundness
3

### Presentation
2

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
This paper presents RefactorBench, a new benchmark designed to evaluate language agents ability to perform non-bug-fixing refactoring of multi-file code repositories. The authors run baselines and present analysis of common failure modes of existing LM agents on the task. The authors then present a new approach to improving AI agent task performance by directly modeling and conditioning inference on task state.

### Strengths
* clear explanation of generation of the benchmark + helpful metrics of the benchmark by proxies for difficulty (number of files / lines, instruction detail). Many questions can be explored with this dataset by using the different degrees of detail of NL insn, small-granularity feedback from the AST unit tests, and complexity of large repositories
* clean formulation of the task as a POMDP well-addresses the identified failure modes and motivates the state-aware method 
* compelling analysis of the results, with proper side experiments and task-related ablations to motivate state-aware agents
* refactoring is an interesting task, as prior works have focused on bug-fixing refactors. The insight that refactoring often necessitates "broken" intermediate states on the way to task completion poses an interesting research question for agentic frameworks.
* representing the "state" as NL keeps the framework flexible and fairly interpretable

### Weaknesses
 * the main distinction from SWE-bench is described as "handcrafted and underrepresented multi-file refactoring tasks", but SWE-bench does include some tasks that resemble "refactoring" in the form of feature requests.
* I worry that this is a benchmark that would soon be saturated, but I would not necessarily consider that a reason for rejection. Additionally, the contributions of this paper in the form of analysis make this point less relevant.
* I would have liked to see more analysis of why state is important specifically for refactoring. Can we get some qualitative analysis of what sorts of subtasks are done better with state modeling? What are some failure cases in the NL description of the state?

### Questions
* how did you choose the repositories to do refactoring on?
* Why do you think that refactoring now causes LM agents to edit the wrong files, while debugging LM agents rather consistently do? Does it have to do with the nature of refactoring being correct --> intermediately broken --> correct but refactored?

### Soundness
4

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
The sources present *RefactorBench*, a novel benchmark for evaluating language models' (LMs) capabilities in multi-file code refactoring tasks. The benchmark comprises 100 handcrafted tasks requiring edits across multiple files, with varying instruction sets to assess the models' ability to follow instructions and reason over past actions. The authors demonstrate that current LMs struggle with these complex tasks, particularly due to difficulties tracking past actions and maintaining context. To address this limitation, they propose "state-aware" interfaces that provide LMs with a representation of the current state of the codebase, leading to significant improvements in task performance. Finally, the authors outline potential future directions for research, including developing more efficient context generalization techniques and constructing robust interaction mechanisms for language agents in digital environments.

### Strengths
This is a well-written benchmark paper with clear motivation.

1. Filling the gap between existing bug-fixing benchmarks (e.g., SWE-Bench) and the need for real-world developers (e.g., code refactoring). Repo-level code generation benchmarks [1, 2, 3] are necessary.
2. Well-organized and comprehensive literature review for automated software engineering (ASE) systems.
3. Clear data collection procedure. Statistics on RefactorBench tasks, repositories, and AST-based unit tests are included.
4. Clear problem formulation as POMDP. Standardized evaluation with AST-based unit tests. The code is easy to run from anonymous GitHub.
5. An interesting discovery of the SWE-Agent prone to fix bugs instead of refactoring. The error analysis is also comprehensive.
6. An interesting discovery of state awareness's significance in enhancing language agents' capabilities with a synthetic experiment. The figure and flowchart are easy to understand.


[1] Zhang, F., Chen, B., Zhang, Y., Keung, J., Liu, J., Zan, D., ... & Chen, W. (2023, December). RepoCoder: Repository-Level Code Completion Through Iterative Retrieval and Generation. In Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing (pp. 2471-2484).

[2] Li, B., Wu, W., Tang, Z., Shi, L., Yang, J., Li, J., ... & Chen, K. (2024). Devbench: A comprehensive benchmark for software development. arXiv preprint arXiv:2403.08604.

[3] Liu, Y., Tang, X., Cai, Z., Lu, J., Zhang, Y., Shao, Y., ... & Gerstein, M. (2023). ML-Bench: Large Language Models Leverage Open-source Libraries for Machine Learning Tasks. arXiv e-prints, arXiv-2311.

[4] Huang, Q., Vora, J., Liang, P., & Leskovec, J. (2023). Benchmarking Large Language Models as AI Research Agents. In NeurIPS 2023 Foundation Models for Decision Making Workshop.

### Weaknesses
This paper has several weaknesses regarding the evaluation methodologies.
1. The tasks are relatively easy:
    - For most of the tasks given in the anonymous GitHub, I've learned that LLMs cannot even move some code snippets to another file or add additional parameters to one function. Is that correct?
       - In `problems/ansible_refactor/sort-groups-to-group-sort-task.txt`: Rename `sort_groups` to `group_sort` and update all references in the repo.
       - In `problems/ansible_refactor/add-log-parameter-get-group-vars-task.txt`: Add a log parameter to `get_group_vars,` keep the base case as true, and update the rest of the repository calls to have `log=False.`
       - $\ldots$
    - From my experience using Cursor and GitHub Copilot, the observation in this paper is not true. Most refactoring like these can be solved with one click of the mouse.
       - For example, I can modify the original function using the Cursor and open all the relevant files (i.e., Ctrl+F for that specific function). The Cursor will devise an auto-completion suggestion to refactor all usage of this function.
       I am pretty sure that if our language agent is equipped with some retrieval tools and employs a hierarchical structure (i.e., multi-agent) in which each agent updates one file separately, it would largely improve performance and consistency.

2. Bad definition of refactoring:
    - Martin Fowler's "Repetition is the root of all software evil" is a good point. However, I did not see any prompt examples of reducing repetition within the refactor tasks. From my daily experience, a good refactor should reduce the complexity and repetition of a large codebase and increase the portability of modules and functions. It is not about adding a logger to a function or moving some code to `utils.py.`
    - The refactor should not be evaluated using unit tests only. Unlike the bug-fixes scenario in SWE-Bench, the function before refactoring should also pass the unit test. The objective should be, for example, to reduce the length/loops of the initial code after refactoring while still passing the unit test.
    - I don't have a clear idea of how to evaluate the refactoring process, but it is obvious that using a pass rate for unit tests is insufficient. Below are some potential metrics you can choose from (maybe for your next benchmark).
      - *Test Execution Time*: After refactoring, measure if the test suite executes faster.
      - *Linting and Style Compliance*: Assess adherence to coding standards. (This might not be helpful because most code generated by LLM should follow linting compliance).
      - *Lines of Code (LOC)*: While not always directly indicative of quality, a reduction in LOC often reflects simplification.
      - *Function Size*: Track average function length; shorter, well-named functions are generally easier to understand and test.
      - *Coupling Metrics*: Evaluate coupling using Coupling Between Objects (CBO) measures. (I hate the coupling of my code. So, if the LLMs can solve that, it will be really helpful.)
      - *Dependency Analysis*: Check the number and nature of dependencies between modules. Reducing unnecessary dependencies enhances modularity and flexibility in the code.

3. Other frameworks worthy to test on [1, 2, 3]
     - Aider [1] also has a good way of code edits and refactoring using `git diff` [4].
     - Papers such as [2, 5] evaluate their performance on multiple agent frameworks.

### Questions
''Repetition is the root of all software evil'' -- Martin Fowler

It is a reference to the software engineering principle of Don't Repeat Yourself (DRY). The idea behind DRY is that repeating code or logic in multiple places can lead to problems.

What is the relationship of this quote with the whole paper?

### Soundness
3

### Presentation
4

### Contribution
2
