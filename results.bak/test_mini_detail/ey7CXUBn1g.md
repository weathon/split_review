Now I have a solid calibration. Let me write the full consolidated review.

## Summary

2-3 sentence summary of the paper's contribution.

## Strengths
- strength 1 with evidence
- strength 2 with evidence

## Weaknesses
// List only reasonable points. Rank by severity.
// Not every paper has weaknesses at every tier. Leave a tier empty (or write "None") if nothing applies.

### Fatal
// Errors that invalidate the paper's core claims or results.
// Examples: fundamentally flawed methodology, unsupported central claim, incorrect proofs, data fabrication concerns.
// Most papers have none. Leave empty if none apply.

### Major
// Issues that a reviewer would weigh against acceptance, and that the authors should fully resolve in a rebuttal.
// Examples: missing critical baseline, overclaimed scope unsupported by experiments, significant methodological gap.
// Not every paper has major weaknesses. Do not invent them to fill this section.

- weakness 1 — why it matters
- weakness 2 — why it matters

### Minor
// Issues worth the authors' attention but unlikely to change an accept/reject decision.
// Examples: addressable in rebuttal, limited scope of one experiment, unclear phrasing of a claim, missing ablation that would strengthen but not invalidate.

- weakness 1 — why it matters

### Trivial
// Small issues the authors should fix but that carry no weight in evaluation.
// Examples: typos, minor notation inconsistencies, suboptimal figure choices, small presentation issues.

- weakness 1

## Nice-to-Haves
- suggestion that would improve but is not a core flaw

## Removed Points
Include something like this "These points are flagged to be removed, treat them with caution"
Weaknesses that are removed keep the details of the S/W just in case they are useful 

## Novel Insights
One paragraph synthesizing genuinely novel observations.
If no genuinely novel insight emerges from the reviews beyond the paper's own contributions, write
"None beyond the paper's own contributions."

## Suggestions
- specific actionable suggestion

Let me compose now.## Summary

AdaSVD proposes two techniques for post-training SVD-based LLM compression: **adaComp**, which compensates truncation error by alternately updating $\mathcal{U}$ and $\mathcal{V}^\top$ via Moore-Penrose pseudoinverse on a calibration set, and **adaCR**, which assigns layer-specific compression ratios based on cosine similarity between each layer's input and output. On LLaMA2-7B at 40% compression, AdaSVD achieves WikiText-2 perplexity of 14.76 vs. 16.11 for SVD-LLM and improves average zero-shot reasoning accuracy from 40.69 to 42.63. The method is evaluated across multiple LLM families and shown to be orthogonal to weight quantization.

---

## Strengths

1. **AdaComp's Moore-Penrose pseudoinverse update yields stable and effective error compensation.** Figure 3(a) shows the proposed MPPU produces a smooth, monotonic MSE reduction, unlike the naive update (NU) which fluctuates. Table 3a quantifies the benefit: at 60% compression on WikiText-2, adding adaComp reduces perplexity from 78.82 to 50.33, a ~36% relative improvement. The stack-of-batch strategy (SoBC) further reduces error without increasing GPU memory, as shown in Figure 3(b).

2. **AdaSVD consistently and robustly outperforms SVD-LLM across multiple LLM families and compression ratios.** Table 1 on LLaMA2-7B shows AdaSVD beats SVD-LLM at every compression ratio on all three language modeling datasets (e.g., 14.76 vs. 16.11 at 40% on WikiText-2) and achieves higher average accuracy on five reasoning tasks. Table 2 extends these gains to OPT-6.7B, Vicuna-7B, and Mistral-7B at 60% compression. The improvements are consistent and not cherry-picked for a single favorable setting.

3. **The ablation study cleanly isolates the contribution of each component.** Table 3a shows adaComp alone improves over SVD-LLM; Table 3b shows adaCR further improves over constant compression ratios; Table 3c investigates iteration sensitivity; Table 3d examines the minimum retention ratio. This systematic disambiguation makes the paper's empirical claims verifiable and reproducible.

