Now I have enough calibration to write the final review. Here it is:

---

## Summary

This paper studies Online Inventory Optimization (OIO) in non-stationary environments and proposes algorithms with dynamic regret guarantees. The key technical insight is a two-stage projection strategy that decouples the base learner from the carryover-stock constraint, revealing a connection between OIO and Smoothed OCO (SOCO). Via Lemma 1 the OIO regret is bounded by a SOCO regret with switching cost proportional to $L_{\max}$ (the maximum sell-out period). The paper provides (i) a near-optimal dynamic regret bound $\tilde{\mathcal{O}}(\sqrt{L_{\max}(1+P_T)T})$ using a doubling trick and the SOGD algorithm, (ii) an improved static regret bound $\mathcal{O}(\sqrt{L_{\max}T})$ (a $\sqrt{L_{\max}}$ improvement over prior work), and (iii) a matching static lower bound $\Omega(\sqrt{L_{\max}T})$.

## Strengths

- **Novel reduction from OIO to SOCO.** Lemma 1 and Eq. (8) are a genuinely new connection: the two-stage projection transforms the carryover-stock difficulty into a switching cost paid by the base learner, cleanly eliminating the dynamic feasibility mismatch between $y_t$ and $u_t$. This is the paper's core intellectual contribution and is not present in prior OIO work.

- **First dynamic regret guarantee for OIO.** Theorem 4 provides the first sublinear dynamic regret bound for online inventory optimization, extending beyond the static-regret-only guarantees of all prior work (Table 1). The bound adapts to unknown $L_{\max}$ and $P_T$ without a priori knowledge.

- **Matching static lower bound.** Theorem 5 proves an $\Omega(GD\sqrt{L_{\max}T})$ lower bound, which together with the $\mathcal{O}(\sqrt{L_{\max}T})$ static upper bound resolves (for the linear-capacity case) the open question raised by Hihat et al. (2023) about optimality.

- **Adversarial demand model.** The paper assumes fully adversarial demand and loss functions (Section 3), strictly more general than the i.i.d. or independent assumptions in all prior inventory management works listed in Table 1.

- **Clear, well-structured exposition.** The algorithmic descriptions (Algs. 2–5) are detailed, the cycle-based analysis framework is well motivated, and the paper is transparent about its assumptions (Remark 2, Conclusions).

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Scope restriction to linear capacity constraints limits the comparison with prior work.** The paper assumes a linear-sum capacity constraint $\sum_i y_t^i \leq D$ (Eq. 3), while Hihat et al. (2023) and some other works use general convex constraints. The paper acknowledges this in Remark 2 and the Conclusions, but Table 1's comparison of regret bounds with these works is not apples-to-apples due to different constraint classes. The $\sqrt{L_{\max}}$ improvement in static regret could be partially or entirely driven by the simpler constraint rather than algorithmic innovation. This does not invalidate the paper's results (which are valid for the linear setting) but it tempers the claimed "improvement over existing studies."

2. **The "near-optimal dynamic regret" claim is not fully established.** The paper proves a dynamic upper bound $\tilde{\mathcal{O}}(\sqrt{L_{\max}(1+P_T)T})$ and a *static* lower bound $\Omega(\sqrt{L_{\max}T})$ (Theorem 5), but provides no *dynamic* lower bound involving $P_T$ alongside $L_{\max}$. The $\sqrt{1+P_T}$ factor matches the standard OCO dynamic lower bound (Zhang et al., 2018b), and the $\sqrt{L_{\max}}$ factor is justified by the static lower bound, but the paper never proves a lower bound for the joint rate $\sqrt{L_{\max}(1+P_T)}$ against a dynamic comparator. Calling the bound "near-optimal" is plausible but slightly imprecise without this step.

3. **The $\ell_1$-norm switching cost vs. standard $\ell_2$-norm in SOCO.** Lemma 1 and Eq. (8) produce an $\ell_1$-norm switching cost, whereas the SOCO literature (e.g., Zhang et al., 2022a) typically uses $\ell_2$-norm. The paper acknowledges this (footnote 7) and the algorithms handle it, but the mismatch means the analysis must track the $\ell_1/\ell_2$ conversion throughout (adding $\sqrt{N}$ factors). The paper states this is tracked "in the regret analyses" but does not show the conversion explicitly in the main text.

### Trivial
None.

## Nice-to-Haves

