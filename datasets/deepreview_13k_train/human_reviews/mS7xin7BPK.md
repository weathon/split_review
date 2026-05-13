# LEGO-Compiler: Enhancing Neural Compilation Through Composable Chain of Thought

- Decision: Reject
- Scores: 10, 5, 5, 6

## Abstract
Large language models (LLMs) have the potential to revolutionize how we design and implement compilers and code translation tools. However, existing LLMs struggle to handle long and complex programs.  We introduce LEGO-Compiler, a novel neural compilation system that leverages LLMs to translate high-level languages into assembly code. Our approach centers on three key innovations: LEGO translation, which decomposes the input program into manageable blocks; annotation-based Chain-of-Thoughts, guiding LLMs through the compilation process with LLM-annotated context; and a feedback mechanism for self-correction. Supported by formal proofs of code composability, LEGO-Compiler demonstrates high accuracy on multiple datasets, including over 99% on ExeBench and 100% on industrial-grade CoreMark, and successfully handles programs far exceeding the length limitations of native LLM translation. This work opens new avenues for applying LLMs to system-level tasks, complementing traditional compiler technologies.

## Human Reviews

## Human Reviewer 1

### Rating
10

### Rating Number
10

### Confidence
2

### Summary
The paper presents a novel neural compilation system aimed at translating high-level programming languages into assembly code using Large Language Models (LLMs). Recognizing LLMs' limitations in handling complex and lengthy code, the authors introduce "LEGO translation," which decomposes large programs into smaller, manageable blocks (akin to LEGO pieces) that can be individually translated and reassembled. This process is enhanced by a Chain-of-Thought (CoT) approach and a feedback-driven self-correction mechanism, helping LLMs manage the intricate steps of code compilation more accurately.

Contributions include:

1. **LEGO Translation**: A modular approach to breaking down programs into composable blocks, making translation more efficient and scalable.
2. **Annotation-Based Chain-of-Thought (CoT)**: LLMs are guided through the compilation process with intermediate annotations, improving context comprehension and translation accuracy.
3. **Feedback Mechanism**: A self-correcting system that uses error feedback for iterative improvement in the translation process.
4. **Empirical and Theoretical Validation**: LEGO-Compiler achieves over 99% accuracy on ExeBench and fully compiles CoreMark, demonstrating its potential for handling code complexity and scalability.

### Strengths
1. **Originality**: The paper introduces several novel concepts, primarily the "LEGO translation" approach. This method effectively decomposes complex code into smaller, semantically composable blocks, allowing for more scalable and accurate translations. This compositional approach is particularly original in the neural compilation field, where such modular treatment of code is uncommon. Furthermore, the annotation-based Chain-of-Thought (CoT) and feedback-driven self-correction mechanisms are innovative enhancements that showcase a creative blend of ideas from traditional compiler techniques with modern neural architecture capabilities. By positioning LEGO-Compiler as a system capable of complementing traditional compilers, the paper broadens the scope of neural compilation research.

2. **Quality**: The paper provides a robust empirical validation of the LEGO-Compiler’s effectiveness across diverse benchmarks, such as ExeBench, CoreMark, and the newly introduced LongFunction dataset. The results are impressive, showing over 99% accuracy on ExeBench and full compilation success on CoreMark, indicating the system's capability to handle real-world, industry-grade code. The inclusion of both theoretical and empirical support, including formal proofs of composability, reinforces the quality and rigor of the research.

3. **Clarity**: The paper is well-structured and clearly explains the methods used, such as the part-split algorithm, control flow annotations, struct annotations, and feedback mechanisms. Visual aids, like flowcharts and annotated code examples, further enhance understanding, particularly for complex concepts like variable mapping and CoT stages. Overall, the clear presentation makes the LEGO translation process and associated mechanisms accessible to readers with varying levels of expertise in neural compilation and compiler design.

4. **Significance**: This work makes a strong case for the potential of LLMs in neural compilation, an area traditionally dominated by classical compilers. By demonstrating that LLMs can efficiently handle code translation tasks that were previously infeasible due to context limitations, the paper sets a foundation for future research on LLM-based compilation. The proposed modular approach to code translation may influence other domains where handling long or complex code sequences is challenging. Additionally, the introduction of the LongFunction dataset provides a valuable benchmark for evaluating neural compilers, potentially serving as a standard for future advancements in the field.

