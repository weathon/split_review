---
job_id: aba8c41a-b5f4-46a1-a73f-7326c399b1ae
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: pW6rFymZ8F.pdf
paper: EMBodiedMAE: A Unified 3D Multi-Modal Representation for Robot Manipulation
main_score_norm: 0.6
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, focusing on self-supervised multi-modal representation learning, datasets/benchmarks, and applications to robot manipulation.

## Minimum Quality
Pass ✅. The paper contains the expected scientific structure, including abstract, introduction, methodology, experiments, quantitative and qualitative results, related work, and conclusion/limitations, and it provides enough technical and empirical material to merit full review.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find any hidden prompts, suspicious instructions targeting automated reviewers, or other manipulative content in the provided paper text and figures.

# Expected Review Outcome:
## Summary
This paper introduces EmbodiedMAE, a multi-modal masked autoencoder for robot manipulation that jointly learns representations from RGB, depth, and point cloud inputs. The work also constructs DROID-3D by augmenting DROID with processed depth maps and point clouds, and evaluates the learned representations on LIBERO, MetaWorld, and two real-world robot platforms. The main claim is that pre-training on DROID-3D with stochastic multi-modal masking and cross-modal decoding yields better policy learning performance than a range of existing vision foundation model baselines.

## Strengths
- The paper tackles an important problem. There is a real gap between general-purpose 2D visual pretraining and the spatial demands of robot manipulation, and the attempt to build a unified representation across RGB, depth, and point clouds is well motivated.

- The dataset contribution is meaningful. Constructing DROID-3D from the full DROID collection, rather than a small subset, is potentially valuable for the community. The qualitative comparison in **Figure 2** is helpful in conveying the paper’s central motivation: the authors argue that off-the-shelf or weakly processed depth in existing embodied datasets is too noisy for precise manipulation, and the figure makes that claim visually plausible.

- The model design is reasonably coherent. The encoder-decoder setup in **Figure 1** clearly communicates the training pipeline, especially the stochastic masking over modalities and the teacher-student distillation stage. Even though the ingredients are familiar, the overall system is assembled in a way that is easy to understand and aligned with the downstream robotics use case.

- The empirical evaluation is broad. The paper covers 70 simulated tasks and 20 real-world tasks across two robot platforms, which is a stronger evaluation story than many representation-learning-for-robotics papers that stay entirely in simulation.

- The results are generally competitive. In **Table 1**, EmbodiedMAE variants are strong on MetaWorld, especially in multi-modal settings. For example, the point-cloud version reaches the best overall average (77.7), and the RGBD version improves substantially over the naive DINOv2-RGBD baseline (76.2 vs. 54.4 average). This supports the paper’s claim that simply appending 3D input is not enough, and that pretraining for multi-modal fusion matters.

- The real-world section is a genuine strength. **Figure 8** suggests gains are not limited to benchmark simulation, and the contrast between RGB-only and RGBD/PC settings is informative. The xArm results, in particular, support the claim that 3D cues help on tasks where localization precision matters.

- The qualitative reconstructions in **Figure 3** are useful. The recoloring example is a nice sanity check that the model is not just copying pixels blindly, and the cross-modal prediction examples do suggest nontrivial alignment between geometry and appearance.

- The paper does provide some ablations on distillation choices and tests transfer to another policy architecture in **Tables 2, 3, and 4**, which is better than reporting only one backbone and one set of headline numbers.

## Weaknesses
1. **The main source of the gains is not cleanly isolated, and this matters because the paper bundles together several contributions at once.**  
   The paper presents at least four moving parts: a new processed dataset (DROID-3D), a multi-modal MAE objective, stochastic masking via a Dirichlet allocation, and a teacher-student distillation procedure from a ViT-Giant model. Yet the empirical section mostly evaluates the whole package against external baselines. This makes it hard to tell what is actually doing the heavy lifting.  
   Concretely, the ablations in **Section 3.5** and **Table 4** focus only on the distillation stage and do not disentangle whether the improvements come from:  
   (i) having better depth/point cloud data,  
   (ii) using cross-modal masking at all,  
   (iii) using the specific decoder fusion design, or  
   (iv) simply pretraining on in-domain robot data at larger scale than the baselines.  
   This is not a cosmetic issue. The paper’s scientific value depends on whether it teaches the community something specific about multi-modal representation learning, rather than merely showing that “large in-domain pretraining plus good data plus distillation works.”

