Now I have a thorough understanding of the paper and the calibration landscape. Let me write the final consolidated review.

---

## Summary

This paper presents the first theoretical analysis of the training dynamics of a one-layer Mamba model for in-context learning (ICL) in binary classification tasks with additive outliers. The model is simplified to a linear-attention-plus-gating architecture. The paper proves convergence guarantees (Theorem 1), a generalization bound showing Mamba can tolerate an outlier fraction approaching 1 (Theorem 2), and a comparison to a one-layer linear Transformer that can only tolerate α<1/2 (Theorems 3–4). Corollaries 1–2 mechanistically characterize how the linear attention selects same-pattern examples and how the gating suppresses outliers. Synthetic experiments confirm the theoretical predictions, and a three-layer experiment shows the mechanism persists in deeper models.

## Strengths

- **First theoretical analysis of Mamba training dynamics for ICL.** The paper explicitly claims and supports this with a rigorous analysis framework. Prior ICL theory focused on Transformers; Mamba's nonlinear gating presents analytical challenges that the paper addresses head-on, making this a genuinely novel contribution.

- **Quantitative robustness guarantee with outlier fraction approaching 1.** Theorem 2 proves that Mamba's ICL error remains bounded when the test-time outlier fraction α satisfies α < min(1, p_a·l_tr/l_ts). Since p_a·l_tr/l_ts can be ≥ 1, the guarantee holds up to α ≈ 1. This is validated experimentally in Figure 2, where Mamba maintains error < 10⁻² for α up to 0.8 while the linear Transformer's error rises sharply after α > 0.5.

- **Mechanistic characterization with clear empirical verification.** Corollaries 1 and 2 decompose Mamba's operation into selective attention (same-pattern examples favored) and gating suppression (outliers suppressed; clean examples decay exponentially with index distance). Figures 3 and 4 directly verify these predictions, and Table 1's CQ result (Mamba drops to 82.73% when outliers are closest to the query) is consistent with and explained by Corollary 2's local bias.

- **Theoretical comparison isolating the effect of gating.** By comparing against a linear Transformer with gating removed (Section 3.4), the paper cleanly isolates the effect of the gating mechanism. Remark 6 explicitly cautions that the comparison is restricted to the one-layer, single-head linear setting and that larger Transformers can achieve robustness through other means, preventing overclaiming.

## Weaknesses

### Fatal
None.

### Major
- **The test-time outlier condition (Theorem 2, Condition (a)) is restrictive and limits generality.** The guarantee requires that every test-time outlier be a positive linear combination of the V training outlier patterns, with strictly positive sum of coefficients (Eq. 11). This rules out test-time outliers that are entirely novel directions orthogonal to the training outlier subspace. The paper claims this "captures a wide range of possible outlier patterns" (Remark 3), but a realistic threat model (e.g., the "James Bond" poisoning example in Figure 1 introducing a completely new trigger phrase) would not be a linear combination of previously seen outlier patterns. The paper does not discuss this limitation in the conclusion. Since robustness to *arbitrarily novel* outliers is the practically relevant claim, this condition substantially narrows the scope of the robustness result.

- **No verification that experimental parameters satisfy the theoretical conditions.** Theorem 1 involves several interdependent bounds (on κ_a, l_tr, B, etc.) whose simultaneous satisfiability for a realistic ε (e.g., 0.01) is not obvious. The experiments use fixed parameters (κ_a=2, p_a=0.6, β=3, V=3, l_tr=20) but do not check whether these satisfy the theorem's conditions. While a rough check suggests they likely do (e.g., Vβ⁻⁴≈0.037 ≤ κ_a=2), the paper should explicitly perform and report this verification. As written, there is a gap between the theoretical conditions and the empirical demonstration.

### Minor
- **Occasional imprecision in the "Transformer" vs. "linear Transformer" framing.** The paper consistently uses "linear Transformer" in the abstract and technical sections, but the introduction asks "Under what conditions can Mamba outperform Transformers for ICL?" (Section 1) without the "linear" qualifier, and some section headings use "Transformers" generically. Remark 6 does address this directly, but the abstract and introduction could state the scoping more prominently to avoid misleading casual readers.

