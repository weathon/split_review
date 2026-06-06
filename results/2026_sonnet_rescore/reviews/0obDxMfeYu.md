## Summary

Medix is a two-stage framework for OOD detection leveraging unlabeled "wild" data (an unlabeled mixture of InD and OOD samples). Stage 1 applies an iterative greedy algorithm based on the element-wise median (EWM) of model gradients to extract OOD candidates from the unlabeled wild mixture; Stage 2 trains a binary OOD detector on the filtered candidates and labeled InD data, following Du et al. (2024a). The paper derives finite-sample bounds on inlier and outlier misclassification rates and benchmarks Medix against 20 baselines on CIFAR-10/CIFAR-100.

---

## Strengths

- **Strong empirical results with replicated runs**: Table 1 shows Medix achieves average FPR95 of 0.80% vs. 3.40% for WOODS on CIFAR-10 — a substantial and clearly significant improvement. On CIFAR-100 (Table 2), average FPR95 is 5.42% vs. 6.74% for WOODS and 46.40% for KNN+. Results are averaged over five runs with standard deviations reported.

- **Two-sided theoretical guarantees under mild assumptions**: Theorems 4.1 and 4.2 jointly bound both the inlier misclassification rate (InD samples flagged as OOD) and the outlier misclassification rate (OOD samples retained as InD) under sub-Gaussian gradient assumptions, decomposing error into contamination, concentration, and separation effects. Remark 4.3 further provides empirical evidence via Q-Q plots that the sub-Gaussian assumption holds in practice.

- **Well-motivated algorithm design**: Figure 1 shows a clear, monotonic increase in L₂ deviation between the mean InD gradient and the EWM of wild gradients as more OOD samples are added, providing a principled empirical motivation for both the filtering objective and the convergence criterion.

- **Synthetic validation of filtering accuracy**: Figure 2 demonstrates that on a 2D Gaussian synthetic task, Algorithm 1 correctly flags 87.5% of true OOD samples, directly corroborating the theoretical bound with an error rate of 12.5%.

- **Coverage of unseen OOD setting**: Section 5.3 and Appendix A.4 explicitly address the harder $P_\mathrm{out}^\mathrm{test} \neq P_\mathrm{out}^\mathrm{wild}$ scenario, showing Medix outperforms baselines even under distribution mismatch.

---

## Weaknesses

### Fatal
None.

### Major

- **Missing direct comparison and ablation against Du et al. (2024a)**: The paper explicitly states "for Stage 2, we follow the protocol introduced by Du et al. (2024a)" (Section 3.2, line 61). The only claimed novelty is Stage 1 (the EWM filtering). However, Du et al. (2024a) as a complete end-to-end system (with their own Stage 1 thresholding + their Stage 2) does not appear in either Table 1 or Table 2, nor is an ablation run that substitutes Medix's Stage 1 with Du et al.'s thresholding while holding Stage 2 fixed. CONJ and DRL — the other more recent wild-data methods cited in Section 5.1 — appear only in Appendix A.3. The 1.32% FPR95 improvement over WOODS on CIFAR-100 is real but modest, and without isolating Stage 1's contribution from the choice of the Stage 2 objective (different from WOODS), the core claim that "median-based filtering is a better approach to OOD candidate extraction" is not fully substantiated. This is the single most important evidential gap.

### Minor

- **Theory covers one-shot EWM but algorithm is iterative-greedy**: Theorems 4.1 and 4.2 are stated for "the EWM filtering rule" — a one-shot threshold. Algorithm 1 is an iterative leave-one-out greedy procedure that removes top-$k$ samples per round. The main paper never explains how the iterative procedure inherits the one-shot EWM bounds, nor does it state that the theorems apply specifically to the simpler rule. Appendix C contains the proofs, but the gap between the theoretical object and the implemented algorithm is left unaddressed in the body. Even a one-paragraph bridge ("Algorithm 1 approximates the EWM threshold by…; the bound applies to the one-shot rule and serves as a reference") would help.

