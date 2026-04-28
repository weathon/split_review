# CursorCore: Assist Programming through Aligning Anything

- Decision: Reject
- Avg Score: 6.00
- Scores: 8, 5, 6, 5

## Abstract
Large language models have been successfully applied to programming assistance tasks, such as code completion, code insertion, and instructional code editing. However, these applications remain insufficiently automated and struggle to effectively integrate various types of information during the programming process, including coding history, current code, and user instructions. In this work, we propose a new conversational framework that comprehensively integrates these information sources, collect data to train our models and evaluate their performance. Firstly, to thoroughly evaluate how well models align with different types of information and the quality of their outputs, we introduce a new benchmark, \benchname (Assist Programming Eval), to comprehensively assess the performance of models in programming assistance tasks. Then, for data collection, we develop a data generation pipeline, \pipelinename, which synthesizes training data from diverse sources, such as GitHub and online judge platforms. This pipeline can automatically generate various types of messages throughout the programming process. Finally, using this pipeline, we generate 219K samples, fine-tune multiple models, and develop the \modelname series. We show that \modelname outperforms other models of comparable size. This framework unifies applications such as inline chat and automated editing, contributes to the advancement of coding assistants.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper proposes:
(1) the Assistant-Conversation Framework. This combines multiple components like System (priming to the tasks), History (past edits and changes made in code), Current (The current code being processed), User (instructions for the task) and Assistant (the responses from the model).
(2) APEval: A benchmark for holistic programming assistant evaluation.
(3) CursorCore: A model for assisted programming tasks.

### Strengths
- Current agents lack history information and are very specific to the current context which is the key challenge this paper tries to solve.
- Real user scenarios are a more complex framework of interactions similar to the one proposed.
- The benchmark created evaluates information use from different context sources.

### Weaknesses
 - The improvements with using CursorCode is not clear from the performance differential.
- The conversational framework needs to be motivated better as its hard to understand why this system was chosen. Also, the paper tries to cover a lot of things which makes it hard to focus on the core problem.

### Questions
Formatting:
- Caption for figure 2 can be improved.
- Table 1 caption should explain the data.
- Figure 7 and 8 are hard to parse.

Writing:
Related works should talk about other tasks in AI for code that look at the history of changes like OverWatch.

### Soundness
4

### Presentation
3

### Contribution
4

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper presents CursorCore, an AI-powered programming assistant that improves programming support by utilizing multiple sources of information, including code change history, current code and user intention, throughout the coding process. CursorCore introduces a new framework, Assistant-Conversation, and establishes a benchmark, APEval, to assess its effectiveness. The work also develops the Programming-Instruct pipeline for training data synthesis. Evaluation results in HumanEval benchmark shows the effectiveness of CursorCore.

### Strengths
- The paper addresses a critical limitation of current code benchmarks by focusing on continuous code editing, aligning its benchmarks more closely with real-world development scenarios.
- The paper introduces Programming-Instruct, a data synthesis pipeline that generates a substantial dataset of 219K samples from sources like GitHub. Experimental results demonstrate that this dataset effectively supports supervised fine-tuning, making it a valuable resource for training code assistance models.
- The description of the Assistant-Conversation framework is clear and comprehensive.

### Weaknesses
 - The paper addresses a critical limitation of current code benchmarks by focusing on continuous code editing, aligning its benchmarks more closely with real-world development scenarios.
- The paper introduces Programming-Instruct, a data synthesis pipeline that generates a substantial dataset of 219K samples from sources like GitHub. Experimental results demonstrate that this dataset effectively supports supervised fine-tuning, making it a valuable resource for training code assistance models.
- The description of the Assistant-Conversation framework is clear and comprehensive.

