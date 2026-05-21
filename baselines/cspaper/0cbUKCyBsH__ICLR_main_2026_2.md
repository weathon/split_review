---
job_id: 8abfed0d-c888-4fad-ab20-080aaa44880d
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: 0cbUKCyBsH.pdf
paper: Influence-Aware Forecasting: Breaking the Self-Stimulation Barrier in Time Series
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is squarely within general machine learning, time series forecasting, multimodal learning, learning theory, and datasets/benchmarks, all of which are in scope for ICLR.

## Minimum Quality
Pass ✅. The paper includes the necessary components, abstract, introduction, related-work-style contextualization, method, experiments/results, and conclusion, and it presents a non-trivial methodological and benchmark contribution; however, there are substantial soundness and clarity issues that should be handled in full review rather than desk rejection.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find hidden prompts, reviewer-directed instructions, or other obvious manipulative content in the provided paper text and figures.

# Expected Review Outcome:
## Summary
This paper argues that standard time series forecasting suffers from a “self-stimulation” limitation, because models predict future values using only historical observations and ignore external influences. The paper introduces an influence-aware forecasting paradigm, IATSF, provides a benchmark with temporally aligned textual influences, and proposes a lightweight model, FIATS, that uses channel-aware cross-attention between time series channels and text embeddings. Experiments on synthetic, weather, traffic, electricity, and game-user datasets report sizable gains over standard forecasting baselines and several pretrained time-series foundation models.

## Strengths
The paper is ambitious in scope. It does not just propose another architecture tweak, it tries to tie together a problem diagnosis, a theoretical framing, a benchmark, and a baseline model. That breadth is valuable, and the paper does make a clear attempt to articulate why exogenous information should matter in forecasting rather than merely asserting it empirically.

The main empirical message is easy to follow: when future-relevant external context is available, using it helps. In particular, **Table 1 (Page 7)** shows very large gains on the FM Toy, NYC Traffic Speed, and both Atmospheric Physics variants. Even allowing for the caveats discussed below, the margins are large enough that they are unlikely to be explained by pure noise. The Atmospheric Physics results are especially notable because the improvements are sustained across all four forecast horizons.

The paper also includes some reasonably informative component analysis. **Table 3 (Page 9)** is one of the stronger parts of the experimental section. The “Zero News” and “Zero Desc.” ablations are directly tied to the claimed roles of influences and channel descriptions, and the degradation there is at least directionally consistent with the proposed design story. I appreciate that the authors did not restrict the ablation to swapping embedding backbones only.

Some figures are helpful for intuition. **Figure 2 (Page 6)** gives a fairly concrete overview of how FIATS combines a patch-based time-series encoder with a text-side influence encoder and a decoder modulated by influence embeddings. Even though some of the math around CASM/CAPS is underspecified, the diagram itself makes the dataflow easier to understand. Likewise, **Figure 3 (Page 8)** is useful because it does not only show a success case, it also exposes a failure mode, namely that FIATS misses a rainfall event when the influence input is absent or misaligned. That honesty is helpful.

The paper also tackles an under-served benchmark issue. The critique that many text-plus-time-series setups suffer from leakage, weak temporal alignment, or prompt-centric formulations is fair. A benchmark designed around temporally synced, externally sourced influence signals could be useful to the community if the dataset construction details are cleaned up and documented more rigorously.

## Weaknesses
I have quite a few concerns, and several of them affect the core scientific claims rather than just polish.

1. **The central theoretical claim is overstated relative to what is actually proved.**  
   The paper repeatedly states, starting from the abstract and Section 2, that it “formally prove[s]” a hard mathematical barrier for self-stimulated forecasting. But in the main paper, **Proposition 2.1 on Page 3** is presented as a general statement,
   \[
   \mathrm{Cov}(\epsilon)\succeq \mathbb{E}_{X_h}\left[\nabla_U F\,\Sigma\,(\nabla_U F)^\top\right],
   \]
   while the derivation in the appendix makes clear that this is only obtained through a **first-order Taylor approximation around \(U=\mu\)** in the nonlinear case, see **Eq. (29)-(32), Pages 17-18**. That is not a general exact lower bound for arbitrary nonlinear \(F\), it is an approximation whose validity depends on neglected higher-order terms. The distinction matters because the paper’s main rhetorical position, namely that a universal “hard barrier” has been proved, is much stronger than what the math supports. For nonlinear systems, the exact object is the conditional covariance \(\mathbb{E}_{X_h}[\mathrm{Cov}_U(F(X_h,U)\mid X_h)]\), not the Jacobian-based expression in Eq. (3). The current presentation mixes these up.

