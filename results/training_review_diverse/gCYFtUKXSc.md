Now I have enough information to construct the final consolidated review. Let me compile everything.

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

Let me write this now.

First, let me be clear about the paper type: It's a **new-method paper** proposing a library-based relearning framework for continual learning, with an information-bottleneck motivation and experimental validation.

Key decisions on what to keep/remove:

**Remove (to Removed Points):**
1. The reviewer's criticism that CLOM+c's held-out validation critique is "inconsistent" because the library also uses extra data. The paper correctly distinguishes between unseen held-out data (CLOM+c) and seen training data (library). This is a misunderstanding. → REMOVE
2. The "library size inconsistency" criticism (TinyImageNet 5% vs 10% for CIFAR). Keeping absolute |L_T| fixed at 5000 is a deliberate design choice, not an inconsistency. → REMOVE
3. The claim that "wrong learning" and "shortcut learning" are never defined — they ARE defined in the introduction (line 12). → REMOVE
4. The claim that the method is not clearly defined for non-task-ID methods — the paper does have a subsection and empirical results. The explanation is brief but it exists. → DOWNGRADE to minor
5. The demand for a toy analytical example — scope creep, move to Nice-to-Haves
6. The criticism about "OnPro" being absent from comparison — keep, as OnPro is cited as the only directly related shortcut-learning CL method. Not comparing to it is a valid weakness.
7. The "0.2pp on CIFAR10-5T" — I can't verify from text, and the Strength Finder mentions +5.4% on CIFAR100-20T, suggesting different comparisons. I'll keep the general point about modest gains but not cite specific numbers I can't verify.
8. The Strength Finder's claim about "theoretical justification" being empirically supported by Figure 1 — this is plausible but Figure 1 is from a single dataset/run. I'll keep as a qualified strength.

Let me finalize my structure now.Here is my consolidated final review after cross-checking every claim against the paper.

---

## Summary

This paper proposes a library-based relearning framework for continual learning (CL). It introduces a larger, unbiased "library" of past data (beyond the standard replay buffer) to detect and recover from shortcut learning. After training each new task, an active quiz on the library determines if relearning is needed; if so, a small subset of informative samples (selected via a transformed difficulty score) is used to update all task classifiers. The method is motivated by an information-bottleneck analysis and evaluated on CIFAR-10/100 and TinyImageNet under multiple task splits, showing consistent accuracy improvements over the CLOM baseline and across DER++ and BiC.

---

## Strengths

1. **Novel library-based relearning framework.** The idea of maintaining a larger, unbiased library (beyond the standard replay buffer) to detect forgotten information, combined with an active quiz that decides when to relearn, is a genuinely new architectural contribution to CL. It goes beyond simply increasing buffer size by introducing a principled mechanism for *detecting* when shortcut learning has occurred.

2. **Consistent improvement across multiple settings.** The relearning variant (CLOM+RL) improves over the strong CLOM baseline across all five dataset/split combinations (CIFAR10-5T, CIFAR100-10T, CIFAR100-20T, TinyImageNet-5T, TinyImageNet-10T). The paper notes that the gap widens as the number of tasks increases, suggesting the method is particularly beneficial in more complex CL scenarios.

3. **Orthogonal applicability to different baseline types.** Table 2 shows that library-based relearning improves not only the task-ID-based CLOM but also the non-task-ID methods DER++ and BiC. This demonstrates the method's generality beyond a single family of approaches.

4. **Empirical motivation in Figure 1.** The attention-map visualization (Figure 1a) and mutual-information curves (Figure 1b) provide direct, intuitive evidence that shortcut learning occurs in CL and that relearning can partially recover the compressed information. This grounds the method's motivation in observable behavior.

5. **Ablation on library size (Figure 5).** The paper investigates how library size interacts with the difficulty level of selected samples, finding that a moderate library (5000–10,000 samples) gives the best balance. This provides practical guidance for deploying the method.

---

## Weaknesses

### Fatal

None.

### Major

