## Summary

VISTA proposes a modular framework for scaling causal structure learning: decompose the graph into Markov Blanket-centered subgraphs, learn each with an off-the-shelf base learner, aggregate via a weighted voting scheme (exponential decay penalty on low-support edges), and enforce acyclicity via a Feedback Arc Set heuristic. The method is model-agnostic, parallelizable, and comes with theoretical finite-sample error bounds and an asymptotic consistency claim. Experiments on synthetic (ER/SF graphs, 30–300 nodes) and real (Sachs) data with six base learners show consistent F1/SHD improvements and substantial runtime reductions (3–10×).

## Strengths

1. **Consistent empirical improvements across diverse base learners.** Table 1 demonstrates that VISTA-WV improves F1 and reduces FDR for all six tested base learners (NOTEARS, GOLEM, DAG-GNN, GraN-DAG, SCORE, CAM) on both ER and SF graphs. Improvements span both differentiable optimizers (NOTEARS, GOLEM, DAG-GNN, GraN-DAG) and combinatorial learners (SCORE). For example, GOLEM F1 from 0.35→0.60 on ER5; DAG-GNN from 0.33→0.59. This directly supports the model-agnostic claim.

2. **Substantial runtime reductions (3–10×) enabling larger-scale learning.** Table 3 shows NOTEARS dropping from 12,515s to 2,136s at n=300, DAG-GNN from 17,713s to 1,960s, and critically SCORE—which fails at n=300 standalone—completing in 225s with VISTA. These gains are a direct consequence of the divide-and-conquer design, not algorithm-specific acceleration.

3. **Clean, principled aggregation with explicit precision-recall control.** The weighted voting score (1−e^{−λm})·A/m is simple and interpretable. Theorem 3.4 gives an actionable interval for λ relating target error ε and threshold t. The paper uses a single fixed (λ=0.5, t=0.7) across all main experiments, avoiding cherry-picking. The exponential penalty on low-support edges successfully filters noise (FDR reductions of 50–80% relative to baselines).

4. **Coverage guarantee (Proposition 3.1) ensures the divide phase does not discard true edges.** Assuming correct MB identification, every true edge appears in the union of MB subgraphs. This provides a formal foundation: errors arise from imperfect local learning or aggregation, not the decomposition itself.

## Weaknesses

### Major

1. **The theoretical guarantees rely on an independence assumption that the paper itself acknowledges is violated in practice, creating a significant gap between claimed and actual rigor.** Theorem 3.2 models votes as independent Binomial trials (A ∼ Binomial(m, p)). The paper states (line 138) that "subgraphs learned from the same dataset can induce correlations among votes" and the bound should be "interpreted as a qualitative guide." Yet the abstract (line 9), introduction (lines 28–29), and conclusion (line 287) present these as rigorous theoretical guarantees without caveats. A theorem whose premise is conceded to be violated in the actual operating regime, and whose conclusion is described as a qualitative guide, does not constitute the guarantee the paper advertises. This gap between advertised and actual rigor is the paper's most significant weakness.

2. **The asymptotic consistency proof (Theorem 3.5) assumes m = C log n subgraphs per edge, but this quantity may not scale with n in the sparse graphs VISTA targets.** For an edge (X,Y), the number m of MB subgraphs containing both endpoints is bounded by the degrees of X and Y (their parents, children, and spouses). In sparse graphs with bounded average degree—precisely the regime where divide-and-conquer is most useful—this number does not grow unboundedly with n, making the premise of the asymptotic claim difficult to realize. (The deterministic finite-sample bounds via Theorem 3.2 are not affected by this issue.)

### Minor

3. **CAM is listed as a baseline (line 174) but never appears in any result table.** The paper names CAM among the benchmarked methods but no table reports CAM standalone or VISTA+CAM performance. This is an inconsistency that needs resolution.

4. **The MB solver used in all experiments is not specified.** The paper emphasizes MB-agnosticism as a feature, but for reproducibility, the specific MB estimator used in the reported experiments should be identified. Figure 1 references MB F1 scores without naming the solver; the main text only notes implementing "the MB solver used in that work" (line 174, referring to DCILP).

