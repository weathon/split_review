Now I'll synthesize the final review.

## Summary

The paper proposes CorreGen, a generative framework for robust multi-view clustering (MVC) under noisy correspondence (NC). It identifies two distinct types of NC — category-level mismatch (same-class samples incorrectly treated as negatives) and sample-level mismatch (misaligned or unalignable cross-view pairs) — and addresses both via a maximum likelihood formulation solved with an EM algorithm. In the E-step, soft cross-view correspondences are inferred through optimal transport with GMM-guided marginals and a virtual sample mechanism to handle noise; in the M-step, the embedding network is updated to maximize the expected log-likelihood. The paper also proves that InfoNCE is a special case of this formulation under uniform marginal and degenerate posterior assumptions. Experiments on four datasets under varying mismatch and corruption ratios show consistent improvements over seven baselines, with particularly large gains on the naturally noisy UMPC-Food101 dataset.

## Strengths

- **Precise formalization of two types of noisy correspondence.** Definitions 1 and 2 (category-level vs. sample-level mismatch) are clearly stated and go beyond the generic "noisy correspondence" used in prior work. This distinction directly motivates the method's design (GMM marginals for category structure, virtual sample for unalignable samples) and is a substantive conceptual contribution.

- **Principled generative formulation with EM solution.** Casting NC in MVC as maximum likelihood estimation over latent cross-view correspondences (Eq. 2–4) and solving via EM is a clean departure from existing discriminative approaches. The derivation from the ELBO through the E-step (OT with GMM-guided marginals and virtual sample) and M-step (weighted log-likelihood maximization) is well-structured.

- **InfoNCE as a special case (Proposition 2).** Proving that standard InfoNCE emerges under uniform marginals and degenerate posterior is a non-trivial theoretical insight that unifies the proposed generative framework with widely-used contrastive objectives.

- **Strong and consistent empirical results.** Tables 1 and 2 show CorreGen outperforming all seven baselines on all four datasets across mismatch ratios from 0% to 80% and corruption ratios up to 50%. The gains are substantial and consistent — e.g., on UMPC-Food101 at 0% MR, CorreGen achieves 49.77% ACC vs. DIVIDE's 36.20% (+13.6 absolute), and this advantage persists under heavy noise (80% MR: 43.00% vs. CANDY's 27.59%). The consistency across three metrics (ACC, NMI, ARI) is reassuring.

- **Qualitative validation of correspondence recovery.** Figure 3 shows posterior heatmaps evolving from a sparse diagonal to a block-diagonal structure matching the ground-truth category-level correspondences, providing direct evidence that the E-step is learning meaningful latent alignments.

## Weaknesses

### Major
None.

### Minor

- **Baseline comparison setup at 0% noise is not fully specified.** The paper states that CorreGen is implemented "on top of DIVIDE as the base model" and that a view realignment strategy is applied uniformly with batch size 512, but does not clarify whether the baseline numbers (particularly DIVIDE) were produced under *identical* training conditions (same optimizer, learning rate, backbone architecture, training schedule, etc.). The 13.6% absolute gain over DIVIDE on UMPC-Food101 at 0% additional noise is impressive, but some readers may wonder how much of this gap is attributable to the generative formulation versus unstated differences in training configuration. The relative robustness trends under controlled noise strongly support the core claim, but the authors should explicitly confirm that all baselines were retrained under matched settings or discuss any discrepancies.

