## Summary
This paper proposes Forest-based Graph Learning (FGL), a novel paradigm for semi-supervised node classification that reformulates message passing as transport over spanning trees. The four-component framework consists of: (1) a KNN-based pseudo-label pre-processing step to augment graph connectivity; (2) a homophily-guided tree sampler using a two-stage attention estimator; (3) a general linear-time tree aggregator (Theorem 1) supporting any Combine/Disentangle aggregator; and (4) a mean-based tree fuser. Theorem 2 provides an asymptotic monotonicity result connecting homophily estimator quality to tree distribution quality.

---

## Strengths

- **Novel paradigm with principled motivation (Sec. 4 / Eq. 1):** The observation that spanning trees are the *minimal* structures achieving global coverage—breaking the cost-per-structure × number-of-structures trade-off—is clean and non-obvious. The position paper framing in Eq. 1 is genuinely useful for the community.

- **Theorem 1 — general linear-time tree aggregator:** The Combine/Disentangle property abstraction (Eq. 4) and the two-recursion derivation (Eq. 5–6) provide a principled, aggregator-agnostic mechanism that achieves all-pairs interaction in O(n) time. The claim that linear attention, RNNs, and SSMs all satisfy these properties broadens the framework's applicability.

- **Theorem 2 — monotonicity of homophily-biased tree distribution:** The proof that R\_Ĝ(Δ) is monotonically increasing for Δ ≥ Δ₀ with an asymptotically tight upper bound determined by homophilous connected components is a clean theoretical result directly tied to the method's design. The companion Figure 6 (sampled trees showing 0.9058 vs. 0.8018 homophily on Cora, 0.9026 vs. 0.6768 on Cornell) provides direct empirical confirmation.

- **Efficiency evidence (Table 2):** Running times 2–5× faster than GCNII and DiFFormer, and faster than SGFormer on large graphs (0.079s vs. 0.051s on Flickr is comparable; 0.246s vs. 0.114s on ArXiv is slightly slower), are credible and substantive. The linear complexity is borne out in practice.

- **Table 4 homophily estimator ablation:** The systematic comparison of six estimator variants confirms that better homophily estimation produces better results and directly validates Theorem 2's motivating claim.

---

## Weaknesses

### Fatal
None.

### Major

- **Pre-processing attribution gap — the headline results on heterophilous graphs cannot be attributed to spanning trees without a missing control experiment.** Section 4.1 explicitly states that the KNN pseudo-label augmentation "increases the *homophily ratio*," which directly improves node classification. The ablation Table 3, row (1) (w/o Global Submodule = no tree aggregation at all, only pre-processing + local submodule) already achieves Texas **82.88%**, Wisconsin **83.92%**, Cornell **75.68%**. These numbers already exceed *every* baseline in Table 1 for Texas and Wisconsin (best baselines: SGFormer 78.92%, GraphMamba 80.39%) before any spanning-tree mechanism is applied. The paper never applies this same KNN pre-processing to any strong baseline (e.g., SGFormer, GCNII, DiFFormer) to isolate the incremental contribution of tree-based aggregation. Without that control, the 91.89%/86.27%/83.24% headline results on Texas/Wisconsin/Cornell cannot be attributed to FGL's spanning-tree paradigm rather than the graph rewriting. This is the central empirical gap: the framing claims the spanning-tree mechanism drives the results, but the ablation evidence suggests pre-processing + local attention already does most of the work on the datasets where FGL's gains are most extreme.

- **Split protocol ambiguity for Texas/Wisconsin/Cornell affecting baseline validity.** The paper states results "strictly follow the standard public splits in (Kipf & Welling, 2017)," but these graphs are not part of K&W's original benchmark. The most common published protocol for Texas/Wisconsin/Cornell uses Pei et al.'s Geom-GCN splits. Applying K&W's 20-per-class protocol to Texas (5 classes, 183 nodes) yields ~100 training nodes (~54% of the graph), which is very different from the Geom-GCN 60/20/20% split. The reproduced GCNII baseline on Texas (69.19%) is substantially below published GCNII results on these graphs (typically 77–80%), suggesting the splits used may not match those under which baselines were originally validated. Since the three heterophilous small graphs are precisely where FGL shows the largest gains, this ambiguity is material. The paper should unambiguously state the exact split counts for Texas/Wisconsin/Cornell.

### Minor

- **Theory–implementation gap in Theorem 2.** Theorem 2 assumes oracle edge scores (p for homophilous, q for heterophilous edges), but the implementation uses softmax attention coefficients α (Eq. 3) as a noisy proxy. The paper uses Fig. 5 (a ground-truth oracle sweep over p) to bridge this gap, but Fig. 5 is not an implementation test — it shows that oracle information helps, which is expected. The gap between the theorem's clean binary assumption and the learned continuous attention scores remains informal. A brief discussion of how far α can deviate from the ideal p/q ratio would substantially close this gap.

- **Fig. 5 claim overstated relative to what the figure shows.** The paper states in the Interpretability section: "perfect estimation (accuracy is 1) leading to *perfect classification*." However, Fig. 5's x-axis runs from 0.0 to 0.9, peaks around p = 0.7–0.8, and then *slightly decreases*. The value p = 1.0 is not plotted, and the figure shows no evidence of asymptotically perfect classification. This claim is not supported by the evidence presented.

- **Actor performance anomaly unexplained.** FGL achieves 39.88% on Actor, while Graphormer achieves 62.70% — a 23-point gap. The paper's motivation centers on long-range interaction, yet the method performing worst on Actor among models capable of running on it deserves at minimum a brief discussion. The average rank metric partially obscures this failure mode.

