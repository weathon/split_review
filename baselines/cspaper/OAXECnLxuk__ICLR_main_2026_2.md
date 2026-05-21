---
job_id: 4ca4d479-0410-49cf-a8ff-e4ec5f489b9c
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: OAXECnLxuk.pdf
paper: DaVinci: Reinforcing Visual-Structural Syntax in MLLMs for Generalized Scientific Diagram Parsing
main_score_norm: 0.6
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, combining multimodal representation learning, reinforcement learning, structured prediction, and a dataset/benchmark contribution for diagram-to-code generation.

## Minimum Quality
Pass ✅. The paper contains the necessary scientific components, including abstract, introduction, related work, methodology, experiments, results analysis, and conclusion. While I found several non-trivial issues and inconsistencies that lower my confidence in some claims, they do not rise to the level of a desk rejection.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find hidden instructions, suspicious reviewer-targeted prompts, or other manipulative content in the provided paper text.

# Expected Review Outcome:
## Summary
This paper studies scientific diagram parsing as image-to-TikZ generation with multimodal LLMs. The authors propose DaVinci, a two-stage framework that first performs supervised fine-tuning on a newly curated TikZ30K dataset with reordered code and injected comments, and then applies GRPO-based reinforcement learning with a hybrid reward combining text alignment, geometric matching, image similarity, and compile success. Experiments on DATikZ\(_{v3}\) report strong compile rates and competitive image fidelity, with additional human evaluation and ablations on data curation and reward design.

## Strengths
1. The paper tackles a real and difficult problem. Parsing raster scientific diagrams into structured, editable code is a meaningful task, and the motivation is clear from both the introduction and the use cases in **Figure 1**. The editability angle, converting image to TikZ and then to SVG or code-editable representations, is practically compelling and relevant to the ICLR audience interested in multimodal reasoning and structured generation.

2. The overall system design is sensible. The separation between SFT for learning local primitives and grammar, followed by RL for structural refinement, is intuitive and reasonably motivated. **Figure 3** is especially helpful here, because it makes clear that the RL signal is not purely image-based, but decomposes into code-, vector-, and image-level feedback. That multimodal reward construction is one of the paper’s better ideas.

3. The data curation story is stronger than in many dataset-heavy papers. The authors do more than simply collect code-image pairs. The explicit attention to drawing order normalization and comment injection is well motivated, and **Figure 2** provides a concrete visualization of why raw TikZ ordering can be harmful for autoregressive models. This is not just a cosmetic preprocessing step, it directly changes the learning problem from one with arbitrary sequence permutations to one with more consistent target programs.

4. The empirical gains on compile rate are substantial. In **Table 1**, DaVinci-7B reaches **97.60 Pass@1**, which is a large jump over the base Qwen2.5-VL-7B (**59.59**) and also clearly above strong open and proprietary baselines on this metric. For this task, compile success is not a side metric, it is central, so this is a meaningful improvement.

5. The ablation on data processing is informative. **Table 4** shows a fairly clean progression from the base model to Original30K, Reordering30K, and TikZ30K, suggesting that both reordering and comments matter. The increase from **69.74** to **78.78** to **84.50 Pass@1** gives useful evidence that the dataset interventions are doing real work rather than being decorative narrative.

6. The reward ablation in **Table 5** is also directionally supportive. Adding \(R_{\text{text}}\) improves textual alignment metrics, and adding both \(R_{\text{text}}\) and \(R_{\text{geom}}\) improves the custom textual and geometry scores while also improving MSE and LPIPS relative to the image-only base. I appreciate that the table does not only report the final combined model, but decomposes the reward contribution.

7. The paper includes qualitative analysis rather than hiding behind aggregate metrics. **Figure 4** is useful because it shows the kinds of structural and alignment differences the authors care about, such as node placement, graph connectivity, and text positioning. The examples support the claim that compile rate alone is not enough and that structural fidelity matters.

8. The human evaluation is a welcome addition. Even though I have some concerns about interpretation, the use of Best-Worst Scaling and reporting of inter-annotator agreement adds credibility beyond automated image similarity metrics.

## Weaknesses
1. The paper’s experimental reporting contains several internal inconsistencies, and this matters more than the authors seem to realize. On **Page 7, Section 4.1**, RL training is described with a global batch size of **512**, rollout batch size **256**, rollout number **10**, and **500 steps**. In contrast, **Table 12 on Page 35** reports global batch size **128**, rollout number **8**, and **300 steps**. These are not minor bookkeeping differences, they materially affect compute, optimization dynamics, and reproducibility. If the paper wants credit for careful RL post-training, the training configuration cannot drift between the main text and appendix. Right now, I do not know which setup actually produced the reported numbers.

