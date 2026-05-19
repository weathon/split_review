- Decision: Reject
- Avg Score: 4.00
- Scores: 3, 3, 5, 5
Now I have a thorough understanding of the paper. Let me produce the final consolidated review.

I've verified all claims against the actual paper text. Here is the analysis:

**Verified (keep):**
- Heuristic planning baseline missing (MAJOR)
- r'/p' values not reported (Minor)
- SMAC only uses MAPPO (Minor)
- Abstract oversells relative to SMAC results (Minor)
- 3 seeds, limited statistical reporting (Minor)
- LBF grid size not specified (Trivial)

**Factually wrong/misread (remove):**
- Claim that "assignment-to-action mapping is not explained" — Section 4.3 clearly defines the assignment set over the action space
- Claim that "Planning Function Generation is underspecified" — Section 4.3 + Algorithm 1 explain the mechanism

---

## Summary

YOLO-MARL proposes a framework that makes a single LLM call per environment to generate a "planning function" — a Python function that assigns high-level tasks to agents based on the global state. During MARL training, agents receive additional reward shaping based on whether their actions align with these assigned tasks. The LLM is never called again during training or execution. The method is evaluated on LBF, MPE, and SMAC with three underlying MARL algorithms (MAPPO, QMIX, MADDPG).

## Strengths

- **One-time LLM interaction eliminates recurrent API cost**: The paper's core design choice — using a single LLM call upfront rather than repeatedly querying during training — is a genuine and well-motivated efficiency advantage over methods that call LLMs at every step (abstract, Section 4, line 135: "less than a dollar per environment"). This directly addresses a practical barrier to integrating LLMs with RL training.

- **Large and consistent gains on a sparse-reward benchmark**: On Level-Based Foraging, YOLO-MARL improves QMIX mean return from 0.38 to 0.78 (105% improvement at 2M steps) and accelerates MAPPO convergence roughly 2× (mean return 0.93 vs. 0.31 at 0.2M steps) (Table 1, Figure 3). These are substantial, unambiguous improvements on a challenging environment where the baseline struggles.

- **Tested across three MARL algorithms**: The framework is evaluated with QMIX, MADDPG, and MAPPO across multiple environments (Sections 5.2.1–5.2.3), demonstrating it is not tied to a single base algorithm. Performance improvements are observed for all three algorithms on LBF and MPE.

- **Ablation studies are informative**: The paper includes three meaningful ablations: (1) removing Strategy Generation degrades planning function quality (Section 6.1), (2) removing State Interpretation causes the LLM to produce erroneous code (Section 6.2, with concrete failure examples), and (3) replacing the planning function with direct LLM-generated rewards yields near-zero returns (Section 6.3). These validate the design choices.

## Weaknesses

### Fatal
None.

### Major
- **Missing baseline: non-LLM heuristic reward shaping.** The paper's stated contribution depends on the LLM's planning/reasoning capabilities adding value. However, there is no comparison against a simple, hand-coded heuristic that provides the same kind of task-based reward shaping (e.g., in LBF: "reward agents for moving toward the nearest food"). Without this baseline, it is impossible to determine whether the observed improvements come from the LLM's reasoning or simply from the presence of additional reward structure during training. Section 6.3 (reward generation without planning) replaces the *environment reward* entirely rather than adding on top of it — a fundamentally different setup that does not answer this question. The paper's central claim about leveraging LLM capabilities would be substantially strengthened by isolating the LLM's contribution through this comparison.

### Minor
- **Abstract overclaims relative to SMAC evidence.** The abstract states YOLO-MARL "outperforms traditional MARL algorithms" across all environments, but the SMAC results only show "comparable results on certain maps" (Section 5.2.3, line 240) with overlapping win-rate curves. The conclusion (line 365) appropriately tempers this to "outperforms or achieve competitive results," but the abstract does not reflect this nuance. This mismatch between headline claim and empirical evidence should be corrected.

