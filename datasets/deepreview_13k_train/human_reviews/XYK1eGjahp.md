# Can Transformers Reason Logically? A Study in SAT Solving

- Decision: Reject
- Scores: 8, 3, 5, 5, 5

## Abstract
We theoretically and empirically study the logical reasoning capabilities of LLMs in the context of the Boolean satisfiability (SAT) problem. 
First, we construct a decoder-only Transformer that can solve SAT using backtracking and deduction via Chain-of-Thought (CoT). We prove its correctness by showing trace equivalence to the well-known DPLL SAT-solving algorithm. Second, to support the implementation of this abstract construction, we design a compiler \cname that takes as input a procedural specification and outputs a transformer model implementing this specification. Third, rather than \textit{programming} a transformer to reason, we evaluate empirically whether it can be \textit{trained} to do so by learning directly from algorithmic traces (``reasoning paths'') of the DPLL algorithm.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper investigates the capabilities of LLMs to solve an NP-complete problem, the 3-SAT problem. The authors first prove by construction that LLMs can simulate the DPLL algorithm to solve the 3-SAT problem with a bounded number of variables. To support this theoretical argument, they also compiled a Transformer implementation from the construction, which perfectly solved the bounded 3-SAT problems in their evaluation. A further empirical investigation demonstrated that, instead of by construction, LLMs could learn to solve the bounded 3-SAT problems whereas they are unable to generalize to problems with more variables. This observation matches the limitation of the theoretical construction requiring a bounded number of variables for 3-SAT problems.

### Strengths
1. This is the first work to study the capabilities of LLMs to solve NP-complete problems.
2. This paper proves by construction that LLMs can simulate the DPLL algorithm to solve the 3-SAT problem with, though, a bounded number of variables. It demonstrates that Transformers can perform unit propagation and backtracking, which are the core operations of the DPLL algorithm.
3. To support the theoretical argument, the authors also developed a compiler to compile the theoretical construction into a Transformer implementation and verified its practical capability to perfectly solve bounded 3-SAT problems.
4. The evaluation results match the theoretical statement. The main theorem implies that Transformers can perfectly solve 3-SAT problems with a bounded number of variables. In the evaluation, they also observed near-100% accuracy over problems with a bounded number of variables whereas the accuracy dropped significantly as the variable number further increased.

### Weaknesses
1. The main theorem implies that an arbitrarily large LLM is required to simulate a general DPLL algorithm for solving all 3-SAT problems. Considering a bounded program (a program of a specific size) can implement the general DPLL algorithm, it is still unclear how to approach the general DPLL algorithm using a bounded LLM.
2. The experiment setting in Sec 6.2 contradicts the description of Figure 2. Sec 6.2 states that the model is trained on the Marginal dataset and evaluated on the three generated datasets while Figure 2 describes the other way.

### Questions
1. What is the maximum number of steps, w.r.t. the variable number, for running DPLL over the generated 3-SAT problems? How does it compare to the empirical maximum CoT length?
2. What is the accuracy of the compiled model on instances with more than 20 variables, i.e. beyond the guaranteed upper bound? Does the accuracy drop drastically?

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This work investigates the application of the Transformer architecture for SAT solving. 
To this end, the authors present theoretical boundaries on decoder-only Transformers' size and solving capabilities in 3-SAT problems.
Furthermore, they introduce "Parametric Transformer" (PARAT) to create and evaluate the SAT-solving model.
The evaluation itself consists of a simulation study where 3-SAT problems with varying numbers of variables have been generated as a benchmark.
The authors show how their compiled model is able to solve all problems with perfect accuracy, while models that were trained instead fail when challenged with problems of previously unseen numbers of variables.

### Strengths
The authors present how a 3-SAT solving algorithm can be expressed within the confinements of the building blocks of the Transformer architecture and demonstrate that it remains accurate across varying numbers of involved variables and clauses.

### Weaknesses
The contribution and significance of PARAT remained unclear to me after considering both the main text and appendices. 
The authors claim that PARAT "is designed to provide an intuitive syntax resembling standard numerical array manipulation, akin to NumPy, [...]" (page 6, line 311). 
Considering the referenced "ParametricTransformer Code" in Appendix D, it becomes evident that the language in question is pure Python using the numpy library. 
The language "Python" is named not once in the paper, and the formulation of contributing a "compiler" with the notation "akin to" numpy and PARAT's "NumPy-like Array Syntax" (page 6, line 314) seems completely unjustified and bordering on deception. The core issue is that the paper presents PARAT as a novel language and compiler, but the provided examples reveal it to be standard Python code leveraging the NumPy library. The 'compiler' appears to be a function that transforms a specific subset of Python/NumPy code into a PyTorch model, rather than a general-purpose compiler for a new language. This distinction is crucial and not adequately addressed, leading to the impression that the authors are overstating their contribution. The lack of clarity around the actual compilation process, specifically how the Python/NumPy code is translated into Transformer weights, further obscures the significance of PARAT. The paper does not provide sufficient detail on the limitations of the subset of Python/NumPy that can be compiled, nor does it discuss how the compilation process handles different data types or array operations beyond the provided examples.

