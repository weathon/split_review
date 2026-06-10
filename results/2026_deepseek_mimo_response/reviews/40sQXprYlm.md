Now let me write the final review with all calibration complete.

## Summary
This paper introduces Distributed Neural Architectures (DNA), a framework where tokens follow learned, content-dependent paths through computational modules with routers, unifying Mixture-of-Experts, Mixture-of-Depths, weight sharing, and early exit. The authors train DNA models in vision (ImageNet) and language (FineWeb-Edu), showing competitive performance with dense baselines and rich interpretability of emergent routing patterns — including path specialization, power-law path distributions, and content-dependent compute allocation.

## Strengths
- **Ambitious unification of conditional computing paradigms**: The paper cleanly formulates DNAs as generalizing MoE, MoD, parameter sharing, and early exit (Section 2.1, Eqs. 1–3), with visual evidence in Figures 2 and 6 (bottom panels) that a mixture of all these methods emerges from end-to-end training without explicit structural priors.
- **Rich interpretability analysis across both domains**: Figure 3 shows emergent path specialization where low-rank paths aggregate patches with high-level features (edges, flat colors) and high-rank paths group visually similar patches (brass instruments, puzzle pieces). Section 4.2 documents that router R₁ consistently groups semantically similar tokens (punctuation → M₂₇, word pieces → M₂₉, plural nouns → M₁). The deep-dream routing visualization (Figure 4) is a methodological novelty that reveals what routing decisions encode at each step.
- **Emergent compute allocation correlates with input complexity**: Figure 5 shows high-compute images are texture-rich with intricate boundaries, while low-compute images are visually simpler. In language (Section 4.3), low-compute documents include HTML code, bibliographies, and non-Latin scripts.
- **Competitive language performance**: Table 3 shows top-2 DNA outperforms GPT-2 medium on validation loss (2.674 vs 2.720) and 5/7 downstream benchmarks, despite having fewer non-shared active parameters (266M vs 406M). The interpretability findings — emergent specialization, compute allocation, and structural analysis — are genuinely valuable contributions.

## Weaknesses
### Fatal
None.

### Major
- **Parameter budget asymmetry complicates comparison fairness**: The top-2 language DNA that beats GPT-2 has 603M total parameters vs GPT-2's 406M (49% more) and 433M vs 406M active parameters (7% more). The top-1 language DNA, which matches the 406M active parameter budget exactly, actually underperforms GPT-2 on most benchmarks (Table 3: 2.754 vs 2.720 loss, worse on 5/7 tasks). In vision, top-1 DNA has 34M total vs ViT-small's 22M (54% more) yet underperforms (79.1% vs 79.8%). The paper reports these numbers in Tables 1–2 but does not discuss the implications for comparison fairness. A controlled comparison at matched total parameter budgets would substantially strengthen the feasibility claim.
- **No comparison with MoE or MoD baselines**: The paper positions DNA as generalizing MoE and MoD but does not compare against either at the same scale. Since these are the most directly relevant baselines, a direct comparison would clarify what DNA adds beyond explicit structural priors — particularly whether the emergent routing outperforms purpose-designed routing.
- **No variance estimates**: All results are reported for "the best run" (Section 2.2). Given stochastic routing via hard top-k sampling, single-run results cannot establish whether performance differences (e.g., the 0.046 loss gap between top-2 DNA and GPT-2) are reliable.

### Minor
- **Power-law in vision is structural, not emergent**: Figure 1c states that "the distribution of paths through the random model also follows power-law with exponent −1," matching the trained vision model's exponent. Only the trained language model shows a different exponent (−1.2 vs −1 for random). The paper acknowledges this but still presents the power-law as a headline finding. The vision power-law should be reframed as a structural property.
- **Sparse attention confound not isolated**: When a module receives a subset of tokens, those tokens attend only to each other (Figure 1b caption). This creates data-dependent attention sparsity fundamentally different from dense attention. The paper does not disentangle the effect of routing from the effect of sparse attention, leaving open whether performance gaps are partly due to lost cross-group attention interactions.
- **Lack of ablations over key hyperparameters**: s_max, N_m, and N_b likely significantly affect emergent structure and performance, but no systematic ablation is provided.

