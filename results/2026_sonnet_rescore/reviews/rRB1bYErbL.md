Now let me write the consolidated meta-review based on a careful reading of the paper.

---

## Summary

R-HORIZON proposes a query composition method that links single-horizon reasoning problems into sequential, interdependent chains to evaluate and train Large Reasoning Models (LRMs) on long-horizon tasks. The paper contributes (1) a benchmark evaluating 26 LRMs across 6 datasets that reveals consistent performance degradation as reasoning horizons grow, and (2) a training method using composed-query RLVR that improves both multi-horizon and standard (single-problem) performance, with notable gains on AIME24 (+7.5 absolute for standard, +17.4 for composed).

---

## Strengths

- **Large-scale evaluation demonstrating consistent performance collapse**: Figure 3 shows that across all 26 models, all six datasets, and multiple n values, performance monotonically degrades as the number of composed queries grows. The degradation is not marginal — e.g., DeepSeek-R1 drops from 87.3% (n=1) to 24.6% (n=5) on AIME25. This is a genuine empirical finding with real diagnostic value for the field, independent of any metric design issues.

- **Clean operationalization of effective reasoning length**: Figure 6 shows that error positions (token index at which failure occurs) stabilize within narrow, model-size-specific ranges (7B: 4–6k tokens, 32B: 8–10k tokens on MATH500). This is a well-executed, concrete finding that independently validates the concept of a bounded reasoning horizon.

- **Multidimensional failure analysis corroborating the central claim**: Figure 5 (error type decomposition), Figure 7 (reflection locality), and Figure 8 (thinking budget front-loading) jointly produce a coherent picture of why models fail under long horizons — context stress, insufficient long-range reflection, and poor budget allocation. The three analyses reinforce each other.

- **Compelling training result with rollout efficiency analysis**: Table 1 and Figure 4 show that training with n=2 composed data outperforms n=1 training on both AIME24 (n=1: +7.5) and AIME24 (n=2: +17.4). Figure 10 adds a mechanistic explanation: composed data yields ~20% more effective samples per training batch, providing a concrete training-dynamics rationale for the performance gain.

- **Scalable and controllable construction pipeline**: Algorithm 1 and the filtering pipeline (Equations 1–2) are self-contained, require only integer-answer problems and a verifier, and are applicable to any existing math/code dataset. This makes the method practically useful to the community.

---

## Weaknesses

### Fatal
None.

### Major

- **The expected accuracy baseline (Eq. 4) is structurally inconsistent with the sequential dependency design, conflating error propagation with reasoning degradation.** Eq. 4 computes Acc_expected(Q) = ∏ p_i, implicitly assuming the n sub-problems are independently attempted. However, Algorithm 1 defines dependencies such that the answer to problem i is substituted as a key variable in problem i+1 via f_i(a_i). Under this design, an error in problem i *deterministically* corrupts problems i+1 through n regardless of reasoning quality on those problems. Even a model with zero long-context degradation would show actual < expected, because a single early error cascades. The gap highlighted in Figure 1 and Figure 6 therefore conflates two distinct phenomena: genuine per-step reasoning degradation and algebraic error propagation through the chain. The paper presents this gap throughout as diagnostic evidence of reasoning limitation without acknowledging this confound. A cleaner metric — per-problem accuracy *conditioned on all prior problems being correct* — would isolate per-step degradation from propagation effects. Section 5.1's error type breakdown is informative but does not resolve this baseline problem.

- **Training evidence is limited to a single model without controls to isolate the compositional data structure as the causal factor.** All training experiments (Table 1, Figure 4) use only R1-Qwen-7B. Whether the +7.5 AIME24 gain generalizes to 32B-scale or different architectures is unknown. More critically, the n=1 baseline uses data filtered through Problem Filtering (Equations 1–2) requiring integer answers and extractable key variables, while standard Skywork-OR1 data does not carry these restrictions. The n=2 training condition uses the same filtered pool composed into pairs. The two conditions are not matched in difficulty distribution — the filtered pool skews toward numeric, integer-valued answers. It is therefore not established whether the AIME24 gains stem from the composed structure or from the implicit difficulty shift in the training data. No statistical significance or variance across training runs is reported in Table 1.

### Minor

- **The dependency mechanism is arithmetically trivial while the paper frames it as "complex interdependence."** Algorithm 1 defines f_i(x) = x + (m_{i+1} - a_i), a pure constant offset. Substituting a_i into problem i+1 amounts to replacing one integer with another integer by a fixed delta. Section 5.1 confirms this: Dependency Reasoning Errors are small and remain a low fraction of total errors in Figure 5, with Problem Reasoning Errors dominating. The claim in the introduction that R-HORIZON produces "complex multi-horizon reasoning scenarios" with "interdependent problems" meaningfully distinct from simple concatenation is only partially supported — the dependency rarely causes errors on its own; the stress is primarily context length. The paper is more accurate when it calls this "simple dependencies" (Section 5.1, paragraph 1). Framing should be adjusted accordingly.

- **The WebShaper agentic evaluation is underanalyzed.** Section 4.2 acknowledges that "many trained reasoning models have lost their ability to call tools, resulting in poor performance" on WebShaper. However, the WebShaper data in Figure 3 shows highly heterogeneous behavior: o4-Mini dramatically *improves* from n=1 (43.7%) to n=2 (87.6%), while R1-Qwen-32B collapses to near-zero. This is the most striking within-task model divergence in the entire benchmark, yet it receives a single-sentence dismissal. It is unclear whether the R-HORIZON composition approach applies meaningfully to agentic tasks or whether WebShaper is measuring a confound (tool availability in models). Including the task without deeper analysis inflates the breadth claim without proportional analytical support.

