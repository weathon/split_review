## Summary

The paper asks whether LLM-generated citation graphs are distinguishable from human ones, building paired graphs for 10,000 focal papers (~275k references from SciSciNet) using GPT-4o and Claude Sonnet 4.5. It evaluates a progressive pipeline: (i) structure-only RF on graph-level descriptors, (ii) RF on aggregated title/abstract embeddings, and (iii) GNNs combining structure and node embeddings. The central finding is that graph topology alone barely separates LLM from human bibliographies (RF ≈0.60), while embeddings sharply boost discriminability (RF ≈0.83, GNNs ≈0.93), implying that detection and debiasing should target semantic content rather than citation topology.

---

## Strengths

- **Clean topology-vs.-semantics decomposition backed by concrete numbers:** Tables 1, 2, and 3, together with Figures 2 and 3, collectively show that RF structural accuracy on GT vs. GPT sits at 0.61, while the same RF on aggregated embeddings reaches 0.83, and GNNs with embedding node features reach up to 93.78% (GAT, Table 3). The random baseline is cleanly separated by structural features (0.89–0.93), ruling out the trivial hypothesis that LLM bibliographies are generically plausible rather than topologically realistic.

- **Rigorous, multi-level random baselines:** Section 3 constructs field-level, subfield-level, and temporally constrained random baselines that preserve out-degree and field distributions while destroying latent citation structure. The temporal baseline explicitly controls for the fact that GPT-4o suggests ~6% post-focal-paper references, yet random graphs remain clearly separable from both GT and LLM graphs even under this constraint (Appendix Figures 14, Table 11), strengthening the causal interpretation.

- **Multi-model and multi-encoder robustness:** The full pipeline is replicated with Claude Sonnet 4.5 (RF GT vs. Claude ≈0.77) and with SPECTER2 embeddings alongside OpenAI embeddings; results persist across all combinations (Section 6, Appendix Figures 6–11). Cross-generator generalization (train on GPT-4o, test on Claude) achieves ≈0.72 RF accuracy, suggesting a shared semantic fingerprint not specific to a single LLM.

- **i.i.d. vector ablation directly validates that gains are semantic:** Section 6 reports that replacing node embeddings with dimension-matched i.i.d. random vectors collapses RF/GNN accuracy to chance. This is a direct internal control showing that feature count, not statistical artifact, explains the embedding gains.

- **Distributional saturation check:** Permutation-averaged Wasserstein distance over accumulated runs (Section 6, Appendix Figure 19) confirms that hyperparameter sweep distributions saturate early, validating that the reported distributions are not undersampled.

---

## Weaknesses

### Fatal
None.

### Major

- **Missing MLP/DeepSets ablation on node embeddings — the GNN's structural credit is unverified.** The paper frames its GNN results as evidence that "learned message passing can match or surpass the signal exposed by simpler baselines" (Section 5) and that GNNs "learn jointly from structure and node text" (Section 1). However, the RF in Section 5 uses a *sum* of all node embedding vectors — a single graph-level vector that discards all positional/structural information. The GNN in Section 6 processes each node's 3072-dimensional embedding individually via message passing. The 10-point gap (RF 83% → GNN 93%) could arise entirely from better non-linear aggregation over the set of node embeddings rather than from any exploitation of graph topology. A straightforward ablation — an MLP or DeepSets model consuming the same per-node embeddings without message passing — is required to separate these two hypotheses. Without it, the 93% accuracy is a real and reproducible number, but the attributed mechanism (joint structure-plus-semantics) is unverified. This is the paper's primary interpretive gap.

### Minor

- **"Accuracies clustering around chance level" is imprecise for structural GNNs.** Section 6 states that "performance drops sharply... with accuracies clustering around chance level" for GNN structural features in the GT vs. GPT task. Table 3 shows GCN at 57.73 ± 2.10 and GAT at 57.40 ± 2.44, which are consistent with the RF structural baseline (~60%) and above chance, whereas GIN at 51.71 is near chance. The generalization is accurate for GIN but not for GCN/GAT. A more precise statement — "no GNN architecture surpasses the RF structural baseline" — would be informative and accurate.

- **Graph size reduction asymmetry is unacknowledged.** Section 3 randomly removes references from ground truth and random graphs to match the smaller GPT-verified-reference count. Randomly dropping human-chosen references may disproportionately remove structurally distinctive references (self-citations, methodological ancestors), potentially compressing the GT distribution toward the LLM distribution. The paper neither acknowledges nor tests this. Given that the directional effect is conservative (it would understate separability, making reported numbers lower bounds), this does not threaten the conclusions but should be noted and, ideally, tested with a sensitivity analysis (e.g., comparing RF accuracy at different trimming fractions).

