## Summary

This paper introduces EmoSign, the first ASL video dataset annotated for sentiment, emotion categories, and qualitative emotion cue descriptions by 3 Deaf native signers. The 200 clips are drawn from ASLLRP and selected via VADER text sentiment analysis. The paper benchmarks 4 multimodal LLMs across caption-only, video-only, and video+caption conditions, finding that current models fail to leverage visual cues for emotion recognition in sign language.

## Strengths

- **First ASL dataset with fine-grained emotional annotations from Deaf native signers**: Table 1 provides clear evidence that no existing ASL dataset includes emotion or sentiment labels. Using Deaf native signers with professional interpretation experience directly addresses a documented weakness of the closest prior work, FePh, which used hearing annotators known to misinterpret signers' facial expressions (Section 2, citing Lim et al., 2024).

- **Rich multi-layer annotation design**: The three-task pipeline (sentiment → emotion classification → free-response cue descriptions, Section 3.2) goes beyond standard label datasets. The open-ended cue descriptions provide interpretable grounding for each annotation decision and enable the emotion cue grounding task.

- **Full-body video retention capturing diverse emotional markers**: Unlike FePh (face-cropped), EmoSign retains full-body video, enabling annotation of sign speed, movement size, body posture, and head movements. Section 3.4 identifies three concrete annotation themes: non-manual markers, sign modifications, and contextual disambiguation.

- **Clear evidence of model visual grounding failure**: Tables 3 and 4 show that video-only performance is drastically worse than caption-only or video+caption across models. AffectGPT outputs neutral for nearly all video-only sentiment inputs (wF1 ≈ 0.04, Table 3), and GPT-4o defaults to only happiness/frustration predictions without captions (Section 5.2). This reveals a genuine gap in current MLLMs.

- **Insightful qualitative failure mode analysis**: Figure 3 concretely demonstrates that models interpret the same visual cue differently depending on whether text is available, suggesting post-hoc visual reasoning rather than genuine visual grounding.

## Weaknesses

### Fatal
None.

### Major

- **Text-driven selection bias confounds the modality ablation study**: The dataset was constructed by using VADER text sentiment analysis to select the "100 most positive and 100 most negative utterances" based on their text captions (Section 3.1, line 115: "we selected the 100 most positive and 100 most negative utterances based on the VADER scores"). The paper's primary analytical finding — that models "fail to integrate visual cues" and "heavily rely on text captions" (Section 5) — is then inferred from caption-only vs. video-only vs. video+caption benchmarks. But the dataset was curated for videos whose text is emotionally salient, so text being informative is partially circular. The Limitations section (Section 6) mentions that "VADER results differed from the annotators' results" but does not address how this confounds modality ablation interpretation.

- **Inconsistent model prompting makes cross-model comparison unreliable**: GPT-4o was prompted for all three tasks simultaneously with forced structured output, while other models were prompted task-by-task because they "were unable to consistently produce clean output when prompted to respond to all three benchmark tasks at once" (Section 4.2). This means GPT-4o benefits from shared context across tasks, while others do not. Tables 3 and 4 present all four models side-by-side without discussing this asymmetry.

- **Low inter-annotator agreement on several emotion categories undermines per-category benchmarking**: Table 2 reports Krippendorff's alpha for surprise_neg (0.119), disgust (0.166), frustration (0.330), and anger (0.370). Alpha values below ~0.2 indicate no reliable agreement beyond chance. Table 4 reports per-class accuracy for all 10 categories including those with near-random agreement, without discussing what this means for benchmark validity on those categories.

### Minor

- **Small dataset with no statistical reliability measures**: 140 single-expression clips across 11 classes means some classes likely have very few samples. Table 4 reports per-class accuracy with no sample counts, no confidence intervals, and no significance testing. The paper acknowledges the small size (Section 3) but does not address how this affects benchmark interpretability.

- **Emotion cue grounding analysis is purely qualitative**: Section 5.3 describes "several randomly selected videos" that were "manually inspected." For a benchmark paper, even a small-scale quantitative analysis matching model-identified cues against ground truth cue descriptions would be more convincing.

- **Krippendorff's alpha compared to Fleiss' kappa from other datasets**: Section 3.3 contextualizes the average alpha (0.593) against MELD (Fleiss' kappa = 0.43) and IEMOCAP (Fleiss' kappa = 0.48). These are different metrics not directly comparable — Fleiss' kappa is typically lower for the same level of agreement.

- **MiniGPT4 caption-only outlier unexplained**: MiniGPT4's 3-class wAcc of 1.92% and 7-class wAcc of 0.00% (Table 3) indicate fundamental task parsing failure, yet the paper includes these in cross-model comparisons without investigation.

### Trivial

- 23 clips (200 - 140 single-expression - 37 multi-expression) unaccounted for in the benchmark analysis.

