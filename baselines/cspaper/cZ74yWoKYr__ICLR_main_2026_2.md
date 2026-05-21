---
job_id: 7a8e9c77-1c0f-46bf-b08a-cb605fbfe826
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: cZ74yWoKYr.pdf
paper: Identify Critical KV Cache in LLM Inference from an Output Perturbation Perspective
main_score_norm: 0.8
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, it studies efficient LNN inference through transformer KV-cache selection, with a mix of learning-theoretic motivation, optimization-style analysis, and empirical evaluation on long-context language modeling benchmarks.

## Minimum Quality
Pass ✅. The paper contains the expected scientific structure, including Abstract, Introduction, Related Work, a methodological section with equations and algorithms, experiments with quantitative results, and a conclusion. While there are several clarity and rigor issues in the derivations and exposition, they do not rise to the level of a desk-reject-worthy fatal flaw, and the empirical evidence is substantial.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find any hidden prompts, suspicious instructions targeting automated reviewers, or other manipulative content in the provided paper text.

# Expected Review Outcome:
## Summary
This paper studies KV-cache eviction for long-context LLM inference from an output-perturbation perspective. The core idea is to formalize “critical” cache entries as those whose retention minimizes perturbation of the attention output, derive an upper bound on this perturbation that depends on both attention weights and projected value states, and use that analysis to propose a two-stage greedy selection rule. The method is then plugged into SnapKV, AdaKV, and HeadKV, and evaluated on Ruler, LongBench, and SCBench across Llama, Mistral, and Qwen models.

## Strengths
The main strength is that the paper tries to give a cleaner principle for KV eviction than the usual “high attention means important” heuristic. Framing the selection problem via perturbation of the attention output is a sensible perspective, and the derivation around Equations (3) to (6) does make the paper’s central point visible: once the output is written as \(AVW^O\), importance should depend not only on \(A_i\), but also on the magnitude of the projected value contribution \(\| (VW^O)_{i,:} \|_1\). Even if the theory is not airtight in every step, the paper does succeed in articulating why pure attention-based retention is incomplete.

The plug-and-play aspect is appealing. The authors do not require retraining or architecture changes, and the integration pathway in **Section 3.6** and **Algorithm 2** is straightforward. In practice, this kind of compatibility matters more than many papers admit, because the KV-compression ecosystem is already fragmented across budget-allocation and observation-window variants.

The empirical section is broad. The paper covers synthetic long-context stress tests (Ruler), real-world long-context tasks (LongBench), and a multi-turn QA setting (SCBench). This is better than a single-benchmark story. **Figure 1** is effective as a high-level summary: across the three base eviction methods and three models, the claimed reduction in compression loss is consistently large, and the figure supports the authors’ “universal enhancement” framing better than a wall of prose would.

The results tables are generally favorable and not limited to cherry-picked single tasks. In **Table 1** on Ruler, the method often yields large gains when added to each base strategy, especially on difficult retrieval-style tasks and under stronger compression. Likewise, **Table 2** on LongBench shows a fairly consistent pattern over domains and models, particularly in the long-dependency domains the paper emphasizes. The fact that gains appear on top of SnapKV, AdaKV, and HeadKV is stronger evidence than merely beating one weaker baseline.

I also appreciated the perturbation analyses in **Figures 4, 5, and 6**. These figures are directly tied to the paper’s claimed mechanism, not just end-task score improvements. In particular, **Figure 4** supports the statement that perturbation is reduced in most heads, and **Figure 5** gives a plausible cumulative story across layers. This kind of mechanistic analysis is much more useful than the usual “our method works, trust us” plot.

Efficiency overhead appears modest relative to the quality gains. The prefill latency evidence in **Figure 3(a)** and the discussion in **Section 4.6** suggest that the extra \(VW^O\)-related computation is not a deal-breaker. For a method positioned as a selector on top of existing eviction pipelines, this is important.

## Weaknesses
1. **The mathematical setup has multiple notation and formulation inconsistencies, and these are not cosmetic.**  
   In **Equation (2)**, attention is written as
   \[
   A=\mathrm{softmax}(qK^T/\sqrt{d}),
   \]
   while \(q\in \mathbb{R}^{1\times d_h}\) and \(K\in\mathbb{R}^{n\times d_h}\) from **Equation (1)**. The scaling should ordinarily be by \(\sqrt{d_h}\), not \(\sqrt{d}\), unless the paper is redefining the head dimension in a nonstandard way. Since the derivation of the selector depends on this attention distribution, this mismatch should be fixed explicitly. There is also inconsistent notation for projected values, alternating between \(\boldsymbol{\mathcal V}\), \(\boldsymbol{\nu}\), and \(\boldsymbol v\) across **Theorem 3.3**, **Equation (10)**, and **Theorem 3.5 / Equation (15)**. When a paper’s main contribution lives inside the derivation, sloppy symbols are not a minor editorial issue, they directly reduce confidence that the proof steps were fully checked.

