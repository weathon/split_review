---
job_id: 2ec4284c-dc05-47e1-8826-4477b358657e
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: xFo13SaHQm.pdf
paper: WithAnyone: Mitigating Copy-Paste Artifacts in Identity-Consistent Generation via Contrastive Training on MultiID-2M
main_score_norm: 0.6
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is squarely within ICLR scope, covering generative models, representation learning for vision, and a new dataset/benchmark for identity-consistent image generation.

## Minimum Quality
Pass ✅. The submission includes all core components expected of a research paper, namely Abstract, Introduction, Related Work, Method, Experiments, quantitative and qualitative results, and Conclusion, and it provides enough technical and empirical content to clear the minimum bar for full review.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find hidden prompts, reviewer-targeted instructions, or other manipulative content in the provided paper text.

# Expected Review Outcome:
## Summary
This paper studies identity-consistent image generation with a focus on what the authors call the copy-paste artifact, where models overfit to the reference image and fail to preserve identity under natural variations such as pose, expression, and lighting. The paper contributes a new paired multi-identity dataset, MultiID-2M, a benchmark and metric suite called MultiID-Bench for evaluating identity fidelity versus copy-paste behavior, and a diffusion-based model, WithAnyone, trained with paired supervision, a GT-aligned identity loss, and an identity contrastive loss with extended negatives.

## Strengths
The paper tackles a real and under-discussed failure mode in identity-conditioned generation. The central framing, that maximizing similarity to the reference can perversely reward literal copying rather than robust identity preservation, is well motivated in the introduction and concretely illustrated in **Figure 2** on Page 2. That figure is actually useful rather than decorative: it shows that realistic intra-person variation can produce noticeably lower face similarity than naive readers may expect, which directly supports the paper’s argument that high reference similarity is not always desirable.

A major strength is the dataset and benchmark contribution. The field has indeed suffered from a lack of open, paired, multi-identity data, and the paper articulates this gap clearly in Sections 1 and 3. Even if one views the modeling contribution as somewhat incremental, a standardized benchmark for multi-ID generation with paired references is valuable for the community. **Table 4** in the supplementary material also makes the positioning reasonably concrete by comparing image count, number of paired samples, and references per identity against prior identity-centric datasets.

The benchmark design is one of the stronger parts of the paper. The distinction between $\mathrm{Sim}_{\mathrm{GT}}$ and $\mathrm{Sim}_{\mathrm{Ref}}$ in **Equation (1)** is conceptually sensible, and the copy-paste metric in **Equation (2)** is a meaningful attempt to normalize whether the generated image is closer to the reference or the ground-truth realization. I appreciated that the paper does not simply introduce a new score in the abstract, but also uses it to expose a trade-off across many baselines in **Figure 5**. That figure is one of the paper’s most persuasive pieces of evidence: most competing methods lie on a similarity versus copy-paste curve, while the proposed method is positioned off that curve in a more favorable region.

The empirical coverage is fairly broad. The paper compares against a substantial set of recent general customization and identity-specific baselines in **Tables 1 and 2**, covering both single-person and multi-person settings. On the single-person subset in **Table 1a**, the proposed method achieves near-best or best numbers on several identity-oriented metrics, while keeping copy-paste materially lower than methods such as UMO, PuLID, and InstantID. On the multi-person subsets in **Table 2**, the method is also competitive and often best on $\mathrm{Sim}(\mathrm{GT})$, which is aligned with the paper’s intended evaluation target.

The ablation study in **Table 3** is not exhaustive, but it does provide evidence that the paired-data phase matters. In particular, removing Phase 3 increases copy-paste from 0.161 to 0.239 while keeping $\mathrm{Sim}(\mathrm{GT})$ at roughly the same level, which directly supports the paper’s main thesis that paired training is important for escaping reconstruction-induced copying. That is one of the cleaner and more convincing findings in the paper.

The architecture and training design are reasonably clear visually. **Figure 3** gives a readable overview of both the data pipeline and the four training phases, and **Figure 4** helps explain the separation between identity-discriminative face features and optional semantically entangled image features. For a paper that combines dataset construction, model design, and a multi-phase recipe, these figures do a good job reducing cognitive load.

The qualitative comparisons in **Figure 6** are also helpful. They support the claim that some baselines either over-copy reference appearance or fail to maintain identity under changed pose/expression prompts, while the proposed model often lands in a better compromise. Qualitative figures are easy to over-claim from, but here they broadly align with the quantitative story.

## Weaknesses
My main concern is that the paper’s strongest contribution is the dataset/benchmark, while the algorithmic contribution feels more like a careful assembly of known ingredients than a deeply new modeling idea. The core method in Section 5 combines a standard flow-matching objective, a cosine identity loss in **Equation (4)**, and an InfoNCE-style contrastive loss in **Equation (5)** with a larger negative pool. That is not inherently bad, but the paper often writes as if the method itself is a substantial conceptual leap. I do not think the main paper convincingly differentiates this recipe from prior identity-preserving tuning work that already uses identity embeddings, reconstruction training, and auxiliary identity-alignment objectives. This matters because the overall contribution claim in the abstract and conclusion packages dataset, benchmark, and method together; in reality, the method appears to be the least distinctive of the three.

