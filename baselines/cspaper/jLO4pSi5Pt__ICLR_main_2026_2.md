---
job_id: d10f04ce-688b-42e7-9f13-0d06f1f2d66d
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: jLO4pSi5Pt.pdf
paper: Long-Tailed Test-Time Adaptation for Vision-Language Models
main_score_norm: 0.6
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, focusing on test-time adaptation, vision-language models, and long-tailed representation learning under distribution shift.

## Minimum Quality
Pass ✅. The paper contains the expected scientific structure, including abstract, introduction, related work, methodology, experiments, quantitative results, and conclusion; despite several technical and presentation issues, it clears the minimum bar for full review rather than desk rejection.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find hidden prompts, suspicious reviewer-targeting instructions, or other manipulative content in the provided paper text and figures.

# Expected Review Outcome:
## Summary
This paper studies test-time adaptation for vision-language models under long-tailed test streams, a setting the authors call Long-tailed Test-Time Adaptation (L-TTA). The proposed method combines three pieces: Synergistic Prototypes, which maintain two prototype types to enrich tail classes; Rebalancing Shortcuts, which adapt prototypes through shared hyper-class vectors and a class re-allocation loss; and Balanced Entropy Minimization, which modifies entropy minimization using dynamically estimated class priors and confidence-dependent penalties. Experiments on long-tailed variants of OOD, cross-domain, and corruption benchmarks report improvements over several recent VLM TTA baselines in both accuracy and macro-F1.

## Strengths
1. The paper tackles a practically relevant setting that has received much less attention than balanced test-time adaptation. The central motivation, namely that online TTA can amplify head-class dominance and damage tail classes in sequential streams, is reasonable and important for realistic deployment.

2. The empirical section is fairly broad in scope. The paper evaluates on multiple benchmark families, including OOD benchmarks, cross-domain transfer, corruption robustness, and additional backbones. In particular, **Table 1**, **Table 2**, and **Table 3** show a fairly consistent pattern that the proposed method improves macro-F1 in addition to raw accuracy, which is the right metric emphasis for the claimed long-tailed setting. The gains on the corruption benchmark in **Table 3** are especially notable, where the macro-F1 margin over prior methods is larger than on the cleaner cross-domain setup.

3. I appreciated that the paper does not only report average accuracy, but also repeatedly emphasizes class balance. The inclusion of macro-F1 throughout the main tables is appropriate, and the head/tail analyses referenced in the appendix are directionally aligned with the paper’s claims.

4. The architecture-level intuition is communicated reasonably well through the figures. **Figure 1** is useful for framing the problem and intended failure modes, especially the distinction between text-induced tail erosion and modality-bias amplification. **Figure 3** also helps the reader understand the interaction between the three components, namely how augmented views feed prototype updates, how shortcuts act on prototypes, and how the final logits are formed before BEM is applied. Even though some math details remain underspecified, the high-level pipeline is easier to follow because of this figure.

5. The ablation section is reasonably substantive rather than superficial. **Table 6** shows that using only DP or only EP is worse than combining them, and that adding BEM on top of SyP+RS gives an additional bump. Likewise, **Figure 4** gives some indication that performance is not obtained from a single knife-edge hyperparameter setting. This is useful because the method introduces several new knobs.

6. The paper makes an effort to discuss efficiency instead of only reporting performance. **Table 4** suggests that L-TTA is cheaper than several gradient-heavy baselines while still improving the harmonic mean of accuracy and macro-F1. That trade-off matters for TTA, where inference-time overhead is part of the actual method cost.

## Weaknesses
1. The novelty claim is overstated relative to what is actually introduced. The paper repeatedly frames itself as the first study of long-tailed TTA for VLMs, but the method itself is largely a composition of familiar ingredients: prototype or cache accumulation, attention-based lightweight adaptation, and a prior-adjusted entropy objective. The specific combination may be new, but the paper does not do enough to separate “new setting” from “new mechanism.” This matters because the contribution is strongest if the long-tailed VLM phenomenon really forces qualitatively new design choices, rather than just another cache/prototype variant with reweighting. Right now the positioning is somewhat too grand for the level of methodological departure shown in Sections 3.2 and 4.

2. Several of the paper’s “VLM-specific” failure-mode claims are not convincingly established as specific to VLMs rather than general imbalance effects. In **Figure 1(b.1)**, the argument about “rich classes” is suggestive but not especially rigorous, since the figure mainly shows classwise variability and alignment-level trends without a clean causal test that isolates text priors from the visual stream or from ordinary class difficulty. Similarly, **Figure 1(b.2)** compares SAR on a VLM backbone versus a visual backbone, but this alone does not demonstrate that modality mismatch is the core reason for failure; there are many confounders between backbone families and adaptation dynamics. Since these failure modes motivate the whole design, the evidence should be tighter.

