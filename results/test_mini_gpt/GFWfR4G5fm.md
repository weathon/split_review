## Summary

The paper argues that static supervised causal learning (SCL) suffers under distribution shifts in graph structure, mechanisms, and noise, and proposes test-time training for SCL. Its concrete method, TACTIC, searches for sparse candidate graphs whose fitted mechanisms give high distributional alignment to the test dataset, generates a customized synthetic training set from those graphs, trains an SCL model, and predicts the test graph. The idea is timely and empirically promising, but the paper currently overstates the causal meaning of its likelihood-based alignment objective and leaves important details of the test-time optimization/evaluation protocol underspecified.

## Strengths

- **Clear empirical diagnosis of static SCL under controlled distribution shifts.** Section 3.1 defines shifts over graph type, mechanism, noise, and component-mixed combinations, and Figure 2 reports substantial AUROC drops relative to i.i.d. training, e.g. RFF\_G\_97.8 drops from 100 under i.i.d. to 42 under mechanism shift, and Chebyshev\_G\_62.3 drops from 93 to 64 under graph shift.

- **A concrete and natural test-time adaptation framework for SCL.** The paper moves beyond static pretraining by constructing a training set per test instance, which is a plausible response to the synthetic-to-real mismatch discussed in Section 3.

- **Strong reported empirical gains on several non-i.i.d. and real/pseudo-real settings.** In Table 2, TACTIC(Notears) is best on Linear\_U, Chebyshev\_G, Sachs, and Syntren, including 78.9 AUROC on Sachs versus 67.1 for PC, 62.3 for AVICI, and 61.8 for NOTEARS, and 80.1 on Syntren versus 65.4 for AVICI and 64.6 for RESIT. The paper also appropriately notes that AVICI remains best on RFF\_G.

- **Useful ablations of sparsity and the two-stage pipeline.** Table 3 shows that removing the sparsity penalty hurts performance, especially on Chebyshev\_G and Sachs, supporting the need for more than pure distributional fit. Table 4 separates seed graph, highest-score graph, and final SCL output, showing that the final SCL model changes and often improves upon the graph-search output.

- **Broad baseline coverage.** Table 2 compares against PC, GES, NOTEARS, RESIT, SCORE, NoGAM, and AVICI, which makes the empirical comparison more informative than a comparison only against prior SCL or only against traditional causal discovery methods.

## Weaknesses

### Fatal

None.

### Major

- **The AD objective is presented as causally meaningful, but as written it is only an observational predictive-likelihood criterion plus sparsity.** Equation (3) defines  
  \[
  AD(G^k_{\text{train}},D_{\text{test}})=\frac{1}{d}\sum_i \log p(X_i\mid f_i^k),
  \]
  where \(f_i^k\) is fitted from \(D_{\text{test}}\) using the candidate parents. The paper then states that this likelihood “simultaneously reflects structural correctness and mechanistic fidelity” and later that AD+sparsity ensures “causal similarity.” This is too strong. Observational conditional likelihood generally cannot distinguish Markov-equivalent DAGs, and flexible conditional models can prefer predictive but non-causal conditioning sets. The sparsity term in Eq. (5) helps prevent dense degeneracy but does not by itself solve orientation ambiguity or identify causal parents. This does not make TACTIC useless as a heuristic, but it substantially weakens the paper’s central causal interpretation.

- **The estimation of AD appears to fit and evaluate mechanisms on the same test data, with no stated protection against overfitting.** Section 4.1 says that for a candidate graph, the mechanisms are regressed “from the observed \(D_{\text{test}}\)” and Eq. (3) scores \(\log p(X_i\mid f_i^k)\). The paper does not specify a train/validation split, cross-fitting, mechanism complexity control, residual likelihood model, or held-out likelihood evaluation. Since this score drives graph refinement and training-data generation, overfitted mechanisms could be rewarded as “aligned” even when the graph is not causally close to the true graph.

