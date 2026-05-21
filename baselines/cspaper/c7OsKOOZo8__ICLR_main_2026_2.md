---
job_id: aa9cbbfc-ed15-4b5c-b044-9ad517f552e9
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: c7OsKOOZo8.pdf
paper: Expert-Guided Cross-View Fusion with Self-Derived Lesion Proposals for Multi-View Diabetic Retinopathy Grading
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, it proposes a representation-learning and cross-view fusion method for multi-view medical image classification, with explicit methodological contributions in lesion proposal generation and expert-guided fusion.

## Minimum Quality
Pass ✅. The paper contains the expected scientific structure, including Abstract, Introduction, Related Work, Method, Experiments with quantitative results, and Conclusion. While I have substantial concerns about novelty positioning, mathematical precision, and experimental completeness, these do not rise to the level of an immediate desk rejection.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find hidden prompts, suspicious instructions to automated reviewers, or other manipulative content in the provided paper text or figures.

# Expected Review Outcome:
## Summary
This paper studies multi-view diabetic retinopathy grading from fundus images, with the goal of reducing reliance on external lesion or vessel annotations. The proposed framework combines a Grade-Activated Lesion Proposal module, which derives stage-wise class-activation-based lesion proposals from intermediate features, and a Cross-View Lesion Expert Guided Regional Fusion module, which uses gated experts and proposal-restricted cross-view attention for fusion across views. Experiments on MFIDDR and DRTiD show improvements over several end-to-end baselines, and competitive results against methods that use external lesion, vessel, or anatomical annotations.

## Strengths
The paper addresses a relevant problem in medical vision, namely how to exploit multi-view structure while avoiding dependence on costly external lesion annotations. That practical motivation is clear and well explained in the introduction.

The overall architecture in **Figure 2** is helpful. In particular, **Figure 2(b)** makes the GALP pipeline reasonably intuitive by showing how stage features are routed through an auxiliary classifier into grade-conditioned evidence maps and then Top-$K$ region selection. **Figure 2(c)** also conveys the intended logic of the method, namely that adjacent-view proposal tokens are processed by a small expert pool and fused through weighted cross-view attention, rather than indiscriminate full-token fusion. This visual decomposition supports the paper’s central claim that the method tries to restrict cross-view interaction to lesion-salient regions instead of the full background.

The empirical results on MFIDDR are promising. In **Table 1**, the lesion-free version of the proposed model improves over the strongest listed end-to-end baselines, for example over ETMC and MVCINN on Acc/Kappa/F1, and comes close to some externally informed methods despite not using their extra supervision. That is a meaningful practical result if the comparison is fair.

The ablation in **Table 4** is directionally useful. Removing GALP, Experts, or all of LGRF consistently reduces Acc/Kappa/F1, which supports the claim that the two major modules contribute beyond the plain backbone. The gain is not huge, but it is reasonably consistent across the shown metrics.

The paper also includes grade-wise analysis on MFIDDR in **Table 2**, which is better than reporting only aggregate accuracy. The fact that the method appears strongest in Grades 2 and 3 is potentially important, since those mid-to-severe classes are often where clinically relevant lesion evidence becomes more distributed and multi-view corroboration may matter.

## Weaknesses
1. **The core claim that CAM peaks correspond to lesion proposals is asserted much more strongly than it is validated.**  
   The whole paper hinges on the idea in **Section 3.2** that grade-conditioned evidence maps can be interpreted as lesion regions, and that Top-$K$ selected patches become meaningful lesion proposals. However, the paper does not provide any direct evidence that these proposals actually overlap with lesions, even on MFIDDR where lesion masks are explicitly available according to **Section 4.1**. This matters a lot scientifically: if the selected regions mostly capture confounders, camera artifacts, view-specific anatomy, or coarse disease-correlated texture rather than lesions, then the method is not really demonstrating "self-derived lesion proposals" in the sense claimed by the title and abstract. At minimum, I expected either overlap statistics with available lesion masks, or qualitative examples showing proposal localization on representative images across grades. The absence of such validation makes the central interpretability and mechanism claim under-supported.

