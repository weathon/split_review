Now I have a thorough understanding of the paper. Let me compose the final consolidated review.

## Summary

This paper introduces Robust Gymnasium, a unified modular benchmark for robust reinforcement learning built on a Disrupted-MDP formulation that jointly models observation, action, reward, and environment disruptions. The benchmark offers over 60 task environments across 11 task bases spanning control, robotics, safe RL, and multi-agent RL, and the paper reports baseline results from several standard and robust RL algorithms. The contribution addresses a genuine gap—the lack of standardized evaluation platforms for robust RL.

## Strengths

- **First unified benchmark covering all major disruption types in a single framework.** The Disrupted-MDP formulation (Sec. 2) jointly models observation, action, reward, and environment disruptors, unlike prior benchmarks that addressed only one type of uncertainty or environment shifts. This is a clear and well-motivated design contribution.

- **Task coverage spans multiple RL paradigms.** The benchmark draws from 11 task bases (MuJoCo, robosuite, Safety-Gymnasium, MAMuJoCo, etc.) covering over 60 tasks across standard RL, safe RL, and multi-agent RL. This breadth is essential for evaluating robustness across different problem classes and is a genuine step beyond existing robustness-focused benchmarks.

- **Systematic benchmarking reveals real deficiencies across paradigms.** Experiments in Sec. 4 show that SOTA robust RL methods (OMPO, RSC, ATLA, DBC) degrade significantly under single-stage disruptions, and standard RL algorithms collapse under post-training disturbances. The LLM-based adversarial disturbance experiment (Sec. 4.5) demonstrates a novel evaluation capability beyond fixed-distribution attacks.

- **Modular and flexible task construction.** Sec. 3.3 describes a clear three-step construction process (select task base → choose disruptor type/mode → specify timing/frequency) enabling systematic ablation studies. The support for multiple simultaneous disruptors and varying operation frequencies adds genuine flexibility.

## Weaknesses

### Fatal
None.

### Major

- **Experimental validation is too narrow to match the paper's own claims of comprehensiveness.** The paper claims "over sixty diverse tasks" and a "comprehensive evaluation" (line 22), but experiments are reported for roughly 7 tasks (HalfCheetah-v4, Ant-v4/v5, Hopper-v5, DoorCausal-v1, LiftCausal-v1, Walker2d, MA-HalfCheetah). For a benchmark paper whose central contribution is a standardized evaluation platform, the reader cannot assess how algorithms perform across the full suite, nor can they use the reported results as reference baselines for most tasks. Figures 5–9 show selected trends, but a systematic table reporting performance across a representative set of tasks (e.g., 15–20 covering different bases and disruption types) is absent. This is the most structurally significant weakness.

- **Inconsistent evaluation protocol prevents cross-paradigm comparison.** The paper introduces two evaluation settings—In-training and Post-training—but applies them arbitrarily: both are used for standard RL (Sec. 4.1), only In-training for robust RL (Sec. 4.2), safe RL (Sec. 4.3), and MARL (Sec. 4.4). Post-training robustness (the more realistic evaluation for deployment) is never assessed for robust, safe, or multi-agent algorithms. This inconsistency limits the benchmark's utility as a fair comparison tool across paradigms.

- **No statistical reliability information.** The paper does not report the number of random seeds, standard errors, or confidence intervals for any experiment. All performance curves (Figs. 5–9) appear to show single runs or point estimates without variability measures. Given the well-known noise in RL results (Henderson et al., 2018; Colas et al., 2018), the reader cannot determine whether observed differences are meaningful. The paper itself cites Colas et al. but does not follow its recommendations.

### Minor

- **Missing systematic comparison to the closest existing benchmark (RRLS).** RRLS (Zouitine et al., 2024) also addresses robustness to environment shifts. The paper mentions it only in passing (lines 20, 78, 84, 109) without a clear contrast of features (e.g., a table comparing supported disruption types, task bases, evaluation modes). A reader familiar with RRLS cannot easily identify what genuinely new capability Robust-Gymnasium provides.

- **LLM adversarial experiment lacks comparison to other learned adversaries.** Section 4.5 compares LLM-generated noise to uniform noise but not to alternative adversarial methods (e.g., a learned adversary from ATLA). This makes it difficult to assess whether the LLM adds value beyond novelty, and the experiment feels disconnected from the main benchmarking narrative.

- **Main text does not adequately summarize task diversity.** The detailed task list is relegated to Figure 17 (appendix, stripped by parser). The body text mentions "over 60 task environments" and "eleven task bases" but never summarizes action spaces, observation types, or how many tasks come from each base. This makes it hard for a reader to appreciate coverage from the main paper alone.

