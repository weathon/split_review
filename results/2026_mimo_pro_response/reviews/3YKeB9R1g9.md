Now I have a comprehensive calibration picture. Let me write the final review.

**Round 1 bracket: 6.0–8.0** based on the retrieved anchors.
**Round 2 narrowed to: 6.5–7.5**, with the paper sitting above the 6.00–6.50 Accept papers (Multi-Power Law, Scaling Optimal LR, Straight to Zero, Language models scale reliably) due to broader contributions, and slightly below u-μP (7.33) due to the 234 TPP limitation and narrow early stopping validation.

---

## Summary
This paper extends the "supercollapse" phenomenon from Qiu et al. (2025) to practical LLM training, demonstrating that normalized training loss curves collapse across model sizes (300M–3.9B) when three scale-invariant controls are held fixed: the AdamW timescale τ, tokens-per-parameter ratio (TPP), and learning-rate schedule. The authors identify these controls via systematic experiments grounded in a noisy quadratic model, introduce the Celerity LLM family trained under collapse principles, and demonstrate two practical applications — collapse-based training diagnostics and early stopping in hyperparameter tuning.

## Strengths
- **Principled extension of collapse to practical LLM-scale training with AdamW.** Qiu et al. (2025) only demonstrated collapse at small scale with vanilla Adam and explicitly called for tests at larger scales with practical scaling recipes. This paper directly addresses that gap by showing collapse across 300M–3.9B models with full AdamW (including weight decay), co-scaled width/depth/batch size, and μP/CompleteP (Section 3, Figures 3–4, 6).
- **Mechanistic explanation of scale-invariant controls.** The paper identifies τ, TPP, and LR schedule as the three controls governing TLC shape, supported by a noisy quadratic model (Equation 3) providing a principled bias-variance decomposition. Figure 3 demonstrates empirically that sweeping η, λ, or B produces matching TLC shapes when τ matches — this is a novel analytical contribution beyond prior work.
- **Real-world diagnostic case study.** Collapse residuals detected a numerical instability in the 1.8B run starting at ~60% of training, whereas raw TLC only showed an upward trend after ~90% (Figures 1 right, 6 right). The timing directly guided debugging and avoided wasted investigation — a concrete, non-hypothetical demonstration of practical value.
- **Competitive Celerity model family with principled TPP design.** Figure 5 provides a principled derivation of the compute-compression trade-off justifying 234 TPP. Figure 2 shows Celerity on the accuracy/compute Pareto frontier against OLMo, SmolLM, Gemma, and Llama variants, achieving comparable accuracy to BTLm with 75% fewer FLOPs.
- **Practical early stopping with cross-scale transfer.** The surrogate model fit at 111M scale (1000× fewer FLOPs) transfers to 3.3B, achieving negligible loss gaps when stopping after 10–30% of training for λ sweeps, outperforming random and current-best baselines (Figure 9).
- **Effective negative control.** Figure 1 left demonstrates that Llama-2 (with varying TPP and τ) fails to collapse, directly highlighting the necessity of the identified conditions.

## Weaknesses

### Fatal
None.

### Major
- **Collapse breaks at 234 TPP for training loss — the paper's most interesting TPP band.** The paper acknowledges: "At 234 TPP, divergences appear late in training for larger models. Investigating, we find loss improves disproportionately on training data, while held-out data remains aligned with projections" (Section 4, p. 202). This is significant because 234 TPP is the band justifying Celerity's novel parameter-efficiency trade-off (62% fewer parameters, 67% more FLOPs). Notably, while 20 TPP and 80 TPP each get dedicated collapse panels in Figure 6 (left and middle), 234 TPP does not — only the unnormalized 1.8B training loss with the bug-related blip is shown (Figure 6 right). The claim about held-out loss is stated in a single sentence without supporting data or figures. Since the diagnostic framework (collapse residuals for monitoring) is built on training loss curves, this gap undermines confidence in the framework's reliability at the primary operating point. Showing held-out loss collapse at 234 TPP would resolve this and strengthen the paper substantially.

