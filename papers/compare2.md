```markdown

1. 他们的review非常generic（看附录的例子）自己批判generic但是自己就是非常generic的，这是非常严重的，这个不是一般的深度不够，而是几乎全是废话，去掉grounding之后对于任何paper都成立
2. 共用一个meta rubic这种东西必然导致同质化的review，这不单单导致generic，还会导致同质化，这不是metric好不好的问题，是一个关于reeview agent质量的问题
3. shared rubic用来生成review，paper specific rubic用来judge，这两个rubic很大程度是重叠的，当然效果好
4. 用一个微调的小模型来draf没有意义，这个小模型性能非常差（我看过），可能拉低了整体质量，而且小模型学到的更加generic
5. 数值比较只做了MSE，MAE没有做correlation，review分数这种东西非常中心化，我试过always predict 6的MAE也只有1.3.
6. 混淆了grounding和valid，一个weakness可以不grounding但是valid（这篇论文的motivation不成立）也可以grounding但是不valid（论文Section 3.1测试了3x3 CNN但是没有测试5x5 CNN）
```


Review from REVIEWGROUNDER
Summary:
The paper proposes SEA (Sparse linear Attention with Estimated Attention mask), a test-time
linear-complexity attention module. SEA first estimates a compressed T × K attention matrix
using Performer-based kernel attention and a 3-layer CNN decoder, then generates a sparse mask
via a novel grouped top-kˆ selection (per-query, per-head, per-batch, causal-per-batch) and
interpolates it to a full T × T mask. Sparse attention is computed with a custom FlatCSR format
that exploits the mask structure. Knowledge-distillation losses (Eq. 1) align the compressed
matrix, the sparse attention, and the context features with a pretrained quadratic teacher.
Experiments on OPT-125M (Wikitext-2) and BERT-base (GLUE) show that SEA matches or exceeds the
quadratic teacher (e.g., 0.1% GLUE-MNLI gap, lower perplexity than the teacher on OPT-125M) while
using 81% less memory and 33% of the latency at sequence length 2
13. Dynamic-k experiments
demonstrate that increasing k after training improves accuracy and can surpass the teacher. The
FlatCSR implementation yields a 6.6× speedup over a COO baseline.
Strengths:
1. Introduces a two-phase linear-attention pipeline (kernel-based estimation + sparse mask) with
provable O(T) inference cost (Section 3.1, Fig. 1).
2. Provides a concrete knowledge-distillation training scheme (Eq. 1) that preserves the
teacher’s dynamic attention patterns.
3. Proposes FlatCSR, a modified CSR format that leverages the grouped top-k mask, achieving up to
6.6× faster sparse operations than COO (Table 1).
4. Empirically demonstrates state-of-the-art results on language modeling (Table baseline.opt)
and GLUE (Table baseline.glue), with faster convergence (Fig. exp.figure.opt_curve).
5. Shows that the sparsity hyper-parameter k can be increased post-training to improve accuracy
(Section 4.3, Fig. exp.figure.opt_dynamic_k, exp.figure.bert_dynamic_k).
6. Offers interpretability via visualized estimated attention (Fig. exp.figure.attention) and
provides the FlatCSR code.
Weaknesses:
1. Adaptation cost not fully quantified – While Section 3.3 describes replacing the teacher’s
attention with SEA and fine-tuning via KD, the paper does not report the additional training
time, data size, or compute needed for this adaptation, which may limit plug-and-play
applicability. (Section 3.3)
2. Limited model and task diversity – Experiments are confined to OPT-125M/1.3B for causal LM and
BERT-base for GLUE. Broader evaluation on larger LLMs (e.g., GPT-2/3) or vision transformers
would strengthen claims of generality. (Section 4)
3. CNN decoder architecture details missing – The decoder is said to be a 3-layer 2-D CNN with
channel-expansion ch and width-reduction cs, but kernel sizes, strides, padding, and channel
counts are omitted, hindering reproducibility. (Section 3.1, “CNN Decoder”)
4. Computational overhead not fully broken down – The latency breakdown (Fig.
exp.figure.complexity bottom) shows percentages for dense, FlatCSR, and other ops, but
absolute FLOP counts for the Performer encoder, CNN decoder, and top-k selection are absent,
making it hard to assess the true cost of the estimator. (Fig. exp.figure.complexity)
5. Hyper-parameter selection guidance limited – The paper provides an ablation for grouping
strategies (Table method.table.ablation_k) and dynamic-k results, yet offers no systematic
procedure for choosing K or the base k for new tasks, nor analysis of sensitivity to these
choices. (Table method.table.ablation_k, Section 4.3)
6. Scalability beyond 2
13 not explored – Memory and latency are shown up to sequence length 2
13
;
experiments on longer sequences (e.g., 2
15 or more) would better demonstrate linear scaling
claims. (Fig. exp.figure.complexity)
7. Comparative positioning could be richer – Related works such as SLA (hybrid sparse-linear for
diffusion models) and SPARSEK (learnable differentiable top-k) address similar efficiency
goals. Direct empirical comparison or discussion of trade-offs would clarify SEA’s niche.
(Related-work summaries)
Questions:
1. What is the exact training budget (GPU hours, dataset size) required to replace a pretrained
transformer’s attention with SEA via the KD procedure described in Section 3.3?
2. Can the authors provide the full CNN decoder specification (kernel size, stride, padding,
number of channels per layer) to enable exact replication?
3. How do FLOP counts for the Performer encoder, CNN decoder, and grouped top-k selection compare
to a vanilla quadratic attention layer for a typical sequence length (e.g., T = 8192)?
4. What guidelines do the authors recommend for selecting the compressed width K and base
sparsity k when adapting SEA to a new model or task?
5. Have the authors evaluated SEA on sequence lengths larger than 2
13 to confirm the claimed O(T)
scaling in practice?
6. How would SEA perform against recent hybrid methods such as SLA or SPARSEK that also combine
sparse and linear components, especially in terms of interpretability and training overhead?
Rating: 5.5
Decision: reject

