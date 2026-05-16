Now I have verified the key claims against the paper. Let me produce the final consolidated review.

## Summary

The paper introduces VideoPrompter, a training-free framework that improves zero-shot video understanding by combining a frozen VLM with two generative models: a video-to-text model (Video-ChatGPT) that produces descriptive captions of the query video, and an LLM (GPT-3.5) that generates richer class-label descriptors including a Tree Hierarchy of Categories for high-level action context. The method is evaluated across three zero-shot settings (action recognition, video-text retrieval, time-sensitive tasks) on up to seven datasets, showing consistent improvements over base VLMs.

## Strengths

- **Consistent zero-shot gains across multiple VLMs and datasets**: Table 2 shows VideoPrompter improves *every* base VLM (CLIP, ViFi-CLIP, AIM, ActionCLIP) on HMDB-51, UCF-101, SSv2, and K400. CLIP gains +13.29% on HMDB-51 and +11.05% on UCF-101, directly supporting the claim that the framework boosts zero-shot performance. These improvements are substantial and consistent, not cherry-picked.

- **Generalization to three distinct zero-shot settings**: The paper demonstrates improvements not only in action recognition but also video-to-text/text-to-video retrieval (Table 3, R@1 gains of +3.11 and +1.8) and time-sensitive video tasks (Table 4, +10% on synthetic data). This breadth demonstrates that the framework is not narrowly tailored to a single task.

- **Plug-and-play design validated across four VLMs**: VideoPrompter is applied without modification to CLIP, ViFi-CLIP, AIM, and ActionCLIP, improving all of them. This supports the claim that the approach is a general-purpose module rather than a method that only works with one specific backbone.

- **Efficient descriptor design validated against CUPL**: Table 5 shows VideoPrompter outperforms CUPL (an image-focused descriptor method) on HMDB-51, UCF-101, and SSv2 while using only 3 language descriptors versus CUPL's 50, indicating the video-specific prompt design is both more efficient and more effective.

- **Ablation studies confirm design rationale**: Figure 3 (left) validates that combining video and video-textual-description embeddings outperforms either alone; Figure 3 (middle) shows CLIP-based filtering further boosts performance; Figure 4 demonstrates that VGPT and GPT-3.5 complement each other.

## Weaknesses

### Major
None.

### Minor

1. **Partially overstated comparison with fine-tuned methods**: The paper claims (lines 231, 460) that CLIP+VideoPrompter "performs on par with the fully-finetuned methods like ViFi-CLIP and ActionCLIP." While this is accurate for ActionCLIP (VideoPrompter outperforms it on all datasets) and for HMDB/SSv2 vs ViFi-CLIP, on UCF-101 the gap is notable: CLIP+VideoPrompter achieves 72.77 vs ViFi-CLIP's 77.5 (~5% gap). The claim should be qualified to match the actual numbers precisely. This does not undermine the paper's core contribution — the consistent improvements over base VLMs are real — but the phrasing unnecessarily invites skepticism.

2. **No variance estimates for stochastic generative components**: The method uses Video-ChatGPT at temperature 0.5 and GPT-3.5 at temperature 0.2, both of which produce non-deterministic outputs. All experiments appear to be single-run. Without multiple seeds or confidence intervals, the reader cannot assess whether observed improvements (e.g., +1.4 on Charades) are systematic or within noise. This is a real evidential gap, though single-run evaluations are common in the field for large-scale benchmarks.

3. **Time-consistency metric undefined**: The "time-consistency score" in Table 4 is never defined in the paper. While it is presumably from Bagad et al. (2023) [bagad2023test], the paper does not explain what the score measures, what "50.0 (chance)" means, or why a +10% gain on the synthetic dataset is meaningful. The Charades improvement (+1.4) is small and lacks variance estimates. The temporal understanding claims rest on thin evidence.

4. **High-level action context ablation not isolated from "any additional context"**: Table 6 shows that adding action context improves accuracy, but there is no comparison to simpler baselines such as a single generic context ("action," "video") or human-defined fixed categories. Without these controls, it is unclear whether the *hierarchical grouping* per se drives the gain, or whether any additional contextual information would produce similar improvements.

5. **Fusion strategy not ablated**: The weighted-average fusion in Eq. (3) uses cosine similarity as the weight β₂. The paper does not compare this to alternative fusion strategies (e.g., concatenation + projection, learned scalar, gating). While the chosen method is simple and reasonable, the lack of comparison leaves open whether a better fusion exists.

