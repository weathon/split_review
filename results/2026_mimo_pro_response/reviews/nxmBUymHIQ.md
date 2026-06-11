## Summary
This paper proposes LoLoRA, a memory-efficient LoRA variant that updates adapter matrix A via local learning rules (HPCA or autoencoder loss) during the forward pass while training B via backpropagation. The main theoretical contribution is Theorem 4.4, proving that the optimal A initialization lies in the dominant eigenspace of the input covariance matrix under random regression assumptions, formally justifying the empirical findings of EVA (Paischer et al., 2024). Experiments span RoBERTa-large/GLUE, LLaMA-3.1-8B/GSM8K, LLaVA-v1.5-7B, and ablations on TinyLlama-1.1B/Alpaca.

## Strengths
- **Rigorous theoretical characterization of optimal A (Theorem 4.4):** Proves that the optimal A is any nonsingular linear transformation of the top-r eigenvectors of Σ_zz (lines 164–169), formally justifying why PCA-based initialization works — filling the exact theoretical gap that EVA was criticized for lacking when it was reviewed (EVA received 4.75, partly for "lacking theoretical justification" for PCA initialization).
- **Clean A/B asymmetry result (Theorems 4.4 vs 4.5):** Theorem 4.5 (lines 176–181) shows any full-rank B gives identical expected loss regardless of direction, while Theorem 4.4 shows A has a data-dependent optimal subspace. This formally explains the empirically observed asymmetry (Zhu et al., 2024) and directly motivates the hybrid local-global design.
- **Memory savings with maintained accuracy on GSM8K (Table 3):** LoLoRA HPCA achieves 82.9% accuracy at 26 GB extra memory vs standard LoRA at 82.1% at 30 GB — a 13% memory reduction with a 0.8 pp accuracy gain. This is the strongest concrete evidence for the method's practical value.
- **Comprehensive ablation validating theory (Tables 5 & 6):** Across ranks {2, 4, 8} with 4 initializations and 5 local rules (3 seeds each), PCA-converging methods (HPCA, AE) achieve perplexity 2.535–2.557 while SoftHebb (non-PCA) lags at 2.572–2.574, exactly matching Theorem 4.4's prediction. Mean-centering matters (HPCA no mean: 2.540–2.561 vs HPCA: 2.535–2.557).
- **No-spurious-minima guarantee for AE (Theorem 4.6):** All local minima of the autoencoder loss are global and equal the dominant eigensubspace (lines 199–202), providing implementation flexibility.
- **Clear algorithmic presentation:** Algorithm 1 with the explicit FREE_MEMORY(z) step at line 6 and Figure 1's visual comparison of LoRA, LoRA-FA, and LoLoRA make the method easy to understand and reproduce.

## Weaknesses

### Fatal
None.

### Major
- **Online HPCA updates add no clear value over offline EVA initialization.** Against the fair baseline of EVA-initialized LoRA-FA: GLUE (Tables 1–2) shows LoLoRA winning 5/8 tasks by 0.1–1.6 and losing 2/8 by 0.1, all within noise margins; GSM8K (Table 3) tied at 82.9%; LLaVA (Table 4) LoRA-FA (EVA) is slightly *better* on perplexity (2.92 vs 2.93) and loss (1.070 vs 1.075). The conclusion claims "HPCA consistently outperforms standard LoRA-FA" (line 332) but this comparison is against uniform-init LoRA-FA. Against EVA — the meaningful comparison — the online update mechanism adds nothing, reducing the contribution to "HPCA online updates approximate EVA's offline PCA." The paper partially acknowledges this ("HPCA updates do not improve EVA-initialized adapters" in the LLaVA summary, line 296) but the conclusion overstates the finding.
  - **Why it matters:** If EVA initialization + frozen A achieves equivalent results, the local update mechanism's added complexity and extra optimizer state are not justified by the experiments. The paper needs to identify a concrete setting where online adaptation outperforms offline initialization.

- **Consistent performance gap with standard LoRA on GLUE.** Across all 8 GLUE benchmarks, LoLoRA HPCA underperforms standard LoRA: CoLA (66.3 vs 69.6, −3.3), QQP (90.6 vs 91.7, −1.1), MRPC (89.9 vs 90.9, −1.0), MNLI (90.3 vs 90.8, −0.5), STS-B (92.0 vs 92.3, −0.3), QNLI (94.7 vs 94.9, −0.2), SST-2 (96.4 vs 96.6, −0.2). The abstract claims "maintains performance comparable to standard LoRA" but the CoLA and QQP gaps are non-trivial. The paper itself acknowledges "classical LoRA remains the strongest overall" (line 259) but does not discuss why LoLoRA struggles on NLU tasks specifically, especially when on GSM8K it slightly beats standard LoRA.
  - **Why it matters:** The abstract's "comparable" claim is not uniformly supported. While GSM8K results are stronger, the GLUE gap undermines the generality of the claim.