2. **The theoretical setup relies on assumptions that are much stronger than the paper admits, and these assumptions are often violated in the motivating applications.**  
   A key assumption throughout the proofs is \(U\perp X_h\), stated explicitly in the appendix, for example **Pages 14-18**. But in realistic forecasting settings, “external influences” such as weather, traffic incidents, marketing events, and game updates are rarely independent of the historical state. Weather today is correlated with weather yesterday; developer updates are endogenous to game performance; traffic conditions and weather both have temporal persistence. Once \(U\) is statistically dependent on \(X_h\), the decomposition into “irreducible self-stimulation error” plus model mismatch is no longer as clean as claimed, and self-stimulated models can partially infer information about \(U\) from \(X_h\). This substantially weakens the universality of the claimed barrier. The theory may still be useful as a stylized argument, but then it should be presented as such, not as a near-definitive explanation for why modern TSF has plateaued.

3. **There is a mismatch between the task formulation and the actual deployment setting.**  
   In **Section 4.1 (Page 4)**, the paper defines the input as future-aligned influence \(U_f\), and explicitly assumes influences take effect instantaneously. The benchmark then uses known future information, expert forecasts, or hypothetical future events as inputs. However, the main quantitative results do not seem to evaluate the realistic case where \(U_f\) itself must be forecasted with uncertainty. The appendix even states in **B.3 (Pages 21-22)** that inaccurate influence forecasting can dominate test error and “invalidates isolated model evaluation,” then circumvents this by assuming a near-perfect forecaster for fairness. That is a major loophole. If the practical claim is that influence-aware forecasting is “the primary path forward,” then the paper needs to quantify the benefit under noisy or imperfect future influence inputs in the main paper, not defer realism by assumption.

4. **The benchmark construction raises leakage and fairness questions that are not fully resolved in the main paper.**  
   The paper strongly emphasizes “leak-free” design, but some dataset construction choices are at best unusual. A concrete example is the Electricity Utility dataset, where the appendix states that the original timestamp was incorrect and the authors infer public holidays from **channel 319 showing obvious patterns**, then use that to produce captions, see **Page 39**. That is perilously close to constructing textual input from the target data itself. Even if the intent was benign, this should have been discussed explicitly in the main paper, because it directly affects the credibility of the benchmark. More broadly, the main paper says the atmospheric text is based on weather reports and summaries, but the appendix later clarifies that LLMs were used to generate diverse textual descriptions, see **Page 40**. The exact boundary between independent external information and processed summaries of future conditions is not sufficiently spelled out in the main paper.

5. **The empirical comparisons are not fully controlled, so it is hard to isolate whether gains come from access to extra information or from better modeling of that information.**  
   This is perhaps the most important experimental issue. In **Table 1 (Page 7)**, FIATS receives future-aligned textual influence inputs, whereas nearly all baselines are self-stimulated models that do not receive exogenous information at all. Unsurprisingly, the model with more information wins. But this only shows that the information is useful, not that FIATS is the right way to exploit it. A fairer comparison would include exogenous-aware baselines that consume the same or similar future influence input, such as straightforward concatenation or cross-attention variants built on strong backbones, or existing exogenous-variable forecasting baselines adapted to the benchmark. The paper cites exogenous-variable forecasting work in the introduction, but these methods are not represented in the main experiments. Without those controls, the architectural contribution is less convincing than the paper suggests.

