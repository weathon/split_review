Now I have all the information I need. Let me synthesize the final review.

---

## Summary

This paper addresses a genuine and underexplored problem in interventional causal discovery: post-treatment selection, where samples are selectively retained after interventions (e.g., QC filtering in gene expression studies). The authors show that existing frameworks conflate dependencies induced by post-treatment selection with true causation, as both produce the same invariance patterns (variant marginal distributions, invariant conditionals). They introduce a new formulation extending augmented DAGs with an explicit selection node, define FI-Markov equivalence and the F-PAG graphical representation (with novel edge types →-, - capturing finer distinctions), and develop the F-FCI algorithm with soundness and completeness guarantees. Experiments on synthetic data show consistent improvements over strong baselines, and a real-world application on the Norman single-cell perturbation dataset recovers biologically validated edges while flagging genes plausibly affected by QC-based selection.

## Strengths

- **Novel problem identification with rigorous formalization.** The paper identifies post-treatment selection as a distinct challenge that lies beyond existing interventional causal discovery frameworks (Section 2.2, Figure 1). The modeling via augmented DAGs with an explicit selection node S and intervention indicators ψ (Definition 1, Eq. 1) is principled and cleanly unifies observational and interventional data under selection.

- **Principled theoretical framework.** The characterization of Markov properties (Theorem 1), the lemmas on when interventions alter marginal vs. conditional distributions (Lemmas 3–4), and the FI-Markov equivalence with graphical criteria (Theorem 2) form a coherent foundation. The F-PAG (Definition 5) with its novel edge types (→-, -) is a genuinely useful representational tool that goes beyond standard PAGs.

- **Soundness and completeness with explicit conditions.** The F-FCI algorithm (Algorithm 1) is accompanied by soundness (Theorem 3) and completeness (Theorem 4) proofs. The proofs explicitly discuss the conditions under which fine-grained distinctions are recoverable — including the dependence on Type I inducing nodes for →- and - edges (Appendix B, lines 1341-1351) — and the paper acknowledges this limitation in Section 6.

- **Strong synthetic results against diverse baselines.** F-FCI consistently outperforms GIES, IGSP, UT-IGSP, JCI-GSP, FCI-interven, and CDIS across graph sizes in DAG Precision and SHD (Figure 6), with gains exceeding 15% in some settings. The method also demonstrates the ability to identify post-treatment selection (Table 1), with accuracy exceeding 70% at larger sample sizes.

## Weaknesses

### Fatal

None.

### Major

None that undermine the paper's core claims. The theoretical framework is sound, the algorithm is well-motivated, and the synthetic results convincingly demonstrate the method's advantages.

### Minor

- **Missing ablation of Step 2.3 (disambiguation via Type I nodes).** The synthetic experiments show that F-FCI outperforms baselines, but they do not isolate how much of the gain comes from the basic interventional orientation rules (Step 2.2) versus the fine-grained disambiguation enabled by Type I inducing nodes (Step 2.3). An ablation comparing full F-FCI against a variant omitting Step 2.3 would clarify whether the claimed ability to distinguish direct causation from selection-induced dependencies is empirically borne out or whether the gains primarily reflect standard interventional orientation. This is the most substantive empirical gap.

- **Norman dataset evaluation is suggestive rather than definitive for selection detection.** The paper flags genes (ZNF318, CDKN1C, CDKN1A, RREB1) as affected by post-treatment selection and provides plausible biological reasoning linking them to QC filtering. However, there is no independent ground truth or holdout validation that confirms these genes are genuinely selected against in the data-generating process. The causal edges validated via Enrichr test whether the method recovers known regulatory relationships, not whether it correctly disentangles causation from selection. This is an exploratory result and the paper appropriately frames it as such, but the strength of the empirical claim about selection identification is limited.

