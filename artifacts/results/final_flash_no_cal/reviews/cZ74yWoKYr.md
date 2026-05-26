Now I have a thorough understanding of the paper. Let me produce the consolidated review.

## Summary

This paper studies KV cache eviction in LLMs from an output perturbation perspective. The authors derive an upper bound on attention output perturbation (Theorem 3.3) showing that both attention weights **and** projected value states (VW^O) matter — the latter being overlooked by prior attention-weight-only heuristics. They propose a two-stage perturbation-constrained selection algorithm that incorporates value-state norms, and integrate it as a plug-and-play module into three existing eviction methods (SnapKV, AdaKV, HeadKV). Evaluations on 29 datasets across three LLMs (Llama-3.1-8B, Mistral-7B, Qwen2.5-32B) show consistent quality improvements at various cache budgets, with negligible runtime overhead.

## Strengths

1. **Novel theoretical perspective identifying a genuinely overlooked factor.** The paper derives a rigorous output-perturbation upper bound (Theorem 3.3) that explicitly includes projected value states ‖V_i,: W^O‖₁ alongside attention weights. This formalizes why existing attention-weight-only heuristics are suboptimal and identifies a concrete new term for selection. The theoretical analysis (Theorems 3.3, 3.5) is clean and internally consistent.

2. **Consistent and substantial empirical improvement across diverse settings.** When integrated with three SOTA methods on three LLMs spanning different families and scales, the algorithm consistently reduces compression loss. For example, at 40% cache on Ruler, AdaKV's average score with Llama-3.1-8B goes from 78.38 to 86.28; on LongBench, AdaKV's loss drops from 6.0% to 2.4%. On Mistral-7B at 40% Ruler, AdaKV improves from 34.88 to 69.17 — a very large gain. These improvements hold across cache sizes (20%–60%), across 88/90 long-dependency test cases on LongBench, and on SCBench multi-turn QA with 227K average context.

3. **Negligible computational overhead.** The added computation is limited to ‖VW^O‖₁ (linear in complexity). At 32K context, TTFT increases by only 0.06s (batch 1) and 0.04s/request (batch 4). Decoding latency is identical to the base eviction method (0.0332s vs 0.0828s full cache, a 2.49× speedup). This makes the method highly practical.

4. **Empirical validation that the algorithm reduces actual output perturbation.** Section 4.7 shows that the perturbation-constrained selection lowers L₁ output perturbation in 92% of Llama-3.1-8B heads and 86% of Mistral-7B heads, with the reduction accumulating across layers and holding across budgets from 2.5% to 40%. This directly confirms that constraining the theoretical bound translates into real perturbation reduction.

5. **Robustness with a simple default hyperparameter (α=0.5).** The α sensitivity analysis (Table 4) shows robust performance on Llama-3.1-8B across α ∈ {0, 0.3, 0.5, 0.7} on LongBench, and the safeguard is shown necessary because α=0 causes a catastrophic 10+ point drop on Mistral-7B. This demonstrates both the necessity of the two-stage design for some models and the practical ease of use.

## Weaknesses

### Fatal
None.

### Major

1. **Theory-practice gap in query availability is not acknowledged or justified.** The theoretical development (Definition 3.1, Theorems 3.3, 3.5) assumes the query state *q* is known at selection time — attention weights A = softmax(qK^T) depend on the specific query. However, the main experimental setting (Section 4.1) compresses the context *independently before the question is introduced*, meaning the actual query is unavailable. The algorithm is then applied using accumulated attention weights from an observation window as a proxy (Algorithm 2). The paper never discusses this discrepancy, nor does it explain why the theoretical bound (which depends on the precise query-dependent A) should motivate an algorithm that uses an averaged proxy. The core contribution — incorporating value-state norms — is unaffected by this gap because ‖V_i,:W^O‖₁ is query-independent. But the paper's framing as a "formally grounded perspective" and "formal study" is weakened because the main evaluation setting does not satisfy the theory's query-availability precondition. The paper would benefit from explicitly delineating the applicable scope of the theory, acknowledging the gap, and providing a rationale (e.g., that the observation-window average is a standard empirical approximation and the value-norm term carries the key theoretical insight regardless).

### Minor

2. **The contribution of the value-norm term is not cleanly isolated from the two-stage design.** The algorithm has two novel components jointly introduced: (a) the value-norm term ‖V_i,:W^O‖₁, and (b) the two-stage budget split (α-safeguard). The comparison against base methods (attention-only, single-stage) shows overall improvement, but it does not reveal how much comes from the value norm versus the two-stage procedure. A natural ablation would be: two-stage selection with *attention-only* in both stages (i.e., the same budget split but without the value-norm term), which would isolate the value norm's contribution. The α=0 experiment (Table 4) partially addresses this for the single-stage case but on Mistral fails due to σ violation, making it uninformative. Without this ablation, attributing the improvement specifically to the value-state insight (rather than to the two-stage budget allocation) remains somewhat confounded.

3. **The "more than half" claim needs stronger support.** The abstract and introduction state the algorithm "reduces compression loss by more than *half* on average across 29 datasets." The aggregated per-benchmark averages (Figure 1, Tables 1–2) show large reductions, but several individual method-model combinations fall below 50% reduction (e.g., SnapKV on Llama-3.1-8B Ruler: 38.7% reduction; HeadKV on Llama-3.1-8B LongBench: 28.3% reduction). The claim may still be true *on average across the 29 individual datasets*, but the paper provides only per-benchmark aggregates (13 Ruler + 16 LongBench) rather than the per-dataset breakdown needed to verify the average. Providing the exact average and/or per-dataset numbers would substantiate the headline claim.

