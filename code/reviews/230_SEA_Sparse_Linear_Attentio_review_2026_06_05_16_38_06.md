# Review of papers/230_SEA_Sparse_Linear_Attentio.md

Now I have enough detail to write the final review. Let me synthesize the findings.

---

## Summary

SEA introduces a linear-complexity attention mechanism that uses a Performer-based encoder and CNN decoder to estimate a compressed attention matrix (T × K), applies grouped top-k selection to build a sparse mask, and performs final sparse attention via a novel FlatCSR operation. Training uses rich multi-objective knowledge distillation from a pretrained quadratic teacher, including direct supervision on the attention matrix. The approach is evaluated on OPT (causal language modeling, Wikitext-2) and BERT (GLUE text classification), showing state-of-the-art efficiency–accuracy trade-offs among linear attention methods tested.

---

## Strengths

1. **Memory reduction with competitive/superior perplexity (Table 2):** For OPT-1.3B, SEA achieves 13.5 PPL vs. 13.9 for vanilla while using 499 MB vs. 1120 MB. For OPT-125M, PPL improves from 29.2 to 26.0 with memory cut from 408 MB to 187 MB — a concrete, quantified demonstration of the main claim.

2. **FlatCSR sparse format engineering (Table 3):** FlatCSR achieves 11.4 ms latency vs. 75.66 ms for COO (6.63× speedup) and 817.5 MB vs. 1194 MB memory — a solid, reproducible systems contribution with clear numbers.

3. **Post-training k flexibility (Fig. 6):** Increasing k after training without retraining consistently improves perplexity and eventually surpasses the vanilla quadratic baseline, demonstrating a practically useful deployment-time adaptability property.

4. **Strong GLUE results with five baselines (Fig. 7a, Table A.8):** SEA outperforms Reformer, Sinkhorn, Performer, Cosformer, and Synthesizer on all tested GLUE subsets, coming within 0.1% of quadratic attention on MNLI — a broader and more credible comparison than the language modeling table.

5. **Interpretable attention visualization (Fig. 9):** The compressed attention matrix closely resembles the teacher's attention for both bi-directional (BERT/MNLI) and causal (OPT/Wikitext-2) settings, supporting the interpretability claim concretely.

---

## Weaknesses

### Fatal
None.

### Major

- **Training regime confound in Table 2:** SEA is trained with a rich multi-objective KD loss (Eq. 1: $\mathcal{L}_\text{approx}$, $\mathcal{L}_\text{prob}$, $\mathcal{L}_\text{context}$, $\mathcal{L}_\text{kd}$, $\mathcal{L}_\text{kd,task}$, $\mathcal{L}_\text{task}$) including direct attention matrix supervision from the quadratic teacher. The baselines, Reformer and Performer, are trained "for the same 10k steps" (Table 2 caption), but the paper never states whether they receive the same layerwise KD objective or only the task loss. Since Reformer and Performer cannot straightforwardly receive the attention matrix distillation term (this is an explicit design motivation for SEA; see §1 and §3.2), the gap in Table 2 conflates architectural quality with training regime. The paper correctly frames "KD-enabled training" as a *feature* of SEA, but as presented it cannot determine how much of the ~47% PPL gap over Performer is attributable to architecture vs. the richer training signal. Training a Performer or Cosformer student under the same layerwise KD objective (even approximately) would substantially clarify the picture.

- **Ambiguity of "surpasses quadratic baseline" claim:** Table 2 shows SEA at 26.0 PPL vs. vanilla OPT-125M at 29.2. The abstract highlights this as a main result. However, it is unclear whether "Vanilla" in Table 2 refers to pretrained OPT-125M evaluated directly (no fine-tuning on Wikitext-2) or fine-tuned for 10k steps. The Table 2 caption says "we trained the same number of steps (10k) for each method," but all four entries are Reformer, Performer, SEA, and Vanilla — and "training" Vanilla would mean domain-adapting OPT on Wikitext-2. If the Vanilla OPT is the off-the-shelf pretrained model, then SEA benefits from both the KD fine-tuning and architectural change relative to the unfine-tuned baseline. A fine-tuned quadratic OPT-125M on Wikitext-2 for 10k steps is required to disentangle these effects.

- **Narrow baseline set in language modeling table:** Table 2 contains only Reformer and Performer. The GLUE comparison (Table A.8) uses five baselines. The paper discusses Cosformer, Scatterbrain, BigBird, and Synthesizer in §2, and Cosformer is tested in GLUE — its absence from Table 2 leaves the primary language modeling result resting on comparison to just two methods. The paper gives a brief justification ("two representative baselines"), but this is insufficient given that the abstract's strongest claim is anchored to this table.

### Minor

- **No quantitative ablation for CNN decoder:** The paper asserts "The CNN is a necessary part of SEA" (§3.1) and shows qualitative Fig. 3, but no ablation compares CNN decoder vs. MLP-only decoder quantitatively. Given the added architectural complexity, this is worth at least a single number.

- **Output mixing term ($s_\text{mix}$) contribution not isolated:** The final output $C_\text{sea}$ blends sparse attention output and global pooling via learned $s_\text{mix}$ (§3.1.1). No ablation isolates this term, making it unclear how much of the gain is from the sparse pathway vs. the global pooling fallback.

