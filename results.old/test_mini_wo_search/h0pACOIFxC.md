Now I have all the verification I need. Let me synthesize the authoritative final review.

---

## Summary

This paper proposes Meta-Adapters (instantiated as Meta-LoRA), a meta-learning objective for the intermediate retraining stage of foundation model pipelines. The core idea is to train base weights such that per-task low-rank adapters can easily fit each retraining task, thereby preparing the model for future fine-tuning. The authors provide theoretical analysis on linear models with symmetric low-rank structure, proving that standard retraining yields non-adaptable parameters while Meta-LoRA recovers optimally adaptable parameters (exactly for T≥3, with bounded error for T≥1). Synthetic linear experiments and RoBERTa experiments on ConvAI2 support the claims. The theoretical contribution is novel and substantive—particularly the finding that only T≥3 tasks suffice for exact recovery regardless of dimension or rank—while the empirical validation at the LLM scale is directionally correct but less rigorous.

## Strengths

- **Provable suboptimality of standard retraining for downstream adaptation (Theorem 1, Corollary 1).** The paper shows that standard retraining recovers parameters whose deviation from the ground truth has rank *kT*, so any LoRA adaptation of rank ≤ *kT* on an unseen task incurs strictly positive test loss. This is the first rigorous demonstration of a fundamental failure mode in the conventional two-phase pipeline.
- **Exact recovery guarantee with only T≥3 tasks (Theorem 3).** The proof that for T≥3 all global minima of the Meta-LoRA objective recover the ground truth parameters exactly (up to orthogonal symmetry) is a strong result that is weaker in its requirements than prior multi-task learning theory, which typically needs T > k or T > d.
- **Second-order stationarity implies global optimality for T=2 (Theorem 4).** Establishing that every SOSP of the Meta-LoRA objective is a global minimum provides a rigorous justification that local optimization methods can reliably minimize this non-convex objective without spurious local minima.
- **Synthetic linear experiments cleanly validate the theory across multiple dimensions (Figure 1).** The ablation over d, N, N′, and T confirms the theoretical predictions: Meta-LoRA outperforms SR+LoRA in every setting, and the T≥3 regime shows the predicted performance plateau, matching Theorem 3.
- **Clear, consistent gains on a real LLM benchmark (Table 1).** On ConvAI2 with RoBERTa-Large, Meta-LoRA-8 achieves 45.76% average accuracy vs. 41.52% for SR+LoRA at rank-8, and 47.48% vs. 39.57% at rank-16, demonstrating that the core insight transfers beyond linear models.

## Weaknesses

### Fatal

None.

### Major

- **Gap between symmetric-adapter theory and the general asymmetric formulation.** The theoretical analysis (Section 3) assumes *symmetric* adapters **U**_t**U**_t^⊤ during retraining, and the linear experiments match this. However, the general Meta-LoRA formulation (Equation 4, lines 82–85) uses *asymmetric* adapters **U**_**i**_^{(t)}**V**_**i**_^{(t)⊤}, and the LLM experiments do not specify which parameterization is used during retraining. The paper explicitly says "We use the Meta-LoRA loss but with symmetric low-rank adapters **U**_t**U**_t^⊤ for the t-th task in retraining" (line 144) and "We allow asymmetric adapters at test time," but it never discusses whether the theoretical guarantees (exact recovery, rank bounds) carry over to asymmetric adapters during retraining. Symmetric (PSD-constrained) and asymmetric (unconstrained) parameterizations have fundamentally different optimization landscapes and rank properties. The paper needs to either (a) provide an argument—even a heuristic one—for why the guarantees should transfer, (b) prove analogous results for asymmetric adapters, or (c) transparently acknowledge this gap and frame the LLM results as testing the *spirit* rather than the *letter* of the theory.

- **Insufficient statistical rigor and underspecified experimental setup in LLM experiments.** (i) Only 5 random trials are reported, and results are given as medians without any variance, confidence intervals, or significance tests (lines 306–307). With 5 trials and 10 test tasks, the observed ~4–8% improvements could be driven by outlier runs. (ii) The standard retraining (SR) baseline is underspecified: the paper does not state whether SR retrains all 355M parameters or uses LoRA adapters, what optimizer or learning rate is used, how many epochs, or what batch size. (iii) Since the retraining dataset averages only ~117 samples per task (~1170 total) for a 355M parameter model, the SR baseline faces severe overfitting risk that Meta-LoRA's per-task low-rank adapters naturally avoid—this confound is not discussed or controlled for. Adding a controlled baseline where SR uses the same per-task LoRA parameterization as Meta-LoRA (but with the standard objective) would isolate the effect of the meta-objective from the effect of reduced parameter capacity.