Review from Split_Claude:
========================================================================
FINAL REVIEW
========================================================================
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

Predicted score: 5.0


Review from Split D:

========================================================================
FINAL REVIEW
========================================================================
## Summary
SEA proposes a method to replace quadratic attention in pretrained transformers with a linear-complexity alternative at inference time. The core pipeline: (1) use Performer (kernel-based linear attention) with a CNN decoder to produce a compressed attention matrix of size T×K (K≪T), (2) apply grouped top-k̂ selection to form a sparse binary mask, (3) interpolate the mask to T×T space, and (4) perform sparse attention. Training uses multi-level knowledge distillation from the pretrained quadratic teacher. The paper evaluates on Wikitext-2 language modeling (OPT-125M) and GLUE classification (BERT-base), reporting competitive performance with substantially lower memory, plus a novel FlatCSR sparse format.

## Strengths
- **Genuinely novel architecture combining kernel-based and sparse attention with KD**: The pipeline — Performer → CNN decoder → compressed attention → top-k̂ selection → sparse mask → sparse attention — is creative and well-motivated. Using KD to distill teacher attention patterns into the compressed estimate is a clean solution to the problem that prior linear attention methods cannot straightforwardly benefit from attention-matrix distillation (Section 3, Fig. 2).
- **Linear memory scaling verified empirically**: Fig. 8 (top-left) demonstrates O(T) peak VRAM scaling, with 81.05% reduction vs. quadratic attention at T=2^13, and continued operation beyond sequence lengths where quadratic attention runs out of memory (Section 5).
- **Dynamic k adjustment is a practically useful property**: Section 4.3 and Fig. 7b show that k can be increased post-training to improve accuracy without further gradient updates — all SEA models trained at k=32,64,128 surpass the vanilla teacher's perplexity of 29.2 when k is relaxed. This deployment flexibility is not offered by prior linear attention methods.
- **FlatCSR is a concrete engineering contribution**: The novel CSR tensor format achieves 6.63× speedup over COO sparse format (Section 5, Table 3), with latency breakdown showing FlatCSR sparse operations at 46.28% of total vs. COO's 86.68% (Fig. 8 bottom).
- **Clean ablation validates design choices**: Table 1 ablates four grouping strategies for top-k̂ selection across three k values on GLUE-MNLI, with causal-per-batch consistently performing best, justifying the default used in main experiments.
- **Multi-architecture validation**: Method is evaluated on both decoder-only (OPT for causal LM) and encoder-only (BERT for GLUE classification) architectures, with comparison against five baselines (Reformer, Sinkhorn, Performer, Cosformer, Synthesizer) on GLUE.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor
- **Abstract-body mismatch on model scale**: The abstract prominently claims SEA "achieves better perplexity than OPT-1.3B, using roughly half the memory of OPT-1.3B" (line 19), but the main body describes experiments exclusively on OPT-125M (Section 4.1, Fig. 5, the text around line 145). The OPT-1.3B results appear to reside only in appendix tables (Tables 2, A.8). This creates a structural gap where the paper's strongest headline claim is not substantiated by the main text the reader can inspect. Either the OPT-1.3B experiment should be described in the body, or the abstract should be aligned with what the body presents.
- **Key architectural components are not ablated**: The CNN decoder is described as "a necessary part of SEA" (line 80) and the V_I trick (passing an interpolated identity matrix to Performer, line 78) is motivated as potentially enabling "more accurate estimation." Neither component is ablated. Without these ablations, the reader cannot assess whether these design choices are load-bearing or incidental.
- **Language modeling baselines are thin**: Only Reformer and Performer are compared on Wikitext-2 (Section 4.1). Cosformer, Linear Transformer, and other linear attention methods evaluated on GLUE are absent from the LM comparison. Scatterbrain — the closest prior work combining sparse and kernel-based approaches — is discussed in related work (line 56) but never evaluated as a baseline.
- **Grouped top-k̂ ablation is limited to MNLI**: Table 1 validates the causal-per-batch strategy only on GLUE-MNLI. The causal variant's behavior may differ for language modeling (where causality is structurally enforced), but no LM ablation is provided.
- **Training cost is opaque**: Equation (1) and line 139 reveal that training computes the dense student attention A_i = σ(Q_i K_i^T) — an O(T^2) operation. The paper never states training complexity explicitly, nor reports training wall-clock time or memory, making it difficult to assess the practical cost of adopting SEA.
- **Interpretability claim rests on qualitative visualization only**: Section 6 and Figs. 9-10 show attention heatmaps that qualitatively resemble the teacher's, but no quantitative metric (correlation coefficient, MSE, etc.) is reported for the match between estimated and teacher attention. The claim that SEA "maintains an interpretable attention matrix" (abstract, line 19) would be strengthened by quantitative evidence or a concrete downstream interpretability use case.