2. **Several mathematical definitions are underspecified or internally inconsistent enough to weaken confidence in the implementation.**  
   There are multiple issues here:
   - In **Equation (3)**, the notation for the class-specific weight vector is confusing. The text says $\mathbf{w}^{(\hat{\mathbf{y}}^{i}_{s_n})}_{s_n}\in\mathbb{R}^{C_{s_n}}$, but the equation indexes it as $\mathbf{w}^{(\hat{\mathbf{y}}^{i}_{s_n})}_{s_n,\tilde{c}}$ while summing over $c$. It is unclear whether $\tilde{c}$ and $c$ are intended to be the same index or not.
   - The phrase "predicted grade $\hat{\mathbf{y}}^{i}_{s_n}$" is also sloppy mathematically. $\hat{\mathbf{y}}^{i}_{s_n}$ is introduced as a softmax distribution after **Equation (1)**, not a discrete class index. CAM normally uses a class index, e.g. $\arg\max_k \hat y_k$, not the probability vector itself.
   - The normalization after **Equation (3)** is informal, written as $\tilde{\mathbf{A}}=(\mathbf{A}-\min)/(\max-\min)$ without precise indexing or treatment of the degenerate case $\max=\min$.
   - In **Equation (11)**, the load-balancing loss is defined using $\hat u_m$ as the fraction of tokens assigned to expert $m$, but the routing in **Equation (9)** appears to be performed from the mean of current-view tokens, which would naturally give one routing distribution per sample rather than token-level routing. The notion of "fraction of tokens actually assigned" therefore does not cleanly match the preceding routing definition.  
   These are not cosmetic nits. The paper’s contribution is methodological, so if the proposal formation and expert routing are not stated cleanly, it becomes hard to assess correctness or reproduce the system.

3. **The fusion design is more restricted than the paper’s framing suggests, and the rationale for that restriction is not discussed.**  
   In **Section 3.3**, cross-view fusion is performed only between a view and its adjacent cyclic view $j=i+1$ (with wrap-around), rather than across all other views. For a four-view setting like MFIDDR, this is a strong architectural choice. It means each view only receives direct information from one other view, not from all complementary views. Yet the paper markets the approach as exploiting cross-view corroboration broadly. This discrepancy matters because in multi-view retinal imaging, the most informative corroborating view may not be the arbitrarily defined adjacent one. I can imagine both computational and anatomical reasons for the design, but the paper does not justify them, compare against all-to-all fusion, or analyze whether the cyclic adjacency is meaningful or merely convenient.

4. **The empirical gains are real but modest, and the paper overstates the strength of the SOTA claims.**  
   The strongest lesion-free result on MFIDDR in **Table 1** is $83.9$ Acc versus $81.5$ for ETMC and $80.1$ for MVCINN, which is solid. But against the best externally informed methods the gap is not universally closed, and on DRTiD in **Table 3** the main gain over CrossFiT is only $76.0$ vs $75.6$ Acc, while the AUCs are mixed and the table formatting is ambiguous enough that it is not immediately clear whether macro-AUC is reported. The conclusion and abstract repeatedly use broad phrases like "surpass strong baselines" and "SOTA competitiveness" without enough restraint. For a medical imaging paper with small absolute differences, stronger statistical support is needed. There are no confidence intervals, no repeated runs, no significance testing, and no indication of variance. Without that, it is hard to know whether some reported wins, especially on DRTiD, are robust or just within normal training noise.

5. **The comparison protocol raises fairness questions because pretraining and auxiliary information are not normalized across baselines.**  
   In **Section 4.1**, the backbone initialization differs by dataset and follows prior work: ImageNet pretraining on MFIDDR, EyePACS pretraining on DRTiD. That is acceptable by itself, but the comparison tables mix methods from different papers, potentially with different backbones, preprocessors, image resolutions, and pretraining schemes. For example, the paper uses Swin-B and additional preprocessing on MFIDDR, while several listed baselines likely use quite different settings. This does not invalidate the comparison, but it does mean the tables should be interpreted carefully. The paper should make much clearer which baselines are numbers copied from prior work under potentially non-identical training recipes, and which, if any, are reimplemented under a shared protocol. Right now the framing is a bit too confident for what appears to be mostly cross-paper comparison.

6. **The ablation study is too shallow to substantiate the mechanism of the method.**  
   **Table 4** shows that removing GALP or LGRF hurts performance, but the ablation does not probe the design choices that are actually central to the claimed contribution. For example:
   - Is CAM-based Top-$K$ proposal selection better than random regions, uniform top-left patches, or simple saliency from feature norms?
   - Is routing from mean current-view tokens in **Equation (9)** better than self-view proposal routing, all-view routing, or ungated expert averaging?
   - Is adjacent-view fusion better than all-other-view fusion?
   - Does using Top-$K$ proposals help because of sparsity, or simply because fewer tokens reduce overfitting?  
   The hyperparameter plots in **Figure 3** are also quite limited. They show that $\alpha=50\%$, $K_2=2$, and $M=6$ work best among a small discrete set, but they do not explain why. Also, the gains in **Figure 3(a-c)** are fairly small, which suggests the method may not be especially sensitive to the proposed expert machinery. The paper needs stronger ablations tied to the conceptual claims, not just module removal.