- A discussion of what technical obstacles prevent extending Lemma 1 (and the overall analysis) from linear constraints $\sum_i y_t^i \leq D$ to general convex constraints $\mathcal{C}$ would be valuable. The paper states this is left for future work (Conclusions) but a brief description of where the proof breaks would help readers.
- An explicit comparison of the paper's static regret bound under the linear constraint against a version of MaxCOSD (Hihat et al., 2023) specialized to linear constraints would isolate whether the $\sqrt{L_{\max}}$ improvement comes from the algorithmic design or the constraint relaxation.

## Removed Points

*Criticisms removed per filtering rules:*

1. *"The proof is entirely in the appendix, and without verification, it is unclear whether the overhead terms or detection delays invalidate the claimed bound"* — **Removed.** The paper's appendix is stripped by the parser per ICLR convention. Criticisms that rely on missing appendix content cannot be evaluated.
2. *"The regret bound for SOGD (Theorem 4) introduces a log T factor without a clear derivation from the cited algorithm"* — **Removed.** The derivation is in the appendix.
3. *"The claim that OGD yields overhead O(L_max^{1.5}) inconsistent with Theorem 3's O(L_max log L_max)"* — **Removed.** This assumes a specific proof path (Theorem 2 → Theorem 3) that may not be how Theorem 3 is derived. Without the appendix to verify the actual proof, the claimed mismatch is speculative.
4. *"No experiments of any kind"* — **Removed.** This is a theory paper; experiments are not required. The contribution is theoretical bounds, not empirical validation.
5. *Strengths that are generic or conflict with verified weaknesses* — **Removed.** E.g., "clean definition of problem difficulty" (subjective/superficial), "per-round computational overhead is only O(log T)" (adds little to the core contribution).
6. *Formatter nitpicks and reproducibility complaints about missing hyperparameters or implementation details* — **Removed** per the hard rules.

## Novel Insights

Beyond the paper's own contributions, the meta-review reveals an interesting structural point: the paper establishes a *two-way connection* between OIO and SOCO — not only does it reduce OIO regret to SOCO regret (Lemma 1), but the lower bound results flow in the reverse direction (Corollary 1: a lower bound for OIO implies a lower bound for SOCO). This bidirectional link between two previously separate problem families is a novel observation worth highlighting, though the paper only briefly mentions it. It suggests future work could transport results between the two settings in either direction.

## Suggestions

- **Clarify the optimality claim.** Add a brief statement acknowledging that only a static lower bound is proven, and that the "near-optimal" qualifier refers to the $\sqrt{L_{\max}}$ factor being tight (via Theorem 5) while the $\sqrt{1+P_T}$ factor matches the known OCO lower bound for dynamic regret — a joint dynamic lower bound remains open.
- **Add a brief discussion of the $\ell_1$-vs-$\ell_2$ conversion.** Show the explicit factor introduced when switching norms and confirm it is absorbed into the $\tilde{\mathcal{O}}$ notation or otherwise handled.
- **Explicitly scope the improvement claim.** When stating the $\sqrt{L_{\max}}$ improvement over prior work, add a sentence noting that the comparison involves different capacity constraints and that results are not directly transferable.

## Score and Decision

**Calibration anchors** (all from the deepreview_13k corpus):

| Path | Avg Score | Comparison |
|------|-----------|------------|
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/J7hbPeOZ39.md` | 3.00 | Dynamic pricing paper with standard UCB techniques and strong assumptions. The current paper has greater technical novelty and a cleaner contribution. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/Rdb0HxGJa3.md` | 4.50 | OCO-with-predictions paper with incremental contributions and clarity issues. The current paper is better motivated and has a more well-defined theoretical result. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/WIerHtNyKr.md` | 5.25 | Convex-concave optimization paper with modular algorithm but incremental novelty. The current paper's core reduction (OIO→SOCO) is more novel. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/5sixirvG0I.md` | 5.33 | MARL inventory paper with experiments but no theoretical guarantees. The current paper is stronger in theory but has no experiments. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/qlzxeNESWI.md` | 6.50 | BwAK paper with elegant but somewhat incremental ideas. The current paper has roughly comparable novelty but narrower scope. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/fMTPkDEhLQ.md` | 8.00 | Tight lower bounds with novel construction, universally praised. The current paper does not reach this level of completeness/impact. |

The paper contributes a genuinely novel technical reduction (OIO → SOCO), obtains the first dynamic regret for OIO, and provides a matching static lower bound. The main limitation — linear capacity constraints — is transparently acknowledged. Relative to the anchors, the contribution is cleaner and more novel than the 4–5 range papers but has a narrower scope than the 8-range paper. The appropriate score is **6.0**.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>