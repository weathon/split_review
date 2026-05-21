---
job_id: cfbdc29d-bf4b-4133-a269-dd084e67528a
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: D5PJX02Jki.pdf
paper: Beyond Real: Imaginary Extension of Rotary Position Embeddings for Long-Context LLMs
main_score_norm: 0.6
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅ This paper is clearly within ICLR scope, focusing on positional representations and attention mechanisms for long-context language models, with both methodological and empirical contributions relevant to representation learning and large-scale language modeling.

## Minimum Quality
Pass ✅ The paper contains all core sections, including abstract, introduction, related work, methodology, experiments, quantitative results, discussion, and conclusion. While there are several clarity and validation issues, the work is complete enough, technically coherent overall, and supported by nontrivial experiments rather than being a thin engineering note.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅ I did not find any hidden prompts, suspicious reviewer-targeting instructions, or other manipulative content in the provided paper text and figures.

# Expected Review Outcome:
## Summary
This paper proposes RoPE++, an extension of rotary position embeddings that uses the imaginary component of the complex-valued RoPE interaction, rather than discarding it as in the standard formulation. The method introduces imaginary attention heads alongside the usual real ones, in two variants, RoPE++EC, which keeps KV cache size fixed and increases head count, and RoPE++EH, which keeps head count fixed and reduces QKV parameters and KV cache. The paper provides a mathematical reformulation of the imaginary term, argues that it is better suited to long-range dependency modeling, and evaluates the approach on 376M and 776M language models across short-context and long-context benchmarks.

## Strengths
The paper has a clear and concrete central idea. Revisiting the complex form of RoPE and asking whether the discarded imaginary term contains useful positional signal is a reasonable and interesting angle, and the resulting construction is simple enough that it could matter in practice.

I appreciated that the paper does not just propose one configuration, but two clearly motivated operating points. Section 3.3 makes the tradeoff explicit: RoPE++EC targets better quality at similar cache cost, while RoPE++EH targets efficiency by reducing KV cache and QKV parameters. This makes the contribution more practically relevant than a single monolithic variant.

The core derivation is reasonably intuitive. In particular, **Equation 4** is the key equation in the paper, because it shows that the proposed imaginary attention can still be written in the same absolute/relative positional form as standard RoPE, with the main change being a fixed extra rotation of the query by $-\pi/2$. That formulation helps demystify the method and makes it plausible that RoPE++ can be implemented with modest architectural disruption.

The paper includes a fairly broad experimental suite for models of this size. It covers both standard short-context evaluations and synthetic long-context benchmarks, and it also studies interaction with context-extension methods such as PI and YaRN in **Table 3**. This is better than papers that only show one cherry-picked long-context benchmark and call it a day.

There are some genuinely encouraging empirical results. In **Table 2**, RoPE++EC is consistently stronger than RoPE on the long-context averages for both 376M and 776M. For example, at 776M, the RULER average improves from 27.4 to 29.4, and BABILong average from 22.8 to 24.1. The gains are not massive, but they are directionally consistent on the long-context side, which is the main advertised goal of the method.

The efficiency story for RoPE++EH is also supported with concrete evidence rather than hand-waving. **Figure 4** shows lower memory cost and lower TPOT than RoPE, and the margin widens with context length. Since many long-context papers quietly hide their inference-time costs, I appreciate that this paper makes the systems tradeoff visible.

The qualitative attention analysis is useful, even if not fully conclusive. **Figure 5** does show a visible behavioral difference between real and imaginary heads, with imaginary heads appearing more global. Whether this proves the claimed mechanism is another question, but it at least aligns with the hypothesis and gives some interpretability signal beyond raw benchmark numbers.

## Weaknesses
1. **The paper’s central claim about “information loss” in standard RoPE is rhetorically stronger than what is actually established.**  
   The introduction and abstract repeatedly frame RoPE as discarding “valuable phase information” and causing “irreversible information loss” because only the real component is used. That statement is too sweeping given what is shown in the main paper. RoPE’s attention score is, by design, a real-valued bilinear form, and the fact that one can write it as the real part of a complex interaction does not by itself imply that the imaginary component is missing information that the model “should” have used. The paper demonstrates that adding a second, related bilinear form can help, which is interesting, but that is weaker than proving the standard formulation is intrinsically lossy in a harmful sense. This matters because the novelty and motivation of the paper rest heavily on this framing. I would urge the authors to tone this down and distinguish “an unused complementary signal that empirically helps” from “a fundamental flaw in RoPE.”

