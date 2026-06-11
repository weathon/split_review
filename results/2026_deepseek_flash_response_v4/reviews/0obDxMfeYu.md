Based on my thorough analysis and calibration, here is my final consolidated review.

## Summary

This paper introduces Medix, a framework for OOD detection that uses unlabeled wild data via a two-stage pipeline: (1) filtering candidate outliers from mixed wild data using the element-wise median (EWM) of model gradients in a greedy leave-one-out procedure, and (2) training a binary OOD detector on the identified outliers plus labeled InD data. The paper provides theoretical error bounds (Theorems 4.1 and 4.2) that decompose misclassification into contamination, concentration, and separation effects, and reports state-of-the-art empirical results across 20 baselines on CIFAR-10 and CIFAR-100.

## Strengths

- **Provable two-sided error bounds for median-based filtering (Theorems 4.1 and 4.2).** The paper derives theoretical guarantees on both inlier and outlier misclassification rates that decompose into interpretable terms — contamination (controlled when π < 0.5), concentration (decaying as 1/√m), and separation (exponential in Δ²). This is a meaningful theoretical contribution given that few prior works provide formal guarantees for the in-the-wild OOD setting. The paper also provides an alternative bound under only bounded second moments (Theorem C.3), strengthening the robustness of the theoretical framework.

- **State-of-the-art empirical results across all evaluated settings (Tables 1 and 2).** Medix achieves the best average FPR95 and AUROC among all 20 baselines on both CIFAR-10 (average FPR95 0.80% vs. 3.40% for WOODS, 10.30% for KNN+) and CIFAR-100 (5.42% vs. 6.74% for WOODS, 46.40% for KNN+). Results are reported with standard deviations over 5 runs and show consistent superiority.

- **Empirical validation of the sub-Gaussian assumption used in the theory (Remark 4.3, Figures 4a/4b).** The paper provides histograms and Q-Q plots of InD gradient values showing bell-shaped, light-tailed behavior that supports the sub-Gaussian assumption in the theoretical bounds. The availability of a looser bound under bounded second moments provides additional rigor beyond a single distributional assumption.

- **Empirical motivation for the median-based formulation (Figure 1).** The clear monotonic increase in L2-norm deviation between the average InD gradient and the EWM of wild-data gradients as OOD samples are added provides direct grounding for the optimization problem and stopping criterion.

## Weaknesses

### Fatal
None.

### Major

1. **The computational cost of Algorithm 1 is not adequately addressed in the main text.** The paper acknowledges that solving the original optimization problem (Eq. 4) is "computationally prohibitive" and proposes Algorithm 1 as a greedy approximation. However, Algorithm 1 itself — which at each iteration computes the element-wise median of all remaining samples' gradients and evaluates the impact of removing each individual sample — has substantial computational cost at the dataset sizes used (≥25,000 wild samples). The main text defers all discussion of runtime to the appendix (Appendix A.6) without any indication of wall-clock time, optimization strategy, or even a brief complexity characterization. For a method whose core distinguishing component is the median-based filtering, omitting any feasibility discussion from the main text makes it difficult for readers to assess practical deployability. This does not invalidate the results (the experiments were clearly run), but it is a significant gap in presentation for a practical OOD detection method.

2. **The theoretical bounds are loose at the main experimental setting (π = 0.5), creating a gap between the paper's rhetoric and the theoretical guarantees.** At π = 0.5, the contamination term in Theorem 4.1 is π/[2(1-π)] = 0.5, meaning the theorem guarantees only that ERR_in ≤ 0.5 + small concentration terms — a near-chance level guarantee. Similarly, Theorem 4.2 gives ERR_out ≤ 0.5 + separation + concentration. The abstract claims that the theory "demonstrates Medix achieves a low error rate," but the bounds at the actual experimental setting are essentially vacuous. The empirical performance (e.g., 12.5% error in the synthetic experiment) is far better, which means the theory is not explaining the method's practical behavior at the parameter setting actually used. The structural decomposition of errors is still valuable, but the quantitative guarantees at π=0.5 are much weaker than the paper's framing suggests.

