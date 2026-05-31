Now let me run calibration searches to anchor the score.**Round 1 bracket: ~4–6** (below large-scale comprehensive benchmarks; above poorly-executed papers; comparable to solid but limited dataset papers)

Now narrowing:Now let me read one of the most similar anchors in full to sharpen my comparison:Now I have enough information to write the consolidated review. Let me put it all together.

---

## Summary

EmoSign introduces the first American Sign Language video dataset with sentiment ratings (7-point Likert), multi-category emotion intensity annotations, and open-ended descriptions of visual emotion cues, all provided by three Deaf native ASL signers with professional interpretation experience. 200 clips drawn from ASLLRP are benchmarked across four multimodal LLMs (GPT-4o, AffectGPT, Qwen2.5-VL, MiniGPT4) under caption-only, video-only, and video+caption input conditions. Results show that models struggle with video-only emotion recognition in ASL and improve substantially when text captions are provided.

---

## Strengths

- **First ASL emotion dataset annotated by Deaf native signers with multi-layer annotations.** Table 1 confirms no prior ASL dataset contains emotion labels, sentiment ratings, or cue descriptions. The use of Deaf annotators with professional interpretation experience is methodologically critical, as Section 2 documents that hearing annotators frequently misinterpret ASL facial expressions. This directly addresses FePh's key weakness.

- **Benchmark experiments document a meaningful and reproducible failure mode in current MLLMs.** Tables 3 and 4 demonstrate consistently that vision-only performance collapses across all four models, with AffectGPT nearly always predicting neutral and GPT-4o defaulting to happiness/frustration in video-only conditions. The pattern is consistent across four independent models, giving the finding empirical robustness despite the small dataset size.

- **Annotation reliability is documented transparently with contextualisation against the field standard.** Table 2 reports Krippendorff's alpha per label (average α = 0.593), and Section 3.3 contextualizes this against MELD (Fleiss' kappa = 0.43) and IEMOCAP (0.48), demonstrating that overall annotation quality meets or exceeds community norms.

- **The qualitative grounding analysis in Section 5.3 surfaces a genuinely informative failure pattern.** The demonstration in Figure 3 that models assign the same visual cue opposing emotional valence depending on whether a text caption is present provides a concrete and reproducible illustration of post-hoc rationalization behavior in MLLMs.

---

## Weaknesses

### Fatal
None.

### Major

- **VADER-based clip selection creates a structural confound in the caption-only benchmark condition.** Clips were selected by ranking on VADER text sentiment — the 100 most positive and 100 most negative utterances (Section 3.1). This guarantees that the English captions are emotionally extreme *by construction*, relative to naturalistic ASL corpora. When caption-only model conditions are evaluated and compared to video-only conditions, models operating on captions benefit from the selection regime in aggregate, even when individual ground-truth labels diverge from VADER's predictions. The paper's central comparative claim — that models "fail to integrate visual cues" and "heavily rely on text captions" — partially rests on this comparison (Tables 3 and 4). While the observation that VADER results differed from annotators (Section 6) is invoked as evidence of visual signal, it does not address the distributional confound: the caption-only condition is made relatively capable *by design*. The paper does not acknowledge this limitation in the results discussion where the modality comparison claim is stated most strongly.

- **Per-class benchmark statistics are unreliable at this scale and the paper does not carry appropriate caveats into the results interpretation.** The single-expression classification task (Table 4) covers 10 emotion classes across 140 clips; from Figure 2C, anger (~25 clips), surprise_neg (~25 clips), and disgust (~30 clips) contribute minimal per-class samples. Multiple per-class accuracy entries in Table 4 show 0% for multiple models, which is noise at this sample count rather than a meaningful measurement. The paper reports these values to whole-percentage precision but treats them as interpretable signals — e.g., "AffectGPT still retained its tendency to give neutral predictions, though less so than before" (Section 5.2). Statistical reliability of these per-class numbers is not acknowledged in the results discussion despite the scale issue being noted in Section 3.

