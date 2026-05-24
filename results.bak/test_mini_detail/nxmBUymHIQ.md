Now I have all the information I need. Let me construct the final consolidated review.

## Summary

The paper proposes LoLoRA, a hybrid fine-tuning method that replaces gradient-based backpropagation through LoRA's A matrix with local, unsupervised Hebbian PCA (HPCA) updates computed during the forward pass. This eliminates the need to store input activations for A during backpropagation, reducing memory. The authors provide a theoretical analysis (Theorem 4.4) showing that optimal A aligns with the principal components of the input covariance, and they compare LoLoRA against LoRA, LoRA-FA, and EVA-initialized variants across GLUE, math reasoning (GSM8K), and multimodal (LLaVA) tasks.

## Strengths

- **Theoretical characterization of optimal frozen A (Theorem 4.4):** The paper proves that under random linear regression assumptions, any optimal A must span the top r eigenvectors of the input covariance matrix. This is a clean mathematical result that grounds the choice of PCA-based methods for initializing A and is the paper's most solid contribution. The proof is sketched in Section 4 with details deferred to the appendix.

- **Thorough ablation study of local update rules (Table 6):** The paper compares HPCA, AE, SoftHebb, and variants across ranks 2, 4, 8 on TinyLlama/Alpaca. This convincingly shows that HPCA-based rules converge to the right subspace (perplexity 2.535–2.557 vs. 2.521–2.537 for full LoRA), while SoftHebb performs substantially worse (2.572–2.574). This is a useful empirical contribution for practitioners choosing local learning rules.

- **Evaluation across diverse model families and tasks:** The method is tested on RoBERTa-large (GLUE NLU), LLaMA-3.1-8B (math reasoning), and LLaVA-v1.5-7B (multimodal), demonstrating that the local-update approach works across architectures and modalities.

## Weaknesses

### Major

- **LoLoRA does not demonstrate a clear advantage over the simpler LoRA-FA (EVA) baseline.** The paper's central claim is that LoLoRA "mitigates the trade-off between memory and performance." However, across all three experimental setups, LoLoRA HPCA does not consistently outperform LoRA-FA with EVA initialization — a baseline that achieves the same memory savings with no online updates:
  - **GLUE (Tables 1–2):** LoLoRA HPCA is worse than LoRA-FA (uniform) on 5 of 8 tasks (CoLA −1.6, RTE −1.8, MNLI −0.3, QQP −0.2, SST-2 −0.3). Against LoRA-FA (EVA), LoLoRA is mixed but the pattern is not one of systematic improvement.
  - **Math reasoning (Table 3):** LoLoRA HPCA (82.9%) and LoRA-FA (EVA) (82.9%) are identical. Both are within 1σ of LoRA-FA uniform (82.6%) and standard LoRA (82.1%).
  - **LLaVA (Table 4):** LoLoRA HPCA (perplexity 2.93) is between LoRA-FA uniform (2.97) and LoRA-FA EVA (2.92), and worse than standard LoRA (2.90).
  - The memory savings over LoRA (26 GB vs. 30 GB in Table 3) are identical to LoRA-FA's, and in the LLaVA setting the savings are only 0.5 GB (~2%).

  The method introduces extra optimizer state for the local updates (line `Opt_loc.accumulate(A, g_A^loc) + Opt_loc.step(A)` in Algorithm 1), which LoRA-FA does not have. The paper acknowledges this but never quantifies the overhead. Given that the simpler LoRA-FA (EVA) matches or exceeds LoLoRA on almost every metric, it is unclear what advantage the online HPCA updates provide.

- **The theoretical analysis does not motivate the online updates — it motivates EVA initialization.** Theorem 4.4 proves that under strong assumptions (i.i.d. Gaussian ΔW₀, isolated submodule, stationary input distribution), any matrix A whose row space spans the top r eigenvectors of the input covariance is optimal. As the paper's own Table 5 shows, LoRA-FA with a fixed EVA initialization already satisfies this condition. The theory therefore justifies the EVA initialization (already known from Paischer et al., 2024), not the need for online HPCA updates during fine-tuning. The paper conflates two distinct claims: (a) PCA of inputs is a good basis for A (supported by theory), and (b) HPCA updates during training improve over a fixed PCA basis (not supported by the theory, and the experiments show no consistent improvement).

