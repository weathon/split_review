Now I have all the information needed. Let me write the final review.

---

## Summary

This paper proposes Patch-Wise and Keyword-Aware Attention (PKA) for efficient multi-condition control in Diffusion Transformers. The method decomposes full multi-modal attention into Position-Aligned Attention (PAA) for spatial conditions (one-to-one token correspondence) and Keyword-Scoped Attention (KSA) for subject-driven conditions (sparse attention via a keyword-derived relevance mask), complemented by a Condition Cache and an early-timestep sampling strategy. The paper reports up to 10× attention-module speedup and 5.12× VRAM reduction with maintained or improved generation quality compared to OminiControl2 and UniCombine.

## Strengths

- **Empirically grounded decomposition via attention analysis**: Figures 2 and 3 provide concrete visual evidence that multi-condition attention is highly redundant—spatial conditions show near-diagonal attention matrices and subject conditions show sparse, keyword-correlated activations—directly motivating the distinct PAA and KSA designs. This is not merely asserted but demonstrated with specific heatmap visualizations.

- **Substantial and scalable efficiency gains**: Figures 7–8 demonstrate 3.90×–10× attention-module speedup and 2.46×–5.12× VRAM reduction compared to UniCombine's full attention, with the proposed method's cost remaining nearly flat (under 25s, under 500MB even at 16 conditions) while baselines grow steeply. The scaling behavior demonstrates genuinely sub-quadratic complexity rather than a fixed improvement.

- **Quality maintained or improved across all tasks**: Table 1 shows the method achieves the best FID (52.99, 62.08, 53.01), SSIM, CLIP-I, and DINOv2 scores across three multi-condition tasks (Subject-Canny, Subject-Depth, Canny-Depth), with CLIP-T trailing by at most 0.003. The depth MSE improvement is particularly striking (160 vs. 312 on Subject-Depth, 114 vs. 250 on Canny-Depth).

- **Well-designed perturbation experiment motivating early-timestep sampling**: Figure 5 presents a clean asymmetric perturbation experiment showing that early/high-t perturbations degrade SSIM immediately (0.50→0.48 at step 1, 0.42 at step 3), while late-timestep perturbations remain stable at 0.50 through step 4, providing clear empirical evidence for the shifted sampling strategy.

- **Comprehensive component-level ablations**: Figures 9, 10, and 11 provide multi-dimensional ablations—PAA vs. SWA vs. full attention (efficiency and quality), KSA threshold ε sweep (graceful degradation from 16.99s/368MB to 15.23s/230MB), and early-timestep sampling across different (μ, δ) configurations.

## Weaknesses

### Fatal

None

### Major

- **Missing ablation separating attention mechanism from training strategy**: Table 1 presents "Ours" combining all three contributions (PAA, KSA, early-timestep sampling). The component ablations (Sections 4.3.1–4.3.3) test each in isolation but critically, there is no result for "PKA + standard Logit-N(0,1) sampling" vs. "standard attention + early-timestep sampling." Without this 2×2 decomposition, the reader cannot determine whether quality improvements in Table 1 are driven by the attention mechanism, the training strategy, or their combination. If early-timestep sampling alone accounts for most quality gains, the paper's main contribution reduces to the efficiency story. This is the most important gap because the headline claim is "maintaining or even improving generative quality."

- **Baseline training protocol is ambiguous**: The paper states it fine-tunes FLUX.1 with LoRA for 20K iterations (Section 4.1) and uses "OminiControl2 and UniCombine as baselines," but never clarifies whether baseline numbers in Table 1 are re-produced under identical training conditions (same curated Subject200K subset filtered for descriptive keywords, same iterations, same optimizer) or taken from original papers. This matters because the authors curate a filtered subset of Subject200K—a non-trivial preprocessing step that could advantage their method. If baselines use original-paper numbers trained on different data/protocols, Table 1 is not a controlled comparison.

- **KSA keyword extraction mechanism is unspecified**: KSA depends on identifying "a small set of keyword tokens K" from the text prompt (Eq. 3, Section 3.2.2). The paper states these "typically contain just 1 to 2 tokens" but never describes how they are identified at inference time. Section 4.1 mentions filtering training data so "each image caption contains a descriptive keyword," but this is a data-level annotation, not an inference-time extraction procedure. Without specifying whether keywords are user-specified, extracted via NLP parsing, or identified via cross-attention scores, the method is not reproducible and the reader cannot assess KSA's robustness across different prompt types.

### Minor

