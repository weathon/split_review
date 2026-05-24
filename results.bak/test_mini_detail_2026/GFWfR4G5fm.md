Now I have all the information needed. Let me write the final consolidated review.

## Summary

This paper identifies three limitations of static supervised causal learning (SCL) — fragility under distribution shifts, compositional generalization failure, and synthetic-to-real performance gap — and proposes a Test-Time Training framework (TTT-SCL) instantiated as TACTIC. TACTIC dynamically searches over candidate graphs using a likelihood-based Alignment of Distribution (AD) metric plus sparsity, generates training data aligned with each test instance, then trains an SCL model on that data. On the real-world Sachs dataset, TACTIC achieves 78.9 AUROC vs. 62.3 for the strong SCL baseline AVICI, and similar improvements hold across synthetic and pseudo-real benchmarks.

## Strengths

1. **Test-time training for SCL is a conceptually novel paradigm shift.** The paper convincingly argues that static pre-training with diversity is insufficient for real-world causal discovery, and proposes dynamically constructing training data per test instance. This reframing is well-motivated and clearly differentiates from prior SCL work (Sec. 1, Fig. 1).

2. **State-of-the-art results on real-world and pseudo-real data.** TACTIC (Notears) achieves 78.9 AUROC on Sachs vs. 62.3 for AVICI, and 80.1 vs. 65.4 on SynTReN (Table 2). These are substantial, unambiguous improvements on the most practically relevant benchmarks, directly supporting the central claim that test-time alignment improves real-world applicability.

3. **Careful ablation demonstrates the sparsity penalty is necessary.** Removing the sparsity term (Table 3) causes significant drops across all test settings (e.g., Chebyshev_G from 83.0 to 69.7, Sachs from 78.9 to 63.5). This cleanly shows that AD alone admits degenerate dense solutions, and the sparsity constraint is a genuine design contribution.

4. **Stage-wise analysis shows SCL adds value beyond search.** Table 4 shows consistent improvement from seed → highest-score graph → final SCL output (e.g., Sachs: 61.8 → 66.6 → 78.9). This cleanly demonstrates that TACTIC is not merely a score-based method in disguise.

5. **Robustness to seed quality.** TACTIC (random) still achieves strong performance (e.g., 88.4 on RFF_G, 72.0 on SynTReN, Table 2), showing the method does not critically depend on a good initialization.

## Weaknesses

### Major

1. **The AD metric implementation is underspecified.** The central technical step — how the mechanisms are regressed from test data given a candidate graph — is described only as "we regress the corresponding mechanisms from the observed D_test" via "Structure-Induced Mechanism (SIM)," with implementation details deferred to the (stripped) Appendix A. The AD formula (Eq. 3) uses `log p(X_i | f_i^k)` where `f_i^k` is "the fitting function," but the paper never states what regression method is used (linear? spline? neural network? Gaussian process?) or what noise/likelihood model is used during AD computation (as opposed to the N(0,1) used for generating training data, Sec. 4.2 step 3). This matters because the choice implicitly encodes assumptions about mechanism class; if a linear fit is used, the search may be biased toward linearizable graphs. The paper claims "many ways to implement AD" exist (Sec. 4.1), but the actual instantiation used for all reported results is needed for reproducibility and to assess assumptions. This is the single most actionable weakness — it is not a fatal flaw (the method clearly works empirically), but it must be clarified.

2. **The compositional generalization evidence is weaker than claimed.** The paper states SCL models "cannot handle novel combinations" as a "fundamental limitation," but the supporting evidence (Figure 2, "Component-mixed" vs. "i.i.d") shows modest drops (e.g., RFF_G 90→86, Linear_U 92→89). No variance or significance tests are reported for these comparisons. Moreover, the Mechanism shift condition causes far larger drops, suggesting that mechanism mismatch — not compositional failure per se — is the dominant failure mode. The paper would be strengthened by either (a) showing statistically significant compositional effects with proper error bars, or (b) reframing the motivation to center on mechanism mismatch and the synthetic-to-real gap (Issue 3), which the Sachs/SynTReN results support unequivocally.

