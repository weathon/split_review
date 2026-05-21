---
job_id: 604a1df0-a6da-49aa-a997-fcffbbfced4d
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: YvMkU4BYOA.pdf
paper: XBIC: Shapley-Enhanced BIC for Accurate Causal Discovery in Discrete Bayesian Networks
main_score_norm: 0.2
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, specifically causal reasoning, probabilistic methods, and interpretable ML for structure learning in Bayesian networks.

## Minimum Quality
Pass ✅. The submission contains the core components expected of a research paper, including abstract, introduction, related work, method, experiments/results, and conclusion/limitations. While I have substantial concerns about methodological justification, experimental fairness, and clarity, these do not rise to the level of an immediate desk rejection from the paper text alone.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not detect hidden prompts, suspicious instructions to reviewers, or other obvious attempts to manipulate automated reviewing in the provided paper content.

# Expected Review Outcome:
## Summary
This paper proposes XBIC, a modification of the BIC score for discrete Bayesian network structure learning that uses aggregated SHAP values from per-node XGBoost classifiers to reduce the effective complexity penalty of edges that appear directionally supported. The method is implemented in a hill-climbing DAG search and evaluated on ten benchmark discrete Bayesian networks across seven sample-size regimes, with comparisons against hill-climbing BIC, PC, and a generalized-score GES variant. The main empirical claim is that XBIC improves oriented-edge recovery, especially in medium-to-larger networks and moderate-to-large sample regimes.

## Strengths
The paper tackles a real and well-motivated issue in score-based causal discovery for discrete data, namely the difficulty of orienting edges inside Markov-equivalent classes when likelihood-based scores alone are weakly informative. Framing the goal as improving orientation, rather than claiming full identifiability, is a sensible problem formulation.

The proposed mechanism is easy to understand at a high level and has practical appeal. In particular, the authors do not replace the score-based search pipeline wholesale, but instead propose a drop-in modification of the standard BIC penalty. That makes the idea potentially easy to test within existing Bayesian network toolchains.

Figure 1 is helpful in conveying the overall workflow. It clearly separates the three stages, classifier training, attribution aggregation, and hill-climbing search, and this supports the paper’s central claim that the method can be viewed as a front-loaded augmentation of a standard BIC pipeline rather than an entirely new discovery framework.

The empirical study is broader than a toy demonstration. Table 1 shows a reasonably diverse benchmark suite, from very small networks such as Asia and Survey to larger graphs such as Win95pts and Hepar2, with varied parameter counts and in-degrees. This breadth makes the evaluation more informative than a paper that only reports on a couple of tiny canonical networks.

The results do suggest that the method can improve directed-edge metrics in a number of settings. In Table 2, XBIC often yields positive \(F_1\) deltas relative to BIC and PC, especially on Alarm, Insurance, and several medium-to-large networks at moderate sample sizes. Figure 2 also gives a reasonably coherent picture of the intended precision-recall trade-off as \(w\) varies, where larger \(w\) tends to raise recall while occasionally lowering precision. That trend is at least directionally consistent with the design of Equation 2.

The paper is upfront that the method incurs extra computational cost and does not try to hide this. Table 5 makes clear that XBIC is much slower than plain BIC-HC and PC, which is important information for readers evaluating whether the gains are worth the overhead.

The paper also has some positive reproducibility signals. The algorithms are presented at a procedural level, the main hyperparameter sweep over \(w\) is disclosed, and code availability is stated.

## Weaknesses
1. **The core scoring modification in Equation 2 is heuristic, and the paper does not provide a convincing statistical justification for why SHAP magnitudes should divide the BIC complexity term.**  
   This is the central issue for me. In standard BIC, the penalty term arises from an asymptotic approximation to the marginal likelihood. In Equation 2 on Page 4, the penalty is replaced by
   \[
   \frac{\log N}{2}\frac{\dim(G)}{\exp(w\,\mathrm{SHAP}(G))},
   \]
   where \(\mathrm{SHAP}(G)=\sum_{(j\to i)\in E(G)} |\bar{\Phi}_{j\to i}|\) from Equation 3. This modification is not derived from any probabilistic model, marginal likelihood approximation, regularized objective, or Bayesian prior over graphs. It is a hand-crafted rescaling. That does not make it useless, but it matters because the paper repeatedly presents XBIC as a principled enhancement of BIC. Right now, it looks much closer to a heuristic score shaping term than to a BIC variant with established meaning. Without a clearer derivation or at least a stronger conceptual argument, it is hard to know when this adjustment is sensible versus when it may simply distort model selection.

