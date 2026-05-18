Now I have all the information I need. Let me compile the final consolidated review.

---

## Summary

This paper proposes TopInG, a framework for intrinsically interpretable graph learning that uses persistent homology to distinguish rationale subgraphs from noise. The key ideas are: (1) learning a filtration function that orders edges by importance, modeling a generating process where the rationale subgraph is built first; (2) a topological discrepancy loss based on Wasserstein distance between persistence diagram distributions; and (3) theoretical guarantees (Theorem 3.4) that the ground-truth rationale subgraph uniquely optimizes this loss under certain conditions. Empirical results on synthetic and real benchmarks show improvements over prior interpretable GNN methods.

## Strengths

- **Novel topological framework with a uniqueness guarantee.** The paper introduces persistent rationale filtration learning, a genuinely new perspective on the rationale subgraph identification problem. Theorem 3.2 provides upper and lower bounds for the topological discrepancy, and Theorem 3.4 proves that under stated conditions the ground-truth rationale subgraph is the unique optimum of the proposed loss. Remark 3.5 correctly notes this guarantee does not require invariance across instances — a genuine advance over prior work that assumes stable/invariant rationales. *(Supported: lines 115–143)*

- **Stable performance on variiform rationale subgraphs.** Figure 3 demonstrates that as the number of rationale subgraphs grows (BA-HouseOrGrid-nRnd dataset), TopInG's interpretation AUC remains near-constant while DIR and GSAT degrade sharply. The paper created this synthetic dataset specifically to test this challenge, and the results directly validate the core claim about handling variable rationales. *(Supported: lines 196, 203)*

- **Principled approximation of the topological constraint.** The lower bound of topological discrepancy is approximated using learnable, Lipschitz-continuous vectorizations of persistence diagrams with multi-head attention (Remark 3.3). This provides a tractable, differentiable loss that adaptively focuses on relevant topological features — a practical bridge between the abstract theory and a trainable model. *(Supported: lines 117–137)*

- **Bimodal prior regularization addresses attention collapse.** The paper uses a mixture-of-Gaussians prior with a penalty term to prevent mode collapse, explicitly contrasting this with GSAT's unimodal prior (Section 3.3). The ablation (Table 3, Figure 4) shows that the topological and prior components play complementary roles. *(Supported: lines 147–159, 170–173)*

## Weaknesses

### Fatal

None.

### Major

- **Confounded experimental comparison due to different backbones.** The paper states: "GIN is used as the backbone model for baselines" and "We first apply CINPP as our backbone" (lines 190–192). This means TopInG's quantitative results in Tables 1 and 2 reflect the combination of the topological loss *and* a more expressive backbone (CINPP supports general filtrations on simplicial/cell complexes), while all baselines use GIN. The paper's central empirical claim — that the topological framework itself improves interpretation and prediction — cannot be cleanly attributed from these comparisons. The justification ("to test the wide applicability of TOPING") does not resolve the confound. An ablation running TopInG with a GIN backbone on a representative subset of datasets is necessary to isolate the contribution of the topological loss. Without this, the quantitative comparisons in Tables 1 and 2 are not interpretable as evidence for the proposed method's effectiveness.

### Minor

- **Inconsistent description of the extraction procedure.** The method section (line 111) says "For simplicity, one can just consider σ to be a hard cut with threshold value t=0.5" to separate rationale from noise. But Section 3.3 (line 170) states "in practice we do not use a hard threshold to filter the graphs. What we do is computing the persistent homology along ascending ordering and descending ordering separately, to mimic a hard cut." While the two statements are reconcilable — the hard cut is a conceptual simplification, and the ascending/descending computation is the practical implementation — the presentation is confusing. The paper should unify the description and explicitly state what extraction procedure is used during training versus inference, and how the topological loss relates to the final extracted subgraph.

- **Theoretical assumptions not examined relative to experimental domains.** Theorem 3.4 assumes |E_X| < |E_ϵ| and that G_X* is minimal (any proper subgraph loses label information). These are reasonable for a first theoretical result, but the paper does not discuss whether these conditions hold for the datasets tested or how violations would affect the guarantee. Adding a brief discussion of when the assumptions are plausible (e.g., rationale is typically smaller than noise in the test domains) would strengthen the connection between theory and experiments.