3. **Potential overfitting through cyclic dependency is not discussed.** TACTIC uses the test data to (a) compute AD scores, (b) generate training data, and (c) evaluate the trained SCL model — all on the same test instance. The SCL model never sees data from a different distribution. While this is a valid test-time training design, the paper does not discuss the risk that the SCL model merely memorizes patterns that are specifically crafted for this test set. A control experiment — e.g., training on Sachs-aligned data and testing on a modified version of Sachs with altered mechanisms — would substantiate that the model learns transferable causal structure.

### Minor

1. **The exact acceptance rule for stochastic refinement is ambiguous in text.** The caption of Figure 3 shows `α = min[1, score(G_{k+1})/score(G_k)]`, which is a Metropolis-like acceptance criterion. The main text (Sec. 4.2) only says "accepted with probability proportional to its score," which is less precise. The acceptance rule should be stated explicitly in the body.

2. **Missing details about the SCL backbone architecture.** The paper uses the AVICI architecture as its SCL backbone but does not state whether it re-trains the same architecture or a smaller one, nor what hyperparameters are used. Since AVICI (scm-v0) was pretrained on up to 100-node graphs and TACTIC trains from scratch on only 200 instances, the architecture and training procedure should match what the AVICI authors used (or at least be specified).

3. **Unclear whether Table 4 improvement comes from SCL inductive bias or ensembling over K=200 graphs.** The stage-wise analysis compares the single highest-scoring graph against the final SCL output. However, the SCL model trains on all K=200 graphs, which gives it more information than a single graph. The improvement could partly come from ensembling over multiple candidates rather than solely from the SCL model's inductive bias. An ablation training an SCL model on 200 random graphs (same sparsity level) would disambiguate this.

### Trivial

- The number of test instances / trials for synthetic data (Table 2 standard deviations) is not reported.
- The number of stochastic refinement steps is not given; only the final number of training graphs K=200 is stated.
- The "highest-score graph" shows a *decrease* on Linear_U (82.0 → 80.1, Table 4), suggesting the search phase can sometimes degrade performance. A brief discussion would be helpful.

## Nice-to-Haves

