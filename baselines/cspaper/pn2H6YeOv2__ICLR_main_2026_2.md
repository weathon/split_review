---
job_id: 0b89c869-1bff-4885-8a53-eb2d29964e1f
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: pn2H6YeOv2.pdf
paper: PI-CCA: Prompt-Invariant CCA Certificates for Replay-Free Continual Multimodal Learning
main_score_norm: 0.6
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, focusing on replay-free continual learning for vision-language models, representation geometry, and multimodal transfer/robustness.

## Minimum Quality
Pass ✅. The submission contains the required scientific components, including Abstract, Introduction, Related Work, Method, Experiments, quantitative results, and Conclusion, and it provides sufficient technical and empirical substance to merit full review rather than desk rejection.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find hidden instructions, prompt-injection attempts, or suspicious reviewer-targeted manipulations in the provided paper text.

# Expected Review Outcome:
## Summary
This paper proposes PI-CCA, a replay-free continual multimodal learning method that attempts to preserve cross-modal alignment by storing a compact certificate consisting of top-$k$ canonical correlations and sketched canonical subspaces derived from whitened image-text cross-covariance. During continual adaptation, the model regularizes current minibatch alignment toward this certificate via spectral, subspace, and prompt-invariance losses, while updating the certificate with EMA-based streaming statistics.

The method is evaluated on four continual vision-language benchmarks, MTIL, X-TAIL, VLCL, and ConStruct-VL, where the paper reports better performance than prior replay-free baselines. The paper also includes ablations on the different loss terms, sketching choices, prompt perturbations, and certificate capacity, plus a theoretical section relating geometry drift to excess risk and dynamic regret.

## Strengths
1. The paper has a clear high-level idea. Instead of preserving logits, similarity matrices, or parameters, it tries to preserve the geometry of cross-modal alignment itself through canonical correlations and subspaces. That is a meaningful conceptual reframing for replay-free VL continual learning, and it is stated cleanly in Sections 1 and 3.

2. The method is reasonably modular and implementation-friendly. The training objective in **Equation (7)** combines the task loss with spectral preservation, subspace preservation, and prompt-invariance terms in a way that is easy to understand and, at least at a high level, easy to integrate into LoRA-based continual adaptation. I also appreciate that the paper explicitly discusses practical choices for whitening, block power iteration, EMA updates, and stop-gradient design in Section 3.4.

3. The empirical coverage is broad for a main-track submission. The authors do not rely on a single benchmark, but report results across classification-style continual learning, retrieval, and structured multimodal concept learning. This breadth matters because a geometry-based method could easily overfit one protocol.

4. The headline empirical results are competitive. In **Table 1**, PI-CCA is consistently the best reported replay-free method on MTIL and X-TAIL across Avg, Last, and Transfer, with gains that are not huge but are steady across all three metrics. For example, on MTIL Avg it improves over C-CLIP from 75.2 to 76.8, and on X-TAIL Transfer it improves over the strongest reported baseline from 64.2 or 63.8 up to 64.7. These are not dramatic leaps, but they are consistent, which is often more convincing than a single cherry-picked win.

5. **Table 2** is also a positive point for the paper. PI-CCA is best on both VLCL I2T/T2I R@1 and on ConStruct-VL FA/AF among replay-free methods, while even exceeding one synthetic-replay baseline in VLCL. This strengthens the claim that the method is not tied only to classification.

6. The ablation in **Table 3** is informative rather than decorative. Removing either the spectral term or the subspace term causes the largest drops, which supports the paper’s central claim that both the spectrum and subspace directions matter. I also found the “Hungarian pairing vs. sorted surrogate” row useful, because it shows the simpler approximation is sufficient in their regime.

7. The figures are, for the most part, well aligned with the main story. **Figure 1** does a good job explaining the architecture and data flow, especially the interaction between prompt perturbations, the sketched projectors, and the certificate. **Figure 2** is also helpful because it shows the method is not only about accuracy, but about a cost-accuracy-memory tradeoff; the “knee” near $(k,h)=(64,256)$ gives a concrete rationale for the default configuration instead of making it look arbitrary.

8. The prompt robustness analysis in **Figure 4** is useful and directly relevant to the paper’s title and motivation. The curves show that adding $\mathcal{L}_{\mathrm{pi}}$ reduces degradation under both ID and OOD prompt perturbations, which is better than merely reporting one averaged robustness number.

9. The theoretical section is not empty decoration. The bound in **Theorem 1** at least formalizes the paper’s intuition that excess risk can be controlled by spectral drift, subspace drift, and tail energy, and that gives some conceptual support to the objective design.

