Now I have all the information I need. Let me synthesize the final review.

Key points to evaluate:

**Verified weaknesses from the Harsh Critic:**

1. **Core architecture not ablated**: True — no comparison against a model without LS modules trained with the same recipe. This is a significant gap, though the paper cites prior work (xu-etal-2023-condensing) showing hard-gated assignment achieves similar performance to MoE with 4x fewer parameters, providing indirect support.

2. **"Every single translation direction" claim**: True — only group averages are shown. However, the group averages show X-ALMA winning in every group for both directions. Could X-ALMA lose on individual languages within a group? Possibly, but the claim "every single translation direction" could also mean "every direction (en→xx and xx→en)" not "every individual language pair." The wording is ambiguous. Let me re-read: "in every single translation direction on the FLORES-200 and WMT'23 test datasets" — this is ambiguous. It could mean "in all translation directions" (i.e., both en→xx and xx→en) or "in each individual translation direction per language." The claim is at minimum overstrong if not backed by per-language results.

3. **French in Group 4**: True and clearly an error. French is a Romance language. This is a genuine misclassification. However, the impact on model performance is speculative without an experiment.

4. **DPO/SimPO baselines**: The paper actually compares both naive versions (which collapse) and BC-regularized versions (which work much better). The comparison with BC-regularized versions is more fair. ARPO still wins but by smaller margins. The harsh critic's point about misconfigured baselines partially applies to the naive versions, but the paper also provides BC-regularized comparisons. This is partially addressed.

**Points to remove/weaken:**

- "Which loading strategy was used for evaluation?" — Not stated, but this is a minor nitpick about implementation details.
- "τ_θ circular dependency" — This is a common pattern in RL/optimization (policy depends on itself). Not a real weakness.
- "η=1.5 not tuned" — Nitpick about hyperparameter tuning, especially since this is standard practice.
- "Flores-200 dev data in SFT" — The paper explicitly analyzes this in Figure 3 (right), showing Flores dev data provides no significant gain, addressing overlap concerns.
- "SFT data size of 3-7K" — Not a criticism raised but just noting.
- "Parameter size advantage" — This is partially valid but the paper includes Aya-23-35B and Aya-101 which are comparable or larger. The smaller baselines are the best available massively multilingual models.
- "Analyses only on Group 6" — Valid concern about generalizability but the paper explains this choice (most challenging group).

Let me now compose the final review.</think>## Summary

X-ALMA extends the ALMA translation model from 6 to 50 languages using a plug-and-play architecture with language-specific LoRA modules (grouped by linguistic family), a five-stage training recipe (3 pre-training + 2 post-training), and a novel preference optimization method called Adaptive-Rejection Preference Optimization (ARPO) that adaptively scales the dis-preferred loss term based on similarity between preferred and dis-preferred translations. The model achieves the best group-average COMET-22 scores across all 8 language groups on FLORES-200 and all 6 language pairs on WMT'23, outperforming prior multilingual LLMs including Aya-101 and Aya-23.

## Strengths

- **Consistent state-of-the-art group averages across all 50 languages**: Tables 2–4 show X-ALMA achieving the highest COMET-22 scores in every group for both en→xx and xx→en on FLORES-200 and every pair on WMT'23, including outperforming models that focus only on high-resource languages (Aya-23-8B/35B) on the "High" subset averages. This is a strong empirical result for a 50-language model.

- **ARPO provides a well-motivated mechanism for over-rejection**: The adaptive penalty τ_θ (Equations 3–5) that scales the dis-preferred term based on log-likelihood similarity between y_w and y_l is a concrete, clearly defined mechanism. Table 5 shows ARPO maintains stable BLEU (27.8) while DPO+BC (23.5) and CPO (22.2) still suffer BLEU drops, and ARPO achieves the highest COMET-22 (90.6) and XCOMET-XL (81.3). The improvement over CPO is consistent across metrics.

- **Multi-stage training recipe validated by ablation**: Figure 3 (left) demonstrates consistent, stepwise performance improvement through all five training stages on Group 6, showing no stage is redundant.

