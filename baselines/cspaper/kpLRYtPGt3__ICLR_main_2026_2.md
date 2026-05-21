---
job_id: 334c592d-d3f7-4a12-b4ee-f2ef0b9bf062
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: kpLRYtPGt3.pdf
paper: NEON: Negative Extrapolation from Self-Training Improves Image Generation
main_score_norm: 0.8
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is squarely in scope for ICLR, it proposes a method for improving generative models, includes theoretical analysis of learning dynamics under synthetic self-training, and evaluates across several image generation architectures.

## Minimum Quality
Pass ✅. The submission contains the required scientific components, including abstract, introduction, related-work discussion, methodology, experiments with quantitative and qualitative results, and a conclusion; despite several technical and presentation issues, it clears the minimum bar for a full review rather than desk rejection.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find any hidden prompts, suspicious instructions to automated reviewers, or other manipulative content in the provided paper text.

# Expected Review Outcome:
## Summary
This paper proposes Neon, a simple post-hoc method for improving image generators by first briefly self-training a base model on its own synthetic samples, then reversing that update through a linear parameter extrapolation, $\theta_{\text{Neon}}=(1+w)\theta_r-w\theta_s$. The paper argues theoretically that common mode-seeking samplers induce anti-alignment between synthetic-data and real-data gradients, making negative extrapolation beneficial, and empirically evaluates the idea across diffusion, flow matching, autoregressive, and few-step image generators on CIFAR-10, FFHQ, and ImageNet. The reported results show consistent FID improvements with very small additional compute, including a reported ImageNet-256 FID of 1.02 for xAR-L.

## Strengths
1. The core idea is unusually simple and practically attractive. Algorithm 1 on **Page 4** is about as lightweight as these post-hoc model improvement methods get: synthesize samples once, fine-tune briefly, then do a single linear merge. That low-friction implementation story matters, especially compared with methods that require auxiliary discriminators, likelihood ratios, or inference-time modifications.

2. The paper does a good job connecting a simple recipe to a principled intuition. **Figure 2** on **Page 4** is a strong piece of exposition, it visualizes the central claim that the reverse of the self-training degradation direction can resemble the direction obtained from additional real data. Even though the toy study is not itself decisive evidence, it makes the geometric thesis of the paper very easy to grasp.

3. The empirical scope is broad. The method is tested on diffusion, flow matching, autoregressive, and few-step generators, which is wider architectural coverage than many synthetic-data or post-hoc improvement papers. The results in **Figure 3** (**Page 6**), **Figure 5** (**Page 7**), and **Figure 7** (**Page 8**) all show a fairly consistent pattern: there is usually a modest self-training budget where Neon improves the base model rather than hurting it. That cross-family consistency is one of the strongest aspects of the submission.

4. The compute-efficiency claim is compelling and, based on the paper’s own evidence, largely supported. In **Figure 3**, the best improvements arrive at fairly small synthetic training budgets, and the xAR / IMM curves in **Figures 5 and 7** suggest that the useful direction stabilizes early. If this phenomenon is robust, it is a meaningful practical contribution.

5. The paper goes beyond reporting raw FID and attempts to explain the mechanism. The precision-recall analysis in **Figure 4** (**Page 7**) and **Figure 6** (**Page 8**) is helpful. In particular, **Figure 4** supports the claim that Neon improves recall while trading off some precision, and **Figure 6** makes clear that the interaction between merge weight $w$ and CFG scale $\gamma$ is not cosmetic. This is better than a paper that just drops a leaderboard number and calls it a day.

6. The aggregate comparison in **Table A.1** is useful for contextualizing where Neon is genuinely competitive. It shows that Neon is not merely improving weak baselines, it is competitive with strong post-hoc alternatives and appears to set the best reported ImageNet-256 FID in the table for xAR-L + Neon. I also appreciate that the table does not pretend Neon is uniformly best everywhere, for example FFHQ-64 and ImageNet-512 remain stronger for some alternatives.

