## Summary

This paper integrates n-gram induction heads (from Akyürek et al.) into transformers for Algorithm Distillation-based in-context reinforcement learning (ICRL). The authors replace some multi-head attention layers with n-gram layers that compute higher-order n-gram statistics, and claim three benefits: reduced data requirements (up to 27×), reduced hyperparameter sensitivity, and applicability to image observations via vector quantization. Experiments span Dark Room, Key-to-Door, and Miniworld (3D) environments.

## Strengths

- **Well-designed evaluation protocol using Expected Maximum Performance (EMP):** Rather than cherry-picking best runs, the paper reports EMP over random hyperparameter searches (Section 3.2, Figures 2, 4, 5, 6), providing a principled comparison of both maximum achievable performance and training robustness. This is a genuine methodological strength that makes the results more trustworthy than typical single-best-run reporting.

- **Consistent improvements across multiple environments and modalities:** The n-gram method shows faster HP convergence in Dark Room (Figure 2: ~20 vs >400 assignments), Key-to-Door (Figure 4), and both Miniworld settings (Figure 5, 6). The extension to pixel-based observations via VQ (Section 2.3, validated in Figures 5 and 6) broadens the method's applicability beyond the discrete settings where n-gram matching is trivial.

- **Controlled internal data efficiency comparison (Figure 1):** Figure 1 provides a direct, controlled comparison on Dark Room showing the n-gram method reaches near-optimal performance with ~128 goals versus ~512 for the baseline AD, on the same data pipeline with the same number of goals varied along a single axis. This is well-controlled evidence of improved data efficiency.

- **Useful ablation studies:** Table 1(a)-(b) show the method is insensitive to n-gram length and layer position (EMP ranges 0.67–0.76), reducing the practical overhead of the new hyperparameters. The permuted mask experiment (Table 1(c)) demonstrates that broken matching doesn't degrade performance below baseline.

## Weaknesses

### Fatal
None.

### Major

- **The 27× data reduction claim compares against external results rather than a controlled experiment.** The headline claim (Section 4.2, Figure 4) compares their method's result with 100 goals / 1000 histories against Laskin et al.'s [17] reported result using 2048 goals / 2048 histories — a different publication's training pipeline, hyperparameter search protocol, and data structure. The paper's own controlled comparison in Figure 1 (Dark Room, same pipeline) shows ~4× improvement (128 vs 512 goals), which is meaningful but far from 27×. The Appendix B justification for the 27× computation is stripped from the accessible version, but even so, cross-paper comparisons with different data structures (diverse tasks vs. many histories per task) introduce confounds that a single controlled experiment would resolve. This is the first bullet of the paper's contributions, and it is not convincingly substantiated by the available evidence.

- **Only one baseline (AD) is compared.** The paper's contribution is framed as improving ICRL broadly, but all experiments compare only against Algorithm Distillation [17]. Given the growing ICRL landscape (Decision Transformer variants, supervised in-context RL approaches), a single baseline makes it difficult to assess the generality of the improvements. The paper would be substantially stronger with even one additional baseline.

### Minor

- **The distinction between data efficiency and hyperparameter search efficiency is blurred.** The paper motivates the work around data requirements (Section 1: "reduce the amount of data required for generalization") but the primary experimental metric (EMP vs. HP assignments) measures hyperparameter search efficiency. These are related but distinct properties. Figures 1 and 4 do provide genuine data-efficiency evidence, but the paper's framing could more clearly delineate which results speak to which claim. The EMP curves primarily show that n-gram layers make the HP search surface smoother (fewer trials needed to find good configs), which is valuable but different from traditional data efficiency.

- **Table 1(c) results are presented at different scale/conditions than the main figures, creating interpretive confusion.** The permuted-mask ablation shows EMP of 0.51 ± 0.03 for Miniworld-Dark (Table 1(c)), while Figure 5 shows the n-gram model reaching ~0.94 on the same environment. This large gap suggests different experimental configurations (number of HP trials, data settings) between the ablation tables and main figures, but the paper doesn't clarify this. Additionally, the permuted ≈ baseline result (0.51 vs. 0.52) is better understood as showing that random matching drops performance *back to baseline level*, which actually *supports* the claim that the n-gram matching pattern drives the improvement — yet the paper doesn't frame it this way, missing an opportunity to strengthen the mechanistic argument.

- **No analysis of what the n-gram attention actually learns.** The paper never examines which patterns the n-gram heads match in the RL context, whether matches correspond to semantically meaningful state transitions, or how often matches are found in practice. For image-based observations, the strict matching criterion (all 16 VQ indices must be equal, Section 2.3) may cause many false negatives — no analysis of match rates or VQ reconstruction quality is provided.

- **Evaluations are limited to relatively simple environments.** Dark Room (9×9 grid), Key-to-Door, and Miniworld are useful testbeds but well below the complexity of environments where ICRL is most needed. The paper acknowledges this in the conclusion but it limits the practical significance of the findings.

### Trivial
None.

## Nice-to-Haves
- Replace the n-gram layer with a standard attention layer of identical parameter count to disambiguate whether improvements come from the n-gram mechanism specifically or from additional capacity.
- Visualize n-gram attention patterns during inference to show what the mechanism is actually doing in the RL setting.
- Report VQ codebook utilization and reconstruction quality to validate the image-based matching pipeline.

## Removed Points
These points are flagged to be removed, treat them with caution.

- **"Table 1(c) directly undermines the mechanistic claim" (from harsh critic):** This criticism misinterprets the ablation result. The permuted-mask experiment shows that random matching drops to baseline level (0.51 ≈ 0.52), while the main experiments show correct matching substantially outperforms baseline (e.g., ~0.94 vs ~0.80 on Miniworld-Dark in Figure 5). This actually *supports* the paper's claim that the n-gram mechanism matters. The critic conflates "random matching doesn't help" with "matching quality doesn't matter," ignoring the positive evidence from the main experiments. Removed as factually incorrect interpretation.

