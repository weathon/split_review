# Proving Olympiad Inequalities by Synergizing LLMs and Symbolic Reasoning

- Decision: Accept
- Avg Score: 6.75
- Scores: 8, 5, 8, 6

## Abstract
Large language models (LLMs) can prove mathematical theorems formally by generating proof steps (\textit{a.k.a.} tactics) within a proof system. However, the space of possible tactics is vast and complex, while the available training data for formal proofs is limited, posing a significant challenge to LLM-based tactic generation. To address this, we introduce a neuro-symbolic tactic generator that synergizes the mathematical intuition learned by LLMs with domain-specific insights encoded by symbolic methods. The key aspect of this integration is identifying which parts of mathematical reasoning are best suited to LLMs and which to symbolic methods. While the high-level idea of neuro-symbolic integration is broadly applicable to various mathematical problems, in this paper, we focus specifically on Olympiad inequalities (Figure~1). We analyze how humans solve these problems and distill the techniques into two types of tactics: (1) scaling, handled by symbolic methods, and (2) rewriting, handled by LLMs. In addition, we combine symbolic tools with LLMs to prune and rank the proof goals for efficient proof search. We evaluate our framework on 161 challenging inequalities from multiple mathematics competitions, achieving state-of-the-art performance and significantly outperforming existing LLM and symbolic approaches without requiring additional training data.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper studies a neural-symbolic integration method, named Lips, for mathematical inequality problems. The paper first identifies the two key tactics in inequality problems, scaling and rewriting. Application of the scaling tactic is determined by a symbolic method, and application of the rewriting tactic is by prompting an LLM. Applying these tactics creates new proof goals, and the paper filters the created goals by a symbolic method and scores the surviving ones by prompting an LLM.

### Strengths
+ Solving mathematical inequalities is a challenging, and significant task. It also has application to formal verification.

+ The proposed approach is a nice integration of symbolic and neural methods. The criterion to distinguish between their use in tactic application is clear: reasoning in a finite search space is conducted symbolically and reasoning in an infinite space is neurally. The idea of symbolic filtering and neural scoring is natural, but its significance has been (partly) proven in the experiment.

+ The experiment evaluates the performance of the proposed approach and the potential with respect to the improvement of the underlying LLM. Both are promising.

### Weaknesses
 - I don't think this is a weakness of the current form of the work, but the paper could enhance the work and broaden the audience if it can claim there are other math domains with two types of tactics such that one is suitable for symbolic reasoning (or the search space of its application is finite) and the other is for neural reasoning (or its search space is infinite), like scaling and rewriting in inequality problems.

- Some parts of the proposed approach are unclear (see the following questions).

Other comments:

- l296: In the definition of HM, the correction of the second occurrence of $d_i$ may be $d_j$.
- I think, after calculating the decoupling score and homogeneity score, only top-k candidates are selected (in the experiment, it seems that only top-10 candidates remain), but it might be nice to clarify it in Section 4 (I noticed it during reading Section 5.1).
- The caption of the right figure in Figure 4 is a bit confusing. Rephrasing it to, e.g., "Various sizes of filtered goal sets" may be helpful.
- For RQ2, the paper says a direct comparison of proving time could be unfair, but I'm not sure whether only comparing the pruning ratio of scaling tactics and the number of iterations in goal selection is fair. Even if the pruning and goal selection are improved over a long period of time, it may not lead to improving the performance of the prover itself. I'm wondering that showing all the comparisons of proving time, pruning ration, and the number of iterations in goal selection may be more fair.

### Questions
- How influential on the performance are the symbolic-based transformation tactics, sum-of-squares and tangent line tricks? In other words, what happens if only neural-based transformation is applied?

- What are the up-arrow and down-arrow in the caption of Figure 3?

### Soundness
3

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
4

### Summary
The authors introduce LIPS: a hybrid system for proving inequalities, which combines symbolic solvers, manually crafted heuristics, and   LLMs. LIPS operates within the formal framework of Lean 4. The system is evaluated on a test set of 161 competition-style inequalities of varying difficulty, and is compared to 5 other methods (2 purely symbolic and 3 ML-based). LIPS performs significantly better than the baselines on the considered test set given the time limit of 90 minutes.

### Strengths
The work demonstrates the potential of combining machine learning and symbolic/formal techniques, which is an interesting and still under-explored direction.

The design of LIPS looks well thought out, leveraging appropriate symbolic techniques in the pipeline.

The authors compared LIPS against a representative variety of baselines, both symbolic and ML-based.

The paper is mostly written clearly, and provides enough background information and helpful examples (but some parts are less clear -- see weaknesses below).

### Weaknesses
The test dataset is not publicly available. In particular, the Lean and SMT formalizations are not available. It is relatively easily to introduce unintended errors when formalizing math, so open-sourcing the formalizations is important to make inspection possible. Also, it is crucial to allow other researchers to compare their approaches by providing the test data.