- **Contamination bound is weak at the experimental operating point**: At the experimentally fixed $\pi = 0.5$, the contamination term in Theorem 4.1 becomes $\pi / [2(1-\pi)] = 0.5$. The bound then reads ERR$_\mathrm{in} \leq 0.5 + \text{concentration term}$, which is loose relative to the empirically observed 12.5% error (Figure 2). The regime where the bound is most informative (small $\pi$) is precisely the regime not evaluated experimentally. A discussion acknowledging this loose-at-$\pi{=}0.5$ behavior, or an experimental sweep across $\pi$ values, would strengthen the connection between theory and experiment.

- **Algorithm 1 stopping criterion appears to have a logical bug**: Line 2 reads "**while** $t \leq T$ **or** $|\delta_\mathrm{max}| > \epsilon$ **do**". Under OR logic, the loop continues as long as at least one condition holds, meaning it will always run all $T$ iterations regardless of convergence, and will also continue past $T$ iterations if $|\delta_\mathrm{max}|$ remains large. The stated intent in Section 3.1 is that "the algorithm repeats until there is no significant drop in $\delta_i$ **or** a maximum number of iterations is reached" — i.e., stopping upon either convergence or time-out, which corresponds to "**while** $t \leq T$ **and** $|\delta_\mathrm{max}| > \epsilon$". The current OR condition makes the $\epsilon$ threshold essentially inoperative within the first $T$ iterations.

- **Unseen OOD evaluation relegated to appendix while abstract claims open-world performance**: The abstract states Medix "outperforms existing methods across the board in open-world settings." The main tables (Tables 1 and 2) evaluate with $P_\mathrm{out}^\mathrm{test} = P_\mathrm{out}^\mathrm{wild}$, which is also WOODS's protocol and is a legitimate benchmark — but the harder unseen-OOD setting ($P_\mathrm{out}^\mathrm{test} \neq P_\mathrm{out}^\mathrm{wild}$, Appendix A.4) is the scenario the "open-world" framing most naturally invokes. Including at least a summary row of those appendix results in the main text would better substantiate the paper's framing.

### Trivial

- **$m_\mathrm{min}$ undefined in Theorem 4.1**: The tolerance is set as $\epsilon = \sigma\sqrt{2\log(2dm_\mathrm{min})}$, but $m_\mathrm{min}$ is not defined in the theorem statement. From context it appears to be $\min(m_\mathrm{in}, m_\mathrm{out})$, but this should be stated explicitly.

---

## Nice-to-Haves

- **$\pi$ sensitivity sweep**: Run experiments at $\pi \in \{0.1, 0.2, 0.3, 0.4, 0.5\}$ to validate the theoretical monotonicity claim and to connect theory and experiment at values where the bound is tighter.
- **Wall-clock runtime in main body**: The leave-one-out computation is $O(|\mathcal{S}|^2 \cdot d)$ per iteration; a brief runtime comparison with WOODS in the main text (rather than solely Appendix A.6) is warranted given the method's added complexity.
- **$k$ selection analysis**: The largest $k$ candidate is 20k with a wild dataset of ~25k samples; clarifying behavior at extreme $k$ (near single-step removal) would complete the hyperparameter picture.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **"Medix's setup is structurally identical to OE"** (Harsh Critic): Removed. The critic argues that since Medix uses the same OOD distribution for wild training and test evaluation, it is essentially as strong an assumption as OE. This misreads the distinction: OE requires a *clean, labeled* auxiliary OOD dataset where every sample is known OOD. Medix operates on *unlabeled mixed* data with no identity labels. Testing on the same OOD distribution that appears in the wild mixture is the standard WOODS-style protocol, not an assumption equivalent to OE's labeled separation. The "open-world framing is misleading" claim was partially retained as a Minor weakness (unseen OOD in appendix), but the "structurally same as OE" characterization is incorrect.

- **"Du et al. (2024a) proved bounds on filtering error too, so the paper undersells the theoretical gap"**: Removed. No evidence from the accessible text supports this quantified claim. Treating it as real would require external verification.

- **"InD-only baselines are disadvantaged by 25k vs 50k training split"**: Removed. The paper explicitly acknowledges this (Section 5.3): "This slight difference can be attributed to the fact that our method is trained on 25,000 labeled InD samples, while baseline methods, which do not leverage wild data, use the full CIFAR-100 training set of 50,000 samples." The comparison is acknowledged and is an inherent consequence of constructing the wild mixture. The paper does not hide this asymmetry.

