Now let me do the calibration search.Round 1 bracket: **5.0 – 7.0**. The most relevant anchor is Du et al. (2024a) / SAL at 6.5, which is the direct predecessor work that Medix builds on. Let me narrow with Round 2.Now I have enough to write the complete review. The key calibration anchors are:
- Du et al. (2024a)/SAL at **6.5** (direct predecessor, introduced the framework)
- SPADE (OOD with EVT, theoretical): **5.5**
- ProMix (OOD with diverse auxiliary set, theoretical): **6.0**

---

## Summary

Medix is a two-stage OOD detection framework that filters candidate outliers from unlabeled "wild" (mixed InD/OOD) data using element-wise median (EWM) gradient deviation, then trains a binary OOD classifier on the extracted outliers following Du et al. (2024a)'s Stage 2 protocol. The paper provides finite-sample bounds on the inlier and outlier misclassification rates of the EWM filtering rule, and evaluates against 20 baselines across 11 InD-OOD pairs on CIFAR-10/100, outperforming WOODS by 2.60%/1.32% average FPR95 respectively.

---

## Strengths

- **Strong empirical results over a comprehensive baseline suite**: On CIFAR-10 Medix achieves an average FPR95 of 0.80% versus WOODS's 3.40% (Table 1); on CIFAR-100, 5.42% versus WOODS's 6.74% (Table 2). Results are averaged over five runs with standard deviations reported, and 20 baselines spanning both InD-only and wild-data methods are included. Individual OOD datasets show large improvements (e.g., PLACES365 FPR95 drops from 10.19% to 2.98% on CIFAR-10).

- **Finite-sample two-sided guarantees for EWM filtering**: Theorems 4.1 and 4.2 jointly bound both the inlier and outlier misclassification rates under sub-Gaussian gradient assumptions. The decomposition into contamination, concentration, and separation effects is clean and interpretable. Remark 4.3 also substantiates the sub-Gaussian assumption empirically via histograms and Q-Q plots.

- **Empirical validation of outlier extraction accuracy**: The 2D synthetic experiment in Figure 2 directly demonstrates 87.5% true OOD sample recovery (12.5% error rate), providing a concrete sanity check on the filtering stage's effectiveness beyond aggregate benchmark numbers.

- **Well-motivated gradient deviation criterion**: Figure 1's monotonic increase in L₂ deviation between the average InD gradient and EWM of wild gradients as OOD samples accumulate provides clear empirical motivation for the optimization objective in Eq. (4), distinguishing this from post-hoc design choices.

---

## Weaknesses

### Fatal
- None.

### Major

- **Missing ablation isolating Stage 1 (EWM filtering) contribution**: The paper explicitly states "For stage 2, we follow the protocol introduced by Du et al. (2024a)." The claimed novelty is Stage 1 (the EWM filter). However, there is no ablation that swaps out Du et al.'s Stage 1 (their thresholding filter) while holding Stage 2 fixed. The 1.32% FPR95 improvement over WOODS on CIFAR-100 and 2.60% on CIFAR-10 could plausibly arise from any combination of the filtering change and the different Stage 2 objective used. Without this comparison, the core claim—that median-based filtering is a demonstrably better approach to OOD candidate extraction—is not cleanly supported. This is the single most important evidential gap.

- **Theory covers a one-shot EWM filter, not the greedy iterative Algorithm 1**: Theorems 4.1 and 4.2 are stated for "the EWM filtering rule"—a one-shot thresholding on the element-wise median deviation. Algorithm 1 is an iterative, leave-one-out greedy procedure that removes top-k samples per iteration until convergence. The main paper never bridges this gap explicitly: it does not state that the greedy procedure provably inherits the one-shot bounds (up to some approximation error), nor does it frame Theorems 4.1/4.2 as applying to a simpler surrogate. Theoretical contribution C2 is one of the paper's three main contributions, and the mismatch between the proved guarantees and the deployed algorithm weakens it.

### Minor

- **Theoretical bounds are loose at the experimentally evaluated contamination ratio**: At the fixed value π = 0.5 used in all experiments, the contamination term in Theorem 4.1 equals π/[2(1−π)] = 0.5, so the bound certifies ERR_in ≤ 0.5 + concentration term—a bound that permits up to 50% inlier misclassification. The theorem is most informative at low π, but all evaluations use π = 0.5. The paper does not evaluate or discuss this regime mismatch, and no experiment sweeps π to show where the bound is actually tight or where performance degrades.

