Here is my final consolidated review:

---

## Summary

This paper investigates whether translating benchmark test data into a low-resource language (Arabic) can mask evidence of data contamination while still allowing models to benefit from the leaked content. The authors fine-tune four open-weight LLMs on English test items plus varying proportions (0–100%) of Arabic-translated versions of those same test items, evaluate on English benchmarks, and probe memorization via an adapted TS-Guessing method with choice reordering. The central finding is that MMLU accuracy increases as more Arabic-translated contamination is added, yet standard contamination probes show relatively flat signals—suggesting translation can obscure detection without eliminating the benefit to models.

## Strengths

1. **Novel and important research question.** The interplay between translation and data contamination is underexplored, and the paper identifies a genuine blind spot: current contamination detection methods are English-centric, and translating benchmarks into other languages may hide leakage. This question is timely given the growing use of multilingual LLM evaluation.

2. **Methodological contribution: TS-Guessing with choice reordering for MCQs.** The extension of TS-Guessing (Section 3.3, Figure 1) to handle multiple-choice benchmarks by shuffling answer positions and measuring index-recall rate (IDR) is a reasonable adaptation. The IDR metric provides a contamination signal that goes beyond surface-form overlap, and Table 3a shows concrete evidence (e.g., LLaMA-3.2-1B at 50% contamination achieves IDR 0.643) that some models retain index-position information from fine-tuning.

3. **Systematic experimental scope.** The paper tests 4 models × 3 datasets × 4 contamination proportions = 48 conditions under a consistent LoRA/PEFT setup, providing broader coverage than most single-model or single-dataset contamination studies. Table 2 comprehensively reports all conditions.

## Weaknesses

### Major

1. **Experimental design cannot isolate the effect of translation *per se* (data volume confound).** The training set is defined as D_EN ∪ D_AR(p). At p=0 the model is trained on the English test items; at p=100 it is trained on those same English items plus Arabic translations, effectively doubling the dataset size. Since there is no control condition with an equal-sized *non-contaminated* Arabic corpus, the observed MMLU gains (e.g., Mistral: 0.577→0.690, LLaMA: 0.332→0.431) cannot be attributed specifically to contamination-through-translation as opposed to simply having more training data. The paper needs at minimum a condition where models are trained on D_EN plus an equal amount of non-benchmark Arabic text to separate data volume from contamination effects.

2. **"Near-flat performance" claim is contradicted by the paper's own data for MMLU.** Section 4.2 states that "across contamination levels p ∈ {10, 50, 100}%, the models exhibit approximately equal performance on all evaluated benchmarks" and that this "near-flat trend" indicates translation is masking contamination. However, Table 2 shows clear and often substantial MMLU increases from 10% to 100% contamination: Mistral rises from 0.580 to 0.690 (a 19% relative increase), LLaMA from 0.381 to 0.431 (13% increase), and Gemma from 0.244 to 0.284. These are not "approximately equal," and the inconsistency between the textual claim and the tabular data undermines a central argument.

3. **TS-Guessing probe results create an unresolved tension with the contamination narrative.** Table 3 shows near-floor signals across the board: Index-Recall Rates on MMLU are mostly near zero (except LLaMA at 50%: 0.643, which is non-monotonic), and Exact Match on XQuAD never exceeds 0.103. If models are genuinely memorizing from their training exposure (which includes the English test items directly), the TS-Guessing probe should detect much stronger signals. The paper does not reconcile why contamination probes are so weak while benchmark accuracy rises, leaving the mechanism behind the observed gains ambiguous. This tension is acknowledged but not analyzed.

4. **No English-only contamination baseline at matched size.** The paper cannot demonstrate that translation *masks* contamination without showing what "unmasked" contamination looks like in a comparable English-only setting. A condition with English test items only (at matched data volume) is needed to attribute the "masking" specifically to translation rather than to the general dynamics of fine-tuning on test data.

### Minor

5. **The claim that "models with stronger Arabic capabilities benefit more" is asserted but not measured.** The abstract and results discuss this, but no Arabic proficiency metric (e.g., Arabic benchmark scores, tokenizer coverage, or embedding analyses) is provided or correlated with the findings.

6. **The TACD framework (Section 5) is an unimplemented blueprint.** While forward-looking, presenting it as a contribution without any proof-of-concept experiments weakens the paper. A minimal demonstration (e.g., running TS-Guessing on machine-translated variants of a single benchmark) would strengthen the proposal.

7. **Masking an *incorrect* answer (rather than the correct one) in the TS-Guessing MCQ probe is an unusual design choice.** The paper masks one incorrect answer after shuffling and checks index recall. The rationale for this design over the more intuitive approach of masking the correct answer should be explicitly justified.

### Trivial

8. The literature review (Section 2) is comprehensive but disproportionately long relative to the paper's own contribution; it could be condensed significantly.

## Nice-to-Haves

- Evaluating the fine-tuned models on the Arabic test sets directly would provide a useful sanity check on language-specific memorization patterns.
- A non-contaminated Arabic data control (matched in size to D_AR) would strengthen causal claims.
- Quantitative embedding similarity analysis (cosine similarity between English and Arabic-translated items) is mentioned in the discussion but not reported in the main tables.

