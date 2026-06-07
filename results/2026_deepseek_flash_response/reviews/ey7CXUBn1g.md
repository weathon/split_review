## Summary

This paper proposes AdaSVD, an SVD-based LLM compression method with two components: (1) **adaComp**, which uses a Moore-Penrose pseudoinverse-based alternating update to compensate for truncation error, and (2) **adaCR**, which assigns per-layer compression ratios based on input-output cosine similarity. Experiments on LLaMA2-7B, OPT-6.7B, Vicuna-7B, and Mistral-7B show perplexity gains over SVD-LLM and other baselines at 40–60% compression ratios, and the method is shown to be orthogonal to quantization (GPTQ-INT4).

## Strengths

- **Consistent perplexity improvements over SVD-LLM across all reported ratios on LLaMA2-7B.** The gains widen at higher compression (e.g., WikiText-2 PPL 50.33 vs. 89.90 at 60%), and the trend holds across PTB and C4 as well. This is the paper's central empirical claim and it is well-supported.

- **Clean ablation isolating each proposed component.** Table 3a/3b show that removing adaComp raises PPL from 50.33 to 78.82 at 60% (WikiText-2), and removing adaCR raises it from 50.33 to 69.46, giving clear causal evidence that both components contribute independently.

- **Orthogonality to quantization demonstrated.** Table 4 shows AdaSVD+GPTQ-INT4 outperforms SVD-LLM+GPTQ-INT4 at every compression ratio from 40% to 80% (e.g., 22.55 vs. 33.56 at 40% on WikiText-2), validating the claim of composability.

- **Evaluation across multiple model families.** Results span OPT-6.7B, LLaMA2-7B, Vicuna-7B, and Mistral-7B (four architectures from three families), supporting generalizability claims beyond a single model.

- **Mathematically grounded update mechanism.** Reformulating the update as a least-squares problem solved via SVD-based pseudoinverse (Eq. 8–13) is principled, and Figure 3(a) empirically demonstrates it avoids the instability of the naive gradient-based update.

## Weaknesses

### Major

1. **Iteration ablation (Table 3c) contradicts the paper's own textual claim.** The data consistently shows that 1 iteration outperforms 3 and 15 iterations at *every* reported compression ratio (40%, 50%, 60%) on both WikiText-2 and C4. For example, at 60% on WikiText-2: 1 iter = 50.33, 3 iter = 64.12, 15 iter = 62.34. Yet Section 4.3 states: *"In contrast, under higher compression ratios, additional iterations lead to performance improvements"* — this is factually wrong for the 60% data presented. The paper's framing of alternating updates "until convergence" (Eq. 16, line 210) is misleading when the optimal number of iterations is 1. This is a correctable error (the method still works with 1 iteration), but it directly undermines a core narrative claim and requires substantial revision of Section 4.3's discussion.

2. **The mapping from (mrr, trr) hyperparameters to a desired global compression ratio is underspecified.** Equation (19) defines per-layer ratios as `CR(W) = mrr + I_n(W)·(trr − mrr)`. While the mathematics imply the average CR equals `trr` (because `I_n(W)` has mean 1 by construction), the paper never states this explicitly or explains how `mrr` and `trr` are chosen to hit a specific target (40%, 50%, 60%). Table 3d explores `mrr` empirically, but a reproducible procedure for calibrating these hyperparameters to a desired overall compression target is missing. This impedes reproduction.

### Minor

3. **No variance or confidence intervals reported** despite using only 256 calibration samples, where results may be sensitive to random sample selection. Given the small calibration set, multi-seed runs would substantially strengthen the evidence.

4. **adaCR can degrade performance without adaComp on some datasets.** At 40% C4, AdaSVD without adaComp (i.e., adaCR only) achieves PPL 66.29 versus the SVD-LLM baseline of 61.95 — *worse* than the baseline. This means the adaptive ratio allocation can hurt on its own on certain datasets, and the positive result relies on adaComp compensating. The paper does not discuss this asymmetry.

5. **Claims of prior work "largely overlooking" weight compensation are overstated.** SVD-LLM and ASVD both address compression error through different mechanisms (data whitening, input-channel scaling). The novelty lies in the specific compensation procedure, not in the observation itself.

