## Summary

LoLoRA proposes a hybrid fine-tuning method that replaces backpropagation through LoRA's A matrix with local, gradient-free Hebbian PCA (HPCA) updates during the forward pass, while B is trained via standard backpropagation. The paper contributes a theoretical result (Theorem 4.4) proving that optimal A spans the top-\(r\) eigenspace of the input covariance matrix under random regression assumptions, which motivates the HPCA update rule. Experiments span three settings (RoBERTa-large on GLUE, LLaMA-3.1-8B on math reasoning, LLaVA-v1.5-7B on multimodal instruction tuning) with reported memory savings of ~13% vs. standard LoRA on the math setup.

---

## Strengths

1. **Clean theoretical characterization of optimal A.** Theorem 4.4 provides a formal derivation—under well-specified (if strong) assumptions—that the optimal frozen or locally-updated A should span the top-\(r\) eigensubspace of the input covariance matrix. This extends the empirical findings of the EVA initialization (Paischer et al., 2024) with an optimality proof and is a genuine theoretical contribution.

2. **Measured memory reduction at scale.** In the LLaMA-3.1-8B mathematical-reasoning experiment (Table 3), LoLoRA HPCA uses 26 GB of extra GPU memory vs. 30 GB for standard LoRA (~13% reduction) while matching the best baseline accuracy of 0.829. The memory savings are verifiable and non-trivial.

3. **Informative ablation study linking theory to practice.** Table 6 compares multiple local update rules (HPCA, AE, SoftHebb) and confirms that only methods that converge to the PCA subspace (HPCA, AE) perform well, while SoftHebb (which does not converge to the top-\(r\) eigenspace) performs significantly worse. This provides empirical grounding for the theoretical result.

4. **Systematic comparison of A initializations for LoRA-FA.** Table 5 compares uniform, orthogonal, PiSSA, and EVA initializations on TinyLlama-1.1B and confirms that EVA (which aligns with the theoretical optimum) yields the lowest validation perplexity at every tested rank. This ablation is clean and informative.

---

## Weaknesses

### Major

1. **The method does not demonstrate a clear advantage over simply freezing A with a good initialization (EVA).** This is the paper's central weakness. The core claim is that *online* local updates of A provide benefit over freezing A. However, across all three benchmarks, LoLoRA HPCA never clearly outperforms LoRA-FA with EVA initialization:
   - **GLUE (Tables 1–2):** LoLoRA is numerically worse than LoRA-FA(uniform) on 5/8 tasks, ties on 2, and is better on only 1 (QNLI, +0.1). Against LoRA-FA(EVA), LoLoRA matches or slightly edges ahead on some tasks but still falls well below standard LoRA on most metrics. The paper's own summary notes that "classical LoRA remains the strongest overall."
   - **Math reasoning (Table 3):** LoLoRA (0.829) ties LoRA-FA(EVA) (0.829) and is +0.003 ahead of LoRA-FA(uniform) (0.826)—all within one standard deviation.
   - **LLaVA (Table 4):** LoLoRA perplexity (2.93) is *worse* than LoRA-FA(EVA) (2.92) and only trivially better than LoRA-FA(uniform) (2.97).
   
   Since LoRA-FA(EVA) achieves the same memory savings without the complexity of local optimizer states, the paper does not establish a scenario where the online adaptation provides a meaningful advantage. The claim in the Conclusion that "HPCA consistently outperforms standard LoRA-FA in two out of three experimental setups" is true only when "standard LoRA-FA" refers to uniform initialization, and even then the improvements are marginal and within error bars.

2. **The theoretical analysis justifies optimal initialization, not online adaptation.** Theorem 4.4 proves that optimal A spans the dominant eigenspace of \(\Sigma_{zz}\), which directly justifies EVA (a one-shot PCA precomputation). The paper then uses the same theorem to motivate *iterative* HPCA updates, but the theory says nothing about whether online tracking of a non-stationary subspace during fine-tuning yields additional benefit over a single precomputed PCA. The ablation (Table 6) confirms that any PCA-converging rule works about as well as EVA, but no experiment demonstrates a setting where the adaptive tracking actually helps (e.g., non-stationary input distributions, curriculum learning, or sequential task adaptation). The theoretical contribution is thus effectively orthogonal to the method's claimed advantage over EVA.

### Minor

