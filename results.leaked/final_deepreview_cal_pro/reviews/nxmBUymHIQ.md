Now I have all the information needed. Let me write the consolidated review.

---

## Summary

LoLoRA proposes a hybrid fine-tuning method for LoRA adapters: matrix A is updated during the forward pass via local, unsupervised learning rules (HPCA or autoencoder loss) that converge to the PCA subspace of layer inputs, while matrix B is trained via standard backpropagation. This eliminates the need to store A's activations for the backward pass, reducing peak GPU memory. The paper provides a theoretical result (Theorem 4.4) showing that, under a random regression assumption, the optimal A initialization spans the top r eigenvectors of the input covariance — justifying PCA-based approaches like EVA and the proposed online HPCA updates. Experiments on GLUE, MetaMathQA, and LLaVA demonstrate memory savings (~13%) with competitive performance.

## Strengths

- **Theoretical justification for PCA-based initialization of A**: Theorem 4.4 proves that under random regression assumptions, optimal A matrices are nonsingular transformations of the leading r eigenvectors of the input covariance Σzz. This directly addresses a gap noted by reviewers of the EVA paper (which proposed PCA initialization without theoretical backing). The result provides a principled motivation for both EVA and the local HPCA updates in LoLoRA.

- **Online alternative to preprocessing-based initialization**: Tables 5–6 show that LoLoRA with HPCA updates achieves validation perplexity virtually identical to LoRA-FA with EVA initialization (e.g., r=8: 2.535 vs 2.536), without requiring a separate PCA pass over the dataset before training. This is a practical advantage for streaming or large-scale settings.

- **Verified memory savings with maintained accuracy on math reasoning**: On MetaMathQA → GSM8K Platinum (Table 3), LoLoRA HPCA reduces peak extra GPU memory from 30 GB (standard LoRA) to 26 GB while achieving 0.829 ± 0.004 accuracy, matching the best method and outperforming standard LoRA (0.821).

- **Broad empirical coverage**: The method is evaluated across three distinct settings — NLU (RoBERTa-large on GLUE), mathematical reasoning (LLaMA-3.1-8B on MetaMathQA), and multimodal fine-tuning (LLaVA-v1.5-7B on Visual Instruct 150K) — with consistent experimental methodology and ablations on initialization and local rules (Tables 5–6).

- **Clear algorithmic specification**: Algorithm 1 concisely defines the forward-pass modification, making the method straightforward to implement and reproduce.

## Weaknesses

### Fatal

None. The core claims are reasonably supported by the evidence presented.

### Major

- **Marginal empirical advantage over EVA-initialized frozen A**: The paper's primary motivation is to "mitigate the trade-off" between memory savings and performance that occurs when freezing A. Yet across experiments, LoLoRA HPCA performs comparably to — but does not clearly outperform — LoRA-FA with EVA initialization. On MathQA they tie (0.829); on LLaVA, LoLoRA (2.93 perplexity) is slightly behind LoRA-FA EVA (2.92); the TinyLlama ablations show near-identical perplexity between LoLoRA HPCA and LoRA-FA EVA across all ranks. The main demonstrated advantage over EVA is that LoLoRA is online (no preprocessing), not that it achieves better final performance. The paper would be strengthened by demonstrating a scenario where online adaptation of A provides a clear performance benefit over any static initialization — for example, under distribution shift or in streaming settings.

- **Theory relies on simplifying assumptions not validated for real fine-tuning**: Theorem 4.4 assumes the optimal weight change ΔW₀ has i.i.d. Gaussian entries (Assumption 4.1). In actual fine-tuning, ΔW is driven by the task-specific loss, not random noise. The paper acknowledges this limitation in the conclusion but does not empirically investigate whether the PCA subspace actually aligns with the A matrices learned by standard end-to-end LoRA — a natural sanity check that would strengthen the theory-practice connection.

### Minor

