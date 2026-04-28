# ImProver: Agent-Based Automated Proof Optimization

- Decision: Accept
- Avg Score: 6.75
- Scores: 6, 5, 8, 8

## Abstract
Large language models (LLMs) have been used to generate formal proofs of mathematical theorems in proofs assistants such as Lean.
However, we often want to optimize a formal proof with respect to various criteria, depending on its downstream use.
For example, we may want a proof to adhere to a certain style, or to be readable, concise, or modularly structured. 
Having suitably optimized proofs is also important for learning tasks, especially since human-written proofs may not optimal for that purpose.
To this end, we study a new problem of automated proof optimization: rewriting a proof so that it is correct and optimizes for an arbitrary criterion, such as length or readability.
As a first method for automated proof optimization, we present \methodname{}, a large-language-model agent that rewrites proofs to optimize arbitrary user-defined metrics in Lean.
We find that naively applying LLMs to proof optimization falls short, and we incorporate various improvements into \methodname{}, such as the use of symbolic Lean context in a novel Chain-of-States technique, as well as error-correction and retrieval. We test \methodname{} on rewriting real-world undergraduate, competition, and research-level mathematics theorems, finding that \methodname{} is capable of rewriting proofs so that they are substantially shorter, more modular, and more readable.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces ImProver, a large language model (LLM) agent designed for automated proof optimization in the proof assistant Lean. ImProver adopts several LLM augmentation methods, including a Chain-of-States technique that provides intermediate proof states to LLM, retrieval methods, and sampling methods.

The paper defines three key metrics for evaluation: the Length Metric, which aims to minimize the number of tactic invocations; the Readability Metric, which favors a declarative haveproof style; and the Completion Metric, which measures proof correctness.

In experiments, the author compares ImProver with the baseline GPT-4o model on Mathematics in Lean (MIL), Compfiles, and Mathlib datasets. The results show that ImProver reduces the length of 35.44% of proofs compared to 8.31% for GPT-4o, and increases readability in 24.56% of proofs compared to 6.13% for GPT-4o. Proof completion was evaluated only on the selected MIL dataset, where ImProver achieved 39.13% successful proof generation compared to 21.73% for GPT-4o.

### Strengths
This paper first discovers a new field of automated proof optimization, and conducts a pioneering attempt in this field, marking the first significant effort to use LLMs for enhancing formal proofs with respect to certain metrics in proof assistants like Lean. A notable strength of this work is its emphasis on the role of proof states in guiding LLMs. By introducing the Chain-of-States technique, which provides intermediate proof states to the LLM, the authors demonstrate an understanding of how contextual information can significantly improve the accuracy and efficiency of proof optimization.

### Weaknesses
- The method proposed in this paper is well-suited for metrics that can be directly computed from the formal proof. However, this limits its applicability to more complex metrics such as readability. The paper defines readability as the ratio of explicitly typed have tactics to the total number of tactic invocations in line 130. This simple definition may lead to a proof with numerous unused have tactics being considered more readable than a normal proof. The reviewer considers readability to be a multifaceted metric, influenced by various factors including the use of underlines, the depth of proof terms, the naming of variables, appropriate comments within the proof, and other stylistic elements. These factors are challenging to quantify with a simple function, suggesting that the proposed method may not be effective for assessing readability or other nuanced aspects of proof quality.
- The reviewer suggests developing a combined metric that considers both length and readability for a more accurate assessment of proof quality in real applications, since improving in one metric may significantly sacrificing other metrics. Additional experiments should test whether the framework described in the paper can effectively balance and improve these combined metrics.
- The proof generation results in Table 7 are limited to specific selected datasets. The reviewer believes that ImProver's neural theorem proving results should also be evaluated on unselected datasets and more commonly used test sets, and compared with a wider range of models to provide a comprehensive assessment of the proposed method's performance.
- The comparison with GPT-4o, which lacks proper Lean 4 syntax capabilities, may not accurately reflect the effect of RAG or refinement policies of ImProver. More ablation studies could be conducted to demonstrate that the rise in performance is not solely due to the guidance for correct Lean 4 syntax in the prompt.
- The reviewer suggests that rule-based optimization methods for Lean, particularly for the length metric (e.g., using nested termwise proofs to replace tactic-based proofs), exist. The authors should compare ImProver with these methods to demonstrate its relative strengths.

### Questions
- Could the authors clarify under what criterion the mathematical branch of the dataset for testing the neural theorem proving effect was selected and whether they have evaluated the method on the entire dataset and other commonly used datasets?
- Could the author clarify whether they have tried any rule-based methods and compared their results to those produced by ImProver?

### Soundness
3

### Presentation
4

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
The paper tackles the proof optimization problem, which aims to optimize partly written proofs with respect to a given criterion (such as length and readability).
The paper also addresses the problem by querying to LLMs and ranking the outputs with the criterion.

### Strengths
+ The paper tackles the proof optimization, which has not been considered yet in neural theorem proving, and proposes a (simple) approach to it.
+ The proposed approach can outperform the baseline, which simply queries to an LLM (GPT-4o).

