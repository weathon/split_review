Now I have sufficient calibration context. Let me write the final consolidated review.

## Summary

This paper investigates whether large language models can mitigate catastrophic forgetting in Graph Continual Learning (GCL). It makes three contributions: (1) identifying a task-ID leakage flaw in the standard GCL evaluation protocol (local testing), where even mean pooling achieves 100% task-ID prediction, (2) introducing LLM4GCL, the first comprehensive benchmark evaluating 9 LLM/GLM-based methods across 7 text-attributed graphs under the more realistic global testing setup, and (3) proposing SimGCL, a method combining graph-prompted instruction tuning with prototype-based classification that achieves strong gains on most datasets but struggles on larger, sparser graphs.

## Strengths

1. **Clean identification of task-ID leakage in local-testing GCL (Section 3.1, Table 1).** The paper provides concrete, unambiguous evidence that the standard local-testing setup in NCIL leaks task IDs: a simple mean-pooling operation achieves 100% task-ID prediction accuracy and 0% forgetting on all 7 datasets, matching the previous SOTA (TPP). This is the first systematic diagnosis of this flaw in the GCL literature and is a genuine, actionable contribution — future GCL work will need to account for this finding.

2. **First comprehensive LLM benchmark for GCL (Section 3.2, Tables 2-4).** The paper evaluates 9 LLM/GLM-based methods across 7 datasets spanning multiple domains, scales, and session configurations under a unified, rehearsal-free protocol. This provides a structured foundation for future research, including scaling analysis (Figure 3), session-length analysis (Table 4), and observations about which method families are viable in GCL.

3. **SimGCL achieves substantial improvements on most datasets (Tables 2, 3).** On 5 of 7 datasets in NCIL, SimGCL outperforms the best GNN baseline (Cosine) by 7–35 absolute percentage points in average accuracy. The improvement over GNN-based SOTA is approximately 20% absolute averaged across datasets, supporting the paper's headline claim. The method's design — first-session LoRA tuning + frozen prototypes — is also computationally efficient.

4. **Systematic analysis of GLM limitations in GCL (Obs. ❸, Obs. ④).** The paper identifies two root causes for GLM underperformance: overfitting to few-shot samples and LLM-GNN representation misalignment, supported by concrete results. This analysis goes beyond mere benchmarking and provides diagnostic insight for future method design.

## Weaknesses

### Major

1. **Missing ablation disentangles graph-prompt from tuning (Section 3.3 vs. SimpleCIL baseline).** SimGCL differs from the SimpleCIL baseline in two uncontrolled ways: (a) it uses a graph-structured prompt encoding neighborhood information, and (b) it performs LoRA-based instruction tuning on the first session (SimpleCIL uses a frozen backbone). The claimed advantage that "graph-structured instruction tuning and prompting framework enhances LLMs' comprehension of graph topology" (Obs. ⑧) is not isolable from the effect of tuning alone. Without ablations — minimally "SimGCL w/o graph prompt" (same LoRA tuning, text-only prompt) and "SimGCL w/o tuning" (graph prompt, frozen LLM) — the paper cannot attribute its gains to graph-structure awareness. This is the most significant weakness, as it undermines the paper's design rationale for the method.

2. **Inconsistent performance and understated limitations (Tables 2, 3, 4).** SimGCL underperforms SimpleCIL on several settings: Arxiv-23 in NCIL (38.7 vs. 52.4 average accuracy), WikiCS in FSNCIL (68.8 vs. 73.2), Arxiv-23 in FSNCIL (31.8 vs. 49.8), and Arxiv in FSNCIL (36.3 vs. 46.4). Under long-session configurations (2W20S on Arxiv, Table 4), SimGCL's final accuracy drops to 17.5 vs. SimpleCIL's 39.1. The paper acknowledges these in passing (Obs. ⑧ bottom) but the abstract and framing ("surpasses by around 20%", "consistently overperform") are misleading. The method has a clear failure mode on larger, sparser, and longer-session settings that is not adequately investigated.

### Minor

3. **No error bars or statistical tests reported.** All results in Tables 2-4 are single numbers. For a benchmark paper, variance across runs is important to assess the reliability of comparisons, especially when margins are small (e.g., SimGCL vs. SimpleCIL on WikiCS in NCIL: 73.5 vs. 71.4, or on Products: 71.1 vs. 66.8). This is a standard expectation for empirical papers in this domain.

4. **No sensitivity analysis of the scaling hyperparameter τ (Equation 2).** The temperature scaling factor τ in the prototype classification could significantly affect results. The paper provides no analysis of how τ was chosen or how sensitive results are to its value.

