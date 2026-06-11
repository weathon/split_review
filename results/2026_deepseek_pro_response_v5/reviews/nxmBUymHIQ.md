Now I have enough information to finalize the review and score. Let me compile everything.

**Calibration comparison:**

| Anchor | Score | Comparison to LoLoRA |
|---|---|---|
| CAN (1.50) — Hebbian learning, R1 | 1.50 | LoLoRA is substantially better — has theory, multi-domain experiments, clear method |
| Projected Subnetworks (2.00) — R1 | 2.00 | LoLoRA is better — more principled approach, better evaluation |
| ASR Medication (2.00) — R1 | 2.00 | Not comparable; LoLoRA is more technically sophisticated |
| Activations Aren't Cheap (4.25) — R1, R2 | 4.25 | LoLoRA is slightly better — has theoretical contribution, but similar empirical issues |
| Selective Layer Freezing (3.75) — R2 | 3.75 | LoLoRA is better — more novel method + theory |
| Singular Value Adaptation (3.75) — R2 | 3.75 | LoLoRA is better — more complete evaluation |
| **EVA (4.75)** — R2 | 4.75 | **Most comparable.** LoLoRA provides the theory EVA lacked, but empirical case weaker |
| MoRA (4.75) — R2 | 4.75 | Similar quality — mixed empirical evidence but real idea |
| GLoRA (4.75) — R2 | 4.75 | Similar quality |
| **LoRA-FA (5.33)** — R1 | 5.33 | LoRA-FA is better — simpler method with cleaner empirical validation |
| ReLoRA (5.75) — R1 | 5.75 | ReLoRA is better — stronger empirical results, clearer contribution |
| LoRAM (6.20) — R1 | 6.20 | LoRAM is clearly better |
| VeRA (7.25) — R1 | 7.25 | Much stronger paper |

**Bracket from R1:** 3.5–5.5  
**Narrowing from R2:** LoLoRA sits near EVA (4.75) — slightly below due to weaker empirical validation. **Final score: 4.5.**

The paper has a real theoretical contribution (Theorem 4.4) but the empirical story is unconvincing: LoLoRA doesn't clearly beat LoRA-FA (EVA), the memory framing is misleading, and the EVA inconsistency across benchmarks is never addressed.

---

## Summary

LoLoRA proposes a memory-efficient LoRA variant where adapter matrix A is updated during the forward pass using gradient-free Hebbian PCA (HPCA) or autoencoder reconstruction, eliminating the need to store A's activations for backpropagation, while matrix B is trained conventionally via backprop. The paper provides a theoretical analysis (Theorem 4.4) proving that under random regression assumptions, the optimal A initialization spans the top-r principal components of the input covariance matrix, motivating HPCA-style forward-pass updates. Experiments span NLU (RoBERTa-large on GLUE), math reasoning (LLaMA-3.1-8B on GSM8K), multimodal fine-tuning (LLaVA-v1.5-7B), and ablations on TinyLlama.

## Strengths

- **Clean theoretical result motivating the method (Theorem 4.4):** The derivation showing that the optimal A initialization under random regression assumptions is any nonsingular linear transformation of the top-r eigenvectors of the input covariance matrix provides a principled justification for why PCA-based updates to A should work. This formalizes the empirical motivation behind EVA (Paischer et al., 2024) within a broader theoretical framework that the EVA paper itself lacked (EVA reviewers explicitly criticized the absence of theoretical justification).

- **Systematic ablation of local update rules (Table 6):** The comparison of five distinct local update variants (HPCA, HPCA no-mean, HPCA svd-first, AE, SoftHebb) across three ranks cleanly demonstrates that methods converging to the PCA subspace (HPCA variants, AE) cluster together in perplexity (~2.535–2.558 at r=8) and substantially outperform SoftHebb (2.572), which lacks this convergence property. This directly validates the theoretical prediction that any rule converging to the dominant eigensubspace should work.

- **Multi-domain evaluation:** The method is evaluated across three model families (RoBERTa-large, LLaMA-3.1-8B, LLaVA-v1.5-7B) and task types (NLU, math reasoning, multimodal), providing reasonable breadth for a new method paper.

## Weaknesses

### Fatal

None.

### Major

- **LoLoRA does not demonstrate a clear benefit over LoRA-FA with EVA initialization.** On MathQA (Table 3), LoLoRA HPCA and LoRA-FA (EVA) tie at 0.829 accuracy. On LLaVA (Table 4), LoRA-FA (EVA) achieves lower perplexity than LoLoRA HPCA (2.92 vs 2.93). On GLUE, LoLoRA HPCA beats LoRA-FA (EVA) but is itself beaten by LoRA-FA (uniform) on most tasks. The ablation (Table 6) shows LoRA-FA (EVA) at 2.536 vs LoLoRA HPCA at 2.535 at r=8 — virtually identical. Since LoRA-FA (EVA) is simpler (no per-step local updates, no local optimizer state, identical forward-pass cost beyond a one-time PCA pass), the paper has not demonstrated why anyone should adopt LoLoRA over LoRA-FA (EVA). The claimed advantage reduces to "doesn't need a separate PCA pass," which is a thin justification.

