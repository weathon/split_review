## Summary

RadEyeVideo proposes a prompting method that converts radiologists' eye-gaze fixation data into temporally ordered video sequences (red dot overlaid on CXR images) and feeds them into general-domain video-capable LVLMs for chest X-ray report generation and diagnosis. The core idea is that prior work using static heatmaps or text prompts discards the sequential order of gaze, whereas a video representation preserves both spatial and temporal dynamics. The paper evaluates this approach across three general-domain LVLMs (LongVA, VideoLLaMA2, LLaVA-OneVision) and compares against heatmap and text-based gaze prompting as well as several medical-domain models (CXR-LLaVA, CheXagent, LLaVA-Med, CXRMate).

## Strengths

- **Novel and well-motivated video-based gaze representation**: Prior work (Kim et al., 2024a,b) represented eye-gaze as static heatmaps or text ordered by duration, both of which discard the scan-path sequence. RadEyeVideo is the first work to encode radiologists' gaze as a video, preserving the temporal progression of fixations (Section 2.2, Equations 1–4). The motivation — that expert radiologists follow structured scan paths and this sequence provides clinically relevant context — is clearly articulated and plausible. Figure 1 concretely contrasts the proposed approach against prior methods.

- **Clear and reproducible methodology**: The gaze-video construction pipeline is fully specified: fixation-duration filtering (Equation 1), frame allocation proportional to duration at 10 fps (Equation 3), and uniform sampling to a fixed number of frames (Equation 4). The thresholding, sampling strategy, and all hyperparameters (5-pixel dot radius, 16 frames, fps=10) are stated. The paper provides code to recreate the MIMIC-Eye-Video dataset, compensating for the inability to directly redistribute the MIMIC-Eye data.

- **Broad head-to-head comparison of gaze-prompting strategies**: The study compares four gaze-integration methods (NoEye, Heat Map, Fixation Text, RadEyeVideo) across three general-domain video LVLMs and four medical-domain baselines (Section 3, Table 3), using five diverse evaluation metrics (ROUGE, BERTScore, CheXbert, RadGraph, RaTEScore). This is the most comprehensive comparison of gaze-prompting formats for LVLMs in CXR analysis.

## Weaknesses

### Major

- **The Results section is virtually empty — the paper's quantitative claims are unsubstantiated by discussion**: Section 4 consists of a single three-sentence paragraph that states gaze information "generally helps" with one exception. There is:
  - No per-metric breakdown (which metrics improved most? Did RadEyeVideo help ROUGE more than CheXbert? Which radiology-specific metrics benefited?)
  - No discussion of the diagnosis task results at all (diagnosis is described as a task in Sections 2.5 and 3.3.2, with a separate CheXbert metric defined, but Section 4 only discusses Findings and Impression)
  - No comparison of performance patterns between the alpha and beta splits
  - No identification of which specific model + task combination yields the headline "up to 25.4%" improvement
  - No confidence intervals, variance estimates, or statistical significance tests (especially critical given the 92-image beta set)
  - The paper mentions "on average 7.9% performance boost on all tasks" but does not specify which split (alpha or beta) this refers to or break down the improvement per task

  For a paper making strong comparative claims ("outperform medical models as well as those specifically trained for CXR report generation"), this level of analysis is insufficient. The reader cannot evaluate whether the reported improvements are robust, concentrated in specific metrics, or driven by particular model/task combinations.

- **Only scaled composite scores are reported — raw scores are absent**: Table 3 reports only averages of metrics scaled relative to CheXagent (Equation 5). The raw scores for each of the five individual metrics are never shown. Since the paper also does not report CheXagent's raw scores on the same metrics, the scaled scores are uninterpretable without the underlying data. A single composite average obscures which dimensions of quality are actually improving and by how much. This is especially problematic because the five metrics capture very different aspects (lexical overlap via ROUGE, semantic similarity via BERTScore, clinical accuracy via CheXbert, structured clinical entities via RadGraph, and radiology-specific n-gram overlap via RaTEScore) — aggregating them into a single number loses the signal needed to understand *what* RadEyeVideo improves.

- **Diagnosis results are never reported**: Section 2.5 defines the diagnosis task, Section 3.3.2 specifies a separate CheXbert micro F1 metric for it, and the evaluation hyperparameters (Section 3.3.1) set max token length to 192 for diagnosis. However, Section 4 only discusses "Findings and Impression" with no mention of diagnosis. It is unclear whether diagnosis results are included in Table 3 or omitted entirely. This is a significant gap — the paper claims diagnosis as a task in the abstract and contributions but provides no evidence about it.

### Minor