- **"Self-adjusted" mechanism is vaguely described.** The term "self-adjusted" is used repeatedly (lines 6, 22, 113, 137, 172) to describe the topological constraint, but the mechanism is simply multi-head attention over vectorized persistence diagrams selecting top-2 maximums (Remark 3.3). The paper should define what "self-adjusted" means concretely — it appears to refer to the attention mechanism's ability to focus on data-dependent topological features during training, which is standard attention behavior rather than a distinct adaptive mechanism.

- **The "up to 20%+" claim is imprecise.** The abstract and contributions (lines 9, 24) state improvements "up to 20%+ on both predictive accuracy and interpretation quality." This is technically defensible as a "best-case" claim but suggests typical gains of this magnitude, which is not supported by the tables across all datasets. The paper should qualify which specific datasets and metrics justify this number and report aggregate gains more precisely.

### Trivial

- **Statistical significance reporting is ad hoc.** The shadowed entries in tables are defined as "mean-1*std larger than the mean of the corresponding best baselines" (lines 205, 209). This threshold is not a standard significance test. Using confidence intervals or paired statistical tests would be more standard, though this is a minor presentation issue given the field's norms.

## Nice-to-Haves

- An ablation using TopInG with a GIN backbone on a subset of datasets (e.g., SPmotif0.5, BA-HouseOrGrid-nRnd) would cleanly isolate the topological contribution from the backbone choice.
- Reporting training time and memory comparisons would help practitioners assess the computational trade-off, which the paper's limitation section (lines 228–231) acknowledges as a bottleneck.
- Visualizing learned filtrations for multiple instances (beyond Figure 1) would further illustrate how the method separates rationale from noise despite variability.

## Removed Points

These points were flagged by reviewers but are removed or downgraded per policy:

- **Typographical error criticisms** (e.g., "varriform", "descrepency", "Na¨ıve", "theoritical"): Removed per instruction — these are parser artifacts, not author errors in the original submission.
- **Criticism that the proof is relegated to the appendix and "cannot be verified from the main text"**: Removed per instruction — the parser strips appendix content; the appendix exists in the original submission.
- **"Missing specific numbers in ablation table"**: The table is presented as an image (parser limitation). The original submission contains the numeric values in the table; this criticism stems from the text extraction rather than a genuine paper flaw.
- **Strength from Strength Finder about "Empirical gains exceeding 20% on both interpretation and prediction"**: Moved here because this claimed strength conflicts with the verified weakness about confounded backbones — the attribution of these gains to the topological framework specifically is undermined by the backbone mismatch.
- **Strength from Strength Finder about "Strong performance on spurious-correlation benchmarks"**: Same reason — the backbone confound applies equally to these results.

## Novel Insights

None beyond the paper's own contributions. The reviews surface a clear tension between the paper's genuine theoretical novelty and a methodological confound in its empirical evaluation, but this is a standard peer-review observation rather than a novel insight.

## Suggestions

1. **Run TopInG with a GIN backbone** on a representative subset of datasets (SPmotif0.5, BA-HouseOrGrid-nRnd). If performance holds, the topological loss is the driver; if it drops, either discuss the synergy or recompute baselines with CINPP.
2. **Unify the extraction procedure description**: explicitly state whether a hard threshold or the ascending/descending filtration is used during training and inference, and clarify the connection between the two descriptions.
3. **Add a brief discussion** of when the theoretical assumptions (|E_X| < |E_ϵ|, minimality of G_X*) are likely to hold in the experimental domains and what violations would imply.
4. **Provide a proof sketch** of Theorem 3.4 in the main text (the key steps and how assumptions are used) to make the theoretical contribution more transparent.
5. **Report quantitative values** in the ablation analysis and include error bars in sensitivity plots.

## Score and Decision

The paper introduces a novel and theoretically grounded topological framework for interpretable graph learning, with a genuine advance in handling variiform rationale subgraphs. The theoretical bounds and uniqueness guarantee are contributions that stand independently of the experiments. However, the empirical evaluation has a significant confound — the method uses CINPP while baselines use GIN — that prevents clean attribution of the reported gains to the proposed topological loss. This issue is addressable but requires additional experiments. The presentation also has several clarity issues that need revision.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>