## Weaknesses
1. The main methodological premise is plausible, but the paper still overstates how directly the optimization target matches the claimed invariant. The paper repeatedly says it preserves “alignment invariants,” yet the actual training loss operates on minibatch estimates of whitened cross-covariance, plus sketched surrogates of projectors, plus EMA-refreshed certificates. This is already several approximation layers away from the true population alignment geometry. The authors do acknowledge some of this in Section 3.3 when they say that $\widehat{Q}_\bullet$ are “not exact projectors” and that the Frobenius distance is a surrogate under near-isometric sketches, but the writing elsewhere is much stronger than the math really justifies. This matters scientifically because the paper’s conceptual selling point is exactly that it preserves the true object rather than a proxy, while in practice it still relies on multiple proxies and approximations.

2. There is a notable mismatch, and in one place an apparent inconsistency, between the main-text method and the algorithmic details. In the main text, the sketched Gram projectors are defined as $\widehat{Q}_v=\widehat{S}_v\widehat{S}_v^\top$ and $\widehat{Q}_t=\widehat{S}_t\widehat{S}_t^\top$ in Section 3.3, which is dimensionally consistent with **Equation (10)**. But in **Algorithm 1, line 8** in the appendix, $\widehat{Q}_v$ is written as $\widehat{S}_v\widehat{S}_t^\top$, which would be a cross-modal quantity rather than a projector and is inconsistent with the method description. Since the paper asks the reader to trust fairly intricate geometry computations, this kind of inconsistency is not a cosmetic typo. It directly affects confidence in whether the implemented loss matches the stated one.

3. The certificate update in **Equation (13)** raises a conceptual concern that the paper does not fully resolve. The stored certificate is refreshed every step using the current task statistics:
\[
\boldsymbol{\rho}^\star \leftarrow (1-\alpha)\boldsymbol{\rho}^\star + \alpha \widetilde{\boldsymbol{\rho}}, \quad
\boldsymbol{S}_v^\star \leftarrow \operatorname{orth}((1-\alpha)\boldsymbol{S}_v^\star + \alpha \widetilde{\boldsymbol{S}}_v),
\]
and similarly for text. This makes the “reference” itself drift toward the current task. That may be good for plasticity, but it also weakens the interpretation of the certificate as preserving the original alignment skeleton. The paper presents this as controlled plasticity, but does not really analyze the stability-plasticity tradeoff induced by this moving target, beyond a shallow ablation with $\alpha=0$ in **Table 3**. In continual learning, whether the anchor is fixed or drifting is a central issue, not a small implementation detail.

4. The theoretical claims are directionally useful but substantially weaker than the paper’s rhetoric suggests. **Theorem 1** bounds the risk difference by $\|M-M^\star\|_2$, then decomposes the rank-$k$ part into spectral and subspace terms. This is fine as a Lipschitz perturbation argument, but it does not demonstrate that preserving the top-$k$ canonical spectrum and subspaces is sufficient for robust zero-shot retention in realistic continual settings. The result depends on strong assumptions, especially bounded whitened embeddings in (A1) and a Lipschitz loss in the scalar score in (A2), and the comparator $M^\star$ is simply assumed. Moreover, the “dynamic regret” bound in **Theorem 2** is essentially a per-step summation of the single-step bound, not a new online-learning guarantee derived from the update rule. So the theory is better described as intuition-consistent perturbation analysis than as a substantive guarantee for the proposed training dynamics. The paper should tone down the claims accordingly.

5. The empirical comparison is broad, but the fairness and completeness of the baseline story are still not fully convincing from the main paper alone. The paper compares to many recent VL-CL methods, which is good, but it does not include simple strong controls in the main tables such as plain LoRA finetuning, LoRA plus generic regularizers, or other minimal baselines. Those controls appear only later in the appendix. That omission matters because the gains in **Tables 1 and 2** over the strongest replay-free baselines are modest, typically around 1 to 2 points, and without seeing the simplest baselines in the main text it is harder to judge how much of the gain comes from the CCA certificate specifically rather than from a careful LoRA recipe and tuning budget.

6. Some experimental claims are stronger than what is actually shown in the main paper. For instance, the text around **Figure 3** argues that preserving CCA geometry “predicts retention rather than being a coincidental regularizer.” But the evidence shown is correlational scatter across hyperparameter sweeps. A strong correlation between geometry drift and performance drop is interesting, yet it does not establish that geometry preservation is the causal driver rather than a correlated byproduct of better optimization or lower update magnitude. This is exactly the kind of place where the paper could use a sharper intervention study, rather than leaning on regression lines and confidence intervals.

