Now I have sufficient anchors to finalize. Let me consolidate my analysis.

**Round 1 Bracket:** 5.0 – 6.5, between LoRA-FA (5.33) and LoRAM (6.20).

**Round 2 narrows it:** The paper is clearly better than EVA (4.75) and LoRA-FA (5.33) due to added theory and online mechanism, but weaker than ReLoRA (5.75) which showed clearer practical gains, and well below the primarily theoretical "Expressive Power of LoRA" (6.50).

---

## Summary

This paper proposes LoLoRA, a method that replaces gradient-based backpropagation updates of the LoRA A matrix with local, forward-pass updates (Hebbian PCA or autoencoder loss). This eliminates the need to store A's activations, matching the memory savings of LoRA-FA (frozen A) while aiming to improve performance through online adaptation. The paper provides theoretical analysis showing that under random regression assumptions, the optimal fixed A spans the top principal components of the input covariance, motivating the Hebbian PCA approach. Experiments span GLUE, math reasoning, and multimodal tuning.

## Strengths

- **Genuine theoretical contribution (Theorems 4.4–4.6):** The paper proves that under stated assumptions, the optimal A initialization is any nonsingular transformation of the top-r eigenvectors of the input covariance. Theorem 4.5 complements this by showing B initialization is irrelevant (any full-rank B is equivalent). These results provide a principled justification for PCA-based A initialization and explain the asymmetry between A and B adapters — a finding with implications beyond this specific method.

- **Well-motivated method bridging theory and practice:** The theoretical result directly motivates the choice of Hebbian PCA updates, which are known to converge to the principal eigenspace. The ablation study (Tables 5–6) validates this design: EVA (PCA-based) initialization consistently outperforms uniform, orthogonal, and PiSSA for frozen A, and online HPCA/AE updates match or approach this quality without requiring a separate PCA pre-computation pass.

- **Comprehensive empirical coverage across model types and tasks:** Experiments include RoBERTa-large on GLUE (language understanding), LLaMA-3.1-8B on MetaMathQA→GSM8K (math reasoning), and LLaVA-v1.5-7B on Visual Instruct (multimodal), plus ablations on TinyLlama. This diversity provides reasonable evidence of generality.

- **Transparent limitations:** The paper acknowledges the stationarity assumption in the theory, the extra optimizer state from local updates, and cases where memory gains are limited (e.g., LLaVA with large image tokens).

## Weaknesses

### Fatal
None.

### Major

- **Marginal empirical advantage over the static EVA baseline.** The core practical claim is that online local updates improve over simply freezing A. However, across the headline experiments, LoLoRA's performance is matched or nearly matched by LoRA-FA with EVA initialization (a one-shot PCA of input activations, requiring no online mechanism). On MathQA (Table 3), both achieve 0.829 accuracy. On LLaVA (Table 4), LoRA-FA (EVA) achieves *better* perplexity (2.92 vs. 2.93). On GLUE, LoLoRA does outperform LoRA-FA (EVA) on 5 of 8 tasks, but margins are small. The paper acknowledges that EVA achieves comparable performance and notes LoLoRA's advantage is avoiding the separate PCA pre-computation pass. But this advantage is modest for standard static-dataset fine-tuning, and the paper provides no evidence of settings where online adaptation meaningfully outperforms a well-initialized static A. This weakens the central value proposition.

- **Untested claim of distribution shift adaptivity.** The abstract states the method allows LoRA to "adapt to input distribution shifts," and this language recurs in framing the method's motivation. Yet no experiment involves any distribution shift — all datasets are static, and fine-tuning proceeds on a single fixed distribution. This is a substantive overclaim relative to the evidence provided.

### Minor

- **Theory-to-method gap.** Theorem 4.4 analyzes the optimal *static* A under assumptions of i.i.d. Gaussian ΔW₀ and isolated submodules with stationary targets. These are acknowledged as limitations in the conclusion. However, the leap from "optimal static A spans the top eigenspace" to "online Hebbian updates improve training" is asserted rather than demonstrated. The paper does not, for instance, track how A's alignment with the principal eigenspace evolves during training, which would connect the theory to the online behavior and distinguish the method from simple static initialization.