2. **The claimed “consistency remark” is overstated and not established by the paper.**  
   On Page 5, the authors argue that because the modified penalty still scales like \(O(\log N)\) for fixed \(w\) and bounded \(\mathrm{SHAP}(G)\), “this preserves large-sample consistency.” That is much too quick. BIC consistency is not only about preserving the order of the penalty in \(N\), but about the specific asymptotic comparison between likelihood improvements and complexity costs under the model class and scoring criterion. Here, the multiplicative factor
   \[
   c(G)=\exp(-w\,\mathrm{SHAP}(G))
   \]
   depends on the candidate graph \(G\), and in practice it is estimated from learned predictive models rather than the generative BN itself. The paper does not show that this graph-dependent factor preserves the ranking needed for consistency, nor that the SHAP-based term converges to something compatible with the true DAG. A statement like “preserving \(O(\log N)\) growth” is not enough. This matters because the paper uses the language of preserving a core property of BIC without proving it.

3. **The directional signal extracted from SHAP is not clearly justified as causal or even orientation-specific evidence in the way the paper uses it.**  
   Equation 4 defines
   \[
   \bar{\Phi}_{j\to i}=\frac{1}{|S_i|}\sum_{n\in S_i}\phi_j^{(n)}(f_i).
   \]
   The argument in Section 3.2 is that if \(|\bar{\Phi}_{1\to 2}|\gg |\bar{\Phi}_{2\to 1}|\), then \(X_1\to X_2\) has stronger directional support. But SHAP values here are computed from discriminative predictors \(f_i: X_{\backslash i}\to X_i\), trained on all other variables. Those attributions reflect predictive usefulness under the chosen model and feature dependence assumptions, not necessarily causal direction. In a collider, confounder, or mediator pattern, predictive asymmetry can be influenced by variable cardinalities, class imbalance, redundant predictors, and model inductive bias. The paper states the intuition, but it does not adequately analyze when this intuition should be expected to hold for discrete Bayesian networks. Because this SHAP asymmetry is exactly what drives the score modification, the missing justification affects the scientific core of the submission.

4. **The use of absolute SHAP values in Equation 3 may discard information that is important for the claimed directional interpretation.**  
   The score uses
   \[
   \mathrm{SHAP}(G)=\sum_{(j\to i)\in E(G)} |\bar{\Phi}_{j\to i}|.
   \]
   Taking absolute values collapses positive and negative contributions into a single “strength” signal. For predictive explanation this is common, but for orientation it is not obvious that magnitude alone is what should modulate edge confidence. A feature could have large but unstable or class-dependent signed effects, or symmetric magnitudes in both directions, which would not necessarily support one orientation over another. The paper never discusses why \(|\bar{\Phi}_{j\to i}|\) is the right statistic rather than, for example, a signed, normalized, variance-aware, or pairwise contrastive quantity such as \(|\bar{\Phi}_{j\to i}|-|\bar{\Phi}_{i\to j}|\). This matters because the present definition rewards graphs for including edges with large predictive attribution, even if that attribution does not cleanly distinguish direction.

5. **The evaluation protocol disadvantages at least some baselines, especially PC, and likely inflates the reported directed-edge gains.**  
   On Page 6, the paper states that for baselines returning a PDAG, the authors “complete it to a DAG by randomly orienting undirected edges (while preserving acyclicity) before computing directed-edge metrics.” This is a problematic choice. PC is designed to output a CPDAG precisely because some directions are not identifiable from the data. Randomly orienting undirected edges converts principled uncertainty into arbitrary errors, and then the paper evaluates directed precision/recall/\(F_1\) against a fully directed ground truth. Unsurprisingly, this can make a method that always outputs a DAG look much better on orientation metrics, even if the comparison is not conceptually fair. At minimum, the paper should report CPDAG-aware metrics such as skeleton quality, SHD to the equivalence class, or orientation accuracy restricted to compelled edges. As written, the comparison to PC in Table 2 and Table 4 is not very informative scientifically.

