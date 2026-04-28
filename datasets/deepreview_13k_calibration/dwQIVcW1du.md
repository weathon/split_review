# From Code to Correctness: Closing the Last Mile of Code Generation with Hierarchical Debugging

- Decision: Reject
- Avg Score: 5.20
- Scores: 5, 5, 5, 5, 6

## Abstract
While large language models have made significant strides in code generation, the pass rate of the generated code is bottlenecked on subtle errors, often requiring human intervention to pass tests, especially for complex problems. Existing LLM-based debugging systems treat generated programs as monolithic units, failing to address bugs at multiple levels of granularity, from low-level syntax errors to high-level algorithmic flaws. In this paper, we introduce \textit{Multi-Granularity Debugger} (\approach), a hierarchical code debugger by isolating, identifying, and resolving bugs at various levels of granularity. \approach decomposes problematic code into a hierarchical tree structure of subfunctions, with each level representing a particular granularity of error. During debugging, it analyzes each subfunction and iteratively resolves bugs in a bottom-up manner. To effectively test each subfunction, we propose an LLM-simulated Python executor, which traces code execution and tracks important variable states to pinpoint errors accurately. 
Extensive experiments demonstrate that \approach outperforms existing debugging systems, achieving an 18.9\% improvement in accuracy over seed generations in HumanEval and a 97.6\% repair success rate in HumanEvalFix. Furthermore, \approach effectively fixes bugs across different categories and difficulty levels, demonstrating its robustness and effectiveness.\footnote{Code and data available at \codeurl}

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper proposes MGDebugger which aims to improve correct code generation using a multi-step approach with LLMs. The approach combines hierarchical code decomposition, test generation, and simulated test execution. Note that all these components are proposed to be done using LLMs. The results of these are used for debugging using a tree structure in a bottom-up fashion to generate bug free code.

### Strengths
The paper tackles the problem of code generation using a multi-step approach. This is a timely contribution given the popularity of multi-step approaches and code generation.  The paper is well written and organized. The individual components of the approach as well as using multi-step approaches for code generation are common; however, in the proposed approach various such components come together in a novel fashion.

### Weaknesses
I overall think the evaluations could be stronger.
- This is especially important considering the stochasticity of LLMs and even further increased variability for multi-step approaches. The results lack error bars.
- The evaluations are done using three datasets, which are all python based and composed of mainly basic problems. It would be great to see more diversity in benchmarks to better convey an understanding of the limitations of the proposed approach. You can consider adding the MultiPL-E benchmark (Cassano et al. 2023).
- As mentioned above, various components come together for the proposed approach, but it would be good to better understand the effects of those through more ablation studies (I know that authors present an ablation study but I propose some extensions to it below as part of Questions).
- The authors conduct extensive evaluations with respect to other approaches in the literature. However, my understanding is that the proposed approach requires more steps and thus is more expensive compared to the rest. It would be good to also add results showcasing computational requirements (like number of steps or number of tokens generated).

### Questions
- It would be interesting to see if you can encourage subfunctions from the beginning and understand the impact of this in comparison with the hierarchical code decomposition step.
- How do the results compare if you swap simulated code execution with real code execution?
- Why are you using only small models of size 7B-22B? Is it possible to add results with bigger models? It’d be interesting to see the effectiveness of the proposed approach with bigger models.
- Table 3. Is it possible to add the no-debugging case?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The paper presents MGDebugger, a hierarchical debugging framework for LLM-generated code. Unlike traditional methods that handle code as a single unit, MGDebugger decomposes code into a tree of subfunctions, enabling targeted bottom-up debugging. This approach uses an LLM-simulated Python executor to trace execution and improve error localization.

### Strengths
MGDebugger offers a structured, hierarchical approach that isolates bugs at multiple granularity levels, an advance over monolithic debugging methods. It outperforms existing techniques like Reflexion and Self-Debugging on benchmarks such as HumanEval, providing a clearer, systematic debugging process. The methodology and experimental results are well-presented, showcasing MGDebugger’s potential to improve reliability in LLM-generated code​.