- **The test-time hyperparameter and model-selection protocol is unclear, especially for single real datasets.** The method uses \(\lambda\), a SIM regression/likelihood model, stochastic refinement, initialization, and \(K=200\) generated graphs; only some of these are specified in the main text. For a test-time method evaluated on Sachs and Syntren, it is essential to know how \(\lambda\), the SIM class, search length/proposal settings, and any stopping criteria are chosen without access to ground-truth graphs. This matters because these are effectively test-time choices that can strongly affect the final graph.

- **The paper does not fully disentangle TACTIC from a score-based search plus post-processing.** Table 4 is useful, but the final model is trained on synthetic datasets labeled by the graphs found by the same stochastic search procedure. When the final SCL output substantially exceeds the best searched graph, e.g. Sachs 66.6 to 78.9 AUROC, the paper should better explain what additional causal information is introduced by the supervised phase. The current evidence shows improved benchmark AUROC, but not yet why the SCL stage should be interpreted as learning more accurate causal relationships rather than smoothing, ensembling, or biasing pseudo-labels generated by the score.

### Minor

- **The stochastic acceptance rule is underspecified and may be mathematically ill-defined as written.** Section 4.2 says candidates are “accepted with probability proportional to its score,” and Figure 3 gives  
  \[
  \alpha=\min[1, score(G^{k+1}_{train},D_{test})/score(G^k_{train},D_{test})].
  \]
  But Eq. (5) is a log-likelihood-like quantity minus an \(L_0\) penalty and can be negative, so a direct ratio is not generally a valid probability. If an exponential Metropolis rule or normalization is used, it should be stated clearly.

- **The likelihood model in Eq. (3) is not defined precisely enough.** The paper does not specify what \(p(X_i\mid f_i^k)\) is: whether residuals are Gaussian, whether variance is estimated, how roots are handled, what regression class is used for SIM, and how parent-set/model complexity is controlled beyond the edge-count penalty. These details are not cosmetic because they determine the behavior of the alignment score.

- **The strongest real-world framing is somewhat overclaimed relative to the evidence in Table 1.** Table 1 supports the narrower claim that strong synthetic performance does not guarantee real-data superiority: AVICI is excellent on RFF\_G but weaker on Sachs. However, AVICI is better than PC on Syntren, and Sachs is a single real dataset, so the paper should soften claims that static SCL broadly “collapses” or fundamentally lacks real-world applicability.

- **AUROC comparability across baselines needs clarification.** The paper reports AUROC as the headline metric for methods such as PC, GES, NOTEARS, RESIT, SCORE, NoGAM, AVICI, and TACTIC. Neural methods naturally output edge scores, but some traditional methods often output hard graphs unless internal scores or p-values are used. The paper should state exactly what continuous scores are used for each baseline; otherwise AUROC comparisons may mix probability outputs with binary outputs.

- **The default Gaussian noise used for forward sampling is not reconciled with the paper’s motivation around noise shifts.** Section 4.2 says the generated noise distribution is set to \(\mathcal{N}(0,1)\) by default, while Section 3 emphasizes noise shift as a major source of SCL degradation. If residual/noise distributions are fitted in AD but ignored during generation, this may reduce the intended test-distribution alignment.

### Trivial

None.

## Nice-to-Haves

- Include sensitivity analyses for \(\lambda\), number of refinement steps, \(K\), initialization, and SIM model class, especially on Sachs/Syntren-like settings.
- Add a comparison to stronger score-search post-processing baselines, such as posterior edge frequencies over sampled graphs, model averaging over high-score graphs, or returning a calibrated ensemble of searched graphs.
- Report runtime or computational cost for the full test-time procedure, since training a new SCL model per test instance is practically different from running PC, NOTEARS, or a pretrained AVICI model.
- Clarify the component-mixed construction in Section 3.1: exactly which graph/mechanism/noise combinations are withheld and whether marginal frequencies are matched.

## Removed Points

These points are flagged to be removed, treat them with caution.

