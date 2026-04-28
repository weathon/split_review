# DRoC: Elevating Large Language Models for Complex Vehicle Routing via Decomposed Retrieval of Constraints

- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 8, 6, 6

## Abstract
This paper proposes Decomposed Retrieval of Constraints (DRoC), a novel framework aimed at enhancing large language models (LLMs) in exploiting solvers to tackle vehicle routing problems (VRPs) with intricate constraints. While LLMs have shown promise in solving simple VRPs, their potential in addressing complex VRP variants is still suppressed, due to the limited embedded internal knowledge that is required to accurately reflect diverse VRP constraints. Our approach mitigates the issue by integrating external knowledge via a novel retrieval-augmented generation (RAG) approach. More specifically, the DRoC decomposes VRP constraints, externally retrieves information relevant to each constraint, and synergistically combines internal and external knowledge to benefit the program generation for solving VRPs. The DRoC also allows LLMs to dynamically select between RAG and self-debugging mechanisms, thereby optimizing program generation without the need for additional training. Experiments across 48 VRP variants exhibit the superiority of DRoC, with significant improvements in the accuracy rate and runtime error rate delivered by the generated programs. The DRoC framework has the potential to elevate LLM performance in complex optimization tasks, fostering the applicability of LLMs in industries such as transportation and logistics.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This work is along the popular direction of using LLM to automatically generate modeling code and then call solvers in the backend to solve the problem. Specifically, it proposes a novel framework that enhances LLMs in code generation to solve complex vehicle routing problems (VRPs) with intricate constraints. Traditional LLMs perform well on simpler VRPs but struggle with complex versions due to a lack of embedded domain-specific knowledge. The proposed DRoC framework addresses this by using a retrieval-augmented generation (RAG) approach to incorporate external knowledge for constraint modeling.

### Strengths
The problem is well motivated. It is important to be solve different variants of VRP problems. From the numerical results, it appears that with the proposed approach, the accuracy of modeling is improved substantially.

### Weaknesses
1. The RAG technique is common for code generation. What is the challenge of applying RAG in solving VRP? The novelty of this paper is limited.
2. In practice, there are also other variants of VRP which cannot be solved immediately by the solvers. The paper does not address the case where the problem at hand cannot be solved by the VRP solver.

### Questions
1. What happens if the given VRP variant cannot be solved by the solver?
2. In the experiment, the authors use "optimality gap" as a criterion. Is the feasibility verified first? Otherwise we would have objective value that is not feasible, or even lower than the optimal value of that problem.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The work proposes a framework for solving complex vehicle routing problems using LLMs. The framework's novelty is decomposed retrieval of constraints, where the VRP's constraints are decomposed into individual constraints, and then relevant conditioning documents are retrieved, and code generation is conditioned on those documents.

### Strengths
The  work combines an algorithmic solution with queries to LLM to solve challenging problems of operation research. The algorithms are described in detail, and accompanied by extensive empirical evaluation and ablation study.

### Weaknesses
Update: authors' clarifications and answers are quite convincing. Updating my evaluation accordingly.

Introduction: vehicle routing problems in computer science are not formulated or solved to route vehicle, contrary to what the introduction says. Many VRPs are hard problems to which other problems can be reduced to show hardness and devise approximations.

Methodology: including a code base on VRPs into the set of the documents for retrieval introduces data leakage and effectively replaces code generation with search for appropriate code. Integration with Gurobi, where only single constraint solutions are provided, does not convince otherwise because Gurobi is a specific solver where constraints are inherently and trivially composable.  

Empirical evaluation: there are two important missing baselines without which the evaluation does not make much sense.
1. Any VRP problem can be solved optimally by enumeration. Judging by the figures, problem instances are small, so enumeration should be feasible if slow. What is the ratio of running times  by DRoC and by enumeration? On both successful and unsuccessful instances, mean and standard deviation of the log ratio of running times.

2.There are non-LLM based (including the code base used for conditioning) algorithm implementation for VRP problems used for evaluation (here is how the optimal solution metrics are obtained). Similarly, what is the ratio of running times (mean/standard deviation of log ratio)?

### Questions
What is the set of VRP problems the evaluation was performed on? Is this set publicly available?

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
4

### Summary
The paper presents DRoC, an approach for LLM-based generation of VRP optimization models via decomposed retrieval of constraints. Specifically, DRoC iteratively improves solutions by using both self-debugging and specialized RAG that integrates external knowledge per constraint based on decomposition of the VRP constraints. Experiments on 48 VRP variants and two solvers (OR-Tools, Gurobi) show the proposed approach significantly outperforms the baselines.


----
Based on the authors' response and improvements to the paper, I have increased my evaluation.

### Strengths
Strengths:
- LLMs for operations research modelling is an important topic with significant recent interest.
- Experiments over 48 VRP variants show significant gains for the proposed approach
- Paper is mostly clear and written well.

