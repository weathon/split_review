---
job_id: a528afc7-7740-4fbb-a701-524dabf2baba
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: ZF0xRAdsuY.pdf
paper: Bound by Semanticity: Universal Laws Governing the Generalization-Identification Tradeoff
main_score_norm: 0.6
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is directly in scope for ICLR, combining representation learning, metric/similarity learning, learning theory, and applications to neuroscience/cognitive science, with empirical studies on neural networks, CNNs, LLMs, and VLMs.

## Minimum Quality
Pass ✅. The paper contains the expected scientific components, namely abstract, introduction, setup/methodology, theoretical results, experiments, and discussion, and it presents a coherent technical contribution with mathematical derivations plus empirical validation. I do see limitations and some overreach in the claims, but not fatal flaws that would warrant desk rejection.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find hidden prompts, reviewer-targeting instructions, or other manipulative content in the provided paper text or figures.

# Expected Review Outcome:
## Summary
This paper studies a tradeoff between generalization and identification under finite semantic resolution. The main contribution is a theoretical framework, based on similarity judgments over metric spaces, that derives closed-form relationships between similarity-task accuracy $p_S$ and identification accuracy $p_I$ for simplified similarity functions, including extensions to noise and multi-item settings. The paper then presents empirical evidence from a toy ReLU network, a bird-species CNN experiment, and prompting-based studies on LLMs and VLMs, arguing that analogous finite-resolution effects appear in more realistic systems.

## Strengths
1. The paper has a clear and interesting core idea. The framing of representational limits through a generalization-identification tradeoff is easy to grasp, and the setup in Section 2 is conceptually clean. The use of two simple tasks, similarity judgment and identification, gives the theory a concrete operational meaning.

2. The theoretical development in Section 3 is stronger than what one often sees in papers making broad claims about representation. In particular, **Theorem 1** gives explicit formulas,
\[
p_S(\varepsilon)=\frac12+\langle b(\varepsilon)\rangle-\langle b(\varepsilon)\rangle^2-\mathrm{Var}(b(\varepsilon)),
\quad
p_I(\varepsilon)=1-\frac12\langle b(\varepsilon)\rangle,
\]
which make the role of geometry and heterogeneity interpretable. The dependence of $p_S$ on $\mathrm{Var}(b(\varepsilon))$ is a useful insight, not just a formal curiosity, because it predicts that non-homogeneous spaces should depress similarity performance relative to a homogeneous ideal.

3. The extension to the multi-item regime in **Equations (7) and (8)** is valuable. Even though the formulas become more involved, the asymptotic interpretation, especially the approximate $p_I^n(\varepsilon)\approx (b(\varepsilon)n)^{-1}$ behavior discussed on Pages 6 to 7, gives a compact explanation for why multi-object processing could collapse quickly as the number of items increases.

4. **Figure 2** is effective. Panel (a) clearly illustrates the proposed Pareto region in the $(p_S,p_I)$ plane and distinguishes the homogeneous-space boundary from degraded performance under noise, while panel (b) visually conveys the penalty due to heterogeneity. This figure is one of the strongest parts of the exposition because it makes the theoretical claim immediately legible.

5. The toy-network experiment in Section 4 is a good match to the theory. **Figure 4b** is especially useful because it does not merely show endpoint performance, it shows trajectories through the $(p_S,p_I)$ plane during training. The comparison between the reconstruction-only run, the circle-trained run, and the segment-trained run provides an interpretable bridge from the closed-form theory to learned representations.

6. The paper deserves credit for attempting to connect the abstract theory to several model classes rather than stopping at a toy experiment. The CNN, LLM, and VLM studies in Section 5 make the paper more relevant to the broader ICLR audience.

7. The discussion section is appropriately candid about at least one important limitation, namely that the current framework focuses on non-compositional representations and does not directly account for hierarchical or symbolic generalization.

## Weaknesses
1. The paper’s strongest results are derived for a highly idealized similarity family, but the title and several claims are phrased in a much broader, almost law-like way than the evidence really supports. The central theory in Section 3 is built around the **constant similarity function in Definition 1**, namely
\[
g_{\varepsilon;\Delta}(x,y)=\mathbbm{1}_{B_\varepsilon(x)}(y)+\Delta\mathbbm{1}_{M\setminus B_\varepsilon(x)}(y).
\]
This is analytically convenient, but it is an extreme discretization of similarity. The paper does later discuss exponential and linear-decay intuitions, but the exact “universal Pareto front” claim on Pages 4 to 5 is only exact under restrictive assumptions, especially homogeneous spaces or the reduction to the scalar quantity $b(\varepsilon)$. In other words, the universal part is much more conditional than the presentation sometimes suggests. That matters scientifically because the paper’s headline message is stronger than what has actually been proven.

