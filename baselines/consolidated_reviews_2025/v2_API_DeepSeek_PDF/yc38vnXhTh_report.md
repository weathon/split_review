## Summary
This paper presents **ACTOR**, an LLM-powered agent for simulating high-level, long-horizon human behavior in 3D indoor environments, and **BEHAVIOR HUB**, a large-scale dataset of >10k scene-aware human behavior samples generated via an LLM-based pipeline. ACTOR operates in a perceive-plan-act cycle, using an LLM controller with hierarchical goal decomposition and customizable value functions (real-valued and language-based) to enable active tree search (greedy, beam, MCTS) for behavior planning. The value functions combine commonsense likelihood from the LLM with environment-specific evaluations (e.g., shortest path) and personalized preferences (e.g., "neat person" prompts). BEHAVIOR HUB contains 1k+ daily goals, 15.7 steps on average, spanning 1.5k indoor scenes with aligned motion sequences.

The main contributions are: (1) a value-driven behavior planning framework that integrates LLM reasoning with active tree search and customizable value functions; (2) BEHAVIOR HUB, a large-scale automatically generated benchmark for human behavior simulation; (3) an integrated perceive-plan-act agent architecture for end-to-end 3D human behavior simulation. On the BEHAVIOR HUB benchmark, ACTOR outperforms baselines (LLMaP, HuggingGPT) by nearly doubling Goal Success Rate (0.472 vs 0.317), but a significant gap to human performance remains (human BERT-S 0.959 vs ACTOR 0.879). Human evaluation confirms these trends.

## Strengths
**S1 — Well-motivated problem and holistic framing.** The paper identifies a genuine gap: existing work treats behavior planning (text-based task decomposition) and motion generation (low-level action synthesis) as separate problems, whereas realistic human behavior simulation requires integrated perceive-plan-act loops in dynamic 3D environments. The four barriers (goal achievement, environmental dynamics, behavioral multiplicity, missing testbed) are clearly articulated.

**S2 — Comprehensive dataset contribution.** BEHAVIOR HUB (10k samples, 1.5k scenes, 2k activities, 15.7 avg steps) is an order of magnitude larger than existing human-authored benchmarks like ActivityPrograms/VirtualHome. The automatic data generation pipeline using LLMs with scene-conditioned prompts, combined with motion-scene alignment (MOVER-based optimization + Transformer blending), is a practical approach to scaling behavior data.

**S3 — Modular and extensible architecture.** The ACTOR framework cleanly separates perception (linguistic scene descriptions), planning (LLM + value functions + tree search), and action (off-the-shelf motion generation models). This modularity allows independent improvement of each component, and the ablation study confirms that each module contributes positively. The pluggable value functions (real-valued + language-based) and search algorithms (greedy, beam, MCTS) provide flexibility.

**S4 — Strong empirical results with human validation.** Under the BEHAVIOR HUB benchmark, ACTOR nearly doubles the Goal Success Rate (0.472 vs 0.317) and achieves substantially lower FID (2.087 vs 5.386) compared to strong baselines. The human evaluation (5-point Likert, 5 participants) confirms that ACTOR generates more complete and rational plans than baselines. The downstream task experiment (scene-aware and language-conditioned motion generation) shows that BEHAVIOR HUB benefits other tasks.

**S5 — Transparent documentation of assets and ethics.** The appendix thoroughly documents dataset licenses, consent procedures, and potential negative societal impacts (deceptive virtual characters), with a gated release plan. This level of documentation is commendable.

## Weaknesses
**W1 — Value function composition assumes conditional independence without justification.** The combined value probability is defined as a product of individual value functions (pv = Π_n pv_n). This assumes that different value dimensions (e.g., shortest path efficiency, neat-person preference) are conditionally independent — a strong, unstated assumption. Correlated preferences would produce distorted joint probabilities. The normalization for real-valued functions and the ad-hoc probability mapping for language-based values (sure=1.0, more-likely=0.7, less-likely=0.3, impossible=0.01) are arbitrary and lack calibration.

