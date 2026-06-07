Now I have sufficient anchors. Let me finalize the review.

**Round 1 Bracket:** 4.5–6.5, based on comparison with MORE (4.00), MoLE (5.00), PERFT (5.33), MoLEx (6.33), and Parameter-Efficient Fusion (7.00).

**Round 2 Narrowing:** Comparing against MeteoRA (6.20, Accept), MoLEx (6.33, Accept), Seeded LoRA (5.00, Reject), and PERFT (5.33, Reject):

Our paper is clearly stronger than MORE (4.00) and Seeded LoRA (5.00) due to broader evaluation, novel RSL loss, and principled gradient derivation. It is comparable to PERFT (5.33) but with a more principled technical contribution (RSL entropy regularization vs. PERFT's design-space exploration). It is slightly below MeteoRA (6.20) — MeteoRA has stronger engineering (CUDA kernel, 28 adapters) while our paper has a more principled loss but weaker ablation discipline. It is below Parameter-Efficient Fusion (7.00), which has stronger theoretical backing.

**Final score: 5.5.** The paper has a genuine technical contribution (RSL loss), broad evaluation, and useful data-efficiency results, but the evaluation conflates architectural placement with the loss function, SSM adaptation is unspecified, and the cross-model transfer experiment lacks justification.

---

## Summary

LoRA-Mixer proposes a mixture-of-experts framework for composing LoRA adapters by placing experts on the linear projection layers (Q/K/V/O) of attention modules rather than on FFN blocks or parallel branches. Its main technical contribution is the Routing Specialization Loss (RSL), which augments standard MoE auxiliary loss with an entropy regularization term to promote input-aware expert specialization while maintaining load balance, supported by gradient derivations (Eq. 7–9). The paper evaluates across 15 benchmarks on three base models (Falcon-Mamba-7B, Mistral-7B, LLaMA3-8B) and demonstrates data efficiency (Table 9) and plug-and-play reuse of frozen LoRA modules (Table 3).

## Strengths

- **RSL loss formulation is clean, well-motivated, and the paper's strongest contribution.** The entropy regularization term (Eq. 5) adds a principled, token-level gradient signal (Eq. 9) absent from standard auxiliary losses. Table 8 provides evidence that, under identical 2k training data conditions, RSL outperforms GMoE, DS-MoE, and AESL by substantial margins (e.g., 57.32 vs. 50.46 on HumanEval). The data-efficiency gains are clearly shown in Table 9: RSL reaches 79.26 average with 2k samples, while the no-RSL variant needs 4k to reach comparable performance (79.14).
- **Plug-and-play routing over frozen LoRAs is demonstrated as a practical capability.** Table 3 shows LoRA-Mixer composing five off-the-shelf LoRA modules from LoRAHub under Flan-T5 with frozen expert parameters and only 2k routing-training examples, outperforming single-LoRA fine-tuning on 4 of 5 GLUE tasks (e.g., CoLA: 82.14 vs. 80.54, MRPC: 85.15 vs. 83.76).
- **Architectural placement on projection layers is a genuine design distinction** from prior LoRA-MoE work (MixLoRA targets FFN; MoLE uses parallel output-fusion). The Falcon-Mamba-7B results in Table 2, where MixLoRA is explicitly inapplicable, provide some evidence of architectural flexibility, though the SSM mapping details are unspecified (see Weaknesses).
- **Expert load visualizations provide mechanistic insight.** Figure 4 shows per-task expert activation patterns with vs. without RSL, directly visualizing that RSL produces input-aware specialization (different experts dominate different tasks) while no-RSL yields near-uniform activations.

## Weaknesses

### Fatal
None.

### Major

- **The architectural placement contribution and the RSL loss contribution are never disentangled.** The paper makes two simultaneous claims: (a) placing LoRA experts on Q/K/V projection layers is superior to FFN-based or parallel-branch placement, and (b) RSL is a better routing loss. No experiment isolates the placement decision. A controlled ablation would hold the router and RSL constant and vary only whether experts are applied to projection layers vs. FFN layers vs. parallel branches. Without this, the reader cannot determine whether the gains in Table 2 come from the projection-layer placement, from RSL, or from their combination. Given that the projection-layer placement is presented as the key architectural novelty (Figure 1, §3.2), this is a significant evidential gap.
- **SSM compatibility is claimed but never specified.** The paper repeatedly claims compatibility with state-space models and uses Falcon-Mamba-7B as a testbed, but there is no description of how LoRA-Mixer maps onto Mamba's architecture. Mamba blocks have input projection, state projection, and output projection matrices with different dimensionalities and semantics from Transformer Q/K/V. Which projections receive LoRA-Mixer experts? How does routing interact with the recurrent state computation? Without this specification, the Falcon-Mamba results cannot be interpreted or reproduced, and the claim of architecture-agnostic design is unsubstantiated.
- **The cross-model transfer experiment (Table 5) lacks justification and shows mixed results.** LoRA adapters are trained as low-rank deltas to specific base weight matrices. Transferring LoRA parameters trained on Mistral-7B directly to LLaMA3-8B has no well-defined relationship to the target model's weights. The paper offers no justification for why this transfer should work. Results are mixed: the transferred model underperforms the LLaMA3 baseline on ARC-E (85.89 vs. 88.45, a relative drop) while showing modest gains on GSM8K and ARC-C. The paper should explain what exactly is being transferred (router weights, expert weights, or both) and why this is expected to be meaningful.

### Minor

- **The $\mathcal{F}_{\text{route}}$ operation in Eq. (4) is not explicitly defined in that equation**, though the mechanism can be pieced together from Eq. (2) (standard MoE weighted-sum) and §3.3 (soft expert fusion during training, sparse top-K during inference). The paper's central forward-pass equation should be self-contained.
- **The headline "48% of trainable parameters" claim is not supported by parameter counts in the main paper.** The main text references appendices A.4 and A.7, but a headline quantitative claim repeated in both abstract and introduction should be substantiated by at least a summary table in the main paper body.
- **The headline gains (+3.79%, +2.90%, +3.95%) are best-case cherry-picks.** Examining Table 2 across all three model groups, the modal improvement over the best baseline is approximately 0.5–2.0 percentage points. On Falcon-Mamba, gains over the simple LoRA baseline are under 1 point on several tasks (e.g., Medical: 78.01 vs. 77.26; CoLA: 85.91 vs. 85.62). The abstract's framing overstates the typical gain.
- **The "LoRA" baseline in Table 2 is ambiguous.** It is unclear whether this is a single multi-task LoRA trained on all data, or per-task LoRAs composed without routing. If it is a single LoRA, then LoRA-Mixer uses E× more adapter parameters, making the parameter comparison central to interpreting the gains.
- **The hard-routing training regime (§3.2) reduces to independently training each LoRA on its own domain** when domain labels are available. This is presented as a feature of the MoE framework but is essentially standard per-task LoRA training — no actual mixture happens during this phase.
- **The plug-and-play experiment (Table 3) is underdeveloped** relative to its importance. Only 5 LoRAs on 5 GLUE tasks are tested, and LoRA-Mixer loses to single-LoRA fine-tuning on QQP (84.75 vs. 85.55). This experiment should be the centerpiece if plug-and-play reuse is a primary motivation.
- **The specialization analysis in Figure 4 uses only 3 tasks and 5 experts**, and the paper does not explain how these were selected or whether the pattern generalizes.
- **The value of λ (entropy regularization coefficient) is never reported**, and no sweep over λ is shown. Given the delicate balance RSL involves between load-balancing and specialization, this is important for reproducibility.

### Trivial

- The loss name is inconsistent: "Router Specialization Balancing Loss" (abstract) vs. "Routing Specialization Balance Loss" (§3.3).
- Standard deviations are not reported for the main results in Table 2, despite the paper stating experiments are run 3 times.

## Nice-to-Haves
- An ablation applying RSL as a drop-in replacement for auxiliary losses in existing LoRA-MoE architectures (e.g., MixLoRA or MoLE) to cleanly isolate RSL's contribution from the LoRA-Mixer architecture.
- Scaling up the plug-and-play experiment (Table 3) with more LoRAs and tasks, and a direct comparison against LoRAHub as a method (not just as a source of LoRAs).
- Reporting the actual λ value used and showing a sensitivity sweep.

## Removed Points
These points are flagged to be removed, treat them with caution.

- **Harsh Critic claim that $\mathcal{F}_{\text{route}}$ is "never specified — a structural gap at the heart of the method"**: REMOVED as a fatal claim. The routing mechanism is described: Eq. (2) defines the standard MoE weighted-sum over top-K experts, and §3.3 specifies "soft expert fusion" during training and "sparse top-K fusion" during inference. The information is present, just not consolidated in Eq. (4). Demoted to Minor.
- **Harsh Critic's demand for "variance/standard deviations" for all main results**: REMOVED as a standalone major concern. Kept as Trivial.
- **Harsh Critic's criticism about MixLoRA having "gradient entanglement issues" and MoLE "lacking sparse routing" being "cursory and underspecified"**: REMOVED. These are brief characterizations in related work — standard in conference papers.
- **Harsh Critic's concern about fairness of comparison against GMoE, DS-MoE, and AESL (hyperparameter tuning)**: REMOVED. The paper states all experiments use the same training data (2k) and vary only the loss — a clean ablation design. The speculation about unfair hyperparameter settings is ungrounded.
- **Harsh Critic's claim that Figure 3 "shows essentially uniform loads... does not demonstrate specialization"**: REMOVED. The paper uses Figure 3 to demonstrate load balancing and Figure 4 to demonstrate specialization — this is by design, not a flaw.
- **Strength Finder's framing of cross-model transfer as "validating modularity and robustness"**: REMOVED. Table 5 shows mixed results with a clear ARC-E failure.
- **Strength Finder's claim about Falcon-Mamba being "the single most persuasive piece of evidence"**: WEAKENED. The margins over the simple LoRA baseline are modest (often <1 point), and SSM adaptation details are unspecified.

## Novel Insights
None beyond the paper's own contributions. The RSL loss with its entropy-gradient derivation (Eq. 7–9) and the information-bottleneck framing for routing are the paper's own contributions that the reviews confirm as well-motivated.

## Suggestions
- The paper would be substantially stronger if the two innovations (architectural placement and RSL loss) were disentangled. Either apply RSL to existing LoRA-MoE architectures (MixLoRA, MoLE) to isolate the loss's contribution, or run a placement ablation (Q/K/V vs. FFN vs. parallel) with RSL held constant.
- If plug-and-play LoRA reuse is the primary motivation, scale up Section 4.3 substantially with more LoRAs, more tasks, and a direct comparison against LoRAHub as a method.
- The cross-model transfer experiment (Table 5) needs a clear explanation of what is transferred and why it is expected to work, or should be removed.

## Anchor Comparison

| Anchor Paper | Score | Round | Comparison |
|---|---|---|---|
| MORE (Mixture of Low-Rank Experts) | 4.00 | R1 | Our paper is stronger: broader eval (15 benchmarks vs. GLUE only), principled RSL loss, modern LLMs |
| MoLE (Mixture of LoRA Experts) | 5.00 | R1 | Our paper is stronger: broader eval, principled loss with gradient derivation, data efficiency analysis |
| Seeded LoRA | 5.00 | R2 | Our paper is stronger: more principled routing mechanism, broader model/testing coverage |
| PERFT | 5.33 | R1/R2 | Comparable: both have framework contributions; our RSL loss is more principled than PERFT's design-space exploration |
| MeteoRA | 6.20 | R2 | Our paper is slightly weaker: MeteoRA has stronger engineering (CUDA kernel, 28 adapters), comparable evaluation breadth; our RSL is more principled but ablated less rigorously |
| MoLEx | 6.33 | R2 | Our paper is slightly weaker: MoLEx has a more novel architectural idea (layers as experts) with theory; our evaluation is broader on modern LLMs |
| Parameter-Efficient Multi-Task Model Fusion | 7.00 | R2 | Our paper is clearly weaker: that paper has stronger theoretical backing (NTK) and clearer hypothesis testing |

**Round 1 Bracket:** 4.5–6.5. **Round 2 narrowed to:** 5.0–6.0, centered near 5.5 — above PERFT (5.33) and MoLE (5.00) due to principled loss and broader evaluation, but below MeteoRA (6.20) and MoLEx (6.33) due to weaker ablation discipline, unspecified SSM adaptation, and conflated claims.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>