The mathematical presentation around the contrastive loss is sloppy enough to reduce confidence. In **Equation (5)** on Page 6, the stated numerator is $\exp(\cos(\mathbf{g}, \mathbf{t})/\tau)$ while the denominator is written as $\sum_{j=1}^M \exp(\cos(\mathbf{g}, \mathbf{n}_j))/\tau)$. As written, the positive pair does not appear in the denominator, which is not the standard InfoNCE form. If the intention is
\[
-\log \frac{\exp(\cos(\mathbf g,\mathbf t)/\tau)}{\exp(\cos(\mathbf g,\mathbf t)/\tau)+\sum_{j=1}^{M}\exp(\cos(\mathbf g,\mathbf n_j)/\tau)},
\]
then the equation should say exactly that. If not, the loss is unusual and needs justification. This is not a cosmetic nitpick, because the precise form changes the optimization behavior.

Relatedly, the notation around positives and references is inconsistent. Section 5.1 says the contrastive loss “pulls the generated image closer to its reference images,” but **Equation (5)** uses $\mathbf t$ as the positive sample, where $\mathbf t$ is earlier defined as the target or ground-truth embedding, not the reference embedding. That may be a reasonable design choice, but the prose and notation do not match. The paper repeatedly alternates between “reference” supervision and “ground-truth-aligned” supervision, and this becomes especially confusing because **Equation (4)** and **Equation (5)** both use $\cos(\mathbf g,\mathbf t)$. If the method is primarily anchored to the target image rather than the reference image, that should be stated more cleanly, and the role of the reference in the contrastive objective should be clarified.

There is another mathematical inconsistency regarding the flow-matching parameterization. In the main paper, **Equation (3)** defines
\[
x_t = (1-t)x_0 + t x_1
\]
and regresses the target velocity $(x_1-x_0)$. In the appendix, **Equation (10)** instead states
\[
x_t = (1-t)x_1 + t x_0,
\]
and then says the model predicts the velocity corresponding to $x_0-x_1$. These are opposite conventions. One can make either convention work, but both cannot simultaneously describe the same training setup unless the signs and interpolation directions are adjusted consistently. This is exactly the kind of detail that should not wobble in a paper making training-objective claims.

The GT-aligned identity loss is intuitively appealing, but the main paper underspecifies an important assumption: it uses ground-truth landmarks to align the generated face. That means the loss depends on target-side geometric information that is unavailable at inference. The paper frames this as “implicitly supervises generated landmarks” on Page 5, but that is a strong claim and the main text does not justify why learning under GT landmark alignment should improve identity rather than partially bake in target-specific geometry. **Figure 7** on Page 9 gives a qualitative comparison of GT-aligned versus prediction-aligned landmarks, but it is still not fully convincing that this supervision is not conflating identity learning with target pose/alignment leakage. At minimum, the paper should discuss this more candidly as a training-time privileged signal.

The copy-paste metric in **Equation (2)** is interesting, but its interpretation is a bit too optimistic in the text. The score depends on the face embedding model and on the angular distance between target and reference, normalized by $\max(\theta_{tr},\varepsilon)$. When $\theta_{tr}$ is small, the metric can become unstable or very sensitive to small embedding perturbations, even with $\varepsilon$. The paper says the score lies in $[-1,1]$, but this boundedness is asserted rather than derived, and in practice it depends on triangle-inequality-like behavior in angular space. More importantly, the metric is only meaningful if the face embedding backbone is itself reliable under pose, lighting, makeup, occlusion, and artistic style changes, which is exactly the regime under discussion. The paper partially addresses evaluator bias in the appendix by averaging ArcFace, FaceNet, and AdaFace for similarity, but the main paper does not explain clearly whether the copy-paste metric also uses that averaging or only a single embedding model. This ambiguity matters because the benchmark contribution stands or falls on evaluation design.

I also found the experimental story somewhat selective. **Table 1a** shows the proposed method achieving the best $\mathrm{Sim}(\mathrm{GT})$ among many baselines, but its aesthetic score is lower than a large fraction of competitors, and its OmniContext performance in **Table 1b** is not particularly strong overall. The authors acknowledge this partially, but the writeup leans heavily on the benchmark they designed. That makes it harder to disentangle “the method is better” from “the evaluation particularly rewards the method’s design choices.” Stronger cross-benchmark validation would have helped.

The ablation study is useful but still too shallow for the paper’s central claims. **Table 3** bundles several factors, but it does not isolate enough. For example, the paper argues that the extended-negative contrastive loss is crucial, yet the ablation “w/o Ext. Neg.” changes both the effective number of negatives and likely the optimization regime. Similarly, the paired-data benefit is demonstrated by removing Phase 3, but that phase changes both the data distribution and the objective context. The results support the intuition, but not as cleanly as the prose suggests. Since the method contribution is already modest, stronger ablations are important.

