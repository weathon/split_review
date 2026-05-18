Now I have a thorough understanding of the paper and can produce the consolidated review.

## Summary

The paper proposes TAMO, a framework that treats tables as an independent modality by encoding their structural information via a permutation-invariant hypergraph neural network and injecting the resulting representations into LLMs as learnable soft prompts. The paper also introduces StructQA, a new benchmark designed to evaluate table structure understanding. On five datasets (HiTab, WikiTQ, WikiSQL, FeTaQA, and StructQA), TAMO achieves an average relative gain of 42.65% over pure-text baselines in the frozen LLM setting and remains competitive with or exceeds fine-tuned baselines.

## Strengths

- **Novel paradigm of encoding tables as an independent modality for LLMs.** The paper reframes table reasoning as a multimodal problem by learning a separate structural representation via hypergraph encoding and injecting it as a soft prompt. This goes well beyond prior work that relies solely on serialization or formatting tricks. The probing experiment (Figure 2) showing GPT-4 and TableLlama below 40% answer consistency under permutation directly motivates the approach.

- **Hypergraph modeling that jointly captures hierarchy and permutation invariance.** The construction in Section 2.2 converts arbitrary tables (flat or hierarchical) into hypergraphs where leaf cells are nodes and row/column headers are hyperedges. The use of Set Transformer-based multiset functions as inductive biases ensures the encoder processes sets of nodes/hyperedges in a permutation-invariant manner — a principled choice that aligns with the structural properties of tabular data.

- **Consistent and substantial empirical gains across diverse settings.** On five benchmarks under frozen-LLM, LoRA, and full SFT settings, TAMO consistently improves over text-only counterparts (Table 2). The 42.65% average relative gain in the frozen setting and the ability to outperform GPT-3.5/GPT-4 on 4 of 5 datasets are striking. The method also scales across different LLMs (TableLlama, Mistral-7B, Llama3) as shown in Table 3 and remains computationally efficient (Figure 7).

- **StructQA benchmark for isolating table structure understanding.** The benchmark (Section 3.1, Appendix B) targets five specific structural reasoning tasks and evaluates models along three axes: direct accuracy, permuted accuracy, and answer consistency. This fills a gap in existing evaluation suites and cleanly exposes LLMs' inability to handle structural variation — a finding that generalizes beyond the paper's own method.

## Weaknesses

### Fatal

None.

### Major

- **Missing explanation of how multiple structure tokens are generated, creating a contradiction between the methodology description and the experiment.** Section 2.3 defines the structure representation as a single pooled vector: $\mathbf{X}_{st} = \text{MLP}(\text{Pooling}(\hat{\mathbf{X}}_\mathcal{V}, \hat{\mathbf{X}}_\mathcal{E})) \in \mathbb{R}^{d_l}$. This is a single $d_l$-dimensional vector, implying one token. Yet Section 3.8 explicitly varies the "number of table structure tokens" from 1 to 9 (Figure 8), and the default setup uses a single token (Figure 5 refers to "[table structure token]" in the singular). The paper never explains how multiple tokens are derived — whether from multiple seed vectors in the Set Transformer (the parameter `S` is described as a "trainable parameter vector," singular), from multiple MLP output heads, or via some other mechanism. This is not a minor omission: it directly affects reproducibility and the interpretation of whether gains come from the hypergraph encoder or from an undocumented architectural choice for token expansion. Readers cannot replicate the method or evaluate the reported token-count experiments without this clarification.

### Minor

- **Permutation invariance claim is underspecified and conflates structural topology with content.** The paper (line 68) states that "altering rows or columns maintains a consistent graph structure (both nodes and edges), effectively reflecting the permutation invariance of tables." This is true for the hypergraph *topology* (which positions belong to which row/column hyperedges) but does not address the content side: node embeddings carry cell values, and when cells are permuted, the initial node representations change accordingly. The encoder's multiset functions operate on these content-bearing representations. The paper should state formally what the encoder is invariant to (the set of connections between positions) and what it is not (the binding of values to positions). The empirical robustness experiment (Section 3.6) is a valid practical test, but the framing conflates two distinct notions of invariance, which can confuse readers. A cleaner experiment would be to measure answer variance across multiple random permutations of the *same table at test time* and report the distribution rather than a single permuted score.

- **Node embedding initialization is not specified.** The paper does not describe how the initial node embeddings $\mathbf{x}_v$ and hyperedge embeddings $\mathbf{x}_e$ are obtained (Section 2.2). Are they derived from cell text via an embedding layer, randomly initialized and learned, or obtained from a pre-trained text encoder? The answer changes how the encoder is interpreted: text-based initialization would mean the encoder partially duplicates the LLM's own text processing, while random initialization would emphasize purely structural learning. This should be clarified.

- **Selective omission of training hyperparameters.** Learning rates, batch sizes, optimizer choices, number of encoder layers, and LoRA rank are not reported. Given the large gains (42.65%), knowing the sensitivity of results to these choices is important for evaluating baseline fairness and reproducibility.

- **No error bars or confidence intervals.** None of the results in Tables 2 or 3 include standard deviations or confidence intervals, despite the modest size of the StructQA test set (1500 samples) and the inherent stochasticity of LLM generation. While single runs are common in cost-intensive LLM experiments, the paper's largest quantitative claim (42.65% average gain) rests on a single pass per configuration, raising the possibility that results are inflated by outlier runs.

