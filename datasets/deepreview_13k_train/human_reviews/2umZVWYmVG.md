# Assessing Large Language Models for Valid and Correct Code Reasoning

- Decision: Reject
- Scores: 3, 6, 3, 3

## Abstract
Frontier large language models (LLMs) consider reasoning as first-class citizens: they learn to refine their reasoning process and try different strategies during training. Thereby, when prompted, can think through problems and respond better with proper reasoning. For programming tasks, this makes code reasoning a must. In this paper, we propose the task of Code Execution Simulation (CES) as a proxy for evaluating the code reasoning capabilities of LLMs. CES defines the notions of valid or invalid reasoning process, which enables it to promptly (1) determine where the execution simulation diverges from ground truth for incorrect output predictions (essential to understanding limitations of LLMs in code reasoning) and (2) identify suspiciously correct output predictions (essential to understanding reasoning shortcuts, hallucinations, or potential data leakage). In addition to evaluating LLMs’ execution reasoning on a program with a single test, CES measures their reasoning consistency across tests with the same or different prime path coverage. This enables it to evaluate the code reasoning of LLMs in a spectrum: strong, weak, and random. Our results show that LLMs, to a great extent (82.32%), follow a valid reasoning process (results in 30.79% correct and 51.53% incorrect output predictions). However, their reasoning is mostly random (55.59%) or weak (41.69%), which explains their weakness in programming tasksthat require flow- or path-sensitive program analysis to succeed.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces Code Execution Simulation (CES), a new benchmark aimed at advancing the evaluation of large language models (LLMs) in code reasoning, particularly for complex programming tasks. CES addresses limitations in existing techniques, which lack comprehensive flow sensitivity and diagnostic capability, by unifying output prediction with key intermediate state evaluations—focusing on flow-sensitive execution paths. CES prompts LLMs at essential decision points (e.g., loop variables, conditions) and leverages adaptive in-context examples for clarity, providing a scalable framework that supports diagnosing reasoning divergence and consistency across varying test coverages. Evaluating thirteen models, including GPT-4 Turbo, Gemini-1.5 Pro, CodeLlama, DeepSeekCoder, Magicoder-S, SemCoder-S, and StarCoder2, on the HumanEval dataset of Python problems, the study finds that while LLMs generally exhibit a high rate of valid reasoning steps (82.32%), their reasoning quality remains predominantly random (55.59%) or weak (41.69%), often falling short in complex flow-sensitive tasks.

### Strengths
I think the paper is bringing out an important research question.

The general idea of expecting that LLMs can emulate code if we want to use them for more general software engineering tasks is an interesting one. I would encourage the authors to continue along this research direction.

### Weaknesses
Overall I think the paper is not ready for publication yet. The writing of the paper could be improved in places.
For example, in Equation 1 the notation is not clear. CES and GT should have something to differentiate from the variables in the equation. In Figure 7, the radar plot and legend are unclear.

The definition of prime paths being between any two program points requires justification. Could the authors justify this decision. I can imagine that the there are a lot more inputs and dependencies at some intermediate point. An alternative that seems natural would be to consider acyclic paths from the start of a program to some intermediate point. This way the inputs are clearly defined as the inputs to the program.  

RQ4 is the most important part of the paper. However, the results are underwhelming currently. The fact that there is no correlation between an LLM correctly emulating a piece of code and the LLM doing well on the programming task for that same piece of code does not support the hypothesis of the paper. Are there other explanations for this observation?

Though I agree with the authors that it would be better if we the LLMs could also emulate the code, I do think this is neither necessary nor sufficient to be able to find bugs, as an example. A lot of humans also find bugs by just pattern matching based on their experience. 

I would recommend that the authors explore programs outside of HumanEval, perhaps also exploring other programming languages (C/C++, for instance). The reason being that these programs and programming languages are "too simple" and might require detailed understanding of the program semantics. Perhaps using more complex C/C++ programs involving bitwise operations, pointer arithmetic, etc. and looking at  tasks requiring a more detailed semantic understanding of the program (such as finding security vulnerabilities) might be more conducive to proving the hypothesis of the paper.

### Questions
- Why not use paths that always start from the beginning of the program?

- Are there other explanations for RQ4?

- Why restrict to HumanEval programs? 

- Did you explore other programming languages other than Python?

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
3

### Summary
The paper proposes a Code Execution Simulation (CES) task to evaluate how well current language models understand and are able to execute code. The tasks is simulated the execution of a program by following the execution trace and producing the intermediate states. They introduce two aspects that go beyond code execution results correctness: checking if the simulated execution trace deviates from the correct program execution trace, and identifying situations where the model gets the right answer through questionable means. They also investigate how consistently these models perform with different test cases covering different execution paths. They find that LLMs still struggle with execution, especially for tasks that are more control flow sensitive.

