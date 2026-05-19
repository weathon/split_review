- Decision: Accept
- Avg Score: 6.25
- Scores: 8, 3, 8, 6
Now I have all the information I need. Let me write the consolidated review.

## Summary

This paper introduces SRPO, a method for offline RL that uses a pretrained diffusion behavior model to compute a score-based regularization term in the gradient of a deterministic policy, completely avoiding iterative diffusion sampling at both training time and evaluation. The key insight is that the gradient of the reverse-KL behavior regularization term reduces to the score function of the behavior distribution, which can be estimated by a pretrained diffusion model without generating any action samples. Empirically, SRPO achieves competitive performance on D4RL benchmarks (87.1 average on locomotion, 73.6 on AntMaze) while being 25–1000× faster in action sampling than prior diffusion-based methods and using only 0.01%–0.25% of their computational FLOPs.

## Strengths

- **Drastic inference speedup without sacrificing core performance**: SRPO achieves 25–1000× faster action sampling than leading diffusion-based methods (Diffusion-QL, IDQL, QGPO) while matching or exceeding their D4RL scores on several tasks. This is supported by Figure 1 (performance vs. computation scatter plot), Figure 6 (training/inference time bar charts), and the explicit numbers in Section 5.2: "computational FLOPS amount to only 0.25% to 0.01% of other methods." This is a genuine, practically important contribution — existing diffusion-based offline RL methods are indeed hamstrung by slow sampling.

- **Novel gradient-level regularization that avoids diffusion sampling entirely**: The paper derives (Eq. 7) that the gradient of the reverse-KL behavior-regularized objective reduces to the score function of the behavior distribution, which a pretrained diffusion model can approximate via its noise prediction network. This insight — replacing sample-based KL estimation with score-based gradient regularization — enables the efficiency gains. The derivation is sound and clearly presented in Section 3.

- **Competitive or state-of-the-art results on locomotion benchmarks**: Table 1 reports a locomotion average of 87.1, exceeding IQL (76.9), TD3+BC (75.3), and IDQL (82.1), and competitive with Diffusion-QL (88.0) and QGPO (86.6). SRPO achieves the highest scores on HalfCheetah Medium (60.4 vs. 54.1 for QGPO) and Walker2d Medium-Expert (114.0 vs. 112.7 for IDQL). All of this is achieved with a simple deterministic Gaussian policy at inference.

- **Informative ablation studies**: Figure 5 systematically ablates the weighting function ω(t) and the baseline subtraction (ε). The experiments show that ensembling over diffusion times is beneficial, that ω(t)=σ² is a reasonable default, and that subtracting the noise baseline consistently improves performance. The paper also honestly reports that AntMaze tasks are sensitive to ω(t) while locomotion tasks are not.

- **Clear motivation and visualizations**: Figures 2 and 3 provide intuitive 2D bandit illustrations comparing forward-KL vs. reverse-KL policy extraction and demonstrating SRPO's mode-seeking behavior. Figure 4 shows stable training curves across diverse tasks.

## Weaknesses

### Fatal
None.

### Major

- **The surrogate objective (Eq. 8) is a heuristic whose bias is not well-characterized.** The paper replaces the original KL divergence with a weighted ensemble of KL divergences at different diffusion times. While the paper acknowledges that this biases the objective and shows in the ablation that the choice of ω(t) substantially affects results — particularly on AntMaze, where SRPO (73.6) underperforms IDQL (79.1) and QGPO (78.3) — it provides no theoretical analysis of the nature, magnitude, or conditions under which this bias harms or helps performance. The claim that ensembling "might yield a smoother and more robust gradient landscape" is speculative. This does not invalidate the contribution (the algorithm demonstrably works), but it limits conceptual understanding and makes it harder to predict when SRPO will succeed or fail. The authors provide ablation studies but no analysis of why the sensitivity arises, what the surrogate actually optimizes, or how far the resulting policy may be from the true optimal policy of Eq. 5.

### Minor

- **The "state-of-the-art performance" claim in the abstract is overly broad.** The abstract states SRPO maintains "state-of-the-art performance" on D4RL tasks, but the AntMaze average (73.6) is clearly below QGPO (78.3) and IDQL (79.1). This claim is accurate if restricted to locomotion (where SRPO averages 87.1 vs. Diffusion-QL's 88.0 and QGPO's 86.6), but should be qualified to acknowledge the AntMaze gap. The paper's own body text (Section 5.1) is more measured, saying SRPO "comes close to matching the benchmarks set by other state-of-the-art diffusion-based methods."

- **No discussion of limitations.** The conclusion (Section 6) summarizes contributions but does not mention any limitations. The heuristic nature of the surrogate objective, the sensitivity on AntMaze, and the dependence on a pretrained diffusion model are all limitations that should be acknowledged.

- **No empirical comparison with Efficient Diffusion RL.** The paper cites Efficient Diffusion RL (efficientdiffusionrl) in the related work as a method that reduces sampling steps but notes it does not "entirely eliminate the need for iterative sampling." A direct comparison on both performance and speed would strengthen the claim that SRPO is computationally preferable.

### Trivial

- The "proposition" environment numbering appears reset in the PDF extraction (lines 339, 347). This is a LaTeX formatting artifact.

## Nice-to-Haves

- Provide wall-clock milliseconds per action in a table alongside the FLOP percentages (Figure 6), to make the efficiency advantage more concrete for practitioners.
- A brief conceptual justification for why DreamFusion-style ensembling and baseline subtraction techniques are appropriate for RL regularization (currently stated but not motivated).
- A qualitative analysis of AntMaze failure cases (e.g., visualizing the policy's action distribution on a simple maze) to diagnose whether the score regularization becomes too conservative in sparse-reward settings.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"The connection to DreamFusion is under-motivated"** — The paper adequately discusses the connection in Sections 4 (line 351) and the related work (Section 5). The borrowing is straightforward and the paper explains the analogy clearly enough.
- **"Proposition numbering is broken"** — This is a LaTeX formatting artifact in the PDF extraction, not a content issue in the original submission.
- **"No formal bound on the bias"** — This is a restatement of the major weakness above, not a separate point. The reviewer's framing as "fatal" is overblown; the paper acknowledges the bias empirically.
- **Strengths about "addressing an important problem" or "the problem is well-motivated"** — These are generic and not specific to this paper's contribution.
- **Speculative concerns about whether the weighting function choice "coincidentally" works** — The ablation study addresses this directly, showing ω(t)=σ² is a robust default across tasks.

## Novel Insights

None beyond the paper's own contributions. The key synthesis from the reviews is that the paper's main weakness — the heuristic surrogate objective — is also the source of its strength: ensembling over diffusion times provides a smoother gradient signal that empirically works well, but the lack of theoretical characterization limits the paper's depth. This tension between practical efficacy and theoretical understanding is a common pattern in applied RL papers that borrow techniques from adjacent fields (here, text-to-3D generation).

## Suggestions

- **Qualify the SOTA claim**: Replace "maintaining state-of-the-art performance" in the abstract with a more precise statement, e.g., "achieving competitive performance on D4RL locomotion tasks (87.1 average) and strong results on AntMaze."
- **Add a limitations paragraph to the conclusion** that discusses (1) the heuristic nature of the surrogate objective, (2) the sensitivity on AntMaze, and (3) the reliance on a pretrained diffusion model.
- **Provide a brief theoretical discussion** of the surrogate objective — even a simple bound or a variational interpretation would significantly strengthen the paper.
- **Include Efficient Diffusion RL in the comparison** if feasible, or at minimum discuss why a direct comparison was not possible.
- **Add wall-clock inference time per action** in a small table to complement Figure 6.