4. **Inconsistency between algorithm pseudocode and its textual description.** The text (Section 3.4) states that Stage 1 "prioritize[s] KV cache entries with high attention weights," implying selection by raw attention weights A_i. The Assumption 3.4 also defines σ using raw attention weights: σ = Σ Top_k(A, b'). However, Algorithm 1's pseudocode (line 3) reassigns the variable A to be the *product* (A+ε) ⊙ ‖V_i,:W^O‖₁, and then uses this product for selection in *both* stages (lines 5, 8). The pseudocode either has a variable-naming bug (the two stages should use different criteria) or the text description is inaccurate. This should be resolved for clarity and reproducibility.

### Trivial
None.

## Nice-to-Haves

- **Statistical significance / error bars.** The experimental conclusions would be strengthened by reporting variance across multiple runs or seeds, though the consistent direction of improvement across 88/90 long-dependency cases partially mitigates this concern.
- **Per-head σ distribution.** The paper claims (Section 3.5) that with α=0.5, σ>0.5 in "over 99% of attention heads," citing Appendix A. A figure showing the σ distribution across heads and layers for each model would help readers understand where and why the assumption might fail, especially for Mistral-7B where the α=0 case collapses.
- **Simple compression comparison.** The paper defers the "simple compression" (question available at selection time) setting to Appendix F. A main-text comparison between simple and independent compression would clarify whether the theoretical bound's query-dependence affects performance in practice, strengthening (or contextualizing) the theoretical motivation.

## Removed Points

- **Criticism about missing σ distribution / Appendix A content.** The paper states the σ analysis is in Appendix A. Since the parser strips appendices, this criticism cannot be verified from the available text and is removed per the rules on appendix content.
- **Criticism that the bound is linear and Top-b would be optimal without two-stage design.** This is partially addressed in the paper: the bound is *not* exactly linear (it includes the (2 − 1/σ) term depending on total selected attention weight), and the paper explicitly motivates the two-stage design through Assumption 3.4 (σ>0.5). The critic's framing overlooks the dependency on σ.
- **Request for longer-sequence efficiency numbers on SCBench.** The paper provides efficiency results at 32K (its primary setting) and SCBench results at 100K. Requesting efficiency numbers at the longer length for a method whose added cost is linear is a scope-expansion request.
- **Minor presentation/style nitpicks and generic concern sweeps** (e.g., "could the metric be measuring a proxy?" without specific evidence of a problem).

## Novel Insights

The key insight from this review synthesis is that the paper's two core contributions — (1) the theoretical identification of value-state norms as a critical factor in KV cache selection, and (2) the practical algorithm incorporating them — are partially decoupled. The value-norm insight (contribution 1) is robust to the query-availability issue because it is query-independent; it could stand as a theoretical contribution even in the proxy setting. The practical algorithm (contribution 2) combines this insight with a two-stage budget allocation that serves as an orthogonal safeguard. The main disconnect is that the paper's "formally grounded" framing ties the two together too tightly, implying the full algorithm is derived from the theory for the exact setting evaluated, when in fact the theory applies to a different setting (query-available) and the algorithm uses standard empirical approximations for the query-dependent part. Untangling this would strengthen both contributions: the theoretical insight is cleaner than the framing admits, and the empirical results are stronger than the overclaimed formalism suggests.

## Suggestions

1. **Acknowledge the query-availability gap explicitly** in Section 3.2 or 3.6. State that the theoretical analysis applies when the query is known (simple compression), and when the query is unknown (the primary evaluation setting), the observation-window average provides an empirical approximation — a standard practice in this field — while the value-norm term remains directly applicable because it is query-independent.

2. **Add an ablation isolating the value-norm term.** Implement two-stage attention-only selection (same budget split α=0.5, but using raw A_i instead of the product in both stages) and compare to the full method on a representative subset (e.g., Llama-3.1-8B on LongBench at 20% and 40% cache). This would cleanly separate the benefit of the two-stage design from the benefit of incorporating value norms.

3. **Provide per-dataset breakdowns** for the loss numbers underlying the "more than half" claim, or alternatively rephrase the claim to precisely state the average reduction and range across datasets.

4. **Fix the inconsistency in Algorithm 1.** Either correct the pseudocode to match the description (using attention weights only in Stage 1 and the product in Stage 2) or, if both stages intentionally use the same product criterion, revise the text and Assumption 3.4 to describe Stage 1 as prioritizing entries with high product values (which naturally correlates with high attention weights).

## Score and Decision

This paper makes a genuine contribution by identifying that projected value-state norms matter for KV cache selection — a factor overlooked by prior attention-weight-only heuristics — and by demonstrating consistent, substantial empirical improvements with negligible overhead. The weaknesses are primarily about framing and presentation rather than fundamental flaws: the theory-practice gap on query availability is real but does not invalidate the core empirical findings, the missing ablation can be addressed, and the "more than half" claim needs better support. The algorithmic inconsistency (Stage 1 criterion in pseudocode vs. text) is a clarity issue that should be fixed.

The empirical evidence is strong, the method is practical, and the theoretical insight (value norms matter) is novel and well-motivated even if the "formally grounded" framing is somewhat overstated for the main evaluation setting. This is a solid contribution that will be of interest to the efficient LLM inference community.

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>