- **"Computational cost is O(|S|² · d) and not discussed in main body"**: Removed. Appendix A.6 covers computational efficiency; deferring implementation-level analysis to the appendix is standard practice and does not threaten the core claims.

- **"k=20k could reduce algorithm to a one-shot procedure"**: Removed as a standalone weakness. Hyperparameter selection from {4k, 7k, 10k, 20k} is discussed in Section 5.2. The possibility that a large $k$ makes the procedure nearly single-step is a valid implementation nuance (partially retained in Nice-to-Haves) but not a methodological flaw.

- **"Notation collision between ε in Theorem 4.1 and ε in Algorithm 1"**: Removed as a pure formatting nitpick; parseable from context.

- **Strength Finder — "Robustness to hyperparameters (Appendix A.2)"**: Removed from strengths. The supporting evidence is in the stripped appendix; cannot verify specifics. Mentioned as a supporting claim only.

---

## Novel Insights

The use of element-wise gradient median as an OOD separability criterion is the paper's most distinctive technical idea. The key empirical observation (Figure 1: L₂ deviation between mean InD gradient and EWM of wild gradients increases monotonically with OOD fraction) provides both algorithm motivation and a data-driven convergence criterion, unifying the optimization objective with a principled stopping rule. The theoretical decomposition into contamination, concentration, and separation effects is clean and offers a vocabulary for understanding when median-based filtering will or will not work — in particular, the separation condition in Theorem 4.2 ($\|\mu_\mathrm{out} - \bar\nabla_\mathrm{in}\|_2 \geq \Delta\sqrt{d}$) gives a concrete, checkable requirement on the gradient-space distinguishability of InD and OOD distributions.

---

## Suggestions

1. **Add Du et al. (2024a) as a standalone baseline in Tables 1/2**, or run the targeted ablation: Medix-Stage-1 + Du-Stage-2 vs. Du-Stage-1 + Du-Stage-2. This one comparison would definitively establish the value of EWM filtering over threshold-based filtering.
2. **Fix the stopping criterion in Algorithm 1** from "or" to "and" (or provide a justification for the OR logic if it is intentional).
3. **Promote the unseen-OOD result (Appendix A.4) to the main body**, at minimum as a table row alongside Tables 1/2, to substantiate the "open-world" framing in the abstract.
4. **Define $m_\mathrm{min}$ in Theorem 4.1** and clarify the relationship between the one-shot EWM theoretical object and Algorithm 1's iterative procedure in the main text (one paragraph suffices).
5. **Include a $\pi$-sweep experiment** or at least a discussion of how the bound behaves across $\pi$ values to connect the theoretical regime to the experimental regime.

---

## Score and Decision

**Originality**: The EWM-based gradient filtering in Stage 1 is a genuinely new mechanism for OOD candidate extraction. Stage 2 is adopted from Du et al. (2024a). Moderate originality overall.

**Importance**: OOD detection with unlabeled wild data is a practically significant problem; providing both theoretical guarantees and strong empirical baselines is valuable.

**Claims supported**: The empirical claims (Tables 1/2, Figure 2) are well-supported within the chosen experimental protocol. The theoretical-to-algorithmic gap and the missing Du et al. (2024a) ablation weaken the support for the core claim that Stage 1 is the source of improvement.

**Soundness**: The framework is methodologically sound. The stopping criterion bug in Algorithm 1 and the theory-algorithm gap are real, addressable issues rather than fundamental flaws.

**Clarity**: Mostly clear; CONJ and DRL's placement in the appendix while cited in Section 5.1 as baselines is awkward. The $m_\mathrm{min}$ definition and algorithm convergence logic need fixing.

**Community value**: 20-baseline comparison, theoretical analysis, and reproducible code provide value. The CIFAR-10 results are notably strong.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>

<subscores>
<originality>3</originality>
<importance>4</importance>
<claims_supported>3</claims_supported>
<soundness>3</soundness>
<clarity>3</clarity>
<community_value>4</community_value>
</subscores>