### Trivial
- **30% skip comparison baseline**: The shallower GPT-2 baseline (Table 3) reduces depth rather than total parameters. Training GPT-2 with 30% fewer total parameters would provide a more informative comparison.

## Nice-to-Haves
- Add a DNA variant with global attention to disentangle routing from sparse attention effects.
- Compare against a standard MoE or MoD model at the same scale.
- Report mean ± std across 3–5 seeds for key configurations.

## Removed Points
These points are flagged to be removed, treat them with caution.
- Harsh critic's concern that the paper doesn't discuss sparse attention as an architectural difference — the paper acknowledges this in Figure 1b caption as "dynamic (i.e. data-dependent) sparsity." Moved to Minor tier since partial addressal exists but the effect is not isolated.
- Harsh critic's concern about efficiency motivation creating false expectations — the paper explicitly states in footnote 3 that it is "not focused on beating SOTA models" and frames itself as feasibility/concept work. Scope creep.
- Strength finder's power-law as "novel emergent property" — contradicted by the paper's own admission that random models show the same exponent in vision (Section 1, Figure 1c caption).
- Strength finder's claim about cross-model parameter sharing consistency — Section 4.3 reports that for language models, "module reuse is most likely random" and there is "no correlation between two different DNA models," contradicting the universality of this strength.

## Novel Insights
The paper's most novel contribution is the interpretability analysis. The emergent path specialization — patches grouped by visual features routing through shared paths, semantically similar tokens routing to the same modules — is qualitatively different from what is typically observed in MoE or dense models. The deep-dream routing visualization (Figure 4) is a methodological innovation revealing that early routing steps capture texture/edges while later steps capture large-scale features. The finding that random models exhibit power-law path distributions (exponent −1) while training changes the exponent only in language (to −1.2) is a genuinely interesting structural observation. These interpretability insights could drive significant follow-up work even where the evaluation has gaps.

## Suggestions
- **Critical**: Train DNA models and dense baselines at matched total parameter budgets to validate feasibility claims.
- **Important**: Run each key configuration with 3–5 seeds and report mean ± std.
- **Important**: Add a comparison with a standard MoE model at the same scale.
- **Minor**: Reframe the vision power-law as a structural property of the architecture rather than an emergent property of training.
- **Minor**: Ablate over s_max or N_m to show how emergent structure changes with architecture scale.

## Calibration Report

**Round 1 — Bracketing (5.5–7.0)**:
- ViMoE (3.00, Reject): Much weaker — incremental empirical study with no novel insights.
- MOEfication (3.40, Reject): Much weaker — focused sparsification method without interpretability depth.
- Mutual-Inform SMoE (5.75, Reject): Weaker — moderate novelty, poor presentation, no interpretability.
- More Experts Than Galaxies (5.67, Accept): Comparable ambition, but DNA has richer interpretability analysis.
- SMEAR (6.00, Reject): Similar ambition level, but DNA has broader conceptual scope and unique interpretability.
- A Simple Interpretable Transformer (6.00, Accept): Similar evaluation depth but narrower scope than DNA.
- γ-MoD (6.67, Accept): More controlled evaluation but less conceptual novelty; DNA has stronger interpretability.
- Tight Clusters (7.00, Accept): Stronger theoretical grounding and more controlled evaluation.
- MoE++ (8.00, Accept): Clearly stronger — cleaner comparisons, better ablations, clear efficiency gains.

**Round 2 — Narrowing (5.0–7.0)**:
- BEEM (6.25, Accept): Focused method, clear improvements. DNA has broader scope but weaker empirical control.
- Mechanism of Stacked Attention Heads (6.33, Accept): Similar analytical approach, limited scale. DNA has comparable novelty.
- Looking Beyond Top-1 (6.40, Reject): Interesting analysis but evaluation gaps. DNA has comparable weaknesses.
- γ-MoD (6.67, Accept): Best direct comparison — DNA has stronger conceptual contribution and interpretability but weaker evaluation control.

The paper sits between γ-MoD (6.67) and SMEAR/BEEM (6.0–6.25). The interpretability contribution is uniquely strong, but the evaluation gaps (parameter asymmetry, no variance, no MoE/MoD comparison) prevent a higher score. 6.5 reflects this: the interpretability work pushes it above the 6.0 anchors, while the evaluation issues keep it below the 7.0 anchors.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>