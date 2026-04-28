# Tests as Instructions: A Test-Driven-Development Benchmark for LLM Code Generation

- Decision: Reject
- Avg Score: 4.00
- Scores: 6, 6, 1, 3

## Abstract
This paper focuses on test-driven development (TDD) tasks, where test cases act as both instruction and verification for LLM code generation. We build a TDD benchmark to evaluate frontier models, where reasoning models of OpenAI achieve SOTA. We identify instruction following and in-context learning as the critical abilities for all models to succeed at TDD tasks. We further reveal their vulnerabilities to long instructions as an area of improvement.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper introduces a benchmark for evaluating LLM on test-driven development. The prompt simply contains a list of test-cases, and instructions to pass them, while returning only code. There are no hidden text-cases. To pass, LLM needs to generate code which passes all the tests in the prompt.
The benchmark contains 1000 React problems (this is a popular java script library) and solutions of 16 LLM to these problems, where each LLM generates response 10 times to estimate test failure rate. The benchmark contains a good distribution of task difficulties, from trivial to unsolvable. The authors categorize errors that cause test-cases to fail, into categories such as missing library import, deprecated frameworks are used, etc. The find that not surprisingly adding more test-cases to the prompt is more likely to cause failure (2 and 4 test-case prompts are evaluated), and that o1 models show superior performance.

I am not familiar with React, and not willing to learn it for the purpose of writing this review, so I just skipped most of the exampled.

### Strengths
I was looking forward to reading this paper, as the issue is certainly topical. Many of these benchmarks is being created, and this one is novel.

Benchmark generation is very costly, so the current project is useful.

### Weaknesses
Being focused on React is the main weakness. The authors claim that this is done because React is popular, and the code it produces is brief, but I am not convinced. Surely many python problems can be solved with few lines of code, and Python is a more popular language. This needs to be motivated.

Despite initial excitement, I feel like I learned very little from this paper. It seems obvious that most LLM coding mistakes come from missing libraries, ignoring instructions and training on legacy code. It would help focus presentation to clarify the conclusions. 

There is no discussion of how adding more tests breaks LLM. For example, does the same happen to human coders? Adding TWO issues to implement in a prompt is not the same as making the prompt longer with 4 test-cases, please clarify the framing around this.

### Questions
What was the real reason for using React?

Performance seems to be very stable, such that LLM do not improve very much between pass@1 and pass@10. This seems interesting, but why is that?

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
This paper introduces a new test-driven-development benchmark for code LLMs, wherein the instructions given to the language model is the code of the test directly, without going through a natural language description of the task. A benchmark of 1000 React tasks is constituted.

18 models, proprietary and open-source, of various sizes, are tested on the benchmark. The authors analyze the failure types and propose explanations for the various types of failures. They find that the latest o1 models from OpenAI, trained to reason in natural language before committing to an output, achieve impressive scores on the benchmark but forget part of the instruction, leading to lower scores than Sonnet on the most complex tasks.

### Strengths
## Originality

