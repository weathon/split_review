---
job_id: f05654e0-133a-4ef5-a32b-6824dbaaf2de
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: Rj5ZJk956j.pdf
paper: Weakening Neurons: A Newly Discovered Read-Write Functionality in Transformers with Outsize Influence
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, specifically interpretability of learned representations in transformer language models and neuron-level analysis of gated MLPs.

## Minimum Quality
Pass ✅. The submission contains the expected scientific components, including Abstract, Introduction, Related Work, Method, experiments/ablations, results, case studies, and Conclusion; while I have substantial concerns about novelty, validation, and interpretation, these are review-stage quality issues rather than desk-reject defects.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find hidden prompts, suspicious instructions to automated reviewers, or other obvious manipulation attempts in the provided paper content.

# Expected Review Outcome:
## Summary
This paper studies gated MLP neurons in transformer LLMs through a simple read-write perspective based on cosine similarities among $\mathbf{w}_{\text{gate}}$, $\mathbf{w}_{\text{in}}$, and $\mathbf{w}_{\text{out}}$. Using this lens, the authors define a taxonomy of neuron types, emphasize a class they call weakening neurons, report cross-model layerwise patterns in several open LLMs, and perform ablations in OLMo-7B to argue that weakening neurons are disproportionately influential.

The paper further introduces conditional ablations based on the signs of $x_{\text{gate}}$ and $x_{\text{in}}$, and uses these to claim that some important effects of weakening neurons arise specifically when $x_{\text{gate}}<0$, which the authors interpret as evidence that negative gate values have mechanistic importance beyond training dynamics.

## Strengths
1. The paper asks an interesting mechanistic-interpretability question that is specific to modern gated MLPs, rather than reusing analyses developed for ReLU/GELU-style neurons. That focus is timely, since many current LLMs use SwiGLU or GEGLU.

2. The read-write framing is intuitive and easy to follow. Equations (1) and (2) on Pages 3-4 give a clean decomposition of how a gated neuron reads from the residual stream and writes back to it. Even though the method is simple, it is a reasonable starting point for analyzing gated neurons.

3. The cross-model descriptive analysis is broad. The authors inspect many model families and scales, and Figure 1(a) on Page 5, together with the larger multi-model view in Figure 40, does show a recurring shift in median $\cos(\mathbf{w}_{\text{in}},\mathbf{w}_{\text{out}})$ from positive in earlier/middle layers toward negative in later layers. Whether this deserves the paper’s stronger claims is debatable, but the descriptive pattern itself is potentially useful.

4. Figure 2 is one of the more convincing parts of the paper. The layerwise scatter plots for Llama-3.2-3B make it visually apparent that neurons are not distributed like a purely random cloud around zero, and the movement of clusters across layers supports the claim that the proposed cosine geometry captures some nontrivial structure. This figure does useful explanatory work, especially compared with the random-initialization baseline in Figure 6.

5. The ablation section is ambitious and goes beyond a purely descriptive weight analysis. The attempt to isolate sign-conditioned subsets of activations is interesting, and the bottom panels of Figure 3(b) provide a concrete hypothesis about which activation regimes matter most.

6. The paper is rich in qualitative analysis. The case-study tables, especially Table 2 and Table 3, help connect the abstract taxonomy to actual neurons and token behaviors. Even if some interpretations are speculative, the effort to triangulate weight geometry, vocabulary projections, and activation examples is appreciated.

7. The work is reasonably reproducible in spirit. The authors state model choices, dataset source, ablation settings, and computational cost. For an interpretability paper, this level of operational detail is helpful.

