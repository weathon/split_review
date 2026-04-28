# DSPy: Compiling Declarative Language Model Calls into State-of-the-Art Pipelines

- Decision: Accept
- Avg Score: 7.33
- Scores: 8, 8, 6

## Abstract
The ML community is rapidly exploring techniques for prompting language models (LMs) and for stacking them into pipelines that solve complex tasks. Unfortunately, existing LM pipelines are typically implemented using hard-coded “prompt templates”, i.e. lengthy strings discovered via trial and error. Toward a more systematic approach for developing and optimizing LM pipelines, we introduce DSPy, a programming model that abstracts LM pipelines as text transformation graphs, or imperative computational graphs where LMs are invoked through declarative modules. DSPy modules are parameterized, meaning they can learn how to apply compositions of prompting, finetuning, augmentation, and reasoning techniques. We design a compiler that will optimize any DSPy pipeline to maximize a given metric, by creating and collecting demonstrations. We conduct two case studies, showing that succinct DSPy programs can express and optimize pipelines that reason about math word problems, tackle multi-hop retrieval, answer complex questions, and control agent loops. Within minutes of compiling, DSPy can automatically produce pipelines that outperform out-of-the-box few-shot prompting as well as expert-created demonstrations for GPT-3.5 and Llama2-13b-chat. On top of that, DSPy programs compiled for relatively small LMs like 770M parameter T5 and Llama2-13b-chat are competitive with many approaches that rely on large and proprietary LMs like GPT-3.5 and on expert-written prompt chains. DSPy is available at https://github.com/stanfordnlp/dspy

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces DSPy, a framework for expressing LM pipelines in a higher level language with support for automatic pipeline optimization. The results demonstrate that 1) complex pipelines can be written quickly and concisely in DSPy and 2) their automatic pipeline optimizations yield substantial gains in performance for two multi-step reasoning tasks (math reasoning and multi-hop QA).

### Strengths
DSPy is a major improvement over manually composing complex LM pipelines by hand. The paper also demonstrates the possibility of automatically optimizing parts of the pipeline once written in the DSPy framework. Finally, the experimental results are very impressive, particularly given the simplicity of user experience.

### Weaknesses
There is a major missing related work [1], which takes a similar approach of expressing LM pipelines as programs, and also comes with built-in optimizations. I would be happy to increase my score if the paper is revised to include a discussion comparing the two approaches.

A more minor concern is that the optimization techniques demonstrated here are relatively limited in scope. From a conceptual standpoint, I would have liked to see more than ensembling or bootstrapping few shot examples.

### Questions
Do the authors have any ideas for future optimization strategies (or "teleprompters") that could be implemented within this framework?

### Soundness
4 excellent

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presents a programming model DSPy that allows defining parameterized LLM-based text transformations. Under this model, multi-step LLM strategies like chain-of-thought, ensembles of chains-of-thoughts, ReAct, and reflection are straightforward to implement. The parameters in these strategies can include the few-shot demonstrations and the specific prompting wording, and DSPy admits using LLM-powered search strategies for optimizing over these strategy parameters. With DSPy, the paper authors demonstrate using a large language model to optimize prompting strategies for use with comparatively smaller language models.

### Strengths
* The paper introduces a novel programming paradigm for defining and optimizing parameterized LLM-based text transformations.
* Though I have not used DSPy myself, my impression is that there is a focus on expressiveness and usability in the programming model, which enhances its usefulness for the ICLR community. One piece of evidence for this expressiveness is the ability showcased to write CoT, reflection, ReAct, and other prompting strategies concisely within the DSPy model. Another is the composibility e.g. of different programs with different optimization (aka "compilation") approaches.
* DSPy reduces the reliance of creating LLM-based text transformations on manual prompting. This can be seen as a strength, reducing the need for expertise in prompt writing. (It can also on some occasions be a weakness if it increases the amount of examples required e.g. from none.)

