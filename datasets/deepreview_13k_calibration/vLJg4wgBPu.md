# GPT Is Becoming a Turing Machine: Here Are Some Ways to Program It

- Decision: Reject
- Avg Score: 4.25
- Scores: 3, 5, 3, 6

## Abstract
We demonstrate that, through appropriate prompting, GPT-3 family of models can be triggered to perform iterative behaviours necessary to execute (rather than just write or recall) programs that involve loops, including several popular algorithms found in computer science curricula or  software developer interviews.  We trigger execution and description of {\bf iterations} by {\bf regimenting self-attention} (IRSA)  in one (or a combination) of three ways: 1) Using strong repetitive structure in an example of an execution path of a target program for one particular input, 2) Prompting with fragments of execution paths, and 3) Explicitly forbidding (skipping) self-attention to parts of the generated text. On a dynamic program execution, IRSA leads to larger accuracy gains than replacing the model with the much more powerful GPT-4. IRSA has promising applications in education, as the prompts and responses resemble student assignments in data structures and algorithms classes. Our findings hold implications for evaluating LLMs, which typically target the in-context learning: We show that prompts that may not even cover one full task example can trigger algorithmic behaviour, allowing solving problems previously thought of as hard for LLMs, such as logical puzzles. Consequently, prompt design plays an even more critical role in LLM performance than previously recognized.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes a highly structured prompting technique, IRSA, to trigger iterative (multi-step) logic execution in LLMs. The main contributions of the paper are algorithmic and empirical with some exploration of the implications to models of computation. In particular, the paper demonstrates that highly-structured prompts can be used to trigger LLMs to correctly simulate a "trace" (internal state, looping) of classical iterative algorithms (e.g., sorting). Experiments evaluating GPT's ability to simulate the execution of such algorithms shows that it does better on these computational tasks using IRSA prompts compared with less structured prompts.

### Strengths
+ The paper explores an important question of broad interest to the community. The exact capabilities and limits of LLMs remain unclear. This work shows that highly structured prompts can be used to better control LLM output on tasks requiring precise state control (memory) and iterative execution (loops).

+ The proposed prompts (IRSA) are intuitively clear. They seem novel, to my knowledge.

+ The experiments demonstrate that the IRSA prompts do indeed help the LLM correctly simulate algorithms requiring loops over the distribution of inputs considered. There is a good amount of detail included in the main paper and appendices.

### Weaknesses
- The use of a trace in the prompt raises a few questions, which are not addressed. A classic sorting algorithm can correctly sort very long lists using a relatively short specification of the algorithm. Can IRSA do the same (sort long input lists with a short trace)? The experiments seem restricted to short inputs length 5 in sorting, for example). The scaling, generalization and robustness of the IRSA prompt to different inputs aren't well explored in the paper. Specifically, the paper does not explore how the length of the input list impacts the performance of the IRSA prompt. It is unclear if the model can maintain the correct state and iterative execution for significantly larger inputs or if the performance degrades as the input size increases. The paper should provide a more detailed analysis of how the length of the input affects the correctness and efficiency of the approach.

- The paper could better highlight its algorithmic and empirical contributions relative to a rapidly growing body of literature on how to improve a LLM's instruction-following abilities. At the moment, I'm not sure if the experiments conclusively demonstrate that IRSA improves the instruction-following (via algorithm execution) abilities of a LLM. The paper should more clearly differentiate the proposed approach from existing methods for improving instruction following, and provide a more in-depth analysis of the specific advantages of IRSA in the context of algorithmic execution. It is not clear if the gains are due to the specific structure of IRSA or if similar gains could be achieved with other structured prompting techniques.

- The terminology used can sometimes be a bit loose. For example, "this strategy hardens the attention", "skipping unnecessary attention saves computation", etc. More formal descriptions of these important ideas would increase the technical rigor of the paper. Alternatively, the paper could simplify the description to emphasize the empirical aspects (i.e., prompt engineering), which are also valuable. The paper should provide more precise definitions of terms like "hardens the attention" and "skipping unnecessary attention" or clarify that these are informal descriptions. The lack of formal definitions makes it difficult to understand the underlying mechanisms and limits the generalizability of the findings.

### Questions
- How well do the proposed prompts do on significantly larger inputs? How does performance (esp correctness) vary with input size?

- How does the performance of the approach change if the LLM **hasn't** seen traces of the algorithms in its training data or not? For example, it seems plausible that traces of sorting and classical algorithmis might appear in training data. Does IRSA work if the trace is "new" to the LLM? Might synthetic tasks be needed here to eliminate this threat to validity?

- I was able to verify that GPT-4 correctly outputs a trace for the example shown in Prompt 1. However, the same prompt on a slightly larger input produces a correct answer but starts to include comments like one might see in code. Is this expected?

```
<original Prompt 1>
Problem: 0, 3, 3, 1, 2, 10, 98, 2000, 1232, 454422, 001, -222, 4533, 24, 99
EXECUTION
```

starts to produce comments like these

```
    // The iterations continue until no swaps are made in an entire iteration.

    Iteration:
       set swap_flag=false. 
       // Comparisons occur here for all pairs.
       // ...

       // After several iterations, the list is eventually sorted.
       // No swaps occurred so, swap_flag=false
```

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The proposed method essentially gives a full stack trace of a programmatic execution on a problem as a prompt to the LLM, and ask the LLM to solve a task by imitating the content of the stack trace. Thus, the LLM can copy the overall structure of the trace, retaining the rigid programmatic execution, while making the appropriate substitutions when the values change. The stack trace includes the "source code", so that the state changes are paired with the appropriate reasoning steps on why the state needs to be changed in that fashion.