## Weaknesses
1. The main theoretical claims are stronger than what the main paper really establishes. The abstract and contributions claim a rigorous proof that mode-seeking samplers create anti-alignment and thereby guarantee the effectiveness of negative extrapolation. In the main text, however, the core guarantee is heavily local and assumption-dependent. **Equation (4)** on **Page 5** gives only a local Taylor expansion around $\theta_r$, and **Theorem 1** requires small $\|\varepsilon\|_{H_d}$, bounded preconditioned geometry, and favorable bias terms $(\eta_0,\eta_1,\cos\varphi)$. For diffusion and flow models, the key step is pushed into the appendix and relies on an additional curvature-density coupling assumption (A-MONO in Appendix B.7), which is not stated in the main paper when the universality claim is made. That matters because the paper’s marketing line is “this works because common samplers induce anti-alignment,” while the main-paper theorem really says “under a particular local expansion and sampler-bias geometry, a sufficient condition yields anti-alignment.” Those are not the same strength of statement.

2. There are several notation and exposition inconsistencies in the core technical sections, and they are not trivial cosmetic issues because they undermine confidence in a theory-heavy paper. A few examples:
   - In **Equation (5)** on **Page 5**, the sampler notation suddenly becomes $q_{\theta_r,n}$, whereas earlier the paper defines $q_{\theta,\kappa}$; that looks like an indexing error.
   - In **Section 4** on **Page 6**, the text says “starting from a public checkpoint $G_{\theta_s}$,” but throughout the method the base model should be $G_{\theta_r}$.
   - On **Page 9**, the discussion of model quality refers to the condition $\|\varepsilon\|_F$ being small, but the main theory is written in the $H_d$-geometry, $\|\varepsilon\|_{H_d}$.
   - The caption of **Figure 4** on **Page 7** appears broken: it says both $w=-1$ and $w=0$ correspond to $\theta_{\mathrm{Neon}}=\theta_*$, which cannot be right and conflicts with the text around it.
   
   For a paper that leans heavily on equations and geometric reasoning, this kind of sloppiness is not harmless.

3. The experimental story does not cleanly isolate how much of the gain comes from Neon itself versus post-hoc retuning of inference hyperparameters. This is especially clear in the autoregressive and IMM sections. On **Page 7**, the paper says evaluation jointly optimizes both merge weight $w$ and CFG scale $\gamma$, and **Figure 6** on **Page 8** explicitly argues that joint tuning is “crucial.” But then the comparison that matters is not only base model vs base+Neon, it is also “base model with re-optimized $\gamma$” vs “Neon with re-optimized $(w,\gamma)$”, and similarly “self-trained checkpoint with re-optimized $\gamma$” vs Neon. The paper does not report this decomposition clearly enough. Since $\gamma$ alone can strongly alter the precision-recall trade-off, some of the reported FID gain may be coming from retuning the sampler after weight modification rather than from the specific negative extrapolation principle.

4. The paper is missing a set of simple but important baselines that would help establish that the benefit is specific to the proposed degradation direction rather than generic weight extrapolation. For example, I would have liked to see comparisons to:
   - extrapolating along a standard late-training checkpoint direction from the original training run,
   - interpolation / extrapolation between neighboring checkpoints without any synthetic self-training,
   - a generic one-step “negative learning rate” update along some unrelated or random synthetic batch direction,
   - EMA/SWA-style or checkpoint-averaging baselines where applicable.
   
   Right now, the evidence shows that “this particular direction found by short self-training can be useful,” but it does not fully rule out the simpler explanation that many mildly improving extrapolation directions exist in these pretrained generators. Given how simple the final rule is, this baseline family feels important.

5. The empirical results are broad, but the paper is thin on robustness statistics. Almost every claim is reported as a best FID after searching over $w$ and sometimes $\gamma$, yet there are no error bars, confidence intervals, or seed-to-seed variability estimates in the main paper. This especially matters for claims like “works effectively with as few as 1k synthetic samples” and for the tiny compute-overhead regime, where the outcome could be sensitive to noise in fine-tuning or evaluation. **Figure 3** and **Figure 5** present smooth curves with multiple settings, but without any uncertainty it is hard to judge how stable the gains really are. This is not fatal, but it weakens the strength of the empirical case.

6. Some of the strongest claims in the contribution list are supported by relatively narrow evidence. The transfer claim [C5] is based mainly on **Figure 8** on **Page 9**, where one target model, EDM-VP on CIFAR-10, is improved using synthetic data from two other architectures. That is an interesting proof of concept, but “the degradation signal is transferable” reads broader than what is actually demonstrated in the main paper. Similarly, the claim that Neon does not require a near-optimal base model, based on **Figure 9**, is suggestive, but still only shown for one architecture and one dataset.

