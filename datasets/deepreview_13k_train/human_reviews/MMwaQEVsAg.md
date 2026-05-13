# Commit0: Library Generation from Scratch

- Decision: Accept
- Scores: 6, 6, 8

## Abstract
With the goal of benchmarking generative systems beyond expert software development ability, we introduce \commitzero, a benchmark that challenges AI agents to write libraries from scratch. Agents are provided with a specification document outlining the library's API as well as a suite of interactive unit tests, with the goal of producing an implementation of this API accordingly. The implementation is validated through running these unit tests. 
As a benchmark, \commitzero is designed to move beyond static one-shot code generation towards agents that must process long-form natural language specifications, adapt to multi-stage feedback, and generate code with complex dependencies.
\commitzero also offers an interactive environment where models receive static analysis and execution feedback on the code they generate. Our experiments demonstrate that while current agents can pass some unit tests, none can yet fully reproduce full libraries. Results also show that interactive feedback is quite useful for models to generate code that passes more unit tests, validating the benchmarks that facilitate its use.
We publicly release the benchmark\footnote{\url{https://huggingface.io/}}.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper introduces commit0, a benchmark for evaluating programming agents on generating software libraries from scratch given comprehensive specifications and unit tests. The authors then present SDE-1, a prototype agent that demonstrates different aspects of designing agents for this task such as drafting an implementation, feedback via linters, refining with execution feedback.

### Strengths
1. **Ambitious benchmark even if not for current gen models.** I particularly like that the benchmark pushes beyond current codegen evaluation setups by targeting full library implementations. Although this might seem too difficult a task currently, having such a benchmark could produce interesting solutions in the space (a la swebench), esp. for such long-horizon tasks.

2. **Multiple sources of feedback.** It's nice to see the benchmark itself integrate several sources of feedback such as linting, coverage, and unit tests. This is usually moved to the agent/system being evaluated, but I think having some standard ones such as linting within the benchmark makes comparing solutions more standardized.

### Weaknesses
 **Missing actionable insights.** While commit0 tackles a newer task compared to related work like HumanEval, SWEBench, and R2E, I'm not convinced the insights gathered are interesting or new. While the community can attempt to extract more, it would be nice for the paper to suggest a few directions even with primitive experiments. For instance, the diminishing returns on iterating with execution feedback has already been shown in prior work. I'm wondering if there's any evidence that this task will bring new insights for designing code generation systems/agents or training better models.

**SDE-1 Design** The authors mention that to balance the model's broader context of other functions, they use an entire module as one unit of generation with module-level dependency analysis. I am not convinced that this is a good choice. A module can be quite large in popular repositories and libraries (such as the ones in commit0) spanning a few 100 lines making it quite complicated to generate. My concern is that the result "random-ordering leads to more passed tests than topological sort" is a result of the unit being too large to generate, leading to more incorrect implementations.

### Questions
Que: In Figure4, it's unclear what the columns "stage 1" and "+ spec" suggests. It seems that the only prompt for a commit0 task is the specification of the library. However, the "stage 1" column suggests a setting where you don't pass the spec at all? What is the prompt in this case?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces a new benchmark commit0, evaluating agents abilities of writing python libraries from scratch. In this benchmark, agents are provided with starter repos, specifications, and unit tests to start with. Then, the agents' final commits with the implementation of the libraries would be tested by the unit tests. They also designed a prototype agent SDE-I that operates in three stages.

### Strengths
- The authors curated a new benchmark commit0 that could assess agents' abilities of implementing various python functions. This benchmark could help with evaluating and thus further improving agents' code and repo generation abilities.
- The authors introduced a new framework SDE-I which could assist the repo generation process for agents.
- The authors perform some ablation studies that might provide insights into how agents utilize additional information of specifications/tests

### Weaknesses
 - The authors did not provide comprehensive evaluation of their proposed agent SDE-I on the full benchmark commit0 that they curated. They only provide full results of SDE-I of stage 1 on the full benchmark. Thus, their results might not fully reflect the actual abilities of SDE-I on commit0. It would be good to have the results of all stages of SDE-I on commit0.
- The authors did not evaluate other existing agents on commit0, which makes it less clear how current agents perform on such tasks. It would be interesting to have results of agents based on frameworks like ReACT or CodeAct on commit0.
- The authors do not provide example instances from the commit0 benchmark, nor example trajectories by SDE-I on commit 0. It would also be nice to have code for synthesizing new data and example benchmark evaluation code. With example instances provided, it will be more clear what are tasks like in commit0. It would be good to have 1 or 2 examples in the main text of the paper and include more in the appendix.
- The authors did not provide the average cost of SDE-I on commit0. For example, it would be good to have a table containing the average cost of the proprietary models.
- The authors did not make clear how they prevent agents from accessing existing online implementations of the python functions via web browsing. It would be good to have a more detailed explanation maybe in the appendix.
- When performing ablation study, the authors found a decrease in performance of the agent when additionally provided with the specifications or tests, and hypothesized that this might be due to the specifications/tests not relevant to implementation. However, the authors only feed the first 10000 tokens of the full specification / test to the agent. The prompts being incomplete might affect the performance. It would be more interesting to see if including relevant details of the specification / test would help improve agent performances.

### Questions
- It would be nice if the authors could provide further explanation on how they prevent agents from accessing existing online implementations of the python functions via web browsing.
- It would be nice if they authors could provide more example instances from commit0 and provide example trajectories by SDE-I.

### Soundness
2

### Presentation
3

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
Summary: The Commit0 paper proposes a new benchmark for the coding proficiency of large language models. Simple existing coding benchmarks are typically done on smaller well defined problems with a simpler interaction model of providing a problem description to the LLM and getting back the LLM’s generated code solution. Commit0 tries to create problems to solve with the complexity a human software engineer would have to solve in a real job, like implementing a whole set of related functions from the spec for the library. Commit0 also includes the iterative nature of software development where the LLM’s code solutions are run through lint checks, and test case checks and the test results and LLM generated code are passed back to the LLM to allow it to iterate and attempt to fix any issues found.

Commit0 also includes an example LLM agent SDE-I to implement the functionality needed to solve the benchmark proposed. The SDE-I agent calls leading LLM models from places like Anthropic and OpenAI to provide baseline scores for the Commit-0 benchmark. The SDE-I agent defines the basic dataflow, prompts and interfaces needed to complete the Commit0 benchmark tasks. 

The goal of this benchmark is to more accurately assess how well LLMs can do solving coding problems that are a lot more like what real human SDE have to do at work. Improvements in the benchmark will come from better LLMs being developed, and improvements to SDE-I to create better prompts and work-flows to pass to the LLMs the best context in terms of related code and task descriptions of the functionality required in the context window passed to the LLM.

### Strengths
Commit0 is a much more realistic measure of how well an LLM will do software development on a task that matches what real human software developers have to do in their jobs.

Including the iterative nature of software development by passing back lint and test errors to the LLM to allow it to attempt further edits and improvements to the code is great.

Having a whole set of functions to implement to support a scenario is great to force the LLM to handle the complexity of tasks real human software engineers have to deal with.

### Weaknesses
W0: The computational burden to solve the full Commit0 test set is immense, so the cost to run this benchmark might be prohibitive for many labs to participate. What does it cost currently?

W1: Real developers have to produce specs for the high-level design and shared data structures, and also unit tests and docs for all the private functions they are writing. That sort of thing I guess could be all done inside the SDE-I agent, but the ability for the agent to ask itself, what is the spec for this internal function, what are the unit tests for to verify this internal function is correctly implemented and allowing the agent to iterate on the errors it finds by running it’s own unit tests on it’s own internal (and public) functions and being able to ask itself if the function it wrote completely implements all aspects of the spec in a “reflexion” sort of way I think will be important to enable surpassing human levels of coding in the SDE-I agent.

W2: With training LLMs there are these scaling laws about if you use a bigger model, or train for longer on more data – the results just get better.  Similarly for the SDE-I agent if it’s allowed to independently generate each function multiple times and then pick the best implementation in a “reflexional” sort of manner, or allowed to iterate more times to fix errors, and to restart from scratch if it is still failing a function’s tests after N calls – the error rate can be pushed lower with more CPU/GPU power applied. So comparing different SDE-I agents – it seems like there has to be budget of how many tokens-in/tokens-out are allowed to compare different approaches. If you are running your LLM local, then maybe it’s wall clock time.  If you are calling models in the cloud, maybe it’s total cost in $$$, but it just feels like to find the best SDE-I design the total compute between different approaches has to be held constant, or the total cost of calling models in the cloud has to be constant, for fair comparisons between SDE-I agents and the LLMs they use.

### Questions
Q0: What does it cost to run the Commit0 tests to get the numbers presented in the paper? It would be nice to see more baselines like from Llama 8,70,405 or Mistral or the leading coding LLMs, even if just for the lite/small testset.

Q1: I think defining a smaller subset of the benchmark was smart in the paper, given the cost to solve the whole thing. Would it make sense or be useful to take current simple benchmarks (humaneval, etc) and plug them in as tiny benchmark sets in Commit0, so the power of being able to iterate on the lint and test results can be checked out by smaller labs. Also to debug and tune future SDE-I agents, it might be nice to have proof of concept small Commit0 test sets to test against.  I suggest repackaging common coding datasets in Commit0 format because some effort has been made to exclude (humaneval, etc) from LLM training datasets, so as a fast easy Commit0 dataset they could serve some use.

Q2: Would a benchmark for Commit0 leaderboard of best results for $20 compute, $200 compute make sense?  Like should I use OpenAI’s most expensive model for fewer calls/iterations or use OpenAI’s smaller less expensive models for more calls/iterations? Basically level the playing field so it’s the best agent for a fixed cost – use any LLM you want – but you only have $20 or $200 to work with. Design a test subset and pick a dollar $$$ amount that is reasonable for labs to participate.  In the SDE-I agent basically you run through all the problems in the benchmark in 1 pass and then you just keep iterating on your results till you run out of money.

### Soundness
3

### Presentation
3

### Contribution
3