- **Removed: availability/release concerns about AVICI or other cited models/tools.** The paper cites the relevant systems, and availability doubts should not be treated as author errors.

- **Removed: missing related work criticisms.** The final review does not introduce claims about absent citations because external related-work completeness cannot be verified from the extracted paper alone.

- **Removed: formatting, grammar, and typo issues.** The provided text is extracted from PDF, and formatting artifacts are not evaluated.

- **Removed: “missing appendix” concerns.** Several details are said to be in appendices, but the appendix is stripped in the provided extraction. I retained only issues that materially affect the main-method interpretation and are anchored in the main text, not criticisms based solely on appendix absence.

- **Removed/softened: the claim that Table 4 proves TACTIC “is not just” score-based causal discovery.** Table 4 does show a performance increase from the highest-score graph to the final SCL output, so it is a legitimate strength. However, I retained the narrower weakness that the causal source of this additional information is under-explained.

- **Removed/softened: requests for many more datasets as a decisive flaw.** The existing evaluation includes synthetic, real Sachs, and pseudo-real Syntren, plus reported appendix benchmarks. More datasets would help but are not by themselves a core rejection reason.

- **Removed: broad claims that the evaluation “lacks rigor” without a concrete anchor.** Only specific issues tied to Table 1, Table 2, Eq. (3), Eq. (5), and Figure 3 were retained.

## Novel Insights

The most important synthesis is that the paper’s empirical idea and its causal interpretation should be separated. TACTIC may be a useful test-time pseudo-labeling/adaptation method for SCL, and Tables 2–4 provide encouraging evidence for that pragmatic view. However, the current formulation presents AD as a causal-alignment metric, while its actual definition is closer to penalized predictive likelihood fitted on the test data. The paper would be much stronger if it either established assumptions under which AD+sparsity is causally identifying, or explicitly reframed TACTIC as an empirically effective test-time training heuristic rather than a principled causal-similarity objective.

## Suggestions

- Reframe the main claim: say AD is a tractable distributional/predictive alignment heuristic, not generally a causal-alignment guarantee, unless additional assumptions are provided.
- Define the likelihood model in Eq. (3) precisely: residual distribution, variance estimation, root-node likelihood, regression class, regularization, and whether scoring is in-sample or held-out.
- Use cross-fitting or held-out likelihood for AD: fit SIM mechanisms on one split of \(D_{\text{test}}\), evaluate on another, and report whether the gains persist.
- Add score-search baselines that do not train an SCL model: highest-score graph, sampled-edge-frequency graph, ensemble over high-score graphs, and calibrated posterior-like edge scores.
- Explain test-time hyperparameter selection without ground-truth graph labels; if defaults are used, show robustness.
- Specify AUROC scoring for every baseline, especially traditional methods that may output hard graphs.
- Fit or at least test residual/noise distributions for data generation rather than always using standard Gaussian noise, given the paper’s own emphasis on noise shift.

## Score and Decision

### Calibration

**Round-1 bracket.** I retrieved weak, middle, and strong anchors around causal discovery/SCL/distribution-shift papers. The weak anchors around score 3 tended to have unclear methods, poor rigor, or serious conceptual flaws. The strong anchors around score 8 had substantially stronger theoretical or empirical foundations and clearer assumptions. This paper is clearly stronger than the score-3 causal discovery anchors because it has a concrete method and meaningful empirical results, but it is well below the score-8 anchors because its central causal-alignment claim is not justified. After Round 1, my bracket was **5.0–6.0**.

