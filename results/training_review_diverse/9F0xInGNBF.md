Now I have all the evidence needed. Let me construct the final consolidated review.

---

## Summary

This paper proposes VideoPrompter, a training-free framework that combines a video-to-text model (Video-ChatGPT) with an LLM (GPT-3.5) to boost the zero-shot performance of existing vision-language models (VLMs) for video understanding. The framework enriches both sides of the VLM: (1) query video features are enhanced by fusing them with video-to-text descriptions, and (2) classifier representations are enriched by LLM-generated video-specific descriptors and high-level action context. The paper evaluates across three settings (action recognition, retrieval, time-sensitive tasks) on 7 datasets with 4 different VLMs, reporting consistent improvements.

## Strengths

1. **Consistent zero-shot gains across multiple VLMs and benchmarks (Table 2).** The framework improves top-1 accuracy for CLIP (HMDB +13.29, UCF +11.05, SSv2 +2.15, K400 +4.64), ViFi-CLIP, AIM, and ActionCLIP across four action recognition datasets. This directly supports the core claim of plug-and-play adaptability.

2. **Complementary dual enhancement validated by ablation (Figure 4).** The paper shows that removing either the video-to-text module (VGPT) or the text-to-text module (GPT-3.5) yields suboptimal performance compared to their combination, and this pattern holds across benchmarks. This supports the claim that both visual feature enrichment and classifier refinement contribute.

3. **Descriptor efficiency demonstrated vs. CUPL (Table 5).** VideoPrompter outperforms CUPL (which uses 50 prompts per class) with only 3 language descriptors plus video textual descriptions, showing that carefully designed video-specific prompts are more effective than large descriptor ensembles.

4. **Evaluation across diverse settings (3 zero-shot settings, 7 datasets, 4 VLMs).** The paper extends beyond standard action recognition into retrieval and time-sensitive video tasks, demonstrating the framework's breadth and providing evidence of generality.

5. **Ablation on design choices (Figure 3).** The paper investigates fusion strategies, CLIP-based filtering of erroneous descriptions, and temperature-driven diversity, providing practical guidance for deployment.

## Weaknesses

### Fatal
None.

### Major

1. **"On par with fully fine-tuned methods" claim is not supported by the evidence.** The paper states that VideoPrompter + CLIP "performs on par with the various existing fully fine-tuned methods." On HMDB-51, VP+CLIP achieves 50.79, which is below ViFi-CLIP's baseline of 51.82. On UCF-101, VP+CLIP achieves 72.77, which is well below ViFi-CLIP's 77.50. The only fine-tuned method VP+CLIP clearly matches or exceeds is ActionCLIP (49.20 on HMDB, 69.52 on UCF). The better numbers (57.12 on HMDB) are from VP applied on top of ViFi-CLIP itself, which is a different comparison. This overclaim needs correction.

2. **Narrow baseline set relative to the submission date.** The paper compares against methods spanning 2021–2023 (CLIP, ViFi-CLIP, AIM, ActionCLIP, CUPL) but does not situate itself against stronger zero-shot video methods from the 2024–2026 period. The core claim—that VP improves the base VLM—is not undermined, but the broader claim about effectiveness is uncalibrated. Without knowing how VP + a 2021 VLM compares against a 2025/2026 VLM alone, the reader cannot assess whether the framework provides practical value beyond what newer models already deliver.

### Minor

1. **Novelty framing overstates the contribution.** The paper frames its two modifications as novel, but both draw heavily on established ideas:
   - Using a generative model to describe a query and fusing that description with embeddings is a known strategy in visual-language fusion.
   - LLM-enriched class descriptors are established by Menon et al. (2022) and Pratt et al. (2022), which the paper cites.
   - The "Tree Hierarchy of Categories" (Section 3.2.3) is a straightforward prompt asking GPT-3.5 to group semantically similar classes. It is not a hierarchical structure—it produces a flat list of categories (Table in the paper). Calling it a "Tree Hierarchy" and claiming it as "a novel way" overstates what is essentially a simple grouping operation.
   
   The paper's actual contribution—demonstrating that an ensemble of off-the-shelf generative models can boost VLMs for video—is reasonable but should be characterized as an engineering/system contribution, not as algorithmic novelty.

2. **Missing analysis of video-to-text description quality.** The framework's visual enhancement depends entirely on the quality of Video-ChatGPT's descriptions. The paper mentions CLIP-based filtering to remove erroneous descriptions (Section 3.2.2) but does not quantify how often errors occur, what types of errors dominate (e.g., hallucination, incomplete coverage), or how much filtering improves versus harms performance. Without this, practitioners cannot assess the reliability of the approach.

3. **Time-sensitivity results gap not discussed.** The framework gains +10% on the synthetic temporal benchmark but only +1.4% on Charades (Table 4). The paper frames only the 10% gain ("substantial gain") without explaining why real-world gains are an order of magnitude smaller. This asymmetry warrants analysis.

