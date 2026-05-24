## Summary

This paper proposes CodeTransformer-GAT, a hierarchical code embedding model that combines token-level transformer attention, function-level graph attention on ASTs, and module-level attention with a code dependency graph, all optimized via policy gradient for RL state representation. The model is evaluated on three code-related RL tasks (code completion, program repair, algorithmic problem solving) with reported improvements over several baselines.

---

## Strengths

- **Concrete multi-level attention architecture**: The paper specifies three attention mechanisms with distinct equations (Eq. 1–3) operating at token, function, and module levels, reflecting the intuition that code understanding requires multiple abstraction levels. An ablation study (Table 2) provides some evidence that each level contributes positively.

- **Empirical comparisons on multiple tasks**: Table 1 reports the proposed model outperforming five baselines (Sequence Transformer, Tree-LSTM, CodeBERT, GNN-CDG, Flat-GAT) on three code tasks, with the largest margins on program repair success rate (+5.7 points) and algorithmic pass rate (+6.2 points).

- **Scalability analysis**: Figure 3 and the accompanying table examine prediction error vs. code complexity, showing slower error growth than two baselines. Memory scaling analysis notes linear (vs. quadratic) growth relative to program size.

---

## Weaknesses

### Fatal

1. **The paper is largely incomprehensible**. Key passages are grammatically broken and semantically confused throughout:
   - Abstract: *"Traditional approaches regularly address code embeddings as flat sequences or to be reliant only on graph-based representations, which don't capture the complex level of interplay between local and global code features."*
   - Introduction: *"Recent progress is being made in code representation learning to demonstrate exciting results with Neural Investigations."*
   - Conclusion: *"The hierarchical cherry-picking of the code embedding system with multi-level attention Research into mechanisms provides major breakthrough..."*
   - Section 4.2: *"The transformer part processes token GAT sequences while the one longer the GAT depends on AST AND code dependency graph (CDG) structures."*
   
   The paper discloses in Section 9 that LLM polishing was used; the result is still barely readable. A paper whose core claims cannot be reliably parsed does not meet the minimum bar for scientific communication. This makes it impossible to conduct a proper technical review.

2. **The RL experimental framework is not properly defined**. The paper claims to evaluate on three RL tasks but never specifies the underlying MDP for any of them. No state space, action space, reward function, or transition dynamics are provided — the entirety of the MDP description is: *"Each task was implemented as a Markov Decision Process (MDP) where states represent the current program state and actions correspond to valid code modifications or additions"* (Section 5.1). The action space is vaguely described as *"token-level edits (insert/replace/delete) and (complexity raising functions, name changes of variables)"* (Section 5.5) — "complexity raising functions" is not defined. Without proper task formulation, the reported RL performance numbers (cumulative reward, sample efficiency) are uninterpretable.

3. **The evaluation lacks basic scientific rigor**:
   - Table 1 reports single-pass numbers with no variance or confidence intervals, despite claiming significance via paired t-tests (p < 0.01) in Section 5.4.
   - Learning curves (Figure 2) show no error bands or confidence intervals.
   - The ablation study (Table 2) is reported for only one task (program repair) with no significance testing.
   - The scalability analysis (Figure 3 and associated table) uses "Baseline 1" and "Baseline 2" without ever identifying which methods they correspond to — an opaque comparison that prevents any meaningful assessment.

### Major

4. **Factual inconsistency in reported results**: The text claims *"a 6.6% absolute improvement in code completion BLEU score"* over CodeBERT, but Table 1 shows 72.9 vs. 68.4, a difference of 4.5 absolute points (6.6% *relative*). Claims of "absolute" vs. "relative" improvement are conflated.

5. **Attribution errors in dataset references**: The paper states *"We used the APPS benchmark (Cui, 2024)"* (Section 5.1), but the cited Cui 2024 paper describes "Webapp1k," a different benchmark. APPS was introduced by Hendrycks et al. 2021 (also cited in the paper), so the attribution is factually incorrect.

6. **Questionable novelty relative to cited prior work**: The paper itself cites Gao et al. 2023 ("SG-Trans") and Zhou et al. 2022 as prior work using hierarchical attention for code. The claimed differentiation — optimizing embeddings for RL — reduces to standard policy gradient (Eq. 6 is generic). The paper does not isolate the effect of RL-specific optimization from the hierarchical architecture, nor does it compare against a version of its own model trained without RL (e.g., supervised only), making it impossible to determine whether the RL component contributes anything beyond the architecture.

### Minor

7. **"CodeBLEU (?)" with a question mark**: Section 5.4 lists "CodeBLEU score (?)" as an evaluation metric, with the question mark presumably indicating uncertainty about the metric definition. This suggests the authors themselves are unsure about their evaluation instrumentation.

