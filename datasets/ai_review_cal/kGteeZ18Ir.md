- Decision: Accept
- Avg Score: 5.75
- Scores: 8, 5, 5, 5
Now I have a thorough understanding of the paper and can verify all reviewer claims against the actual text. Let me produce the final review.

## Summary

This paper presents a large-scale empirical study of how assigning socio-demographic personas (e.g., "an Asian person," "a physically disabled person") to LLMs degrades their reasoning performance across 24 datasets, 19 personas, and 4 LLMs. The core finding is that persona assignment surfaces deep-seated biases that cause substantial accuracy drops — up to 69% relative on some datasets — that manifest both as explicit abstentions (refusing to answer while citing stereotypes) and as implicit reasoning errors that persist even after filtering abstentions. The paper also shows that simple prompt-based de-biasing instructions are ineffective.

## Strengths

- **Largest-scale systematic study of persona-induced reasoning bias**: The paper evaluates 19 diverse personas across 5 socio-demographic groups on 24 reasoning datasets (math, law, medicine, morals, programming, etc.), all under a consistent methodology. This scope is a clear step beyond prior work, which focused on toxicity or harmful text rather than reasoning performance (§2, Tables 1-2).

- **Differentiation between explicit abstentions and implicit reasoning errors**: The analysis in §4 cleanly separates two distinct manifestations of bias — refusals that explicitly cite stereotypes (e.g., 58% of errors for Phys. Disabled) and harder-to-detect implicit reasoning drops that persist even after removing abstained questions (e.g., 39% drop for Obama vs. Trump Supporter on college math). This provides a nuanced picture that goes beyond counting superficial refusals.

- **Empirical demonstration that simple de-biasing prompts fail**: The paper tests three task-agnostic mitigation strategies ("don't refuse," "no stereotypes," "treat as human") and shows they have minimal to no effect; the "treat human" intervention actually worsens bias for some persona pairs (§5, Figure 7). This negative result is valuable because it shows that the bias runs deeper than surface-level alignment can address.

- **Transparent negative results and open data**: The paper honestly reports that the only effective intervention (adding task-specific expertise) is acknowledged as not generalizable. The release of ~1.5 million model outputs enables follow-up work.

## Weaknesses

### Fatal
None.

### Major

- **Cross-model claims outstrip the presented evidence**: The abstract and introduction prominently frame the study as covering "4 LLMs" (gpt-3.5-turbo-0613, gpt-3.5-turbo-1106, GPT-4-Turbo, Llama-2-70b-chat). However, the entire main body (§3 Findings, §4 Analysis, §5 Mitigation) presents results exclusively for the June 2023 ChatGPT. The other three models receive only a few sentences in the Discussion (§6), with no figures, no breakdown comparable to the primary analysis, and no dataset-level comparisons. The paper's headline claim about the "ubiquity" of persona-induced bias *across models* is not proportionally supported. The paper *does* transparently footnote its ChatGPT focus (footnote 3, line 26), but the abstract and conclusion still assert the claim broadly. This is fixable by restructuring: either treat the paper as explicitly about ChatGPT with supplementary cross-model evidence, or move at least one additional model's full results into the main body.

- **Multiple hypothesis testing is not addressed**: The paper performs a very large number of statistical tests across 19 personas × 24 datasets × 3 instructions (plus pairwise comparisons across groups), using Wilson's confidence intervals at α=0.05 without any correction for multiplicity (line 54). Under standard α=0.05, roughly 5% of null tests would flag as significant by chance. Figures 2-4 report counts of "statistically significant" drops. While the very large effect sizes (e.g., 69% drops) are clearly real and would survive correction, the paper's numerical claim that "80% of personas demonstrate bias" could be somewhat inflated if it depends on counting any significant drop on at least one dataset. The authors should apply a correction (e.g., Benjamini-Hochberg) and report how many significant drops survive. This is an evidential rigor issue rather than a fatal one — the core finding of widespread bias is unlikely to collapse — but it undermines the precision of the reported statistics.

### Minor

- **"Average Human" baseline is interpretively ambiguous**: The paper treats "Average Human" as a neutral reference point and uses language like "sub-human performance" (line 75-76) and "worse than an average human" for certain personas. However, the "Average Human" is itself a model-constructed persona whose properties are not independently validated. The model's default conception of "average human" may reflect its own biases (e.g., able-bodied, male, educated). Comparing "Physically Disabled" against this baseline is comparing one model simulation against another, not against a verified ground truth. The gap is still a real model behavior worth reporting, but the "sub-human" framing is stronger than what the comparison supports. A brief acknowledgment of this limitation would strengthen the paper's interpretive rigor.

