Now I have a thorough understanding of the paper and can verify each reviewer claim. Let me produce the final review.

## Summary

This paper introduces QDAIF (Quality-Diversity through AI Feedback), which combines quality-diversity (QD) search algorithms with language models to generate diverse, high-quality creative text. The key insight is that LMs can instantiate all three components of QD search—variation (via LMX mutation), quality evaluation (via prompted AI feedback), and diversity evaluation (via prompted AI feedback)—enabling QD to be applied to subjective text domains where hand-crafted measures are infeasible. Experiments across opinion writing, short stories, and poetry show QDAIF achieves higher QD scores than several baselines, and a human evaluation provides evidence that AI-evaluated scores correlate reasonably with human judgment.

## Strengths

- **Novel integration of LM-based evaluation for both quality and diversity in QD search.** Prior work used LMs for variation and quality evaluation but not for diversity characterization. Using a single LM to evaluate both aspects via natural language prompts (Section 3, Figure 2) is a genuinely novel synthesis that opens subjective text domains to QD algorithms that previously required hand-engineered measures. The paper clearly identifies this gap (Section 2) and shows how AI feedback fills it.

- **Consistent and significant QD score improvements across multiple baselines and domains.** On Opinions, Stories-Genre, Stories-Ending, and Stories-Genre&Ending, QDAIF achieves substantially higher QD scores than all four baselines (Figure 3), including quality-only optimization (basefour), demonstrating that the QD search with AI feedback for both axes drives the improvement. The Poetry domain shows a similarly large gap (QD score 130 vs. 76 for random generation, Figure 4).

- **Human evaluation provides grounding evidence.** The human study (Table 1) shows QDAIF is competitive with or better than baselines in human-perceived quality-diversity, and agreement rates between AI and human annotators are competitive with inter-human agreement. This provides some empirical evidence that the AI feedback loop is not purely self-referential.

- **Ablation and robustness analysis supports the method's generality.** The paper tests multiple design choices—LMX model size (13B vs. 30B/70B), few-shot AI feedback counts (2/4/8-shot), zero-shot initialization, and different mutation operators (Section 4.3). QDAIF remains effective across these variations, supporting the claim that the QD framework itself drives improvements rather than a specific configuration.

## Weaknesses

### Fatal
None.

### Major

- **Reliance on AI feedback quality without sufficient validation against reward hacking.** The paper's primary quantitative evidence (Figure 3 QD scores) is computed using AI feedback for both quality and diversity. The authors themselves note (Discussion, Section 5) that "the correlation drops when the evaluated quality is in the range 0.995 to 1" and that "text generation might have exploited certain attributes or phrasings that allow an LM to give a high-quality estimate, but not what humans would agree is good." This is not a minor edge case—it directly threatens whether the reported QD score differences reflect genuine quality-diversity improvements or artifacts that game the AI evaluator. The human evaluation that could validate this was conducted only on *elite samples from a single median run per condition* (Section 4.1, "chosen from the median QD score run out of 5 random seed runs"), which does not provide a rigorous check on whether the QD score gaps in Figure 3 are driven by genuine improvements or by AI-evaluated artifacts. Without either (a) human evaluation of a representative sample of the *full archive* across multiple runs, or (b) a systematic analysis quantifying the extent and impact of reward hacking, the quantitative superiority of QDAIF over baselines is plausible but not convincingly demonstrated against this known failure mode. The paper transparently acknowledges the limitation, which is commendable, but does not provide evidence that it does not undermine the central quantitative results.

### Minor

- **Non-uniform binning sensitivity not analyzed.** The paper uses custom non-uniform bins based on AI feedback logits (Section 3, "Discretization") with the rationale that "qualitative changes in behavior do not uniformly correspond to changes in the logits." Given that the QD score sums across bins, the results could be sensitive to the bin edge placement. A comparison with uniform binning or a sensitivity analysis would strengthen the results. The qualitative justification provided is reasonable but does not rule out that the reported performance gaps are partly an artifact of the binning scheme.

