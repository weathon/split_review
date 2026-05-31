Now let me do calibration searches to score the paper.Round 1 bracket: The paper appears to sit between 5.5 and 8.0. Let me read the closest anchor papers before narrowing.Now I have sufficient calibration. Let me compile the full final review.

## Summary

The paper introduces *persona vectors* — linear directions in LLM activation space corresponding to specific character traits, extracted via a fully automated pipeline from natural-language trait descriptions. The pipeline uses a frontier LLM to generate contrastive system prompts, evaluation questions, and a scoring rubric; vectors are then extracted via contrastive mean activations and validated by an LLM judge. These vectors enable four applications demonstrated on Qwen2.5-7B-Instruct and Llama-3.1-8B-Instruct across three negative traits (evil, sycophancy, hallucination): (1) deployment-time monitoring of prompt-induced behavioral shifts, (2) inference-time steering, (3) a novel *preventative* steering method applied during finetuning, and (4) pre-finetuning data screening at both dataset and individual-sample level. The preventative steering method and data-screening capabilities are the most original and practically significant contributions.

---

## Strengths

- **Fully automated persona-vector extraction**: The pipeline requires only a trait name and description; a single generic template generates all artifacts (contrastive prompts, evaluation questions, rubric). Figure 2 confirms steering effectiveness across layers, and Appendix D validates the judge-based scoring against human evaluators and external benchmarks, making the approach broadly accessible without per-trait engineering effort.

- **Strong finetuning correlation results**: Figure 4 shows r = 0.76–0.97 between finetuning-induced activation shifts along persona vectors and post-finetuning trait expression scores across six trait–model combinations. This demonstrates that persona vectors capture the internal representation mediating behavioral change rather than superficial textual patterns.

- **Novel and capability-preserving preventative steering**: Steering *toward* the persona direction *during* finetuning (Section 5, Figures 5–6) limits trait acquisition more effectively than post-hoc inference-time steering while substantially better preserving MMLU performance. The fact-acquisition case study (Section 5.2) is the paper's strongest demonstration: preventative hallucination steering allows a model to learn 1,000 new facts without acquiring the accompanying hallucination tendency, whereas inference-time steering degrades both new-fact recall and MMLU.

- **Pre-finetuning data screening with strong predictive power**: Dataset-level projection difference predicts post-finetuning trait expression (r = 0.88–0.95, Figure 7) before any training occurs. Sample-level projections cleanly separate trait-inducing from control samples in both explicitly trait-eliciting and EM-like datasets (Figure 8), and the method is shown in Appendix N to complement LLM-based filtering by catching samples that would otherwise escape it.

- **Monitoring of prompt-induced shifts before generation**: Figure 3 shows projections at the last prompt token correlate r = 0.75–0.83 with subsequent trait expression across system-prompt and many-shot conditions, enabling pre-generation behavioral shift detection.

---

## Weaknesses

### Fatal
None.

### Major

- **Cross-trait specificity is weaker than the core framing claims** — The paper's central framing is that *trait-specific* persona vectors are the key contribution. However, the within-trait finetuning correlation for sycophancy in Qwen (r = 0.769, Figure 4) is numerically lower than the upper bound of the reported cross-trait baseline range (r = 0.34–0.86, Appendix I.2). Footnote 6 explicitly acknowledges: "negative traits tend to shift together." The ranges overlap, meaning the sycophancy vector's predictive advantage over a generic "negativity direction" is not established for the Qwen model. The paper does not decompose shared versus trait-specific variance (e.g., by projecting vectors onto their common principal component), and does not test whether a single generic negativity vector would perform comparably across the mitigation and screening tasks. This matters concretely: if evil and sycophancy vectors are highly collinear, "evil-specific" prevention may simply be "negativity suppression," and the practical precision of each application is less than the trait-specific framing implies. The paper should either present a decomposition analysis or explicitly reframe around a negativity-aware control framework.

- **LLM evaluation circularity is real and not fully resolved in the main text** — Claude 3.7 Sonnet generates the contrastive system prompts, the evaluation questions, *and* the evaluation rubric; GPT-4.1-mini then evaluates model responses against this rubric. Persona vectors are extracted from activations on Claude-generated prompts. If Claude's implicit concept of a trait systematically aligns with the activation directions it produced, the reported correlations (e.g., r = 0.967 for hallucination in Llama, Figure 4) may be inflated relative to ground truth. The paper validates against human annotators and external benchmarks in Appendix D — the right response — but no quantitative agreement between LLM-judge scores and human annotations appears in the main text for any trait or model. Including even one such number (e.g., Spearman ρ between judge and human ratings for one trait) in the main text would substantially increase confidence in the high-precision correlation figures.

### Minor