- **"Physically Disabled" as a monolithic persona**: The paper treats "Physically Disabled" as a single persona without acknowledging the diversity of disability experiences. The model's behavior may conflate physical disability with cognitive disability (as the abstention examples suggest). A short discussion of this limitation in representation would be responsible.

- **Positive stereotypes and asymmetries are not discussed**: The analysis focuses on performance *drops* as bias, but the heatmap in Figure 5 shows some personas consistently outperforming others (e.g., Jewish outperforming Christian on STEM; Obama Supporter outperforming Trump Supporter on ethics). These asymmetries may also reflect harmful stereotypes (e.g., of Jews as high-achieving). The paper should briefly acknowledge that bias can cut both ways.

### Trivial

- The category heatmap (Figure 5) uses a colormap where small color differences can appear visually larger, slightly inflating the perceived gaps between near-identical cells.

## Nice-to-Haves

- **Mechanism analysis**: The paper documents *that* bias occurs (abstentions + implicit errors) but does not probe *why*. A small qualitative analysis of model reasoning traces (e.g., chain-of-thought across personas on a few math questions) could illuminate whether the bias operates through retrieval, reasoning, or confidence thresholding. This would deepen the contribution without requiring new experiments.

- **Dataset sensitivity analysis**: The paper does not discuss whether the 24 datasets are equally sensitive to bias — some datasets (e.g., math) may be more prone to abstentions while others (e.g., ethics) show subtle reasoning shifts. A brief note on dataset-level variation would strengthen the methodology section.

- **Instruction variance deserves more prominence**: The paper notes in §6 that bias varies significantly across the three persona instructions (e.g., one instruction raises the Phys. Disabled drop from 40% to 53%). This is a critical caveat that could be surfaced earlier, as the instruction-averaged results may understate worst-case bias in real applications where a single instruction is used.

## Removed Points

- **Criticism about missing related work**: Removed per instructions — I cannot verify the existence or absence of external references.
- **Criticism about not releasing code/data at time of review**: Removed per instructions — the paper states code and outputs will be released.
- **Criticism about missing appendix content or proofs**: Removed per instructions — parser may strip appendix sections; they exist in the original submission.
- **Strength Finder's "cross-model comparison" claimed strength**: Removed because it conflicts with the verified weakness that cross-model evidence is thin. Moving it here rather than listing it as a strength avoids contradiction.
- **Formatting and typo nitpicks**: Removed per instructions — these are parser artifacts, not author errors.
- **General concern about "evaluation lacks rigor" without specific anchor**: Removed per instructions — criticisms must anchor to specific sentences/figures/tables.

## Novel Insights

The most interesting finding not fully articulated in the paper's own framing is the **asymmetry in how bias manifests across persona types**: for disability and religion personas, bias is largely *explicit* (high abstention rates — 58% for Phys. Disabled, 49% for Religious), meaning the model overtly states its stereotype. For political affiliation, race, and gender personas, abstentions are minimal (<11%), yet performance drops still occur — the bias is *entirely implicit* and detectable only through aggregate accuracy differences. This suggests fundamentally different mechanisms may be at play: the model seems to have a "script" for certain demographic stereotypes (disability → can't do math) that triggers conscious refusal, while for others the bias operates at a more subtle level the model does not verbalize. Understanding this dissociation between explicit refusal and implicit performance degradation could be a productive direction for mechanistic interpretability.

## Suggestions

1. Apply a multiple testing correction (e.g., Benjamini-Hochberg) to all significance tests and report the number of significant drops that survive. The headline percentages may change modestly, but the correction will make the paper's evidential claims more defensible.

2. Restructure the paper to align its claims with its evidence: either (a) reframe the main body as a ChatGPT study with other models as supplementary evidence (adjusting the abstract language), or (b) move at least one additional model's full breakdown (bar charts analogous to Figures 2-3) into the main body to support the cross-model claims.

3. Add a brief sentence acknowledging that the "Average Human" baseline is a model construction and that comparisons to it reflect relative model behavior, not ground-truth human competence.

4. Include a short discussion of how bias varies across the three persona instructions (currently buried in §6) earlier in the paper, perhaps alongside the Results section, to give readers context for the averaged numbers.
