Now I have sufficient information to write the meta-review. Let me assess the rebuttal against the paper.

## Summary

SparseFW frames layerwise LLM pruning as a convex relaxation of the combinatorial mask-selection problem and solves it via the Frank-Wolfe algorithm. The paper demonstrates that Wanda, RIA, and SparseGPT are greedy approximations to the same underlying MASK SELECTION objective, then proposes solving the relaxed version via FW. Empirically evaluated on five modern GPT architectures at 50%, 60%, and 2:4 sparsity, showing consistent gains over Wanda and RIA, especially at higher sparsity levels.

---

## Rebuttal Assessment

---

**Weakness:** Vanilla SparseFW (α=0.0) fails; paper frames FW as replacing greedy heuristics
**Author's response:** Partially address
**Assessment:** Partially convincing — The paper is genuinely transparent: Section 2.3 (line 157) explicitly states "setting α = 0.0 (full FW without any fixed weights) consistently yields worse results than the baselines," and the Limitations (lines 278–283) explicitly acknowledge the local-global mismatch and that "inductive biases still appear necessary." The original review already credited this disclosure—the weakness was about the gap between the narrative and the mechanism, not hidden information. The authors' pushback that FW still accounts for weight interactions over 10% of entries (via Gram matrix $G = XX^\top$) is technically valid, and the α-ablation (Table 2, appendix) does confirm even small α values bring gains. However, the deployed method still has 90% of its mask decided by Wanda, so the characterization of FW as "accounts for weight interactions unlike greedy heuristics" in the abstract/introduction remains overstated for the actual deployed configuration. The promise to revise framing does not help the paper as submitted.
**Score impact:** Weakness unchanged (review already calibrated to the disclosure)

---

**Weakness:** Theory (Lemma 1) does not cover the deployed α-constrained method
**Author's response:** Acknowledge
**Assessment:** Unconvincing — Authors correctly note that the constrained feasible set is a face of the original polytope and that FW convergence arguments transfer qualitatively. However, they only promise "we will add this as a corollary in the revision." This is a future commitment, not evidence in the paper. The gap remains: Lemma 1 bounds vanilla SparseFW over the full $\mathcal{C}_k$, while Table 1 evaluates the α=0.9 variant over a strictly smaller polytope. Formal closure of this gap does not exist in the submission.
**Score impact:** Weakness unchanged

---

**Weakness:** SparseGPT excluded; "state-of-the-art" claims are ambiguous
**Author's response:** Partially address
**Assessment:** Partially convincing — The principled exclusion rationale is sound and explicitly stated in Section 3 (line 192): SparseGPT solves a joint mask selection + weight reconstruction objective (Equation 2), while SparseFW/Wanda/RIA address pure mask selection. This distinction is clear in the paper. However, the conclusion (line 276) still reads "improves perplexity and zero-shot accuracy over state-of-the-art LLM pruning approaches"—verified in the paper—which omits SparseGPT from the scope in a non-obvious way. The authors promise to add a comparison row and revise language, but neither exists in the current submission.
**Score impact:** Weakness partially downgraded (the methodological exclusion rationale is principled and already present; the language issue is real but addressable)

---

**Weakness:** At 50% sparsity, improvements inconsistent and sometimes negative
**Author's response:** Partially address
**Assessment:** Partially convincing — Authors correctly note that the paper already acknowledges this pattern: "We generally observe much more consistent and bigger improvements in the higher sparsity regimes than for 50% sparsity" (line 194, verified). The zero-shot accuracy at 50% is indeed more uniformly positive (verified from Table 1: SparseFW typically gains 0.5–2% accuracy even at 50% sparsity), providing nuance. However, specific perplexity regressions at 50% (7.89 vs. 7.79 on DeepSeek, 10.21 vs. 9.88 on LLaMA-3.1-8B, verified in Table 1) remain. "Generally on par or better" is still slightly misleading for perplexity at 50%.
**Score impact:** Weakness slightly downgraded (zero-shot point is valid and adds context, paper does already acknowledge the pattern)

---