The implementation of LIPS and MCTS is not available for testing and inspection, and there is no promise of open sourcing it. 

Some parts of the description of LIPS are unclear to me -- see questions below. In particular, it is described how LIPS generate a set of new proof goals from one proof goal, but the main body of the paper does not contain any information on how search is conducted in the resulting tree of proof goals.

The related work section is missing important related literature. Combining formal theorem proving with machine learning is not limited to LLMs. There is a rich body of research combining other ML approaches and proof assistants [1,2,3,4,5]. It is very well possible that more light-weight ML approaches would be more suitable as non-symbolic components of LIPS.

The evaluation is somewhat limited and unconvincing. 
- It would be informative to see a "time limit vs proof success rate" plot in addition to the table showing the stats for the 90 min. time limit. This limit is rather high, and I suspect that the symbolic approaches, when they solve an inequality, they do this within the first couple of minutes.
- It is possible that the improvement achieved by LIPS compared to CAD-based approaches is due to the set of carefully handcrafted scaling lemmas that fit the test problems. Also, it seems that the size of the filtered set was selected to fit the test problems best, and there was no separate validation set to fit this parameter.
- It would be good to see more ablations: the effect of symbolic filtering; the effect of special tactics (sum of squares, tangent line). 

The problems from the test set are publicly available on the internet, therefore GPT-4o could be trained on those. This raises a question about reliability of the evaluation of LIPS, where GPT-4o is used. 

Theorem proving in Lean is not sufficiently introduced, which is important given the ML-oriented audience of ICLR.

The presented approach to an extent is inspiring other combinations of symbolic and ML techniques, but LIPS as a system is very specific to the problem of proving competition-style inequalities; it may not translate to more general / practical problems in any simple way. 

Minor remarks:
- The description of the X axis in Figure 4b looks to be wrong.
- Figure 3 shows 19 problems, whereas in the text you write about 20 problems.
- The Y axis of the left plot in Figure 3 should start at 0 not 60.
- "AM-GM inequality" -- you should explain the acronym here. 

### Questions
1. Could you provide the Lean and SMT formalizations of the test inequalities?
2. Could you provide the implementation of LIPS?
3. What precise parameters were used for SMT solvers to obtain the CAD baseline? 
4. How is MCTS implemented? Do you apply symbolic filtering during the search, similarly as in LIPS?
5. Why do you write "Please reason step by step" in the prompts for neural ranking? What are the full resulting responses from GPT-4o? 
6. What is meant by "iteration of LIPS" in Figure 3? And what is an "iteration" in the oracle? How do you obtain the oracle proofs?
7. How does search work in LIPS? Is it best-first search? Or breadth-first search?
8. In line 412 you write: "LIPS outperforms the existing method in 13 out of 20 problems". I cannot see this in Figure 3, could you explain?
9. When you do neural rewriting, how do you verify that the rewrite is correct?
10. You use SymPy's `simplify` to compare with "neural" rewrites. What does this function do? 
11. Did you consider to use simpler ML techniques in place of GPT-4o? 
12. What would happen if you get rid of the neural ranking and use solely homogeneity and decoupling metrics to rank the goals? 
13. You write: "Our techniques could serve as a solid foundation for broader areas of mathematical research such as
information theory, optimization, and deep learning". Could you explain a bit how?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper introduces LIPS, a neuro-symbolic system that combines large language models (LLMs) and symbolic reasoning to solve Olympiad-level inequality problems in formal theorem proving. 

LIPS divides tactics into scaling (using symbolic tools) and rewriting (using LLMs):

Scaling applies known inequality lemmas (e.g., AM-GM or Cauchy-Schwarz inequalities) to refine subterms in the target inequality. The symbolic approach allows exhaustive enumeration of lemma applications across potential arguments. However, only certain applications lead to correct deductions since overscaling risks invalidating the inequality. To address this, LIPS uses counterexample filtering to eliminate incorrect transformations. This involves generating possible solutions with symbolic tools (e.g., CAD solvers) to check whether the inequality holds across variable values, discarding transformations that fail.

Rewriting tactics focus on algebraic transformations to express terms in alternative but equivalent forms. This space is vast (infinite transformations possible), so LLMs are employed to guide the selection, generating transformations that preserve provability. LIPS designs prompts for common transformations (e.g., factorization, denominator simplification), allowing the LLM to filter likely useful transformations.

The authors conduct evaluations on 161 challenging inequality problems and demonstrate their system is significantly more capable than existing systems.

### Strengths
The paper takes a novel approach (to my knowledge) to solve olympiad inequalities following the recent paradigm shift of using test-time compute to solve mathematical problems. The domain specificity of solving inequality problems is very well exploited. The method rigorously categorizes proof tactics into scaling and rewriting, with each category handled by techniques suited to its complexity. This results in successful results as demonstrated by extensive experiments and results in proofs written in Lean 4 and hence has guarantees.

