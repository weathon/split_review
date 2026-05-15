Thank you. I have now read the full paper and verified all claims systematically. Let me produce the consolidated review.

---

## Summary

SwitchLoRA proposes a parameter-efficient pre-training method that periodically swaps individual column/row vectors of LoRA adapters with a pool of candidate vectors, enabling the cumulative parameter update to reach full rank while keeping per-step communication costs low. The method is evaluated on LLaMA models from 130M to 1.3B parameters, achieving perplexity of 15.01 on the 1.3B model — surpassing full-rank training's 15.23 — while reducing trainable parameters by roughly 50–60%.

## Strengths

- **SwitchLoRA surpasses full-rank perplexity on the 1.3B model while reducing parameters.** Table 3 reports perplexity 15.01 (SwitchLoRA rank=512) vs. 15.23 (full-rank), and the paper reports a 54% reduction in trainable parameters (Table 4). This is a concrete, non-trivial result for parameter-efficient pre-training.

- **Consistent perplexity improvements across model scales compared to vanilla LoRA.** Table 2 shows SwitchLoRA rank=128 on the 350M model achieves 19.96 vs. LoRA's 31.87 and full-rank's 18.72. At rank=256 on 350M, SwitchLoRA (18.70) nearly matches full-rank (18.72). The gap between LoRA and SwitchLoRA grows with model size, suggesting the method becomes more valuable at scale.

- **Favorable comparison against the most closely related methods (ReLoRA and GaLore).** SwitchLoRA outperforms ReLoRA even when ReLoRA uses 25× more full-rank warm-up steps (5,000 vs. 200). Against GaLore (Table 4), SwitchLoRA achieves lower perplexity across multiple settings (e.g., rank=32: 25.26 vs. 34.09). The comparison at different ranks, model sizes, and sequence lengths provides evidence the advantage is systematic.

- **The method is well-motivated and conceptually clean.** The insight — that LoRA's rank limitation during pre-training stems from fixed subspaces, and that smooth low-dimensional swapping avoids the optimizer state disruption that forces ReLoRA/GaLore to use long intervals — is clearly articulated. The algorithmic design (Algorithm 1 and 2) is concise.

- **GLUE evaluation goes beyond perplexity alone.** Most prior low-rank pre-training papers (ReLoRA, GaLore) evaluate only perplexity. SwitchLoRA provides downstream fine-tuning results on 5 GLUE tasks for both 350M and 1.3B models, giving a more complete picture of learned representation quality.

## Weaknesses

### Fatal
None.

### Major

- **No ablation studies of any core design choice.** The method introduces several interdependent mechanisms: switching frequency schedule (exponential decay), initial interval (1/40), decay rate θ, freeze duration (N=5), candidate selection strategy (random/sequential), candidate pool size (min(m,n)), and counterpart optimizer reset. **None of these are ablated.** The paper's central claim — that higher update frequency (1/40 vs. ReLoRA's 1/5000) drives the improvement — is never tested by, e.g., running SwitchLoRA at a lower frequency like 1/5000. Without such controls, the contribution of individual components is unknown. This is the most significant gap in the experimental evaluation.

- **GLUE fine-tuning results are mixed and not adequately discussed.** For the 1.3B model (Table 6), SwitchLoRA pre-training yields roughly +1% average improvement — the paper's headline claim. But for the **350M model (Table 5)**, SwitchLoRA pre-training underperforms full-rank pre-training on 4 of 5 tasks, with CoLA dropping catastrophically from **42.95 to 23.13** (a ~46% relative loss). The paper acknowledges this in passing ("except for the CoLA task") but does not discuss why the 350M model fails to transfer while the 1.3B model succeeds. This raises questions about whether the method is reliably beneficial or only works at certain scales/configurations. The 1.3B results are genuinely promising, but the 350M results are concerning and need explanation.

- **Incomplete method specification: how candidate vectors receive training signal is implicit.** The paper defines candidate pools $\mathcal{C}(\mathbf{B})$ and $\mathcal{C}(\mathbf{A}^T)$ and the swap mechanism (Algorithm 1), but it never explicitly states that candidates are trained *only when they occupy active positions in $\mathbf{B}$ or $\mathbf{A}$*. A reader unfamiliar with the swap semantics must infer this from the swap operation (line 112 of Algorithm 1: the candidate becomes the active vector, and the active vector becomes a candidate). The paper should state this explicitly. While the mechanism is reconstructable, the lack of clear prose is a reproducibility concern.

- **Placeholder text left in the manuscript.** Line 364 reads: "SwitchLoRA outperforms GaLore by [insert performance difference], and outperforms the full-rank model by [insert performance difference]." This indicates the paper was not finalized before submission and undermines confidence in the thoroughness of the evaluation.

### Minor

- **Learning rate differs substantially between methods (full-rank: 0.001, LoRA: 0.01, SwitchLoRA: 0.02).** The paper states these were selected from the same search grid, which is a reasonable tuning protocol. However, the 20× gap between full-rank (0.001) and SwitchLoRA (0.02) means the claim of "surpassing full-rank" rests partly on hyperparameter choices. A learning-rate sweep for the full-rank baseline at higher rates (0.01, 0.02) would strengthen the claim. The paper's own statement that the "optimal learning rate remains consistent across different model sizes for all methods" while reporting different rates for each method is confusingly worded.