2. **The mathematical exposition has several notational and derivational problems, and they are not cosmetic.**  
   There are multiple places where the equations are sloppy enough to impede verification. For example, **Equation 2** appears malformed in the text: the second line starts with an equals sign and the decomposition across sine and cosine terms is broken in a way that makes it difficult to check signs and grouping. Likewise, in **Equation 5**, the discrete characteristic curve is written as
   \[
   c_{\text{Im}}(\Delta t)=\frac{2}{d}\sum_{n=0}^{d/2-1}\sin\left(10^{-\frac{8n}{2}}\Delta t\right),
   \]
   which looks inconsistent with the standard RoPE frequency schedule and also inconsistent with **Equation 7** in the appendix, where the exponent uses $d$ in the denominator. This is probably a typo, but here is the problem: the whole interpretive argument in Section 3.2 relies on the shape of this characteristic curve. If the formula is misstated in the main paper, readers cannot reliably check the claimed sine-integral behavior. Similarly, in Appendix B the term $\boldsymbol{\mathcal{R}}_{-\frac{\sigma}{2}-\Delta t}$ appears in the derivation for imaginary attention, which seems dimensionally and conceptually off, and likely should involve $-\pi/2$ rather than $-\sigma/2$. These issues make the mathematical part look less mature than it needs to be.

3. **The theory is mostly expectation-level intuition, not a convincing explanation of why the method should improve actual trained attention behavior.**  
   Section 3.2 argues that imaginary attention attends more to distant positions based on the average of $\sin(\theta \Delta t)$ across frequencies, and **Figure 1** visualizes a slowly declining imaginary characteristic curve. But this is a very weak bridge to actual transformer behavior. Real attention in a trained model is shaped by learned $Q,K$ projections, softmax normalization, content effects, and head specialization, not by the standalone average of trigonometric kernels. The paper acknowledges this only partially. In other words, **Figure 1** is a suggestive cartoon plus averaged kernel plot, not evidence that the model will systematically route useful long-range information through the imaginary heads. The paper would be much stronger if the theory were presented as heuristic intuition rather than near-mechanistic explanation.

4. **The comparisons are not as strong as the claim “outperform vanilla RoPE and other position embeddings on average” makes them sound.**  
   Looking carefully at **Table 1**, the short-context results are mixed. At 776M short, ALiBi already achieves a stronger average than RoPE, and RoPE++EH underperforms RoPE on GPQA quite severely, 15.8 vs 25.8. At 1.5B in the appendix, the picture becomes even less clean, but even in the main paper the improvement story is clearly not uniform. The average gains are modest and come with regressions on some tasks. This matters because the paper sometimes sounds like a broadly superior positional encoding, while the evidence supports something narrower: RoPE++EC looks useful for long-context-oriented settings, RoPE++EH is an efficiency-quality tradeoff, and neither is an across-the-board win on all tasks.

5. **RoPE++EH’s quality-efficiency tradeoff is presented a bit too optimistically.**  
   The selling point of RoPE++EH is that it keeps head count fixed while halving QKV parameters and KV cache. That is interesting, but the quality sacrifice is not consistently minor. In **Table 2**, for 776M Long, RoPE++EH is slightly better than RoPE on RULER average, 28.6 vs 27.4, but substantially worse on BABILong average, 19.4 vs 22.8. For 376M Long, the same pattern appears, with BABILong improving slightly but RULER roughly flat or slightly down. So the message is not “comparable performance with half the cache” in a robust sense; it is “a mixed quality tradeoff whose success depends on benchmark.” Since efficiency is one of the paper’s key claimed contributions, this nuance should be made much clearer.

6. **The long-context evaluation relies heavily on synthetic benchmarks, and the paper does not establish impact on realistic long-document language tasks.**  
   The main long-context evidence comes from RULER and BABILong in **Table 2** and **Figure 6**. Those are useful diagnostics, but they are not enough to support broad claims about long-context LLM capability. There is no evaluation on long-document QA, summarization, book/code retrieval, or multi-hop document reasoning datasets. This matters because the proposed mechanism is specifically argued to help “retrieve long-context information,” yet the paper mostly validates that on synthetic setups designed to stress positional tracking and retrieval. It is entirely possible for a method to improve RULER/BABILong while having little or no effect on realistic long-form tasks.

7. **The causal evidence that imaginary heads are responsible for long-context gains is still fairly weak.**  
   Section 5.2 and **Figure 5(j)** use Gaussian noise injected into real vs imaginary attention and show that corrupting imaginary attention hurts more. This is interesting, but it is not a clean causal isolation. The real and imaginary branches are not symmetric objects in a trained model, and equal-variance noise does not imply equal semantic perturbation. Moreover, the paper does not report whether the same conclusion holds across multiple layers, heads, datasets, or seeds. The attention maps in **Figure 5(a-i)** are also cherry-picked examples from specific heads and layers. As presented, these analyses support the hypothesis, but do not establish it strongly enough to justify claims like “imaginary attentions play a dominant role” without qualification.

