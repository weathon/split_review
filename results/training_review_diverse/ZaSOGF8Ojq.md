I've now thoroughly read the paper and analyzed all reviewer claims against the actual text. Let me produce the consolidated review.

---

## Summary

This paper proposes TOPING, a framework for intrinsically interpretable graph learning that leverages persistent homology to learn a filtration separating rationale subgraphs from their complements. The key idea is a "topological discrepancy" loss — a Wasserstein distance between distributions of persistence diagrams from the two subfiltrations — which encourages the model to learn a filtration that creates a persistent topological gap between rationale and noise edges. The paper provides theoretical bounds (Theorem 3.2), a tractable lower-bound approximation via learned Lipschitz vectorization, and Theorem 3.4 claiming the ground-truth indicator uniquely optimizes the topological discrepancy under certain conditions. Experiments on eight synthetic and real-world graph datasets show improvements over baselines in both interpretation AUC and prediction accuracy, including a new variiform-rationale challenge.

## Strengths

1. **Novel integration of persistent homology with intrinsically interpretable GNNs.** The paper provides a genuinely new perspective by modeling graph attention as a generating process and using persistent homology to track topological features through a learned filtration (Section 3). Figure 1 gives a concrete intuitive illustration showing how the learned filtration creates a persistent gap between rationale and noise edges. This is a clear departure from prior attention-based (GSAT, GMT) or invariance-based (DIR) approaches.

2. **Tractable lower-bound approximation with theoretical grounding.** Theorem 3.2 provides an upper and lower bound for the topological discrepancy. The lower bound is realized via Lipschitz-continuous vectorization functions (Hofer et al., 2019) with multi-head attention (Remark 3.3), making the otherwise abstract topological Wasserstein distance computable in practice. The connection between the bounds and the known $d_{\mathrm{GH}}$-stability of bottleneck distance is sensible given the paper's framing.

3. **Consistent and substantial empirical gains across multiple benchmarks.** Interpretation AUC improvements are reported on nearly all datasets, with especially notable margins on SpuriousMotif datasets (Section 4.2). The variiform-rationale experiment (BA-HouseOrGrid-nRnd, Figure 3) demonstrates a meaningful failure mode of existing methods that TOPING handles better, directly supporting the paper's core motivation.

4. **Honest acknowledgment of limitations.** Section 5.1 clearly discusses the computational bottleneck from CPU-based persistent homology computation and the lack of GPU acceleration, which is refreshingly candid and helps the community understand practical trade-offs.

## Weaknesses

### Fatal

None.

### Major

- **Ambiguity in experimental backbone specification.** The Setup paragraph (Section 4.1) states: "GIN is used as the backbone model for baselines. Furthermore... We first apply CINPP as our backbone to test the wide applicability of TOPING." This phrasing is genuinely ambiguous about which backbone TOPING uses in the main results (Tables 1 and 2). The paper also claims "All methods adopt the same graph encoder and optimization protocol to ensure fair comparisons," which suggests the main results use GIN for all methods with CINPP as a separate test of generality. However, the wording "GIN is used as the backbone model for baselines" could be read as implying TOPING does not use GIN. **The authors must explicitly state which backbone TOPING uses in each table and, if the main results use the same backbone as baselines, confirm this unambiguously.** If TOPING uses a more expressive backbone (CINPP) while baselines use GIN, the reported improvements cannot be attributed to the proposed method.

### Minor

- **Theorem 3.4 lacks a proof sketch in the main text.** The paper states "The proof is a bit technical" and provides no intuition for the uniqueness claim. While the full proof likely appears in the appendix (which is stripped by the parser), the lack of even a brief sketch in the main body makes it impossible for readers to assess the plausibility of the result. The conditions ($|E_X| < |E_\epsilon|$, minimality of $G_X^*$) are stated, but how these interact with the Wasserstein distance on persistence-diagram distributions to yield a unique indicator function is not explained. Adding a 3–5 sentence proof sketch would significantly strengthen the paper.

- **Implementation of the threshold $t$ in the topological discrepancy loss is underspecified.** The loss $d_{\mathrm{topo}}(\mathbb{P}(\mathcal{T}\circ\mathcal{F}_\phi(G_{\leq t})), \mathbb{P}(\mathcal{T}\circ\mathcal{F}_\phi(G_{\geq t})))$ depends on a global threshold $t$, and the same symbol $t=0.5$ is used for the extraction function $\sigma$. The Related Work section (line 170) mentions "computing the persistent homology along ascending ordering and descending ordering separately, to mimic a hard cut," which addresses the concern in principle, but the exact algorithmic procedure — whether $t$ is fixed, learned, or swept — is not described. This should be clarified with a short algorithmic description or pseudocode.