## Removed Points

- *Criticism that the 0% baseline already includes English test data as a "fatal design flaw":* This is reframed as Major weakness #1 above because the paper's comparison *among* p=10–100% conditions still provides useful evidence about translation masking detection probes. The p=0→p=100 comparison is indeed conflated, but the p=10→p=100 comparison is partially informative.
- *Criticism that "no evaluation on Arabic benchmarks" is a missing piece:* Demoted to Nice-to-Have since the paper's main question is about English evaluation after Arabic training.
- *Strength about "TACD as a forward-looking blueprint":* Demoted from core strength to minor contribution since it is an unimplemented discussion.
- *Strength about "systematic experimental design":* Kept but qualified—the breadth is real, though the design confounds weaken it.
- *Nitpicks about formatting, appendix contents, and literature review length:* Removed per filtering rules.

## Novel Insights

The most interesting observation from the reviews is that the TS-Guessing results may actually contain an underexploited finding: the fact that probe signals stay flat across contamination levels *while* MMLU accuracy rises could indicate that fine-tuning-driven contamination operates through a different mechanism than pre-training contamination—one that standard probes are not designed to detect. The paper gestures at this interpretation but does not develop it. If pursued, this could reframe the paper from "translation masks contamination" to "current probes fail at detecting fine-tuning-level contamination generally, and translation is one trigger revealing this failure."

## Suggestions

1. **Redesign the experiment** to include (i) a clean baseline with no test data in training, (ii) an English-only contamination condition at matched sizes, and (iii) a non-contaminated Arabic data condition at matched volume. Only then can the effect of translation *per se* be isolated.
2. **Correct the overstatement** in Section 4.2 about "approximately equal performance" on MMLU—the data clearly show monotonic increases. Either qualify the claim to apply only to XQuAD/MLQA or provide a statistical test evaluating flatness.
3. **Analyze the TS-Guessing failure cases** in depth. Why are contamination signals so low despite training on the test set? Is the probing method unsuited to instruction-tuned models fine-tuned with LoRA? Does fine-tuning change memorization dynamics compared to pre-training?
4. **Move the TACD framework to a discussion section** or implement a minimal proof-of-concept, rather than presenting it as a standalone contribution.

## Score and Decision

**Initial bracket (Round 1):** After reviewing anchors in three bands (weak: avg ≤3.5; middle: avg 3.5–7.5; strong: avg ≥7.5), the paper sits clearly in the middle band. Against "Time Travel in LLMs" (avg 7.0, accepted spotlight)—which has a clear methodology validated on known contaminated models—our paper is substantially weaker in experimental rigor. Against "Elephants Never Forget" (avg 4.75, rejected)—which shares issues of unvalidated methods and conclusions outpacing evidence—our paper is at a similar quality level, though with a more novel research question. Against "Exploring Memorization in Fine-tuned Language Models" (avg 4.0, withdrawn/rejected)—which had severe confound issues—our paper is somewhat stronger in experimental scope.

**Narrowing (Round 2):** Within the [3.5, 6.0] bracket, the most comparable anchor is "Elephants Never Forget" (avg 4.75, rejected). Both papers present interesting contamination-detection ideas but suffer from insufficiently validated methodologies and conclusions that outpace the evidence. Our paper's experimental design confounds (data volume, no clean baseline, TS-Guessing tension) are structurally similar in severity to the confounds that led to rejection of that paper, though our research question is more original. The paper is stronger than "Exploring Memorization in Fine-tuned Language Models" (avg 4.0) but weaker than "The Reasonableness Behind Unreasonable Translation Capability" (avg 5.75, accepted), which had a more thorough ablation design.

**Final score:** 4.5

**Calibration anchors used:**

| Anchor | Path | Avg Score | Round | Comparison |
|--------|------|-----------|-------|------------|
| Time Travel in LLMs | 2Rwq6c3tvr.md | 7.0 | R1 | Much stronger validation; our paper is clearly below |
| To the Cutoff... and Beyond? | m2NVG4Htxs.md | 6.75 | R1 | Clever longitudinal design; our paper is less rigorous |
| Reasonableness Behind Translation | 3KDbIWT26J.md | 5.75 | R1 | More thorough ablation; our paper weaker in rigor |
| Elephants Never Forget | lwtaEhDx9x.md | 4.75 | R1, R2 | Similar quality; both have unvalidated methods |
| Exploring Memorization in Fine-tuning | sVs7lV691r.md | 4.0 | R2 | Similar confound issues; our paper has broader scope |
| Cheating Auto LLM Benchmarks | syThiTmWWm.md | 7.75 | R1 | Much stronger execution and validation |
| When Is Multilinguality a Curse? | i7oU4nfKEA.md | 6.25 | R2 | Much larger-scale empirical work |
| Paramanu (Indian language models) | lAkke7Yj1T.md | 3.0 | R1 | Lower quality; our paper is stronger |
| Llamas think in English | fSbPwHjdDG.md | 3.0 | R1 | Different topic; comparable quality |
| MIND SCRAMBLE | KBixkDNE8p.md | 3.0 | R1 | Lower quality; our paper is stronger |

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>