3. The mathematical specification is shaky in a few important places, and this reduces confidence in both reproducibility and the theoretical narrative.
   - In **Equation (4)**, the update is described as “via an EMA manner,” but the formula is not a standard EMA with a fixed momentum. Instead, it looks like a normalized running average indexed by \(N_{c,s}^{\texttt{DP}}\). That is not merely terminology, it changes the adaptation dynamics materially.
   - In **Equation (5)**, the notation is awkward and partly inconsistent. \(\bm{\phi}_c\) is written as a scalar but boldfaced, and the update counter \(N_{c,s}^{\texttt{EP}}\) is said to “increase by \(\bm{\phi}_c\) at each step,” which means the counter is fractional. That may be intended, but then the semantics of “counter” and the resulting normalization need to be defined much more carefully.
   - In **Equation (6)**, the attention operator is underspecified. The text says “RS is implemented by a cross-attention with shared hyper-class vectors,” yet the formula \(\texttt{Attn}([\bm{v}_c,\bm{t}_c], \bm{q}_j)\bm{q}_j + \bm{v}_c\) does not define query, key, and value projections, nor whether the update sums over \(j\) or uses a single selected \(j\). As written, the equation is not operationally complete.
   - In **Equation (7)**, the CRA loss resembles a load-balancing surrogate, but the construction is difficult to verify because the pseudo-label counts and average activations are multiplied without a clear normalization or justification for why minimizing that dot product yields uniform expert usage. The connection to MoE load balancing is asserted more than derived.

4. The theoretical claims around BEM are much weaker than the paper suggests. **Proposition 1** and **Proposition 2** are stated as guarantees of rebalancing behavior, but even from the main paper alone, the assumptions are too vague to support the strength of these claims. The split into \(\mathcal{C}_{\texttt{head}}\) and \(\mathcal{C}_{\texttt{tail}}\) is left abstract, and the propositions reason about expectations of logit gradients without specifying the underlying data distribution or confidence distribution. More importantly, the propositions do not establish anything like optimization convergence, improved risk, or even monotone balancing on actual streams; they only state inequalities on expected gradients under assumptions that are not checkable from the main text. So the theory currently reads more like suggestive intuition dressed up as a guarantee.

5. The definition of BEM itself in **Equation (9)** is not fully clear. The penalty term uses \((1-\hat{\mathbb{P}})^\beta\), but \(\hat{\mathbb{P}}\) is not cleanly defined in the equation. It appears to be derived from the current prediction, yet the paper does not state whether it is the classwise softmax over \(\bm{z}\), the max-confidence scalar, or a detached pseudo-label distribution. This is not a cosmetic notation issue, because the gradient of \(\mathcal{L}_{\texttt{BEM}}\) depends critically on whether that factor is treated as a differentiable function of \(\bm{z}\) or as a constant weight. Also, the class prior \(\bm{\pi}\) is “continually updated based on the current predicted pseudolabels,” which risks reinforcing early head-class bias. The paper claims BEM mitigates this, but does not explain why the self-updated prior does not simply drift toward the same dominant classes.

6. There are result presentation issues in the main tables that need to be cleaned up before I would fully trust the empirical story.
   - In **Table 2**, the ImageNet result for L-TTA is reported as **70.46 / 64.39**, whereas nearly every baseline is in the mid-80s to high-80s for accuracy on the same row block. That is a dramatic drop, yet the row still contributes to a reported best overall average. This may be a typo, a different protocol, or a formatting issue, but as printed it is hard to reconcile with the surrounding numbers and should not be left ambiguous.
   - In **Table 1**, the dataset header changes from ImageNet-R at imb=10 to **ImageNet-B** at imb=20 and 50, while the text of the benchmark earlier describes ImageNet-A, ImageNet-R, ImageNet-S, and ImageNet-V2. This looks like a labeling inconsistency. It may be minor editorially, but it raises avoidable confusion about what was actually evaluated.
   - In **Table 4**, memory for WATT is listed as “\(1.54 \times 71\),” which is unusual formatting and not directly interpretable. Since this table is meant to support efficiency claims, the reported units and notation should be unambiguous.

7. The fairness of the long-tailed benchmark construction is not fully convincing. On **Page 7**, the paper says that datasets are manipulated by random sampling into an exponentially decayed class distribution, but “if the calculated cardinality is less than the class cardinality itself, we simply keep that class unchanged.” This sentence is confusing, because a calculated target cardinality being less than the existing class size is precisely when one would expect subsampling. If this means some datasets remain only mildly imbalanced or partially modified, then the actual imbalance protocol may differ across datasets in a way that complicates comparison. Since the entire paper is built around synthetic long-tail generation, the protocol needs to be much more explicit in the main text.