**W2 — GSRPL metric has an asymmetric path-length bias.** The GSRPL formula uses max(g, l) in the denominator, giving full efficiency credit when the agent's path is shorter than the ground-truth path (l < g → ratio = 1). This fails to penalize implausibly short paths that bypass necessary scene interactions or violate physical constraints.

**W3 — Ablation study lacks statistical rigor and interaction analysis.** The component analysis adds modules cumulatively without testing individual component contributions in isolation or measuring interactions between components. No variance or significance tests are reported, making it difficult to assess whether the observed improvements (e.g., GSR 0.261 → 0.306 for Value Func.) are reliable.

**W4 — LLM-based data generation quality is not externally validated.** The linguistic plan filtering uses BERTScore similarity and LLM self-validation ("Is this a valid plan?"), both of which are weak quality controls. LLM self-assessment is circular — the same model generating the plans evaluates them. No external human validation of plan quality at scale is reported.

**W5 — Perception module is underspecified.** The perception pipeline is described as "readily available models and heuristic functions" without naming specific models, architectures, or processing steps. The mapping from raw scene geometry to structured linguistic descriptions is a critical system component that is not reproducible from the current description.

**W6 — Conclusion lacks limitations and quantitative anchoring.** The conclusion recaps contributions without mentioning any limitations (static object interactions, search depth constraint, cultural bias potential, small rater pool) or key quantitative results (e.g., the human performance gap).

**W7 — Introduction narrative could be sharper.** The opening paragraph lists applications without creating research-gap tension. The four barriers are numbered inconsistently (three then four). The BEHAVIOR HUB paragraph in the introduction is overly detailed, making it read like a method section rather than a motivational narrative.

## Key Issues
**Issue 1 (Major) — Value function product formulation lacks theoretical grounding.** [Severity: Major, Validity Risk: High]
The core planning mechanism combines value probabilities via multiplication (pv = Π_n pv_n). This assumes conditional independence among value dimensions — an assumption that is neither stated nor tested. Correlated preferences (e.g., efficiency and neatness) could be double-counted, producing distorted decisions. Additionally, the probability mapping for language-based values (sure=1.0, more-likely=0.7, etc.) is ad-hoc. Without normalization details or calibration, this fusion mechanism is not reproducible.
- **Evidence:** Page 5 - Value Function paragraph (lines 111-124).
- **Required action:** State the independence assumption explicitly, specify the normalization method, justify the probability mapping, or provide a sensitivity analysis showing that alternative fusion strategies produce similar results.

**Issue 2 (Major) — GSRPL metric asymmetrically handles path length.** [Severity: Major, Validity Risk: Medium]
GSRPL = GSR · g / max(g, l) gives full efficiency credit when the agent's path is shorter than ground truth (l < g). This fails to penalize unrealistically short paths that may bypass necessary interactions or violate scene constraints.
- **Evidence:** Page 8 - Evaluation Metric paragraph (lines 85-88).
- **Required action:** Change to a symmetric ratio (e.g., min(g,l)/max(g,l)) or justify why shorter-than-reference paths should receive full credit, with explicit discussion of when l < g can occur and whether it reflects valid behavior.

**Issue 3 (Major) — Ablation study lacks statistical rigor and interaction testing.** [Severity: Major, Validity Risk: Medium]
The incremental component analysis (Baseline → +Active Search → +Hier. Prior → +Value Func.) cannot separate individual contributions from interaction effects. No variance or significance tests are reported. GSR differences across ablation conditions (e.g., 0.244 vs 0.287 vs 0.306 for search algorithms) could be within noise range.
- **Evidence:** Page 10 - Table 3a-3c and accompanying text (lines 84-93).
- **Required action:** Add at least one cross-ablation (e.g., Value Func. without Hier. Prior). Report means and standard deviations over ≥3 seeds. Report computational budgets for fair search algorithm comparison.

