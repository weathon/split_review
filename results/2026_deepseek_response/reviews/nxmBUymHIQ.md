Now I have all the information I need. Let me write the final review.

## Summary
LoLoRA is a hybrid fine-tuning method that updates the A matrix in LoRA with gradient-free local Hebbian rules (HPCA/AE) during the forward pass, avoiding storage of input activations for backprop through A. The paper also provides a theoretical characterization (Theorem 4.4) showing that under a random regression model, optimal A spans the top-r PCA subspace of the input covariance — formally grounding PCA-based initialization (EVA) and motivating local PCA-converging updates.

## Strengths
1. **Clean theoretical derivation of optimal A (Theorem 4.4)**: The paper proves that under a random regression assumption, the optimal frozen A matrices are nonsingular transformations of the top-r eigenvectors of the input covariance. This is a genuine formal contribution that goes beyond the experimental evidence in prior work like EVA (Paischer et al., 2024), which received criticism for lacking theoretical justification. See Section 4, Theorem 4.4.

2. **Well-designed hybrid training scheme**: Algorithm 1 clearly integrates local Hebbian updates on A (forward pass) with gradient-based B training (backward pass), freeing activations for A without requiring a separate PCA pass. The design is distinct from LoRA-FA (which fully freezes A) and is cleanly presented.

3. **Systematic ablations on initialization and local rules**: Tables 5–6 compare four initializations (Uniform, Orthogonal, PiSSA, EVA) and five local update rules (HPCA variants, AE, SoftHebb) on TinyLlama–Alpaca. The results show that EVA initialization is the strongest for LoRA-FA, and that HPCA/AE converge to similar perplexity without a separate PCA pass. This thorough evaluation is a strength of the paper.

4. **Competitive memory–accuracy tradeoff on mathematical reasoning**: On GSM8K (Table 3), LoLoRA HPCA achieves 0.829 accuracy with 26 GB extra memory, matching the best LoRA-FA variant and outperforming standard LoRA (0.821, 30 GB) while saving 13% peak memory.

## Weaknesses

### Fatal
None.

### Major
1. **LoLoRA does not convincingly outperform well-initialized LoRA-FA.** Across all three experimental settings, LoLoRA HPCA ties or loses to LoRA-FA (EVA):
   - **GLUE** (Tables 1–2): LoLoRA HPCA (66.3–94.7 across tasks) is roughly comparable to LoRA-FA (EVA) (64.7–94.5), and underperforms LoRA-FA (uniform) on 4 of 8 tasks (CoLA, RTE, QQP, SST-2).
   - **GSM8K** (Table 3): Both LoLoRA HPCA and LoRA-FA (EVA) achieve 0.829 — identical.
   - **LLaVA** (Table 4): LoLoRA HPCA perplexity 2.93 vs LoRA-FA (EVA) 2.92 — LoLoRA is slightly worse.
   
   The paper claims LoLoRA "consistently outperforms standard LoRA-FA," but this holds only against *uniform* initialization, and even then the gaps are small and often within 1 standard deviation. Against the stronger EVA-initialized variant — the more meaningful comparison — LoLoRA never clearly wins. The central narrative that local updates mitigate LoRA-FA's "degraded performance" is not borne out by the data.

2. **Memory savings over LoRA-FA are negligible while adding complexity.** Table 4 shows LoLoRA at 24.1 GB vs LoRA-FA at 23.9 GB (0.2 GB difference, <1%). Table 3 shows both at 26 GB. The memory advantage over standard LoRA is already achieved by LoRA-FA alone. LoLoRA adds extra optimizer state for local updates, introduces new hyperparameters (local learning rate, HPCA smoothing factor), and adds tuning cost — with no clear memory or quality benefit over well-initialized frozen-A baselines.

### Minor
1. **Best-of-epoch reporting for math reasoning (Table 3).** The GSM8K results report the best accuracy from checkpoints taken every 0.2 epoch, rather than final-epoch performance. This protocol can inflate results and makes comparisons harder to interpret. The paper should report final-epoch accuracy as the primary metric.

2. **Limited LLaVA evaluation.** The multimodal experiment uses a 20% subset with one epoch of training. While this is transparently described, conclusions about multimodal transferability would be stronger with full-dataset training.

3. **Overstated framing.** The abstract and conclusion claim that LoLoRA "mitigates the trade-off" between memory savings and LoRA-FA's degraded performance. However, on GLUE, LoLoRA underperforms even uniform-initialized LoRA-FA on half the tasks, and the "advantage" in the other two setups rests on tiny gaps against uniform-only LoRA-FA.

4. **Theory primarily supports EVA initialization, not the online-update aspect of LoLoRA.** Theorem 4.4 characterizes the optimal *frozen* A — it explains why PCA-based initialization (EVA) is optimal, but does not address why *online local updates during training* should outperform a one-time PCA initialization. The paper does not test the non-stationarity scenario that would be needed to show adaptive updates add value. The theory is a nice formal anchor for EVA-style initialization, but it does not uniquely motivate LoLoRA's core claim.

### Trivial
None.

