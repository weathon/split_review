Now I have sufficient calibration data. Let me write the consolidated review.

## Summary
2-3 sentence summary of the paper's contribution.

## Strengths
- strength 1 with evidence
- strength 2 with evidence

## Weaknesses
### Fatal
### Major
### Minor
### Trivial

## Nice-to-Haves

## Removed Points

## Novel Insights

## Suggestions

## Score and Decision

---

Let me compile the final review based on careful verification of all claims against the paper.

**Verification of reviewer claims:**

1. **λ hyperparameter concern** (Harsh Critic): The paper states in Section 5.5: "λ is ultimately established at 0.1, selected from the range [0.1:0.1:1.0] based on the best classification accuracy on the validation set." The parameter analysis (Fig 1b) only shows CIFAR-10→CIFAR-100. The paper doesn't explicitly state whether λ was tuned separately for other settings. This is a legitimate but minor concern. **KEEP as Minor.**

2. **AUROC suggestion** (Harsh Critic): The paper uses AUPR, which is standard for OOD detection. The reviewer suggests adding AUROC — this is a nice-to-have, not a weakness. **MOVE to Nice-to-Haves.**

3. **KL regularization clarity** (Harsh Critic): The paper mentions "following previous works (Sensoy et al., 2018; Deng et al., 2023), we adopt an additional KL-divergence based regularization for optimization, and its detailed introduction can be found in Appendix A.2." The appendix is stripped by the parser. The paper clearly references where to find this. **REMOVE** (parser artifact).

4. **Scalability** (Harsh Critic): Suggests ImageNet-100. This is scope creep — the paper's experiments already cover classical, few-shot, noisy, and video settings. **REMOVE.**

5. **No structural flaw** (Harsh Critic): Agreed, I verified the derivations are sound and match the paper.

6. **Strength finder claims** - All strengths are specific and verifiable from the paper text. **KEEP all.**

Let me now construct the review.Here is my consolidated final review:

---

## Summary

This paper identifies and relaxes two "nonessential settings" in Evidential Deep Learning (EDL): (1) the prior weight parameter \(W\) (or equivalently \(\lambda = W/C\)), which EDL historically fixes to the number of classes, is reinterpreted as a tunable hyperparameter; (2) the variance-minimization regularization term \(\mathcal{L}_{var}\) in the EDL loss is deprecated because it pushes the Dirichlet PDF toward a Dirac delta, exacerbating overconfidence. The resulting method (R-EDL) replaces both rigidities with principled alternatives while staying within the subjective logic framework. Experiments on classical, few-shot, noisy-label, and video-modality settings show consistent improvements over EDL and the state-of-the-art \(\mathcal{I}\)-EDL.

## Strengths

1. **Clear theoretical analysis of the prior weight's role.** Section 3.2 derives how \(W\) governs the trade-off between evidence proportion and magnitude (Eqs. 7–8), and gives a concrete counter-intuitive example (100-class task where extreme evidence [100,0,…] yields predicted probability ≈ 0.5 when \(W=100\)). This is the first formal treatment of this parameter in the EDL literature.

2. **Principled justification for removing the variance-minimization term.** Section 3.3 shows that \(\mathcal{L}_{var}\) drives the Dirichlet PDF toward a Dirac delta (Eq. 13), forcing infinite target-class evidence and worsening overconfidence. Replacing it with direct expectation optimization (Eq. 11) is well-motivated and grounded in subjective logic.

3. **Consistent empirical gains across multiple challenging settings.** Tables 1 and 2 show statistically significant improvements over both EDL and \(\mathcal{I}\)-EDL in classical and few-shot settings. For example, on CIFAR-10→SVHN (Table 1), R-EDL achieves 85.00% OOD AUPR vs. \(\mathcal{I}\)-EDL's 83.26% (+1.74% absolute). Gains extend to noisy settings (Fig. 1a) and video-modality (Appendix D.4).

4. **Ablation study cleanly isolates each contribution.** Table 3 shows that relaxing only \(\lambda\) (keeping \(\lambda=1\)) yields 83.24% AUPR, relaxing only \(\mathcal{L}_{var}\) yields 84.04%, and combining both reaches 85.00% on CIFAR-10→SVHN. This confirms both relaxations contribute positively and synergistically.

5. **Parameter sensitivity analysis.** Fig. 1(b) plots accuracy and OOD AUPR against \(\lambda\) from 0.01 to 1.5, demonstrating that the optimal value (\(\lambda \approx 0.1\)) differs from the traditional default (\(\lambda=1\)) and that R-EDL beats EDL across the entire range.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Hyperparameter \(\lambda\) is only analyzed on one dataset pair.** The parameter analysis (Fig. 1b) sweeps \(\lambda\) only on CIFAR-10→CIFAR-100. The paper selects \(\lambda=0.1\) based on CIFAR-10 validation accuracy and uses this value across all experiments (MNIST, mini-ImageNet few-shot, video). It is not shown whether \(\lambda=0.1\) is near-optimal for these other settings, and the paper does not state explicitly whether \(\lambda\) was tuned separately per setting or kept constant. This matters because if \(\lambda\) were tuned per setting, some reported gains could partly reflect hyperparameter optimization rather than the relaxations themselves. However, two factors mitigate the concern: (a) the ablation row "R-EDL w/ \(\lambda=1\)" in Table 3 still outperforms both EDL and \(\mathcal{I}\)-EDL on most metrics, showing that even with the *original* \(\lambda\) setting, deprecating \(\mathcal{L}_{var}\) alone helps; (b) the paper honestly acknowledges the optimal \(\lambda\) mechanism as future work. Still, the paper would be stronger with sensitivity analysis on at least one additional dataset (e.g., mini-ImageNet few-shot).