### Questions
I have no questions for the authors.

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper investigates the logical reasoning capabilities of Transformer models in solving SAT problems. The authors designed a decoder Transformer to emulate the DPLL algorithm, tackling SAT through variable selection, conflict detection, and backtracking. The PARAT compiler translates high-level procedural logic into model weights, enabling practical implementation.

### Strengths
1. Leveraging a Transformer to simulate the entire DPLL SAT-solving process, rather than focusing on optimizing specific heuristics such as variable selection, represents a novel approach.
2. The paper presents the PARAT compiler, which translates the procedural logic of the DPLL solving process into a Transformer model, achieving perfect accuracy on SAT problems with up to 20 variables and 88 clauses.
3. The trained model sustains high accuracy on SAT test instances with variable counts comparable to those in the training dataset.

### Weaknesses
1. The evaluation assessed only the accuracy of satisfiability predictions, without examining the correctness of the reasoning process itself. Thus, even when predictions were correct, the reasoning steps might still diverge from the intended algorithm. Additionally, there was no in-depth analysis of the accuracy drop on larger SAT instances to identify if errors arose from issues in conflict analysis, backtracking, or other specific areas. For example, the model might be learning to predict SAT/UNSAT based on statistical properties of the input clauses rather than by emulating the DPLL algorithm's logical steps. This is especially concerning given the lack of analysis into specific failure modes.
2. The experiments compared the Chain-of-Thought (CoT) length solely with theoretical upper bounds, without including baseline comparisons. Evaluating against the reasoning steps of a standard DPLL solver or other baselines could offer a clearer perspective on the model’s reasoning capabilities. Without such comparisons, it's difficult to assess the efficiency and validity of the model's reasoning steps. For instance, the model might be taking significantly longer or making unnecessary steps compared to a traditional solver.
3. The trained model shows limited generalization, performing well only on test instances with variable counts similar to those in the training data. Its accuracy declines significantly on SAT instances with up to 20 variables, possibly dropping below 50%. This suggests that the model may be overfitting to the training data's specific variable counts and clause structures, rather than learning a generalizable logical reasoning process.

### Questions
The model demonstrates poor generalization, achieving high accuracy only on SAT instances with variable counts similar to those in the training data. Performance significantly declines on larger instances, indicating that it may be learning patterns specific to the training data rather than pure logical reasoning, thus failing to fully substantiate the claim that Transformers are capable of logical reasoning.

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper provides a theoretical analysis of the Transformer's ability to solve 3-SAT problems through chain of thoughts, along with a compiler that can output a Transformer model satisfying a given specification. The empirical results demonstrate that the Transformer can achieve high accuracy in solving small-scale 3-SAT problems.

### Strengths
The problem tackled in this paper is highly interesting and relevant. I appreciate the effort of theoretical analysis conducted on the reasoning capabilities of transformer models, which is a rapidly evolving and impactful area of AI research.

### Weaknesses
This paper has several issues that need to be addressed.

First, the paper's introduction claims to answer a "fundamental question about whether LLMs can perform propositional reasoning." However, after reviewing the paper, it does not appear that the theoretical and empirical analysis provided is sufficient to conclusively answer this broad question. The analysis is focused narrowly on 3-SAT problems, and it is unclear how the results could be generalized to other propositional reasoning problems. Specifically, the paper does not address the nuances of different logical connectives beyond AND, OR, and NOT, which are core to propositional reasoning. Furthermore, the model used in the experiments may not be representative of a typical large language model with billions of parameters, raising concerns about the scalability and generalizability of the findings. The use of a custom-compiled transformer, while theoretically interesting, limits the direct applicability of these results to existing LLMs.

Second, the proofs for the theorems presented in Section 4 are missing. While it is possible the proofs require additional space, it is necessary to at least provide a high-level outline of the proof approach in Section 4. Purely moving numerous lemmas and proofs to an appendix is an unsatisfactory way to present such a crucial part of the paper. This lack of immediate access to the core theoretical arguments makes it difficult to assess the validity and novelty of the claims. The reader is forced to navigate the appendix to understand the theoretical underpinnings, which hinders the flow and accessibility of the paper.

Third, the incremental contribution of the proposed compiler compared to the prior Tracr compiler is unclear. It appears that the primary focus of this work is on addressing implementation issues with Tracr, but the specific novel aspects are not well articulated. The paper should clearly explain what new capabilities or improvements are offered by the proposed compiler over the previous work. For instance, the paper should quantify the performance gains or the expanded range of algorithms that the new compiler enables, compared to Tracr. Without such concrete details, it is difficult to ascertain the significance of this contribution.

