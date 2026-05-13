# RepoGraph: Enhancing AI Software Engineering with Repository-level Code Graph

- Decision: Accept
- Scores: 6, 6, 6, 8, 5

## Abstract
Large Language Models (LLMs) excel in code generation yet struggle with modern AI software engineering tasks. 
Unlike traditional function-level or file-level coding tasks, AI software engineering requires not only basic coding proficiency but also advanced skills in managing and interacting with code repositories.
However, existing methods often overlook the need for repository-level code understanding, which is crucial for accurately grasping the broader context and developing effective solutions.
On this basis, we present \repograph, a plug-in module that manages a repository-level structure for modern AI software engineering solutions. \repograph offers the desired guidance and serves as a repository-wide navigation for AI software engineers. 
We evaluate \repograph on the SWE-bench by plugging it into four different methods of two lines of approaches, where \repograph substantially boosts the performance of all systems, leading to \textit{a new state-of-the-art} among open-source frameworks.
Our analyses also demonstrate the extensibility and flexibility of \repograph by testing on another repo-level coding benchmark, CrossCodeEval.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes RepoGraph, a plug-in module designed to extract repository-level definition and invocation information, offering graphical navigation to improve AI software engineering. RepoGraph is compatible with popular agent-based and procedural based LLM frameworks. The authors conduct experiments with GPT-4 and GPT-4o on SWE-bench, yielding a promising result.

### Strengths
- RepoGraph can be easily built and integrated into existing methods and its construction process is straightforward and well-defined.
  
- The analysis presented in this paper is clear and detailed. The authors offering several key observations and insightful explanations, which could be inspiring for future research and broader adoption.
  
- The author conducted additional transferibility experiments to better explain the effectiveness of RepoGraph.
  
- The authors give comparative analysis between procedural and agent-based methods.
  
- A thorough classification analysis of error cases is provided, with specific examples for each category.

### Weaknesses
 - The primary experimental results are presented solely on SWE-bench-Lite, and the improvement in accuracy resolution are not particularly significant. Additionally, the paper mainly focuses on the resolved numbers and accuracy as evaluation criterion. In cases with a limited number of passes, the quantitative comparison and analysis is not convincing enough and may exhibit considerable variance. It would be beneficial for the authors to provide a thorough analysis of both pass and fail cases, as examining failed cases could also highlight improvements in error localization and correction capability of RepoGraph.

- As the authors note, the paper only evaluates based on GPT-4 and GPT-4o. Given the increasing availability of various General LLMs and Code LLMs, such as Claude and other open-source models, it would be better for the authors to include results from these additional LLMs. Previous studies indicate that different LLMs have varying performance when applied to new methods or tasks. It would be valuable to see how RepoGraph performs across a broader range of LLMs.

- A presentation issue in Figure 10: some numbers overlap, and certain white numbers blend into the background.

### Questions
The authors state that in the error analysis 'when integrated with REPOGRAPH, the proportion of error types “incorrect localization” and “contextual misalignment” largely decreases'. However, this conclusion appears limited in significance due to the small number of passed samples involved. Could the authors provide further clarification on how this conclusion was reached? Have the authors considered the implications of having too few passed samples in their analysis?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper presents an approach to navigating software repos and
offer the desired navigation by incorporating
information at the line level, file level, and repository level. Toward that end, the authors
proposed a graph-learning-based framework with nodes corresponding to code-line level and edges corresponding
to connections of the nodes at the repo level.

### Strengths
- A plug-in-based framework to easily integrate with other AI-based tools
- Code and docker provided for reproducibility

### Weaknesses
 - No human evolution studies
- Missing prior relevant literature

The authors could verify their assessment on SWE-bench Verified, released as a part of the benchmark.

Although the proposed work seems promising, the article lacks relevant literature citations. How to navigate the software repository has been studied by software engineering researchers before the LLM era. The
approaches include the navigation behavior of developers using eye-tracking data, during code summarization tasks.
I encourage the authors to consult the works of Bonita Sharif and follow the references.

### Questions
According to Figure 3, RepGraph was not able to find all error cases when added as a plug-in with Agentless and SWE-Agent. 
As RepoGrpah works at line-level, file-level, and repo-level and was added as a plug-in, I expected RepoGrapgh to cover all error cases of Agentless and SWE-Agent.
Do the authors have any intuition or hypothesis of the observation of Figure 3?

### Soundness
3

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
4

### Summary
This paper introduces RepoGraph, a plug-in designed to enhance the capabilities of LLMs in understanding and navigating code repositories. RepoGraph constructs a graph-based representation of the entire codebase using abstract syntax tree parsing. The system is evaluated using the SWE-bench Lite and CrossCodeEval benchmarks, demonstrating its effectiveness in issue resolution and fault localization. The authors also conduct various analyses, including complementarity and failure cause analysis.