- **GLUE results do not favor LoLoRA**: On GLUE (Tables 1–2), LoLoRA HPCA underperforms LoRA-FA with uniform initialization on 5 of 8 tasks (CoLA, RTE, MNLI, QQP, SST-2), sometimes by meaningful margins. The paper acknowledges that classical LoRA "remains the strongest overall" on GLUE but the result weakens the generality of the approach. Notably, EVA initialization performs particularly poorly on GLUE (e.g., 64.7 on CoLA vs 67.9 for uniform), so LoLoRA does improve over EVA here — but the comparison to the simpler uniform baseline is unfavorable.

- **Memory accounting for local optimizer state is not quantified**: The local optimizer (Opt_loc in Algorithm 1) adds its own state that partially offsets activation memory savings. The paper notes this in the conclusion ("our method introduces a small amount of extra optimizer state") but does not provide a component-by-component memory breakdown to let readers evaluate the net savings relative to LoRA-FA.

- **The conclusion's framing slightly oversells**: The claim that "HPCA consistently outperforms standard LoRA-FA in two out of three experimental setups" is technically accurate when counting GLUE, MathQA, and LLaVA as the three setups (LoLoRA wins on MathQA and LLaVA vs. uniform FA). However, within the GLUE setup, LoLoRA loses on most individual tasks, and against the EVA-initialized baseline the advantage disappears entirely. The phrasing could mislead readers about the strength of the empirical case.

### Trivial

None.

## Nice-to-Haves

- A direct empirical check of whether A's row space in standard end-to-end LoRA aligns with the top PCA directions of activations would bridge the theory and practice more convincingly.
- An experiment in a setting with distribution shift (continual learning, multi-task, or long fine-tuning runs where initial PCA becomes stale) could demonstrate a clear advantage of online A updates over any static initialization.
- A memory component breakdown (frozen weights, B gradients/optimizer, A local-optimizer state, activations) would make the efficiency claims more transparent.
- GLUE experiments with larger models (e.g., a 7B decoder) where the memory differences are more impactful would strengthen the practical case.

## Removed Points

These points are flagged to be removed, treat them with caution:

1. **"The empirical case for LoLoRA over a well-initialized frozen A is weak… EVA initialization that itself already exploits the principal components"** — The harsh critic's framing incorrectly treats EVA as a uniformly strong baseline. On GLUE, EVA initialization performs *worse* than uniform initialization (CoLA: 64.7 vs 67.9; RTE: 83.6 vs 86.4), and LoLoRA HPCA actually *improves* over EVA on these tasks. The critic's claim that LoLoRA "does not consistently outperform LoRA-FA with a sensible initialization" is misleading because it treats EVA as "sensible" when the data shows it is not. The real story is more nuanced: LoLoRA provides an online alternative that matches or improves upon EVA without needing preprocessing, while EVA itself is not universally beneficial.

2. **"The theoretical analysis rests on an assumption that severs it from the actual fine-tuning problem"** — This overstates the issue. Theoretical analyses in ML routinely use simplifying assumptions to derive insights; the paper explicitly acknowledges the limitation. The appropriate framing is that the theory provides motivation and the empirical results provide validation, not that the theory is "severed" from practice. Moved from fatal to major (weakened).

3. **"The conclusions overstate the results… The claim misrepresents the full set of results"** — The claim "HPCA consistently outperforms standard LoRA-FA in two out of three experimental setups" is factually correct when "standard LoRA-FA" means the uniform-initialized version (which is the standard). On MathQA: 0.829 > 0.826. On LLaVA: 2.93 < 2.97 (lower perplexity is better). On GLUE: LoLoRA underperforms. That is exactly 2/3. The harsh critic's assertion that this is "not supported by the data" is incorrect. However, the claim is narrow (uniform FA only), so this is moved to a minor weakness about framing.

4. **Harsh critic's "section-by-section notes" about missing memory breakdown** — The paper references Appendix D for detailed memory analysis. The appendix is stripped in the parser output, so we cannot verify what it contains. This is a parser issue, not an author error.

5. **"The GLUE experiments could include runs with larger models"** — This is scope creep. The paper already evaluates on models up to 8B parameters (LLaMA-3.1-8B, LLaVA-7B). Moved to nice-to-have.

6. **Strength Finder's "comprehensive ablation of initializations and local rules"** — Valid and kept as supporting evidence.