- **The emotion cue grounding task is framed as a benchmark in Section 4.1 but receives no quantitative evaluation in Section 5.3.** Section 4.1 introduces it as one of "three tasks" with benchmark intent; Section 5.3 states "we manually inspected several randomly selected videos." No metric is defined, no systematic comparison is made, and no reproducible measure is reported. Calling this a benchmark task overstates what is done and sets expectations the qualitative inspection cannot fulfill. The paper already has ground-truth cue descriptions from annotators that could support at minimum a keyword-overlap or agreement measure against model outputs.

### Minor

- **Near-chance inter-annotator agreement for surprise_neg (α = 0.119) and disgust (α = 0.166) is documented in Table 2 but not flagged when interpreting emotion classification results.** When Table 4 is discussed, confusion errors and model biases involving these categories are described as model failures without acknowledgment that the ground-truth labels in these categories are themselves weakly agreed upon. Given these α values are close to zero on a −1 to +1 scale, results in these categories should carry explicit reliability caveats.

- **The proposed explanation for neutral-to-positive model bias — RLHF alignment — is speculative.** Section 5.1 presents this as "a possible reason" and appropriately hedges with "more research is required," but the explanation is given more narrative weight than its support warrants. Training distribution skew and prompt phrasing are equally plausible, and no test distinguishes among these explanations.

### Trivial
None identified beyond parser artifacts already excluded per policy.

---

## Nice-to-Haves

- Including clips where VADER score and annotator label clearly diverge as a sub-analysis group would sharpen the paper's central modality comparison claim. Even 20–30 such clips would let the paper directly show models fail in cases where text provides misleading signal, which is a cleaner test of the thesis that models over-rely on text.
- Bootstrap confidence intervals on wF1 for Table 3 main results would meaningfully contextualize whether cross-model and cross-condition differences are reliable or within noise — especially important given the 200-clip scale.
- A simple keyword-match or annotator-cue overlap measure between model grounding outputs and the ground-truth cue descriptions would convert Section 5.3 from qualitative illustration to a quantitative benchmark, without requiring new data collection.
- Multi-label classification results on the 37 multi-expression clips are deferred to future work. Even preliminary, exploratory numbers on this subset would make the benchmark more complete, as those clips represent 18.5% of the dataset.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Strength Finder claim that VADER pipeline "enhances dataset robustness for benchmarking"**: This directly conflicts with the verified VADER confound weakness. The selection mechanism creates an experimentally convenient but confounded dataset for caption-vs-video comparisons. Removed per the rule that when a strength and weakness disagree, the weakness wins.

- **Harsh Critic claim about clips annotated by only one annotator contributing "no agreement information"**: This is a genuine procedural edge case (Section 3.3 notes "minimally 1, maximally 3 annotators") but the harsh critic inflates it without quantifying how many clips are affected. Without a count, this is a speculative severity claim. Downgraded to not-retained because the frequency is unestablished.

- **Harsh Critic request for more diverse signer pool beyond ASLLRP**: Legitimate scope concern but it's scoped out in Section 6 ("Future work can adapt our annotation pipeline to incorporate sign videos in more naturalistic settings"). Criticizing a first-of-kind dataset for not solving generalization immediately is scope creep given explicit acknowledgment.

- **Harsh Critic request for multi-label results**: The paper explicitly scopes this to future work (Section 6). Retained as a nice-to-have rather than a weakness.

- **Harsh Critic "structural" framing of the VADER confound as near-fatal**: The confound is real and Major, but it does not invalidate the dataset itself or the general finding that models fail visually. The dataset remains usable and the direction of the finding remains supported. Retained as Major, not promoted to Fatal.

---

## Novel Insights