- **Practical deployment flexibility**: The three model-loading strategies (single on-demand module, merged model, full MoE) offer genuine flexibility for different memory constraints—a real engineering advantage over standard MoE approaches.

## Weaknesses

### Fatal
None.

### Major

- **Core architecture never ablated against a shared-model baseline**: The plug-and-play LS module architecture is presented as a primary contribution, yet no experiment compares X-ALMA against a single shared model (no LS modules) trained with the same five-stage recipe. The ablation in Figure 4 only removes training stages, not architectural components. The paper cites xu-etal-2023-condensing showing hard-gated assignment can match MoE with 4× fewer parameters, but this provides only indirect support for the current design on this task and scale. Without this comparison, it remains unclear whether the gains come from the architecture, the training recipe, or their combination. This is a significant gap for a paper whose architecture design is a stated core contribution.

- **"Every single translation direction" claim unsupported by presented evidence**: The abstract claims X-ALMA "surpasses state-of-the-art open-source multilingual LLMs...in every single translation direction on the FLORES-200 and WMT'23 test datasets." Tables 2–4 only report group averages ("All" and "High"), not per-language per-direction results. A model could lose on individual low-resource languages while winning the group average, which would directly contradict the paper's framing of "quality regardless of resource level." Since the paper is released with checkpoints, per-language scores likely exist; their omission from the paper is a substantive evidential gap given the strength of the claim. The claim should either be backed by per-language results or softened to match what is actually shown (group averages).

### Minor

- **French (fr) incorrectly grouped as "Southeast Asian" in Table 1**: French is a Romance language but is placed in Group 4 "Southeast Asian Languages" alongside Indonesian, Malay, Thai, and Vietnamese. This is a factual misclassification in a table whose organizing principle is "Linguistic Feature" and language family. The paper explicitly claims manual grouping "yields more accurate classification" than automated tools (Section 3.2); this error contradicts that claim. The actual impact on model performance is unknown and likely limited (French is high-resource and would presumably learn well regardless), but it undermines confidence in the grouping rationale.

- **All analyses limited to Group 6**: Section 6 states "All analyses will be conducted on languages in Group 6." The preference optimization comparison (Table 5), the ablation study (Figure 4), and the data composition analysis are all on Group 6 only. The paper's core claim covers all 50 languages, and results could differ for lower-resource groups (7 and 8), where ARPO's adaptive rejection dynamics may behave differently with noisier preference pairs.

- **Fairness of preference optimization comparison is partially addressed but still concerns remain**: Table 5 shows naive DPO and SimPO catastrophically failing (BLEU≈0), which the paper uses to illustrate over-rejection. However, the more meaningful comparison is with BC-regularized versions (DPO+BC, SimPO+BC, KTO+BC), where ARPO's advantage narrows considerably (e.g., BLEU 27.8 vs 26.4 for KTO+BC; COMET-22 90.6 vs 90.3 for KTO+BC). The paper does not report hyperparameter tuning efforts for any method including baselines. The naive baseline failures may reflect known sensitivity of DPO/SimPO to the MT setting rather than a fundamental problem, since CPO (which already includes BC) was specifically designed for this domain. The comparison with CPO—the most natural baseline—is the fairest, and ARPO's margin there (90.6 vs 90.2 COMET-22 on en→xx) is modest.

### Trivial
None.

## Nice-to-Haves

- An ablation comparing the LS module architecture against a shared model with the same training recipe would directly test the architectural contribution claim and is the most impactful addition possible.
- Per-language COMET-22 results (even in a table or appendix) would substantiate the "every single direction" claim. Since the model and data are released, these results presumably already exist.
- Correcting the French grouping and reporting any performance change would strengthen confidence in the manual grouping approach.
- Analysis of ARPO on a low-resource-heavy group (e.g., Groups 7 or 8) to verify generalizability beyond the typologically-mixed Group 6.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"Which loading strategy was used for reported results?"** (Harsh Critic Section 3.1): Minor implementation detail; does not affect validity of results. Whichever strategy was used, the reported numbers are what they are.