### Weaknesses
 - Because the proposed approach to the proof optimization (described in Section 3) is simple, I find the main contribution of the paper is in applying LLMs to proof optimization, a problem in theorem proving. When evaluating the paper from such a viewpoint, I admit the proof optimization problem may be worth studying, but I don't think the paper argues its value in a convincing manner. The second paragraph of Section 1 discusses the importance of the proof optimization, but there is no reference to support the argument. That is, there is no objective material to find the importance of the problem. Therefore, it is unclear and unconvincing what benefit is expected by solving the proof optimization problem.

- Some experimental setting and terminology are unclear (see the following questions).

Typos:

- l35: precision --> imprecision

### Questions
- It is possible to explain the benefits of solving the proof optimization problem with application domains (such as formal verification or mathematical education), references, and concrete examples that support the claim?
- I think it is important to incorporate some kind of random in using the best-of-n technique. Does the proposed approach ensure diversity in the LLM outputs when using the best-of-n technique? If yes, how it is achieved? Otherwise, how do you address the potential issue of deterministic outputs?
- Can you provide a detailed description of the input format for ImProver and GPT-4o in the experiment? Especially, does the input include the original proof from the dataset, a partial proof, or start with an empty proof?
- The paper claims ImProver can rewrite proofs so that they are more modular. Can you provide a clear definition of 'modular' in the paper?  It would also be helpful to give modular and non-modular examples.
- What does the paper mean by efficient proofs? (E.g., it says "These proofs are extremely efficient" in lines 266-267).

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
Authors are studying whether LLMs can optimize formal math proofs for additional criteria besides correctness, such as length and readability. They find that naively applying LLMs don’t perform great at this task, but that multiple interventions like augmenting the formal proof with comments, adding relevant context via retrieval, or selecting the best of N solutions, substantially improves performance. Finally, they ablate these interventions and find that each contributes substantially to the overall performance.

### Strengths
The authors frame an interesting and potentially very impactful problem, propose a smart solution, and execute on that solution well. The paper is well-written and the results appear convincing to me.

### Weaknesses
The authors could mention interactive proofs / prover-verifier games (https://arxiv.org/abs/2108.12099), where LLMs are trained to write informal math proofs to be maximally legible to an independent verifier, as related work.

I believe the caption of Figure 1 should read (left) instead of (right)?

For reproducibility, the authors should mention the exact version of GPT-4o they used for their experiments (gpt-4o-2024-08-06 ?)

I’m taking it on trust that “readability” defined as in the paper is a sensible definition - to someone not familiar with Lean, the "readability-optimized" version of the proof in Figure 3 is not actually a lot easier to parse than the other version.

Idle musing, feel free to ignore: Do you have thoughts about the ceiling/floor of your proposed metrics - are there degenerate solutions? In particular, could `we evaluate this using the ratio of number of explicitly typed have tactics to total number of tactic invocations.` incentivize the model to generate a lot of superfluous `have` tactics to inflate this metric?

### Questions
Idle musing, feel free to ignore: Do you have thoughts about the ceiling/floor of your proposed metrics - are there degenerate solutions? In particular, could `we evaluate this using the ratio of number of explicitly typed have tactics to total number of tactic invocations.` incentivize the model to generate a lot of superfluous `have` tactics to inflate this metric?

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper proposes ImProver, a framework designed to optimize proofs based on various metrics, such as shortening proof length and enhancing human readability. The authors establish several performance metrics to evaluate the quality of improvements and conduct comprehensive case studies across representative benchmark datasets for an extensive analysis.

### Strengths
- As the first work in proof optimization, this paper defines novel and reasonable metrics to quantify the quality of Lean proofs.
- The paper integrates several advancements from the LLM community, including proof generation, retrieval, chain of thought (CoT) reasoning, and self-correction in code generation, for optimizing proofs. The inclusion of these methods is well-motivated, and the experiments are extensive. Furthermore, ImProver achieves notable performance without using models fine-tuned specifically for proof generation, showing its significant contributions to proof synthesis and optimization.
- The open-source code is well-structured and documented, facilitating easy adoption and use by the community.

### Weaknesses
While the experimental results are comprehensive, their presentation could be improved, which is particularly important for a paper focused on advancing LLM applications in proof optimization. Specifically, in Section 4.2.1 on ablation testing:

- At line 450, the term “string list” is introduced without prior definition. Could the authors clarify the relationship between "string list" and the "flat" format mentioned earlier? This would help ensure consistency in terminology throughout the paper.
- Table 5 could be clarified further. Upon cross-checking, it appears that the best/worst values are based on configurations giving the highest “improvement” scores, whereas the last row presents the best scores across all configurations. It would be helpful to explicitly state this distinction in the main text to enhance clarity.

### Questions
- Could the authors elaborate further on the “flat” and “structured” formats described in Section 3.1.2 and provide examples for clarity?
- When selecting parameters in the ablation study, why was the best parameter combination chosen based on improvement rather than accuracy? Could the authors discuss the trade-offs between optimizing for improvement versus accuracy, and how this choice might impact the practical applicability of ImProver?

### Soundness
3

### Presentation
3

### Contribution
2