4. **AdaSVD is orthogonal to weight quantization.** Table 4 shows AdaSVD+GPTQ-INT4 consistently beats SVD-LLM+GPTQ at every compression ratio (e.g., 82.08 vs. 119.46 at 60% on WikiText-2), demonstrating that AdaSVD's benefits complement other compression approaches.

5. **The stack-of-batch strategy (SoBC) is a practical contribution.** It allows more calibration data to be leveraged under memory constraints without changing the core algorithm, and Figure 3(b) shows it meaningfully reduces compression error relative to naive calibration.

---

## Weaknesses

### Fatal

None.

### Major

**1. The conceptual justification for adaCR's importance metric is weak and potentially inverted.**  The paper defines layer importance as $\mathcal{I}(\mathcal{W}) = \text{similarity}(\mathcal{X}, \mathcal{Y})$ — the cosine similarity between a layer's input $\mathcal{X}$ and its output $\mathcal{Y}=\mathcal{W}\mathcal{X}$ — and states this measures "impact on the input" (Section 3.2, Eq. 17). However, high cosine similarity means the output is nearly proportional to the input, which is the *opposite* of high impact; it means the layer changes the input very little. The paper provides no theoretical or intuitive reasoning for why this specific metric captures sensitivity to SVD truncation, nor does it compare against alternative importance measures (e.g., singular-value decay rate, output sensitivity to input perturbations, or gradient-based metrics). While Table 3b empirically shows that adaCR improves over constant compression ratios, it is unclear whether *any* non-uniform allocation would yield similar gains or whether this particular cosine-similarity-based allocation is meaningful. This is a methodological gap in the core design of adaCR.

**2. The reported perplexities for FWSVD and ASVD are orders of magnitude above what the original papers report for similar models.** At 40% compression on LLaMA2-7B, FWSVD yields 8,060.35 and ASVD yields 1,609.32 on WikiText-2, vs. SVD-LLM's 16.11. The paper acknowledges (Section 4.2) that "FWSVD and ASVD fail on these LLMs with compression ratios under 60%" and says they used official GitHub repos. However, the discrepancy between these numbers and what those methods should plausibly achieve is so large that it undermines confidence in the experimental setup. The paper does not explain whether the failure is due to model version differences (LLaMA2 vs. LLaMA v1), calibration data mismatch, or a bug in the reproduction. The main comparison (AdaSVD vs. SVD-LLM) is likely valid since SVD-LLM's numbers are reasonable, but the overall table lacks an essential sanity-check footnote or explanation for why two established baselines collapse so dramatically. This needs to be transparently addressed.

### Minor

1. **VLM evaluation is qualitative only.** Figure 5 shows example image captions from SVD, SVD-LLM, and AdaSVD on LLaVA-7B, with correct/wrong parts color-coded. No quantitative metric (perplexity on a vision-language benchmark, CIDEr, or accuracy) is provided in the main paper. The paper mentions "more comparisons in supplementary file," but VLM compression is listed as a contribution area, so even a single quantitative table in the main paper would significantly strengthen this claim.

2. **No inference latency or GPU memory measurements.** The paper's motivation (Section 1) emphasizes that SVD reduces memory requirements and accelerates inference, and claims SVD is "more versatile across different platforms." Yet the experiments report only parameter-reduction ratios (compression ratio). Actual end-to-end latency (tokens/sec) and peak GPU memory usage (with and without two-factor storage) would substantiate the practical motivation.

3. **The paper uses a fixed 1 iteration for adaComp in all main results with limited justification.** Table 3c shows that 1 iteration is optimal at 40% and 50% compression, but 3 or 15 iterations sometimes hurt performance due to overfitting. The paper notes this pattern qualitatively but provides no practical guideline or early-stopping rule for selecting the iteration count at an unseen compression ratio or model.

