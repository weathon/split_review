Now I have all the information needed. Let me compose the final consolidated review.

## Summary

This paper proposes Robust Diffusion Classifier (RDC), a generative classifier built from a diffusion model. RDC classifies inputs by computing class-conditional diffusion losses and applying Bayes' theorem, with a likelihood maximization pre-optimization step that moves inputs toward high-density regions before classification. The paper provides theoretical analysis showing the optimal diffusion classifier achieves perfect robustness, proposes a multi-head diffusion backbone for efficiency, and reports 75.67% ℓ∞ robust accuracy on CIFAR-10 (ε=8/255), outperforming prior methods.

## Strengths

1. **Novel and well-motivated approach.** The idea of converting a diffusion model into a generative classifier for adversarial robustness is genuinely creative and addresses a clear limitation of prior work (discriminative classifiers' vulnerability and diffusion-based purification's weak adaptive-attack resistance). The framing — harnessing the diffusion model's accurate score estimation across the data space as a classifier rather than just a preprocessor — is conceptually clean.

2. **Strong empirical results with credible improvements.** RDC achieves 75.67% robust accuracy under ℓ∞ AutoAttack (ε=8/255), surpassing AT-EDM by +4.77% and all prior generative classifiers by a large margin (Table 1). The generalization results across ℓ∞, ℓ2, and StAdv threats are particularly striking — >30% average improvement and >53.90% under StAdv — supporting the claim that the method is agnostic to the threat model.

3. **Theoretical foundation.** Theorem 2 and Corollary 3 show that an optimal diffusion classifier achieves 100% robust accuracy under ℓ∞ and ℓ2 attacks, providing a principled reason why the approach can be highly robust. While the gap between optimal and practical models is acknowledged, this analysis grounds the method in theory rather than being purely empirical.

4. **Careful adaptive-attack methodology.** The paper goes beyond standard AutoAttack by implementing BPDA, Lagrange attacks, exact gradient attacks (for N=1), and analyzing gradient variance. BPDA closely matches the exact gradient for N=1 (69.53% vs. 69.92%), and the Lagrange attack does not find stronger attacks than BPDA for N=5. Gradient variance is shown to be low (Fig. 1a). These steps represent a serious effort to rule out gradient obfuscation.

5. **Practical efficiency contribution.** The multi-head diffusion backbone (modifying the last UNet layer to output K×3 channels) reduces NFEs from K×T to T per image, a practically meaningful improvement that makes the otherwise expensive diffusion classifier feasible for CIFAR-10-scale evaluation.

## Weaknesses

### Fatal
None.

### Major

1. **Evaluation on a 512-image subset without statistical grounding.** The paper evaluates all main results on 512 randomly selected images from CIFAR-10 (line 247), citing computational cost. No confidence intervals, standard deviations, or bootstrapped estimates are reported. The paper claims "robust accuracy of most baselines does not change much on our selected subset" (line 262) but provides zero evidence for this — no comparison of subset numbers to full-test-set RobustBench values, no quantification of the deviation, and no justification for "does not change much." Since all baselines (AT-EDM, AT-DDPM, DiffPure) are normally evaluated on the full 10,000-image test set, and the state-of-the-art claims hinge on a +4.77% margin, the reader cannot assess whether the reported advantage would hold on the full distribution. The paper's central empirical contribution rests on uncertain footing.

2. **BPDA gradient approximation validated only for N=1, while main results rely on N=5.** The paper shows that BPDA and exact gradient match closely for N=1 (69.53% vs. 69.92%, Table 2). However, the main robustness claim (75.67%) uses N=5 optimization steps, where exact gradient computation is infeasible due to memory. Gradient approximation error can compound over multiple unrolled optimization steps, potentially making BPDA for N=5 a weaker attack than the true gradient. The Lagrange attack (which uses the same BPDA gradient) also does not resolve this. Without any verification for N>1 — e.g., exact gradient for N=2 or N=3 via gradient checkpointing on a smaller batch, or finite-difference gradient checks on a subsample — the claimed robustness for the full RDC may be overestimated. This is the most critical evidential gap.

### Minor

3. **"Pre-trained diffusion model" framing overstates what is used off-the-shelf.** The title and abstract emphasize "a single pre-trained diffusion model" as the foundation. However, the multi-head diffusion backbone requires modifying the UNet's last convolutional layer to output K×3 channel noise predictions (line 231), which in turn requires either training from scratch or fine-tuning with a modified architecture. The paper does not clarify whether this modification requires full retraining or is a lightweight fine-tuning, nor does it report the associated cost. The method remains interesting with retraining, but the "pre-trained" framing should be qualified.

4. **No runtime or inference-cost comparison.** The paper does not report wall-clock time, NFEs, or per-image inference cost for RDC vs. any baseline. Likelihood maximization (N=5) requires 5 forward+backward passes through the UNet, and the diffusion classifier uses T (e.g., 1000) forward passes even with multi-head diffusion. Without reporting actual computational cost, it is impossible to assess the practical trade-off between RDC's improved robustness and its computational burden.

