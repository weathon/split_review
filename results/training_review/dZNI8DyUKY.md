Now I have a thorough understanding of the paper and can cross-check all claims. Let me produce the final consolidated review.

## Summary

This paper proposes MAEP, a test-time adversarial purification method that integrates a Masked Autoencoder (MAE) into a purifier framework, offering an alternative to diffusion-based purifiers. The key idea is to leverage MAE's masking mechanism as a self-supervised preprocessing step before a downstream classifier, and the paper's central empirical finding is that an MAEP trained on CIFAR-10 achieves competitive robust accuracy on ImageNet under AutoAttack, outperforming diffusion-based models (DiffPure, ScoreOpt) that were trained on ImageNet directly. The paper also identifies and addresses a train-test discrepancy in the masking ratio (r=0.5 during training vs. r=0 at inference) via lightweight LoRA finetuning.

## Strengths

- **Novel integration of MAE into adversarial purification.** MAEP is, to my knowledge, the first pure-purifier framework based on masked autoencoders, as distinct from DRAM (detection+repair) and NIM-MAE (adversarial training). The paper clearly delineates this distinction in Table 1 and throughout the text.

- **Impressive defense transferability demonstrated empirically.** The headline result — MAEP trained on CIFAR-10 achieves ~74% robust accuracy on ImageNet under AutoAttack (ε∞=4/255), outperforming DiffPure (68.60%) and ScoreOpt (68.05%) that were trained on ImageNet — is both surprising and practically relevant. This cross-resolution, cross-dataset transfer is a genuinely differentiator from diffusion-based purifiers that lose robustness when moved off their training distribution (documented in Tables 2 and 3).

- **Practical efficiency.** MAEP reports inference times of 0.01s per image on CIFAR-10 (Table 9) and training time of 11.7 hours (Table 10), versus 1.04s–1.32s inference and days of training for diffusion methods. This makes the approach substantially more practical for resource-constrained or real-time settings.

- **Identifies and mitigates the train-test masking discrepancy.** Section 4.4 surfaces a subtle issue — masking ratio r=0.5 during training vs. r=0 at inference — and addresses it via LoRA finetuning, demonstrably improving both clean and robust accuracy (Table 5). This is a genuine practical insight specific to MAE-based purification.

## Weaknesses

### Fatal
None.

### Major

- **No evaluation against adaptive attacks that differentiate through the purifier.** For any adversarial purification method, the standard evaluation protocol requires testing against attacks that are aware of the purification mechanism — e.g., BPDA (backward-pass differentiable approximation) or PGD with full gradients through the purifier. The paper tests only against AutoAttack and PGD, which treat the purifier as a black box. Without adaptive attacks, the reported robust accuracies are not validated against the most relevant threat model. This is the single most important missing experiment for a purification paper, and its absence means the headline robustness claims (especially "state-of-the-art performance") are not yet credibly established.

### Minor

- **Overclaimed generalization from narrow baselines.** The abstract states that MAEP "outperforms existing diffusion-based models trained specifically on ImageNet," but the comparison is against only two diffusion models (DiffPure, ScoreOpt). While the margins are meaningful (~74% vs. ~68% at ε=4/255 on ImageNet), the sweeping "state-of-the-art" language is not commensurate with the breadth of baselines. A more measured claim (e.g., "outperforms representative diffusion-based purifiers DiffPure and ScoreOpt") would better align with the evidence.

- **Theoretical justification is informal and tangentially connected to MAE's specific contribution.** Section 4.2 provides a derivation that purification loss ℓ₁(𝒫(xₐ),x) approximately aligns with the negative adversarial perturbation direction, and Table 4 offers empirical support. However, this derivation explains why *any* purifier with a reconstruction loss (like DISCO) can maintain clean accuracy — it does not explain what the masking mechanism specifically adds. The connection to why MAE's masking helps (beyond being a generic autoencoder) is left as an assertion rather than analyzed. This weakens the paper's conceptual contribution even if the empirical results are valid.

- **No direct comparison with DRAM (the most closely related MAE-based defense).** The paper excludes DRAM because it involves detection (not pure purification), which is a reasonable scoping choice. However, including DRAM — even as a reference point — would contextualize where MAEP stands relative to the closest MAE-based competitor, especially since the paper claims to be the "first" MAE-based purifier and needs to demonstrate the advantages of the pure-purification design.