7. The comparison framing in **Table A.1** should be read carefully. The table is helpful, but it also mixes very different model families, different numbers of function evaluations, and different kinds of post-hoc methods. That is fine for context, but some of the prose around it occasionally drifts toward a stronger “state-of-the-art” framing than the table fully justifies across all settings. For instance, on FFHQ-64 and ImageNet-512 the paper is clearly competitive rather than best. I do not object to the ImageNet-256 claim, but the broader tone could be more measured.

8. The theorem-to-practice bridge is still somewhat loose. In the theory, the synthetic distribution is frozen as $q_{\theta_r,\kappa}$ and the analysis is local in a population-risk sense. In practice, the method uses finite synthetic datasets, original training recipes, learning-rate schedules, and checkpoint selection after tuning. The appendix does discuss finite-sample effects, but from the main paper alone it is still not obvious when the practical recipe should fail, beyond the generic statement about diversity-seeking samplers. I would have liked a more explicit discussion of failure modes in the main text, especially since **Figure 3** already hints at non-monotonic behavior in $|\mathcal{S}|$ and training budget.

## Questions
1. Can the authors disentangle the gain from negative extrapolation itself versus inference retuning? Concretely, for the autoregressive and IMM results, please report:
   - base model with re-optimized $\gamma$ only,
   - self-trained model $\theta_s$ with re-optimized $\gamma$,
   - Neon with fixed original $\gamma$,
   - Neon with jointly optimized $(w,\gamma)$.
   
   This would make **Figure 6** much more informative scientifically, rather than only operationally.

2. Can the authors add or at least discuss simple extrapolation baselines? In particular, does extrapolating along ordinary training-checkpoint directions, or along synthetic directions from unrelated / random samples, produce similar gains? A clear negative result there would substantially increase my confidence that the effect is genuinely tied to the paper’s anti-alignment mechanism.

3. Please clarify the exact scope of the theoretical claims in the main text. For diffusion and flow models, is the claimed anti-alignment result contingent on the curvature-density coupling assumption from the appendix? If yes, that assumption should be surfaced explicitly in Section 3.1 rather than hidden behind a broad universality claim.

4. Can the authors provide some estimate of variance across seeds, at least for one diffusion model and one autoregressive model? Even a small table showing mean $\pm$ std for the best setting in **Figure 3** and **Figure 5** would help assess robustness.

5. Please correct the technical inconsistencies and typos around **Figure 4**, **Equation (5)**, the $\theta_r/\theta_s$ mismatch in Section 4, and the norm mismatch on **Page 9**. These are easy to fix, but in the current form they distract from an otherwise strong paper.

6. For the transfer result in **Figure 8**, did the authors try the reverse directions as well, for example improving flow or IMM from EDM-generated samples? If those results are weaker or fail, that would still be valuable because it would help define the limits of transferability.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
The paper studies image generation on standard public benchmarks and does not raise a specific ethics concern beyond the generic misuse risks shared by most image-generation methods. Those risks are acknowledged briefly in the ethics statement, but I do not see a conference-level ethics flag that is uniquely triggered by this submission.

## Soundness Rating
3: good. The central empirical claims are supported reasonably well across multiple architectures, and the theoretical story is meaningful, but several assumptions are stronger and more local than the paper’s presentation suggests, and some key ablations are still missing.

## Presentation Rating
3: good. The paper is generally well organized and easy to follow, with strong motivating figures such as **Figure 2**, but there are enough notation inconsistencies, caption errors, and theorem-presentation gaps that I cannot rate it higher.

## Contribution Rating
4: excellent. Despite my criticisms, this is a meaningful contribution: the method is simple, broadly applicable within image generation, empirically strong, and conceptually interesting in how it turns self-training degradation into a useful signal.

## Overall Rating
8: Accept, good paper (poster). I have real reservations about overclaimed theory and incomplete baseline isolation, but the combination of simplicity, breadth of empirical evidence, and practical effectiveness makes this a strong contribution overall.

## Reviewer Confidence
4: confident. I am comfortable with the overall assessment and checked the main derivations and experimental claims carefully, though some appendix-level technical details would still benefit from author clarification.