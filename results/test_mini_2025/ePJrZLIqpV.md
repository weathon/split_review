Now I have all the information I need to produce the final review.

**Round 1 bracket**: Based on the calibration search and my reading, the paper sits between 3.5 and 5.5. The weak-band anchors (avg ≤3.5) are too low — the paper has genuine novel ideas (TIA, MMA) and consistent empirical trends. The middle-band anchor PdA9HAxO4w (avg 5.0, Reject) and the 5.8 anchor (iR5qF9N1Ge, Reject) are comparable in having interesting ideas but evaluation gaps. The 6.25 anchors (e.g., TASAR, Accept Poster) are clearly stronger (code release, comprehensive evaluation, proper budgets).

**Round 2 narrowing**: I examined papers in the 3.5–5.5 range more closely. LvjSLnMlwY (avg 4.25, Reject) and DYVSLfiyRN (avg 4.0, Withdrawn) are the closest matches. The paper under review has more original core ideas than these anchors (TIA/MMA are genuinely new attacks, not just adaptations of existing techniques), but the evaluation gaps are also more severe (no perturbation budgets, defense only against own attack, no clean accuracy). I place the paper slightly above the 4.0–4.25 range at **4.5** — the ideas are worth noting but the evaluation is not ready for publication.

---

## Summary

This paper proposes two novel audio-visual adversarial attacks — the Temporal Invariance Attack (TIA) and the Modality Misalignment Attack (MMA) — that exploit temporal redundancy and cross-modal semantic alignment, plus an adversarial training defense with efficient perturbation crafting and curriculum learning. The core ideas are well-motivated by experiments in Section 3 showing that temporal masking boosts transferability and that modality correlation provides a compensatory effect.

## Strengths

1. **Novel, domain-specific attack designs.** TIA targets temporally invariant features by minimizing feature variance across transformed frames, and MMA disrupts cross-modal semantic alignment by reducing feature similarity between audio and visual streams. These are genuinely tailored to audio-visual data, unlike prior work that adapts image-domain attacks. The attacks are conceptually clean and well-motivated by the empirical study in Section 3.

2. **Consistent empirical advantage across diverse architectures.** In Figure 5, TIA, MMA, and their combination TMA consistently outperform all baselines (FGSM, I-FGSM, MI-FGSM, MIG, PAM) across 8 different audio-visual model configurations spanning AlexNet/ResNet visual backbones, VGG/ResNet audio backbones, and sum/concat fusion layers. TIA exceeds PAM by 15.7% on average, and TMA reaches 95.2% average success rate.

3. **Empirical motivation grounded in audio-visual properties, not just intuition.** Section 3 provides direct experimental evidence (Figures 1 and 2) that temporal redundancy can boost adversarial transferability by up to 13.8% and that modality correlation compensates against perturbations. These findings are quantified, not merely stated, and they directly inform the design of TIA and MMA.

4. **Ablation reveals anti-overfitting behavior of the proposed attacks.** Figure 8 shows that TIA and MMA maintain or improve transferability as attack iterations increase, while I-FGSM and MI-FGSM degrade due to overfitting to the surrogate model. This provides mechanistic insight into why the proposed attacks are stronger.

## Weaknesses

### Major

1. **No perturbation budgets reported (ε_v, ε_a).** The problem formulation in Eq. (1) defines ε_v and ε_a, but the experimental sections (6.1–6.4) never specify the values used. This is the most critical omission: (a) the reader cannot tell whether the proposed attacks outperform baselines because they are genuinely stronger or merely allowed larger perturbations; (b) the defense results are uninterpretable — the 2.28% improvement over CRMT-AT could reflect a better defense or simply a different attack budget; (c) the paper is not reproducible as presented. *This is verifiable on the page: the only mentions of ε are in the problem formulation (lines 121–123, 200); no numerical values appear anywhere in Section 6.*

2. **Defense evaluated only against the authors' own attack.** Section 6.4 states: "We use our strongest attack TMA to evaluate the robustness." The claimed robustness improvement is demonstrated exclusively against the specific attack (TMA) that the defense was designed to counter. To support the claim that the defense "largely improves adversarial robustness," the paper must show robustness against a *range* of attacks (standard PGD, MI-FGSM, etc.). Evaluating only against TMA is circular — the defense incorporates curricular training and efficient perturbation crafting explicitly tailored to generate TMA-like examples, so improvement on TMA is expected.

3. **No clean accuracy reported for any defense method.** Adversarial training typically degrades clean accuracy. The paper reports only attack success rates in Figure 7, with no clean (unperturbed) classification accuracy for any defense method (AT, DCFL, Mixup, CRMT-AT, Ours). Without this, the reader cannot assess whether the robustness improvement comes at a prohibitive cost. *Verifiable: grep for "clean accuracy" returns no matches.*

### Minor

4. **Weak empirical support for the MMA hypothesis.** The paper hypothesizes that "lower semantic correlation leads to higher adversarial audio-visual transferability" and supports this with Figure 3, which shows only 4 data points (FGSM, I-FGSM, MI-FGSM, NI-FGSM) with no statistical test or error bars. FGSM (ASR ~31%, C.S. ~42%) and I-FGSM (ASR ~30%, C.S. ~43%) show essentially the same ASR with similar C.S., and MI-FGSM and NI-FGSM have nearly identical C.S. (~38%) but different ASR (53% vs. 55%). The relationship is suggestive but the evidence is too thin to strongly motivate the attack design.

