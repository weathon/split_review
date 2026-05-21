---
job_id: 62e6b278-af70-4652-8147-a3a6db9c90df
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: R8y089OGoo.pdf
paper: Dichotomous Diffusion Policy Optimization
main_score_norm: 0.6
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly in scope for ICLR, centered on reinforcement learning, diffusion/generative policies, offline and offline-to-online RL, and applications to robotics and autonomous driving.

## Minimum Quality
Pass ✅. The submission contains the expected scientific structure, including abstract, introduction, methods, experiments, quantitative results, related work, and conclusion. While there are notable clarity and methodological gaps, the paper presents a non-trivial technical idea with substantial empirical evaluation, so it does not fall below desk-rejection quality.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find hidden prompts, suspicious instructions targeting automated reviewers, or other manipulative content in the provided paper text.

# Expected Review Outcome:
## Summary
This paper proposes DIPOLE, a reinforcement-learning method for diffusion or flow-based policy optimization built from a modified KL-regularized objective. The key idea is to replace the unstable exponential reweighting in standard KL-regularized policy extraction with a decomposition into two bounded sigmoid-weighted policies, a positive policy favoring high-value actions and a negative policy favoring low-value actions, and then combine their scores at inference time in a classifier-free-guidance-like manner. The method is evaluated on offline and offline-to-online RL benchmarks, ExORL and OGBench, and is also scaled to a large vision-language-action model for autonomous driving on NAVSIM.

## Strengths
1. The paper tackles a real and timely problem. RL fine-tuning for diffusion policies is indeed difficult because direct backpropagation through denoising is noisy and expensive, while likelihood-based policy gradient approaches for diffusion often rely on approximations that become awkward in practice. This is a meaningful target for ICLR.

2. The central idea is conceptually appealing. The decomposition from an exponential reweighting into dichotomous sigmoid-weighted components gives an intuitive way to separate “move toward good actions” and “move away from bad actions.” In that sense, the paper does more than just stack existing tricks, it reframes KL-regularized extraction into a guidance-style construction that is easy to understand at a high level.

3. The connection to classifier-free guidance is a nice interpretive bridge. In particular, **Equation (10)** provides a simple score-combination rule,
\[
\nabla_a \log \pi^\star(a|s) = (1+\omega)\nabla_a \log \pi^+(a|s) - \omega \nabla_a \log \pi^-(a|s),
\]
which makes the proposed inference mechanism easy to implement in diffusion-policy pipelines. This is one of the cleaner parts of the paper.

4. The empirical scope is broad. The paper reports results on 39 offline RL tasks across ExORL and OGBench, includes offline-to-online fine-tuning on OGBench, and adds a large-scale autonomous driving experiment on NAVSIM. That breadth is appreciable and gives the work practical relevance beyond a single benchmark family.

5. Some of the tabulated results are genuinely strong. In **Table 1**, DIPOLE improves substantially over Gaussian baselines and typically beats prior diffusion/flow baselines on ExORL. Examples like Walker-stand, Walker-walk, Quadruped-walk, and Cheetah-run-backward are not tiny gains. Likewise, in **Table 2**, DIPOLE is best on several OGBench categories, especially cube-double-play and scene-play, where the gains over prior methods are meaningful rather than cosmetic.

6. The autonomous driving section is ambitious and potentially impactful. In **Table 4**, the NAVSIM results suggest that the method can scale to a 1B-parameter VLA setting and improve over the imitation-pretrained DP-VLA baseline. That kind of scaling story is interesting for the community.

7. **Figure 1** is effective as a high-level illustration. It communicates the intended contrast between unstable exponential weighting and the proposed dichotomous extraction, and it also helps motivate the controllability via the greediness parameter \(\omega\). For a paper with a somewhat abstract derivation, that visual does useful explanatory work.

8. **Figure 2** is also helpful qualitatively. The overlaid NAVSIM trajectories make the claimed behavioral change more concrete: the DIPOLE-finetuned model appears to correct trajectories in cases where the imitation-pretrained model drifts into unsafe or off-road behavior. Qualitative evidence does not replace controlled analysis, but here it supports the practical story told by **Table 4**.

## Weaknesses
1. The theoretical derivation is not as clean as the paper presents it, and the optimization over \(d^\pi\) is handled too casually.  
   The objective in **Equation (5)** depends on the visitation distribution \(d^\pi(s)\), yet the derivation of **Theorem 1** and the appendix proof effectively optimize pointwise in \(\pi(a|s)\) as if \(d^\pi\) were fixed. This is a common shortcut in KL-regularized RL derivations when one is really solving a per-state policy improvement subproblem, but that distinction matters. As written, the theorem is phrased as the optimal solution for Eq. (5), not for a local greedy update with fixed state distribution. The appendix proof on **Pages 15–16** includes \(d^\pi(s)\) in the Lagrangian and then differentiates with respect to \(\pi(a|s)\) without accounting for the dependence of \(d^\pi\) on \(\pi\). That is not a minor stylistic issue, it changes what is actually being optimized and weakens the claimed formal justification.

