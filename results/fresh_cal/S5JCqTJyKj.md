Now I have a thorough understanding of the paper and can verify all claims. Let me produce the consolidated review.

## Summary

This paper introduces Deferred Activated Backdoor Functionality (DABF), a new backdoor attack paradigm where the backdoor remains dormant (produces benign outputs even on triggered inputs) during initial deployment and only activates after the model undergoes routine fine-tuning on benign data — requiring no further attacker intervention. The authors propose DeferBad, a two-phase method: (1) standard backdoor injection followed by (2) a partial model update on clean data to conceal the backdoor by creating a "fragile unlearning" state that reverses under subsequent fine-tuning. Experiments on CIFAR-10 and Tiny ImageNet with multiple architectures (ResNet18, VGG16, EfficientNet-B0), trigger types (BadNets, ISSBA), and seven state-of-the-art detection methods provide initial evidence that the approach works.

---

## Strengths

1. **Genuinely novel attack paradigm.** DABF is conceptually distinct from prior backdoor attacks. Unlike conventional attacks that activate immediately (and are thus detectable), and unlike latent backdoors (Yao et al. 2019) that produce abnormal latent representations for triggered inputs during dormancy, DABF produces normal output behavior even on triggered inputs during the dormant phase. The paper formalizes this as an optimization problem (Section 3) and provides a concrete implementation. The key distinction from prior deferred attacks — no attacker intervention required for activation, robustness to which layers are fine-tuned — is new and practically relevant.

2. **Concrete empirical demonstration of dormancy and reactivation.** After concealment, ASR drops to 0.07%–0.60% across architectures on CIFAR-10 (Table 3), confirming genuine dormancy. After fine-tuning, ASR reaches 94.07% (ResNet18/BadNet), 93.23% (VGG16/BadNet), and 97.35% (EfficientNet/BadNet), confirming reactivation. These are large, clear effects that directly support the core claim.

3. **Demonstrated evasion of multiple standard detection methods.** DeferBad-infected models produce Neural Cleanse anomaly indices *lower than clean models* (0.672 vs 0.778 on CIFAR-10, Figure 3b), STRIP entropy distributions *higher than normal models* (Figure 3d), and GradCAM activation maps indistinguishable from clean models (Figure 3a). Scale-Up and IDB-PSC are also evaded. These results are striking because they invert the typical signal that detection methods rely on — the backdoored model appears *cleaner* than clean models on these metrics.

4. **Systematic evaluation across architectures and trigger types.** The method works on ResNet18, VGG16, and EfficientNet-B0, with both simple (BadNets) and complex (ISSBA) triggers, providing evidence that the mechanism is not brittle or tied to a single setup. Varying the number of fine-tuned layers (Figure 2) shows robustness across different fine-tuning configurations.

---

## Weaknesses

### Fatal
None.

### Major

1. **No quantitative comparison against prior deferred backdoor attacks.** The paper positions DeferBad relative to latent backdoors (Yao et al. 2019) and unlearning-based deferred attacks (Di et al. 2022; Liu et al. 2024; Huang et al. 2024) via qualitative Table 1, claiming DeferBad "addresses these limitations." However, **zero experiments compare DeferBad against any of these methods** under the same conditions. Without comparisons on ASR after fine-tuning, stealth metrics, or sensitivity to layer selection, the claimed advantages are unsubstantiated. This is the most significant evaluation gap: the paper needs to show *how much better* DeferBad is than the alternatives it claims to surpass.

2. **Limited fine-tuning scenarios tested relative to the generality claimed.** The paper tests two scenarios: (a) adding held-out data from the same distribution, and (b) fine-tuning on corrupted (CIFAR-10-C) versions of the same data. The introduction motivates the attack by noting that models are "adapted to new data distributions, or learned new tasks" (line 22), yet **no experiment tests task transfer** (e.g., CIFAR-10 → CIFAR-100, or fine-tuning on a subset of classes). The abstract and conclusion claim "various fine-tuning scenarios" and "robustness against various fine-tuning strategies," which overstates what was tested. Real-world fine-tuning for transfer learning is the most common use case the attack would exploit, and it is untested.

3. **Stealthiness evidence is incomplete.** Several defense results raise concerns:
   - **Fine-Pruning on Tiny ImageNet drives ASR to nearly 0%** (Section 5.3), a serious failure case for the attack on the larger dataset. The paper notes this but does not analyze why, nor does it discuss this limitation in the conclusion.
   - **RCS partially detects DeferBad** — detection scores are lower than for conventional BadNets but the method "showed some capability in detecting DeferBad" (line 164). The paper does not report the actual detection scores or the false positive rate.
   - **No variance or confidence intervals reported.** All results appear to be single-run. Detection metrics (Neural Cleanse anomaly index, STRIP entropy) can be noisy, and single runs are insufficient to establish statistical reliability.
   - **The relevant stealth baseline is other *deferred* attacks**, not just conventional attacks like BadNets, which are trivially detectable. Showing that DeferBad is stealthier than latent backdoors or unlearning-based attacks would substantiate the claimed advantages.

4. **The "defender knows the trigger" claim is untested and overstated.** The paper states that DABF "can potentially evade detection even in stronger scenarios, i.e., a defender knows the trigger, where all previous backdoor attacks fail" (line 22, echoed in abstract and contributions). While the paper uses hedging language ("potentially"), this is presented as an important advantage. No experiment tests this scenario, and no adaptive defense (e.g., a defender who fine-tunes the model and checks if ASR rises) is considered. This claim should either be removed or accompanied by an explicit test/analysis.

### Minor

