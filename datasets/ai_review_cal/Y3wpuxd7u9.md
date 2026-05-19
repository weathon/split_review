- Decision: Accept
- Avg Score: 6.25
- Scores: 6, 6, 5, 8
I have verified all claims against the paper. Here is my consolidated review.

---

## Summary

GoLLIE fine-tunes a Code-LLaMA model to follow natural-language annotation guidelines for zero-shot information extraction. The input-output format uses Python classes with docstrings and comments to encode guidelines; several regularization techniques prevent the model from shortcutting via label name memorization. Across 18 held-out datasets covering NER, event extraction, and argument extraction, GoLLIE 7B achieves 55.3 average F1, a +13 point gain over the no-guidelines baseline, outperforming prior zero-shot methods including Instruct-UIE and PromptNER.

## Strengths

- **Large, consistent zero-shot gains across diverse tasks and datasets.** Table 3 (lines 244–247) shows GoLLIE 7B achieves 55.3 average F1 vs. 42.3 for the baseline (+13 points absolute), and 58.4 on the SoTA-matched subset vs. 42.6 SoTA average. Gains are positive on nearly every individual dataset, across NER, EE, and EAE, supporting the core claim reliably.

- **Rigorous ablation with p-values identifies representative candidates as the critical component.** Table 4 (lines 285–290) shows removing candidates drops F1 from 55.3 to 49.9 (p=2.2e-10), by far the largest individual effect. Class dropout also reaches significance (54.0, p=0.004). This attributional evidence directly supports the paper's thesis that the guidelines—especially concrete examples—drive the improvement.

- **In-depth error analysis reveals when and why guidelines help or fail.** Section 6 provides per-label analysis (Table 5) with concrete failure modes: ambiguous catch-all labels (*Misc*), conflicts between fine-grained and coarse entities (*Scientist* vs. *Person*), annotations that contradict guidelines (*Time* in MultiNERD), and strong label preconceptions from pre-training. This goes well beyond aggregate reporting and demonstrates genuine understanding of the model's behavior.

- **Broad evaluation spanning 5 IE tasks and 18 held-out datasets** from diverse domains (Twitter, cybercrime, biomedical, science, Wikipedia, search queries) provides thorough empirical grounding. The train/evaluation split carefully avoids domain overlap (Table 1).

- **Honest scaling analysis with cost-benefit discussion.** The paper reports that GoLLIE 34B reaches 60.0 F1 vs. 58.4 for 7B, but notes that "some datasets do not see benefits from increasing the LLM size" and advises weighing performance gains against computational costs.

## Weaknesses

### Fatal
None.

### Major

- **Guideline creation protocol introduces a potential evaluation confound.** The paper states (line 137): "When such guidelines are not publicly available, we ask human experts to create them, based on the annotations from the development split." This means guidelines for some evaluation datasets were reverse-engineered from the very data they are tested on, which could inflate results if the guidelines were inadvertently tuned to the annotation patterns of those datasets. The paper does not (a) specify which evaluation datasets used original guidelines vs. human-created ones, (b) discuss how this might affect the zero-shot interpretation, or (c) provide a restricted evaluation on only originally-available guidelines to verify that gains persist. This is the most significant threat to the paper's central claim and should be explicitly addressed and controlled for.

### Minor

- **Several regularization components lack statistically significant effects.** The ablation (Table 4) shows that class order shuffling (p=0.072, F1 *increases* when removed), paraphrasing (p=0.11), and class name masking (p=0.10) do not produce statistically significant drops at the 0.05 level. The paper acknowledges this ("seem to have no significant contribution to the final result," line 299), yet still includes all five components in the final method and describes them as measures that "stop the model from... attending only to the label names" (line 87). While harmless, describing multiple ineffective components as essential overstates the precision of the method.

### Trivial
None.

## Nice-to-Haves

- Restricting evaluation to datasets with *originally published* guidelines (e.g., CrossNER domains, MultiNERD, MIT Movie/Restaurant) and showing the same pattern of gains would directly address the main concern about confounded guideline creation.
- Specifying which ablation removes yielded positive vs. negative effects on individual datasets could clarify whether the non-significant components cancel out or are truly inert.

## Removed Points

The following criticisms from the inputs were reviewed and excluded with justification:

- *Claim that shuffling, paraphrasing, and masking all yield p-values > 0.10.* — This is factually imprecise. The actual p-value for removing shuffling is 0.072 (not > 0.10). The broader point about statistical significance is retained as a Minor weakness; the specific numerical claim is removed.
- *SoTA comparison precision complaint* (that the "Average SoTA" of 42.6 excludes datasets without reported SoTA). — This is a standard way to compute an average over available data; the per-dataset comparisons are clear either way, and GoLLIE outperforms all listed SoTA entries individually. No actual problem exists here.
- *Missing comparison against a version with guidelines but without fine-tuning.* — The paper already compares against PromptNER (GPT-3.5 with Chain-of-Thought using definitions) in Figure 1 and Section 5, showing that even 175B models with guidelines underperform (~20 F1). This comparison exists and is unfavorable to the critic's suggested alternative.
- *Several generic "strengths" from the Strength Finder* — statements such as "this paper addressed an important problem" or generic praise without specific evidence were dropped per the filtering instructions.
- *Missing related works* — not included per protocol (no external confirmation source).

## Novel Insights

None beyond the paper's own contributions. The reviews surface one genuinely insightful observation not systematically explored in the paper: the guidelines used in evaluation may differ in quality and origin (original vs. human-created), and the paper could strengthen its claims by disentangling these cases. This is a limitation the paper should address but does not invalidate the core finding.

## Suggestions

1. **Disentangle guideline origin.** Report which evaluation datasets had original guidelines and which used human-created ones. Recompute zero-shot F1 separately for each subset to demonstrate the method's robustness independent of the creation protocol. If the gap is small or favors original-guideline datasets, this directly neutralizes the main concern.
2. **Simplify the regularization pipeline.** Given the ablation results, consider dropping or downplaying class order shuffling, paraphrasing, and masking, or explain why they are retained despite non-significant average effects (e.g., regularization against specific failure modes not captured by aggregate F1).
3. **Acknowledge the guideline creation limitation explicitly in the conclusions** and discuss whether it could affect the zero-shot interpretation.