- **Theorem statements could be more precise about conditions.** Theorem 4 states that each substructure type "can be identified by different types of CI patterns" without explicitly conditioning on the availability of interventions on Type I inducing nodes. The proof does address this condition (lines 1341-1351 discuss when →- and - are/aren't identifiable), but the theorem statement itself would benefit from making this dependency explicit. This is a presentation issue — the underlying results are correct — but contributes to readers potentially overestimating the method's scope.

### Trivial

- The termination condition in Algorithm 1 Step 2.1 ("If no more paths can be blocked then break") is stated informally. While the logic is clear to practitioners, a more algorithmic specification would improve reproducibility.
- The condition sets in Step 2.1 are enumerated from "AllPaths" without discussion of computational limits on path enumeration in dense graphs.

## Nice-to-Haves

- An evaluation under constrained interventions where Type I inducing nodes are intentionally excluded from the intervention set, to calibrate how far the output F-PAG falls back toward standard equivalence classes in such regimes.
- A visual case study (e.g., a small synthetic graph) showing a specific false positive that a baseline like FCI-interven makes due to post-treatment selection, which F-FCI correctly avoids through its disambiguation step.
- The paper mentions Type II inducing nodes as a limitation; outlining potential strategies (parametric assumptions, auxiliary constraints) for handling these cases would strengthen the forward-looking discussion.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"The soundness/completeness theorems do not explicitly condition on the requirement of interventional data on Type I nodes"** — This is not accurate. The proof of Theorem 3 (lines 1341-1351) explicitly discusses cases where Type I inducing nodes are present vs. absent (Type II), and the Limitations section (lines 716-718) states: "The identification of direct causal links and selection structures depends critically on the presence of Type I inducing nodes." The paper is transparent about this condition. The theorems are about what CI patterns identify what structures given available data; they do not claim universal identifiability without Type I nodes.

- **"The completeness theorem is stated unconditionally"** — Overstated. Theorem 4 is a claim about mapping CI patterns to substructure types. It does not guarantee that every graph yields all patterns — it says each pattern type that exists can be identified. The conditionality is in the proof and limitations, and Theorem 4 is correct as stated.

- **"The proof sketches are too high-level / not rigorous"** — The proofs in Appendix B provide step-by-step reasoning for each mark type (tail, arrowhead, square, →-, -) with explicit handling of edge cases (e.g., Y-structures in Figure 8, Type I vs Type II nodes in Figure 9). While not formalized to theorem-prover standards, they are substantive and match the norms of the causal discovery literature.

- **"The gains might be attributable primarily to the interventional orientation rules that do not require the disambiguation step"** — This is speculative rather than demonstrated. It is a valid hypothesis motivating an ablation (which is why the missing ablation is listed as a Minor weakness), but it is not a confirmed problem with the paper. The paper does show that F-FCI recovers selection structures (Table 1), and the ablation question is about attribution, not correctness.

- **Harsh critic's formatting/notation nitpicks** — The parser artifacts (broken characters, garbled symbols) in the PDF extraction are not author errors. The original submission does not have these issues.

- **Criticism that the Norman dataset biological interpretation is "post-hoc and anecdotal"** — The paper acknowledges the exploratory nature of this analysis and uses prior knowledge (Enrichr, ChEA, GEO, ARCHS4) to validate identified causal edges. For a real-world biological dataset where ground truth is unavailable, this is standard practice.

## Novel Insights

The most novel insight emerging from this work is the systematic characterization of how post-treatment selection creates a structural symmetry with causation in interventional invariance patterns, and how this symmetry can be broken by exploiting hard interventions on intermediate Type I inducing nodes that block selection effects on latent confounders. This reveals that the information needed to distinguish causation from selection is not in the endpoint CI patterns (which are identical) but in the CI patterns involving intermediate nodes along inducing paths — a genuinely non-obvious insight that motivates the algorithm design and explains why prior frameworks cannot make this distinction.

## Suggestions

- Add the Step 2.3 ablation experiment. This is the single most impactful improvement: show what F-FCI without disambiguation achieves vs. full F-FCI, to quantify how much the fine-grained equivalence matters in practice.
- In the abstract and introduction, add a brief qualifier about the dependence on Type I inducing nodes for the finest distinctions (e.g., "when interventional data on suitable intermediate variables is available"). The limitation is already discussed in Section 6, but front-loading it prevents overclaiming.
- For the Norman evaluation, consider a quantitative validation strategy: e.g., use known TF-target pairs from independent databases as a partial ground truth for directed edges, and report precision/recall specifically on those pairs.
- Tighten the Theorem 4 statement to make explicit that identification of →- and - edge types depends on the presence of Type I inducing nodes with available interventional data, consistent with what the proof already acknowledges.

## Score and Decision

### Anchor comparison

| Anchor | Avg Score | Decision | Comparison |
|--------|-----------|----------|------------|
| `/home/wg25r/review_agent/human_reviews_2026/ta8BKRa1bl.md` | 6.00 | Accept | Strong theory (identifiability from two environments), but limited to bivariate synthetic experiments. Our paper has comparable theory plus broader experiments. Our experiments are stronger; theory is comparably rigorous in parts but less formally polished in places. |
| `/home/wg25r/review_agent/human_reviews_2026/BNHplerBYE.md` | 5.33 | Accept | First score-based method for partially observed models. Similar contribution level (novel algorithm with identifiability). Our paper is comparable — novel problem formulation, sound algorithm, solid synthetic results. |
| `/home/wg25r/review_agent/human_reviews_2026/s0nYSwlV3I.md` | 5.00 | Accept | Causal discovery from temporal data with theoretical guarantees. Similar structure: theory + algorithm + synthetic + one real-world dataset. Our paper has stronger theory (soundness + completeness). |
| `/home/wg25r/review_agent/human_reviews_2026/V7pT2ZRoTB.md` | 4.50 | Accept | Theoretical guarantees on random graphs but narrow empirical scope. Our paper is stronger empirically. |
| `/home/wg25r/review_agent/human_reviews_2026/lYearSsgXj.md` | 4.50 | Reject | Coupled confounding and collider biases with strong assumptions. Our paper has explicit limitations discussion and broader experiments. |
| `/home/wg25r/review_agent/human_reviews_2026/HfiRzzmFt8.md` | 4.00 | Reject | Bayesian causal discovery with unclear contributions and presentation issues. Our paper is much clearer and better motivated. |
| `/home/wg25r/review_agent/human_reviews_2026/Twpdb61nE0.md` | 3.33 | Reject | Differentiable causal order regularizer, incremental contribution. Our paper has substantially more novelty and depth. |
| `/home/wg25r/review_agent/human_reviews_2026/YvMkU4BYOA.md` | 2.00 | Reject | Heuristic BIC modification with weak theory. Our paper is far stronger theoretically and empirically. |

**Calibration judgment:** The paper sits in the 5.0–6.0 range. It is clearly stronger than the 4.0–4.5 rejected papers (better theory, clearer contributions, better experiments) and comparable to accepted papers at 5.0–6.0. It does not reach 6.0+ because of the missing ablation (minor but substantive) and the somewhat preliminary real-world validation. The theoretical framework is solid, the problem is important, and the synthetic results are convincing. **Score: 5.5.**

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>