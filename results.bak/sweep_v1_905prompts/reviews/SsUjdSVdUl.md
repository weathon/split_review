I now have sufficient calibration. Let me write the consolidated review.

## Summary

This paper proposes Critique-RL, a two-stage reinforcement learning approach for training critiquing language models without relying on stronger supervisors. The key insight is that RL with indirect reward signals (based on actor refinement) alone degrades discriminability, producing either overly conservative or overly aggressive critics. Stage I explicitly optimizes discriminability via direct rule-based rewards, and Stage II optimizes helpfulness via refinement rewards while preserving discriminability through KL regularization. Experiments on mathematical reasoning tasks across Qwen2.5-3B/7B show substantial gains over SFT, STaR, Retroformer, and CTRL baselines, with consistent improvements on out-of-domain tasks and iterative training.

## Strengths

- **Genuine diagnostic insight (training dynamics analysis, §4.1, Figure 3)**: The paper systematically identifies that indirect reward signals ($r_{\text{refine}}$, $r_\Delta$, $r_{\text{correction}}$) fail to optimize both $\Delta^{i\rightarrow c}$ and $\Delta^{c\rightarrow i}$ simultaneously because discriminability degrades. This analysis goes beyond the usual "our method works" narrative and provides a clear, empirically grounded motivation for the two-stage design.

- **Clean, well-motivated two-stage solution (Algorithm 1, §4.2)**: Stage I's direct discrimination reward and Stage II's joint optimization with KL regularization to the Stage I model are simple, principled, and directly address the identified failure modes. The design choices are well-explained.

- **Strong and consistent empirical results (Table 1, Table 4)**: Critique-RL consistently outperforms all baselines across 3 in-domain datasets (MATH, GSM8K, AQuA) and 2 OOD datasets (SVAMP, TheoremQA) at both 3B and 7B scales. The margins are substantial — e.g., +5.74% accuracy over CTRL on MATH (7B), +3.71% on SVAMP (7B). Discrimination accuracy (Acc@Dis) gains are even larger (e.g., +13.78% on MATH over CTRL for 7B).

- **Thorough ablation and analysis (Table 3, Figure 5)**: Ablation studies isolate the contribution of each stage, show that removing discrimination terms from Stage II causes sharp drops, and demonstrate that the method also improves helpfulness (not just discrimination) when evaluated with an oracle verifier. The iterative training results (Table 2) show continued gains from a second iteration.

- **Demonstrated generalization**: The method transfers to OOD tasks (Table 4), scales to larger models (72B, Llama3.2, DeepSeek-R1 — referenced in Appendix C), and is explored on an open-ended summarization task (Appendix G) where rule-based verifiers cannot be directly applied.

## Weaknesses

### Fatal
None.

### Major

- **No statistical significance or variance reporting**: All results in Tables 1–4 and the iterative training results appear to be from single runs. RL training with 3B/7B policies on 6,000 critique examples can exhibit variance; differences of a few percent could fall within run-to-run noise. Although the consistency of trends across datasets and model sizes mitigates this concern, the absence of any multi-seed experiments or confidence intervals weakens the reliability claims.

- **The discrimination extraction function $f(x,y,c)$ is underspecified (Equation 7, Algorithm 1)**: The paper defines $f(x,y,c)$ as "the critique model's judgment of the correctness of the original response" and relies on parsing this for the discrimination reward $r_{\text{dis}}$. The exact mechanism — whether via structured output parsing (as suggested by Figure 2, which shows "Correctness of the final answer: Wrong"), regex extraction, or prompted classification — is never stated. This matters for reproducibility and for assessing whether the reward signal is clean. The example in Figure 2 and the mention that "critique models are prompted to give correctness judgments for each step" (line 236) partially clarify the approach, but the paper should state the extraction procedure explicitly.

### Minor

- **No dedicated limitations or discussion of the training-time oracle verifier**: The paper correctly states it does not need an oracle verifier *at test time*, but training still depends on a rule-based correctness verifier for both Stage I ($r_{\text{oracle}}$) and Stage II ($r_{\text{refine}}$). The summarization experiment in Appendix G attempts to address this gap, but the main paper does not discuss this limitation or speculate on how to extend the method to domains where answer correctness cannot be verified by string matching. This omission leaves the "scalable oversight" claim somewhat incomplete.