- **No concrete demonstration of modularity.** Section 3.3 describes the three-step construction process conceptually but provides no code snippet, walkthrough, or example of adding a custom disruptor or new task base. This weakens the claim of modularity and raises the barrier for potential adopters.

- **Disruptor frequencies are mentioned but minimally exploited.** The paper describes step-wise and episode-wise disruption timing (Sec. 3.2) but only varies frequency in the LLM experiment (Sec. 4.5, 100F vs. 500F). One systematic experiment varying disruption intervals beyond the LLM setting would strengthen the claim that the benchmark supports multiple time-scales.

### Trivial
None.

## Nice-to-Haves

- A concrete code example (2–3 paragraphs) in the main text showing how to define a custom disruptor and plug it into an existing task would substantially lower the barrier for adoption.
- Testing robust RL algorithms (RSC, OMPO) on observation- and action-disruption tasks (beyond the environment-disruption tasks used in Sec. 4.2) could reveal whether these algorithms' robustness generalizes across disruption types.
- A feature-comparison table contrasting Robust-Gymnasium with RRLS and other related benchmarks would help readers quickly understand the unique value.

## Removed Points

- **"The list of over sixty tasks is relegated to a figure in the appendix"** — The appendix sections were stripped by the PDF parser, not omitted by the authors. However, the core of the criticism (that the main text lacks a summary of task diversity) is retained as a Minor weakness above. The appendix complaint itself is removed.
- **"The paper would also benefit from a short paragraph explaining the key differences [to RRLS]"** — This is subsumed into the Minor weakness about missing systematic comparison; the specific "paragraph" framing is removed as a suggestion style rather than a flaw.
- **"Varying operation frequencies enables disruptors to operate intermittently"** related asks beyond the LLM frequency variation — This was partially addressed in Sec. 4.5 and the remaining scope is moved to Nice-to-Haves.

## Novel Insights

The review process surfaces one insight that goes beyond the paper's own claims: the tension between breadth (60+ tasks) and depth (thorough baselining on all of them) is particularly acute for benchmark papers. The paper's real value lies in the framework's *architecture* and *coverage*, yet the evaluation section reads like a typical algorithm paper that validates on a handful of environments. A benchmark paper may benefit from explicitly scoping what it delivers: extensive benchmarks *of algorithms* versus extensive benchmarks *as a platform*. Here, the platform contribution is strong, but the paper presents it as if the baselining experiments themselves should be the proof of comprehensiveness, which sets an expectation the experiments do not meet. Future benchmark papers in this space should consider separating these two contributions more clearly.

## Suggestions

1. **Add a systematic baseline table** — Provide a table (in the main paper or a clearly referenced supplement) reporting mean return and standard deviation across multiple seeds for every algorithm–task–disruption combination on a representative set of 15–20 tasks spanning different bases and disruption types. This single addition would resolve the narrow-validation weakness and immediately serve as a reference for future work.

2. **State the number of random seeds used and add error bars/shaded regions** to all performance plots. This is essential for RL experiments and is straightforward to add.

3. **Apply the Post-training evaluation protocol to robust, safe, and multi-agent algorithms** to enable fair cross-paradigm comparison. At minimum, note explicitly which algorithms are evaluated under which protocol and why.

4. **Add a feature-comparison table with RRLS** and other robustness-related benchmarks to clarify the paper's specific contributions.

5. **Include a short code snippet or pseudocode** demonstrating how to define a custom disruptor and construct a Robust-Gymnasium task, to substantiate the modularity claim.

## Score and Decision

The paper addresses a genuine and important gap, and the Disrupted-MDP framework is well-designed. The potential impact is high. However, the experimental validation is too narrow to support the claimed comprehensiveness, the evaluation protocol is inconsistently applied, and the absence of statistical rigor undermines the reliability of the reported results. These are fixable issues, but they require substantial additions. I recommend major revision.

**Originality:** Good — the unified disruption formulation and cross-paradigm coverage are novel.
**Importance of question:** High — standardized robust RL evaluation is a real bottleneck.
**Claims support:** Weak — "comprehensive evaluation" is not supported by the 7-task experimental set.
**Soundness:** Moderate — framework design is sound, but experiments lack statistical rigor.
**Clarity:** Adequate — the main text could better summarize the benchmark's breadth.
**Value to community:** Potentially high, once the experimental scope is expanded.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>