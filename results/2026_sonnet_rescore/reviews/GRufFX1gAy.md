## Summary
InnoGym introduces a benchmark (iBench) and execution environment (iGym) for evaluating the *innovation potential* of AI agents. The core idea is to measure agents along two axes — Performance Gain (G) and Novelty (N) — rather than correctness alone. iBench contains 18 curated tasks from real-world engineering and scientific competitions, filtered through a two-stage pipeline from an initial pool of 197 tasks. Experiments across three agent frameworks (MLAB, CODEACT, AIDE) on a 10-task subset reveal that agents frequently generate moderately novel solutions yet consistently fail to exceed human state-of-the-art performance, exposing a robustness-over-novelty gap.

---

## Strengths

- **Principled dual-axis innovation framework**: The paper formalizes innovation as occupying specific regimes in (G, N) space — breakthrough, performance, and conceptual innovation — using clean mathematical definitions (Eqs. 2–3). This is a concrete, usable extension over correctness-only evaluation.

- **Rigorous task curation pipeline**: The 197 → 72 → 18 filtering process, including resource availability checks, evaluator executability/correctness validation, and Pearson ≥ 0.9 / Kendall-τ ≥ 0.8 leaderboard consistency requirements for the performance evaluator, provides a reproducible and transparent basis for iBench.

- **Empirical demonstration of the novelty–robustness gap**: Table 2 shows that agents achieve moderate novelty scores (MLAB mean N = 56.55) while delivering uniformly negative performance gains (MLAB mean G = −24.32), directly instantiating the paper's central diagnostic claim that creativity and robust execution are decoupled in current agents.

- **Clear positioning against prior benchmarks**: Table 1 systematically compares InnoGym against seven closely related benchmarks on multiple dimensions; InnoGym is the only one to collect reference solutions *and* evaluate novelty alongside performance.

- **Unified execution environment**: iGym addresses real gaps in existing SDKs (robust recovery, native concurrency, consistent tool management), making cross-framework comparisons reproducible.

---

## Weaknesses

### Fatal
None.

### Major

- **Novelty metric validation absent from the main text**: The paper's primary differentiator over every existing benchmark is the Novelty metric N. The rubric for computing N (six dimensions on a 0–4 scale, rated by GPT-5 comparing structured strategy representations) is described at a high level in Section 4.1, but *all* reliability evidence — inter-run agreement, sensitivity to prompt phrasing, correlation with expert human judgment — is deferred to Appx. F. For a metric that is the entire value-add over prior benchmarks (Table 1), this is a significant presentational gap. Without at least a summary of key validation results in the main text, readers cannot assess whether the "Eval Novelty ✓" column in Table 1 represents a demonstrated capability or an engineering choice with unverified properties. The main paper should include at minimum: (1) consistency of N across repeated evaluations on the same submission, and (2) an illustrative correlation with expert human ratings on a small sample.

- **Experimental coverage is sparse and unevenly missing**: Only 10 of 18 benchmark tasks are included in the main experiments, and within those 10, failures ("/" entries) are pervasive: CDML and PTTALC return "/" for all three agents; BEETL(MI) returns "/" for CODEACT and AIDE; NPR returns "/" for AIDE; RCIC and BEETL(Sleep) return "/" for MLAB. This means many cells in Table 2 are structurally absent. The paper reports averages in the bottom row of Table 2 without specifying how "/" entries are handled (excluded from denominator, treated as zero?), making cross-agent comparisons on those averages difficult to interpret. For a benchmark paper, demonstrating discriminative value requires a reasonably complete result matrix.

### Minor

- **Analysis section generalized from a single task**: All of Section 4.3 — temporal dynamics of G and N (Fig. 6a), model comparison (Fig. 6b), temperature effects (Fig. 6c), and the solution-space tree (Fig. 5) — is derived exclusively from the Circle Packing problem. Findings are presented in general terms ("G tends to improve over time," "a sweet spot in the mid-temperature range"), but Circle Packing is an atypical task in the benchmark (classical NP-hard, mathematically well-structured, compact solution space). The paper should hedge its generalizations more carefully or provide even one additional task to corroborate the pattern.

- **No validation bar specified for the novelty evaluator**: For the performance metric, the paper sets explicit thresholds (Pearson ≥ 0.9, Kendall-τ ≥ 0.8 with official leaderboard). No analogous quality bar is specified for the novelty pipeline, making it unclear what level of agreement would have caused a task to be excluded for novelty-evaluation failures.

- **Stage 2 task-selection criteria are underspecified**: The Stage 2 description ("prioritizing newer and more representative tasks") does not specify the prioritization rule, making it difficult to assess potential selection bias in the 18 retained tasks.

### Trivial