LIPS sets a new benchmark for inequality theorem proving by combining machine learning with symbolic techniques, which is promising for broader applications in automated mathematics. 

The paper is well-organized, clearly explaining both the technical details of scaling and rewriting, and the hybrid neuro-symbolic approach.

### Weaknesses
It is unclear to me how LLM rewritings are formalized in Lean 4 - is it a Lean 4 tactic that can do the rewrites of LLM? If that is the case, it would be interesting to use this as a tactic in general theorem proving in Lean 4.

The datasets used (e.g., ChenNEQ, MO-INT, 567NEQ) focus on specific competition-level inequalities, which might limit generalizability. I don't understand why authors took a random sample of 100 from 567NEQ instead of running the system on all of them. I think it is important to make sure that there was no contamination due to solutions of these problems appearing in training data of GPT4o, although I believe the failure of other LLM based approaches is evidence that LISP's added value is significant.

I believe some evaluation comparing to existing theorem provers such as the one from DeepSeek or LeanCopilot could be included. I would also love to see the code on how the LLM rewriting tactics could be formalized in Lean 4.

### Questions
- Can you describe how the Lean 4 commands such as `llm_simplify`, `llm_rearrange`, etc. do? It would be great if you could provide a complete Lean 4 code that people can run for reproducibility and verification purposes.  
- It would be interesting also to compare to existing Neural Theorem Provers in Lean 4 such as DeepSeek Prover V1.5 or LeanCopilot.

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper presents a neuro-symbolic tactic generator designed to solve typical inequality problems found in
maths olympiad contests. The authors identify two general strategies often employed by humans in solving these problems, which involve creating new goals via:
- Scaling, which involves the application of known lemmas, inequalities, etc., to the inequality that needs solving.
- Rewriting, which involves using common equivalent transformations on the inequality that needs solving.

Lips utilises a blend of symbolic methods, used for scaling and some rewriting, and LLMs, primarily used for rewriting inequalities and ranking and selecting goals. The performance of Lips is compared with state of the art tools on common benchmarks. Additionally, general paradigms for neuro-symbolic reasoning are extracted from the approach Lips takes for math olympiad inequality problems.

### Strengths
- The development of neuro-symbolic tools for reasoning about formal tasks is quite intriguing, and this paper contributes nicely in that its findings seem to transcend the specific task of solving maths olympiad questions.
- The approach taken by Lips is explained in detail and is easy to comprehend. Overall, the concept behind Lips appears sound.
- The experimental parts of the paper are sufficiently supported. 
- The paper is well-written and organized, with everything supported by examples. 
I found it an enjoyable read.

### Weaknesses
I order the weaknesses from most to least important:
- It is unclear to me how impactful the findings of this paper are beyond 
the development of a well-performing neuro-symbolic tactic generator 
for these specific inequality problems. While the workflow of Lips 
is a nice combination of symbolic and LLM-based components, the underlying 
idea seems rather straightforward: whenever symbolic methods are 
sufficient (as in the scaling steps), use symbolic; and whenever things 
become less clear (as in rewriting and goal selection), use LLM. While I 
may be incorrect, this seems folklore to me.
- While I appreciate the paper's lightweight tone, at times, 
it feels that many choices are justified by intuition alone. 
For example, the authors state that scaling and rewriting are the methods humans use to solve such inequality problems. This seems reasonable to me, yet there is no evidential support for this in the paper. Similarly, in Section 4.1, the authors introduce criteria for ranking proof goals. 
Again, these appear reasonable to me, but there is no support for these claims. 
It may well be the case that research on such questions is simply non-existent, but I would have appreciated it being stated more clearly why we have to rely on intuition.
- At some points, the paper's language is a bit too informal. For example, 
in the paragraph starting with line 180, it is stated that OpenAI's o1-preview 
"cannot solve a specific inequality". The proof presented is an example 
of a prompt given to o1-preview, where it fails to address this particular 
inequality. Clearly, this is not a sufficient argument to claim that 
o1-preview is generally unable to solve such inequality tasks.

### Questions
- As mentioned in my weaknesses, I remain unconvinced about the broader impact of this paper beyond 
the neuro-symbolic resolution of inequality problems. Could you clarify what the novel findings are 
in a wider context? Maybe even what are specific tasks, problems that benefit from your reasearch, aside 
math olympiad problems? 

- The development of a tool like Lips could be noteworthy, but I am not familiar with similar existing 
tools. Am I correct in understanding that it is the first tool to integrate neural and symbolic components? 
In your experiments, it appears that you only compare it to tools that are either purely neural or purely 
symbolic.

### Soundness
3

### Presentation
4

### Contribution
2