## Nice-to-Haves

- Report per-class sample counts alongside accuracy in Table 4.
- Report what fraction of ASLLRP videos had neutral VADER scores but showed strong visual emotional expression, to characterize the selection bias.
- Add error bars or confidence intervals on benchmark metrics given the 200-sample dataset.
- Discuss why only 4 of ASLLRP's 19 signers are represented (Section 3.4) and implications for generalizability.

## Removed Points

These points are flagged to be removed, treat them with caution.
- Generic criticisms about dataset size (200 is small but acknowledged as pioneering effort with citations to similar-sized datasets).
- Formatting/style issues are parser artifacts, not author errors.

## Novel Insights

The paper's key novel observation is that MLLMs interpret visual emotion cues in sign language differently depending on text availability (Figure 3): one model describes the signer as showing "joyful expression" in video-only but interprets the same video as showing "frustration or anger" when captions are provided. This suggests models construct post-hoc visual explanations consistent with their text-derived sentiment judgments rather than genuinely grounding emotion in visual features — a real and underexplored failure mode.

## Suggestions

- Acknowledge the VADER-based selection bias explicitly and discuss how it affects modality ablation interpretation. Ideally, report results on a subset selected for visual emotional salience.
- Match prompting conditions across models or present GPT-4o results separately. At minimum, discuss the asymmetry and its implications for cross-model comparison.
- Exclude or caveat the low-agreement emotion categories (surprise_neg, disgust) from per-category benchmarking, or discuss how to interpret accuracy on unreliable categories.
- Report per-class sample counts and confidence intervals alongside Table 4.

## Reporting

**All anchors retrieved:**

Round 1:
- gwZ90hFSL2 (1.00) — Chinese NLP for humanoid robots, unrelated. Strong reject.
- 5lUdTogEL3 (1.00) — Person re-identification, unrelated. Strong reject.
- 5kMwiMnUip (1.40) — LLM jailbreaking, unrelated. Strong reject.
- lMW9d1AqC9 (1.67) — Sign language to SQL, different scope. Reject.
- Jq8HYNZG9s (3.00) — Shadowboxing benchmark, different. Reject.
- EqCbc4wrzy (2.50) — Multimodal deception dataset, weaker paper. Reject.
- gNoqEdT2wO (2.33) — Multimodal CL benchmark, different. Reject.
- 7kRFnSFN89 (5.00) — Sign language translation with LLMs. Reject.
- flgrH5nK4H (4.00) — One-shot ISLR. Reject.
- otoggKnn0A (4.00) — Hand action dataset. Reject.
- f1uXrAjpOH (5.40) — **OV-MER multimodal emotion dataset, most directly comparable. Reject.**
- L2kbdthX5M (6.25) — SignAvatars 3D SL dataset. Reject.
- 0Xt7uT04cQ (6.40) — Uni-Sign sign language understanding. Accept.
- LqaEEs3UxU (5.75) — Sign2GPT translation. Accept.
- F6h0v1CTpC (6.00) — EmpathyRobot dataset. Reject.
- 7gUrYE50Rb (8.00) — EQA-MX embodied QA. Accept.
- Q6a9W6kzv5 (8.00) — PhysBench VLM benchmark. Accept.
- SctfBCLmWo (8.00) — Dataset bias analysis. Accept.
- z8sxoCYgmd (8.00) — LOKI synthetic detection benchmark. Accept.

Round 2:
- mao3y822aM (5.50) — NanoLM scaling benchmark. Reject.
- 2ET561DyPe (5.50) — Few-Class Arena. Accept (borderline).
- ydH8nU5csJ (4.60) — VLT benchmark. Reject.
- H9UnNgdq0g (6.25) — MediConfusion medical benchmark. Accept.
- xLPakPOKDX (5.00) — Causal diffusion. Reject.
- vbr1OKK19i (4.75) — VQA modality ablation. Reject.
- hom2oeHCnz (5.33) — Debiasing analysis. Reject.

**Round 1 bracket: 4.5–6.5.** EmoSign is clearly above the 2.5–4.5 reject papers (MDPE, DTVLT, FHA-Kitchens) and comparable to OV-MER (5.40, rejected). It's below accepted sign language papers like Uni-Sign (6.40).

**Round 2 narrowed to 5.0–6.0.** The most comparable paper is OV-MER (5.40, rejected), another multimodal emotion dataset with benchmarks. EmoSign has clearer novelty (first ASL emotion, Deaf annotators) and stronger practical motivation, but comparable benchmark confounds.

**Final score: 5.5.** The genuine novelty of the dataset contribution (first ASL emotion dataset, Deaf annotators, compelling practical motivation) elevates it above typical reject-range papers, but the confounds in the benchmark analysis (selection bias, inconsistent prompting, low-agreement categories being benchmarked) prevent it from reaching clear accept territory.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>