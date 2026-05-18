Now I have a thorough understanding of the paper and all reviewer claims. Let me produce the final consolidated review.

## Summary

This paper identifies a trade-off in training robust ensembles: lowering the Lipschitz constant of individual models improves their individual robustness but increases adversarial example transferability within the ensemble, harming overall ensemble robustness. To address this, the authors propose LOTOS (Layer-wise Orthogonalization for Training rObust enSembles), which orthogonalizes the top-*k* subspaces of corresponding affine layers across ensemble members. They provide a theoretical argument (Theorem 4.1) that *k*=1 suffices for convolutional layers. Empirically, LOTOS improves black-box robust accuracy by up to 6 p.p. over clipped baselines on CIFAR-10 and can be combined with prior methods like TRS for additional gains.

## Strengths

- **First to identify and empirically validate a trade-off between Lipschitz continuity and ensemble transferability.** Figure 1 clearly shows that as the layer-wise clipping value decreases, individual robust accuracy increases but the average transferability rate (*T_rate*) among ensemble members also rises. This insight is novel and well-supported — prior work treated Lipschitz continuity as purely beneficial for robustness without examining its effect on ensemble diversity.

- **LOTOS effectively reduces transferability while preserving individual robustness gains from Lipschitz clipping.** In Table 1, LOTOS achieves up to 6 p.p. higher black-box robust accuracy over C=1 (clipped) baselines across both CIFAR-10 and CIFAR-100 with ResNet-18 and DLA architectures. Figure 2 shows that LOTOS reduces *T_rate* by roughly 20% compared to C=1 ensembles.

- **LOTOS combines with prior SOTA (TRS) and yields further improvements.** Table 3 shows that LOTOS + TRS outperforms TRS alone by up to 10.7 p.p. on CIFAR-100, and the paper notes no hyperparameter tuning was performed for this combination, suggesting further gains are possible.

- **Ablation studies convincingly validate key design choices.** The ensemble-size ablation (Table 2) shows LOTOS improves robust accuracy by 14 p.p. when scaling from 3 to 9 models, while C=1 improves by only 3 p.p. — confirming that LOTOS is solving a diversity problem that clipping alone cannot. Figure 3 (Left) confirms that *k*=1 is empirically sufficient, and Figure 3 (Right) shows that applying LOTOS only to the first convolutional layer retains most of the benefit, enabling heterogeneous ensembles.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Theorem 4.1's theoretical grounding is weaker than claimed.** The theorem assumes a single input/output channel and circular padding — neither holds for typical convolutional layers in architectures like ResNet-18 (multi-channel, zero padding). The bound depends on ‖*f*‖₂, which is only implicitly controlled through weight decay. The theorem does not *directly* prove that *k*=1 is sufficient for practice; it only bounds the effect on higher singular vectors given control of the first. Fortunately, the empirical ablation in Figure 3 (Left) convincingly shows that *k*=1 works, so the theorem is not necessary for the paper's claims. However, the paper presents it as a key contribution ("we theoretically show that *k* does not need to be large"), and the gap between the theory and practice should be acknowledged.

2. **Comparison to prior SOTA is fragmented.** The main robustness table (Table 1) only compares LOTOS to "Orig" and "C=1" baselines. DVERGE (Yang et al., 2020) is discussed but only appears in the (stripped) appendix (§S.9). TRS appears in a separate table (Table 3) that combines it with LOTOS, but there is no single table where LOTOS-alone, DVERGE, and TRS are all evaluated under identical conditions with a single set of attack parameters. A unified comparison would make the empirical contribution immediately clear.

3. **Proposition 3.3 provides indirect support.** The proposition bounds the difference in *population losses* on adversarial examples, which is a proxy for transferability rather than a direct measure of misclassification agreement. Two models can have similar losses but disagree on predictions. The paper uses appropriately cautious language ("might be an indicator," "might imply"), and the empirical evidence in Figure 1 is the actual support for the conjecture. The proposition is not misleading, but its theoretical weight is modest.

4. **Sensitivity of the key hyperparameters λ and mal is not reported.** The paper varies mal in Figure 2 and mentions λ in the loss formulation, but never states the default values used or provides an ablation on λ. This makes it harder to gauge how much tuning was needed to achieve the reported results.

