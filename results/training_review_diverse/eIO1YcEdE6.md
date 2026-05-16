I now have all the information needed. Let me construct the final consolidated review.

## Summary

This paper proposes Wolf, a mixture-of-experts video captioning framework that combines outputs from multiple image-level (CogAgent, GPT-4V) and video-level (VILA-1.5, Gemini-Pro-1.5) VLMs via LLM-based summarization. The paper also introduces CapScore, an LLM-based evaluation metric for caption quality and similarity, and releases four benchmark datasets spanning autonomous driving, general scenes, and robotics. The central claim is that Wolf produces significantly more accurate, less hallucinated captions than any individual component model, with reported improvements of 55.6% (quality) and 77.4% (similarity) over GPT-4V on driving videos.

## Strengths

- **Novel mixture-of-experts summarization framework for video captioning**: Wolf is the first framework to systematically combine image-level and video-level VLMs with LLM-based summarization for video captioning (Section 3, Figure 1). The design is well-motivated: image models have richer pre-training data but lack temporal understanding, while video models handle motion but may miss fine-grained detail. The chain-of-thought approach for image models and motion captions from bounding box trajectories are sensible architectural choices.

- **CapScore metric with human alignment validation**: The paper introduces a structured LLM-based evaluation metric with two sub-scores (caption similarity and caption quality) and validates alignment against human judgments on 100 robotics videos with 10 evaluators (Section 4.2.2, Table 1, Figure 4). While limited in scope, this correlation evidence is a genuine step forward for video captioning evaluation, which has lacked standardized metrics for long-form captions.

- **Consistent quantitative improvements across diverse domains**: Wolf achieves the best or second-best CapScore across all four datasets (Tables 2, 3), and the improvement patterns are consistent — Wolf outperforms individual models on driving, Pexels, and robotics. The finetuning experiment (Section 5.4, Figure 6) demonstrates downstream utility: training VILA-1.5 on Wolf-generated captions boosts its caption similarity from 48.6% to 71.4% and quality from 26.4% to 48.0% on interactive driving videos.

- **Finetuning validation on standard benchmarks (ActivityNet, MSRVTT)**: Table 5 shows that VILA-1.5 finetuned with Wolf captions improves QA accuracy on standard benchmarks (82.6→84.3 on ActivityNet, 76.5→78.2 on MSRVTT). This is the cleanest evidence in the paper because these benchmarks are independent of Wolf's design and CapScore, directly demonstrating that Wolf captions carry useful signal for downstream model training.

- **Ablation study isolating component contributions**: Table 4 systematically ablates model combinations (CogAgent middle frame → CogAgent with CoT → adding VILA-1.5 → adding Gemini-Pro-1.5 → adding GPT-4V), showing each component positively contributes to final CapScore and the chain-of-thought procedure significantly improves image-level model performance.

## Weaknesses

### Major

- **Overclaim of "human-annotated" datasets — ground truth involves GPT rewriting for three of four datasets**. The abstract claims "four human-annotated datasets" and the contributions state "human-annotated captions." However, Section 4 reveals that only the robotics dataset (100 videos) is fully manually captioned. For the driving datasets (500 interactive + 4,785 normal videos), ground truth is constructed from structured annotations (lane modes, homotopies, agent states) and then "use GPT 3.5 to summarize each clip to build the final caption" (Section 4.1.1). The Pexels dataset captioning process is described only as "GPT-based rewriting" with no specifics. This labeling is misleading — these are best described as *structured-annotation-derived* datasets with GPT-assisted summarization, not human-annotated datasets. Readers cannot assess how much of the ground truth reflects genuine human judgment vs. GPT rewriting artifacts.

