# Planning-Driven Programming: A Large Language Model Programming Workflow

- Decision: Reject
- Scores: 8, 5, 3, 3

## Abstract
The strong performance of large language models (LLMs) on natural language processing tasks raises extensive discussion on their application to code generation. Recent work suggests multiple sampling approaches to improve initial code generation accuracy or program repair approaches to refine the code. However, these methods suffer from LLMs' inefficiencies and limited reasoning capacity. In this work, we propose an LLM programming workflow (LPW) designed to improve both initial code generation and subsequent refinements within a structured two-phase workflow. Specifically, in the solution generation phase, the LLM first outlines a solution plan that decomposes the problem into manageable sub-problems and then verifies the generated solution plan through visible test cases. Subsequently, in the code implementation phase, the LLM initially drafts a code according to the solution plan and its verification. If the generated code fails the visible tests, the plan verification serves as the intended natural language solution to consistently inform the refinement process for correcting bugs. We further introduce SLPW, a sampling variant of LPW, which initially generates multiple solution plans and plan verifications, produces a program for each plan and its verification, and refines each program as necessary until one successfully passes the visible tests. Compared to the  state-of-the-art methods across various existing LLMs, our experimental results show that LPW significantly improves the Pass@1 accuracy by up to 16.4\% on well-established text-to-code generation benchmarks, especially with a notable improvement of around 10\% on challenging benchmarks. Additionally, SLPW  demonstrates up to a 5.6\% improvement over LPW and sets new state-of-the-art Pass@1 accuracy on various benchmarks, e.g., 98.2\% on HumanEval, 84.8\% on MBPP, 64.0\% on APPS, and 35.3\% on CodeContest, using the advanced LLM GPT-4o as the backbone.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
The paper introduces the LLM Programming Workflow (LPW) and LPW with Sampling (SLPW), which is a 3-stage agentic framework to solve function-level NL-to-Code problems like HumanEval and MBPP. The 3 stages are:

1. **Plan Generation**: the backbone LLM is prompted to generate a step-by-step natural language plan for implementation
2. **Plan Verification & Refinement**: the backbone LLM is prompted to simulate the steps in the natural language plan on visible tests, compare the simulated output against the expected output, and (optionally) self-refine the plan until a self-verified plan is generated.
3. **Iterative implementation & Refinement**: the backbone LLM is prompted to implement the solution given the self-verified plan, and (optionally) self-refine the implementation given various feedback: failed hidden test case, expected output, execution trace, explanation of failure, and revised-and-verified plan.

Experiments demonstrate that LPW and SLPW outperform Self-Planning [2], Self-Debugging [3], and LDB [4] when using GPT-4o, GPT-3.5, Llama-3, and Phi-3 as the backbone model.