In summary, the paper’s originality, comprehensive evaluation, clear articulation, and impactful contributions make it a substantial addition to the literature on neural compilation. The LEGO-Compiler represents a significant step forward in addressing scalability issues and extending the capabilities of LLMs in code translation, providing a solid framework for further research and practical applications.

### Weaknesses
 **Weaknesses**

While the LEGO-Compiler paper makes substantial contributions to the field of neural compilation, there are a few areas where improvements could enhance its impact and clarity. I offer constructive feedback on the following points to help the work align more closely with its goals:

1.  **Scalability and Efficiency**: Although the paper demonstrates the scalability of LEGO-Compiler on long functions and complex codebases like CoreMark, it acknowledges higher computational costs relative to traditional compilers. However, the paper stops short of providing any concrete analysis of these costs or suggesting optimizations to mitigate them. Including a quantitative comparison of LEGO-Compiler's efficiency against traditional methods (e.g., runtime, memory usage) would provide a clearer understanding of its real-world applicability. Additionally, further exploration of methods to reduce computational demands, such as model pruning or more efficient context handling within the LLM, could add significant value. Specifically, the paper lacks a detailed breakdown of the time spent in each phase of the LEGO translation process, such as code splitting, individual block translation, and reassembly. This makes it difficult to pinpoint the bottlenecks and areas for potential optimization. For example, it would be beneficial to know the average time taken to translate a single code block of a given size, and how this time scales with the complexity of the block. Furthermore, the memory footprint of the LLM during translation is not discussed, which is a critical factor for practical deployment, especially on resource-constrained devices.

2.  **Evaluation Breadth and Context**: While the empirical results on ExeBench and CoreMark are compelling, the choice of datasets might limit the generalizability of the findings. ExeBench and CoreMark focus on specific C code structures, leaving open questions about how LEGO-Compiler would perform on code from other languages or highly varied program structures. An evaluation across different programming languages, such as Java or Python, would highlight the flexibility of LEGO-Compiler and make the case for its broader applicability. Furthermore, testing on real-world projects with interdependencies, libraries, or complex input-output structures would more fully reflect the challenges neural compilers face outside of controlled benchmarks. The current evaluation also lacks a detailed analysis of how the performance varies with different code characteristics, such as the density of control flow statements, the presence of complex data structures, or the depth of function call hierarchies. This analysis is crucial for understanding the limitations of the approach and identifying areas where it might struggle.

3.  **Error Feedback and Self-Correction Limitations**: Although the paper proposes a feedback-driven self-correction mechanism, it appears to rely on error feedback types that may not always be straightforward to integrate in practice (e.g., assembler, runtime, and behavioral error feedback). Each type of error feedback requires specific handling, which could complicate implementation in a more generalized setting. It would be beneficial if the paper discussed how to automate or streamline these correction processes more effectively. Providing more specific insights or examples on how this system could handle unforeseen or non-standard errors could also strengthen the approach and demonstrate the robustness of LEGO-Compiler’s feedback mechanism. The paper does not specify how the feedback is used to guide the LLM in subsequent translation attempts. For instance, it is unclear whether the LLM is simply provided with the error message or if it is given more detailed information about the location and nature of the error. A detailed explanation of the feedback loop and how it influences the LLM's behavior is needed.

4.  **Detailed Ablation of LEGO Translation**: While the LEGO translation method is central to the paper's contributions, the empirical results could benefit from a more detailed ablation study focused specifically on this component. For example, examining how various part sizes or splitting strategies affect accuracy and performance on different codebases would provide insights into the optimal configurations of LEGO translation. This could be helpful for future researchers or practitioners looking to adapt or refine the approach. The paper does not explore the impact of different splitting algorithms on the translation quality. For example, it would be useful to compare the performance of the current algorithm with simpler splitting strategies, such as splitting at function boundaries or at fixed intervals. This would help to isolate the contribution of the specific splitting algorithm used in the paper.

5.  **Limited Discussion of Edge Cases and Limitations**: Although LEGO-Compiler achieves high accuracy on ExeBench and CoreMark, the paper does not explicitly discuss any scenarios where the system may fail or struggle. For example, specific cases of nested or non-linear control flows, rare syntax patterns, or highly recursive functions could challenge the system’s modular translation approach. Highlighting these limitations, possibly with failure case analyses or suggestions for future handling of edge cases, would provide a more balanced perspective on LEGO-Compiler’s strengths and limitations. The paper also lacks a discussion of how the system handles code with complex pointer arithmetic or dynamic memory allocation. These are common features in C programs, and it is important to understand how they are handled by the LEGO translation process.