8. **"Uniform Attention" baseline not defined**: Table 2 includes a "Uniform Attention" variant achieving 49.8% success rate, but the paper never explains what this baseline is (uniform across all levels? uniform across tokens?). The description in Section 5.2 for "Flat-GAT" — *applying uniform attention across all nodes regardless of hierarchy* — partially clarifies, but the two are apparently different baselines.

### Trivial

- Section 5.5 action space mentions "complexity raising functions" with no definition.
- Section 4.2 has a garbled sentence fragment: "the architecture discussed in Figure 1 How these components interact."
- The reference list is incomplete (truncated in our view) and uses inconsistent formatting.

---

## Nice-to-Haves

- Report results with standard deviations over multiple random seeds (at least 5 runs).
- Provide complete MDP definitions for each task: state space, action space, reward function, and example trajectories.
- Identify "Baseline 1" and "Baseline 2" in the scalability analysis.
- Include a comparison where the same hierarchical architecture is trained without the RL objective (supervised only) to isolate the benefit of RL optimization.
- Provide concrete examples of learned attention patterns (e.g., attention heatmaps for a specific program).

---

## Removed Points

*These points are flagged to be removed; treat them with caution:*

- **Criticisms questioning reference existence** (Gomez et al., 2025 as "not a published paper"; "Park et al., 2025" having "no established venue"; "arXiv preprints that may not exist"). Per policy, all cited references are assumed to exist. **Removed.**
- **Criticism about LLM polishing implying inauthenticity**. The paper transparently discloses this in Section 9; the issue is that even after polishing the writing is poor, not that LLM use is inherently problematic. **Removed** (absorbed into Weakness 1).
- **Criticism about missing appendix/proofs and missing related works**. Per policy, we cannot verify these. **Removed.**
- **Strength Finder claim about "end-to-end optimization for RL objective"** — Eq. 6 is standard policy gradient; the contribution is not novel. **Removed.**
- **Strength Finder claim about "task-adaptive attention patterns"** — evidence is extremely thin (two numbers, 2.1 vs. 3.8 edges). **Removed.**
- **Strength Finder claim about CDG components** — Eq. 7–8 are standard multi-head attention and MLP edge updates. **Removed.**
- **Harsh critic's speculation that baselines are "under-tuned"** — cannot be verified from the paper alone. **Removed.**
- **Discussion (Section 7.2) described as "filler"** — subjective opinion. **Removed.**

---

## Novel Insights

None beyond the paper's own contributions. The reviews surface the same core observation: the paper's contribution (hierarchical multi-level attention for code) is plausible in principle, but the writing is so poor and the experimental framework so incomplete that neither the novelty nor the effectiveness of the method can be properly assessed.

---

## Suggestions

1. **Rewrite the paper from scratch** with a focus on clear, grammatically correct prose. Every sentence should be checked for semantic coherence. The current text is below the minimum readability standard for peer review.
2. **Provide complete MDP definitions** for every task: define the state, action, transition, and reward functions formally. Give a concrete example of a state-action-reward trajectory for one task.
3. **Add error bars and statistical tests** to all quantitative results. Every table and learning curve should reflect variance over multiple independent runs.
4. **Identify all baselines** in every figure and table, including the scalability analysis (Figure 3).
5. **Correct the APPS citation** (attributed to Hendrycks et al., 2021, not Cui, 2024) and the inconsistent "6.6% absolute" claim.
6. **Add an ablation isolating RL optimization** from the architecture by comparing against a supervised-only variant of the same model.

---

## Score and Decision

**Calibration anchors** (all from the deepreview_13k corpus):

| Path | Avg Score | Comparison |
|------|-----------|------------|
| `8QTpYC4smR` (LLM survey) | 1.0 | Pure survey with no contribution. Current paper is slightly better (has equations and results). |
| `Uj0h13lVrR` (GFlowNets) | 1.0 | Reviewer described it as "very difficult to figure out what this paper is trying to do." Similar incomprehensibility. Current paper has more concrete architecture details. |
| `N18Z2MkMEa` (FALCON) | 3.0 | Coherent writing, proper experiments. Current paper is substantially worse on both fronts. |
| `tdbK3TGFl1` (Asymmetric Embeddings) | 3.5 | Has theoretical results and moderate experiments. Current paper lacks theoretical grounding and has weaker experiments. |
| `4ytRL3HJrq` (Nova) | 5.60 | Well-written, comprehensive experiments. Current paper is far below this standard. |
| `ms0VgzSGF2` (Self-Predictive RL) | 6.75 | Strong theory + clean experiments. Far beyond current paper. |

The paper has fatal structural problems — incomprehensible writing, undefined RL experimental framework, and evaluation lacking basic statistical rigor — that collectively prevent it from meeting the bar for acceptance. It is most comparable to the score-1.0 GFlowNets paper in terms of readability issues, but makes a somewhat more concrete attempt at presenting an architecture and results. The paper is substantially weaker than score-3.0 papers (which at least have coherent writing and proper experiments).

MY FINAL SCORE: <score>2.0</score>
MY FINAL DECISION: <decision>Reject</decision>