- **The conclusion overstates the results.** The paper claims "Our experiments showed that HPCA consistently outperforms standard LoRA-FA in two out of three experimental setups." On GLUE, LoLoRA is worse than LoRA-FA (uniform) on most tasks. On math reasoning, it ties with LoRA-FA (EVA). On LLaVA, it is better than LoRA-FA (uniform) but worse than LoRA-FA (EVA). At best this is 0.5 out of 3 setups, not 2/3. The claim of "consistently outperforming" is not supported by the evidence presented.

### Minor

- **The local optimizer (Opt_loc) is underspecified.** Algorithm 1 uses `Opt_loc` for the local HPCA updates, but the paper states only that the general training settings use AdamW. It does not clarify whether Opt_loc is also AdamW, SGD, or something else. If it is Adam (with two momentum buffers), the memory for optimizing A could significantly cut into the claimed savings. This is a reproducibility concern.

- **The claim of practical advantage over EVA (no separate PCA pre-pass) is asserted but not measured.** The paper says "Online methods have the advantage of not requiring a separate incremental PCA pass before training" (Section 5.4), but never measures the time or memory cost of the EVA pre-pass. Without that measurement, the claimed advantage is speculative.

- **The "best checkpoint" reporting in Table 3 inflates the numbers.** The paper reports the best result among checkpoints every 0.2 epoch rather than the final model. While this is a known practice, the differences between methods (0.821–0.829) are within twice the standard deviation (0.004–0.005), meaning no statistical claim can be made.

### Trivial

None.

## Nice-to-Haves

- Directly comparing LoLoRA HPCA vs. LoRA-FA (EVA) with total training time including any EVA pre-pass would strengthen the practical motivation. The paper's strongest framing would be as an online alternative to EVA that avoids pre-processing, but this requires measuring the pre-pass cost.
- Specifying the optimizer for the local updates and reporting total memory including its state would make the memory comparison honest.

## Removed Points

These points were raised by the reviewers but are not included as weaknesses in the main review for the reasons stated:

- **Criticism that LoRA-FA (EVA) was omitted from the math reasoning setting (Table 3):** This is factually incorrect — LoRA-FA (EVA) is present in Table 3 with accuracy 0.829. The critic's point that EVA and LoLoRA achieve identical performance is valid, but the claim of omission is wrong. → **Removed.**

- **Criticism that the memory advantage is "not unique to LoLoRA":** While true that LoRA-FA already saves the same activation memory, the paper positions LoLoRA as improving upon LoRA-FA by adapting A online, not as a fundamentally different memory-saving approach. The relevant question is whether the online updates add value, which is addressed in the Major weaknesses above. → **Subsumed under the first Major weakness.**

- **Criticism about "unfair comparison" favoring LoLoRA by omission:** The reviewer argued that ablations compare LoLoRA variants among themselves rather than against LoRA-FA EVA. However, Tables 5 and 6 can be cross-referenced: LoRA-FA (EVA) at r=2 gives 2.558 (Table 5), while LoLoRA HPCA gives 2.557 (Table 6). The paper does not hide this comparison — it is implicitly available. → **Removed.**

- **Strength about "practical advantage over static EVA initialization":** The Strength Finder claimed this as a strength, but the paper never measures the time or memory cost of the EVA pre-pass. The advantage is asserted, not demonstrated. → **Moved here.**

## Novel Insights

None beyond the paper's own contributions. The key tension identified by the reviewers — that the theory justifies a fixed initialization (EVA) rather than the online updates, and the experiments confirm that the two are equivalent — is a genuine insight that emerged from cross-referencing the paper's claims against its evidence.

## Suggestions