3. **Missing baselines on main benchmarks.** PiSSA (Meng et al., 2024) appears only in the TinyLlama ablation (Table 5), where it performs competitively with uniform initialization. Since PiSSA is a well-known SVD-based initialization that also avoids storing A's activations, its absence from the GLUE, MathQA, and LLaVA main tables weakens the evaluation. The paper would be strengthened by including PiSSA and perhaps other informed initializations in the main comparisons to show that the advantage is not simply about better initialization.

4. **Memory comparison between LoLoRA and LoRA-FA is not broken down cleanly.** On LLaVA (Table 4), LoLoRA uses 24.1 GB of extra memory vs. LoRA-FA's 23.9 GB—a small but real increase. The paper attributes this to local optimizer states but does not quantify the overhead or discuss whether the memory savings over LoRA (24.6 GB) justify the added complexity. A clear breakdown of where the memory goes (activations, optimizer states for A vs. B, etc.) would help readers assess the practical trade-off.

5. **Local update hyperparameters are underspecified.** The method introduces a local learning rate, smoothing factor (0.98 is mentioned in the text for HPCA), and optimizer states for A. These are not fully reported outside of the ablation caption; the paper refers to Appendix C (stripped by the parser) for details. Reproducibility requires these values in the main text or a public supplement.

### Trivial

- The paper claims on line 85 that \(W\) can be "\(W_q\), \(W_k\), \(W_o\), or \(W_o\)" — the last two appear to be a duplicate (\(W_o\) listed twice); presumably one should be \(W_v\) or \(W_{proj}\).

---

## Nice-to-Haves

- **Test the adaptive hypothesis directly.** The paper motivates online updates with "adapting to input distribution shifts." A targeted experiment with explicit non-stationarity (e.g., curriculum learning or sequential fine-tuning on two different tasks) that compares LoLoRA to LoRA-FA(EVA) would directly test whether the adaptive mechanism provides any benefit.
- **Track subspace alignment during training.** Measuring how closely the subspace spanned by LoLoRA's A tracks the evolving covariance, relative to the fixed EVA subspace, would provide direct evidence for (or against) the claimed advantage.

---

## Removed Points