8. The implementation details contain at least one likely typo with methodological implications. On **Page 7**, the paper states \(K = 0.3\), even though \(K\) was introduced as the number of hyper-class vectors in **Equation (6)** and should therefore be an integer. Later, **Figure 4(c)** also studies “vector number \(K\)” over values from 0.1 to 1, suggesting that the actual tuned quantity is probably a ratio rather than a count. This inconsistency matters because it obscures what architecture was actually instantiated.

9. Some of the claims drawn from the figures are stronger than what the figures really support. **Figure 2(a)** shows t-SNE plots comparing SCAP and L-TTA, but t-SNE is fragile and visually persuasive in ways that are not always reliable for quantitative conclusions. Saying that existing methods show “severe degradation in tail-class representations” based on this panel is a bit too strong. Likewise, **Figure 2(b)** on macro-F1 versus imbalance ratio is more convincing, but the figure includes only a small subset of baselines. If this figure is used as core evidence of robustness, then either more methods should be shown or the claim should be narrowed.

10. The writing is understandable overall, but the exposition is rough in many local places. There are repeated grammatical errors, inconsistent naming, and notation drift. Examples include “how summarizes how” on **Page 5**, switching between ImageNet-V and ImageNet-V2 or ImageNet-R/ImageNet-B in tables, “attenticon” in **Equation (7)**, and class/vector variable naming that changes meaning across sections. None of these individually kill the paper, but together they make the method harder to audit than it should be for a conference paper proposing multiple intertwined components.

## Questions
1. Please clarify the exact operational form of **Equation (6)**. Is the prototype update
\[
\bm{v}_c \leftarrow \sum_{j=1}^{K} \alpha_{c,j}\bm{q}_j + \bm{v}_c
\]
with \(\alpha_{c,j} = \texttt{Attn}([\bm{v}_c,\bm{t}_c], \bm{q}_j)\), or is there only a top-1 expert used? The current notation reads as if a single \(j\) is used, but the loss in **Equation (7)** suggests all experts participate.

2. In **Equation (9)**, what exactly is \(\hat{\mathbb{P}}\)? Is it the current softmax distribution \(\sigma(\bm{z})\), a detached copy of it, or only the max-confidence entry? This is important because the gradient path through the confidence-dependent prior penalty materially changes the objective.

3. Please explain the apparent anomaly in **Table 2** for ImageNet, where L-TTA’s accuracy is shown as 70.46 while all strong baselines are in the 84 to 89 range. Is this a typo, a different setting, or a protocol difference? This should be fixed explicitly in the rebuttal or final version.

4. Please clarify the imbalance generation protocol on **Page 7**. The sentence about keeping a class unchanged “if the calculated cardinality is less than the class cardinality itself” seems backwards. A precise formula for target class counts, and whether subsampling is always applied, would increase confidence in the benchmark construction.

5. Can the authors provide a cleaner justification for why the dynamically updated pseudo-label prior in BEM does not amplify early mistakes? For example, do you observe prior collapse toward head classes early in the stream, and if not, why not?

6. The paper argues that the failure modes are VLM-specific. What direct evidence, beyond the suggestive comparisons in **Figure 1**, can you provide that these phenomena are not simply generic long-tailed TTA issues? A stronger controlled comparison or additional ablation would increase confidence in the problem formulation.

7. Since **Table 4** is used to make an efficiency argument, please standardize what is counted in runtime and memory for all methods. Are view generation, prompt ensemble costs, and cache/prototype storage included uniformly across baselines?

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
No major ethics concerns are evident from the paper itself. The work is a methodological study on test-time adaptation for image classification benchmarks and does not introduce obvious privacy, safety, or human-subject issues beyond standard model deployment considerations.

## Soundness Rating
2: fair. The empirical evidence is fairly extensive and generally supportive, but several mathematical definitions and result-table inconsistencies reduce confidence in the technical precision of the paper.

## Presentation Rating
2: fair. The high-level idea is understandable and the figures help, but notation issues, table inconsistencies, and multiple writing problems noticeably hurt clarity.

## Contribution Rating
3: good. The problem setting is relevant and the empirical scope is useful to the community, even if the methodological novelty and theoretical support are less convincing than the paper claims.

## Overall Rating
6: Marginally above the acceptance threshold. But would not mind if paper is rejected. The paper addresses an important and underexplored setting and backs it with broad experiments, but there are enough issues in positioning, mathematical specification, and result presentation that this is not an easy accept.

## Reviewer Confidence
4: confident. I am confident in the overall assessment and checked the main method, equations, figures, and result tables carefully, though some ambiguities in the paper prevent complete verification of all technical details.