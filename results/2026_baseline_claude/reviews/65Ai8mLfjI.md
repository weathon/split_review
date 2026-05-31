## Summary

This paper revisits the role of pooled CLIP text embeddings (global text conditioning) in diffusion transformers. The authors first demonstrate empirically that the pooled CLIP embedding has limited or no influence on generation quality in modern models like FLUX schnell (for long prompts) and HiDream-Fast. They then argue this component should not be discarded but rather repurposed: they propose **modulation guidance**, a training-free technique that applies CFG-style extrapolation in the modulation vector space to steer generation toward desirable properties (aesthetics, complexity, correct hands, accurate counts). The method is extended to CLIP-free models via lightweight fine-tuning, and validated on text-to-image, text-to-video, and instruction-guided image editing tasks.

---

## Strengths

- **Focused, practically motivated research question.** The growing trend of dropping pooled CLIP embeddings in modern DiTs lacks empirical justification; this paper fills that gap with systematic ablations across FLUX schnell and HiDream-Fast, using both short and long prompt subsets and quantitative quality metrics (Table 1, Figure 1). This analysis is original and informative.

- **Simple, broadly applicable technique.** Modulation guidance (Eq. 3) is a minimal modification—adding a guidance vector in the shared conditioning space y—with negligible runtime overhead. It requires no training for existing models with CLIP, extends gracefully to CLIP-free models via 1K–4K iterations of distillation fine-tuning, and applies to multi-step and few-step diffusion models alike.

- **Consistent empirical gains across diverse settings.** The improvements are reported on 5 image models (FLUX schnell, FLUX dev, SD3.5 Large, HiDream, COSMOS) and 2 video models (Hunyuan 13B, CausVid 1.3B), with both human side-by-side evaluations and automatic metrics (PickScore, CLIP Score, ImageReward, HPSv3, VBench). Gains are consistent in direction and statistically significant for aesthetics/complexity. Object counting (+9 on GenEval), hands correction (+18% human SbS), and video dynamic degree (+11 for CausVid) are particularly compelling.

- **Mechanistic interpretability.** Figure 4 provides an attention-map analysis showing that modulation guidance redirects model attention toward task-relevant tokens (e.g., *hands*, *child*). This is a useful mechanistic insight beyond the empirical gains.

- **Practical outperformance of existing baselines.** The paper benchmarks against Normalized Attention Guidance, Concept Sliders, and LLM-enhanced prompts, outperforming on all evaluated tasks while adding no extra runtime overhead.

---

## Weaknesses

### Fatal
None.

### Major

1. **Incomplete explanation of why CLIP becomes inactive for long prompts.** The most likely mechanism is well-known: CLIP has a hard 77-token context limit, so for "long" prompts (≥77 tokens), the CLIP embedding is saturated and provides redundant information relative to the uncapped T5 encoder. The paper never states this, instead describing the inactivity as surprising and unexplained. This omission weakens the interpretive contribution of Section 4. Understanding *why* CLIP is inactive is important for knowing whether this applies in other contexts.

2. **Guidance formulation is straightforward but the novelty claim needs more precision.** Equation (3) is a direct analog of CFG but applied to the conditioning vector y rather than to the predicted noise/score. Related attention-guidance methods (Chen et al., 2025; Hong et al., 2023) already apply CFG-style extrapolation in feature space. The specific choice of the modulation vector as the guidance target is the novel element, but the paper could more clearly articulate what properties of the modulation space make this specifically advantageous over applying guidance at other points (e.g., in the residual stream or via attention).

3. **Manual prompt selection is the core bottleneck with insufficient guidance for practitioners.** Positive and negative prompts are hand-crafted per-task (Appendix D, Table 5), and the paper does not quantify sensitivity to these choices. Without systematic ablations on prompt selection strategies, replicating results for a new task is unclear.

### Minor

1. **Dynamic guidance strategy is a simple step function (Figure 3b) with limited ablation.** The motivation for skipping early layers specifically is primarily empirical. While Appendix B mentions more complex strategies, the paper does not present a principled understanding of *why* early layers should be excluded from guidance.

2. **Human evaluation sample sizes are modest.** 128 prompts for general changes and 70 for counting (Table 3) may not always reach statistical significance across all metrics; some wins in "Defects" and "Relevance" hover near 50% and may reflect noise.

3. **Video evaluation lacks human assessment.** For video tasks, only VBench automatic metrics are reported. Human evaluation of video dynamic quality and text alignment would strengthen the claim.

### Trivial
None worth noting.

---

## Nice-to-Haves

- An explicit discussion of CLIP's 77-token saturation and its connection to the prompt-length dependency in Figure 1 would significantly strengthen Section 4.
- A sensitivity analysis over positive/negative prompt choices for one representative task would help practitioners understand the robustness of the method.
- A short ablation comparing guidance at different points in the network (modulation vs. attention vs. residual) would sharpen the justification for modulation space specifically.

---

## Novel Insights

The paper's central novel insight is that the pooled CLIP embedding in diffusion transformers, while largely redundant as a conditioning signal, can serve as an interpretable guidance direction in the modulation space. This reframing—from conditioning to guidance—is conceptually clean and empirically well-supported. The attention-map analysis (Figure 4) provides a useful mechanistic lens: modulation guidance does not directly synthesize new content but redistributes the model's attention toward task-relevant tokens. The finding that this transfer works for CLIP-free models (via lightweight distillation into the MLP) and generalizes across image and video domains is a meaningful practical contribution to the growing toolkit of inference-time steering methods.

---

## Suggestions

- Add a brief paragraph explaining CLIP's 77-token limit as the most parsimonious explanation for the prompt-length dependency in Figure 1.
- Include a table or figure showing sensitivity to different positive/negative prompt choices for at least one task (e.g., hands correction), to guide practitioners.
- Provide a layer-ablation study showing performance as a function of the step-function cutoff index *i* in Figure 3b to motivate the dynamic strategy more rigorously.

---

## Score and Decision

The paper addresses a well-motivated research question, offers a clean analysis of an underexplored design choice, proposes a simple and broadly applicable technique, and validates it comprehensively across multiple models and tasks. The technique is somewhat incremental (CFG in modulation space), and the lack of explanation for why CLIP becomes inactive is a notable gap. Nevertheless, the work is technically sound, practically useful, and delivers consistent improvements with negligible overhead—making it a genuine contribution to the community.

MY FINAL SCORE: <score>6</score>
MY FINAL DECISION: <decision>Accept</decision>