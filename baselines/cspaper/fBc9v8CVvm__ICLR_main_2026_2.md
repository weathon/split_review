---
job_id: 6149750f-b959-421b-924f-03e7c29645ae
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: fBc9v8CVvm.pdf
paper: TwinFlow: Realizing One-Step Generation on Large Models with Self-Adversarial Flows
main_score_norm: 0.6
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅ The paper is clearly within ICLR scope, it studies generative models, flow matching, and efficient one-step/few-step sampling for large-scale image generation.

## Minimum Quality
Pass ✅ The submission contains the expected scientific structure, including abstract, introduction, related work, methodology, experiments with quantitative and qualitative results, and conclusion/limitations; while some derivations and explanations are shaky, the paper is complete and provides substantial empirical evidence.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅ I did not find any hidden prompts, suspicious instructions to reviewers, or other manipulative content in the provided paper text and figures.

# Expected Review Outcome:
## Summary
This paper proposes TWINFLOW, a teacher-free and discriminator-free training framework for one-step and few-step generative modeling based on a twin-trajectory construction over an extended time interval \(t \in [-1,1]\). The method introduces a self-adversarial loss on a negative-time “fake” branch and a rectification loss that matches velocity fields between the fake and real branches, then integrates these terms with an any-step base objective. Empirically, the paper reports strong 1-NFE and 2-NFE results on text-to-image generation, including on large multimodal generators such as Qwen-Image-20B, with favorable comparisons to RCGM, sCM, MeanFlow, DMD-style approaches, and SANA-Sprint.

## Strengths
1. The paper targets an important and timely problem. Reducing NFEs to 1 or 2 for large generative models is practically meaningful, and the paper does not frame this as a toy setup. The large-model setting, especially the experiments on Qwen-Image-20B in Section 4.2 and Table 3 on Page 8, makes the contribution relevant beyond small-scale academic benchmarks.

2. The empirical results are strong enough to take seriously. In Table 2 on Page 7, Qwen-Image-TWINFLOW reaches \(0.86/0.90^\dagger\) GenEval and \(86.52\) DPG-Bench at 1-NFE, which is a dramatic improvement over Qwen-Image-RCGM at 1-NFE (\(0.52\), \(59.50\), \(0.30\) on GenEval, DPG-Bench, WISE). This is not a marginal bump, it is the difference between a method that is barely usable at 1 step and one that is plausibly competitive. Table 4 on Page 9 similarly shows the method is competitive on dedicated text-to-image backbones, particularly in the 1-NFE regime where TWINFLOW-0.6B gets \(0.83\) GenEval versus \(0.80\) for RCGM-0.6B and \(0.72\) for SANA-Sprint-0.6B.

3. The scalability argument is one of the paper’s strongest points. Figure 2(b) on Page 3 is a useful, concrete figure rather than decorative marketing. It directly supports the claim that methods requiring auxiliary models are difficult to scale to ultra-large generators, since DMD2 on Qwen-Image-20B is shown as OOM while TWINFLOW remains feasible. Table 3 reinforces this by reporting OOM for raw VSD/DMD/SiD configurations on Qwen-Image-20B. For a paper arguing simplicity and scalability, this systems evidence matters.

4. The paper does a good job of making the qualitative case that the 1-step/2-step outputs are not obviously degenerate. Figure 3 on Page 8 is particularly effective here. It compares Qwen-Image-20B at increasing NFEs against TWINFLOW at 1 and 2 NFEs, and the presented examples do support the claim that TWINFLOW can recover recognizable semantics and useful detail at very low step counts. The visual comparison is not a substitute for quantitative evaluation, but it does align with the reported benchmark gains.

5. The ablation in Figure 4(b) on Page 10 is informative. It shows that adding \(\mathcal{L}_{\mathrm{TwinFlow}}\) improves 1-NFE DPG scores across OpenUni, SANA, and Qwen-Image, with the largest gain on Qwen-Image. This is one of the few places where the paper directly probes whether the proposed term is actually carrying the method, and the answer seems to be yes.

6. Relative to many acceleration papers, the submission does compare against several reasonable baselines across both “with auxiliary models” and “without auxiliary models.” Tables 3 and 4 include sCM, MeanFlow, RCGM, DMD, SiD, and VSD, which gives readers a useful practical picture of where the method sits.