5. **On the Sachs real-data benchmark (Table 4), precision gains come at a substantial recall cost for most baselines.** GraN-DAG+VISTA achieves FDR=0.00 but TPR drops from 0.53 to 0.29; SCORE+VISTA TPR drops from 0.18 to 0.12; GOLEM+VISTA TPR drops from 0.26 to 0.18. Only DAG-GNN shows a TPR increase (0.12→0.18). The paper claims VISTA "consistently reduces false discoveries and improves structural accuracy" without adequately discussing this precision-recall trade-off.

6. **For the strongest baseline (NOTEARS on ER5, F1=0.76±0.24), VISTA-WV yields only +0.03 F1 gain (well within the baseline's wide error bar).** The headline improvement claim is better supported by weaker baselines where gains are larger (e.g., GOLEM +0.25, DAG-GNN +0.26). The paper would benefit from explicitly separating these regimes.

### Trivial

- Figure 4's λ sensitivity uses t=0.5 while main results use t=0.7, making the connection between the analysis and the reported operating point less direct.
- The number of independent experimental runs is not stated alongside reported standard deviations.

## Nice-to-Haves

- An ablation comparing FAS-before-filtering vs. filter-before-FAS to empirically justify the ordering design choice.
- A sensitivity analysis where MB identification is corrupted to varying degrees (noise injection into MB estimates) to demonstrate graceful degradation.
- Results on a larger real-world benchmark beyond Sachs (11 nodes) to substantiate the "large-scale" claim on real data.

## Removed Points

These points were raised in reviewer inputs but are excluded from the main weaknesses above, with justifications:

- **Criticism that NV is "catastrophically bad" (SHD=3171, F1=0.23):** Removed because the paper explicitly positions NV as a demonstration of the coverage/recall property, not as a standalone method. The text states NV "serves to demonstrate... every ground-truth causal edge must appear in the union of MB subgraphs." High recall (TPR=0.97) is the intended property.
- **DCILP comparison deferred to Appendix F.2:** Removed per hard rule. The parser strips appendices; the paper states this comparison exists in Appendix F.2. Cannot penalize for parser-stripped content.
- **Missing proof details in appendix:** Removed per hard rule (parser strips appendices).
- **Runtime serial vs. parallel distinction not clarified:** Weakened to a nice-to-have; the pseudocode is standard exposition and the paper states parallelizability.
- **NOTEARS performance discrepancy between normalized/unnormalized data:** Removed as a minor unexplained observation that does not affect the paper's core claims.
- **Strength about asymptotic consistency being "first theoretical result in its comparison set":** Removed as it conflicts with the verified weakness that the asymptotic claim's premise may not be realizable.
- **Generic strengths about importance of the problem:** Removed; these lack paper-specific grounding.

## Novel Insights

None beyond the paper's own contributions. The reviewer inputs surface no connections the paper itself misses.

## Suggestions

1. Reframe the theoretical contribution honestly: present the Binomial analysis as an idealized characterization providing qualitative guidance (analogous to ensemble method justifications under i.i.d. assumptions), and explicitly discuss when the independence approximation is reasonable.
2. For Theorem 3.5, discuss the realizability of m = C log n in sparse graphs, or re-derive the consistency result under a bounded-m setting with a different convergence argument.
3. Specify the MB solver used in all experiments and report its accuracy (beyond Figure 1's single curve) across different graph sizes and types.
4. Include CAM results in the main paper, or state why they are omitted.
5. Add a paragraph acknowledging the precision-recall trade-off observed on Sachs, qualifying the "improves accuracy without sacrificing recall" claim.
6. Report the number of independent runs alongside standard deviations.

## Score and Decision

**Calibration details:**
- **Round 1 bracket:** 4.5–6.5 (above the weak ~3.0 papers, below the strong 8.0 accepts).
- **Round 2 anchors:** Exact Distributed Structure-Learning (5.25, *slightly weaker* — narrower experiments); Causal Graph Learning via Distributional Invariance (5.00, *slightly weaker* — comparable theory gap but less comprehensive experiments); Two Time-Slices (6.33, *slightly stronger* — clearer theory but narrower scope); Causal Modelling Agents (6.25, *slightly stronger* — fewer theoretical concerns); Test-Time Learning (5.50, *comparable* — similar strengths/weaknesses profile).
- **Final placement:** The paper has broader experiments and a cleaner method than the 5.0–5.25 anchors, but the theoretical overclaiming is a more significant weakness than the issues in the 6.0+ anchors. Positioned at **5.5**.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>