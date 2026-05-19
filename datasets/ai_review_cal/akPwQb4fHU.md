- Decision: Reject
- Avg Score: 3.67
- Scores: 5, 3, 3
Now I have sufficient information to produce the consolidated review.

## Summary

The paper proposes DeSSeR, a training-free pipeline that decomposes challenging zero-shot segmentation into recognition, localization, and segmentation stages, using M-LLMs (GPT-4o, CogVLM) for semantic guidance of an LVM segmenter (SAM). Key components include instance-aware prompting, uncertainty estimation via resampling, and selective re-localization with MLLM gridding. Experiments on camouflage object detection (CAMO), polyp segmentation (CVC300), and anomaly detection (VisA) report >10% improvements over zero-shot baselines.

## Strengths

1. **Clear isolation of the semantic bottleneck in LVMs**: Section 2.2 provides a controlled motivating experiment (100 CAMO images) showing that when SEEM fails (large MAE), adding a semantic cue (object name from M-LLM) substantially improves performance. Table 3 quantifies this with Box IoU comparisons across recognition/localization decomposition strategies. This pins down the specific failure mode (semantic lack, not visual inability) more precisely than prior work.

2. **Consistent and large improvements across diverse challenging tasks**: Table 2 shows DeSSeR outperforms all zero-shot/weakly-supervised baselines across CAMO, CVC300, and VisA, with margins the paper quantifies as >10%. The framework is training-free yet achieves results competitive with fully-supervised approaches on multiple tasks, which is a genuinely useful capability.

3. **Novel selective re-localization via MLLM gridding**: Section 3.3 introduces a training-free uncertainty estimation mechanism (sampling for consistency) coupled with a gridding-based localization strategy that uses the recognizer M-LLM to verify and correct failed localizations (Algorithm 1, lines 8-14). Table 6 confirms this component is frequently triggered and improves results; Figure 3 provides qualitative examples where gridding succeeds when the primary localizer fails. This adaptive correction extends beyond prior decomposition pipelines (e.g., CPVLF) that lack such error recovery.

4. **Systematic ablation of decomposition benefits**: Table 3 and Section 3.1 test multiple M-LLMs (both open-source and closed-source) for localization with and without decomposition (first recognize name, then localize). The consistent improvement across models provides controlled evidence for the coarse-to-fine design choice.

## Weaknesses

### Fatal
None.

### Major

1. **Missing direct comparison against a simple end-to-end model pipeline without the proposed components**: The paper compares against task-specific methods, general vision models, and LVLMs with segmentation ability (Table 2), and includes ablations of components (Tables 4, 6). However, the most natural baseline — a straightforward "ask GPT-4o for the object name → ask CogVLM for a bounding box → SAM for segmentation" pipeline, without selective re-localization, gridding, or uncertainty estimation — is not evaluated end-to-end on all three datasets. The motivating experiment (Section 2.2) shows that a naive two-step approach already improves over direct LVM segmentation, but the paper does not quantify how much additional gain the *full DeSSeR pipeline* (with its extra complexity of uncertainty estimation and gridding) provides over this simple model composition. Without this, the marginal value of the paper's novel components is unclear.

2. **VisA evaluation protocol limits comparability**: The paper evaluates only on the 1,200 anomaly-containing images of VisA (denoted "VisA\*" in Table 2), while citing fully-supervised methods. Pixel-level metrics computed on anomaly-only subsets are not directly comparable to metrics computed on the full test set (including normal images), which is the standard protocol in anomaly detection. The paper claims "results comparable to fully-supervised methods" — but this comparison may not be apples-to-apples. The authors should either (a) re-evaluate on the full VisA test set, (b) confirm that the cited fully-supervised methods also used the same subset, or (c) explicitly state the difference and quantify its impact.

### Minor

1. **Uncertainty estimation uses only n=1 resample**: Section 4.1 states "resampling time (1)" and Algorithm 1 loops `for i=1 to n` with n=1. This means a single additional sample is drawn and compared to the original prediction. Section 3.3.1 claims to "test consistency over multiple answers," which is at odds with n=1. Drawing one extra sample provides negligible information about prediction consistency; reliable uncertainty estimation typically requires more samples or model confidence scores. The authors should either justify why a single sample suffices or increase n.

