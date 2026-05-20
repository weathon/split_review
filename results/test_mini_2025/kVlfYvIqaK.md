Now I have all the data I need. Let me write the consolidated review.

## Summary

This paper proposes DyGPrompt, a prompt learning framework for dynamic graphs that addresses the gap between pre-training (link prediction) and downstream tasks (node classification and link prediction). The framework introduces (1) dual prompts — a node prompt and a time prompt — to bridge both task objective and temporal discrepancies, and (2) dual condition-nets (time-conditioned node prompts and node-conditioned time prompts) to capture the mutual characterization between node and time patterns. The method is evaluated on four benchmark datasets across multiple backbones, demonstrating substantial improvements over both static graph prompting methods and the only existing dynamic graph prompting baseline (TiGPrompt).

## Strengths

1. **Novel and well-motivated dual condition-nets for mutual node-time characterization.** The paper identifies that node and time patterns mutually influence each other — an insight overlooked by prior dynamic graph prompting work (TiGPrompt). The dual condition-nets (TCN and NCN) are a principled architectural response to this observation. The ablation provides direct evidence: on Wikipedia node classification, adding both condition-nets to dual prompts (DyGPrompt: 82.09) outperforms dual prompts alone (Variant 4: 72.25), a gain of ~10 AUC points (Table 2).

2. **Strong experimental design with comprehensive evaluation.** The paper evaluates across 4 datasets, 3 tasks (node classification, transductive and inductive link prediction), 6 backbones (DYREP, JODIE, TGAT, TGN, TREND, GraphMixer), and 4 baseline categories. The 100-task × 5-seed protocol (500 trials per setting) provides robust statistics. DyGPrompt achieves best or runner-up performance on all 12 task–dataset combinations in Table 1, often with large margins (e.g., +15–20 AUC points over static graph prompts on Wikipedia/Reddit node classification). The backbone analysis (Table 3) shows DyGPrompt improves the backbone in 49 of 54 comparisons, confirming generality.

3. **Parameter-efficient design.** The condition-nets use bottleneck MLPs (hypernetworks) to generate conditional prompts from input features, avoiding direct parameterization over nodes and timestamps. The sensitivity analysis (Fig. 4) shows stable performance over a range of bottleneck ratios, validating the efficiency–effectiveness trade-off.

4. **Honest treatment of the data-scarce evaluation setting.** The REMARK paragraph transparently acknowledges why conventional DGNN baselines score lower than originally reported — because the evaluation uses a two-stage pre-training + limited downstream data protocol rather than the original setting where models train on data immediately preceding the test set. This contrasts with the many papers that would simply not discuss this discrepancy.

## Weaknesses

### Major

- **Inconsistency between Table 2 ablation and the accompanying text.** The text (Section 5.3) states "Variant 2 (with node prompt) and Variant 3 (with time prompt) outperform Variant 1 (without these prompts)," but the checkmark columns in Table 2 are swapped: Variant 1 has node prompt ✓ while Variant 2 has ✗✗✗✗ (no prompts). This mismatch makes it impossible to cleanly interpret which variant the text refers to. While the numerical patterns still support the paper's overall conclusions (comparing Variant 5 vs Variant 2 shows the benefit of NCN; Variant 6 vs Variant 3 shows TCN's benefit), this error undermines the precision of the ablation narrative and must be corrected. The most likely fix is swapping the checkmarks for Variant 1 and Variant 2 in the node prompt column.

### Minor

- **Missing standard deviations in the ablation table (Table 2).** Table 1 reports standard deviations alongside all results, but Table 2 reports only point estimates. Without error bars, it is difficult to assess whether differences between variants (e.g., Variant 2 vs Variant 3 on Wikipedia: 72.59 vs 73.22) are statistically significant or within noise. The ablation is central to the paper's claims about component importance.

- **Several baselines perform near or below random.** CPDG on Wikipedia node classification scores 43.56% AUC (below random 50%), and several other baselines hover near 50% on specific settings. While the paper acknowledges that conventional DGNNs underperform in this data-scarce protocol, it does not discuss whether separate hyperparameter searches were conducted for each baseline under this new setting. This weakens the reader's ability to attribute all performance differences to the method rather than mis-tuned baselines.