### Strengths
1. Originality: RepoGraph introduces a novel approach by leveraging repository-level graph-based representations, which provides a more comprehensive understanding of the codebase. 

2. Quality: The paper is well-written, with a clear explanation of how RepoGraph work. It provides a robust experimental setup that evaluates the tool's performance across multiple dimensions. 

3. Clarity: The distinctions between RepoGraph and other repository understanding techniques are clearly articulated, making it easy to understand the motivation and design of the tool. 

4. Significance: Its contributions could lead to improvements in the effectiveness of automated issue resolution and code navigation tools.

### Weaknesses
1. Performance Gains: While RepoGraph shows some improvement in issue resolution and fault localization, the gains are relatively small.

2. Cost Assessment: The paper does not adequately address the potential computational costs associated with graph construction and search operations. A thorough analysis of these costs, including time overhead, would strengthen the paper by providing a better understanding of RepoGraph’s practical feasibility.

3. Reproducibility: The open-source code provided in the repository is not entirely reproducible based on the available documentation. Specific issues include: 

	(1) Environment Setup: The steps for setting up the execution environment are incomplete. It is unclear whether specific configurations or environments are needed for the tool to function properly. 

	(2) Configuration: The LLMs require additional keys for configuration, but the paper lacks guidance on how to set these up.

	(3) Evaluation Steps: There is no clear documentation on how to evaluate the generated results effectively. Detailed instructions on the 	evaluation process would help ensure that users can reproduce the experimental findings.

### Questions
- Can the authors provide more information about the computational overhead involved in constructing and using the repository-level graphs? Specifically, how does the time complexity compare to other methods?

- Given the small performance improvements, could the authors discuss potential areas for further optimization or enhancement of RepoGraph that could lead to more significant gains?

- Could the authors offer guidance on the reproducibility, specifically:

    - What are the exact environment requirements for running the tool?
    - How should the necessary keys for LLM configuration be set up?
    - What steps should users follow to accurately evaluate the results generated by RepoGraph?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper introduces a framework called *RepoGraph* for fine-grained modeling of code repositories to address the current challenges in repository-level code tasks. *RepoGraph* leverages tree-sitter to model code repositories at the level of code behavior, constructing a code structure graph based on the invocation and dependency relationships between functions and classes. By using this graph, *RepoGraph* provides more accurate code context for given retrieval terms, thereby improving the accuracy of code task completion. The authors tested *RepoGraph* on the **SWE-bench** benchmark, demonstrating that it can be seamlessly integrated with both advanced agent-based and non-agent frameworks, significantly enhancing the accuracy of issue-fixing tasks. Furthermore, they tested it on the **CrossCodeEval** benchmark, verifying that *RepoGraph* can also be applied to repository-level code completion tasks.

### Strengths
1.	Conducting high-quality, fine-grained modeling of code repositories is extremely challenging due to the numerous corner cases that need to be considered. Implementing such a detailed model for code repositories is no easy task, and I truly appreciate the authors’ efforts.
2.	*RepoGraph* can be seamlessly integrated with both agent-based and non-agent frameworks, significantly improving the ability to fix issues on the **SWE-bench**. This will be highly beneficial for future agent-driven code development.
3.	*RepoGraph* can also be applied to repository-level code completion tasks, which will be very useful for code completion in daily development.
4.	The authors conducted extensive experiments to validate the effectiveness of *RepoGraph*.
5.	Compared to other papers I have reviewed, this paper is well-written, with a clear structure and a balanced level of detail.

### Weaknesses
This paper is well-written and does not have any major weaknesses, but there are a few minor typos:

•	`Line 228`: There is a repetition of `such as`.

•	`Line 306`: The sentence `To assess the patch application rate, we attempt to apply the generated patches to the repository using the patch program; successful applications contribute to this metric.` has a somewhat disjointed structure and logic. The semicolon is typically used to connect two independent but related clauses, but in this case, the first part of the sentence is not a complete clause, even though there is a logical connection between the two parts.

### Questions
1.	Although the authors mentioned that due to resource limitations, only 500 samples were used for experiments on **CrossCodeEval**, the cost of conducting a full test on **CrossCodeEval** does not seem to be significantly higher compared to testing on **SWE-Bench**. This is because the cross-file context retrieved should not be very long. Could the authors report the costs of each test?
2.	While GPT-4o is also capable of code completion, **CrossCodeEval** primarily evaluates the completion abilities of base code models. Could the authors include results from some open-source code models, such as `Deepseek-Coder-V2` and `Qwen2.5-Coder`? These models should be relatively easy to run locally for inference.

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The authors introduce RepoGraph, a new tool that turns a codebase into a graph structure. The authors demonstrate how this tool, which can be integrated into both agent-ic and procedural AI software engineering frameworks, leads to improvements across the board for existing methods. The repository is constructed by filtering out unnecessary file types and repository-dependent code, identifying object oriented programmatic entities, and constructing the remaining pieces of the codebase into a graph. The experimental setup follows existing work. The authors demonstrate improvements for a number of existing AI SWE solutions when RepoGraph is integrated into them and perform some analyses around RepoGraph parameters, localization statistics, and transferability.

