Now I have a thorough understanding of the paper. Let me produce the final consolidated review.

## Summary

This paper proposes DT-Mem, a Decision Transformer augmented with an explicit, content-addressable memory module (inspired by working memory) that stores, retrieves, and updates information via attention mechanisms. The architecture consists of a Transformer module (13M params), a memory module (7M params), and an MLP module. Evaluation on Atari games and Meta-World shows that DT-Mem achieves competitive or superior generalization with fewer total parameters and less training time compared to baselines, and that fine-tuning only the memory module via LoRA enables efficient task adaptation.

## Strengths

- **Parameter efficiency**: DT-Mem with 20M total parameters achieves human-normalized IQM scores (Figure 3) comparable to Multi-game Decision Transformer (MDT) with 200M parameters — a roughly 10× reduction in parameters for similar generalization performance. This directly supports the core claim that explicit memory reduces reliance on model scale.

- **Strong zero-shot generalization on held-out Atari games**: On five games never seen during training (Table 1), DT-Mem outperforms both MDT and RMDT in four out of five games, with 95% confidence intervals reported (e.g., 0.69 vs. 0.56 for RMDT on Alien, 0.62 vs. 0.51 on Ms. Pac-Man). This provides quantitative evidence that the memory module aids generalization to unseen tasks.

- **Parameter-efficient fine-tuning on Meta-World**: On Meta-World ML45 (Table 2), DT-Mem fine-tuning only 147K LoRA parameters outperforms Hyper-Decision Transformer's 2.3M hyper-network parameters in both zero-shot (53.1% vs. 45.4%) and fine-tuned (89.3% vs. 86.3%) settings. This demonstrates that memory-only adaptation is both more parameter-efficient and more effective.

- **Consistent pre-training improvement**: On the 17 Atari games used for pre-training (Figure 6), DT-Mem outperforms MDT in 13/17 games and RMDT in 15/17 games as measured by relative improvement over the best score in the dataset, showing that the memory module helps learning during training, not just at test time.

## Weaknesses

### Fatal
None.

### Major

- **Imprecise and dimensionally ambiguous method description (Section 4, Steps 2–4).** The core memory equations contain unresolved ambiguities that prevent precise understanding and reproduction:
  - The softmax axis for computing the addressing weight **w** (Step 2) and the write strength **β** (Step 3) is never specified. The products **QK^T** and **Q̂K̂^T** involve matrices with mismatched dimensions (memory slots × input positions), and it is unclear how these yield vectors of compatible length.
  - The retrieval equation **E_out = w ⊙ M_t** uses element-wise multiplication between a vector **w** (length N) and a matrix **M_t** (N×d) without specifying broadcasting semantics.
  - The adding vector **ϵ^a = (w ⊙ β) Ŵ^v x** is described as a "vector" but the product of a length-N vector with a d-dimensional vector (Ŵ^v x) is dimensionally underspecified — it must be an outer product (yielding an N×d matrix) to be added to the memory, but the text calls it a "vector" and does not clarify.
  - For a method paper whose central contribution is this memory module, this imprecision is a serious reproducibility concern. The general NTM-inspired idea is understandable, but a reader could not implement the method from the text alone.

- **Confusing and potentially inconsistent loss function notation (Section 4.3).** The return-to-go is defined as **r̂_t = Σ_{t+1}^{t+K} r_t** (line 244), but the loss function (line 289) uses **||r̃_t − r̂_t||²** where **r̃_t** is the predicted reward — so the model predicts the reward but the target is the return-to-go? Meanwhile **||R̃_t − r_t||²** compares the predicted return-to-go (**R̃_t**) to the immediate reward (**r_t**). The notation appears inconsistent and it is unclear what each prediction head actually targets.

- **Training efficiency claims lack necessary controls.** The paper states DT-Mem reduces training time by 4×, 8×, and 32× vs. MDT-13M, MDT-40M, and MDT-200M respectively (Section 5.4). Since DT-Mem (20M) has *more* parameters than MDT-13M, the 4× speedup over a smaller model is counterintuitive. The paper does not clarify whether this speedup comes from fewer training steps to convergence, faster per-step computation, or other factors. Without controlling for step counts, convergence criteria, or implementation optimizations, the efficiency claims are not properly evidenced. (The referenced Table 4 and Figure 7 are in the appendix, but the main-text justification remains insufficient.)

### Minor

