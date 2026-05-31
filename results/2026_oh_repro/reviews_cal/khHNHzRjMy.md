## Summary
This paper introduces **EmoSign**, a multimodal dataset of **200 ASL signing videos** annotated by **3 Deaf ASL signers** with (i) sentiment labels, (ii) **10-way single-emotion labels**, and (iii) **free-text descriptions of visual emotion cues** (e.g., facial expression, speed, body language). The paper also proposes baseline benchmarks for sentiment/emotion classification using multimodal models under **video-only / caption-only / video+caption** settings and analyzes qualitative “cue grounding” behavior.

Overall: **original and valuable dataset direction**, but the **benchmark evidence and reporting currently do not sufficiently support the strongest claims about “visual emotion understanding from signing”**.

## Strengths
- **ASL-appropriate annotation source + cue rationales**: The dataset is explicitly designed around the ASL-specific issue that facial/body signals serve both grammatical and affective functions, and uses **“3 Deaf ASL signers with professional interpretation experience”** (Abstract) plus **open-ended cue descriptions** (e.g., Fig. 3 example ground-truth mentions mouth morphemes, head shake/tilt; lines 301–303). This is a concrete and meaningful design choice for construct validity in this domain.
- **Baseline design reveals a clear modality gap**: Table 4 shows a consistent pattern that **video-only performs substantially worse** than caption-only and video+caption, and the paper itself highlights the key interpretation: “**Models performed similarly in caption-only and video-caption conditions … which suggest models rely on text information**” (Table 4 caption, lines 261–262). This is a useful diagnostic result for future work.

## Weaknesses

### Fatal
None.

### Major
- **Benchmark does not isolate “emotion understanding from signing” from caption sentiment cues, yet the main conclusion is framed as a visual-integration failure.**  
  The central claim in the Abstract is that “**current multimodal models fail to integrate visual cues into emotional reasoning**” (line 9). However, the paper’s own Table 4 summary states that caption-only and video+caption are similar and suggests text reliance (lines 261–262), which admits an alternative explanation: **captions may already encode most of the emotion signal**, making the task largely solvable by text sentiment/emotion recognition. The paper does not include controls that would specifically test *visual contribution* (e.g., emotion-word masking, neutral-caption subsets, minimal pairs). As written, Table 4 supports “models rely heavily on captions on this benchmark” more strongly than it supports the broader conclusion “models fail to integrate visual cues” as a general capability statement.
- **Key dataset/benchmark statistics needed to interpret “bias toward positive emotions” and overall results are missing from the main text (label distribution, confusion patterns), and reported metrics are potentially unstable at n=200.**  
  The paper claims models “**exhibit bias towards positive emotions**” (Abstract, line 9; also line 28), but the excerpted paper does not provide (in the visible sections) a label distribution table, confusion matrices, or an analysis that separates **model bias** from simply following **class priors**. Additionally, with **200 videos across 10 emotions** (Abstract), benchmark numbers in Table 4 vary widely across classes and modalities (e.g., many near-zero per-class accuracies in video-only; lines 269–272). With this dataset size, comparisons across models/modality would be much more credible with **uncertainty estimates** (e.g., bootstrap CIs) or at least clearer reporting of split protocol and class counts; these are not present in the extracted main text.

### Minor
- **Emotion cue grounding analysis is explicitly “preliminary” and anecdotal, but is used to motivate conclusions about visual grounding behavior.**  
  Section 5.3 states: “**we manually inspected several randomly selected videos**” (line 284). The observations (e.g., “recurring sense that the models were attempting to construct explanations consistent with … text sentiment”; lines 287–289) are plausible and interesting, but without a defined sampling protocol or scoring rubric they should be treated as qualitative hypotheses rather than evidence-backed findings.
- **VADER-based prefiltering risks selecting clips where English captions carry affect, potentially weakening the paper’s positioning around uniquely visual/non-manual emotional cues—this is acknowledged but not quantified.**  
  The limitations note: “**VADER offered a simple filter for emotionally salient videos; we found VADER results differed from the annotators' results** …” (lines 330–331). However, the paper does not quantify how this filtering shaped the final dataset (e.g., how many candidates were excluded/kept; how often VADER vs annotators disagree; whether selection increased caption affectivity). Given Table 4’s text-dominance pattern, this selection step becomes important to report more concretely.

### Trivial
None.

## Nice-to-Haves
- Add an **evaluation condition that masks/removes explicit emotion words** in captions (or uses caption-neutral subsets) to quantify visual contribution directly; this would align tightly with the paper’s stated goal of understanding non-manual/visual affect cues in ASL.
- Provide a **compact “dataset card” table** in the main text: emotion/sentiment class counts, clip duration stats, caption length stats, and split protocol.

## Removed Points
These points are flagged to be removed, treat them with caution.
- “The appendix/supplement likely contains missing details.” Removed because we cannot assume what is in stripped appendices; only issues verifiable from the visible text were retained.
- Any criticism asserting certain cited models/tools/datasets are unavailable or unreleased. Removed per instruction (citations are assumed to exist).

## Novel Insights
The paper’s own results already imply a key diagnostic: **EmoSign, as currently constructed/evaluated, seems to function more as a “caption emotion inference” benchmark than an ASL-visual-affect benchmark**, because caption-only ≈ video+caption (Table 4 caption, lines 261–262). This is not merely a baseline weakness; it is a dataset/benchmark design signal. A simple redesign (caption masking / neutral-caption subset) could convert the same annotation effort into a much cleaner probe of *non-manual affect understanding*, matching the paper’s motivating linguistic argument.

