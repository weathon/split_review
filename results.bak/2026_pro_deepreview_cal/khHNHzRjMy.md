Now I have sufficient anchors to calibrate. Let me synthesize the final review.

**Calibration summary:**

| Paper | Score | How EmoSign compares |
|---|---|---|
| TemporalBench | 4.20 (R1) | EmoSign is stronger — real data, focused problem, cleaner annotation |
| MMToM-QA | 4.75 (R1) | EmoSign is stronger — real videos, not synthetic, genuine annotator expertise |
| OV-MER | 5.40 (R1/R2) | EmoSign slightly stronger — cleaner methodology, transparent IAA reporting, no data leakage |
| SignAvatars | 6.25 (R1) | SignAvatars is stronger — 70K videos, 117 hours vs 200 clips, 16 min; but automated annotations |
| Uni-Sign | 6.40 (R1) | Uni-Sign is stronger — 1,985 hours dataset + novel framework + SOTA results |

**Bracket:** 5.0–6.0. EmoSign sits above OV-MER (5.40) due to cleaner methodology, but well below SignAvatars (6.25) due to scale limitations and IAA issues. **Final score: 5.5.**

---

## Summary
This paper introduces EmoSign, the first dataset with sentiment and emotion labels for ASL videos. It contains 200 clips (~16 min) from the ASLLRP corpus, annotated by three Deaf native ASL signers with sentiment (7-point scale), 10 emotion categories (presence + intensity), and open-ended emotion cue descriptions. The paper also benchmarks four multimodal LLMs (GPT-4o, AffectGPT, Qwen2.5-VL, MiniGPT4) on sentiment classification, single-label emotion classification, and a qualitative emotion cue grounding analysis, revealing that models rely heavily on text captions and struggle to integrate visual emotion cues.

## Strengths

- **Novel dataset filling a genuine gap**: EmoSign is, to the best of my knowledge, the first dataset providing fine-grained sentiment, emotion category, and intensity labels for ASL videos, along with open-ended cue descriptions. Table 1 convincingly establishes this against existing sign language corpora.

- **Rigorous community-centered annotation**: The use of three Deaf native ASL signers with professional interpretation experience (Section 3.2) is a genuine strength. This is the right annotator population for this task — hearing non-signers frequently misinterpret Deaf signers' facial expressions, as the paper correctly notes (Lim et al., 2024). The three-layer annotation process (sentiment → emotion categories → free-text cue descriptions) with confidence ratings and a training session is thoughtfully designed.

- **Well-structured benchmark revealing model limitations**: The three-condition ablation (caption-only, video-only, video+caption) across four models (Tables 3–4) cleanly demonstrates that current MLLMs cannot leverage visual emotion cues from signing. GPT-4o's video-only 3-class sentiment wF1 of 24.43 vs. 76.72 with captions is a striking result. The emotion cue grounding analysis (Section 5.3, Figure 3) provides concrete, human-verified examples of models producing contradictory interpretations of the same visual cues depending on text context — a genuinely informative failure analysis.

- **Transparent annotation quality reporting**: Table 2 reports Krippendorff's α for every label without cherry-picking, and the paper contextualizes these values against widely-used benchmarks (MELD, IEMOCAP). This transparency is commendable and allows readers to calibrate their confidence in different parts of the benchmark.

## Weaknesses

### Fatal
None.

### Major

- **Low inter-annotator agreement undermines several emotion categories as evaluation targets**: Krippendorff's α is 0.119 for surprise-negative, 0.166 for disgust, and below 0.4 for sadness (0.333), frustration (0.330), fear (0.351), and anger (0.370). With only three annotators, agreement at these levels means the majority-vote labels carry very little signal for those categories. The paper compares these favorably against MELD and IEMOCAP (Section 3.3), but those benchmarks are themselves known for annotation ambiguity, and the comparison uses different agreement metrics (Krippendorff's α vs. Fleiss' κ). Evaluating models on categories where humans barely agree produces uninterpretable results: a per-class accuracy of 50% for "disgust" (Table 4) could reflect chance-level human agreement rather than any model capability. The paper should either restrict its benchmark claims to categories with acceptable agreement (sentiment α=0.738, joy α=0.699, excited α=0.552, worry α=0.555) or treat the low-agreement categories as explicitly exploratory.

- **Dataset scale limits benchmark generalizability**: 200 clips (16 min, 4 signers) drawn from a single corpus is a thin foundation for a benchmark. The paper cites similarly-sized high-quality datasets (Arodi et al., 2024; Krojer et al., 2024) to justify the scale, and the community-engagement challenges of collecting this data are real. But for a dataset positioned as "establishing a new benchmark" (abstract), the small number of signers and clips means benchmark results may not generalize beyond these specific utterances. This is partially addressed by the paper's own limitations section but constrains the strength of the empirical conclusions.

### Minor