## Nice-to-Haves
- An experiment testing whether local updates adapt to non-stationary input distributions (e.g., varying data ordering or curriculum learning).
- Verification (e.g., subspace distance) that the HPCA-learned A during training converges toward the true PCA eigenvectors of the input covariance.
- Sensitivity analysis for the local rule hyperparameters (learning rate, HPCA smoothing factor) in the main paper rather than the appendix.

## Removed Points
These are excluded per the filtering rules:
- "Optimizer Opt_loc is not specified" — Algorithm 1 takes Opt_loc as input; details are in Appendix C (stripped by parser; they exist in the original submission).
- Missing appendix/hyperparameter details, reproducibility nitpicks about implementation — appendix sections exist in the original submission; parser strips them.
- Concerns about unfair comparison when the asymmetry favors the baseline (not the authors' method).
- Pure formatting nitpicks and typos — these are parser artifacts from PDF extraction.
- Generic "evaluation lacks rigor" or "baselines may not be fair" without concrete anchoring in the paper text.
- The EVA paper (Paischer et al., 2024) comparison is retained in the review but the critic's concern that EVA "does not correspond to currently available systems" is removed — the paper cites the EVA paper, so it exists.

## Novel Insights
The Harsh Critic's most incisive observation is that Theorem 4.4 (optimal A = top PCA subspace) is actually stronger evidence *against* LoLoRA than *for* it: if the optimal A is simply the top eigenspace of the stationary input covariance, then a pre-computed PCA (EVA) already achieves this, and online updates add complexity without demonstrated benefit. The paper acknowledges non-stationarity as a limitation but does not test it. This reframing — that the theory supports EVA more fundamentally than LoLoRA — is the key critical insight that the merger surfaces beyond the paper's own narrative.

## Suggestions
1. Either provide evidence that LoLoRA's online adaptation helps under distribution shift, or reframe the contribution as "a method that achieves the benefits of EVA initialization without a separate PCA pass."
2. Report final-epoch GSM8K results alongside or instead of best-of-epoch values.
3. Include an ablation comparing LoLoRA (uniform init) over time against LoRA-FA (EVA) to visualize whether the local updates actually converge toward the EVA-quality subspace.

## Score and Decision

### Calibration Round 1 — Bracketing
I retrieved anchors in three bands on the topic of "LoRA fine-tuning parameter-efficient LLM memory":
- **Weak band** (score < 3.5): Avg 3.0–3.33. Papers like HoLoRA (3.0), UnoLoRA (3.0), ALLoRA (3.33). These papers had clear fatal flaws or very incremental contributions without theoretical grounding. LoLoRA is clearly above this band — it has a genuine theoretical contribution and stronger experiments.
- **Middle band** (3.5 < score < 7.5): LoRA-FA (5.33), LoRAM (6.20), Activations Aren't Cheap (4.25), MoRA (4.75). This is the relevant comparison range.
- **Strong band** (score > 7.5): Avg 8.0. Papers like HiRA (8.0), Context-Parametric Inversion (8.0). LoLoRA is clearly below this band — these papers have much stronger empirical findings and broader impact.

**Round 1 bracket: 4.5 – 5.5**

### Calibration Round 2 — Narrowing
I retrieved additional anchors within and near the bracket:
- **EVA (Explained Variance Adaptation)** (avg 4.75, Reject): Closely related work. Reviewers criticized it for marginal improvements and lack of theoretical justification. LoLoRA is stronger than EVA because it *has* the theoretical justification that EVA lacked. However, LoLoRA shares EVA's problem of marginal empirical improvement. **LoLoRA is moderately stronger than EVA.**
- **LoRA-FA** (avg 5.33, Reject): The most directly relevant baseline. Reviewers found it incremental and questioned the practical significance of memory savings. LoLoRA has more novelty (local updates + theory) than LoRA-FA but faces the same "memory savings minimal in practice" criticism. **LoLoRA is slightly stronger than LoRA-FA.**
- **Activations Aren't Cheap in LoRA** (avg 4.25, Reject): Narrow scope, reformulation-based contribution. LoLoRA has stronger theory and broader scope. **LoLoRA is clearly stronger than this.**
- **ReLoRA** (avg 5.75, Accept): Also faced complexity-vs-performance concerns but was accepted for its potential in pre-training. LoLoRA has a cleaner theoretical contribution but ReLoRA has demonstrated a clearer practical use case. **LoLoRA is slightly weaker than ReLoRA.**
- **GeoLoRA** (avg 6.25, Accept): Stronger theoretical guarantees (convergence, error bounds), better empirical results, and demonstrated efficiency gains. **LoLoRA is clearly weaker than GeoLoRA.**

### Final Score Determination
LoLoRA is above the low-band papers (3.0–3.33) and below the strong-band papers (8.0). Within the middle band, it sits above EVA (4.75) and Activations Aren't Cheap (4.25), slightly above LoRA-FA (5.33) due to the theoretical contribution, but below ReLoRA (5.75) and GeoLoRA (6.25). The paper's strengths — a genuine theoretical result and clean method — are counterbalanced by the weakness that the method's claimed advantage over well-initialized LoRA-FA is not empirically demonstrated. The theory (Theorem 4.4) is a meaningful formal contribution, but it primarily supports EVA-style initialization rather than uniquely motivating the LoLoRA approach. Score: **5.0**.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>