4. **CUPL comparison lacks controlled ablation.** Table 5 compares VideoPrompter against CUPL, but the improvements are small (HMDB: 50.44→52.51; UCF: 73.54→73.88; SSv2: 4.81→4.87). Since CUPL uses GPT-3 while VP uses GPT-3.5, and CUPL without VGPT achieves 49.14 vs. VP with VGPT at 52.51, the source of the gain (GPT model version, VGPT addition, or prompt design) is confounded. A controlled comparison isolating each factor would strengthen the claim.

5. **Computational overhead not characterized.** The framework generates 10 video descriptions per query (filtered to 3) plus LLM-generated descriptors, introducing latency and API costs. The paper does not discuss this trade-off, which is important for practical deployment.

### Trivial

- The "performs on par with fully fine-tuned methods" claim in both Section 4 and the Conclusion should be softened to accurately reflect the results.
- The "Tree Hierarchy" is a flat grouping, not a hierarchy; the terminology is misleading.
- Notation: Equation (1) has minor LaTeX artifacts ("\cos" vs "cos") that should be cleaned up.

## Nice-to-Haves

- Evaluate with a more recent video-to-text model to demonstrate model-agnosticism beyond Video-ChatGPT (2023).
- Report retrieval results on additional datasets beyond MSR-VTT to strengthen generality claims.
- Quantify the per-dataset error rate of VGPT descriptions and the filtering retention rate.

## Removed Points

These points were flagged by reviewers but are removed per the review guidelines:

- **"Cannot be independently verified"** (reproducibility concern about cited models/tools): The paper states code will be released. Per hard rules, reproducibility concerns grounded in doubting cited entities are removed.
- **"Stray \bm command," "notation formatting," "figure cannot be seen"**: These are PDF-parser artifacts, not errors in the original submission. Removed per hard rules.
- **"No comparison to video-specific LLM-based enhancement techniques that may have appeared between 2023 and 2026"**: The paper cannot compare to unspecified methods it does not cite. Removed.
- **"No evaluation on Ego4D, FineGym, long-form video tasks"**: Scope creep. The paper evaluates on 7 datasets across 3 settings; demanding more benchmarks turns this into a different paper. Removed.
- **"Improvements from individual components are each modest"** (harsh critic claim): The paper shows CLIP alone at 37.5 vs. VP at 50.79 on HMDB—that is a 35% relative improvement, not modest. Factually inaccurate characterization. Removed.
- **"Gains would likely be smaller or negative against stronger baselines"**: Speculative without evidence. Removed.

## Novel Insights

None beyond the paper's own contributions. The strength finder and harsh critic converge on the same points: the framework works and is validated, but the novelty is more about engineering integration than algorithmic invention, and the evaluation would benefit from modern baselines.

## Suggestions

1. **Replace "fully fine-tuned" comparisons with honest framing.** Soften the claim to: "Our framework substantially narrows the gap to fine-tuned methods while requiring no training" and show this gap honestly (VP+CLIP 50.79 vs. ViFi-CLIP 51.82 on HMDB; 72.77 vs. 77.50 on UCF).

2. **Add a controlled ablation for the CUPL comparison.** Compare VP against CUPL using the same GPT model (GPT-3.5) and same VLM, with and without VGPT, to isolate whether gains come from the GPT version, the VGPT module, or the prompt design.

3. **Quantify VGPT description reliability.** Report per-dataset statistics: description quality scores, filtering rates, and at least one concrete failure case. This would make the paper more useful to practitioners.

4. **Address the time-sensitivity gap.** Discuss why the framework helps synthetic data far more than Charades—is it dataset difficulty, description quality, or task nature?

5. **Include at least one contemporary zero-shot video baseline.** Even comparing VP + CLIP against InternVideo or a recent video-language model at zero-shot would calibrate the reader on where the framework stands relative to modern methods.

6. **Renamed "Tree Hierarchy of Categories"** to something more accurate (e.g., "High-Level Action Context Grouping") to avoid overclaiming.

## Score and Decision

**Originality**: 4/10 — The individual components (VGPT descriptions, LLM descriptors) are established; the contribution is in the ensemble design and its application to video, which is incremental.

**Importance of research question**: 7/10 — Training-free enhancement of VLMs for video is practically valuable and well-motivated.

**Claims supported**: 5/10 — The core claim (VP boosts base VLM) is supported. The secondary claims ("on par with fine-tuned," "novel Tree Hierarchy," significant time-sensitivity gain) are overclaimed or lack sufficient evidence.

**Soundness of experiments**: 6/10 — Good breadth (7 datasets, 4 VLMs, 3 settings) and useful ablations, but weakened by outdated baselines and missing failure-case analysis.

**Clarity of writing**: 6/10 — Generally clear, but the "Tree Hierarchy" framing is misleading and some claims are overly bold relative to the data.

**Value to community**: 6/10 — Practitioners may find the framework useful as a plug-in, but the lack of contemporary calibration limits immediate impact.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>