- **Memory savings framing is misleading.** The paper consistently compares memory against standard LoRA (e.g., "13% extra memory reduction" in the MathQA summary at line 277, "up to 20% less GPU memory" in GLUE at line 259). The proper baseline for memory comparison is LoRA-FA, which already eliminates A's activation storage AND A's optimizer state. LoLoRA reintroduces optimizer state for A's local updates (acknowledged at line 334: "our method introduces a small amount of extra optimizer state for the local updates, unlike standard LoRA-FA"). Table 4 confirms LoLoRA uses 24.1 GB vs LoRA-FA's 23.9 GB — LoLoRA is slightly worse on memory than LoRA-FA. The claimed memory advantage over LoRA-FA does not exist.

- **EVA initialization inconsistency is never analyzed.** EVA initialization (PCA of input activations) is central to the theoretical motivation, yet its empirical performance is inconsistent: it substantially underperforms uniform initialization on GLUE (e.g., CoLA 64.7 vs 67.9, RTE 83.6 vs 86.4) while being the best method on MathQA (0.829) and TinyLlama/Alpaca (Table 5). The paper notes the GLUE underperformance (line 259: "EVA initialization underperforms on this setting") but offers no analysis or hypothesis for why PCA-based initialization — which Theorem 4.4 proves is theoretically optimal — would systematically hurt on some benchmarks. This unexplained inconsistency undermines confidence in the theoretical narrative.

### Minor

- **"Comparable performance to standard LoRA" is overstated for GLUE.** The abstract claims LoLoRA "maintains performance comparable to standard LoRA." On GLUE (Tables 1-2), LoLoRA HPCA is consistently behind standard LoRA: CoLA 66.3 vs 69.6, MNLI 90.3 vs 90.8, QQP 90.6 vs 91.7, MRPC 89.9 vs 90.9. While gaps are modest, the phrasing overstates the empirical picture for NLU.

- **Local optimizer for A is unspecified.** Algorithm 1 uses `Opt_loc` for A but the paper never specifies whether this is AdamW, SGD, or another optimizer, nor what learning rate or hyperparameters are used for the local updates. The general training settings (line 235) mention AdamW for "all scenarios" but do not distinguish between the global optimizer for B and the local optimizer for A. This is a reproducibility gap.

### Trivial

- **Vaswani et al. (2023) citation appears erroneous (line 124).** Definition 4.1 references "Vaswani et al. (2023)" for the global loss definition. The well-known Vaswani et al. paper is the 2017 "Attention Is All You Need." This appears to be a citation error (likely the authors meant a different reference).

## Nice-to-Haves

- A proper memory budget breakdown comparing LoRA, LoRA-FA, and LoLoRA, quantifying optimizer state for A's local updates, would clarify the method's actual memory profile.
- The paper would benefit from testing settings where online HPCA updates provide a clear advantage over one-time PCA, such as continual learning or tasks with shifting input distributions — these are the natural use cases for online adaptation.
- Statistical significance analysis for the many comparisons falling within mutual error bars would strengthen the empirical claims.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **Harsh Critic claim that "Theorem 4.5 is unconnected to any design choice."** REMOVED. Theorem 4.5 directly supports the paper's argument about A/B asymmetry — it shows any full-rank B is optimal while A has a structured optimum. This connects to the design choice of locally updating A and using gradient-based updates for B.

- **Harsh Critic claim about "no direct comparison to LoRA-FA (EVA) as a named baseline in summary tables."** REMOVED. LoRA-FA (EVA) appears explicitly as a named row in Tables 1-6.

- **Strength Finder claim that "the method reuses standard AdamW for both A and B."** REMOVED as a standalone strength. The paper does not explicitly state this; `Opt_loc` is left unspecified. This was an inference not supported by the text.

- **Strength Finder claim about "up to 20% less GPU memory" as verified in Appendix D.** REMOVED as a strength. The Appendix was stripped in parsing and the claim cannot be verified from the main paper alone. Moreover, this comparison is to standard LoRA rather than LoRA-FA.

- **Harsh Critic complaint about "the base model accuracy (0.79) is from a single evaluation without error bars."** REMOVED. The base model accuracy is from a fixed pre-trained checkpoint evaluated deterministically — there is no training variance to capture for a frozen model.

- **Harsh Critic formatting nitpick about "purple" in Figure 1 caption.** REMOVED — this is a parser artifact; the original submission would have correct spelling ("purple").

- **Harsh Critic concern that "the memory data is in Appendix D (which was stripped)."** REMOVED. The appendix exists in the original submission; stripped appendices are a parsing artifact, not an author error.

