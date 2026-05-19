## Summary
# Final Review Report

## Summary

This paper presents SPAR (Self-Play with Tree-Search Refinement), a framework for improving instruction-following capabilities of Large Language Models (LLMs). The core insight is that preference pairs constructed from independently sampled responses contain content variations irrelevant to whether the instruction is followed, which interferes with preference learning. SPAR addresses this by using a tree-search refinement strategy: starting from actor-generated responses that fail to follow instructions (identified by a refiner model), a tree search explores multiple refinement paths to produce corrected responses that differ minimally from the original, thereby highlighting only the instruction-relevant differences. The actor is trained via DPO on these refinement pairs, and the refiner via RFT on judgment and refinement data, in an iterative self-play loop.

The paper demonstrates that a LLaMA3-8B-Instruct model trained with SPAR over three iterations outperforms GPT-4-Turbo on the IFEval benchmark (81.8% avg vs 81.3%), while maintaining general capabilities on GSM8k, TriviaQA, MMLU, and HumanEval. The method also scales to larger models (GLM-4-9B, LLaMA3-70B) and shows that inference-time tree-search further boosts performance. Extensive ablation studies confirm the importance of refinement pairs, tree search, and iterative training.

**Strengths:** The core idea is well-motivated and clearly communicated. The synthetic experiment (Section 3.5) cleanly demonstrates the interference problem in independent sampling. The experimental evaluation is broad (multiple model families, multiple benchmarks, both actor and refiner evaluations, comprehensive baselines). The release of code, data, and models is commendable for reproducibility.

**Core Weaknesses:** (1) Statistical significance is not reported — all results are point estimates without variance, making it difficult to assess whether the often small improvements (1-2 pp on IFEval) are reliable. (2) The DPO loss in Eq. (2) omits the auxiliary SFT loss term (α=0.1) used in actual training, creating a reproducibility gap. (3) The refiner exhibits substantial self-evaluation bias (90.5% self-evaluated vs 79.0% by GPT-4o), which is acknowledged but not analyzed — this bias threatens the long-term stability of the self-play loop. (4) The method depends on GPT-4o-Mini for bootstrapping, limiting full autonomy. **Novelty and literature comparison conclusions are deferred to manual verification because external paper search was unavailable in this run.**

## Strengths
1. **Well-motivated problem analysis.** The paper identifies a genuine limitation in existing preference learning approaches for instruction following: independently sampled responses introduce content variations that are irrelevant to whether the instruction was followed. This observation is intuitive and backed by a clean synthetic experiment (Section 3.5) that isolates the interfering factor effect. The story-generation example in Figure 1 is pedagogically effective.

2. **Methodologically sound framework design.** The actor-refiner separation with tree-search refinement is a principled way to generate preference pairs that minimize irrelevant variation while maximizing instruction-relevant signal. The use of BFS/DFS to explore refinement paths, combined with self-consistency (majority voting) for judgment, addresses the practical challenge that direct refinement often fails. The iterative self-play loop (actor DPO + refiner RFT) is well-structured.

3. **Comprehensive empirical evaluation.** The paper evaluates SPAR across three model families (LLaMA3-8B, GLM-4-9B, LLaMA3-70B, Mistral-7B), two instruction-following benchmarks (IFEval, FollowBench), and compares against five baselines (AutoIF, SELF, Humpback, Self-Rewarding, Meta-Rewarding). Both actor and refiner capabilities are assessed, including judgment (LLMBar) and refinement accuracy. General-purpose benchmarks (GSM8k, TriviaQA, MMLU, HumanEval) confirm that instruction-following gains do not come at the cost of general capability loss.

