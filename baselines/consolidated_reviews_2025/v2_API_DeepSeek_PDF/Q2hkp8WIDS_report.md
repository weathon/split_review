## Summary
# Final Review Report

## Summary

This paper introduces OC-STORM, an object-centric model-based reinforcement learning (MBRL) pipeline that integrates a frozen vision foundation model (Cutie) for extracting compact object feature vectors and feeds them alongside raw observations into a spatial-temporal transformer world model. The work builds on the STORM algorithm and is evaluated on the Atari 100k benchmark (26 games) and the visually complex game Hollow Knight (6 bosses). The core motivation is that conventional MBRL methods relying on L2 reconstruction loss may overlook small decision-critical objects in visually complex environments.

**Key strengths:** The paper presents a clean, well-motivated integration of modern video object segmentation (Cutie) into an MBRL framework, with reasonable experimental breadth across Atari and a novel challenging domain (Hollow Knight). The ablation studies (vector vs mask representation, number of annotation masks, attention vs MLP policy) are informative. The object-feature reconstruction experiment on Boxing provides an intuitive sanity check.

**Key weaknesses:** (1) The manual annotation requirement (6-12 masks per environment) and need to pre-specify the number of objects K limit practical scalability, and this limitation is downplayed with a weak analogy. (2) The Hollow Knight evaluation uses a substantially different reward function (virtual termination on damage) that itself significantly improves performance, confounding the assessment of the object-centric contribution. (3) Statistical rigor is lacking: no variance or significance tests are reported for any experiment, and only 3 seeds are used for Hollow Knight. (4) The "first to successfully adopt object-centric learning on Atari" novelty claim cannot be verified without systematic comparison to prior work (e.g., Nakano et al., 2024, who also extend STORM with slot attention). (5) The Conclusion is generic and includes unsupported forward-looking speculation.

**Overall assessment:** The paper makes a useful empirical contribution by demonstrating that frozen vision foundation model features can improve MBRL sample efficiency, but the current evidence is incomplete. Key claims are overstated relative to the evidence, and the practical significance is limited by the annotation burden and confounded comparison settings.

## Strengths
1. **Well-motivated problem formulation.** The paper clearly identifies a genuine limitation of current MBRL methods: L2 reconstruction loss can overlook small decision-critical objects. This motivation is supported by qualitative evidence (Appendix B, reconstruction failure examples on Hollow Knight) and is a recognized challenge in the field.

2. **Practical integration of modern vision tools.** Using Cutie as a frozen feature extractor is a pragmatic design choice that avoids end-to-end training complexity. The four-step pipeline (annotate → extract → model → policy) is clearly described, and the Cutie selection rationale (compact vector representation, video-level consistency, few-shot annotation, out-of-domain generalization) is well-justified.

3. **Informative ablation studies.** The paper includes several useful ablations: (a) vector vs mask object representation (Section 5.2, Figure 4), which shows the benefit of using Cutie's feature vectors over binary masks; (b) impact of the number of annotation masks (Appendix E.2, Figure 11), demonstrating robustness to annotation quantity; (c) attention-based vs MLP-based policy (Appendix E.1, Figure 10), revealing overfitting issues with attention policies. These analyses provide practical guidance for future work.

4. **Novel challenging benchmark (Hollow Knight).** The paper introduces Hollow Knight boss fights as a visually complex RL testbed with dynamic backgrounds, small key objects, and stochastic boss behavior. This is a valuable addition to the evaluation landscape beyond the saturated Atari 100k benchmark. The custom environment wrapper (Hyper-V setup, keyboard binding action space) represents non-trivial engineering effort.

5. **Object feature reconstruction validation.** The reconstruction experiment (Section 5.1, Figure 3) using a ConvTranspose2d decoder on Atari Boxing provides a clean sanity check that Cutie's 2048-d feature vectors encode sufficient information about object state and position to reconstruct observations.

6. **Computational efficiency in representation.** Using compact 2048-d vectors per object rather than full-resolution masks or attention maps is a sensible design for keeping the downstream world model tractable, especially as the number of objects K grows.

## Weaknesses
1. **Statistical rigor is inadequate.** No variance estimates, confidence intervals, or significance tests are reported for any experimental result. For Atari (5 seeds) and Hollow Knight (3 seeds), only mean scores are presented in Tables 1 and 3. Given the well-known high variance in RL evaluation, especially at 100k steps, this omission is significant. Several improvements are small (e.g., Boxing: 81.2→92.2, Pong: 18.4→20.6), and without variance the reader cannot assess reliability.