- **Figure 1 (right) legend is difficult to interpret**: The caption says "w/o Critique-RL @2k and @3k indicating sampling amounts that are 2 times and 3 times the x-axis value, respectively," and the data table lists "w/o Critique-RL (3B)" twice with different values. The mapping between curves and methods is unclear, making the inference-time scaling comparison less interpretable than it should be.

- **Iterative training data reuse is not specified (Table 2)**: The second iteration of training improves Acc from 48.6 to 51.0 and Acc@Dis from 82.8 to 86.5, but the paper does not state whether the same RL dataset ($\mathcal{D}_{\text{RL}}$) is reused or new data is sampled. Reusing the same data would raise questions about overfitting and saturation.

### Trivial

- The legend in Figure 3 appears to list "Baseline(r_correction)" as "Baseline(r_correction)" — a minor typographical inconsistency.
- The paper uses RLOO as the base algorithm but does not specify whether the same codebase was used for all RL baselines (Retroformer uses PPO, CTRL uses GRPO), which could affect the fairness of comparisons.

## Nice-to-Haves

- An ablation that uses only KL regularization in Stage II (without $r_{\text{dis}}$) and separately an ablation with $r_{\text{dis}}$ but without KL regularization would help isolate the contribution of each term more precisely. The current "Stage II w/o discrimination" ablation removes both simultaneously.
- Comparison to non-RL refinement methods (Self-Refine, SuperCorrect, Critic-CoT) is in Appendix E — a brief mention or summary in the main paper would help readers situate the method relative to the broader critique/refinement literature.

## Removed Points

These points were considered but removed with justification:

- **"Narrow task scope limits claims of 'scalable oversight' generality"** (from Harsh Critic): Partially removed. The paper does focus on mathematical reasoning, but it also evaluates on summarization (Appendix G) and OOD tasks. The claim about "scalable oversight" is qualified by the training-time verifier assumption, which I retain as a Minor weakness above. The claim that the method "does not rely on stronger labeling or an oracle reward function during testing" is technically accurate and properly scoped. The criticism about the oracle verifier during *training* is retained as Minor, but the assertion that this "limits claims of generality" overstates the issue — the paper primarily targets math reasoning where such verifiers exist.

- **"Stage I reward might be essentially supervised learning, not RL"** (from Harsh Critic): Removed. The reward in Stage I is $r_{\text{dis}}(x,y,c) = \mathbb{1}(f(x,y,c) = r_{\text{oracle}}(x,y))$, which is a binary signal applied through RL (RLOO). The critic samples different critiques and is reinforced when its judgment matches the oracle. This is a standard RL setup, not supervised learning. Even if extraction is "trivial" (parsing "Correct"/"Wrong"), the RL aspect comes from exploration over critique outputs and KL regularization — the same as how RLHF uses binary preference labels.

- **"No Critic baseline comparison is unfair because the actor was additionally fine-tuned"** (from Harsh Critic): This is a confusion. The "No Critic" row reports the actor's zero-shot reasoning accuracy. The SFT and RL rows use the *same* fixed actor model with an added critic. The comparison is fair — the improvement from "No Critic" to SFT includes the effect of both the critic initialization and the actor's prior fine-tuning, but all critic-based methods share the same actor, so the relative comparisons among them are valid. The absolute comparison to "No Critic" simply shows that having any critic (even a weak one) helps.

- **"Missing baselines like distilling from GPT-4"** (from Harsh Critic): Removed per instructions — the paper explicitly aims to avoid stronger supervision, and including distillation baselines would contradict the paper's framing. This is scope-appropriate.

- **Various strengths from Strength Finder that are generic** (e.g., "addressed an important problem," "the method is well-motivated"): Removed as superficial. The specific, evidence-backed strengths are retained.

## Novel Insights

The paper's most novel contribution is the empirical demonstration and analysis of a structural tension between discriminability and helpfulness when training critique models with RL — specifically, that indirect refinement-based rewards optimize only for the *outcome* of the critique (does the refinement improve?) rather than the *correctness* of the critique's judgment. This explains why prior RL methods (Retroformer, CTRL) hit a performance ceiling: they cannot distinguish between a critique that is correct and one that happens to lead to a good refinement by chance. The two-stage decomposition (first optimize discrimination, then helpfulness with regularization) is a clean solution that reflects this diagnosis. This insight — that critique model training requires explicit discrimination optimization rather than relying on proxy signals — is practically useful for the scalable oversight community.

