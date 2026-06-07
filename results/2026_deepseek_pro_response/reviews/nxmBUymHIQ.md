Now let me finalize the review. Let me compare:

- **EigenLoRA (5.00)**: PCA on adapter weights, limited theory, weak evaluations — LoLoRA is better (stronger theory, better evaluations on modern LLMs)
- **Partial-LoRA / Winning Tickets (5.20)**: LTH applied to LoRA, decent theory but small models — LoLoRA evaluates on more relevant models (LLaMA-8B, LLaVA-7B) but has weaker empirical claims
- **LoRA-FA (5.33)**: The direct predecessor — LoLoRA adds theory + mechanism but loses on empirical clarity
- **PaCA (6.00)**: Much clearer empirical benefits — LoLoRA is clearly below this

LoLoRA has more theoretical substance than the 5.0-5.2 anchors and evaluates on more relevant models, but its core empirical claim (outperforming LoRA-FA) is unconvincing. Final score: **5.0**.

---

## Summary
LoLoRA proposes a memory-efficient LoRA variant that updates the A adapter matrix during the forward pass using local, gradient-free update rules (Hebbian PCA / autoencoder), eliminating the need to store input activations for A's backward pass. The paper provides theoretical justification (Theorem 4.4) that under a random regression model, the optimal A initialization spans the top-r PCA subspace of the input covariance. Experiments span NLU (GLUE with RoBERTa-large), math reasoning (MetaMathQA→GSM8K with LLaMA-3.1-8B), multimodal instruction tuning (LLaVA-7B), and ablations (TinyLlama).

## Strengths
- **Theorem 4.4 provides a clean theoretical characterization** of the optimal A initialization: under the random regression assumption, the optimal A is a nonsingular transformation of the top-r PCA eigenvectors of the input covariance (line 168-169). This gives principled theoretical grounding for EVA-style PCA initialization that was previously only empirically motivated.
- **Novel architectural integration** of local Hebbian/PCA learning into LoRA — updating A during the forward pass via HPCA while B is trained via standard backprop (Algorithm 1, lines 1-7). This bridges PEFT and local learning in a creative way not previously explored for LLM fine-tuning.
- **Thorough ablation study (Table 6)** systematically compares five local update rules (HPCA variants, AE, SoftHebb) across three ranks, empirically validating that rules converging to the PCA subspace perform similarly (2.535–2.536 at r=8) while SoftHebb degrades to 2.572 — directly corroborating the theoretical claim that the target subspace, not the specific learning rule, is what matters. The comparison of LoRA-FA initializations in Table 5 is similarly informative.
- **Theorem 4.5 establishes formal A/B asymmetry**: any full-rank B initialization is equally good (line 178-179), while Theorem 4.4 shows A has a constrained optimal set. This provides theoretical grounding for applying local updates only to A rather than B, complementing prior empirical asymmetry findings.
- **Multi-domain evaluation** across NLU (8 GLUE tasks), math reasoning (LLaMA-3.1-8B), and multimodal tuning (LLaVA-7B) with a TinyLlama ablation, demonstrating the method across three model scales and modalities.

## Weaknesses

### Fatal
None.

### Major
- **The empirical case for LoLoRA over LoRA-FA is not established.** On GLUE (Tables 1–2), LoLoRA HPCA underperforms LoRA-FA with uniform initialization on 5 of 8 tasks (CoLA: 66.3 vs 67.9, RTE: 84.6 vs 86.4, MNLI: 90.3 vs 90.6, QQP: 90.6 vs 90.8, SST-2: 96.4 vs 96.7). On MathQA (Table 3), the gap vs LoRA-FA (uniform) is 0.003 with overlapping ±0.005 error bars. In the ablation (Tables 5–6), LoRA-FA with EVA init (2.536 at r=8) is essentially identical to LoLoRA HPCA (2.535). The paper's central value proposition — that LoLoRA fixes LoRA-FA's performance degradation while keeping its memory savings — is not convincingly demonstrated. The paper's own conclusion that "HPCA consistently outperforms standard LoRA-FA in two out of three experimental setups" (line 332-333) overstates the evidence when the GLUE results show the opposite pattern.
- **Theory–method coherence gap.** Theorem 4.4 justifies one-time PCA initialization of A (EVA), not the continuous online HPCA updates that define LoLoRA. The paper bridges this by noting HPCA converges to the PCA subspace (line 170), but HPCA convergence guarantees assume stationary inputs, while during fine-tuning the input distribution shifts as B is updated. The paper acknowledges non-stationarity as a limitation (line 334), but this is not a minor caveat — it severs the logical connection between the theoretical analysis (optimal static initialization) and the method's core mechanism (online chasing of a moving subspace). The theory primarily justifies EVA-style initialization, which LoRA-FA can already use.

### Minor
- **Memory savings are identical to LoRA-FA's.** The activation memory advantage over standard LoRA (avoiding storing z for A's backward pass) is exactly LoRA-FA's contribution, and LoLoRA introduces additional optimizer state for local updates (acknowledged in line 334 but not quantified). The net memory advantage over LoRA-FA may be zero or negative once the local optimizer state is accounted for.
- **Full LoRA consistently outperforms all LoLoRA variants** in the ablation (Table 6; 2.521 vs 2.535 at r=8). This performance cost of the memory savings should be foregrounded more prominently so readers can assess the trade-off.
- **Best-of-checkpoint evaluation on MathQA** (evaluation every 0.2 epochs, reporting the best result) risks overfitting to the evaluation schedule and may inflate reported scores relative to final-checkpoint evaluation.
- **No statistical testing on GLUE.** With 8 tasks and differences often under 1%, reporting only means ± std without any statistical test makes it impossible to assess whether observed differences are meaningful or attributable to seed variation.