- **Missing ensemble baseline undermines the claim that Wolf's specific design drives improvements**. Wolf is an ensemble of four models (CogAgent + GPT-4V + VILA-1.5 + Gemini-Pro-1.5) with additional LLM summarization, yet it is compared only against individual component models (Tables 2, 3). An ensemble is expected to outperform any single member. The paper lacks a critical control: a baseline that runs the same four models independently and combines their outputs via a simple mechanism (e.g., concatenation + a generic GPT-4 summarization prompt) *without* Wolf's chain-of-thought prompting, motion captions, or structured summarization pipeline. Without this control, the reader cannot tell whether the gains come from: (a) having access to multiple models (trivially true), (b) Wolf's specific chain-of-thought design, or (c) Wolf's motion captions and summarization prompts. The ablation in Table 4 shows that more models help, but never compares Wolf to a non-Wolf ensemble.

- **GPT-in-the-loop evaluation creates a subtle but real bias concern**. The ground truth for the driving datasets is GPT-3.5-summarized (Section 4.1.1), CapScore uses GPT-4 (Section 4.2.1), and Wolf uses GPT-4V as a component and GPT-4 for summarization (Section 3). While this is not a strict "closed loop" (the ground truth is fundamentally derived from structured annotations, not GPT-generated content), the shared GPT family introduces a systematic style/length bias risk: GPT-4 as evaluator may systematically prefer captions that "look like" GPT-generated text. This concern is partially mitigated by: (a) the human correlation study on 100 robotics videos (which uses fully manual ground truth), (b) the finetuning results on ActivityNet/MSRVTT (which are independent benchmarks), and (c) the use of different GPT variants (3.5 for ground truth, 4 for evaluation, 4V as a Wolf component). However, the paper does not quantify this risk or evaluate with an independent non-GPT evaluator on the main driving benchmarks.

### Minor

- **Human validation of CapScore is limited to one domain (robotics, 100 videos).** The human-evaluation correlation (Table 1, Figure 4) validates CapScore only on the smallest dataset (100 robotics videos). The headline quantitative results — the 55.6% and 77.4% improvements on driving videos — rely on CapScore without corresponding human validation on driving data. Given that the driving ground truth involves GPT-3.5 (unlike the fully manual robotics ground truth), the correlation between CapScore and human judgment on driving-domain data is unknown.

- **Frame sampling asymmetry between Wolf and GPT-4V baseline.** GPT-4V receives 16 uniformly sampled frames (Section 5.1), while Wolf samples 2 fps — which could be 40 frames for a 20-second clip. This asymmetry gives Wolf more visual information and confounds the comparison: is Wolf better because of its summarization framework, or because it simply sees more frames? A controlled comparison where GPT-4V receives the same number of frames at the same density would be more informative.

- **Structural alignment between Wolf's motion captions and the driving ground truth pipeline.** The ground truth for the driving dataset is constructed using lane modes, homotopies, and agent states (Section 4.1.1). Wolf's motion captions use bounding box trajectories (Section 3). Both pipelines derive motion information from similar underlying spatial annotations for the NuScenes dataset. This structural similarity could give Wolf an advantage on the driving benchmark that may not transfer to other domains — the paper does not discuss this potential confound.

- **Finetuning experiment (Table 5) confounds caption quality with data quantity.** The finetuned VILA-1.5 model is trained on Wolf-generated captions for 4,785 additional videos beyond the original training data. The improvement over the baseline could partially reflect simply having more training data rather than the quality of Wolf's captions. A control finetuned on an equal number of captions from another source (e.g., GPT-4V-generated captions for the same videos) would isolate the contribution of Wolf's caption quality.

- **Latency/cost comparison absent.** The paper discusses efficiency optimization (Section 6) but provides no quantitative comparison of Wolf's inference cost vs. single-model baselines. Running four models (including GPT-4V and Gemini-Pro-1.5) and an additional GPT-4 summarization step is clearly more expensive than any single model; the magnitude of this overhead should be reported to let readers assess the practical trade-off.

### Trivial

- Prompt templates for chain-of-thought generation, motion caption summarization, and the final summarization are described at a high level but not reproduced verbatim in the main text or appendix, which would aid reproducibility.
- The description of frame rate adaptation ("For short videos that sample less frames, we will increase fps to capture more details," Section 5.1) is vague — no threshold or adjustment rule is given.
- Statistical significance (confidence intervals, standard deviations) is not reported for the main CapScore comparisons, which would be valuable given variability in LLM-based scoring.

