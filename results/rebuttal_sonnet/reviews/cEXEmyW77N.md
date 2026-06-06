## Summary

This paper investigates whether LLM-generated citation graphs (GPT-4o and Claude Sonnet 4.5 from parametric knowledge) are distinguishable from human citation graphs. Using 10,000 focal papers (~275k references) from SciSciNet, the authors apply a progressive pipeline—structural feature classifiers (RF) → semantic embedding classifiers → GNNs with embedding node features—and find topology alone barely separates LLM from human graphs (~0.60) while semantic embeddings sharply raise discriminability (~0.83 RF, ~93% GNN). The central conclusion: LLMs mimic citation topology but leave detectable semantic fingerprints, so detection/debiasing should target content signals.

---

## Rebuttal Assessment

- **Weakness:** Missing MLP/DeepSets ablation
  - **Author's response:** Partially address
  - **Assessment:** Partially convincing — The author correctly argues that the paper's *central* thesis (structure-vs.-semantics dichotomy) is independently established by the RF comparisons (Table 1: 0.61 structural vs. Table 2: 0.83 embedding), without requiring the GNN gains to be causally attributed to message passing. This is a valid point verified in the paper: Section 5's RF embeddings result (0.8346) alone establishes the key dichotomy. The author also notes that the Section 6 framing "learn jointly from structure and node text" describes input modalities rather than causal attribution—verified in the paper. However, this is a post-hoc reframing: the paper's progression explicitly presents GNNs as yielding "further gains" above the RF, and the text says GNNs "learn jointly from structure and node text, yielding further gains." This implies topology contributes to the GNN gain, which remains unverified without the MLP baseline. The commitment to add one in revision does not help the current submission.
  - **Score impact:** Weakness downgraded (from major to moderate-major) — the core structure-semantics finding is independently supported, but the GNN framing remains interpretively unsupported.

- **Weakness:** Semantic fingerprint detected but not characterized
  - **Author's response:** Acknowledge
  - **Assessment:** Unconvincing as a mitigation — The author points to Figure 3(b-c) cosine/Euclidean distance diagnostics and the RF leaf depth observation. Verified: Figure 3(b-c) exists in the paper and shows aggregate alignment differences. However, aggregate cosine similarity comparisons do not characterize *which* semantic dimensions (recency, prestige, topical breadth) drive discriminability—which was the reviewer's request. The author acknowledges this outright as a valid limitation.
  - **Score impact:** Weakness unchanged — acknowledged but not resolved.

- **Weakness:** Cross-LLM generalization underemphasized
  - **Author's response:** Partially address
  - **Assessment:** Partially convincing — Verified: Section 6 does contain the sentence "Training on GPT-4o and testing on Claude Sonnet 4.5 yields substantial above-chance generalization for all GNNs (See results in Appendix 8); an RF trained on GPT-4o also reaches ≈0.72 when the generator is swapped at test time (See results in Appendix 9)." Section 7 also briefly mentions "cross-generator experiments." So the finding is technically in the main body. However, the author concedes it merits expansion and detailed results remain in the appendix. The finding is present but underemphasized, as originally flagged.
  - **Score impact:** Weakness downgraded (from minor to trivial) — the finding is in the main body; the concern is one of emphasis, not absence.

- **Weakness:** Minor reporting imprecision on structural GNN results
  - **Author's response:** Partially address
  - **Assessment:** Convincing on the substance — Verified: Table 3 shows GCN 57.73%, GAT 57.40%, GIN 51.71%. The paper text says "accuracies clustering around chance level," which is accurate for GIN but imprecise for GCN and GAT. The author acknowledges this imprecision and agrees the corrected statement should be "no GNN architecture exceeds the RF structural baseline of 0.61." This is factually the correct and more informative formulation.
  - **Score impact:** Weakness unchanged (trivial) — acknowledged imprecision; the result itself is unaffected.

- **Weakness:** Graph size equalization unanalyzed
  - **Author's response:** Partially address
  - **Assessment:** Partially convincing — The author correctly reasons that random removal of human references biases toward *underestimating* separability, making the 83–93% figures conservative. This is a sound argument, though it is not stated in the paper. The multiple robustness checks across embeddings and LLM families provide indirect confidence. The paper does not explicitly analyze the equalization procedure's effect.
  - **Score impact:** Weakness downgraded (from minor to trivial) — the direction of bias is toward conservatism, supported by consistent robustness results.

- **Weakness:** Edge count as node-level feature unexplained
  - **Author's response:** Partially address
  - **Assessment:** Partially convincing — Verified: Section 6 explicitly states "the graph's total number of edges, which is a graph level features but here assigned as node feature in GNN training." The pooling rationale (sum-based aggregation recovers graph-level constant) is cited via Cui et al. (2022). The reviewer's observation that this provides no within-graph discrimination is correct and acknowledged by the author.
  - **Score impact:** Weakness unchanged (trivial).