2. **The jump from the perturbation bound to the specific two-stage greedy algorithm is weaker than the paper suggests.**  
   The key optimization target in **Equation (5)** is
   \[
   \theta = C-\left(2-\frac{1}{\sum_i \mathcal N_i A_i}\right)\sum_i \mathcal N_i A_i \|\mathcal V_{i,:}\|_1.
   \]
   This objective couples the selected indices through the denominator \(\sum_i \mathcal N_i A_i\). The proposed **Algorithm 1** then replaces the difficult joint combinatorial problem with a two-stage top-\(k\) heuristic. That is acceptable as a heuristic, but the paper frequently phrases the method as if it is a direct consequence of worst-case perturbation minimization. It is not. The dependence on the denominator is precisely what makes the exact problem nontrivial, and the algorithm mostly sidesteps that with a staged approximation and an assumption on \(\sigma\). The paper would be stronger if it were more candid that the method is a heuristic inspired by the bound, rather than a principled optimizer of the stated objective.

3. **Assumption 3.4 is doing a lot of work, yet it is both strong and awkwardly handled in the main paper.**  
   In **Section 3.5**, the paper assumes the first-stage budget \(b' = b \times \alpha\) captures more than half the total attention mass:
   \[
   \sigma = \sum_i \mathcal N'_i A_i > 0.5.
   \]
   This condition is then used to keep \(2-1/\sigma>0\) in **Theorem 3.5**. The problem is that the assumption is not a benign technicality, it is central to why the stage-2 objective becomes a monotone top-\(k\) selection. In the main paper, the presentation is also inconsistent: **Algorithm 1** lists \(\alpha=0.25\) in its header, while **Section 3.5** says “we set \(\alpha\) to a fixed value 0.5”, and the experiments later also use \(\alpha=0.5\). That contradiction is not acceptable for the core hyperparameter controlling the method. Moreover, when the assumption fails, the paper does not clearly state what breaks theoretically. **Table 4** partially hints at failure modes for Mistral when \(\alpha=0\), but the theory section should discuss this explicitly, not bury the fragility in later ablations.

4. **The proof style is too loose for the strength of the claims.**  
   **Theorem 3.3** is essentially a triangle-inequality upper bound. That part is fine, but the paper then repeatedly interprets the resulting score as revealing the insufficiency of attention-only selection. This is plausible, but the proof itself only shows an upper bound involving \(A_i\|\mathcal V_{i,:}\|_1\), not that this score is tight, optimal, or consistently better aligned with downstream generation quality than alternatives. Likewise, in **Theorem 3.5** and its proof on **Page 21**, the chain leading from \(\theta\) to \(\hat\theta\) is not especially clean. The notation even switches to \(\mathcal N_i'''\) in **Equation (15)**, which appears to be a typo. More importantly, the derivation uses inequalities to produce a new upper bound, then says stage 2 “directly minimizes” that upper bound. What it actually minimizes is the linearized term under the imposed assumption and fixed stage-1 selection. That is a more limited statement than the prose suggests.

5. **The exposition around the algorithms is confusing enough to hinder reproducibility.**  
   **Algorithm 1** is not cleanly specified. On line 2 it computes \(A=\mathrm{softmax}(qK^T)\), which omits the scaling term from **Equation (2)**. On line 2 or 3, \(V\) is overwritten by \(VW^O\), then line 3 redefines \(A\) as \((A+\epsilon)\odot (\text{L1 norm of each rows in }V)\). If this new \(A\) is already the product score \(A_i\|\mathcal V_{i,:}\|_1\), then stage 2 is no longer really described as a separate optimization variable but as another top-\(k\) over a repurposed vector. The paper could still be implementable, but the current pseudocode is much more “suggestive sketch” than precise algorithmic specification. For a systems-facing paper where small implementation choices matter, that is a meaningful weakness.

6. **The empirical evidence is strong on additive gains over three baselines, but weaker on isolating what actually matters in the proposed score.**  
   The paper argues that projected value states and \(W^O\) are crucial, yet there is no main-paper ablation separating:  
   - attention-only stage 2 vs. \(A_i\|\mathcal V_{i,:}\|_1\),  
   - use of \(V\) alone vs. \(VW^O\),  
   - \(L_1\) norm vs. other summary statistics of the projected value,  
   - one-stage unified ranking vs. the proposed two-stage split.  
   **Table 4** studies \(\alpha\), and **Figure 9** in the appendix compares \(L_1\) and \(L_2\), but the main paper never really dissects whether the gain comes from the perturbation-derived score, from the first-stage safeguard, or simply from mixing two heuristics. Given that the central claim is conceptual, this matters a lot.

7. **The comparison set is narrower than the paper’s rhetoric implies.**  
   The paper compares “with vs. without ours” on SnapKV, AdaKV, and HeadKV, which is useful. But several relevant cache-compression methods are either only mentioned in passing or excluded from direct comparison. For example, methods such as PyramidKV and DuoAttention are clearly part of the practical landscape for long-context efficiency, and the absence of a same-table main-paper comparison makes it harder to judge whether the proposed perturbation-based selection is competitive beyond the specific wrapper settings chosen by the authors. Since the paper claims to offer a “new perspective” for the cache eviction field, the main paper should do more than show improvements over three closely related attention-accumulation pipelines.

8. **Some tables and figures expose presentation issues that make interpretation unnecessarily difficult.**  
   **Table 1** is packed and hard to parse. The model labels appear garbled in places, for example “Llama 3.0”, “AdaKV 3.0”, and “AdaKV 3.0” again where the intended model names seem to be Llama-3.1-8B, Mistral-7B, and Qwen-2.5-32B. This is not just cosmetic, because the reader needs to know exactly which block corresponds to which model before trusting cross-model conclusions. **Table 2** has similar formatting irregularities, including rows like “Llama-3.8B” and “Ours-32B”, which look like transcription or typesetting mistakes. These tables are central evidence, so such errors undermine confidence. On the figure side, **Figure 2** is useful in showing trends across cache sizes, but it is visually dense and small-panel-heavy; the paper would benefit from a clearer aggregation plot or selective task grouping in the main text.

9. **The paper overstates universality a bit.**  
   The abstract and introduction repeatedly describe the method as “universal” and “plug-and-play”. Plug-and-play, yes, mostly. Universal, not really established. The integration story is shown only for methods that already rely on accumulated attention scores and top-\(k\)-style retention. Even **Section 3.6** implicitly limits the scope to that family. A selector depending on \(A_i\) and \(VW^O\) is not obviously compatible with every cache compression scheme, especially those based on quantization, sharing, or sparse attention patterns rather than explicit eviction rankings. The paper should narrow this wording.

10. **The link between lower output perturbation and downstream task quality is plausible but still somewhat indirect.**  
    **Figures 4 to 6** are a good start, and I appreciated them. Still, the paper stops short of quantifying how strongly the perturbation proxy correlates with actual generation quality across tasks, heads, or layers. For instance, if perturbation is reduced in 92% of heads in **Figure 4**, what fraction of the task-level improvement is explained by this, and where does the theory fail to predict quality? Since the entire paper is built around output perturbation as the criterion of criticality, a more explicit correlation analysis would strengthen the scientific claim.

## Questions
1. In **Equation (2)** and **Algorithm 1**, should the attention scaling be \(\sqrt{d_h}\) rather than \(\sqrt{d}\)? Please clarify the intended dimensions and confirm whether the implementation uses the standard head-dimension scaling.

2. **Algorithm 1** states \(\alpha=0.25\) in its header, while **Section 3.5** and the experiments use \(\alpha=0.5\). Which one is correct? Was this only a typo in the pseudocode, or were any experiments run with 0.25?

3. Can the authors provide a cleaner statement of what is and is not theoretically guaranteed? In particular, do you claim to optimize the original upper bound in **Equation (5)**, or a surrogate upper bound after imposing **Assumption 3.4** and fixing stage 1? A more precise wording would improve the paper substantially.

4. A main-paper ablation isolating the role of projected values would increase my confidence. For example, how do the following compare on the same benchmark and budget:  
   \[
   \text{TopK}(A_i), \quad \text{TopK}(A_i\|V_{i,:}\|_1), \quad \text{TopK}(A_i\|(VW^O)_{i,:}\|_1)?
   \]
   This would directly test whether \(W^O\)-projected values are really the source of the gain.

5. Have the authors examined whether the perturbation proxy correlates with downstream loss or accuracy at the sample level? A scatter plot or correlation table between \(\|o-\hat o\|_1\) and task score degradation would help validate the paper’s central premise.

6. The comparison set in the main paper is focused on three baselines that share a similar selection backbone. Could the authors add, in the main paper rather than only elsewhere, comparisons against at least one additional strong cache-compression method with a somewhat different design philosophy?

7. For **Table 1** and **Table 2**, please check and correct the model labels and formatting issues. Several entries are confusing enough that I had to infer which block belonged to which model.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
None. The paper studies inference-time efficiency methods for language models and does not introduce an obvious new ethics concern beyond standard deployment issues already associated with LLMs.

## Soundness Rating
3: good. The core intuition is reasonable, the empirical methodology is fairly extensive, and the main claims are supported at a practical level. However, the theoretical presentation has enough looseness and inconsistency that I cannot rate soundness as excellent.

## Presentation Rating
2: fair. The paper is understandable overall, but the exposition is rough in several important places, especially around notation, theorem statements, pseudocode consistency, and some table formatting.

## Contribution Rating
3: good. The perturbation-based perspective is a meaningful contribution to the KV-cache eviction literature, and the practical gains across multiple baselines and benchmarks make the work valuable to the community, even if the method is more heuristic than the strongest wording suggests.

## Overall Rating
8: Accept, good paper (poster). I have real reservations about the theorem-to-algorithm jump, the inconsistent notation, and the lack of sharper ablations isolating the source of the gains. Still, the paper makes a useful conceptual move beyond attention-only heuristics, and the empirical results across **Figure 1**, **Table 1**, **Table 2**, and the perturbation analyses are strong enough that I think this is worth accepting.

## Reviewer Confidence
4: confident. I am confident in the assessment and familiar with the area, though a few proof details and implementation choices would benefit from clarification in rebuttal.