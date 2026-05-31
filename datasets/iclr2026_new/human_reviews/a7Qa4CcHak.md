## Human Reviewer 1

### Summary
The work contributes a new benchmark, with 74 tasks across a range of domains, that test realistic terminal-based software capability. Each task is reasonably carefully reviewed and has undergone several quality checks. While there are no human baselines of these tasks, the creation process involves time and difficulty estimates. The agents tested perform reasonably well, providing confidence that there is some signal, while also not being close to saturation.

### Strengths
Overall, the paper is exceptionally strong:
* It is well-presented, with clear information about the tasks, the task creation process, and agent testing methodology. 
* The tasks are well-reviewed, lending confidence that the benchmark is of high quality.
* A large number of agents were tested
* Failure analysis provides valuable information.

### Weaknesses
The paper would have been stronger if:
* we had human baselines (i.e. an expert or junior engineer was asked to complete the task in the same conditions), instead of time estimates as these might over/under estimate the actual time required (famously this is quite hard to accurately do).

### Questions
* What happened to the other tasks from the 229 that were not selected? Did they not pass quality checks? 
* Did you verify that the LLM judge that was used in failure analysis was accurate by manually verifying a small sample?

### Soundness
4

### Presentation
4

### Contribution
4

### Rating
8

### Confidence
5

---

## Human Reviewer 2

### Summary
This paper introduces Terminal_Bench, a benchmark for evaluating AI agents' capabilities in terminal environments. The authors build a test suite containing various real-world terminal tasks, spanning file operations, system administration, and development workflows. Through systematic experiments on mainstream language models, the work reveals that even state-of-the-art models exhibit significant limitations when handling complex terminal interactions.

### Strengths
1. **Comprehensive task coverage**: The benchmark spans multiple levels from basic file operations to complex system configurations, offering good representativeness of real-world scenarios
2. **Automated evaluation pipeline**: Establishes a fairly complete automated testing and scoring infrastructure, reducing subjectivity in assessment
3. **Thorough empirical validation**: Systematic comparison across multiple mainstream models effectively reveals current technological limitations
4. **Strong reproducibility**: Detailed task descriptions and evaluation scripts facilitate adoption and extension by other researchers
5. **Insightful error analysis**: Categorizes and discusses failure modes, providing useful guidance for future improvements

### Weaknesses
1. **Limited diversity in certain categories**: While covering multiple task types, some categories (network configuration, distributed system management) have sparse representation, potentially failing to capture the full spectrum of real-world usage
2. **Narrow evaluation metrics**: Predominantly relies on binary pass/fail assessment, lacking consideration of execution efficiency, code quality, and other important dimensions. The scoring mechanism for partial completion is insufficiently granular
3. **Static environment limitations**: Testing environments are relatively static, not adequately simulating dynamic environmental changes, concurrent operations, and other complexities found in production settings
4. **Insufficient treatment of user interaction**: Terminal operations frequently require user confirmation and interaction, but the benchmark's design doesn't adequately address this aspect
5. **Security considerations absent**: The paper lacks substantive discussion of security risks associated with AI agents executing terminal commands, and doesn't propose corresponding safety mechanisms

### Questions
1. For complex multi-step tasks with state dependencies, how do you ensure evaluation fairness? Different execution paths may achieve the same goal - how does your system handle this variability?
2. What was the methodology for task selection and design? Was there user research or expert consultation to validate task representativeness?
3. For failed executions, does the evaluation system credit partially correct steps? How do you quantify degrees of "near-correctness"?
4. Real-world terminal environments vary across system versions and configurations - how does the benchmark account for this environmental diversity?
5. Have you considered extending the benchmark to include security testing, such as detecting whether models might execute potentially dangerous commands?

### Soundness
3

### Presentation
2

### Contribution
3

### Rating
6

### Confidence
4

---

## Human Reviewer 3

### Summary
This paper introduces a collection of 74 new agentic tasks that can be completed entirely using the terminal. The tasks were built using a crowdsourcing process with multiple steps of verification and testing. The performance of 18 different models across six different agent scaffoldings were tested on the tasks, showing a maximum average resolution rate of slightly below 35%. An error analysis was performed at both the trajectory and command level, showing that models display a balanced variety of errors when completing tasks, not indicating any single important bottleneck.

### Strengths
1. Thorough testing and verification process throughout task development, including algorithmic, LLM-powered, and human review.
1. Builds on standards/checklists from prior work, like MAST and ABC
1. Used a collaborative crowd sourcing process to build a relatively large number of diverse and difficulty tasks
1. Developing a simple, shared scaffold as a reasonable point of comparison
1. Detailed error analysis

### Weaknesses
1. It's possible that the comparisons would be more fair if the best/preferred scaffold for each agent were used rather than a shared scaffold (which might still favor one model over others).
1. An LLM judge for error analysis was chosen based on agreement with a human annotator on 20 traces, but there are 74 tasks. I think this leaves open a large possibility of sampling bias.
1. "Most agents attempt tasks for less than 20 minutes." This seems very limiting, when most of the tasks are estimated to take humans at least an hour. Models are known to suffer from early stopping in agent tasks, it seems this was not controlled for.
1. The tasks are all public, limiting the longevity of this benchmark

### Questions
1. "We find that command failures calling executables that are not installed or not in PATH are the most frequent." Are you sure that the environments or agent scaffolds don't simply have bugs? Are the environments missing standard linux packages? Did you have humans try to complete the tasks in the same environment as the agents?
1. Have you collected data from agents while attempting to limit their tendency to submit early?

### Soundness
4

### Presentation
4

### Contribution
3

### Rating
8

### Confidence
4