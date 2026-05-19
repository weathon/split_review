- Decision: Reject
- Avg Score: 5.00
- Scores: 6, 5, 6, 3
Now I have all the information needed to produce the consolidated review. Let me write it.

## Summary

This paper proposes Self-TPT, a framework that replaces per-image test-time prompt tuning with class-level self-supervised adaptation. The key idea is to use Contrastive Prompt Tuning (CPT)—which creates positive pairs by varying class token positions in the prompt sequence—to adapt prompts using only target class names as a preprocessing step, avoiding per-image computation during inference. A gradient matching (GM) loss further aligns CPT gradients with classification gradients. The method achieves a 25× speedup and 30× memory reduction over the prior TPT method PromptAlign while maintaining or slightly improving accuracy across cross-dataset, base-to-new, and domain generalization benchmarks.

---

## Strengths

1. **Massive efficiency gains are convincingly demonstrated.** Table 1 shows Self-TPT achieves 146.7 FPS and 0.32GB memory on CLIP-B/16 versus PromptAlign's 5.3 FPS and 11.2GB (25× faster, 30× less memory). Even with augmented views (Self-TPT-v), it maintains a 5× speed advantage. These numbers are directly validated in the paper's data and are the work's strongest contribution.

2. **State-of-the-art accuracy across three diverse benchmarks, without sacrificing efficiency.** Self-TPT (or its -v variant) achieves the highest average accuracy on cross-dataset generalization (67.85% vs PromptAlign's 66.92%), base-to-new generalization (77.47% vs PromptSRC+TPT's 76.26%), and domain generalization (65.38% vs PromptAlign's 63.56%)—shown in Tables 2, 3, and 4 respectively. The improvements are consistent across datasets, not driven by a single outlier.

3. **Comprehensive ablation study isolating each component's contribution.** Table 5a shows the incremental gains from adding CPT (+1.3 avg over CoOp), applying it at test time (+1.3), and adding GM loss (+0.7). Table 5b confirms all four prompt views contribute, and Table 5c validates the design choices for the GM loss (EMA + cosine similarity). Each design decision is empirically justified.

4. **Model versatility is demonstrated across architectures and VLMs.** Tables 8 and 9 show consistent improvements over baselines on five backbones (RN50, RN101, ViT-B/32, ViT-B/16, ViT-L/14) and on a different VLM (EVA-CLIP: 79.81% vs 78.68% for PromptSRC), confirming the method is not brittle or architecture-specific.

5. **Data efficiency analysis provides practical insights.** Table 7 shows Self-TPT retains higher accuracy than CoOp, MaPLe, and PromptSRC when source data is reduced to 25% (74.40% vs 73.20%). Figure 3's analysis of class diversity vs. instance count provides actionable guidance for practitioners.

---

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Precision of the efficiency claims could better distinguish the two variants.** The abstract and introduction highlight "25-fold increase in inference speed and reducing memory usage by 30-fold" and describe Self-TPT as achieving "state-of-the-art performance." However, the 25×/30× figures come from Self-TPT (non-v), while the SOTA accuracy results in Tables 2–4 sometimes come from Self-TPT-v (which uses 63 augmented views at test time). The paper does clearly introduce Self-TPT-v in the implementation details (Section 4.1) and separates both variants in all tables, so this is not misleading—but a reader scanning only the abstract and Figure 1c may not realize the high-efficiency and SOTA-accuracy numbers correspond to partially overlapping configurations. A brief clarifying sentence in the abstract or conclusion would resolve this.

2. **No standard deviations are reported for any result.** The paper states results are averaged over three seeds, but no variance or confidence intervals are provided. Several comparisons are close (e.g., Self-TPT 67.72 vs. Self-TPT-v 67.85 in Table 2; CoOp 63.88 baseline). Without error bars, it is impossible to assess the statistical significance of these differences. While single-seed runs are common in the prompt learning literature, reporting variance over seeds is standard practice and would substantially strengthen the evaluation.

3. **The gradient correlation analysis is suggestive but stops short of direct causal evidence.** Figure 2 shows that CPT and classification gradients have positive cosine similarity across 10/11 datasets, and the GM loss increases this similarity in 8/11. The paper appropriately uses measured language ("suggests," "plausible explanation"). However, the GM loss itself yields only marginal gains (Table 5a: +0.1 on Generic, +0.1 on Fine-Grained, +1.5 on Specialized), and the core claim that CPT "mimics" classification gradients is supported only by correlational evidence. A stronger test—e.g., ablating CPT with a different SSL task known to have lower gradient similarity—would make the argument more convincing.

### Trivial
None.

---

## Nice-to-Haves

- **Discussion of limitations.** The paper would benefit from a brief limitations section addressing when class-name-only adaptation may be insufficient (e.g., EuroSAT, where Self-TPT underperforms LLM-based methods like WaffleCLIP, suggesting visual context can sometimes matter).
- **Code release statement.** Explicitly stating whether the code will be released would help reproducibility, though this is not a requirement for evaluation.
- **The gradient analysis could be strengthened** by reporting the actual cosine similarity values and their variance across datasets, and by including a scatter plot of gradient similarity vs. performance gain per dataset.

---

## Removed Points

These points were flagged by reviewers but are removed from the main review for the reasons stated:

1. **EMA weight normalization concern** (Harsh Critic: "the formula appears to be missing the normalization of the EMA weights"). The GM loss uses cosine similarity, which is scale-invariant—the unnormalized EMA weights have no effect on the loss value. This is a misunderstanding, not a paper flaw.
2. **"Overclaiming" about "balancing the efficiency-efficacy trade-off"** (Harsh Critic: "Self-TPT improves both... not a trade-off"). The paper's own variant (Self-TPT-v) shows the trade-off exists (more computation yields higher accuracy), so the framing is not incorrect. Semantic nitpick.
3. **Fairness nuance about class names** (Harsh Critic: "no significant issue here"). The reviewer explicitly says this is not a problem. Removed.
4. **PromptAlign memory numbers being "surprisingly high"** (Harsh Critic, Section-by-Section). This is an observation about a baseline, not a weakness of the paper.
5. **Hand-crafted prompt as "regularizer" wording** (Harsh Critic, Section-by-Section). The paper's wording ("regulate the contrastive learning process") is a reasonable description of adding an extra positive view to guide learning. Minor phrasing choice, not a substantive issue.
6. **Strength Finder's claim about "effectively balancing the efficiency-efficacy trade-off"** being a strength. This phrasing appears in the paper's own abstract; keeping it as a strength would double-count and the paper's own evidence supports it.

---

## Novel Insights

The reviews converge on a useful reframing: Self-TPT's primary contribution is not another incremental accuracy improvement (the SOTA deltas are 0.9–1.8%), but rather demonstrating that test-time prompt tuning can be reformulated as a *one-time, text-only preprocessing step* that eliminates per-image compute entirely. The 25×/30× efficiency gains over PromptAlign represent a qualitative shift in the deployment feasibility of TTA for VLMs, not just a quantitative advance. The paper shows that the class-level SSL proxy works surprisingly well, even better in some settings than per-image methods that see each test sample. This suggests that much of the value of test-time prompt adaptation comes from calibrating prompts to the *class vocabulary* of the target domain rather than to individual image statistics—an insight that could influence future TTA design.

---

## Suggestions

- Add a clarifying sentence to the abstract/Introduction such as: *"Self-TPT (without test-time augmentation) achieves 25× speedup and 30× memory savings; Self-TPT-v, which uses 63 augmented views for fair comparison with prior methods, achieves a 5× speedup while setting new SOTA accuracy."*
- Report standard deviations or confidence intervals for all main results, especially given the three-seed averaging.
- Add a brief limitations paragraph acknowledging that class-level adaptation cannot address image-level distribution shifts (e.g., adversarial degradation) and that some datasets (e.g., satellite imagery) may benefit from visual context.

---
