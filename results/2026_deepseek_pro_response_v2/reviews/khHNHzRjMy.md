Now I have a complete set of comparisons. Let me write the final review.

**Calibration summary:**

Round 1 bracketing:
- MDPE (2.50, Reject) — clearly below EmoSign
- OV-MER (5.40, Reject) — EmoSign is somewhat stronger (cleaner methodology, genuine expert annotation, no data leakage issues)
- SignAvatars (6.25, Reject) — clearly above EmoSign (much larger scale, more comprehensive)
- Uni-Sign (6.40, Accept) — clearly above EmoSign (larger scale, SOTA results, more comprehensive evaluation)
- MIntRec2.0 (6.50, Accept) — clearly above EmoSign

Round 2 narrowing:
- Shot2Story (5.50, Accept) — EmoSign is comparable. Shot2Story has far larger scale (43K videos) but its annotation pipeline is GPT-4 + human verification and was criticized for limited novelty. EmoSign has unique, expert-driven annotations filling a genuine gap but has more concrete methodological limitations (VADER filtering, low IAA categories).
- Sign2GPT (5.75, Accept) — EmoSign is slightly below (method paper with SOTA results vs. dataset paper with first benchmark)
- DTVLT (4.60, Reject) — EmoSign is clearly stronger

**Final score: 5.5** — between OV-MER (5.40) and Shot2Story (5.50), comparable in overall quality to Shot2Story but with different tradeoffs.

---

## Summary

EmoSign introduces the first ASL video dataset with fine-grained sentiment and emotion annotations from Deaf native signers. It contains 200 utterances (selected as the 100 most positive and 100 most negative by VADER text filtering from ASLLRP) annotated for sentiment (7-point scale), 10 emotion categories (intensity 0–3), and open-ended emotion cue descriptions. The paper benchmarks four multimodal LLMs on sentiment analysis, emotion classification, and emotion cue grounding across caption-only, video-only, and video+caption conditions. The key finding is that models integrate visual information for coarse sentiment but fail to do so for fine-grained emotion classification, relying on text shortcuts instead.

## Strengths

- **Deaf native signer annotators with professional interpretation experience**: The dataset's credibility rests on this design choice. Recruiting Deaf native signers who can distinguish grammatical from emotional facial expressions is essential given that hearing individuals frequently misinterpret signers' expressions (Lim et al., 2024, cited in the paper). This directly addresses a limitation of prior work like FePh, which used hearing annotators (Section 2, lines 77–83).

- **Multi-layered annotation scheme with open-ended cue descriptions**: Beyond categorical labels, the free-text cue descriptions (Section 3.2) enable documentation of *how* emotions manifest in signing. The thematic analysis in Section 3.4 identifies concrete patterns — non-manual markers (furrowed brows, pursed lips, head thrusts), sign modifications (size, speed, repetition), and contextual disambiguation strategies — that would be inaccessible from categorical labels alone. This distinguishes EmoSign from all prior ASL datasets in Table 1.

- **Ablation-based benchmark design isolating modality contributions**: The three-condition setup (caption-only, video-only, video+caption) across Tables 3 and 4 provides direct evidence for the paper's claims. The finding is nuanced: video+caption improves over caption-only for sentiment analysis (GPT-4o 7-class wF1: 18.23 → 26.35 in Table 3) but not for emotion classification (Table 4 shows caption-only and video+caption wAcc are comparable across models), suggesting models can use visual cues for coarse valence but default to text for fine-grained emotion discrimination.

- **Transparent IAA reporting with contextualization**: Table 2 openly reports per-label Krippendorff's alpha scores (average 0.593), including low values for negative emotions. This is honest and rare in the field.

- **Specific, actionable failure mode characterization** in Section 5.3 and Figure 3, including GPT-4o's repetitive "relaxed body language" phrasing, Qwen2.5's category error of requesting audio for sign language, and the finding that identical visual cues are interpreted oppositely depending on caption availability (Figure 3).

## Weaknesses

### Fatal

None.

### Major

- **VADER-based dataset construction limits benchmark scope and weakens interpretation of caption-condition results.** By selecting the 100 most positive and 100 most negative utterances based on VADER text sentiment (Section 3.1, line 115), the dataset systematically excludes cases where text is neutral but visual emotion is strong, or where text and visual emotion conflict. Caption-only sentiment baselines are elevated by construction — the captions were pre-selected to be emotionally charged. The paper briefly acknowledges the VADER limitation in Section 6 (line 330) but does not discuss how this selection bias affects the interpretation of benchmark results, particularly the caption-only and video+caption sentiment conditions. The paper's core narrative about models failing to integrate visual cues remains supported by the emotion classification results (where caption-only ≈ video+caption), but the sentiment analysis interpretation requires more careful qualification. Stratifying the dataset into cases where text sentiment aligns with versus diverges from annotator visual-emotion judgments would turn this limitation into a diagnostic feature.

