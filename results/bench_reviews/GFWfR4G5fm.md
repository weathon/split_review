Now I have all the information needed. Let me synthesize the final review.

## Summary

This paper identifies three fundamental limitations of static Supervised Causal Learning (SCL)—fragility to distribution shifts, failure in compositional generalization, and poor synthetic-to-real transfer—and proposes Test-Time Training for SCL (TTT-SCL), a paradigm shift that dynamically generates training data aligned with each test instance. The core insight is that distributional alignment between candidate graphs and test data can be captured via a proposed Alignment of Distribution (AD) metric, combined with a sparsity penalty. The TACTIC method instantiates this via stochastic graph refinement. Experiments show TACTIC significantly outperforms existing SCL and traditional causal discovery methods, with a 16.6-point AUROC gain over the best static SCL on the real-world Sachs dataset.

## Strengths

- **Compelling empirical demonstration of SCL limitations:** The factorial experimental design in Section 3 systematically isolates distribution shifts across graph structure, mechanism, and noise dimensions. The "Component-mixed" condition (Figure 2) provides a clean test of compositional generalization, revealing that SCL models memorize configurations rather than learning modular causal factors—a genuinely important finding for the field.
- **Creative paradigm shift with tractable operationalization:** The TTT-SCL framework represents a genuinely novel direction—moving from static, diversity-seeking pre-training to dynamic, test-time concentration. The AD metric (Eq. 3) provides a principled bridge between structural hypotheses and observable distributions via Structure-Induced Mechanism forward-sampling, making the idea operational.
- **Strong, well-validated empirical results:** TACTIC (Notears) achieves 78.9 AUROC on Sachs vs. 62.3 for AVICI (Table 2), 86.3 on Linear_U, and 83.0 on Chebyshev_G where pre-training collapses. The sparsity ablation (Table 3) and stage-wise analysis (Table 4) provide convincing evidence that both AD and sparsity are essential, and that the SCL training phase adds genuine value beyond score-based search alone.
- **Clear experimental hygiene:** The two-variant comparison (TACTIC random vs. TACTIC Notears) isolates the contribution of smart initialization. Consistent results across multiple metrics are noted and deferred to Appendix D, and results with alternative backbones are validated in Appendix C.

## Weaknesses

### Fatal

None.

### Major

- **Limited real-world evaluation in the main text:** The main empirical results rely on a single real dataset (Sachs) and one pseudo-real generator (SynTReN). While four additional bnlearn benchmarks are referenced as appearing in Appendix G, the core claim of real-world applicability would be substantially strengthened by including at least one additional real dataset in the main evaluation. This is the most significant gap between the paper's promise and its presented evidence.

### Minor

- **Underspecified mechanism fitting in the main text:** The AD metric (Eq. 3) depends critically on regressing mechanisms from test data via SIM, but the main text does not state what regression model class is used, how the likelihood \(p(X_i \mid f_i^k)\) is parameterized beyond the default Gaussian noise mentioned in Section 4.2, or how these choices vary across synthetic and real datasets. The appendix likely covers this, but the main text should summarize these design decisions since they are central to the method's validity.
- **AD metric robustness under noise-model mismatch not discussed:** The paper generates training data with Gaussian noise by default (Section 4.2), yet evaluates AD as a likelihood on test data that may have non-Gaussian noise (e.g., Uniform in the Linear_U setting). Whether and why AD remains a useful scoring function under this mismatch is not addressed, leaving open a question about the method's behavior on real data with unknown noise characteristics.
- **Hyperparameter and search-procedure details absent from main text:** The sparsity trade-off \(\lambda\) value, the proposal distribution for graph modifications, the DAG-enforcement mechanism, and the number of MCMC iterations are not specified in the main text. While \(K=200\) is given (Section 4.3), these remaining details are essential for understanding the method's practical behavior. Again, the appendix likely addresses this, but brief mention in the main text is warranted.

### Trivial

- The distinction between "diversity fails" and "compositional generalization fails" versus Montagna et al. (2024) is stated but could be more deeply argued in Section 5.
- The precise exclusion rules in the Component-mixed training setup could be made more explicit to strengthen the compositional generalization claim.

## Nice-to-Haves

- A discussion relating the AD + sparsity score to classical score-based objectives (e.g., BIC, BGe) would help readers situate TACTIC within the broader causal discovery landscape and clarify what SCL training adds beyond optimizing such a score.
- A deeper analysis or intuition for why training an SCL model on graphs from the search trajectory (stage 2→3 in Table 4) yields better predictions than simply taking the highest-scoring graph would strengthen the central claim about the value of the SCL phase.

## Removed Points

*These points are flagged to be removed, treat them with caution.*