**Round-2 narrowing.** The closest anchor is `/home/wg25r/split_review/datasets/deepreview_13k_calibration/ZXs3pkmrRG.md` (“Test-Time Learning of Causal Structure from Interventional Data”), avg 5.50, which is topically very similar: test-time SCL for causal structure learning with strong experiments but concerns about theoretical justification, algorithmic clarity, and whether the learned phase adds principled value. The present paper is comparable but somewhat weaker because its central AD objective is observational likelihood and is overclaimed as causal alignment. It is also comparable to `/home/wg25r/split_review/datasets/deepreview_13k_calibration/lQYi2zeDyh.md` at avg 5.00, which studied amortized causal discovery and identifiability with useful insights but limited scope and unresolved methodological concerns. Relative to these, I place this paper at **5.0**: promising and potentially valuable, but not yet sufficiently sound or clearly justified for acceptance.

### Retrieved anchor list and comparisons

- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/AvXrppAS2o.md`, avg 3.00, Round 1 — weaker than this paper; the reviewed paper has a clearer method and stronger empirical causal-discovery evaluation.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/JzFLBOFMZ2.md`, avg 3.20, Round 1 — weaker; that anchor had major conceptual/presentation issues, while this paper is more coherent and empirically grounded.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/fSxiromxAq.md`, avg 3.00, Round 1 — weaker; this paper has more substantial experiments and a clearer contribution.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/TRHyAnInUC.md`, avg 3.25, Round 1 — weaker; the present paper’s empirical case is more developed, though still methodologically incomplete.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/q07DDpu8Xb.md`, avg 5.25, Round 1 — similar range; both have causal identifiability/alignment ambitions with concerns about assumptions and rigor.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/lQYi2zeDyh.md`, avg 5.00, Round 1 and Round 2 — very similar; both address supervised/amortized causal discovery and distribution shift, with useful insights but unresolved identifiability/methodological limitations.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/pOoKI3ouv1.md`, avg 5.75, Round 1 — somewhat stronger theoretically, though less directly comparable empirically.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/22ywev7zMt.md`, avg 5.67, Round 1 — similar broad OOD/causal framing, but less topically close.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/Nx4PMtJ1ER.md`, avg 8.00, Round 1 — much stronger; it has clearer theoretical guarantees and more rigorous causal-discovery foundations.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/xByvdb3DCm.md`, avg 8.00, Round 1 — stronger; accepted-level causal discovery contribution with more principled modeling.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/k38Th3x4d9.md`, avg 8.00, Round 1 — stronger; better-supported method and application story.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/hrqNOxpItr.md`, avg 8.00, Round 1 — stronger overall theoretical contribution, though less topically close.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/iaP7yHRq1l.md`, avg 5.50, Round 2 — similar score range; that benchmark paper had extensive experiments but significant concerns about interpretation and setup, analogous to this paper’s AD interpretation issues.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/HBf6HFnpmH.md`, avg 5.50, Round 2 — similar broad empirical causal-evaluation contribution, with limitations in scope and conclusions.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/8GhwePP7vA.md`, avg 4.25, Round 2 — weaker; the present paper has more concrete causal-discovery experiments and stronger empirical evidence.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/ToveGL9vRN.md`, avg 5.50, Round 2 — similar; useful empirical causal-discovery analysis but overclaiming and insufficient theoretical support.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/yQUbpAHbIZ.md`, avg 6.00, Round 2 — somewhat stronger/more narrowly grounded methodologically.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/x3F8oPxKV2.md`, avg 6.25, Round 2 — stronger in novelty and clarity of task, though also limited by assumptions; this paper’s central objective is less justified.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/ZXs3pkmrRG.md`, avg 5.50, Round 2 — closest topical anchor; the present paper is slightly weaker because its observational likelihood alignment is more problematic as a causal criterion.

**Overall evaluation.** The paper is original and addresses an important weakness of static SCL. The empirical results are promising and potentially valuable to the causal discovery community. However, the claims are not yet well supported at the level advertised: the central AD score is not established as a causal-alignment measure, the in-sample/test-time optimization protocol is underspecified, and the added value of the final SCL phase over score-based pseudo-labeling needs cleaner controls. I therefore recommend rejection in its current form, but the direction is worth pursuing.

MY FINAL SCORE: <score>5.0</score>  
MY FINAL DECISION: <decision>Reject</decision>