- **Cross-LLM generalization is buried in appendices.** The train-on-GPT / test-on-Claude result (RF ≈0.72, GNNs above chance) is reported only by reference to appendices in Section 6. This is arguably the most practically relevant result in the paper — it shows detection is not model-specific — and merits a dedicated paragraph in the main body.

### Trivial

- **Edge count as identical node feature:** Section 6 notes that "the graph's total number of edges, which is a graph-level feature, [is] here assigned as node feature in GNN training." Every node in the same graph therefore carries identical values on that dimension, making it usable only for inter-graph discrimination, not intra-graph message passing. The paper states this choice but does not explain the motivation for including it in the node feature vector rather than as a separate graph-level readout.

---

## Nice-to-Haves

- A brief characterization of which semantic dimensions the RF classifier exploits (e.g., top PCA components broken down by recency, prestige proxy, or field-specificity) would transform the conclusion from "detect using semantics" into "detect and correct *this* semantic shift." Section 8 acknowledges this as future work, and the ingredients (embeddings, SciSciNet metadata, RF feature importance) are all present. Even a rough top-20 PCA or cosine-distance decomposition by metadata stratum would substantially strengthen the practical recommendation.

- The i.i.d. ablation (Section 6) is reported in an appendix. Moving it to the main text would pre-empt the most natural alternative explanation for the embedding gains.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Hallucination stratum not covered (Harsh Critic, Section 3 note):** Removed because the paper explicitly scopes this out in Section 8: "we focus solely on the parametrically retrieved references, allowing for a stricter lab setting and probing directly the biases of the models. We do not consider the references that would be obtained when models have access to external databases." This is a deliberate, documented design choice, not a gap.

- **Semantic fingerprint "detected but not characterized" (Harsh Critic):** Weakened to Nice-to-Have. The paper explicitly defers this in Section 8 ("Future work could probe which semantic dimensions drive separability..."), and the discussion in Section 7 does gesture at candidate dimensions (recency tilt, prestige). A paper identifying *that* a semantic fingerprint exists and is detectable makes a complete empirical contribution; characterizing *what* the fingerprint consists of is the natural follow-on study.

- **Strength claim: "Systematic ablation and transparency in evaluation"** (Strength Finder) — Partially retained. The i.i.d. ablation and Wasserstein saturation check are real. However, the claim that "structural features assigned as node features in GNNs are a deliberate choice motivated by prior work on sum-based aggregation" overstates the paper's justification; the paper cites Cui et al. (2022) for sum aggregation in a different context. Retained the i.i.d. ablation as a specific concrete strength; dropped the sum-aggregation justification claim.

---

## Novel Insights

The most noteworthy observation — underscored by the harsh reviewer and only partially surfaced by the paper itself — is the cross-generator result: a classifier trained on GPT-4o bibliography fingerprints transfers to Claude Sonnet 4.5 at ≈0.72 RF accuracy, considerably above chance. This implies that the detectable semantic fingerprint is not idiosyncratic to a single model family but reflects a shared distributional property of frontier LLMs trained on similar corpora, likely encoding shared recency bias, prestige preference, or topical narrowness. If this generalizes to further models, the practical implication is that detection pipelines do not require per-model training — a significant operationally useful observation that the paper presents only in passing.

---

## Suggestions

1. Add an MLP (or DeepSets) baseline that ingests the same per-node embedding sequence without message passing, and report its accuracy alongside Table 3. If the MLP matches the GNN, revise the framing to emphasize "better per-node semantic aggregation vs. sum pooling" rather than "joint structure-plus-semantics." If the GNN exceeds the MLP, the message-passing claim is validated.

2. Promote the cross-generator experiment to the main body (Section 6 or 7) with a dedicated paragraph. The ≈0.72 RF accuracy under generator swap, alongside the GNN above-chance result, is the most deployment-relevant finding and should not be relegated to appendices.

3. Add one sentence to Section 3 acknowledging the conservative direction of the graph-size trimming bias, and if feasible, a brief sensitivity analysis comparing RF accuracy at different trimming levels.

4. Revise "accuracies clustering around chance level" in Section 6 to accurately reflect that GCN/GAT reach ~57-58% (matching the RF structural baseline), while only GIN reaches near-chance. The informative claim is that no GNN architecture surpasses the structural RF.

---

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>

<subscores>
<originality>3</originality>
<importance>4</importance>
<claims_supported>4</claims_supported>
<soundness>3</soundness>
<clarity>4</clarity>
<community_value>4</community_value>
</subscores>