- **"Under-specification of mechanism fitting" as a fatal issue (Harsh Critic Issue 1):** The harsh critic claimed the paper provides "no information" on regression models, noise distributions, etc. The appendix (stripped by the parser) very likely contains these details. Moved to Minor with the note that the main text should summarize them.
- **"Missing hyperparameter and search-procedure details" as a methodological gap (Harsh Critic Issue 2):** Same treatment—appendix likely covers these. Moved to Minor.
- **"Overcomes the OOD generalization problem" is imprecise (Harsh Critic):** The paper describes test-time adaptation, which is a reasonable way to address the problem. This is a semantic nitpick about word choice, not a substantive issue. Removed.
- **Strengths dropped from Strength Finder:** None—all five identified strengths are specific, evidence-backed, and verified against the paper.
- **Human Reviewer Finder weaknesses about unrelated topics** (e.g., T-Caus weaknesses about time-series modeling, incorrect claims about baselines—these are from different papers and do not apply).

## Novel Insights

The paper's most novel insight is that compositional generalization—the ability to recombine seen causal components (mechanisms, graph structures, noise types) into unseen configurations—is the true bottleneck for SCL, not merely insufficient diversity. This reframes the problem from "collect more training data" to "dynamically concentrate training data at test time," which is a fundamentally different solution strategy than prior work. The AD metric operationalizes this concentration elegantly by using the test data itself as the bridge between structural hypotheses and distributional alignment, creating a self-supervised signal at test time without requiring any pre-existing model of the test domain.

## Suggestions

- Move at least one bnlearn benchmark result from Appendix G into the main text to strengthen the real-world evidence.
- Add a brief paragraph in Section 4.1 summarizing the mechanism-fitting implementation (regression model class, likelihood parameterization) even if details remain in the appendix.
- Discuss the robustness of AD to noise-model mismatch, either through a brief analytical argument or a small additional experiment, as this directly affects confidence in real-world applicability.

Now, to position my score relative to the calibration anchors.

**Anchor comparison:**

- `/home/wg25r/review_agent/human_reviews_2026/ZZaIDVoWFA.md` (T-Caus, avg 3.50, Withdrawn): This paper had unclear contributions, incorrect claims, and unfair evaluation. The paper under review is substantially stronger—its contributions are clear, its claims are well-supported, and its evaluation is fair and thorough.
- `/home/wg25r/review_agent/human_reviews_2026/T29Oa85nzw.md` (CausalProfiler, avg 3.33, Reject): Incremental benchmark generator with overclaimed scope and presentation issues. The paper under review has a more novel contribution (a new method, not just a generator) and stronger empirical validation.
- `/home/wg25r/review_agent/human_reviews_2026/sAyus4Ljfn.md` (CausGNN, avg 3.00, Withdrawn): Unoriginal framing, missing baselines, marginal gains. The paper under review has genuinely original framing, comprehensive baselines, and large performance gains.
- `/home/wg25r/review_agent/human_reviews_2026/MtdrOCLAGY.md` (TCD-Arena, avg 4.50, Accept Poster): Thorough benchmark but fully synthetic, incremental contribution. The paper under review has both a novel method contribution and stronger real-world results.
- `/home/wg25r/review_agent/human_reviews_2026/uQzPkWvTyo.md` (CauSciBench, avg 5.00, Reject): Benchmark paper with evaluation metric issues and limited novelty. The paper under review is stronger—it proposes a method rather than just a benchmark, with clearer problem framing.
- `/home/wg25r/review_agent/human_reviews_2026/4XVczusV2K.md` (DiSCO, avg 5.50, Accept Poster): Novel MoE method for OOD graph learning with theory and strong experiments. Comparable quality level—both have novel methods, good experiments, and some presentation/analysis gaps.
- `/home/wg25r/review_agent/human_reviews_2026/sFjxg8cyJS.md` (When Shift Happens, avg 6.00, Accept Poster): Strong theoretical contribution explaining OOD paradox. The paper under review is more empirical but similarly strong in its domain. The theory in sFjxg8cyJS gives it a slight edge.
- `/home/wg25r/review_agent/human_reviews_2026/XOPH34Extq.md` (TabStruct, avg 7.00, Accept Oral): Exceptionally thorough benchmark with novel metrics and comprehensive evaluation. The paper under review is not at this level of thoroughness—the real-world evaluation is thinner and implementation details are less completely specified in the main text.

The paper under review is clearly above the ~3.0–4.5 band, comparable to the 5.5 accept, and somewhat below the 7.0 oral. I place it at 6.0: it has a genuinely novel idea, strong problem motivation, convincing empirical results, and clean ablation studies. The main weaknesses (limited real-world data in main text, underspecified details) are addressable and do not undermine the core claims.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>