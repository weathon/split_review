## Summary

The paper proposes Verbalized Graph Representation Learning (VGRL), a framework that uses multiple frozen LLMs (Predictor, Optimizer, Summary) with natural-language "parameters" (textual category descriptions) to perform node classification on text-attributed graphs. The core ideas are: (1) representing model parameters as human-readable text to achieve full interpretability across input, training, and decision stages, and (2) iteratively refining these text descriptions through LLM prompts instead of gradient-based fine-tuning, avoiding costly LLM weight updates.

## Strengths

- **Novel conceptual framing**: The idea of treating model parameters as natural language text (θ ∈ Θ_language) and optimizing them entirely through LLM communication is genuinely novel. This goes beyond prior LLM+GNN work that either fine-tunes LLM weights or uses LLMs only as a one-shot feature enhancer. Section 4.2 formalizes this verbalized-parameter concept with concrete definitions.

- **Proof-of-concept of iterative text-based optimization**: Figure 3 shows accuracy increasing over mini-batch iterations, and the framework uses open-source Llama3.1 8B (line 195), providing a concrete demonstration that performance can be improved via prompt-based text optimization without updating LLM weights.

- **Illustrative case study with end-to-end traceability**: Section 5.4 and Figure 4 trace a single node's prediction through the Predictor LLM's reasoning, the Optimizer LLM's error analysis, and the final decision rationale — all in natural language. This concretely illustrates the transparency the framework aims to achieve.

## Weaknesses

### Fatal
None.

### Major

- **Experimental evaluation is far too limited to support the paper's claims.** The paper tests on only one dataset (Cora), and only a *subset* of its nodes (line 182: "We extracted a subset of nodes from the Cora dataset"). The "baselines" in Table 3 — "Node only" and "Summary" — are stripped-down variants of the authors' own framework, not established methods. There is no comparison to any standard GNN (GCN, GAT, GraphSAGE) or any existing LLM+GNN approach (TAPE, LLM-as-Predictor variants). The paper claims "VGRL achieves better performance" (line 195), but without any external baselines and on a single dataset this is unsupported. The paper lists as a contribution (line 31) "validate the effectiveness of this method from multiple perspectives on real-world datasets," but this is not delivered.

- **The central claim of "full interpretability" is asserted but never validated.** The paper's core contribution is that VGRL is "fully interpretable" across input, training process, and decision-making. However, there is no evaluation of interpretability quality whatsoever: no human study measuring whether users understand the explanations, no faithfulness metrics checking whether the LLM's stated reasoning matches its actual decision process, no comparison of explanation utility against GNNExplainer or any alternative. The paper assumes that because outputs are in natural language, the process is inherently interpretable — but LLM-generated explanations are known to suffer from faithfulness problems (plausible but post-hoc rationalizations). The paper itself criticizes prior work TAPE (line 44: "can only be proven effective indirectly through the performance of downstream tasks") for the same evidential gap it then reproduces.

### Minor

- **Optimization dynamics are uncharacterized.** The optimizer LLM is prompted to generate improved category descriptions based on prediction errors (lines 135–141), but there is no analysis of whether this process reliably improves descriptions, how many iterations are needed, whether it converges, or how sensitive it is to the optimizer prompt Ψ. Without such analysis, the iterative process remains an opaque LLM-prompting loop whose behavior is unpredictable.

- **Theoretical analysis (Section 6) is very weak.** The theorem states: if category descriptions faithfully represent category information (condition 1) and that information is non-redundant with graph structure (condition 2), then they provide useful information for prediction. This is essentially a tautology — the conditions directly assert the conclusion. No proof is given, and no practical method for verifying conditions 1 and 2 is provided. This does not constitute a meaningful theoretical contribution.

- **Experimental reporting is incomplete.** The paper does not state how many nodes were used, the train/validation/test split, or any variance/standard deviation across runs. The phrase "blurred the concept of epochs and treated each batch as a single step" (line 182) is methodologically unclear.

### Trivial

- **Section numbering is disordered** (4.1, 4.5, 4.2, 4.3, 4.4, 4.6), indicating hasty assembly.

## Nice-to-Haves

- A computation cost analysis comparing VGRL (multiple LLM calls per node per iteration) against fine-tuning alternatives would substantiate the efficiency claim.
- Providing the exact prompt templates in full-text form would improve reproducibility.

## Removed Points

These points were flagged by the reviewers but removed per filtering rules. They should be treated with caution.

- "No discussion of faithful explanations from LLMs in related work" — removed per rule: do not mention missing related works (cannot verify what the paper should have cited).
- "Tables are embedded as images and values cannot be verified" — removed: parser artifact, not a paper problem.
- "Full prompts must be provided in the appendix" — removed per rule: complaints about missing appendix content.
- "The paper compares itself against a straw-man version of prior work" — removed: the paper's characterization of prior methods' scope (input-only, training-only, decision-only interpretability) is factually accurate; the real problem (lack of validation) is already covered above.
- Strength Finder's claim of a "theoretical guarantee" — removed: the theorem in Section 6 is too weak/tautological to count as a genuine strength.

## Novel Insights

The harsh critic's observation that the paper reproduces the same evidential gap it criticizes in prior work (TAPE "can only be proven effective indirectly through the performance of downstream tasks") is the sharpest cross-cutting point: the paper faults TAPE for not validating interpretability directly, yet VGRL does the same. Neither reviewer noted that the multi-LLM framework's cost — multiple LLM calls per node per iteration — may undermine the claimed efficiency advantage at any realistic scale; a single finetuning pass could be cheaper than thousands of iterative inference calls.

## Suggestions

1. **Evaluate on at least 3–4 standard benchmarks** (Cora, Citeseer, PubMed, OGBN-ARXIV) against GCN, GAT, GraphSAGE, and TAPE. Report accuracy with variance over multiple runs.
2. **Validate interpretability directly**: Conduct a human evaluation (do users find VGRL's explanations helpful?) or use faithfulness metrics (do the stated rationales actually determine the predictions?). Compare against GNNExplainer's subgraph explanations.
3. **Analyze the optimizer's behavior**: Report convergence curves across multiple random seeds, study sensitivity to the optimizer prompt Ψ, and quantify whether improvements are consistent.
4. **Report basic experimental details**: number of nodes used, train/test split ratio, and standard deviations across runs.

MY FINAL SCORE: <score>3.0</score>
MY FINAL DECISION: <decision>Reject</decision>