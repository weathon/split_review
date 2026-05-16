Now I have a thorough understanding of the paper. Let me produce the final consolidated review.

---

## Summary

This paper proposes the Key-Locks (K&L) backdoor attack, which decouples the trigger mechanism from model parameters by embedding multiple "locks" during training and generating input-specific "keys" via gradient descent at inference. The paper formally identifies "high binding" between triggers and model parameters as the root cause of backdoor vulnerability to defenses. Experiments across four datasets, four architectures, and eight defense algorithms show K&L is the only method among seven baselines that maintains non-trivial Attack Success Rates under all tested defenses.

## Strengths

- **Conceptual contribution (high-binding analysis).** The paper is the first to explicitly formalize three necessary conditions for backdoor attacks (stealth, efficacy, normal operation) and to identify "high binding" with model parameters as the structural weakness exploited by defenses (Section 1, Figure 1). This framework provides a principled rationale for the K&L design and is not a mere restatement of existing ideas.

- **Empirically validated decoupling strategy.** Table 1 shows K&L is the only method among seven baselines (BadNet, Blended, WaNet, Bpp, Input-Aware, SSBA) that achieves non-trivial ASR under all eight evaluated defenses across all four datasets — e.g., 71.59% ASR on CIFAR-10 under ANP pruning where all other methods fall below 3%, and 99.92% ASR on Tiny ImageNet under RNP. This systematic comparison demonstrates a clear practical advantage of the decoupling approach.

- **Rigorous and comprehensive experimental protocol.** The evaluation covers four diverse datasets (CIFAR-10/100, GTSRB, Tiny ImageNet), four modern architectures (PreActResNet18, VGG19-BN, MobileNet-v3, EfficientNet-B3), and eight state-of-the-art defenses spanning pruning, fine-tuning, unlearning, knowledge distillation, and attribution-based detection. All baselines are re-implemented with published hyperparameters, and code is publicly released.

- **Attribution-based stealthiness analysis.** The paper uses BIG attribution (Figure 2, Table 2) to quantitatively demonstrate that K&L backdoor samples have the highest Cosine similarity to clean-sample attribution maps, providing evidence of stealthiness beyond ASR numbers alone.

## Weaknesses

### Fatal
None.

### Major

- **The AAC metric (listed as a contribution) is never defined.** The paper introduces the Accuracy-ASR Curve (AAC) as a third contribution in the introduction and reports AAC values (AAC1=0.9415, AAC3=0.9111, AAC5=0.8772) in the results section, as well as the term "AAV." However, the extracted text contains no description of how the curve is constructed, what the subscripts 1/3/5 refer to, what AAV stands for, or how AAC is computed from empirical data. A claimed contribution that is not specified cannot be evaluated.

- **Ablation study is announced but no results are presented in the text.** Section 4.3 describes the four parameters under study (epochs, learning rate, level, attack step size) and their default settings, but provides zero output — no table, no figure, no summary of findings. Even accounting for possible parser-stripped figures, the main text should contain a prose summary of the ablation conclusions. This makes it impossible to assess how sensitive K&L is to its hyperparameters.

### Minor

- **"Locks loss" and "maintain loss" are named but not explicitly mapped to loss terms in Eq. 7.** The paper refers repeatedly to these losses (Sections 3.3.1, 3.3.2) but never states "maintain loss = L(x,y;W)" or "locks loss = L(x′,c_t;W)." Eq. 7 *does* define the dual-objective training procedure, so the method is not missing — but the disconnection between the named concepts and the equations creates unnecessary ambiguity. Explicitly labeling the terms would resolve this.

- **The key-generation procedure in Eqs. 5–6 is gradient-descent perturbation of inputs, which is structurally identical to an adversarial attack at inference time.** The paper's defense (Section 3.4) focuses on the training-phase difference (model parameters are modified during training), which is correct but incomplete: the key itself is still a per-input adversarial perturbation. The paper would be stronger if it experimentally validated why this is not merely an adversarial attack — e.g., by showing that keys fail without pre-trained locks, or that the required perturbation magnitude is significantly smaller than a standard PGD attack of equivalent strength.

- **Section 3.3 (Embedding Locks) header and content are missing from the extracted text.** The paper jumps from Section 3.2 (heading only) directly to Section 3.3.1, so the description of the embedding process is absent from the text trace. Eq. 7 in Section 3.4 partially fills this gap by providing the training objective, but the missing section likely contained additional detail (e.g., training algorithm, poisoning schedule) that would aid reproducibility.

### Trivial
- Duplicate word: "the the" on line 18.

## Nice-to-Haves
- A direct comparison of keys vs. standard PGD adversarial perturbations at the same perturbation budget, to empirically validate the claim that locks enable easier category transition.
- A summary table of multi-architecture results (VGG19, MobileNet, EfficientNet) in the main text rather than only in the appendix.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **Harsh critic's claim that "the method is not specified with enough precision to be reproducible" as a fatal structural flaw.** The training objective IS given in Eq. 7 (dual-objective optimization: W* = argmin_W L(x,y;W) + λ L(x′,c_t;W)), and the key generation IS given in Eqs. 5–6. The method is not "undefined" — it is underspecified in naming and section continuity, not absent. Lowered from Fatal to Minor.

- **Harsh critic's claim that Section 2 does not position K&L relative to Input-Aware/SSBA.** The paper explicitly states: "Input-Aware attack generate unique triggers for each input, however the generator is highly related to the model parameters" and in Section 3.3.2 that K&L's key generation "differs from the generator in Input-aware methods... it does not have parameters and does not require training." The positioning exists; this criticism is irrelevant.

- **Harsh critic's claim that Tables/Figures being non-visible invalidates the evidence.** Tables 1–3 and Figures 2–4 are image files that the parser cannot render, but the paper's textual description provides key quantitative results (71.59% ASR under ANP, 99.92% under RNP, AAC values, Cosine similarity scores). The text alone is sufficient to assess the paper's main claims; visual tables would strengthen but are not absent.

- **Strength Finder's claim about the AAC metric as a strength.** Since the metric is never defined in the extracted text, it cannot stand as a demonstrated strength. It is a claimed contribution awaiting verification, not a confirmed strength. Downgraded.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Define the AAC metric explicitly.** Include the formal definition of how the Accuracy-ASR Curve is constructed, what AAV stands for, and what the subscripts (1, 3, 5) represent. Without this, the claimed third contribution is unverifiable.

2. **Explicitly map "Locks loss" and "maintain loss" to the terms in Eq. 7.** Add a sentence such as: "The first term L(x,y;W) is the maintain loss (preserving accuracy on clean inputs), and the second term L(x′,c_t;W) is the locks loss (embedding the backdoor)."

3. **Add ablation results to the main text.** Even a brief summary of findings or a small table would make the ablation study informative rather than merely present.

4. **Provide an experiment demonstrating why keys are not just adversarial perturbations.** For example, generate keys from a model *without* locks and show they require significantly larger perturbation to reach the target class, or fail entirely at the same perturbation budget.

5. **Reconstruct any content missing from Section 3.3** to ensure the "Embedding Locks" training procedure is documented end-to-end in the text (not only in figures).

## Score and Decision

The paper makes a genuine conceptual contribution (identifying and addressing "high binding") and provides strong empirical evidence that K&L outperforms seven baselines across eight defenses. The core weakness is presentation: a claimed contribution (AAC) is not defined, loss names are not mapped to equations, and ablation results are absent from the text. These are all fixable in revision. The paper has real value to the backdoor attack/defense community and the evidence, where visible, supports the claims.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>