- The paper divides the HumanEval benchmark into four settings, each with 41 examples, which limits direct comparison across these settings. This approach uses different data for each setting, making it difficult to assess their relative effectiveness. For instance, settings with code history (H) might not be particularly relevant for a task like HumanEval’s code generation, raising questions about its utility in this context. The lack of a consistent test set across all settings makes it impossible to determine if the observed performance differences are due to the model or the specific test data used in each setting. This significantly hinders the ability to draw meaningful conclusions about the impact of different input modalities.
- The evaluation relies heavily on code generation tasks, which may not fully capture the utility of incorporating code change history information (H) as input. In Table 4, the setting with H seems perform worse than without H. Expanding to additional tasks beyond code generation, such as code refactoring, bug fixing, or code completion within a larger context, could better assess the contribution of code history information and more accurately reflect the value of the proposed framework across a broader range of code assistant applications. The current evaluation does not explore the potential benefits of historical information in these scenarios, limiting the scope of the conclusions.
- The experimental results analysis is insufficient. In Table 4’s 6B+ model comparison, CursorCore underperforms relative to its base models in specific settings, such as DS-Coder’s C+U, Yi-Coder’s C, and Qwen-Coder’s H+C and C+U settings. This raises questions about the factors driving these inconsistencies, suggesting that the paper’s analysis of model performance across settings could be more thorough to address the causes of these variances. The paper does not provide a detailed analysis of why the fine-tuned model sometimes performs worse than the base models, which is a critical point that needs further investigation. The lack of analysis makes it difficult to understand the limitations of the proposed approach and how to improve it.

### Questions
- How do you determine the appropriate timing for recording code changes? In real-world scenarios, code changes are often continuous; for example, a modification to a single code block may consist of multiple edits across different lines, and each line may undergo multiple token-level edits. How are boundaries between different history records (H1, H2, etc.) defined?
- How does the framework address the issue of long inputs? With a large number of code changes, the input text can become very lengthy. What strategies are used to manage or reduce input length while preserving relevant information?
- How is the code change history constructed for APEval during manual annotation? Given that HumanEval’s inputs are only function declarations, how do annotators simulate the evolution of a function declaration through code changes to build realistic histories?

### Soundness
3

### Presentation
3

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
This paper presents a dataset synthesis pipeline to generate mixed style programming data to support in-context code generation task. The paper considers a mixture of history steps, current context, user instruction for generation code completion together with rationale as the task. To collect training and evaluation dataset, the authors consider (1) use LLM to generate intermediate steps from an initial program, (2) collect from github commits, and (3) collect coding platform submits. A random mixture approach is taken to generate tasks, with LLM as a judge to compare consistency. 

The authors present three models trained on this dataset (with mixture from all sources), and CursorCore models show impressive improvement over baseline models of similar size.

### Strengths
This paper's main contribution is the dataset synthesis approach, that leverages AIprogrammer to generate code edit histories from seed code snippets. Then, together with the mixture strategy, APEval includes a diverse set of insertion, editing, generation tasks. Given that fine-grained coding history data can be difficult to obtain, this synthetic approach is great for this task.

The dataset selection process also highlights the benefit of mixing datasets with both chat data and synthetic data. It seems like the gain from github and online coding platform is minimal, which potentially requires additional analysis.

### Weaknesses
There are two weakness of the paper:

1. As a benchmark paper, this paper doesn't provide a very convincing evaluation dataset. The authors should provide analysis of the evaluation dataset, justifying (1) why the evaluation set reflects practical editing needs (since AIprogrammer generated data may not completely align with typical programming styles), (2) how does the evaluation set ensures high accuracy, especially with respect to the contextual information (as the authors filtered with the AI judge).

2. The paper doesn't make clear comparison with dataset curated from github/coding submits and synthetic data, despite dataset selection section clearly show that git-commit and online submit made minimal contribution on top of AIProgrammer + Evol-instruct. I suggest the authors provide some insights about their difference qualitatively (e.g., how does the editing styles different among them). If possible, maybe perform cross-evaluation between models trained on these subsets (e.g., train on AIProgrammer, but eval on git data / then train on git data and eval on AIProgrammer data). This might highlight and justify how these datasets should be mixed together.