1. **ISSBA ASR is substantially lower and unanalyzed.** On VGG16 with ISSBA, ASR after fine-tuning is only 48.54% (Table 3). The paper calls this "significant," but for a targeted attack on a 10-class task (random baseline 10%), 48% may not constitute a practical threat. The paper does not analyze why more complex triggers (ISSBA) are harder to reactivate, nor does it discuss what ASR threshold constitutes a successful attack.

2. **The unlearning dataset (D_unlearn) is not described in the main text.** The paper states concealment uses "an unlearning dataset D_unlearn" (line 103) and refers to Table 2 for details, but Table 2 is an image stripped by the parser. The composition, size, and relationship of D_unlearn to the training/fine-tuning data are not specified in the readable text. This matters because if D_unlearn overlaps with the fine-tuning data, the measured reactivation could be inflated. The authors should define D_unlearn explicitly in the main text.

3. **No ablation on concealment layer selection.** The method's core novel step is the *partial* update during concealment. Yet the paper only varies which layers are *fine-tuned* (Figure 2), not which layers are *concealed*. Ablations on (a) full vs. partial concealment update, (b) different layer choices for concealment, and (c) multiple concealment rounds are missing and would strengthen the understanding of the mechanism.

4. **Optimization formulation is disconnected from the method.** Section 3 presents a clean optimization objective, but Section 4 (DeferBad) implements a heuristic two-phase procedure that does not directly optimize it. The paper should clarify that DeferBad is an approximate solution rather than a direct instantiation.

### Trivial
None.

---

## Nice-to-Haves

- **Test fine-tuning on task transfer** (e.g., CIFAR-10 → CIFAR-100, or fine-tuning on a subset of classes). This is the most common real-world use case and would significantly strengthen the generality claim.
- **Report results with multiple random seeds** with variance, especially for detection metrics.
- **Include adaptive defenses** (e.g., a defender who sanity-checks ASR after a small fine-tuning step, or monitors latent representation drift).
- **Test on larger-scale datasets** (e.g., ImageNet-1K) to assess scalability.
- **Validate the latent representation distinction** from Yao et al. (2019) via an experiment comparing latent representations for triggered inputs.

---

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **"D_unlearn never described" — overstated due to parser stripping.** The paper refers to Table 2 for hyperparameters, optimization strategies, and specific settings. Table 2 appears as an image in the original PDF and was stripped by the parser. While the main text could be more explicit, the criticism that D_unlearn is "never described" is partially an artifact of the text extraction. I have kept the substantive concern (composition/overlap) as a Minor weakness above.
2. **"The distinction from latent backdoors should be validated by experiment comparing latent representations"** — The paper provides a conceptual distinction (normal output vs. different latent representations) and backs DeferBad's behavior with empirical evidence (near-zero ASR, normal GradCAM, normal Neural Cleanse indices). A direct comparison of latent representations is a nice-to-have, not a required validation of the paper's contribution.
3. **"Threat model disconnected from method"** — The paper presents the optimization as a formalization of the threat model, not as a claim that DeferBad directly optimizes it. This is a minor presentational point that does not affect the scientific validity.
4. **"Scalability to ImageNet-1K"** — A reasonable suggestion but not a weakness of the current work; the method is demonstrated on standard benchmarks (CIFAR-10, Tiny ImageNet) and the paper already acknowledges vision-only scope as a limitation.
5. **"Adaptive defense considerations"** — No backdoor attack paper is expected to pre-emptively address all possible adaptive defenses. This is a useful suggestion for future work but not a current weakness.
6. **Strength Finder: claims of "systematic robustness across diverse fine-tuning scenarios"** — The strength is genuine but the finder's promotional framing is softened above. Only two fine-tuning scenarios were tested (plus varying layer counts), not "diverse" ones.

---

## Novel Insights

None beyond the paper's own contributions. The two reviewers' perspectives are largely consistent: both recognize the novelty of the DABF paradigm and the strength of the core empirical demonstration (dormancy → reactivation, evasion of multiple detectors), while both identify the same critical gaps (no comparison with prior deferred attacks, limited fine-tuning scope, untested "knowing trigger" claim). The primary novel insight from synthesis is that the paper's weakest claims (generality to "various" scenarios, superiority over prior deferred attacks, "knowing trigger" evasion) are precisely the ones that are most persuasive if true — and the ones the evidence least supports. Strengthening exactly these three points would transform the paper from an interesting proof-of-concept to a convincing, impactful contribution.

---

## Suggestions

1. **Add quantitative comparison against at least one prior deferred backdoor method** (e.g., latent backdoors from Yao et al. 2019). Compare ASR after fine-tuning, Neural Cleanse anomaly indices, and sensitivity to layer selection. This single addition would address the most critical gap.

2. **Expand fine-tuning scenarios to include task transfer**, e.g., train on CIFAR-10 and fine-tune on CIFAR-100, or pre-train on Tiny ImageNet and fine-tune on a subset. This directly tests the real-world scenario the attack is motivated by.

3. **Either remove the "defender knows the trigger" claim or test it.** If kept, design an experiment where a defender who knows the trigger attempts to detect DeferBad (e.g., by fine-tuning the model themselves and monitoring ASR, or by checking for latent distribution shifts). If untestable, hedge the language more carefully.

4. **Report variance across multiple seeds** for all main results (Tables 3, 4, detection metrics). Single-run results are insufficient for detection thresholds that can be noisy.

5. **Explicitly define D_unlearn** (size, composition, overlap with training/fine-tuning data) in the main text, and ablate the choice of concealment layers.

---

## Score and Decision

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>