2. **Reward shaping confound on Hollow Knight.** The paper introduces a novel reward function (virtual termination on taking damage) in Appendix D.4, which is shown in Figure 7 to substantially improve STORM's performance on its own. This confounds the assessment of the object-centric module's contribution. The claim of "best-known sample efficiency on several Hollow Knight bosses" in the Abstract is misleading because prior work used incompatible reward functions.

3. **Manual annotation burden is underplayed.** The pipeline requires 6-12 segmentation masks per environment and pre-specification of K (number of objects). The paper's defense ("just like telling rules to humans") is a weak analogy. The time cost of annotation, sensitivity to annotation quality, and the human-in-the-loop requirement are not quantified. This limits practical scalability.

4. **Unverifiable novelty claim.** The statement "To our knowledge, we are the first to successfully adopt object-centric learning on Atari and the visually more complex Hollow Knight without relying on an extensive number of labels or accessing internal game states" is a strong novelty claim that cannot be fully verified without systematic literature comparison (external retrieval unavailable in this run). Notably, Nakano et al. (2024) also extends STORM with object-centric representations (slot attention), and the paper's differentiation from this work is only briefly stated without empirical comparison.

5. **Conclusion is generic and speculative.** The final paragraph (Page 10) discusses "disentangling perceptual learning from policy learning" and "paving the way for more intuitive and robust agent behaviors" without any connection to the paper's findings. This is aspirational language unsuitable for a scientific conclusion.

6. **STORM* baseline discrepancy.** The paper retrains STORM with a "more lightweight configuration" (STORM*) that achieves 114.2% mean HNS vs the original STORM's 122%. This 7.8 percentage point gap is not explained. If the lightweight configuration harms STORM more than OC-STORM, the reported improvements may overstate the object-centric benefit.

7. **Missing computational cost analysis.** The paper claims the vector representation is "computationally efficient" but provides no runtime, FLOPs, or memory comparisons between STORM*, STORM*+mask, and OC-STORM (vector). Given that Cutie requires upscaled 420×320 (Atari) or 480p (HK) inputs and runs a transformer-based segmentation model, the computational overhead should be quantified.

8. **Limited evaluation of representation completeness.** The reconstruction experiment (Section 5.1) is only conducted on Atari Boxing, the simplest possible case (2 objects, static background). No validation is provided for multi-object environments (K≥3) or visually complex scenes (Hollow Knight).

## Key Issues
### Issue 1 (Critical): Hollow Knight reward shaping confound undermines the strongest results
**Location:** Page 8 - Section 4.2 (Hollow Knight), Page 21-22 - Appendix D.4
**Evidence:** Appendix D.4 describes a custom reward function that assigns a virtual termination signal when the agent takes damage. Figure 7 shows this reward shaping alone substantially improves STORM's performance. 
**Impact:** Since OC-STORM and STORM* both use this modified reward, the comparison between them is internally fair. However, the abstract claim "best-known sample efficiency on several Hollow Knight bosses" is misleading because prior work used incompatible reward functions. The paper acknowledges this limitation indirectly ("since Hollow Knight is not yet an established benchmark... direct comparisons with existing methods impractical") but still makes the unqualified claim.
**Required action:** Remove the "best-known" claim from Abstract and Introduction. Add an explicit statement that the Hollow Knight results use a custom reward function that differs from prior work, and that cross-study comparisons are not intended.

### Issue 2 (Major): Missing variance and significance testing
**Location:** Page 6-7 - Section 4.1 (Atari 100k), Page 8 - Section 4.2 (Hollow Knight)
**Evidence:** Tables 1 and 3 present only mean scores without standard deviations. Only 5 seeds (Atari) and 3 seeds (Hollow Knight) are used. Several improvements are small (Boxing: +11, Pong: +2.2, Breakout: +11.5).
**Impact:** Without variance, the statistical reliability of claimed improvements cannot be assessed. Many improvements could be within noise range.
**Required action:** Add per-game standard deviations and, where possible, confidence intervals or bootstrap-estimated p-values for the OC-STORM vs STORM* comparison.

