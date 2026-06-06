## Summary

EmoSign introduces the first ASL emotion dataset annotated by three Deaf native ASL signers with professional interpretation experience, providing sentiment ratings (7-point scale), emotion category intensities (10 categories), and free-text descriptions of emotional cues for 200 video clips. The paper accompanies the dataset with baseline benchmarks of four multimodal LLMs (GPT-4o, AffectGPT, Qwen2.5-VL-7B, MiniGPT4) under three modality conditions (caption-only, video-only, video+caption), finding that models fail to meaningfully integrate visual cues and exhibit positive-emotion bias. The core contribution is the dataset itself and the documentation of a clear gap in current model capabilities for sign language affective understanding.

---

## Strengths

- **First sign-language emotion dataset annotated by Deaf native signers (Table 1, Section 3.2).** Table 1 confirms no existing ASL dataset (YouTube-ASL, OpenASL, How2Sign, ASLLRP, MS-ASL, ASL STEM Wiki) contains sentiment or emotion labels. The choice of Deaf annotators with professional interpretation experience is specifically motivated by the known problem that hearing individuals frequently misinterpret signers' facial expressions (Lim et al., 2024), a problem documented for the prior closest work FePh.

- **Multi-layer annotations covering sentiment, emotion intensity, and open-ended cue descriptions.** The dataset provides fine-grained 7-point sentiment, 0–3 intensity ratings across 10 emotion categories, and free-text descriptions of the visual cues that drove each judgment (Section 3.2, 3.4). The cue descriptions identify concrete, previously undocumented patterns (mouth morphemes, sign size/speed modifications, body orientation shifts) and are directly used as ground truth in the grounding analysis of Section 5.3.

- **Reasonable overall inter-annotator agreement contextualized against community standards.** Table 2 reports an average Krippendorff's α of 0.593; the paper correctly notes this exceeds Fleiss' κ for both MELD (0.43) and IEMOCAP (0.48), grounding the reliability claim in relevant comparison points.

- **Benchmark results concretely expose model failure modes.** Tables 3 and 4 show that video-only performance is systematically poor across all four models, with AffectGPT producing near-constant neutral output and GPT-4o collapsing to a happiness/frustration vocabulary without textual context. The qualitative grounding analysis in Figure 3 demonstrates that the same visual cue (e.g., hand movement near the face) is interpreted in opposite emotional directions depending on caption availability—a specific, paper-grounded failure mode rather than a generic observation.

---

## Weaknesses

### Fatal
None.

### Major

- **VADER-based clip selection partially confounds the caption-only benchmark condition.** Section 3.1 states explicitly that the final 200 clips were selected as "the 100 most positive and 100 most negative utterances based on VADER scores." This guarantees that the English captions in the dataset are on average unusually emotionally salient compared to an unfiltered ASL corpus. When models are evaluated in the caption-only condition against these same emotionally extreme captions, they benefit structurally from the selection mechanism—regardless of whether individual annotator labels diverge from VADER predictions. The paper's central comparative claim in Sections 5.1–5.2 ("models rely on text captions for emotion reasoning") is therefore partially inflated by design: caption-only performance looks good partly because the captions were selected to be emotionally extreme. The video-only finding (models fail visually) is *not* confounded and remains valid, but the specific conclusion that captions are particularly informative relative to video needs to be stated with greater care. Section 6 acknowledges that VADER labels often differed from annotator labels on individual clips, but does not address the distributional-level issue.

- **Per-class benchmark statistics at this scale lack reliable interpretation.** The emotion classification task (Table 4) operates on 140 single-expression clips distributed across 10 categories. From Figure 2C, several categories appear in roughly 25–30 clips before single-expression filtering, meaning some per-class test sets likely contain single-digit sample counts. Per-category accuracy reported to integer precision (e.g., SP(N) = 67 for MiniGPT4 Caption) is not a stable measurement at this scale — a single flip could change it by 15+ points. The paper acknowledges small size in Section 3 but does not carry this caveat into the results discussion, where categorical patterns are stated as findings (e.g., Section 5.2: "Qwen2.5 to happiness and neutral," "GPT-4o almost always classified videos as displaying either happiness or frustration"). These are likely real tendencies, but their magnitude cannot be reliably quantified from per-class statistics at this sample size.

### Minor

- **Emotion cue grounding is framed as a benchmark task but has no quantitative evaluation.** Section 4.1 introduces it as one of "three tasks of increasing complexity," alongside the sentiment and classification tasks that receive numerical results. Section 5.3 then reveals the treatment is entirely qualitative: "we manually inspected several randomly selected videos." The asymmetry between framing and execution is misleading. Ground-truth cue descriptions exist in the dataset (Section 3.4); even keyword overlap or binary match between annotator descriptions and model reasoning outputs would give quantitative traction. As written, it is exploratory analysis, not a benchmark.