- **The preventative steering mechanism is asserted but not probed** — Section 5 states the mechanism is that adding the persona vector "counteracts the finetuning objective's tendency to push the model along that direction." This is plausible but untested. A single control experiment — applying the sycophancy vector to prevent evil acquisition, or vice versa — would determine whether trait-specific information is necessary or whether generic activation perturbation during training explains the benefit. Without this, practitioners cannot predict when the method will generalize to new traits or models.

- **Within-prompt-type monitoring correlations buried and unquantified** — Section 3.3 acknowledges "more modest correlations when controlling for prompt type (Appendix E.2)" but provides no numbers. This caveat is critical for calibrating the monitoring application's practical scope: if within-type correlations are near zero, the application detects only large, explicit shifts rather than subtle deployment-time drift. At minimum, one representative within-type r value should appear in the main text to prevent readers from over-interpreting the headline r = 0.75–0.83 as deployment-ready precision.

- **Experiments limited to 7–8B parameter models** — All experiments use Qwen2.5-7B-Instruct and Llama-3.1-8B-Instruct. Whether persona vectors remain coherent, specific, or controllable at larger scales (e.g., 70B, frontier models trained with different alignment procedures) is entirely unaddressed. The practical claims in the abstract generalize beyond what the evidence supports.

- **Capability assessment uses only MMLU** — For the finetuning setting, MMLU is a coarse metric for detecting subtle behavioral degradation. Domain-specific capability metrics on the same prompt distribution used for training would provide more direct evidence that desired knowledge or skill acquisition is not sacrificed by preventative steering.

### Trivial

- **Duplicate paragraphs in Section 5.1** — The third and fourth paragraphs of Section 5.1 are nearly identical, both describing the comparison to CAFT and the regularization ablation in essentially the same words. This is a copy-paste artifact that should be removed.

- **Non-independence of data points in Figure 4** — Each dataset has three versions (Normal, I, II) constructed from the same base, so n ≈ 24 is not i.i.d.; effective degrees of freedom are closer to 8 per panel. Reporting p < 0.001 based on the nominal sample size overstates inferential strength; a note acknowledging this dependency would be appropriate.

---

## Nice-to-Haves

- **Shared vs. trait-specific variance decomposition**: Extract the first principal component of the three persona vectors (evil, sycophancy, hallucination); project each vector onto this shared direction and its residual; report which component drives the finetuning correlations in Section 4 and the prevention results in Section 5. Either finding (shared or specific) would be informative and directly address the cross-trait specificity concern.

- **Wrong-vector control experiment for preventative steering**: One additional ablation (e.g., using the sycophancy vector to prevent evil acquisition) would resolve whether the mechanism is trait-specific or general. This single experiment would make Section 5's claims substantially more actionable.

- **Real-world data filtering result from Appendix N in the main text**: Section 6.2 mentions that "In Appendix N, we show this method works on real-world datasets to select samples that induce or suppress a given trait, even escaping LLM filters," but includes no summary numbers. This is one of the paper's most practically compelling results; a single precision/recall or example figure in Section 6.2 would materially strengthen the paper's practical argument.

- **Explicit reporting of within-prompt-type monitoring correlations in Section 3.3**: Rather than pointing to Appendix E.2, quoting one representative within-type r value in the main text would give readers an accurate calibration of the monitoring application's limits versus capabilities.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **(Harsh Critic) "The paper does not flag model-scale limitations."** Removed: The paper explicitly notes that limitations are discussed in Appendix B. Per review rules, absence of content from stripped appendix sections cannot be penalized.

- **(Harsh Critic) "Section 6.2's claim about complementarity with LLM-based filtering is an important practical result that goes entirely unreported in the main text."** Partially retained as a Nice-to-Have; the main claim *is* stated in Section 6.2 ("including some which would otherwise escape LLM-based data filtering"), even if not numerically quantified. The absence of numbers is a valid enhancement request but not a substantive weakness.

- **(Harsh Critic) "Abstract's monitoring claim is not accurately represented."** Removed as a standalone weakness. The paper explicitly tempers the claim in Section 3.3 and refers readers to the appendix for within-type correlations. The abstract phrasing ("monitor fluctuations in the Assistant's personality") is technically supported by the prompt-level monitoring results even if the precision at the intra-type level is uncertain.

- **(Strength Finder) "Generalisation across positive traits (optimism, humor)."** Downgraded from a core strength. The positive-trait results are in the stripped appendix (Appendix I) and cannot be directly verified; leaving as context only.

---

## Novel Insights

The preventative steering concept — steering a model *toward* an undesired trait *during* finetuning in order to inoculate the model against acquiring that trait — is counterintuitive and, if confirmed at larger scales, could become a practical tool for fine-tuning-as-a-service providers. The intuition (that preemptively saturating the persona direction reduces the pressure for finetuning to shift activations along it) is novel compared to post-hoc inference-time approaches. The fact-acquisition case study provides a compelling proof-of-concept: a model can be finetuned to learn 1,000 new post-cutoff facts while its general hallucination tendency is simultaneously suppressed to baseline, a dissociation that inference-time steering cannot achieve without destroying factual recall. The combination of this preventative method with pre-training data screening (projection difference as a dataset-level and sample-level risk signal) constitutes a coherent pre-to-during-training safety toolkit that goes beyond what any prior single-application steering paper has offered.