2. The proof itself contains notation and KKT inconsistencies that reduce confidence in the mathematical presentation.  
   In the appendix proof of **Theorem 1** on **Page 15**, the derivative in **Equation (13)** and the resulting expression in **Equation (14)** are not written carefully. In **Equation (14)**, the factor
\[
\exp\left(\omega\beta\frac{\alpha_s+\gamma_{s,a}}{d^\pi(s)} - 1 - \log Z(s)\right)
\]
appears, which is odd because the Lagrange multipliers are introduced outside the \(d^\pi(s)\)-weighted term in **Equation (12)**, so dividing by \(d^\pi(s)\) in that way is not justified from the displayed Lagrangian. Also, if nonnegativity constraints are active, complementary slackness conditions should be discussed, yet the proof simply jumps to proportionality on the support of \(\mu\). The final result may be intuitively plausible, but the written derivation does not meet the bar implied by the theorem statement.

3. The key sampling claim is only approximately implemented, and the approximation error is largely brushed aside.  
   The main text leans heavily on **Equation (10)** to justify inference by linearly combining the two policies’ scores. However, the appendix itself acknowledges on **Pages 15–16** that the exact intermediate score along the diffusion path generally requires a non-linear correction term, given by **Equations (17)** and **(18)**, and that the practical rule
\[
\epsilon_t^\star(a|s)\approx (1+\omega)\epsilon_t^+(a|s)-\omega \epsilon_t^-(a|s)
\]
in **Equation (19)** is only an approximation, especially motivated when \(\omega\) is relatively small. This creates a gap between the theory and what is actually run. The paper then markets “perfect controllability” in the abstract and introduction, which is too strong given that the implemented guidance is approximate away from \(t=0\). This matters because the controllability story is one of the main selling points.

4. The practical method introduces additional ad hoc ingredients that are not integrated into the theory.  
   In **Appendix D.2, Page 18**, the weighting is modified from \(\sigma(\beta G(s,a))\) to \(\sigma(\beta G(s,a)+k)\) with a task-specific shift \(k\). This is not a minor engineering footnote, because changing the argument of the sigmoid changes the implied positive/negative partition and the extracted policy family. Yet the main method section never develops a corresponding objective or theorem for the shifted form. So the paper’s clean theoretical picture is not fully the method that is actually evaluated. The same issue appears with rejection sampling in **Equation (20)** on **Page 18**, which is important in the final ExORL performance but is not really part of the core derivation.

5. The empirical attribution is weaker than it should be, because the paper does not sufficiently isolate what is driving the gains.  
   The main claim is that dichotomous decomposition yields better stability and greediness than exponential weighting or prior CFG-style methods. But the paper does not include a direct main-paper comparison against the most obvious ablation: a single-policy sigmoid-weighted regression without dichotomous decomposition, or a clipped/normalized exponential-weighted regression under the same architecture and value estimator. Without that, it is hard to know whether the gains come from the two-policy construction itself, from the shift parameter \(k\), from rejection sampling, from using a strong flow-policy backbone, or from tuning \(\beta,\omega,N,\tau\) per task. The appendix ablations are mentioned, but the main paper leaves the causal story underdetermined.

6. The comparison tables are strong in places, but they are also more mixed than the narrative suggests.  
   In **Table 2**, DIPOLE is not uniformly best. On humanoidmaze-large-navigate, IFQL is better in aggregate (11 vs 6), and on antsoccer-arena-navigate, FQL slightly exceeds DIPOLE (60 vs 57). The paper says “best or near-best,” which is fair, but some of the prose around greedy extraction reads more sweeping than the evidence supports. Similarly, **Table 3** shows offline-to-online results that are competitive rather than clearly dominant. DIPOLE wins on humanoidmaze-m and antsoccer-arena, but on cube-double FQL slightly edges it after online tuning, and on scene several methods reach 100. This is not a fatal issue, but the paper would benefit from a more measured interpretation of where the method helps most.

7. The NAVSIM experiment is interesting but scientifically less clean than the benchmark sections.  
   The use of “navtest” training, described on **Pages 8 and 20–21**, is unusual enough that it needs more careful framing. The paper says this variant is meant for scenarios where RL can be applied without ground-truth supervision, but training on the test split, even without labels, makes the evaluation setting harder to interpret. The resulting gain in **Table 4** is large, but the protocol is no longer directly comparable to standard train/test generalization claims. Also, the comparison against DPPO is only reported for navtest, not symmetrically for navtrain, which makes the head-to-head comparison incomplete.

8. The paper claims training stability, but the evidence for stability is thinner than the rhetoric.  
   A central motivation is that exponential weighting causes instability and loss domination by a few large-weight samples, while the proposed sigmoid decomposition is stable. Yet the main paper does not provide direct optimization diagnostics such as loss curves, gradient norms, weight distributions, or failure rates across seeds. **Figure 6** in the appendix shows offline-to-online learning curves, but that is not the same as demonstrating that the proposed bounded weights solve the claimed optimization pathology. Since “stable” is in effect part of the method’s thesis, the paper should show it more directly.