- **Typo in Equation (10).** In the neighbor aggregation term, the node-conditioned time prompt for neighbor *u* at time *t'* is written as $\tilde{\mathbf{p}}_{t',v}^{\text{time}}$ but should be $\tilde{\mathbf{p}}_{t',u}^{\text{time}}$ (since the neighbor is node *u*). This appears to be a copy-paste error from the central node term.

- **Variable reuse in Equations (8)–(9).** The output of the node condition-net is defined as $\tilde{\mathbf{p}}_{t,v}^{\text{time}}$ in Eq. (8), then overwritten after element-wise multiplication in Eq. (9). A different symbol for the final adjusted time feature would improve clarity.

### Trivial

- The figure caption for Figure 1 repeats unnecessarily (a parser artifact in the extracted version, but the original should be checked).

## Nice-to-Haves

- A direct visualization of how the time-conditioned node prompts vary across times for a fixed node (or vice versa) would provide more direct evidence that the conditional prompts are capturing the claimed mutual characterization, beyond showing that "the full method works."
- A brief limitations discussion (e.g., reliance on a pre-trained DGNN quality, potential scalability of condition-nets for very large node sets, boundary of the similarity-based template for unusual downstream tasks) would improve completeness.

## Removed Points

The following points from the reviewers have been removed with justification:

- **"Missing code release statement"** (Harsh Critic): The paper does not explicitly commit to code release, but this is a common ask that many accepted papers do not address in the submission itself. It does not affect the scientific evaluation of the paper's content.
- **"Figure 1 caption repeats itself"** (Harsh Critic): This is a parser artifact from PDF extraction; the original formatting is not at issue.
- **"Claim about graph classification being rarely evaluated could use a citation"** (Harsh Critic): The paper already provides citations (Skarding et al., 2021; Pareja et al., 2020; Xu et al., 2020; Chen et al., 2024) in footnote 1.
- **Generic scope-creep suggestions** (Strength Finder strengths about "addressing an important problem"): Removed because these are generic/superficial. Other strengths that are concrete and evidenced are retained.
- **Weaknesses about missing appendix content** (implicit from Harsh Critic): Removed per hard rules — the parser strips these sections; they exist in the original submission.

## Novel Insights

None beyond the paper's own contributions. The reviews surface no novel observations that the paper itself does not already articulate.

## Suggestions

1. Fix the checkmark inconsistency between Table 2 and the ablation text in Section 5.3. This is the most important correction — it currently impairs interpretability.
2. Add standard deviations to Table 2, or at minimum, report statistical significance between key variant pairs.
3. Correct the typo in Eq. (10) ($\tilde{\mathbf{p}}_{t',v}^{\text{time}}$ → $\tilde{\mathbf{p}}_{t',u}^{\text{time}}$) and consider a distinct symbol for the final adjusted time feature in Eqs. (8)–(9).
4. Briefly discuss whether hyperparameter tuning was conducted separately for each baseline under the data-scarce protocol, especially for baselines that perform near or below random.

## Score and Decision

### Calibration Anchors

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|-----------|
| c87QZPTVVm.md (LLM dynamic prompting) | 3.00 | R1 (low) | Unrelated topic (LLM prompting); much lower quality |
| WRKVA3TgSv.md (LLMs modify graphs) | 3.00 | R1 (low) | Unrelated; lower quality |
| ds3Tcnrte8.md (KG prompting for LLMs) | 3.00 | R1 (low) | Unrelated; lower quality |
| 070DFUdNh7.md (GraphGPT) | 4.50 | R1 (mid) | Graph pre-training but with weaker experiments, overclaimed performance; DyGPrompt is stronger |
| 4IT2pgc9v6.md (OFA) | 7.00 | R1 (high) | Broader scope (unified graph model), accepted spotlight; DyGPrompt has cleaner experiments but narrower scope |
| fU8H4lzkIm.md (PhyMPGN) | 8.00 | R1 (high) | Unrelated domain (PDEs); DyGPrompt not comparable |
| G32oY4Vnm8.md (PTaRL) | 8.00 | R1 (high) | Unrelated (tabular); not comparable |
| P7KIGdgW8S.md (Hölder stability of GNNs) | 8.00 | R1 (high) | Theory paper; not comparable |
| gjfOL9z5Xr.md (DyVal) | 6.50 | R1 (mid) | Unrelated (LLM evaluation) |
| 5JOxazmj8b.md (Link Prediction to Forecasting) | 5.50 | R2 (mid-low) | About evaluation methodology; DyGPrompt is stronger |
| mIjblC9hfm.md (GOFA) | 6.50 | R2 (mid-high) | Graph foundation model with LLMs, accepted poster; comparable rigor but DyGPrompt has cleaner experiments |
| ViNe1fjGME.md (Deep Temp Graph Clustering) | 7.33 | R2 (mid-high) | Accepted poster; one reviewer noted limited technical contribution; DyGPrompt has clearer novelty |
| AJBkfwXh3u.md (Causality DyGNN explanations) | 6.00 | R2 (mid-high) | Accepted poster on DyGNN interpretability; different contribution type |

**Round 1 bracket:** 4.5–8.0 (DyGPrompt is clearly above GraphGPT's 4.5 and below the 8-range theory papers).

**Round 2 narrowing:** Compared to GOFA (6.5, accepted poster), DyGPrompt has cleaner, more convincing experiments with better ablation and a more clearly defined contribution. Compared to OFA (7.0, accepted spotlight), DyGPrompt has a less ambitious scope but its experiments are more rigorous and its novelty is clearer (less overlap with prior work). The main issue — the table inconsistency — is readily addressable and does not threaten the core claims. The paper is solidly above the ICLR acceptance threshold.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>