## Summary

This paper proposes a hierarchical code embedding model with token-level, function-level, and module-level attention mechanisms for reinforcement learning state representation in code-related tasks. The model combines sequential (Transformer) and graph-based (GAT) attention to encode programs at multiple abstraction levels, and is evaluated on code completion (PY150), program repair (ManySStuBs4J), and algorithmic problem solving (APPS). The paper currently reads as an incomplete draft with severe credibility issues: the writing is largely incoherent, experimental results lack any variance reporting, key experimental components are undefined or contain placeholder text, and the limitations section is literally empty.

## Strengths

- **The high-level architectural idea is discernible and reasonable in principle.** Combining token-level, function-level, and module-level attention with both syntactic (AST) and semantic (CDG) graph structure is a plausible direction for code representation, and the three-task evaluation design (completion, repair, algorithmic solving) provides a natural breadth requirement. These strengths are entirely theoretical — the paper fails to deliver on them.

## Weaknesses

### Fatal

None. The paper does not contain a verifiable fatal flaw (e.g., provably incorrect math, contradictory claims) that definitively invalidates the core idea — it is simply too poorly executed to evaluate.

### Major

1. **The paper reads as an incomplete, unpolished draft — not as a finished submission.** Verifiable examples from the paper itself:
   - Limitations section (Section 7.1) contains the verbatim text "Need to discuss several limitations of this study" and nothing else (line 334).
   - The evaluation metrics list includes "CodeBLEU score (?)" — a literal question mark in parentheses (line 210).
   - The conclusion states "The hierarchical cherry-picking of the code embedding system with multi-level attention Research into mechanisms provides major breakthrough" (line 352), which is grammatically and semantically broken.
   - The introduction contains nonsensical phrases: "exciting results with Neural Investigations," "Sequential or Tele-centric analysis," "structural aspects Peps by itself" (line 19), and "making a more complete structural paper than previous graph-based approaches" (line 25).
   - The action space is described as including "(complexity raising functions, name changes of variables)" (line 229) — grammatically broken and unclear.
   
   These are not PDF-extraction artifacts; they are content-level problems that make the paper impossible to evaluate as a scientific submission.

2. **All experimental results are reported without variance or statistical rigor, despite explicit claims of statistical testing.** Table 1 reports single-point numbers for all metrics across six methods with no standard deviations, confidence intervals, or error bars. The same applies to Table 2 (ablation study: single percentages, no standard deviations). Section 5.4 states "All metrics were computed on held-out test sets … with statistical significance tested via paired t-tests (p < 0.01)," yet no actual p-values, test statistics, or any statistical evidence are presented anywhere. This renders the claimed performance differences unverifiable.

3. **Figure 3 uses "Baseline 1" and "Baseline 2" that are never defined in the paper.** Neither the caption, the table below the figure, nor the main text identifies which methods these baselines correspond to. This makes the scalability analysis (Section 6.6) uninterpretable.

4. **The RL formulation is radically underspecified across all three tasks.** Section 5.1 states "Each task was implemented as a Markov Decision Process (MDP) where states represent the current program state and actions correspond to valid code modifications or additions" — this is not a formal definition. No task receives a proper specification of its state space, action space, reward function, discount factor, episode horizon, or transition dynamics. For code completion on a 150K-token vocabulary, what exactly is the action space? For algorithmic problem solving on APPS (generating entire programs), how does an RL agent tractably explore the space of token-level edits? These gaps make the experiments unreproducible in principle.

5. **Baseline implementations are described at a level that makes fair comparison impossible.** Each of the five baselines receives a single sentence of description (Section 5.2). The paper states they were "adapted to output state representations of comparable dimensionality (768-D) and trained with identical RL algorithms for fair comparison" but provides zero detail on: the policy network architecture used with each baseline, hyperparameters (learning rates, batch sizes, network depths), how CodeBERT was fine-tuned with RL (reward modeling, PPO clipping, value head), or whether any baseline-specific tuning was performed. Two baselines ("GNN-CDG" and "Flat-GAT") appear to be author-constructed variants with no implementation details or citations to specific papers.

### Minor

- **The claimed novelty is unclear relative to existing work.** Equations (1)–(4) and (7)–(8) are each standard attention mechanisms (relative positional attention, GAT attention, Bahdanau attention, dot-product attention). The "hierarchical" aspect is applying these different mechanisms at different levels, but the paper does not explain what cross-level information flow exists beyond concatenation in Equation (5), nor does it articulate what architectural innovation distinguishes this from, e.g., running a Transformer encoder and a GAT encoder separately and concatenating their outputs.