### Weaknesses
 * My impression is that the value-add of DSPy for any of the listed strategies is somewhat small. E.g. implementing any of CoT, Reflection, or ReAct without DSPy does not require much code. The same is true, I think, for the optimization approaches / compilers. I expect this value-add grows when working with many such strategies at once, and additionally that DSPy provides organizational value both as the programs and compilers grow in complexity, and as the set of people using them grows. Being able to compose different strategies and compiler techniques is also one of the key beneficial properties of the system.
* The evaluations performed do not provide a measure of compute usage or time (both for compilation as well as inference of the compiled programs), which makes comparisons across programs and compilers less meaningful.
* There are no examples of compiled programs provided in the paper or appendices. I think an analysis of compiled programs would benefit the paper meaningfully. In particular, some unanswered questions about the compiled programs include: how do they differ from the types of prompt programs that people write by hand or using other frameworks? how do programs compiled for small LMs differ from those compiled for large LMs? are there any obvious patterns in the compiled programs? how about obvious shortcomings or irregularities, where additional hand-optimization would be easy? any evidence that the optimization techniques overfit to the validation set?

### Questions
# Questions and Suggestions:

Terminology: In the abstract you say DSPy programs are "compiled to" a language model. I think this wording is a bit wrong or misleading, and that it would be better to say the program is "optimized for" or (if you insist on the language of compilation) "compiled for".

The paper has a repeated metaphor with neural network abstractions and deep learning frameworks (Section 1 paragraph 3, and Section 2 paragraph 1, and Section 3.2 paragraph 4). The metaphor rests on two properties of DSPy: its programs are modular and admit optimization. However, the main feature of deep learning systems is that they admit *gradient based* optimization, which is absent from DSPy, weakening the metaphor.

Teleprompters are described as general-purpose optimization strategies, though if I understand correctly they are limited to gradient-free optimization techniques. This detail warrants mentioning.

Strong claim: The paper claims DSPy is the first programming model that translates prompting techniques into parameterized declarative modules that can be optimized. In evaluating this claim, I considered the following relevant works that I thought I would note here.
Dohan 2022 Language Model Cascades https://arxiv.org/abs/2207.10342 also casts several prompting techniques like scratchpads / chain of thought, verifiers, STaR, selection-inference under a unified framework.
Decomposed Prompting: A Modular Approach for Solving Complex Tasks https://arxiv.org/abs/2210.02406 splits tasks into subtasks that are solved a recombined to solve the overall task.
ANPL: Compiling Natural Programs with Interactive Decomposition https://arxiv.org/abs/2305.18498 admits the user performing the decomposition of tasks into subtasks.
Large Language Models as Optimizers https://arxiv.org/abs/2309.03409 like a DSPy compiler produces text-transformation using an LLM to perform prompt optimization.
Among these, Dohan 2022 is closest to the claim made in the paper.

-- In your treatment of Predict, I don't think the inclusion of the "None" implementation detail aids the discussion.

In the list of parameters (Section 3.2, paragraph 3), field descriptions are omitted. 
How do you think about safety during SQL generation, since SQL queries can modify or delete tables. How do you approach using tools with side effects during compilation?
In the RAG example at the end of Section 3.2, is it complete without a definition of Retrieve provided?
How can a DSPy user introduce a new Retrieve implementation?

In my view, one of the key results is that expensive LLMs can be used during the optimization process of a prompt pipeline targeting smaller LMs. I will copy here the text from the "weaknesses section" above pertaining to this point: There are no examples of compiled programs provided in the paper or appendices. I think an analysis of compiled programs would benefit the paper meaningfully. In particular, some unanswered questions about the compiled programs include: how do they differ from the types of prompt programs that people write by hand or using other frameworks? how do programs compiled for small LMs differ from those compiled for large LMs? are there any obvious patterns in the compiled programs? how about obvious shortcomings or irregularities, where additional hand-optimization would be easy? any evidence that the optimization techniques overfit to the validation set?

Regarding how the compiled programs differ when targeting smaller LMs, a qualitative investigation with examples would be welcome.