- **Latency regime qualification buried:** SEA at OPT-125M is 6.76 ms vs. 4.88 ms for vanilla — SEA is slower (Table 2). Fig. 8 shows the crossover is around sequence length $2^{13}$. The introduction's efficiency framing does not prominently note this regime dependency; practitioners may be misled.

### Trivial

- §4.3 calls the post-training k improvement "surprising" but provides no mechanistic discussion. A brief hypothesis (e.g., trained weights preserve full attention knowledge that can be recovered with more sparse slots) would improve the section.

---

## Nice-to-Haves

- Include a fine-tuned quadratic OPT-125M baseline on Wikitext-2 (same 10k steps, task loss only) to separate the fine-tuning benefit from the architectural benefit, especially for the "surpasses vanilla" claim.
- Train Performer with the same layerwise KD objective as SEA and add it as an additional baseline; this would directly quantify how much of the performance gain is architectural vs. training regime.
- Add at least one additional language modeling baseline from those tested on GLUE (e.g., Cosformer) to strengthen Table 2.
- Extend §4.3 with a brief analysis of why post-training k increase can surpass vanilla — the behavior is important for understanding SEA's generalization properties.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **"Framing overstates contrast" (Harsh Critic — Abstract):** The critic argues that SEA "also requires fine-tuning" and therefore the motivation that "previous methods cannot be easily swapped" is overstated. However, the paper's distinction is real: previous methods require retraining attention relations from scratch, while SEA uses KD directly on the attention matrix. This is a genuine architectural difference, not a misleading framing. Removed.

- **V_I ablation missing (Harsh Critic — §3.1):** The critic notes that including $V_I$ in $V_\text{cat}$ is unablated. This is a minor design detail and the intuition (FAVOR+(Q, K, I) ≈ QK^T) is well-grounded. Demanding an ablation for every design choice inflates weakness lists without adding substantive critique. Moved to minor/nice-to-have level.

- **Strength: "interpretability maintained" (Strength Finder):** Kept as a strength — Fig. 9 provides direct visual evidence and the claim is concrete to this paper.

- **Strength: "SEA opens the possibility of running large transformers on resource-limited devices" (generic significance statement):** Too generic. The memory savings are concrete (499 MB vs. 1120 MB for OPT-1.3B) but the "resource-limited device" framing is vague. Removed as a standalone strength; subsumed into the memory-reduction strength.

---

## Novel Insights

The most genuinely novel observation in this paper is the post-training k adjustment property (§4.3, Fig. 6): a model trained with k=64 can, without any retraining, be re-run at k=2048+ and surpass the quadratic teacher's perplexity. This suggests that the SEA training procedure — particularly the layerwise KD from the quadratic attention matrix — embeds richer token-relationship information into the network weights than is expressed by the sparse mask at training time. This "latent richness" property is architecturally interesting and could have implications for adaptive inference systems that dynamically trade off accuracy vs. compute at deployment time based on available resources. The reviewers flag it as "surprising" without explanation; the paper would benefit from a mechanistic discussion, as this could be a secondary contribution in its own right.

---

## Suggestions

1. **Explicitly state training conditions for baselines in Table 2:** Clarify whether Reformer and Performer receive only task loss or also KD losses, and from which pretrained initialization. This single clarification substantially changes interpretability of the main result.
2. **Add fine-tuned vanilla OPT to Table 2:** Fine-tune vanilla OPT-125M for 10k steps on Wikitext-2 with task loss and report its PPL. If SEA still outperforms, the claim is much stronger.
3. **Add Cosformer to Table 2** (it's already tested on GLUE, so marginal cost is low).
4. **Report CNN ablation quantitatively:** A single row in the ablation table comparing MLP-only vs. CNN decoder would address the "necessary part" claim empirically.
5. **Clarify the k post-training phenomenon** with at least a paragraph of analysis in §4.3.

---

## Evaluation on Key Axes

- **Originality:** Moderate-to-high. Combining Performer encoding + CNN decoder + top-k sparse attention + KD from teacher attention matrix is a novel composition. FlatCSR is an original engineering contribution.
- **Importance of research question:** High. Efficient attention for long-sequence transformers is an active and practically significant area.
- **Claim support:** Moderate. GLUE results are well-supported (5 baselines, multiple datasets). Language modeling results are less well-supported due to the KD confound and narrow baseline set.
- **Soundness of experiments:** Moderate. Training setup is underspecified for the critical Table 2 comparison. The "surpasses vanilla" framing requires a clarification of what "vanilla" entails. GLUE experiments are more rigorous.
- **Clarity of writing:** Good overall, with §3.1–3.2 being technically dense but navigable. The latency regime dependency is undersold.
- **Value to research community:** Real. If the KD confound is addressed, SEA would represent a meaningful advance for adapting pretrained transformers to long-sequence settings with memory constraints.

---

## Score and Decision

The paper presents a technically interesting method with genuine practical contributions (FlatCSR, KD-enabled training pipeline, post-training k flexibility). The GLUE results are reasonably convincing, and the memory savings are concrete. However, the main language modeling result in Table 2 — the paper's headline claim — is undercut by: (1) an undisclosed and potentially asymmetric training regime across methods, (2) ambiguity about whether the vanilla quadratic baseline received the same fine-tuning, and (3) reliance on only two baselines. These are not fatal flaws (the GLUE table partially compensates), but they mean the strongest claims cannot be taken at face value without additional clarification. The required additions are feasible and would substantially change the evidential picture.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>

**Predicted score: 5.0**
