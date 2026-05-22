Now I have enough information. Let me compile the final review.

---

## Summary

NuSA-CL proposes a memory-free continual learning framework for vision-language models (CLIP). The key idea is to compute the SVD of each weight matrix before a new task, identify a "null space" (low-energy spectral directions), and then constrain all task-specific low-rank updates to lie strictly within this null space. After training, the update is merged back into the backbone, keeping the parameter count fixed. The method achieves strong results on the MTIL benchmark (Transfer 68.6%, Avg 75.1%, Last 82.8% — best among storage-free methods) and scales to 50-step CIFAR100 (71.85% Last accuracy, +4.4% over ZSCL). The paper also provides extensive mechanistic analysis (spectral dynamics, subspace ablations, rank tradeoff) that convincingly demonstrates *why* the null-space constraint works.

## Strengths

- **Best storage-free performance on MTIL (Table 1).** NuSA-CL uses only 1.5M trainable parameters, zero additional storage, 6.6 GB peak GPU memory, and 1.21 GPU-hours, while outperforming all other storage-free methods (LoRA, MiLoRA) by 4–6% on Transfer and Avg. It is competitive with storage-based methods at a fraction of the resource cost.

- **Convincing mechanistic analysis (Section 6, Figure 2, Table 4).** The paper goes beyond reporting numbers and shows *why* the method works: (a) spectral dynamics (Figure 2) demonstrate that NuSA-CL progressively fills underutilized spectral directions rather than overwriting principal components; (b) subspace ablation (Tail vs. Top vs. Random) cleanly shows that low-energy directions cause less forgetting; (c) core mechanism ablations (Table 4a) verify that the persistent constraint and multimodal adaptation are both essential. This depth of analysis is rare and substantially strengthens the paper.

- **Scalability to long sequences (Table 3).** On the 50-step CIFAR100 class-incremental benchmark, NuSA-CL achieves 71.85% Last accuracy, outperforming ZSCL by 4.4%. The gap widens as the sequence lengthens, supporting the claim that the dynamic null-space recomposition strategy remains effective over many tasks.