The paper's most novel contribution beyond the dataset itself is the empirical documentation — across four independent models and multiple conditions — that contemporary MLLMs systematically construct post-hoc textual rationalizations for emotional predictions rather than independently grounding emotions in visual content. The Figure 3 demonstration that the same visual cue receives opposite emotional valence depending on caption availability is a concrete, reproducible illustration of this failure mode. This finding has implications beyond ASL: it suggests that standard video+caption inputs may cause MLLMs to suppress genuine visual reasoning in favor of text-driven confabulation, a problem that should motivate architectural and evaluation work in multimodal emotion recognition more broadly.

---

## Suggestions

1. **Reframe the modality comparison claim** to acknowledge the VADER confound explicitly: state that caption-only performance is an upper bound inflated by the selection procedure, and qualify the "reliance on text" finding accordingly.
2. **Add a supplementary table** showing per-class sample counts in Table 4 so readers can immediately assess statistical reliability for each emotion category.
3. **Flag α < 0.25 categories** (surprise_neg, disgust) with explicit caveats in Section 5.2 wherever per-class model behavior in those categories is discussed.
4. **Convert Section 5.3 to a simple quantitative task** using keyword or concept overlap between model outputs and ground-truth cue descriptions, using the already-collected annotator free-text responses as reference.

---

## Score and Decision

**Calibration summary:**

| Anchor | Avg Score | Round | Comparison |
|---|---|---|---|
| EqCbc4wrzy (Multimodal Deception Dataset) | 2.50 | R1 (low band) | Weaker than EmoSign — dataset effort without careful annotation expertise |
| lMW9d1AqC9 (Sign Language to SQL) | 1.67 | R1 (low band) | Much weaker — pseudoscientific framing |
| YrxhSkfHh0 (UniFast HGR multimodal) | 3.33 | R1 (low band) | Weaker — method paper with limited empirical grounding |
| f1uXrAjpOH (OV-MER Dataset+Benchmark) | 5.40 | R1/R2 (mid band) | Most comparable topically — larger scale, more comprehensive benchmark, but EmoSign more methodologically careful on annotation side; EmoSign weaker on benchmark design |
| nY9nITZQjc (MIntRec2.0) | 6.50 | R1 (mid-high) | Stronger — 15,040 samples, 30 classes, accepted |
| sMFqEror1b (MMToM-QA) | 4.75 | R1 (mid band) | Comparable scope, similar rejection outcome |
| 9DDJuab67K (Unimodal Distillation MER) | 3.80 | R2 (low-mid) | Weaker — methods paper with modest contribution |
| powufeT93G (Domain-Specific Embeddings) | 5.25 | R2 (mid) | Less comparable; EmoSign's niche contribution comparable in standing |
| a4sknPttwV (DCA-Bench) | 5.50 | R2 (mid) | Comparable benchmark contribution, EmoSign slightly below due to design confound |

**Round 1 bracket:** 4.0–6.0

**Round 2 narrowing:** The closest anchors are f1uXrAjpOH (5.40, rejected) and sMFqEror1b (4.75, rejected). EmoSign is comparable in spirit to these — a dataset+benchmark paper in a specialized domain with genuine contribution but significant methodological limitations. It falls below f1uXrAjpOH in scale and benchmark comprehensiveness, and carries a structural confound in its key experimental design (VADER selection), a qualitative-only grounding "benchmark," and per-class statistics that are unreliable at the given scale. The dataset contribution itself is real and fills a genuine gap, but the benchmark claims are overstated relative to the experimental support. Positioning EmoSign below f1uXrAjpOH at approximately 4.5.

**Final evaluation by axis:**
- *Originality*: High — first dataset of this kind for ASL with Deaf native signers and multi-layer annotation
- *Importance of research question*: High — practical consequences for Deaf community representation in AI systems
- *Claims well-supported*: Moderate — core finding that models struggle visually is robust; modality attribution claims are confounded
- *Soundness of experiments*: Moderate — VADER confound, small per-class samples, qualitative grounding task undermine benchmark rigor
- *Clarity of writing*: Good — well-organized, clearly explains methodology
- *Value to research community*: Moderate-high as a dataset resource; moderate as a benchmark paper

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>