## Suggestions
- **Tighten the main claim**: either (a) restrict claims to “on EmoSign, models rely on captions and struggle in video-only,” or (b) add benchmark controls that directly measure incremental value of visual cues (masking/minimal pairs/subsets where annotators mark visually-driven affect).
- **Add dataset statistics necessary for interpreting bias and difficulty**: label distribution (emotion + sentiment), confusion matrices for at least the best model, and a clearer statement of split strategy; if possible, add bootstrap CIs for totals in Tables 3–4.
- **Make VADER filtering impact explicit**: report candidate pool size, selection rate, and a small analysis of caption affectivity before/after filtering.

## Score and Decision

**Axis-based evaluation (language first):**
- **Originality:** High for ASL emotion + cue rationales annotated by Deaf signers; this combination is distinctive.
- **Importance:** High; emotion in sign language and the grammatical-vs-affective facial cue entanglement is a real and under-served problem.
- **Claims well-supported:** Medium-low; the strongest “visual integration failure” claim is not cleanly identified by the current benchmark design.
- **Soundness of experiments:** Medium; baseline comparisons exist, but small-n reporting and lack of controls/uncertainty weaken conclusions.
- **Clarity:** Generally clear in what is shown (e.g., Table 4 interpretation is explicit), but missing key benchmark/dataset stats in the visible text.
- **Value to community:** Potentially high as a resource; the dataset itself may be useful even if the benchmark/claims need tightening.

### Calibration anchors used (all retrieved)

**Round 1 anchors**
- Weak band (<3.5):
  - `EqCbc4wrzy.md` (avg 2.50, R1) — substantially weaker than this paper; lacks clear benchmark validity and has fuzzier construct definition.
  - `gNoqEdT2wO.md` (avg 2.33, R1) — weaker; generic benchmark issues.
  - `YGWxpOI6Y0.md` (avg 3.40, R1) — weaker; method-focused reject.
  - `ujNe7sybJu.md` (avg 2.50, R1) — weaker.
- Middle band (3.5–7.5):
  - `L2kbdthX5M.md` (avg 6.25, R1) — stronger engineering/scale; this paper is narrower/smaller and less benchmark-rigorous.
  - `f1uXrAjpOH.md` (avg 5.40, R1) — comparable tier; both are dataset/benchmark papers with evaluation-design concerns.
  - `7kRFnSFN89.md` (avg 5.00, R1) — similar tier but different topic; this paper’s dataset contribution is clearer than that anchor’s method pitch.
  - `0Xt7uT04cQ.md` (avg 6.40, R1) — stronger/scale; above this paper.
- Strong band (>7.5):
  - `z8sxoCYgmd.md` (avg 8.00, R1) — clearly stronger: larger benchmark, clearer tasks, more comprehensive validation.
  - `HnhNRrLPwm.md` (avg 8.00, R1) — stronger.
  - `uAFHCZRmXk.md` (avg 8.00, R1) — stronger.
  - `TPZRq4FALB.md` (avg 8.00, R1) — stronger.

**Round 1 bracket:** based on these, EmoSign is **between 5 and 6.5** (clearly above weak rejects; clearly below the best-in-class benchmark papers around 8).

**Round 2 anchors (inside bracket)**
- 4.5–6.0:
  - `kiwyQsZIGP.md` (avg 5.00, R2) — comparable quality; both emphasize evaluation validity. EmoSign is similar/slightly stronger in domain specificity but weaker in benchmark controls.
  - `2ET561DyPe.md` (avg 5.50, R2) — comparable; EmoSign’s dataset novelty is good but experimental/statistical reporting is less complete.
  - `ybiwT2yP1c.md` (avg 5.00, R2) — comparable tier.
  - `Dtxc7mlKRg.md` (avg 4.60, R2) — this paper is stronger than this anchor.
- 6.0–7.5:
  - `L2kbdthX5M.md` (avg 6.25, R2) — overall stronger than EmoSign due to scale and benchmark maturity.
  - `0Xt7uT04cQ.md` (avg 6.40, R2) — stronger.
  - `ybfmpJiKXX.md` (avg 6.33, R2) — comparable/slightly stronger; more complete dataset reporting.
  - `T5QLRRHyL1.md` (avg 7.00, R2) — stronger.
  - `cpGPPLLYYx.md` (avg 6.50, R2) — stronger overall benchmark construction and analysis.
  - `le4IoZZHy1.md` (avg 6.20, R2) — somewhat stronger evaluation protocol.
  - `vvi5OjPhbu.md` (avg 6.50, R2) — stronger scale and dataset completeness.
  - `fCi4o83Mfs.md` (avg 6.75, R2) — stronger analysis.

**Narrowing to final score:** Compared to the ~6.2–6.5 anchors, EmoSign is **weaker on benchmark rigor/controls** and **missing key stats/uncertainty**, but it is **clearly above 4.6–5.0 level** because the dataset contribution is concrete and the main experimental finding (caption dominance; video-only weakness) is clearly reported. Net: **near the upper end of 5–6 but below 6.0–6.5 accept-tier benchmark papers**.

## Score and Decision
**Score: 5.5**  
**Decision: Reject** (promising dataset idea and annotation design; benchmark validity/claim support not yet at ICLR bar)

MY FINAL SCORE: <score>5.5</score>  
MY FINAL DECISION: <decision>Reject</decision>