2. The decision rule in **Equation (1)** and **Equation (2)** uses Luce-style normalization over similarities,
\[
D_i=\frac{g(x_i,p)}{\sum_k g(x_k,p)},
\]
which is a specific behavioral model, not an inevitable consequence of the representation. The paper does not really justify why this is the correct or even preferred decoder for all the systems discussed later, especially CNNs, LLMs, and VLMs. In the toy model, the choice is more defensible because the outputs are explicitly constructed from pairwise similarities. But for prompted LLMs and VLMs in Section 5, the operational link between internal representation geometry and the Luce choice rule is much weaker. This matters because the claimed universality is partly riding on a fixed decision mechanism rather than purely on representational constraints.

3. There are some issues of mathematical clarity and notation that should be fixed. The most obvious one is in **Definition 1 on Page 4**, where the text defines the constant similarity function with resolution $\varepsilon$ but writes
\[
g_{\varepsilon;\Delta}(x,y)=\mathbbm{1}_{B_r(x)}(y)+\Delta \mathbbm{1}_{M\setminus B_r(x)}(y),
\]
using $r$ instead of $\varepsilon$. This is presumably a typo, but it is not a trivial typo because the entire paper revolves around the resolution parameter. Similarly, the paper alternates between talking about $S$ and $M$ as the stimulus space after introducing the bijection $\Phi:S\to M$, which is understandable but occasionally sloppy. For a theory paper hinging on exact derivations, these details matter.

4. Some derivational steps are plausible but not sufficiently transparent in the main paper, which weakens confidence in the claimed generality. For instance, **Theorem 3** gives compact expressions for $p_S^n$ and $p_I^n$, but the main text does not communicate the combinatorial intuition particularly well, and the expectation over $p\sim \nu$ is then set aside by focusing on the homogeneous case. That is fine as a special case, but it again narrows the actual universality. In effect, the paper proves something broad, then interprets mostly the easiest special regime where the geometry collapses to a scalar parameter. The distinction between “general theorem” and “practically interpreted homogeneous case” should be much sharper.

5. The empirical section with realistic models is suggestive, but it does not fully validate the stronger theoretical claims. The CNN result in **Figure 5a** shows a tradeoff as $\alpha$ and $\varepsilon$ vary, but a tradeoff induced by training with a weighted objective,
\[
\mathcal{L}=(1-\alpha)\mathcal{L}_{\mathrm{id}}+\alpha \mathcal{L}_{\mathrm{sim}},
\]
is not by itself evidence of a fundamental representational law. Multi-objective optimization usually produces tradeoffs. What would matter is stronger evidence that the observed frontier matches the theoretical structure in a nontrivial way, beyond the generic fact that optimizing one metric can hurt another. As presented in the main paper, that distinction remains blurry.

6. The LLM and VLM experiments in Section 5 are too indirect relative to the theoretical setup. In **Figure 5b**, the year-similarity experiments are prompt-based behavioral tests on language models. These curves do show degradation away from reference dates, but that could reflect many things, such as inconsistent instruction following, world-knowledge sparsity, tokenization quirks for numerals, or prompt-template artifacts. Likewise, the spatial VLM maps in **Figure 5c** are interesting, but they do not isolate “finite semantic resolution” from simpler confounds like visual localization difficulty or answer-format instability. The paper acknowledges on Page 10 that direct demonstration of the tradeoff in large language-vision models is still outstanding, and that caveat is important. As it stands, the large-model evidence supports “there may be finite-resolution-like behavior” more than “the same law persists.”

7. The scope of comparison to prior work is somewhat thin for such an ambitious positioning. The paper cites Frankland et al. (2021) as the conceptual seed and mentions Shepard’s law, the binding problem, and some modern interpretability papers. But the reader is still left without a very crisp statement of what is genuinely new relative to prior cognitive-science formulations of the generalization-vs-identification tension. Is the key novelty the exact closed forms for constant similarity? the multi-item extension? the link to neural-network experiments? or the universality claim? The paper would benefit from a more surgical positioning statement, because right now novelty is spread across several partial contributions, which makes it harder to judge the advance.