### Trivial

None.

## Nice-to-Haves

- The paper claims memory scales linearly with program size (Section 6.6), but provides no actual memory measurements — only a qualitative statement and the uninterpretable Figure 3.
- The ablation study (Table 2) removes entire architectural levels, which changes total model capacity. Isolating the effect of the hierarchical design would require controlling for parameter count.

## Removed Points

These points were removed from the main review with brief justification:

- **"Results are fabricated / AI-generated"** — The harsh critic's strongest characterization. While the paper has severe credibility issues (no variance, placeholder text, unlabeled baselines), the claim of deliberate fabrication is an inference that goes beyond what can be definitively proven from the paper text alone. The verifiable evidence has been retained in Major weaknesses 1–5.
- **"APPS 67.5% pass rate is above what specialized LLMs achieve"** — This criticism relies on external knowledge not present in the paper (exceptional performance does not necessarily indicate fabrication). The core issue (no verification mechanism) is already covered in Major weakness 2.
- **"Suspiciously smooth learning curves"** — The learning curves are described in figure captions but cannot be visually verified from text. Removed as unverifiable speculation.
- **Strength Finder strengths 1–3 and 6** — These strengths (claiming multi-level outperformance, ablation confirms contributions, linear scaling, three-task breadth) rest on trusting the paper's unreported-variance results and undefined baselines. Per the rule: "When a strength and weakness disagree, the weakness wins." Since the paper's results cannot be verified (Major weakness 2), these claimed strengths are invalid.
- **Missing related work** — Per instructions, this cannot be raised without external verification.
- **Formatting/style/typo nitpicks** — Removed per instruction that these are parser artifacts.
- **Reproducibility concerns about undisclosed hyperparameters** — Too generic; the baseline implementation gap (Major weakness 5) already covers this.

## Novel Insights

None beyond the paper's own contributions. The reviews surface no synthesis that meaningfully advances beyond identifying that the paper is an incomplete draft with unverifiable results.

## Suggestions

1. **Complete the paper before submission.** Fill in the empty limitations section, remove placeholder text ("CodeBLEU score (?)"), and proofread the entire manuscript for grammatical coherence.
2. **Report variance for every experimental result.** Provide standard deviations over multiple random seeds for all tables and figures. Report actual p-values if statistical tests are claimed.
3. **Define every baseline unambiguously.** Name "Baseline 1" and "Baseline 2" in Figure 3 explicitly. Provide sufficient implementation detail (architecture, hyperparameters, training setup) for each baseline to be reproduced.
4. **Formally specify the MDP for each task.** For code completion, program repair, and algorithmic problem solving, provide: state space, action space (with vocabulary size where applicable), reward function, discount factor, episode horizon, and termination condition.
5. **Clarify the architectural novelty.** State explicitly what cross-level interactions exist beyond concatenation, and whether the contribution is architectural or lies in the end-to-end RL training of such a multi-level encoder.

## Score and Decision

**Calibration anchors (all retrieved from the corpus):**

| Path | Avg Score | Comparison to this paper |
|---|---|---|
| /home/wg25r/split_review/datasets/deepreview_13k_calibration/N18Z2MkMEa.md (FALCON) | 3.00 | Had unclear writing and weak novelty, but at minimum had a coherent method description with actual experiments on real benchmarks and preserved basic academic writing standards. This paper is substantially worse — it has placeholder sections, nonsensical prose, and unverifiable results. |
| /home/wg25r/split_review/datasets/deepreview_13k_calibration/vLqkCvjHRD.md (RLCF) | 4.75 | Clear writing, well-motivated method, realistic experiments with baselines. This paper is far below this standard. |
| /home/wg25r/split_review/datasets/deepreview_13k_calibration/4ytRL3HJrq.md (Nova) | 5.60 | Well-structured hierarchical attention paper with actual experiments, ablation studies, and clear writing. The contrast in execution quality is extreme. |
| /home/wg25r/split_review/datasets/deepreview_13k_calibration/vfzRRjumpX.md (CodeSage) | 5.75 | Thorough code representation learning paper with comprehensive experiments and clear writing. Not comparable in quality. |
| /home/wg25r/split_review/datasets/deepreview_13k_calibration/OwtMhMSybu.md (RECODE) | 7.33 | Strong RL exploration paper with rigorous experiments. This paper is incomparable in quality. |

MY FINAL SCORE: <score>1.5</score>
MY FINAL DECISION: <decision>Reject</decision>