## Weaknesses
1. The theoretical justification is the paper’s weakest part, and it is weaker than the confidence of the prose suggests. The key derivation in Section 3.2, from KL matching in Equation (3) to the practical rectification loss in Equation (9), leaves several nontrivial steps underspecified. In Equation (4) on Page 5, the gradient of \(D_{\mathrm{KL}}(p_{\text{fake}}\|p_{\text{real}})\) is written as if \(\mathbf{x}_t\) is reparameterized through \(\theta\), but the expectations and distributional dependencies are handled loosely. Then in Equation (8), the Jacobian
\[
\frac{\partial \mathbf{x}_{t'}^{\text{fake}}}{\partial \theta}
\]
is simplified through a chain of substitutions ending with a proportionality to
\[
-\frac{\partial \mathbf{F}_\theta(\mathbf{z},0)}{\partial \theta},
\]
but this skips important dependence paths and replaces equality with proportionality exactly where the argument needs to be precise. That would be acceptable as intuition, but the paper presents this as a derivation motivating the final loss in Equation (9). As written, Equation (9) feels more like a heuristic inspired by the KL argument than a principled estimator of the gradient in Equation (6). This matters because the “self-adversarial” story is the conceptual core of the paper.

2. The score-to-velocity relation is not explained carefully enough for such a central identity. Equation (5) on Page 5,
\[
\mathbf{s}(\mathbf{x}_t) = -\frac{\mathbf{x}_t + (1-t)\mathbf{F}_\theta(\mathbf{x}_t,t)}{t},
\]
is imported from the appendix, but in the main paper it is used as the bridge from density matching to velocity matching. The issue is not only that the proof is deferred, it is that the notation around \(\mathbf{F}_\theta\), \(\bm f_\theta\), velocity field, and target times \(r\) changes across Sections 2 and 3. In Section 2, \(\bm{f}(\mathbf{x}_t,r)\) predicts \(\mathbf{x}_r - \mathbf{x}_t\) and under flow matching \(\bm{f}_\theta(\mathbf{x}_t,r)=\mathbf{F}_\theta(\mathbf{x}_t,r)\cdot (t-r)\). But in Section 3, \(\mathbf{F}_\theta(\mathbf{x}_t,t)\) is directly treated as the velocity field, while the implementation notes also say Network\((x_t,t,r)\) implements \(\mathbf{F}_\theta(\mathbf{x}_t,r)\). This makes Equations (5)-(9) harder to parse than they should be. A method paper proposing a new objective should not require readers to reverse-engineer which function is the velocity, which is the displacement, and which arguments are active in each equation.

3. The experimental comparisons are strong but not always cleanly controlled, especially when making broad claims against adversarial or proprietary pipelines. For example, Table 4 on Page 9 reports that TWINFLOW slightly underperforms SANA-Sprint on DPG-Bench at 1-NFE, yet the text in Section 4.3 explains this away by saying the gap is “primarily data-driven” due to SANA-Sprint’s reliance on larger proprietary data. That may be true, but the paper does not provide evidence for this attribution. Once the training data differ, the paper should be much more careful about causal language regarding why one method wins or loses. Similarly, some baselines are reported from literature and some are “tested by ourselves,” indicated by \(\dagger\), but the exact parity of evaluation settings is not always fully transparent in the main paper.

4. Several of the headline comparisons in Table 2 on Page 7 are between very different model families, training datasets, and prompt processing pipelines. The table mixes unified multimodal models, rewritten-prompt settings, RL-enhanced variants, and few-step tuned versions. The result is impressive-looking, but scientifically a bit muddy. For instance, Qwen-Image-TWINFLOW at 1-NFE is compared to Bagel, OmniGen2, MetaQuery-XL, and Qwen-Image-Lightning, but these systems differ in more than inference step count. The paper does acknowledge some prompt rewriting via \( \dagger \), which is good, yet the broader message sometimes slides from “competitive under these benchmark settings” to “better than most multi-step models,” which overstates what Table 2 actually isolates.

5. The ablation coverage is not sufficient for the method’s main design claims. Figure 4(a) only varies the batch split parameter \(\lambda\), and Figure 4(b) only tests adding or removing \(\mathcal{L}_{\mathrm{TwinFlow}}\) as a whole. What is missing is exactly the decomposition needed to understand the method: what happens with only \(\mathcal{L}_{\mathrm{adv}}\), only \(\mathcal{L}_{\mathrm{rectify}}\), positive branch only, negative-time conditioning without fake trajectory regeneration, same noise vs different noise for \(\mathbf{z}\) and \(\mathbf{z}^{\text{fake}}\), and \(N=0/1/2\) in the any-step formulation. Because the method has multiple moving parts, the current ablation leaves the reader unable to tell which component is essential and which is a convenience. Figure 4(b) tells me the package helps; it does not tell me why.

6. The simplicity claim is somewhat overstated because it conflates “no auxiliary model” with “simple training objective.” Table 1 on Page 3 is useful, but it reduces method complexity to counts of auxiliary/frozen models. By that metric TWINFLOW indeed looks attractive. However, the actual training recipe introduces an extended time domain, two trajectory types, a self-generated fake branch, a stop-gradient rectification target, and mixed mini-batches with different \(r\)-sampling rules. This is still operationally complex, just in a different way. I do not think this invalidates the contribution, but the rhetoric should be toned down. “One-model” is fair; “simple” needs more nuance.

7. The paper repeatedly emphasizes “self-adversarial” training, but the adversarial nature is more metaphorical than formal. Equation (2) on Page 4 is just a supervised flow-matching loss on model-generated fake samples at negative time. There is no min-max game, no discriminator, and no explicit divergence maximization/minimization interplay. This matters because the wording may lead readers to infer a closer connection to adversarial training than is actually present. The paper would be stronger if it simply framed this as self-generated hard-negative trajectory training plus velocity rectification, rather than trying to borrow the adversarial label for rhetorical force.

8. Some presentation issues, while not fatal, do affect readability. There are a number of grammatical mistakes and awkward phrasings, for example “minimize of the difference” in the Figure 2 caption on Page 3, “which we collectively name it” in Section 3.3 on Page 6, and several places where notation switches between bold and non-bold forms. Figure 4’s caption says “(a) and (c)” and then refers to “(b)” trained on the same dataset, but the layout is visually busy and the exact axes require effort to decode. This is fixable, but the presentation is not yet at the level of polish I would expect for a paper leaning heavily on a new conceptual framing.

## Questions
1. Can the authors give a cleaner derivation, in the main paper, of how Equation (9) follows from Equations (6) and (8)? In particular, which terms are being ignored, approximated, or treated with stop-gradient, and under what assumptions? A response with the exact optimization target implied by \(d(\cdot,\cdot)\), plus the gradient of Equation (9), would substantially increase my confidence.

2. What is the contribution of each component separately: \(\mathcal{L}_{\mathrm{adv}}\) alone, \(\mathcal{L}_{\mathrm{rectify}}\) alone, and both together? Please provide at least one table on a representative backbone, ideally with 1-NFE and 2-NFE metrics. Right now Figure 4(b) only compares with and without the combined \(\mathcal{L}_{\mathrm{TwinFlow}}\), which is not enough to understand the mechanism.

3. How sensitive is the method to the choice of fake-sample construction \(\mathbf{x}^{\mathrm{fake}} = \mathbf{z} - \mathbf{F}_\theta(\mathbf{z},0)\) and to using a different noise \(\mathbf{z}^{\mathrm{fake}}\) for the fake trajectory? The paper explicitly says \(\mathbf{z}^{\mathrm{fake}}\) “does not need to be the same as \(\mathbf{z}\)” in Section 3.1, but no evidence is provided. This seems central, not incidental.

4. In Table 3, why do DMD and SiD exhibit lower WISE/GenEval despite relatively decent DPG-Bench in some rows, and why do DMD/SiD 1-NFE sometimes not degrade much from 2-NFE? Are these baselines fully converged under the memory-constrained LoRA fake-score setup, or are they handicapped by the implementation compromise? Clarifying this would help assess how much of the gain is due to the proposed method versus practical trainability differences.

5. Could the authors provide failure-case analysis, ideally by prompt category? For example, are the remaining gaps versus the original 100-NFE Qwen-Image concentrated in counting, spatial relation, fine text rendering, or style prompts? Table 5 in the supplement gives some category scores for GenEval, and bringing a concise version of that analysis into the discussion would improve the scientific value.

6. Figure 3 qualitatively suggests that TWINFLOW at 1-2 NFE can rival much larger NFEs of the base model. Can the authors quantify this more directly with a matched-NFE curve on the same backbone, for example GenEval/DPG versus NFE for baseline Qwen-Image and TWINFLOW? That would make the “trajectory straightening” claim much more convincing than isolated image panels.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
The paper focuses on training objectives and efficiency for generative image models, and I did not identify specific ethics issues in the main paper that require separate ethics review beyond the standard concerns associated with text-to-image systems.

## Soundness Rating
3: good. The paper has substantial empirical support and the main practical claims are mostly backed by experiments, but the theoretical motivation around Equations (3) to (9) is not rigorous enough to fully justify the method as derived rather than heuristic.

## Presentation Rating
2: fair. The paper is readable overall and the experimental section is fairly informative, but the notation is inconsistent, several mathematical steps are underspecified, and some writing/figure presentation issues make the core method harder to follow than necessary.

## Contribution Rating
3: good. The large-scale empirical demonstration of 1-step/few-step generation without auxiliary models is valuable and relevant to the ICLR community, even if the conceptual novelty and theoretical articulation are less clean than the paper claims.

## Overall Rating
6: Marginally above the acceptance threshold. But would not mind if paper is rejected. The empirical results, especially on Qwen-Image-20B and in Tables 2 to 4, are strong enough that I lean positive, and the systems/scalability angle is genuinely useful. That said, the paper’s conceptual and mathematical framing is noticeably shakier than the empirical section, and I would like to see a clearer rebuttal on the derivation and component-wise ablations.

## Reviewer Confidence
4: confident. I am confident in the overall assessment and familiar with the relevant literature on few-step diffusion/flow acceleration, though I do think some of the derivational details would benefit from author clarification.