In Table 1, reporting some measure of compute usage or time both for compilation and inference would be valuable, and would make the various strategies (both programs and compilation approaches) more readily comparable.

Note: MultiChainComparison implementation is not provided.
Note: Do the compilation approaches account for overfitting the validation set?

Another idea for further study: Can you compile a DSPy program for a small LM and then run that program using a more powerful LLM different from the one targeted during compilation in order to save on compilation costs? What sort of performance degradation does this incur?

I also include here some typographic issues I identified in the paper. These did not meaningfully hinder readability of the work.

Typo: GMS08K -> GSM8K (page 2, paragraph 4)
Typo: format -> formats (page 4, Section 3.2)
Typo: grammar: but -> or (page 5, Section 3.3)
Typo: "As we assumes" in the example at the end of Section 3.3
Typo: these -> this, ensembles -> ensembling (page 6, stage 3)
Typo: "specific math problems or particular LM." -> "specific to math problems or a particular LM." (page 7)

### Soundness
3 good

### Presentation
3 good

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
This paper introduces DSPy, an LM pipeline framework consisting of a programming model and compiler. The programming model provides composable and declarative modules for LM instruction. These modules function similarly to function calls, allowing users to define input/output behavior using natural language signatures. The compiler is capable of generating high-quality prompts automatically or fine-tuning LMs using a general optimization strategy (teleprompter). Through evaluations on GSM8K and HotpotQA, the authors demonstrate DSPy's ability to reduce the required number of handwritten prompt templates.

### Strengths
1. Novel Approach. This paper introduces a novel approach to systematically build LM pipelines and compile modules into a set of prompts (or fine-tunes) optimized for specific tasks. The approach is promising, showcasing its ability to reduce the human effort required to develop prompt pipelines. 
2. Well-Written. The paper is clearly written and presents the core concepts of DSPy in a straightforward manner.

### Weaknesses
1. Lack of details: DSPy stands out from other frameworks, like LangChain, due to its capacity for automatic prompt generation and optimization. However, the introduction of the DSPy Compiler lacks sufficient specificity. It would be beneficial to provide more comprehensive details on how DSPy generates candidate values for module parameters (instructions, field description, and example input/output) based on signatures. Specifically, the paper does not detail the mechanisms for how the compiler explores the space of possible instructions or how it generates diverse examples for few-shot learning. The process of creating these candidate values is critical to the success of the optimization, and the paper should elaborate on the algorithms used for this process.


### Questions
## Approach:
1. Can we easily implement common and advanced prompting techniques with signatures? I noticed that the signatures used in the Case Study are quite simple. When it comes to dealing with complex user intentions, do you think additional hand-written comments are necessary alongside signatures? For instance, in the ChainOfThought module, I found that the prompt "Let's think step by step" still requires handwriting within the module. How many prompts would need to be handwritten to achieve functional equivalence with a complex prompt (such as Appendix D prompt 6) using signatures?
2. How can users debug their DSPy programs effectively? In Section 4 of the paper, it is mentioned that "A well-decomposed program can typically find at least a few training examples..." I suppose that the success of optimization depends on a well-structured decomposition by the user, which implies the need for frequent modification of DSPy programs. Consequently, it raises the question of how users can determine which modules are not functioning correctly. Is it necessary for users to repeatedly rewrite the entire DSPy program?
3. How much does the optimization cost in terms of computing resources or API usage? (This question may exceed the paper's scope) 
## Evaluation
1. In section 5, Hypothesis 2, the paper mentions the possibility of DSPy outperforming expert-written prompts. However, is there an evaluation comparing DSPy with handwritten prompts to support this claim?
2. In Section 5 of the paper, it states, "... ‘how they compare on GSM8K with program P when compiled with strategy S’, which is a well-defined and reproducible run.” How can the reproducibility of these results be ensured?
3. In Case Study 1 using the GSM8K dataset, GPT-3.5 with 5 few shots achieves a score of 57%, while vanilla+GPT-3.5+fewshot only scores 33.1%. What factors contribute to the decline in performance, considering the similarity between these two approaches?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good
