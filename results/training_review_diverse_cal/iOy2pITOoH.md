Here is the final consolidated review.

---

## Summary

Spark Transformer is an architectural variant of the Transformer that achieves high unstructured sparsity in both FFN (8% nonzeros) and attention (≤256 tokens attended) without quality loss, extra parameters, or multi-stage training. It uses a novel **statistical top‑k** operator (linear-time threshold estimation via Gaussian quantiles) and a low‑rank predictor carved from the input's existing dimensions (fixed split via matrix *P*). Trained from scratch using the Gemma‑2 2B recipe, the resulting Spark Gemma‑2 matches the dense baseline on standard benchmarks while delivering a 3.1× FLOPs reduction and up to 1.79× measured CPU speedup.

---

## Strengths

1. **Statistical top‑k is lightweight, provably well‑behaved, and incurs minimal training overhead** (Section 2, Theorems 1‑2, Figure 4). The operator has O(*d*) complexity, a closed-form soft-thresholding solution, and is shown to be far faster than JAX's optimized `approx_max_k` even at low recall — a practical win for training accelerators.

2. **Unified sparsity for FFN and attention without extra parameters or multi‑stage training** (Section 3). The predictor is formed by repurposing a fixed subset of the input dimensions (matrix *P*), avoiding the auxiliary parameters and post-hoc fine-tuning required by prior work (ProSparse, LLaMA ReGLU). Table 2 shows Spark Gemma‑2 matches dense Gemma‑2 quality while using 8% FFN nonzeros and ≤256 attended tokens.

3. **Single‑stage pretraining achieves high sparsity without quality degradation** (Table 2, Figure 1). On MMLU, HellaSwag, and other benchmarks, Spark Gemma‑2 scores are within rounding error of the dense baseline. Figure 1 confirms that sparsity targets are maintained throughout the full 480k‑step training run across all 26 layers.

4. **Ablation studies provide clear guidance on hyper‑parameter choices** (Figure 5). The optimal rank *r* is near *d*<sub>model</sub>/2 (1024 out of 2304), and quality is robust across 5%–10% sparsity levels, giving practitioners a tunable compute‑quality trade‑off.

5. **Measured CPU speedups demonstrate practical relevance on accessible hardware** (Figure 3, Table 3). Spark Gemma‑2 achieves 1.70× prefill and 1.79× decoding speedup on a 16‑core CPU, and 86 ms/token on a 4‑core VM — exceeding average human reading speed. The CPU focus is honestly acknowledged as a "hardware lottery" limitation.

---

## Weaknesses

### Fatal
None.

### Major

1. **The low‑rank predictor's accuracy is not directly measured.** The paper asserts that scores computed on a fixed half of the query dimensions can reliably predict which keys/neurons to activate, but provides no diagnostic of the predictor's fidelity — no recall, Jaccard similarity, or ranking correlation between the low‑rank predictor's selection and the full‑rank scores. The ablation on *r* (Figure 5a) shows quality is maintained overall, but this does not distinguish between two very different scenarios: (a) the predictor is highly accurate, selecting nearly the same top‑*k* entries as the full scores, or (b) the model simply learns to tolerate frequent prediction errors. Without this distinction, the reader cannot assess whether the predictor design is robust or brittle, nor derive principled guidance for choosing *r* in new settings (e.g., larger models, different data distributions). This is the most significant gap because it affects understanding of *why* the method works.

2. **Validation on a single architecture (Gemma‑2 2B).** While the experiments are thorough for this one model, the paper frames Spark Transformer as a general architectural contribution. Demonstrating the method on at least one unrelated architecture (e.g., a LLaMA‑like model at 1B scale) would substantially strengthen claims of generality. The current evaluation is a strong single case study, not a general validation.

### Minor

3. **The Gaussian assumption verification relies primarily on sparsity counts, not distribution diagnostics.** The paper acknowledges the Gaussian assumption may not hold after training, references Appendix D.1, and provides per‑layer sparsity tracking (Figure 1) showing the target sparsity is maintained. However, this only confirms the *outcome* (sparsity level) of Statistical‑Top‑k, not the *mechanism* (whether activation values remain approximately Gaussian). Histograms of activation distributions at initialization, mid‑training, and convergence (with Gaussian fits overlaid) would make the "approximately Gaussian" claim concrete rather than deferred to an appendix.

