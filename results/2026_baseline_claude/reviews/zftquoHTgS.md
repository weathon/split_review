## Summary
SmartSwitch is a training-free, plug-and-play inference framework that addresses the "underthinking" problem in LongCoT LLMs—where models prematurely abandon promising reasoning paths. A Perception module detects thought switches via linguistic cues and scores the preceding thought with a Process Reward Model (PRM); an Intervention module backtracks the generation context and injects a "deepen prompt" when a high-scoring thought was abandoned. Experiments across five DeepSeek-R1-Distill and QwQ-32B models on five math benchmarks show consistent accuracy improvements alongside reduced inference time and response length.

---

## Strengths

- **Well-evidenced problem framing.** The paper defines a quantitative Underthinking Frequency (UF) metric and demonstrates its correlation with task difficulty (Figure 2a) and answer correctness (Figure 2b) across six diverse models. The qualitative example in Figure 1(a) is concrete and memorable.

- **Consistent and substantial empirical gains.** Across all five models (1.5B–32B) and five benchmarks (AIME24/25, AMC23, MATH-500, GaoKao), SmartSwitch yields universally positive improvements, with particularly striking gains on AIME25 (+16.7 pp for 1.5B, +23.3 pp for 7B). Using 32 samples per query ensures stable pass@1 estimates.

- **Simultaneous efficiency improvement.** Tables 2 and 3 show that SmartSwitch reduces both average response length and wall-clock inference time across models—up to −35.3% time for 7B on AIME24—despite adding PRM calls. The interpretation (targeted deepening prunes wasteful shallow exploration) is compelling and well supported.

- **Targeted ablation coverage.** The paper evaluates PRM choice (Table 4), process division strategy (Table 6), score aggregation strategy (Table 7), threshold sensitivity (Table 8), and comparison with standard prompting and TIP (Table 5). Each ablation is informative: for instance, "Always Intervene" degrading below the vanilla baseline directly motivates PRM-guided selectivity.

- **Training-free and model-agnostic design.** No fine-tuning is required; the framework is applied at inference time. The "Boost Performance on Failures without Hurting Successes" analysis (Section 5.3) further confirms that interventions are targeted and do not harm already-correct trajectories.

---

## Weaknesses

### Fatal
None identified.

### Major

1. **Extreme threshold sensitivity with potential test-set leakage.** Table 8 shows an unusually sharp peak at τ=0.70: moving to τ=0.69 or τ=0.71 drops accuracy by 10–13 percentage points for every tested model. This cliff behavior (a single digit in the second decimal place determining success) is atypical for robust hyperparameter design. Critically, the ablation of τ is performed on AIME24—the same benchmark used for the primary comparison in Table 1. If τ=0.70 was selected by evaluating on AIME24, the reported AIME24 numbers in Table 1 are optimistically biased. The AIME25, AMC23, MATH-500, and GaoKao results are not directly affected by this concern and remain credible, but the paper should explicitly state whether τ was chosen on a held-out set or directly on AIME24.

2. **Linguistic-cue detection is model-family specific.** The detection mechanism relies on explicit markers (e.g., "Alternatively"). Models trained to produce LongCoT with such markers (DeepSeek-R1-Distill, QwQ-32B) are naturally compatible, but general-purpose models without these conventions—or those that switch thoughts implicitly—are not covered. The paper presents this as a "plug-and-play" solution, but the mechanism is implicitly tailored to the evaluated model family.

### Minor

1. **UF metric equates token length with underthinking quality.** λ_i(L)=1 iff |T_i| < L is a purely heuristic proxy. A brief but correct derivation step would be flagged as underthinking, while a long but incoherent thought would not. The paper does not validate how well UF correlates with independently judged "premature abandonment," which would strengthen the metric's standing.

2. **Overhead of PRM scoring not characterized in detail.** While wall-clock improvements are reported, the paper does not break down per-call PRM latency or show how overhead scales with intervention frequency. For deployment settings where the PRM and base model must share hardware, the speedup may not materialize equally.

3. **Single PRM with uniform threshold across all model sizes.** Universal-PRM-7B is used with τ=0.70 for all five models ranging from 1.5B to 32B. It is non-obvious that a single PRM calibrated for a particular score scale generalizes uniformly across model sizes; per-model threshold tuning is reasonable but is not explored.

### Trivial
None worth noting.

---

## Nice-to-Haves

- A held-out hyperparameter validation set (distinct from AIME24 and AIME25) would provide clean evidence that τ=0.70 generalizes without test-set tuning.
- An analysis of *which specific linguistic cues* triggered the most interventions, and their correlation with final answer correctness, would strengthen the rationale for cue-based detection.
- Even one non-math domain example (e.g., coding) would support the generalization claim in the conclusion.

---

## Novel Insights

SmartSwitch reveals a counterintuitive property: shallower exploration under LongCoT is not corrected by longer context limits alone—the model repeatedly branches to new thoughts before exploiting high-potential ones. The key observation is that PRM-guided selective interruption with context rollback simultaneously reduces response length and inference time while improving accuracy. This implies that the token budget in failing trajectories is disproportionately spent on low-quality thought-switching overhead, not on deep reasoning—a finding with practical implications for inference-time compute allocation in LongCoT systems.

---

## Suggestions

- Report whether τ=0.70 was selected on a validation split that does not overlap with the reported test benchmarks; if it was tuned on AIME24, exclude AIME24 from the primary Table 1 claim or add a cross-validated sweep.
- Include a brief empirical characterization of PRM call latency and the break-even point (at what intervention frequency does wall-clock time begin to increase) to help practitioners deploy the system.
- Validate UF by having human annotators rate a sample of flagged short thoughts as genuinely "premature" versus "appropriately brief," to establish metric validity independent of downstream accuracy.

---

## Score and Decision

The paper tackles a real and well-characterized problem in LLM reasoning, proposes a clean and practical solution, and supports it with broad, consistent empirical evidence across model scales and benchmarks. The efficiency result (faster and more accurate) is notable. The primary concern—that τ=0.70 was chosen on the same benchmark reported in the main table—warrants scrutiny but does not invalidate results on the other four benchmarks, which collectively make a strong case. The linguistic-cue reliance is acknowledged and is a meaningful scope limitation. Overall, this is a well-executed applied contribution above the ICLR average quality bar.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>