- **Reward parameters r' and p' are never disclosed.** Algorithm 1 (line 80) lists r' and p' as hyperparameters, and Section 4.4 describes their role, but their numerical values are never reported for any experiment. These values likely affect the magnitude of improvement and are needed for reproducibility.

- **SMAC evaluation is limited to MAPPO only.** The paper tests QMIX, MADDPG, and MAPPO on LBF and MPE, but only MAPPO on SMAC — the most complex and strategically demanding environment. This limits the generality of claims about compatibility with various MARL algorithms in more challenging settings.

- **Statistical reporting is minimal.** All experiments use 3 seeds. Key claims like "105% improvement" and "2× faster convergence" are based on point comparisons at specific timesteps rather than aggregate metrics (e.g., AUC, final-performance significance testing). With 3 seeds and overlapping ranges in some figures, these claims would benefit from error bars and formal significance assessment.

### Trivial
- The LBF grid size and specific environment parameters (beyond the 2-player, 2-food setting) are not stated in the paper; readers must consult the cited Benchmarking reference.

## Nice-to-Haves
- Adding a heuristic planning baseline (as described under Major weaknesses) would most directly strengthen the paper's claim about the value of LLM planning.
- Disclosing r' and p' values and showing sensitivity to them would improve reproducibility.
- Reporting per-map SMAC results with more granularity (which maps improve, which degrade) rather than the vague "comparable results on certain maps."

## Removed Points
These points are flagged to be removed; treat them with caution.
- *"Planning Function Generation is underspecified; the assignment-to-action mapping is not explained"* — **Removed**: Section 4.3 explicitly defines the assignment set over the action space (line 130: "We define the assignment set T over the action space such that an action can belong to multiple assignments and vice versa") and Algorithm 1 checks `a_i in T_i`. The mechanism is described.
- *"State Interpretation Module requires environment-specific engineering of moderate complexity"* overstatement as a weakness — **Removed/downgraded**: The paper's claim of "only basic background understanding" (line 16) is reasonable for the level of effort required (writing a Python function to parse known observation vector components). Not a meaningful weakness.
- *"No statistical significance or effect size reporting"* criticized as a major gap — **Demoted to Minor**: 3 seeds is standard practice in MARL papers. The concern is noted but does not rise to the level the harsh critic assigns it.
- Several generic area-of-concern sweep criticisms from the harsh critic lack concrete anchors in the paper and are removed.

## Novel Insights
None beyond the paper's own contributions. The two automated reviews provide the expected perspectives: the harsh critic correctly identifies the missing heuristic baseline as the central evaluation gap but overstates several other concerns (e.g., the assignment-to-action mapping is actually explained); the strength finder accurately identifies the one-time LLM cost advantage and the strong LBF results. The key synthesis insight is that the paper's most interesting question — *does the LLM's planning capability provide value beyond what a simple heuristic could?* — remains unanswered by the current experimental design, and this is the single most impactful improvement the authors could make.

## Suggestions
1. **Add a non-LLM heuristic planning baseline.** This is the single most important addition. For each environment, construct a simple, hand-coded mapping from state features to task assignments (e.g., nearest-food assignment in LBF, nearest-landmark in MPE). If YOLO-MARL beats this baseline, the LLM's contribution is demonstrated. If not, the paper's contribution reduces to "reward shaping works," which is already well-known.
2. **Disclose r' and p' values** and ideally include a sensitivity analysis showing how different values affect results.
3. **Tone down the abstract** to match the evidence: "outperforms or achieves competitive results" rather than "outperforms" would accurately reflect the SMAC findings.
4. **Extend SMAC evaluation** to at least one more MAPPO variant or, if computationally feasible, to QMIX on simpler SMAC maps.
5. **Report per-map SMAC results more granularly** (e.g., a table of final win rates with confidence intervals) rather than relying solely on figures with overlapping curves.