6. **The baseline set is limited for the paper’s stated claim, and the positioning against existing discrete BN structure learning methods is incomplete.**  
   The paper compares to BIC-HC, PC, and one GES variant, but explicitly excludes MMHC on the grounds that it is “not the focus” (Page 6). That is not a persuasive reason to omit a standard hybrid baseline in discrete Bayesian network discovery, especially when the method’s advertised advantage is better orientation under practical search. Since XBIC itself is a hybrid-like construction, using predictive models and explanations to bias a score-based search, comparison to MMHC or other strong hybrid/search baselines would be highly relevant. Similarly, the related work section emphasizes that this is the first method of its exact kind, but there is little comparison against alternative score-based search enhancements for discrete BN learning. The paper may still have a useful idea, but the empirical case is weaker because the baseline panel is narrow.

7. **The reported gains are modest relative to the computational overhead, and the paper does not convincingly analyze the cost-benefit trade-off.**  
   Table 4 shows average absolute \(F_1\) improvements of only \(0.03\) to \(0.04\) over BIC for \(w=1,2\), while Table 5 shows runtime jumps from fractions of a second or a few seconds for BIC to tens, hundreds, or thousands of seconds for XBIC. For example, Asia goes from \(0.39\) seconds to \(74.78\) seconds, Survey from \(0.09\) to \(54.21\), and Win95pts from \(75.33\) to \(2139.27\). That is often two to three orders of magnitude slower for relatively modest absolute gains. The paper mentions that the added cost is “manageable for offline discovery,” but does not provide a more rigorous discussion of when this trade-off is favorable. This matters because practical adoption depends not only on whether there is a gain, but whether the gain is meaningful enough to justify the added pipeline complexity.

8. **Several important experimental details are underspecified or internally inconsistent, which makes it harder to trust the exact numbers.**  
   A concrete example is the hyperparameter search description on Page 6, which says Optuna uses an “RMSE objective” for per-target tuning. But the task is discrete classification, and Section 3.1 defines \(f_i\) as a classifier with class probabilities. RMSE is a strange choice here unless carefully motivated, and the paper does not explain how it is computed for multiclass outputs or why it is preferred over log-loss or classification error. Another issue is that the confidence threshold \(\tau\) is referred to as fixed and later varied in a sensitivity statement, but the exact default value is never clearly stated in the main text. In Algorithm 1, if \(|S_i|=0\), the definition on line 9 is incomplete; the return value for \(\bar{\Phi}^{(i)}\) in that case should be explicitly defined. These are not cosmetic problems, because the final score depends directly on the attribution aggregation pipeline.

9. **The results presentation is selective, and some tables make it difficult to assess whether the method is consistently better in a statistically meaningful sense.**  
   Table 2 only reports \(F_1\) deltas of XBIC relative to baselines, not the underlying absolute \(F_1\) values. This hides whether a delta like \(+0.05\) corresponds to a meaningful practical change or noise around low absolute scores. It also makes it difficult to judge robustness across datasets. Likewise, Table 4 aggregates across 700 runs into global average relative improvements, but averaging relative gains over very different networks and data regimes can obscure failures and instability. The paper does mention negative deltas for some settings, such as Asia, Survey, Child, Water, Win95pts, and Hepar2 in Table 2, but the narrative emphasizes consistency more strongly than the table supports. A clearer per-network absolute summary with confidence intervals would strengthen the empirical case.

10. **Figure-based evidence only partially supports the main story and also exposes instability that the paper does not discuss enough.**  
   Figure 2 is useful, but it cuts both ways. In Figure 2(a)-(c), recall generally increases with \(w\), consistent with the softer penalty in Equation 2. However, Figure 2(e) and especially Figure 2(f) show that precision can vary substantially and with wide uncertainty, particularly on Sachs at small sample sizes. That means the SHAP-guided weighting is not simply “adding directional information”; it is also changing the search bias in a way that may over-admit edges. This is not a fatal issue, but the paper should analyze where and why this happens. Similarly, Figure 3 is presented as evidence of SHD gains over GES, but without the corresponding absolute SHD values or the count of completed GES runs per setting, the practical significance is hard to interpret.

