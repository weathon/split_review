## Summary

Dynamic Nested Depth (DND) is a post-training method that selectively reprocesses a subset of "critical" tokens through weight-shared transformer layers, adding negligible parameters (<0.1M) and compute (~6% extra FLOPs). Token selection is governed by a learned threshold-based router, with two novel training strategies: a push-pull router controlling loss (score dispersion + distribution preservation) and an adaptive threshold control scheme (buffer proportional control + EMA synchronization). The method is validated on three 1B-scale dense models (Qwen3-1.7B, Llama3.2-1B, Gemma3-1B) and one 30B MoE model (Qwen3-30B-A3B), yielding average improvements of +1.88, +2.61, +2.50, and +0.87 points, respectively, across 11–17 benchmarks.

---

## Strengths

- **Consistent, substantial gains on 1B models:** Tables 1 demonstrates average improvements of +1.88, +2.61, and +2.50 across three architecturally distinct 1B models covering 11 benchmarks spanning diverse domains (reasoning, math, coding, alignment). The breadth rules out cherry-picking and the magnitude (especially +3.70–5.02 BBH, +3.86–5.30 GPQA) is large enough that noise cannot plausibly explain it.

- **Ablation evidence validates each training component:** Table 4 shows that replacing the full training strategy with a z-loss-like baseline degrades average gain from +1.88 to +1.01 (–0.87), and removing either the router controlling loss (RC) or the threshold control (TC) further reduces gains, directly confirming the necessity of the proposed joint strategy (Section 4.4).

- **Mechanistic token selection analysis:** Figure 4b shows r=−0.58 between selection frequency and post-DND entropy reduction, meaning frequently selected tokens reliably have their uncertainty reduced by the nested pass—the most credible mechanistic validation in the paper. Figure 4a (r=0.34) provides corroborating (though weaker) evidence that high-entropy tokens are preferentially selected.

- **Threshold control effectiveness demonstrated empirically:** Figures 5, 6a, and 6b show that the combination of buffer proportional control and EMA synchronization suppresses training-time ratio oscillations to within a tight 5% band, confirming the practicality of the threshold scheme.

- **Practical inference overhead:** Table 3 reports 91.6–93.1% throughput retention on Qwen3-30B-A3B across four length configurations, substantiating the minimal-overhead claim.

---

## Weaknesses

### Fatal
None.

### Major

- **Missing 100% token ablation undermines the selective-computation thesis.** Table 4 ablates selection ratios of 10%, 20%, and 30%, but never tests 100%—reprocessing all tokens uniformly through the same weight-shared layer. This is the single most important missing control: the paper claims that *selective* routing is the source of the gains, but without comparing against uniform reprocessing through an identical extra shared-weight pass, it cannot distinguish "dynamic selection adds useful inductive bias" from "any additional compute at this position helps." If a 100% variant matches or beats selective DND, the routing mechanism's value would need to be reframed (e.g., efficiency, not accuracy). If selective DND beats 100%, the central claim is strongly validated. The experiment is inexpensive to run and would substantially change the strength of the paper's core argument.

- **Attention scope of the nested pass is under-specified, affecting both reproducibility and the FLOPs claim.** Equation 3 describes Pack/Unpack operators but never states what the packed subsequence attends to during the nested transformer pass: (a) only the other selected tokens in the compact sequence, (b) the full original sequence via fetched KV states, or (c) some other masking scheme. Choice (a) severs cross-token context and is the configuration consistent with the "~6% extra FLOPs" figure; choice (b) would require fetching the full sequence's KV cache and is computationally more expensive. The architecture section does not resolve this. This is not a trivial omission—it determines the validity of the FLOPs claim and affects reproducibility.

### Minor

- **30B model results lack statistical grounding for small-margin gains.** Several Table 2 improvements are very small: +0.13 BBH, +0.15 MATH, +0.20 MATH-500, +0.27 DROP. These are single-run point estimates without confidence intervals or multi-seed variance. The larger gains (+1.83 C-Eval, +2.05 BFCL, +1.42 LCB-v6) are more credible in isolation, but the aggregated +0.87 average is dragged upward by these larger entries. A multi-seed run even on a representative 4–5 benchmarks would establish which 30B gains are reliable.

- **Notation inconsistency in the router loss equations.** Equation 6 introduces summation indices $L_a$ to $L_c$, and Equation 7 uses $L_e$ to $L_r$—four symbols not defined with respect to the architecture's established $L_s$ and $L_e$ notation. The use of $L_e$ in Eq. 7 directly conflicts with $L_e$ (the DND end layer) defined in Section 3.1. The paper does not clarify whether these loss functions apply to the full DND layer range or a subset thereof.

- **Ablation study is confined to Qwen3-1.7B.** Table 4's training strategy and hyperparameter ablations are conducted only on Qwen3-1.7B. It is not stated whether the same hyperparameter settings (layer range 4:23, k=20%) transfer directly to Llama3.2-1B and Gemma3-1B, or whether additional tuning was performed. Given that the Llama and Gemma results (+2.61 and +2.50) are actually larger than Qwen3-1.7B (+1.88), confirming configuration transferability would strengthen the paper's generalization claim.

- **r=0.34 characterized as strong validation.** Section 4.5 states that Figure 4a demonstrates DND "preferentially selects tokens with greater uncertainty," but r=0.34 represents a modest positive correlation, not a strong one. The Figure 4b result (r=−0.58) is much more compelling and should be the lead mechanistic evidence.