2. **Noise robustness experiment is somewhat limited.** Figure 1(a) reports the *average* of classification accuracy and OOD AUPR under Gaussian noise, but does not show the two metrics separately. Since OOD detection and classification accuracy can exhibit different sensitivity to noise, separate plots would give a clearer picture.

### Trivial
None.

## Nice-to-Haves

- **AUROC in addition to AUPR.** Many recent OOD detection papers report AUROC alongside AUPR. While AUPR is appropriate when the outlier class is rare, including AUROC would improve comparability with the broader literature.
- **Guidance on choosing \(\lambda\).** A simple heuristic (e.g., related to total evidence scale or cross-validation rule) would increase practical utility beyond the current empirical selection.

## Removed Points

- **"KL regularization term is unclear."** The paper explicitly references Appendix A.2 for the KL term's form and weight. The appendix is stripped by the parser; this is not a paper flaw.
- **"Scalability to larger datasets (ImageNet-100)."** The paper's experiments already span classical, few-shot, noisy, and video settings. Requesting a larger benchmark is scope creep, not a weakness.
- **"Missing comparison with prior works on uncertainty."** The related work section covers EDL extensions and other single-model uncertainty methods adequately. The reviewer did not identify a specific missing baseline — this was speculation.
- **Strengths removed:** Generic strengths about "addressing an important problem" or "well-written" that lacked specific content anchors were dropped. Only evidence-grounded strengths are retained.
- **"The method seems easy to implement"** from strength finder — generic, removed.

## Novel Insights

None beyond the paper's own contributions. The reviews surface no observation about the method or results that the authors themselves do not already note. The harsh critic correctly identifies the \(\lambda\)-generalization concern, which the paper itself acknowledges as a limitation in the conclusion.

## Suggestions

1. **Add \(\lambda\) sensitivity analysis for at least one additional setting** (e.g., mini-ImageNet few-shot or video). This would significantly strengthen the claim that the relaxation is robust rather than tuned.
2. **Report whether \(\lambda\) was tuned separately per experimental setting** or kept constant at 0.1. If constant, state this explicitly and justify; if tuned, report the optimal values found for each setting.
3. **Separate the two metrics in the noise plot** (Fig. 1a) rather than averaging them, so readers can assess robustness of classification and OOD detection independently.

---

## Calibration Anchors

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| `zeeLxGw5pp.md` | 3.20 | R1 | Weaker paper; flawed method + unclear writing |
| `6Z8rZlKpNT.md` | 3.40 | R1 | Weaker paper; method with limited empirical validation |
| `10fsmnw6aD.md` | 2.50 | R1 | Much weaker; poorly-scoped work |
| `KBGbEncHZF.md` | 3.00 | R1 | Much weaker; mainly about deepfake detection |
| `56jIlazr6a.md` | 5.25 | R1/R2 | Comparable in clarity but had theoretical gaps; R-EDL is more rigorous |
| `ym0ubZrsmm.md` | 5.33 | R1/R2 | Comparable venue/setting but had dataset-specific concerns about generalizability |
| `iqAbdT35hE.md` | 5.75 | R1/R2 | Comparable in OOD focus; R-EDL has more thorough ablation |
| `cv2iMNWCsh.md` | 7.25 | R1 | Stronger paper; broader scope and deeper theoretical treatment |
| `A7t7z6g6tM.md` | 6.00 | R2 | Directly comparable (EDL extension). R-EDL has more conventional/convincing experiments |
| `bDWXhzZT40.md` | 6.67 | R2 | Broader scope and more extensive experiments; R-EDL is more focused |
| `pDDODPtpx9.md` | 6.50 | R2 | Comparable quality; different domain (regression) |
| `ruGY8v10mK.md` | 6.50 | R2 | Similar quality; R-EDL's theoretical grounding is stronger |

**Round 1 bracket:** Between 4.5 and 7.5 (clearly above weak anchors at 2.5–3.4, clearly below the 7.5+ band which contains papers with broader scope and deeper theory).

**Narrowing:** Compared against the directly comparable anchor `A7t7z6g6tM.md` (avg 6.0, Hyper Evidential Deep Learning, another EDL extension), R-EDL has more standard experimental setups and cleaner ablation. Compared against `bDWXhzZT40.md` (avg 6.67), R-EDL is more focused but less broad in scope. R-EDL sits between these two and is slightly above the 6.0 anchor, placing it at **6.5**.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>