### Minor
- **GSM8K checkpoint selection protocol is ambiguous.** "The model was tested on GSM8K every 0.2 epoch during fine-tuning, and the best result is reported for each method" (line 265). It is unclear whether the best checkpoint is selected using validation loss or test accuracy — if the latter, this is a mild form of test-set leakage. The paper should clarify and also report results at a fixed checkpoint (e.g., end of epoch).
- **Rank for Tables 1–4 not stated in main text.** The rank r and LoRA alpha used for the main experiments are deferred to Appendix C. Since performance varies significantly with rank (demonstrated in Tables 5 & 6), this should be stated inline for readability and reproducibility.
- **Memory savings negligible on LLaVA (Table 4).** 24.1 vs 24.6 GB (~2% savings), honestly acknowledged as due to the visual encoder dominating memory. This limits the practical impact claim for multimodal settings.
- **Theorem 4.6's relationship to known PCA/autoencoder results.** The paper presents the convergence of the symmetric autoencoder to the dominant eigensubspace (lines 197–202) but does not note the well-known connection to classical results on autoencoder PCA convergence (e.g., Baldi & Hornik, 1989). A brief acknowledgment would be appropriate.

### Trivial
- **Typo in Definition 3.1 (line 81):** "W_q, W_k, W_o, or W_o" — W_o appears twice; should be W_q, W_k, W_v, W_o.

## Nice-to-Haves
- Identify and present a concrete setting where online HPCA adaptation outperforms offline EVA initialization (e.g., when EVA's PCA is computed on a poor sample, when input distributions shift during training, or at very low ranks where initialization matters most).
- Compare against gradient checkpointing to contextualize the memory savings — if gradient checkpointing achieves comparable savings with full LoRA quality, the value proposition weakens.
- Measure the spectrum of real ΔW₀ after full LoRA training and compare to the random matrix prediction, strengthening the theoretical contribution's practical relevance.
- Discuss the computational overhead of local updates more explicitly (Table 4 shows ~7 min overhead on LLaVA but this isn't analyzed).

## Removed Points
These points are flagged to be removed, treat them with caution:
- Harsh critic's concern about Assumption 4.1 (random regression matrix) being unrealistic: Verified as stated (line 150) but this is a standard theoretical simplification, not a flaw. The paper doesn't overclaim from this assumption — Theorem 4.4 is stated "under certain assumptions" and the paper doesn't claim the result holds universally.
- Harsh critic's concern about Definition 3.1 typo: Verified as a real typo (line 81: "W_q, W_k, W_o, or W_o"), moved to Trivial.
- Strength Finder's "broad experimental coverage" — while true, this is a supporting observation, not a core strength.

## Novel Insights
The paper's most novel insight is Theorem 4.4, which provides a complete characterization of the set of optimal A matrices — not just PCA but the full equivalence class of nonsingular transformations of the top-r eigenvectors. This directly fills a theoretical gap identified in the EPA paper's reviews (EVA scored 4.75, with multiple reviewers criticizing the lack of theory for why PCA initialization works). The A/B asymmetry (Theorems 4.4 vs 4.5) is also genuinely insightful: it formally explains why A requires data-dependent initialization while B does not, connecting to and extending the empirical observations of Zhu et al. (2024). However, the practical insight — that online HPCA approximates offline EVA — is observational rather than a significant methodological advance, as the experiments show the two are equivalent.

## Suggestions
- **Highest priority:** Present a setting where online HPCA adaptation demonstrably beats offline EVA initialization — without this, the practical contribution is marginal.
- Clarify the GSM8K checkpoint selection protocol (validation loss vs test accuracy).
- State rank and alpha in the main text for Tables 1–4.
- Discuss the CoLA gap specifically — what about NLU tasks makes LoLoRA underperform standard LoRA?
- Add a brief note connecting Theorem 4.6 to the known symmetric autoencoder/PCA convergence literature.

## Calibration Anchors

| Anchor Paper | Avg Human Score | Round | Comparison to LoLoRA |
|---|---|---|---|
| ALLoRA | 3.33 | 1 | LoLoRA has substantially better theory and more comprehensive experiments |
| UnoLoRA | 3.00 | 1 | LoLoRA is more novel and better validated |
| HoLoRA | 3.00 | 1 | LoLoRA has a stronger theoretical foundation |
| MoRA | 4.75 | 1 | MoRA has a novel mechanism but less theory; comparable practical marginality |
| EVA (Paischer et al.) | 4.75 | 2 | LoLoRA directly fills EVA's theoretical gap; practical results are equivalent |
| EigenLoRA | 5.00 | 2 | Different application of PCA to adapters; comparable contribution level |
| LoRA-FA | 5.33 | 1 | LoRA-FA introduced the core freeze-A idea with minimal theory; LoLoRA adds substantial theory but similar practical results vs EVA |
| ReLoRA | 5.75 | 1 | ReLoRA has a more impactful practical contribution (applicable to pretraining) with less theory |
| ROSA | 6.00 | 1 | ROSA is more expressive but was also rejected; different approach |
| LoRAM | 6.20 | 1 | LoRAM addresses a different bottleneck (base weight memory) with stronger practical gains |
| LLaMA-Adapter | 6.33 | 1 | Different approach (zero-init attention), more novel method |
| HiRA | 8.00 | 1 | Clean novel idea with strong empirical gains; clearly above LoLoRA |

**Round 1 bracket:** 4.5–5.5. The paper sits above EVA (4.75, which lacked the theory LoLoRA provides) and around LoRA-FA (5.33, which introduced the core mechanism). LoLoRA's genuine theoretical contribution (Theorems 4.4–4.6) elevates it above EVA, but the lack of clear practical improvement over EVA keeps it from reaching the level of accepted papers like ReLoRA (5.75). Final score: **5.0** — the theory is valuable but the experiments don't demonstrate that online local updates meaningfully improve upon offline PCA initialization.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>