**Issue 4 (Major) — LLM-based data plan quality is insufficiently validated.** [Severity: Major, Research Value Risk: Medium]
BEHAVIOR HUB's linguistic plans are filtered via BERTScore diversity and LLM self-validation ("Is this a valid plan?"). LLM self-assessment is circular and can overestimate quality. The human verification step (§5.2) applies only to motion-scene alignment, not to plan quality. The human evaluation results (Table 2) show that human-written plans are consistently preferred, indirectly confirming quality limitations.
- **Evidence:** Page 7 - Filtering paragraph (lines 155-175) and Page 2 - BEHAVIOR HUB paragraph (lines 88-104).
- **Required action:** Add a human evaluation subset for plan quality in BEHAVIOR HUB. Replace or supplement LLM self-validation with cross-validation against held-out human-authored plans.

**Issue 5 (Major) — Perception module is a black box.** [Severity: Major, Reproducibility Risk: High]
The perception pipeline (§4.1) is described as using "readily available models and heuristic functions" to convert scene geometry into linguistic descriptions. No specific models, architectures, or processing steps are named. This component is critical for the perceive-plan-act loop but cannot be reproduced.
- **Evidence:** Page 4 - Perception paragraph (lines 195-210).
- **Required action:** Specify which models are used (e.g., segmentation model name, spatial relation extractor), provide the prompt templates for converting scene data to text, and release the perception module code.

## Actionable Suggestions
**A1 — Disclose and justify the value function independence assumption (Must).**
In §4.2 (Value Function), add a sentence: "Note that the product formulation p_v = ∏_n p_{v_n} assumes conditional independence among value dimensions. If two values are correlated (e.g., a neat person also prefers efficient routes), the product may over-count shared variance. We adopt this simplifying assumption for modularity and leave learned fusion to future work." Also specify the normalization used for real-valued functions: "Real-valued outputs (e.g., distance) are converted to probabilities via softmax over candidate actions: p_{v_n}(a) = exp(-d_n(a)/τ) / ∑_{a'} exp(-d_n(a')/τ)."

**A2 — Fix the GSRPL metric to handle short paths symmetrically (Must).**
Change the GSRPL definition from GSR · g/max(g,l) to GSR · min(g,l)/max(g,l), or equivalently GSR · (1 - |g-l|/max(g,l)). This ensures that both overly short and overly long paths are penalized. If the original formula is retained, add explicit justification: "g represents the minimum feasible path length under scene constraints, so l < g should not occur in valid simulations."

**A3 — Add cross-ablations and statistical reporting (Must).**
Add at least two additional ablation conditions: (i) "Baseline + Value Func." (without Active Search or Hier. Prior) and (ii) "Baseline + Hier. Prior" (without Active Search). Report all ablation metrics as mean ± std over ≥3 independent seeds with different scene/goal splits. For search algorithms, report total nodes expanded to ensure fair comparison across methods.

**A4 — Supplement LLM-based plan validation with human evaluation (Must).**
Randomly sample 100-200 plans from BEHAVIOR HUB and have 2-3 human annotators rate plan validity (complete, rational, executable). Report the agreement rate between LLM self-validation and human judgments. If agreement is low, adjust the LLM filtering threshold or add a human-in-the-loop verification step.

**A5 — Specify the perception pipeline components (Must).**
In §4.1 (Perception), replace "readily available models and heuristic functions" with specific model names, e.g., "We use a pre-trained Point Transformer for 3D semantic segmentation of the scene geometry, followed by a rule-based spatial relation extractor that computes object proximity and containment relationships. The agent's action history and position are tracked by the simulator state registry. All information is formatted into a language description using the template shown below."

**A6 — Restructure the Conclusion to include limitations and quantitative findings (Must).**
Replace the current conclusion with a three-paragraph structure: (1) validated contributions with key numbers, (2) bounded limitations (static interactions, search depth, LLM validation, indoor-only), (3) specific future work directions.

**A7 — Sharpen the Introduction narrative (Nice-to-have).**
Rewrite paragraph 1 to create research-gap tension before listing applications. In paragraph 2, fix the "three major barriers" numbering (drop (iv) or rename to "three barriers and a practical gap"). Move the detailed BEHAVIOR HUB construction description (paragraph 4) to §5 and keep the introduction focused on motivation and high-level approach only.