2. **The comparison to baselines is not fully controlled for pretraining data and compute, which weakens the contribution claim.**  
   The paper repeatedly claims that EmbodiedMAE “outperforms state-of-the-art VFMs in both training efficiency and final performance,” but the comparisons are somewhat apples-to-oranges. DINOv2, SigLIP, R3M, VC-1, SPA, and DP3 differ substantially in pretraining data, objectives, scale, and intended use. EmbodiedMAE is pretrained specifically on DROID-3D, which is highly aligned with the downstream setting. That may be exactly the right design choice, but then the paper should be more careful about attributing gains to architecture rather than domain-matched data.  
   This becomes particularly important in **Figure 6** and **Table 1**, where the performance gaps are used to support fairly broad claims. A stronger comparison would include, for example, a simpler MAE or DINO-style model pretrained on the same DROID-3D data under similar compute, or an RGB-only version trained from scratch on DROID-3D with the same ViT backbone. Without this, the paper’s “state-of-the-art representation” claim feels stronger than the presented evidence supports.

3. **The mathematical formulation in Section 2 is underspecified at several critical places.**  
   The objective in **Equation (1)** is presented as
   \[
   \mathcal{L}_{\mathrm{MAE}} = \mathbb{E}_{(I,D,P)\sim \mathcal{D}, \mathrm{Dir}(\alpha)} \left[\|g(h_I,h)-I_2\|^2 + \|g(h_D,h)-D_2\|^2 + \|g(h_P,h)-P_2\|^2\right].
   \]
   But this hides several implementation choices that are important for correctness and reproducibility:
   - The notation suggests reconstruction of the masked views \(I_2,D_2,P_2\), but the tensor shapes differ substantially across modalities, especially for point clouds grouped by FPS/KNN. The exact target representation for \(P_2\) is not formally defined in the main paper.
   - The sentence after Eq. (1) says \(g_I(h_I,h)\) and \(g_D(h_D,h)\) are \(l_2\)-normalized and \(g_P(h_P,h)\) is group-center normalized, but the corresponding normalization of the targets is only loosely described. Is the loss applied to standardized RGB patches, standardized depth patches, and centered point sets? The current wording is too vague.
   - The masking notation in **Section 2.2** also blurs whether each modality has the same patch count \(L\). For RGB/depth \(L=\frac{HW}{16^2}\), while for point clouds \(L=N\). Yet the masks are introduced as \(m_I,m_D,m_P \in \{0,1\}^L\), which implicitly assumes a shared \(L\). That is notationally inconsistent. A more accurate notation would use \(L_I,L_D,L_P\), with the Dirichlet controlling visible-token counts across modalities under \(\sum_m n_m = n_{\text{visible}}\).  
   These are fixable issues, but they are not trivial. For a multi-modal MAE paper, the exact optimization target and masking mechanics are central, not bookkeeping.

4. **The evidence for “strong cross-modal fusion” is suggestive but overinterpreted.**  
   **Figure 3** is visually interesting, but the conclusions drawn in **Section 3.2** go too far relative to the evidence. In particular, the claim that the recoloring case “suggests EmbodiedMAE has implicitly learned object-level semantic segmentation” is much stronger than what the figure establishes. The example could also be explained by local appearance propagation or texture-context priors, rather than a robust emergent object segmentation ability.  
   If the authors want to make that semantic claim, they should support it with actual quantitative probes, for example object-level correspondence, segmentation transfer, masked region consistency, or at least a broader set of controlled examples. Right now, **Figure 3** is a nice qualitative sanity check, but not enough to support the paper’s stronger interpretation.

5. **Some reported empirical claims are too broad for the granularity of the presented data.**  
   The paper frequently states that EmbodiedMAE “consistently” outperforms baselines, but the tables show a more mixed picture. For example, in **Table 1**, EmbodiedMAE-RGB ties SPA-RGB on average (both 73.0), and on the “Medium” MetaWorld subset it is actually below SPA-RGB (60.4 vs. 62.8). Similarly, on the “Very Hard” subset, EmbodiedMAE-RGBD is below DINOv2-RGBD (61.6 vs. 65.6).  
   None of this is fatal, but the paper should be more precise. The model is often better overall, especially in multi-modal settings, but not uniformly dominant in every configuration. The current phrasing oversells the consistency of the gains.

6. **The real-world evaluation is promising but statistically thin.**  
   The real-world experiments in **Figure 8** are useful, but each task is evaluated with only 10 trials, and the paper reports averages without uncertainty estimates or per-task breakdowns in the main text. On top of that, only 20 demonstrations per task are collected for SO100 and xArm, which makes variance and run sensitivity especially relevant.  
   This matters because the paper uses these experiments to support practical deployment claims. Without confidence intervals, seed variance, or task-level detail in the main paper, it is difficult to judge how stable the observed gains really are. A few successes one way or the other can swing an average noticeably under such small trial counts.

