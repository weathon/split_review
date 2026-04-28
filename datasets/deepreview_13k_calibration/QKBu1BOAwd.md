# From Exploration to Mastery: Enabling LLMs to Master Tools via Self-Driven Interactions

- Decision: Accept
- Avg Score: 7.33
- Scores: 8, 8, 6

## Abstract
Tool learning enables Large Language Models (LLMs) to interact with external environments by invoking tools, serving as an effective strategy to mitigate the limitations inherent in their pre-training data.
In this process, tool documentation plays a crucial role by providing usage instructions for LLMs, thereby facilitating effective tool utilization.
This paper concentrates on the critical challenge of bridging the comprehension gap between LLMs and external tools due to the inadequacies and inaccuracies inherent in existing human-centric tool documentation. 
We propose a novel framework, \textbf{\ourmodel}, aimed at \textbf{\underline{D}}ynamically \textbf{\underline{R}}efining tool documentation through the \textbf{\underline{A}}nalysis of \textbf{\underline{F}}eedback and \textbf{\underline{T}}rails emanating from LLMs' interactions with external tools. 
This methodology pivots on an innovative trial-and-error approach, consisting of three distinct learning phases: experience gathering, learning from experience, and documentation rewriting, to iteratively enhance the tool documentation.
This process is further optimized by implementing a diversity-promoting exploration strategy to ensure explorative diversity and a tool-adaptive termination mechanism to prevent overfitting while enhancing efficiency. 
Extensive experiments on multiple datasets demonstrate that \ourmodel's iterative, feedback-based refinement significantly ameliorates documentation quality, fostering a deeper comprehension and more effective utilization of tools by LLMs.
Notably, our analysis reveals that the tool documentation refined via our approach demonstrates robust cross-model generalization capabilities.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper highlights the importance of proper tool documentation to improve tool learning. Due to incomplete documentation or consideration of human intuition, tool documentation may not include all the information to be useful for an LLM. To resolve these issues, the paper proposed DRAFT that iteratively gathers ‘experience’, learns from it, and rewrites the documentation for future usage.

### Strengths
1. DRAFT significantly outperforms across two benchmarks and outperforms three baselines.
2. It also verifies the results through a small human study — showing its effectiveness in practical use cases.
3. The paper provides an in-depth analysis of the impact of iteration count on the performance as well as the improved performance for retrieval in the rewritten documentation.

### Weaknesses
1. According to the first contribution highlighted in the introduction, DRAFT highlights ‘inefficiencies and inaccuracies within existing tool documentation hamper the effective utilization of tools by LLMs’. However, the paper does not show any quantitative evaluation of this claim rather than explaining the problems associated with it. Hence, I think the ‘highlight’ itself may not be a novel contribution as much as the framework.
2. For ‘tool-adaptive termination mechanism’, is it possible to measure the impact of different threshold on the performance of DRAFT?

### Questions
1. The paper highlights how the count of iteration impacts the performance of DRAFT mentioning - ‘a decline in performance is observed after a certain number of iterations. This decline may be attributed to the introduction of redundant information as the number of iterations increases, potentially leading to overfitting’. Is it possible to measure the count of redundant information in the system? It would be nice to see some sort of hallucination error measurement on top of DRAFT.

### Soundness
3

### Presentation
4

### Contribution
4

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper addresses the tool usage challenge for LLMs. The core idea is to develop a explore-analyze-rewrite approach to refine tool documentation to improve LLMs' ability to use tools that may have lower quality documentation. To enhance tool documentation refinement, DRAFT encourages diverse queries to try out different queries to trigger different tool behaviors; these execution results are then leveraged into the analysis phase for documentation rewriting. 

DRAFT is evaluated on ToolBench and RestBench, results on CP% and WIN% shows that the refined document improves task completion, especially compared to closely related EasyTool. Detailed analysis of iteraction rounds, ablation results on diversity and adaptive shows significance of features in DRAFT. Also, it's interesting to learn that refined document could also potentially benefit tool retrieval and human understanding.

### Strengths
This paper provides a well designed approach for improving LLMs' tool using ability without additional training. The document refinement approach, while not new, is well designed considering how to leverage LLMs' self-reflection ability and trial-and-error approach to enhance document quality. This paper has the following strengths:

1. Leveraging diversity of exploration and trial-and-error to compensate potential limitation of the the initial document. Where other refinement approach like EasyTool may not be able to obtain such extra information.
2. The evaluation has fair comparison with related work to highlight performance gain. The detailed analysis show additional benefits of this approach.

### Weaknesses
This paper can be improved upon the following two areas:

1. Please elaborate more in detail about Explorer design and evaluation. DRAFT relies on diverse queries/parameters to trigger different tool behaviors. It looks like the query generation depends on LLM to sample parameters automatically based on tool signature as provided by toolbench. It would be ideal to analyze how diverse in terms of parameter coverage, especially for certain types of parameter like arrays / strings. I imagine if the document is indeed incomplete as mentioned in the intro, these special cases may be less likely going to be hit during exploration. While existing benchmarks conveniently provide well defined parameter domain, it would worth the authors to include in the discussion about how to generalize this for tool documents without good parameter documentation.