4. **Scalability demonstration.** The method scales from 7B/8B models to 70B, showing consistent improvements (SPAR-70B-DPO-iter3 achieves 86.1% on IFEval vs LLaMA3-70B-Instruct's 83.4%). This suggests the core technique is not limited by model capacity.

5. **Ablation insights.** The ablation studies (Tables 4, 5, and 10) convincingly show that all components — tree search, iterative training, and refinement pairs — contribute positively. The comparison of decoding strategies (BFS, DFS, Best-of-N, iterative refinement) provides useful practical guidance.

6. **Open-source release.** Code, data, and models are publicly released, which aids reproducibility and follow-up research.

## Weaknesses
The following weaknesses are organized by severity, from most to least impactful. Each weakness is traceable to specific manuscript evidence and annotation IDs.

1. **Missing statistical significance (Major).** All main results in Tables 1, 2, 6, 7, 8 are reported as point estimates without variance, confidence intervals, or significance tests. The margins over strong baselines are often small (e.g., SPAR-8B-DPO-iter3 81.8% vs Meta-Rewarding 79.9% on IFEval — a 1.9 pp difference). Without multi-seed variance or paired significance tests, readers cannot assess whether these improvements are statistically reliable. This is especially problematic for iterative improvements where gains from iter1→iter3 are incremental. *(Annotation: Page 6 - Evaluation Benchmarks)*

2. **DPO loss equation omits auxiliary SFT loss (Major).** Equation (2) shows the standard DPO loss, but Appendix C reveals that an additional SFT loss on the chosen response with weight α=0.1 is used during training. This modification changes the effective optimization objective and affects the reward implicit in the DPO formulation. The main text does not mention or explain this term, creating a reproducibility gap between what the method section describes and what was actually implemented. *(Annotation: Page 5 - Actor Training)*

3. **Self-evaluation bias unmitigated (Major).** Table 3 shows that the refiner's self-evaluated accuracy (Acc-SPAR 90.5% for iter3) substantially exceeds its accuracy as judged by GPT-4o (Acc-GPT 79.0%), an 11.5 pp gap. While the paper correctly acknowledges this bias (Section 3.4), it does not analyze its origin, impact on training stability, or propose mitigation. If the refiner systematically overestimates its refinement quality, the training signal for the actor may degrade over iterations, threatening the long-term claim of "continuous self-improvement." *(Annotation: Page 8 - Refiner Evaluation Results)*

4. **Bootstrapping dependency on proprietary LLM (Major).** The refiner initialization relies on GPT-4o-Mini for generating judgment and refinement SFT data (Section 2.2.2). This means the "self-play" loop is not fully autonomous — it requires an external, closed-source teacher to bootstrap. The paper does not analyze how GPT-4o-Mini's systematic judgment biases propagate through the self-play iterations, nor does it test sensitivity to different teacher models. *(Annotation: Page 4 - Actor and Refiner Initialization)*

5. **No variance reporting for inference-time scaling experiments (Moderate).** Figure 5 and the "w/ tree search" row in Table 1 show performance gains from inference-time tree search, but the exact computational budget (depth, branch limit, number of node expansions) is not specified for the inference results. Without these details, the claim that "refinement is more powerful than generation" for test-time compute scaling cannot be independently verified or reproduced. *(Annotation: Page 16 - Implementation Details)*

6. **Ablation confound: refinement vs. data quantity (Moderate).** The "w/o Refinement" ablation (Table 4) removes refinement pairs entirely, causing a -3.1 drop on FollowBench. The paper attributes this solely to the absence of refinement (i.e., presence of interfering factors). However, removing refinement also reduces the total amount of preference data and changes the similarity structure of pairs (0.90 string similarity for refinement vs 0.85 for independent sampling). The observed drop could be partly due to reduced data quantity or easier learning from more similar pairs, rather than purely the absence of interfering factors. *(Annotation: Page 9 - Ablations and Analysis)*

7. **Incomplete related-work differentiation (Minor).** The related work sections (4.1, 4.2) are structured as chronological surveys rather than comparative analyses organized by design axes. The closest baseline (SELF) shares the self-feedback+refinement paradigm, but the differentiating factors (contrastive pairs vs. correct-only training) are not clearly articulated until the experiment section. *(Annotation: Page 10 - Related Work)*

8. **Missing limitations section in conclusion (Minor).** The conclusion (Section 5) states positive results without discussing any limitations. For an ICLR paper, a brief limitations paragraph covering the bootstrapping dependency, self-evaluation bias, and computational cost of tree search would strengthen scientific completeness. *(Annotation: Page 10 - Conclusion)*

## Key Issues
This section presents the top-5 ranked issues by severity, research-value impact, validity risk, fixability, and confidence.

| Rank | Issue | Severity | Research-Value Impact | Validity Risk | Fixability | Confidence | Annotation ID |
|------|-------|----------|----------------------|---------------|------------|------------|---------------|
| 1 | Missing statistical significance across all benchmarks | Major | High: without variance, incremental gains (1-2pp) may not generalize | High: core experimental claims rely on unreplicated results | Easy: run 3+ seeds, report mean±std, add paired bootstrap test | High | Page 6 - Evaluation Benchmarks |
| 2 | DPO loss Eq. (2) omits auxiliary SFT loss (α=0.1) | Major | High: reproducibility gap between method description and implementation | Medium: loss discrepancy changes optimization objective | Easy: revise Eq. (2) to include SFT term, mention α in main text | High | Page 5 - Actor Training |
| 3 | Self-evaluation bias: 11.5pp gap (90.5% vs 79.0%) not analyzed | Major | Medium-High: threatens long-term self-play stability claim | Medium: direction of bias is clear, but impact on training is unquantified | Medium: add calibration analysis, external validation checks | Moderate | Page 8 - Refiner Evaluation |
| 4 | Bootstrapping dependency on GPT-4o-Mini | Major | Medium: limits autonomy claim of self-play framework | Medium: teacher bias may propagate but is not analyzed | Hard: test alternate teacher models, quantify bias propagation | Moderate | Page 4 - Actor and Refiner Initialization |
| 5 | Inference-time tree search lacks reproducibility details | Moderate | Medium: key experiment (test-time scaling) cannot be reproduced | Low-Medium: qualitative trend is clear; exact budget missing | Easy: add inference tree-search hyperparameters to Appendix | High | Page 16 - Implementation Details |

These five issues represent the highest-priority concerns. Issues 1 and 2 are the most readily fixable with the highest confidence, while Issues 3 and 4 require deeper methodological changes but are important for long-term credibility.

## Actionable Suggestions
### Must-Fix (Publication-Critical)

**S1. Add statistical significance reporting (P0).**
- **Problem:** All results are point estimates without variance.
- **Action:** Run each experiment with 3+ random seeds. Report mean±std for all main tables (Tables 1, 2, 6, 7, 8). Add a paired bootstrap test (α=0.05) comparing SPAR against the strongest baseline on IFEval and FollowBench.
- **Location:** Tables 1, 2, 6, 7, 8; Section 3.3.
- **Expected impact:** Converts unsupported "significant improvements" into statistically grounded claims.

**S2. Fix DPO loss equation (P0).**
- **Problem:** Eq. (2) omits the auxiliary SFT loss (α=0.1) described in Appendix C.
- **Action:** Replace Eq. (2) with the actual loss used:
  $$L = \mathbb{E}_{(x,y_w,y_l)\sim D_t_{\text{dpo}}} \left[ \log \sigma\left( \beta \log \frac{\pi^t_\theta(y_w|x)}{\pi_{\text{ref}}(y_w|x)} - \beta \log \frac{\pi^t_\theta(y_l|x)}{\pi_{\text{ref}}(y_l|x)} \right) \right] - \alpha \cdot \mathbb{E}_{(x,y_w)} \left[ \log \pi^t_\theta(y_w|x) \right]$$
  where α=0.1. Add a sentence in Section 2.3.3 explaining why this auxiliary term is used.
- **Location:** Page 5, Eq. (2) and surrounding text.
- **Expected impact:** Eliminates reproducibility gap.

**S3. Analyze self-evaluation bias (P0).**
- **Problem:** The 11.5pp gap between Acc-SPAR and Acc-GPT is acknowledged but not analyzed.
- **Action:** (a) Compute per-sample agreement between the refiner's judgment and GPT-4o's judgment on the refinement test set. (b) Report whether the bias is systematic (e.g., always overconfident) or varies by example difficulty. (c) Add a paragraph in Section 3.4 discussing implications for training stability. (d) Consider adding an external validation check every N iterations.
- **Location:** Section 3.4, after Table 3 discussion.
- **Expected impact:** Either confirms the self-play loop is stable despite bias, or identifies a correction mechanism.

**S4. Bound the "surpasses GPT-4-Turbo" claim (P1).**
- **Problem:** Abstract and Introduction state "surpasses GPT-4-Turbo on the IFEval benchmark" without sufficient scope qualification.
- **Action:** Add "on the IFEval benchmark" explicitly to the abstract sentence. In the Introduction, note that this does not claim overall superiority. See the Mentor Revised Version in the Abstract annotation (Page 1).
- **Location:** Page 1 (Abstract), Page 2 (Introduction).
- **Expected impact:** Prevents misinterpretation and improves scientific accuracy.

### Nice-to-Have (Quality Improvement)

**S5. Report inference-time tree-search configuration (P1).**
- **Problem:** The "w/ tree search" row and Figure 5 lack exact inference budgets.
- **Action:** Add to Appendix C: depth limit, branch limit, BFS/DFS choice, and computational budget (number of node expansions) used for the inference-time results in Table 1 and Figure 5.
- **Location:** Appendix C.
- **Expected impact:** Enables full reproducibility of the test-time scaling results.

**S6. Add limitations paragraph to conclusion (P1).**
- **Problem:** Conclusion lacks any limitations discussion.
- **Action:** Add a 3-4 sentence paragraph covering: (a) bootstrapping dependency on GPT-4o-Mini, (b) self-evaluation bias, (c) computational cost of tree search, (d) limited iteration count (3). See the Mentor Revised Version in the Conclusion annotation (Page 10).
- **Location:** Section 5, before the closing sentence.
- **Expected impact:** Improves scientific completeness and reviewer trust.

**S7. Restructure related work as comparison table (P2).**
- **Problem:** Sections 4.1-4.2 are chronological surveys.
- **Action:** Replace the final paragraph of Section 4.2 with a structured comparison of SPAR vs. SELF, Self-Rewarding, Meta-Rewarding along axes: data construction method, variation control, feedback source, and self-improvement loop design.
- **Location:** Page 10, Section 4.2.
- **Expected impact:** Makes the novelty and differentiation clearer to readers.

**S8. Add controlled experiment for ablation confound (P2).**
- **Problem:** The "w/o Refinement" ablation confounds refinement presence with data quantity and pair similarity.
- **Action:** Add an ablation where independently sampled pairs are matched in number to refinement pairs, with similarity controlled (e.g., by sampling from the same story template but varying only constraint-relevant portions).
- **Location:** Section 3.5 or Appendix.
- **Expected impact:** Strengthens the causal claim that refinement (not just data quantity) drives improvement.

## Storyline Options + Writing Outlines
### Current Storyline Diagnosis

The current paper structure follows: Big Picture (LLM success) -> Gap (independent sampling introduces interference) -> Solution (SPAR with tree-search refinement) -> Evidence (IFEval, FollowBench results) -> Contribution statements. This is a reasonable default structure. However, the narrative has two weaknesses:

1. **The introduction front-loads general LLM success before targeting instruction-following.** Paragraph 1 opens with generic LLM success references before narrowing to instruction following. This wastes reader attention on content that is not specific to the paper's contribution.

2. **The "interfering factor" concept is introduced in the gap paragraph but not named or formalized until later.** The paper would benefit from an explicit term (e.g., "variation confound" or "instruction-irrelevant variation") used consistently from the introduction onward.

### Candidate Storyline A (Recommended) — Problem-First with Explicit Terminology

**Abstract Outline:**
- S1 (Problem): Instruction-following requires recognizing subtle constraints; even small deviations can cause task failure.
- S2 (Gap): Current preference learning methods construct pairs from independently sampled responses, introducing instruction-irrelevant content variation that confounds learning.
- S3 (Solution): We propose SPAR, a self-play framework that uses tree-search refinement to generate preference pairs differing only in instruction-relevant aspects.
- S4 (Key Result): LLaMA3-8B with SPAR (3 iterations) achieves 81.8% on IFEval, outperforming GPT-4-Turbo (81.3%), while maintaining general capabilities.
- S5 (Scope/Scalability): SPAR scales to larger models (70B) and benefits from inference-time tree search; code and data are released.

**Introduction Outline (5 paragraphs):**
- P1 (Hook + Problem): "When a language model is asked to 'write a story ending with X,' two independently sampled responses may differ entirely in content — yet only one satisfies the ending constraint. This instruction-irrelevant variation is the core challenge we address." (Replaces current generic LLM opening.)
- P2 (Gap + Formalization): Define preference learning for instruction following. State formally: independently sampled pairs contain both instruction-relevant signal (did the model follow the constraint?) and instruction-irrelevant noise (story content, style, length). This noise interferes with DPO's ability to learn the relevant signal.
- P3 (Solution Intuition): Introduce SPAR. The key idea: instead of sampling independent responses, start from a failed response and refine it minimally until it succeeds. This creates pairs where the only difference is instruction-adherence.
- P4 (Method Sketch): Actor-refiner loop, tree-search exploration of refinement paths, DPO for actor, RFT for refiner, iterative self-play.
- P5 (Result Preview + Contributions): IFEval results, scalability, inference-time gains. Three bullet contributions (as revised in annotation).

### Candidate Storyline B — Mechanism-Focused

- P1: Directly state the mechanism: preference learning for instruction following fails when responses vary in irrelevant ways.
- P2: Show why existing methods (Self-Rewarding, Meta-Rewarding) suffer from this via independent sampling.
- P3: Introduce controlled refinement as the solution.
- P4: SPAR architecture and iterative self-play.
- P5: Empirical validation and contributions.

### Recommendation

**Use Storyline A.** It front-loads a concrete example (story ending) that immediately engages readers, and it uses explicit terminology ("instruction-irrelevant variation") that creates a clear conceptual handle for the rest of the paper. The current Figure 1 example is well-placed; it should be referenced in the first paragraph, not the second.

**Writing-level improvements needed:**
1. Replace "performing solution" (contribution list) with "effective solution" or "practical approach."
2. Use consistent terminology: "instruction-irrelevant variation" instead of "interfering factors" and "extraneous factors."
3. In the method section, add one sentence of explanation for why tree search produces more comparable pairs before diving into the BFS/DFS details (Page 3).
4. Add explicit forward references from the introduction to key experiments (e.g., "as confirmed by controlled synthetic experiments in Section 3.5").

## Priority Revision Plan
The following plan prioritizes revisions by their expected impact on paper quality, validity, and reviewer acceptance.

| Priority | Action | Effort | Impact | Section | Annotation Ref |
|----------|--------|--------|--------|---------|----------------|
| P0 | Add statistical significance (3+ seeds, mean±std, bootstrap test) | 1-2 weeks of compute | High — converts unsupported claims into reliable evidence | Tables 1,2,6,7,8; Section 3.3 | Page 6 - Evaluation Benchmarks |
| P0 | Fix DPO loss equation to include auxiliary SFT term | <1 day | High — eliminates reproducibility gap | Eq. (2), Section 2.3.3 | Page 5 - Actor Training |
| P0 | Analyze self-evaluation bias (calibration analysis, external validation) | 1 week | High — determines whether self-play loop is stable long-term | Section 3.4 | Page 8 - Refiner Evaluation |
| P1 | Bound "surpasses GPT-4-Turbo" claim in Abstract and Introduction | <1 day | Medium — prevents misinterpretation | Abstract, Page 2 | Page 1 - Abstract |
| P1 | Report inference-time tree-search hyperparameters | <1 day | Medium — enables reproducibility of test-time scaling results | Appendix C | Page 16 - Implementation Details |
| P1 | Add limitations paragraph to conclusion | <1 day | Medium — improves scientific completeness | Section 5 | Page 10 - Conclusion |
| P2 | Restructure related work as comparative analysis | 2-3 days | Medium — clarifies differentiation | Sections 4.1, 4.2 | Page 10 - Related Work |
| P2 | Run controlled ablation for refinement vs. data quantity confound | 1 week | Medium — strengthens causal claim | Section 3.5 or Appendix | Page 9 - Ablations |
| P2 | Investigate teacher model bias propagation | 2-3 weeks | Medium-High — strengthens autonomy claim | Section 2.2.2 + Appendix | Page 4 - Refiner Init |
| P3 | Improve abstract storyline (problem-first with concrete example) | <1 day | Low-Medium — readability polish | Abstract | Page 1 - Abstract |

### Recommended Execution Order

**Phase 1 (Week 1-2, before resubmission):**
1. P0: Fix DPO equation and add auxiliary loss discussion.
2. P0: Run 3-seed experiments for main results, add variance bars.
3. P1: Bound "surpasses GPT-4-Turbo" in abstract/intro.
4. P1: Report inference tree-search configuration.
5. P1: Add limitations to conclusion.

**Phase 2 (Week 3-4):**
6. P0: Self-evaluation bias analysis and calibration.
7. P2: Controlled ablation for refinement vs. data quantity.
8. P2: Restructure related work.

**Phase 3 (Before final submission):**
9. P2: Teacher model bias propagation analysis.
10. P3: Abstract storyline polish.

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory

| Exp ID | Objective/Hypothesis | Setup | Metrics | Main Outcome | Claim Supported | Current Limitation |
|--------|---------------------|-------|---------|-------------|----------------|-------------------|
| E1 | Main IFEval evaluation: SPAR improves instruction-following | 3 architectures, 3 iterations, DPO training | IFEval P(L), I(L), P(S), I(S), Avg | SPAR-8B-DPO-iter3: 81.8% avg, surpasses GPT-4-Turbo (81.3%) | C2 (method improves IF) | No variance or significance test; modest 1.9pp over Meta-Rewarding |
| E2 | FollowBench evaluation | Same setup as E1 | FollowBench SSR by level (Lv1-5) and Avg | SPAR-8B-DPO-iter3: 68.8% avg (+1.5 over Meta-Rewarding) | C2 | Modest improvement; FollowBench uses subjective LLM-as-judge |
| E3 | General capability maintenance | GSM8k, TriviaQA, MMLU, HumanEval | Task-specific accuracy | SPAR maintains or slightly improves general performance (+1.6 avg for LLaMA3-8B) | C2 (no degradation) | Some metrics (MMLU) show negligible change; improvement mostly on GSM8k/HumanEval |
| E4 | Baseline comparison (Figure 3) | SPAR vs SELF, Humpback, Self-Rewarding, Meta-Rewarding | IFEval across iterations | SPAR consistently outperforms all baselines | C1, C2 | Baseline SFT data tailored to SPAR's actor-refiner paradigm may disadvantage others |
| E5 | Refiner judgment evaluation (Table 2) | LLMBar (Natural + Adversarial) | Acc, F1 | SPAR-8B-RFT-iter3: 68.3% Acc (surpasses GPT-4o-Mini 67.4%) | C2 (refiner improves) | Self-evaluation bias (Acc-SPAR vs Acc-GPT gap) not analyzed |
| E6 | Refinement accuracy (Table 3) | 200 samples from D_RSFT | Acc-GPT, Acc-SPAR | SPAR-8B-RFT-iter3: 79.0% (GPT-4o judge), 90.5% (self-judge) | C2 (refinement improves) | Large self-evaluation gap (11.5pp) |
| E7 | Synthetic data experiment (Figure 4) | Character Sequence Gen + Start/End Story Gen | Accuracy over training steps | Refinement pairs significantly outperform interfering pairs | C1 (interfering factors harm learning) | Synthetic tasks may not fully generalize to real instruction-following complexity |
| E8 | Ablation on actor (Table 4) | SPAR-8B-DPO-iter3 variants | IFEval, FollowBench | All components matter: w/o Refinement (-3.1), w/o Tree Search (-1.7), w/o Iterative (-2.0) | C2 | Refinement confounded with data quantity and pair similarity |
| E9 | Ablation on refiner (Table 5) | SPAR-8B-RFT-iter3 variants | LLMBar Natural/Adversarial | w/o Tree Search hurts adversarial more (-4.3 Acc, -8.2 F1) | C2 (tree search helps robustness) | Small absolute changes |
| E10 | Test-time compute scaling (Figure 5) | Decoding strategies on SPAR-8B-DPO-iter3 | IFEval vs inference budget | Tree search refinement > best-of-N generation at larger budgets | C2 (inference scaling) | Exact inference budget not specified; hard to reproduce |

### Research-Theme Gap Diagnosis

**New knowledge gap:** The paper's primary claim to new knowledge is the identification of "interfering factors" in independently sampled preference pairs. This is well-supported by the synthetic experiments. However, the paper does not establish **how much** of the real IFEval/FollowBench improvement comes from eliminating interference vs. from other factors (better data, more similar pairs, more training data from tree search). The causal mechanism is asserted but not fully isolated.

**Reproducibility gap:** The DPO loss equation discrepancy (S2) and missing inference tree-search details (S5) directly reduce reproducibility.

**Impact on practice/understanding gap:** The paper claims "continuous self-improvement" but only tests 3 iterations and does not analyze whether the self-play loop would further improve, plateau, or degrade with more iterations. The self-evaluation bias issue suggests degradation is possible.

### Proposed Research Experiments (P0/P1/P2)

**P0.1: Multi-seed variance and significance testing**
- **Target Claim:** "SPAR significantly improves instruction-following" (all iteration results).
- **Hypothesis:** SPAR's improvements over strong baselines are statistically significant.
- **Minimal Design:** Run SPAR-8B-DPO-iter1/2/3 and Meta-Rewarding with 5 seeds each. Report mean±std for IFEval and FollowBench. Use paired bootstrap (10k resamples) for SPAR vs. strongest baseline at each iteration.
- **Controls:** Same seed for all model initializations within each run.
- **Success Criterion:** SPAR-iter3 outperforms baseline with p<0.05 on both benchmarks.
- **Estimated Cost:** ~5× current compute (5 seeds instead of 1). ~1 week on 8×A100.
- **Expected Quality Gain:** Converts anecdotal improvements into statistically grounded claims.

**P0.2: Self-evaluation bias calibration analysis**
- **Target Claim:** "The refiner iteratively improves toward the teacher."
- **Hypothesis:** The refiner's self-evaluation bias is systematic (overconfidence) and can be calibrated.
- **Minimal Design:** For SPAR-8B-RFT-iter3, collect per-sample judgment confidence (if available) or prediction probability on the 200-sample refinement test set. Compute calibration curve (expected vs. observed accuracy) and compare with GPT-4o's calibration.
- **Success Criterion:** If calibration is monotonic, propose a bias correction factor. If non-monotonic, analyze failure cases.
- **Estimated Cost:** <1 day of compute + analysis.
- **Expected Quality Gain:** Either confirms the refiner is well-calibrated (strengthening claims) or identifies a fixable bias.

**P1.1: Controlled ablation for refinement vs. data quantity**
- **Target Claim:** "Refinement pairs improve learning by eliminating interfering factors."
- **Hypothesis:** Controlling for data quantity, refinement pairs still outperform independent pairs.
- **Minimal Design:** Create a matched setting: for each prompt, generate N refinement pairs (using tree search) and N independent pairs. Train DPO on each set with matched hyperparameters. Compare IFEval scores.
- **Controls:** Equal N, same training budget, same base model.
- **Success Criterion:** Refinement pairs outperform independent pairs at each N.
- **Estimated Cost:** ~1 week on 8×A100.
- **Expected Quality Gain:** Removes confound and strengthens causal claim.

**P1.2: Iteration extrapolation (4th iteration test)**
- **Target Claim:** "SPAR enables continuous self-improvement."
- **Hypothesis:** SPAR continues to improve at iteration 4 or plateaus gracefully.
- **Minimal Design:** Run one additional iteration of SPAR-8B (iter4) using the same pipeline. Evaluate on IFEval and FollowBench.
- **Success Criterion:** Either improvement from iter3 to iter4, or a plateau with no degradation. If degradation occurs, analyze why.
- **Estimated Cost:** ~2 weeks on 8×A100.
- **Expected Quality Gain:** Strongly informs the "continuous self-improvement" claim.

**P2.1: Teacher model sensitivity analysis**
- **Target Claim:** "SPAR bootstraps effectively from any sufficiently capable teacher."
- **Hypothesis:** Initializing the refiner with different teachers (e.g., GPT-4o, Claude-3, or a stronger open-source model) leads to similar final performance.
- **Minimal Design:** Replace GPT-4o-Mini with one alternative teacher for the refiner SFT data construction. Run SPAR-8B for 3 iterations and compare.
- **Success Criterion:** Final performance gap <2% across teacher choices.
- **Estimated Cost:** ~3 weeks on 8×A100 (significant API cost for alternative teacher).
- **Expected Quality Gain:** Validates robustness to teacher choice and strengthens autonomy claim.

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score: 6.5/10**

**Rationale (prioritizing research value and novelty):** 
The paper presents a genuinely well-motivated idea — the identification of "interfering factors" in independently sampled preference pairs for instruction-following — and the synthetic experiment (Section 3.5) cleanly demonstrates this effect. The SPAR framework (tree-search refinement for controlled preference pair construction) is a sound methodological response to this problem, and the empirical results across multiple model families and benchmarks show consistent, if incremental, improvements over strong baselines. The open-source release of code, data, and models is commendable.

However, the score is constrained by the following factors:
1. **No statistical significance reporting** — without variance estimates, the incremental gains (1-2 pp on IFEval) cannot be assessed for reliability.
2. **DPO loss reproducibility gap** — Eq. (2) omits the actual training objective (auxiliary SFT loss), which undermines trust in the method description.
3. **Self-evaluation bias unmitigated** — the 11.5pp gap between self-evaluated and externally-evaluated refinement accuracy casts uncertainty on the self-improvement loop.
4. **Novelty is deferred** — due to Retrieval-Disabled Mode, novelty and literature comparison are not independently verified; the score assumes the paper's claims about prior work are accurate.
5. **Missing limitations section** reduces scientific completeness.

These are fixable issues: Items 1 and 2 can be resolved with moderate compute effort; Item 3 requires additional analysis but is tractable. If all P0/P1 issues are addressed, the paper could be significantly strengthened.

**Post-Revision Target: [7.5, 8.0]/10**

This target assumes the following improvements are completed:
- Statistical significance added (multi-seed variance + bootstrap tests)
- DPO equation corrected
- Self-evaluation bias analyzed and discussed
- "Surpasses GPT-4-Turbo" claim appropriately scoped
- Inference-time tree-search configuration reported
- Limitations added
- Limitations paragraph added to conclusion
- Related work restructured for clearer differentiation

If these changes are made, the paper would present a well-supported, reproducible, and scientifically rigorous contribution to the instruction-following alignment literature. The upper bound (8.0) is achievable if the self-evaluation bias analysis reveals the refiner is well-calibrated despite the gap, and if multi-seed experiments confirm statistical significance of the main results.