- **CONJ and DRL baselines excluded from main tables**: Section 5.1 names CONJ (Peng et al., 2024) and DRL (Zhang et al., 2024) as part of the competitive comparison, but they appear only in Appendix A.3. Including competitive recent baselines in the main comparison while reporting them only in the appendix understates what the paper is actually competing against.

- **Notation collision between ε in Algorithm 1 and Theorem 4.1**: Algorithm 1's convergence threshold ε and Theorem 4.1's tolerance ε = σ√(2log(2dm_min)) are different quantities sharing the same symbol. This creates confusion when reading the theoretical section and connecting it to the algorithm.

- **m_min undefined in Theorem 4.1 statement**: The bound involves m_min but does not define it within the theorem. From context it appears to be min(m_in, m_out), but this should be stated explicitly in the theorem.

### Trivial

- **Half-dataset discrepancy acknowledged but presentation is imprecise**: The paper correctly notes that methods not using wild data train on all 50,000 InD samples while Medix trains on 25,000, attributing the accuracy gap to this. The paper acknowledges this ("this slight difference can be attributed to…") but presents all methods in the same table without flagging the column for direct comparability. Adding a footnote or column label would clarify.

---

## Nice-to-Haves

- A main-paper result in the unseen OOD setting (P_out^test ≠ P_out^wild), which is currently in Appendix A.4. The abstract's "open-world" framing most directly implies this harder scenario; the main text should at least report the headline numbers for it.
- A sweep over π ∈ {0.1, 0.2, 0.3, 0.4, 0.5} to show where the method degrades and where the theoretical bounds become tight; this would convert a logical gap in the current paper into a positive empirical finding.
- A main-paper wall-clock runtime comparison with WOODS, since the leave-one-out EWM computation scales quadratically with wild-set size; Appendix A.6 exists but the main body should mention it.
- Formally proving (or clearly acknowledging) that Algorithm 1 inherits the one-shot EWM bounds up to an additional approximation error.

---

## Removed Points

*These points are flagged to be removed, treat them with caution.*

- **"Open-world framing is fundamentally misleading" (Harsh Critic, Critical Issue 1)**: Partially valid but demoted. The "same OOD distribution in wild training and test" design is the *standard evaluation protocol* adopted from WOODS (Katz-Samuels et al., 2022a), which the paper explicitly follows: "We use the same experimental protocol as Katz-Samuels et al. (2022a)." The harsh critic's framing this as uniquely problematic for Medix ignores that all wild-data OOD papers in the comparison (WOODS, OE, Energy+OE) operate under the same setup. Furthermore, the unseen-OOD setting IS evaluated in Appendix A.4. The concern is therefore not a structural flaw in Medix but a community-wide evaluation convention; it reduces to a Nice-to-Have (move A.4 results to main paper).

- **"OR vs AND stopping criterion is a bug" (Harsh Critic, Section-by-Section Notes)**: The OR condition in Algorithm 1 line 2 ("while t ≤ T or |δ_max| > ε") is not obviously a bug. It makes the loop run until *both* the maximum iteration count is exceeded *and* the convergence criterion is met—a stricter condition than AND. Whether this is intended is ambiguous, but the claim that "ε is meaningless" with OR is incorrect: the loop can terminate early if both conditions simultaneously fail. Removed because it is speculative.

- **"k can be 20,000 making this effectively one iteration" (Harsh Critic)**: The critic notes k ∈ {4k, 7k, 10k, 20k} with a ~25,000-sample wild set. Hyperparameter k is selected to maximize OOD performance (Section 5.2), not to guarantee multi-iteration behavior; the method implicitly adapts k to the dataset size. This is a speculative concern about edge-case behavior, not a demonstrated problem.

- **"Accuracy comparison is not directly comparable" (Harsh Critic)**: The paper already explicitly acknowledges and explains the half-dataset discrepancy. Demoted to Trivial (presentation note).

- **Generic strength about problem importance (Strength Finder)**: Removed per filtering instructions; kept only strengths with specific evidence.

---

## Novel Insights