### Minor

- **Missing basic hyperparameters for LLM experiments.** The paper reports no learning rates, optimizer choice, batch size, LoRA alpha/scaling, number of epochs, or how rank 8 was selected for the ConvAI2 experiments. This harms reproducibility beyond the Table 1 results.
- **Theorem 4 (strict saddle property) is proven only for T=2.** While the paper acknowledges this limitation (line 261) and notes that GD works in practice for T>2, the strict saddle analysis does not extend to the more practical T≥3 regime, limiting its theoretical coverage.
- **Theorem 1 and Corollary 1 assume infinite noise-free samples.** The paper states "we assume access to infinite samples during the retraining process" (line 103). The practical implication that any rank ≤ *kT* adapter yields nonzero loss relies on this assumption; in finite-sample noisy settings the gap could be smaller. A brief acknowledgment of this would strengthen the narrative.

### Trivial

- The proof sketch of Theorem 3 states Lemma 1 (line 205) but the lemma's statement depends on the independence assumption (Remark 1, line 106–108) which is not restated in the lemma itself. Making this dependency explicit would improve clarity.

## Nice-to-Haves

- A training time or FLOPs comparison between Meta-LoRA and standard retraining would help practitioners assess the computational trade-off.
- Including a noise-free oracle (exact recovery under the theory) as a reference line in the synthetic experiment plots would directly illustrate the gap to the theoretical optimum.

## Removed Points

These points were raised by reviewers but are removed for the reasons stated below. Treat them with caution if re-evaluating.

- *"Missing related work on task diversity (Du et al. 2021, Collins et al. 2022)."* — According to the meta-instructions, missing related work citations are not flagged because external sources cannot be confirmed.
- *"Criticism that Theorem 4 has limited practical relevance because T=2 is too small."* — The paper explicitly acknowledges this limitation (line 261) and provides empirical evidence that GD works for T>2. The critic's framing adds no new information beyond what the paper already states.
- *"Speculation that asymmetric adapters are used in LLM experiments (not verified from paper)."* — The LLM experiments section does not specify symmetric vs. asymmetric adapters during retraining. The general formulation in eq. (4) is asymmetric, but the paper does not confirm that the LLM experiments used it. This goes beyond what is on the page.
- *"Speculation that SR baseline uses full 355M parameter fine-tuning."* — The paper does not specify the SR parameterization for LLM experiments. The critic's claim is an assumption, not a verified fact from the paper text.
- *"General concern about computational cost comparison."* — This is a nice-to-have, not a weakness of the core contribution.
- *"Generic strength about the paper addressing an important problem."* — Dropped per instruction to remove generic/unspecific strengths.

## Novel Insights

The most novel observation emerging from the reviews is that the paper's key theoretical result—exact recovery with only T≥3 tasks, independent of dimension d and rank k—is a genuinely non-trivial improvement over prior multi-task meta-learning bounds. The reviewers correctly note that the price of this strong result is the symmetric-adapter assumption, which creates a tension between theoretical tractability and practical implementation. No reviewer identified a fatal flaw in the theory itself; the concerns are concentrated on whether the empirical instantiation faithfully inherits the theoretical guarantees. This suggests the paper's weakest link is not the math but the bridge from the math to the experiments—a repair that is straightforward in principle (add a controlled LoRA-vs-LoRA baseline in LLM experiments, with confidence intervals and a discussion of the symmetric/asymmetric gap) but non-trivial in execution.

## Suggestions

1. **Address the symmetric/asymmetric gap directly in the paper.** Either provide a theoretical argument for why asymmetric adapters should inherit similar guarantees (or a conjecture with supporting intuition), or explicitly acknowledge the gap and frame the LLM results as a test of the general approach rather than a precise instantiation of the theory.
2. **Add a controlled LLM baseline where standard retraining also uses per-task LoRA adapters** (same parameterization as Meta-LoRA but with the standard additive objective). This isolates the effect of the meta-objective from the effect of reduced parameter capacity during retraining.
3. **Report per-task means with standard deviations or IQRs across the 5 trials**, and ideally a paired significance test (e.g., Wilcoxon signed-rank across the 10 tasks). This is standard practice for 5-repeat experiments.
4. **Disclose the hyperparameters used in LLM experiments**: optimizer, learning rate, batch size, LoRA alpha/scaling, number of epochs, and how rank 8 was chosen.

## Score and Decision

This paper makes a meaningful theoretical contribution that stands on its own. The synthetic experiments cleanly validate the theory. The LLM experiments are directionally correct but need stronger statistical reporting and a controlled baseline to fully substantiate the practical claims. None of the weaknesses are fatal; all are addressable in a rebuttal or minor revision.

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>