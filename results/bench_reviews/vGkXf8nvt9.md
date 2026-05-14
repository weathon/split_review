Now I have a thorough understanding of the paper and the calibration anchors. Let me assemble the final review.

---

## Summary

The paper proposes Forget-to-Focus (F2F), a two-stage protocol that performs targeted unlearning on a general-domain "forget set" (BookCorpus) before fine-tuning on a domain-specific dataset. The central claim is that actively removing irrelevant pre-training knowledge via gradient ascent (stabilized by gradient descent on a retain set) improves domain specialization. Experiments span coding (HumanEval, MBPP), medical (PubMedQA, MedMCQA), and math (MATH, GSM8K) domains across models from 0.6B to 72B parameters. The paper reports consistent gains over standard fine-tuning, DAPT, and LoRA, and supports these with representational analyses (CKA, SVCCA, PCA-shift, Fisher) and calibration improvements.

## Strengths

- **Novel framing of unlearning for domain adaptation**: The paper repurposes machine unlearning from a privacy tool into a deliberate preparatory stage for enhancing fine-tuning. This is a genuinely fresh perspective supported by a clear empirical protocol. The central hypothesis — that suppressing irrelevant priors creates a cleaner optimization landscape for specialization — is articulated well and tested systematically.

- **Comprehensive, multi-domain, multi-scale empirical validation**: F2F is evaluated on 3 domains (coding, medical, math), 5+ model families (Qwen, LLaMA, Gemma), and scales from 0.6B to 72B parameters. Table 1 shows F2F (GA+GD + SFT) achieving HumanEval pass@1 of 42.07 for Qwen-0.6B vs. 31.71 for SFT alone (+10.36 points), and 60.37 for LLaMA-8B vs. 56.71 for SFT. Multi-seed results in Appendix Table 9 confirm robustness: e.g., Qwen 2.5 7B HumanEval: 53.70 ± 0.005 (F2F) vs. 44.35 ± 0.004 (SFT), a +9.4 point gain with tiny standard deviations. The GA-only variant (no retain set, σ=0) also shows consistent gains over SFT across models in Table 1 (e.g., Qwen-0.6B HumanEval: 40.02 GA+SFT vs. 31.71 SFT), providing evidence that the gains are not solely attributable to retain-set warm-start.

- **Multi-faceted representational analysis**: The paper goes beyond accuracy to analyze CKA, SVCCA, PCA-shift, and Fisher information. Figure 4 shows F2F causes greater representational drift from the unlearned model than standard tuning. Figure 7 demonstrates F2F redistributes Fisher sensitivity to moderate shallow-layer activity while standard fine-tuning sharply amplifies it. These analyses provide mechanistic evidence connecting unlearning to altered representational geometry.

- **Calibration and reliability improvements on medical QA**: Table 7 shows F2F reduces ECE to 0.050 vs. 0.277 for standard fine-tuning — a practically meaningful improvement for sensitive applications. Figure 8 confirms better-spread confidence distributions. Broad-skill retention is also verified (Table 5), with F2F largely preserving or improving general benchmark performance and Alpaca-Eval win rate.

- **Ablation of forget-set quality and unlearning variants**: Table 3 systematically compares BC-Select, BC-Mixed, and BC-Cosine forget sets across three domains, and Figure 3 compares GA+GD, GA, NPO, and GA+KL unlearning algorithms, providing actionable practical guidance.

## Weaknesses

### Fatal

None.

### Major

- **Retain set drawn from downstream fine-tuning data creates a potential confound**: The paper states (line 331): "The retain set is a small subset of the fine-tuning data, following prior work (Geng et al., 2025)." During the GA+GD unlearning phase, the model performs gradient *descent* on this retain set simultaneously with gradient *ascent* on the forget set (BookCorpus). This means the model receives some exposure to target-domain data before fine-tuning begins. While the retain set is used as a stabilizer (not as pre-training), and while the GA-only variant (σ=0, no retain set) still shows consistent improvements over SFT in Table 1, the paper could more explicitly disentangle how much of the GA+GD gain comes from unlearning vs. from early exposure to the retain set. The DAPT baseline provides partial comparison (DAPT also exposes the model to domain text), but a direct ablation with a non-domain retain set would strengthen the contribution.