---

## Suggestions

1. Present a shared-vs.-specific variance decomposition for persona vectors to directly address the cross-trait specificity concern.
2. Add a wrong-vector control condition for preventative steering (e.g., sycophancy vector → evil prevention) to mechanistically validate or reframe the method.
3. Report at least one quantitative LLM-judge vs. human-annotator agreement figure in the main text for calibrating the core correlation claims.
4. Include one representative within-prompt-type monitoring correlation value in Section 3.3 with appropriate interpretive framing.
5. Move a headline result from the real-world dataset experiment (Appendix N) into Section 6.2.
6. Remove the duplicate paragraphs in Section 5.1.
7. Supplement MMLU with a domain-specific capability metric in Section 5's evaluation.

---

## Score and Decision

**Anchor summary:**

| Paper | Path | Avg Score | Round | Comparison |
|---|---|---|---|---|
| Steering Language Models (ActAdd) | `2XBPdPIcFK.md` | 5.00 | R1 | Single-application activation steering; paper under review is substantially more comprehensive and original. |
| Conceptors + Activation Steering | `9wjGUN65tY.md` | 5.00 | R1 | Theoretical extension of steering; narrower scope and fewer applications than paper under review. |
| Entropic Activation Steering | `YCu7H0kFS3.md` | 4.75 | R1 | Single application (agent exploration); clearly weaker in scope and originality. |
| Instruction-Following via Activation Steering | `wozhdnRCtw.md` | 7.00 | R1 | Four models, three instruction tasks; paper under review has more novel contributions (preventative steering, data screening, automated pipeline). |
| MAP Multi-Human-Value Alignment | `NN6QHwgRrQ.md` | 8.00 | R1 | Multi-value alignment formulation; different method class. |
| Booster (harmful finetuning defense) | `tTPHgb0EtV.md` | 8.00 | R1+R2 | Focused, clean harmful finetuning defense with unanimous 8s; paper under review has broader scope but more open methodological questions. |
| Safety Layers in Aligned LLMs | `kUH1yPMAn7.md` | 6.00 | R2 | Identifies safety-critical layers; interpretability only, no active interventions. |
| Safety Neurons | `yR47RmND1m.md` | 6.20 | R2 | Identifies and tunes safety neurons; narrower than paper under review. |
| Durable Safeguards for Open-Weight LLMs | `fXJCqdUSVG.md` | 6.50 | R2 | Analysis/critique paper, no novel methods proposed. |
| Do as I do (Safely) | `lXE5lB6ppV.md` | 5.75 | R2 | Task-specific finetuning safety risks; narrower scope and weaker results than paper under review. |
| Measuring Effects of Steered Representations | `z1yI8uoVU3.md` | 3.00 | R1 | Evaluation framework for steering; clearly weaker. |

**Round 1 bracket**: 5.5–8.0.

**Round 2 narrowing**: The paper is clearly above the 5.0–6.0 anchor papers (it has far more scope, novelty, and empirical rigor). It is comparable to or slightly above the instruction-following steering paper (7.0): both automate vector extraction and apply steering to practical tasks, but the paper under review adds preventative steering (novel), data screening (novel), the safety-relevant trait focus, and the automated pipeline. The Booster paper (8.0) is a natural upper anchor: it has a clean, focused mechanism for harmful finetuning defense with unanimous 8s, but covers only a single application. The paper under review covers four applications but has real unresolved questions (cross-trait specificity, evaluation circularity, unvalidated mechanism) that the Booster paper does not. This places the paper squarely at **7.0** — meaningfully above the instruction-following paper in novelty and scope, but not reaching the focused methodological cleanliness of Booster.

**Originality**: High — the preventative steering and automated data screening contributions are original. The monitoring and inference-time steering applications build on prior work but are applied to a novel persona-vector extraction framework.

**Importance**: High — the paper targets practically consequential failure modes (emergent misalignment, sycophancy drift, hallucination) and provides a toolkit covering the full finetuning lifecycle.

**Claim support**: Mostly solid, with the cross-trait specificity and evaluation circularity as real gaps that weaken precise claims.

**Experimental soundness**: Good — two models, three traits (plus additional in appendix), multiple dataset types, comparison to baselines.

**Clarity**: Good, with the exception of the duplicate paragraphs and the underquantified monitoring limitation.

**Community value**: High — the automated pipeline lowers the barrier to adoption and the preventative steering result is directly actionable.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>