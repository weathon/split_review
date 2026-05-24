Now I have a thorough understanding of the paper and calibration anchors. Let me construct the final review.

**Initial bracket assessment:** Based on round 1, the paper sits between the weak anchors (~2.5-3.0) and the strong anchors (~8.0). Given the paper's clear contribution and algorithm but significant framing and rigor issues, I'd bracket it between 4.5 and 5.5.

**Round 2 anchors comparison:**
- Vv3PGcSn7c (5.50, Accept): Clean post-processing fairness, 2 tabular datasets, proper error bars. Our paper has broader scope but weaker statistical rigor → slightly weaker → ~5.0
- NEFldJX4zb (5.33, Accept): Debiasing w/ spurious correlations, thorough experiments. Comparable quality but our paper has framing issues → ~5.0
- L8pyycR4wW (5.50, Accept): Clean theoretical framing, good experiments. Our paper has weaker theory → ~5.0
- FL98GeTuwf (4.50, Reject): Strong theory but limited empirical (1 dataset). Our paper is stronger empirically → ~5.0
- GLlx240C5B (3.00, Reject): Low novelty, derivative. Our paper is much stronger → well above this

The paper is consistently above reject-level anchors (~3) and slightly below or comparable to solid Accept-level anchors (~5.33-5.50). I'll settle on 5.0.

Now writing the review.

## Final Review Structure

### Weaknesses to include:

**Major:**
1. Framing overclaim - paper frames "concept forgetting" as a new problem while acknowledging it's demographic parity. The contributions section says "introduce the framework" which overstates novelty.
2. Theorem 1 doesn't support the algorithm's primary claim of reducing concept violation - it only guarantees stability when violation is already low.
3. No error bars / confidence intervals for any experimental results despite stochastic elements.

**Minor:**
1. Computational cost of baselines not reported - makes efficiency comparison incomplete.
2. miniImageNet results (17% reduction) unexplained.
3. No "do nothing" baseline (fine-tuning on original labels without label annealing).
4. The "concept" for MNIST/CIFAR-10 is just forgetting a particular class - simpler than typical concept forgetting.

**Removed (with justification):**
- "Concept forgetting is exactly demographic parity" → paper acknowledges this. Keep as framing overclaim only.
- "Distinction from unlearning is trivially so" → paper makes a valid and useful distinction.
- "Anthropomorphic 'forget'" → style nitpick.
- "Feedback loop could converge to degenerate" → speculative, experiments show otherwise.
- Various others that are factually wrong or speculative.

Let me write this up now.Now I have all the evidence I need. Let me construct the final consolidated review.

## Summary

The paper introduces "concept forgetting" — making a pre-trained classifier's predictions independent of a specified categorical concept — and proposes the Label Annealing (LAN) algorithm. LAN iteratively reassigns labels within concept subgroups so that each subgroup's label distribution matches the model's own predicted class distribution, then fine-tunes on the pseudo-labels. Experiments across MNIST, CIFAR-10, miniImageNet, and CelebA with various architectures show LAN can substantially reduce concept violation (a total-variation variant of demographic parity) in as few as one epoch of fine-tuning, often outperforming fairness baselines on the accuracy–violation trade-off.

## Strengths

1. **Simple and efficient algorithm with strong empirical results.** LAN is conceptually clean: within each concept subgroup, sort by prediction confidence and reassign labels to match the overall predicted class distribution. Using just one epoch of fine-tuning, it reduces concept violation by 85% on MNIST, 73% on CIFAR-10, and 81% on CelebA binary concepts while maintaining high accuracy (Tables 1–2). The single-epoch efficiency is a genuine practical advantage over existing fairness methods that require many epochs to converge.

2. **Consistent outperformance over multiple fairness baselines.** The trade-off curves in Figure 3 span eight settings (varying datasets, architectures, and concepts) and consistently show LAN's curve below FERMI, Continuous-Fairness, and Fairness-KDE — meaning lower concept violation at the same accuracy level. This is not cherry-picked from one favorable setting.