### Weaknesses
MGDebugger’s novelty is somewhat limited as its approach is similar to **[1]**. The evaluation could be broadened with more datasets, like SweBench, and by including mainstream models like LLaMA 3.1 and CodeLlama to better gauge generalizability and effectiveness in diverse debugging scenarios.

### Questions
1. Could the authors extend their experiments to include additional datasets like SweBench to further validate MGDebugger’s robustness?
2. How does MGDebugger’s approach differ from the hierarchical debugging framework in [1]?
3. Can the authors test MGDebugger on other prominent models, such as LLaMA 3.1 and CodeLlama, to strengthen its applicability across various LLMs?

**References**

**[1]** Chunqiu Steven Xia, Yinlin Deng, Soren Dunn, and Lingming Zhang. *Agentless: Demystifying LLM-based Software Engineering Agents*. arXiv preprint arXiv:2407.01489, 2024.

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
4

### Summary
This paper presents MGDebugger, which decomposes problematic code into a hierarchical tree structure of subfunctions, with
each level representing a particular granularity of error. It analyzes each subfunctions and identify the errors in different levels to resolve bugs. For each subfunctions, it uses LLMs to simulate the Python execution, track variables and pinpoint errors. Experiments demonstrate that MGDebugger outperforms existing tools on simple Python programming tasks like HumanEval, and program fix benchmarks like HumanEvalFix.

### Strengths
1. This paper presents a promising insight: LLMs can debug programs in modular functions and resolve program errors level by level. 
2. The idea is presented clearly and the experiment results presents significant improvements. 
3. The authors conducts extensive experiments on the ablation and debugging improvements compared to the existing methods.

### Weaknesses
1. The paper only evaluated on open-source code models, which possibly not good at the natural language explanation generation. It would be great if the paper can conduct experiment on main-stream closed-source models (for example GPT-4, Claude2) and open-source models with good natural language capabilities (for example Llama-3.1).

2. The paper proposed methods that highly depend on LLMs' reasoning and language analysis capabilities, which I have concerns about. First, the paper use LLMs to decompose programs into subfunctions. While decomposing programs for debugging in general is a promising direction and would be beneficial to large-scale programs, the decomposition is decided by LLMs instead of the language features. This brings uncertainty to the decomposition: how does the LLM decide how to break down a large function? What if this function is recursively called and cannot be decomposed into tree-structures? It could be great if the authors could provide a comparison experiment for compare the proposed method with directly decomposing program into syntax-level functions by static analysis.

Second, the paper use LLMs to generate test cases, which brings the inaccuracy of test generation of LLMs. It would be great to see the accuracy of test case generation. For example, given the same test input, how many test outputs generated by LLMs are the same as the ground truth test outputs (which can be obtained from running the canonical solution of the task).

Third, the proposed method also depend on LLMs for program execution simulation, which also require LLMs to be accurate on program reasoning. Some deep-dive analysis on whether the intermediate state predicted by LLMs are accurate would be helpful.The author could conduct a experiment on comparing the intermediate state predicted by LLMs with those from an actual Python interpreter on several sampled examples.

Also, why to avoid the program execution in MGDebugger is not fully motivated in this paper since the tasks are mostly small Python programming tasks. The execution is neither infeasible nor time-consuming. It would be great to see a comparison of the time and computational resources required for LLM-based simulation versus actual executionAlso, as most of the programs in HumanEval, MBPP and HumanEvalFix are small, the decomposition could sometimes fall back to a single function debugging if there is only one function in the generated response. It would be insightful if the authors can present a large-scale program debugging (for example, tasks from CodeContests or SWE-bench), which I think would be the killer application of the proposed method. 