### Issue 3 (Major): Unverifiable novelty claim and insufficient comparison with Nakano et al. (2024)
**Location:** Page 2 - Introduction, Page 4 - Related Work (Object-Centric RL)
**Evidence:** The paper claims to be "the first to successfully adopt object-centric learning on Atari and Hollow Knight without extensive labels or internal game states." However, Nakano et al. (2024) also extends STORM with object-centric representations (slot attention), and the paper only briefly distinguishes itself ("we use a pre-trained vision model instead of unsupervised slot attention") without empirical comparison.
**Impact:** The novelty differentiation from the most directly related work is asserted but not demonstrated.
**Required action:** Either add a direct experimental comparison with slot-attention-based STORM (if feasible) or reframe the contribution as "a practical demonstration that frozen vision model features can improve MBRL" rather than a first-claim.

### Issue 4 (Major): STORM* baseline discrepancy unexplained
**Location:** Page 7 - Table 1 caption
**Evidence:** STORM* (114.2% HNS) underperforms the original STORM (122% HNS) by 7.8 percentage points. The caption states "we use a more lightweight configuration for faster training" but does not specify which hyperparameters changed.
**Impact:** This unexplained gap raises the question of whether OC-STORM's improvement over STORM* might partially reflect asymmetric degradation from the configuration change rather than the object-centric module.
**Required action:** Report the specific configuration differences and, ideally, run OC-STORM with the original STORM configuration on a subset of games to verify the improvement holds.

### Issue 5 (Major): Generic conclusion with unsupported speculation
**Location:** Page 10 - Section 7 (Conclusions)
**Evidence:** The second paragraph discusses "paving the way for more intuitive and robust agent behaviors in increasingly complex scenarios" without referencing any evidence from the paper.
**Impact:** Weakens scientific credibility. A conclusion should summarize validated findings and bounded limitations.
**Required action:** Replace the speculative paragraph with a concise limitations recap and concrete future directions.

## Actionable Suggestions
### S1 (Must): Add variance and significance information to all experimental tables
Revise Tables 1 and 3 to include standard deviations across seeds. For Atari, report mean ± std over 5 seeds. For Hollow Knight, report over 3 seeds. Add a note in the experimental setup: "We assess statistical significance using a paired bootstrap test (1000 resamples) comparing OC-STORM vs STORM* per game; results with p < 0.05 are marked with *."

### S2 (Must): Qualify Hollow Knight claims and reward function
- Remove "best-known sample efficiency" from Abstract and Introduction.
- Add an explicit paragraph in Section 4.2: "We note that the Hollow Knight results use a custom reward function (Appendix D.4) that differs from prior work. While OC-STORM and STORM* are compared under identical conditions, direct comparisons with previously published results on Hollow Knight should account for differences in reward design."

### S3 (Must): Explain STORM* vs original STORM discrepancy
Add a dedicated paragraph or appendix section specifying exactly which hyperparameters were changed (e.g., "We reduced the number of transformer layers from 3 to 2 and the feature dimension from 512 to 256, reducing total parameters by approximately 40%."). Run OC-STORM with the original (non-lightweight) STORM configuration on at least 5 representative games to verify that the improvement holds when using the original configuration.

### S4 (Must): Rewrite Conclusion to focus on validated findings
Replace the speculative second paragraph with: "The main limitations of the current work are: (a) manual annotation is required per environment (6-12 masks), (b) tracking quality degrades on duplicate objects, and (c) the benefit over baselines is most pronounced in games where key information can be represented as objects. Future work should investigate automated object discovery and test the pipeline on real-world robotic tasks."

### S5 (Must): Reduce strength of novelty claim
Replace "first to successfully adopt object-centric learning on Atari and the visually more complex Hollow Knight" with: "Our work demonstrates that integrating a frozen video object segmentation model (Cutie) into an MBRL pipeline improves sample efficiency on several visually complex environments, including Atari games and Hollow Knight, without requiring game-internal state access."

### S6 (Nice-to-have): Add computational cost comparison
Add a table comparing per-step runtime and peak GPU memory for: (a) STORM* (visual only), (b) STORM* + mask OCRL, (c) OC-STORM (vector module + visual module). Report both training and inference cost.

### S7 (Nice-to-have): Expand reconstruction validation
Add reconstruction experiments on at least one multi-object Atari game (e.g., Alien, K=4) and one Hollow Knight scene to validate that the 2048-d vector representation captures object state in more complex settings.