4. **The i.i.d. assumption in Theorem 1 is not discussed in the context of actual activations.** The entries of *K*<sup>⊤</sup>*q* share the same query *q* and are therefore not independent. The paper does not address whether or how this dependence affects the error bound, leaving a gap between the theory and the practical setting.

5. **The softplus in Spark Attention (Eq. 14) is motivated only as "empirically observed to offer quality benefits" without an ablation.** A brief experiment showing quality with and without softplus would eliminate the guesswork.

6. **CPU‑only evaluation leaves the gap between FLOPs reduction (3.1×) and actual speedup (≤1.79×) underexplored.** The paper is transparent about this gap and cites the "hardware lottery." However, a simulation or analysis bounding the speedup achievable under ideal sparse hardware would help the reader understand what fraction of the FLOPs reduction is practically realizable.

### Trivial
None.

---

## Nice-to‑Haves

- An oracle comparison: replace Statistical‑Top‑k with exact top‑k on the full scores during inference to isolate quality loss due to the approximation vs. the predictor.
- A brief note on training dynamics — whether the δ=0 setting required any gradient stabilization or learning rate tuning.
- Experimental comparison or discussion contrasting unstructured sparsity (this work) with MoE‑style structured sparsity in terms of training/serving trade‑offs.

---

## Removed Points

These points were flagged by reviewers but are removed or downgraded after fact‑checking against the paper:

- **"No layer‑by‑layer sparsity counts"** — Figure 1 explicitly shows sparsity per layer across all 26 layers at selected training steps. This claim is factually wrong.
- **"Missing appendix / unavailable appendix content"** — The parser strips appendices; Section D.1 and D.2 are referenced and exist in the original submission. Per policy, this is not a valid criticism.
- **"Not a drop‑in replacement due to wider d_ff"** — The paper clearly explains the iso‑parameter design (*d*<sub>ff</sub>=13824 vs. gated *d*<sub>ff</sub>'=9216) and correctly states parameter count is identical. This is a deliberate design choice, not a flaw.
- **"The authors should add Y / domain Z / additional tasks"** — These demands for broadened scope (e.g., testing on every possible benchmark, covering all related methods) would turn the paper into a different, broader paper and would not change the accept/reject judgment on the current contribution.

---

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a genuinely novel observation that the paper itself does not already make or implicitly contain.

---

## Suggestions

1. **Add predictor accuracy diagnostics.** Compute recall (fraction of true top‑*k* entries captured by the low‑rank predictor) or Jaccard similarity between low‑rank and full‑rank selections for a sample of inputs across layers and training steps. This would either confirm the predictor is accurate or reveal surprising robustness that warrants explanation.

2. **Validate on a second architecture.** A smaller‑scale experiment on a LLaMA‑like model (even 1B parameters) would significantly strengthen the generality claim.

3. **Add activation distribution histograms to the main text.** Show the empirical distribution of *K*<sup>⊤</sup>*q* entries at initialization and convergence, with a Gaussian overlay, to make the "approximately Gaussian" claim tangible.

4. **Ablate the softplus** in Spark Attention and report the quality difference.

5. **Discuss the independence assumption** in Theorem 1 and its implications for the practical setting where activation entries are dependent.

---

## Score and Decision

**Originality** — Good. Statistical top‑k for activation sparsity and the dimension‑split predictor are genuinely novel.  
**Importance** — High. Efficient LLM architectures are a critical and timely problem.  
**Claims supported** — Mostly. The central claims (quality maintenance, sparsity, FLOPs reduction, CPU speedup) are well‑supported. The mechanism of the predictor is under‑diagnosed.  
**Soundness** — Good. Experimental design is appropriate; the main gap is depth of diagnostic analysis.  
**Clarity** — Good. The paper is well‑structured and clearly written.  
**Value to community** — High. The approach is clean, principled, and could influence future efficient architecture design.

The paper makes a meaningful contribution but falls short of a top‑tier acceptance due to the unmeasured predictor accuracy and single‑architecture validation. No fatal flaws exist; the core claims are supported. A strong revision adding predictor diagnostics and a second architecture would substantially strengthen the paper.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>