3. The paper possibly uses an inappropriate setting of baselines: In Table1, the results from 'No-Debugging' is generated by a prompt without containing visible test cases. Therefore, the effect of debugging does not offset the additional information gain from visible test cases. It would be better if the author could follow settings in previous work like Self-Debugging (G.1)[1] to set up 'No-Debugging' baseline.

### Questions
1. Could you please provide the comparison results on some advanced models (GPT, Claude, etc.) or some open-source models with better natural language capabilities?
2. Could you provide the accuracy of LLM-based test generation and program execution? 
3. How would MGDebugger generate the tree structure if the program contain recursions?
4. Could you please provide a case study of MGDebugger working on a larger scale of program? Examples from CodeContests or SWE-bench could serve good starting point.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes a multi-granularity debugger system, MGDebugger, to resolve bugs in problematic code. In particular, it decomposes code into a hierarchical tree structure and fixes the underlying problems in each divided subfunction separately. Extensive experiments on some popular benchmarks, including HumanEval, MBPP and HumanEvalFix, have demonstrated the effectiveness of the proposed techniques.

### Strengths
- an interesting idea to decompose the code for repair.
- good results compared with baselines
- well-written and easy to follow

### Weaknesses
 - One of the major concerns in this work is that it relies on LLMs heavily. Using LLMs for decomposition, test case generation, and execution. I am confused about the effectiveness of each component when using LLMs. Also, as LLMs are black-box, whether to use some traditional program analysis tools for replacement. Some relevant experiments to compare with traditional tools are needed.
- Another major concern is that the fixed errors are too simple (examples from case studies), which hinders the proposed technique from being applied. 
- Some more powerful models, such as GPT-4o, are missing for evaluation.

### Questions
- What is the difference between accuracy and RSR? Why is accuracy higher than RSR in the experimental results?
- What is the performance of MGDebugger when applying it in program repair such as Defects4J?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
- This paper propose a Multi-granularity Debugger, named MGDebugger, that leverages LLMs to debug LLM-generated code
- This paper proposes a hierarchical debugging strategy from low-level errors to high-level flaws
- The evaluation results of this paper indicates the effectiveness of MGDebugger

### Strengths
- This paper is clearly written and easy to comprehend
- This paper is well-motivated and address an important AI4SE task, automated debugging/repair
- This paper conduct a comprehensive evaluation on three LLMs with various parameter size

### Weaknesses
Generally, I think this paper addresses an important AI4SE task and conduct a comprehensive empirical study about existing work in this area, which has a large number of existing work. However, I have some concerns below:

- Baseline Choice: Noticing that most existing automated program repair (APR) work [1-4] are evaluated on Defect4J, which is a repo-level repair benchmark, I am curious about the choice of HumanEval/MBPP/HumanEvalFix, which are relatively easiler than Defect4J. I think the evaluation results on Defect4J might better indicate the effectiveness of your approach in a real world setting or you might explain the reason of not evalaluating on Defect4J
- Technical Contribution: Existing work also conduct debugging/repair on ASTs, e.g., KNOD [3], I think it is better to explain the difference between your approach and these work
- Selection of components in your approach: In section 3.4, you use a LLM-simulated execution to obtain execution results, and I am curious about the reason of leveraging LLMs instead of directly executing the targeted code (as HumanEval/MBPP are not difficult to build a execution environment)

### Questions
1. Similar with the "weakness" section, what is reason of choosing HumanEval/MBPP/HumanEvalFix instead of Defect4J? 
2. What is the difference between your approach and existing APR approaches on ASTs, e.g., KNOD (maybe some explanation is necessary)?
3. What is the reason of leveraging LLMs instead of directly executing the targeted code to obtain the execution results?
4.In Algorithm 1: 1) why conduct  MGDebugger before execution, i.e., you might conduct debugging on a correct one? 2) what is the definition of Line 13 "f^{'} \gets DEBUG(f, ...)"?

### Soundness
2

### Presentation
3

### Contribution
3
