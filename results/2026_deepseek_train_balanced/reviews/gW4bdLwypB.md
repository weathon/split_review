## Summary

The paper investigates three multi-objective optimization (MOO) formulations for multilingual multi-task ASR: single-level (VS-ASR), bilevel constrained (VC-ASR), and multilevel (VM-ASR). The central thesis is that separating highly conflicting objectives into different optimization levels improves performance over flattening them. Experiments on CoVoST v2 show VM-ASR consistently outperforms baselines and the two simpler formulations across languages and model scales.

## Strengths

- **Systematic formulation of three MOO frameworks (Section 3)**: VS-ASR, VC-ASR, and VM-ASR are formally defined with clear mathematical formulations (Eqs. 2–5), creating a useful taxonomy that prior multilingual multi-task ASR work had not explicitly laid out. This enables principled comparison and reproducible future work.

- **Consistent empirical gains on CoVoST v2 across languages and model sizes (Tables 1, 2)**: VM-ASR (USA) improves ASR WER by up to 22.3% and S2TT BLEU by up to 27.9% over Two-stage PT+FT on the 100M model, with gains across all five languages tested and at both 58M and 100M scales. The trend that VM-ASR > VC-ASR > VS-ASR holds consistently, supporting the central claim about hierarchical separation.

- **Penalty parameter sensitivity analysis (Tables 3, 4; Finding F4)**: The paper shows that large penalty parameters harm generalization while well-calibrated ones yield measurable improvements (ASR: 8.3%, S2TT: 2.2%), providing a practically useful ablation of a non-trivial hyperparameter.

## Weaknesses

### Major

- **Claim F3 (task-based vs. language-based hierarchy) has no experimental support**: The paper lists "Task-based hierarchy outperforms language-based hierarchy in both efficiency and accuracy" as a main finding (F3, lines 27–28). Remark 1 (line 112) describes language-based MLO as involving English (LibriSpeech) and Chinese (AISHELL) with alternating primary/secondary levels. However, **no experimental comparison between task-based and language-based hierarchies appears anywhere in the paper**. The only hierarchy variants reported are task-based sequences (UAS, USA) in Tables 1 and 2. F3 is presented as a headline contribution with zero comparative evidence — there is nothing to compare against. This is not a missing ablation; it is a claimed finding the paper does not attempt to support with data. Refer to Remark 1 (line 112) for the description and to the experimental sections for the absence.

- **Claimed evaluation scope does not match reported experiments**: The abstract (line 4) and introduction (line 21) claim experiments on LibriSpeech, AISHELL v1, and CoVoST v2. However, Section 5 only reports results on CoVoST v2. The sole reference to the other datasets is (line 162): "Additionally, we performed experiments with a combination of the LibriSpeech and AISHELL datasets" — but **no results, tables, or analysis from these datasets follow**. The claim of "consistent performance gains ... across multiple languages" cannot be verified for English (LibriSpeech) or Chinese (AISHELL). The claimed evaluation breadth is one-third of what is actually presented.

- **Section 5.2 is entirely empty** (lines 186–189): The section titled "CONFLICTING ASR AND S2TT OBJECTIVES" — which should contain the paper's central analysis of the conflict that motivates the entire approach — consists of a heading followed by blank lines and then Section 6. The paper as submitted is structurally incomplete at a critical juncture.

### Minor

- **"Up to" framing inflates perceived gains**: The experimental narrative (lines 182–184) reports improvements as "up to 22.3%" for ASR and "up to 27.9%" for S2TT. However, the paper's own average improvements stated in F2 are 5.6% and 5.9% — roughly a 5× gap for S2TT. While both numbers are present in the paper, leading with peak values in the body text while stating averages only in the findings list is a framing choice that exaggerates the method's typical advantage. A reader skimming the results will come away believing VM-ASR delivers ~20%+ gains.

- **No statistical uncertainty reported**: No standard deviations, confidence intervals, or significance tests accompany any result. Given that MOO training involves dynamic weighting, penalty schedules, and hierarchical optimization — all sources of variance — the reader cannot assess whether reported differences between methods (especially the smaller ones, e.g., VS-ASR vs. VC-ASR) are meaningful or within noise.

- **VC-ASR constraint uses an impractical reference value**: Equation (4) constrains $l_u(\theta) - \min_\theta l_u(\theta) \leq \epsilon$, referencing the global minimum of the self-supervised loss — a quantity unknown during training. The paper does not explain how this is handled in practice (e.g., whether $\min_\theta l_u(\theta)$ is dropped, approximated, or replaced with an empirical proxy).

### Trivial

None.

## Nice-to-Haves

- A comparison against a different MOO gradient aggregation method (e.g., PCGrad or CAGrad replacing MoDo within the same hierarchical formulation) would help isolate whether gains come from the multilevel structure or from the specific MOO solver.
- Reporting per-language results transparently (rather than aggregated "best" and "average" numbers) would help practitioners assess consistency.

## Removed Points

These points from the inputs were removed or downgraded with justifications:

- **"No comparison to alternative MOO algorithms"** (Harsh Critic): The paper's contribution is the MLO formulation structure, not the MOO solver. The comparison would strengthen the paper but its absence is not a core flaw. → Downgraded to Nice-to-Have.
- **"Missing related works on bilevel/multilevel optimization"** (Harsh Critic): The paper cites Miettinen (1999) and relevant speech literature. This criticism is overly broad and not anchored to a specific gap. → Removed.
- **"Baseline descriptions too sparse"** (Harsh Critic): Baselines are described with references to prior publications (Saif et al., 2024; Gong et al., 2022). The description level is within community norms. → Removed.
- **Strength Finder strength #2 ("Clear demonstration that task-based hierarchy outperforms language-based hierarchy")**: Directly conflicts with the verified weakness that F3 has no experimental support. → Removed.
- **Strength Finder strength #5 ("Validation across three benchmark datasets")**: Incorrect — only CoVoST v2 results are reported. LibriSpeech and AISHELL results are absent. → Removed.
- **"No convergence or training dynamics analysis"** (Harsh Critic): Asks for additional analysis beyond the paper's scope; not a weakness of what is on the page. → Moved to Nice-to-Have.
- **"Compute budget for baselines not discussed"** (Harsh Critic): Training costs are reported (lines 166-167). The comparison against baselines' compute is a reasonable request but not a weakness. → Removed.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the paper's structural gaps (unsupported claims, missing results, empty sections) but do not produce any insight about the method or domain that the paper itself does not articulate.

## Suggestions

1. Either report the LibriSpeech and AISHELL results or remove those datasets from the paper's claimed scope (abstract, introduction, F3).
2. Either provide experimental evidence for F3 (task-based vs. language-based hierarchy comparison) or retract this finding — it cannot stand as a claimed contribution without data.
3. Replace the "up to" framing with average improvements as the primary narrative, and report per-language results transparently so readers can assess consistency.
4. Populate Section 5.2 with the analysis it promises, or remove the heading.
5. Add basic statistical uncertainty measures (standard deviations or confidence intervals) to the main results.

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>