### Questions
What is the incremental contribution of the proposed compiler compared to the prior Tracr compiler?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
The paper contributes to research on understanding the reasoning capabilities of transformers when using the chain of thought. Its contributions are threefold:
- It asserts that a decoder-only transformer can, in principle, solve Boolean SAT using the chain-of-thought to reason similar to the DPLL algorithm.
- It introduces PARAT, described as a "compiler that takes procedural specifications as input and outputs a transformer model that implements these specifications."
- It empirically explores whether a transformer can be trained to solve SAT problems.

### Strengths
- Investigating the reasoning capabilities of transformers, particularly concerning formal 
problems, is highly valuable.
- Boolean satisfiability serves as an appropriate baseline candidate.
- Supporting the initial contribution of theoretical expressiveness with experiments that 
provide a practical perspective is a sound approach.

### Weaknesses
My main concerns regard the first two contributions. I categorize the weaknesses based on the contributions of this paper and order them from most important to least important in each category.

### Transformers with CoT solve SAT
- The claim of the paper may be perceived as somewhat misleading. While it states, 
  "we construct a decoder-only Transformer that can solve SAT," the actual result 
  (Theorem 1) is that "for any $p,c \in \mathbb{N}^+$ there exists a decoder-only Transformer 
  with [...] that can decide all 3SAT instances of at most $p$ variables and $c$ clauses using CoT." 
  This is correctly described as the construction of a decoder-only Transformer for 
  a bounded version of 3SAT. Alternatively, Theorem 1 implies that the class of all 
  decoder-only Transformers solves the general 3SAT problem: given an arbitrary 
  3SAT formula, there exists a decoder-only Transformer that can reason whether it is satisfiable. 
  The distinction is significant, as this contribution of the paper is directed towards proving 
  that a single decoder-only Transformer exists for solving SAT. In fact this is not implied by Theorem 1.
- Definition 4.3 could benefit from clarification. While the intended meaning might be inferred, 
  there remains uncertainty due to the probabilistic nature of the map computed by a decoder-only 
  transformer. The pivotal question is ensuring the decision procedure always 
  terminates. It appears that a parameter may be absent in this definition, one that would 
  guarantee termination after a predetermined length if an end-of-sequence token does not 
  appear.
- The intuition behind the Transformer template constructed for Theorem 1 needs improvement.
  While Figure 1 is comprehensive, despite being oddly distant in placement within the paper, 
  the explanations from line 277 to 300 are overly abstract. Specifically, lines 288 to 294 
  lack clarity, making it difficult for the reader to grasp their meaning. This may confuse 
  the reader more than it helps.

### Parat
- The main concern is that the paper struggles to clearly define what PARAT is. The initial description 
between lines 85 to 87 reads, "We design PARAT, a compiler of high-level sequence operations in Numpy-like 
syntax into Transformer model weights, to empirically validate and analyse theoretical constructions of 
Transformer algorithms." However, there is ambiguity surrounding the terms "compiler", "high-level sequence operations", "Transformer model weights", and "Transformer algorithms". Further on line 306, it states, "... a framework for converting theoretical constructions of Transformers into practical models ...". Yet, it remains unclear what is meant by "theoretical constructions of Transformers" and how these relate to "high-level sequence operations". The first detailed exposition of PARAT (commencing with section 5.1) immediately delves into features and operations, leaving a reader, such as myself, completely perplexed as to what it truly encompasses.
- Without addressing the aforementioned ambiguities, it remains unclear why PARAT's contribution is significant for exploring the reasoning capabilities of Transformers, the paper's primary objective. While it appears to be a useful tool, developed with considerable effort, it seems to distract from the main aim of the paper and takes up space that could be used to better elucidate the first contribution.

### Questions
Having shared broad and high-level concerns regarding the paper, I encourage the authors to address these directly. 
Here is a summary of the key points:
- Do you agree that your theoretical contributions do not demonstrate the existence of a decoder-only Transformer that solves SAT? Do you believe this could be resolved with minor revisions, and if so, how would you approach this?
- How do you ensure the decision procedure in Definition 4.3 always terminates? What considerations 
lead to defining the "semantics" of a decoder-only transformer as mapping to a probability 
distribution? Is this crucial? If I am not mistaken, this perspective somewhat diverges from research 
addressing the expressiveness of transformers, such as the paper "Attention is Turing-complete", which you cite, or studies focusing on the expressiveness of single-pass or encoder-only transformers.
- Can you provide a clear and concise definition of what Parat is?

### Soundness
2

### Presentation
2

### Contribution
3