2. The formulation of the hybrid reward is underspecified and, in places, mathematically inconsistent with the text. In **Equation (2)** on **Page 5**, the total reward is written as
\[
R_{\text{hybrid}} = R_{\text{text}} + R_{\text{geom}} + R_{\text{img}} + R_{\text{pass}},
\]
and the paper says “we do not set special weights for each reward component.” But in the very next paragraph on **Page 6**, \(R_{\text{pass}}\) is said not to be an explicit bonus at all; instead, if compilation fails, the other three rewards are forced to their minimum values. That means \(R_{\text{pass}}\) is not actually an additive term in the sense suggested by Equation (2). This is more than notation sloppiness, because it changes the optimization landscape. The authors should either redefine \(R_{\text{hybrid}}\) piecewise, for example
\[
R_{\text{hybrid}}(C)=
\begin{cases}
R_{\text{text}} + R_{\text{geom}} + R_{\text{img}}, & \text{if compile}(C)=1 \\
R_{\min}, & \text{otherwise,}
\end{cases}
\]
or explicitly define \(R_{\text{pass}}\) as a scalar and keep the other terms untouched. As written, the equation and prose do not match.

3. The spatio-textual reward description mixes two different extraction stories and is therefore confusing. On **Pages 5 to 6**, the paper argues that PDF vectorization allows text extraction in an “error-free manner,” because the exact text objects and boxes are available from the PDF. But the matching pipeline then discusses “minor OCR errors” and a Levenshtein-threshold stage in **Algorithm 1** and surrounding text. If the text is directly extracted from vectorized PDFs, OCR errors should not be part of the core failure model. If there are normalization issues, ligatures, LaTeX tokenization mismatches, or parser-level extraction failures, the paper should say that. Right now “error-free extraction” and “approximate matching for OCR errors” are in tension. This matters because the whole reward design is sold on being more precise than OCR-based alternatives.

4. Several critical reward-design details are missing from the main paper, which makes it hard to assess whether the method is actually well specified. For \(R_{\text{text}}\), **Equation (3)** depends on the matching procedure and an “adaptive threshold,” but the threshold function is not defined in the main text. For \(R_{\text{geom}}\), **Equation (4)** uses a scaling constant \(k\), but the paper never states its value in the main paper. The type-specific costs on **Pages 32 to 33** are better specified, but the extraction procedure for geometric primitives from PDFs is still only described at a fairly high level. For a reward-driven RL paper, these are core methodological ingredients, not implementation trivia.

5. The claim strength around proprietary model comparisons is too aggressive relative to the evidence. In the abstract and introduction, the paper states that DaVinci “surpasses leading proprietary models like GPT-5 and Claude-Sonnet-4,” which is directionally supported on compile rate in **Table 1**. However, the broader framing reads as if the model is uniformly stronger, which is not true. In **Table 1**, Gemini-2.5-Pro-Thinking has better DreamSim and LPIPS than DaVinci-7B, and in human evaluation **Table 3**, Gemini clearly outperforms DaVinci-7B with a score of **0.50** versus **-0.01**. The authors partially acknowledge this on **Page 9**, but the headline narrative still overreaches. A more careful claim would be that DaVinci excels in compile success and overall open-model performance, while remaining mixed against the strongest proprietary systems.

6. The evaluation remains heavily image-centric despite the paper’s emphasis on structural syntax. This is a conceptual mismatch. The central pitch is that diagrams require correct structural relationships, spatial-textual alignment, and geometric consistency. Yet the primary quantitative evaluation in **Table 1** is dominated by image metrics and surface code metrics like TED and cBLEU. The paper does include custom textual and geometry scores in **Table 5**, but only for reward ablations, not for the main benchmark comparisons in **Table 1**. That omission matters because the paper’s main contribution is precisely a structure-aware reward. Without reporting structure-aware metrics for all models on the main benchmark, the case for superior structural parsing remains incomplete.

7. Relatedly, the human evaluation actually exposes a tension that the paper does not sufficiently resolve. **Figure 4** and the accompanying discussion on **Pages 8 to 10** suggest DaVinci has superior structural precision in many examples, but **Table 3** shows it is not preferred over Gemini by human annotators. This does not invalidate the method, but it does weaken the implied connection between the proposed reward components and human-perceived quality. The paper would be stronger if it analyzed failure modes where high compile success and good custom reward alignment do not translate to better human judgments.

8. The novelty is moderate rather than especially strong. The system combines three familiar ingredients: curated SFT data, reward-based post-training with GRPO, and multimodal similarity signals. The useful part is the vectorized representation for reward construction, but the paper does not do enough to distinguish this from adjacent rendering-aware or structure-aware reward design work. There are also missing or under-discussed neighboring works on diagram/graphics code generation and evaluation that would help position the contribution more sharply, especially recent RL-style graphics program synthesis and structure-aware diagram evaluation. As written, the paper is stronger on execution than on literature positioning.

9. The analysis of **Figure 2** and the dataset augmentation story is persuasive, but the paper does not quantify how often the original datasets actually suffer from ordering pathologies or how much diversity is lost by normalization. This matters because code reordering could in principle remove legitimate stylistic variability and make the model better at reproducing the authors’ canonicalized syntax rather than truly better at parsing. **Table 4** shows compile-rate gains after reordering, but not whether structural fidelity or semantic correctness also improves independently of compiler success.

