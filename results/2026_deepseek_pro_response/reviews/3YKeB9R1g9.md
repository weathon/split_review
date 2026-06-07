Now let me compare against these Round 2 anchors and finalize.

**Comparisons:**

- **WYL4eFLcxG (6.00):** Studies optimal LR scaling across token horizons. Clean but narrow — one empirical finding, limited theoretical analysis, doesn't explore interactions. Current paper is broader (τ as unifying control, Celerity family, two applications), has a theoretical framework (noisy quadratic model), and larger-scale validation. **Current paper is stronger.**

- **bmrYu2Ekdz (6.50):** PolyPythias — releases 45 training runs studying seed stability. Well-executed, accepted. But models only up to 410M, contribution is primarily data release + analysis. Current paper has larger scale (3.9B), theoretical framework, and practical applications. **Current paper is comparable or slightly stronger.**

- **o9YC0B6P2m (6.75):** Scaling Law with LR Annealing — predicts loss curves across schedules. Showed validation loss, not just training loss. Rejected despite high score due to theoretical gaps and ad-hoc formulation. **Current paper has broader scope but similar empirical limitations; slightly weaker on rigor.**

- **KnoS9XxIlK (6.00):** Multi-power law for loss prediction. Similar limitations (empirical law, training loss only, limited scales 25M-400M). Current paper has much larger scale (3.9B), more applications, and τ discovery. **Current paper is stronger.**

**Final bracket: 6.0–6.75. I settle at 6.5** — above the clean-but-narrow 6.0 papers, comparable to PolyPythias at 6.5, and below the more rigorously validated 6.75 paper. The paper has genuine contributions (τ as unifying parameter, practical applications at scale) offset by real limitations (collapse breaks at high TPP, training-loss-only evaluation).

Now let me write the final review.

---

Let me compile the final review now. I need to make sure I properly attribute the removed points and include all sections.## Summary
This paper demonstrates that training loss curves (TLCs) collapse onto a universal trajectory across model scales when three controls are matched: the AdamW timescale τ = B/(ηλD), the tokens-per-parameter ratio (TPP), and the learning rate schedule. It extends Qiu et al. (2025)'s small-scale findings to practical LLM training with AdamW, weight decay, and co-scaled width/depth/batch size. The paper introduces Celerity, a model family trained under collapse conditions, and demonstrates two applications: using collapse residuals as an early diagnostic for training pathologies and enabling early stopping in hyperparameter optimization.

## Strengths
- **Systematic isolation of τ as the unifying control parameter for TLC shape (Fig. 3, Sec. 3):** Sweeping η, λ, or B independently all produce matching normalized TLCs when the resulting τ values are identical. This clean experiment establishes τ — not individual hyperparameters — as the fundamental quantity governing curve shape, validated on a 610M model at 80 TPP.
- **Demonstration of collapse at LLM scale with practical recipes (Figs. 1, 6, Sec. 4):** Prior work validated collapse only for small models with vanilla Adam and no weight decay. This paper shows collapse for models up to 3.9B using AdamW, weight decay, and co-scaled width/depth/batch size via CompleteP — directly addressing the gap identified by Qiu et al. (2025).
- **Collapse residuals as a practical diagnostic for training pathologies (Fig. 1 right, Fig. 6 right, Sec. 4):** The 1.8B case study provides compelling real-world validation. A numerical instability was detected via collapse residuals starting at ~60% of training, while the raw loss curve showed only a late-stage blip near 90%. The paper documents the full debugging story — root-cause identification (numerical issue in a loss kernel at specific microbatch sizes) and successful repair.
- **Early stopping in HPO via collapse alignment (Fig. 9, Sec. 5):** The method selects optimal hyperparameters after 10–30% of training by aligning partial curves to a predicted normalized TLC fit at 111M scale (~1000× fewer FLOPs). It beats both random selection and the "current best" heuristic used in prior work (Almazrouei et al., 2023). The τ-fixing insight for batch size sweeps (Fig. 7) — that fixing τ rather than λ preserves curve ordering and enables reliable early stopping — is a practical methodological contribution.
- **Celerity's competitive positioning on the compute-efficiency frontier (Fig. 2, Sec. 4):** Against public models (Gemma, Llama, SmolLM, OLMo, etc.), Celerity forms the accuracy/compute Pareto frontier up to the largest training budget, matching BTLm's accuracy with 75% fewer FLOPs.

