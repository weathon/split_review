## Summary

This paper proposes a framework for graph learning called random walk neural networks, where a random walk on a graph produces a machine-readable record (in plain text) processed by a neural network (typically a transformer language model). The paper proves invariance guarantees with unconstrained reader networks (Theorem 1), universal approximation in probability via cover-time bounds (Theorems 3, 5), and draws a formal parallel to message-passing showing that over-smoothing is structurally avoided while over-squashing manifests as probabilistic under-reaching. Empirically, the method achieves 100% on SR25 (the first walk-based method to solve this 3-WL-hard benchmark), competitive results on 8-cycle counting, and a training-free transductive classification result on ogbn-arxiv using a frozen LLM (74.75% with Llama3-70b).

## Strengths

- **First walk-based method to solve SR25 with 100% accuracy.** Table 1 (line 376) shows DeBERTa-walk achieving 100% on SR25 where AgentNet (6.7%) and CRaWl (46.6%) fail. This directly demonstrates the claim that the framework can separate strongly regular graphs beyond the 3-WL test, an established hard benchmark (line 389-390).

- **Clean, principled decomposition of invariance.** Theorem 1 (line 88-90) and Theorem 2 (line 142-144) show that invariance can be isolated to the random walk algorithm and recording function, placing no constraints on the reader neural network. The anonymization scheme (line 134-136) and named-neighborhoods extension (line 137-139) are constructive, simple, and explicit. This is structurally different from MPNNs where invariance is hard-coded in feature mixing (line 156-157).

- **Connecting over-squashing to probabilistic under-reaching.** Theorem 7 (line 281-287) formalizes that the Jacobian bound for the simplified random walk model is $\frac{1}{l+1}[\sum_{t=0}^l P^t]_{uv}$, matching the MPNN bound structurally but with a different mechanism. This is a genuinely insightful theoretical contribution that reframes the literature's understanding of over-squashing in walk-based methods.

- **Provably finite local cover times on infinite graphs via restarts.** Theorem 5 (line 195-197) proves that any nonzero restart probability guarantees finite cover time for a local ball $B_r(v)$ on an infinite graph, and Theorem 4 (line 192-194) shows this is *not* guaranteed without restarts. This is a rigorous, practical design principle with a clear proof.

- **Named neighborhoods reduce effective coverage from $O(n^3)$ to $O(n^2)$.** The combination of the minimum-degree local rule (Eq. 6, line 115-118) with named neighborhoods (line 149-152) makes edge coverage reducible to vertex coverage, directly shortening the walk length required for universal approximation (Theorem 3, line 222-228).

## Weaknesses

### Major

- **Misleading comparison claim on ogbn-arxiv.** The introduction (line 42) states the method "outperforms message passing networks" on ogbn-arxiv. From Table 3 (lines 465-469, 482-487): Llama3-8b-walk achieves 71.10%, which is **below** GCN (71.74%), GAT (73.91%), and RevGAT (74.26%). Only the 70b variant (74.75%) exceeds the best GNN. The claim as stated is inaccurate for the 8b variant, and the paper never qualifies this with the model-scale asymmetry (70b has ~100× more parameters than any GNN baseline). The core finding — that a frozen LLM can leverage graph structure via random walk prompting — is interesting and novel even with this qualification.

### Minor

- **Over-smoothing analysis uses a simplified averaging model while the paper makes general claims.** Section 3.2 (line 270) introduces "a simple random walk neural network that runs a uniform random walk... reads the record... by averaging." Theorem 6 (line 274-276) proves this model avoids input-independent convergence. The abstract (line 8) and introduction (line 36-37) claim more broadly that over-smoothing is "inherently avoided" and the trade-off is "eliminated" for *random walk neural networks* without qualification. While the structural insight (decoupling feature processing from $P$) plausibly extends to any reader, the formal guarantees are only established for averaging. The paper should either argue why the averaging analysis carries over to transformer readers or qualify the claims.

- **Missing experimental details for the ogbn-arxiv experiment.** The paper does not specify: (1) the walk length or number of steps used, (2) whether restarts were used and with what parameters, (3) how the random walk operates on the directed edges of ogbn-arxiv (follow citation direction, reverse direction, or treat as undirected), (4) how text attributes are truncated to fit within 8,192 tokens given that ~29 vertices with full titles+abstracts are recorded. Line 493 acknowledges directed edges but the footnote (line 74) only says "extending to directed or attributed graphs is possible" without specifying the actual protocol. The result cannot be fully reproduced or assessed without these details.