6.  **Potential for Fine-Tuning or Model Customization**: The paper could discuss in greater depth how LEGO-Compiler’s performance might benefit from fine-tuning on specific code domains or architectures, particularly given the reliance on LLMs trained on general datasets. Tailoring the model to domain-specific code (e.g., embedded systems, high-performance computing) could optimize its accuracy and efficiency for these applications. The authors could address whether or not such fine-tuning might enhance LEGO-Compiler’s flexibility and discuss how researchers might incorporate this approach in practice. The paper does not explore the potential benefits of using different LLMs with varying architectures or training datasets. It would be valuable to understand how the choice of LLM affects the performance of the LEGO-Compiler and whether certain LLMs are better suited for specific types of code.

### Questions
1. **Computational Costs and Efficiency**: Can the authors provide a more detailed comparison of LEGO-Compiler’s computational efficiency relative to traditional compilers? Specifically, it would be helpful to know if there are areas where LEGO-Compiler could optimize computational resource usage or if there are plans to explore methods, like model pruning or improved in-context memory, to enhance efficiency without sacrificing accuracy.

2. **Applicability Across Languages**: Given that the experiments focus primarily on C code, how adaptable is LEGO-Compiler to other programming languages, especially those with different memory management paradigms (e.g., Java) or highly dynamic types (e.g., Python)? Could the authors clarify any plans for testing the approach on different languages and any anticipated challenges they foresee in these cases?

3. **Error Feedback Mechanism**: The feedback-driven self-correction mechanism relies on different feedback types (assembler, runtime, and behavioral). Could the authors elaborate on how feasible it is to implement each type of feedback in practice and discuss any automation strategies they envision to simplify the process? Additionally, are there specific cases or error types where this feedback approach might struggle?

4. **Granularity of LEGO Translation**: The paper introduces LEGO translation as a modular, part-split approach to handling complex code but lacks detailed ablation on part size selection and splitting strategies. Could the authors share insights or planned experiments on how they arrived at optimal part sizes? For instance, have they explored whether finer or coarser splits might impact translation accuracy differently across datasets or LLM models?

5. **Handling of Edge Cases and Recursion**: Does LEGO-Compiler currently have specific strategies for handling edge cases such as deeply nested loops, irregular control flows, or highly recursive functions, which may challenge modular composition? If so, could the authors elaborate on these strategies? If not, do they have ideas for how these cases could be integrated into the current approach?

6. **Potential for Model Fine-Tuning**: Given that LEGO-Compiler leverages general LLMs, would the authors consider fine-tuning models on specific types of code (e.g., embedded systems, HPC) to improve results further? Could they clarify if they have experimented with or plan to experiment with domain-specific tuning, and if so, any notable improvements observed?

7. **Comparison with Non-LLM Neural Compilers**: How does LEGO-Compiler compare to other non-LLM-based neural compilers or neural translation systems, both in terms of accuracy and scalability? Including this comparison, especially if backed by experimental data, would strengthen the paper’s case for adopting LLMs in neural compilation. Could the authors provide clarification or consider adding this in future revisions?

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The paper presents a technique for neural translation from high-level language to assembly code, focusing on functionality (and not optimization). The core idea is to decompose the program into basic blocks (following traditional compilers) and perform non-optimized translation of each basic block using an LLM. To maintain a mapping of variables to low-level memory locations, LEGO-Compiler uses a separate LLM step. The memory mapping is used as context for the translation of each basic block. To deal with identical variable names across scopes, LEGO-Compiler applies a renaming preprocessing pass. The translation is shown to be effective on 500 programs from ExeBench and additional examples from CoreMark.

### Strengths
- The first work I'm aware of to show effective translation of reasonably sized programs
- Compelling approach: 
	- decompose large programs into basic blocks 
	- annotation-based CoT for providing memory mapping 
	- feedback mechanism for self-correction

### Weaknesses
 - What is the motivation for this work? You seem to replace the parts of the compiler that are computationally more efficient with syntax-directed translation (SDT), and suggest no benefit in doing that. I am sure you have something in mind, so please make it more explicit. 
