## Summary

The paper proposes the Aligned Scoring Rule (ASR), which extends the ElicitationGPT framework of Wu & Hartline (2024) by formulating a convex optimization problem (Program 2) over the space of separate proper scoring rules to minimize MSE against a reference score (instructor score or LLM-Judge). The key theoretical contribution is showing that this optimization is convex (Corollary 3.4), enabling global optimality with gradient descent. Experiments on a peer grading dataset across 22 assignments demonstrate that ASR substantially improves Pearson and Spearman correlation with reference scores over non-aligned baselines.

---

## Strengths

- **Convex formulation with properness guarantees**: Program 2 is a quadratic program over 6 variables per dimension, and Corollary 3.4 proves it is convex. This is verified directly in the paper: "Both our objective and constraints are convex in the variables." The result ensures global optimality and efficient optimization while provably preserving incentive alignment.

- **Sound properness inheritance**: The paper correctly inherits Theorems 3.2 and 3.3 from Wu & Hartline (2024) — properness under non-inverting QA oracle and adversarial robustness — and restricts its optimization to the space of separate scoring rules that preserve these guarantees. The theoretical architecture is clean and sound.

- **Negative/positive statement pair preprocessing**: Section 4.1 introduces a concrete improvement to the summarization oracle by pairing each statement with its semantic opposite before clustering. This prevents opposite sentiments from being conflated as different elicitation states, a genuine engineering contribution that improves robustness.

- **Empirically motivated "know-it-or-not" assumption**: Assumption 2.2 is justified by direct observation of the peer grading dataset ("In our peer grading dataset, we observe that textual reports either express a state being 0 or 1, or have no information"), grounding the ternary report space in actual data behavior rather than imposing it axiomatically.

- **Large alignment gains on Pearson/Spearman**: ASR achieves Pearson 0.717 vs. 0.294 for EGPT(AV) (Table 1a). While the MSE improvement is partially circular (see Weaknesses), the correlation gains are not directly optimized and represent genuine evidence of improved alignment.

---

## Weaknesses

### Fatal
None.

### Major

- **In-sample (circular) evaluation for the MSE metric**: Program 2 defines ASR as the minimizer of MSE against reference scores on the dataset. Table 1 then reports MSE between ASR and those same reference scores as the primary comparison metric. The paper never describes a train/test split or cross-validation protocol. Since ASR is defined to minimize MSE on the data, the reported MSE advantage over unoptimized baselines is partially tautological. The phrase "ASR aligns best with the reference on all metrics" is therefore circular for MSE. The nearly-identity linear fit in Figure 4 is also expected by construction under in-sample evaluation, as the OLS solution minimizing MSE will, by definition, lie on the regression target. Pearson and Spearman improvements (0.717 vs. 0.294) are more meaningful because they are not directly optimized, but they are still in-sample. The absence of any held-out validation prevents the reader from assessing whether the alignment generalizes.

- **No non-proper alignment baseline**: The only alignment-optimized method is ASR (which is also proper). The paper never compares against an unconstrained alignment baseline — e.g., linear regression or unconstrained MSE minimization over the QA features. Without this, the paper cannot answer its central design question: how much alignment quality is sacrificed by the properness constraint? A small gap would constitute a compelling "properness for near-free" result; a large gap would motivate further work. Either direction is informative; the current evaluation leaves this question entirely open.

### Minor

- **Overstatement of Instructor–LLM-Judge correlation**: Section 5.2 states that a Pearson correlation of 0.554 means the LLM-Judge score "can serve as a substitute for the costly and noisy instructor score." A correlation of 0.55 leaves substantial unexplained variance and is generally characterized as moderate, not as grounds for substitutability. The claim would be more defensible if framed as an alternative alignment target.

- **Spearman comparison methodological inconsistency (acknowledged but unresolved)**: Footnote 3 discloses that Spearman correlation is computed on individual reviews in this paper, while Wu & Hartline (2024) compute it on student-level averages. Since EGPT(AV/MV) were designed and validated for student-level scoring, evaluating them at the individual review level may understate their intended performance on ranking tasks. The Spearman comparison in Table 1 should be interpreted with this caveat.

### Trivial
None.

---

## Nice-to-Haves

