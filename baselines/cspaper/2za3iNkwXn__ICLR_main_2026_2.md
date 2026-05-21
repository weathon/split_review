---
job_id: 3924a30d-c5d6-4f31-b5f2-874e7ff7a4be
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: 2za3iNkwXn.pdf
paper: When Reasoning Meets Compression: Understanding the Effects of LLMs Compression on Large Reasoning Models
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, it studies compression, benchmarking, and mechanistic interpretation of large reasoning models, which fits large-scale learning, language modeling, benchmarks, and interpretation of learned representations.

## Minimum Quality
Pass ✅. The paper contains the essential components expected of a research submission, including abstract, introduction, methodology, experiments, quantitative results, interpretation analysis, and conclusion. While I have technical and evidentiary concerns, they do not rise to the level of a desk rejection.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find hidden prompts, reviewer-targeting instructions, or other manipulative content in the provided paper text and figures.

# Expected Review Outcome:
## Summary
This paper studies how three compression paradigms, quantization, distillation, and pruning, affect large reasoning models, primarily DeepSeek-R1 and its distilled variants. The authors combine performance benchmarking on four reasoning datasets with a mechanistic interpretation pipeline based on difference-of-means steering vectors and attribution patching over linear modules, then use the resulting importance scores to identify modules that appear especially sensitive to compression and to motivate selective protection experiments.

## Strengths
The paper tackles a timely and practically relevant question. Compression of reasoning-focused LLMs is becoming important very quickly, and the paper does more than just report another benchmark table, it tries to connect performance degradation to weight-level structure. That broader framing is useful.

The empirical scope is reasonably broad for a main-paper study. In **Table 1** the paper compares several compression families rather than only one favorite method, and includes dynamic low-bit quantization, multiple PTQ baselines, distillation-only models, and pruning. Even if these comparisons are not perfectly apples-to-apples, the table gives a helpful high-level map of where current methods break first. In particular, the contrast between relatively mild degradation at 4-bit and sharp degradation for several 3-bit settings is an informative empirical takeaway.

The paper has a concrete mechanistic angle, which is more interesting than a pure benchmarking submission. The use of module-by-layer heatmaps is a strength of the presentation. **Figure 2** is especially useful because it shows both absolute importance for the distilled model and the importance shift relative to the base model. Whether or not one fully buys the causal interpretation, the figure does support the narrower claim that the final layer, and specifically the final-layer MLP up projection, is an outlier under the authors' metric. This is one of the clearer parts of the paper.

The authors do not stop at interpretation and try to validate it interventionally. **Table 3** is a strong part of the paper: selectively quantizing a single component and observing large accuracy drops is a sensible way to stress-test the importance ranking. The fact that `32_up` performs worst on average among the tested single-component perturbations gives at least some empirical support that the score is not pure visualization theater.

The mixed-precision protection experiment in **Table 4** is simple but practically meaningful. Protecting only the final-layer MLP while keeping the rest in 3-bit and recovering nontrivial average accuracy is exactly the kind of result that compression researchers can act on. I appreciate that this experiment is tightly linked to the interpretation claim rather than being an unrelated add-on.

The writing is generally readable, and **Figure 1** gives a decent overview of the pipeline from benchmarking to interpretation to verification. For a paper spanning several compression paradigms and multiple model families, the structure is relatively easy to follow.

## Weaknesses
1. **The central mechanistic claims are stronger than what the proposed attribution setup really supports.**  
   The paper repeatedly talks about locating “the most important weights” and “causal relationships” between weights and reasoning capabilities, especially in **Sections 2.2, 2.3, and 4.1**. But the actual pipeline computes a behavior-specific direction from difference of means and then uses a gradient-based score,
   \[
   \mathbf{I}_{m\ell}^{c}\approx \frac{1}{|\mathcal{D}_{+}|}\left|\sum_{s_i^c\in \mathcal{D}_+} (\hat{\mathbf{u}}_{m\ell}^c)^\top \frac{\partial}{\partial \mathbf{a}_{m\ell}} \mathcal{L}(s_i^c)\right|,
   \]
   in **Equation on Page 4**. This is an attribution proxy, not a direct causal effect estimate. It is sensitive to scaling, local linearization error, and the choice of loss and token subset. The paper does include downstream validation, which helps, but the wording remains too causal throughout. A more careful phrasing would be “importance under this attribution metric” rather than “precisely locate compression effects on model weights” or “causal relationships.”