### Strengths
## potentially significant

This paper outlines several good prompting strategies, which are useful if you want to have the LLM to reason programmatically, with a rigid syntactic structure in its execution trace. The paper explains each strategy, irsa, skip attention, fragmented prompting with examples, and show the proposed prompts can achieve better results paired with a weaker model (gpt3.5) than a naive prompt with a more advanced model (gpt4)

The analogy of GPT as a turing machine is good too.

### Weaknesses
## poor quality and clarity

It is unclear if the proposed method can be reliably replicated to other domains, given that it is only evaluated on a handful of problems. I believe this work can be made substantially better if an automated method could be derived turning an existing complex program into a prompt, and evaluated on a larger set of problems, rather than the simplistic 100 python arithmetic problems.

## less than ideal novelty
It is also unclear how the proposed method is significantly different from Nye (2021)'s work on scratchpad, as both leverages trace information extensively. It would be good to have a related work section to spell out the exact differences.

The paper note that the proposed technique may be beneficial in the education domain. However, wouldn't having a LLM to simply mark up an existing execution trade of actually running the program be a better (and more correct) alternative?

### Questions
A program's execution can often have extraordinarily long traces, is the proposed method capable of handling this explosion of trace size, especially language models have a limited context window size? How would the proposed technique handle more complex program executions, which invariably have a long trace that would be infeasible to "print out" as sequences of tokens for an auto-regressive model?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work proposes IRSA (iterations by regimenting self-attention) for the use of GPT3 model to execute programs that have loops. Its core idea is using an example input and its execution path for constructing highly structured prompts. It further explores combining multiple fragments of execution paths, instead of a prompt that covers entire execution path of any single example. It then skips parts of generated text when performing self-attention for more efficient token use. GPT3+IRSA outperforms GPT4 for executing the programs given the evaluated programs.

### Strengths
This is an interesting work. 
The proposed approach seems to work given the evaluated programs.

### Weaknesses
The proposed work may point out an interesting direction for using LLMs to execute programs, but its current form and results are premature and it’s not ready to be published. 

The presentation of IRSA has been majorly illustrated by examples. While such examples are useful, there still lacks a formulation of IRSA. The IRSA prompting for these examples look ad-hoc, and it is not clear how IRSA can be automatically applied to execute general programs, without significant manual efforts. Specifically, the method lacks a clear, algorithmic description that would allow for independent implementation and testing. The current explanation relies heavily on specific examples, making it difficult to understand the underlying principles and generalize the approach to new scenarios or program types. The absence of a formal definition makes it hard to assess the method's limitations and potential for broader applicability.

The example and its execution path play the critical role in IRSA. Isn’t the availability of an execution path too strong assumption for enabling GPT to execute a program? There are many things not discussed, including how to select the example and how to achieve the execution path. Is there one example or multiple examples used in IRSA? The reliance on a pre-existing execution path raises questions about the practical applicability of the method. In many real-world scenarios, obtaining such a path might be as challenging as executing the program itself. The paper does not address how these execution paths are generated or if the method can be adapted to situations where such paths are not readily available. Furthermore, the paper does not discuss the impact of the choice of example on the performance of IRSA, nor does it explore the use of multiple examples and their potential benefits or drawbacks.

It is not clear why IRSA is not used together with GPT4, which casts doubts on the applicability of IRSA approach. The evaluation is neither comprehensive nor systematic. The example programs in the evaluation look simplistic.

### Questions
1. Is there an algorithmic formulation of IRSA? For example, interested people can refer to this formulation to implement IRSA and execute programs using LLMs. 

2. Is the execution path assumption in IRSA too strong? How many examples are used in IRSA?  

3. Can IRSA be used with LLMs other than GPT-3?

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In this paper, the author(s) explore the description and execution of iterative algorithms in large language models. In particular, the author(s) propose “iterations by regimenting self-attention” (IRSA) in which they provide a repetitive and comprehensive example in prompts. Moreover, they illustrate two variants, fragmented prompting and skip attention, which can improve accuracy and address token limitations. Further, the author(s) design a “GPT compiler” that can generate execution paths for large language models similar to IRSA.

### Strengths
Importance of contribution: The proposed solution can achieve outperformance than state-of-the-art approaches. Meanwhile, it also highlights the significance of prompting engineering as GPT-3 applied IRSA can generate more accurate results than GPT-4 without IRSA.

Soundness: The author(s) explain the approach in detail, and conduct evaluation via comparative analysis regarding different questions. 

Quality of presentation: The paper is well-organized, and the language is technical yet understandable for readers with domain knowledge.

Comparison with related works: The author(s) introduce extant studies on large language model prompting.

### Weaknesses
 - The methodology can be elaborated for better clarity.
- The overall structure of this paper can be adjusted.
- The research gaps can be further highlighted and discussed.

### Questions
- Section 2.1: “a variant of Bubble Sort algorithm adapted to this problem and shown in Prompt 2 can be used to solve 76% of these puzzles”, the author(s) should provide evaluation results to support this statement.
- I wonder whether the author(s) consider applying IRSA to GPT-4 and test the result accuracy.
- The author(s) generate random non-repeating digit sequences in the Bubble Sort problem, I wonder whether repeating digits can affect the results.
- I understand the conference has page limits, the authors can consider adjusting the font of prompts to save more space to elaborate the solution description, especially Section 2.4. The font of Prompt 1 is larger than the following prompts.
- The authors should clarify the evaluation metric is accuracy in the caption of Table 1-3.
- The author(s) can consider comprehensively comparing the proposed models with related work to clearly identify the research gap.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
3 good