- 99% accuracy on a testset of 500 examples from ExeBench is very different from the "over 99% on ExeBench" (40k examples, or 23k examples after filtering). A different claim at a factor of x46.

- Many steps in LEGO-Compiler are very similar to the ones applied by a traditional compiler. 
	- values collection
	- variable mapping
	- splitting into basic blocks 

- The major step being replaced with an LLM is the translation of a basic block.

- The translation at basic-block level, assuming local variables are managed on the stack (without dealing with register assignment) and swapping in/out from registers on every entry/exit to a statement is quite naive. 

- the fact that you can translate the instructions of each basic block separately is the basis of traditional compilers. The more intricate challenges are around register allocation and memory allocation across blocks. Not to mention optimizations, as you declared these to be out of scope. 

- In C.3 you compare the computation cost of LEGO-Compiler to the human effort require to build a compiler. Most of the human effort is outside what is done by the LEGO-compiler. The decomposition into basic blocks and non-optimized translation is achievable within undergraduate level compiler homework. 

- Traditional compilers provide a deterministic and predictable outcome. The computational effort associated with your approach is orders of magnitude bigger, and provides no guarantees. Why would we take this approach? 

- I would guess that there is exploring optimizations can be more fruitful for this technique.

- Your translation is based on the fact that each statement is completely independent. The assumption of composability (Appendix B) does not hold when memory allocation is permitted (due to aliasing).

Consider the program:
```
int *p = malloc(sizeof(int));
int *q = p;
*p = 10;
*q = 20
```

The code is supposed to:

1.	Allocate memory for an int and store it in p.
2.	Make q point to the same memory as p.
3.	Store 10 in the memory pointed to by p.
4.	Store 20 in the same location via q, so the final value in memory is 20.

However, if translation treats *p = 10 and *q = 20 as independent, it could lead to the (incorrect) assumption that p and q point to different locations, and might (incorrectly) allocate separate memory for p and q. 


Another (somewhat similar) issue may arise if the LLM decides to re-order instruction in a block without observing that they are dependent (for example, when operating on cells of an array, assigning them one after the other).



# Additional Questions 


- You say "we don't rely on an existing compiler" = how do you get the examples for ICL? What is "compiler knowledge guided CoT"

- what does "trivial semantic units" mean?

- what do you mean by "semantically commposable control blocks", are these just basic blocks as implied later? 

- what is the difference from how a traditional compiler works to "translate" each block separaetly, while maintaining a symbol table? What part of the compiler are you really replacing? The syntax-directed translation rules? What is the value in replacing these? 

- who is responsible for allocating the addresses? For example, who assigns blksize to -36(%rbp) in Figure 1(b).


- Line 270-272, can you provide more details about this renaming pass? is it aware of scoping rules? 

- Line 322-323 - 99% accuracy on a testset of 500 examples from ExeBench is very different from the "over 99% on ExeBench" (40k examples, or 23k examples after filtering). A different claim at a factor of x46.

# Minor 

- l 62 - "we [do] not"

### Questions
(1) what is the motivation for this work?

- Many steps in LEGO-Compiler are very similar to the ones applied by a traditional compiler. 
	- values collection
	- variable mapping
	- splitting into basic blocks 

- The major step being replaced with an LLM is the translation of a basic block.

- The translation at basic-block level, assuming local variables are managed on the stack (without dealing with register assignment) and swapping in/out from registers on every entry/exit to a statement is quite naive. 

- the fact that you can translate the instructions of each basic block separately is the basis of traditional compilers. The more intricate challenges are around register allocation and memory allocation across blocks. Not to mention optimizations, as you declared these to be out of scope. 

- In C.3 you compare the computation cost of LEGO-Compiler to the human effort require to build a compiler. Most of the human effort is outside what is done by the LEGO-compiler. The decomposition into basic blocks and non-optimized translation is achievable within undergraduate level compiler homework. 

- Traditional compilers provide a deterministic and predictable outcome. The computational effort associated with your approach is orders of magnitude bigger, and provides no guarantees. Why would we take this approach? 

- I would guess that there is exploring optimizations can be more fruitful for this technique.

(2) what are the assumptions you are making about the programming language and the translation? 

Your translation is based on the fact that each statement is completely independent. The assumption of composability (Appendix B) does not hold when memory allocation is permitted (due to aliasing).

Consider the program:
```
int *p = malloc(sizeof(int));
int *q = p;
*p = 10;
*q = 20
```

The code is supposed to:

1.	Allocate memory for an int and store it in p.
2.	Make q point to the same memory as p.
3.	Store 10 in the memory pointed to by p.
4.	Store 20 in the same location via q, so the final value in memory is 20.

However, if translation treats *p = 10 and *q = 20 as independent, it could lead to the (incorrect) assumption that p and q point to different locations, and might (incorrectly) allocate separate memory for p and q. 


Another (somewhat similar) issue may arise if the LLM decides to re-order instruction in a block without observing that they are dependent (for example, when operating on cells of an array, assigning them one after the other). 




# Additional Questions 


- You say "we don't rely on an existing compiler" = how do you get the examples for ICL? What is "compiler knowledge guided CoT"

- what does "trivial semantic units" mean?

- what do you mean by "semantically commposable control blocks", are these just basic blocks as implied later? 

- what is the difference from how a traditional compiler works to "translate" each block separaetly, while maintaining a symbol table? What part of the compiler are you really replacing? The syntax-directed translation rules? What is the value in replacing these? 

- who is responsible for allocating the addresses? For example, who assigns blksize to -36(%rbp) in Figure 1(b).


- Line 270-272, can you provide more details about this renaming pass? is it aware of scoping rules? 

- Line 322-323 - 99% accuracy on a testset of 500 examples from ExeBench is very different from the "over 99% on ExeBench" (40k examples, or 23k examples after filtering). A different claim at a factor of x46.

# Minor 

- l 62 - "we [do] not"

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper proposes to use a set of methods to improve the quality of neural code translation. More precisely, the authors propose three methods: 1) LEGO translation, which decomposes large programs into smaller blocks; 2) Using annotations and Chain-of-Thought to guide the LLM through the compilation process; and 3) Using feedback obtained after compiling the translated code for self-correction. The authors evaluate their proposed method on a subset of 500 C codes randomly selected from ExeBench (a dataset of 40k executable C programs). They show that their proposed method improves the quality of code generated by existing LLMs when evaluated on the proposed benchmark (GPT-4o, Claude-3.5-Sonnet and DeepseekCoder). Claude-3.5-Sonnet improves by 7.4% while GPT-4o improves by 23%.

### Strengths
-	The problem of Neural Compilation is hard and challenging. A minor mistake can make the generated code invalid.
-	Achieving an accuracy reaching 99% and even 100% on the task of neural compilation is an interesting result.

### Weaknesses
While the proposed work is important, and while the results are interesting, I do not believe that the contribution is strong enough. One of my concerns with the paper is that the authors combine a set of well-known and obvious methods and apply them in the context of neural compilation to improve its quality. There is clearly a degree of novelty in doing this, but I believe it is not strong enough. This said, I still think the work and the results are quite interesting.

One of the main ideas proposed in the paper is to compile code block by block instead of compiling it in one shot. The authors do not provide a clear ablation study showing the effect of this idea (alone). I would suggest adding an experiment where you take the baseline and use it to compile code block-by-block (without using the pass@k method, where you reject the generated code if it does not compiler and generate other samples of the code). The pass@k column in Table 1 currently includes two techniques: the translation block-by-block and the detection of syntactic errors in the generated code. Can you add a column to evaluate the use of block-by-block compilation when applied alone?

The authors do not provide a detailed analysis of how long their compilation process takes. They propose an iterative process which might take a long time and therefore it is important to evaluate how long compilation takes.

The current paper also does not compare with previous work. While such a comparison is not necessary, it would have helped the reader better appreciate the contribution of this paper. For example, the authors could have generated LLVM-IR using LLMs and compared with Guo and Moses [1]. I’m saying this because adapting your tool-chain to generate LLVM-IR does not require a significant amount of work since you already generate code for x86 64, arm-v8a, and riscv64. This said, I do not think this experiment is essential for the validation of your contribution. It is rather recommended.

It would be interesting to show a breakdown of the accuracy of the LEGO-compiler on the different hardware architectures (x86 64, arm-v8a, and riscv64). Does the LEGO-compiler do well on all of them?