## Weaknesses

### Fatal
None.

### Major
- **Collapse breaks down at 234 TPP for larger models, undercutting the claimed universality.** At line 202 the paper states: "At 234 TPP, divergences appear late in training for larger models (Fig. 1, middle)." This is the paper's primary TPP band and the regime most relevant for parameter efficiency. The paper attributes this to training-data overfitting, but that is precisely where monitoring and prediction would be most practically valuable. The abstract claims collapse as a general phenomenon when τ and TPP are fixed, yet the evidence shows it fails at the highest TPP for the largest models. The paper does not quantify how badly collapse degrades or at what scale/TPP the breakdown begins, narrowing the domain of applicability relative to what is claimed.

- **All collapse analysis is on training loss, yet the practical motivations implicitly depend on generalization.** Every figure demonstrating collapse (Figs. 1, 3, 4, 6, 8) uses training loss. The early stopping method (Sec. 5) selects hyperparameters by predicting training loss L(T) — whether lower predicted training loss translates to better downstream models is not addressed. The paper's own evidence at line 202 shows that training-loss collapse and held-out-loss behavior can decouple: at 234 TPP, training loss diverges while "held-out data remains aligned with projections." If training-loss collapse can be present while models overfit, the diagnostic value for HPO is called into question. The paper should either demonstrate validation-loss collapse or clearly bound all claims and applications to training-loss behavior only.

### Minor
- **The "early-align" normalization method introduces circularity for the monitoring use case (Sec. 4).** By choosing L(T) to "best align" a partial curve with a reference (line 194), the paper fits a free parameter to maximize apparent alignment. For the early stopping application (Sec. 5), this is less concerning since the fitted L(T) is the prediction and is evaluated empirically (Fig. 9). But for the diagnostic use case in Section 4, it partially constructs the alignment it then uses to detect deviations. The paper mentions an alternative (power-law extrapolation, line 193) but does not compare the two.

- **The link between τ-optimality and collapse is asserted rather than demonstrated.** The paper claims collapse "emerges as a robust marker of compute-efficient and stable pre-training" (line 31). But it defers entirely to Bergsma et al. (2025a) for τ optimality and never tests the contrapositive: does deliberately suboptimal τ at fixed TPP produce non-collapse, and are those runs indeed less compute-efficient? The core empirical claim — fixed τ + TPP → collapse — is well-supported; the optimality framing is an overstatement of that evidence.

- **Narrow downstream evaluation and missing ablations for the parametric model.** The compute-efficiency frontier claim (Fig. 2) rests on only 7 tasks whose selection is not justified. The parametric surrogate model (Eq. 4–5) has a functional form chosen pragmatically rather than derived from Section 3 theory, and the paper does not compare against a pure power-law baseline for the whole curve.

### Trivial
- **λ values for Celerity models are not explicitly tabulated.** They can be derived from the reported τ, η, B, TPP, and N values (λ = B/(η·τ·TPP·N)), but explicitly listing them would aid reproducibility.

## Nice-to-Haves
- A quantitative collapse metric (e.g., mean absolute deviation between normalized curves) compared against a null baseline would strengthen claims beyond visual judgment.
- Testing the early stopping method on hyperparameters beyond λ (e.g., η, B sweeps) would demonstrate generality.
- A more thorough analysis of the 234 TPP divergence — it may be the most interesting finding about the limits of collapse and deserves deeper treatment rather than being noted in passing.
- Comparison of the "early-align" normalization against the power-law extrapolation alternative to quantify how much the free parameter contributes to apparent alignment.

## Removed Points
These points are flagged to be removed, treat them with caution:

- **Harsh Critic Point 4 (missing λ values is a critical reproducibility gap):** REMOVED — λ can be derived from τ = B/(ηλD) using the reported τ, η, B, TPP, and N values. All quantities needed for verification ARE present in the paper.

- **Harsh Critic's "critical implementation details missing" framing:** DEMOTED to Trivial — the paper reports the key quantities. The missing λ values are derivable, not missing.

- **Strength Finder: "Theoretical grounding via the noisy quadratic model (Eq. 3, Appendix B.3)" as a standalone strength:** PARTIALLY REMOVED — the full derivation is in the stripped appendix, so this strength cannot be fully verified. However, Eq. 3 is presented in the main text (line 127) with explanation, so partial credit is warranted. The theoretical contribution is noted within the broader conceptual framework strength.