### Strengths
- The paper provides a very thorough investigation of LLMs' capability for code execution. They not only provide a reasonable framework to define strong or weak code execution capability but also have detailed error analysis. They also investigate more than 10 models across small to large, closed to open. This will be a valuable resource for readers interested in the capabilities of current LLMs.
- It is interesting to study the "invalid reasoning path," which they define as incorrect intermediate output but correct end results or branch selection, etc. It shows how the model may not follow exactly how to execute the instructions for the current state, unlike a program, and then still get the final answer correct.
- Many other insights are backed by results from many different models. For example, they also investigate the consistency of code execution ability across different test inputs that cover different paths and show that most LLMs are not consistent in the sense that while they can execute some test cases successfully, even with test cases going through the same path, they often may still get them wrong.

### Weaknesses
The paper thoroughly investigates many aspects related to the execution path, like strong vs weak reasoning etc. However, it is not clear if the impact of variable values is discussed. For example, it isn't clear how things like large intermediate integers or long lists would affect the CSE results.



### Questions
- It is said that valid reasoning is at 83.32% but still only has a low accuracy of 30.79% being correct. Isn't this a bit misleading for the reader before looking into the definition of valid reasoning? The valid reasoning looks like anything but the invalid reasoning, and the invalid reasoning is not defined by whether the intermediate prediction results are wrong. So the valid reasoning containing errors should not be a surprising thing, right?
- Is there a typo in line 362 or line 20 about the number for valid reasoning? (83.32 vs 82.32)

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The presented paper proposes a new method for assessing the capability of LLMs to predict intermediate states of program execution. The method picks specific/relevant parts of the program such as branching conditions and loops and prompts the LLM to predict the state at these lines during execution of the program with a specific input. The authors then analyze how well the LLM prediction aligns with the program state and use this to assess the capability of LLMs to correctly and consistently reason about program states and to diagnose at which point the LLM starts incorrect predictions.

### Strengths
- The paper is well-written and nicely structured. The figures and tables are well formatted and legible.
- The story is engaging and the tackled topic interesting.
- The proposed method promises improvements of previous work regarding the ability to pinpoint errors made by LLMs during reasoning at a lower inference cost.

### Weaknesses
1) Choice of predicted values

The proposed method compares to previous work that assesses the internal state of the program at other positions. It is not clear why exactly the proposed positions introduced in Sec 3.1. (branch taking, predicates, return value) specifically are the mainly relevant positions. The main argument appears to be that these are the most relevant values to detect and diagnose inconsistencies, and predicting further values would confuse the model.

It is possible that such assertions hold for the given dataset (or even more general programs) but I did not find any evidence pointing in this direction. Specifically, the exclusion of assignment statements is not justified, and it is not clear that the chosen set of statements sufficiently captures mispredictions in assignments. The authors claim that predicting assignment values results in poor performance, but this is not supported by experimental evidence. A proper ablation study comparing the chosen subset of statements with a more comprehensive set including assignments would be necessary to validate this claim. The reference in Section 3 generally argues that long contexts deteriorate model performance, but it is not clear that this outweighs the potential benefit of more detailed insight into predicted values.

2) Confusing Definitions of valid/invalid reasoning

a) No correspondence to "consistency"

The authors mark any reasoning as invalid (Sec 3.3.) if an intermediate state (i.e. predicate) is incorrectly predicted but the consequence is predicted correctly (i.e. the branch-taking based on the predicate). This appears to not accurately capture whether the _reasoning_ was indeed wrong, since the intermediate state and consequence could still be _consistent_ (i.e. for "if p or not p:", it does not matter what is predicted for p to correctly predict that the branch is taken) and thus not represent a case of incorrect reasoning. It could or could not be that in the given dataset the introduced invalid reasoning always constitutes incorrect reasoning, but such evidence is missing from the paper.

b) Incorrect outputs are valid reasoning

The definition of "valid reasoning" includes (by definition) all instances where the model outputs incorrect output. This naming is confusing at best, since I would not expect that incorrect instances can constitute valid reasoning. As already mentioned in 2) this is due to a lack of evaluation of _consistency_ which I would consider indicative of reasoning.

3) Weak performance at CES may imply subpar benchmark design

In Sec 5.2 the authors mention many cases of "suspiciously correct" outputs based on natural language reasoning and inconsistent with the produced code reasoning. My interpretation of this would be that the presented code evaluation is potentially unnatural and confusing to the language model and thus artificially reduces performance, where free-form reasoning in natural language allows the models to correctly derive a result. Interesting counter-evidence for such an interpretation would be that models also often override correctly reasoned code states with incorrect (i.e. biased through function names) natural language reasoning results.