### Trivial

- **Push-pull training dynamic lacks visualization of score histograms at convergence.** The paper argues that $\mathcal{L}_\text{sd}$ and $\mathcal{L}_\text{dp}$ together produce discriminative, stable routing distributions, but no histogram of routing scores at training completion is shown. The equilibrium is intuitively motivated but empirically unverified in the paper.

---

## Nice-to-Haves

- **ITT comparison across all three dense models.** Currently, the ITT baseline appears only for Qwen3-1.7B (+0.05 avg vs. DND's +1.88). Including ITT results for Llama3.2-1B and Gemma3-1B would better quantify the architectural advantage of DND over ITT's training-inference mismatch, rather than leaving the attribution ambiguous (architecture vs. implementation quality).

- **Routing score histogram at convergence.** A visualization of the empirical distribution of $p^i$ values after training would concretize the push-pull equilibrium described in Section 3.2.1 and directly confirm that scores are neither collapsed near 0/1 nor uniformly concentrated at 0.5.

- **Confirmation of identical training data for SFT and DND+SFT.** The paper describes training data as "a significant volume of synthetic material built upon a high-quality seed set of 1-2 million instances" (Section 4.2). An explicit statement confirming that baseline SFT and DND+SFT use the exact same dataset, optimizer, and schedule would eliminate any confounding factor in the comparative results.

---

## Removed Points

*These points are flagged for removal; treat them with caution.*

- **Harsh Critic: Introduction oversells connection to latent test-time scaling.** Removed as scope-creep. The introduction uses latent strategies as motivation rather than claiming algorithmic equivalence. The actual DND mechanism is clearly differentiated in Sections 3.1 and 3.2.

- **Harsh Critic: "Selectively reprocessing subset vs. uniform reprocessing through the same layers."** Partially retained as the Major weakness above, but the framing that this makes the paper "below the bar for acceptance" is too strong given the consistent empirical evidence across four models.

- **Strength Finder: Problem importance / DND "addresses an important problem."** Removed as generic (scale-invariant strength).

- **Harsh Critic: Training data composition not fully disclosed.** Demoted to Nice-to-Have. Lack of data characterization is common in industry-adjacent LLM papers and does not threaten the internal validity of the SFT vs. DND+SFT comparison, which is the relevant contrast.

---

## Novel Insights

The paper's most genuinely novel technical contribution is the formalization of the push-pull router training dynamic (Section 3.2.1): rather than using a single entropy-based or load-balancing loss, the joint $\mathcal{L}_\text{sd}$–$\mathcal{L}_\text{dp}$ framework simultaneously prevents score clustering and avoids gradient saturation at the sigmoid boundary. This is a non-obvious design point for token-choice routing in autoregressive models. The threshold control mechanism (buffer proportional control + EMA synchronization) is similarly distinct from z-loss approaches and is shown empirically to achieve tighter ratio control. The mechanistic evidence that selected tokens exhibit reduced logit entropy post-DND (Figure 4b, r=−0.58) provides interpretability grounding rarely seen in post-training method papers. Together, these constitute a self-consistent technical system that goes beyond "select tokens, run again."

---

## Suggestions

1. **Add the 100% token variant to Table 4.** Run DND with all tokens selected (uniform reprocessing through the same weight-shared layer) and report its average performance. This single experiment would confirm or reframe the central claim about selective computation.

2. **Specify the attention scope in Section 3.1.2.** Add one sentence clarifying exactly what the packed subsequence attends to during the nested transformer pass (e.g., "selected tokens attend only to each other within the compact subsequence, with new sequential positional embeddings assigned post-packing"). This resolves both the reproducibility and FLOPs validity questions.

3. **Add multi-seed variance for at least a representative subset of the 30B experiments.** Even 3 seeds on 5 benchmarks (BBH, MATH, GPQA, BFCL, LCB-v6) would distinguish reliably positive from noise-level gains in Table 2.

4. **Clarify the notation in Eqs. 6–7.** Replace $L_a, L_c, L_e, L_r$ with explicit references to the architecture notation ($L_s, L_e$) or define them precisely in the text.

---

## Evaluation on Key Axes

- **Originality:** Moderate-to-good. The selective nested reprocessing idea combines known components (token routing, weight sharing, recurrence) in a novel post-training formulation. The push-pull router loss and EMA threshold synchronization are distinctly new design elements.
- **Importance of research question:** High. Parameter-efficient post-training methods for improving off-the-shelf LLMs are of significant practical interest.
- **Claims supported:** Mostly, with gaps. Gain claims on 1B models are well-supported; 30B gains partially; the *selective vs. uniform compute* thesis is the unsupported claim.
- **Soundness of experiments:** Good for 1B models; weaker (single-run, marginal numbers) for the 30B model. The ablations in Table 4 are thorough for Qwen3-1.7B but absent for other architectures.
- **Clarity of writing:** Generally clear, with a notation inconsistency in Section 3.2.1 and an important omission in Section 3.1.2.
- **Value to research community:** Meaningful. The method is plug-and-play, the training recipes are described, and the empirical results across diverse architectures are practically informative.

---

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>

<subscores>
<originality>3</originality>
<importance>4</importance>
<claims_supported>3</claims_supported>
<soundness>3</soundness>
<clarity>3</clarity>
<community_value>4</community_value>
</subscores>