2. **The mathematical formulation is underspecified and in places inconsistent enough to reduce confidence in the interpretation results.**  
   There are several issues in **Section 2.2**:
   - In the normalization definition on **Page 4**, the notation appears inconsistent:
     \[
     \hat{\mathbf{u}}_{m\ell}^{c}=\mathbf{u}_{m\ell}^{c}\cdot\left\lVert\frac{\mathbf{a}_{m\ell}^{\text{all}}}{\mathbf{a}_{m\ell}^{c}}\right\rVert_{2}
     \]
     but the text defines \(\overline{\mathbf{a}}_{m\ell}^{\text{all}}\), not \(\mathbf{a}_{m\ell}^{\text{all}}\), and it is not clear what \(\mathbf{a}_{m\ell}^c\) in the denominator exactly denotes, since earlier the behavior-conditioned object is \(\overline{\mathbf{a}}_{m\ell}^c(s_i^c)\), not a single aggregate vector with this name. Is this a ratio of norms, an elementwise division, or shorthand for a scalar rescaling? As written, it is ambiguous.
   - The definition of \(s_j\) is “the token sequence of the entire LRM output (prompt and output tokens)” on **Page 3**, which is odd because the prompt is not output. More importantly, comparing behavior spans from generated reasoning traces to full prompt-plus-output sequences may inject a strong confound unrelated to the target behavior.
   - The loss \(\mathcal{L}(s_i^c)\) in the attribution step is called “the cross-entropy loss of \(s_i^c\),” but it is not specified whether the gradient is taken only over the labeled span, over next-token losses within the span, or over the whole sequence conditioned on the prompt. That distinction matters for interpreting \(\partial \mathcal{L}/\partial \mathbf{a}_{m\ell}\).
   
   These are not cosmetic issues. This interpretation pipeline is one of the paper’s main contributions, and the exact meaning of the score depends on these choices.

3. **The evidence for “knowledge is affected more than reasoning” is suggestive, but the paper overstates what is established.**  
   The core claim in **Section 3.3** and Takeaway 3.3 is that “pruning and distillation compress knowledge retention more than reasoning capabilities.” The main evidence is mostly MuSiQue under a closed-book setting plus parameter-count differences across models in **Tables 1 and 2**. The problem is that MuSiQue is not a pure knowledge probe. It combines retrieval burden, multi-hop decomposition, answer generation, and potentially calibration issues. So lower MuSiQue does not isolate parametric knowledge loss. The appendix RAG result is directionally interesting, but in the main paper the claim is stronger than the main-text evidence warrants. At minimum, the paper should present this as a hypothesis supported by MuSiQue and not as a general conclusion about knowledge vs reasoning.

4. **The benchmark design is narrower than the paper’s broad claims of generalization.**  
   The abstract and conclusion make claims that “generalize across both R1 and non-R1 LRMs,” and the paper often discusses “LRMs” broadly. But the main paper is still heavily centered on DeepSeek-R1 and R1-distilled Llama/Qwen models. The selected tasks in **Section 2.5** are all short-answer benchmark-style datasets, mostly accuracy-driven and fairly constrained. There are no open-ended reasoning tasks, no process supervision metrics, no tool-use settings, no long-form generation quality checks, and no broader non-R1 analysis in the main text. So the paper’s actual evidence supports “these findings appear on the specific families and tasks we tested,” not a field-wide claim about LRMs.

5. **The comparison across compression methods is not fully controlled, which weakens some cross-method conclusions.**  
   This is visible in **Table 1** and acknowledged partly in **Appendix D**. The dynamic quantization results on full DeepSeek-R1 are not directly comparable to the 4-bit/3-bit PTQ results on distilled non-MoE models. The methods differ in architecture, calibration regime, and deployment stack. The paper still draws broad takeaways such as 2.51-bit dynamic quantization being the “best overall performance” and uses those comparisons to discuss compression strategy quality. That is understandable from an empirical survey perspective, but it is not a controlled comparison. The conclusions should distinguish clearly between “best among tested model+method combinations” and “best compression strategy.”

6. **The selective validation experiments are useful but still too narrow to fully support the stronger importance-ranking claims.**  
   **Table 3** tests only five single-component perturbations on one model, and the rank-order consistency is already imperfect, as the authors note with `1_up`. That is not fatal, but it means the evidence is still limited. If the paper wants to claim that the attribution metric solves a “fundamental problem” of locating important weights, it needs broader validation across more modules, more models, and ideally more perturbation types. Right now the evidence supports a narrower claim that the metric can help identify some highly sensitive modules.

7. **The decision to visualize only decreases in relative importance risks confirmation bias in the main narrative.**  
   In **Section 2.3**, the paper sets all increases in relative importance to zero for the main visualizations. I understand the intuition, and the appendix tries to justify it, but this is still a loaded presentation choice. Relative importance is normalized to sum to one, so decreases and increases are coupled. Hiding one side of the shift makes it easier to tell a one-directional damage story. In **Figure 3**, for example, the concentration of dark values in final-layer modules supports the “overly compressed” claim, but without net-change or increase views in the main paper the reader cannot judge whether this is part of a broader redistribution pattern. Since these heatmaps are central evidence, the main text should show at least one net-change figure, not delegate that to the appendix.