### Questions
As mentioned above, the authors should:
(1) elaborate why eval dataset is convincing, and should be used by future model developers for the general coding assistant benchmark.
(2) compare in detail about data from three sources.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper presents (1) a new conversational framework called Assistant-Conversation aimed at simplifying the programming process.  The paper also presents (2) a benchmark set for assisted programming, namely APEval, which has 164 benchmarks that are hand-curated starting with HumanEval and adding some or all of the "history", "code", and "user" components.  Since generating APEval like benchmarks is time consuming manual process, the paper also presents (3) a method, Programming-Instruct, to automate data collection.  Finally, the dataset is used (4) to fine-tune LLMs and get CursorCore models.

Assistant-Conversation framework: The framework consists of the elements system (S), history (H), current snapshot of code (C), user query (U) and assistant response (A).  The paper observes that current models have limitations in dealing with these 5 pieces.  This point about history (H) not being incorporated in prediction has been made previously in many papers in software engineering conferences; see, for example, see the FSE 2023 paper titled "Grace: Language models meet code edits."

APEval: APEval is an extension of HumanEval generated by asking programmers with varying levels of experience to annotate HumanEval by interacting with an LLM. The paper identifies four categories of benchmarks, where we either have H,C,U or just H,C, or just C, U or just C. Benchmarks for each category are generated by humans starting from HumanEval benchmarks.  There are a total of 164 benchmarks in APEval, 41 of each category, where history (H) ranges from 21-139 lines, code (C) ranges from 8-31 lines, and user query (U) ranges from 3-19 lines (Table 1).  The benchmark set could be useful contribution, but there is no mention of releasing the benchmark set in the paper.

Programming-Instruct: The idea here is to get a history of code snapshots generated in the process of solving a programming task. This history could come from an LLM, or Git commits, or online submissions of (partial or incorrect) solutions of programming tasks. The data is processed and categorized into HCU, HC, CU or C buckets. The user query U is LLM generated.

Cursor-Core: The data generated in (3) above is used to fine-tune Deepseek-Coder, Yi-Coder AI and Qwen2.5-Coder of different sizes. The benchmarks in (2) are used to evaluate.

The evaluation results show that the fine-tuned model perform better than the base models, and other models in that (size) category. The fine-tuned CursorCore models all perform worse than GPT-4o.

### Strengths
+ The paper describes a fairly extensive effort that includes benchmark generation using human annotations,
automated data generation, and fine tuning. 

+ Evaluation across several models, including several open-source models, across sizes

### Weaknesses
 - While the effort is impressive, the take-home message remains unclear. The paper starts by emphasizing the need for history (H) -- but inclusion of H almost always leads to worse performance (going from C to HC or going from CU to HCU) -- in fact, that is also true for GPT-4o, which is evidence contrary to the thesis of the paper. The code (C) and user interaction (U) part is already part of most LLM-based programming assistants. 

- The abstract also emphasizes conversational framework, but I did not find any conversational interactions here, just the history of the code.

- The presentation is poor because the paper tries to pack too much information in the limited space.

### Questions
1. what is the conversational bit in the Assistant-Conversation framework?

2. Lines 288-293 discuss the process of discarding some segments that are not aligned with "user's purpose" -- is there any check in place to ensure that this step does not throws away some important segments? How do you decide if something is aligned with user's purpose when you may not even have the user query (U)?

3. Line 340-343 mention "randomly utilize two powerful open-source LLMs" -- utilize for what?

4. Line 295-296 mention things that are mentioned only there in the main part of the paper. What are the learnings from that part of the paper? Is there a conclusion to be drawn, and if so, then it should be in the main paper, and if not, then adding 2 sentences with a pointer to the Appendix is not very helpful.

### Soundness
3

### Presentation
2

### Contribution
2