8. **The paper does not disentangle gains from increased architectural capacity versus gains from the imaginary formulation itself, especially for RoPE++EC.**  
   RoPE++EC keeps cache size fixed but doubles the number of attention heads and enlarges $W_o$, as described in Section 3.3. This is not a tiny implementation detail, it changes the architecture. The paper says the only cost is an additional imaginary attention under fixed QKV parameter budget, but the representational structure has still changed. A fair concern is that some of the gain in **Table 1** and **Table 2** may come from modified head granularity or output mixing, rather than specifically from leveraging the imaginary component. The main paper lacks a control that would isolate this, such as a same-head-count or same-$W_o$ alternative with a different deterministic query transform unrelated to the complex imaginary term.

9. **The literature positioning is a bit selective given the strength of the novelty claim.**  
   The paper cites several RoPE extensions, which is good, but the related-work discussion stays broad and does not sharply position this method against other recent analyses or modifications of RoPE that also revisit intrinsic failure modes rather than just interpolation tricks. Since the paper’s pitch is “few works revisit RoPE’s intrinsic computation,” I expected a more precise comparison of what exactly is new here: is it the complex-valued reinterpretation, the dual-head construction, the length-extrapolation argument, or the cache-efficiency configuration? Right now, those pieces are bundled together, which makes the contribution seem a bit more singular than it actually is.

10. **Presentation quality is uneven, and several figures/tables are under-explained in the main text.**  
    **Figure 2** is meant to be important for understanding how GQA changes under RoPE++EC and RoPE++EH, but the figure is small and the text does not walk through the tensor/accounting implications carefully. Similarly, **Figure 3** is central to the extrapolation claim in Section 3.4, yet it is hard to read from the main paper and the argument requires careful interpretation of which cross-dimension interactions have seen positive/negative embedding ranges during training. The paper also has numerous language and formatting issues, including repeated wording, broken equation layouts, and several places where the prose becomes more promotional than precise. For a method paper hinging on a subtle mathematical reinterpretation, this lack of polish hurts.

## Questions
1. The strongest concern for me is disentangling the benefit of the imaginary formulation from the benefit of architectural changes in RoPE++EC. Can the authors provide a control with the same number of output heads and comparable $W_o$ size, but replacing the imaginary branch with another deterministic query transform that is not derived from the imaginary component? This would help isolate whether the gains come from “imaginary attention” specifically.

2. In **Equation 5**, is the exponent in the discrete approximation a typo? It appears inconsistent with the standard frequency schedule and with **Equation 7** in the appendix. Please provide the corrected expression and confirm that the plotted characteristic curve in **Figure 1** uses the intended formula.

3. Relatedly, Appendix B seems to contain a likely typo involving $\boldsymbol{\mathcal{R}}_{-\frac{\sigma}{2}-\Delta t}$ in the imaginary-attention expectation argument. Please clarify the exact derivation and whether this should be $-\pi/2$ instead of $-\sigma/2$. Since the main narrative relies on these formulas, this clarification matters.

4. Can the authors provide more evidence that the long-context improvements transfer beyond synthetic retrieval-style benchmarks? Even one or two realistic long-context evaluations would substantially increase my confidence in the practical relevance of the method.

5. For **RoPE++EH**, can the authors better characterize when the half-cache tradeoff is favorable and when it is not? The mixed behavior in **Table 2**, especially on BABILong at 776M, suggests the tradeoff is benchmark-dependent. A clearer efficiency-quality Pareto analysis would help.

6. How sensitive are the findings in **Figure 5** to seed choice, layer/head choice, and the exact noise injection protocol? Right now the “imaginary heads are more dominant” claim feels stronger than the evidence shown. A more systematic perturbation study could strengthen the mechanistic argument.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
The work is a methodological study on positional encodings for language models and does not present a clear ethics issue in the main paper. The experiments use standard public corpora and benchmarks, and I did not identify a paper-specific concern requiring formal ethics review.

## Soundness Rating
3: good. The core method is technically plausible and the empirical evidence is meaningful, but several mathematical statements are presented too loosely, and the causal/mechanistic claims are stronger than what the evidence fully supports.

## Presentation Rating
2: fair. The overall structure is understandable, but the paper has notable notation issues, broken equation formatting, and some under-explained figures and claims that reduce clarity.

## Contribution Rating
3: good. The idea of exploiting the imaginary component of RoPE is interesting and useful enough to matter, especially for long-context modeling, but the empirical gains are moderate and the paper does not fully isolate what drives them.

## Overall Rating
6: Marginally above the acceptance threshold. But would not mind if paper is rejected. The paper has a real idea and enough evidence to be taken seriously, especially for long-context settings, but it overstates some of its theoretical conclusions and leaves important ablations and clarifications on the table.

## Reviewer Confidence
4: confident. I am confident in the overall assessment and checked the main mathematical and empirical claims with care, although some implementation-level details and all appendix derivations were not independently verified in full.