### S8 (Nice-to-have): Add annotation cost quantification
Add a sentence in Section 3.1: "Manual annotation of 6 masks for an Atari game requires approximately X minutes; for 12 Hollow Knight masks, approximately Y minutes." This makes the practical cost transparent.

## Storyline Options + Writing Outlines
### Abstract Outline (Revised)
Recommended 5-sentence structure:
- **S1 (Problem):** "Deep reinforcement learning from pixels suffers from low sample efficiency, a challenge that model-based reinforcement learning (MBRL) addresses via learned world models."
- **S2 (Limitation of prior work):** "However, conventional MBRL methods rely on L2 reconstruction loss, which is dominated by large background areas and can miss small decision-critical objects."
- **S3 (Proposed method):** "We propose OC-STORM, an object-centric MBRL pipeline that integrates a frozen pre-trained vision model (Cutie) to extract compact 2048-dimensional object features, which are combined with raw observations in a spatial-temporal transformer world model."
- **S4 (Key results with numbers):** "On the Atari 100k benchmark, OC-STORM achieves a mean human-normalized score of 134.8% versus 114.2% for the baseline STORM, outperforming it on 18 of 26 games. On the more complex Hollow Knight domain, OC-STORM improves win rates by up to 43 percentage points across bosses under matched conditions."
- **S5 (Bounded implication):** "These results demonstrate that incorporating object-centric features from foundation vision models can substantially improve MBRL sample efficiency in visually complex environments, while the need for minimal manual annotation (6-12 masks per environment) suggests promising directions for reducing human involvement."

### Introduction Outline (Revised)
The current introduction has a reasonable structure but can be improved for narrative clarity and evidence grounding.

**Current paragraph map:**
- P1: DRL success → sample efficiency problem → MBRL solution → reconstruction loss limitation
- P2: Recent CV advances → proposed pipeline → contribution claims
- P3: Summary contribution statement

**Revised paragraph map (4 paragraphs):**

**P1 (Big Picture + Gap):** Start with the concrete problem: MBRL methods learn world models through pixel reconstruction, but L2 loss is insensitive to small objects. Add the quantitative motivation: "For example, in Hollow Knight, the player character and boss occupy less than 5% of the visual area, yet determine all reward signals." End with the gap: "Consequently, existing MBRL methods can reconstruct backgrounds well while missing the very elements needed for control."

**P2 (CV Advances + Opportunity):** Bridge to the opportunity: "Recent advances in video object segmentation—particularly Cutie, which provides compact vector representations of objects across frames with few-shot annotation—offer a way to directly provide decision-relevant information to the world model." This paragraph should explain why Cutie is the right tool (vector representation, consistency, few-shot) without the bullet-list style.

**P3 (Proposed Solution + Differentiator):** Introduce the four-step pipeline concisely. Then add a sentence that clearly differentiates from prior object-centric MBRL work: "Unlike FOCUS (Ferraro et al., 2023), which passes binary masks to DreamerV2, and Nakano et al. (2024), which uses unsupervised slot attention within STORM, OC-STORM leverages pre-trained, frozen object features that capture rich state and positional information without requiring joint training of the perception module."

**P4 (Contributions + Results Preview):** State contributions with concrete numbers: "OC-STORM outperforms the STORM baseline on 18 of 26 Atari 100k games (134.8% vs 114.2% mean HNS) and achieves consistent improvements across six Hollow Knight bosses, including a 43 percentage point win-rate increase on Mage Lord."

### Title Suggestion
Current: "OBJECTS MATTER: OBJECT-CENTRIC WORLD MODELS IMPROVE REINFORCEMENT LEARNING IN VISUALLY COMPLEX ENVIRONMENTS"

Suggested revision: "OC-STORM: Object-Centric World Models Improve Sample Efficiency in Visually Complex Reinforcement Learning Environments"

Rationale: Adds the acronym (OC-STORM) for memorability and replaces the generic "Improve Reinforcement Learning" with the specific benefit ("Improve Sample Efficiency"), which is the paper's core claim.

## Priority Revision Plan
### P0 (Critical — must fix before resubmission)

1. **Address reward shaping confound (Key Issue 1)**
   - Remove "best-known sample efficiency" claim from Abstract and Introduction.
   - Add explicit caveat in Section 4.2 about reward function differences.
   - **Expected impact:** Restores scientific credibility of Hollow Knight results.