- A runtime/scalability analysis for different graph sizes would help users assess applicability. The (stripped) Appendix F is said to contain this, but a brief note in the main text would be useful.
- Reporting F1 or SHD alongside AUROC in the main text (instead of deferring to Appendix D) would give a fuller picture, since AUROC on sparse graphs can be dominated by true negatives.
- The overfitting risk (Weakness #3) could be partially addressed by a cross-prediction experiment (train on Sachs-aligned data, predict on held-out Sachs subsets).

## Removed Points

- **"The AD metric is underspecified to the point of irreproducibility" (as a fatal flaw):** While the AD metric implementation details are indeed underspecified in the main text (I retain this as a Major weakness), calling it "fatal" or "structural" overstates the case. The core idea — regress mechanisms from test data under the candidate graph and compute likelihood — is clearly described; the missing details are the specific regression method and noise model, which are important for reproducibility but do not invalidate the method. The paper acknowledges "many ways to implement AD" (Sec. 4.1) and defers details to Appendix A. Since the appendix is stripped during parsing, the original submission likely contains these details. I downgraded this from the critic's "structural gap" to Major.
- **Criticism about AVICI comparison not being controlled (different architecture):** The paper likely uses the same AVICI architecture for TACTIC's SCL backbone if the publicly released code confirms this. The reviewer assumes a difference without evidence; the authors state "we mainly use AVICI as the model backbone" (Sec. 3.1). This removed point reflects speculation.
- **Criticism about variance overlapping in Table 3 (Chebyshev_G):** The claim that TACTIC(Notears) has std 8.7 and TACTIC(Notears-s) has 12.4, making a 83.0 vs 69.7 comparison "nearly overlapping" is mathematically incorrect. A one-sided overlap would require the intervals to cover each other's means; 69.7 + 12.4 = 82.1, which barely touches 83.0, and standard deviations are not confidence intervals. More importantly, all other datasets show large, unambiguous drops. Removed.
- **Strength Finder's generic strengths about "important problem" and "systematic experimental design":** These are true but generic; the real concrete strengths are captured above.
- **Strength about "validation across architectures and metrics" (Appendix C and D):** Confirming consistent results with a secondary backbone and additional metrics is a legitimate supporting strength, but it is a minor supporting point that does not need its own heading.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. In the main text, specify the exact regression method used for SIM (linear regression? additive noise regression with splines?) and the likelihood model used in AD computation. This is essential for reproducibility.
2. Soften the "fundamental limitation" claim about compositional generalization unless statistical significance is established with proper error bars.
3. Add a brief discussion of the overfitting risk and, if space permits, a simple control experiment where the TACTIC-generated training data is tested on a modified version of the same test set.
4. Explicitly state the Metropolis acceptance rule (`α = min[1, score(G_{k+1})/score(G_k)]`) in the body of Section 4.2, not just in the figure caption.
5. Add an ablation where the SCL model is trained on K=200 random graphs (same sparsity) to disambiguate whether the improvement in Table 4 comes from SCL inductive bias vs. access to multiple training candidates.

## Score and Decision

**Round 1 — Bracketing:** I queried three bands on topics similar to "supervised causal learning / test-time training / graph discovery." Weak anchors in the 2.0–3.33 range (foundation model approach for causal graph learning at 3.0, game-theoretic CD at 2.0, efficient differentiable causal order at 3.33) were clearly weaker than this paper — they had more fundamental methodological issues or far thinner experimental validation. Middle-band anchors (4.0–6.0) included a dynamic causal graphs paper (6.0, accepted poster) and ABCDEFG (4.0, reject). Strong-band anchors (7.5+) were on unrelated topics (multimodal reasoning, RL, text-to-3D). Initial bracket: **4.5 – 7.5**.

**Round 2 — Narrowing:** Inside the bracket, I compared against:
- **Dynamic Causal Graphs via PCE (avg 6.0, accept poster):** That paper had stronger theoretical analysis (identifiability proofs, convergence guarantees) but weaker empirics (single dataset, 9 variables). Our paper has the opposite profile — weaker theory/method specification but stronger empirics (multiple synthetic datasets + Sachs + SynTReN, multiple seeds). Comparable overall quality.
- **CausalFM (avg 6.67, accept poster):** That paper had strong theory (identifiability theorem, well-specified prior analysis) and thorough experiments. It is more polished and rigorous than our paper.
- **Specialization After Generalization / TTT Understanding (avg 6.8, accept poster):** Strong theoretical analysis of TTT but in a different domain (vision/language), making direct comparison difficult.
- **CausalAffect (avg 5.0, reject):** Fundamental causal identification issues; our paper is clearly better.

Against the 6.0 anchor (Dynamic Causal Graphs via PCE), this paper is slightly weaker due to the underspecification problem and weaker compositional generalization evidence, but the empirical validation is broader. Against the 6.67 anchor (CausalFM), this paper is weaker — CausalFM had clearer method specification and stronger theory.

Final score: **6.0**. This paper has a genuinely novel and well-motivated paradigm that delivers strong empirical results, but it is held back by the underspecified AD metric implementation and the overclaimed compositional generalization motivation — issues that are fixable but diminish the paper's polish relative to the 6.5+ tier.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>

### Calibration Anchors Summary

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| vSAWV43kvs.md (Foundation Model for Causal Graph Learning) | 3.00 | R1 | Significantly weaker — limited to linear SEMs, major generalization concerns |
| HfiRzzmFt8.md (ABCDEFG) | 4.00 | R1 | Weaker — novelty concerns, unclear practical applicability |
| 4bnCXOtHTm.md (Dynamic Causal Graphs via PCE) | 6.00 | R1+R2 | Similar quality — stronger theory, weaker empirics; our paper inverts this |
| d2L1ndOKjq.md (CausalFM) | 6.67 | R2 | Stronger — clearer method, strong theory, thorough experiments |
| PJ29BlwG7w.md (CausalAffect) | 5.00 | R2 | Weaker — causal identifiability issues in its framework |
| 1c6Ao3CpKt.md (TTT understanding) | 6.80 | R2 | Different domain, harder to directly compare |