- **LoRA-only baseline at higher ranks is missing for the 1.3B model.** Table 3 reports SwitchLoRA rank=256 and rank=512 for 1.3B but no LoRA-only row at either rank. Given that LoRA rank=128 performs very poorly on smaller models (perplexity 31.87 on 350M vs. 18.72 full-rank), it is reasonable to assume LoRA alone would not match SwitchLoRA. But the direct comparison at the same rank on the largest model would cleanly demonstrate the benefit of switching.

- **The rank claim ("ensures updated parameters are full-rank") overstates instantaneous capability.** The paper correctly argues that over time, swapping through $\min(m,n)$ distinct candidate vectors allows the cumulative update to span a full-rank space. However, the phrase "ensures updated parameters are full-rank" (line 93) could be read as claiming the adapter itself is always full-rank, which is not true (it always has rank ≤ r at any single step). The text is clarified by referencing ReLoRA/DeltaLoRA, but the phrasing is imprecise.

### Trivial
- The 130M model uses sequence length 256 while larger models use 512 (Table 1). This difference is not explained; presumably it is due to GPU memory constraints given the larger per-GPU batch size (150 vs. 72/16), but stating this explicitly would help.

## Nice-to-Haves
- An effective-rank measurement over time (via SVD of $\sum \Delta \mathbf{W}$) would directly verify the claim that SwitchLoRA accumulates a higher-rank update than standard LoRA.
- Reporting which fraction of candidate vectors are actually used over the full training run would validate whether the pool size $\min(m,n)$ is necessary or whether a smaller pool suffices.

## Removed Points

The following points from the reviews were evaluated against the paper and removed for the stated reasons:

1. **"Candidate vectors are never updated after initialization"** — Removed because this misunderstands the swap mechanism. Algorithm 1 swaps candidate vectors into active positions (line 112), where they receive gradients during subsequent training steps. When swapped out, they carry learned information back to the pool. The method is underspecified in prose but the algorithm is clear.

2. **"Figure 3 caption mentions 1.3B but data is missing"** — Removed because it is factually wrong. The figure file paths confirm all three panels are present: llama250m, llama350m, and llama1b (line 277). The 1.3B data is included.

3. **"Paper does not state what rank GaLore uses"** — Removed because Table 4 explicitly includes columns "Rank=128" and "Rank=32" that report both methods at these ranks.

4. **"The rank argument conflates current rank with cumulative rank"** — Weakened to Minor. The paper's claim (line 93) is about the set of vectors used over time, not instantaneous rank. The phrasing is imprecise but the intended meaning is clear from context and the cited references.

5. **"The initialization formulas appear ad-hoc / suspicious"** — Removed. The formulas are derived from Xavier/Kaiming initialization as stated, and no formal error in the math was verifiable from the paper text alone. This is a technical judgment call that would require domain expertise beyond a meta-review to confirm.

6. **"Criticism that GLUE 1.3B average is not computed"** — Removed. The paper states the average is "approximately 1%," which is verifiable from the table: per-task differences sum to roughly +1.04 points on average. The paper could be more precise, but the claim is not unsupported.

7. **"Table 2 omits full-rank for 1.3B"** — Removed. Table 2 is explicitly for 130M/250M/350M models. Table 3 separately reports the 1.3B results including full-rank. This is a standard organization choice, not an omission.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a perspective on SwitchLoRA that the paper itself misses. The key tension — that the 350M downstream results contradict the 1.3B downstream results — is present in the paper's data but not adequately discussed by the paper or by the reviewers in a way that generates new insight beyond what the numbers show.

## Suggestions

1. **Add ablation experiments.** At minimum, ablate: (a) switching frequency — run with fixed frequency 1/5000 (matching ReLoRA) to isolate the benefit of high-frequency switching; (b) freeze duration N — test N=0, N=5, N=20; (c) candidate selection — random vs. sequential vs. norm-based. This is the single most important revision.

2. **Explain the 350M GLUE failure.** Why does CoLA drop 46%? Is this a fluke due to high variance (the standard deviation is ±15), or a systematic problem? Addressing this directly would strengthen the paper's credibility.

3. **Clarify candidate training in prose.** Add a sentence explicitly stating that candidate vectors receive gradients only when occupying active positions in B or A, and describe what happens to optimizer states when vectors transition between the active set and the candidate pool.

4. **Remove the placeholder text.** This is a trivial fix but creates a poor impression; it should have been caught before submission.

5. **Include a rank-sweep for LoRA on the 1.3B model** to directly compare SwitchLoRA and vanilla LoRA at matching ranks (256 and 512) on the largest scale.

## Score and Decision

The paper presents a genuinely novel idea with promising results on the 1.3B model — beating full-rank perplexity is a non-trivial achievement. However, the evaluation is substantially incomplete: the complete absence of ablation studies makes it impossible to attribute the improvement to any specific component, and the mixed downstream results on the 350M model are not adequately explained. Combined with the placeholder text and underspecified algorithm details, these issues collectively prevent the paper from making a convincing case in its current form. The core idea merits further development, but the evidence presented is insufficient for acceptance.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>