### Trivial
- The paper references Fig. 6 in Section 4.3 for the dynamic-k result on Wikitext-2, but Fig. 6 is not present in the main body (visualized figures stop at Fig. 5, then jump to Fig. 7). Presumably in the appendix, but the reference numbering is confusing for main-text readers.

## Nice-to-Haves
- A KD-controlled baseline (quadratic student trained with the same distillation losses as SEA) would help isolate how much of SEA's performance comes from multi-level KD vs. the attention mechanism itself, though this goes beyond the paper's core contribution claim.
- Extending evaluation to a genuinely long-context task would strengthen the practical motivation, since the paper's key selling point is linear complexity for long sequences.
- A quantitative metric for attention matrix fidelity (e.g., Pearson correlation between estimated and teacher attention) would complement the qualitative visualizations in Section 6.

## Removed Points
These points were flagged by reviewers but are removed from the final review:

- **"KD confound makes the attention mechanism comparison unfair"** — REMOVED. This misreads the paper's contribution. The paper's core claim is about the full SEA pipeline (linear attention + KD), not about the attention mechanism in isolation. KD is an integral part of the method, so comparing SEA (which includes KD) against the vanilla quadratic teacher (which serves as the KD teacher) is a valid evaluation of whether the full method preserves teacher performance.
- **"Linear complexity claim needs more careful accounting because the mask is T×T"** — REMOVED. The paper explicitly addresses this (line 94-95): the interpolation from compressed M̂ to M* has linear complexity because it only operates on the nonzero indices. The FlatCSR format (Section 5) is designed specifically for this purpose, and Fig. 8 provides a detailed latency breakdown confirming linear scaling. No methodological gap exists here.
- **"Fig. 6 is missing from the main body" as a substance criticism** — moved to Trivial. This is an appendix placement issue, not a content problem. Per review guidelines, critiques about stripped appendix content are excluded from substantive weakness assessment.
- **"CNN hyperparameters (c_s, c_h, d') not specified in main text"** — REMOVED. These are implementation details reasonably deferred to the appendix; their absence from the main text does not affect understanding of the method.
- **Demand for confidence intervals / larger datasets / user studies** — REMOVED. These are scope-creep critiques: single-run evaluation on Wikitext-2 and GLUE is standard in the efficient-attention literature.

## Novel Insights
None beyond the paper's own contributions. The core insight — that kernel-based linear attention can produce a compressed attention estimate suitable for KD from a quadratic teacher, which in turn enables sparse attention with strong performance — is the paper's own contribution and is well-articulated.

## Suggestions
- Resolve the abstract-body mismatch: either add a paragraph in Section 4.1 summarizing the OPT-1.3B results (with perplexity, memory, and baseline comparisons), or revise the abstract to reflect the OPT-125M evidence that the body actually presents.
- Add ablations for the CNN decoder and V_I trick — even a single-row table showing performance with and without each component would substantially strengthen the method's empirical grounding.
- Include Scatterbrain as a baseline in at least one experiment, since it is the closest prior work (combining sparse + kernel methods) and is discussed in related work.
- Report training cost (wall-clock time, peak memory) to give readers a complete picture of SEA's practical trade-offs.

## Score and Decision
The paper presents a genuinely novel and well-motivated method for linear-complexity attention that leverages KD to preserve pretrained attention quality. The empirical results on OPT-125M and BERT-base show the method works, and the FlatCSR format is a solid engineering contribution. The dynamic k adjustment property is practically valuable. However, the abstract makes a headline claim (OPT-1.3B) not substantiated in the body, several key components lack ablations, the LM baselines are sparse, and training cost is opaque. These are addressable issues that do not undermine the core contribution but collectively weaken the paper's empirical rigor.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>

Predicted score: 6.0