---
job_id: 78f01571-0281-4640-8cb4-dd6e0fa26ce1
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: ulXBsAYSwU.pdf
paper: MolMiner: Towards Controllable, 3D-Aware, Fragment-Based Molecular Design
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope as a generative modeling paper for molecular design, combining autoregressive modeling, graph/geometry-aware learning, conditional generation, and benchmarking for an ML application in chemistry.

## Minimum Quality
Pass ✅. The submission contains the expected core components, including Abstract, Introduction, Related Work, Method, Experiments, quantitative results, limitations, and conclusion. While I have substantial concerns about empirical completeness, mathematical precision, and positioning, these are review-level weaknesses rather than desk-reject issues.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find any hidden instructions, suspicious reviewer-targeting text, or other manipulative content in the provided paper text and figures.

# Expected Review Outcome:
## Summary
This paper presents MolMiner, a fragment-based autoregressive molecular generator that aims to combine four ingredients in one framework: order-agnostic rollouts, symmetry-aware fragment attachment handling, dynamic 3D geometry updates through force-field relaxation, and multi-property conditional generation over twelve molecular properties. The model uses a transformer decoder with a distance-based attention bias and supports conditioning on any subset of properties by sampling unspecified ones from a Gaussian mixture model. The experimental section evaluates unconditional generation via property-distribution matching and conditional generation via calibration plots over the 12 target properties.

## Strengths
- The paper tackles a practically relevant problem setting. The focus is not just unconditional molecule generation, but controllable generation under many user-specified property constraints, which is a more realistic use case for inverse design.

- The overall system design is reasonably coherent. The fragment-based representation, the local attachment/termination actions, and the order-agnostic rollout idea fit together naturally. The paper is trying to solve a real modeling bottleneck rather than merely adding one more neural architecture to a crowded benchmark.

- I appreciate that the authors explicitly discuss symmetry handling for fragment attachments, rather than sweeping it under the rug. Even though the presentation is not yet fully rigorous, this is an important engineering and modeling issue in fragment-based generation.

- The conditional-generation evaluation is more informative than the usual “one scalar optimization score” style. In particular, **Figure 2** is useful because it exposes where control works and where it does not. The plots make it easy to see that properties like logP, SAS, and FractionCSP3 are reasonably calibrated, while QED, molWt, and MR show systematic deviations. That is a much more honest and useful presentation than reporting only average property errors.

- The paper also deserves some credit for not over-claiming unconditional superiority. **Table 1** makes it clear that MolMiner is weaker than HierVAE on several unconditional distribution-matching metrics, especially molWt, TPSA, and MR. This transparency helps the reader separate the model’s main contribution, conditional control, from aspects where it is not yet competitive.

- The ablation plots in the appendix, although not decisive for the final verdict, do provide some support for a few design decisions. For example, the geometry-related training curves in **Figure 6** and the rollout-resampling curves in **Figure 8** are at least directionally consistent with the authors’ claims that geometry helps and resampling regularizes training.

## Weaknesses
1. **The empirical comparison is too narrow for the paper’s scope and claims.**  
   The paper claims to unify dynamic geometry, symmetry handling, order-agnostic generation, and high-dimensional conditioning, but the main quantitative comparison in unconditional generation is essentially against only **HierVAE** in **Table 1** (Pages 6-7). That is simply too thin for a paper making broad claims about controllable, 3D-aware, fragment-based molecular design. Since the central pitch is not merely “another fragment model,” but specifically a geometry-aware and controllable one, the experimental section should compare to stronger contemporary geometry-aware and/or fragment-based baselines, or at least explain in a much more systematic way why such comparisons are impossible. As written, the reader is left with a one-baseline story plus an anecdotal exclusion of MoLeR. That weakens the paper’s ability to substantiate its claimed advance over the prior art.

2. **The central benefit of dynamic 3D geometry is asserted more than demonstrated.**  
   The main methodological hook is that intermediate molecular geometry is dynamically relaxed and used during generation. Yet the evidence that this matters for downstream generation quality is limited. The main paper gives only a brief statement in Section 4.1 that geometry-aware attention helps when initialized with positive bias, and the supporting evidence is relegated to appendix training curves. But better reconstruction loss in **Figure 6** is not the same as demonstrating materially better generation quality, conditional controllability, or chemically meaningful 3D behavior. If the core claim is that force-field-updated geometry improves generation, then the paper should show this in generation-time metrics, not only training/validation loss curves. Right now, the 3D-aware story feels under-validated relative to how prominently it is marketed.

3. **The order-agnostic rollout contribution is also under-validated.**  
   Equation (1) and Equation (3) put order-agnostic factorization at the center of the model, and Section 3.3 argues it improves flexibility and acts as a regularizer. However, the evidence again mostly reduces to improved loss curves under resampling, especially in **Figure 8**. That is suggestive, but it does not really establish whether order-agnostic generation leads to better sample quality, better conditional calibration, better diversity, or more robust generalization compared with fixed rollout orders. This matters because order-agnostic factorization is one of the paper’s headline contributions. At present, it reads more like a plausible design choice than a convincingly demonstrated scientific contribution.