- **Early stopping validated exclusively on weight decay sweeps.** The early stopping procedure (Section 5, Figure 9) is demonstrated only on λ sweeps at 1.7B/20TPP and 3.3B/30TPP. The paper argues that TLC shape depends only on τ and TPP, with λ being one way to vary τ — but this creates a somewhat circular validation if λ is the only hyperparameter swept in the evaluation. Learning rate and batch size sweeps are more common in practice. While Figure 7 illustrates that fixing τ preserves ordering during batch size sweeps, the full early stopping procedure is not tested on these. Even one additional hyperparameter type would substantially strengthen the generality claim.

### Minor
- **Architecture and data mismatch between controlled study and Celerity.** Section 3 uses a GPT2-like architecture with SwiGLU, GPT2 vocabulary, SlimPajama data, and 2048 context length. Celerity (Table 2) uses Squared ReLU, Llama-3 vocabulary (128K), curated educational/math/code data, and 8192 context length. The theoretical analysis (Appendix B.3) is developed under μP, but Celerity uses CompleteP. While Celerity's collapse curves (Figure 6) suggest the findings transfer, the paper does not explicitly discuss this architectural gap, and a brief ablation or acknowledgment would strengthen the work.

- **Normalization choice (L̂ = 0) vs. Qiu et al. without comparison.** The paper states "simply dividing by the final training loss (i.e., L̂ = 0 in Eq. (1)) resulted in optimal alignment across scales" (Section 3, p. 101), while Qiu et al. (2025) use L̂ set to estimated irreducible loss. Since this normalization formula is central to the paper's methodology, a brief comparison or justification beyond the empirical observation would be valuable.

- **Collapse quality metric N(r) shown in figures but never formally defined.** Figures 6 and 1 show N(r) values (e.g., N(r=0.175) for 20 TPP, N(r=0.087) for 80 TPP) but the paper never defines this metric, explains how it is computed, or discusses thresholds for practical utility.

### Trivial
- The phrase "collapse emerges as a signature of compute-efficient training" (Abstract) is slightly overstated — the paper shows collapse emerges when hyperparameters follow recent scaling laws, which is necessary but not sufficient for compute efficiency.

## Nice-to-Haves
- Characterize held-out loss collapse at 234 TPP explicitly with supporting data/figures.
- Extend early stopping evaluation to at least learning rate sweeps.
- Provide wall-clock savings estimates for the early stopping procedure.
- Discuss sensitivity of the surrogate model to fixed constants (ε₁=0.001, ε₂=0.1, m=0.05) in Equation 4.

## Removed Points
These points are flagged to be removed, treat them with caution:
- Nitpicks about reproducibility (undocumented convergence of alternating optimization, number of iterations needed) — reasonable nice-to-have but not a core weakness.
- Concerns about the surrogate model's ad-hoc functional form — the paper grounds the first term in power-law theory and the second in LR schedule effects; this is reasonable for an empirical paper.
- General concerns about formatting or presentation — parser artifacts, not paper issues.

## Novel Insights
The key novel observation from the review synthesis is that the paper's most compelling practical contribution — collapse-based monitoring — is undermined at the very TPP band (234) that motivates Celerity's design. The paper acknowledges training loss divergence at 234 TPP but only claims held-out loss remains aligned without showing evidence. If the authors can demonstrate held-out loss collapse at 234 TPP, this limitation becomes a feature (switching to held-out loss for high-TPP monitoring), but the current evidentiary gap leaves the diagnostic framework's reliability uncertain at the most interesting operating point.

## Suggestions
- Add a figure showing held-out loss collapse at 234 TPP to directly address the overfitting divergence issue.
- Extend the early stopping evaluation (Section 5) to at least learning rate sweeps, which are more common than weight decay sweeps in practice.
- Briefly discuss the architecture/data transfer gap between the controlled study (Section 3) and Celerity (Section 4).
- Formally define the N(r) collapse quality metric and discuss what constitutes "tight enough" collapse for practical use.