### Weaknesses
Weaknesses:
- I have major concerns regarding the experimental evaluation:
	- Evaluation based on success rate can be misleading: the generated code could run successfully and lead to a feasible solution but not the correct one for the requirement. For example, it can ignore (relax) some of the constraints, thus keep the problem feasible.
	- Evaluation based on optimality gap is also unclear to me in this setting. Comparing optimality gaps makes sense when we compare the efficiency of solving or modelling techniques (assuming both candidates are solving the same problem). Here we are comparing the accuracy of the formulation. If you are not solving the same problem (e.g., because generation dropped a constraint or added a constraint while maintaining feasibility) it is not clear how this helps. 
	- It is also not clear how the optimal solution (used in the OG computation) is obtained. Is it based on a ground-truth formulation, or on solving the generated instance for longer? While the appendix indicates a time limit of 100s to determine optimal solution, it is not clear what was the time limit for the solving of the generated instances.
	- Overall it seems like none of the evaluation actually talks about the correctness of the generated model.

- A more restricted setting (user provides both the name of the VRP variant and the signature of the function with clear documentation) compared to various previous work that supported natural language. This is a more restricted setting that requires more expertise from the user (both coding and familiarity with the literature). For example, if the user knows the problem they are solving is called "Capacitated Vehicle Routing Problem with Time Windows and Multiple Depots", they can probably decompose it themselves to the aspects of "capacitated" "time windows" and "multiple depots" (or that we could hard code those for each of the 48 problems, there are not that many) eliminating the need for a decomposer. This is not a flaw but it does restrict the potential impact of the approach.

- From a technical perspective there is limited innovation and it is more of a new LLM-based workflow. It is not entirely clear to me that these ideas will generalize well outside of VRP (even in the world of operations research), for example, the decomposer seems to rely heavily on the very useful naming of VRP problems that clearly define its constraints.

- Minor: 
	* OG is presented as a fraction but presented in percentage.
	* According to OG formula it is not clear that OG is bounded at 1 (the difference can be larger than the optimal value), and therefore it is not clear why 1 is used for unsuccessful programs.

### Questions
I would appreciate if the authors could comment on the points mentioned above, in particular with respect to the experimental evaluation.

### Soundness
2

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
This work mainly established a novel RAG-LLM framework called DRoC which can resolve various complex VRPs with composite constraints. DRoC incorporates internal LLM knowledge and external information by decomposing the retrieval of constraints, deeply stimulating the intrinsic ability of LLM in intergrating different sources, and generating the problem-solving code without any training process. This approach can either flexibly apply vairous expert documentations or rigorously self-debug as circumstances may require, while iteratively optimizing the solution multiple times. The experimental results indicate that DRoC achieves SOTA preference in each metric compared with other homogeneous methods.

### Strengths
- This paper clearly states its research motivation and emphasizes why it is important to establish a novel LLM framework for solving complex VRPs.
- The methodology is rigorous and mature, paying attention to many practical details. This can be reflected in the mechanisms of the router, the debugger and the retriever with a refined structure.
- The experimental results in section 5 show a promising enhancement when compared to the listed former approaches. Ablations studies also support the structure design of DRoC.
- DRoC proposed a flexible problem-solving LLM-based framework without any training requirement. This framework could be referenced in other LLM scenarios with fast external information access.

### Weaknesses
 - In my prospective, this is a pure prompt-based framework that may lack novelty and seem trivial. It would more significant if DRoC could shows more strong points other than SOTA preference, such as the generalization ability in analogous problems, remarkable inference efficiency, or convincing justification of framework structures, etc.
- The figure 2 can be more precise in order to guide the reader to better understand the framework structure. (1) The workflow of this flowchart is currently incomplete. For example, the "if not passed" desicion node needs "yes/no" paths to direct different outcomes. (2) The specific positions of each LLM module mentioned in appendix A should be indicated in this chart. For example, when does DRoC apply the first/second-stage filters?
- There is no specific dataset description in section 5. Appendix B provides an overall illustration of the considered VRP variants. However, the source of 48 problems remains unclear. This may affect the reproducibility of DRoC's experimental results.

### Questions
- It seems this is a code generation problem specifically. Is it more proper to add the keyword "code generation" to this paper?
- In figure 1, why are the numbers of different additional constraints not the same? A uniform standard is better needed, especially for the intro figure.
- At the end of section 4.2 "Single-constraint resolution", does "selecting the most relevant document" mean that currently DRoC retrieves information from only one document for each additional constraint? Is there any opportunity for LLMs to retrieve and digest information from multiple documents and make a composite utilizaiton of them?
- What are the standard prompts in section 5.1?
- What's the support for the statement at the end of section 5.4 "the LLMs can solve the 48 VRP variants with more composite constraints, indicating that complex tasks can be fulfilled by our decomposition-based method" ?
- I do not understand the motivations behind section 5.6 and 5.8, which seem not to be tightly related to the main topic of DRoC.

### Soundness
3

### Presentation
2

### Contribution
2