## Nice-to-Haves

- A validation of CapScore against human judgments on the driving datasets (not just robotics), even on a subset.
- Reporting Wolf's performance with standard n-gram metrics (CIDEr, BLEU) on the robotics dataset (which has fully manual ground truth) as an orthogonal check.
- A latency/cost breakdown comparing Wolf to individual models.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **CapScore prompt issue**: Removed because the reviewer claimed the prompt asks to score "captions 1, 2, 3, 4 and 5" without the ground truth. The paper clearly states "Assume we have 6 captions" where caption 6 is the ground truth reference — the prompt correctly asks to score the 5 candidate captions against it. No error exists.

- **"Ground truth transparency buried in long paragraph"**: Removed because the sentence "All captions were generated using a combination of ground truth information, rule-based heuristics, human labeling, and GPT-based rewriting" appears as the opening statement of Section 4, before any subsections. It is prominently placed, not buried.

- **"Extensive description of lane modes is overly detailed"**: Removed because this is a judgment about scope/style, not a substantive weakness. The detail is directly relevant to how the driving ground truth is constructed, which is critical for understanding the data quality.

- **"Related work section is thin"**: Removed per instructions — missing related works should not be mentioned as I cannot verify their existence.

- **"Leaderboard is not yet available" as a weakness**: The paper transparently states "will be released upon publication" (Section 4.2.3). This is a promise about future work, not an overclaim of current accomplishment. Minor at most.

- **"Missing appendix/proofs"**: Removed per instructions — the parser strips appendix content; they exist in the original submission.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the key tension in the paper: Wolf's core idea (ensemble of VLMs + LLM summarization) is sensible and the finetuning evidence suggests genuine utility, but the evaluation framework has enough GPT overlap to erode confidence in the headline quantitative claims. The most productive path forward would be to add an ensemble baseline and evaluate on at least one dataset with fully independent (non-GPT) ground truth for the main results. The paper's contributions are real but the evidence is weaker than claimed.

## Suggestions

1. **Add a naive ensemble baseline**: Have the same four component models generate captions independently, concatenate them, and feed to GPT-4 with a simple summarization prompt (without Wolf's chain-of-thought or motion captions). If Wolf still outperforms this baseline, the specific design choices are validated. If not, the "mixture of models" effect is dominant.

2. **Evaluate on at least one dataset with fully independent ground truth** for the main results — either manually caption a larger subset of driving videos (200-300 videos), or use the fully manual robotics dataset (which at 100 videos is too small for the headline claim but could be expanded).

3. **Control for frame count**: Feed GPT-4V the same number of frames that Wolf uses (2 fps) to isolate whether Wolf's advantage is from more visual information or from the summarization pipeline.

4. **Control for data quantity in the finetuning experiment**: Compare VILA-1.5 finetuned on Wolf captions against VILA-1.5 finetuned on an equal number of captions from a single strong model (e.g., Gemini-Pro-1.5) to ensure the improvement is from caption quality rather than data volume.

5. **Report CapScore standard deviations or confidence intervals** across repeated evaluations, especially given the reliance on GPT-4 scoring.

## Score and Decision

The paper proposes a well-motivated framework with genuine contributions (ensemble summarization design, CapScore metric, benchmark datasets), and the finetuning validation on ActivityNet/MSRVTT provides useful independent evidence. However, the evaluation has meaningful gaps: the headline quantitative comparisons lack an ensemble baseline control, the ground truth for the main datasets involves GPT rewriting (not pure human annotation as claimed), CapScore human validation is limited to one domain, and there are confounds in the experimental setup (frame sampling asymmetry, data quantity in finetuning). These issues collectively weaken — but do not invalidate — the central claims. The paper would be substantially strengthened by addressing them. In its current form, the evidence does not fully support the claimed superiority.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>