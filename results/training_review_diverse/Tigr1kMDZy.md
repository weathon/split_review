Now I have a thorough understanding of the paper. Let me write the consolidated review.

## Summary

This paper investigates why language models imitate incorrect demonstrations in few-shot classification. It identifies two related phenomena: (1) "overthinking"—when given incorrect demonstrations, the model's accuracy peaks at intermediate layers and degrades in later layers—and (2) "false induction heads"—specific attention heads in later layers that attend to and propagate incorrect labels from previous demonstrations. Through logit lens observations across 11 models and 14 datasets, plus causal ablation studies, the paper shows that removing just 5 such heads reduces the accuracy gap between correct and incorrect prompts by 38.9% on average. The work spans observational (logit lens) and causal (ablation, early-exiting) evidence across multiple model families (GPT-J, GPT2-XL, GPT-NeoX, Pythia, Llama2) and instruction-tuned variants.

## Strengths

- **Identifies and causally validates a specific mechanistic cause of false imitation.** The paper defines false induction heads via three properties (label-attending, class-sensitive, label-promoting) and shows that ablating just 5 such heads reduces the accuracy gap by 38.9% over 14 datasets, with negligible effect on correct prompts and no effect from random-head control ablations (Section 5, Figure \ref{fig:main} right). This goes beyond prior correlational analyses of in-context learning.

- **Introduces overthinking as a phenomenon revealing the temporal dynamics of harmful imitation.** By decoding from intermediate layers with the logit lens, the paper shows that given incorrect demonstrations, early layers consistently outperform the final layer—a pattern replicated across 11 models and 14 datasets (Section 4). This pinpoints *where* in the computation harmful imitation arises, something prior work (e.g., Min et al. 2022) did not address.

- **Demonstrates that late-layer attention heads (not MLPs) drive the effect.** The paper compares ablating full layers, attention-only, and MLP-only, showing that removing attention heads alone recovers almost the full benefit of early-exiting (Table \ref{new-ablations-main-table}). This attribution supports the mechanistic focus on induction-like heads.

- **Extensive evaluation across models, datasets, and prompt variations establishes generality.** The findings hold for 8 pretrained models (GPT-J, GPT2-XL, GPT-NeoX, Pythia variants, Llama2-7B) and 3 instruction-tuned variants, on 14 classification tasks spanning sentiment, NLI, topic classification, and a synthetic dataset, across multiple misleading prompt types (permuted labels, random labels, half-correct labels).

- **Careful control experiments rule out alternative explanations.** The paper tests whether the effect is simply a learned relabeling by replacing permuted labels with semantically unrelated labels ("A" vs. "B"), showing that the ground-truth content of labels matters (Section 6). It also tests random and half-correct labels (Section 3.2) to show overthinking generalizes across misleading prompt types.

## Weaknesses

### Fatal
None.

### Major
None. The paper's core claims—that overthinking exists and is causally attributable to specific late-layer attention heads—are well-supported by converging evidence from logit lens observations, early-exiting experiments, and ablation studies across diverse models and datasets.

### Minor

- **The 38.9% gap reduction is reported without variability metrics.** The headline figure is given as a single average without confidence intervals, standard deviations, or per-dataset ranges. While the appendix (Table \ref{ablation_main_table}, likely a parser omission) presumably contains per-dataset results, the main text should summarize variability—whether the effect ranges from, e.g., 10% to 80% across datasets or is consistently 30–50%. Without this, the reader cannot assess whether the claim is robust or driven by a handful of datasets.

- **Mechanistic verification (attention patterns, class-sensitivity) is only performed on the toy Unnatural dataset.** The prefix-matching score identifies heads on Unnatural, and their causal effect is tested on all 14 datasets. The paper states (line 230–231): "since false induction heads were identified using only the toy Unnatural dataset but affect context-following on all datasets, this implies their behavior generalizes across tasks." This is transparent about the selection, but the mechanistic description (class-sensitive attention) is only visually verified on Unnatural (Figure 5). A brief check—e.g., computing PM scores or attention patterns for the identified heads on one or two non-toy datasets (SST-2, AGNews)—would significantly strengthen the mechanistic claim and rule out the possibility that different heads would be selected on different datasets.

- **Recency effects are not explicitly controlled for in the attention analysis.** The paper does not directly rule out the simpler explanation that identified heads simply attend to the *most recent* label token regardless of class, rather than performing class-sensitive matching. Averaging the PM score over many prompts implicitly handles this (a recency-only head would have near-zero PM score on average), but an explicit control—e.g., comparing attention to same-class vs. different-class labels while controlling for token position or recency—would make the "class-sensitive" label more precise.

- **Overthinking on correct prompts is acknowledged but not deeply analyzed.** The paper notes (Section 6) that even with correct demonstrations, GPT2-XL and other models show some overthinking, described as "a potential misalignment between the pretraining objective and the downstream few-shot task." This is an interesting finding that could complicate the "overthinking" narrative—is overthinking a phenomenon *about false demonstrations specifically*, or a more general artifact of pretraining? The paper correctly scopes its main claims to the false-demonstration setting, but this observation deserves more discussion of whether it represents the same mechanism or a different one.

### Trivial
None.

## Nice-to-Haves

- Report per-dataset scatterplot or confidence intervals for the 38.9% gap reduction figure.
- Correlate per-head PM scores with per-head ablation effect sizes across *all* heads (not just top-5) to tighten the link between the score and causal impact.
- Compute PM scores for the identified heads on 1–2 non-Unnatural datasets (e.g., SST-2, AGNews) to verify that the heads exhibit class-sensitive attention patterns beyond the toy dataset.
- Compare attention to labels after same-class vs. different-class inputs while controlling for recency/position to rule out the simpler "most recent label" explanation.

## Removed Points

These points were raised by reviewers but are removed for the following reasons:

- **Logit lens fragility as a weakness:** The harsh critic correctly notes this is *not* a flaw because the paper's causal ablation evidence is independent of the logit lens. Removed because it is not actually a weakness—the critic states so explicitly.

- **"Table \ref{ablation_main_table} not present in the excerpt":** This is a parser artifact; the table exists in the original submission. The underlying concern (missing variability metrics) is preserved above. The specific observation about the table's absence is removed.

- **Overthinking on correct prompts as an undeveloped point:** The paper already addresses this in Section 6 (Discussion, lines 290–292), describing it as "a potential misalignment between the pretraining objective and the downstream few-shot task." The paper scopes its main findings to the false-demonstration setting. Removed as already addressed.

## Novel Insights

None beyond the paper's own contributions. The reviews largely validate the paper's framing and requests for additional reporting details rather than offering fundamentally new interpretations.

## Suggestions

1. Add per-dataset variability (range, standard deviation, or per-dataset scatterplot) for the 38.9% gap reduction in the main text, not just in the appendix table.
2. Verify attention patterns of the identified false induction heads on at least one non-Unnatural dataset (e.g., SST-2) to confirm the mechanistic claim generalizes beyond the toy setting.
3. Conduct an explicit control for recency in attention—measure whether heads attend to the label following same-class inputs more than to the most recent label token when controlling for position.

## Score and Decision

This is a solid interpretability paper with a clearly scoped contribution. The overthinking phenomenon is convincingly demonstrated across 11 models and 14 datasets with converging observational and causal evidence. The localization to false induction heads is supported by careful ablation studies with proper controls. The weaknesses are minor and addressable (variability reporting, mechanistic verification scope, recency control). The paper makes a genuine contribution to understanding harmful imitation in language models and is likely to be useful to the community.

MY FINAL SCORE: <pineapple>7.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>