### Minor

1. **Theorem 4.1 defines ε = σ√(2 log(2d m_min)) but ε does not appear in the bound.** The parameter is introduced and then never referenced in the final inequality. This is confusing; the presentation should clarify the role of ε (likely used in the proof to derive concentration) or remove it from the theorem statement.

2. **The main evaluation protocol has P_out^test = P_out (the OOD test distribution is the same as the OOD distribution mixed into the wild data).** While the paper follows the same protocol as WOODS and defers an unseen-OOD experiment to the appendix (Appendix A.4), the main-text claims that Medix "outperforms existing methods across the board in open-world settings" do not qualify that the tested OOD distribution coincides with the one present in the wild data. This overstates the generality demonstrated in the main experiments.

3. **The claimed advantage of dataset-level mixing (vs. batch-level mixing in prior work) is not empirically validated in the main experiments.** The related work argues that Medix "enables dataset-level mixing without relying on batch-level structure," but the experiments follow the same wild-data construction protocol as WOODS and Du et al. (2024a). No experiment in the available text tests a scenario where batch composition is unstructured, so this claimed advantage remains a theoretical assertion without empirical support.

4. **The comparison with InD-only methods is not perfectly apples-to-apples.** Medix is trained on 25,000 labeled InD samples (half the CIFAR dataset), while InD-only baselines use the full 50,000 samples. The paper acknowledges this, but the effect on OOD detection metrics is not disentangled: a model trained on less InD data may be less confident on InD inputs, potentially making OOD detection easier. A controlled experiment with uniform data quantity would strengthen the comparison.

### Trivial
- The "40.98% improvement over KNN+" statistic in the introduction does not specify absolute vs. relative improvement (it is 40.98 percentage points absolute, or ~88.3% relative reduction).

## Nice-to-Haves
- Explaining the mechanistic reason why OOD gradients under pseudo-labels systematically differ from InD gradients would strengthen the motivation beyond the observed correlation in Figure 1.
- A more challenging synthetic experiment (e.g., partially overlapping inlier/outlier distributions) would better validate the method's robustness beyond the clear-separation proof-of-concept.

## Removed Points

These points from the inputs were removed as invalid, noise, or better placed elsewhere:

- **"Computational intractability is not acknowledged"** — Inaccurate; the paper explicitly says on line 93: "Solving the optimization problem in equation 4 can be computationally prohibitive... To address this, we propose a greedy approximation." The remaining valid concern (Algorithm 1's own cost not discussed in main text) is retained as Major Weakness 1.
- **"Missing hyperparameter sensitivity analysis"** — The paper states on line 238 that this is in Appendix A.2. The parser strips appendices from all papers; they exist in the original submission.
- **"Gradient filtering feels heuristic"** — The paper provides both empirical motivation (Figure 1) and theoretical analysis (Theorems 4.1, 4.2). Calling it purely heuristic ignores the theoretical framework.
- **"The synthetic experiment is too easy"** — The paper explicitly states "This simulation is designed to be simple to facilitate better understanding" (line 236). Downgraded to Nice-to-Have.
- **Strength: "Relaxation of the batch-level mixing assumption"** — Claimed as a strength by the Strength Finder but not empirically validated; repurposed as Minor Weakness 3 instead.

## Novel Insights

None beyond the paper's own contributions. The two reviews surface a useful tension: the median-based approach has intuitive appeal (robustness to contamination) and strong empirical results, but both the computational practicality of Algorithm 1 and the tightness of the theory at the operating π=0.5 setting create a gap between the paper's framing and what is actually supported. This is a pattern common to papers that introduce a theoretically-motivated heuristic: the theory explains the *structure* of errors but not the *magnitude* of success.

## Suggestions

1. Include a brief analysis of Algorithm 1's per-iteration cost and actual wall-clock time in the main text — even a single sentence summarizing the appendix's findings would help.
2. Qualify the theoretical bounds by explicitly discussing their tightness at π=0.5, or present the bounds at a more favorable π value alongside empirical misclassification rates for comparison.
3. Add a sentence in the main results section clarifying that P_out^test = P_out in the main experiments, and reference the unseen-OOD experiment in the appendix.
4. Run a controlled experiment where all methods use the same 25,000 InD samples to disentangle data quantity from method quality.

## Score and Decision

**Calibration report:**

All anchors retrieved:

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| 3ZdGSTxKuy (Harry Potter video OOD) | 2.00 | R1 | Much weaker — different topic, low-quality work |
| KK29oh8jZs (Synthetic OOD benchmarks) | 3.00 | R1 | Much weaker — narrow synthetic study |
| 6Z8rZlKpNT (Normalizing flows OOD) | 3.40 | R1 | Much weaker — post-hoc method without theory |
| rcKzU0Vns0 (Active learning + OOD) | 2.50 | R1 | Much weaker — different setting |
| l5ouuojPGe (Thresholding strategies) | 3.00 | R1 | Much weaker — niche topic |
| bcWwhF8cTZ (Gradient norm OOD error) | 5.50 | R1/R2 | Weaker — significant overlap with prior work (GradNorm), rejected |
| Cdhxv0Oz1v (Fisher info gradient OOD) | 4.20 | R1 | Weaker — limited empirical scope |
| RWZzGkFh3S (Outlier gradient analysis) | 4.50 | R1 | Clearer below — focuses on different problem (detrimental training samples) |
| zUrdd5NRLH (GROD) | 5.00 | R1 | Weaker — less comprehensive evaluation |
| **jlEjB8MVGa (SAL/Du et al. 2024a)** | **6.50** | **R1/R2** | **Most directly comparable — same setting, similar two-stage approach; Medix has stronger empirical scope but weaker presentation of computational cost** |
| MrslLZmkye (SEE-OoD) | 4.25 | R2 | Weaker — limited baselines, GAN-based approach |
| Go8hf9wKJx (DOG - diffusion outlier generation) | 4.25 | R2 | Weaker — different setting (surrogate outliers) |
| nUBLhhVM1l (Tight Rates outlier transfer) | 6.33 | R2 | Comparable — theoretical analysis of transfer, different setting |
| iriEqxFB4y (DOS - diverse outlier sampling) | 7.33 | R2 | Stronger — cleaner presentation, but different setting (clean auxiliary OOD) |
| Bo6GpQ3B9a (Out-of-domain unlabeled data) | 7.00 | R2 | Stronger — more polished theory, but different problem |

**Round 1 bracket:** 4.0 – 7.0 (between the clearly weaker papers below 3.5 and the strong-but-different-topic papers at 7.5+)

**Round 2 narrowing:** The key anchor is SAL/Du et al. 2024a (6.50), which addresses the identical problem setting with a different approach (top singular value vs median). Medix is slightly below SAL because (a) the computational cost of Algorithm 1 is not discussed in the main text, whereas SAL's top-singular-value computation is clearly efficient, and (b) the theoretical bounds at π=0.5 are weaker than the paper's rhetoric suggests. However, Medix has stronger empirical breadth (20 baselines) and a genuinely novel approach (median-based filtering). The lower-range anchors (4.25–5.50) are clearly below Medix in scope and contribution.

**Final score: 6.0** — A solid paper with a novel idea, compelling empirical results, and useful theoretical analysis. The main weaknesses (computational presentation gap, loose bounds at π=0.5, evaluation overlap) are real but fixable. Comparable in contribution to SAL (Du et al. 2024a, score 6.50) but slightly below due to presentation gaps in the main text.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>