8. The paper repeatedly uses language like “universal laws,” “fundamental limits,” and “foundational informational constraints,” especially in the abstract and discussion, but the empirical evidence is not broad enough to support such sweeping wording. The theory is exact for a stylized decoder and stylized similarity classes. The toy model supports the mechanism; the larger-model experiments are consistent with it but far from definitive. This mismatch between evidence and rhetoric matters because it can lead readers to over-interpret what has been established.

9. The main paper lacks stronger quantitative evaluation of theory-versus-experiment fit in the realistic settings. **Figure 4b** does a decent job qualitatively, and the black curve from **Proposition 1** appears to match the toy-network circle training reasonably well. But for the CNN and large-model experiments in **Figure 5**, the paper mostly gives qualitative correspondence, not rigorous fit tests or falsifiable alternatives. If the paper wants to argue that the same law appears across architectures, this is precisely where one would want stronger quantitative backing.

10. There is also a mild internal inconsistency in the exposition of the toy model loss. The main paper says the model is trained to perform 3-item similarity tests, but the theory emphasized in the main figures and discussion is mostly the 2-item tradeoff. That is not wrong, yet it makes the comparison in **Figure 4b** slightly less clean than it initially appears. The paper could do more to explain why plotting the observed trajectory in the same $(p_S,p_I)$ plane remains the right comparison object across these task variants.

## Questions
1. The strongest theoretical claims rely on the constant similarity model in **Definition 1**. Can the authors clarify exactly which parts of the “universal Pareto front” statement are still expected to hold for broader families of monotone similarity functions beyond the constant and linear-decay cases? A precise statement here would substantially increase my confidence.

2. For the large-model studies in Section 5, can the authors better justify why the observed behavioral curves should be interpreted as consequences of internal similarity resolution, rather than prompt-level or modality-specific confounds? Even a concise argument tying the evaluation protocol more tightly to **Equations (1) and (2)** would help.

3. In **Figure 5a**, how much of the observed frontier is specific to the explicit multi-objective training loss versus an intrinsic representational constraint? If the authors have evidence that the same tradeoff appears even without directly weighting $\mathcal{L}_{\mathrm{sim}}$ and $\mathcal{L}_{\mathrm{id}}$, that would strengthen the paper.

4. Please clarify the typo/inconsistency in **Definition 1**, where $B_r(x)$ appears instead of $B_\varepsilon(x)$. More broadly, I would encourage a careful pass over notation, because theory papers live or die by these details.

5. The paper highlights the $1/n$ collapse from **Equation (8)**. Can the authors provide a stronger empirical check of this specific scaling law in a controlled learned model, rather than mainly qualitative alignment in prompted LLMs? That would make the multi-item claim much more compelling.

6. For the toy model in Section 4, why is the comparison in **Figure 4b** centered on the 2D $(p_S,p_I)$ plane when training is done on 3-item similarity tasks? A short explanation of the measurement protocol and why this is theoretically justified would improve clarity.

7. The heterogeneity term $\mathrm{Var}(b(\varepsilon))$ in **Equation (3)** is one of the more interesting insights in the paper. Do the authors have a direct quantitative measurement of this term, or a proxy for it, in the segment-vs-circle toy experiment from **Figure 4b**? A more explicit test of that prediction would be quite valuable.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
No major ethics concerns are apparent from the main paper. The experiments use standard model evaluation settings and synthetic or established benchmark-style tasks, and I did not identify issues requiring specialized ethics review based on the submitted text.

## Soundness Rating
3: good. The theoretical analysis is meaningful and mostly convincing, but several central claims are narrower than the rhetoric suggests, and the realistic-model experiments are more suggestive than conclusive.

## Presentation Rating
3: good. The paper is readable and the figures are helpful, especially Figures 2, 4, and 5, but there are notable notation issues and some overstatement that reduce precision.

## Contribution Rating
3: good. The paper makes a substantive contribution by formalizing a tradeoff with explicit formulas and connecting it to learned representations, though I am less convinced by the breadth of the universality claims.

## Overall Rating
6: Marginally above the acceptance threshold. But would not mind if paper is rejected.  
The paper has a strong conceptual core, useful theory, and a good toy-model validation, which together put it on the positive side for me. At the same time, the larger empirical claims are not yet as airtight as the title and framing imply, so this is not an easy accept.

## Reviewer Confidence
4: confident. I am confident in the assessment and checked the main mathematical claims and the alignment between the equations, figures, and stated conclusions, though I cannot fully verify every proof detail from the appendix within review time.