- **Poetry experiment confounds method change with model and operator changes.** The Poetry domain (Section 4.4) uses a different model (GPT-4 rather than the finetuned 13B model used for Opinions/Stories), a different mutation operator (instruction-guided rewrite rather than LMX), and a different evaluation approach (categorical labels rather than logit-based). This makes it difficult to attribute the improvement specifically to QDAIF as opposed to the stronger model or the rewrite operator. The paper partially addresses this with a GPT-3.5-Turbo ablation mentioned in the appendix (showing a wider gap, supporting QDAIF's contribution), but the confound is not cleanly disentangled in the main text.

- **Computational cost not discussed.** The paper never discusses how many LM calls QDAIF requires per iteration or the total computational cost. For 2000 iterations with a 13B model doing generation + quality evaluation + diversity evaluation, the cost is substantial. A brief note on wall-clock time or API costs would help readers assess practical feasibility.

- **Finetuned AI feedback model transparency.** The Opinions and Stories experiments use a finetuned AI feedback model whose details (training data, process) are deferred to the appendix (which the parser strips, but existed in the original submission). The paper does not clarify in the main text whether this model was trained on data overlapping with the evaluation domains, which would raise a circularity concern—the AI evaluator might simply recognize what it was trained to recognize as good, and the evolutionary search could exploit that trained notion. The Poetry domain uses off-the-shelf GPT-4, which avoids this concern, but the paper does not compare findings across these two evaluator types to discuss whether the results transfer.

### Trivial

- **Number of runs (5 random seeds) is on the lower end.** While bootstrapped 95% CIs from 100k resamples are standard and the CIs are reported, 5 seeds provides limited generalizability. This is standard practice in evolutionary computation but worth noting.

## Nice-to-Haves

- **Human evaluation on a stratified sample of the full archive** across multiple seeds (not just elite samples from a single median run). Even a small-scale study (~200 samples) would provide a much stronger check on whether reward hacking affects the main conclusions.
- **Sensitivity analysis of the non-uniform binning** compared against uniform binning.
- **An analysis of cases where AI and human ratings diverge**, with example texts and characteristic patterns, turning a known limitation into a practical insight.
- **Ablation using randomly assigned diversity bins** or only quality feedback with a uniform diversity prior, to further isolate the contribution of the AI-evaluated diversity measure.

## Removed Points

- **"Baselines do not control for the effect of AI feedback itself" / "No comparison against hand-crafted QD measures"** — Removed because the paper's premise is that hand-crafted measures are infeasible for these domains (Section 2, Section 3 explicitly discuss this limitation). Asking for a QD baseline with hand-crafted measures contradicts the paper's stated scope and is not a fair criticism. The paper's comparisons against non-QD baselines (including quality-only optimization) are appropriate for its claims.
- **"Prompt templates should be in the main paper"** — Removed. Deferring long prompt templates to the appendix is standard practice; this is a formatting preference, not a substantive weakness.
- **"5 runs is a weak basis for claiming generalizability"** — Downgraded to Trivial. 5 seeds with bootstrapped CIs is standard in the EC community. This does not threaten the paper's conclusions.
- **"Missing related works"** — Not included, as I cannot independently verify their existence.

## Novel Insights

The reviews collectively surface an important tension: QDAIF's central innovation—using AI feedback for both quality and diversity—is also its central vulnerability. The paper shows that AI feedback *can* work (the human evaluation on elite samples is encouraging), but it does not establish *when* it fails or *how often*. The reward-hacking regime the authors identify (quality scores near 1.0) is precisely the region where QDAIF's archive is most populated after many iterations, meaning the main results may live in the least reliable part of the AI evaluator's range. This is a structural issue in any method that uses a learned evaluator to guide open-ended search toward that evaluator's own maxima. The paper's value would be substantially strengthened not by more results but by characterizing this failure mode empirically—showing examples, quantifying its prevalence, and testing mitigations (e.g., ensemble evaluation). The Poetry domain's use of categorical diversity labels (less prone to exploitation than continuous logit scores) hints at one design principle for future work.

## Suggestions

1. **Run a focused human evaluation on a stratified sample of the full archive** across multiple runs (not just elite samples from a single run), computing human-evaluated QD scores for each method. This directly addresses the reward-hacking concern and would either confirm or qualify the main claims.

2. **Characterize the reward-hacking regime empirically.** Show examples of texts where AI and human quality ratings diverge (especially in the 0.995–1.0 range), quantify how frequently this occurs in QDAIF archives vs. baselines, and discuss whether it affects the relative rankings.

3. **Replace or supplement the non-uniform binning** with a sensitivity analysis showing that results are not driven by bin boundary choices.

4. **Include a brief computational cost note** (wall-clock time or API cost per 2000-iteration run) in the main paper.

## Score and Decision

This paper introduces a well-motivated and novel integration of QD search with AI feedback for quality and diversity evaluation. The core idea is sound, the experiments span multiple creative writing domains, and the human evaluation provides some validation. The paper is clearly written and its contribution is likely to be influential.

However, the paper's central quantitative results rely on AI feedback whose reliability is not sufficiently validated against the method's own known failure mode (reward hacking). The human evaluation is too limited in scope to rule out the possibility that QDAIF's higher QD scores reflect artifacts that game the AI evaluator rather than genuine quality-diversity improvements. This is the paper's most significant weakness, and it is ultimately the difference between a promising demonstration and a fully convincing one.

The contribution is real, and the paper should be taken seriously. But acceptance requires addressing the reward-hacking concern, ideally by validating AI-evaluated QD scores against human evaluation on a representative sample of the full archive. With such evidence, this would be a strong paper.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Weak Accept</orange>