**A8 — Add a title that communicates problem + method + outcome (Nice-to-have).**
Current title: "Towards Human-like Virtual Beings: Simulating Human Behavior in 3D Scenes" — consider: "ACTOR: Value-Driven Behavior Planning for Long-Horizon Human Simulation in 3D Environments" to highlight the technical contribution (value-driven planning) and evaluation scope (long-horizon).

## Storyline Options + Writing Outlines
### Current Storyline Analysis
The paper currently uses a "Problem → Four Barriers → Our Solution → Dataset → Results" arc. The main weaknesses are: (1) the opening paragraph lists applications instead of creating research-gap tension; (2) the BEHAVIOR HUB description in the introduction is too detailed; (3) the contribution statement is not sharply delineated from prior work.

### Alternative Storyline Candidate A (Recommended): Gap-First Arc
**Big Picture → Gap → Proposed Method → Key Result → Bounded Impact**

P1 (Opening): "Building autonomous agents that replicate human behavior in realistic 3D environments — from virtual beings to humanoid robots — is a foundational challenge for AGI. While recent progress in vision-language models has enabled isolated capabilities such as low-level motion imitation and short-horizon task planning, no existing system can autonomously execute high-level, long-horizon goals (e.g., 'prepare for work') by integrating perception, planning, and action within dynamic 3D environments."

P2 (Barriers): "Achieving integrated human behavior simulation requires overcoming three interconnected barriers..." (present barriers i-iii clearly, separate dataset gap as a practical obstacle).

P3 (ACTOR): Brief high-level method description (value-driven planning, hierarchical tree, MCTS), mapping each design choice to a specific barrier.

P4 (Dataset): One sentence motivation for BEHAVIOR HUB, then state scale and key statistics.

P5 (Results & Contribution): Quantitative highlights with bounded claims, mention human gap, list contributions.

### Alternative Storyline Candidate B: Capability-Driven Arc
**Current Capability → What's Missing → How We Bridge → Evidence**

P1: Start with the impressive but isolated recent capabilities (motion generation, text planning), use Figure 1 to visualize the fragmentation.

P2: Define the integrated capability target (value-driven, long-horizon, environment-reactive behavior), then show the three barriers plus dataset gap.

P3: Introduce ACTOR as the bridge — each component addresses one barrier.

P4: BEHAVIOR HUB as the enabler for training and evaluation.

P5: Conclude with headline results and limitations.

### Recommended Abstract Outline (4-5 Sentences)
**S1 (Problem & Domain):** "Building autonomous agents that replicate human behavior in realistic 3D environments is a key step toward artificial general intelligence, requiring integration of perception, planning, and action under dynamic environmental conditions."

**S2 (Prior Gap):** "Existing work addresses either low-level motion imitation or short-horizon task planning separately, lacking holistic goal achievement and environment-adaptive behavior."

**S3 (Proposed Method):** "We introduce ACTOR, an LLM-powered agent that uses hierarchical goal decomposition with customizable value functions (real-valued and language-based) to enable active tree search for environment-aware behavior planning in 3D households."

**S4 (Dataset):** "We also contribute BEHAVIOR HUB, a large-scale dataset of over 10k scene-aware human behavior samples synthesized via LLM-based planning and motion-scene alignment."

**S5 (Results & Bounded Claim):** "On our benchmark, ACTOR nearly doubles the goal success rate compared to strong baselines (0.472 vs 0.317), though a significant gap to human performance remains, highlighting the need for further development in value-driven behavior simulation."

### Recommended Introduction Outline (Paragraph-Level)
**P1 — Establish Territory and Gap:**
- Role: Identify the problem and why existing capabilities are insufficient.
- Key claim: No integrated system exists for long-horizon behavior in 3D.
- Evidence: Reference Figure 1 showing fragmentation.
- Transition: "This gap arises from three interconnected barriers..."

**P2 — Define Barriers:**
- Role: Make the research challenge concrete.
- Key claims: (i) holistic goal achievement, (ii) environmental reactivity, (iii) value-guided decisions under behavioral multiplicity.
- Note: Drop barrier (iv) from here; treat dataset gap separately.
- Evidence: Use the "prepare for work" running example throughout.