- **No measures of variance or statistical significance.** No confidence intervals, standard deviations, or significance tests are reported for any experimental result (Tables 1, 2, 3). For stochastic methods involving random walk sampling and LM inference (with sampling hyperparameters), this is a meaningful omission. Table 1 reports training accuracy to one decimal point, which is insufficient to assess reliability.

### Trivial

- The paper uses "Section~ref{sec:algorithm}" in Section 3 (line 203) to reference Section 2, but the actual label appears to be `sec:graph_level` — the reference is broken in the rendered text.

## Nice-to-Haves

- **Ablation studies** would strengthen the paper. Key design choices (anonymization vs. anonymization+named neighborhoods, minimum degree local rule vs. uniform walk, non-backtracking vs. standard, DeBERTa vs. other LMs) are not ablated, making it impossible to attribute which components drive performance.

- **The gap between theoretical walk-length requirements and practical usage** could be discussed. The theory requires $l > C_V(G)/\delta$ for high-confidence approximation (Theorem 3, line 226), which for ogbn-arxiv (n=170k) would be ~$10^{10}$ steps with $O(n^2)$ cover time. Practice uses walks that fit within 8k tokens. A brief discussion of when the theory applies vs. when shorter walks suffice empirically would be welcome, though this gap is common in universal approximation theory.

- **Computational cost comparisons** (wall-clock time, parameter counts, FLOPs) with baselines would help contextualize the results, especially given the large LM backbone.

## Removed Points

These points were raised by reviewers but removed or downgraded from the final assessment with justification:

- **"The over-smoothing analysis is a structural gap that invalidates the paper's core claims"** (from Harsh Critic). Removed as overstated. The simplified model is a standard proxy used in the MPNN literature itself (see line 260: "This simple model is often used as a proxy to study the aforementioned issues" with citations). The structural insight about decoupling feature processing from $P$ is a property of the framework, not just the averaging reader. The concern is reasonable but merits a minor qualification, not a fatal downgrade.

- **"The ogbn-arxiv directed graph issue is an undocumented gap between theory and practice"** (from Harsh Critic partially). Downgraded from potential fatal/structural to minor documentation issue. The paper explicitly acknowledges the directed edges (line 493) and notes extension is possible (line 74 footnote). The concern is about unspecified implementation details, not about the theoretical framework being inapplicable. The results may still be valid; the issue is documentation, not correctness.

- **"Weakness about unfair comparison favoring baselines"** — Not applicable; the asymmetry favors the author's method (70b vs smaller GNNs), which per rules should not be flagged.

- **"The theoretical proof that over-smoothing is inherently avoided"** (from Strength Finder's Strength 2). Not removed — kept as a genuine strength of the simplified model analysis, though qualified as applying to the averaging model.

- **"Missing related works"** — Removed per hard rules.

- **"Formatting/style nitpicks"** — Removed per hard rules.

- **"Reproducibility concerns about unreleased models/code"** — Removed per hard rules (cited references are assumed to exist).

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Clarify the ogbn-arxiv experimental protocol.** Specify walk length, restart parameters, how the walk operates on directed edges (cite direction, reverse, or undirected), how text is truncated to fit the 8,192 token window, and the number of walks per test vertex. Report variance across random seeds or walks.

2. **Qualify the comparison claims.** In the introduction and conclusion, replace "outperforms message passing networks" with a more precise statement, e.g., "the 70b variant achieves 74.75%, exceeding the best GNN (RevGAT, 74.26%), while the 8b variant (71.10%) remains competitive with GCN (71.74%)." Acknowledge the model-scale asymmetry.

3. **Explicitly state the scope of the over-smoothing analysis.** Add a sentence clarifying that Theorem 6 (Theorem 8 in paper's numbering) establishes the principle for a simplified averaging model, and that the structural decoupling property applies to the full transformer-based method, though the formal guarantee for non-linear readers is an open direction.

4. **Add a brief ablation** of at least one design choice (e.g., anonymization vs. anonymization+named neighborhoods, or min-degree vs. uniform walk) on the SR25 or substructure counting dataset to help attribute contributions.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>