- **No ablation isolating the memory module's contribution.** The paper compares DT-Mem (20M = 13M transformer + 7M memory) against MDT-20M (all parameters in the transformer). While controlling for total parameter count is standard, an ablation that removes the memory module from DT-Mem while keeping the transformer backbone would directly isolate the memory's effect and strengthen the causal claim.

- **Meta-World HDT comparison uses cross-paper numbers.** The paper acknowledges it does not have access to the HDT implementation (line 315) and reports HDT results from the original paper. Without re-running under identical conditions (data splits, trajectory lengths, random seeds), this comparison is less reliable than the Atari experiments where baselines were re-trained.

- **Key hyperparameters not reported.** The number of memory slots N, latent dimension d, learning rate, optimizer, batch size, and training schedule are not specified in the main text, hampering reproducibility.

- **No discussion of limitations.** The paper does not discuss potential limitations such as: fixed memory size, the overhead of attention over memory slots at inference time, or whether the approach scales to settings with very different observation or action spaces.

### Trivial

- Typo on line 186: "random matrix $_M$" should be "$M$".
- Missing space on line 384: "DT-Memdemonstrates".
- The use of **∇** in the notation for the position address (line 231) appears to be a formatting artifact.

## Nice-to-Haves

- An ablation of DT-Mem without the memory module (same transformer backbone, 13M params) would cleanly separate the memory contribution from the effect of additional parameters.
- Reporting FLOPs or per-step wall-clock time (rather than total training time) would make the efficiency claims more precise.
- Reporting absolute scores (not just relative improvement) for the 17 pre-training games in Figure 6 would support the pre-training claims more transparently.
- Specifying the softmax axis for all attention-based operations and providing tensor shapes in a table would resolve the method imprecision.

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Claim that the paper reports no significance tests / no confidence intervals.** The paper explicitly reports 95% confidence intervals for Table 1 (line 391). Removed as factually incorrect.
- **Claim that Table 4 and Figure 7 are "missing" and data cannot be verified.** These are in appendix sections stripped by the PDF parser; they exist in the original submission. Removed per parser-artifact rule.
- **Claim that MDT-20M comparison is "unfair" / stacks the deck.** Comparing at equal total parameter count (20M vs. 20M) is standard and defensible. The missing ablation (noted in Minor) is a different concern. Removed as overclaimed.
- **Claim that "state-of-the-art" is unsupported because CQL/IQL are not included.** CQL and IQL are offline RL methods based on dynamic programming, not sequence modeling — demanding comparison is scope creep. Removed.
- **Claim about cherry-picking via game selection.** The paper explicitly states games were selected alphabetically to prevent cherry-picking (line 338-339). Removed as contradicted by the paper text.
- **Strength Finder strengths about generic contributions** (e.g., "addressing an important problem") — dropped as vague and not tied to specific evidence.

## Novel Insights

None beyond the paper's own contributions. The reviewers do not contribute a synthetic insight that goes beyond what the paper itself claims.

## Suggestions

1. **Fix the method equations.** Unambiguously specify all tensor shapes, the softmax axis for every attention operation, and whether operations like **w ⊙ M_t** and **(w ⊙ β) Ŵ^v x** use broadcasting or outer products. A concrete forward-pass example with explicit dimensions would resolve most reproducibility concerns.

2. **Clarify the loss function.** Either rename the variables so that predicted reward is compared to immediate reward and predicted return-to-go is compared to the actual return-to-go, or explain the mismatch if the notation is intentional.

3. **Control the efficiency comparison.** Report per-step training time and number of steps to reach a given loss threshold separately, so readers can distinguish between architectural speed and optimization efficiency.

4. **Add a direct ablation** (DT-Mem without memory, or a DT scaled to the same compute budget) to isolate the memory module's contribution from the mere addition of parameters.

5. **Report hyperparameters** (N, d, learning rate, optimizer, batch size) in the main text.

## Score and Decision

This paper addresses a relevant problem (efficient multi-task decision making) and proposes a plausible architectural modification with promising empirical results — particularly the 10× parameter efficiency gain on Atari and the strong Meta-World results with LoRA fine-tuning. However, the method description contains imprecisions that undermine reproducibility for a contribution that is entirely about a new module, the loss notation is confusing, and the efficiency claims lack necessary controls. The core contributions are real but the presentation is not yet at the standard required for acceptance. A revision that fixes the equations, clarifies the loss, and tightens the experimental controls could make this a strong paper.

**Score**: 5.5

**Decision**: Reject (borderline; major revisions needed)

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>