- **"τ_θ circular dependency / training instability"** (Harsh Critic Section 4): This is a standard pattern in on-policy optimization (policy gradient methods, PPO, etc. all have the policy depend on itself). Not a genuine weakness unless evidence of instability is shown.

- **"η=1.5 not ablated"** (Harsh Critic Section 4): Trivial hyperparameter nitpick. The paper sets both η and β, and single-value hyperparameters are standard.

- **"Flores-200 dev/test overlap"** (Harsh Critic Section 5.1): The paper explicitly addresses this in Figure 3 (right), showing Flores dev data provides no significant gain over NTREX+WMT, directly testing the overlap concern. The harsh critic ignored this analysis.

- **"Preference data noise from reference-as-preferred"** (Harsh Critic Section 5.1): The paper acknowledges this and provides a reasoned justification (avoiding metric bias). This is a known tradeoff, not an unaddressed weakness.

- **"Parameter size advantage over smaller baselines"** (Harsh Critic Section 5.3): The paper includes Aya-23-35B and Aya-101 as comparably-sized or larger baselines. Criticizing comparison with smaller models is unfair when the paper also includes larger ones. Per the hard rules, if the comparison asymmetry is unfavorable to the author's method (i.e., the author includes larger baselines too), this is not a valid criticism.

- **"NLLB-3.3B is a particularly small baseline"**: Same reasoning as above—the paper includes larger baselines as well.

- **"Missing per-language, per-direction results" as a demand for a 50×2 matrix**: This is a valid concern about the claim, but rephrased as a demand for all per-language results is too strong. Included as a major weakness above in more measured form.

- **"Pseudo-monolingual stage underspecified"** (ratio, order, why random): Minor implementation detail; the paper describes the construction method clearly enough to reproduce.

- **"Missing translation examples for over-rejection"**: Nice-to-have but not a weakness; the paper provides quantitative evidence.

- **Strength Finder claim "ARPO effectively addresses over-rejection with strong empirical evidence"**: Partially conflicts with the verified weakness that the DPO/SimPO naive baselines may be unfairly configured. The ARPO vs CPO comparison (the fairest) shows a more modest advantage. I kept a modified version of this as a strength but noted the qualification.

- **Strength Finder claim "Breaks the curse of multilinguality"**: Too strong without the architecture ablation. Modified to reflect what is actually shown (group average performance).

## Novel Insights

The French misclassification in Group 4 ("Southeast Asian Languages") is not just a cosmetic error—it reveals a tension in the paper's design philosophy. The paper argues manually curated grouping by linguistic family is superior to automated tools, yet a basic linguistic error slipped through. More interestingly, French is a high-resource language likely to perform well regardless of its module assignment, which raises the question: does the grouping matter most for high-resource languages (which are robust) or for low-resource languages (which might benefit most from being grouped with typologically similar languages)? This suggests the grouping's value proposition may be asymmetric across resource levels—a nuance the paper does not explore.

## Suggestions

- Run one ablation: train the same 5-stage recipe with a single shared LoRA module (no per-group specialization) on the same 13B backbone and compare against X-ALMA. This single experiment would definitively establish the architecture's contribution and is the most important missing piece.

- Soften the "every single translation direction" claim to "on average across every language group and both translation directions" unless per-language results are provided.

## Score and Decision

Evaluating on the specified axes: **Originality** is moderate—the hard-gated language-specific module idea borrows from xu-etal-2023-condensing, but the 5-stage recipe and ARPO are novel. **Research question importance** is high—scaling multilingual MT without quality loss is a significant problem. **Claim support** is mixed—group-average SOTA is well demonstrated, but the architecture's necessity and the "every single direction" claim are not fully substantiated. **Experiment soundness** is good for the main results but has gaps (no architecture ablation, single-group analyses). **Clarity** is good. **Community value** is strong—released model, data, and a practical deployment framework.

The paper makes real contributions: a strong 50-language translation model, a well-validated training recipe, and a practical plug-and-play architecture. However, the two major weaknesses (no architecture ablation, overstrong "every single direction" claim) are significant but not fatal—the empirical results are strong regardless. The model is released, enabling the community to verify per-language performance independently.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>