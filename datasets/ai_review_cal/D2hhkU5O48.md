- Decision: Accept
- Avg Score: 6.75
- Scores: 8, 5, 6, 8
Now I have a complete understanding of the paper and can verify reviewer claims directly. Let me produce the consolidated review.

## Summary

This paper introduces β-calibration, a generalization of average-case calibration that conditions calibration guarantees on groups of question-answer pairs defined by a user-specified mapping β. The authors instantiate β via a kd-tree on DistilBERT embeddings, propose two post-hoc calibration algorithms (β-binning and scaling-β-binning), and prove a distribution-free, high-probability bound on the conditional β-calibration error for both algorithms. Experiments on five QA datasets with two LLMs and two elicitation prompts show that the proposed methods substantially reduce β-calibration error compared to standard post-hoc calibrators and are competitive on selective QA.

## Strengths

1. **Novel and well-motivated definition of β-calibration (Definition 3, §2.2).** The paper identifies a genuine limitation of average-case calibration for generative QA — that a user who only sees answers from one subgroup cannot rely on an average guarantee — and formalizes the remedy via conditioning on an arbitrary grouping function β. The running example (Table 1) cleanly illustrates why average calibration can be misleading at the group level. This is the paper's central conceptual contribution.

2. **Distribution-free theoretical guarantee (Theorem 1, §3.4).** The paper proves that both β-binning and scaling-β-binning achieve (ε, α)-conditional β-calibration with ε = √(log(2N/bα)/(2(b-1))) + ν, where ν captures label misspecification. The bound is non-asymptotic, holds for any data distribution, and explicitly connects the approximation level ε to the bin size b and misspecification ν — providing actionable guidance for hyperparameter selection (Figure 2).

3. **Consistent and substantial empirical improvement in β-calibration error.** Across all reported settings in Table 2, the proposed methods (BB, S-BB, HS-BB) achieve β-calibration errors far below all baselines. For example, on MMLU Verb1s-Top1 Mistral, CE(h;β) drops from 0.639 (None) to 0.149 (HS-BB), and the baselines that ignore groups (S-B, S, B) all lie between 0.258 and 0.393. The gap is large enough to be meaningful even without perfect baseline tuning.

4. **Practical instantiation of β via kd-tree on DistilBERT embeddings (§2.3).** The embed-then-bin approach to define β is concrete, computationally efficient, and principled. The observation that depth d=0 recovers standard calibration shows the framework cleanly generalizes existing practice. The use of a kd-tree provides adaptive partitioning that respects the geometry of the embedding space without requiring a fixed grid.

5. **Hierarchical scaling-β-binning (HS-BB, §3.2) as a technically sound solution to sparse partitions.** The use of hierarchical logistic regression with random intercepts and slopes per partition is a well-motivated design choice: it allows information sharing across groups through partial pooling, which is essential when the kd-tree produces fine-grained partitions with few data points. HS-BB is empirically the strongest variant, validating this design.

## Weaknesses

### Fatal
None.

### Major

1. **Hyperparameter tuning procedure creates an apples-to-oranges comparison on the primary metric.** The paper states (§5, Training) that hyperparameters (kd-tree depth *d*, bin size *b*, number of bins *B*) are selected to optimize AUAC, **not** the primary evaluation metric CE(h;β). The authors argue this is justified because "our schemes already aim to minimize CE(h;β)," but the concern is that the reported CE(h;β) values for the proposed methods come from model configurations not selected to minimize that metric, whereas baseline tuning procedures are not described at all. The paper does not explain whether baselines (Platt scaling, scaling-binning, UMD) were also tuned (and on which metric), leaving open the possibility that the large gaps in CE(h;β) reflect asymmetric tuning effort rather than algorithmic superiority. The authors should either (a) tune all methods on the same metric on a held-out validation split, or (b) clearly document the tuning procedure for every baseline and justify why tuning on AUAC does not disadvantage their methods on CE(h;β).

### Minor

2. **Gap between the theoretical guarantee (conditional) and the empirical evaluation (marginal).** Theorem 1 proves a bound on *conditional* β-calibration error (Definition 4), which requires the calibration gap to be small for *every* (group, bin) pair simultaneously. The experiments, however, evaluate only the *marginal* β-calibration error CE(h;β) (Definition 5), which averages over groups and bins. The paper's footnote on page 8 explicitly acknowledges that conditional calibration is stronger and notes the distinction, but it does not report any estimate of the conditional metric or discuss whether the stronger guarantee approximately holds in practice. Since the conditional guarantee is the paper's key theoretical contribution, some empirical evidence that it is meaningfully attained (or a clear explanation of why the marginal metric is the appropriate one for evaluation) would substantially tighten the paper's argument.

3. **Missing a simple group-wise baseline to isolate the effect of conditioning on groups.** The experiments compare only against methods that target *average-case* calibration (Platt scaling, UMD, scaling-binning). While it is expected that conditioning on groups improves group-conditional calibration error, the paper's claim that its specific algorithmic choices (hierarchical scaling, UMD-within-groups, kd-tree partitioning) drive the improvement would be strengthened by including a simple per-group baseline — e.g., per-group Platt scaling or per-group equal-width binning using the same kd-tree partition. Without this, the reader cannot tell whether the improvement comes from the *fact* of conditioning on groups or from the specific design of the proposed algorithms.