2. **Add variance reporting (Key Issue 2)**
   - Add standard deviations to Tables 1 and 3.
   - Add significance tests (bootstrap or paired) for OC-STORM vs STORM*.
   - **Expected impact:** Allows readers to assess reliability of claimed improvements.

3. **Explain STORM* configuration and verify improvement (Key Issue 4)**
   - Document the "lightweight configuration" differences.
   - Run OC-STORM with original STORM configuration on 5+ games.
   - **Expected impact:** Removes ambiguity about whether improvements are robust.

4. **Rewrite Conclusion (Key Issue 5)**
   - Remove speculative second paragraph.
   - Add quantitative summary and bounded limitations.
   - **Expected impact:** Strengthens scientific writing quality.

### P1 (High priority — strongly recommended)

5. **Reduce novelty claim strength (Key Issue 3)**
   - Replace "first to successfully adopt" with a defensible positioning statement.
   - Expand comparison with Nakano et al. (2024) in related work.
   - **Expected impact:** Avoids desk-reject-level overclaiming.

6. **Quantify annotation cost (Weakness 3)**
   - Add annotation time estimates.
   - Include sensitivity analysis in main text (currently Appendix E.2).
   - **Expected impact:** Demonstrates transparency about practical limitations.

### P2 (Nice-to-have — quality improvement)

7. **Add computational cost analysis**
   - Runtime and memory comparison across configurations.

8. **Expand object feature validation**
   - Reconstruction experiments on multi-object environments.

9. **Reorganize MBRL related work**
   - Group by design philosophy rather than chronology.

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory

| Exp ID | Objective/Hypothesis | Setup (data/split/protocol/baselines) | Metrics | Main Outcome | Claim Supported | Current Limitation |
|--------|---------------------|---------------------------------------|---------|--------------|-----------------|-------------------|
| E1 | Atari 100k benchmark comparison | 26 Atari games, 100k steps, 5 seeds, mean over 20 eval episodes. Baselines: IRIS, DreamerV3, STORM, DIAMOND, STORM* | Mean/median HNS, per-game score | OC-STORM outperforms STORM* on 18/26 games; mean HNS 134.8% vs 114.2% | C3 (performance gain) | No variance reported; STORM* discrepancy unexplained |
| E2 | Hollow Knight boss comparison | 6 bosses, 100k steps, 3 seeds, 20 eval episodes. Baseline: STORM* | Episode return, win rate (WR) | OC-STORM improves return on 6/6 bosses, WR on 4/6 | C3 (performance gain) | Custom reward function different from prior work; only 3 seeds |
| E3 | Object representation completeness (Sec 5.1) | Atari Boxing, 4-layer ConvTranspose2d decoder, 10k train / 1k val frames | Reconstruction quality (qualitative) | Features capture position and state | C1 (feature sufficiency) | Only tested on 2-object Boxing |
| E4 | Vector vs mask ablation (Sec 5.2) | Atari Boxing, Pong, Hollow Knight Hornet, Mantis Lords. Config: mask vs vector vs both | Episode return curves | Vector outperforms mask; both modules best | C1 (vector advantage) | Mechanism speculative; no resolution-controlled ablation |
| E5 | Attention vs MLP policy (App E.1) | Atari Boxing, Pong (object module only) | Episode return, episode length | MLP avoids local optima (Pong scoring phase) | Design justification | Limited to 2 games |
| E6 | Annotation count sensitivity (App E.2) | Atari Boxing, Pong (object module only) | Episode return curves | More masks → more robust performance | Pipeline robustness | Only 2 environments |
| E7 | Segmentation error robustness (App K) | Atari Boxing, Pong with feature zeroing at varying probabilities | Episode return curves | Performance degrades gracefully with zeroing probability | Pipeline robustness | Synthetic noise; not actual Cutie failure modes |
| E8 | Meta-world continuous control (App J) | 4 Meta-world tasks, comparison with MWM and DreamerV2 | Success rate curves | OC-STORM competitive on continuous tasks | Generalization claim | Limited tasks; no comparison with MWM on all tasks |

### Research-Theme Gap Diagnosis

