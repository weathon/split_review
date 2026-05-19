- Decision: Reject
- Avg Score: 5.50
- Scores: 3, 5, 6, 8
Now I have everything I need. Let me produce the final consolidated review.

## Summary

This paper proposes INR-Bayes, a Bayesian framework for joint reconstruction of multiple objects using implicit neural representations (INRs) in sparse-view CT. The method introduces latent variables that capture common patterns across objects through a variational EM procedure, with a KL divergence term that adaptively regularizes individual reconstructions based on their similarity. Experiments on four CT datasets plus CelebA demonstrate advantages in reconstruction quality and, more distinctively, robustness to overfitting and noise.

## Strengths

- **Principled adaptive regularization mechanism.** The method extends beyond simple averaging or meta-initialization approaches. The closed-form M-step (Eq. 7) automatically adjusts regularization strength per weight element — larger variance in the prior leads to weaker regularization and vice versa — which is both novel and computationally efficient.

- **Strong robustness to overfitting under extended training and noisy measurements.** Figures 3–4 and Table 2 convincingly show that baselines (SingleINR, MAML, FedAvg) degrade substantially under extended training or noise, while INR-Bayes maintains stable performance. This is a practically important advantage given that early stopping is unreliable in sparse-view CT without ground-truth references. The individual convergence curves in Figure 5 demonstrate that different patients have different optimal stopping points, making a one-size-fits-all early stopping strategy inherently flawed — directly motivating INR-Bayes's robustness.

- **Effective transfer to unseen objects.** Table 3 reports that on new LungCT patients (not used during joint training), INR-Bayes achieves PSNR 31.31 and SSIM 0.799, clearly outperforming SingleINR (30.22/0.769), FedAvg (29.89/0.754), and MAML (30.42/0.770). This indicates that the learned prior generalizes better than meta-initialization approaches.

- **Comprehensive and well-structured experimental design.** The paper evaluates six noiseless settings (four CT datasets + CelebA), three noisy settings, an ablation on number of nodes, varying numbers of scanning angles, and a transfer-to-unseen-objects scenario. Three joint-reconstruction baselines (INRWild, MAML, FedAvg) are adapted from existing work and clearly taxonomized in Section 3.1.

- **Consistent reconstruction quality improvement across most settings.** In Table 1, INR-Bayes achieves the highest PSNR in all six noiseless settings and the highest SSIM in five out of six. In noisy settings (Table 2), it achieves the highest PSNR and SSIM on all three CT datasets. These gains are supported by error bars and visual comparisons.

## Weaknesses

### Fatal

None.

### Major

- **Narrative overreach in the "consistently outperforms" claim.** The Table 1 caption states that INR-Bayes "consistently" outperforms other methods, which is contradicted by the CelebA SSIM entry where RegLLT-TV achieves 0.858 vs. INR-Bayes's 0.847. The main text (line 305) acknowledges "the exception of the SSIM values on the CelebA dataset," but the caption itself remains misleading. Additionally, the contributions list foregrounds "enhanced reconstruction quality" as the primary benefit without explicitly mentioning robustness/overfitting resistance, even though the overfitting evidence is the paper's strongest and most distinctive finding. This framing mismatch weakens the paper's internal coherence.

- **Absence of statistical significance testing.** The paper reports means and standard errors but performs no formal significance tests (paired t-tests, Wilcoxon, confidence intervals for differences). This matters because several noiseless comparisons show only modest differences relative to error bars — for example, Inter-walnut PSNR: INR-Bayes 36.13±0.33 vs. MAML 35.66±0.38 (difference ≈0.47 vs. combined SE ≈0.50); Inter-Lung PSNR: 33.75±0.20 vs. 33.13±0.22 (difference ≈0.62 vs. combined SE ≈0.30). Without significance testing, the reader cannot assess which differences are reproducible vs. evaluation noise. This is particularly relevant because the paper claims "outperforms the compared INR-based baselines" as a central contribution.