4. **Some methodological details are underspecified.** Specifically: (a) The hierarchical logistic regression model (§3.2) — is it fitted via maximum likelihood (e.g., with lme4 or statsmodels) or via Bayesian inference with specified priors? The paper does not state the fitting procedure or software package, making the method harder to reproduce. (b) The claim that the test-time fallback fraction (Algorithm 2) is "negligible" (line 234) is not quantified. A concrete number would be useful. (c) The text embedded for kd-tree construction is implied by the notation β_emb: Q×A → ℝ^768 to be the concatenated QA pair, but this is never explicitly stated.

### Trivial

5. The claim of "up to 30% increase in selective answering performance" (line 55) overstates the results in some settings — for example, on MMLU Ling1s-Top1 Mistral, the "None" baseline achieves AUAC = 0.269, identical to HS-BB's 0.269. The paper partially acknowledges this (line 373) but the abstract-level claim could be moderated.

## Nice-to-Haves

- Quantify the test-time fallback rate for points falling outside all kd-tree partitions (Algorithm 2), as suggested by the authors themselves when they describe the fraction as "negligible."
- Report reliability diagrams per group for a few example kd-tree partitions to visually illustrate the improvement.
- Reduce reliance on proxy labels from Llama 3.1 by including a small-scale human-annotated evaluation, since both the calibration evaluation and the hierarchical scaling step use the same proxy generation mechanism.
- Report training time for scaling-β-binning to help readers gauge practical feasibility.

## Removed Points

- **Hyperparameter tuning inconsistency as "fundamental mismatch":** The critic frames this as a fatal flaw. However, the paper's explanation — that the methods are *designed* to minimize CE(h;β) structurally (independent of hyperparameter choice), and that tuning on AUAC merely selects among configurations that are all good for CE(h;β) — is a reasonable justification. The real issue is the *undisclosed baseline tuning*, not a "fundamental mismatch." Downgraded from potential fatal to Major.

- **"Disconnect between theoretical guarantee and empirical evaluation" as a structural flaw:** The critic implies this gap undermines the paper's claims. But the paper's footnote (line 280) explicitly discusses the conditional vs. marginal distinction. The theoretical result proves the *stronger* conditional bound; reporting the marginal metric in experiments is conservative, not deceptive. The gap should be discussed, but it is not a "disconnect" that invalidates the theory. Downgraded from potential major to Minor.

- **Reproducibility concerns about kd-tree construction (embedding choice, tree depth, splitting criteria):** The paper specifies DistilBERT [CLS] embedding and states that maximum depth *d* is the key hyperparameter tuned via validation. Standard kd-trees use median splitting. The embedding of QA pairs follows straightforwardly from the notation β_emb: Q×A → ℝ^768. These details are sufficient for a competent practitioner to reimplement; the critic's request for "sensitivity analysis on alternative embeddings" is a nice-to-have, not a weakness. Removed.

- **Criticism about using the 20% split for kd-tree construction:** This is a deliberate design choice to avoid data leakage (the kd-tree is built before calibration training). This is standard practice, not a flaw. Removed.

- **Strawman about the kd-tree comment in Algorithm 1:** The critic says the comment about "points outside of bounded kd-tree spaces" is misplaced because training points are all inside the tree. The comment is indeed a forward reference to the test-time use case, but the algorithm is correct — the root-level fallback calibrator is constructed during training for use at test time. The presentation is clear enough; removing this.

- **Requirement for explicit ν estimation procedure:** The paper says ν can be "estimated empirically using a hold-out dataset" (line 310) and that this estimate guides the choice of *b* via the relationship in Figure 2 and Theorem 1. In experiments, they search over a range of ν ∈ [0, 0.05]. This is a standard and reasonable approach. Removed.

- **Strength Finder's generic strengths (e.g., "addressed an important problem," "the problem is timely and important"):** These are generic and not specific evidence of the paper's contribution. Removed.

## Novel Insights

None beyond the paper's own contributions. The review surfaces a genuine tension in the evaluation design (tuning on AUAC but evaluating on CE(h;β)) that is worth noting but is not a flaw in the core methodology.

## Suggestions

1. **Clarify baseline tuning procedures.** Document what hyperparameters, if any, were tuned for each baseline (Platt scaling, UMD, scaling-binning), what metric was used, and what search was performed. This is essential for fair comparison.

2. **Either tune all methods on CE(h;β) or present separate results.** If tuning on AUAC is retained, report CE(h;β) both for models selected on AUAC and for models selected on CE(h;β), or clearly state that the proposed methods' CE(h;β) is not harmed by tuning on a different metric and show that the main results are robust to the tuning criterion.

3. **Add a simple per-group baseline.** The easiest addition is per-group Platt scaling with the same kd-tree partition (fit a logistic regression per group, without hierarchy). This would directly show whether the hierarchy and UMD machinery adds value beyond just conditioning on groups.

4. **Report the conditional β-calibration error or discuss why it's not reported.** Even an approximate estimate (e.g., the maximum deviation across (group, bin) pairs) would help connect the theory to the experiments.

5. **Quantify the fallback fraction** for test points that fall outside all kd-tree partitions.