- **Harsh Critic's claim that the paper "never quantifies inter-run variation or compares collapse tightness to it":** MOVED to Nice-to-Haves — this is a suggestion to strengthen the paper, not a current flaw. The paper's claims about collapse are evaluated visually (which is standard in this line of work, including Qiu et al. 2025), and adding a quantitative metric would be an improvement rather than addressing an error.

## Novel Insights
The identification of τ = B/(ηλD) as a unified, scale-invariant control that governs TLC shape across three independently-swept hyperparameters (η, λ, B) is a genuinely novel and practically useful insight. The demonstration that fixing τ (rather than λ) during batch size sweeps preserves curve ordering — enabling reliable early stopping — has immediate practical implications for HPO workflows. The 1.8B debugging case study provides rare, concrete evidence that collapse-based monitoring can detect training issues substantially earlier than raw loss inspection, offering a principled alternative to the ad-hoc diagnostics currently used in large-scale training.

## Suggestions
- Temper claims about universality to match the evidence: collapse is clean at 20 and 80 TPP but degrades at 234 TPP for larger models due to overfitting. Characterize this as a finding about the limits of collapse rather than downplaying it.
- Either include validation loss curves in the collapse analysis, or explicitly scope all claims and applications to training loss only, with discussion of implications for generalization.
- Report the derived λ values for each Celerity model configuration.
- Add a quantitative collapse metric and a null baseline to move beyond visual judgment of alignment quality.

## Score and Decision

**Round 1 bracket:** 5.5–7.0 (stronger than MLhquJb1qN at 5.25, comparable to o9YC0B6P2m at 6.75, below d8w0pmvXbZ at 8.00).

**Round 2 narrowing:** Compared against WYL4eFLcxG (6.00), KnoS9XxIlK (6.00), bmrYu2Ekdz (6.50), o9YC0B6P2m (6.75), and mao3y822aM (5.50). The current paper is broader and more impactful than the 6.0-anchors, comparable to bmrYu2Ekdz at 6.50, and slightly weaker in rigor than o9YC0B6P2m at 6.75.

**Anchor summary:**
| Path | Score | Round | Comparison |
|---|---|---|---|
| BUpdp5gETF | 2.50 | R1 | Different topic (decoupled LR schedules), much weaker |
| 7X65yoKl3Y | 3.33 | R1 | Different topic (LoRA), much weaker |
| SaOxhcDCM3 | 3.20 | R1 | Different topic (self-consuming training), much weaker |
| KxQnhe5UuJ | 3.00 | R1 | Different topic (CL HPO), much weaker |
| KnoS9XxIlK | 6.00 | R1,R2 | Similar loss-prediction scope; current paper broader and at larger scale → current stronger |
| MLhquJb1qN | 5.25 | R1,R2 | τ-related concepts but weaker empirics; current paper clearly stronger |
| o9YC0B6P2m | 6.75 | R1,R2 | Similar loss-curve prediction; shows validation loss, slightly more rigorous → current slightly weaker |
| WYL4eFLcxG | 6.00 | R1,R2 | Clean but narrow LR scaling study; current paper broader with more applications → current stronger |
| d8w0pmvXbZ | 8.00 | R1 | Excellent empirical study on training stability; current paper less thorough → current clearly weaker |
| Tzh6xAJSll | 7.60 | R1 | Theoretical scaling laws for associative memories; different topic |
| wg1PCg3CUP | 8.00 | R1 | Precision scaling laws; different focus |
| et5l9qPUhm | 8.00 | R1 | Model collapse from synthetic data; different topic |
| xGM5shdGJD | 5.20 | R2 | Scaling law estimation best practices; different topic |
| mao3y822aM | 5.50 | R2 | Loss prediction benchmark; current paper has more novelty and applications → current stronger |
| bmrYu2Ekdz | 6.50 | R2 | Training stability study; comparable quality, current has larger scale and more applications → comparable |
| GeUK3zGreN | 6.50 | R2 | Transformer training without warmup; different topic |
| bAFVlpFQvT | 6.75 | R2 | Memory-efficient training with larger mini-batches; different topic |
| kvLenbZZgg | 6.25 | R2 | Transformer block coupling; different topic |

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>