7. The handling of prompt invariance is sensible, but still under-specified in a way that affects reproducibility and interpretation. The main text defines perturbations as synonym/template variation with $\delta \sim \mathcal P$, and **Equation (11)** averages text-side projectors across $M$ perturbations. However, the distribution $\mathcal P$ is not specified precisely enough in the main body, and the perturbation strength parameter used in **Figure 4** is only operationally explained later. Since the paper’s title explicitly foregrounds prompt invariance, this part should be much more concrete in the main text, including whether perturbations are sampled uniformly across template families, how synonym substitutions are filtered for semantic preservation, and whether there is any task-specific tuning of the perturbation set.

8. There are presentation and notation issues that undermine confidence more than they should. Examples include repeated confusion between “PI-CCA” and “P1-CCA” in several places, inconsistent capitalization, and some sloppy appendix content. Most concerning, **Page 11 / Figure 1 in the appendix area** appears to contain a clearly erroneous caption, “Comparison of the performance of the proposed approach with the proposed approach,” which looks like broken or accidental content. The appendix also includes a toy Python script in Appendix A.5 that is not just simplified, but mathematically inconsistent with the actual method, for example using direct matrix inverse rather than inverse square root whitening and omitting the shrinkage/orthogonal sketch machinery. I am not judging based on the appendix alone, but these issues collectively make the paper feel less carefully checked than it should be for a method whose credibility depends on precise linear algebra.

## Questions
1. The main mathematical clarification I would most like in the rebuttal concerns the subspace loss. In **Equation (10)**, the method relies on
\[
\mathcal{L}_{\text{sub}}=\tfrac12\|\widehat{Q}_v-Q_v^\star\|_F^2+\tfrac12\|\widehat{Q}_t-\bar{Q}_t^\star\|_F^2,
\]
while explicitly noting that these are only sketched surrogates, not true projectors in the original space. Can the authors give a more precise statement of what sketch assumptions are actually needed so that this surrogate is faithful enough for optimization, and whether those assumptions are expected to hold at the chosen $(k,h)$ values? Even an empirical sanity check comparing sketched and full projector distances on a tractable subset would increase confidence.

2. Please clarify the inconsistency between the main-text projector definition and **Algorithm 1, line 8**, where $\widehat{Q}_v$ appears to be written as $\widehat{S}_v\widehat{S}_t^\top$. Is this a typo in the algorithm, a typo in the text, or are two different quantities being used? This is important because it changes the meaning of the loss substantially.

3. How sensitive is the method to smaller batch sizes, stronger class imbalance, or noisier streams? Since the approach depends on minibatch covariance estimation and whitening in **Equations (1) and (2)**, it would help to know whether the reported results are stable outside the fairly large effective batch size described in the appendix. A compact main-text experiment or discussion here would strengthen the practical relevance considerably.

4. On the certificate refresh in **Equation (13)**, can the authors explain more clearly what is being preserved over long horizons, especially after many tasks? If the certificate is repeatedly updated toward recent tasks, what prevents slow erosion of the original zero-shot geometry that the paper claims to protect? A longer-horizon drift plot against the initial certificate would be useful.

5. The theory would be more convincing if the authors explicitly tempered the claim scope. Are they willing to revise the wording so that **Theorems 1 and 2** are framed as perturbation-style support for the objective, rather than as guarantees that the method preserves zero-shot behavior under domain and prompt shift? That would make the theoretical contribution more accurate and easier to evaluate.

6. For the prompt invariance module, please specify more concretely the perturbation distribution $\mathcal P$ used in the main experiments, especially for **Figure 4**. What exact transformations are applied at each perturbation strength $s$, and how do the authors ensure that perturbations preserve label semantics rather than introducing task difficulty shifts unrelated to prompt robustness?

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
The paper uses standard public benchmarks and proposes a replay-free method partly motivated by privacy and storage constraints. Based on the paper content, I do not see a specific ethics issue that requires separate ethics review.

## Soundness Rating
3: good. The method is technically plausible and supported by reasonably broad experiments, but there are enough issues around approximation fidelity, theoretical overreach, and methodological clarity that I cannot rate the technical support as excellent.

## Presentation Rating
3: good. The paper is generally readable and well organized, and several figures and tables are useful, but there are nontrivial notation inconsistencies, some sloppy appendix content, and a few places where the rhetoric is cleaner than the actual technical support.

## Contribution Rating
3: good. The geometry-first CCA certificate perspective is a meaningful contribution for replay-free VL continual learning, and the empirical results make it worth sharing with the community, even though the gains are moderate and the justification is not fully airtight.

## Overall Rating
6: Marginally above the acceptance threshold. But would not mind if paper is rejected. The paper has a credible and interesting core idea, broad empirical coverage, and solid replay-free results, but it also has real weaknesses in theoretical positioning, precision of the method description, and the strength of some claims. I lean positive because the contribution is useful and sufficiently distinct, though it is not a comfortable accept.

## Reviewer Confidence
4: confident. I am confident in my assessment overall, though it is still possible that some implementation details are cleaner than the paper currently conveys.