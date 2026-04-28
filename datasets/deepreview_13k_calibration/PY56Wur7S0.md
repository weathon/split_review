# Execution-guided within-prompt search for programming-by-example

- Decision: Accept
- Avg Score: 5.75
- Scores: 6, 6, 6, 5

## Abstract
Soundness is an important property in programming-by-example (PBE) as it allows synthesizers to perform a search over a domain-specific language (DSL) that terminates when any sound program is found.
Large language models (LLMs) can generate code from examples without being limited to a DSL, but they lack search, as samples are independent.
One can sampling code until a sound program is generated, but that is very inefficient.
In this paper, we use an LLM as a policy that generates lines of code and then join these lines of code to let the LLM implicitly estimate the value of each of these lines in its next iteration.
We further guide the policy and value estimation by executing each line and annotating it with its results on the given examples. 
This allows us to search for programs within a single, expanding prompt until a sound program is found by letting the policy reason in both the syntactic (code) and semantic (execution) space.
We evaluate this approach on straight-line Python code generation using five benchmarks across different domains (string transformations, list transformations, and arbitrary Python programming problems).
We show that the model effectively uses the execution results to guide the search and that within-prompt search performs well at low token budgets.
We also analyze how the model behaves as a policy and value, show that it can parallelize the search, and that it can implicitly backtrack over earlier generations.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper builds on past work on program synthesis, in particular at the intersection of language model guided synthesis and execution guided synthesis. The authors propose a synthesis technique called *execution-guided within-prompt* search. It is execution-guided in that after each line of Python code is written by the language model, it is executed and the result is appended as a comment to the line. And the *within-prompt* technique is based on the idea of taking several single-line completions from the model, concatenating them into a sequence of lines (despite being completions for a single line – of course renaming is done to avoid conflicts), so that at the next step of search the language model will implicitly pick which one (or more) values to use downstream. They evaluate the model and ablations on a range of datasets and find considerable benefits.

### Strengths
- The core ideas are interesting and useful. The idea of appending execution information makes sense, and is very related to past work (which the authors cite) on guiding synthesis using execution results of program prefixes – it's surprisingly not an idea that I have seen used with LLMs in particular, where the execution information can be shown as a string for many data types, but it makes a lot of sense to do it and is found to be beneficial here.
    - Some more related work: ExeDec (Shi et al 2024) is a relevant piece of related work – they don't use the execution of the program prefix to guide execution, rather they predict the execution result of the next step ("subgoal") they want to accomplish in the program and then write code conditioned to try to achieve that. Generally work on code repair is also very related – while it involves writing whole functions at once and seeing their execution results and error messages, it's still quite related. 
- The within-prompt search idea is also interesting – and it's intriguing that it sometimes uses more than one intermediate value produced in a single step downstream. It's also nice how the model can recover when it messes up by implicitly backtracking just by building on some earlier execution result.
    - It wasn't obvious to me that this search strategy would work well, given that this is not at all a style of coding that I would expect to see much of in internet training data (often *all* intermediate variables are used, developers don't write extra unused variables too often) – so it's nice to see that it works.
- Figure 4 is nice – it's helpful to see how execution leads to more backtracking, presumably because the model has seen its mistake through the execution result and takes a different approach
- A quite wide range of benchmarks are used, a solid set of benchmarks for a synthesis paper

### Weaknesses
 - The within-prompt search idea is interesting, but it'd be nice to see it compared to other methods for performing the search, where the execution information is still included. One very simple baseline that's not even a search would be to have the LLM explicitly pick which completion to keep, at which point the others are discarded from the context, and the program is written in this new context (as opposed to having all the other choices in the context still). That would produce rollouts instead of a search, but is still a good baseline to have. There is other work, like Tree Of Thoughts (Yao et al 2023) and Stream of Search (Gandhi et al 2024) that have focused on using LLMs for tree search. Comparisons to other methods, whether it's those ones or other tree-search baselines, would strengthen the evaluation. Even if just relatively simple LLM-search-based baselines were used, it would help with making it clear what sorts of alternatives exist to within-prompt search and how it measures up to them (or why none of them apply – but I expect some other simple form of search would apply). In short, it'd be helpful to have experiments that compare within-prompt search to outside-prompt search, to clarify the advantages of this contribution.