1. **OnPro is cited as directly related work but not compared.** The paper identifies OnPro (Wei et al., 2023) as "among the few attempts to address this issue within continual learning" (line 46) and distinguishes its own approach from OnPro's prototype-learning strategy. Yet OnPro does not appear in any experimental comparison. For a paper whose core claim is addressing shortcut learning in CL — and which explicitly names OnPro as the only other work in this niche — the absence of a direct comparison is a significant gap that weakens the claimed SOTA results.

2. **No variance or statistical significance reported.** Every result in Tables 1–3 and Figure 5 is reported as a single point without standard deviations, confidence intervals, or multiple-seed runs. Given that the improvement margins on some settings are modest, the reader cannot judge whether the gains are statistically reliable or within run-to-run noise. This is a basic expectation for experimental papers.

3. **Claims of "state-of-the-art" and "large margin" are insufficiently supported.** The abstract and conclusion claim SOTA performance and improvements "by a large margin," but: (a) the main comparison relies on baseline numbers from Kim et al. (2022a) and Lin et al. (2024) (2–4 years old); (b) the strongest variant adds library-based relearning on top of CLOM, which already used a held-out validation set — the paper itself calls this comparison "not fair" in CLOM+c's favor — making the claimed margin difficult to interpret; and (c) without variance estimates, the practical significance of the gains is unclear.

4. **Key design choices are not validated against simpler alternatives.** The sin-based difficulty-score transformation (Eq. 5, parameterized by c) and the quiz threshold (λ=100) are central to the method, but:
   - No ablation compares the sine transformation to baselines such as raw difficulty scores, uniform sampling, or capping.
   - No sensitivity analysis is provided for λ. The paper notes that always-relearning gives better accuracy (Table 3), meaning the quiz sacrifices performance for unmeasured computational savings — without any analysis of the accuracy-cost tradeoff.

5. **No measured computational cost.** The paper provides a complexity analysis (O(|L_t|×S), etc.) but reports no actual training times, FLOPs, or wall-clock comparisons to baselines. The claim of "comparable computational cost" is unverifiable, especially given the 700+100+100 epoch training schedule and the repeated forward passes over the library during scoring and quizzing.

### Minor

1. **Extension to non-task-ID methods is underspecified.** The subsection "Relearning for non-task-ID-based replay methods" is only two sentences. The difficulty score D_t^i depends on per-task logits (max over inter-task vs. intra-task), which do not naturally exist in single-head methods. How the selection and quiz mechanisms are adapted for DER++ and BiC is not described, though results are reported. This makes the generality claim harder to assess.

