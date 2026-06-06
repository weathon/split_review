## Summary

The paper proposes Iterated In-Context Language Learning (IICLL), a paradigm for simulating cultural transmission in LLMs to probe their inductive biases toward Information Bottleneck (IB)-efficient semantic systems. It couples this with a systematic English color naming evaluation across 39 LLMs. The main findings are: (1) frontier instruction-tuned LLMs—especially Gemini 2.0—can achieve high English-alignment and IB efficiency; (2) all four IICLL-tested models iteratively restructure random pseudo-label systems toward the IB bound over generations; and (3) Gemini 2.0 uniquely recapitulates the full complexity range of human color naming systems observed in the WCS. The paper frames these findings as evidence for a human-like inductive bias toward IB-efficiency in LLMs.

---

## Strengths

- **IICLL is a genuinely novel paradigm.** Building on Zhu & Griffiths (2024)'s I-ICL, the paper extends it specifically to artificial language learning with pseudo labels, enabling direct quantitative comparison to human iterated language learning (ILL) data (Xu et al., 2013; Imel et al., 2025). The experimental design is carefully engineered to mirror the human protocol, and the convergence trajectories in Figs. 3–4 — using random initializations across varying *k* and running multiple chains — constitute rigorous evidence that IICLL pressure alone moves all four models toward the IB bound.

- **The 39-model English color naming survey is systematic and informative.** By varying model family, size, training stage, and input modality, the paper provides the most comprehensive characterization of LLM color naming to date. The concrete finding that instruction-tuning, more than pre-training scale, drives IB-alignment (Fig. 2c) and the surprising discovery that models like Olmo 2 32B and Qwen 2.5 VL 7B produce WCS-like systems despite failing to match English (Fig. 9 in Appendix E) are non-trivial empirical observations.

- **The Olmo 2 training trajectory (Appendix F) provides a concrete mechanistic clue.** The finding that English-alignment improves only modestly during pre-training but jumps substantially after instruction-tuning is a useful empirical anchor for future work on the origins of IB-like biases in LLMs.

- **The rotation control (Appendix H) validates the non-trivial structure of emergent Gemini systems.** The paper reports (Sec. 4.2): "rotations away from the actual emergent systems lead to a significant decrease in efficiency and alignment for Gemini." This rules out the possibility that the measured IB efficiency for Gemini is an artifact of the metric or grid geometry — the specific category structures that emerge, not just any compact partitioning, are genuinely near-optimal.

- **Comparison to human IL data as a principled benchmark.** Plotting IICLL trajectories against Xu et al. (2013)'s human IL chains and Imel et al. (2025)'s IB analysis of those chains provides a calibrated reference that is rare in this type of study.

---

## Weaknesses

### Fatal
None.

### Major

- **Stimulus-recognition confound undermines the "domain-general inductive bias" framing.** The paper's central inferential claim is that IICLL reveals an inductive bias toward IB-efficiency *beyond memorization*: models receive pseudo-labels and no indication the stimuli are colors. However, the stimuli presented to text-based models are sRGB coordinate triples — a format deeply embedded in model training data (HTML, CSS, color picker docs, etc.). A model can recognize that (230, 50, 30) is a warm red and group it perceptually with nearby reds without any abstract compression bias. For Gemini specifically, actual color image patches are used (Sec. 3: "For multimodal models, we generated a square colored image"), making perceptual recognition even more direct. The paper acknowledges in the Discussion that "the precise origins of the bias we observe in LLMs toward efficiency are unclear," but does not engage with this specific confound. The two competing hypotheses — (a) LLMs have a domain-general abstract inductive bias toward IB efficiency; (b) LLMs apply learned color knowledge to organize recognizable stimuli efficiently — make nearly identical predictions in the color domain but are conceptually distinct. The experimental design as presented cannot discriminate between them. This is an evidential limitation rather than a structural flaw (the findings are real), but the abstract's conclusion "human-aligned semantic categories can emerge in LLMs via the same fundamental principle that underlies semantic efficiency in humans" and the Shepard circles section's invocation of "domain-general" generality both run ahead of what the color experiments alone can establish.

- **The headline full-range IB result rests on a single model, and the rotation analysis is inconclusive for the other three.** The paper is transparent about this (Sec. 4.2: "only Gemini is able to recapitulate the wide range of near-optimal IB-tradeoffs"), but the rotation analysis — the primary argument that the emergent systems are non-trivially efficient — is reported as "less conclusive for the other models." This means the strongest positive claim is supported only for Gemini. The paper attributes the gap to in-context learning capacity and notes the k=14 condition requires 84 in-context examples, but this is post-hoc and untested. Whether increasing in-context capacity for the other models would close the gap, or whether Gemini's multimodal training contributes, is unresolved. The generalization from Gemini's result to LLMs broadly is therefore not fully warranted by evidence.

### Minor

- **The Shepard circles section (Sec. 4.3) is honest about its limitations but over-invoked elsewhere.** The paper correctly states: "An important direction for future work is to test whether this emergent structure also supports greater IB-efficiency as seen in humans." Compact 2D partitioning is not the same as IB efficiency, and without a perceptual prior for Shepard circles no IB analysis can be done. As a qualitative pilot for a single model under a single condition (*k*=4), this section is appropriately scoped — but the abstract, introduction, and discussion cite it as supporting "domain-generality" of the bias, which overstates what four visual IICLL chains support.