- **No compute-equivalent control for the unlearning phase**: F2F adds an unlearning phase (1000 steps, ~0.55 GPU-hours on A100 per Appendix C.1) before fine-tuning. The baselines (SFT, LoRA) do not receive an equivalent amount of additional optimization. DAPT serves as a partial control (it also involves additional pretraining), but a more targeted control — e.g., the same number of gradient steps on random general text with standard gradient descent, followed by fine-tuning — would better isolate whether the gains arise specifically from gradient *ascent* on the forget set or from any additional optimization. The GA-only results and the DAPT comparison mitigate this concern, but it remains a gap.

### Minor

- **Theoretical analysis (Section 2) is disconnected from the empirical work**: The convex, strongly-convex analysis with orthogonal subspace decomposition does not apply to LLM fine-tuning and does not inform the experimental design. The proposition and corollary are stated but never referenced in interpreting results. This section could be shortened or removed without affecting the paper's contribution.

- **Larger models fine-tuned for only 1 epoch (Section 3.4)**: All models except Qwen-0.6B are fine-tuned for a single epoch "due to their larger parameter sizes and to reduce the risk of overfitting." This means larger models undergo far less adaptation than the 0.6B model (8 epochs). The gains from F2F may partially reflect compensation for an undertuned baseline, particularly for Gemma-2B and LLaMA variants where SFT alone shows regressions on some benchmarks. The paper would benefit from showing that F2F's advantage persists under more comparable fine-tuning budgets.

- **No contamination analysis for code and math datasets**: OpenCoder (fine-tuning data) and HumanEval/MBPP (evaluation) may share overlapping content, as may OpenMathInstruct and MATH/GSM8K. The paper does not analyze or decontaminate. While unlikely to explain the magnitude of observed gains, a brief analysis would address a standard concern in LLM benchmarking.

### Trivial

- The notation in Section 2 is difficult to parse due to rendering issues (though this may be a PDF extraction artifact). For clarity, the key update rule and propositions could be presented more cleanly.

## Nice-to-Haves

- An ablation where the retain set is replaced by non-domain general text would directly address the retain-set confound and strengthen the central claim that *unlearning* (rather than early domain exposure) drives the gains.

- A compute-equivalent baseline (e.g., continued pretraining on random BookCorpus with standard GD for the same number of steps, then fine-tuning) would isolate the effect of gradient ascent.

- Perplexity or loss curves during the unlearning phase, showing that the forget-set loss increases while retain-set loss stays stable, would provide direct evidence that targeted forgetting is actually occurring (beyond the SAE-based forgetting probe in Appendix A.3).