11. **The exposition is decent at the pipeline level, but some core causal distinctions are blurred.**  
   The introduction correctly notes that Markov-equivalent DAGs are hard to orient from observational data, but the method section sometimes slides into language suggesting that local SHAP asymmetries provide “directional evidence” in a stronger sense than the paper justifies. The distinction between predictive asymmetry, statistical asymmetry, and causal identifiability should be handled much more carefully. This matters because the contribution hinges on readers accepting that these attributions are meaningful inputs to a causal score, not just an arbitrary side signal.

## Questions
1. The most important issue is the statistical status of Equation 2. Can the authors provide a more rigorous derivation or at least a stronger justification for why dividing the BIC penalty by \(\exp(w\,\mathrm{SHAP}(G))\) is the right form? Why this exponential transformation, and why should the SHAP aggregate act on the penalty rather than as an additive prior or regularizer?

2. The consistency remark on Page 5 is currently too strong. Can the authors either substantially weaken the claim or provide a real argument showing that the graph-dependent factor \(c(G)=\exp(-w\,\mathrm{SHAP}(G))\) does not break BIC-style consistency? In particular, what assumptions are required on the learned SHAP quantities as \(N\to\infty\)?

3. Can the authors clarify the exact definition of the SHAP values used for multiclass XGBoost targets? Are these per-class SHAP values, SHAP values for the predicted class only, or some aggregation over classes? This affects Equation 4 materially.

4. What happens in Algorithm 1 when \(|S_i|=0\)? Please define the returned \(\bar{\Phi}_{j\to i}\) explicitly and explain how often this occurs in practice across the 700 runs.

5. Why is Optuna tuned with an RMSE objective for a classification task? Please specify the precise objective and justify it. If this is a typo, it should be corrected.

6. The current comparison to PC seems unfair for directed-edge metrics because undirected edges are randomly oriented before scoring. Could the authors provide CPDAG-aware metrics, or at least orientation accuracy only on compelled edges, to show that the gains are not an artifact of forcing PC into a fully directed graph?

7. Could the authors include absolute \(F_1\), precision, recall, and SHD values, not just deltas, for the main comparisons in Table 2 and Table 4? That would make it easier to assess practical significance.

8. Since Table 5 shows large runtime overhead, can the authors quantify the wall-clock impact of each stage separately, classifier training, SHAP computation, and hill-climbing, and report whether the quality gains persist under lighter-weight predictors or approximate SHAP?

9. A more informative ablation would compare at least: standard BIC, BIC plus a random edge-weight term, BIC plus non-SHAP feature importance, and the full SHAP-based version. Can the authors provide evidence that the gains specifically come from SHAP-derived directional information rather than from injecting any auxiliary asymmetry into the search?

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
No major ethics concerns are apparent from the paper itself. The work studies benchmark Bayesian networks and standard algorithmic evaluation. Any downstream use in domains such as healthcare would still require care, but that is not a direct ethics-review trigger for the present submission.

## Soundness Rating
2: fair. The idea is plausible as a heuristic and the experiments show some signal, but the central scoring modification is not well justified, the consistency claim is overstated, and parts of the evaluation protocol weaken confidence in the conclusions.

## Presentation Rating
2: fair. The paper is readable and Figure 1 helps, but several key mathematical and experimental details are underspecified, some claims are stronger than what is established, and the presentation of results via deltas alone obscures interpretation.

## Contribution Rating
2: fair. There is an interesting idea here, namely injecting attribution-derived asymmetry into a score-based discrete causal discovery pipeline, but the current execution and validation do not yet support a strong contribution at ICLR level.

## Overall Rating
2: Reject, not good enough. The paper contains a potentially interesting heuristic, but in its current form the method is not theoretically grounded enough, the empirical evaluation is not yet fair or complete enough, and the practical value relative to the large computational overhead is not convincingly established.

## Reviewer Confidence
4: confident. I am familiar with score-based causal discovery, Bayesian network structure learning, and attribution methods, and I checked the main equations, algorithmic choices, figures, and tables carefully.