8. **Statistical reliability is thin for some of the key interpretation inputs.**  
   The interpretability dataset consists of only 120 annotated instances, 30 from each benchmark, as stated in **Section 2.2**. For four behaviors and module-wise heatmaps over every layer and linear component, that is not much data. The GPT-4o annotation robustness check is only described in the appendix, and even there some uncertainty intervals are wide. Given that fine-grained heatmaps in **Figures 2, 3, 4, 6, 7** are used to motivate concrete claims about specific projections and layers, the small annotation set raises concern about stability. The paper would be more convincing if it reported sensitivity of the highlighted modules to re-sampling or alternative annotation runs in the main text.

9. **Some performance claims would benefit from statistical caution, especially where differences are small or single-pass results are mixed.**  
   In **Table 1**, many differences among 4-bit methods are very small, sometimes within what one would expect from decoding variance, and the original R1 and dynamic quantized variants are marked with \( \dagger \) as not averaged over three runs. In **Table 2**, sparsity trends are informative, but again the table is one-pass only. This matters because the paper occasionally interprets relatively small gaps as meaningful evidence for method superiority or benchmark sensitivity. The broad trends are believable, but some of the sharper comparative conclusions should be toned down.

10. **Related-work positioning is decent but not fully sharpened around prior work on compression versus knowledge and on broader quantization benchmarking.**  
   The paper cites a large number of compression papers, which is good. Still, the discussion of the “knowledge vs reasoning” distinction in **Section 3.3** would benefit from tighter positioning relative to prior work specifically studying compression and parametric knowledge, and the quantization benchmarking angle could be positioned more explicitly against broader LLM compression benchmark/toolkit efforts. As written, the paper sometimes presents observations as more fresh than the positioning supports. This is not a fatal literature gap, but it does reduce the sharpness of the contribution claim.

## Questions
1. In **Section 2.2**, please define the normalization in the steering vector formula unambiguously. What exactly are \(\mathbf{a}_{m\ell}^{\text{all}}\) and \(\mathbf{a}_{m\ell}^{c}\) in
   \[
   \hat{\mathbf{u}}_{m\ell}^{c}=\mathbf{u}_{m\ell}^{c}\cdot\left\lVert\frac{\mathbf{a}_{m\ell}^{\text{all}}}{\mathbf{a}_{m\ell}^{c}}\right\rVert_2 ?
   \]
   Is the division elementwise, and over which aggregated vectors? A clean correction here would materially increase confidence.

2. For the attribution score, what is the exact loss being differentiated? Is \(\mathcal{L}(s_i^c)\) the sum of next-token cross-entropies over the labeled behavior span only, over the whole response, or something else? Also, at what token positions are activations \(\mathbf{a}_{m\ell}\) taken for the gradient contraction?

3. Can the authors provide a stability analysis of the highlighted modules under annotation re-sampling or alternative behavior-span extraction? For example, does final-layer `up_proj` remain top-ranked if the 120-instance set is bootstrapped or if the GPT-4o annotations are regenerated with a different seed/temperature?

4. The key claim in **Section 3.3** is about knowledge vs reasoning. Can the authors moderate or better justify that claim using more direct evidence? For example, even a compact main-text analysis separating knowledge-heavy and knowledge-light subsets, or reporting a more direct factual recall probe, would help.

5. In **Figure 3**, the claim is that AWQ overly compresses final-layer modules and gate projections. Could the authors report whether this pattern still holds when visualizing net change rather than only decreases, or include a summary metric of total lost relative importance in these modules? That would reduce concern that the figure is partly a presentation artifact.

6. For **Table 3**, can the authors expand the validation beyond five selected modules, perhaps by testing a larger sample of modules spanning the rank spectrum? Right now the evidence is promising, but somewhat cherry-pickable.

7. Given that **Table 1** compares dynamic quantization on full R1 against PTQ methods on distilled models, can the authors be more explicit about which conclusions are cross-method and which are just observations across different model-method combinations? A clearer separation would improve the paper’s scientific precision.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
No major ethics concerns are apparent from the main paper. The work is a benchmarking and interpretability study of model compression methods and does not appear to involve sensitive human subjects data or risky deployment claims in the main text.

## Soundness Rating
2: fair. The paper has a real empirical contribution and some convincing intervention-based validation, but several of the strongest claims, especially around causality, weight importance, and knowledge-versus-reasoning, are supported less cleanly than the writing suggests.

## Presentation Rating
3: good. The paper is generally well organized and readable, and the figures and tables are informative, but key mathematical definitions in Section 2 are not precise enough for a contribution that leans heavily on the interpretation method.

## Contribution Rating
2: fair. The combination of benchmarking and mechanistic analysis is interesting and useful, especially the selective protection result, but the broader claims are a bit overextended relative to the evidence and the main-paper scope remains somewhat narrow.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted. The paper is timely, reasonably executed, and has one practically useful result, namely identifying modules worth protecting during quantization. Still, the mechanistic methodology is not specified cleanly enough, several conclusions are stronger than the evidence warrants, and the generalization claims should be more restrained for an ICLR main-track acceptance.

## Reviewer Confidence
4: confident. I am familiar with LLM compression and interpretability work, and I checked the main methodological and empirical claims carefully, though I did not verify appendix-only details exhaustively.