### Trivial

- **CUPL comparison caveats**: The comparison with CUPL (Table 5) is favorable to the authors' method, but CUPL was designed for images and uses GPT-3 (not GPT-3.5). The paper could briefly note that the comparison, while useful, involves different design regimes. (This does not affect the conclusion — VideoPrompter's advantage is clear.)

- **Interpretability analysis is qualitative**: Figure 2 provides an illustrative example but no quantitative evaluation (e.g., overlap with human-annotated key objects/actions). This is a nice demo but not a rigorous experimental result.

## Nice-to-Haves

- Running multiple seeds (≥3) for the main action recognition results and reporting mean/std would substantially strengthen confidence in the results, especially given the stochastic generative components.
- Adding baselines for the high-level action context: (a) single generic context, (b) human-defined categories, (c) random grouping, to isolate the value of the LLM-based hierarchical grouping.
- Briefly defining the time-consistency score from Bagad et al. for readability.
- Including an ablation of fusion strategies (e.g., averaging vs. concatenation vs. learned weights) would strengthen the methodological justification.

## Removed Points

These points were flagged but removed with justification:

1. **"The paper does not test ablating VGPT while keeping only LLM descriptors plus visual features"** — This is factually incorrect. Figure 4 (described in line 377) explicitly studies the impact of removing VGPT or GPT-3.5 individually, showing the "w/o VGPT" condition. The paper has this ablation.

2. **"The 'training-free' framing should be clarified because Video-ChatGPT is pre-trained"** — "Training-free" in this context means no fine-tuning on the target task, which is standard usage in the field. The paper is consistent with community terminology.

3. **"Table 2 organization is confusing because XCLIP/A5 are listed but not compared to VideoPrompter"** — The table clearly separates "Uni-modal zero-shot models" and "Adapting pre-trained image VL models" from the rows where VideoPrompter is applied. The organization is standard for a comparison table that situates the method in context.

4. **"High-level action context groupings may be manually refined"** — The prompt used with GPT-3.5 is provided verbatim (line 154), making the process transparent and automatic. There is no evidence of manual post-hoc editing, and Table 1 is consistent with the prompt's output format.

5. **"The paper should discuss whether CUPL's prompts were re-engineered for video"** — The paper already addresses this (lines 388-390), noting CUPL uses dataset-specific prompts and 50 descriptors. The comparison is presented as-is with the original CUPL setup.

6. **Missing related works / lack of comparison to specific training-free video methods** — The paper compares to the most relevant baseline (CUPL) and provides thorough ablations. Not citing every possible related method is not a weakness.

## Novel Insights

The reviews surface a useful tension: the paper's core empirical contribution — that simultaneously enriching visual and text representations via two distinct generative models yields consistent zero-shot gains — is convincingly demonstrated, yet several evaluation gaps prevent the results from being fully trusted. The most insightful observation from the reviews is that the stochasticity of the generative components (VGPT at temp 0.5, GPT-3.5 at temp 0.2) is not accounted for, which is a genuine methodological concern that the authors can address with multiple runs. Beyond this, no genuinely novel synthesis emerges beyond the paper's own contributions.

## Suggestions

1. **Precisely calibrate the language around fine-tuned comparisons**: Replace "performs on par with fully-finetuned methods" with a factual statement such as "CLIP + VideoPrompter is competitive with several fully fine-tuned methods (outperforming ActionCLIP on all benchmarks and approaching ViFi-CLIP on most) while requiring no task-specific training."
2. **Report multiple seeds** (at least 3) with mean and standard deviation for the main action recognition results to address the stochasticity concern.
3. **Add simpler baselines for the high-level action context ablation** (single context, human-fixed categories) to isolate whether the LLM-based hierarchical grouping specifically drives gains.
4. **Briefly define the time-consistency score** for self-contained reading, even if citing Bagad et al.

## Score and Decision

The paper presents a clean, well-motivated training-free framework with consistent improvements across multiple VLMs, datasets, and zero-shot settings. The ablations validate the key design choices. The weaknesses are real but addressable: primarily partial overclaiming and missing variance estimates, not fundamental flaws in the methodology. The core contribution is solid and believable.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>