5. **No efficiency comparison against baselines for the defense.** The paper claims "efficient adversarial perturbation crafting" that reduces computational overhead, but Figure 9 only compares training time for different sampling ratios *within* the proposed method. There is no wall-clock comparison to standard adversarial training, CRMT-AT, or any baseline. The efficiency claim is unsupported.

6. **Missing hyperparameter values.** The losses in Eq. (4) include λ₁ and λ₂ as balancing coefficients, but their values are never reported. Similarly, input transformation details (scaling, masking, blurring, mix-up parameters) are listed without specifics.

7. **Eq. (3) notation is confusing and may be incorrect.** The MMA loss is written as $\frac{f_a \cdot f_v}{\|f_a \cdot f_v\|_2^2}$. If "·" denotes the dot product, the denominator is the squared L2 norm of a scalar (the dot product itself), yielding $\mathcal{L}_M = 1/(f_a \cdot f_v)$. Minimizing this maximizes the dot product (i.e., *maximizes* similarity), which is the opposite of the stated goal of minimizing feature similarity. If the notation means something else, it is not explained. This needs clarification.

### Trivial

8. No error bars or standard deviations are reported for any experimental result, making it difficult to assess the significance of small differences (e.g., the 2.28% defense improvement).

## Nice-to-Haves

- Ablate defense components separately: compare (a) standard AT, (b) AT + efficient perturbation crafting only, (c) AT + curriculum only, (d) AT + both, to isolate which component drives the improvement.
- Show attack success rate as a function of perturbation budget ε for the proposed methods versus baselines.
- Include the MIT-MUSIC dataset results (currently only in the appendix, which is stripped by the parser) in the main text for cross-dataset validation.

## Removed Points

- **Criticism about model generality (Section 3 uses only one architecture).** The paper's empirical study is a case study motivating the attack designs, not a comprehensive benchmark. The limitation is implicitly acknowledged, and the main evaluation in Section 6 uses 8 architectures.
- **"State-of-the-art" claim is overbroad.** This is a consequence of weaknesses 1–3 above, not a separate issue. The claim is testable once the evaluation gaps are fixed.
- **"Ensemble attack 100% ASR is suspicious."** This is speculative; it could reflect genuinely strong attacks. The real issue is the missing perturbation budget (weakness 1), which is already listed.
- **"MIG baseline is not described."** The paper cites (Ma et al., 2023), which is standard practice. Missing description of a cited baseline is not a weakness of the paper.
- **Several generic Strengths from the Strength Finder** were removed: generic statements about the problem being important, claims about "state-of-the-art" that the evidence does not fully support, and generic praise of thoroughness. Only concrete, evidence-backed strengths are retained.

## Novel Insights

None beyond the paper's own contributions. The key insight — that temporal redundancy and cross-modal alignment create exploitable vulnerabilities specific to audio-visual models — is well-articulated by the authors themselves.

## Suggestions

1. Report the perturbation budgets ε_v and ε_a for all experiments. Show ASR as a function of ε to demonstrate that the advantage over baselines holds across perturbation sizes.
2. Evaluate the defense against a diverse set of attacks (PGD, MI-FGSM, TIA, MMA, TMA) and report both clean accuracy and robust accuracy for every defense method.
3. Ablate the defense components to isolate the contribution of curriculum learning vs. efficient perturbation crafting vs. dropout.
4. Clarify the notation in Eq. (3) and ensure the loss function correctly implements the stated goal of minimizing feature similarity.
5. Report hyperparameters λ₁, λ₂, learning rates, and attack step budgets.

## Score and Decision

**Round 1 bracket**: I identified anchors in three bands by querying "audio-visual adversarial attack defense adversarial training multimodal robustness." The weak band (avg < 3.5) produced papers scoring 2.5–3.2 — the paper under review is clearly stronger than these. The middle band (3.5–7.5) produced papers scoring 3.67–5.8, including PdA9HAxO4w (avg 5.0, Reject), iR5qF9N1Ge (avg 5.8, Reject), and DYVSLfiyRN (avg 4.0, Withdrawn). The strong band (avg > 7.5) produced papers scoring 7.6–8.0 — the paper under review is clearly weaker than these. Initial bracket: **3.5–5.5**.

**Round 2 narrowing**: I queried papers in the (3.5, 5.5) range on "multimodal adversarial attack audio visual temporal transferability black-box missing evaluation." Retrieved LvjSLnMlwY (avg 4.25, Reject — TUAP for CLIP, similar pattern of interesting ideas but incomplete evaluation), XbLffB0T2z (avg 4.4, Reject — poisoning attacks, different topic), efxXzrbgrX (avg 3.75, Withdrawn), and DYVSLfiyRN (avg 4.0, Withdrawn). Reading LvjSLnMlwY in full showed a paper with one strong vote (8) and three weak ones (3,3,3) — reviewers found it technically competent but insufficiently novel. The paper under review has more original core ideas (truly audio-visual-specific attacks rather than adapted image attacks) but also more severe evaluation gaps (missing budgets, one-sided defense eval). I also read PdA9HAxO4w (avg 5.0, Reject) and iR5qF9N1Ge (avg 5.8, Reject); both have more complete evaluation than the paper under review, with proper hyperparameter reporting and comparison protocols.

**Final position**: The paper's attack ideas are genuinely novel for the audio-visual domain and the empirical results are consistently in their favor. However, the missing perturbation budgets, defense evaluation-only-against-TMA, and absent clean accuracy are significant gaps that prevent the paper from supporting its core claims. The paper sits below PdA9HAxO4w (5.0) and iR5qF9N1Ge (5.8) due to these gaps, and above LvjSLnMlwY (4.25) and DYVSLfiyRN (4.0) due to stronger foundational ideas and more consistent empirical trends.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>