The paper presents the first fully-blown benchmark with test-as-instructions ([Programming Puzzles](https://arxiv.org/abs/2106.05784) also used code as instructions but was focused on algorithmic or mathematical puzzles). As argued in the paper, this prevents a gap between specification and test cases.

## Quality

The analyses in the paper are of good quality and many models are tested. The failure cases are analyzed by the authors, and concrete examples are given, which illustrates the problem and skills required to solve it. 

## Clarity

The paper was straightforwardly written, and easy to follow along.

## Significance

I could see this benchmark being used to assess programming abilities of LLMs or LLM-based systems. As outlined by the authors themselves, test-driven development looks more similar to the way software is developed in teams, and could lead to studies for products that could help developers' productivity.

### Weaknesses
 * I am concerned that the benchmark is too easily saturated by models already. A fully blown, public release of this benchmark should use the multi-feature mode that makes tasks more difficult; and probably use some form of validation (having software engineers write code) to make sure that the tests for the multiple features are indeed satisfiable;
* Another limitation of the paper is that it does not discuss the differences between it and SWE-bench-verified, which has become a standard for coding LLMs. More discussion should be included (for instance following the discussion in 6.4)
* A final concern is the data collection, which is left in the dark in this paper. Where do the tests come from? Are they scraped from Github, from learning websites? How close to the pretraining data are these tasks? Could contamination explain the really high scores?

### Questions
* Have you tried running the benchmark with various forms of agents, and execution feedback? This should easily correct some of the error categories you have discovered (such as version mismatch or uninstalled module);
* Can you provide additional visualizations, explanations and statistics on the contents of the dataset? Perhaps a few additional examples in the appendix as well would be useful.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
1

### Rating Number
1

### Confidence
4

### Summary
This paper proposes a test-driven development (TDD) benchmark, where the model needs to generate code to pass given test cases. The benchmark consists of 1000 Javascript-based web app development tasks. This paper evaluates modern LLMs' performance on the proposed benchmark (e.g., o-1, claude, deepseek, etc). Error analyses show that most LLMs can generate syntax-error-free code, and often pass at least one test case. The paper also proposes a more challenging benchmark by merging two original TDD tasks into a duo-feature task.

### Strengths
1. TDD is an important evaluation task that meets real-world coding scenarios.

### Weaknesses
1. Limited test cases are shown to be hacked by LMs, i.e., LMs often generate incorrect code solutions that can still pass these test cases.
2. Lack of benchmark details. In line 106, the paper claims the benchmark consists of 1000 examples, while never clarifying how these examples are collected.
3. Poor paper writing. All references and tables are in incorrect format. There are a lot of redundant sentences (e.g., in line 161, since $k$ most be smaller or equal to $n$). Duplicated contents (e.g., both Section 2.2 and Section 4.1 are named Task Formulation). Weird paper structure (e.g., Section 4 is merely a case study of o1.

### Questions
see weakness above

### Soundness
1

### Presentation
1

### Contribution
1

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper explores test-driven development (TDD) tasks, utilizing test cases as both guidance and verification mechanisms for LLM-based code generation. The authors introduce a TDD benchmark specifically designed to evaluate the performance of 18 leading-edge LLM models, with OpenAI’s reasoning models achieving state-of-the-art results. The paper highlights two main contributions: the development of a specialized TDD benchmark for assessing LLMs and the insights derived from this evaluation, notably that instruction following and in-context learning are critical for improving LLM performance on complex TDD tasks.
The review requires several clarifications from the authors. Firstly, the paper indicates the presence of a benchmark comprising 1000 tasks (line 106), yet it lacks a comprehensive statistical analysis and comparison concerning its data sources, including the balance of data distribution and the types of data used. Given the emphasis on this benchmark as a significant contribution, a detailed description of the data statistics, collection processes, and methodologies is essential to assess any potential biases.

The introduction could be clearer, particularly the sections detailing the motivation behind the study. Including a concrete example of the TDD task and its motivations would enhance understanding. It would also be beneficial to concisely summarize the paper's contributions in the introductory section.

The presentation of the tables and figures needs improvement for better clarity. For instance, employing different color fonts or using symbols like boxes to highlight critical code segments in Tables 1, 2, and 3 would aid comprehension, especially for readers unfamiliar with specific coding frameworks such as React. Additionally, it is unclear what the horizontal axis represents in Figure 1.

In the section on evaluation results, the paper should address several aspects to provide a more comprehensive presentation of the findings. These include the rationale behind choosing pass@k as an evaluation metric, whether this metric alone suffices to demonstrate the capabilities of LLMs, the setup for the evaluations, and how these evaluations compare with existing benchmarks.

The term 'incomplete manual examination' mentioned in line 225 is vague. Clarification is needed on how many solutions were manually inspected and whether this sampling is sufficient to support the conclusions drawn.

Lastly, the evaluation results section appears overly verbose. Streamlining this section would make the paper more concise and better aligned with the expectations of a research publication, rather than resembling a lab report.

### Strengths
new benchmark development;
Detailed Experiments;
Relevance to Current Challenges

### Weaknesses
This paper explores test-driven development (TDD) tasks, utilizing test cases as both guidance and verification mechanisms for LLM-based code generation. The authors introduce a TDD benchmark specifically designed to evaluate the performance of 18 leading-edge LLM models, with OpenAI’s reasoning models achieving state-of-the-art results. The paper highlights two main contributions: the development of a specialized TDD benchmark for assessing LLMs and the insights derived from this evaluation, notably that instruction following and in-context learning are critical for improving LLM performance on complex TDD tasks.
The review requires several clarifications from the authors. Firstly, the paper indicates the presence of a benchmark comprising 1000 tasks (line 106), yet it lacks a comprehensive statistical analysis and comparison concerning its data sources, including the balance of data distribution and the types of data used. Given the emphasis on this benchmark as a significant contribution, a detailed description of the data statistics, collection processes, and methodologies is essential to assess any potential biases.

The introduction could be clearer, particularly the sections detailing the motivation behind the study. Including a concrete example of the TDD task and its motivations would enhance understanding. It would also be beneficial to concisely summarize the paper's contributions in the introductory section.

The presentation of the tables and figures needs improvement for better clarity. For instance, employing different color fonts or using symbols like boxes to highlight critical code segments in Tables 1, 2, and 3 would aid comprehension, especially for readers unfamiliar with specific coding frameworks such as React. Additionally, it is unclear what the horizontal axis represents in Figure 1.

In the section on evaluation results, the paper should address several aspects to provide a more comprehensive presentation of the findings. These include the rationale behind choosing pass@k as an evaluation metric, whether this metric alone suffices to demonstrate the capabilities of LLMs, the setup for the evaluations, and how these evaluations compare with existing benchmarks.

The term 'incomplete manual examination' mentioned in line 225 is vague. Clarification is needed on how many solutions were manually inspected and whether this sampling is sufficient to support the conclusions drawn.

Lastly, the evaluation results section appears overly verbose. Streamlining this section would make the paper more concise and better aligned with the expectations of a research publication, rather than resembling a lab report.

### Questions
1. Can you provide more comprehensive details about data statistics, collection processes, and methods to evaluate potential biases in the benchmark?

2. Could you include a concrete example to better explain the TDD task and its motivations? Also, could you summarize the contributions of the paper in the introduction for clearer presentation?

3.  Why was pass@k chosen as the evaluation metric, and do you believe one metric is sufficient to demonstrate the capabilities of LLMs? Could you also detail the evaluation setup and compare it with existing benchmarks?

4. What does "incomplete manual examination" mean?

### Soundness
2

### Presentation
1

### Contribution
2