6. **Several method definitions are mathematically underspecified or inconsistent.**  
   The FIATS description in **Section 5, Pages 5-6** has multiple notation problems. For instance, the paper defines
   \[
   \tilde C = Desc\cdot W_Q,\quad \widehat B_{U_f}=(News\cdot W_K)^\top,\quad \tilde U_f=News\cdot W_V,
   \]
   but never clearly specifies the dimensions of \(W_Q,W_K,W_V\), the number of heads, the scaling, or how the residual self-attention layers interact with the cross-attention block in CASM. The sentence “The above analysis show that the attention mechanism can effectively generate the channel-aware influence \(U_f^e\)” skips the actual derivation. In the CAPS description, the attention is written as \(Attention(Q=U_t^c,K,V=\hat Z)\), which is itself malformed notation because \(K\) is left undefined while \(V=\hat Z\) is defined. The text also says “we apply causal attention mask here” but does not specify along which axis the mask is applied, given that the queries come from channel-conditioned future influence embeddings rather than historical decoder tokens. These are not cosmetic issues, they make it difficult to reproduce or even rigorously understand the proposed architecture.

7. **The argument against channel-wise parameter sharing is weakly justified and partly confused.**  
   In **Section 5, Page 6**, the paper claims that previous shared models approximate all channels with the same parameters and introduces an error term
   \[
   \epsilon_i = o_i(Z)-\frac{1}{8}\sum_{j=1}^k o_j(Z),
   \]
   which is odd for at least two reasons. First, the hard-coded \(\frac{1}{8}\) is unexplained and appears inconsistent with general \(k\). Second, modern global multivariate forecasters do not literally reduce all channels to a plain arithmetic mean observation map. The appendix later presents a cleaner linear analysis of shared weights, **Eq. (68)-(78), Pages 22-23)**, but the main-paper version is sloppy and overstates the flaw in prior approaches. If channel-aware decoding is a key contribution, the main paper should present a coherent derivation, not a straw-man approximation.

8. **Some empirical claims are too broad relative to the evidence.**  
   The abstract and conclusion repeatedly suggest that influence-aware modeling is the main route forward for time series forecasting in general. That claim is much broader than what the experiments establish. The paper mostly studies settings where useful future-aligned textual or weather information is deliberately available. This is an important subset of forecasting problems, but far from the whole field. Many time-series tasks do not have reliable future exogenous context, or only have weakly informative proxies. The paper would be much stronger if it framed its contribution as identifying and validating a promising regime, not as diagnosing the field at large.

9. **The presentation quality is below the level expected for a paper making strong theoretical claims.**  
   There are many grammatical errors, notation inconsistencies, and imprecise statements throughout the main paper. A few examples: “obserevation” in the introduction, “falls back to” instead of “reduces to” in **Page 3**, “The above analysis show” on **Page 6**, inconsistent use of \(U_t\) versus \(U_f\), and a duplicated notation entry for \(X_f\) in **Table 4 (Page 13)** where it denotes both future segment and forecasted segment. There is also confusion between \(D\) as dataset and \(D\) as channel descriptors. For a paper whose contribution leans heavily on formal framing, this level of imprecision is costly.

10. **Some figures are suggestive, but they do not fully support the strongest claims being made.**  
    **Figure 1 (Page 3)** is intended to illustrate the “averaging” pathology of self-stimulated forecasting, and the synthetic example is intuitive. But it is essentially a pedagogical cartoon plus one toy visualization; it does not validate the general theory. **Figure 5 (Page 9)** shows attention heatmaps for CASM layers and the text claims these demonstrate sensitivity modeling. I am not convinced. Attention maps are not direct evidence that the model has learned causal or even semantically faithful influence-channel relations, particularly without quantitative analysis linking those maps to predictive importance. At present the figure is interesting but closer to post-hoc storytelling than rigorous validation.

11. **The GAUD evaluation is difficult to interpret from the main paper alone.**  
    The main paper gives only **Figure 4 (Page 8)** and a summary statement that FIATS ranks first on 59.6% of games and improves PatchTST by 12.6% on average. But the appendix tables reveal substantial heterogeneity and several cases where the non-pretrained FIATS is much worse than PatchTST, while the best-performing system is often a pretrained variant labeled “IATSF_pretrain,” not the exact model emphasized in the main text. This makes the central narrative less clean than the main paper suggests. At minimum, the main paper should clearly distinguish FIATS from its pretrained variant and discuss failure cases.

## Questions
1. The main theoretical point would be much more credible if you clearly separated the exact and approximate results. Can you restate **Proposition 2.1** in terms of the exact quantity
   \[
   \mathbb{E}_{X_h}\big[\mathrm{Cov}_U(F(X_h,U)\mid X_h)\big]
   \]
   and then present Eq. (3) only as a first-order approximation under explicit smoothness and small-variance assumptions? A precise rebuttal here would materially improve my confidence.