7. **The “training efficiency” claim is not substantiated rigorously enough.**  
   The abstract and introduction emphasize both training efficiency and performance, but the main paper does not provide a clean wall-clock, FLOPs, or pretraining-cost comparison against competing methods. **Figure 6** shows downstream learning curves, which is useful for policy sample efficiency, but that is not the same as representation learning efficiency.  
   In fact, the paper’s own setup involves pretraining a ViT-Giant model, then distilling smaller models, and processing 76K trajectories into 3D representations with nearly 500 hours of preprocessing time. This may still be a good tradeoff, but calling it “training efficient” without a careful accounting is slippery. The paper should distinguish downstream policy learning efficiency from total end-to-end system cost.

8. **The exposition has a number of rough edges and inconsistencies that reduce confidence.**  
   There are several avoidable presentation issues:  
   - In **Table 1**, “EmboodiedMAE” is misspelled.  
   - The paper says the average in **Table 1** is over all tasks, which is good, but the mismatch between per-split numbers and the overall average is not immediately intuitive and could confuse readers.  
   - The notation around the decoder functions in **Section 2.3** shifts between modality-specific outputs \(g_I, g_D, g_P\) and the generic \(g\) in Eq. (1).  
   - The training details in **Section 2.5** and **Table 8** are not fully aligned, for example the learning rate in the main text is \(1.5\mathrm{e}{-4}\) while **Table 8** lists a peak LR of \(3\mathrm{e}{-4}\). This may be explainable as base-vs-peak LR or pretraining-vs-distillation, but the main paper should state that clearly.  
   None of these individually sink the paper, but together they make the presentation feel less polished than it should be for a systems-heavy empirical paper.

## Questions
1. The biggest issue for me is attribution of gains. Can the authors provide a more controlled comparison where the backbone and pretraining data are matched, and only the pretraining objective differs? For example, an RGB-only MAE or DINO-style pretraining on the same DROID-3D subset would help clarify whether the benefit mainly comes from the multi-modal objective versus simply using better in-domain data.

2. Please clarify the exact optimization targets in **Equation (1)**. For each modality, what precisely is reconstructed and normalized? In particular, for the point cloud branch, is the target a centered point group, a token embedding, or raw coordinates after grouping and normalization? A modality-by-modality tensor-shape description would significantly increase confidence.

3. In **Section 2.2**, the masking notation appears to reuse the same \(L\) for all modalities, although the point-cloud token count \(N\) need not match the RGB/depth patch count. Is there a hidden assumption that the token counts are matched, or is this just a notational shortcut? Please specify the exact allocation rule for visible tokens across modalities when token counts differ.

4. The paper attributes semantic implications to **Figure 3**, especially the recoloring example. Do the authors have any quantitative probe to support the “object-level semantic segmentation” interpretation, or should this claim be toned down to “context-aware appearance propagation”?

5. For the real-world results in **Figure 8**, can the authors provide variance across random seeds or at least per-task success rates in the main rebuttal? With only 10 trials per task, uncertainty matters a lot.

6. The paper claims improved training efficiency. Can the authors provide a clearer cost accounting, separating:  
   \[
   \text{3D preprocessing cost} + \text{teacher pretraining cost} + \text{distillation cost} + \text{downstream policy training cost}?
   \]
   Right now, the evidence mainly supports downstream policy efficiency, not necessarily total system efficiency.

7. Since **Table 4** suggests the distillation alignment loss is very important, what happens with a student trained only with \(\mathcal{L}_{\mathrm{Align}}\) and no MAE term across more tasks/modalities? The result at masking ratio \(1.0\) is interesting and seems to imply the student may inherit most benefits from the teacher without needing much reconstruction loss. That deserves a bit more discussion.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
No major ethics concerns are evident from the main paper. The work uses publicly available robot datasets and standard robot manipulation benchmarks, and the paper does not describe human-subject experiments or release of sensitive personal data.

## Soundness Rating
3: good. The overall methodology is plausible and the empirical study is broad, but some claims are stronger than the evidence, and the core objective/masking formulation in the main paper is not specified as cleanly as it should be.

## Presentation Rating
2: fair. The paper is readable and the figures are useful, but there are notable notation gaps, some overclaiming, and several inconsistencies between sections/tables that reduce clarity.

## Contribution Rating
3: good. The combination of DROID-3D plus a unified multi-modal MAE for manipulation is valuable and relevant to ICLR, even if the conceptual step beyond existing MAE-style multi-modal pretraining feels more incremental than the paper’s tone suggests.

## Overall Rating
6: Marginally above the acceptance threshold. But would not mind if paper is rejected. The paper addresses an important problem, introduces a potentially useful dataset resource, and shows broad empirical gains, especially in multi-modal manipulation settings. However, the work does not fully isolate where the gains come from, some central methodological details are underspecified, and several of the claims are broader than the evidence warrants. I lean positive because the empirical scope and practical relevance are strong, but this is not an easy accept.

## Reviewer Confidence
4: confident. I am confident in the assessment and checked the main technical and empirical details carefully, though I still have some uncertainty because several implementation-critical aspects of the objective are not fully specified in the main paper.