- **No standard deviations or error bars reported for main results.** Tables 1 and 2 report only the mean of five runs. Without variance information, it is difficult to assess whether the reported improvements are stable or driven by outlier runs, especially in settings where gaps between CorreGen and the second-best method are small (e.g., Caltech101 at 20% MR: 68.01 vs. CANDY's 65.79).

- **Noise injection protocol (MR and CR) is described only in the appendix.** For a paper whose primary empirical contribution is robustness under controlled noise, the main text should include at least a paragraph defining how mismatch and corruption ratios are constructed, rather than deferring entirely to Appendix C.

- **Real-world noise evaluation is limited to a single dataset.** Only UMPC-Food101 carries inherent real-world noise. While the synthetic experiments are carefully designed and cover four datasets, the claim of "extensive experiments on both synthetic and real-world noisy datasets" would be stronger with at least one more naturally noisy dataset.

- **The noise ratio hyperparameter ρ requires a priori knowledge.** The virtual sample mechanism uses ρ = 0.2 in experiments (the expected noise proportion), but real-world noise ratios are unknown and vary across datasets. A practical guide for setting ρ without ground truth — or evidence that performance is relatively insensitive to misspecified ρ — would strengthen the method's real-world applicability.

### Trivial
None.

## Nice-to-Haves

- An ablation that isolates the GMM-guided marginal component from the OT solver (comparing CorreGen to a version with uniform marginals) to quantify the contribution of the GMM guidance.
- A demonstration that the generative formulation can be plugged into a different base model (e.g., CANDY) to improve its robustness, showing generality beyond DIVIDE.

## Removed Points

These points were raised in the reviews but are removed from the main assessment:

- **"Comparison at 0% noise reveals a potential confound"** — kept but downgraded to Minor. The critic acknowledges this is "not fatal" and the relative degradation curves support the robustness claim. It remains as a clarity concern.
- **"Transition from Eq. (2) to Eq. (3) is glossed over"** — this is a minor exposition detail; the paper provides the conceptual motivation and the EM derivation that follows is sound. Removed as it does not harm the core claim.
- **"Proposition 2's assumptions are strong enough that the reduction is unsurprising"** — the value of this proposition is in formally unifying generative and contrastive objectives, not in surprise. Removed.
- **Strength Finder's claim about "category-level mismatch and sample-level mismatch"** — kept, but incorporated into the first strength.
- **Suggestion to "directly compare CorreGen to a version with uniform marginals"** — moved to Nice-to-Haves.
- **Suggestion to "show that the method works without relying on DIVIDE"** — moved to Nice-to-Haves.

## Novel Insights

The key insight that transcends the paper's individual contributions is that noisy correspondence in MVC can be fundamentally reframed as a latent variable problem rather than a pair-correction problem. Prior approaches (reweighting, realignment) operate on the given pairs — they decide which pairs to trust or how to fix them. CorreGen instead treats the pairing structure itself as unobserved and infers it probabilistically. This shift from discriminative pair-editing to generative pair-discovery is what enables the method to naturally handle both category-level many-to-many correspondences (via GMM-guided marginals in the OT coupling) and unalignable samples (via the virtual sample) within a single unified objective. The EM iteration — where the E-step estimates correspondences and the M-step uses them to learn better embeddings — creates a virtuous cycle that is particularly effective under high noise. This generative perspective could inform other learning problems where pairing structure is unreliable.

## Suggestions

1. Add standard deviations or confidence intervals to Tables 1 and 2.
2. Explicitly state whether all baselines were retrained under identical hyperparameters or clarify any differences.
3. Move a brief description of the MR/CR noise construction to the main paper (a short paragraph would suffice).
4. Discuss practical strategies for setting ρ without ground-truth noise rates, or show sensitivity analysis for ρ in the main paper.
5. Consider adding at least one more naturally noisy dataset to strengthen the real-world evaluation.

## Score and Decision

**Bracketing (Round 1):** I queried for MVC/NC papers in three bands. The low band (<3.5) contained papers like SpecRaGE (3.40) and VMF (3.00) — weak papers with unclear contributions or flawed methodology. The mid band (3.5–7.5) contained papers like SMvCNet (4.00), M3C (7.00), and COPER (7.25). The high band (>7.5) contained papers at 8.00 — notably strong with unanimous high scores. CorreGen clearly belongs in the mid-to-upper mid band.

**Narrowing (Round 2):** I queried for papers using EM, OT, or generative approaches in MVC. Anchors: COT (6.00, reject — clarity issues and weak motivation), M3C (7.00, accept — solid but with presentation shortcomings), COPER (7.25, accept — strong theory and extensive experiments), GenCorres (6.75, accept — well-motivated generative approach for shape matching), MVP (6.25, accept — incomplete multi-view VAE with some reproducibility concerns). 

**Calibration:** CorreGen is clearly stronger than COT (6.00) and MVP (6.25) — its problem formulation is cleaner, the empirical results are more comprehensive, and there are no structural methodological flaws. It is comparable to M3C (7.00) in overall quality — both have strong core contributions with some presentation gaps. It is slightly below COPER (7.25) in experimental breadth (COPER uses ten datasets and provides theoretical analysis). CorreGen's strengths lie in the principled generative formulation and the clear formalization of NC types, which are genuine contributions that distinguish it from prior MVC work.

**Final score and decision:** The paper makes a significant contribution with a well-motivated and novel approach, strong empirical results, and a clean theoretical framing. The weaknesses are real but addressable and do not undermine the core claims. Score: **7.0**. Decision: **Accept**.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>