- **Abstract overstates speedup scope**: The abstract claims "up to a 10× inference speedup," but the measurement (Section 4.2.1, Figure 7) is specifically for the attention module compared to UniCombine's full-attention mechanism. The body text appropriately scopes this ("compared to the full-attention mechanism in UniCombine"), but the abstract's "inference speedup" overstates what is demonstrated—the rest of the pipeline (condition encoding, VAE decoding, etc.) is not accounted for.

- **No error bars or variance reporting**: Table 1 reports single-point metrics (FID, SSIM, CLIP-I, DINOv2, CLIP-T, F1, MSE) across all tasks with no confidence intervals, standard deviations, or multi-run variance. FID in particular is sensitive to the number of generated samples and random seeds.

- **PAA margin over SWA is modest at the component level**: In Figure 9, PAA achieves 13.63s/237MB vs. the most efficient SWA (window=1) at 14.00s/276MB—roughly a 3% latency and 14% VRAM improvement. The bulk of the efficiency gains come from KSA and the Condition Cache. The paper could be more forthright about this limited component-level margin.

### Trivial

None

## Nice-to-Haves

- A combined ablation table (PKA + standard sampling, standard attention + early-timestep sampling, PKA + early-timestep sampling) would be the single most impactful addition.
- Reporting end-to-end wall-clock inference time (not just attention module) for at least one representative setting would strengthen the efficiency claims for practitioners.
- A failure case analysis for KSA (e.g., abstract prompts where the keyword doesn't localize well) would improve confidence in the method's robustness.
- Clarifying whether Figures 7–8 compare against OminiControl2 with or without its own efficiency techniques (dynamic token pruning, input downsampling, mentioned in Section 2.2) would make the comparison more transparent.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"KSA mask schedule contradictory with Condition Cache"**: The harsh critic questioned whether KSA's per-timestep mask computation contradicts the Condition Cache's first-step-only K/V computation. Upon verification: The Condition Cache stores subject condition K/V (computed once), while KSA's mask (Eq. 3) uses image queries Q_X^t against text keyword keys K_i (from the text prompt). These are different computations operating on different token types. The mask is computed per timestep t and reused at t+1, which is consistent with the paper's description. This criticism misunderstands the paper's architecture.

- **"PAA is just windowed attention with window size 1"**: While technically true at the implementation level, PAA's novelty lies in the deliberate design choice motivated by the empirical attention analysis (Figure 2), not in inventing local attention as a concept. The paper doesn't claim PAA is architecturally novel in isolation—it's one component of a system justified by observed redundancy patterns.

- **Strength about "Condition Cache eliminates redundant computation"**: This is a straightforward consequence of the design (conditions are static across denoising steps) rather than an independent insight. Not listed as a separate strength.

- **Strength about "KSA temporal consistency is elegant"**: The mechanism is functional and described clearly, but calling it "elegant" is subjective and not independently verifiable as a strength beyond what the paper demonstrates.

## Novel Insights

The paper's most novel observation is the empirical demonstration that multi-condition attention redundancy in DiTs is condition-type-specific: spatial conditions exhibit near-diagonal (local) attention patterns while subject conditions exhibit sparse keyword-correlated patterns. This observation directly motivates two different sparse attention strategies rather than a single uniform sparsification approach—a distinction that has practical implications for how multi-condition systems should be designed in DiTs. The early-timestep perturbation analysis (Figure 5) also provides useful evidence that visual conditioning information is predominantly injected during early denoising stages, suggesting that flow-matching fine-tuning strategies should not treat all timesteps equally.

## Suggestions

- Add a 2×2 ablation table: (a) PKA + standard Logit-N(0,1) sampling, (b) standard full attention + early-timestep sampling, (c) full PKA (current "Ours"). This directly addresses what drives the quality results and would take minimal additional compute since the component models already exist.
- Specify the keyword extraction mechanism for KSA—even a simple heuristic (e.g., "we extract the subject noun phrase using spaCy" or "we use the text token with highest cross-attention score to the subject image region") would make the method reproducible and allow readers to reason about failure modes.
- Clarify the baseline protocol: explicitly state whether baseline numbers in Table 1 are re-produced under identical conditions or taken from original papers, and acknowledge any data/protocol differences as a limitation.
- Report end-to-end efficiency (total wall-clock inference time) for at least one representative setting to complement the attention-module-specific measurements.

## Calibration Reporting

**All retrieved anchors across rounds:**

| Anchor | Path | Avg Score | Round | Comparison |
|--------|------|-----------|-------|------------|
| IC-Light | u1cQYxRI1H | 0.50 | 1 | Unrelated topic (illumination harmonization); mislabeled in low-score band |
| KL Divergence GFlowNets | Uj0h13lVrR | 1.00 | 1 | Completely different domain and much weaker paper |
| Balancing Differential L-ReID | 5lUdTogEL3 | 1.00 | 1 | Different domain, rejected for poor methodology |
| NEMESIS Jailbreaking | 5kMwiMnUip | 1.00 | 1 | Unrelated (LLM jailbreaking) |
| Superposition of Diffusion Models | 2o58Mbqkd2 | 3.25 | 1 | Combining diffusion models, different focus, high variance scores |
| Closed-loop Diffusion Control | PiHGrTTnvb | 3.00 | 1 | Different domain (physical systems control) |
| Conditional LoRA Parameter Gen | AjunxrcKa2 | 3.40 | 1 | Different approach to parameter generation, rejected |
| Highlight Diffusion | Jt1gGIumJo | 3.00 | 1 | Related (diffusion acceleration) but much weaker—only 1.52× speedup, limited to SD1.4, poor writing. Our paper is substantially stronger. |
| Towards Enhanced Controllability | kALZASidYe | 3.75 | 1 | Related (controllable diffusion) but limited novelty, poor formatting, rejected. Our paper clearly stronger. |
| APCtrl | yPxhj1FKhG | 3.67 | 1 | Conditional projection for diffusion, different approach, rejected. |
| Inductive Biases in DiTs | lWGXftRS5h | 5.00 | 1 | Study of DiT attention patterns, different contribution type. |
| Simple Diffusion Transformer | w6YS9A78fq | 5.00 | 1 | Unified generation framework, different focus. |
| UniCon | uJqKf24HGN | 7.00 | 1 | **Most relevant anchor.** Efficient control of DiTs via unidirectional flow. Cleaner novelty story but lower efficiency gains (2.3×). Our paper has stronger efficiency numbers but weaker methodology documentation. |
| LinFusion | D2as3jDmRA | 6.25 | 1 | Linear attention for diffusion, different mechanism. |
| LEGO Bricks | qmXedvwrT1 | 6.67 | 1 | Efficient diffusion backbone, similar efficiency focus, clean experiments, some concerns about contribution significance. |
| CTRL (RL for control) | svp1EBA6hA | 6.50 | 1 | Novel RL formulation for conditional control, limited experiments but strong theoretical contribution. Our paper has stronger experiments but weaker methodology. |
| Würstchen | gU58d5QeGv | 8.00 | 1 | Highly efficient T2I architecture, more impactful contribution. |
| Differential Transformer | OvoCm1gGhN | 8.00 | 1 | Foundational attention mechanism work, more impactful. |
| CADS | zMoNrajk2X | 8.00 | 1 | Diffusion sampling diversity, different focus. |
| Dynamic Diffusion Transformer | taHwqSrbrb | 5.50 | 2 | Very relevant—dynamic computation in DiTs. Accepted despite somewhat incremental contributions (router-based masking). Our paper has stronger efficiency gains and addresses multi-condition specifically. |
| SaRA | wGVOxplEbf | 6.20 | 2 | Efficient diffusion fine-tuning, different focus. |
| Qihoo-T2X / PT-DiT | lTrrnNdkOX | 6.40 | 2 | Proxy-tokenized DiT for efficiency. Related mechanism (sparse attention) but different application. |
| ViCo | r2uhY4pXrb | 5.50 | 2 | Visual condition for personalized generation, rejected. |
| CtrLoRA | 3Gga05Jdmj | 6.00 | 2 | Efficient controllable generation framework. Similar quality of evaluation, all 6s from reviewers. |
| Minimal Impact ControlNet | rzbSNDXgGD | 6.00 | 2 | Multi-ControlNet integration. Systematic approach, comprehensive experiments, all 6s. |
| VD3D | 0n4bS0R5MM | 6.20 | 2 | Video DiT camera control, different domain. |
| ControlAR | BWuBDdXVnH | 6.25 | 2 | Controllable AR generation, different architecture. |

**Round 1 bracket: 5.5–7.0.** The paper is clearly above rejected papers in the 3–4 range and comparable to accepted papers in the 6–7 range.

**Round 2 narrowing: 6.0–6.5.** Above DyDiT (5.50, which had more incremental contributions), comparable to CtrLoRA (6.00) and Minimal Impact ControlNet (6.00) but with stronger efficiency numbers, and slightly below UniCon (7.00) which has a cleaner novelty story and better documentation.

**Final score: 6.5.** The paper's efficiency contribution is genuinely strong (10× speedup, 5× VRAM reduction scaling well with conditions), the empirical motivation is compelling, and quality results are consistently best-in-class. The three major methodological gaps (missing combined ablation, baseline ambiguity, unspecified keyword extraction) are real but fixable and do not invalidate the core efficiency claims.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: Accept