> ...if the policy is certain and samples with less diversity, the model is more likely to solve a problem in the end. Conversely, if the policy samples many diverse lines, it is less likely to solve the problem in the end. This indicates that the model does behave like a policy.
- While I agree that the LLM is certainly a policy (it's sampling the next action), this explanation confused me. Correlation between diversity and success rate doesn't mean something behaves "like a policy" – you could certainly have a policy that doesn't have this behavior, and through temperature you can modulate how much diversity you have in a policy, but that's separate from whether it behaves "like a policy". Maybe the authors meant it behaves like a certain kind of policy?

> ...keeps on sampling until we have k = 4 syntactically unique operations. Having more possibilities requires the model to act as a better value function. For 4 out of 5 datasets, the performance slightly increases, reinforcing our intuition that the model correctly picks which option to continue from
- I also agree that the model is implicitly acting as a value function, as it picks what to extend, which is interesting. But I don't follow the statement that having more possibilities "requires" acting as a "better" value function. Having more low-quality options requires a better value function to weed out the bad ones, but having more from the same distribution shouldn't have that effect. Having more of the same quality options *does* require a good value function in order to *benefit* from the extra examples – and this might be what the authors meant, and the wording just confused me.
  - That said, the improvements in Figure 6a are fairly small. As a thought on an experiment that might show larger differences, it'd be interesting to see whether something like only giving it 2 unique options and jumping up to 4 or 6 unique options would have a bigger improvement (and not focusing on the unique vs nonunique distinction). 

- I think that Figures 2a and 2b would likely be better as bar plots instead of a line plots, since the X axis is categorical data not a continuous metric.
- Figure 3 might be better as a heatmap since it's discrete data so arbitrary points aren't needed, and it would help the problem where the density of points is so high that many just look like solid red bars and it's hard to compare them.

- The approach is limited to working with straightline code – but could perhaps be extended to write whole units of code at once containing if statements or loops as long as they're all done in one completion, and there are other interesting directions to build off of there
- The statements about soundness guarantees in the abstract are confusing – and soundness is mentioned far more in the abstract than the paper. The soundness guarantees come from executing the programs to check correctness, which is done when testing programs generated by LLMs, whether or not they were constructed iteratively through the suggested approach here or all at once – that doesn't change the soundness in my understanding.
- line 31: "grail" -> "holy grail"
 > We leverage pre-trained language models to perform programming-by-example without restrictions on the domain (specific language).
- This first line of the contribution list is not itself a contribution of the paper to the field since it's shared by other LLMs synthesis work – it's a feature of the second line (execution-guided within-prompt search)

### Questions
- Is the "8 iteration" limit used for the "Free" and "Straight" settings too? In particular I want to make sure they're not also restricted to only producing 8 lines, which would limit them compared to the "search" based models that are allowed to use more than one line from a single iteration in their solution.

### Soundness
3

### Presentation
2

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
The paper presents “within-prompt search” method to enable LLMs to reason about the syntax and semantics of programs concurrently. This approach is a novel instantiation of PBE with execution guidance specifically designed for LLM-based program synthesis. The within-prompt search technique encodes multiple candidate code completions within a single prompt. This enhances the likelihood of producing syntactically and semantically accurate code.

The authors position the role of the LLM as a policy to generate code and as a value function to evaluate previously generated code based on its semantics (concepts from reinforcement learning theory where the policy guides generation and the value function assesses the quality of partial solutions). The value of these partial programs is determined simply by syntactic validity and consistency with given examples.

Two baselines are used for comparison: an unrestricted baseline without any search constraints or execution annotations and a second baseline where straight-line constraints are imposed, but search and annotations are disabled. The experimental results show a significant improvement in accuracy and consistency with the within-prompt search method.

### Strengths
1. The proposed method is straightforward, yet the experimental results demonstrate substantial improvements over the baselines.
2. The paper is well-written and easy to follow.

### Weaknesses
1. Since partial programs are imperative, the semantic annotations include the results of executing each line of code on example inputs, which can grow combinatorially. The paper does not address the limitations of this approach, particularly given the limited window size in LLM prompts and the increased risk of hallucination as prompt size grows. Specifically, the paper lacks a discussion on how the size of the execution traces impacts the performance and scalability of the method. The authors should provide an analysis of the relationship between the number of intermediate execution results and the accuracy of the synthesized code, especially as the complexity of the target programs increases.
2. The baselines, which use unrestricted and straight-line constraints without search or annotations, may not fully highlight the method's advantages. Incorporating other PBE or LLM-based synthesis techniques with integrated search mechanisms could be helpful. For instance, comparing against methods that use explicit backtracking or iterative refinement strategies would provide a more comprehensive evaluation of the proposed approach. The current baselines do not adequately isolate the specific benefits of the within-prompt search mechanism.
3. The paper's within-prompt search mechanism utilizes an implicit backtracking method, but it’s unclear how effectively this avoids redundant or cyclic paths, which could degrade efficiency. The paper does not discuss the potential for the search to explore semantically equivalent paths, which could lead to wasted computation and increased prompt size without improving the quality of the generated code. A more detailed analysis of the search space exploration is needed.

### Questions
1. Does this approach work only for imperative programming? It seems it might be more suited for functional or recursive code structures.
2. In Line 244, you mention, “We remove any duplicate lines of code based on their execution results.” Does this apply even if lines are syntactically or semantically different beyond the given examples? Could this lead to false negatives in your experiments?
3. Does your approach inherently favor simpler solutions, or can it dynamically adjust priorities based on feedback? Can you do an analysis on the complexity of the synthesized programs? 
4. Since the paper uses standard PBE benchmarks, it would be beneficial to include comparative results from other approaches (e.g., traditional program synthesis methods) on these benchmarks.
5. How does the method handle dead ends—situations where intermediate results do not align with any possible valid completion? A deeper discussion on techniques like pruning unpromising paths or resetting to prior valid states would improve your paper.
6. What do the confidence belts represent in Figure 5?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper proposes a framework to solve PBE by searching for programs by generating lines of code in straight-line program style. When generating the next lines, they consider the partial program generated so far and its corresponding execution state to generate the next line. The LLM here acts as a policy to generate the next action, i.e., line of operation. They show that LLMs with this framework can increase both solving rate and consistency of solving.

### Strengths
* The paper demonstrates that the search and execution improve the performance on different datasets across lists, strings, and basic python programming
* The paper's framework is clean and can be generalized to other programming languages or domains where execution state can be compactly represented

### Weaknesses
 * Issues with the baselines and comparison
  * There is a simple LLM PBE baseline: search by sampling entire programs and then executing to find the right program satisfying the input-output assertions. For the baseline LLM results ("Free" in the figure), they did not do multiple samples and execution. Because the paper proposes to use line-by-line search/generation and execution to find the program satisfying the input-output, it would be better to know how it compares against a simple entire program resample and execute approach without the proposed line-based search.
  * Other neural or symbolic baselines not presented: they use PBE benchmarks from the symbolic methods literature (flashfill++, playgol, list) but their performance is not listed, so readers would not know if using LLM as a search policy is actually better than traditional methods doing program search.
* The paper only uses one model to perform experiments (GPT-4). It would be nice to add results for other models, especially open models or smaller ones, to see if open models can reproduce the results and whether the model size/capability would affect the effectiveness of the approach.

* The baselines used in the paper appear to be significantly weaker than what has been reported in prior work. For example, the SyGuS benchmark results of approximately 75% are considerably lower than the 94% reported in the Hypothesis Search paper [1], which also uses a direct program generation approach with a limited number of samples. This discrepancy raises concerns about the strength of the baselines used for comparison.
* The exclusive use of GPT-4o for evaluation is a significant limitation. While the authors acknowledge this in the limitations section, it is crucial to demonstrate the generalizability of the proposed method across different LLMs. Given the availability of other LLMs with comparable coding capabilities, it is important to verify whether the method's performance is specific to GPT-4o's architecture or training, or if it can be replicated with other models, including open-source options.

### Questions
- It is not clear how the LLM determines which states (partial programs) to expand. Could you lay out the algorithm of the propose framework so it can be less ambigous? Are all the partial programs being expanded with k actions in the default policy setting?
- "Without execution, the model backtracks less, as it does not realize that the current operations $o_{<i}$ are dead ends, and as such performs worse (see Figure 2)." Can you clarify the mechanism of backtracking? Does backtracking only happen when pruning based on the most recent `k` operations? How is the pruning parameter `k` set?
- How do you ensure that there are no statements with side effects modifying the states, e.g., v3 = (v2=1) then v2 is modified?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper targets a form of program synthesis called programming by example (PBE). The setup includes a specification, given via assert statements that encode the input and their respective outputs. The paper proposes an execution-guided technique to guide the synthesis of the program using LLMs by executing each statement of the generated code and providing the result in the prompt itself to inform the generation of the next statement. The paper compares this technique with standard prompting techniques and show that the execution and search strategy improves program accuracy using GPT-4o as the base LLM.

### Strengths
In general, I really like the idea of enabling PBE-style code synthesis with LLMs, especially the implications if we combine PBE with typical NL specifications. I also think the overarching contribution of specifying individual execution results within the prompt is good, and it allows for more fine-grained feedback while generating lines of code.

### Weaknesses
I feel that while the core ideas proposed are neat, the paper lacks clarity and depth in terms of explaining the technique proposed and evaluating it. I'll describe my major complaints below.

## Technique

This section does not do a good job explaining the proposed technique clearly. The text is dense and filled with technical notation, but understanding how they interact and play with each other is not easy. It would have been better to include a diagram of all the phases that contained more details than Figure 1, or even better, an algorithm defining each phase and the steps within the phase along with supporting text.

There are also several poorly defined terms and inconsistencies in notation (defining what a policy, value, program, function, operation, etc. are). Furthermore, the cyclic nature of the technique shown in Figure 1 is not explained in Section 3, so I have no idea how the search space is represented within the prompt, how it grows with each response from the LLM, how it is pruned, to what extent can it be pruned, how backtracking works here (the text doesn't describe backtracking but instead describes operations being pruned).

In summary, section 3 provides some context and details but getting the full picture of the system is very difficult. The paper is significantly under the page limit, so it should be able to clearly detail the entire system without sacrificing the details it already presents.
I have asked specific clarifying questions in the Questions section.

## Evaluation

### Baselines and Benchmarks

The evaluation in this paper is lacking. Even before getting into the details, this paper only evaluates its technique over a single base LLM model. At minimum, I would expect more LLMs of varying techniques and sizes to show up in the evaluation. Also, I would like a more in-depth evaluation of different prompting techniques: standard prompting is just not enough. At minimum, chain-of-thought prompting needs to be there, since it is a pretty standard approach, and I would appreciate other baselines that may directly compare with this paper (some alternate PBE techniques are mentioned in the background section). I do like the diversity of the datasets being evaluated. However, I would like more details about the benchmarks and why they were chosen: what are the challenges that each benchmark provides? How many examples do you need to give, and is it different for each benchmark? what language is each benchmark targeting? etc.

### Metrics

The metrics are not defined properly. First, the pass@k metric has a very specific definition already established in the Codex paper[1]. This metric samples the top k responses from an LLM and measures the probability of at least one sample being correct. That means the metric used in the paper is more like pass@8 (since it is considering 8 responses, but I am not sure if that is necessarily the top-8 responses), or equivalently pass@3. I would like to know the results for different values of k for all baselines with and without search and execution. I also don't think all@3 metric has been defined, nor has the notation being used in 4.3 (line 307/308) been defined.

### Results

I would like a bit more insight drawn from the results. For instance, why does SyGuS have a lower performance for +S+X versus +X? Is there any reason SyGuS and Playgol  have higher accuracies for +X versus +S, while for other datasets it is lower? Also how does standard CoT prompting perform here?

In figure 3, what do the horizontal lines indicate? What exactly does a backtrack mean for Figure 4? What is the difference between WPS and Straight/Free? And in Figure 5, what does it mean by average number of sampled operations? I thought in each case a fixed number of operations were sampled?

## Miscellaneous

In general, there are several grammatical mistakes throughout the paper that make reading it a bit difficult. This is not as major from a technical standpoint, but it is important to correct them.

I also think the background section and related work can be explored more. Especially in related work, explain how your technique contrasts with those existing techniques, and why they are not included in the evaluation. I also think there needs to be a section that talks about LLMs for code generation as well, not just PBE.

### Questions
These are mainly questions to clarify issues I have from section 3, but please also respond to the concerns from the Weakness section.

1. What is the concrete definition of a policy and a value? And what is the difference between an actual value and a value network?
2. What does an operation mean as far as actual code is concerned? i.e. is it a token, statement, code snippet, etc?
3. What is the difference between P(x) and P_j? And is P_j a partial program or a representation of the entire explored search tree at this point?
4. At each stage, you generate operation o_j as per 3.1. But you calculate expectation wrt P_T, which "is a sequence of operations sampled from the (prompted) policy". So is P_T actually sampled at each point on top of o_j, or is P_T just a statistical notion of the possible ways to complete the current program P_{j-1} o o_j?
5. What constitutes an iteration? Is it the entire process included in steps 1--4 from Figure 1 or is it the generation of a single operation?
6. How is the search space explored? Is it more of a BFS search or a DFS search? I notice mentions of backtracking in 3.4 so I assume it is a form of DFS, but in this case how does the backtracking work? At each point does the LLM generate just the response to one unexplored node or responses for all unexplored nodes? and what is the size of the search tree in general? I'd assume it blows up in complexity for large target programs which is why there is the pruning used. Furthermore what do you mean by "operations not used" as far as pruning is concerned? In general I think you can do a better job in section 3 by grounding each step with an example, or at least referring back to Figure 1 on top of a general algorithm.
7. Do you have any safeguards against executing problematic/malicious code? How about results of for loops, incomplete branches, and more complex control flows that may not necessarily terminate?

### Soundness
2

### Presentation
1

### Contribution
2