**Weakness:** Standard deviations omitted from Table 1
**Author's response:** Acknowledge
**Assessment:** Unconvincing as rebuttal — Authors acknowledge the limitation explicitly (Table 1 caption, line 208: "We omit standard deviations for legibility," verified). Promise to include in revision does not help the submission. Several 50% sparsity differences (e.g., 7.79 vs. 7.89) remain statistically unassessable.
**Score impact:** Weakness unchanged

---

**Weakness:** "80% reduction in per-layer pruning error" is relative to Wanda warmstart, potentially misleading
**Author's response:** Refute
**Assessment:** Convincing — The authors' refutation is largely correct. Figure 2 caption (line 190) describes the comparison as "compared to the warmstart mask," and the warmstart is the mask that Wanda-as-standalone-pruner would produce—there is no "Wanda-as-initialization" that differs from "Wanda-as-pruner." The comparison in Figure 2 is therefore equivalent to comparing against Wanda as a deployed method. The authors also correctly identify a minor inconsistency: the abstract says "up to 80%" while the contributions section says "up to 70%" (both verified). This discrepancy is trivial but real.
**Score impact:** Weakness removed (the Minor concern was not well-founded); replaced by Trivial note about the 80%/70% inconsistency

---

**Weakness:** Figure 3 reports min-max rather than standard deviations
**Author's response:** Acknowledge
**Assessment:** N/A (Trivial; acknowledged, will be revised)
**Score impact:** Weakness unchanged (Trivial)

---

## Strengths

- **Unification of Wanda, RIA, and SparseGPT under a common objective.** Equations (4)–(5) derive Wanda's saliency score as the solution to single-weight pruning without reconstruction; RIA is shown to be Wanda on a rescaled matrix. This is clean and analytically valuable.
- **Consistent empirical improvements at ≥60% and 2:4 sparsity.** Table 1 confirms: SparseFW (Wanda) achieves 17.97 vs. 21.53 (Wanda) on LLaMA-3.1-8B at 60%; 14.83 vs. 16.46 (Wanda) on Gemma-2-9B at 60%. Zero-shot accuracy improvements are consistent across all sparsity regimes.
- **Memory-efficient gradient computation.** Precomputing $G = XX^\top$ (dimensions $d_{in} \times d_{in}$, independent of $N$ and $L$) is correctly described and makes the method scalable (Section 2.3, lines 152–155, verified).
- **Formal approximation guarantee (Lemma 1).** Decomposes error into an optimization term (vanishes as $T \to \infty$) and a thresholding term (controlled by $\lambda_{\max}(Q)$ and polytope geometry). No such guarantee exists for Wanda or RIA.
- **Honest disclosure of limitations.** The paper does not hide the α = 0.0 failure or the local-global mismatch—both are disclosed in Section 2.3 and the Limitations section (lines 278–283, verified). This is commendable even if the abstract/introduction framing does not match.

---

## Weaknesses

### Fatal
None.

### Major

- **Vanilla SparseFW (α = 0.0) is worse than baselines; deployed method is a Wanda-initialized local refinement.** The paper is transparent about this (Section 2.3, line 157; Limitations, lines 278–283, verified), but the abstract and introduction still characterize FW as replacing greedy heuristics by accounting for weight interactions globally. The deployed method fixes 90% of the mask via Wanda's criterion and applies FW only over 10% of remaining entries. The interaction-accounting advantage applies to a small residual search space, not the full pruning decision. The rebuttal's claim that this is meaningfully different from "Wanda-initialized local refinement" is technically defensible but not fully persuasive given the 90/10 split.

- **Theoretical analysis (Lemma 1) does not cover the deployed α-constrained method.** Lemma 1 bounds vanilla SparseFW over the full feasible set $\mathcal{C}_k$. The deployed method operates over $\mathcal{C}_k^{(\alpha)} \subsetneq \mathcal{C}_k$ (a face of the polytope). The authors acknowledge this gap but only promise a corollary in revision. The current paper's theoretical and empirical sections are not coherent in this regard.

### Minor