## Suggestions

1. **Run 3–5 seeds and report mean ± std for all main tables.** This is the single highest-priority improvement for a camera-ready version. Without it, the reader cannot assess the significance of the reported gains.
2. **State the extraction function $f(x,y,c)$ explicitly** — either describe the parsing of the structured output format shown in Figure 2, or release the extraction code with the camera-ready.
3. **Add a brief limitations paragraph** discussing the training-time oracle verifier assumption and directions for extending the approach to tasks without rule-based correctness verification.
4. **Clarify Figure 1 (right)**: label each curve clearly, fix the duplicate "(3B)" entries, and ensure the "w/o Critique-RL" vs "Critique-RL" distinction is visually unambiguous.
5. **Specify whether the iterative training (Table 2) reuses the same RL dataset** or samples new data, and discuss potential saturation.

## Score and Decision

### Calibration Anchors

All anchors retrieved across rounds:

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| E4hK8t7FTS (LLM Fine-tuning for Math) | 3.00 | 1 | Weaker — simpler SFT-based approach, no critique training, narrow scope |
| iL9A4e8RdS (RL simulation explanations) | 3.00 | 1 | Weaker — completely different domain, not LLM critique |
| EXaKfdsw04 (StepProof) | 3.25 | 1 | Weaker — autoformalization, different task |
| v3DwQlyGbv (Paramanu-Ganita) | 2.33 | 1 | Weaker — math pretraining, no critique component |
| JEehcb48Vp (Critic-CoT) | 5.75 | 1,2 | **Comparable** — also trains critique models for math, but uses GPT-4 distillation (stronger supervisor), no RL, less comprehensive experiments |
| 50P9TDPEsh (Critique Ability of LLMs) | 4.67 | 1 | Weaker — evaluation benchmark paper, no training method |
| F0GNv13ojF (Designing Effective RL Reward) | 5.17 | 1 | **Slightly weaker** — studies reward models for math RL training, but proposed solutions (Clip/Delta) are less novel than the two-stage insight |
| gdzpnRBP4F (RLSF) | 4.50 | 1 | Weaker — simpler RL from confidence scores, no critique model |
| mMPMHWOdOy (WizardMath) | 8.00 | 1 | Stronger — large-scale RL training with SOTA results, but different focus (math generation, not critique) |
| Sx038qxjek (CRITIC) | 6.50 | 2 | **Comparable** — tool-interactive critiquing, but prompt-based (no training), broader task range |
| 38E4yUbrgr (RLC) | 6.00 | 2 | **Slightly weaker** — RL self-improvement via self-evaluation, but only on Flan-T5 780M, simpler analysis |
| e3odKmatZr (Critique-out-Loud RM) | 5.25 | 2 | Weaker — reward model training, not critique model training |
| pNkOx3IVWI (UltraFeedback) | 6.25 | 2 | **Comparable** — AI feedback collection, different focus (data rather than RL training recipe) |
| 4KqkizXgXU (Curiosity Red-teaming) | 8.00 | 2 | Stronger — different domain (red-teaming), not directly comparable |
| TyFrPOKYXw (Safe RLHF) | 7.50 | 2 | Stronger — broader impact, more established line of work |

**Round 1 bracket**: After bracketing, the paper sits between the weak anchors (~3.0) and strong anchors (~8.0), clearly in the 5–7 range. The middle-band anchors (Critic-CoT 5.75, RL Reward Design 5.17, RLC 6.00) are the most relevant comparisons.

**Round 2 narrowing**: Comparing to Critic-CoT (5.75), this paper is stronger — it has more comprehensive experiments, does not depend on GPT-4 distillation, and provides genuine diagnostic analysis. Comparing to CRITIC (6.50), it is comparable in quality but different in approach; CRITIC's tool-interactive approach is broader in task scope, while Critique-RL's training-based approach provides deeper methodological contribution. Comparing to RLC (6.00), Critique-RL has a stronger experimental setup (larger models, more baselines) and clearer diagnostic analysis. **Final score: 6.5**, reflecting a solid paper with genuine contributions and strong experiments, held back from a higher score by the absence of statistical significance reporting and a few underspecified design details.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>