5. **The claim of "negligible" computational overhead is not quantified.** The paper states that LOTOS is efficient and that overhead is small when only the first layer is orthogonalized, but no training-time comparison (e.g., seconds per epoch vs. baseline) is provided in the main text.

6. **The white-box attack used to measure *T_rate* is not specified.** The paper mentions using "white-box attacks" to evaluate transferability within the ensemble but does not state the attack algorithm, number of steps, or perturbation budget for these internal evaluations.

### Trivial
None (formatting issues are parser artifacts).

## Nice-to-Haves
- A unified table comparing LOTOS, C=1, DVERGE, and TRS under identical conditions with full attack parameters stated.
- A brief sensitivity analysis for λ and mal (even a few sentences noting the range tested and the chosen defaults).
- Training wall-clock time per epoch for LOTOS vs. C=1.
- Explicit statement of the white-box attack configuration used for *T_rate* evaluations.
- Acknowledgement in the main text that Theorem 4.1's assumptions (single channel, circular padding) differ from practice, and that the empirical ablation is the primary justification for *k*=1.

## Removed Points
These points are flagged to be removed; treat them with caution.

- **Missing attack parameters (ε, steps) as a core flaw.** The critic argued that the paper "never specifies the attack algorithm, perturbation budget (ε), number of steps, or any other attack parameters" and that this makes results unverifiable. The paper repeatedly references §S sections (appendix, stripped by the parser), which would contain these experimental details per standard conference format. A brief mention of ε in the main text would be preferable, but this is a presentation issue, not a fatal omission. *Moved from "Fatal/Major" to "Nice-to-Have".*

- **Dependency on FastClip as a practical limitation.** The critic argued LOTOS is tied to FastClip and its limitations. FastClip is a published, citable method; the paper's use of it is no different from using any standard tool. *Removed as speculative.*

- **Criticisms that the paper does not use the reviewer's preferred baselines.** The critic mentions DVERGE and TRS should be in the main table. The paper does compare to TRS (Table 3) and references DVERGE in the appendix. The paper's contribution is about a specific trade-off and a method to address it — not about beating all prior methods on a leaderboard. The fragmented comparison is kept as a Minor weakness; the stronger framing as a "structural weakness" is removed.

- **The claim that LOTOS "cannot be properly evaluated" or "needs major revision."** The paper's core claims are well-supported by the empirical evidence that is present (Figure 1, Figure 2, Table 1, Table 2, ablation studies). The missing details (attack parameters) are standard appendix content. The overall assessment in the harsh review is too severe relative to the actual content. *Removed as disproportionate.*

## Novel Insights
None beyond the paper's own contributions. The reviewers correctly identify the paper's core novel insight — that Lipschitz continuity creates a previously overlooked diversity-robustness trade-off in ensembles — but do not offer a new synthesis beyond what the paper already states.

## Suggestions
- Add a brief paragraph in §5 stating the attack configuration (ε, attack algorithm, steps, restarts) used for the reported robust accuracy numbers. If this is already detailed in the appendix, add a brief note in the main text such as "we use PGD-20 with ε = 0.5 (L2) for CIFAR-10; see §S.X for details."
- Include a single unified table in the main paper comparing LOTOS, C=1, DVERGE, and TRS under identical conditions, or add a sentence explicitly referencing the appendix table that provides this comparison.
- Acknowledge the gap between Theorem 4.1's assumptions and realistic architectures, and clarify that the empirical result (Figure 3 Left) is the primary evidence for *k*=1 sufficiency.
- Report default values for λ and mal, and include a brief sensitivity study in the appendix.

## Score and Decision

**Originality:** Good — the trade-off between Lipschitz continuity and ensemble transferability is a novel observation that reframes a commonly held assumption. **Importance of question:** High — robust ensembles are practically relevant and the identified issue is real. **Claims supported:** Mostly yes — the core empirical claims (trade-off exists, LOTOS mitigates it) are well-supported. The theoretical contribution (Theorem 4.1) is weaker than claimed. **Soundness of experiments:** Solid for what is reported; fragmented comparison to prior work is the main gap. **Clarity:** Reasonable; the paper is generally well-structured. **Value to community:** The trade-off insight is likely to influence how future work designs robust ensembles.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>