---

## Strengths

- **Clear topology–semantics decomposition with monotonically increasing quantitative evidence.** RF on structural features reaches 0.61 (Table 1), RF on aggregated embeddings reaches 0.83 (Table 2), GNNs with embedding node features reach 93% (Table 3), with Figure 2 showing near-complete structural overlap and Figure 3 showing embedding-space separation.
- **Rigorous field-matched random baselines rule out trivial explanations.** Random graphs are cleanly separated at 0.89–0.93, confirming LLM bibliographies achieve non-trivial structural realism.
- **Robustness across model families and embedding backbones.** Results replicated with Claude Sonnet 4.5 (RF ≈ 0.77) and SPECTER2/OpenAI embeddings, with consistent patterns.
- **i.i.d. random vector ablation confirms semantic basis of GNN gains.** Section 6 explicitly reports that RF/GNN accuracy collapses to chance when node embeddings are replaced with random vectors, ruling out dimensionality artifacts.
- **Cross-LLM generalization is present in main body.** Section 6 reports ~0.72 RF cross-generator accuracy, suggesting a shared semantic fingerprint across LLM families.

---

## Weaknesses

### Fatal
None.

### Major
- **Missing MLP/DeepSets ablation (downgraded from original, but not eliminated).** The ~10-point GNN gain over RF (0.83 → 0.93) remains attributed to "joint structure and text learning" without an MLP/DeepSets control using per-node embeddings. The author's reframing—that the core dichotomy is established by RF comparisons alone—is valid, and the paper's primary claim is supported independently. However, the GNN framing in Section 6 implies topology contributes to the gain, which is the interpretive claim that remains untested.

### Minor
- **Semantic fingerprint detected but not characterized.** The practical recommendation to "target content signals" remains underspecified. No first-order characterization of which semantic dimensions (recency, prestige, topical breadth) drive discriminability appears in the paper, despite Figure 3's aggregate similarity diagnostics and appendix RF leaf depth information. This gap limits the actionability of the paper's conclusions.

### Trivial
- **Cross-LLM generalization underemphasized.** Present in Section 6 and 7 but treated briefly; detailed results relegated to appendix.
- **Minor imprecision in structural GNN characterization.** The claim "clustering around chance level" is inaccurate for GCN (57.73%) and GAT (57.40%), which are closer to the RF structural baseline. The correct statement—"no GNN exceeds the RF structural baseline"—is more informative and should replace the current text.
- **Graph size equalization unanalyzed.** Bias direction is toward conservatism (i.e., underestimating separability), but this is not stated in the paper.

---

## Nice-to-Haves

- Add an MLP/DeepSets baseline on per-node embeddings to clarify whether message passing contributes beyond better pooling—either result would sharpen the GNN framing.
- Characterize semantic fingerprint with RF feature importance or cosine similarity breakdowns stratified by recency/prestige/topical breadth.
- Expand cross-LLM generalization to a dedicated paragraph with numerical results in main body.

---

## Novel Insights

The cross-generator generalization finding (RF trained on GPT-4o reaches ~0.72 when tested on Claude Sonnet 4.5) is the paper's most practically significant result and suggests the semantic fingerprint of LLM bibliographies reflects a shared distributional signature—plausibly arising from common training-data recency and prestige biases—rather than architecture-specific behavior. This makes detection model-agnostic in a practically important sense. The paper's progressive pipeline also provides a clean methodological baseline: if structure-only approaches reach ~0.61 while embedding approaches reach ~0.83, the practical implication is clear even without GNN sophistication.

---

## Suggestions

1. Add an MLP/DeepSets baseline on per-node embeddings (no message passing) to isolate whether topology contributes to GNN gains beyond richer aggregation.
2. Provide at least first-order characterization of semantic fingerprint (e.g., RF feature importance, cosine similarity stratified by recency or prestige of included references).
3. Correct Section 6 text from "clustering around chance level" to "no GNN architecture exceeds the RF structural baseline of 0.61" for GCN/GAT/GraphSAGE structural results.

---

## Score and Decision

The rebuttal is honest and does not reveal additional problems. The author's core argument—that the structure-vs.-semantics dichotomy is independently established by RF comparisons, irrespective of GNN interpretation—is verified against the paper and is valid. This partially mitigates the major weakness. However, the GNN framing remains interpretively unsupported in the current submission (no MLP baseline), and the semantic fingerprint goes uncharacterized, limiting actionability. The minor imprecisions and underemphasized findings are acknowledged but not resolved. On balance, the rebuttal justifies downgrading the major weakness but not eliminating it, and the score should remain at 5.0—solid empirical work with clean baselines, but methodologically less novel than accepted papers proposing new methods, and with an underspecified GNN interpretation claim.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Accept</decision>