## Weaknesses
1. **The central methodological leap, from pairwise weight cosines to mechanistic functionality, is much less justified than the paper suggests.**  
   The paper’s taxonomy in Section 4.2, summarized in **Table 1** on Page 4, assigns semantic/functional labels such as “strengthening”, “weakening”, “conditional strengthening”, and “proportional change” based mainly on signs and coarse thresholds of cosine similarities. But the actual neuron contribution in **Equation (2)** is
   $$
   \text{Swish}(\langle \mathbf{w}_{\text{gate}}, \mathbf{x}_{\text{norm}}\rangle)\cdot \langle \mathbf{w}_{\text{in}}, \mathbf{x}_{\text{norm}}\rangle \cdot \mathbf{w}_{\text{out}},
   $$
   so behavior depends jointly on the distribution of residual states, sign patterns, feature magnitudes, LayerNorm geometry, and interaction between the two read vectors, not just on whether $\cos(\mathbf{w}_{\text{in}},\mathbf{w}_{\text{out}})$ is above or below $\pm 0.5$. A neuron can have negative $\cos(\mathbf{w}_{\text{in}},\mathbf{w}_{\text{out}})$ and still usually reinforce a downstream feature on the actual data distribution, depending on the sign structure of $\langle \mathbf{w}_{\text{in}}, \mathbf{x}\rangle$ and $\text{Swish}(\langle \mathbf{w}_{\text{gate}}, \mathbf{x}\rangle)$.  
   Why this matters: much of the paper’s narrative treats these cosine classes as if they were mechanistic types, not just rough geometric descriptors. Without validating that these classes correspond to stable intervention-level behaviors across datasets and contexts, the labels risk being reified beyond what the evidence supports.

2. **The threshold-based taxonomy is arbitrary and insufficiently stress-tested.**  
   On Page 4, the paper chooses $\tau=\pm 0.5$ to classify neurons by “closest prototypical case,” but there is no principled derivation, no sensitivity analysis in the main paper, and no evidence that the main conclusions are stable under threshold variation. This is especially important because many neurons seem to populate continuous clouds rather than tight clusters, as visible in **Figure 2**. A neuron just above 0.5 and one at 0.9 are treated similarly, while one at 0.49 falls into a different category.  
   Why this matters: the headline claims about class prevalence by layer, especially the distributions shown in **Figure 1(b)**, depend directly on this discretization. If small threshold changes significantly alter counts of weakening vs conditional weakening vs orthogonal output neurons, then the descriptive “universal patterns” become much less robust.

3. **The paper overstates the strength of the cross-model evidence.**  
   The paper repeatedly uses language like “universal patterns” and “across models” in Section 5, but the presented evidence is mostly descriptive and partly selective. **Figure 1(a)** shows medians of only $\cos(\mathbf{w}_{\text{in}},\mathbf{w}_{\text{out}})$, not the full taxonomy; **Figure 1(b)** focuses on a single model; **Figure 2** shows only three layers of a single model in the main paper. The broader model coverage appears largely in the appendix. Moreover, the paper initially says “nine different LLMs” in the Abstract, then “12 LLMs” in Section 5 on Page 6, which creates confusion about the actual basis for the universality claim.  
   Why this matters: if the strongest cross-model evidence is not in the main paper, then the central generalization claim is not supported to the level implied by the writing. The current main-paper presentation is closer to “suggestive descriptive regularity” than to a firmly established universal pattern.

4. **The ablation methodology does not isolate what is claimed, and the controls are not strong enough.**  
   In Section 6, the main intervention compares ablating all weakening neurons against ablating the same number of random neurons from the same layers. That is a useful baseline, but it is not sufficient. A more meaningful control would be matched neurons with similar activation frequency, output norm, gate statistics, or absolute cosine magnitude, but different sign structure. Right now, the observed effect could be driven by weakening neurons being unusual in several confounded ways, not specifically by “weakening” functionality.  
   This concern is visible in **Figure 3(a)** and **Figure 3(b)**. The weakening-vs-random gap is large, but the random baseline is too weak to establish causal specificity of the taxonomy. The paper also excludes strengthening neurons from most comparisons because there are too few of them in OLMo-7B (Appendix F.2), which further reduces the fairness of class-level comparisons.  
   Why this matters: the paper’s main claim is not just that some selected neurons matter, but that the proposed RW category of weakening neurons has outsize influence. That claim needs controls matched on alternative explanations.