### Trivial

None.

---

## Nice-to-Haves

- **Compare against a simple gradient-descent baseline for adaComp.** The paper motivates the Moore-Penrose pseudoinverse by showing the naive inverse (NU) is unstable. A comparison with a few gradient-descent steps (with a tuned learning rate) on the same objective would isolate whether the pseudoinverse's benefit comes from closed-form optimality or merely from the fact of performing *any* post-truncation tuning.

- **Include the 70% and 80% compression results in the main paper.** Table 1 and the ablations only cover 40–60%; higher compression ratios are relegated to the supplementary file. Showing these in the main paper would strengthen the claim that AdaSVD is effective "particularly at high compression ratios."

- **Add a limitations paragraph.** The paper does not discuss limitations such as sensitivity to calibration data distribution, potential instability at very low ranks, or the overhead of the alternating update procedure relative to one-shot SVD-LLM.

---

## Removed Points

These points were flagged but removed for the reasons stated below. Treat them with caution if re-examined.

- **"The baseline perplexity issue casts doubt on AdaSVD vs SVD-LLM comparison."** — The critic argued that because FWSVD/ASVD numbers are extreme, the AdaSVD vs. SVD-LLM comparison is also suspect. This is overreach: SVD-LLM produces reasonable numbers (16.11 at 40%, 27.19 at 50%) that are consistent with expectations for compressed 7B models. The comparison between AdaSVD and SVD-LLM rests on these numbers, not on the FWSVD/ASVD numbers. The FWSVD/ASVD issue remains a separate concern about reproduction quality, and I have kept it as a Major weakness (item 2) but do not consider it fatal to the core claim.

- **"The gap between AdaSVD and SVD-LLM is modest (14.76 vs 16.11) — close to 1:1."** — At 40% compression, this gap is about 8% relative perplexity improvement, which is meaningful for LLM compression. The gap grows substantially at higher compression ratios (50.33 vs 89.90 at 60%). This criticism ignores the broader trend across all ratios and models.

- **Criticisms about missing related works** — Removed per protocol: I cannot confirm existence of specific missing citations without external information.

- **"The paper does not compare to a simpler gradient-descent alternative"** — Moved to Nice-to-Haves; this is a suggestion for strengthening, not a core weakness.

- **"No discussion of limitations"** — Moved to Nice-to-Haves.

- **Weaknesses about incomplete appendix, missing proofs in appendix, or absent references** — Removed per protocol: the parser strips appendix content; these exist in the original submission.

- **"The first layer importance in Figure 4 is consistent with residual connections, not with actual importance"** — The critic's claim that high input-output cosine similarity is due to residual connections is speculative. The paper's empirical finding (Figure 4 and Table 3b) shows this metric produces meaningful layer rankings (e.g., first layer and last layers are more important), and the ablation confirms the adaptive allocation improves performance. The conceptual justification is indeed weak (kept as Major weakness 1), but the critic's specific residual-connection objection is not a confirmed flaw.

- **Several generic strengths from the Strength Finder** — Removed generic/superficial claims such as "this paper addressed an important problem" and "this paper targeted an interesting question." Only strengths grounded in specific experimental evidence are retained.

---

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a novel perspective that the paper itself does not already articulate.

---

## Suggestions

1. **Address the FWSVD/ASVD discrepancy transparently.** Add a brief explanation (or footnote) stating the model version used, the specific reproduction settings, and the expected vs. obtained perplexities for these baselines. This will defuse concerns about experimental fairness without changing any results.

2. **Reconsider the framing of the adaCR importance metric.** Either provide an analytical justification for why input-output cosine similarity captures compression sensitivity, or replace the current phrasing ("impact on the input") with a more descriptively accurate one (e.g., "alignment-preserving importance"). Adding a comparison with one alternative metric (e.g., singular-value decay rate) in the ablation would make the choice robust even without full theoretical justification.