### Trivial
- The local optimizer hyperparameters (learning rate, schedule) for HPCA updates are not discussed in the main text (deferred to Appendix C), despite being critical hyperparameters for online PCA convergence.

## Nice-to-Haves
- A gradient checkpointing baseline would contextualize LoLoRA's memory/compute trade-off against the standard technique for reducing activation memory.
- Quantifying the extra optimizer state memory cost of the local updates would allow readers to assess the net memory trade-off vs LoRA-FA.
- An experiment designed to isolate the benefit of online HPCA updates over one-time EVA initialization (e.g., continual fine-tuning across tasks with known distribution shift) would test whether the online mechanism provides value beyond initialization.

## Removed Points
These points are flagged to be removed, treat them with caution.

- **"Missing comparison to Key et al. (2023) 'Local LoRA'"** — REMOVED. Key et al. divides the transformer into layer chunks trained with local loss prediction, which is methodologically different from LoLoRA's Hebbian forward-pass updates on A. The similarity is in the name only, not the method. The work is appropriately cited in the related work section.
- **Harsh critic claim: "never clearly better"** — PARTIALLY REMOVED as an absolute statement. On MRPC (89.9 vs 89.8) and QNLI (94.7 vs 94.6), LoLoRA is marginally ahead of LoRA-FA (uniform). The overall pattern of GLUE results (worse on 5/8 tasks) is retained in the Major weakness above.
- **Strength Finder: "Competitive performance with memory savings on MathQA" claiming 0.829 matches LoRA-FA (EVA) at 0.829** — RETAINED with qualification. The match is genuine, but the gap vs the simpler LoRA-FA (uniform) at 0.826 is within noise. The strength is incorporated into the multi-domain evaluation point rather than as a standalone claim.
- **Strength Finder: "This paper addressed an important problem"** — REMOVED as generic and superficial.

## Novel Insights
The ablation results (Table 6) yield an interesting finding beyond the paper's theoretical contributions: all local update rules that converge to the PCA subspace (HPCA variants, AE) perform essentially identically, while SoftHebb — which targets a different subspace — degrades. This empirically demonstrates that the specific local learning rule matters less than whether it targets the right subspace, which is a practically useful finding for future work combining Hebbian learning with deep networks.

## Suggestions
- Redesign or add GLUE experiments with more seeds and statistical tests, or recalibrate claims to acknowledge that the reported differences between LoLoRA and LoRA-FA are within noise on most tasks.
- Add an experiment that isolates online HPCA benefits over one-time EVA initialization (e.g., continual fine-tuning across multiple tasks where the input distribution genuinely shifts).
- Foreground the Full LoRA vs LoLoRA gap more prominently in tables and discussion, to honestly present the performance cost of the memory savings.
- Report the memory cost of the local optimizer state so the net memory comparison vs LoRA-FA is complete.

## Score and Decision

**Calibration anchors considered across all rounds:**

| Paper | Path | Avg Score | Round | Comparison |
|-------|------|-----------|-------|------------|
| ALLoRA | 7X65yoKl3Y | 3.33 | 1 (weak) | LoLoRA is clearly stronger — has actual theory and a concrete mechanism |
| HoLoRA | igGeaxOiFM | 3.00 | 1 (weak) | LoLoRA is clearly stronger |
| EVA (One Init to Rule Them All) | DM6Q45HWSk | 4.75 | 1 (mid) + 2 | LoLoRA is better — provides the theoretical justification EVA lacked, plus a novel mechanism |
| MoRA | SxOrhLuuVz | 4.75 | 2 | Comparable quality; MoRA had clearer empirical results, LoLoRA has better theory |
| SwitchLoRA | iEUZMISIKj | 4.75 | 2 | LoLoRA is comparable |
| EigenLoRA | KxGGZag9gW | 5.00 | 2 | LoLoRA is comparable or slightly better — stronger theory, more relevant model evaluations |
| Winning Tickets / Partial-LoRA | PxYhHF6FNH | 5.20 | 2 | LoLoRA is comparable — better model diversity but weaker empirical claims |
| LoRA-FA | RbKThNNFxr | 5.33 | 1 (mid) + 2 | LoLoRA adds theory and mechanism but has weaker empirical differentiation from this baseline |
| PaCA | iYkhxre0In | 6.00 | 1 (mid) | LoLoRA is clearly weaker — PaCA shows unambiguous empirical benefits |
| LoRAM (Train Small, Infer Large) | s7DkcgpRxL | 6.20 | 2 | LoLoRA is clearly weaker |
| HiRA | TwJrTz9cRS | 8.00 | 1 (strong) | LoLoRA is clearly weaker |

**Round 1 bracket:** 4.75–6.00 (between EVA and PaCA).  
**Round 2 narrowing:** 5.00–5.33 (between EigenLoRA/Partial-LoRA and LoRA-FA). The paper adds genuine theoretical contributions and a novel mechanism over LoRA-FA, but its core empirical claim (outperforming LoRA-FA) is unconvincing and partially contradicted by the GLUE results.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>