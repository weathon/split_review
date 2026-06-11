Now I have enough data to calibrate. Let me finalize the review and score.

## Summary
This paper proposes IRIS, a reinforcement learning framework for autoregressive text-to-image generation that uses only an intrinsic reward signal — Negative Self-Certainty (NSC), defined as the negative forward KL divergence between a uniform distribution and the model's output distribution. The key observation is that self-certainty has modality-dependent effects: maximizing it helps language reasoning, while minimizing it improves image generation. Applied to Janus-Pro models using GRPO, IRIS achieves performance within 1-3 points of T2I-R1 (which uses four external reward models) on GenEval, T2I-CompBench, and WISE benchmarks, without any external supervision.

## Strengths
- **Novel counter-intuitive finding about modality-dependent self-certainty**: Figure 2 provides clear quantitative evidence that RL alignment increases self-certainty on text tokens (math reasoning, Qwen2.5) but decreases self-certainty on image tokens (T2I generation, Janus-Pro). This directly contradicts the established LLM literature (Zhao et al., 2025b; Zhang et al., 2025a) and is supported by qualitative evidence in Figure 1 showing self-certainty maximization produces uniform, simplified images while NSC produces visually richer ones.

- **Comprehensive ablation study isolating each design choice**: Section 4.3 presents five independent ablation experiments (Figures 5–9): (a) semantic CoT vs. no CoT, (b) minimize vs. maximize image self-certainty, (c) minimize vs. maximize text self-certainty, (d) forward vs. backward KL, and (e) RL-based vs. direct optimization. These systematically validate each component of the design.

- **Meaningful zero-supervision performance**: Table 1 shows IRIS achieves 0.72 vs 0.75 on GenEval-1B, 0.37 vs 0.38 on WISE-1B, and wins on several T2I-CompBench subcategories (color, texture, non-spatial on 1B). An intrinsic-only method capturing most of external-reward performance without any supervision is practically valuable, especially given the difficulty of defining objective quality metrics for image generation.

- **Identification of implementation bug in prior work**: Lines 120–121 document that T2I-R1 uses an incorrect chat template for Janus-Pro models (Janus-style keys instead of Janus-Pro-style keys), corrected in this paper. This is a genuine community contribution.

- **RL necessity demonstrated**: Figure 9 shows direct NSC optimization via gradient descent leads to model collapse, while GRPO maintains stable performance — a practically important finding that justifies the RL framework.

## Weaknesses

### Fatal
None

### Major
- **Abstract and introduction overclaim relative to empirical results**: The abstract states IRIS "achieves performance that is competitive with or superior to external rewards," and the 9.1%/13.3%/28.8% figures (line 44) are presented without clarifying they are improvements over the *base model*, not over T2I-R1. In reality, IRIS consistently underperforms T2I-R1 on overall scores across all three benchmarks at both model scales (GenEval 1B: 0.72 vs 0.75; WISE 1B: 0.37 vs 0.38; GenEval 7B: 0.77 vs 0.78; WISE 7B: 0.48 vs 0.50). The body text uses more measured language ("comparable"), but the abstract creates a misleading first impression. The genuine contribution — that intrinsic rewards capture most of external-reward performance without any supervision — is strong but overstated in the framing.

### Minor
- **No mechanistic explanation for why NSC improves image generation**: The paper empirically shows that lower self-certainty correlates with better images but does not analyze *why* a flatter output distribution over image tokens produces higher quality. Probing what happens to the output distribution during NSC training (e.g., does entropy increase uniformly or redistribute probability mass in structured ways?) would strengthen the core claim beyond the correlational evidence in Figures 1-2.

- **Ablation evaluation uses external reward models rather than standard benchmarks**: The ablation studies (Section 4.3, line 211) evaluate using HPSv2, DINO, GIT, and ORM — the same models used to train T2I-R1. While IRIS never uses these in training (no circularity), replicating key ablations on GenEval/T2I-CompBench/WISE would be more informative and directly comparable to the main results.

- **No human evaluation or failure mode analysis**: The paper makes claims about "human preferences" and "visually rich images" but never evaluates this directly. Even a small-scale human evaluation comparing IRIS, T2I-R1, and base model images, or analysis of when IRIS fails (degenerate outputs, worse-than-base images), would add credibility.

### Trivial
None

## Nice-to-Haves
- Exploring combination of intrinsic + external rewards, since the paper shows they excel on different subcategories (IRIS on natural science, T2I-R1 on aesthetic/spatial tasks).
- Experiments on additional T2I architectures beyond Janus-Pro to test generalizability (acknowledged as limitation in Section 4.4).
- More extensive qualitative analysis beyond the 3 prompts shown in Figure 1.