1. **New knowledge gap:** The core claim—that frozen vision model features improve MBRL—is demonstrated empirically, but the mechanism is not isolated. The benefit could come from (a) the object-centric inductive bias, (b) the higher-dimensional input (2048-d per object), (c) the Cutie-specific positional encoding, or (d) the reward shaping (Hollow Knight). Controlled ablations are needed to separate these factors.

2. **Reproducibility gap:** The missing variance information and the unexplained STORM* configuration change make it difficult to assess result reliability. The custom Hollow Knight environment wrapper (Hyper-V, modding plugin) is complex to reproduce.

3. **Impact on practice gap:** The manual annotation requirement (6-12 masks, pre-specify K) limits practical adoption without further automation or guidance on annotation strategies.

### Proposed Research Experiments

**P0 Experiment 1: Reward-shaping-controlled ablation**
- **Target Claim:** Hollow Knight improvement comes from object-centric features (C1/C3)
- **Hypothesis:** OC-STORM outperforms STORM* even under legacy reward (no virtual termination)
- **Minimal Design:** Run OC-STORM and STORM* on Hornet Protector and Mantis Lords using the "legacy" reward scheme (+1/-1, no termination) from Appendix D.4
- **Controls/Baselines:** STORM* with legacy reward, OC-STORM with legacy reward
- **Metrics:** Episode return, win rate
- **Success Criterion:** OC-STORM improves over STORM* under legacy reward
- **Estimated Cost/Time:** ~2 days (2 bosses × 2 configs × 3 seeds)
- **Expected Paper-Quality Gain:** Resolves the most critical confound; if positive, strongly supports the object-centric claim

**P0 Experiment 2: Statistical significance analysis**
- **Target Claim:** All performance claims (C3)
- **Minimal Design:** Compute per-game standard deviations, 95% confidence intervals, and paired bootstrap p-values (OC-STORM vs STORM*) from existing seed data
- **Expected Paper-Quality Gain:** Transforms unverifiable claims into statistically grounded ones

**P1 Experiment 3: Original STORM configuration validation**
- **Target Claim:** OC-STORM improves over original STORM, not just STORM*
- **Hypothesis:** The improvement holds when using the original STORM hyperparameters
- **Minimal Design:** Run OC-STORM with original STORM config (3 layers, 512-dim features) on 5 games where OC-STORM currently shows improvement
- **Expected Paper-Quality Gain:** Removes ambiguity about the STORM* baseline

**P1 Experiment 4: Multi-object reconstruction validation**
- **Target Claim:** C1 (object feature completeness)
- **Minimal Design:** Train ConvTranspose2d decoder on Atari Alien (K=4) and Hollow Knight (K=2-4) to reconstruct observations from object features
- **Expected Paper-Quality Gain:** Strengthens representation completeness evidence

**P2 Experiment 5: Object-agnostic feature comparison**
- **Target Claim:** The object-centric inductive bias is the source of improvement
- **Minimal Design:** Replace Cutie features with randomly projected patches of the same dimension (2048-d) while keeping everything else fixed; compare performance
- **Expected Paper-Quality Gain:** Isolates whether the object-centric structure or the additional capacity matters more

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score: 5.5 / 10**

**Rationale:** The paper addresses a timely problem (object-centric MBRL) and provides a clean integration of modern vision tools (Cutie) with a strong baseline (STORM). The experimental breadth across Atari and Hollow Knight is reasonable. However, the score is constrained by several major issues: (1) the reward shaping confound on Hollow Knight significantly weakens the strongest results, (2) the complete absence of statistical rigor (no variances, no significance tests) makes it impossible to assess the reliability of reported improvements, (3) the novelty claim is overstated and cannot be verified without systematic comparison with closely related work (Nakano et al., 2024), and (4) the manual annotation burden limits practical value. Research value is moderate: the empirical demonstration is useful but the scientific contribution (beyond showing that an existing vision model can be plugged into MBRL) is incremental.

**Post-Revision Target: [6.5, 7.5] / 10**

**Rationale:** If the authors (a) resolve the reward shaping confound by running a controlled ablation with legacy rewards, (b) add variance and significance testing, (c) clarify the STORM* baseline discrepancy, (d) soften the novelty claim to a defensible level, and (e) rewrite the Conclusion to be evidence-grounded, the paper would present a solid empirical contribution. The upper bound (7.5) reflects the paper's potential as a well-executed demonstration of object-centric MBRL integration. The lower bound (6.5) assumes that only the critical fixes (P0 items) are addressed.