- **Pre-training cost potentially absent from Table 2.** Section 4.5 distinguishes pre-training (for the homophily estimator) from training epochs. Table 2 reports "sec/epoch" and FGL appears fastest, but it is unclear whether pre-training epochs are amortized or excluded. If excluded, the end-to-end efficiency comparison overstates FGL's speed advantage.

### Trivial

- **Wilson's algorithm complexity caveat.** The claim "nearly O(n) time per-tree" for the weighted Wilson algorithm (Section 4.2) should be stated with conditions: O(n) expected time holds for uniform spanning trees; with arbitrary weights, expected running time depends on the mixing time of the weighted random walk, which can be worse. A brief caveat is warranted.

- **Homophily type determination in pre-processing.** Section 4.1 chooses GCN for homophilous and MLP for heterophilous graphs without explaining how this determination is made in practice. The edge homophily ratio from training labels is the natural answer; stating this explicitly would remove ambiguity.

---

## Nice-to-Haves

- Apply the identical KNN pseudo-label pre-processing to SGFormer, GCNII, and DiFFormer as an additional baseline row in Table 3 (or as a separate experiment). This single experiment would resolve the attribution question and either strongly validate the spanning-tree mechanism or guide a reframing of the contribution. This is the highest-leverage addition possible.
- Report standard deviations for Table 1 in the main text rather than the appendix, particularly for the small heterophilous graphs (Texas: 183 nodes, Wisconsin: 251 nodes) where variance across seeds is high.
- Fig. 5 should either extend the p axis to 1.0 or remove the "perfect estimation → perfect classification" claim.

---

## Removed Points
*These points are flagged as removed; treat them with caution.*

- **[Harsh Critic, Removed — strawman]** The criticism that baselines might have been tuned under a different split and FGL benefits from a "more favorable split configuration" is speculative. The paper states all baselines are re-run under the same 10-seed protocol, making the internal comparison valid regardless of what the literature reports for those baselines.

- **[Harsh Critic, Removed — scope creep]** The request for a bound on how far learned α values deviate from true p/q values and how this propagates to tree quality is a reasonable theoretical refinement but exceeds the standard expected for an empirical systems paper. It has been noted as a Minor concern rather than Major.

- **[Harsh Critic, Removed — speculative]** The claim that efficiency comparison excludes pre-training cost is speculative ("if this pre-training cost is excluded"). The paper explicitly describes pre-training and training as separate phases; whether Table 2 includes both is unclear but not confirmed to be misleading.

- **[Strength Finder, Removed — generic]** "Strong empirical performance across diverse datasets" is retained in weakened form given the attribution concern, but the framing as a clean strength is removed since the performance driver is entangled.

- **[Strength Finder, Removed — appendix-dependent]** The generality of the tree aggregator to SSMs and kernel attention is cited from Sec. A.6 of the appendix, which is stripped. The claim is credible given the Combine/Disentangle abstraction shown in Eq. 4, and the strength is retained for the theoretical framework but not for the specific appendix claims.

---

## Novel Insights

The paper's most genuinely novel structural insight is Theorem 1's framing of tree aggregation as a problem that requires only two recursions, computable in O(n), for *any* aggregator satisfying the Combine/Disentangle properties. This is a non-obvious algebraic observation: neighboring nodes in a tree differ in their global message sets by exactly one directed edge, enabling incremental computation via M⁺/M⁻ operators. This positions spanning trees as a general scaffolding layer applicable across a broad family of sequence models and GNN aggregators — a potentially reusable insight beyond the specific FGL instantiation. Theorem 2's characterization of the homophilous connected components as the asymptotic ceiling of achievable tree homophily is also a structurally clean result with implications for understanding the limits of homophily-guided sampling on any graph.

---

## Suggestions

1. **[Critical]** Add one ablation: apply the KNN pseudo-label pre-processing to SGFormer and GCNII, run them on Texas/Wisconsin/Cornell, and compare. This directly tests whether the spanning-tree mechanism contributes beyond graph rewriting.
2. **[Critical]** State the exact train/validation/test split sizes (node counts) for Texas, Wisconsin, and Cornell in the experiments section or Table 7.
3. **[Recommended]** Extend Fig. 5 to p = 1.0 or revise the "perfect classification" claim to match what the figure actually shows.
4. **[Recommended]** Add a brief explanation of why FGL underperforms Graphormer on Actor despite the long-range motivation; this is the one benchmark where the claim is most visibly challenged.
5. **[Minor]** Clarify whether Table 2 timing includes pre-training epochs, or report end-to-end training time separately.

---

## Evaluation on Key Axes

**Originality:** High — the spanning-tree paradigm, the tree aggregator recursions, and the theoretical framing are genuine contributions not previously combined in this form.

**Importance of research question:** High — the efficiency/global-coverage trade-off is a central open problem in graph learning.

**Claims well-supported:** Moderate — theoretical claims (Theorems 1 and 2) are well-supported; empirical claims of state-of-the-art performance have a significant attribution gap due to the pre-processing entanglement.

**Soundness of experiments:** Moderate — comprehensive baselines and ablations are provided, but the single most important ablation (pre-processing control for baselines) is missing, and the split protocol for key datasets is unclear.

**Clarity of writing:** Good — the framework is described clearly; Figure 2 and Figure 3 communicate the method well.

**Value to the research community:** Moderate-to-High — Theorem 1's tree aggregator is a broadly applicable building block; the empirical evidence, once the attribution gap is resolved, would substantially increase this value.

---

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>

<subscores>
<originality>4</originality>
<importance>4</importance>
<claims_supported>2</claims_supported>
<soundness>2</soundness>
<clarity>4</clarity>
<community_value>3</community_value>
</subscores>