### Trivial

None.

## Nice-to-Haves

- Report 70% and 80% compression results (currently in supplementary) in the main text for completeness.
- Include the Table 2 results (different LLMs) summary in the main text rather than deferring entirely to supplementary.
- Add a brief description of SVD-LLM's whitening step for readers unfamiliar with it (currently referenced only as `WHITENING` in Algorithm 1 without explanation).

## Removed Points

These points from the input reviews were removed with justification:

- **"Figure 1 log scale makes differences invisible"** — The log-scale presentation is standard for wide perplexity ranges. The tabulated values confirm the claimed ranking; the visual is secondary.
- **"Performance gap to original model remains large"** — The paper's stated goal is improving over baselines, not matching the uncompressed model. All SVD compression papers at these ratios show substantial degradation; this is a field-level constraint, not a paper-specific weakness.
- **"WHITENING function not explained"** — Standard practice to reference prior work (SVD-LLM). Reproduction is not impeded when readers consult the cited paper.
- **"Stack-of-batch reduces data diversity"** — The paper demonstrates it *helps* empirically (Figure 3b). A trade-off exists but it is not a weakness unless the trade-off is hidden.
- **"Two components not independent"** — This is a speculation about interaction patterns. The ablations treat each component as a binary toggle, which is standard practice. The overall method improves regardless.
- **Generic strengths** about "the problem is important" or "the paper is well-written" were removed as lacking specific evidence.
- **Missing related works** — Removed per instructions (cannot verify existence of missing references).
- **"Critical Issue #3: adaCR mechanism is not specified" / "reproducibility concerns"** — The mechanism *is* specified (Eq. 17–20). The mapping from (mrr, trr) to target ratio is partially implicit but derivable; this has been retained as Major Weakness #2 in a corrected form rather than the original "not specified" framing.

## Novel Insights

None beyond the paper's own contributions.

## Calibration

**Bracket (Round 1):** Between weak-band anchors (score < 3.5, mostly unrelated topics) and strong-band anchors (score > 7.5, unrelated topics). The plausible range was 4.0–6.5 based on topically similar middle-band anchors.

**Narrowing (Round 2):** Compared against:
- ASVD (avg 6.25, Reject, scores 5/6/8/6) — topically very similar. AdaSVD has comparable evaluation breadth but worse internal consistency (Table 3c contradiction). AdaSVD is slightly weaker.
- Basis Sharing (avg 6.50, Accept, scores 8/5/8/5) — stronger method with clearer novelty. AdaSVD is clearly weaker.
- MoE-SVD (avg 5.00, Reject, scores 3/6/6) — narrower scope. AdaSVD is stronger.
- Low-Rank Correction (avg 5.00, Reject, scores 6/6/5/5/3) — comparable tier.
- OATS (avg 6.25, Accept, scores 8/3/8/6) — stronger method and accepted. AdaSVD is clearly weaker.
- AutoTrunc (avg 4.00, Reject, scores 3/3/6) — AdaSVD is clearly stronger.

**Final position:** AdaSVD sits between the weaker anchors (MoE-SVD at 5.0, Low-Rank Correction at 5.0) and the stronger SVD compression anchors (ASVD at 6.25). The Table 3c contradiction lowers it from where it could otherwise sit (~5.5–6.0). Final score: **5.0**.

## Suggestions

1. **Revise Section 4.3's iteration-number discussion to honestly reflect the data.** If 1 iteration is optimal at all ratios tested, state this clearly and either (a) reframe adaComp as a one-shot pseudoinverse correction (dropping the "alternating until convergence" language), or (b) add experiments showing where additional iterations *do* help (e.g., with more calibration data or regularization).
2. **Explicitly state** that `trr` equals the target global compression ratio because `I_n(W)` has mean 1, and describe how `mrr` is chosen empirically (or provide a heuristic).
3. **Add multi-seed variance** to the main results (at least 3 seeds with the 256-sample calibration set).
4. **Discuss the adaCR-alone degradation** on C4 at 40% (Table 3a, row 2) to clarify that adaCR's benefits depend on adaComp's compensation on certain datasets.

## Score and Decision

<score>5.0</score>
<decision>Reject</decision>