**P3 — ACTOR Solution Overview:**
- Role: Show how each design choice addresses a barrier.
- Key mapping: perceive-plan-act cycle → (i), dynamic replanning → (ii), value functions → (iii), tree search/MCTS → behavioral multiplicity.
- Tone: Technical but intuitive. Save formula details for §4.

**P4 — BEHAVIOR HUB Motivation and Scale:**
- Role: Explain why a new dataset is needed and how it was built.
- Key claims: LLM-based generation reduces human cost, scene-conditioned prompts ensure grounding.
- One key statistic: "10k+ samples, 1.5k scenes, 15.7 avg steps."

**P5 — Results Preview and Contributions:**
- Role: Give readers the headline evaluation outcome and bounded expectations.
- Key claims: ACTOR nearly doubles GSR, but human gap remains.
- Contribution list: (1) value-driven behavior planning, (2) BEHAVIOR HUB dataset, (3) integrated agent architecture.

## Priority Revision Plan
### Ranked Error Board (Highest Risk First)

| Rank | Issue | Severity | Validity Risk | Fixability | Confidence | Recommended Action |
|------|-------|----------|---------------|------------|------------|--------------------|
| 1 | Value function product assumes independence | Major | High | Easy (disclosure) | High | Add independence caveat + normalization spec (§4.2) |
| 2 | Perception module is a black box | Major | High | Easy (specify) | High | Name models, release perception code (§4.1) |
| 3 | GSRPL metric asymmetry | Major | Medium | Easy (formula fix) | High | Change to symmetric ratio (§5.4) |
| 4 | Ablation lacks statistical rigor | Major | Medium | Medium (re-run) | High | Add variance, cross-ablations, ±3 seeds (§6.2) |
| 5 | LLM data validation is circular | Major | Medium | Medium (add human eval) | Medium | Add human plan quality subset (§5.1/5.2) |

### Revision Order

**P0 (Must — Before resubmission):**
1. Fix value function independence assumption (§4.2) — add disclosure and normalization spec.
2. Specify perception pipeline components (§4.1) — name models, release code.
3. Fix GSRPL formula (§5.4) — change to symmetric ratio or justify current form.
4. Restructure Conclusion (§7) — include limitations and key numbers.
5. Rewrite Abstract — remove anthropomorphic language, add scope boundaries.

**P1 (Must — With new experiments):**
6. Add cross-ablations and statistical reporting (§6.2) — at least 2 new conditions, 3 seeds, std bars.
7. Add human evaluation of BEHAVIOR HUB plan quality (§5.1) — 100-200 samples, inter-rater agreement.
8. Add limitations paragraph to main text (not just appendix).

**P2 (Nice-to-have — Quality improvement):**
9. Sharpen Introduction narrative — gap-first opening, fix barrier numbering.
10. Add cross-ablation showing Value Func. without Hier. Prior.
11. Improve the related work with explicit comparison dimensions against perceive-plan-act predecessors.
12. Update title to communicate technical contribution.

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory

| Exp ID | Objective/Hypothesis | Setup (data/split/protocol/baselines) | Metrics | Main Outcome | Claim Supported | Current Limitation |
|--------|---------------------|--------------------------------------|---------|--------------|-----------------|-------------------|
| E1 | Behavior Planning quality (Main Set) | BEHAVIOR HUB Main Set; 200 held-out goals for prompting + rest for eval; baselines: LLMaP, HuggingGPT | S-BLEU, BERT-S | ACTOR: 0.170 S-BLEU, 0.879 BERT-S vs LLMaP: 0.089/0.825, HuggingGPT: 0.132/0.856 | C1 (value-driven planning) | No statistical significance reported; human performance is higher (0.203/0.959) |
| E2 | Behavior Simulation quality (Main Set) | Same as E1; baselines: HuggingGPT only (LLMaP cannot simulate) | SSR, GSR, GSRPL, FID, Accuracy | ACTOR: GSR 0.472, FID 2.087 vs HuggingGPT: GSR 0.317, FID 5.386 | C1, C3 | Variance not reported; FID computed via pretrained RNN, not direct motion metrics |
| E3 | Environment-aware planning (Dynamic Subset) | BEHAVIOR HUB Dynamic 300 samples with environmental triggers | BERT-S, GSR, GSRPL | ACTOR: BERT-S 0.862, GSR 0.306 vs HuggingGPT: 0.830/0.164 | C1 (environmental reactivity) | Only 300 samples; no analysis of failure cases |
| E4 | Human Evaluation | 5 participants, 5-point Likert on Dynamic subset | Completeness, Rationality, Quality | ACTOR: 3.05/3.47/3.75 vs Human: 4.02/4.85/- | C3 (plausibility) | Only 5 raters; no inter-rater reliability reported |
| E5 | Key Component Ablation | Dynamic subset; incremental addition (Baseline→+Active Search→+Hier. Prior→+Value Func.) | BERT-S, GSR, GSRPL | Improvement from BERT-S 0.811→0.862, GSR 0.140→0.306 | C1 (component necessity) | No cross-ablation; no variance; cumulative only |
| E6 | Search Algorithm Comparison | Dynamic subset; Greedy vs Beam vs MCTS (w=5) | BERT-S, GSR, GSRPL | MCTS best: 0.862/0.306/0.212 | C1 (MCTS effectiveness) | No compute budget comparison |
| E7 | Modular Scalability | Vicuna-7b vs GPT-3.5 vs GPT-4 | BERT-S, GSR, GSRPL | GPT-4 best: 0.862/0.306/0.212 | C3 (scalability) | Only one open-source model tested |
| E8 | Downstream: Scene-aware Motion | Pretrain on BEHAVIOR HUB, finetune/eval on PROX | MPJPE↓, MPVPE↓ | Improvement: 242.50→201.56 (MPJPE) | C2 (dataset utility) | Single baseline; no cross-validation |
| E9 | Downstream: Language-conditioned Motion | Pretrain on BEHAVIOR HUB, finetune/eval on HumanML3D | FID↓, R Precision↑ | Improvement: FID 0.544→0.471, Precision 0.611→0.705 | C2 (dataset utility) | Single baseline |

### Research-Theme Gap Diagnosis

The current experiments demonstrate that ACTOR works better than baselines, but three research-value dimensions remain weakly supported:

1. **New Knowledge (Moderate):** The paper demonstrates that LLM + value functions + tree search outperforms pure LLM planning. However, the ablation cannot separate the contribution of value functions from hierarchical priors (they are added cumulatively). The fundamental question — "Why does MCTS work better than beam search for this task?" — is not analyzed beyond a citation to general MCTS effectiveness.

2. **Reproducibility (Weak):** The perception module is a black box. The value function normalization is underspecified. Code release is promised but not yet available. These gaps substantially reduce reproducibility.

3. **Impact on Practice/Understanding (Moderate):** BEHAVIOR HUB has clear potential for advancing behavior simulation research, and the downstream task results support this. However, the gap between ACTOR and human performance (BERT-S 0.879 vs 0.959) means the current system is not yet practically deployable.

### Proposed Research Experiments

**P0 Experiment — Cross-Ablation for Value Function Isolation**
- **Target Claim:** C1 — Value functions contribute independently of hierarchical priors.
- **Hypothesis:** Value functions provide non-trivial benefit even without hierarchical priors.
- **Minimal Design:** Add two conditions: (1) Baseline + Value Func. (no Hier. Prior), (2) Baseline + Hier. Prior (no Active Search).
- **Controls/Baselines:** Same Dynamic subset, same GPT-4 backbone.
- **Metrics:** GSR, GSRPL, BERT-S.
- **Success Criterion:** Value Func. alone should improve GSR by ≥0.05 over Baseline.
- **Estimated Cost/Time:** Low — requires 2 additional GPT-4 inference runs on 300 scenarios. ~2 GPU-hours.
- **Expected Paper-Quality Gain:** Clarifies whether Value Func. is independently effective or only works with Hier. Prior. Directly addresses Issue 3 (ablation rigor).

