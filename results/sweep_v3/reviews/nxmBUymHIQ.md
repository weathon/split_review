Now I have everything I need. Let me write the consolidated review.

## Summary

This paper introduces LoLoRA, a LoRA variant that updates the low-rank adapter matrix **A** using local unsupervised rules (HPCA / autoencoder) during the forward pass, avoiding storage of input activations for **A**'s backward pass and thereby reducing memory. The authors provide a theoretical analysis (Theorem 4.4) showing that optimal frozen **A** spans the dominant eigenspace of the input covariance, and propose replacing offline PCA initialization with online HPCA updates. Experiments on GLUE (RoBERTa-large), GSM8K (LLaMA-3.1-8B), LLaVA, and TinyLlama ablations show LoLoRA matches or slightly exceeds uniform-initialized LoRA-FA while achieving the same 4 GB memory reduction as LoRA-FA (26 GB vs. 30 GB for standard LoRA).

## Strengths

1. **Theoretical characterization of optimal A initialization.** Theorem 4.4 proves that, under a random regression model, any optimal frozen **A** must span the dominant eigenspace of the input covariance matrix. This provides a principled justification for PCA-based local updates (HPCA) and complements the empirical results of EVA (Paischer et al., 2024). The asymmetry between **A** and **B** (Theorems 4.4–4.5) is clearly articulated.

2. **Measurable memory reduction with competitive accuracy.** On LLaMA-3.1-8B (Table 3), LoLoRA uses 26 GB extra memory vs. 30 GB for standard LoRA (13% reduction) while achieving 82.9% accuracy — matching the best LoRA-FA variant and outperforming standard LoRA (82.1%) and the base model (79.0%). The ablation (Tables 5–6) further shows that HPCA-based local rules reach within 0.02 perplexity of full LoRA at rank r=2 on TinyLlama.

3. **Broad evaluation across multiple domains.** The method is tested on NLU (8 GLUE tasks), math reasoning (GSM8K), multimodal fine-tuning (LLaVA), and ablations on TinyLlama/Alpaca, comparing against LoRA, LoRA-FA (uniform, EVA), PiSSA, and orthogonal initializations.

## Weaknesses

### Fatal
None.

### Major

1. **The claimed advantage of online adaptation over static EVA initialization is not demonstrated.** The paper positions LoLoRA as "mitigating the trade-off" between memory savings and performance compared to LoRA-FA. However, the experiments consistently show that LoLoRA matches — but does not clearly outperform — LoRA-FA with EVA (data-driven PCA) initialization:
   - **GLUE (Tables 1–2):** LoLoRA HPCA scores comparably to LoRA-FA (EVA) across all 8 tasks (e.g., QNLI: 94.7 vs. 94.5; SST-2: 96.4 vs. 96.3; CoLA: 66.3 vs. 64.7). Differences are within ±1 standard deviation.
   - **GSM8K (Table 3):** LoLoRA and LoRA-FA (EVA) both achieve 82.9% — identical.
   - **LLaVA (Table 4):** LoLoRA HPCA (perplexity 2.93) is slightly worse than LoRA-FA (EVA) (2.92).
   The memory savings are also identical to LoRA-FA (26 GB for both on GSM8K; 24.1 GB vs. 23.9 GB on LLaVA, with a small overhead for the local optimizer state acknowledged by the authors). The paper never tests a scenario where distribution shift during training would make static PCA suboptimal (e.g., multi-task, sequential fine-tuning, or covariate shift). Without this, the key claim that local *online* adaptation provides a benefit over one-shot PCA initialization is unsupported.

2. **The narrative overclaims relative to the evidence.** The abstract states the method "further reduc[es] the memory required for fine-tuning" — but the memory reduction is relative to standard LoRA, not to LoRA-FA (which achieves the same memory with frozen **A**). The conclusion says "HPCA consistently outperforms standard LoRA-FA in two out of three experimental setups" — this is accurate for *uniform-initialized* LoRA-FA, but the paper's framing blurs the distinction between uniform and EVA-initialized LoRA-FA. A reader could walk away thinking LoLoRA brings a clear improvement over all LoRA-FA variants, when in fact the comparison against EVA (the strongest LoRA-FA baseline) is a tie.

### Minor

3. **The theoretical section characterizes static A, not the online setting.** Theorem 4.4 identifies the optimal *static* initialization of **A** under strong assumptions (i.i.d. Gaussian weight change, stationary input covariance, isolated submodule). It does not address the dynamic setting where **A** is updated online during joint training with non-stationary targets and multi-layer error propagation. The paper acknowledges this limitation, but the framing ("the theoretical motivation for our method") suggests stronger support for the online algorithm than the theory actually provides.

4. **Missing rank r for GLUE experiments.** The rank used in the main GLUE experiments (Tables 1–2) is not reported in the text or table captions. The ablations (Tables 5–6) specify ranks r=2,4,8, and the LLaVA and GSM8K sections specify ranks implicitly, but the GLUE section omits this critical detail entirely.

### Trivial
None.

## Nice-to-Haves