- A leave-one-assignment-out cross-validation (or Class 1 / Class 2 split) would convert the in-sample demonstration into a generalization claim, substantially strengthening the empirical contribution.
- An ablation studying how many summary points *m* are needed, or how sensitive ASR is to the number of parameters vs. data points per assignment, would help practitioners calibrate the method's data requirements.
- A non-proper alignment baseline (unconstrained MSE minimization over the same QA features) would directly quantify the alignment cost of properness — the paper's most practically relevant open question.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **"EGPT baselines are not serious contenders in the alignment dimension"** (Harsh Critic): The critic argues the comparison is meaningless because EGPT(AV/MV) aren't optimized for alignment. However, the contribution of the paper *is* alignment optimization, and Wu & Hartline (2024)'s methods represent the prior state-of-the-art for proper textual scoring. Comparing against them is appropriate to show the contribution of alignment optimization. Removed as overstated.

- **"Dataset is too small for the number of parameters"** (Harsh Critic): The critic says the optimization has 6 variables per dimension × m dimensions on a small dataset, making overfitting likely. This concern partially overlaps with the in-sample evaluation concern already listed; as a separate parameter-count argument it is speculative without knowing m per assignment, so it is not elevated separately.

- **"Assumption 2.2 may fail in practice"** (Harsh Critic): The critic asks how many QA outputs fall outside {0,1,⊥}. However, the assumption is explicitly stated as an empirical observation of the dataset, and violating it is already discussed as reducing to approximate properness (ε-approximately proper, Definition 2.1). The concern is valid in principle but the paper addresses it implicitly; treating it as a major gap is an overreach.

- **Generic "near-identity linear fit adds no information beyond MSE"** (Harsh Critic): While true under in-sample evaluation, this is subsumed under the in-sample evaluation weakness above and does not warrant a separate listing.

- **Strength: "Strong evidence that the method successfully converts a non-proper reference into a truthful score that preserves preference ranking"** (Strength Finder): The evidence is qualified by the in-sample evaluation issue; the framing as "strong evidence" is overstated per the conflict rule.

---

## Novel Insights

The most genuinely novel aspect of the paper is the observation that optimizing *over* the space of proper scoring rules — rather than merely constructing one — is tractable as a convex program when restricted to separate (additively decomposable) scoring rules with ternary report spaces. The convexity depends critically on the know-it-or-not assumption, and the paper's implementation of negative/positive statement pairs as a preprocessing step to stabilize LLM clustering is a practical insight with broader applicability to the ElicitationGPT pipeline. The dual framing — ASR as a "proper proxy" that converts a non-proper (but aligned) reference score into a truthful mechanism — is conceptually clean and practically useful for peer grading systems.

---

## Suggestions

1. **Add cross-validation**: Implement leave-one-assignment-out evaluation, or hold out one class (Class 2) entirely and train on the other (Class 1). Report whether the MSE and correlation gains persist on held-out data.
2. **Add unconstrained alignment baseline**: Implement MSE minimization without properness constraints (e.g., ridge regression on QA features) and compare against ASR. Report the alignment gap due to the properness constraint.
3. **Soften the substitutability claim in Section 5.2**: Replace "serve as a substitute" with "serve as an alternative alignment target" for the LLM-Judge score at 0.554 correlation.
4. **Clarify Spearman evaluation**: Either compute student-level Spearman for all methods for a consistent comparison, or explicitly flag the individual-review evaluation as a different (stricter) metric than Wu & Hartline (2024)'s reported figure.

---

## Score and Decision

**Originality**: Moderate. The paper makes an incremental but clean extension of Wu & Hartline (2024) by adding an alignment optimization layer. The convex program formulation is a real contribution.

**Importance**: Moderate-to-high. Aligning proper scoring rules with human preference is a practically important problem for peer grading and beyond.

**Claims supported**: Moderate. The theoretical claims (convexity, properness) are well-supported. The empirical claim that ASR "outperforms prior methods in aligning with human preference" is weakened by the in-sample evaluation design.

**Soundness**: The theoretical framework is sound. The experimental protocol has a methodological gap (in-sample evaluation).

**Clarity**: Good. The paper is well-structured and the optimization formulation is clearly stated.

**Value to the research community**: Moderate. The method is practical and the peer grading use case is concrete, but the evaluation gap limits confidence in deployment recommendations.

---

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>

<subscores>
<originality>3</originality>
<importance>4</importance>
<claims_supported>2</claims_supported>
<soundness>3</soundness>
<clarity>4</clarity>
<community_value>3</community_value>
</subscores>