- Concrete qualitative examples of negative transfer being alleviated (e.g., cases where standard fine-tuning produces incorrect answers due to general-knowledge interference and F2F corrects them) would ground the abstract motivation in Section 1.

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **"The retain set leaks target-domain knowledge, invalidating the claim" (from Harsh Critic #1)** — Removed as a fatal claim because the paper evaluates GA-only (σ=0, no retain set) and shows it consistently outperforms SFT (e.g., Qwen-0.6B HumanEval: 40.02 GA+SFT vs. 31.71 SFT). The retain set is used for stabilization during gradient ascent, not as pre-training, and the gains persist without it. Retained as a major (not fatal) weakness because the paper could more explicitly disentangle retain-set effects in GA+GD.

2. **"Forget set construction is heuristic and unvalidated" (from Harsh Critic #4)** — Removed. The paper systematically evaluates three forget-set types (BC-Select, BC-Mixed, BC-Cosine) in Table 3 and analyzes the relationship between forget-set quality and downstream performance. This is a strength of the paper, not a weakness.

3. **"No systematic comparison of GA+KL and NPO in main experiments" (from Harsh Critic, Section-by-Section)** — Removed. Figure 3 explicitly compares GA+GD, GA, NPO, and GA+KL on medical domain for both Qwen-0.6B and LLaMA-8B. The comparison exists in the main paper.

4. **"Theoretical analysis assumes strong convexity; disconnected from empirical work" (from Harsh Critic, Section 2)** — Retained as minor (not major, not fatal) because while the disconnect is real, it does not threaten the empirical contribution.

5. **"Lack of statistical rigor and variance reporting in main results" (from Harsh Critic #3)** — Partially removed. Table 9 in the appendix provides multi-seed results with standard deviations across both coding and medical domains, showing very small variance (±0.001–0.012). While these are in the appendix rather than main text, this is standard practice in LLM benchmarking. The criticism is softened to a minor note.

6. **"No control for extra training compute" (from Harsh Critic #2)** — Retained as major because DAPT provides only a partial control and a more targeted compute-equivalent baseline would strengthen the contribution. However, this is not fatal because DAPT + the GA-only results together provide evidence that unlearning specifically helps.

7. **"BC-Cosine uses target-domain embeddings — tantamount to target knowledge in forget set" (from Harsh Critic, Section-by-Section)** — Removed. BC-Cosine is designed as a practical automated method for forget-set selection; using target-domain embeddings to identify *non-overlapping* samples is a reasonable approach, not a confound. The embeddings are used to select the forget set (BookCorpus samples far from domain centroid), not to inject domain knowledge.

8. **Strength Finder items removed**: Generic strengths without specific evidence ("the paper tackles an interesting research question") were dropped.

## Novel Insights

The paper's most valuable insight is the empirical demonstration that gradient ascent on general-domain data systematically reshapes LLM representational geometry in ways that benefit downstream specialization — specifically by dampening shallow-layer Fisher sensitivity (which standard fine-tuning amplifies) and by inducing targeted rather than uniform PCA drift. This suggests that unlearning may work not primarily by "erasing" specific facts but by reallocating parameter sensitivity away from low-level generalist features, creating headroom for domain-specific learning. This connection between unlearning and representational efficiency is more interesting than the raw accuracy numbers alone would suggest, and points toward a mechanistic understanding of why removing "irrelevant" knowledge helps.

## Suggestions

1. Add an explicit ablation using a non-domain retain set (e.g., random BookCorpus samples with gradient descent, while still performing gradient ascent on the forget set) to cleanly isolate the unlearning effect from the retain-set warm-start in GA+GD.

2. Shorten or remove the convex-analysis theory in Section 2, or replace it with a more relevant empirical motivation that directly connects to the LLM setting.

3. Run a compute-equivalent baseline (standard GD on random BookCorpus for the same number of unlearning steps, followed by fine-tuning) and report it alongside existing baselines.

4. Provide perplexity trajectories on the forget set during unlearning to demonstrate that gradient ascent is actually increasing loss on BookCorpus, confirming the "forgetting" mechanism.

5. Add a brief contamination analysis or discussion of potential overlap between OpenCoder/HumanEval and OpenMathInstruct/MATH.

## Score and Decision

### Calibration Anchors

| Path | Avg Score | Decision | Comparison |
|------|-----------|----------|------------|
| guUUlHPXRw | 2.00 | Reject | Severely flawed (findings reflect experimental design, not principles); our paper is far more rigorous |
| XZhDjhVwma | 3.50 | Reject | "Exclusive Unlearning" — marginal gains and destroys general capabilities; our paper shows consistent gains while preserving broad skills |
| iKqQGEOeej | 5.50 | Reject | "Memorize to Forget" — narrower evaluation, insufficient novelty justification; our paper has broader empirical scope |
| vcWDDfA4Ev | 6.00 | Accept (Poster) | "ADEPT" — two-stage domain adaptation, evaluated on 2 domains, strong theory; our paper tests 3 domains with more model scales but weaker theory |
| mvLhN0veUd | 6.00 | Accept (Poster) | "Breaking Barriers" — broad empirical study, sound design; comparable empirical breadth, our paper has stronger methodological contribution |
| UHyJqF1mqJ | 3.50 | Reject | Domain adaptation benchmark paper; our paper has a more complete experimental contribution |
| MBJCUQ2Iez | 3.33 | Reject | Evaluation framework paper; not directly comparable |

The paper under review compares favorably with the 6.00-scored anchors (ADEPT and Breaking Barriers) in terms of empirical breadth and significance of findings. It is clearly stronger than the 3.50–5.50 unlearning papers (Exclusive Unlearning, Memorize to Forget) in scope and evidence quality. The retain-set confound and absent compute-equivalent control are real but not fatal — the GA-only results and DAPT comparison provide meaningful mitigation. The theoretical section is weak, but the empirical contribution stands on its own. I assign a score of **6.0**, corresponding to a solid poster acceptance with clear strengths and addressable weaknesses.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>