- **Benchmarking on emotion categories with near-zero inter-annotator agreement is methodologically questionable.** Table 2 reports Krippendorff's alpha below 0.4 for six of ten emotion categories: surprise_neg (0.119), disgust (0.166), frustration (0.330), sadness (0.333), fear (0.351), and anger (0.370). Values of 0.119 and 0.166 indicate near-random agreement. The paper reports per-category accuracy in Table 4 (e.g., SP(N), DG, FS columns) without flagging which categories have unreliable ground truth. Models cannot be meaningfully evaluated on recognizing disgust or negative surprise if annotators themselves could not agree on when those emotions were present. The paper should either exclude unreliable categories from benchmarking or explicitly flag results on those categories as exploratory. The comparison to MELD and IEMOCAP uses different agreement metrics (Krippendorff's alpha vs. Fleiss' kappa), which limits comparability.

### Minor

- **Emotion cue grounding is framed as a benchmark task but delivers only qualitative analysis.** Section 4.1 introduces grounding as one of three benchmark tasks with a formal definition (identifying relevant frames and spatial regions), but Section 5.3 provides only manual inspection of "several randomly selected" videos with qualitative description and a single example in Figure 3. No metrics or systematic comparison are provided. The paper acknowledges this is "preliminary" (line 284), but should either reframe grounding as qualitative analysis or add a quantitative protocol.

- **Anomalous model scores are not diagnosed.** MiniGPT4's caption-only sentiment performance (Table 3: 3-class wAcc 1.92, wF1 5.92; 7-class 0.00/0.00) and AffectGPT's video-only wF1 of 0.04 are far below random chance, suggesting output format issues rather than genuine model capability. The paper does not discuss whether MiniGPT4 was producing labels outside the expected format, which affects result interpretation.

- **Different prompting strategies across models complicate comparison.** GPT-4o answers all three tasks in one API call with structured output and temperature=0, while AffectGPT, Qwen2.5, and MiniGPT4 answer each task separately with seeding (Section 4.2, lines 217–218). The paper notes this was due to output format limitations but does not discuss how it might affect cross-model comparison.

- **23 clips (200 − 140 single-expression − 37 multi-expression = 23) are unaccounted for.** Section 4.1 describes the two subsets but does not explain what happened to the remaining 23 clips or why they were excluded from benchmarking.

### Trivial

- The comparison of inter-annotator agreement with MELD and IEMOCAP uses Krippendorff's alpha for EmoSign versus Fleiss' kappa for the prior datasets. While both are chance-corrected agreement measures, they are not directly comparable and the paper should note this.

## Nice-to-Haves

- Including a simple VADER-on-captions text-only baseline for sentiment would directly quantify how much benchmark performance is attributable to the text sentiment used for dataset construction, making the contribution of visual information more interpretable.
- Fine-tuning experiments with domain-specific models would strengthen the benchmark beyond zero-shot evaluation, though the paper acknowledges this as future work in Section 6.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **Harsh Critic: "The VADER-based dataset construction creates a circularity that undermines the benchmark's central claims."** — While the VADER filtering is a real limitation (kept as Major), the "circularity" framing is overstated. The emotion classification results in Table 4 (where caption-only ≈ video+caption) are not confounded by VADER filtering — emotion labels come from annotators, not VADER. For sentiment, the finding that video+caption *improves* over caption-only remains meaningful even with elevated caption-only baselines. The paper also partially acknowledges the VADER limitation in Section 6.

- **Harsh Critic: "The benchmark evaluates only zero-shot general-purpose MLLMs with no domain-specific baselines" as a structural weakness.** — The paper explicitly frames this as baseline evaluation and acknowledges fine-tuning as future work (Section 6). Establishing zero-shot baselines is standard practice for a first benchmark on a new dataset. This is a reasonable scope choice, not a flaw.

- **Harsh Critic: "No demographic or background information about the annotators is provided" beyond what's in the main text.** — The main text provides essential qualifications (Deaf native ASL signers with professional interpretation experience) and references Appendix A.1 for recruitment details. This is adequate for the main paper.

- **Strength Finder: "Transparent acknowledgment of the VADER-text-selection tension"** — The acknowledgment in Section 6 is a single brief sentence. While honest, it is too minimal to count as a substantive strength separate from the general transparency of the paper.

## Novel Insights

The benchmark reveals a specific and potentially important dissociation: for sentiment analysis, models can integrate visual information with text to improve over text-only baselines (Table 3), but for fine-grained emotion classification, adding video does not consistently improve performance and can even decrease it compared to caption-only (Table 4). This asymmetry suggests that current MLLMs can use visual cues for coarse valence judgments but lack the granularity to distinguish specific emotions from visual input alone — they default to text when fine discrimination is required. The grounding analysis in Figure 3 provides a concrete mechanism: models interpret identical visual cues oppositely depending on which caption is available, suggesting post-hoc rationalization rather than genuine visual understanding. This finding points to a specific architectural limitation (text dominance over visual reasoning) that goes beyond simple modality fusion failures.

## Suggestions

- Explicitly characterize the VADER selection bias by reporting per-sample alignment between VADER text sentiment and annotator visual-emotion judgments. Stratifying results by alignment vs. divergence would turn the limitation into a diagnostic feature.
- Either exclude emotion categories with alpha < 0.4 from benchmark evaluation or add a prominent caveat that results on these categories are exploratory.
- Reframe the grounding section as qualitative analysis rather than a benchmark task, or add a minimal quantitative protocol.
- Report the distribution of annotator coverage per clip (how many had 1, 2, or 3 annotators) and the frequency of ties in majority voting.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>