The qualitative evidence in **Figure 6** is supportive but cherry-pick risk remains. Several examples are favorable to the proposed model, but there is no systematic failure analysis. For example, I would like to know in what cases WithAnyone still collapses toward reference copying, loses identity under large pose changes, or blends multiple people in group scenes. A strong benchmark paper should make failure modes of its own model visible, not only those of competitors.

The paper’s scope is also narrower than the framing implies. The dataset is celebrity-centric and the references are collected from public web images, with many identities having hundreds of images. That is an easier regime than ordinary personalization where one or a few user images are available. The appendix includes some qualitative examples on non-celebrity references, but the main-paper claims about controllable identity generation would be much stronger if the paper were more explicit that its training and evaluation regime is specialized to data-rich public identities. This matters scientifically because the benchmark may not reflect the harder low-shot use case that motivates much prior personalization work.

Finally, the ethics section is thoughtful in wording but thin on technical mitigation. The authors correctly note impersonation and deceptive media risks on Page 10, yet the release plan appears to include models and datasets without any concrete safeguard mechanism such as watermarking, traceability, identity misuse filtering, or restricted generation policies. For a paper explicitly optimizing identity consistency of real public figures, that omission is not trivial.

## Questions
1. Please clarify the exact definition of the contrastive loss in **Equation (5)**. Does the denominator include the positive term or not? If the printed equation is incorrect, please provide the corrected form and confirm which version was actually used in experiments.

2. Please reconcile the inconsistency between **Equation (3)** in the main paper and **Equations (10)–(11)** in the appendix regarding the interpolation direction and velocity target. Which formulation is the actual training objective? If both are equivalent under a sign convention, please write that equivalence explicitly.

3. For the GT-aligned identity loss in **Equation (4)**, how much of the gain comes from improved identity supervision versus privileged access to target landmarks/geometry at training time? A clarification of this point, ideally with a more direct control experiment, would increase my confidence.

4. For **Equation (2)**, which face embedding model is used to compute the copy-paste metric in the main results? If multiple models are averaged for identity similarity, is the same true for copy-paste? If not, why not?

5. Could the authors provide more analysis on cases where WithAnyone fails? In particular, examples involving extreme pose change, occlusion, multiple similar-looking people, or weak/low-quality references would be valuable. This would make the benchmark contribution more credible.

6. The method seems to benefit substantially from Phase 3 in **Table 3**. Can the authors clarify whether the gain is primarily from paired supervision itself, from mixing reconstruction and paired training at 50/50, or from the added identity objectives during that phase? Some disentangling here would help assess what is actually essential.

7. The paper claims WithAnyone “breaks” the fidelity-copy-paste trade-off based on **Figure 5**. I would tone this down unless the authors can show this persists across multiple seeds, evaluator backbones, and broader benchmarks. Can you provide evidence that the observed deviation is robust rather than an artifact of a particular fit or metric choice?

## Flag For Ethics Review
- Yes, Privacy, security and safety  
- Yes, Legal compliance (e.g., GDPR, copyright, terms of use)  
- Yes, Potentially harmful insights, methodologies and applications  

## Details Of Ethics Concerns
The paper develops and releases identity-consistent generation methods for real people, specifically public figures, and explicitly optimizes identity preservation across pose/expression changes. This creates clear impersonation and deceptive-media risks, as acknowledged in the Ethics Statement on **Page 10**. The risk is heightened by the release of a large paired dataset and trained models, because these lower the barrier for misuse.

There are also legal/compliance questions around data collection from web search results, even with Creative Commons filtering, because image reuse permissions, personality rights, publicity rights, and jurisdiction-specific biometric/privacy rules are not fully resolved simply by anonymizing names into internal IDs. The paper discusses licensing constraints and public-source filtering on **Pages 4 and 10**, which is good, but that does not by itself eliminate downstream legal and ethical issues.

My concern is not that the work should be blocked from publication purely on ethics grounds, but that the technical mitigation story is weak relative to the capability being released. I would like the authors to more concretely describe release restrictions, abuse prevention measures, and whether any watermarking, tracing, or misuse detection tools accompany the model.

## Soundness Rating
3: good. The main claims are generally supported by experiments, but there are nontrivial issues in the mathematical specification and some evaluation ambiguities that should be corrected.

## Presentation Rating
3: good. The paper is readable and well organized overall, with helpful figures such as **Figures 3, 4, 5, and 6**, but some notation and objective definitions are inconsistent or imprecise.

## Contribution Rating
3: good. The dataset and benchmark are valuable contributions, and the empirical findings are useful, although the method itself feels more incremental than the paper’s framing suggests.

## Overall Rating
6: Marginally above the acceptance threshold. But would not mind if paper is rejected. The benchmark and dataset contributions are strong enough, and the empirical evidence is compelling enough, to lean positive despite concerns about method novelty, objective specification, and evaluation clarity.

## Reviewer Confidence
4: confident. I am confident in my assessment, though not absolutely certain. It is unlikely, but not impossible, that I misunderstood some implementation details because the paper contains a few inconsistencies in notation and loss definitions.