- **Class-wise support counts missing from emotion classification results**: Table 4 reports per-class accuracy for 10 emotion categories but never states how many videos belong to each class in the single-expression subset (140 clips total). Without class support, per-class accuracies are uninterpretable — e.g., the "disgust" accuracy of 50% (GPT-4o, Video+Caption) could represent 1/2 correct or 10/20. The paper should add a row with per-class N values. Weighted metrics partially address this but obscure minority-class performance.

- **VADER pre-filtering is acknowledged but its effect on the benchmark is not analyzed**: The paper uses VADER on captions to select the 100 most positive and 100 most negative utterances (Section 3.1), then notes in limitations that "VADER results differed from the annotators' results" (Section 6). Since the benchmark compares caption-only, video-only, and video+caption conditions, it matters how often the text sentiment matches the visual sentiment as judged by the Deaf annotators. A brief analysis of text-visual sentiment agreement would strengthen interpretation of the modality ablation.

- **Emotion cue grounding is qualitative and selective**: Section 5.3 explicitly presents this as a preliminary analysis of "several randomly selected videos," which is appropriate. However, Section 4.1 frames it alongside the other tasks as if it were a systematically evaluated benchmark, creating a mild inconsistency in presentation.

### Trivial

- The merging of "joy" and "excited" into "happiness" is well-justified (Jaccard 0.81), but keeping "surprise-positive" (α=0.381) and "surprise-negative" (α=0.119) as separate evaluation categories while having near-chance human agreement on the latter is inconsistent.

## Nice-to-Haves

- A quantitative grounding protocol — even minimal, such as asking models to select among candidate cue descriptions — would strengthen the emotion cue grounding analysis beyond anecdotal examples.
- Macro-averaged metrics alongside the current weighted metrics would give a clearer picture of minority-class performance.
- Expanding the dataset to include more signers and utterances from additional corpora would substantially increase its value as a benchmark.

## Removed Points
These points are flagged to be removed, treat them with caution:

- *Harsh critic: "many categories must have fewer than 10 positive instances"* — This is speculative. The paper does not report per-class N for the single-expression subset, so this claim cannot be verified from the text. The underlying concern (missing class support) is retained as a Minor weakness, but the specific numerical speculation is removed.

- *Harsh critic: "the paper does not provide a convincing foundation for future research, and the structural limitations cannot be fixed through revision alone"* — This is an overall judgment, not a specific verifiable weakness. The actual structural concerns (scale, IAA) are retained separately.

- *Harsh critic: demand to expand the dataset substantially and replace qualitative grounding with quantitative* — These are scope-creep suggestions for future work, not weaknesses of the current paper. Moved to Nice-to-Haves.

- *Harsh critic: "could have noted other recent efforts in affect-aware sign language translation"* — Missing related work claim. Per rules, removed since we cannot verify the existence of un-cited works.

- *Strength Finder: "the problem is important" and similar framing strengths* — Generic/superficial. Removed.

- *Harsh critic: "the paper sometimes writes as if [emotion cue grounding] were a systematically evaluated task"* — Partially true (Section 4.1 lists it alongside other tasks), but Section 5.3 is explicitly qualitative. Demoted to Minor.

## Novel Insights
The reviewers' analysis reveals an interesting tension that the paper itself touches on but does not fully explore: the fact that VADER-based text pre-filtering and the Deaf annotators' visual judgments sometimes disagree is not just a limitation — it is actually *the most scientifically interesting property of this dataset*. These text-visual mismatches are precisely the cases where sign language emotion recognition is hardest and where multimodal models should be learning to override the linguistic shortcut. The paper's strongest contribution may not be the benchmark numbers themselves but rather the curated set of examples where visual and textual emotional signals diverge within a single communicative act. Future work could explicitly mine these mismatches as a targeted diagnostic for multimodal fusion.

## Suggestions

- Add a row to Table 4 with per-class sample counts (N) so readers can interpret per-class accuracies.
- Add a small analysis of text-visual sentiment agreement (how often do VADER caption sentiment and Deaf annotator visual sentiment agree/disagree?) to contextualize the modality ablation.
- Consider restricting the main benchmark claims to the emotion categories with α ≥ 0.4, and report the low-agreement categories in a separate exploratory analysis. This would strengthen the paper's empirical claims rather than weaken them — it shows methodological rigor.
- Tone down language like "comprehensive" and "establishes a new benchmark" in favor of more measured framing (e.g., "an initial benchmark," "a focused dataset").

## Score and Decision

This is a well-motivated paper addressing a genuinely underexplored problem with community-appropriate methodology. The Deaf native-signer annotation and the three-condition benchmark ablation are clear strengths. However, the dataset's small scale (200 clips, 4 signers) and the unreliable ground truth for roughly half the emotion categories constrain what can be claimed from the benchmark results. The paper is stronger than OV-MER (5.40, rejected) due to cleaner annotation methodology and transparent IAA reporting, but weaker than SignAvatars (6.25, rejected) due to scale. The issues are addressable but not trivial — the IAA problem in particular limits the scope of valid conclusions. A score of 5.5 reflects a paper with genuine contributions that would benefit from focused revision.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>