4. **The unconditional evaluation protocol is mismatched with the model’s strongest claims, and even within that protocol the results are not particularly competitive.**  
   In Section 4.2, unconditional generation is evaluated by matching 12 scalar property distributions using 1D Wasserstein distances, plus uniqueness/novelty/diversity. This is a limited view of molecular generation quality, because matching marginal property distributions does not tell us whether the joint distribution, structural realism, or chemistry beyond those descriptors is captured. More importantly, **Table 1** shows MolMiner trails HierVAE quite noticeably on several key properties, especially molecular weight, TPSA, and MR. The paper acknowledges this, but the explanation in Section 5, early termination bias induced by many termination actions, remains speculative because no targeted experiment is provided to verify it. So the paper asks the reader to accept a fairly large performance gap on faith, with only a hypothesis and no direct evidence.

5. **The conditional evaluation is informative, but still incomplete for a model claiming flexible multi-property control.**  
   **Figure 2** is a useful start, but it only evaluates one prompted property at a time while the remaining eleven are sampled from the GMM prior (Section 4.3, Page 7). That leaves the central multi-property control story under-tested. A model that truly supports conditioning on arbitrary subsets of 12 properties should be evaluated on multi-property prompts, especially conflicting or correlated property combinations, not only single-property sweeps. The current setup mostly answers, “Can the model respond monotonically to one control dimension while others are plausibly imputed?” It does not answer the more demanding question, “Can the model satisfy several simultaneous user constraints?” That gap is important because it directly touches the practical utility of the system.

6. **The GMM-based conditioning mechanism is convenient, but the paper overstates its reliability for mixed, constrained property spaces.**  
   Section 3.6 and Appendix A.2 use a Gaussian mixture model to fill in unspecified properties. This is reasonable as a heuristic, but the evidence for adequacy is modest. **Figure 3** uses an elbow-style BIC/AIC argument for choosing \(K=8\), and **Figure 4** evaluates reconstruction of one missing property given the others. That does not establish that the GMM provides faithful conditional samples for arbitrary subsets, nor that it handles discrete properties appropriately. In fact, the appendix itself notes artifacts for discrete variables such as number of rings. Since this GMM is a core enabler of the “condition on any subset” claim, the current validation feels too weak. The framework’s flexibility depends heavily on this component, so this is not a minor detail.

7. **Several mathematical formulations are underspecified or imprecise, which matters because they describe the core learning objective.**  
   - In **Equation (1)**, the paper defines \(p(\mathcal{M})\) as an expectation over a uniform distribution on valid rollout trajectories \(R \sim \mathcal{U}(\mathcal{R}(\mathcal{M}))\). But it is never made explicit what exactly counts as a distinct rollout, whether symmetrically equivalent action sequences are collapsed or counted separately, and how the set \(\mathcal{R}(\mathcal{M})\) is constructed in practice. Given that symmetry handling is a key contribution, this omission is not cosmetic. It affects the meaning of the likelihood itself.
   - In **Equation (3)**, the paper applies Jensen’s inequality to obtain a lower bound, then says it samples one rollout per molecule per epoch. That is fine as a stochastic training heuristic, but the manuscript does not discuss whether this estimator is unbiased for the bound, how rollout variance behaves, or how much the training objective depends on the rollout-sampling distribution. Since the whole order-agnostic story relies on this factorization, more precision is needed.
   - In **Equation (2)**, the attention bias is written as  
     \[
     \alpha_{ij}=\frac{\exp(g(h_i,h_j)+\theta D_{ij})}{\sum_k \exp(g(h_i,h_k)+\theta D_{ik})}, \quad D_{ij}=\exp\left(-\frac{\|x_i-x_j\|^2}{2\sigma^2}\right).
     \]
     This raises several missing details: are \(x_i\) fragment centroids, attachment-point coordinates, or something else; is \(\sigma\) fixed or learned; is \(D_{ij}\) recomputed after every force-field update; and how are fragments with multiple spatially extended atoms reduced to one point? Those choices materially affect the meaning of the geometry-aware attention.
   - In Appendix A.2, the notation around the conditional GMM is sloppy. For example, **Equation (5)** appears to write \(f(\vec{x}_{obs}|\vec{x}_{miss})\) when the surrounding derivation is clearly about \(f(\vec{x}_{miss}|\vec{x}_{obs})\). Similarly, the formula for \(w_k\) includes a summation index on the left-hand side that should not be there. These are not just typographical nits, because this appendix is where the “any subset of properties” mechanism is actually specified.