- **Memory framing is partially misleading.** The paper's memory claims are always relative to standard LoRA (e.g., 26 vs. 30 GB in Table 3), not to LoRA-FA, which already achieves the same savings by freezing A. LoLoRA introduces extra optimizer state for the local updates, making it slightly *less* memory-efficient than LoRA-FA (24.1 vs. 23.9 GB in Table 4). The paper acknowledges this in the conclusion but the framing in the introduction and abstract obscures that the memory savings are inherited from LoRA-FA, not introduced by LoLoRA.

- **Performance reliability on GLUE.** LoLoRA drops noticeably on CoLA (66.3 vs. 69.6 for standard LoRA) and underperforms LoRA-FA (uniform) on RTE (84.6 vs. 86.4). While most tasks are competitive, the method does not consistently match standard LoRA.

### Trivial

- Algorithm 1 updates A *before* computing the output h, meaning u (computed with the old A) is used by B while A has already changed. This inconsistency in the forward pass is defensible as an online-learning practice but is not discussed, and its effect on training dynamics is unexamined.

## Nice-to-Haves
- An experiment with sequential or multi-domain data where the input distribution genuinely shifts, to validate the adaptivity claim.
- Tracking the principal angles between A's row space and the true top-r eigenspace of the input covariance during training, to empirically connect the theory to the online behavior.
- A direct comparison showing whether LoLoRA with EVA initialization outperforms LoRA-FA (EVA) — currently only tested on LLaVA (Table 4), where it does not help.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **Harsh Critic #4 ("Memory savings are not unique to LoLoRA"):** Partially incorporated as Minor weakness #3 above. The harsh critic's framing that this is a fatal or major issue is overstated — the paper does position itself relative to LoRA-FA and acknowledges the extra optimizer state.

- **Harsh Critic #5 (GLUE reliability as a stand-alone major weakness):** The CoLA and RTE drops are real but within normal experimental variation across 8 tasks. Demoted to Minor.

- **Harsh Critic: "The paper would benefit from explicitly contrasting LoLoRA's online updates with the static PCA initialization of EVA":** This is a presentation suggestion, not a substantive weakness. The paper already discusses this contrast in the introduction and ablation sections.

- **Strength Finder: "Comprehensive empirical evaluation" as an unqualified strength:** Retained but the marginal gains temper how impactful this breadth is.

## Novel Insights

The theoretical asymmetry between A and B (Theorems 4.4 and 4.5) — that A's initialization is structurally critical while any full-rank B is equivalent — is a genuinely novel insight with implications beyond this specific method. It explains why LoRA-FA (freezing A) can be harmful but freezing B would not matter, and it provides theoretical grounding for the growing body of work on LoRA initialization strategies. This asymmetry was previously observed empirically (Zhu et al., 2024) but not formally characterized.

## Suggestions

- Either remove the "distribution shift" claim from the abstract or add an experiment demonstrating it. The simplest path is to scope the claim more precisely: the method adapts A to the *current* input distribution online, which is accurate even for static data.
- Add a concrete memory breakdown comparing LoRA, LoRA-FA, and LoLoRA including local optimizer state, to make the trade-offs transparent.
- Report local update learning rate sensitivity, since this introduces a new hyperparameter dimension.

## Score and Decision

**Anchor comparison summary:**

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| EVA (DM6Q45HWSk) | 4.75 | R2 | Our paper adds theory + online mechanism; clearly stronger |
| LoRA-FA (RbKThNNFxr) | 5.33 | R1/R2 | Our paper extends this with theory and online updates; stronger |
| ReLoRA (DLJznSp6X3) | 5.75 | R1/R2 | Similar complexity; ReLoRA had clearer practical gains; our paper slightly weaker |
| LoRAM (s7DkcgpRxL) | 6.20 | R1 | More novel mechanism, stronger results; our paper weaker |
| Expressive Power of LoRA (likXVjmh3E) | 6.50 | R2 | Primarily theoretical; deeper contribution; our paper weaker |
| HiRA (TwJrTz9cRS) | 8.00 | R1 | Clearly stronger contribution with consistent gains; our paper much weaker |

The paper sits between LoRA-FA (5.33) and ReLoRA (5.75), closer to ReLoRA due to its theoretical contribution but held back by the marginal empirical advantage and the untested distribution-shift claim. Score: **5.0**.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>