## Removed Points
These points are flagged to be removed, treat them with caution:
- **"Circular evaluation in ablation studies"** — The harsh critic claims ablation evaluation is circular because IRIS is evaluated on the same four reward models used to train T2I-R1. However, IRIS is never trained on these models (line 211: "we never use these reward models in the training objectives, so they can be simple and unbiased metrics to evaluate the performance"), so this is not circularity. Retained as minor (better evaluation metrics would strengthen but not invalidate).
- **"Cherry-picking subcategory results"** — The harsh critic claims the paper cherry-picks WISE subcategories. However, the paper presents all subcategories in Table 1(c) and explicitly discusses the pattern (lines 207). The different strengths on different tasks are a genuine finding discussed transparently.
- **Strength about "unbiased external reward model evaluation"** — The strength finder's claim about "unbiased assessment" in ablations is somewhat circular since these models are the training objective of the competing method. Not removed entirely but contextualized.

## Novel Insights
The paper's genuinely novel observation is that self-certainty has opposite effects depending on the modality of the output tokens: maximizing self-certainty improves text reasoning while minimizing it improves image generation. This contradicts the established LLM literature and is well-quantified in Figure 2. The practical implication — that intrinsic-only RL can achieve most of the performance of carefully designed external reward pipelines — is useful for the community, especially given the difficulty of defining objective quality metrics for image generation.

## Suggestions
- Revise the abstract to accurately state that IRIS approaches external-reward performance without any supervision, rather than implying it surpasses it. Frame the percentage gains explicitly as improvements over the base model.
- Add a brief analysis probing what happens to the output distribution during NSC training (e.g., entropy statistics across token positions, qualitative analysis of which tokens change most).
- Include ablation results on at least one standard benchmark (GenEval or WISE) to complement the external-reward-based evaluation in Section 4.3.
- Add a small-scale human evaluation (even 50-100 preference comparisons) to substantiate the claim about human preference alignment.

## Calibration Report

**Round 1 bracket**: [4.5, 7.0]

**Anchor papers retrieved** (all queries):

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| u1cQYxRI1H | 0.50 | R1 | Weak reject anchor; different topic (illumination harmonization) |
| Uj0h13lVrR | 1.00 | R1 | Strong reject; flawed GFlowNet paper |
| gwZ90hFSL2 | 1.00 | R1 | Strong reject; unrelated humanoid robot paper |
| 5lUdTogEL3 | 1.00 | R1 | Strong reject; unrelated person re-ID paper |
| TJHB4ySVZM | 3.40 | R1 | Reject; weak T2I paper with poor presentation |
| oOa3ZCtMjJ | 3.00 | R1 | Reject; weak GAN+CLIP T2I paper |
| ZVOGMy8Sd8 | 3.00 | R1 | Reject; weak fashion captioning paper |
| Fk4Op9wpEp | 3.00 | R1 | Reject; RL+ControlNet paper, limited novelty and weak results |
| zkMRmW3gcT | 4.80 | R1 | Reject; design space exploration for AR image generation, SOTA on ImageNet but incremental |
| zfIxlvKq4u | 4.00 | R1 | Reject; AR model design space, similar scope |
| b9dBNNeDd3 | 4.60 | R1 | Reject; Set AR modeling, interesting paradigm but strong reviewer concerns |
| bO31lfEdos | 5.00 | R1 | Reject; human-free RL for hallucination in LVLMs, closest methodological parallel |
| jQP5o1VAVc | 5.75 | R1 | Reject; Fluid scaling study, strong empirical results (SOTA) but limited novelty |
| sgAp2qG86e | 6.25 | R1 | Accept; JetFormer, strong multimodal generative model |
| wryFCrWB0A | 6.20 | R1 | Accept; DnD-Transformer, novel 2D AR image generation |
| q5sOv4xQe4 | 6.80 | R1 | Accept; HART, strong AR T2I model with SOTA results |
| tyEyYT267x | 8.00 | R1 | Accept; strong diffusion LM paper |
| SI2hI0frk6 | 7.60 | R1 | Accept; Transfusion, strong multimodal model |
| 5Ca9sSzuDp | 8.00 | R1 | Accept; CLIP interpretation paper |
| gU58d5QeGv | 8.00 | R1 | Accept; Würstchen, strong T2I architecture |

**Bracketing analysis**: IRIS is clearly above the 3.0-5.0 reject zone (which has papers with weak novelty, poor presentation, or limited results). IRIS has a genuinely novel insight, comprehensive ablations, and solid presentation. However, IRIS sits below the 6.25+ accept zone — the accepted papers (HART, JetFormer, DnD-Transformer) achieve SOTA results or introduce major architectural innovations. IRIS's contribution is more narrow: an insight about self-certainty that enables zero-supervision RL, but with results consistently trailing the external-reward baseline. The closest anchor is bO31lfEdos (human-free RL, score 5.0), which shares the zero-supervision RL motivation but has weaker results and less novelty than IRIS.

**Final score determination**: IRIS is stronger than the 5.0 anchors (more novel insight, better ablations, stronger experimental design) but weaker than the 6.25+ accepted papers (no SOTA results, framing issues). A score of 6.0 reflects a paper with a genuinely interesting contribution and solid methodology that falls slightly short of acceptance due to persistent overclaiming in the abstract and the consistent ~2-3 point performance gap with T2I-R1.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Reject</decision>