2. How critical is the assumption \(U\perp X_h\) for your conclusions? Please discuss what remains true when \(U\) is temporally persistent or statistically dependent on \(X_h\), which seems to be the realistic case for weather, traffic, and market systems. If you have experiments where the influence is partially inferable from history, that would help.

3. Please clarify exactly how future influence text is obtained for each benchmark in the main paper, not only the appendix. For Atmospheric Physics, are the text inputs generated from contemporaneously available forecasts, from historical weather reports corresponding to the future interval, or from LLM summaries of those reports? This distinction is central to the leak-free claim.

4. Can you provide one or more exogenous-aware baselines that consume the same future influence signal? For example, a strong patch-based TS backbone with simple text concatenation, FiLM-style conditioning, or standard cross-attention without CASM/CAPS. This would help disentangle “extra information helps” from “FIATS is the right architecture.”

5. For the Electricity Utility dataset, please explain in detail the procedure described on **Page 39** where holidays are inferred from channel 319. Why is this not target-derived leakage? If the captions depend on thresholding a target channel, please justify why this remains a valid benchmark.

6. The architecture section needs more precise definitions. Please provide explicit tensor shapes and a step-by-step computation for CASM and CAPS, including the exact attention equations, masking, and how channel descriptions interact with patch tokens over time. A pseudocode block would help substantially.

7. The appendix discusses the effect of imperfect influence forecasts. Can you include, in the main paper, a robustness experiment where the influence input is corrupted or replaced with a realistic forecast proxy? **Figure 6 (Page 9 / Page 10)** already hints at noise sensitivity, but it is too abstract. A task-grounded noisy-influence experiment would make the practical contribution much more convincing.

## Flag For Ethics Review
- Yes, Legal compliance (e.g., GDPR, copyright, terms of use)  
- Yes, Responsible research practice (e.g., human subjects, data release)  

## Details Of Ethics Concerns
The concerns are moderate rather than severe, but they are worth checking because the paper’s benchmark contribution depends on data provenance and release conditions.

First, the appendix states that parts of the benchmark will be released under **CC BY-NC-SA 4.0** and that some source data forbid commercial use, see **Pages 38-40**. That may be fine for research use, but the paper should be explicit about which components can be redistributed, which are only transformed derivatives, and whether the planned benchmark release is fully compliant with the source websites’ terms.

Second, the GAUD dataset uses developer logs and the paper says only precomputed embeddings may be released to avoid intellectual property constraints, see **Page 41**. That is sensible, but it also means reproducibility and downstream redistribution rights need to be clearly documented.

Third, for the Atmospheric Physics dataset, the paper uses LLMs to generate or diversify textual descriptions, see **Page 40**. This is not inherently problematic, but benchmark papers should clearly label which text is raw, which is transformed, and which is LLM-generated, since this affects the meaning of “external influences” and the legal status of the released data.

## Soundness Rating
2: fair. The empirical signal is interesting and likely directionally correct, but the main theoretical claims are overstated, key assumptions are strong, and the experimental design does not yet cleanly isolate architectural merit from privileged access to extra information.

## Presentation Rating
2: fair. The high-level story is understandable, and some figures/tables are helpful, but the paper has substantial notation issues, imprecise claims, and several places where the method description is too loose for a technically ambitious submission.

## Contribution Rating
2: fair. The paper identifies a meaningful forecasting regime, namely forecasting with temporally aligned external influence text, and the benchmark effort could be useful. However, the current novelty and significance are diluted by overstated universality claims, insufficiently controlled comparisons, and unresolved benchmark-definition concerns.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted. The paper has a real idea in it, and the benchmark plus empirical results make it more than a throwaway submission. Still, in its current form, I do not think the theoretical framing and experimental evidence are tight enough to support the strength of the claims, especially the “hard barrier” narrative and the implication that FIATS specifically, rather than simply extra future information, is what the experiments validate.

## Reviewer Confidence
4: confident. I am confident in the main concerns, especially around the theory-experiment mismatch, fairness of the comparisons, and technical clarity, though some benchmark-construction details would benefit from author clarification.