3. **Add at least one quantitative VLM result** (perplexity on a vision-language benchmark or a standard captioning metric) to the main paper. A single quantitative number would be far more informative than several qualitative examples.

4. **Report inference latency and/or GPU memory** for at least one model at one or two compression ratios to support the inference-motivation claims.

5. **Include a practical guideline for iteration selection**, such as "run adaComp until the reconstruction error on the calibration set plateaus" or "freeze at 1 iteration for compression ratios ≤ 50% and use 3 iterations for ≥ 60%."

---

## Score and Decision

**Calibration procedure and anchor comparison.**

*Round 1 (bracketing):* Queried the human-review corpus for SVD-based LLM compression papers, split into three score bands. Weak anchors (scores < 3.5): avg 2.5–3.4, mostly withdrawn/rejected papers with fatal flaws or very limited scope. Middle anchors (scores 3.5–7.5): included **Dobi-SVD** (avg 6.2, Accept Poster), **MoE-SVD** (avg 5.0, Reject), **AutoTrunc** (avg 4.0, Withdrawn), **Low-Rank Correction for Quantized LLMs** (avg 5.0, Reject), **Input Compensation for Pruned Models** (avg 5.0, Reject). Strong anchors (scores > 7.5): avg 8.0–8.2, largely oral-level papers on very different topics (LoRA, pre-training data selection, sparse autoencoders) — not directly comparable. Initial bracket: **5.0–6.5**.

*Round 2 (narrowing):* Focused on papers in the 4.5–7.5 range most similar to AdaSVD. Read four anchor papers in full.

- **Dobi-SVD** (avg 6.2, Accept Poster): The closest topical match — also SVD-based LLM compression with post-truncation weight updates and per-layer truncation learning. Dobi-SVD has more theoretical depth (Eckart-Young-Mirsky derivation, differentiable truncation), reports end-to-end speedup, and achieves lower perplexity (9.07 at 40% on LLaMA-7B). The human reviews noted "experimental results are a bit of a mess" (Reviewer 1) and "the submission slightly overstates its novelty." AdaSVD is cleaner methodologically (simpler alternating update, no gradient backprop through SVD) and has more systematic ablations, but lacks the theoretical grounding, speed measurements, and some of Dobi-SVD's raw performance. AdaSVD is **slightly weaker** than Dobi-SVD, placing it below 6.2.

- **MoE-SVD** (avg 5.0, Reject): SVD compression for MoE models. Weaknesses included "accuracy degradation too obvious" and missing comparisons. AdaSVD has clearer improvements over its baselines and more thorough evaluations. AdaSVD is **clearly stronger** than MoE-SVD.

- **Low-Rank Correction for Quantized LLMs** (avg 5.0, Reject): Low-rank correction for quantization. Weaknesses included "limited contribution" and missing complexity analysis. AdaSVD's two-component design is about equally novel but better evaluated. AdaSVD is **moderately stronger** than this paper.

- **AutoTrunc** (avg 4.0, Withdrawn): Automatic truncation for SVD. Weaknesses were severe: poor presentation, overclaimed speed, missing experiments. AdaSVD is **substantially stronger** than AutoTrunc.

- **Input Compensation for Pruned Models** (avg 5.0, Reject): Different domain (pruning compensation). AdaSVD is in a different setting but better executed on its own terms.

*Final score:* AdaSVD sits between the clearly rejected papers (5.0) and the accepted Dobi-SVD (6.2), closer to the middle. The method is sound and the experiments are well-structured with clean ablations. The two main weaknesses — the weak justification for adaCR's importance metric and the unexplained baseline perplexity discrepancy — are genuine but not fatal. VLM evaluation is thin. The paper lacks speed/memory measurements that would fully substantiate the practical motivation. Relative to Dobi-SVD (6.2, accepted), AdaSVD has less theoretical depth and fewer supporting measurements but cleaner methodology. I place it at **5.5**.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>