10. The qualitative section is helpful but somewhat cherry-picked. **Figure 4** shows examples favorable to DaVinci, yet the paper does not include representative failure cases in the main text. Given that the paper explicitly says the remaining failures are mainly dense plots or long outputs on **Page 8**, it would be much more informative to visualize those. Without that, the qualitative evidence is one-sided.

11. There is a mismatch between some code-level metrics and the claimed semantics of the task. On **Page 9**, the authors correctly note that cBLEU can go down while visual fidelity improves. That is fair. But then TED and cBLEU remain prominent main-table metrics in **Table 1** without deeper interpretation. If the authors believe these metrics are weak proxies, they should either downplay them or explicitly discuss when they are misleading. Otherwise the presentation sends mixed signals about what constitutes success.

12. The math around GRPO is mostly standard, but the paper does not discuss an important numerical edge case in **Equation (1)** on **Page 5** and Appendix **Equation (1)** on **Page 15**:
\[
\hat{A}_k = \frac{R_{\text{hybrid}}^{(k)} - \operatorname{mean}(\{R_{\text{hybrid}}^{(j)}\}_{j=1}^G)}{\operatorname{std}(\{R_{\text{hybrid}}^{(j)}\}_{j=1}^G)}.
\]
What happens when all samples in the group receive the same reward, or nearly the same reward, so that the denominator is zero or tiny? This is not a theoretical nitpick. With bounded rewards and compile-failure collapse, low-variance groups are plausible early in training. The paper should state the stabilization used, e.g. \(\operatorname{std}(\cdot)+\epsilon\), or explain how these cases are handled in implementation.

13. Some presentation issues reduce trust. There are repeated terminology inconsistencies, for example “Ti\&Z”, “Ti$\textit{k}$Z”, “TikZ”, “vectorization representation,” and “LIPIS” on **Page 8**, which should presumably be LPIPS. On their own these are minor, but in a paper whose main claims hinge on careful reward and evaluation design, the cumulative effect is that important details feel less polished than they should.

## Questions
1. Please reconcile the RL training settings between **Page 7, Section 4.1** and **Table 12 on Page 35**. Which values are correct for global batch size, rollout number, and training steps, and did the reported benchmark numbers use the same configuration throughout?

2. Can you rewrite **Equation (2)** to match the actual implementation of compile failure handling? Right now the additive formula and the prose description of \(R_{\text{pass}}\) are inconsistent. A precise piecewise definition would increase confidence.

3. For **Equation (3)** and **Algorithm 1**, what exactly is the adaptive threshold \(\tau\)? Please provide the explicit function and explain why approximate text matching is needed if text is extracted directly from the PDF vector representation.

4. For **Equation (4)**, what value of the scaling constant \(k\) was used, and how sensitive are results to it? Even a small sensitivity study would help, since the exponential transform can change the reward geometry a lot.

5. Could you report your custom structure-aware metrics, namely the textual and geometry scores used in **Table 5**, for all models in the main benchmark table? That would materially strengthen the paper, because those metrics are closer to the stated motivation than cBLEU or SSIM alone.

6. Can you provide a comparison against an OCR-based text reward or a raster-parser-based geometry reward? The paper repeatedly argues that vectorized extraction is superior and “error-free,” but there is no direct empirical ablation quantifying that design choice.

7. On the data side, how frequently did code reordering change the sequence substantially, and how often did comment injection alter semantic decomposition? It would help to know whether the gains in **Table 4** come from a widespread improvement or a small subset of highly noisy examples.

8. Please add failure-case analysis in the main paper. In particular, examples where DaVinci compiles successfully but loses semantic structure would be more informative than only favorable examples from **Figure 4**.

9. How were prompts and output constraints standardized across proprietary baselines in **Table 1**? Since compile rate is very sensitive to formatting and package imports, small prompting differences can have outsized effects.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
The paper includes a short data release and licensing discussion, and the human evaluation setup is transparently described with participant demographics and compensation. Based on the main paper, I do not see an ethics issue that requires separate escalation. That said, the licensing and reconstruction approach for partially non-redistributable arXiv-derived sources should remain carefully documented in the final version.

## Soundness Rating
2: fair. The paper presents a plausible method with meaningful experiments, but key methodological details are underspecified and there are important inconsistencies in the training description and reward formalization.

## Presentation Rating
3: good. The paper is readable and generally well organized, with helpful figures such as **Figures 2, 3, and 4**, but clarity is hurt by notation drift, terminology inconsistencies, and some ambiguous or contradictory descriptions.

## Contribution Rating
3: good. The task is important, the dataset curation and vectorized-reward idea are useful, and the empirical gains are substantial, especially on compile rate. Still, the contribution feels more like a strong systems/data/reward integration than a sharply isolated conceptual advance.

## Overall Rating
6: Marginally above the acceptance threshold. But would not mind if paper is rejected.  
I lean positive because the problem is important, the empirical gains are real, and the combination of data curation plus vectorized reward design appears useful in practice. However, the paper needs a more rigorous and internally consistent presentation of its RL setup and reward definition to fully justify its stronger claims.

## Reviewer Confidence
4: confident. I am familiar with multimodal generation, structured prediction, and RL post-training, and I checked the technical details carefully, though some implementation specifics remain unclear from the paper alone.