5. **The likelihood maximization objective is a heuristic with limited analysis.** The approach minimizes unconditional diffusion loss under an ℓ∞ constraint (Eq. 7), arguing that increasing unconditional log-likelihood also increases conditional log-likelihood for the true class (line 188). This is not formally justified — the optimization could move the input to a region of high unconditional density that lies in a different class's territory. The constraint η=8/255 equals the attack budget, meaning the defense's optimization budget is as large as the attacker's. While the ablation on η (Fig. 1b) partially addresses this, the paper does not analyze whether an attacker can exploit this by crafting inputs whose unconditional likelihood maximization pulls them toward a wrong class.

6. **DiffPure baseline evaluation uses a non-standard protocol.** The paper evaluates DiffPure with PGD-200 + 10×EOT instead of AutoAttack with full EOT (line 263), citing memory constraints and the insufficiency of the adjoint method. While the paper provides reasoning, the deviation from the standard evaluation protocol for this baseline makes the comparison less clean. The paper should at minimum report what attack parameters were used for each baseline and justify any deviations.

### Trivial
- No dedicated limitations section discussing failure cases or scenarios where RDC underperforms (e.g., when the diffusion model's density estimation is poor for certain classes).

## Nice-to-Haves
- Reporting bootstrapped 95% confidence intervals for all main results would substantially improve credibility.
- A comparison of baseline numbers on the 512-image subset vs. the full 10,000-image test set (referencing RobustBench) would anchor the evaluation.
- A runtime comparison table (seconds per image for RDC vs. DiffPure vs. AT-EDM) would help assess practical feasibility.
- Partial verification of BPDA accuracy for N=2 or N=3 using gradient checkpointing on a small subsample would strengthen the adaptive attack claims.

## Removed Points

- **"Missing appendix, proofs, or training details"** — Removed per rule: the parser strips appendix content from all papers; these exist in the original submission.
- **"Theorem 1 assumption of d→0 is circular"** — The paper explicitly acknowledges this gap (lines 128, 165) and introduces likelihood maximization precisely to address it. The theoretical analysis separately treats the optimal case (Section 3.2-1) and the practical case. This is a limitation the authors are transparent about, not a structural flaw.
- **"Discriminative vs generative gap is narrower than claimed"** — The remark about the optimal classifier using weighted Euclidean distances is not inconsistent with the paper's framing; a density-based decision rule is fundamentally different from a learned discriminative boundary, and the paper's theoretical results (100% robust accuracy for the optimal classifier) validate its central claim about generative classification.
- **"Formatting/typo nitpicks"** — Removed per rule (parser artifacts).
- **"Missing related work"** — Removed per rule (cannot verify from external sources).

## Novel Insights

The reviews surface two key insights beyond the paper's own contributions. First, the tension between the paper's theoretical framework (Theorem 1 assumes d→0) and its practical algorithm (likelihood maximization exists because d is large) reveals a deeper question: can one directly characterize how the variational bound gap affects classification decisions, rather than treating it as a nuisance to be optimized away? Second, the pattern of evaluative challenges — small test subset, partial gradient verification, heuristic optimization — is a recurring tension in diffusion-based defense papers (DiffPure had similar evaluation debates), and a community-wide expectation for what constitutes sufficient adaptive-attack evaluation for multi-step differentiable defenses has not yet crystallized. RDC would benefit from being the paper that helps set that bar rather than merely meeting the current one.

## Suggestions

1. **Validate on the full CIFAR-10 test set**, even if at the cost of fewer attack iterations. The 512-image subset undermines confidence in the absolute numbers far more than a slightly weaker attack on the full set would.
2. **Provide exact-gradient verification for N=2 or N=3** using gradient checkpointing on a smaller batch, or at minimum compare BPDA results against a forward-difference gradient approximation on a handful of examples to bound the approximation error for multi-step LM.
3. **Report confidence intervals** (bootstrapped or over multiple runs) for all main robustness numbers on the 512-image subset.
4. **Clarify the multi-head diffusion training requirements** — does it require full retraining or just fine-tuning the last layer? What is the computational cost? Acknowledge the "pre-trained" framing qualification explicitly.
5. **Report inference cost** (seconds per image, total NFEs) for RDC and all baselines.

## Score and Decision

The paper proposes a genuinely novel approach to adversarial robustness with strong conceptual backing and theoretically grounded motivation. The empirical results are promising, and the generalization to unseen threats is particularly compelling. However, two major evidential gaps — evaluation on an unanchored 512-image subset without variance reporting, and BPDA validation limited to N=1 while main results use N=5 — prevent full confidence in the central claims. These are addressable in revision but are too significant for unconditional acceptance at a top venue.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>