9. The notation and exposition have several rough edges that make the method harder to verify than necessary.  
   There are inconsistencies between \(w\) and \(\omega\), for example **Equation (10)** introduces \(\omega\), while the practical reverse-process formula on **Page 5** uses \(\tilde{\epsilon}=(1+w)\epsilon^+ - w\epsilon^-\). Algorithm 2 on **Page 16** also uses \(w\). The loss in **Equation (4)** is labeled \(\mathcal{L}_{\epsilon s}\), which looks like a typo. There are also several grammar issues and awkward phrases throughout. None of these alone is devastating, but together they make an already subtle paper harder to audit.

10. The paper’s relationship to prior work is only partially clarified.  
   The paper compares to CFGRL and mentions similarity, but the distinction could be drawn more sharply. In **Section 3.2**, the statement that CFGRL “lacks theoretical backing” is a bit too breezy relative to the paper’s own incomplete derivation. More importantly, the paper would benefit from a clearer positioning against other diffusion-policy optimization approaches that also aim to improve stability or value-conditioning, especially in offline RL. Right now, the paper’s empirical and conceptual niche is understandable, but not fully pinned down.

## Questions
1. Can the authors clarify the exact status of **Theorem 1**? Is it intended as the optimizer of the full RL objective in **Equation (5)**, or of a per-state policy improvement subproblem with fixed \(d^\pi\)? A precise restatement would substantially increase my confidence, because the current proof seems to ignore the dependence of \(d^\pi\) on \(\pi\).

2. Relatedly, can the authors provide a corrected derivation of **Equations (13)–(15)** in the appendix? In particular, please explain the appearance of the \(1/d^\pi(s)\) factor in **Equation (14)** and how the KKT conditions are handled. If the theorem is only meant up to proportionality on the support of \(\mu\), say so clearly and derive it cleanly.

3. The practical algorithm uses the approximate score combination in **Equation (19)**, while **Equations (17)–(18)** suggest a non-linear correction is needed in general. How large is the approximation error as a function of \(\omega\)? A rebuttal with either empirical sensitivity results or a clearer statement of the approximation regime would help.

4. The paper adds a shift parameter \(k\) in **Appendix D.2** and tunes it per task in **Table 6**. Can the authors justify this modification more formally? Is there an objective corresponding to \(\sigma(\beta G + k)\), or is this purely heuristic? It would be useful to know how much of the reported gain depends on this shift.

5. Can the authors provide a direct ablation against a one-policy sigmoid-weighted baseline, and against standard exponential weighting with clipping/normalization, under the same architecture and value learner? This would better isolate whether the benefit comes specifically from dichotomous decomposition.

6. For **Table 3**, how sensitive are the online results to \(\omega\) and the number of rejection samples \(N\)? Since the paper emphasizes controllable greediness, a concrete sensitivity table or plot in the rebuttal would be valuable.

7. For the NAVSIM setting, please clarify how to interpret the “navtest” training protocol in relation to generalization. Is it best viewed as an adaptation scenario rather than a standard held-out test evaluation? A more careful statement would avoid confusion.

8. Since stability is a key selling point, can the authors show direct evidence such as variance across seeds during training, gradient norm statistics, or weight histograms comparing \(\exp(\beta G)\) versus \(\sigma(\beta G)\) and \(1-\sigma(\beta G)\)? That would make the central argument much more convincing.

## Flag For Ethics Review
- Yes, Privacy, security and safety  
- Yes, Potentially harmful insights, methodologies and applications

## Details Of Ethics Concerns
The autonomous driving component introduces safety-relevant deployment implications. In **Section 4.2** and **Table 4**, the method is evaluated for end-to-end driving and discussed in terms of preventing collisions and improving driving behavior. While the benchmark is simulation-based, work of this kind can influence real-world driving systems, so safety, robustness, and failure analysis deserve careful treatment. I do not see a major ethics violation in the paper itself, but the application domain is safety-critical enough that it warrants ethics attention.

## Soundness Rating
3: good. The core idea is plausible and the experiments are substantial, but the mathematical derivation and theory-to-practice alignment are not fully rigorous as written.

## Presentation Rating
3: good. The paper is generally readable and well organized, and the figures/tables are informative, but there are noticeable notation inconsistencies, some over-strong claims, and several places where the exposition should be more precise.

## Contribution Rating
3: good. The dichotomous decomposition and guidance-style policy extraction are useful contributions, and the empirical results make the paper relevant to the ICLR community, though the novelty is not so overwhelming that I would rate it higher.

## Overall Rating
6: Marginally above the acceptance threshold. But would not mind if paper is rejected. The paper has a solid core idea, strong empirical breadth, and enough positive evidence to merit serious consideration, but the theory is presented more confidently than it is actually supported, and the experimental story still leaves some attribution questions open.

## Reviewer Confidence
4: confident. I am confident in my assessment, though not absolutely certain. I am familiar with RL and diffusion-policy optimization, and I checked the main equations and empirical claims carefully, but some implementation details and benchmark-specific nuances could still benefit from author clarification.