### Strengths
RepoGraph examines the question of how codebases can be represented effectively. While other works have tried more traditional approaches for localization, such as retrieval and tool-augmented LMs, RepoGraph demonstrates that reshaping the codebase into a graph that is more traversable and useful for a language model can elicit stronger performance on the downstream editing subtask. The authors discuss a pipeline for carrying this out with Python codebases, showing how simple heuristics for removing noise and preprocessing the codebase in a more friendly way can lead to improvements that are method-agnostic. 

- [Section 3.1, Step 2] - This step seems quite interesting and novel. I think a visualization, something similar to Figure 2 but a bit more grounded in Step 3’s construction, might be helpful for readers to understand this construction more easily.

### Weaknesses
 - Figures 1, 2 - I appreciate the effort that went into these figures, they are clearly drawn quite thoroughly. However, I think it is a bit too complex, making it hard to understand. I’d recommend simplifying the diagrams to make the takeaways a bit more obvious. For example, it took me a while to understand the meaning of the colors in Figure 2, (a).
- The design of RepoGraph seems to be written in a fairly Python-centric manner. This is understandable to some degree, as the main evaluation (SWE-bench) is for Python based repositories. However, the contribution would be more impactful if somehow it was demonstrated that this approach scales to other kinds of codebases (with existing work or a new benchmark?). In Section 5.3, the authors mention how for CrossCodeEval, the evaluation is limited to Python. The authors discuss this in the appendix, but I think the generalizability of RepoGraph is a question that should be answered instead of being deferred to future work. The reliance on Python-specific AST parsing and library introspection techniques raises concerns about the practical effort required to adapt RepoGraph to languages with different syntax and module systems. The paper does not adequately address the challenges of extending the 'project-dependent relation filtering' step to other languages, which would likely require significant manual effort and language-specific expertise.
- [Section 3.1, Step 2] - “We maintain a comprehensive list of methods” ⇒ This sounds like it’s hard-coded for Python. Would I have to manually re-perform this filtering for other languages? Is there an automatic filtering criteria I can apply to come up with a comparable list for another language? The paper does not discuss how this list is generated or maintained, and it is unclear if this process can be automated or generalized to other languages. The reliance on Python-specific library introspection techniques (e.g., `sys.builtin_module_names`, `pkgutil`) further limits the applicability of RepoGraph to other languages.
- [Section 5.2, Line 361] - This claim seems somewhat handwavy to me. The cost metric seems to go up with every method due to the inclusion of RepoGraph. However, this takeaway seems to suggest that the performance increase is proportional or lower than the increased cost - why is this true? What numbers are being compared for this proportion? (e.g. 2.66% increase vs. 0.04 cost increase? Why is this lower?) The paper lacks a clear explanation of how the cost metric is calculated and how it relates to the performance improvements. The claim that the performance increase is proportional or lower than the increased cost is not supported by concrete data or analysis. It's unclear what specific numbers are being compared to make this claim, and the lack of transparency makes it difficult to assess the validity of this conclusion.
- [Section 5.1, Lines 413 - 420] - The discussion on the differences between procedural and agentic approaches is interesting, but I think it’s not quite clear to me why this discussion is included or how it relates to RepoGraph. Is the suggestion that procedural approaches take more advantage of RepoGraph?

### Questions
- [Introduction, Line 75] - “they tend to focus narrowly on specific files, resulting in local optimums”. I’m not sure what this means? Why do agent approaches have this tendency?
- [Intro, Line 85] - What is an “ego-graph”? I see the citation in Line 256, but may be good to define this explicitly as a preliminary somewhere earlier.
- [Section 3.1, Line 205] - how is “non-essential” determined? I could imagine that editing requirements.txt might be necessary to import a new library for carrying out a fix.
- [Section 3.1, Line 216] - What happens in step 1 if the codebase is not written in an object oriented manner? For instance, what if you’re dealing with JavaScript code primarily written in a functional programming style, which may not have classes? Or if you are editing a bash script which may not have these entities?
- [Section 3.2, Line 267] - What is an “edition” stage? Perhaps this is a type? (“Editing”?) Repeated again on Line 350
- [Table 2] - What is # samples?
- [Table 4] - The number of nodes is a bit confusing. In SWE-bench, each codebase has an average of 438k lines. If each node corresponds to a line, why are there only 1419 nodes on average?
- [Figure 3] - Is this for SWE-bench Lite? Or CrossCodeEval?

### Soundness
2

### Presentation
3

### Contribution
3