## Reporting: Anchor Papers

| Anchor | Path | Avg Score | Round | Comparison |
|--------|------|-----------|-------|------------|
| Systematic Review of LLMs | 8QTpYC4smR | 1.00 | 1 | Survey paper, no technical contribution — paper under review is vastly stronger |
| Jailbreaking LLMs with CoT | 5kMwiMnUip | 1.40 | 1 | Weak security paper — not comparable |
| Different Rates for Different Weights | BUpdp5gETF | 2.50 | 1 | Learning rate schedules for MoE, limited scale — paper under review is much stronger |
| ALLoRA | 7X65yoKl3Y | 3.33 | 1 | LoRA fine-tuning, different domain — not directly comparable |
| Scaling Laws for Downstream Performance | BDisxnHzRL | 4.25 | 1 | Scaling law estimation, limited validation — paper under review has stronger validation |
| Power Scheduler | gN4stDLq3t | 4.25 | 1 | LR scheduling across token horizons, narrower — paper under review has more contributions |
| Time Transfer | MLhquJb1qN | 5.25 | 1 | Optimal LR/batch size scaling, small models only (32M-354M) — paper under review is clearly stronger |
| Hitchhiker's Guide to Scaling Law Estimation | xGM5shdGJD | 5.20 | 1 | Best practices for scaling law estimation — complementary, paper under review has different focus |
| NanoLM | mao3y822aM | 5.50 | 1 | Loss prediction via μP — narrower scope |
| Multi-Power Law for Loss Curve Prediction | KnoS9XxIlK | 6.00 | 1 | Very similar topic, narrower scope (LR schedule prediction only) — paper under review has more contributions |
| Scaling Optimal LR Across Token Horizons | WYL4eFLcxG | 6.00 | 1 | LR transfer across token horizons — paper under review has broader scope |
| Straight to Zero | hrOlBgHsMI | 6.33 | 2 | Same research area (LR schedules, AdamW timescale), narrower — paper under review extends this work significantly |
| Language models scale reliably | iZeQBqJamf | 6.50 | 2 | Scaling laws for over-training — complementary, different focus |
| Taming Transformer Without Warmup | GeUK3zGreN | 6.50 | 2 | Training stability analysis — different focus |
| Scaling Law with LR Annealing | o9YC0B6P2m | 6.75 | 1 | Very similar topic, rejected despite high score — paper under review has more contributions and practical applications |
| How Does Critical Batch Size Scale | JCiF03qnmi | 6.80 | 2 | Batch size scaling — paper under review has broader scope |
| Rethinking Sparse Scaling | ud8FtE1N4N | 6.67 | 2 | Sparse pre-training — different focus |
| u-μP | P7KRIiLM8T | 7.33 | 1 | Practical HP transfer for low-precision training — similar quality level, paper under review slightly weaker due to 234 TPP limitation |
| Small-scale proxies for training instabilities | d8w0pmvXbZ | 8.00 | 1 | Training instability study — higher quality, more thorough ablations; paper under review is weaker |
| Scaling Laws for Precision | wg1PCg3CUP | 8.00 | 1 | Precision-aware scaling laws — more polished, paper under review has comparable novelty |

**Bracketing:** Round 1 established bracket 6.0–8.0. Round 2 narrowed to 6.5–7.5. The paper is clearly above the 6.00–6.50 Accept papers (broader scope, model family, practical applications) but slightly below u-μP (7.33) due to the 234 TPP limitation and narrow early stopping validation. The 8.00 papers (Small-scale proxies, Scaling Laws for Precision) are more polished and have fewer limitations.

**Final score: 7.0** — A solid paper with genuine, well-supported contributions that warrants acceptance, with the recommendation that the authors address the 234 TPP issue with held-out loss data and expand early stopping validation beyond weight decay sweeps.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>