- **"Evaluation measures hyperparameter search efficiency, not data efficiency" (from harsh critic, overstated version):** The paper provides both types of evidence — EMP curves for HP sensitivity and Figures 1/4 for data efficiency. The criticism is valid as a clarity concern (see minor weakness above) but not as a fundamental conflation.

- **Missing related works / retrieval-augmented ICRL (from harsh critic):** We cannot verify the existence of specific unmentioned related works, and the paper's related work section covers the main relevant references.

- **"1-gram outperforming 2-gram raises questions about n-gram framing" (from harsh critic):** Table 1(a) shows 1-gram at 0.74 ± 0.02 vs 2-gram at 0.71 ± 0.01 — these are within noise given the error bars. This is not a meaningful concern.

## Novel Insights

The paper's key insight — that hardcoding n-gram induction heads (a mechanism known to emerge in language transformers) into ICRL architectures can shortcut the training process and reduce data requirements — is conceptually straightforward but practically useful. The EMP-based evaluation framework for comparing hyperparameter sensitivity in ICRL is a methodological contribution that could benefit future work in this area. The successful extension to image observations via VQ-based n-gram matching, while simple, demonstrates the mechanism's flexibility beyond discrete settings.

## Suggestions
- Run a controlled data-efficiency experiment on Key-to-Door where both AD and the n-gram method are trained on the same dataset sizes (e.g., 100, 250, 500, 1000 goals) with the same HP search protocol. This would either substantiate or correct the 27× claim.
- Add a control where the n-gram layer is replaced with a standard MHA layer of equal parameter count. This single experiment would address the most important mechanistic question.
- Clarify in the text which experiments measure data efficiency vs. HP search efficiency, and frame the claims accordingly.

## Calibration Report

**Round 1 anchors (bracketing):**
- Weak band (avg < 3.5): 5dDYhvt6dY (3.0, efficient transformer for translation, reject), to4PdiiILF (3.0, ICRL reward hacking, reject), vlOfFI9vWO (3.0, MARL for ViT, reject), INzc851YaM (3.0, multi-objective offline RL, reject)
- Middle band (avg 3.5–7.5): b5MCteb3w7 (4.75, ICRL beyond Bayesian inference, reject), 2PKLRmU7ne (5.60, in-context learning and Occam's razor, reject), aN4Jf6Cx69 (4.50, mechanistic basis of ICL, accept), 1lFZusYFHq (6.20, how transformers implement induction heads, reject)
- Strong band (avg > 7.5): OvoCm1gGhN (8.0, Differential Transformer, accept), mMPMHWOdOy (8.0, WizardMath, accept)

**Round 1 bracket:** Between 4.5 and 6.5. The paper has cleaner methodology than the 4.75 paper (which had fundamental metric issues) but less novelty than the 6.20 theoretical paper.

**Round 2 anchors (narrowing):**
- Band (4.0, 6.0): b5MCteb3w7 (4.75), TFR0GrzERG (5.25, task description in ICL, reject), TSlJ3ikcBZ (5.60, latent variables in ICL, reject), E8TPUAimyJ (4.50, context-scaling vs task-scaling, reject)
- Band (6.0, 7.5): qup9xD8mW4 (6.67, behaviour distillation, accept), XnX7xRoroC (6.25, distilling RL into single-batch datasets, reject), leACdxBEgv (6.67, Adaptive Q-Network, accept), rTBL8OhdhH (7.00, dataset distillation, accept)

**Round 2 comparison:**
- vs. b5MCteb3w7 (4.75, reject): Our paper is clearly better — cleaner evaluation, no fundamental methodological issues, consistent improvements across environments.
- vs. E8TPUAimyJ (4.50, reject): Our paper is stronger — empirical results are more convincing and the setting is more practical.
- vs. TSlJ3ikcBZ (5.60, reject): Comparable contribution level; our paper has more thorough empirical evaluation but less theoretical insight.
- vs. qup9xD8mW4 (6.67, accept): "Behaviour Distillation" introduced a genuinely new problem formulation and novel algorithm; our contribution is more incremental (known technique applied to new domain), though our evaluation is cleaner.
- vs. leACdxBEgv (6.67, accept): "AdaQN" addressed a similar theme (HP sensitivity in RL) with a more novel algorithmic contribution and validation on harder environments (MuJoCo, Atari).

**Final positioning:** The paper sits above the 4.5–5.0 rejected papers (which had fundamental issues) but below the 6.5–7.0 accepted papers (which had more novel algorithmic contributions). The paper's strength is its clean evaluation methodology and consistent improvements; its weakness is the incremental nature of the contribution and limited evaluation scope. Score: 5.5.

## Score and Decision

**Evaluation on key axes:**
- **Originality:** Moderate — applying a known mechanism (n-gram induction heads from Akyürek et al.) to a new domain (ICRL). The VQ-based image matching is a reasonable technical addition.
- **Importance of research question:** Moderate-high — data efficiency and training stability in ICRL are real pain points.
- **Claims well-supported:** Mostly — HP sensitivity claims are well-supported; the 27× data claim is not.
- **Soundness of experiments:** Good — EMP protocol is well-designed, multiple environments tested, ablations provided. Limited by single baseline and simple environments.
- **Clarity of writing:** Good — clear structure, well-motivated, could better distinguish data efficiency from HP search efficiency.
- **Value to community:** Moderate — a practical technique for ICRL practitioners, but limited novelty and scope.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>