5. **No runtime or memory comparison.** The paper claims efficiency ("only requires a single round of instruction tuning") but does not report actual runtime, GPU memory, or parameter count comparisons against GNN baselines. For a method that uses an LLM backbone, this is a practical concern for adoption.

### Trivial

6. **The y-axis range in Figure 3 (20–90) compresses visual differences between SimpleCIL and SimGCL, making direct comparison harder than necessary.**

7. **Edge-density statistics are referenced but not tabulated in the main paper.** The paper mentions "dense graph structures" (Obs. ④) but never gives the actual edge densities of the datasets, which would help readers evaluate the claim.

## Nice-to-Haves

- A forgetting metric (e.g., average forgetting ratio) would strengthen the analysis beyond average and final accuracy, especially for diagnosing whether SimGCL's gains come from better retention or better initial learning.
- Analyzing why SimGCL degrades on long-session and sparse-graph settings (e.g., is the LoRA fine-tuning overfitting to the first session's classes?) would turn a weakness into a discovery.
- Equipping GLM baselines with a simple prototype or replay mechanism would provide a fairer comparison and potentially reveal whether the GLM representations themselves are useful for GCL.

## Removed Points

These points from the reviews were flagged for removal with justification:

- **GLM fairness issue (Critic's Point 3):** The critic argued that evaluating GLMs off-the-shelf without CL adaptation is unfair. Removed — standard benchmarking practice is to evaluate existing methods as-is in a new setting. The paper's observation that current GLMs underperform in GCL is a valid finding, not an unfair comparison.
- **"Limited benchmark usefulness beyond critique" (Critic's Point 4):** Removed — the benchmark provides multiple actionable findings (prototype methods work best, scaling helps, GLMs fail, session-length effects), disproving the claim that it lacks clean takeaways.
- **Generic strengths from Strength Finder about "important problem" and "addressed important question":** Removed per instructions — these are superficial and not specific to the paper's concrete contributions.
- **Reproducibility details about missing hyperparameters:** Removed — the paper states these are in the appendix, which is standard practice and the appendix was stripped by the parser.

## Novel Insights

None beyond the paper's own contributions. The reviews did not surface any perspective on the paper that the authors themselves do not already articulate.

## Suggestions

1. **Run the two critical ablations:** (a) SimGCL w/o graph prompt (LoRA tuning with text-only input) and (b) SimGCL w/o tuning (graph prompt, frozen LLM). This will determine whether the graph prompt or the tuning drives the gains, and is essential to support the paper's design narrative.
2. **Add error bars** (at least 3 runs) to all main tables, and report standard deviations.
3. **Tone down the "consistently overperform" framing** and explicitly discuss the failure modes on Arxiv-23, long-session, and sparse-graph settings. Investigate why SimGCL degrades there — is it overfitting to the first session?
4. **Add a table of dataset statistics** (edge density, number of nodes/edges per session) to the main paper to support Obs. ④.
5. **Report runtime/GPU memory** for the major methods (GCN, SimpleCIL, SimGCL, GraphPrompter) to substantiate the efficiency claim.
6. **Analyze sensitivity of τ** (scaling factor in Eq. 2) and state how it was chosen.

## Score and Decision

**Calibration summary:**

- **Round 1 (bracketing):** Queried three bands. Weak anchors: OCGL (2.33), Eidetic Learning (3.25) — these papers lack the empirical contribution and novel finding of the current paper. Middle anchors: Online Continual Graph Learning (5.00), TiC-LM (6.25), CLDyB (5.67), CIL via Likelihood Ratio (6.00). Strong anchors (8.00): top-tier papers with polished experiments and no significant methodological gaps. → **Bracket: 5.0–6.5.**
- **Round 2 (narrowing):** Queried bands (4.5, 6.5) and (6.0, 7.5). Compared against: CLDyB (5.67, accept) — similar structure (critique + benchmark) but CLDyB's contribution is more methodological while this paper's task-ID leakage finding is more concrete. Likelihood Ratio CIL (6.0, accept) — method paper with similar missing-ablation issues but accepted. Is Multitask Learning (5.75, reject) — analysis paper with theoretical contributions. The current paper is stronger than OCGL (5.0) because it has a genuine empirical finding plus a method, and comparable to CLDyB (5.67) and Likelihood Ratio CIL (6.0) in overall contribution. However, the missing ablation (Major weakness 1) prevents it from reaching the 6.0+ tier. → **Final score anchored at 5.5.**

The paper's core finding (task-ID leakage in local-testing GCL) is a genuine and important contribution that will benefit the community. The benchmark is the first of its kind and provides a useful foundation. However, the method's central claim about graph-prompted encoding is unsupported due to missing ablations, and the overselling of "consistent" superiority detracts from what is otherwise a solid empirical study. With the suggested revisions, this paper would be a clear accept.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>