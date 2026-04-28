# Identifying the Risks of LM Agents with an LM-Emulated Sandbox

- Decision: Accept
- Avg Score: 7.33
- Scores: 8, 8, 6

## Abstract
\label{sec:abstract}
Recent advances in Language Model (LM) agents and tool use, exemplified by applications like ChatGPT Plugins, enable a rich set of capabilities but also amplify potential risks---such as \tentative{leaking private data or causing financial losses}. 
\tentative{Identifying these risks is labor-intensive, necessitating implementing the tools, setting up the environment for each test scenario manually, and finding risky cases.  As tools and agents become more complex, the high cost of testing these agents will make it increasingly difficult to find high-stakes, long-tail risks.}
To address these challenges, we introduce \methodabbrv: a framework that uses an \lm to emulate tool execution and enables scalable testing of \lmagents against a diverse range of tools and scenarios.
Alongside the \sim, we develop an \lm-based automatic \ss \eval that examines agent failures and quantifies associated risks. \tentative{We test both the tool emulator and evaluator through human evaluation and find that \failprecadv of failures identified with \methodabbrv would be valid real-world agent failures.}
Using our curated \tentative{initial} benchmark consisting of \numtoolkit high-stakes toolkits %(most of which are challenging to test in real environments) 
and \numtest \tests, we provide a quantitative risk analysis of current \lmagents and identify numerous \fails with potentially severe outcomes.
Notably, even the safest \lmagent exhibits such failures \bestfailinc of the time according to our evaluator, underscoring the need to develop safer \lmagents for real-world deployment.%
\ificlr%
\else
\footnote{Project website, demo, and open-source code can be found at \url{http://toolemu.}
\fi

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This work introduces ToolEmu, a framework that utilizes a language model to mimic tool execution, allowing for scalable testing of language model agents across a range of tools and scenarios. This includes an LM-based automatic safety evaluator that quantifies associated risks and investigates agent failures. Extensive experiments showcase ToolEmu's effectiveness and efficiency. In terms of effectiveness, it demonstrates, through human evaluation, that 68.8% of the failures identified with ToolEmu would indeed be considered real-world agent failures. Regarding efficiency, it significantly reduces testing time, generating failures in less than 15 minutes compared to the 8 hours required by existing sandboxes for the bash terminal. ToolEmu assesses the safety and usefulness of various LM agents, offering insights into their performance and the impact of prompt tuning.

### Strengths
1.	Compared to some traditional methods, Agent-based ToolEmu reduces the labor needed to construct a testing environment for simulation by utilizing the general intelligence of LLM and various pretended tool functions. 
2.	ToolEmu dramatically reduces testing time, generating failures in less than 15 minutes, a significant improvement compared to the 8 hours typically needed by existing bash terminal sandboxes. This notably enhances testing efficiency.
3.	ToolEmu effectively captures potential failures, as demonstrated through human evaluation, where 68.8% of identified failures were validated as real-world agent failures.

### Weaknesses
1.	The paper could benefit from reorganization to enhance clarity. While it's understandable that due to space constraints, much information had to be placed in the appendices, the frequent transitions between the main text and the appendices could be confusing. I would suggest the authors consider optimizing this structure.
2.	In Table 3, it may be overly simplistic to validate effectiveness by comparing the Cohen’s κ between human annotators and the Cohen’s κ between human annotators and automatic evaluators. Furthermore, if the value of Cohen’s κ between human annotators is only less than 0.5, it raises questions about whether the annotated results of human annotators can be considered as the ground truth.
3.	The contribution of this work could be further improved by providing more interpretability.

### Questions
It's sound work, but I have a couple of queries I'd like to discuss with the author. I'm curious about the reasoning behind the choice of a relatively small sample size of 144 test cases. I would like to understand what level of coverage the research aims to achieve with this number. Additionally, I'm interested in the rationale for using only 100 test cases from the curated dataset for validation. I have concerns about whether such a small sample size is sufficient to validate the experiments effectively.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper identifies a challenge of testing LLM integrations with tools and plugins: how can we test LLM behavior and risks in the context of an open ended set of plugin capabilities and user scenarios?   To address this problem, the paper uses a tool emulator, built using an LLM itself, to emulate potential behaviors of arbitrary plugins.  The paper benchmarks LLM+tool risks in the context of a variety of scenarios, and validates the emulator's identified failures with human annotators.

### Strengths
This is an important problem: As LLM agents are integrated with a wide variety of tools and plugins, conventional software testing methodologies fail to scale to evaluate reliability.  LLM agents with plugins are becoming more and more widely deployed, and finding ways to evaluate LLM performance across an open-ended world of potential plugins is critical.

The design of ToolEmu's curated toolkit is well motivated, with a broad range of risk scenarios.  The evaluation of ToolEmu's identified failures with human annotators is a strength.

### Weaknesses
It's not clear that the range of plugin behaviors that can be emulated with ToolEmu matches the range of real-world software plugins being developed.

Not all identified failures are true failures, either because of invalid emulator behavior or invalid classification.

### Questions
Can ToolEmu scale to handle scenarios involving multiple plugins? Does this introduce new risk scenarios?

Given a range of real-world inspired plugins and user scenarios, could ToolEmu be used to identify the relative risk of real-world scenarios?
 
How might ToolEmu's results provide insights for debugging and fixing problems?

How sensitive is ToolEmu's findings to very minor variations in prompting and/or minor variations in emulated plugin responses?   (i.e., individual word choices, punctuation, etc)

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper is ambitious and tackles a complex and timely issue—evaluating the safety and effectiveness of Language Models (LMs) in various tool use scenarios. The approach of using LMs as both tool emulators and safety evaluators is interesting.

### Strengths
The paper is well-organized and written, with extensive supporting materials in Appendix. The main strengths of this paper include:
• Automatic Safety Evaluator: The development of an automatic safety evaluator using LMs is a significant contribution of the paper.
• Comprehensive Test Cases: The inclusion of a variety of test cases and toolkits, some of which have not been evaluated in previous benchmarks, adds value to the paper.

### Weaknesses
The methodology of using LMs to evaluate other LMs raises concerns such as reliability.

Also, it is unclear how biases or limitations in the evaluating LM might affect the evaluation of the LM being tested, or if ToolEmu, based on LMs, will have/incur potential risks itself.

There are no clear criteria for what makes a failure “severe.” Also, the fact that 6 out of 7 severe failures could be instantiated on a real bash terminal is interesting but lacks statistical context. Are these failures representative?

It is not clear how the authors measure the time it took to instantiate these failures. Was it a straightforward process, or were there complexities that could affect the time? Are the time metrics (8 hours vs. under 15 mins) average times or one-time measurements?

### Questions
Methodology:
- As the authors point out, “LM agents may fail in a variety of unpredictable ways” (Sec 3.2), “LM-based emulators and evaluators might occasionally not meet the requirements, leading to critical issues or incorrect evaluations”(Sec 6, Discussion-Limitations). 
- Also, it is unclear how biases or limitations in the evaluating LM might affect the evaluation of the LM being tested, or if ToolEmu, based on LMs, will have/incur potential risks itself.

Other than this, I have two minor comments:
- Introduction. “Out of these failures, we inspected the 7 severe failures of ChatGPT-3.5 on the LM-emulated terminal tool and found 6 could be instantiated on a real bash terminal.” There are no clear criteria for what makes a failure “severe.” Also, the fact that 6 out of 7 severe failures could be instantiated on a real bash terminal is interesting but lacks statistical context. Are these failures representative?
- Introduction. It is not clear how the authors measure the time it took to instantiate these failures. Was it a straightforward process, or were there complexities that could affect the time? Are the time metrics (8 hours vs. under 15 mins) average times or one-time measurements?

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good