- The paper reports the best score over three runs without reporting variance or the distribution across runs. For a benchmark aiming to characterize agent capability, this conflates consistent performance with lucky runs. Reporting mean ± std or median alongside the best score would be more informative.

---

## Nice-to-Haves

- Including a scatter plot of (G, N) values across all 10 tasks and all agents in a single figure would more powerfully illustrate the claim that agents cluster in the "low G, moderate N" quadrant, reinforcing the main thesis visually.
- The complex-plane representation in Fig. 5(b) is a creative visualization; extending it to show trajectories across multiple tasks would increase its informativeness beyond Circle Packing.
- Even a 2–3 sentence description of the six rubric dimensions used in the GPT-5 novelty judge would allow readers to form an opinion about construct validity without needing to read the appendix.
- Future-proofing: the paper could briefly acknowledge that novelty scores are tied to specific model versions (Codex, GPT-5) and will need re-calibration as models are updated, which is a practical limitation for longitudinal use of the benchmark.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Harsh Critic: "Exploratory problems excluded creates a mathematical asymmetry."** The paper explicitly states it excludes Exploratory Problems because they "cannot be reliably evaluated" (Section 3). This is a design choice the authors acknowledge, not an oversight. The "+∞" case in Eq. (3) is a completeness term for the formal framework, not a claim that the benchmark implements it. Removed as scope-consistent design decision.

- **Harsh Critic: "Reliability of N is deferred to appendix — this is structurally fatal."** The concern is real and retained as Major, but the word "fatal" is not warranted. The appendix exists (Appx. F), and the main paper gives enough design detail (Agent-as-judge, six dimensions, 0–4 scale, GPT-5, Codex extraction) that the pipeline is understandable. The weakness is the absence of a summary in the main text, not a complete absence of evidence.

- **Harsh Critic: "Reproducing novelty scores will be impossible as model versions change."** This is a future concern, not a verifiable problem with the paper as written. Demoted to Nice-to-Have.

- **Strength Finder: "In-depth analysis validates metric dynamics."** The claim that Section 4.3 "validates" the metrics broadly is overstated — it is an illustration on a single task, not a validation across the benchmark's scope. Removed as a standalone strength; the genuine insight (G/N trade-off over time) is captured as part of the experimental findings.

- **Strength Finder: "Clear positioning against prior work."** Retained as a strength, but the framing that InnoGym is "first" to measure novelty needs to be taken at face value per paper claims.

---

## Novel Insights

The paper's most interesting finding is the specific shape of the agent failure mode: agents generate methodologically diverse solutions (moderate N) while uniformly failing to exceed human SOTA (negative G across the board). This is more informative than a simple "agents aren't good enough yet" finding, because it implies the bottleneck is robust *execution* of novel ideas, not idea generation itself. The complex-plane representation in Fig. 5(b), encoding both G (magnitude) and normalized N (angle), is a genuinely creative visualization idiom for multi-dimensional optimization trajectories that could be broadly useful in the agent-evaluation community beyond this specific benchmark.

---

## Suggestions

1. Add a short (half-page) subsection in the main text summarizing the key reliability results from Appx. F — at minimum, intra-run consistency of N and one illustrative human-correlation data point. This is the single most impactful change.
2. Explicitly state how "/" entries are handled in the Table 2 averages (excluded from denominator? This matters for interpreting cross-agent comparisons).
3. Include the names/descriptions of the six rubric dimensions in the main paper (even a bullet list) so readers can assess construct validity inline.
4. For the analysis in Section 4.3, add at least one supporting data point from a second task (even qualitatively) to prevent over-interpretation of Circle Packing as representative.

---

## Evaluation on Key Axes

**Originality**: Moderate-to-high. Formalizing innovation as a (G, N) dual-axis and building an evaluation infrastructure around it is a concrete, non-trivial departure from correctness-only benchmarks.

**Importance of research question**: High. As AI agents are deployed on scientific and engineering problems, distinguishing methodological novelty from performance tuning is increasingly important.

**Claims well-supported**: Moderate. The performance-related claims (agents underperform human SOTA) are well-supported by Table 2. The novelty-related claims depend on an unvalidated (in the main text) metric.

**Soundness of experiments**: Moderate. The experimental design is reasonable, but coverage gaps (10/18 tasks, pervasive "/" entries, single-task analysis) limit confidence in the broader conclusions.

**Clarity of writing**: Good. The framework is explained clearly; the pipeline description is detailed; the benchmark construction is transparent.

**Value to research community**: High. A reproducible, multi-domain platform for evaluating agent innovation is a meaningful infrastructure contribution, and the benchmark tasks are diverse and challenging.

---

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>

<subscores>
<originality>4</originality>
<importance>4</importance>
<claims_supported>3</claims_supported>
<soundness>3</soundness>
<clarity>4</clarity>
<community_value>4</community_value>
</subscores>