- **Practical efficiency and robustness (Table 4b).** SVD initialization takes <1 minute per task (vs. ~81 minutes for InLoRA's data-dependent computation); total training time is 1.21 GPU-hours vs. 4.29 for InLoRA. Performance is stable across a wide range of energy cutoff thresholds (ρ = 0.80 to 0.999), showing minimal hyperparameter sensitivity.

- **Clean theoretical motivation (Lemma 1, Theorem 2).** The paper provides a principled interference bound showing that null-space-constrained updates limit parameter-level interference, and explicitly acknowledges the gap between parameter-space and function-space guarantees (Section 4.2).

## Weaknesses

### Major

- **No error bars or variance reported for any experimental result.** Every result in Tables 1, 2, and 3 is a single point estimate. Continual learning results are sensitive to task order, seed, and initialization. Some margins over strong baselines are modest (e.g., Table 2: Avg 70.3 vs. 68.9 for InLoRA, a 1.4% gap; Last 75.4 vs. 74.8, a 0.6% gap). Without standard deviations over multiple runs, the reader cannot assess whether these differences are statistically significant. Adding means ± std over at least 3 seeds would substantially increase confidence in the core empirical claims.

- **Missing PEFT competitors on the CIFAR100 benchmark (Table 3).** Table 3 compares NuSA-CL against CLIP zero-shot, Continual-FT, LwF, ICaRL, LwF-VR, and ZSCL — but does not include its closest PEFT competitors (LoRA, MiLoRA, InLoRA). Since the paper's core argument about storage-free scalability is most relevant in this class-incremental setting, the absence of these baselines weakens the claim. Adding them would directly test the method's advantage on long sequences against the most comparable approaches.

### Minor

- **Theory–function gap in the framing.** Lemma 1 bounds interference in *parameter space* (Frobenius inner product), but the paper's motivating language in the abstract/introduction ("minimizes interference with previously acquired knowledge") can be read as a function-level guarantee. Section 4.2 explicitly acknowledges this gap ("should be viewed as a local stability condition rather than a full function-level guarantee"), which is good, but the forward-facing sections do not carry this nuance. A few words of qualification in the abstract or introduction would align the framing with the actual theoretical strength.

- **Training hyperparameters not specified in the available text.** The main paper does not state the learning rate, optimizer, batch size, number of training epochs (only "1000 iterations" is mentioned for one ablation), or number of random seeds used. This hinders reproducibility. (These may appear in the appendix, which was stripped by the parser.)

- **No comparison to regularization-based PEFT baselines (e.g., EWC+LoRA, SI+LoRA).** For a method claiming memory-free continual learning, a natural competitor is a simple regularization penalty applied to a LoRA adapter. Its absence leaves open the question of whether the null-space constraint is more effective than off-the-shelf regularization.

### Trivial

- **SVD implementation details not specified.** The paper does not state whether SVD is full or truncated, which library is used, or whether it runs on CPU or GPU.

## Nice-to-Haves

- **Task order sensitivity analysis.** The MTIL benchmark likely uses a fixed task order. A single experiment reversing the order (or a random order) would strengthen claims of generality. The limitations section already flags this as future work.
- **Forward transfer measurement.** Showing that later tasks train faster or achieve higher accuracy than learning from scratch would support the "knowledge accumulation" narrative.
- **Expanding the evaluation to include the CIFAR100 PEFT baselines** (listed under Major above) is the priority; the rest are secondary.

## Removed Points

These points were flagged by reviewers or the strength finder but are removed from the main assessment with justification:

- *"The storage-free vs. storage-based framing overstates a minor advantage because InLoRA's 9MB is negligible in practice."* **Removed.** The categorization is factually correct: InLoRA uses 9MB of gradient projection memory; NuSA-CL uses zero. Whether 9MB matters depends on the deployment scenario, and the paper appropriately targets "resource-constrained" settings. This is a reviewer preference about framing, not a paper flaw.

- *"The abstract's 'zero' claims are slightly misleading because SVD has computational overhead."* **Removed.** The abstract claims zero storage overhead, zero auxiliary model load, and zero parameter growth — all factually correct. SVD computational cost is disclosed in Section 6.

- *"The 'Theorem' label overstates the contribution."* **Removed.** Theorem 2 is a straightforward cumulative extension of Lemma 1. Labeling it a theorem is standard practice for such results; the paper includes the necessary caveat.

## Novel Insights

The paper's core insight — that the approximate null space of a weight matrix (identified via SVD with an energy cutoff) provides a persistent, data-agnostic safe region for sequential updates — is clearly articulated and empirically validated. The most striking finding is not a single accuracy number but the *spectral evidence* (Figure 2): conventional methods (LoRA, Full-FT) barely change the model's effective rank across tasks, whereas NuSA-CL progressively fills underutilized directions. This visualization directly exposes a failure mode of prior methods (overwriting vs. accumulating) and provides a mechanistic explanation for why the null-space constraint mitigates forgetting. The subspace ablation (Tail vs. Top vs. Random) further sharpens this insight by quantifying how much the choice of spectral region matters.

## Suggestions

1. **Add error bars (std over ≥3 seeds) to all main results in Tables 1–3.** This is the single most impactful improvement. Even a brief statement like "results are averaged over 3 random seeds" would address the main evidential concern.
2. **Include LoRA, MiLoRA, and InLoRA on the CIFAR100 benchmark (Table 3)** to directly test the claim of storage-free scalability against the closest competitors.
3. **Report training hyperparameters** (learning rate, optimizer, batch size, scheduler, number of epochs) in the main text or a clearly referenced appendix section.
4. **Add a single sentence in the abstract or introduction** acknowledging that the theoretical analysis operates in parameter space, complementing the existing caveat in Section 4.2.

## Score and Decision

### Calibration Report

**Round 1 bracketing (topically similar CL+VLM papers):**
- Low band (<3.5): mDuton6Tg7 (3.00, Withdrawn), fQTw3w3hnA (3.00, Reject), HeGMugkCOH (3.00, Withdrawn), ixYvy0wOTr (3.00, Withdrawn). These are weaker papers; NuSA-CL is substantially stronger.
- Mid band (3.5–7.5): KeepLoRA T3Vc5fkTzV (5.50, Accept Poster), CNSP NXduufyPtY (4.80, Reject), CoDyRA uqoKr4m8hl (5.00, Reject), N2L Hc71kKCEFG (4.80, Accept Poster). Most relevant.
- High band (>7.5): Papers on navigation (kkBOIsrCXh, 8.00), RL (oBXfPyi47m, 8.00), multimodal reasoning (DM0Y0oL33T, 8.00), text-to-3D (kI27Niy4xY, 8.00). These are not topically similar.

**Round 1 bracket:** 4.5–6.5.

**Round 2 narrowing (4.5–7.5, focused on null-space/orthogonal methods):**
- KeepLoRA T3Vc5fkTzV (5.50, Accept Poster) — very similar method (subspace-constrained LoRA for CL). NuSA-CL has more thorough analysis, better efficiency documentation, and cleaner method, making it somewhat stronger.
- NUFILT HDIf3fYqPP (5.50, Accept Poster) — null-space filtering for model merging. Different setting, comparable score.
- OSFT vQcyqsGJDw (5.00, Accept Poster) — similar SVD-based subspace constraint for LLM CL. Weaker empirical coverage than NuSA-CL.
- CoDyRA uqoKr4m8hl (5.00, Reject) — dynamic-rank LoRA. Rejected over marginal gains and causality concerns.

**Final score determination:** NuSA-CL is stronger than KeepLoRA (5.50) — the analysis section is substantially deeper, efficiency claims are better documented, and the method is simpler (no gradient projection, no storage of previous directions). It is clearly above OSFT (5.00) and CoDyRA (5.00). The main weaknesses (no error bars, missing CIFAR100 PEFT baselines) are real but do not invalidate the core contribution. A score of **6.0** positions the paper appropriately: a solid accept, above the typical 5.0–5.5 range for this sub-area, but not quite in the 7+ tier that would require tighter empirical rigor across the board.

**Calibration anchors (all rounds):**

| Anchor ID | Score | Round | Comparison |
|---|---|---|---|
| mDuton6Tg7 | 3.00 | R1 | Weaker CL+VLM paper; NuSA-CL is much stronger |
| fQTw3w3hnA | 3.00 | R1 | Weaker CL+VLM paper; NuSA-CL is much stronger |
| HeGMugkCOH | 3.00 | R1 | Unrelated TTA paper |
| ixYvy0wOTr | 3.00 | R1 | Weaker CL+VLM; NuSA-CL is much stronger |
| KeepLoRA T3Vc5fkTzV | 5.50 | R1/R2 | Most similar conceptually; NuSA-CL has better analysis and efficiency |
| CNSP NXduufyPtY | 4.80 | R1 | Prompt-based null-space; NuSA-CL is cleaner and more novel |
| N2L Hc71kKCEFG | 4.80 | R1 | Different setting (unlabeled CIL); comparable rigor |
| CoDyRA uqoKr4m8hl | 5.00 | R1/R2 | Dynamic-rank LoRA; NuSA-CL is more principled |
| NUFILT HDIf3fYqPP | 5.50 | R2 | Different setting (model merging); similar quality |
| OSFT vQcyqsGJDw | 5.00 | R2 | SVD-subspace CL for LLMs; NuSA-CL has stronger analysis |
| Compo-ReAlign eiTy6AYeQi | 6.00 | R2 | Different CL setting; similar score tier but different sub-area |

**Score: 6.0 — Accept (Poster)**

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>