- **The mechanism of the sRGB vs. CIELAB difference is unaddressed.** The paper reports (Sec. 4.1) that "all models, including the best performing ones, struggled to align with English naming when colors are presented in CIELAB," attributing this to a "key difference between how LLMs represent color and how humans do." This is a meaningful negative result, but it directly bears on the paper's characterization of LLM color representations as "perceptually grounded" and deserves mechanistic discussion. If the model's alignment is representation-format dependent, what does "perceptually grounded" mean here?

- **IICLL model selection is pre-screened, and the variance specification in Fig. 4 is unclear.** The paper states models were selected because they "performed well in the English color naming task." This is pragmatically justified but means IICLL is tested only on models already known to have human-aligned color representations. The 95% confidence intervals in Fig. 4 are shown without specifying whether they represent variance across random seeds, chain initializations, or both.

### Trivial

None identified.

---

## Nice-to-Haves

- **Varying in-context example count (k) systematically across all four models** would directly test whether the gap between Gemini and the other models is attributable to in-context learning capacity, as the paper hypothesizes. This would help decompose what is model-general from what is Gemini-specific.

- **Analyzing whether the low-complexity attractors for Gemma, Llama, and Qwen correspond to typologically attested simple color naming systems** would strengthen the argument that even their constrained convergence is "human-like" rather than degenerate, following the paper's own logic about IB-efficiency across human languages.

- **A deeper discussion of why image inputs do not consistently outperform sRGB text inputs** (Fig. 8, Appendix E) — and in fact hurt larger model performance — would add insight beyond the current brief mention.

---

## Removed Points

*These points are flagged for removal — treat them with caution.*

1. **Harsh critic's suggestion to use perceptual-feature-engineered stimuli unrecognizable as colors.** This is a nice-to-have for future work but does not constitute a weakness of the current paper, which explicitly scopes itself to color as a testbed domain with uniquely rich human data for comparison.

2. **Strength Finder's Strength 2 ("gradation sharpens the claim of human-like bias")**: The characterization that Gemma/Llama/Qwen plateauing at lower complexity "strengthens" the IB-efficiency case is too optimistic given the inconclusive rotation analysis for those models. Removed to avoid inflating the evidentiary picture.

3. **Harsh critic's complaint about selection bias toward "pre-screened" IICLL models being unreported across all 39.** The paper explicitly acknowledges and discusses this (Appendix L: "smaller models struggle in IICLL to produce non-degenerate category systems"). The selection is justified and reported, not hidden.

4. **Harsh critic's complaint about missing variance specification for IICLL chains.** Partially valid but minor enough to include only as a trivial suggestion; moved to Minor instead of Major per filtering discipline.

5. **Any implied "missing related works" criticism** — not applied here per hard rules.

---

## Novel Insights

The most genuinely novel finding in this paper — beyond documenting that LLMs match human IB efficiency statistics — is the *dynamic trajectory structure* in Fig. 3: IICLL chains for all four models initially *climb* in complexity before descending along the IB bound. This suggests a two-phase dynamic (exploratory expansion, then efficient compression) that may parallel cultural evolution processes in humans and deserves deeper analysis. The observation that some models (Olmo 2 32B, Qwen 2.5 VL 7B) produce WCS-like systems without matching English specifically is also novel and underexplored: it implies that the space of IB-efficient color systems is reachable via multiple training paths, not just English-language immersion.

---

## Suggestions

1. **Reframe the central inferential claim** to distinguish "LLMs trained on human language have representations that, under cultural transmission pressure, converge to IB-efficient systems" from "LLMs possess an abstract domain-general inductive bias toward IB efficiency." The first is fully supported; the second requires non-color evidence or stimuli the model cannot recognize as colors.

2. **Add a systematic k-sensitivity experiment** varying the number of in-context examples for all four models to empirically test the in-context-learning-capacity explanation for the Gemini–other gap.

3. **Strengthen the Shepard circles section** by adding a simple IB-like analysis using a perceptual prior derived from human categorization of Shepard stimuli, or by explicitly framing the section as a purely qualitative pilot in the abstract and introduction.

4. **Discuss the CIELAB/sRGB asymmetry mechanistically**: if sRGB coordinates are associated with color language in training data but CIELAB coordinates are not, this is informative about what "color representation" in LLMs actually means — and bears directly on the "perceptually grounded" claim.

---

## Score and Decision

**Axis evaluations:**
- *Originality*: High. IICLL is a novel and well-designed paradigm; the 39-model IB analysis fills a real gap.
- *Importance*: High. The question of whether LLM semantic representations are organized by human-like efficiency principles is significant for cognitive science, NLP, and AI alignment.
- *Claims supported*: Partially. The core convergence finding is well-supported; the "domain-general abstract inductive bias" framing is not fully established given the stimulus-recognition confound and single-model headline result.
- *Soundness*: Good with caveats. Experimental design is mostly rigorous; the main gap is inferential rather than methodological.
- *Clarity*: High. Well-written, structured clearly, figures are informative.
- *Community value*: High. Useful to both cognitive scientists and NLP researchers; introduces a replicable paradigm.

The paper makes a genuine, novel contribution. The core weakness — the gap between "convergence to IB-efficient systems in color" and "domain-general abstract inductive bias toward IB efficiency" — is real but does not invalidate the empirical findings, and the paper itself partially acknowledges it. The IICLL paradigm is valuable beyond this specific result. Minor recalibration of claims would bring the paper to full strength.

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>

<subscores>
<originality>4</originality>
<importance>4</importance>
<claims_supported>3</claims_supported>
<soundness>4</soundness>
<clarity>4</clarity>
<community_value>4</community_value>
</subscores>