- **The training difficulty filter threshold (Acc_expected > 0.25) is unexplained and unablated.** Section 4.3 states this threshold is used "to manage difficulty," but provides no rationale for 0.25 specifically. Since this filter determines which composed problems appear in training — and by extension the difficulty distribution — it could significantly affect the reported training results. No ablation on this threshold is presented.

### Trivial

- In Figure 3 (AMC23 columns), o4-Mini and Qwen3-235B-Thinking report identical values across all n: 100.0, 97.5, 98.1, 99.1, 96.6. If these are actual scores (not a parser artifact), the paper should note whether this coincidence is real or flag a data-entry issue.

---

## Nice-to-Haves

- Demonstrate the composed-data training effect on at least one 32B-scale model to test whether the gains are specific to 7B scale or more general.
- Report per-problem accuracy conditioned on all prior problems being correct (a conditional accuracy metric), alongside the current all-or-nothing score, to cleanly separate error propagation from per-step reasoning degradation.
- For the agentic WebShaper task, either provide a dedicated analysis of why some models retain tool-calling ability while others do not, or scope the benchmark to mathematical and code tasks until the agentic composition methodology is better validated.
- A brief discussion of *why* R_all outperforms R_last on multi-horizon tasks (Table 1) beyond noting the empirical result — whether it reflects better credit assignment to intermediate steps, reduced reward sparsity effects, or something else.

---

## Removed Points

*These points are flagged to be removed, treat them with caution.*

- **Harsh critic's concern about non-monotonic MATH500 values for DeepSeek-R1 (91.2 at n=4, 92.0 at n=5)**: The paper notes all-or-nothing accuracy with stochastic generation; non-monotonic behavior at small differences is within normal statistical noise for a 30-problem AIME dataset. The numbers could reflect random seeds rather than a data error. Removed as likely noise.

- **Concern about the 40k training / 64k evaluation length mismatch**: The paper explicitly states this setup in Section 4.3. The interaction between truncation and test performance is a reasonable practical concern but is not a methodological flaw — the mismatch applies uniformly across all training conditions being compared. Demoted below threshold.

- **Criticism that dependency chain creates a "structural excuse" for sequential failure**: This is a rephrasing of the error propagation concern (which is retained in Major weaknesses). The additional framing adds no new content and was merged there.

- **Strength Finder claim about "scalable and controllable construction method" as a standalone strength**: Retained but merged into the general strengths bullet, since the scalability stems directly from Algorithm 1 and Equations 1–2 which are verified in the paper.

---

## Novel Insights

The most genuinely novel analytical finding is the *effective reasoning length* measured via error-position stabilization (Figure 6): models of different sizes exhibit consistent token-range boundaries beyond which error probability saturates, independent of total task length. This gives a behaviorally grounded, model-scale-specific characterization of reasoning capacity that is more concrete than prior work on optimal CoT length. The secondary novel finding is that training on composed-query data improves *single-problem* performance (+7.5 AIME24), suggesting that long-horizon exposure during RLVR may confer benefits beyond the multi-horizon setting — possibly by forcing more efficient token allocation (Figures 9b, 9d) that generalizes. The rollout efficiency analysis (Figure 10: ~20% more effective samples with n=2, n=4) provides a training-dynamics explanation for this that is not present in prior RLVR literature.

---

## Suggestions

1. **Replace or supplement the expected accuracy metric**: Add a conditional per-problem accuracy that conditions on all prior problems being answered correctly. This separates the two components currently conflated in Eq. 4: error propagation through the chain and per-step reasoning degradation. Report both in Figure 1 and Figure 6 to give a cleaner diagnostic picture.

2. **Match training data difficulty distribution**: For Table 1, construct an n=1 training baseline from the same filtered pool (D_filtered) to ensure the difficulty distribution matches the n=2 condition. This isolates the effect of composition from the effect of data selection.

3. **Ablate the 0.25 expected accuracy threshold**: Report results at 0.1, 0.25, and 0.5 to characterize sensitivity to this curriculum parameter.

4. **Test training on at least one 32B model**: Even a single additional model would substantially strengthen the generalization claim for the training contribution.

5. **Be precise about the dependency design's scope**: In the introduction, replace "complex multi-horizon reasoning scenarios" with phrasing that accurately reflects the mechanism — sequential numeric dependencies that primarily stress context length and budget allocation, rather than multi-step dependency reasoning per se.

---

## Evaluation on Key Axes

- **Originality**: Moderate-high. The composition-via-dependency idea is straightforward, but the systematic evaluation framework, the effective reasoning length operationalization, and the RLVR training finding are meaningfully novel.
- **Importance of research question**: High. Long-horizon reasoning is a genuine gap in current evaluation and training paradigms; this paper provides practical tools and empirical grounding.
- **Claims supported**: Moderate. The benchmark degradation finding is strongly supported. The training causal claim ("composed structure improves reasoning") is insufficiently controlled.
- **Soundness of experiments**: Moderate. Comprehensive in breadth (26 models, 6 datasets) but thin for training (one model, no variance reporting).
- **Clarity of writing**: Good. The paper is well-structured; the metric design limitation (independence assumption) is the main transparency gap.
- **Value to research community**: High. The benchmark is immediately usable; the training finding, even if needing further validation, opens a productive direction.

---

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>

<subscores>
<originality>3</originality>
<importance>4</importance>
<claims_supported>3</claims_supported>
<soundness>3</soundness>
<clarity>4</clarity>
<community_value>4</community_value>
</subscores>