8. **The symmetry-handling method is interesting, but the main paper does not provide enough rigor to judge whether it is correct or general.**  
   Section 3.2 argues that because extracted fragments are rings or bonds, the atom remapping problem reduces to cyclic permutations. That may hold for their chosen decomposition, but the justification is too informal for such a strong statement. The argument seems to rely on assumptions about RDKit canonicalization behavior and fragment topology that are not fully proven in the main paper. The appendix introduces mappings \(F_i\), a reference mapping \(F_0\), and the standardized map in **Equations (6) and (7)**, but it is not shown why taking  
   \[
   x \mapsto \min_i \left(F_0^{-1}(F_i(x))\right)
   \]
   is the right symmetry-invariant operation, or whether it can merge chemically distinct attachment configurations in edge cases. Given that the entire action space depends on standardized attachment identities, this deserves a clearer formal treatment and at least a sanity-check experiment showing that standardization is stable and collision-free on the dataset.

9. **The presentation contains multiple inaccuracies, naming inconsistencies, and signs of insufficient polishing.**  
   The tables and property names contain several errors, for example **Table 1** includes labels such as “SagP,” “PractCSP3,” “Rfothondt,” and “ANovelty,” and Appendix tables contain similarly garbled headers. The text also alternates between naming conventions for properties. These may look superficial, but they hurt trust because the paper is fundamentally about careful handling of molecular properties and attachment actions. If the tables are not clean, readers naturally worry about whether the preprocessing and evaluation code are equally brittle.

10. **The paper’s claims are broader than what is actually demonstrated.**  
   The title and abstract emphasize “controllable, 3D-aware, fragment-based molecular design,” but the experiments remain centered on reproducing RDKit-computed scalar properties on a ZINC subset. There is no demonstration on structure-sensitive downstream objectives, no evaluation of 3D plausibility beyond the use of UFF, and no task showing that dynamic geometry changes decisions in a chemically meaningful way. So while the ingredients are interesting, the evidence supports a narrower claim: a fragment generator with some geometry bias and moderate single-property calibration on descriptor-level targets. That is still potentially useful, but it is not yet the full story the paper advertises.

## Questions
1. The most important missing experiment for me is multi-property conditional control. Could the authors report results where 2, 3, or more properties are simultaneously prompted, including correlated and conflicting combinations? In particular, I would like to see either joint calibration plots or satisfaction rates for property tuples, not only one-property-at-a-time sweeps.

2. Can the authors provide generation-time evidence, not only training-loss evidence, that dynamic geometry actually helps? For example, comparing the full MolMiner against a variant with \(\theta=0\) in **Equation (2)** on conditional calibration, distribution matching, and diversity would materially increase my confidence.

3. For the order-agnostic contribution, could the authors compare against a fixed rollout order using the same backbone and training budget? Right now the regularization claim is mostly inferred from **Figure 8**, but a direct generation-quality comparison would be much more convincing.

4. Please clarify the exact definition of a valid rollout in **Equation (1)**. How are symmetrically equivalent action sequences counted, and what is the practical algorithm for sampling uniformly from \(\mathcal{R}(\mathcal{M})\)? If the sampling is only approximately uniform, please say so explicitly.

5. In **Equation (2)**, what exactly are the coordinates \(x_i\) for a fragment, how is \(\sigma\) chosen, and are distances based on fragment centroids or attachment-site locations? These details are crucial for understanding the geometric inductive bias.

6. The appendix GMM derivation appears to contain notation errors around **Equation (5)** and the definition of \(w_k\). Please correct these and clarify whether the conditional sampler handles mixed continuous/discrete properties directly, or whether discrete variables are relaxed to continuous values and then post-processed.

7. The symmetry standardization procedure in Section 3.2 and Appendix A.6 is intriguing, but I could not tell how robust it is in practice. Could the authors provide statistics on how often multiple valid mappings occur, whether collisions arise, and whether the standardized mapping ever merges attachment cases that should remain distinct?

8. The paper attributes unconditional underperformance to early termination bias in Section 5. Can the authors test this directly, for example by reporting action-frequency statistics, average rollout lengths, molecule size distributions, or a reweighted termination-loss variant?

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
No major ethics concerns requiring formal ethics review are evident from the paper. The work is a standard molecular generation study on an existing dataset with computed descriptor targets, and the manuscript does not describe deployment or generation of explicitly hazardous compounds.

## Soundness Rating
2: fair. The core method is plausible and some claims are supported, but several central claims, especially around the benefits of geometry and order-agnostic rollouts, are not adequately validated, and key mathematical components are underspecified.

## Presentation Rating
2: fair. The paper is readable at a high level, and some figures, especially **Figure 2**, are useful, but the presentation is weakened by imprecise equations, under-explained methodology, and multiple table/notation inconsistencies.

## Contribution Rating
2: fair. The combination of ideas is interesting and relevant, particularly the attempt to unify fragment-based generation, geometry awareness, and flexible conditioning, but the empirical evidence and positioning are not yet strong enough for me to view this as a solid ICLR-level contribution in its current form.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted. The paper has a promising core idea and some useful evaluation elements, but too many central claims remain under-validated, and the empirical comparison and mathematical precision are not yet strong enough for a positive recommendation.

## Reviewer Confidence
4: confident. I am confident in this assessment, though not absolutely certain. I am familiar with molecular generative modeling and checked the main methodological and experimental details with care.