**P0 Experiment — Variance Reporting**
- **Target Claim:** All performance claims.
- **Hypothesis:** Results are stable across random seeds and data splits.
- **Minimal Design:** Run ACTOR (full system) and strongest baseline (HuggingGPT) with 3 different seeds on the Dynamic subset. Report GSR as mean ± std.
- **Controls/Baselines:** Same as current.
- **Metrics:** GSR, GSRPL, BERT-S.
- **Success Criterion:** std < 0.03 for BERT-S and < 0.05 for GSR.
- **Estimated Cost/Time:** Low — 3 runs per condition. ~6 GPU-hours.
- **Expected Paper-Quality Gain:** Provides statistical grounding for all reported improvements. Directly addresses Issue 3.

**P1 Experiment — Human Validation of BEHAVIOR HUB Plan Quality**
- **Target Claim:** C2 — BEHAVIOR HUB contains "high-quality" behavior samples.
- **Hypothesis:** LLM-generated plans have ≥80% human approval rate.
- **Minimal Design:** Randomly sample 200 plans from BEHAVIOR HUB. Have 2 independent annotators rate each plan as valid/invalid. Compute agreement with LLM self-validation labels.
- **Controls/Baselines:** Compare against 200 human-authored plans from ActivityPrograms.
- **Metrics:** Human approval rate, Cohen's κ for inter-rater agreement.
- **Success Criterion:** Human approval rate ≥ 80%; moderate agreement (κ ≥ 0.4) between LLM and human labels.
- **Estimated Cost/Time:** Low — 2-3 human annotators, ~4 hours total.
- **Expected Paper-Quality Gain:** Substantially strengthens the dataset quality claim. Addresses Issue 4.

**P1 Experiment — Value Function Fusion Sensitivity Analysis**
- **Target Claim:** C1 — Value function fusion is robust to alternative formulations.
- **Hypothesis:** Different fusion strategies (product vs weighted sum vs learned) produce similar rankings.
- **Minimal Design:** Compare three fusion methods: (a) current product, (b) weighted sum with equal weights, (c) soft mixture with learned gating. Use a held-out validation set of 50 goals.
- **Controls/Baselines:** Current product formulation as baseline.
- **Metrics:** GSR, rank correlation between methods.
- **Success Criterion:** Rank correlation ≥ 0.8 between fusion methods.
- **Estimated Cost/Time:** Medium — requires implementation of alternative fusion and additional GPT-4 API calls.
- **Expected Paper-Quality Gain:** Validates that the key results are not artifacts of the product assumption. Addresses Issue 1.

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score:** 6.5 / 10

**Rationale:** The paper addresses a well-motivated and challenging problem (integrated human behavior simulation in 3D), contributes a large-scale dataset (BEHAVIOR HUB) with practical automatic construction methods, and demonstrates a modular architecture (ACTOR) with reasonable empirical results. However, the score is tempered by five major concerns: (1) the value function formulation has an unstated independence assumption that weakens theoretical credibility; (2) the GSRPL metric has an asymmetric path-length bias; (3) the ablation study lacks statistical rigor and interaction analysis; (4) the perception module is a black box reducing reproducibility; and (5) the LLM-based data validation is circular. The research value (new dataset + integrated framework) is solid but the methodological rigor needs strengthening. Novelty is moderate — the paper combines existing ideas (LLM planning, tree search, value functions) in a new application context but the individual components are not novel in isolation. External literature verification was deferred due to retrieval unavailability.

**Post-Revision Target:** [7.5, 8.0] / 10

**Upgrade path:** If the authors (1) disclose and justify the value function independence assumption, (2) specify the perception pipeline, (3) fix the GSRPL formula, (4) add cross-ablations with variance reporting, and (5) add human validation of BEHAVIOR HUB plan quality, the paper would be substantially stronger. The target range reflects the solid research-value foundation (well-motivated problem, large dataset, modular framework) being reinforced with rigorous methodology and transparent reporting.