[1] [Parsel: Algorithmic Reasoning with Language Models by Composing Decompositions](https://arxiv.org/abs/2212.10561)

[2] [Self-planning Code Generation with Large Language Models](https://arxiv.org/abs/2303.06689)

[3] [Teaching Large Language Models to Self-Debug](https://arxiv.org/abs/2304.05128)

[4] [Debug like a Human: A Large Language Model Debugger via Verifying Runtime Execution Step-by-step](https://arxiv.org/abs/2402.16906)

[5] [NExT: Teaching Large Language Models to Reason about Code Execution](https://arxiv.org/abs/2404.14662)

[6] [CRUXEval: A Benchmark for Code Reasoning, Understanding and Execution](https://arxiv.org/abs/2401.03065)

### Strengths
## Novelty

The paper successfully integrates previous working methods, Self-Planning [2] and Self-Debugging [3], into the LPW framework. In addition, LPW novelly introduces the "Plan Verification & Refinement" stage to iteratively refine the quality of the plan.

## Effectiveness

The LPW framework demonstrates substantial improvements over previous agentic frameworks like Self-Planning [2], Self-Debugging [3], and LDB [4].



[1] [Parsel: Algorithmic Reasoning with Language Models by Composing Decompositions](https://arxiv.org/abs/2212.10561)

[2] [Self-planning Code Generation with Large Language Models](https://arxiv.org/abs/2303.06689)

[3] [Teaching Large Language Models to Self-Debug](https://arxiv.org/abs/2304.05128)

[4] [Debug like a Human: A Large Language Model Debugger via Verifying Runtime Execution Step-by-step](https://arxiv.org/abs/2402.16906)

[5] [NExT: Teaching Large Language Models to Reason about Code Execution](https://arxiv.org/abs/2404.14662)

[6] [CRUXEval: A Benchmark for Code Reasoning, Understanding and Execution](https://arxiv.org/abs/2401.03065)

### Weaknesses
## Novelty

Most design choices in LPW have been established and analyzed in previous works: the 1st stage "Plan Generation" is drawn from Self-Planning [2], and the 3rd stage "Iterative implementation & Refinement" follows various prior works [3, 4, 5], especially regarding the feedback mechanisms.

The main novel contribution of LPW lies in its 2nd phase, "Plan Verification & Refinement," making the paper’s overall novelty contingent on the soundness and effectiveness of this one component.



## Soundness

The self-verification process is essentially the LLM simulating the natural language plan on a visible input test case and trying to predict the output. While conceptually appealing, this task is inherently challenging for LLMs as shown by the CRUXEval benchmark [6].

In CRUXEval, the models are tasked to predict the output given an input and a very simple program (no imports, limit on input length, limit on program length). In the setting of LPW, the models are dealing with a more challenging case of predicting the outputs given an arbitrarily complex input and a natural language plan.

For example, if we replace the visible input test case in Figure 5, [-3, -4, 5] with a lengthy list of large integers like [2890, 4719, 1230, 2309, 240, 2190, 34789, 91, 12, 928, ...], it's hard to imagine that the LLM will be able to predict the correct output, even though the nature language plan is simple enough.

It'd be highly beneficial for the author to conduct an in-depth analysis of the quality and reliability of the self-verification process. Some key metrics can be:

1. **Type I Error Rate**: What's the percentage of plans that are correct but get verified as incorrect?
2. **Type II Error Rate**: What's the percentage of plans that are incorrect but get verified as correct?

The current ablation study, represented by LPW-C, ablates both the 1st and 2nd stages, which does not isolate the specific effectiveness of the "Plan Verification & Refinement" stage.

Additionally, separating the effects of "Plan Refinement" and "Plan Verification" could provide further valuable insight. For instance, what would the performance be if the model only performed self-critique and self-refined the plan without simulating it on visible test cases to predict outputs?

Given these observations, the current version of the paper does not fully justify the soundness of its main novel contribution, "Plan Verification & Refinement."

This aspect has the most impact on my Overall Rating, Soundness Rating, and Contribution Rating. I would be glad to reconsider and potentially raise my scores if the authors could address the above concerns.



## Significance

Although LPW demonstrates superior accuracy compared to existing agentic frameworks, it also requires more model calls, potentially increasing the time and financial costs associated with solving each problem. This may impact LPW’s practical applicability in real-world settings where efficiency is critical.

It would be beneficial if the authors could provide an analysis comparing the efficiency and cost of LPW and SLPW with baselines such as Self-Debugging, LDB, LPW-S, and LPW-C. In terms of cost-performance ratio, which framework is the best?

This aspect has a secondary impact on my Overall Rating and Contribution Rating. I would be glad to reconsider and potentially raise my scores if the authors could address the above concerns.


### Questions
## Clarification Questions

In Section 7, the paper states that previous iterative refinement frameworks **"encounter difficulties when the initial code substantially deviates from the original intent"**.

What are the commonalities among problems that LPW solved but LDB failed? Can the LDB failures be attributed to the quality of the initial plan?

It would be better if the authors could provide an error distribution analysis of those problems and demonstrate some examples.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper propose an LLM programming workflow (LPW). The key point of this framework is the plan propose phase and the plan refinement based on visible tests. Then LPW will implement the code based on the verified plans. The refined plan also can help refine the code when the generated code cannot pass the visible tests. It also presents SLPW, which is  a sampling variant to generation multiple solutions and refine as necessary. The results show improvements on benchmarks like HumanEval, MBPP, APPS and CodeContest.

### Strengths
1. This paper presents a well-designed framework. The technical details are solid and easy to reproduce.
2. This paper is presented clearly, illustrating the methods greatly.
3. The authors conduct a series of experiments, which is of great soundness.

### Weaknesses
1. The key point of LPW is the plan proposal and refinement based on visible tests. However, I'm not fully convinced about the refinement capability of plans since it is fully dependent on LLMs. The authors ask the LLM to dry run the plan through the test input, which in essence is a reasoning problem. It would require the LLM to be great at reasoning that it can dry run the operations and get the 'real output' and compare it with the 'grounded output'. Otherwise, it could derive wrong results even when the plan is correct (hallucination). 
If the dry run on plans gives incorrect results, it will fail in result comparison and lead to refinement on correct plans and possibly ends up with a wrong plan. Therefore, I'm a bit curious about the accuracy of the LLM plan dry run, and the accuracy of LLM verficiation checks. Also, what is the authors' insight to improve this accuracy to alleviate the hallucination problem? More ablation study on this would be helpful. Also since the plan acts an important role in LPW, it would be beneficial to sho how many iteration number it takes to refine the plan.

2. The other part of this paper has limited novelty: compared to the related works mentioned in this paper, it seems the paper aggregates these methods to achieve high performance. While this is valuable in real-world applications, the lesson from this is limited. More illustrations on the design choice would be valuable.

3. For SLPW, it is similar to 'pass@k' version of LPW. The author use the UCB algorithm to help decide whether to explore. I'm curious about the effectiveness of the UCB methods here compared to simply selecting the code with the most passed tests.

### Questions
1. Could you illustrate the accuracy of the LLM plan dry run and verification checks?
2. Compared to verify the code intermediate results, what is the benefit of verifying plans directly? How to guarantee the intermediate results generated by LLM reasoning is correct?
3. Could you illustrate more on why choosing the UCB algorithms over simply selecting the code passing the most visible tests?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes an LLM "programming workflow" that the authors dub LPW.
The key idea is to decompose code generation into a sequence of distinct tasks:
- "Planning" how to solve the problem (e.g. coming up with the "architecture" of the solution)
- Constructing the initial code
- If the initial code does not pass the tests:
  - Compare the execution trace to the "plan" to find the bug (note this treats the plan as gold truth)
  - Fix the program
In addition, given the importance of the "plan", the authors include a verification step where an LLM steps through the plan and ensures an implementation thereof will match the specification.

In terms of results, the experiments focus on standard, self-contained Python programming benchmarks such as APPS, HumanEval, MBPP and CodeContests. The authors claim to improve the pass rate compared to several benchmarks including simple self-debugging and one prior agentic approach, but I do not have much confidence in the veracity of their claims (see weaknesses).

### Strengths
This is an important research area, and projects such as this may have a big impact for practitioners.
I believe this paper also includes some novel and interesting ideas, such as comparing the plan to the execution trace during debugging (to help the LLM reason about what went wrong), as well as (in the "sampling" version, SLPW) using a technique from the bandit literature (UCB) to select the set of plans to attempt to implement based on the number of unit tests that the plan is consistent with.
The methodology is mostly clear (see weaknesses) and the writing is good; the authors also do a good job calling out to related work

### Weaknesses
Unfortunately, I was gravely disappointed by the analysis of the experiments in this paper.
In their current form, I do not believe they are meaningful in any real sense - i.e., I don't think they accurately assess how this approach compares to simple baselines like just sampling IID from the model with a higher temperature. Reading lines 338-345 I believe anyone familiar with the code generation literature would immediately realize that the comparisons to the other methods will be unfair.

In particular, the approach fundamentally involves drawing multiple samples from the model - one to construct the plan, one to verify it, one to generate the code, one to compare the trace to the plan (if the code failed), and one to fix the program - and yet the authors label the pass rate of the *final* program as "pass@1", which is incredibly misleading as pass@1 has an established meaning in the literature - the expected pass rate of *one* sample from the model.
Some of these additional calls to the LLM can be coalesced, but some of them cannot.
In particular, anything before execution can obviously not be coalesced with anything that comes after.
As a first order of approximation, it thus seems more fair to compare "pass@1" from LPW with pass@2 from the baseline, but even this does not adequately capture the fact that you have to sample a bunch of additional tokens to construct and verify the plan (in addition to the program).
This is made even worse in the "sampling" variation of the method, where at each point you branch (and, thus, end up with a whole tree of samples from the model).

Evaluating these agentic systems fairly is hard, but there has been much prior work in the literature that has at least **attempted** to account for the additional costs involved (e.g. [1, 2]); sadly this paper is not one of them.
There is only one instance in which I can imagine that the current evaluation strategy would make sense, and that is if LPW was able to solve programs that the baseline *never* could, in which case cost would be irrelevant.
There may or may not be a handful of such tasks in CodeContests, but there certainly are none in APPS, HumanEval or MBPP considering the extensive contamination these aging datasets have been exposed to.

I want to emphasize that there are some interesting nuggets in this paper, and I commend the authors for their effort.
Nonetheless, I truly feel that the experiments are so unfair that they are meaningless, and thus have no choice but to reject the paper in its current state.
I encourage the authors to think more carefully about how to fairly evaluate their system against the different baselines in a way that takes the different costs into account; note that doing so would not require running any more experiments, just changing how you analyze the results (assuming you didn't throw the data away, that is). Concretely, one way to approach this might be to compare pass rates versus the total number of tokens sampled from the model, as proposed in [2].

### Questions
- Have you considered some way of quantifying the computational cost (e.g. the number of samples drawn from the method) of each method?
- If you took the cost of each method into account, how would LPW and SLPW compare against the baselines?
- Given the relative age of the benchmarks used, what impact (if any) do you think data leakage/contamination may have on your conclusions?

### Soundness
1

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper presents a planning driven approach for the code generation problem. The exact setting is to generate code for a completely specified task, where some number of “visible” test cases are provided. The main idea in the paper is to use a planning approach driven by human software engineering practices, adding a design phase before the actual code generation phase. The design consists of a set of high-level steps with well-defined input-output behavior, and the code generation phase generates code for each high-level step. 

The key insight here is that using a design verification step, where the execution of the designed solution is simulated to ensure that the plan is sound. Errors can be caught at an early stage during the design phase if the simulated execution on the visible test cases does not produce the expected results. The authors present two versions of their technique – one where each phase generates one single option, and the other where a sampling approach is used over to explore multiple possibilities for both the design plan and the implementation.  

The authors compare their solution to one baseline (LDW) and show improvements over it for a number of models of varying capabilities including GPT-3.5, Llama-3, Phi-3, and GPT-4o.

### Strengths
+ Well-motivated technique 

+ Improved results of baselines

### Weaknesses
 - Choice of baselines: I am a little baffled by the choice of baselines. The techniques compared against are mostly targeted at debugging, not code generation. Why not pick a few of a plethora of the other code generation techniques: AgentCoder, MapCoder, CodeChain, WizardCoder, etc? If there is a specific reason why this is being done, it needs to be discussed in detail in the paper.  

- Choice of benchmarks: The main evaluation is done on a very simple set of benchmarks. The MBPP and HumanEval datasets are more or less “solved”, and cannot be the basis for evaluating a planning driven technique. I would suggest that the authors do the deeper analysis on the APPS and CodeContests dataset, as well as consider what fragments of other datasets such as swebench will be applicable in the current setting.  

- Flawed evaluation: Even with the chosen baselines and benchmarks,
** The improvements reported in the paper are in the order of a few percentage points. However, LLM-driven techniques, especially complex iterative ones with multi-step planning and reasoning, often have variance similar or larger than this. It is very hard to evaluate the gains without any reporting of variance or standard deviations. 
** Why aren’t SD and SP used for the advanced APPS and CodeContests evaluations? 
** The plots in figure 4 are very misleading -- having a non-zero value as the origin is one of the hallmarks of misleading reporting. At a glance, it makes the empirical improvements seem much better than they are.
** No reporting of cost-to-performance analysis. Does the improved performance of the current techniques come with an increased cost? If so, how much is this increased cost? 

- Related work: There is insufficient discussion of related work, both specifically about code generation as well as general software engineering tasks. For example, there is a large body of recent work targeting the SWE-bench dataset that is arguably harder than the datasets chosen for comparison. There are planning works targeted at both targeted coding tasks and repository-level tasks (Bairi et al. FSE 2024, Zhang et al. ICLR 2023, etc) which are not discussed.  

- Comparison to human software-engineering processes: The technique is presented as an analogue of waterfall and scrum software engineering processes. However, these processes are much more about human-centric planning. For example, scrum specifically prescribes the ideas of sprints, the idea of decision-making by lowest level actors, planning granularity and timelines, etc. None of this translate to the current solution – in particular, the lowest level actor (i.e., the implementation agent) cannot make design decisions here. Further, the waterfall model is generally considered an undesirable practice – hence, I am not sure why that would be a good inspiration. I believe the authors are making a different point about design before implementation, which needs to be stated clearly.

### Questions
1. Have you considered the possibility of going back to the design/planning phase if certain implementations become infeasible? 

2. There is no discussion of limitations in the paper. It is unclear where this technique would and would not be suitable. For example, can we use this for code editing as well? Also, consider moving the unsolved problem analysis into the main paper. 

3. Please comment on the selection of baselines and datasets in the evaluation.

### Soundness
2

### Presentation
3

### Contribution
2