5. **The choice of metrics does not align tightly enough with the paper’s claims, and some interpretations are shaky.**  
   The two highlighted metrics are attribute rate and entropy. Attribute rate is borrowed from prior work on factual recall, but the connection between that metric and the authors’ RW taxonomy is indirect even by their own admission in Appendix F.1. Entropy is easier to compute, but a change in output entropy is a very blunt instrument. In **Figure 3(b)**, the authors interpret entropy reduction as output sharpening and then discuss it in semantic terms, yet entropy can shift due to many non-semantic logit-scale effects, including a few large-magnitude token changes unrelated to meaningful “strengthening” or “weakening” of concepts.  
   Why this matters: the empirical claims end up being broader than the evidence. A class of neurons having a large effect on entropy or attribute rate does not by itself show that the geometric interpretation is mechanistically correct.

6. **The claim about negative gate values being mechanistically important is interesting but not fully nailed down.**  
   Section 6.2 argues that case (iii), $x_{\text{gate}}<0$ and $x_{\text{in}}<0$, is responsible for a large part of the entropy effect. This is based mainly on conditional zero-ablation patterns in **Figure 3(b)**. But zero-ablation is a highly nonlocal intervention, and conditional zero-ablation of a rare subset of activations can create distribution shifts that are hard to interpret. The appendix itself shows that mean ablation changes the picture materially, with additional effects appearing for “gate+_post-” in **Figure 36** (Appendix F.4.2), which makes the clean main-text story less stable than advertised.  
   Why this matters: the paper presents “for the first time, we observe a mechanism involving negative gate values” as one of its central takeaways. The evidence is intriguing, but still short of a robust mechanistic demonstration. At minimum, the claim should be softened to “suggestive evidence.”

7. **The math and notation contain several issues that undermine precision.**  
   - On Page 3, in the explanation below **Equation (2)**, the paper states that $\mathbf{w}_{\text{gate}},\mathbf{w}_{\text{in}}$ are rows of $\mathbf{W}_{\text{gate}}, \mathbf{W}_{\text{out}}$, but this appears to be a typo, since $\mathbf{w}_{\text{in}}$ should be a row of $\mathbf{W}_{\text{in}}$, not $\mathbf{W}_{\text{out}}$. This is minor on its own, but unfortunate in a paper built around careful weight semantics.
   - The sign-preprocessing in Section 3.2 is not innocuous for interpretation, even if it preserves function. Flipping both $\mathbf{w}_{\text{in}}$ and $\mathbf{w}_{\text{out}}$ by $\operatorname{sign}(\cos(\mathbf{w}_{\text{gate}},\mathbf{w}_{\text{in}}))$ changes the geometric statistics being studied. The paper argues in Appendix C that this improves interpretability, but the main text does not sufficiently discuss how much the observed distributions or class assignments depend on this convention. **Figure 5** in the appendix suggests that the preprocessing materially reshapes clusters.  
   - Section 4.2 speaks about “closest prototypical case,” but no explicit distance metric over the triplet of cosines is defined. If the classification is threshold-based rather than nearest-prototype, that should be stated more formally and consistently.  
   Why this matters: in a paper where the contribution is essentially a geometry-based methodology, notation and formal definitions need to be tighter than this.

8. **The paper is weakly positioned relative to closely related prior work and does not convincingly delineate novelty.**  
   The authors acknowledge on Page 2 that Gurnee et al. (2024) already compute cosine similarities between input and output weights for GPT-2. The present paper extends that direction to gated activations and adds a taxonomy plus ablations, which is a fair contribution, but the framing often reads as if the core idea itself were new. More importantly, the paper cites a very closely related line of work but does not clearly articulate what is genuinely methodologically new beyond adapting the cosine-view to a gated setting and assigning labels to regions of cosine space.  
   Why this matters: originality at ICLR is not only about whether a paper studies a new model family, but whether it materially advances analysis tools or understanding. Here the advance feels incremental, and the paper would benefit from a much sharper “what is new beyond prior input-output cosine analyses?” discussion.

9. **Several conclusions rely on selective qualitative interpretation.**  
   The case studies in Section 8 and Tables 2-4 are sometimes interesting, but the paper itself repeatedly notes that weakening neurons are harder to interpret and that some strongest activations show no clear semantic pattern. The leap from those mixed qualitative findings to broad conceptual claims about weakening neurons having “surprising behavior” is a bit too eager.  
   Why this matters: qualitative examples are best used as illustrative support, not as proof of the semantic correctness of a taxonomy. The paper occasionally blurs that line.