Similarly in Sec 5.5. weak correlation of models in CES and other related program understanding tasks do not necessarily imply that models are subpar reasoners, instead it could also imply that CES is not a format in which models can effectively express their code understanding. The new experiments in Appendix A.6 further strengthen this suspicion, as stronger models (GPT-4, Gemini 1.5 Pro) show good performance in bug localization, prediction, and repair, yet there is no correlation to CES. This suggests that CES may not be the ideal format to elicit code reasoning in language models.

The following are some smaller points that left me confused after reading:
- In Sec 5.1. the authors mention that there is no control for the coverage of test cases on programs. This appears weird, it would be interesting to somehow establish a controlled experiment for different path coverage. The detailed Figure 6 partially makes up for this.
- Figure 7 is very difficult for me to parse, especially the legend, but also the choice of chart format, respective the choices of grouping (it might make more sense to overlay models on triangular LO, CO, LC chart?)
- Figure 8: The instruction to the model reads "You are given a piece of Python code and its _output_" while the model is clearly given _input_ below. I hope this is a typo, otherwise it might have implications for the presented numbers.
- In Sec 5.2. "Invalid Reasoning" it reads "[…] LLMs with good performance in valid reasoning also make more invalid reasoning". This seems contradictory since reasoning is either valid or invalid, and the sum of it should be constant - thus increasing one would necessarily decrease the other. Please do clarify what is meant by this statement.

### Questions
Please provide a short statement or clarification to the points raised above.

### Soundness
2

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
The paper introduces Code Execution Simulation (CES), a framework for evaluating code reasoning capabilities in large language models (LLMs). CES measures LLMs’ capacity to predict both output and intermediate program states, including loop variables, iterables, conditional predicates, and branches. Except for the prediction accuracy, CES can identify whether models have valid reasoning process and can determine their reasoning consistency by executing test cases with different prime path coverage. Through experiments on multiple LLMs, the authors find that while LLMs can achieve a high level of valid reasoning (82.32%), their reasoning strength remains inconsistent, often performing at random (55.59%) or weak (41.69%) levels.

### Strengths
- This paper presents a novel framework, Code Execution Simulation (CES), to assess code reasoning in LLMs. Code execution capability is an important aspect to evaluate LLMs.
- CES's design is diagnostic. By defining the notions of valid or invalid reasoning process, it can detect suspiciously correct output predictions under invalid reasoning.
- CES uses a novel reasoning consistency metric to benchmark LLMs' code reasoning abilities as strong, weak and random, by executing multiple tests per program with same or different prime path coverage.

### Weaknesses
 - The primary weakness in this work lies in using code execution simulation as a measure of a model’s code reasoning abilities, which is debatable. While I agree with the authors' choice of evaluating reasoning validity (valid or invalid) and reasoning consistency as indicators of reasoning ability, as they reflect the model's understanding of code logic, the execution process itself requires substantial computational accuracy and strict adherence to instructions. For example, executing `a = b * c` demands multiplication skills, and executing `x = a[5]` requires precise indexing. The relationship between these computational abilities and code reasoning capabilities remains a research question. A model can easily compute `2 * 3`, yielding correct outputs in simple cases, but as inputs scale in complexity, the model's computational skills are challenged. However, this does not necessarily imply a lack of logical understanding or reasoning capability regarding the code’s logic. Thus, code execution simulation is inherently complex, and the authors do not sufficiently discuss this in the paper.
- The definition of the 'invalid reasoning process' is ambiguous. In Equation 4, the authors consider a compound property to be 'invalid' when it contains both correct and incorrect predictions. However, the example provided here involves the loop variable `o` and the loop iterable `zip(evens, odds)`. According to the definition given in Section 3.1, these two do not belong to the same property.
- The authors found in Section 5.5 that CES seems to have no correlation with other coding tasks, but they did not analyze the reasons for this. Is it because CES or bug-related tasks cannot represent the model's code reasoning ability, or do they focus on different aspects of reasoning ability? The authors also did not use other code comprehension tasks, such as code summarization, etc.
- It seems that there are several 'why' questions left unanswered in the evaluation. Why the predictions differed from ground-truth values? Why LLMs make suspiciously correct output predictions. The authors have relied solely on case analysis without providing quantitative data analysis.

### Questions
- Do the authors use the same prompts for different LLMs? How does the in-context learning examples affect the models' performances?
- To what extent does CoT (Chain of Thought) contribute to the results? Considering the hallucination phenomenon in LLMs , could the authors perhaps sample the output multiple times to observe the model's pass@k results?

### Soundness
2

### Presentation
2

### Contribution
2