2. **No variance or significance reporting**: For small test sets like CVC300 (60 images), point estimates without standard deviations or confidence intervals are hard to interpret. The paper reports only single-run point estimates for all experiments.

3. **Headline improvement numbers not cited in text**: The abstract and introduction repeatedly claim "10%+" improvement, but the specific numbers (e.g., S_α, Dice scores) appear only in embedded table images, not in running text. Quoting key values in the text would strengthen the headline claims.

### Trivial

- Several typos (e.g., "illurstrate" → illustrate, "superiorness" → superiority, "predicctionl").
- "recognization" used throughout (should be "recognition").

## Nice-to-Haves

- Report results with at least one fully open-source M-LLM constellation (e.g., LLaVA-1.6 as recognizer, Qwen-VL as localizer) for the full DeSSeR pipeline to demonstrate model-agnostic generalization beyond GPT-4o.
- Report computational overhead (API calls per image, approximate latency/cost) to help readers assess practical usability.
- Include failure case analysis: are errors primarily recognition failures, localization failures, or segmentation failures?
- Extend the error analysis (Table 4) beyond CAMO to other datasets.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"Decomposition of localization is already known"** — The paper explicitly acknowledges this (Section 3.1: "This is consistent with what previous similar work proves in VQA and language field"), so this is not a weakness, it is proper contextualization.
- **"Motivating experiment on 100 images is too small for strong conclusions"** — The paper correctly frames this as a motivational experiment, not a main result. This is appropriate for its purpose.
- **"Paper does not discuss why GPT-4V point labels don't improve performance"** — The paper does note this in Table 5 caption ("indicating that LVLMs such as GPT-4V may face challenges in fine-grained recognition"). A deeper analysis would be nice but its absence is not a weakness.
- **Generic "could be stronger with X" suggestions** from the Strengthening section — These are suggestions, not verified weaknesses. Moved to Nice-to-Haves where appropriate.
- **Formatting/style nitpicks** — Removed per instruction; these are parser artifacts, not author errors.
- **Missing related works** — Cannot verify existence of missing citations; removed per instruction.
- **Criticism about "no open-source M-LLM full pipeline" framed as fatal reproducibility issue** — The paper does test multiple M-LLMs for localization (Table 3, including open-source options) and the method is described with sufficient detail. Requiring a full pipeline with an alternative model set is a reasonable suggestion but not a fatal gap; demoted to Nice-to-Have.

## Novel Insights

The harsh critic's suggestion about the n=1 resampling being contradictory with the paper's stated goal of "testing consistency over multiple answers" is an incisive catch — the paper's text and algorithm parameters are internally inconsistent on this point. The critic also correctly identifies that the paper's strongest claim ("comparable to fully-supervised methods") rests on a VisA evaluation protocol that may differ from the cited methods' protocols, which is a genuine validity concern rather than a nitpick. Conversely, the Strength Finder correctly identifies that the paper's controlled decomposition experiments (Table 3) go beyond prior work that simply asserts LVM limitations without isolating the semantic bottleneck — this is the paper's strongest empirical contribution.

## Suggestions

1. **Add a direct end-to-end baseline**: Implement the simplest reasonable pipeline using the same models (GPT-4o → CogVLM → SAM without selective re-localization) and report results on all three datasets. This isolates the marginal gain from uncertainty estimation and gridding.

2. **Clarify or fix the VisA evaluation**: Either re-evaluate on the full VisA test set, or provide a clear statement that the cited fully-supervised methods use the same anomaly-only subset. If they do not, clearly qualify the "comparable to fully-supervised" claim.

3. **Fix the n=1 uncertainty estimation**: Either increase the number of resamples (n ≥ 3) to make the consistency check meaningful, or use an alternative uncertainty signal (e.g., model logit confidence). If n=1 is intentional, explain the rationale clearly.

4. **Include more instance-aware prompting details and failure analyses** to help readers understand when the method works and when it breaks.