### Questions
-	Can you add an ablation study to evaluate the use of block-by-block compilation alone without rejecting code that does not compile?
-	Can you evaluate how long it takes for the LEGO-compiler to compiler code?
-	I recommend adding a comparison with Guo and Moses (2022). While this experiment is not necessary, it will better clarify the strength of your contribution.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper targets at an important problem of neural compilation, which translates high-level source code into assembly code with Large Language Models (LLMs). The authors propose a new method called LEGO-Compiler, which decomposes a large high-level program into small trunks, compiles individual code snippets, and then composes them together. The authors demonstrate that the LEGO-Compiler achieves an accuracy of over 99% on ExeBench and nearly 100% on CoreMark, which are two benchmarks for evaluating neural compilations.

### Strengths
1. Targeting an important problem of neural compilation.
2. Novel method that adopts the idea of decomposing and composing to handle large complex programs.
3. Proofs of the correctness of the LEGO approach and clearly stated assumptions and limitations.

### Weaknesses
1. Weak benchmarks: the evaluated benchmarks are not complex enough to demonstrate the utility of the LEGO-Compiler.

The program sizes of the benchmarks can be too small. Figure 6 shows the complexity of the ExeBench. The number of programs whose total instruction count exceeds 100 is scarce. Even for the top 10% of most complex programs, the total instruction count hardly exceeds 200. Considering that a statement line in the high-level language may be translated into multiple assembly instructions, the ExeBench could contain only a few dozen lines of code, which is too small to demonstrate the utility of the LEGO-Compiler. Although the authors also evaluate a more complex benchmark, the LongFunction benchmark, the number of complex programs is not reported.

The language features and library usage in the benchmarks are limited. One of the challenges in compilation is the handling of various language features and library calls. For example, multi-dimensional arrays and pointers to functions can be challenging to compile correctly. However, from the examples given in the paper, the benchmarks only contain simple pointer operations and arithmetic operations, which are not complex language features. Moreover, library calls can be hard to compile. System calls, such as `fork` and `execve`, require special handling in the assembly code. The authors do not discuss how the LEGO-Compiler handles these system calls. It is unclear whether the evaluated benchmarks contain such system calls.

Without an understanding of the complexity of the benchmark, it can be hard to draw a conclusion on the effectiveness of the LEGO-Compiler.

2. Lack of comparison with other state-of-the-art methods.

The authors mentioned multiple pieces of work that also target the problem of neural compilation. However, none of the compared approached is evaluated in the paper. The authors should compare the LEGO-Compiler with other state-of-the-art methods to demonstrate the effectiveness of the LEGO-Compiler. In particular, the authors should show the improvement of the LEGO-Compiler over the state-of-the-art methods. Without such comparison, the advantage of the LEGO-Compiler is unclear.

3. Insufficient correctness evaluation on the generated assembly code.

The authors do not verify the correctness of the generated assembly code. The authors mention that they run the test cases provided by the benchmarks, and check whether the output of the generated assembly code passes the test cases. However, this does guarantee that the generated assembly code is correct. Testing cases can be incomplete, and may not cover all behaviors of the program. It can be the case that the generated assembly code happens to pass all the test cases, but is still non-equivalent to the original high-level program. The authors should verify the equivalence of the generated assembly code with the original high-level program. SMT solvers can be a useful tool for this purpose.

Without the correctness verification on the generated code, the achieved accuracy of the LEGO-Compiler is not convincing.

4. The improvement with the LEGO-Compiler compared to baselines is not significant.

The improvement of the LEGO-Compiler over the baseline is less than 1% on the ExeBench, which is not significant. As shown in Table 1, even without the LEGO-style approach, the baselines can already achieve over 98% accuracy. LEGO-Compiler only improves by 1% compared to the Chain-of-Thought baseline. The insignificant improvement raises the question of whether the LEGO-Compiler is necessary.

Moreover, the accuracy of the LEGO-Compiler for all the small LLMs is missing. Also, the Chain-of-Thought baseline is missing for Codestral. The reason behind such missing experiments is not clear. What are the limitations of applying LEGO-Compiler to small LLMs? Answering this question can help understand the limitations and application scope of the LEGO-Compiler.

### Questions
1. How does the LEGO-Compiler handle complex language features and library calls?
2. How does the LEGO-Compiler perform on benchmarks with over 1000 lines of code?
3. How does the LEGO-Compiler compare with other state-of-the-art methods on neural compilation?
4. What is the true accuracy after verifying the correctness of the generated assembly code?
5. Why is the improvement of the LEGO-Compiler over the baseline insignificant?
6. What are the limitations of applying LEGO-Compiler to small LLMs?

### Soundness
2

### Presentation
3

### Contribution
2