- Reframe the contribution honestly: LoLoRA is an online method that achieves performance comparable to LoRA-FA (EVA) without requiring a separate PCA pre-pass. Sharply reduce claims of "outperforming" or "mitigating the trade-off."
- Add a single experiment that measures the time and memory overhead of the EVA pre-pass and compares it to LoLoRA's online HPCA updates. This is the one clean advantage the method could claim.
- Specify the local optimizer and report its memory footprint, including any optimizer states.

## Score and Decision

### Calibration Anchors

**Round 1 (Bracketing) — three bands:**

| Paper | Path | Avg Score | Round | Comparison |
|-------|------|-----------|-------|------------|
| Efficient Low-Rank Diffusion | edx7LTufJF.md | 2.50 | R1 | Weak anchor. Withdrawn paper with a different topic (diffusion). Not directly comparable. |
| HoLoRA | igGeaxOiFM.md | 3.00 | R1 | Weak anchor. LoRA variant with Householder reflectors; withdrawn. LoLoRA is stronger (has experiments, theory). |
| UnoLoRA | 49ti6LOUw5.md | 3.00 | R1 | Weak anchor. Shared LoRA for multitask. LoLoRA has more evaluation. |
| LoRA-FA | RbKThNNFxr.md | 5.33 | R1 | **Most directly relevant anchor.** LoRA-FA freezes A to save memory; was rejected (scores 5,5,6). LoLoRA extends this with local updates and theory, but the core empirical weakness is similar — unclear advantage over simpler baselines. LoLoRA is slightly stronger due to theoretical contribution and ablations, but the empirical gap is comparable. |
| READ | bC50ZOyPQm.md | 5.00 | R1 | Memory-efficient fine-tuning via RNN side network; rejected. READ had a cleaner motivation but narrower evaluation. LoLoRA has broader evaluation and theory. |
| LoRAM | s7DkcgpRxL.md | 6.20 | R1 | Train-pruned-infer-large; accepted poster. Much stronger memory savings (20GB for 70B model). LoLoRA's memory savings are more modest, and the experimental evidence is weaker. |
| HiRA | TwJrTz9cRS.md | 8.00 | R1 | Strong anchor. Hadamard high-rank adaptation; accepted oral. Clear performance improvements over LoRA. Not comparable — LoLoRA does not claim such improvements. |
| LoRA-RITE | VpWki1v2P8.md | 8.67 | R1 | Strong anchor. Transformation-invariant LoRA optimization; accepted oral. Theoretically well-motivated with clear empirical gains. |

**Round 2 (Narrowing) — inside the bracket:**

| Paper | Path | Avg Score | Round | Comparison |
|-------|------|-----------|-------|------------|
| LoRA-FA | RbKThNNFxr.md | 5.33 | R2 | See above. LoLoRA is on par or slightly stronger than this anchor. |
| DeLoRA | X1U74IwuxG.md | 5.25 | R2 | Accepted poster (scores 6,3,6,6). Decoupling angles/strength in LoRA. Incremental but well-presented with sufficient experiments. LoLoRA has a stronger theoretical contribution but weaker empirical evidence. Slightly below this anchor. |
| FLoRA | OALIb8oNfl.md | 5.75 | R2 | Accepted poster (scores 5,6,6,6). Structural integrity in PEFT. Stronger empirical results. LoLoRA is below this anchor. |
| Maintaining Structural Integrity | OALIb8oNfl.md | 5.75 | R2 | Same as FLoRA. |

**Round 1 bracket:** Between 4.0 and 6.0.

**Narrowing:** The most relevant anchor is the LoRA-FA paper (5.33, rejected). LoLoRA has a stronger theoretical component and more thorough ablations, but suffers from the same core weakness: the claimed advantage over simpler baselines is not convincingly demonstrated. Compared to accepted papers (DeLoRA at 5.25, FLoRA at 5.75), LoLoRA's empirical evidence is weaker. The paper's theoretical contribution is real but does not directly support the online method, and the experimental results show parity with a simpler baseline rather than improvement.

**Final score:** 5.0 — marginally below the acceptance threshold.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>