- **New hyperparameters are not tabulated.** The method introduces several parameters ($\alpha$, $\beta$, $\gamma$, learnable prior variances $r_1, r_2$, attention heads=2, vectorization dimension $k=8$, Gumbel-Softmax temperature). While $k=8$ and the 2-head attention are mentioned, the values/ranges for $\alpha,\beta,\gamma$ on each dataset are not reported. The paper says hyperparameters follow previous work, but these are new to TOPING. A supplementary table would aid reproducibility.

- **Non-standard significance reporting.** The paper uses "mean $-$ 1$\times$std larger than the mean of the corresponding best baselines" (Tables 1 and 2 captions) rather than paired statistical tests or explicitly marking significant differences. The metric is unusual and less informative than standard practices (e.g., reporting whether improvements are significant at $p<0.05$). This does not invalidate the results but makes them harder to interpret.

### Trivial

- Theorem 3.4 has a typo: "losses" should be "loses."
- Inconsistent capitalization: "TopIng" in the abstract vs. "TOPING" elsewhere.
- Figure references (Table 3, Figure 4) are described textually without visible numerical values in the extracted text (parser artifact — images stripped).

## Nice-to-Haves

- An explicit comparison of the bimodal KL prior against simpler alternatives (e.g., entropy regularization on attention, or a unimodal prior as in GSAT) on one dataset would help justify the design choice. The paper's discussion in Section 3.3 provides qualitative motivation, but controlled experiments would strengthen it.
- A deeper analysis of what the learned filtration functions capture beyond the single example in Figure 1 — for instance, visualizing persistence gaps across the dataset distribution or correlating gap size with interpretation quality — would be illuminating.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **Theorem 3.4 "unsubstantiated and likely overstated"** — The harsh critic's claim that the proof is missing and the logic is suspect. The full proof is (presumably) in the appendix, which the parser strips. The paper states specific conditions under which the claim holds. Without seeing the proof, the reviewer's speculation about the claim being "implausibly strong" is unfounded. Removed per rule: "REMOVE weaknesses about missing appendix, missing proofs in appendix, or absent references."

- **"Unfair comparison due to mismatched backbones" framed as a critical experimental flaw** — The reviewer asserts that "if TOPING uses CINPP while all baselines use GIN, then the reported improvements... could be driven by the backbone difference." The paper explicitly states "All methods adopt the same graph encoder and optimization protocol to ensure fair comparisons." The wording about CINPP appears to describe an additional experiment testing generality. The criticism is based on a possible misreading of ambiguous but not contradictory text. Downgraded to Major (requiring clarification) rather than a fatal flaw.

- **Tables presented as images / "cannot inspect the actual numbers"** — This is a parser artifact from PDF extraction, not a paper flaw. Removed.

- **"No analysis of the learned filtrations"** — Figure 1 and its long caption provide substantial analysis of a learned filtration example, including the persistence gap. The reviewer appears to have missed this. Removed.

- **Missing related works** — Per rule, I cannot confirm or deny the existence of missing references. Removed.

- **Formatting/style nitpicks (typos, grammar)** — Removed per rule, though a few substantive ones are noted in Trivial.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a new perspective on the work that the paper itself does not already articulate.

## Suggestions

1. **Clarify the backbone.** In the Setup section, explicitly state: "In all main results (Tables 1 and 2), both TOPING and all baselines use GIN as the backbone. We additionally test TOPING with CINPP in [specific experiment] to demonstrate generality." This single change would resolve the most significant concern.

2. **Provide a proof sketch for Theorem 3.4.** Add 3–5 sentences explaining the intuition: how the conditions ($|E_X| < |E_\epsilon|$, minimality of $G_X^*$) together with the structure of $d_{\mathrm{topo}}$ force the optimal $f_\phi$ to be the indicator of $G_X^*$, and why this solution is unique.

3. **Clarify the threshold $t$ implementation.** Add a brief algorithmic description of how the topological discrepancy is computed in practice, explaining the "ascending and descending ordering" workaround and whether $t$ is fixed, learned, or aggregated.

## Score and Decision

The paper proposes a genuinely novel approach that connects topological data analysis with interpretable GNNs in a well-motivated way. The theoretical framing (bounds, tractable approximation) is coherent, and the experimental results are strong across multiple benchmarks. The primary weakness is the ambiguous description of the experimental backbone, which needs unambiguous clarification. The remaining issues (threshold specification, hyperparameter listing, proof sketch) are addressable presentation concerns. The paper's core contribution is solid.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Weak Accept</orange>