- **Demonstrate the value of online adaptation directly.** Run an experiment with covariate shift or sequential fine-tuning (e.g., fine-tune on task A then task B) to show that LoLoRA adapts to changing distributions while static EVA does not.
- **Report the rank and learning rate for the HPCA update rule** in the main text or provide a succinct hyperparameter table for all experiments.
- **Reframe the contribution** as a convenient alternative to LoRA-FA (EVA) that achieves competitive performance without a separate data pass, rather than as a method that "mitigates the trade-off" — the current framing invites unfair comparison.

## Removed Points

- *"LoLoRA HPCA is often worse than LoRA-FA (EVA)"* — **Removed (factually incorrect).** The paper's GLUE results show LoLoRA is comparable to or slightly better than LoRA-FA (EVA) on most tasks (e.g., CoLA: 66.3 vs. 64.7, RTE: 84.6 vs. 83.6, QNLI: 94.7 vs. 94.5). The critic's reading of the tables was inaccurate.
- *"The claim that HPCA consistently outperforms standard LoRA-FA in two out of three experimental setups is not supported"* — **Removed (factually incorrect).** Checking the data: GSM8K (82.9 vs. 82.6) ✓, LLaVA (2.93 vs. 2.97) ✓, GLUE (mixed — some tasks LoLoRA ahead, some behind). "Two out of three" is an accurate description of the overall experimental setups.
- *Speculative criticisms about appendix content, missing proofs, or reproducibility concerns* — **Removed** (parser strips appendices; all papers at this venue are affected equally).
- *"The experiment lacks a head-to-head comparison isolating online adaptation"* — **Retained and upgraded to Major weakness #1** (it is a real concern), but stripped of the framing that this is a "structural/evidential" fatal flaw.
- *"The theoretical justification does not directly support the local update algorithm"* — **Demoted to Minor** (the paper explicitly acknowledges the limitation; the theory provides valid motivation even if it doesn't prove optimality in the dynamic setting).
- *Several generic weaknesses from the Harsh Critic about LoLoRA being "more expensive" or requiring "additional hyperparameters"* — **Removed** (the overhead is minimal and acknowledged by the authors; no evidence it harms practical utility).

## Novel Insights

The strongest observation from the calibrating reviews is that the LoLoRA paper resolves a weakness identified in both the LoRA-FA review (which noted that frozen random **A** may be suboptimal) and the EVA review (which noted a lack of theoretical justification for PCA-based initialization). Theorem 4.4 fills EVA's theoretical gap by proving that spanning the dominant eigenspace is optimal under a random regression model, and LoLoRA's online HPCA updates avoid the suboptimal random initialization that motivated LoRA-FA's limitations. Unfortunately, the paper does not then demonstrate that this combination yields a practical advantage over simply using EVA and freezing **A**.

## Suggestions

1. Add a clear experiment demonstrating distribution shift during fine-tuning (e.g., sequential task fine-tuning or multi-task learning) to show when online HPCA adaptation helps over static EVA initialization.
2. Report the rank and HPCA hyperparameters for all experiments, ideally in a single summary table.
3. Reframe the narrative: "LoLoRA achieves competitive performance with LoRA-FA (EVA) while eliminating the need for a separate PCA data pass" is an honest, valuable contribution that sidesteps overclaim.

## Score and Decision

**Anchor calibration:**

| Anchor | Avg Score | Comparison |
|--------|-----------|------------|
| ReLoRA (DLJznSp6X3) | 5.75, Accept | Similar PEFT method with comparable-vs-baseline results and similar novelty concerns. LoLoRA has stronger theory but weaker experimental differentiation. LoLoRA is slightly weaker. |
| LoRA-FA (RbKThNNFxr) | 5.33, Reject | Directly related predecessor. LoLoRA adds theoretical grounding and local updates. LoLoRA is somewhat stronger. |
| EVA — Explained Variance Adaptation (DM6Q45HWSk) | 4.75, Reject | LoLoRA shares EVA's PCA intuition but adds the theory EVA lacked and the online mechanism. LoLoRA is stronger. |
| Train Small, Infer Large (s7DkcgpRxL) | 6.20, Accept | Different approach to memory-efficient LoRA. More dramatic memory reduction, clearer experimental story. LoLoRA is weaker. |
| Activations Aren't Cheap (3ylNuZXtMg) | 4.25, Reject | Addresses activation memory in LoRA. LoLoRA has more algorithmic novelty and broader evaluation. LoLoRA is stronger. |
| ME-LoRA (0qexTTfnmH) | 3.75, Reject | Bayesian LoRA variant. LoLoRA has more thorough experiments and a more clearly motivated method. LoLoRA is stronger. |

The paper has genuine contributions — a theoretical grounding for PCA-based A initialization and an online local update mechanism that avoids the need for a separate data pass. However, the central claim that online adaptation provides an advantage over static data-driven initialization (EVA) is unsupported by the experiments; LoLoRA matches rather than improves upon EVA-initialized LoRA-FA across every evaluation. The narrative overstates the contribution. The paper falls between the LoRA-FA (5.33, Reject) and ReLoRA (5.75, Accept) anchors — closer to LoRA-FA given the similar issue of insufficient differentiation from the simpler baseline.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>