### Trivial
None.

## Nice-to-Haves

- Reporting standard deviations or confidence intervals for the main results (the paper states results are averaged over 5 runs but provides no variance estimates).
- An ablation replacing the MAE encoder with a standard autoencoder (no masking) to isolate the specific benefit of the masking mechanism for purification.
- Ablation of different masking ratios at inference (beyond r=0) to better understand the train-test discrepancy and the role of information loss.
- Visual side-by-side comparisons of purified images from MAEP vs. DiffPure/DISCO to substantiate the claimed "purification quality."

## Removed Points

These points from the reviewers were flagged for removal; treat them with caution:

- **Criticism about under-specified method (missing loss functions and architecture details).** The paper references Eqs. (9), (10), (12) and says "Details of model structure and parameter settings can be found in Sec." and "Please refer to Sec." — these are clearly cross-references to supplementary/appendix sections that were stripped by the parser. Per the hard rule, criticisms about missing appendix content are removed.

- **Criticism that claimed CIFAR-10 robust accuracy contradicts paper's own text (MAEP 52.04% vs. DiffPure 53.59%).** The specific numerical values cited by the harsh critic come from a table image that is not extractable as text. The paper's textual description (line 215) states "MAEP and ScoreOpt-O are comparable but better than DiffPure." Since the actual table values cannot be verified from the extracted text, this specific numerical claim cannot be validated and is removed.

- **Criticism about missing standard deviations/confidence intervals.** Moved to Nice-to-Haves, as single-pass evaluation without explicit confidence intervals is the norm in large-scale adversarial robustness benchmarking.

- **Criticism that the theoretical section doesn't "meaningfully connect to why MAE helps."** WEAKENED to Minor — the derivation is informal but the paper frames it as "a feasible but simple explanation," not a rigorous proof. The real gap is that it doesn't isolate the masking mechanism's role specifically.

- **Strength about "comprehensive empirical evaluation across multiple benchmarks."** Dropped because it conflicts with the verified weakness about missing adaptive attacks — the evaluation, while covering multiple datasets, is incomplete on the most critical dimension for purification papers.

## Novel Insights

The reviews surface an interesting tension: the paper's most striking result (transfer from CIFAR-10 to ImageNet) is also its least fully validated, because the threat model that matters most for purification (adaptive, gradient-aware attacks) was not tested. The transferability claim itself is supported by the data and is genuinely novel — showing that a lightweight MAE purifier can generalize across resolutions and datasets where diffusion models fail. However, the reviews collectively suggest that the paper's contribution is currently strongest as a *proof of concept* for MAE-based purification with transferability, and weakest as a claim of *state-of-the-art robustness* (which requires adaptive attack evaluation). A revised version that adds adaptive attacks and tones down the SOTA language would substantially strengthen the paper.

## Suggestions

1. **Add adaptive attack evaluation (BPDA, full-gradient PGD through the purifier) on at least one main benchmark (e.g., CIFAR-10).** This is the single change that would most significantly increase confidence in the robustness claims. Without it, the paper cannot be accepted at a venue that requires rigorous evaluation of defenses.

2. **Include DRAM as a comparison point** in at least one table, even if with the caveat that DRAM uses detection. This would clarify the empirical landscape of MAE-based defenses and justify the "first MAE purifier" claim more concretely.

3. **Tone down the "state-of-the-art" language** in the abstract and conclusion to match the actual breadth of baselines (e.g., "outperforms prior diffusion-based purifiers DiffPure and ScoreOpt").

4. **Add an ablation isolating the masking mechanism** (e.g., compare MAEP against a version without masking, or against a standard ViT autoencoder) to directly test whether masking is the source of the benefit or simply the architecture choice.

5. **Report standard deviations** for the main results, especially since the paper already averages over 5 runs — this variance information likely already exists and just needs to be reported.

## Score and Decision

The paper introduces a genuinely novel idea (MAE for adversarial purification) with a practically relevant property (defense transferability across datasets/resolutions) and strong efficiency advantages. However, the evaluation has a significant gap: the absence of adaptive attacks, which is the standard requirement for purification papers, means the core robustness claims are not yet validated against the most relevant threat model. The paper also overclaims relative to its baseline breadth. These issues are fixable but material in the current submission.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>