3. **Broad evaluation scope.** Experiments cover diverse architectures (MLP, MobileNetV2, DenseNet-121, ResNet-50), both binary and multi-level concepts, and four image datasets. The CelebA multi-level concept experiments (Table 2, 63.52% violation reduction) convincingly extend beyond the binary case.

4. **Ablation on key hyperparameters.** Table 3 and Figure 4 examine learning rate sensitivity and iteration count (E=1,2,4), showing that the trade-off improves with more iterations. This gives practitioners actionable guidance.

## Weaknesses

### Major

- **Framing overclaim: the problem is demographic parity, not a new paradigm.** Definition 1 (concept neutrality) is exactly demographic parity, and Definition 2 is the total-variation distance form of the same. The paper explicitly acknowledges this connection in Section 2.1 ("forgetting a particular concept can also be interpreted as achieving independence between the model's prediction and the undesired feature we aim to forget") and cites Dwork et al. 2012, Lowy et al. 2021. Yet the contributions (page 2) state "We introduce the framework of concept forgetting from pre-trained classification models" as if it were a new problem space. The contrast with machine unlearning (Figure 1) is fair but does not justify calling the problem new — it only shows that unlearning is the wrong tool. A candid reframing as "an efficient post-hoc method for achieving demographic parity" would not diminish the algorithmic contribution but would eliminate the novelty inflation.

- **The theoretical guarantee does not explain why LAN reduces concept violation.** Theorem 1 bounds the accuracy loss of the forgotten model *if* the original model already has low concept violation. It is a stability guarantee ("fine-tuning on pseudo-labels won't hurt much if you start from a good place"), not a convergence guarantee. It says nothing about whether LAN reduces violation from a high initial value, which is precisely the setting the experiments address. The bound also scales linearly with the number of iterations E, yet empirically more iterations improve performance — the paper notes this mismatch without resolving it (Section 4.2: "while the upper bound degrades with E, as we show in experiments, the performance improves or remains the same with increasing E"). The paper would be stronger with an analysis of how the label-annealing subroutine drives violation down, or with an honest acknowledgment that the method is heuristic with an empirical justification.

- **No statistical significance reporting.** Tables 1, 2, and 3 report point estimates without standard deviations or confidence intervals. The algorithm involves randomness (stochastic gradient fine-tuning; implicit randomness from sorting ties). Single-run results could be noise. Given that several baselines in Figure 3 produce points that are close to LAN's curve (e.g., Figure 3g–h), confidence intervals would substantially strengthen the claims of superiority.

### Minor