2. **Theoretical analysis is motivational, not a formal derivation.** The information-bottleneck discussion in Section 3 (Eqs. 1–4 in the reviewer's numbering) is a chain of intuitive reasoning rather than a rigorous statement with conditions and guarantees. The paper frames this as a contribution ("theoretical insight from an information bottleneck principle"), but no theorem is stated, no assumptions are formalized, and the step from "the buffer is small" to "the library is necessary" is not logically forced. The mutual-information curves in Figure 1b come from a single run on one dataset without error bars. This weakens but does not invalidate the paper — the main contribution is the method, and the theory is best viewed as a post-hoc motivation rather than a derivation that guided the design.

3. **Training budget comparison missing.** The method uses 700 epochs for feature extractor + 100 for classifier + 100 for relearning = 900 epochs per task (after task 2). The paper does not compare this to the training budgets of baselines, some of which may use far fewer epochs. This makes it hard to attribute gains to the library mechanism vs. simply more training.

4. **Table 2's experimental scope is unclear from the text.** The text does not specify which datasets are used in Table 2 — it only says "for all datasets" with m=500. The reader must infer the setting from the table image, and it is unclear whether results cover all five dataset splits or only a subset.

5. **"Wrong learning" vs. "shortcut learning" terminology is introduced but not systematically maintained.** The paper introduces "wrong learning" in the introduction (line 12) and then immediately uses "shortcut learning" as the primary term throughout. The relationship between the two is stated but not revisited, creating minor terminological confusion.

### Trivial

None that survive verification.

---

## Nice-to-Haves

- A toy analytical example (e.g., linear model with grouped features) that formally demonstrates when and why the library recovers information the replay buffer cannot — this would strengthen the theoretical motivation far more than the current informal MI discussion.
- Runtime or FLOPs measurements comparing the full pipeline (feature extractor + classifier + quiz + relearning) against baseline training.
- Sensitivity analysis on the quiz threshold λ across multiple datasets.
- Ablation comparing the sine-transformed difficulty score to simpler selection strategies (uniform, raw-score-based, hardest-only).

---

## Removed Points

These points were raised by reviewers but are not included in the main weaknesses above. They are listed here for transparency; treat with caution.

1. **"The critique of CLOM+c's held-out validation is inconsistent because the library also uses extra data."** — Removed. The paper correctly distinguishes between unseen held-out validation data (which CLOM+c uses) and seen training data (which the library stores). These are not equivalent, and the paper's criticism of CLOM+c is valid.

2. **"Library size inconsistency (TinyImageNet 5% vs. CIFAR 10%)."** — Removed. Keeping the absolute library size fixed at 5000 across datasets is a deliberate design choice, not an oversight. The percentages naturally differ because the datasets have different total sizes; this is not an inconsistency.

3. **"Wrong learning and shortcut learning are never clearly defined."** — Removed. Both are defined in the introduction (line 12). "Wrong learning" is described as learning features that work only on the current task, and "shortcut learning" (shown in Figure 1a) is given as an instance of this behavior.

4. **"The paper only speculates about shortcut learning being detrimental; the approach may not scale to more general CIL settings."** — This came from the human reviews (directory). The paper's evaluation covers CIFAR10, CIFAR100, and TinyImageNet with varied task counts, which is reasonable evidence of scalability for a CL paper.

5. **Strength Finder claims about "new state-of-the-art by large margins" are taken at face value.** — Filtered. The experimental evidence is qualified by the weaknesses above (missing variance, no comparison to OnPro, modest gains on some settings), so the paper's own SOTA claims cannot be accepted without stronger evidence.

---

## Novel Insights

None beyond the paper's own contributions.

---

## Suggestions

1. **Compare directly to OnPro** under identical protocols. Since OnPro is the only other method the paper identifies as targeting shortcut learning in CL, its absence from the experimental comparison is the single most addressable gap.
2. **Report means and standard deviations** over at least 3–5 random seeds for all main results. This is essential given the modest improvement margins on some settings.
3. **Calibrate the claims.** Replace "state-of-the-art" and "large margin" with specific, quantified statements (e.g., "outperforms CLOM by 1–5 percentage points depending on the setting") and note the practical significance.
4. **Validate the sine transformation** by ablating against at least two simpler baselines (e.g., raw difficulty scores, uniform sampling) to show the performance benefit of the specific design.
5. **Report actual training time or FLOPs** for the full pipeline vs. baseline CLOM to substantiate the claim of comparable computational cost.
6. **Clarify the non-task-ID adaptation.** Describe how the difficulty scores and quiz mechanism are computed for methods with a single classifier head (e.g., DER++).
7. **Add a sensitivity analysis** for the quiz threshold λ on at least one additional dataset beyond CIFAR10-5T.

---

## Score and Decision

The paper identifies a real problem (shortcut learning in CL) and proposes a novel, well-motivated solution (library-based relearning with active quiz). The core idea is sound and the consistent improvements across multiple datasets demonstrate genuine value. However, the current evaluation has significant gaps: a directly related method (OnPro) is cited but not compared; no statistical variance is reported; key design choices are not validated; the "large margin" / "SOTA" claims are overstated relative to the evidence provided; and computational costs are unmeasured. These issues are fixable with revision, but in its present form the paper does not meet the bar for acceptance.

**Score:** 5.0  
**Decision:** Reject

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>