### Minor

- **Missing sensitivity analysis for β (KL weight hyperparameter).** The hyperparameter β controls the balance between reconstruction fidelity and KL regularization. Its value likely affects the trade-off between smoothness and detail preservation, but no ablation or sensitivity study is provided. This would help users understand how to set β in practice and how sensitive results are to its choice.

- **MAML's performance degradation with more nodes is unexplained.** Figure 6 shows that INR-Bayes improves with more joint reconstruction nodes while MAML's performance declines. This is unusual for a meta-learning method (more training data should not hurt) and the paper offers no hypothesis for why this occurs. An explanation — or at minimum a diagnostic analysis — would strengthen the claims about the quality of the learned prior.

- **Single Monte Carlo sample per iteration used without discussion.** The algorithm uses one MC sample from the variational posterior per iteration (line 213: "We only do MC sampling once at each iteration"). The paper asserts this works efficiently but does not discuss whether multiple samples would affect gradient variance or convergence quality. A brief justification or empirical note would improve reproducibility.

### Trivial

- The reference `\Cref{fig:nodes}` (line 456) appears to point to a figure label not present in the extracted text, suggesting a possible broken cross-reference.

## Nice-to-Haves

- A sensitivity analysis for the KL weight β would be a useful addition, helping practitioners understand the trade-off between regularization strength and reconstruction fidelity.
- Reframing the contributions to explicitly foreground robustness and overfitting resistance (alongside quality improvement) would align the narrative more closely with the strongest evidence.

## Removed Points

These points were flagged but are excluded from the main weaknesses after verification against the paper:

- **"MAML and FedAvg receive fewer gradient steps on individual tasks"**: This criticism overlooks that MAML and FedAvg are designed to split compute between meta-learning and adaptation. The 30K total iteration budget is standard — methods are compared at equal total compute. The overfitting experiment (Figure 3) additionally shows that even with extended training, baselines degrade while INR-Bayes does not, which addresses the concern.
- **"Single MC sample is a reproducibility concern"**: Downgraded from the harsh critic's framing to a minor note. The paper explicitly states the choice and it works efficiently — the concern is about documentation depth, not a flaw in the method.
- **"The real contribution is robustness, not quality"**: Overstated. The paper's quality improvements in noiseless settings are real — INR-Bayes achieves highest PSNR in all 6 settings — and the abstract does mention robustness. The mismatch is in emphasis, not substance. Moved to Major weakness #1 (narrative overreach) and Nice-to-Haves.

## Novel Insights

The most striking finding that neither reviewer fully articulated is the tension exposed in the number-of-nodes ablation (Figure 6): INR-Bayes improves with more training objects while MAML degrades. This is not a minor curiosity — it suggests a fundamental difference in how the two methods use multi-object data. INR-Bayes's Bayesian prior converges toward population statistics as sample size grows, while MAML's meta-initialization may overfit to spurious commonalities in the training set, creating an initialization that actively harms adaptation when given more data. This observation could motivate future work on when Bayesian joint reconstruction is preferable to meta-learning.

## Suggestions

1. Revise the table caption to accurately reflect that INR-Bayes achieves the highest metrics in most but not all settings, and rephrase the contributions list to explicitly mention robustness and overfitting resistance as primary benefits alongside reconstruction quality.
2. Add statistical significance tests (e.g., paired t-tests or confidence intervals for the INR-Bayes vs. best-baseline difference) to help readers distinguish meaningful improvements from noise.
3. Include a sensitivity analysis for β (KL weight), showing how it affects the fidelity-regularization trade-off.
4. Offer a hypothesis for MAML's performance drop with more joint nodes — this is a genuinely unusual result that warrants analysis.
5. Briefly discuss why a single MC sample suffices in the variational approximation (e.g., gradient variance is acceptable because the KL term stabilizes learning across iterations).