- **Harsh Critic claim about "error bars overlap throughout — the paper never addresses whether any differences are statistically significant."** Partially REMOVED as a standalone weakness — this is folded into the Nice-to-Haves. Error bars are reported (which is good practice) and most LoRA-variant papers in this space do not conduct formal significance testing. The real issue is that the differences are small, not that they lack formal tests.

- **Harsh Critic question about "the bridge from theory to method — why updating A toward input PCA during training is right."** Partially REMOVED as a fatal or major weakness. The paper explicitly frames this as: given the constraint of no backprop through A, HPCA toward the input PCA is the best thing to do based on Theorem 4.4. This is acknowledged in the limitations (line 334: non-stationarity of targets). The paper is transparent about the assumption.

- **Strength Finder claim about "Practical algorithm design with minimal implementation overhead."** REMOVED as a standalone strength. This is too generic — many LoRA papers have simple algorithms. The actual overhead of the local optimizer state is not quantified, contradicting "minimal."

## Novel Insights

The paper's theoretical framework highlighting the A/B asymmetry (Theorem 4.4 vs 4.5) offers a genuinely novel perspective on LoRA adapter optimization: under random regression assumptions, A has a structured optimum (spanning the top-r PCA subspace) while any full-rank B is equally optimal. This provides theoretical grounding for the empirical observation in prior work (Zhu et al., 2024) that A is more "transferable" and B is more "task-specific." The ablation (Table 6) cleanly validating that any local rule converging to the PCA subspace works comparably is a useful empirical finding for the local learning community — it confirms that the convergence target matters more than the specific update rule.

## Suggestions

- Reframe the paper's contribution around the theoretical insight and the local-update mechanism rather than around claimed memory savings vs LoRA-FA. The honest framing is: LoLoRA achieves similar performance to LoRA-FA (EVA) but does so online without a separate PCA pass. This is a valid but modest contribution that the current abstract and introduction overstate.
- Test settings where online adaptation provides a clear advantage over one-time PCA, such as continual learning or tasks with shifting input distributions — these are the natural motivation for online updates.
- Specify the local optimizer and its hyperparameters explicitly.
- Analyze and discuss why EVA initialization underperforms on GLUE while excelling elsewhere. If the anomaly is due to small PCA sample size or a mismatch between input distribution and task-relevant subspace, this should be investigated.

---

**Anchor summary (all rounds):**

| Path | Score | Round | Comparison |
|---|---|---|---|
| SI6zocV2SS (CAN) | 1.50 | R1 | Much weaker — no theory, limited evaluation |
| WM5G2NWSYC (Projected Subnetworks) | 2.00 | R1 | Weaker — less principled, narrower evaluation |
| gpKEDj9Dgg (ASR Medication) | 2.00 | R1 | Not comparable — application paper, lower rigor |
| kvBuxFxSLR (Selective Layer Freezing) | 3.75 | R2 | Weaker — incremental, less novel |
| VpeAsLmcvg (Singular Value Adaptation) | 3.75 | R2 | Weaker — less complete, no multi-domain eval |
| 3ylNuZXtMg (Activations Aren't Cheap) | 4.25 | R1,R2 | Slightly weaker — practical but less novel |
| qOqCXEXsX4 (Lottery Ticket Adaptation) | 4.25 | R1 | Comparable — real idea, mixed evidence |
| O6QZ4W6GXt (ShareLoRA) | 4.20 | R1 | Slightly weaker — less theoretical depth |
| **DM6Q45HWSk (EVA)** | **4.75** | **R2** | **Most comparable — LoLoRA adds theory EVA lacked but empirical case is weaker** |
| SxOrhLuuVz (MoRA) | 4.75 | R2 | Comparable — mixed empirical evidence |
| NXnNiT0fdp (GLoRA) | 4.75 | R2 | Comparable — similar quality |
| fD8Whiy7ca (Low-Dim Error Feedback) | 5.50 | R2 | Slightly better — stronger empirical results |
| RbKThNNFxr (LoRA-FA) | 5.33 | R1 | Better — simpler method, cleaner validation |
| DLJznSp6X3 (ReLoRA) | 5.75 | R1,R2 | Better — stronger empirical results |
| s7DkcgpRxL (LoRAM) | 6.20 | R1 | Clearly better |
| d4UiXAHN2W (LLaMA-Adapter) | 6.33 | R1 | Clearly better |
| NjNfLdxr3A (VeRA) | 7.25 | R1 | Much stronger |
| TwJrTz9cRS (HiRA) | 8.00 | R1 | Much stronger |

**Bracket:** R1 placed LoLoRA in 3.5–5.5. R2 narrowed to ~4.5, anchored against EVA (4.75). LoLoRA adds theoretical rigor that EVA reviewers explicitly requested, but the empirical case is weaker because the online updates don't clearly beat one-time EVA initialization and the memory framing is misleading. Final score: **4.5**.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>