- **"LoLoRA underperforms LoRA-FA (uniform) on 4/8 GLUE tasks"** — The count is actually 5/8 (CoLA, RTE, MNLI, QQP, SST-2), but the harsh critic's framing implies a stronger failure than the data support given overlapping error bars. The point is retained in Major weakness #1 but softened from its original phrasing.
- **"The paper does not test PiSSA on the main benchmarks"** — Kept with proper attribution as a missing baseline.
- **Strength: "Consistent performance across multiple tasks and models"** — Removed because the performance is mixed, particularly on GLUE where LoLoRA underperforms LoRA-FA(uniform) on most tasks. The evidence does not support "consistent."
- **"Theoretical analysis is disconnected from the actual method"** — Partially removed because the theory does connect to the method via the convergence of HPCA to the PCA subspace (which is shown in the ablation). Retained as the observation that the theory justifies initialization, not online updates (Major #2).
- **Criticism about missing appendix sections (proofs, hyperparameters)** — The parser strips these; they exist in the original submission. Hyperparameter concerns are retained as a minor weakness.
- **"The conclusion overstates findings"** — The conclusion's phrasing is carefully hedged ("in two out of three experimental setups"), so not an overstatement. Kept implicitly via Major #1.
- **Strengths about "addressing an important problem"** — Generic; removed.
- **Strength Finder's claim about consistent performance** — Conflicts with the verified weakness on GLUE; removed per instructions.

---

## Novel Insights

None beyond the paper's own contributions. The reviews surface a recurring pattern: LoLoRA's theoretical contribution (Theorem 4.4) cleanly justifies data-driven initialization (EVA), but the paper attempts to leverage this theory to motivate a more complex online method (HPCA) without providing evidence that the online mechanism adds value over the one-shot initialization it theory justifies. This gap between "optimal initialization" and "benefit of continued adaptation" is the paper's central unaddressed question.

---

## Suggestions

1. Either provide a setting where online adaptation matters (e.g., non-stationary input distributions, multi-task sequential fine-tuning) and demonstrate that LoLoRA tracks the evolving subspace better than frozen EVA, or reframe the contribution as a theoretical justification of EVA initialization with HPCA as a practical approximation that avoids a separate PCA precomputation pass.
2. Include PiSSA and potentially other informed initializations (e.g., LoRA-GA) in the main GLUE and MathQA comparisons.
3. Provide a detailed memory breakdown (activations, optimizer states for A, optimizer states for B) to clarify where LoLoRA's tiny memory overhead over LoRA-FA comes from.
4. Report local update hyperparameters (local learning rate, optimizer choice for A) in the main text.

---

## Score and Decision

### Calibration Anchors

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| /home/wg25r/review_agent/human_reviews_2026/ZBaPU5FL0Z.md (OP-LoRA) | 3.00 | Bracketing | Weaker paper with less theory; rejected. LoLoRA has stronger theory. |
| /home/wg25r/review_agent/human_reviews_2026/bR32fsXLbf.md (DASP) | 3.00 | Bracketing | Similar topic (memory-efficient fine-tuning) but different approach. LoLoRA has cleaner theory. |
| /home/wg25r/review_agent/human_reviews_2026/x5HDAixMaK.md (Kron-LoRA) | 2.00 | Bracketing | Significantly weaker; rejected. LoLoRA is substantially stronger. |
| /home/wg25r/review_agent/human_reviews_2026/QD4DL0OUmZ.md (LoRAct) | 4.00 | Bracketing | Similar profile: marginal empirical gains, missing baselines. Rejected. LoLoRA has better theory but similar empirical weakness. |
| /home/wg25r/review_agent/human_reviews_2026/zL9wxlDExi.md (ScaLoRA) | 4.80 | Bracketing | Strong theory, marginal empirical gains. Rejected. Comparable to LoLoRA in profile, though ScaLoRA's theory is more tightly coupled to its method. |
| /home/wg25r/review_agent/human_reviews_2026/kObvnQ6pUx.md (RaLoRA) | 5.50 | Bracketing | Stronger empirical results (+5% on GLUE). Accepted Poster. LoLoRA is weaker empirically. |
| /home/wg25r/review_agent/human_reviews_2026/ij8xU2yCmX.md (Less is More) | 4.00 | Bracketing | Similar empirical quality but different contribution. Withdrawn/rejected. |
| /home/wg25r/review_agent/human_reviews_2026/OXmRvlihi3.md (LoRA-FA paper) | 3.50 | Narrowing | Directly relevant (LoRA-FA paper). Rejected. LoLoRA has more theory and ablations. |
| /home/wg25r/review_agent/human_reviews_2026/32G5SjCAMV.md (PiCa) | 4.00 | Narrowing | Theory + consistent outperformance. Accepted Poster. LoLoRA empirically weaker. |
| /home/wg25r/review_agent/human_reviews_2026/4nNqVpC3td.md (LoRA-DA) | 5.00 | Narrowing | Strong theory, consistent but modest improvements. Rejected despite good theory. |
| /home/wg25r/review_agent/human_reviews_2026/xSa19DAieH.md (Stable-LoRA) | 4.00 | Narrowing | Theory + method. Accepted Poster. Different contribution focus. |
| /home/wg25r/review_agent/human_reviews_2026/KXJa6pPx0o.md (LoRA-SB) | 4.00 | Narrowing | Theory for initialization. Withdrawn/rejected. |

**Round 1 bracket:** The paper sits between the weak anchor cluster (~2–3, clearly rejected papers with thin contributions) and the strong anchor cluster (~5.5, accepted papers with solid empirical gains). Initial bracket: [3.0, 5.5].

**Round 2 narrowing:** Most comparable to ScaLoRA (4.80, rejected) and LoRA-DA (5.00, rejected)—papers with good theoretical contributions but empirical results that are marginal relative to the complexity they introduce. LoLoRA's empirical case is weaker than both (ScaLoRA shows consistent improvements across tasks; LoRA-DA shows 0.3–1.0% gains with low overhead). The PiCa paper (4.00, accepted as poster) has similar theoretical depth but stronger empirical results. The LoRAct paper (4.00, rejected) has a similar weakness profile.

**Final score:** 4.0. The paper has a genuine theoretical contribution and a reasonably thorough ablation study, but its central empirical claim is not well-supported: the method does not outperform the simpler LoRA-FA(EVA) baseline that it is meant to improve upon. The gap between the theoretical framing and the empirical demonstration of the method's claimed advantage is the paper's fundamental weakness, and it is not overcome by the experiments as presented.

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>