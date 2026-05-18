- Decision: Reject
- Scores: 3, 5, 3, 3, 3

## Merged Review

### Summary

The paper proposes LLM4Solver, a framework that uses a pre-trained LLM as a generator of algorithm code (diving heuristics for MILP solvers) and a derivative-free evolutionary optimizer with multi-objective fitness evaluation to refine the code. Experiments on several MILP benchmarks show that the generated heuristics outperform human-designed and L2DIVE policies in solution quality, efficiency, and cross-benchmark generalization. The method achieves strong performance within a few evolutionary iterations and provides interpretable code with comments. However, multiple reviewers note that the core pipeline closely resembles prior LLM-based heuristic generation works (especially EOH), the comparisons to existing methods are incomplete, the problem instances are relatively small, the experimental baselines are limited, and the contribution is incremental.

### Strengths

- **Efficiency**: The method achieves strong performance within very few evolutionary iterations (e.g., ten iterations), which is valuable in resource-constrained settings (Reviewers 1, 3).
- **Cross-benchmark generalization**: The framework shows strong potential to generalize across different optimization problems and benchmarks, a key challenge in CO solver design (Reviewers 2, 3, 4).
- **Interpretability**: The LLM-generated heuristics are presented as code and comments, offering more interpretability than previous neural-network-based methods (Reviewers 1, 4).
- **Multi-objective fitness evaluation**: The incorporation of a multi-objective fitness function to evaluate performance across multiple benchmark datasets is highlighted as a distinctive component (Reviewers 2, 5).
- **Detailed ablation studies**: The paper provides thorough ablation studies demonstrating the importance of each component (Reviewer 4).
- **Performance under different LLMs**: The manuscript demonstrates performance with different LLMs, showing versatility (Reviewer 5).
- **Minority view (Reviewer 2, score 5)**: Reviewer 2 specifically notes that the combination of evolutionary algorithm and multi-objective fitness yields impressive performance in terms of solution quality, solving time efficiency, and robustness under different scenarios, though they also flag limited novelty.

### Weaknesses

1. **Limited novelty and strong resemblance to existing works**:
   - The core idea of using LLMs with Initialization/Crossover/Mutation prompting to generate heuristics is already present in multiple prior works, most notably EOH (Liu et al., 2024), ReEvo (Ye et al., 2024), and others (Reviewers 1, 2, 3, 4, 5). The only clear innovation appears to be the multi-objective fitness function (Reviewer 5).
   - The paper does not clearly differentiate its methodology from EOH (Reviewer 3). The pipeline mainly builds on top of EOH but is applied to diving heuristics (Reviewer 4).
   - The overall design seems to rely heavily on the LLM’s general capabilities, and many performance gains may stem from the LLM rather than the algorithm’s intrinsic design (Reviewer 1).

2. **Missing comparisons to state-of-the-art methods**:
   - **LLM-based heuristic generation methods**: No experimental comparison with EOH, ReEvo, or other LLM-based hyper-heuristic generation works (Reviewers 1, 2, 3, 5). Without this, it is unclear whether the multi-objective fitness function provides any advantage over existing single-objective LLM-based methods (Reviewer 5).
   - **Symbolic discovery methods** that design heuristics without LLMs (Reviewer 1).
   - **Other solver enhancements**: No comparison with Gurobi or CPLEX (Reviewer 3) or with mainstream Learn2Branch methods (Reviewers 3, 4). The paper only compares with SCIP and L2DIVE.
   - **Neural combinatorial and evolutionary methods**: The paper does not compare with pure evolutionary or neural combinatorial methods (Reviewer 1).
   - **Learning baselines**: Only L2DIVE is used; how would L2DIVE perform if trained under the same multi-objective setting? The lack of source code for L2DIVE makes this comparison difficult but leaves conclusions weak (Reviewer 4).
   - **Number of MIPLIB instances**: Only 20 instances are evaluated, which is too small to draw robust conclusions (Reviewer 4).

3. **Methodological and presentation concerns**:
   - **Prompt sensitivity** is not investigated (Reviewer 1). The impact of different prompts on the generated heuristics is unknown.
   - **Seed function**: The paper does not define how the initial seed function for evolutionary generation is predefined (Reviewer 5).
   - **Lack of example code evolution**: A step-by-step demonstration of how the code evolves over evolutionary iterations would help readers understand the LLM’s role (Reviewer 1).
   - **Multi-objective evolution for generalization**: The mechanism by which multi-objective evolution improves cross-benchmark generalization is not clearly explained (Reviewers 1, 4).
   - **Notation and writing quality**: The description contains repetitive mathematical symbols (e.g., $n$, $N$, $N_{ins}$, $M$, $r$, $k$ with overlapping meanings) and several grammatical errors (e.g., “After generations of iteration”, “gpt35” instead of “gpt3.5”) (Reviewer 5). Some concepts are inadequately defined (e.g., values in brackets in Table 1 are not explained) (Reviewer 5).
   - **Title too broad**: The title does not reflect that the work only designs diving heuristics, not general CO solver algorithms (Reviewer 4).

4. **Limited scope and evaluation**:
   - **Small problem instances**: The experiments are limited to relatively small MILP instances. It is unclear whether the method scales to larger problems with millions of variables and constraints (Reviewers 2, 3). Performance may degrade on large-scale MIP problems (Reviewer 2).
   - **Solver comparison**: The paper only compares with SCIP, which is weaker than state-of-the-art solvers like Gurobi and CPLEX (Reviewer 3).
   - **Application to other solvers**: The framework is only applied to SCIP’s diving heuristic; its applicability to other solvers (e.g., Concorde for TSP) is not explored (Reviewer 3).
   - **Advantages over Learn2Branch**: The paper does not clarify the advantages of Learn2Dive over Learn2Branch, nor does it compare directly with standard Learn2Branch methods (Reviewer 3).

5. **Minority disagreements and open questions**:
   - Reviewer 2 (score 5) asks whether the method can solve larger problems and whether SOEA trained on one benchmark generalizes to others; Reviewer 3 and 4 also raise the scalability question.
   - Reviewer 1 questions whether strong reasoning models (e.g., o1-preview, o1-mini) provide additional advantages.
   - Reviewer 4 asks: (a) how the multi-objective evolution method differs from prior multi-objective evolutionary optimization with LLMs (e.g., Liu et al., 2023), (b) whether the logical descriptions generated alongside the code correctly represent the meaning of the score functions, and (c) what key differences exist in heuristics generated for different datasets and why.
   - Reviewer 5 asks for ablation specifically evaluating the multi-objective fitness component rather than already‑proven crossover/mutation components.