- **"First to input table structures into LLMs" is slightly overstated.** Prior work (e.g., Chain-of-Table's structural operations, StructGPT's iterative structured reasoning, TableLlama's fine-tuning with structural formatting) has provided structural information to LLMs through prompting or formatting conventions. The genuine novelty is encoding tables as a *separate learned modality* via hypergraph features — not the basic idea of providing structure. The current phrasing invites unnecessary pushback and could be tightened.

### Trivial

- None identified that survive the filtering rules.

## Nice-to-Haves

- **Structure-aware serialization baseline.** The paper could strengthen its case by including a baseline that uses a more structure-aware text serialization (e.g., HTML-like markup with explicit row/col tags) to rule out the possibility that the large gains partly reflect suboptimal serialization choices for text-only baselines.
- **Ablation of hypergraph encoder vs. simpler positional encoding.** Replacing the hypergraph encoder with learned row/column position embeddings added to cell tokens would disentangle the benefit of hypergraph-specific interactions from the more general benefit of explicit positional signals.
- **Larger or more diverse StructQA construction.** Using 500 tables from WikiTQ with 3 templates per task is modest. Expanding to more tables and templates would increase coverage and reduce the risk of pattern learning.

## Removed Points

These points were flagged by individual reviewers but are either factually incorrect with respect to the paper, reflect misunderstandings, or violate the filtering rules:

- **"Baseline unfairness due to potentially poor serialization."** The paper follows standard, established serialization conventions (markdown-like, per Herzig et al. 2020; Zhang et al. 2023b; Wang et al. 2024). Speculating that serialization was deliberately weakened is unsupported. Removed per rule on baseline asymmetry and strawman weaknesses.
- **"StructQA tasks are trivially solvable by scripts."** The benchmark is designed to evaluate LLMs' structural understanding, not to be hard for deterministic programs. The key finding that LLMs fail dramatically at these tasks is the contribution. This criticism misses the purpose of the benchmark. Removed.
- **"Missing appendix, proofs, or references."** Parser-stripped sections are not author omissions. Removed per rules.
- **Various formatting/style nitpicks.** Removed per rules.
- **"Related work missing."** The reviewer has no external basis to confirm this and the paper's related work section (Section 4) covers the relevant areas. Removed per rules.

## Novel Insights

The reviews converge on a useful insight not fully articulated in the paper itself: the distinction between *structural invariance* (the hypergraph topology being unchanged under permutation) and *representational invariance* (the encoder output being unchanged under permutation of cell values across positions) is where the paper's theoretical framing is imprecise. The hypergraph encoder is invariant to the former by design, while the latter would be undesirable (it would destroy table semantics). Clarifying this distinction would not only strengthen the paper but also provide a general framework for thinking about what "permutation invariance" means for structured data modalities — a conceptual point that extends beyond this specific method.

## Suggestions

1. **Clarify the multiple-token mechanism.** Explicitly describe how $\mathbf{X}_{st}$ is expanded from a single vector to $k$ tokens (e.g., using $k$ seed vectors in the Set Transformer, or an MLP with $k$ output heads). If the default is a single token, state this clearly and explain that Section 3.8 uses a different variant. This is the single highest-impact fix for reproducibility.

2. **Specify node/hyperedge initialization.** State whether node embeddings are derived from cell text (and via what encoder), randomly initialized, or learned from scratch. This affects how readers interpret whether the encoder captures semantics or only structure.

3. **Provide a formal invariance statement.** Replace the informal "consistent graph structure" phrasing with a precise statement of what the encoder is invariant to (permutation of node ordering within each multiset operation) and what it is not invariant to (the binding of cell values to positions). Include an experiment measuring answer variance over multiple random permutations of the same test table.

4. **Add error bars or confidence intervals** for at least the main results (Table 2), particularly given the large claimed gains. If this is computationally prohibitive, report results over multiple random seeds for the smaller StructQA experiments.

## Score and Decision

**Originality:** High — treating tables as a separate learned modality via hypergraph encoding is genuinely novel.  
**Importance:** High — table reasoning is a critical application area, and the paper identifies and addresses a real limitation of current methods.  
**Claims:** Mostly well-supported, but the technical ambiguity around token generation and the imprecise invariance framing weaken the core methodological claims.  
**Soundness:** Adequate — the experimental setup is reasonable, the baselines are appropriate, and the results are consistent. The missing implementation details and lack of error bars temper confidence somewhat.  
**Clarity:** Fair — the ideas are communicated clearly at a high level, but critical technical details (token generation, node initialization, training hyperparameters) are missing. The invariance discussion conflates two distinct notions.  
**Value:** High — the benchmark (StructQA), the empirical demonstration of LLM failures on structural reasoning, and the TAMO framework all provide useful contributions to the community.

The paper's core contribution is solid, the experiments are extensive and directionally convincing, and the StructQA benchmark is a useful resource. The main weakness — the unexplained gap between the single-vector definition and the multi-token experiment — is a reproducibility issue that can be resolved with clarification, not a structural flaw. However, as it stands, the paper cannot be evaluated with full confidence without this resolution.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>