- **SparseGPT excluded; overreaching "state-of-the-art" language in conclusion.** Conclusion (line 276) claims "improves perplexity and zero-shot accuracy over state-of-the-art LLM pruning approaches" without qualification. Section 3 (line 192) correctly limits scope to mask-selection methods, but the conclusion language is inconsistent with this scope. The methodological exclusion rationale is principled, but one comparison row would have been trivial to include.

- **Perplexity improvements at 50% sparsity are inconsistent and sometimes negative.** Table 1 shows SparseFW (Wanda) at 10.21 vs. RIA's 9.88 on LLaMA-3.1-8B and 7.89 vs. Wanda's 7.79 on DeepSeek-7B. Zero-shot accuracy is more reliable at 50%, but the perplexity metric—the primary evaluation—shows regressions. The paper acknowledges this ("more consistent and bigger improvements in the higher sparsity regimes") but the summary language is still imprecise.

- **Standard deviations absent from Table 1.** Several 50% sparsity differences are within 0.1–0.2 perplexity points. Statistical significance cannot be assessed.

### Trivial

- Abstract claims "up to 80%" error reduction; contributions section claims "up to 70%." Both verified in paper (lines 39, 44). Minor internal inconsistency.
- Figure 3 reports min-max shaded regions rather than standard deviations; less informative about typical variance.

---

## Nice-to-Haves

- Add Lemma 1 corollary for the α-constrained polytope $\mathcal{C}_k^{(\alpha)}$; this is reportedly straightforward given it is a face of $\mathcal{C}_k$.
- Include a single SparseGPT comparison row with explicit note that it solves a different objective.
- Investigate why vanilla FW (α=0.0) fails: calibration distribution mismatch, overoptimization to local objective, or activation outliers circumventing global coherence? This is the most scientifically interesting finding and deserves more than two sentences.
- Report standard deviations in Table 1 for at least one model.

---

## Novel Insights

The most novel insight in this paper is the *diagnostic value of the α = 0.0 failure*: a convex relaxation that correctly and substantially minimizes the local per-layer reconstruction objective (up to 80% error reduction per Figure 4) can nonetheless produce *worse downstream perplexity* than the simple Wanda heuristic. This is a substantive empirical finding about the alignment between layerwise reconstruction objectives and global language model performance—the calibration objective may be inadequately predictive of global quality at high sparsity. The paper discloses this finding honestly but explores it minimally. Systematically understanding this mismatch would illuminate failure modes of the entire layerwise pruning paradigm, including SparseGPT, and represents a scientifically important direction that the paper identifies but does not pursue.

---

## Suggestions

1. Revise abstract and introduction to describe SparseFW as running FW over the residual search space after fixing Wanda-identified high-saliency weights, rather than implying full replacement of greedy heuristics.
2. Add Lemma 1 corollary for the constrained feasible set $\mathcal{C}_k^{(\alpha)}$ to make theory coherent with the evaluated method.
3. Revise conclusion language from "state-of-the-art LLM pruning approaches" to "state-of-the-art mask-selection methods without weight reconstruction."
4. Add a dedicated ablation or discussion investigating *why* α = 0.0 fails globally despite strong local objective reduction.

---

## Score and Decision

The rebuttal is honest and well-organized. It successfully refutes the 80%-relative-to-warmstart concern (that comparison was to Wanda-as-pruner, not a separate initialization variant). It correctly notes that the paper already discloses the α = 0.0 failure and local-global mismatch, points the review already credited. However, it cannot close the major gaps: the theory-deployed method mismatch (only promised for revision), the SparseGPT exclusion with overreaching conclusion language (also promised for revision), and the fundamental α = 0.0 issue (acknowledged but not resolved). Promises of revision do not strengthen the submitted paper.

The rebuttal scores a minor improvement on one concern (80% claim is less misleading than the review implied) and further clarifies that the paper was already more transparent than the original review may have appreciated. These are modest gains. The two major weaknesses (Lemma 1 gap, overreaching claims) remain squarely in place.

Original score: 5.5 / Reject. The rebuttal justifies a slight upward adjustment, as it removes one minor weakness (the 80% claim) and demonstrates the paper's transparency was better than initially credited. However, the major structural issues (theory gap, overreaching framing) remain unchanged. The score moves marginally.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>