## Summary
This paper introduces **EmoSign**, a dataset of **200 ASL signing videos** annotated by **3 Deaf ASL signers** with (i) **sentiment**, (ii) **10-way emotion labels** (with confidence ratings), and (iii) **free-text descriptions of visual emotion cues** (e.g., facial expression, signing speed). It also proposes benchmark tasks (sentiment and emotion classification) and evaluates several multimodal models under **video-only / caption-only / video+caption** settings, concluding that current models underuse visual cues and skew toward positive emotions.

## Strengths
- **Concrete dataset contribution with ASL-expert annotation and cue rationales.** The paper specifies that 3 Deaf ASL signers annotated each video for sentiment/emotion and provided open-ended descriptions of cues (“facial expression, body language, signing speed, emphasized signs,” etc.; Sec. 3.2), which is a meaningful addition beyond label-only emotion datasets.
- **Annotation reliability is reported rather than assumed.** The paper reports **Krippendorff’s alpha per label** (Table 2) and describes the aggregation rule (“majority vote… tie broken by most confident annotator,” Sec. 3.2), giving users an evidence-backed view of label consistency.

## Weaknesses

### Fatal
None.

### Major
- **Benchmark evidence does not cleanly support the strongest claim about *visual* cue integration.** The abstract claims: “*current multimodal models fail to integrate visual cues into emotional reasoning*” (Abstract). However, the main quantitative pattern emphasized by the paper—**caption-only performing similarly to video+caption, while video-only is much worse** (e.g., Sec. 5 / tables referenced there)—is *consistent with* “models ignore video,” but it is also consistent with an alternative explanation: **captions may already carry strong affective lexical signal**, making visual cues unnecessary for the benchmark as currently posed. The paper gestures at cue grounding qualitatively (Sec. 5.3), but as written the benchmark lacks a control that isolates visual contribution (e.g., masking emotion words in captions or selecting “caption-neutral but affect-rich” clips). As a result, the headline causal interpretation (“failure to integrate visual cues”) is not firmly established by the presented evaluation design.
- **“Bias toward positive emotions” is asserted without sufficient in-paper statistical grounding tied to class distributions.** The abstract claims models “*exhibit bias towards positive emotions*” (Abstract), and Sec. 3.2 notes that “positive emotion labels had higher inter-annotator agreement than negative emotion labels.” But the benchmark sections do not, in the extracted paper text, provide the essential evidence needed to support a *bias* claim (as opposed to simple prior-following): e.g., **emotion class counts**, **confusion matrices**, or an analysis comparing predictions to the **label base rates**. Without those anchored statistics, the paper’s bias conclusion is under-justified relative to the strength of the claim.

### Minor
- **Dataset selection pipeline risks over-weighting caption/text sentiment, which may undermine the “visual affect” framing unless quantified.** The dataset is constructed by starting from ASLLRP and using **VADER** as part of selecting emotionally salient clips (Sec. 3.1: “we used VADER… to compute sentiment… then selected…”). The paper also acknowledges mismatch between VADER and annotators (Limitations). Given the paper’s goal of understanding emotion conveyed via *signing*, the paper should quantify how much the VADER pre-filter shaped what ended up in EmoSign (e.g., how often VADER was used to include/exclude candidates; distributions before/after filtering), because this pipeline could inadvertently favor clips whose **English captions already encode sentiment**.
- **Cue-grounding evaluation is presented as anecdotal rather than a defined, repeatable protocol.** Sec. 5.3 describes qualitative inspection of model outputs against annotator cue descriptions (and provides illustrative examples), but it does not define a scoring protocol or systematic evaluation subset. This limits how strongly the paper can claim the dataset “establishes a new benchmark” for cue-level grounding (Abstract) beyond being a promising resource for future grounded evaluation.

### Trivial
None.

## Nice-to-Haves
- Add a **caption-controlled benchmark condition** (e.g., masking explicit emotion words in captions; or a curated subset where annotators indicate the caption is emotionally neutral/ambiguous but affect is clear in signing). This would directly test the paper’s thesis about uniquely visual affect cues.
- Report **emotion/sentiment label distributions** and include at least one **confusion matrix** (or macro-F1 alongside weighted metrics) to make “bias” and failure modes interpretable.

## Removed Points
These points are flagged to be removed, treat them with caution.
- **“Dataset is too small to draw any conclusions / must report confidence intervals.”** While n=200 is indeed limited, small datasets can still be valuable as benchmarks/resources, and the paper does not make statistical significance claims that can be directly falsified from the text alone. The stronger, verifiable issue retained above is not “smallness per se,” but the lack of distributional/statistical evidence supporting specific conclusions like “bias toward positive emotions.”
- **“Annotation protocol is underspecified.”** The paper *does* specify key elements: 3 Deaf ASL signers, labels collected (sentiment/emotion/confidence/cues), and aggregation (majority vote; tie-break by confidence) plus Krippendorff’s alpha (Sec. 3.2, Table 2). Remaining desires (e.g., more detail on disagreements) are best framed as nice-to-haves unless a concrete omission is identifiable.

## Novel Insights
The paper’s most compelling contribution is not the baseline numbers themselves but the **combination** of (i) Deaf-signer cue rationales and (ii) a modality-factorized benchmark (video vs caption vs both). However, to make “visual cue integration” a defensible *benchmark claim* (rather than a plausible interpretation), the evaluation needs at least one **caption-leakage control**; otherwise the benchmark may primarily measure English-caption sentiment classification with optional video input, which is misaligned with the paper’s stated ASL-specific motivation about non-manual affect markers.

## Suggestions
- Introduce a **caption-masked** evaluation (mask or replace explicit affect words/phrases) and report the gap between caption-only and video+caption under masking; this would directly quantify visual contribution.
- Add a **base-rate and confusion analysis** supporting “bias toward positive emotions”: report class counts, prediction histograms, and confusion matrices (or per-class precision/recall), and compare against simple priors.
- Turn Sec. 5.3 into a small, defined protocol: e.g., for a fixed subset, have human raters score whether model explanations mention any annotator-listed cue categories (even a coarse taxonomy like face/body/speed/emphasis), producing a replicable grounding metric.

## Score and Decision
**Originality:** Moderate-high for ASL emotion as a dataset+benchmark with Deaf-signer cue rationales.  
**Importance:** High; emotion understanding in sign language is under-resourced and practically consequential.  
**Support for claims:** Mixed; dataset contribution is supported, but the *benchmark interpretation* about visual integration and bias is not yet tightly supported by controlled analyses.  
**Experimental soundness:** Reasonable as a first pass, but missing targeted controls that match the paper’s strongest causal conclusions.  
**Clarity:** Generally clear on dataset/annotation basics and agreement reporting; benchmark claims could be more carefully scoped.  
**Value to community:** Potentially high as a resource; acceptance depends on whether the benchmark claims are tightened to match the evidence.

MY FINAL SCORE: <score>6.0</score>  
MY FINAL DECISION: <decision>Reject</decision>