2. The exploration-revision loop essentially helps the system to collect more input-output examples that previously doesn't exist in the document. A qualitative analysis between examples generated by revision-only based tool like EasyTool and new examples generated by DRAFT would be helpful to understand this nuance difference.

3. The intro motivates different types of documentation limiations (incomplete, redundant, inaccurate), it would be good to provide qualitative feedback about which scenarios DRAFT is best at improving, especially comparing to prior tools.

### Questions
Check above. In general, this paper is well written, and the experiments are quite convincing to me. Please check above for clarifications about (1) parameter space exploration, (2) analysis of example quality and (3) types of documentations DRAFT best at targeting comparing to others.

### Soundness
4

### Presentation
3

### Contribution
4

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This work introduces a new prompting workflow for improving tool documentation iteratively called DRAFT. While prior tool documentation is typically iterated on manually and laboriously, this work focuses on automating the process of improving documentation via a three step procedure that can be repeated multiple times. The outputs of prior phases (e.g. Explorer, Analyzer) are fed into subsequent phases (Analyzer, Rewriter), where each phase produces prior experiences and filtering that is then used to refine the prompt further. To encourage diverse exploration and ensure that DRAFT terminates at some point, the authors introduce new strategies that encourage such convergence. Following the experimental setup of prior works, the authors show that DRAFT outperforms previous interactive prompting methods and run ablations demonstrating the effect of different parameters and effects of DRAFT.

### Strengths
The motivation established by the authors is sound and makes sense. In addition, the formalizations introduced in Section 2 make it easy to follow how the outputs on one prompt feed into the next. The use of an exploration phase is interesting, similar to fuzzing of a program for software engineering tests. The experiments are sound and it follows prior works. The related work covered by the authors is quite comprehensive. The ablations are complete, as the authors do a good job examining the several parameters of DRAFT.

### Weaknesses
 - While they are clearly thoughtfully made, I would recommend Figures 1 and 2 be simpler to make it easier for a reader to understand what is going on. The captions would also benefit from being more specific about what is going on in the diagram. For instance, for Figure 2, I did not understand what “Trail” (I think this was supposed to be “Trial”?) refers to, is it an iteration of explorer/analyzer/rewriter?
- The methodology section, while clear in how the symbols relate to one another, feels somewhat ungrounded in terms of why certain equations or prompt templates were used. For instance, on line 299 - “when the documentation is adequately aligned with comprehension” - what does this mean? What is adequately aligned? I think introducing more citations and explanations for why contributions such as the diversity and termination mechanisms would be needed for a more rigorous justification of why this method is interesting, and not just a prompt based workflow that happens to work.
- DSPy (Khattab 2022) performs prompt optimization with multiple rounds of trial/error against a validation set. What makes DRAFT different from DSPy as a prompt optimization technique?
- Although the method is proven to be effective in the experimental results, I think it would be nice to see, qualitatively, the effects of better documentation on downstream performance. While it seems that DRAFT improves the quality of the documentation, it is not obvious why better documentation improves empirical performance. For instance, it may also be possible that more “concise” documentation does not necessarily lead to improvements in downstream performance.

### Questions
- Equation 1: What is M? Is this supposed to be A, the Explorer?
- Line 209: How do the two components come together to make up the diversity promoting exploration strategy? Two different constraints were explained, but how do they come together to promote diversity? Is this explicitly included in Algorithm 1 somewhere? Also, is there any citation or support for why self-reflection would promote diversity? How do we know this works?
- Equation 3: Again, what is M?
- Line 281 - “Analogous to recipes requiring different levels of expertise, some tools may reach optimal documentation faster than others”. Any citation for this? What is “optimal” in this case? Also, what does faster mean? Is it in terms of the number of trials? Or the number of explorations needed?
- Equation 5: How did you come up with this? Ignoring empirical performance, why does similarity score + BLEU score work for measuring the degree of change? Why are they weighted equally (e.g. why not weigh surface form similarity / BLEU higher than semantic similarity?)
- Experimental Setup: How many rounds of DRAFT iterations were run (did DRAFT ever not terminate within a certain number of steps)? Were the initial documentations the original ones from DFSDT or ReAct?
- Typo Line 326 - “EayTool”
- The human study detailed in Line 473 onwards feels like it could be better explained. Are the doctor-al (Line 477) students part of the author group? What examples or guidelines did the human annotators use to judge the three criteria correctly? Did the human annotators generally agree with each other (Fleiss Kappa score)?
- Section 2 read a bit repetitive at times - was this section written with the assistance of a language model? It may be easier to read with less redundancy. Specifically, the beginnings of each of the subsections essentially repeat what was stated in the introduction and prior subsections.

### Soundness
2

### Presentation
3

### Contribution
2
