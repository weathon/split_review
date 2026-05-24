Now I have a thorough understanding of the paper and all reviewer inputs. Let me write the consolidated review.

---

## Summary

This paper proposes LoLoRA, a variant of LoRA where the projection-down matrix \(A\) is updated via local unsupervised rules (HPCA / autoencoder) during the forward pass (no activation storage for \(A\)'s backward pass), while \(B\) is trained via standard backpropagation. The paper also proves Theorem 4.4, which characterizes the optimal \(A\) as spanning the dominant PCA subspace of the input covariance. Experiments on GLUE (RoBERTa-large), MetaMathQA (LLaMA-3.1-8B), LLaVA-v1.5-7B, and ablations on TinyLlama-1.1B compare LoLoRA against standard LoRA, LoRA-FA variants, and EVA initialization.

## Strengths

- **Theorem 4.4 is a clean theoretical contribution.** The paper proves that under a random regression model, the optimal frozen matrix \(A\) must span the top principal subspace of the input covariance matrix. This formalizes an intuition that prior work (EVA) had only demonstrated empirically, and goes beyond existing theory by characterizing the entire set of optimal solutions. The asymmetry result (Theorem 4.5, showing any full-rank \(B\) initialization is equivalent) is also valuable.

- **Systematic and well-designed ablation study.** Tables 5 and 6 on TinyLlama-1.1B compare multiple \(A\) initializations (Uniform, Orthogonal, PiSSA, EVA) and multiple local update rules (HPCA, AE, SoftHebb) across ranks 2, 4, and 8. The results are informative: all methods that converge to the PCA subspace (EVA, HPCA, AE) achieve statistically equivalent performance, while methods that do not (SoftHebb) underperform. This provides clear, reproducible guidance.

- **Consistent memory savings vs. standard LoRA.** Across all experiments, LoLoRA reduces peak extra memory compared to standard LoRA (e.g., 26 GB vs 30 GB on MetaMathQA, Table 3; 24.1 GB vs 24.6 GB on LLaVA, Table 4), validating the memory-reduction motivation.

## Weaknesses

### Major

- **The claimed advantage of online adaptation is not empirically tested.** The abstract states that LoLoRA "allow\[s\] it to adapt to input distribution shifts," and the method's distinguishing feature vs. EVA initialization is that it can adapt online. However, every experiment follows a standard static fine-tuning protocol. No experiment evaluates a non-stationary setting (e.g., changing data distribution, streaming data, or a scenario where an offline PCA pre-pass is impossible). Without such a test, the method's core value proposition over the simpler EVA initialization is unsubstantiated. The paper's own ablations show that EVA initialization and LoLoRA achieve nearly identical results, so the reader cannot distinguish whether LoLoRA's online updates provide any benefit at all.

- **LoLoRA does not outperform the strongest baseline (LoRA-FA with EVA) in a way that supports the claimed narrative.** Across the three main experimental settings:
  - **GLUE (Tables 1–2):** LoLoRA HPCA numerically exceeds or matches LoRA-FA (EVA) on 7/8 tasks, but the margins are small (typically <1 point) and within standard error on most tasks. The paper's own summary says LoLoRA achieves "slightly better results than LoRA-FA (EVA)."
  - **MetaMathQA (Table 3):** LoLoRA HPCA and LoRA-FA (EVA) achieve **identical** accuracy (0.829), with overlapping confidence intervals.
  - **LLaVA (Table 4):** LoRA-FA (EVA) achieves **better** perplexity (2.92 vs. 2.93), **lower** loss (1.070 vs. 1.075), and **lower** memory (23.9 GB vs. 24.1 GB) than LoLoRA HPCA.

  The claim "consistently outperforms standard LoRA-FA in two out of three experimental setups" (Conclusion) relies on defining "standard" as uniform-initialized LoRA-FA; against the stronger EVA-initialized baseline, LoLoRA does not show a clear advantage. The method's benefit over the theoretically optimal static initialization is not established.

- **Best-checkpoint selection in Table 3 inflates reported accuracy.** The MetaMathQA experiment reports the best checkpoint over the fine-tuning window ("tested on GSM8K every 0.2 epoch … the best result is reported") rather than the final checkpoint. This is an unusual practice that can inflate results and makes comparison with papers reporting final checkpoints unreliable. The other experiments appear to report best validation metrics but this is not clearly stated for all tables.

### Minor

- **Memory breakdown for LoLoRA's local optimizer state is missing.** The conclusion acknowledges that "our method introduces a small amount of extra optimizer state for the local updates, unlike standard LoRA-FA," but neither the main text nor Appendix D (referenced for memory analysis) provides a detailed breakdown. Quantifying the per-layer overhead of the local optimizer relative to total memory would help a practitioner evaluate the trade-off.

- **The theoretical analysis assumes stationarity and isolated submodules.** Theorem 4.4 analyzes each submodule independently with a stationary target. The paper acknowledges this limitation but does not discuss how violations (non-stationary inputs from upstream layer changes, multi-layer interactions) might affect the validity of the theory for the actual fine-tuning setting. Since LoLoRA's online adaptation is motivated by non-stationarity, this gap is notable.

- **The conclusion's phrasing is ambiguous.** The statement "HPCA consistently outperforms standard LoRA-FA" uses "standard LoRA-FA" to mean uniform-initialized LoRA-FA, but earlier sections use "standard" to refer to the commonly known variant. Since the paper's own experiments show that EVA-initialized LoRA-FA generally performs as well or better than LoLoRA, the phrasing could mislead a casual reader.

### Trivial

- Table 3's "Extra Memory" column reports integer GB when LoRA-FA and LoLoRA both show 26 GB. If there are sub-GB differences between methods, reporting to one decimal would be more informative.

## Nice-to-Haves

- An experiment explicitly testing non-stationary adaptation (e.g., a synthetic setup where the input covariance shifts during training, or an online/streaming scenario) would directly validate the method's distinguishing claim.
- A timing breakdown separating the PCA initialization pass (EVA) from the forward-pass HPCA computation would help practitioners choose between offline and online approaches.
- Reporting final (not best) checkpoints for Table 3 would align with standard practice.

## Removed Points

These points were raised by reviewers but are removed after cross-verification against the paper:

1. **"LoLoRA does not exceed LoRA-FA (EVA) on any of the eight GLUE tasks."** — This is factually incorrect. The paper's Tables 1–2 show LoLoRA HPCA numerically exceeds LoRA-FA (EVA) on CoLA (66.3 vs 64.7), RTE (84.6 vs 83.6), STS-B (92.0 vs 91.9), QNLI (94.7 vs 94.5), and SST-2 (96.4 vs 96.3), and ties on QQP (90.6 vs 90.6). The critic's claim is wrong on the evidence.

2. **"The abstract's memory reduction claim is contradicted by the LLaVA experiment."** — The abstract states "further reducing the memory required for fine-tuning" relative to *standard LoRA*, not relative to LoRA-FA. In the LLaVA table, LoLoRA uses 24.1 GB vs 24.6 GB for standard LoRA, consistent with the claim.

3. **"The paper ignores the EVA baseline."** — False. LoRA-FA (EVA) appears as a baseline in every single experiment table (Tables 1, 2, 3, 4, 5). The paper systematically compares against it.

4. **Reproducibility concerns about "not yet released" artifacts.** — The paper references standard HuggingFace models and datasets; these are publicly available as of the current date.

## Novel Insights

The most interesting observation emerging from the reviews is that the paper's own evidence can be read as a *confirmation* of Theorem 4.4 rather than a validation of LoLoRA as a method: Tables 5–6 show that EVA initialization, HPCA, and AE all converge to nearly identical perplexity on TinyLlama, which is exactly what the theorem predicts (all methods reaching the same PCA subspace are equivalent). The paper could have been stronger had it leaned into this narrative — presenting Theorem 4.4 as the primary contribution and LoLoRA as one convenient implementation rather than claiming superiority over methods that solve the same objective. The fact that LoLoRA does not need a separate data pass for PCA is a genuine operational advantage in some settings, but the paper does not test or emphasize this.

## Suggestions

- **Reframe the paper** around the theoretical result (Theorem 4.4) as the primary contribution, with LoLoRA presented as an online method that achieves the same PCA subspace without a separate data pass, rather than claiming superiority over EVA-initialized LoRA-FA.
- Add a synthetic or real experiment with a non-stationary input distribution to demonstrate LoLoRA's adaptation capability.
- Report final checkpoints (not best) for Table 3, or clearly justify the practice.
- Provide a memory breakdown table showing base model weights, activations, adapter weights, and optimizer states separately for LoRA, LoRA-FA, and LoLoRA.
- Clarify the phrasing about "standard LoRA-FA" in the conclusion to avoid ambiguity.

## Score and Decision

### Calibration

**Round 1 — Bracketing:**
- Weak anchors (< 3.5): ALLoRA (3.33), HoLoRA (3.00) — papers with fatal flaws or very thin contributions. The current paper is much stronger due to its theory and systematic experiments.
- Middle anchors (3.5–7.5): EVA (4.75), LoRA-FA (5.33), Expressive Power of LoRA (6.50), Decoupling Angles (5.25). The EVA paper is the most directly comparable — it proposes a data-driven initialization for LoRA but was rejected for lacking theoretical justification and showing marginal gains. The current paper surpasses EVA on theory but shares the "marginal gains over baselines" problem.
- Strong anchors (> 7.5): TopoLM (8.00), Scaling Laws for Assoc. Memories (7.60), Sparse Autoencoders (8.20) — papers with clean, fully-supported contributions. The current paper does not reach this tier.

Initial bracket: between 4.5 and 6.0.

**Round 2 — Narrowing:**
- LoRA-FA paper (5.33, sim 0.75) — similar setting and memory-saving motivation. Both papers show memory savings but the method advantages are marginal against baselines. The current paper has stronger theory but the LoRA-FA paper has cleaner validation of its core claim. Comparable or slightly lower than LoRA-FA because the empirical gap against the strongest baseline is smaller.
- Expressive Power of LoRA (6.50, sim 0.72) — purely theoretical with limited experiments. The current paper has more empirical breadth but the experiments are less cleanly supporting the method claims. Inferior to this anchor.
- Decoupling Angles (5.25, sim 0.73) — a PEFT method with some theory and experiments. Similar profile: method doesn't dramatically outperform baselines but has genuine insights. Comparable territory.

The paper is stronger than EVA (4.75) due to the theoretical contribution, comparable to or slightly below LoRA-FA (5.33) because LoLoRA's experimental validation against the strongest baseline (EVA) is less convincing than LoRA-FA's validation against standard LoRA. The theory elevates it above EVA but the empirical gap anchors it below 5.5.

**Final score: 5.0**

This reflects a paper with a genuine theoretical contribution and thorough ablations, but whose central method claim is not well-supported by the evidence — LoLoRA does not clearly outperform the simpler EVA-initialized baseline, and its distinguishing feature (online adaptation) is never tested.

<score>5.0</score>
<decision>Reject</decision>