The use of element-wise median of gradients—rather than score thresholds on activations or singular vectors—as the filtering criterion is a genuinely novel design choice in the OOD-with-wild-data literature. The theoretical result that the contamination term π/[2(1−π)] remains bounded for any π < 0.5 formalizes a clean robustness property of the median that does not hold for mean-based or top-singular-vector approaches. The demonstration (Figure 1) that the L₂ distance between average InD gradient and EWM of wild gradients is monotone in OOD contamination provides a foundation for the convergence criterion that is both empirically grounded and theoretically motivated. Together these constitute a coherent median-centric perspective that complements the separability-and-learnability lens of Du et al. (2024a).

---

## Suggestions

1. **Add the Stage 1 ablation to the main paper**: Fix Stage 2 to Du et al. (2024a)'s objective, then compare Du et al.'s thresholding Stage 1 versus Medix's EWM Stage 1. This single experiment would unambiguously establish the contribution.
2. **Move Appendix A.4 (unseen OOD) headline numbers to the main text**: Even a single table row for the unseen-OOD setting (P_out^test ≠ P_out^wild) would address the "open-world" framing.
3. **Clarify the theory-algorithm relationship**: Either add a proposition connecting the iterative Algorithm 1 to the one-shot EWM bounds, or add a sentence explicitly scoping the theorems to the one-shot variant and noting the algorithm as an efficient approximation.
4. **Define m_min inside Theorem 4.1's statement** and resolve the ε notation collision with Algorithm 1.
5. **Add CONJ and DRL to the main tables** or explicitly note in the main text that they are compared in Appendix A.3 with results.

---

## Score and Decision

**Calibration anchors (all rounds)**:

| Path | Avg Score | Round | Comparison |
|---|---|---|---|
| jlEjB8MVGa.md (Du et al. 2024a / SAL) | 6.50 | 1 | Direct predecessor; introduced the full framework. Medix improves Stage 1 but re-uses Stage 2 and same dataset protocol. |
| bcWwhF8cTZ.md (Gradient norm OOD) | 5.50 | 1 | Gradient-based OOD with theory; narrower contribution, rejected. |
| Cdhxv0Oz1v.md (GradRect OOD) | 4.20 | 1 | Gradient-based OOD detection; weaker theory, rejected. |
| RWZzGkFh3S.md (Outlier Gradient Analysis) | 4.50 | 1 | Gradient-based data pruning; empirical focus, rejected. |
| kwCHcaeHrf.md (SPADE / EVT OOD) | 5.50 | 2 | OOD with theoretical guarantees, accepted at 5.5. |
| voVjW1PT2c.md (ProMix) | 6.00 | 2 | OOD detection with auxiliary data and theory; rejected at 6.0. |
| zUrdd5NRLH.md (GROD) | 5.00 | 2 | OOD with PAC theory; weaker empirics, rejected. |
| Jds4tiTo2a.md (Diff-In) | 6.00 | 2 | Gradient-based influence estimation; similar quality range. |

**Round 1 bracket**: 5.0 – 7.0.

**Round 2 narrowing**: The most relevant comparison is Du et al. (2024a) at 6.5—the direct predecessor that introduced the exact framework Medix builds on. Medix's Stage 2 is *identical* to Du et al.'s and contributes a new Stage 1 with its own theory. Relative to Du et al.:
- Medix shows genuine empirical improvements, especially on CIFAR-10.
- The theoretical contribution is similar in style (finite-sample bounds on filtering errors) but covers a different (median-based) filter.
- However, the missing Stage 1 ablation means the core claim is not fully isolated, and the theory-algorithm gap (EWM one-shot bounds vs. greedy iterative Algorithm 1) leaves the theoretical C2 contribution under-supported.

Against ProMix (6.0, rejected) and SPADE (5.5, accepted), Medix has stronger empirics and broader evaluation but similar theoretical depth and clearer gaps. Medix is comparable to or slightly below Du et al.'s 6.5 because Du et al. introduced the full framework while Medix is an incremental improvement on the filtering stage, with real but incompletely supported contributions.

**Final score: 5.5** — the paper is a solid incremental contribution with genuine novelty in the median-based filter and strong empirics, but the missing Stage 1 ablation, the theory-algorithm gap, and the loose bounds at the tested contamination ratio together prevent it from rising to the level of Du et al.'s 6.5.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>