- **Remark 4 contains an ambiguous statement about the upper bound on l_tr.** The remark says "Mamba requires an l_tr that shares the same lower bound as that of the linear Transformers, but it does not require an upper bound." However, Theorem 1 condition (iii) *does* impose an upper bound on l_tr (p_a⁻¹ poly(M₁^{κ_a}) ≳ l_tr). The sentence likely means the *linear Transformer* does not require an upper bound (which is true per Theorem 3), but the subject-antecedent relationship is unclear. This should be corrected.

- **The experiments are conducted only on synthetic data.** While this is standard for theoretical ICL analyses and the three-layer experiment is a good extension, the paper would be stronger with a real-data experiment (the Appendix B.2 real-world experiment is mentioned but not described in the main text).

- **The derivation from Mamba's full formulation to Eq. (3) relies on several strong simplifications** (A = -I, a single shared w across hidden dimensions, the one-layer restriction) that are stated but not discussed in terms of their impact on generality. A brief discussion of which aspects of full Mamba are lost would help readers gauge the faithfulness of the simplified model.

### Trivial
- The parsed condition in Eq. (11) appears garbled (missing logical connectors), though this is likely a parsing artifact.
- Figure axes in the text description are described but the actual image is not rendered — this is a parsing issue.
- The paper does not report variance/confidence intervals for the experimental results in Figures 2–4.

## Nice-to-Haves
- A table or worked example showing that the experimental parameters (κ_a=2, p_a=0.6, β=3, V=3) satisfy all conditions of Theorem 1 for a specific ε (e.g., 0.01 or 0.001).
- A discussion of the CQ vulnerability (Table 1, Mamba drops to 82.73% when outliers are closest to the query) in the limitations section, since an adversary could exploit this placement.
- An extension of the analysis (or at least a discussion) for the case where test-time outliers are *orthogonal* to the training outlier subspace, which would be a more challenging test of robustness.

## Removed Points

**"The comparison to Transformers is systematically misleading."** — The abstract and technical content consistently specify "linear Transformer." The introduction uses "Transformers" generically in one question ("Under what conditions can Mamba outperform Transformers for ICL?"), but Remark 6 explicitly clarifies the scoping. The harsh critic's characterization as "systematically misleading" overstates the issue. However, I have retained a Minor weakness about occasional imprecision.

**"The convergence and sample complexity bounds rely on conditions that may be mutually incompatible or extremely restrictive."** — A rough check using the experimental parameters shows the conditions are satisfiable. The genuine concern is that the paper does not *verify* this, which I have kept as a Major weakness. The claim that they "may be mutually incompatible" without concrete evidence is too strong and has been demoted.

**"The evaluation of ICL generalization does not include tasks that differ structurally from training."** — The paper's scope is binary classification tasks, and "new tasks" in the ICL theory literature standardly means new pattern-label combinations within the same task family. This is not a weakness given the stated scope.

**"Statistical significance" complaint about missing confidence intervals.** — For theoretical verification experiments at this scale, single-run evaluations are standard. Not a genuine weakness.

**"Reproducibility" complaint about architecture details.** — Architecture details are in the appendix, which is standard. The hard rules say to remove such nitpicks.

**Strength Finder's generic strengths.** — Several strengths from the Strength Finder (e.g., "this paper addressed an important problem") were dropped as generic or lacking specific evidence.

## Novel Insights

The reviews do not surface an insight that goes substantially beyond the paper's own contributions. The key observation from the cross-review analysis is that the paper's most interesting finding — that Mamba's gating enables robustness to a higher fraction of outliers than a linear Transformer — comes with a significant caveat: the test-time outliers must lie in the linear span of training outliers. This interplay between the type of guarantee (strong robustness) and the restrictiveness of the condition (positive linear combination) is worth highlighting and could inform future work on whether this condition is necessary or can be relaxed.

## Suggestions

