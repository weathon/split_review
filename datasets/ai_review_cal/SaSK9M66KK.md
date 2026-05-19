- Decision: Reject
- Avg Score: 5.00
- Scores: 6, 6, 3, 5
Now I have all the facts verified directly from the paper. Let me produce the final consolidated review.

## Summary

This paper proposes "Pick and Adapt," an iterative approach for source-free domain adaptation (SFDA). The method is motivated by an empirical risk bound analysis that identifies population risk (due to pseudo-label noise) and domain drift (between pseudo-labeled and unlabeled target data) as key factors. To address these, the paper introduces (1) a top-k importance sampling strategy (I-sampling) that intersects classifier-confidence-based selection with target-class-center-based selection to purify pseudo-labels, and (2) a nearest-neighbor voting semantic alignment loss that aligns unlabeled target data to refined class centers. The two stages are iterated over multiple rounds. Experiments on Office-Home, DomainNet, and VisDA-C show competitive or state-of-the-art results against both UDA and SFDA baselines.

## Strengths

- **Consistent strong empirical results across three benchmarks.** The method achieves state-of-the-art or near-SOTA results on all three standard DA benchmarks. On DomainNet it surpasses the second-best SFDA baseline (GPUE) by 3.6% average accuracy (Table 2). On Office-Home it leads in 9 out of 12 domain tasks and exceeds the prior best SFDA method (C-SFDA) by 0.6% average (Table 1). On VisDA-C it is tied with the strongest baseline GPUE while outperforming others (Table 3).

- **The I-sampling (intersection of C-sampling and T-sampling) is a clean, well-motivated algorithmic idea.** It directly targets the pseudo-label quality issue identified in the theoretical motivation by requiring agreement between classifier confidence and proximity to estimated class centers. The ablation in Section 4.3 (Table 4) and the accuracy-trend analysis (Figure 3) provide empirical evidence that this intersection yields higher pseudo-label purity than either sampling alone.

- **Thorough ablation and diagnostic analysis.** Table 4 decomposes the contribution of each loss term (ℒ_CE, ℒ_SA, ℒ_IM) and shows that the full combination (78.2%) substantially outperforms any subset. Figure 3 tracks accuracy on different target subsets across training rounds, providing insight into how the progressive selection and alignment evolve. This level of diagnostic analysis helps validate that each component behaves as intended.

## Weaknesses

### Fatal
None.

### Major

- **The theoretical bound (Section 3.1) is presented as a formal analysis, but the transition from Theorem 3.1 to Equation 3 is not rigorous.** Theorem 3.1 relies on an i.i.d. sampling assumption for the labeled subset D_{t,l} (line 52–53). The paper then replaces D_{t,l} with the pseudo-labeled set D_{t,pl} (Equation 3) and adds a constant γ for pseudo-label noise. However, D_{t,pl} is not an i.i.d. sample from the target distribution — it is a selectively chosen subset via top-k importance sampling based on model predictions, which introduces selection bias. The added γ does not correct for this distributional mismatch, so the bound in Equation 3 does not follow from Theorem 3.1 as stated. **Why this matters:** The paper presents the theory as a main contribution ("We propose a theoretical analysis on target domain empirical risk bound for SFDA problem," line 21) and claims "clear guidance" from it. While the bound provides useful intuition, presenting it as a formal result that does not actually apply to the designed algorithm overstates the contribution. The authors should either (a) reframe the theory as conceptual motivation rather than a formal bound, or (b) account for the selection bias.

### Minor

- **No error bars or standard deviations reported despite 3 runs.** The evaluation section states "Each domain task is conducted independently 3 times and the average is reported" (line 194), but no variance measures (standard deviation or confidence intervals) are given. This makes small margins (e.g., 0.6% over C-SFDA on Office-Home, 0.0% vs GPUE on VisDA-C) difficult to interpret. The headline improvements on DomainNet (+3.6%) are large enough to withstand this concern, but the lack of variance reporting weakens the statistical rigor of the comparisons.

- **Several key hyperparameters are not reported in the main paper.** The method depends on: K (number of top samples per class), σ (percentage threshold for the reliable set used in center estimation), k (number of nearest neighbors), β (certainty threshold for the semantic alignment loss), and R (number of rounds). None of these are specified in the implementation details (lines 196–197), which harms reproducibility. While some of these may appear in a stripped appendix, their absence from the main text is a practical issue for readers.

- **The combination of existing techniques is incremental.** The individual components — confidence-based selection (C-sampling, similar to SHOT++), target-center-based selection (T-sampling, similar to ProxyMix), and nearest-neighbor label propagation (similar to NRC/AaD) — are well-established in the SFDA literature. The novel element is the intersection (I-sampling) and the iterative combination. The paper would benefit from a clearer discussion of what is specifically new versus what is a synthesis of existing ideas.

- **Incremental improvement over strong SFDA baselines on two of three benchmarks.** On Office-Home, the method improves over C-SFDA by only 0.6%; on VisDA-C it ties GPUE. Only DomainNet shows a large margin (+3.6%). This does not diminish the DomainNet result, but it tempers the claim of "consistently advantageous performance."

### Trivial

- **Symbol mismatch in Theorem 3.1:** The theorem states "with probability at least 1-p" but the bound expression uses log(2/δ), and δ is never defined (lines 56–60). The variable λ is defined as "classification error on D_l" but D_l is not the same as the later-used D_{t,pl} in Equation 3.

## Nice-to-Haves

- A failure analysis for domain pairs where the method underperforms (e.g., Pr→Ar on Office-Home where C-SFDA is better; lines 203–204) would strengthen the contribution by clarifying the method's limitations.
- A comparison of training time / computational cost against baselines (especially single-round vs. multi-round methods) would help assess practical applicability.

## Removed Points

These points were raised by the reviewers but are excluded from the main review for the following reasons:

- **"The large gain (3.6%) on DomainNet is suspicious"** — Speculative. No evidence is provided to question the result, and the paper reports standard evaluation protocols. Removed.
- **"UDA baselines underperforming SFDA baselines is atypical and suggests unfair tuning"** — This pattern is commonly observed in SFDA papers (SFDA methods can outperform UDA methods due to specialized target-domain training). No evidence of mistuning is provided. Removed.
- **"The ρ schedule notation is ambiguous"** — ρ = exp(ite/max_ite)^{-1} = exp(-ite/max_ite). The notation is unusual but unambiguous. Removed.
- **"Missing tasks for some baselines in Table 1"** — Common in DA papers where baselines only report on subsets, and the paper follows the standard protocol. Removed.
- **"Ablation table numbers not shown"** — Table 4 is an image that was parsed incompletely; this is a parser artifact, not a paper deficiency. Removed.
- **"Missing related works"** — Per policy, I cannot verify the existence or absence of related works. Removed.
- **"The certainty metric normalization could be unstable"** — Speculative concern without evidence of instability in practice. The paper's empirical results suggest the method works stably. Removed.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface an observation about the paper that the authors have not already made themselves.

## Suggestions

1. **Reframe the theoretical section explicitly as motivation/intuition** rather than presenting it as a formal bound that applies to the algorithm. Acknowledge the selection bias issue and either (a) correct the bound with a selection-bias correction term, or (b) clearly state that Equation 3 is a heuristic adaptation of the standard bound, not a theorem.
2. **Report standard deviations** for the 3-run results in Tables 1–3.
3. **Disclose all key hyperparameters** (K, σ, k, β, R) in the implementation section.
4. **Add an ablation explicitly comparing I-sampling vs. a simple concatenation of C- and T-sampling** (not just intersection) to demonstrate whether the intersection itself, rather than increased sample size, drives the improvement.