10. **Presentation is readable but uneven, and some claims are too emphatic for the evidence.**  
   Phrases like “completely unexpected,” “for the first time,” and “universal” appear throughout the paper, but the empirical support is often descriptive and single-model in the intervention section. The paper is at its best when it is concrete and analytical, for example around **Figure 2** and the formulation of **Equation (2)**, and weaker when it extrapolates from those observations to strong field-level claims.  
   Why this matters: overclaiming makes it harder to assess the true scientific contribution. A tighter, more calibrated presentation would improve confidence substantially.

## Questions
1. **Threshold sensitivity:** How stable are the layerwise distributions in **Figure 1(b)** and the prevalence trends in Section 5 if the classification threshold is varied, for example from $\tau=0.5$ to $\tau\in\{0.3,0.4,0.6,0.7\}$? A rebuttal with even one compact sensitivity plot would materially increase my confidence that the reported class structure is not an artifact of discretization.

2. **Matched controls for ablation:** Can the authors compare weakening neurons to non-weakening neurons matched for layer, activation frequency, activation magnitude, output norm $\|\mathbf{w}_{\text{out}}\|$, and perhaps $|\cos(\mathbf{w}_{\text{in}},\mathbf{w}_{\text{out}})|$? This would directly test whether the effect is really tied to “weakening” rather than to other correlated properties.

3. **Functional validation of the taxonomy:** Beyond entropy and attribute rate, can the authors provide intervention-based validation that neurons classified as weakening actually tend to reduce logit evidence along their own decoded output direction, and strengthening neurons do the opposite, on naturally occurring activations? Some token-level directional validation would be much more direct than global entropy changes.

4. **Dependence on preprocessing:** How much do the main quantitative results change without the sign preprocessing from Section 3.2? In particular, do the counts in **Figure 1(b)** and the ablation-selected weakening set remain similar? Since this preprocessing changes the geometry being analyzed, the main claims should ideally be shown to be robust to it.

5. **Negative gate claim:** Can the authors provide a cleaner causal test for the “negative gate values matter” conclusion, for example by comparing sign-conditioned effects with a matched-activation-magnitude control or by reporting the frequency and total contribution mass of each condition? Right now **Figure 3(b)** is suggestive, but not conclusive.

6. **Clarification of model counts and universality claim:** The Abstract mentions nine models, while Section 5 mentions 12. Which set underlies each major claim? Please make the evidence trail more explicit.

7. **Formalization of class assignment:** In Section 4.2, is the assignment actually nearest-prototype, threshold-based, or some hybrid? A precise mathematical definition would help.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
No major ethics concerns are apparent from the main paper. The work is a mechanistic interpretability study on existing language models and does not introduce a new deployment-facing system or human-subject experiment in the main submission.

## Soundness Rating
2: fair. The paper contains a plausible descriptive method and some interesting empirical observations, but the central mechanistic claims are only partially supported, and the ablation evidence does not cleanly isolate the advocated interpretation.

## Presentation Rating
3: good. The paper is readable and well organized overall, with helpful figures such as **Figure 2** and useful tables for case studies, but there are notation issues, some ambiguity in definitions, and repeated overstatement relative to the actual evidence.

## Contribution Rating
2: fair. The focus on gated-neuron read-write geometry is relevant and potentially useful, but the methodological advance over prior cosine-based neuron analysis feels modest, and the strongest claims are not supported strongly enough to make this a clear ICLR-level contribution in its current form.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted. The paper is interesting and has some genuinely thought-provoking observations, especially the descriptive geometry in **Figure 2** and the attempt to probe negative gate regimes, but the current version over-interprets a coarse cosine-based taxonomy and does not provide sufficiently targeted validation or controls for its main mechanistic claims.

## Reviewer Confidence
4: confident. I am familiar with the interpretability literature around transformer neurons and weight-space analyses, and I checked the main methodological and empirical claims carefully, though some of the broader appendix material was necessarily assessed at a lighter level than the core main-paper claims.