- **Very low inter-annotator agreement for surprise_neg (α = 0.119) and disgust (α = 0.166) is unremarked in the results discussion.** Table 2 reports these values near chance for ordinal labels. The results in Table 4 report per-class accuracy for SP(N) and DG without noting that the ground-truth labels for these categories carry substantial annotation uncertainty. This limitation should be flagged when interpreting model performance on those specific categories.

- **Clips annotated by a single annotator contribute to majority vote without explicit frequency reporting.** Section 3.3 notes labels may come from "minimally 1, maximally 3 annotators" due to skips, but does not report what fraction of clips fall into the single-annotator case. Those clips provide no agreement information and bypass the majority-vote mechanism entirely.

### Trivial

- The neutral-to-positive model bias is attributed to RLHF training objectives (Section 5.1), but simpler explanations (training-distribution skew, prompt-induced priors) are equally plausible. The hedge "more research is required" is appropriate, but the RLHF framing is given more narrative weight than its evidence warrants.

---

## Nice-to-Haves

- Including a small subset (~20–30 clips) where VADER captions are emotionally neutral but annotators identified strong visual emotional content, and analyzing model performance on that subset separately, would sharpen the claim about caption reliance vs. visual failure without requiring new data collection.
- Bootstrap confidence intervals or standard errors on the wF1/wAcc numbers in Tables 3 and 4 would help contextualize whether inter-model differences are within noise at this sample size.
- The 37 multi-expression clips are already annotated and represent 18.5% of the dataset. Preliminary multi-label classification results, even as an appendix, would make the benchmark more complete rather than leaving it as explicitly deferred future work.
- Caveating in Section 5 that ASLLRP's controlled lab conditions and 4-signer pool may not generalize to naturalistic ASL signing would bound the scope of the conclusions more accurately.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Harsh Critic: "The VADER confound fatally undermines the paper's central claim."** Demoted from fatal to Major. The video-only condition is not confounded, and the paper's most durable finding—that models fail visually at ASL emotion—stands independently of the caption-only comparison. The confound limits strength of the caption-reliance claim, not the core dataset contribution or the visual-failure finding.

- **Strength Finder: "Dataset construction ensures emotional salience through VADER."** Removed as a standalone strength. The VADER selection is a design choice with mixed consequences: it achieves emotional salience (genuine benefit for dataset utility) but creates a benchmark confound (cost for the comparative claims). Listing it as an unqualified strength conflicts with the verified Major weakness above.

- **Strength Finder: "Benchmark experiments directly expose a critical failure."** Partially retained (visual failure finding is solid) but stripped of the claim that caption-reliance is cleanly demonstrated, given the VADER confound.

---

## Novel Insights

The paper's most genuinely interesting finding—verifiable from Figure 3 and Section 5.3—is that models do not simply fail to process visual information; they actively reinterpret the same visual evidence in opposite emotional directions depending on whether text is present. This is not merely a modality-weighting failure but suggests the visual reasoning pipeline is post-hoc rationalization of text-driven conclusions rather than independent visual analysis. This finding, if generalized with systematic treatment, would be a meaningful contribution to the broader multimodal-grounding literature beyond ASL, since it provides direct behavioral evidence for the "language shortcut" hypothesis in affective models. The dataset's free-text cue descriptions from native signers are the right instrument to test this systematically—an opportunity the current paper only partially exploits.

---

## Suggestions

1. **Address the VADER confound explicitly in the paper.** Add a paragraph in Section 5 noting that caption-only performance may be elevated relative to naturalistic distributions because VADER selected emotionally extreme captions. This does not invalidate the result; it scopes it.
2. **Report confidence intervals (even informal ranges) for wF1/wAcc** given the sample sizes, especially in Table 4 per-class columns.
3. **Relabel the "emotion cue grounding" section** as "qualitative analysis" rather than a benchmark task, or add even a lightweight quantitative match metric.
4. **Flag per-category results for surprise_neg and disgust** in the Table 4 discussion as subject to annotation uncertainty per Table 2.
5. **Report the frequency of single-annotator clips** to let readers assess label quality exposure.

---

**Evaluation on key axes:**

- **Originality:** High — genuinely the first dataset of its kind for a documented gap.
- **Importance of research question:** High — sign language emotion recognition has real-world consequences and no prior annotated resources.
- **Claims well supported:** Moderate — the visual-failure finding is well-supported; the caption-reliance claim is partially confounded by data selection.
- **Soundness of experiments:** Moderate — annotation methodology is careful and rigorous; benchmark design has a structural confound and small-scale reliability issues.
- **Clarity of writing:** Good — the paper is clearly organized and accessible.
- **Value to research community:** High — a novel dataset resource with baseline benchmarks fills a real gap; the qualitative findings provide motivation for future model development.

---

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>

<subscores>
<originality>4</originality>
<importance>4</importance>
<claims_supported>3</claims_supported>
<soundness>3</soundness>
<clarity>4</clarity>
<community_value>4</community_value>
</subscores>