7. **The paper misses an opportunity to use the available lesion annotations for validation even in the annotation-free setting.**  
   This is distinct from point 1. The authors correctly argue that training should not depend on lesion annotations, and I agree. However, MFIDDR provides lesion masks according to **Section 4.1**, and those masks could still be used for post hoc evaluation of the self-derived proposals. For instance, proposal recall over lesion pixels, average IoU over selected regions, or lesion-class-sensitive recall across severity grades would directly test the paper’s main narrative. Since the method’s title explicitly foregrounds "Self-Derived Lesion Proposals," the lack of such validation is a significant omission.

8. **Some presentation issues materially reduce clarity.**  
   There are quite a few notation and writing problems: inconsistent variable names ($\alpha$ vs $r$ in **Section 4.1**, where the text says retention ratio $\alpha$ but then says "we fix $r=50\%$"), awkward grammar throughout, and some imprecise wording like "which is the spatial regions most predictive of the grade" on **Page 2**. In **Equation (15)**, the weights passed to $\mathrm{MHA}_{\mathrm{CVA}}$ are written as $\{\hat w^{j}_{s_n,k_2}\}$, whereas earlier the importance weights are defined from routing scores of the current view as $\hat w^{i}_{s_n,k_2}$. This kind of index mismatch is exactly the sort of thing that creates uncertainty about what was actually implemented. The paper is readable overall, but not yet at the level of precision I expect for a method-heavy ICLR submission.

9. **The practical deployment claim is overstated relative to the evidence provided.**  
   The conclusion claims practical potential for clinical deployment. That is too strong given the current experimental scope. The evaluation is limited to two fixed datasets, no robustness tests are shown for missing views, acquisition artifacts, demographic shifts, or class imbalance sensitivity, and no calibration analysis is reported. For medical screening, those issues are not optional extras. I do not require a full clinical study here, but the deployment language should be toned down.

## Questions
1. The paper’s main premise is that GALP produces lesion proposals. Can the authors provide quantitative evidence on MFIDDR that the Top-$K$ selected regions actually overlap with lesion masks, even if those masks are not used for training? For example, proposal recall, pixel overlap, or patch-level lesion coverage would substantially increase my confidence.

2. In **Equation (3)**, what exactly is the class index used to compute the CAM? Is it $\arg\max_k \hat y_k$, the ground-truth class during training, or something else? Please rewrite this equation with unambiguous indexing and explain how gradients flow through the Top-$K$ selection step, if at all.

3. In **Equation (11)**, how is $\hat u_m$ computed given that routing in **Equation (9)** appears sample-level after averaging tokens? Are experts assigned per sample or per token? Please provide a more precise definition of expert utilization and the exact load-balancing implementation.

4. Why is fusion restricted to the adjacent cyclic view in **Section 3.3**? Did the authors test all-to-all fusion or learned view-pair selection? A small ablation here could materially strengthen the cross-view story.

5. For the MFIDDR and DRTiD comparisons in **Tables 1 and 3**, which baseline numbers are taken directly from prior papers and which are reproduced by the authors? If they are not under identical training recipes, please clarify this more explicitly.

6. Can the authors report mean and standard deviation over multiple runs, especially for **Table 3**, where the margin over CrossFiT is only $0.4$ points in accuracy? This would help determine whether the claimed gain is reliable.

7. Since the paper also reports an "Ours (with lesion)" version in **Table 1** and **Table 2**, what exactly is being fused from lesion annotations, and how much of the gain comes from the proposed architecture versus the added lesion supervision? A direct comparison to a simpler lesion-fusion baseline under the same backbone would be useful.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
None beyond standard caution for medical imaging claims. The paper does not raise a specific ethics red flag that requires formal escalation based on the content presented.

## Soundness Rating
2: fair. The method is plausible and the experiments are nontrivial, but important implementation details are underspecified, core mechanism claims are insufficiently validated, and the empirical support lacks uncertainty estimates and stronger fairness controls.

## Presentation Rating
2: fair. The high-level idea is understandable and **Figure 2** helps, but notation inconsistencies, ambiguous equations, and several writing issues materially hinder precise understanding.

## Contribution Rating
2: fair. The paper has a relevant application and a sensible combination of self-derived proposals with cross-view expert fusion, but the contribution is not yet demonstrated with the level of rigor or validation needed to make it a strong ICLR contribution.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted. The paper is promising and addresses a useful problem, with encouraging empirical results, especially on MFIDDR. However, the current version over-claims what the self-derived lesion proposals actually achieve, leaves several mathematical and implementation details ambiguous, and does not provide the validation needed to firmly support its central mechanism.

## Reviewer Confidence
4: confident. I am confident in the overall assessment and carefully checked the method, equations, figures, and tables, though some implementation ambiguities in the paper prevent absolute certainty.