- **The only properly held-out test set (beta) contains only 92 images**: The authors acknowledge this limitation (lines 135–137), but then evaluate primarily on the alpha set (MIMIC-CXR training split). The alpha set is problematic not in the direction the harsh critic claimed (it actually disadvantages the general-domain models, since the medical baselines were trained on it) — but it does mean the paper's generalization claims rest largely on 92 images. For the strong conclusions drawn (general-domain models with gaze "outperform medical models"), a larger held-out evaluation is needed. The paper's own limitation section notes the small dataset but does not discuss the implications for the main claims.

- **No ablation of the method's design choices**: Several hyperparameters are fixed without experimental justification: filtering fixations to those above mean duration (Equation 1), fps=10, sampling to exactly 16 frames (Equation 4), uniform rather than weighted sampling, and the 5-pixel gaze dot radius. A critical control is missing: comparing RadEyeVideo's true temporal order against a shuffled-frame version of the same video. Without this, the paper's central claim that "sequential order matters" is asserted but not directly tested — the improvements could come from the visual overlay of attention regions rather than the temporal structure specifically. The heatmap baseline partially controls for spatial attention but not for the temporal-sequence claim.

- **Textual inconsistency in the scaling metric definition**: Line 181 states: "let S_{m,CheXagent} represent the score of the **LLaVA-Med** for the same metric m." LLaVA-Med and CheXagent are different models. From context (line 179: "scaling based on CheXagent"; Table 3 caption: "scaled metrics based on CheXagent"), CheXagent is clearly the intended denominator. This is a typographical error that creates confusion about which reference model was actually used.

### Trivial

- None. The writing and presentation quality is adequate.

## Nice-to-Haves

- A control experiment comparing RadEyeVideo against a shuffled-frame video (same frames in random order) would directly test whether temporal order matters, which is the paper's core conceptual claim.
- Ablating the fixation-duration threshold (no filtering vs. mean-based vs. median-based) and the number of sampled frames (e.g., 8, 16, 32) would strengthen the methodological contribution.
- Reporting per-metric raw scores as a supplementary table would make the results interpretable and address the main weakness about the opaque scaling.

## Removed Points

*These points from inputs were removed or demoted after verification against the paper:*

- **The harsh critic's claim that evaluating on the alpha set (MIMIC-CXR training split) is a "fundamental methodological violation" that "invalidates the headline claim"** — Removed. This criticism gets the direction wrong. The medical baselines (CXR-LLaVA, CheXagent) were *trained* on the MIMIC-CXR training set; the general-domain LVLMs were not. Evaluating on the alpha set gives the medical models an advantage, not the proposed method. If RadEyeVideo+general-domain LVLMs outperform medical models on the alpha set, that strengthens the claim, not weakens it. The concern about small beta set size is retained as a Minor weakness.
- **"Scaling metric is internally contradictory and obscures the actual results"** (framed as structural) — Demoted to Minor. The text has a typo (LLaVA-Med vs. CheXagent in line 181) but the surrounding context (line 179: "scaling based on CheXagent"; Table 3 caption: "scaled metrics based on CheXagent") makes the intended reference unambiguous. The lack of raw scores is a separate concern retained as Major.
- **Formatting/style nitpicks, CXRMate inclusion criticism, temperature-0 nitpick, max-token-length criticism** — Removed per filtering rules. These reflect reviewer preferences rather than actual flaws.
- **Strength Finder's strength about "outperforming medical models"** — Moved here. The claim is made by the paper but insufficiently supported given the evaluation gaps (small beta set, no raw scores, no diagnosis results). It is not a verified strength.

## Novel Insights

None beyond the paper's own contributions. The reviews surface no observation about the method or domain that the paper itself does not already articulate.

## Suggestions

1. **Rewrite the Results section** with a thorough discussion: report raw scores per metric (ROUGE, BERTScore, CheXbert, RadGraph, RaTEScore) for each model × condition × split combination before showing the scaled composite. Break down which metrics benefit most and whether patterns differ between alpha and beta splits. Include variance estimates or confidence intervals, especially for the 92-image beta set.
2. **Report diagnosis results** or explicitly state why they are excluded.
3. **Add a control experiment** comparing true-ordering against shuffled-frame ordering to directly test the temporal-sequence claim. Also ablate at least one key hyperparameter (e.g., 16 vs. 32 frames, or fixation filtering threshold).
4. **Fix the textual inconsistency** in the scaling metric description (line 181) so the reference model is unambiguous.

## Score and Decision

**MY FINAL SCORE: <score>4.5</score>**
**MY FINAL DECISION: <decision>Reject</decision>**