7. **Strength Finder's "clear, self-contained algorithmic description"** — Valid and kept.

## Novel Insights

The paper's key novel insight is the theoretical result (Theorem 4.4) that unifies the asymmetry between LoRA matrices A and B: under a random regression model, there exists a well-characterized set of optimal initializations for A (spanning the top PCA subspace of inputs) but no similarly privileged initialization for B (any full-rank B is equally optimal). This formalizes why freezing A with a good initialization is more viable than freezing B, and why input-driven local updates that converge to the PCA subspace can substitute for gradient-based training of A. The paper also demonstrates empirically that online PCA-converging rules (HPCA) achieve this without the preprocessing cost of batch PCA methods like EVA.

## Suggestions

- Add a concrete experiment showing when online A updates matter: a continual learning or multi-task setup where the input distribution shifts, making a static PCA initialization stale. This would demonstrate the unique value of LoLoRA over EVA-initialized LoRA-FA.
- Include a sanity check measuring cosine similarity between A's row space in standard end-to-end LoRA and the top PCA directions of activations, to validate the theory's predictions on real fine-tuning trajectories.
- Provide a table with per-component memory breakdown (frozen weights, activations, B optimizer state, A local optimizer state) for transparency on net savings.

## Score and Decision

**Calibration anchors referenced:**

| Anchor | Avg Score | Round | Comparison to LoLoRA |
|--------|-----------|-------|----------------------|
| EVA (DM6Q45HWSk) | 4.75 | R2 | LoLoRA is stronger — adds the theory EVA lacked and an online method |
| RAC-LoRA (VSK3GykuE) | 5.00 | R2 | Similar theory+method paper; LoLoRA has broader empirical evaluation |
| LoRA-FA (RbKThNNFxr) | 5.33 | R1 | LoLoRA builds on LoRA-FA with theory + local updates; comparable quality |
| ReLoRA (DLJznSp6X3) | 5.75 | R1 | ReLoRA is more ambitious (pre-training scale, larger speedups); LoLoRA is below this |
| RandLoRA (Hn5eoTunHN) | 6.00 | R1 | RandLoRA has clearer empirical gains; LoLoRA is below this |
| ALLoRA (7X65yoKl3Y) | 3.33 | R1 | LoLoRA is clearly stronger than rejected LoRA variants with fundamental issues |
| HoLoRA (igGeaxOiFM) | 3.00 | R1 | LoLoRA is clearly stronger |

**Round 1 bracket**: 4.5 – 6.0
**Round 2 narrowing**: The EVA anchor (4.75) confirms LoLoRA should score above it due to added theory. LoRA-FA (5.33) is the closest comparable — LoLoRA adds theoretical grounding and an online mechanism but has similarly marginal empirical gains. I place LoLoRA at 5.0, slightly below LoRA-FA because LoRA-FA was the first to propose the freeze-A approach and had more comprehensive large-model experiments, while LoLoRA's refinement (local updates) shows thin advantages.

**Originality**: The combination of local Hebbian/PCA updates with backprop-trained LoRA is novel in the LLM fine-tuning context. The theoretical result is a clean formalization of why PCA-based A initialization is optimal.

**Importance**: Memory-efficient fine-tuning is an important practical problem. The paper addresses a real bottleneck (activation memory in LoRA) but the proposed solution offers modest gains over existing approaches.

**Claim support**: The main claims (memory savings, competitive performance, theoretical grounding for PCA initialization) are reasonably supported. The claim of "mitigating the trade-off" is partially supported — LoLoRA matches but doesn't clearly exceed EVA-init frozen A.

**Soundness**: The method is sound; the theory is mathematically correct under stated assumptions; the experiments use standard benchmarks and report variance across seeds. The main gap is the theory-practice connection under the random regression assumption.

**Clarity**: The paper is well-organized with clear algorithmic description, though some experimental details are deferred to the appendix.

**Value to community**: The theoretical result (Theorem 4.4) provides a useful perspective on LoRA adapter asymmetry that may inform future work. The practical method offers a modest but real improvement in the memory-performance trade-off for LoRA fine-tuning.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>