- **Computational cost of baselines not reported.** The paper motivates LAN by arguing that fairness methods require many epochs (citing FERMI's O(1/ε⁴) iteration count), but does not report the actual number of epochs or wall-clock time used for each baseline in the experiments. Without this, the efficiency advantage is asserted rather than directly demonstrated. Running baselines at the same low epoch budget (e.g., 1 epoch) alongside their full-convergence results would cleanly separate the effect of the method from the effect of fewer gradient steps.

- **Unexplained weak result on miniImageNet.** Table 1 shows only 17.05% concept violation reduction on miniImageNet, far below the 73–85% on other datasets. The paper does not analyze why. This is worth a brief discussion: is the concept more entangled? Is the model harder to fine-tune? Readers evaluating the method for their own use would benefit from understanding the failure mode.

- **Missing "do nothing" control.** Fine-tuning the original model on the *original* labels for one epoch (without label annealing) would quantify how much of the violation reduction comes from label reassignment versus the fine-tuning procedure itself. This is a natural ablation that would isolate LAN's core mechanism.

- **Concept definition for MNIST/CIFAR-10 is a special case.** On MNIST, forgetting "digit-3" means the concept and the label are aligned (the concept value is identical to the class label). This is simpler than the general setting where concept and label are independent attributes (e.g., gender in CelebA while classifying attractiveness). The paper would benefit from explicitly noting this distinction.

### Trivial

None that survive filtering.

## Nice-to-Haves

- Report results as means ± std over multiple random seeds (3–5).
- Show trade-off curves for baselines under the same 1-epoch budget as LAN.
- Provide wall-clock times alongside the trade-off plots.
- Analyze the convergence behavior of the label-annealing subroutine theoretically or empirically (e.g., does violation decrease monotonically with iterations?).
- Run a control experiment: fine-tune on original labels for 1 epoch and report violation change.

## Removed Points

These points were raised by one of the input reviews but are removed or demoted for reasons noted:

- *"Concept forgetting is not a new problem — it is demographic parity under a different name"* → Partially kept, downgraded from "fatal structural issue" to a major framing overclaim. The paper itself acknowledges the connection to demographic parity (Section 2.1), so this is not a hidden flaw but an issue of framing.
- *"The contrast with machine unlearning is a straw-man"* → Removed. The paper makes a valid argument: unlearning removes *data points*, not *concepts* that appear in every example. This is a real distinction worth making, even if the conclusion (unlearning is the wrong tool) is unsurprising.
- *"'Forget' is anthropomorphic"* → Removed as a pure style nitpick.
- *"The algorithm could converge to a degenerate solution if the model is already confident"* → Removed. This is speculative and the experiments show LAN does reduce violation, so the concern does not materialize.
- *"Fairness baselines should be run for the same budget"* → Kept as a minor weakness (computational cost not reported) but reformulated: the paper's efficiency claim needs direct evidence.
- *"The feedback loop from using model predictions to define labels is a concern"* → Removed; it is a description of how the algorithm works, not a demonstrated problem.
- *"The related work section on unlearning is orthogonal"* → Removed. The distinction from unlearning helps scope the paper and is correctly argued.
- *"The third property (small time complexity) is not formalized"* → Removed; it is stated qualitatively as a design goal, which is standard for such papers.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface any observation about the method that the authors have not already stated or that would reshape how the contribution is understood.

## Suggestions

1. **Reframe the contribution.** Replace "introducing the framework of concept forgetting" with a more accurate statement: "We propose an efficient post-hoc method for achieving demographic parity (which we call concept forgetting) in pre-trained classifiers." This aligns the claimed novelty with the actual novelty (the LAN algorithm, not the problem definition).

2. **Address the theory–practice gap in Theorem 1.** Either (a) prove a bound showing that LAN reduces concept violation (not just that it preserves accuracy when violation is already low), or (b) explicitly state that LAN is an empirically motivated heuristic and frame the theorem as a safety/retention result.

3. **Add error bars.** Re-run experiments with 3–5 different random seeds and report mean ± std for both concept violation and accuracy.

4. **Add a "do nothing" control.** Report the concept violation after fine-tuning on original labels (no label annealing) for 1 epoch, to isolate the effect of the label redistribution.

5. **Report computational cost of baselines.** Include the number of epochs or wall-clock time for each baseline method, and consider a comparison where all methods are limited to the same small epoch budget.

---

## Score and Decision

**Bracketing (Round 1):** Weak anchors (2.0–3.0): post-hoc interpretability or shallow fairness analyses, rejected. Middle anchors (4.5–5.5): fairness post-processing and debiasing papers with solid experiments but scope limitations, mostly accepted as posters. Strong anchors (8.0): unrelated LLM-scale papers. Narrowed bracket: 4.5–5.5.

**Narrowing (Round 2):** Anchors inside bracket:
- Vv3PGcSn7c (5.50, Accept): Clean post-processing fairness, 2 tabular datasets, proper error bars. Our paper has broader empirical scope but weaker rigor → slightly weaker.
- NEFldJX4zb (5.33, Accept): Debiasing via distribution balancing with thorough experiments. Comparable quality; our paper has worse theory but a simpler algorithm → comparable.
- FL98GeTuwf (4.50, Reject): Strong theory, weak empirical (1 dataset). Our paper is empirically much stronger → above this.
- L8pyycR4wW (5.50, Accept): Clean theory, good experiments. Our paper has weaker theory → slightly weaker.

Consistent placement: 5.0 — stronger than clear rejects (4.5) but slightly below the cleanest poster-level accept papers (5.33–5.50) due to the framing overclaim and missing statistical rigor.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Accept</decision>