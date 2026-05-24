Now I have all the information I need. Let me synthesize the final review.

---

## Summary

LoLoRA proposes a hybrid fine-tuning method where LoRA adapter matrix A is updated via gradient-free local learning rules (Hebbian PCA or autoencoder loss) during the forward pass, while matrix B is trained via standard backpropagation. This avoids storing activations for A (matching LoRA-FA's memory savings) while allowing A to adapt to input distribution shifts. The paper provides a theoretical result (Theorem 4.4) showing that under a random regression model, the optimal A initialization spans the principal subspace of the input covariance matrix, which grounds both the EVA initialization method and the proposed HPCA local updates.

## Strengths

- **Genuine theoretical contribution (Theorem 4.4):** The proof that, under a random-target assumption, the optimal initialization for frozen A is any nonsingular transform of the top-r eigenvectors of the input covariance matrix is mathematically sound and provides a principled justification for PCA-based initialization schemes. This directly connects to and theoretically grounds the empirical findings of the EVA method (Paischer et al., 2024).

- **Multi-setting experimental evaluation:** The paper evaluates across natural language understanding (GLUE with RoBERTa-large), mathematical reasoning (GSM8K with LLaMA-3.1-8B), multimodal instruction tuning (LLaVA-v1.5-7B), and includes ablation studies on initialization and local update variants (TinyLlama-1.1B on Alpaca). This breadth is appropriate for establishing the method's general behavior.

- **Clean ablation of local update rules (Table 6):** The comparison of HPCA, HPCA variants, AE, and SoftHebb on TinyLlama confirms the theoretical prediction that any rule converging to the principal subspace performs similarly, with HPCA and AE being the practical choices.

## Weaknesses

### Fatal

None.

### Major

- **The core empirical claim is not supported: LoLoRA does not consistently improve over LoRA-FA.** This is the central problem. On GLUE (Tables 1–2), LoRA-FA with uniform initialization matches or exceeds LoLoRA HPCA on five of eight tasks; where LoLoRA wins, margins are negligible (e.g., QNLI 94.7 vs. 94.6). On GSM8K (Table 3), LoLoRA HPCA achieves 0.829 — exactly tied with LoRA-FA (EVA) and only 0.003 above LoRA-FA (uniform). On LLaVA (Table 4), LoLoRA HPCA's perplexity of 2.93 sits between LoRA-FA uniform (2.97) and LoRA-FA EVA (2.92). There is no experimental setting where LoLoRA unambiguously outperforms the best LoRA-FA variant. Since LoRA-FA is strictly simpler (no local optimizer, no local learning rule computations, no additional hyperparameters), the paper has not demonstrated that LoLoRA's added complexity is justified. The abstract's claim of "mitigating the trade-off" is therefore overstated given the evidence.

### Minor

- **The memory-savings framing, while not misleading, could be more precise.** The abstract's "further reducing the memory required for fine-tuning" compares against standard LoRA, not LoRA-FA — and the paper is transparent about this in the body text and tables, where LoRA-FA and LoLoRA show identical or near-identical memory (26 vs. 26 GB in Table 3, 23.9 vs. 24.1 GB in Table 4). However, the introduction's narrative could leave a casual reader with the impression that LoLoRA offers additional savings over LoRA-FA when it does not. The small 0.2 GB overhead from LoLoRA's local optimizer state (Opt_loc in Algorithm 1) is acknowledged in the conclusion but would benefit from explicit discussion earlier.

- **The theory-practice gap limits the impact of the theoretical analysis.** Theorem 4.4 assumes i.i.d. Gaussian ΔW₀ (Assumption 4.1) and a fixed input covariance Σ_zz — conditions far removed from real fine-tuning where target weight changes are highly structured and input distributions evolve as the model trains. The paper acknowledges this limitation in the conclusion ("each submodule isolated with stationary targets, which is not strictly the case in multilayer architecture"), but the disconnect is visible in the data: the theoretically optimal EVA initialization underperforms uniform random freezing on several GLUE tasks (e.g., CoLA 64.7 vs. 67.9), suggesting the theory's assumptions do not reliably predict practical outcomes.

- **The paper's own summary overstates the results.** The conclusion states "HPCA consistently outperforms standard LoRA-FA in two out of three experimental setups." On GSM8K, LoLoRA ties with the best LoRA-FA variant and beats the uniform variant by only 0.003 — not a genuine outperformance. On LLaVA, LoLoRA beats LoRA-FA uniform but loses to LoRA-FA EVA. On GLUE, LoLoRA is arguably worse than LoRA-FA uniform. The claim of "two out of three" does not accurately reflect the flat empirical landscape.

### Trivial

- The distinction between "HPCA" and "HPCA (svd first)" in Table 6 is initially confusing without careful reading of the local rules description.
- Some inconsistency in reporting: the GLUE summary says LoLoRA achieves "slightly better results than LoRA-FA (EVA)" but the tables show LoLoRA beats LoRA-FA (EVA) on only 3 of 8 tasks.

## Nice-to-Haves

- A scenario where LoRA-FA (even with good initialization) demonstrably fails and LoLoRA recovers would substantially strengthen the contribution — e.g., tasks with significant input distribution shift during training, or longer training regimes beyond one epoch.
- A rigorous wall-clock time and throughput comparison accounting for the local optimizer overhead would make the practical trade-off clearer.
- An analysis of how rank r affects the memory/performance trade-off for LoLoRA vs. LoRA-FA, since larger r increases A's optimizer state size.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"The introduction and abstract give the impression that LoLoRA offers further memory reduction beyond LoRA-FA, but it does not"** — REMOVED. The paper explicitly states memory savings come from not storing A's activations, which LoRA-FA also does. The abstract's "further reducing" is clearly relative to standard LoRA. The tables report memory for all methods transparently.

- **"The paper does not quantify [optimizer state] or include it in the reported memory figures"** — REMOVED. Tables 3–4 report peak allocated GPU memory, which inherently includes optimizer states. The 0–0.2 GB difference between LoRA-FA and LoLoRA is visible and the overhead is acknowledged in the conclusion.

- **"A comparison with other activation-memory-reduction techniques (e.g., gradient checkpointing, reversible layers) is absent"** — REMOVED. This is scope creep; the paper's contribution is within the LoRA family and doesn't need to benchmark against orthogonal memory-reduction approaches.

- **"The theoretical section assumes full-rank Σ_zz and no discussion of regularisation or finite-batch effects"** — REMOVED. The theory section is already appropriately scoped; demanding treatment of finite-batch effects or regularization is beyond what's reasonable for a theoretical motivation section.

- **From Strength Finder: "LoLoRA HPCA achieves 82.9% accuracy on GSM8K while using only 26 GB extra GPU memory... directly supports the claim"** — DEMOTED. This is factually true but doesn't distinguish LoLoRA from LoRA-FA (EVA), which achieves the same accuracy and memory. Cannot serve as evidence of LoLoRA's advantage.

- **From Strength Finder: "Rigorous comparison across multiple tasks... LoLoRA consistently improves over the naive frozen-A baseline"** — PARTIALLY REMOVED. The multi-task comparison is genuine, but "consistently improves" is not supported by the data.

## Novel Insights

None beyond the paper's own contributions. The central tension — that local Hebbian updates are a clever idea that the experiments fail to validate — was surfaced by multiple reviewing perspectives but was already visible in the paper's own data.

## Suggestions

- The authors should identify or construct at least one setting where LoRA-FA (with EVA initialization) measurably fails and LoLoRA recovers the gap. Without this, the paper cannot substantiate its core claim even with a rebuttal.
- Shorten the theoretical section and prominently state its limitations earlier; the current positioning gives the theory more weight than the experiments can support.
- Recalibrate the claims throughout (abstract, conclusion, section summaries) to reflect that LoLoRA is a competitive alternative to LoRA-FA — not a clear improvement over it. The honest framing would be: "LoLoRA matches LoRA-FA's memory savings while achieving comparable performance, showing that gradient-free local updates can replace frozen-A without loss."

## Score and Decision

**Round 1 bracketing:** Queried weak (≤3.5), middle (3.5–7.5), and strong (≥7.5) anchors on LoRA memory-efficient fine-tuning topics. The paper sits clearly in the middle band — below strong anchors like HiRA (8.00) and Cut Your Losses (8.50), and above weak anchors like HoLoRA (3.00) and L-MSA (3.00). Initial bracket: 4.0–6.0.

**Round 2 narrowing:** Retrieved anchors inside 3.5–6.5 on LoRA variants and PEFT initialization. Key comparisons:
- **LoRA-FA (5.33, Reject):** The original frozen-A paper. LoLoRA adds theoretical grounding and local updates but shows comparable empirical weakness. LoLoRA is roughly at parity — slightly more novel in concept but similarly unable to demonstrate clear practical advantage.
- **EVA (4.75, Reject):** Data-driven SVD initialization. LoLoRA is strictly better: it provides the theoretical justification EVA lacked (Theorem 4.4) and goes beyond static initialization to dynamic updates.
- **ReLoRA (5.75, Accept):** Low-rank updates for pre-training. Shows clearer empirical benefits (5.5 GB savings, 9–40% speedup) at scale. LoLoRA is weaker empirically.
- **MoRA (4.75, Reject):** High-rank LoRA variant with task-specific improvements. Similar empirical pattern to LoLoRA — gains in some settings but not broadly convincing.

LoLoRA sits between EVA (4.75) and LoRA-FA (5.33), with theoretical contributions exceeding both but empirical validation falling short of what would justify acceptance.

**Final score:** 5.0, reflecting genuine theoretical novelty and reasonable experimental breadth, but ultimately undermined by the failure to demonstrate that the proposed local updates provide a meaningful improvement over the simpler LoRA-FA baseline.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>