1. **Explicitly verify that the experimental parameters satisfy Theorem 1's conditions** with a worked numerical example for a specified ε. This bridges the theory-experiment gap.
2. **Clarify the scoping of the comparison** in the abstract and introduction by leading with "one-layer linear Transformer" rather than introducing "Transformer" generically and then qualifying later. Consider revising the title of Section 3.4 to include "linear."
3. **Discuss the test-time outlier condition as a limitation** in the conclusion, and ideally characterize what happens when test-time outliers are orthogonal to the training subspace (even as a failure case).
4. **Fix the ambiguous sentence in Remark 4** about which model does not require an upper bound on l_tr.
5. **Add the real-data experiment** (currently in Appendix B.2) to the main text, even briefly, to strengthen the claim that the theory explains practical behavior.
6. **Acknowledge the CQ vulnerability** (Table 1, Mamba drops to 82.73%) as a limitation in the conclusion, since it reveals a clear attack surface.

## Score and Decision

**Calibration anchors:**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| /home/wg25r/review_agent/human_reviews/vOfDGYGVyj.md (Sparse Mamba) | 2.50 | 1 | Unrelated application paper; far below |
| /home/wg25r/review_agent/human_reviews/cagNCwQEEN.md (Multimodal Instruction Tuning) | 3.40 | 1 | Unrelated application paper; far below |
| /home/wg25r/review_agent/human_reviews/7ZyFjPUeJp.md (Self-predictive Mamba) | 3.00 | 1 | Unrelated application paper; far below |
| /home/wg25r/review_agent/human_reviews/0yVP49SDg0.md (Mamba-HMIL) | 3.25 | 1 | Unrelated application paper; far below |
| /home/wg25r/review_agent/human_reviews/AL1fq05o7H.md (Original Mamba paper) | 6.25 | 2 | Landmark architecture paper with different contribution type; comparable score band |
| /home/wg25r/review_agent/human_reviews/kxpswbhr1r.md (In-context Convergence of Transformers) | 5.75 | 1,2 | Most directly comparable: studies one-layer Transformer ICL training dynamics. The paper under review is stronger (has experiments, studies harder-to-analyze Mamba architecture) |
| /home/wg25r/review_agent/human_reviews/1TXDtnDIsV.md (Learning Mamba as Continual Learner) | 4.67 | 1 | Mamba application paper with limited novelty; our paper has stronger theory |
| /home/wg25r/review_agent/human_reviews/LgzRo1RpLS.md (MambaExtend) | 6.25 | 1,2 | Practical Mamba improvement paper; different contribution type |
| /home/wg25r/review_agent/human_reviews/6uUmpPvqUU.md (Closeness of ICL and Weight Shifting) | 5.00 | 2 | Lower quality ICL theory paper; our paper is stronger |
| /home/wg25r/review_agent/human_reviews/8fQlGQkj0S.md (In-context Task Retrieval) | 5.20 | 2 | ICL theory paper with similar limitations; comparable quality |
| /home/wg25r/review_agent/human_reviews/HuBFimORiz.md (Global Optimality of ICL) | 4.33 | 2 | Linear attention ICL paper; our paper is stronger |
| /home/wg25r/review_agent/human_reviews/aN4Jf6Cx69.md (Mechanistic basis of ICL) | 9.00 | 1 | Top-tier ICL paper; our paper is below this |
| /home/wg25r/review_agent/human_reviews/ikwEDva1JZ.md (ICL Beyond Simple Functions) | 6.50 | 2 | Strong ICL theory+experiments paper (accepted poster); our paper is slightly less thorough |
| /home/wg25r/review_agent/human_reviews/tPNHOoZFl9.md (Learning Dynamics of LLM Finetuning) | 8.00 | 1 | Top-tier learning dynamics paper; far above |
| /home/wg25r/review_agent/human_reviews/SPS6HzVzyt.md (Context-Parametric Inversion) | 8.00 | 1 | Top-tier; far above |

**Round-1 bracket:** Between ~4 and ~7 (clearly above weak application papers, clearly below top-tier papers like 8+).

**Round-2 narrowing:** The paper is most comparable to "In-context Convergence of Transformers" (5.75) and "ICL Beyond Simple Functions" (6.50). Relative to the former, the paper under review is stronger due to the presence of experiments and the analysis of a less-understood architecture. Relative to the latter, it is slightly weaker in experimental thoroughness. This places it between these two anchors, closer to 6.0.

**Final score: 6.0** — Solid theoretical contribution with clear evidence and reasonable experiments. The restrictive outlier condition and the theory-experiment verification gap prevent a higher score but do not undermine the core contribution.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>