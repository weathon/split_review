---
job_id: c7389cd6-2138-4b2e-b85b-14ecc205b4d9
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: rI2Fa13fUL.pdf
paper: Offline Reinforcement Learning with Generative Trajectory Policies
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, combining reinforcement learning and generative modeling, with a focus on offline RL and continuous-time generative policies.

## Minimum Quality
Pass ✅. The paper contains the expected core sections, presents a coherent method with mathematical formulation and experiments, and although I have notable concerns about novelty positioning, theoretical precision, and experimental completeness, these do not rise to the level of a desk rejection.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not detect hidden prompts, suspicious reviewer-targeting instructions, or other manipulative content in the provided paper text or figures.

# Expected Review Outcome:
## Summary
This paper proposes Generative Trajectory Policies (GTP), an offline RL policy class that frames diffusion, flow matching, consistency models, and related approaches under a unified ODE solution-map perspective. Building on this view, the method learns a state-conditioned flow map for actions and introduces two practical ingredients for offline RL, a closed-form score approximation for stable and efficient training, and an advantage-weighted generative objective for policy improvement. The empirical evaluation on D4RL reports strong behavior cloning and offline RL performance, particularly on AntMaze tasks.

## Strengths
1. The paper has a clear high-level motivation and addresses a real issue in generative offline RL, namely the tension between expressive but slow iterative policies and fast but weaker few-step alternatives. This is a relevant problem for ICLR.

2. The unifying ODE perspective is useful as an organizing lens. Sections 3.1 to 3.4 give a reasonably coherent story connecting diffusion, consistency models, CTMs, shortcut models, and mean flows through the flow map \(\Phi(\mathbf{x}_t,t,s)\). Even if parts of this unification are somewhat conceptual rather than deeply new, it helps structure the design space.

3. The empirical results are strong on standard benchmarks. In **Table 1** on Page 9, GTP-BC is competitive or best on most Gym tasks and shows especially large gains on AntMaze, for example \(85.0\) on antmaze-md and \(74.4\) on antmaze-mp, substantially above D-BC and C-BC. In **Table 2** on Page 10, the full GTP method achieves the highest average on Gym and a very strong AntMaze average of \(80.6\), with particularly strong results on antmaze-u, antmaze-md, and antmaze-ld. These are meaningful empirical strengths.

4. The paper does include some ablation evidence rather than only headline numbers. **Table 3** on Page 10 provides a direct comparison for the score approximation and the proposed value-guided objective. Even though the ablation is narrow, it does support the claim that the proposed training formulation is more stable than a naive linear \(Q\)-term combination.

5. **Figure 2** is one of the stronger figures in the paper. Panel (a) clearly communicates the intended role of the score approximation, replacing a potentially unstable self-supervised trajectory with a more stable teacher-like analytical approximation. Panel (b) also gives an intuitive picture for the value-guided objective, namely moving the BC trajectory toward a higher-value region while staying near the data. For a paper that mixes ODE language and RL objectives, this figure genuinely helps readability.

6. **Figure 1** also serves the exposition reasonably well. It visually contrasts iterative solvers with direct jumps via a learned flow map, which matches the narrative in Section 3.2. The figure supports the paper’s central intuition that learning a solution map may reduce iterative sampling burden.

7. The presentation is generally readable, and the method section is organized in a way that makes it possible to follow the pipeline from unified formulation to practical actor-critic training. Algorithm 1 on Page 8 is simple and helpful.

## Weaknesses
1. **The central methodological novelty is not as crisp as the paper claims, especially relative to CTMs and other solution-map learning methods already discussed by the authors themselves.**  
   This issue appears throughout **Sections 3.2 to 3.4** and becomes most visible on **Pages 4 to 5**, where the paper introduces \(\phi(\mathbf{x}_t,t,s)\), the instantaneous anchor, and the trajectory consistency loss, and then immediately states in **Section 3.4** that CTMs “instantiate both core components of our unified framework.” Once the paper itself acknowledges that CTMs already parameterize \(\Phi(\mathbf{x}_t,t,s)\) and combine trajectory consistency with an auxiliary diffusion-style local loss, the burden is on the authors to explain very precisely what is new in GTP beyond adapting this family to offline RL with advantage weighting and the score approximation trick. Right now, that distinction remains blurry.  
   Why this matters: if the main algorithmic content is largely “CTM-like trajectory learning + standard advantage reweighting + an analytical teacher substitution,” then the paper is closer to a careful integration paper than to a distinctly new policy class. That can still be publishable, but it should be claimed and evaluated more honestly. As written, the paper repeatedly suggests a broader conceptual leap than is fully substantiated.

2. **The mathematical definition of the surrogate field in Theorem 1 contains a clear typo or inconsistency, and that is not a cosmetic issue because it sits at the core of the paper’s main practical claim.**  
   On **Page 6**, **Theorem 1** defines
   \[
   f^{\star}(\mathbf{x}_t,t):=\frac{\mathbf{x}_t-\mathbb{E}[\mathbf{x}\mid \mathbf{x}_t]}{\tilde f},
   \]
   which is dimensionally wrong and inconsistent with the appendix, where **Equation (32)** on **Page 19** gives the expected form
   \[
   f^{\star}(\mathbf{x}_t,t)=\frac{\mathbf{x}_t-\mathbb{E}[\mathbf{x}\mid \mathbf{x}_t]}{t}.
   \]
   This is not a minor notational blemish because Theorem 1 is supposed to justify replacing the learned or ideal field with the surrogate \(\tilde f(\mathbf{x}_t,t)= (\mathbf{x}_t-\mathbf{x})/t\). A malformed definition in the theorem statement undermines confidence that the main result was checked carefully.  
   Why this matters: the theorem is being used to support the entire score-approximation training scheme in Section 4.1. If the theorem statement is sloppy at this level, reviewers are left wondering whether the assumptions, convergence order, and objective comparison were all verified with equal care.

3. **The theoretical support for the score approximation is weaker than advertised, and the asymptotic claim does not really justify the practical replacement made in the algorithm.**  
   The paper’s main formal claim is **Equation (10)** on **Page 6**, stating
   \[
   \left|\mathcal{L}_{\mathrm{prac}}(\theta)-\mathcal{L}_{\mathrm{ideal}}(\theta)\right|=O(h^p).
   \]
   But several gaps remain:
   - The theorem is asymptotic in solver step size \(h\), while the practical implementation in **Remark 1** effectively eliminates the solver and directly uses \( \mathbf{x}_u=\mathbf{x}+u\mathbf{z} \) in **Equation (11)**. The paper jumps from “a solver-based practical objective differs by \(O(h^p)\)” to “we can use one-step perturbations and remove multi-step integration” without really quantifying the resulting approximation gap in the actual algorithm used.
   - The proof relies on Lipschitz assumptions and bounded second moments of solver states, but these conditions are not discussed in the RL setting where the network is state-conditioned and action distributions may be clipped or bounded by the environment.
   - The result compares two objectives in expectation, not the learned policies, critic stability, or offline RL performance. This is a much weaker statement than the prose around **Remark 2** suggests.
   Why this matters: the paper repeatedly presents the score approximation as “theoretically principled,” but the theory mainly says that under standard numerical assumptions, two solver-based losses are close. That does not fully support the stronger practical narrative that the approximation yields stable and correct trajectory supervision in actor-critic offline RL.

4. **The derivation and practical implementation of the value-guided objective are under-specified and partly over-claimed.**  
   **Theorem 2** on **Page 7** states that the optimal KL-regularized solution is
   \[
   \pi^*(a|s)\propto \pi_{\mathrm{BC}}(a|s)\exp(\eta A(s,a)),
   \]
   and then claims that training a generative policy is equivalent to solving the weighted generative objective in **Equation (13)**. This derivation is broadly standard, but the actual implemented weight in **Equation (14)** truncates negative advantages and normalizes by \(\mathrm{std}(A)\):
   \[
   w(s,a)=\exp\left(\eta\cdot \frac{\max(0,A(s,a))}{\mathrm{std}(A)+\epsilon}\right).
   \]
   This is no longer the same objective. The paper treats the practical heuristic as if it were a straightforward numerically stable implementation of the theorem, but clipping all negative advantages to zero materially changes the target distribution. Samples with very negative advantage are no longer downweighted relative to neutral ones; they all get weight \(1\).  
   Why this matters: the paper’s “theoretically correct way” claim is too strong. In practice, the algorithm uses a different objective, and the gap between theorem and implementation is exactly where offline RL methods often succeed or fail. This needs a more honest treatment.

5. **The actor-critic formulation leaves important implementation details ambiguous, and this affects reproducibility and evaluation fairness.**  
   In **Section 4.3** on **Pages 7 to 8**, several key details are not fully specified in the main paper:
   - How exactly is \(A(s,a)\) computed in practice? Is \(V(s)\) derived via a separate network, via \(\mathbb{E}_{a\sim\pi}[Q(s,a)]\), via expectile regression, or simply through a baseline from the batch? The theorem uses an advantage, but the implementation details in the main paper are missing.
   - What distribution is used for sampling \(t,u,\tau\) in **Equations (17)-(18)**? The time sampling scheme can materially change training.
   - Since actions in D4RL continuous control are bounded, how is the Gaussian noising \(a_t=a+t z\) handled near action limits? Is there clipping, tanh-squashing, or rescaling?
   - The critic target in **Equation (16)** uses \(\pi_{\theta'}(s')\), but the paper does not discuss whether multiple action samples are drawn, whether there is any conservative regularization, or how OOD action generation is controlled.
   Why this matters: for offline RL, these details are not secondary. They directly affect stability, extrapolation error, and the fairness of baseline comparisons.

6. **The experiments are strong but not sufficiently isolating the claimed contributions, especially the “GTP policy class” versus generic offline RL weighting tricks.**  
   The paper claims three things at once: a new policy parameterization, a score-approximation training trick, and a value-guided actor update. However, the ablation support is quite limited:
   - **Table 3** on **Page 10** only evaluates one environment, hopper-medium-expert-v2. That is too narrow for such broad claims about stability and efficiency.
   - The “linear Q-term” baseline is intentionally weak and brittle, but there is no comparison to other stronger value-guided generative objectives already common in offline RL, beyond end-to-end benchmark tables.
   - There is no ablation removing the trajectory consistency loss or the instantaneous flow loss separately in the main paper, so it remains unclear whether both components are necessary.
   - There is no controlled experiment comparing the same backbone with and without learning the full map \(\Phi(\cdot,t,s)\), which would be the cleanest test of the claimed benefit of the trajectory-policy paradigm itself.
   Why this matters: a paper centered on a new policy class should show which gains come from the class itself, rather than from a better actor-weighting scheme or from training stabilization heuristics.

7. **The benchmark comparisons, while impressive, raise some fairness and positioning concerns.**  
   Looking at **Table 1** and **Table 2**, the method is compared against a mix of methods from different eras and sometimes heterogeneous training setups. But the paper does not explain whether compute budgets, network sizes, sampling steps, and tuning effort were matched. For example, on **Page 8** the paper says diffusion and GTP use \(K=5\) sampling steps while consistency uses \(K=2\). That is a reasonable default, but it is not enough to conclude that GTP resolves the expressiveness-efficiency trade-off unless the training and inference comparisons are also normalized.  
   Why this matters: stronger benchmark numbers are valuable, but offline RL is notoriously sensitive to hyperparameters and implementation details. Without tighter fairness controls or same-codebase reimplementations in the main paper, the SOTA claim should be treated with some caution.

8. **The efficiency claim is under-supported in the main paper.**  
   The title and abstract place substantial weight on bridging the speed-performance gap between diffusion and consistency policies. However, in the main paper, the evidence is modest:
   - **Table 3** gives training time only on one task.
   - The more direct inference-time comparison appears only later in supplementary material, and even there the evidence is on a single environment and reports only milliseconds without performance in the same table.
   - **Figure 1** is conceptually helpful, but it visualizes “direct jump versus iterative solver” at a high level; it does not itself validate the practical efficiency of the learned policy.
   Why this matters: this is one of the paper’s headline claims. If a paper promises to bridge a speed-quality trade-off, the empirical support for speed should be as central and systematic as the support for return.

9. **Some quantitative claims in the results text are overstated relative to the tables.**  
   On **Page 9**, the paper says GTP-BC achieves “state-of-the-art performances in 11 out of 15 tasks.” Reading **Table 1**, that may be numerically true depending on exactly which baselines are counted, but several gains are small, and on some tasks GTP-BC is not best, for example walker2d-medium and walker2d-medium-expert. Likewise on **Page 9-10**, the “new state-of-the-art for generative policies in offline RL” claim from **Table 2** is directionally supported, but the margin on Gym average over D-QL is relatively modest, \(89.0\) vs \(87.9\), while some individual tasks favor competitors.  
   Why this matters: this is not fatal, but the rhetoric is a bit too sweeping. A more careful statement would increase trust.

10. **The paper’s treatment of off-support actions and conservative offline RL concerns is too light.**  
    The method remains an expressive generative actor guided by a learned critic. Yet the main paper offers little discussion of why advantage-weighted training on dataset actions is sufficient to avoid harmful extrapolation when the learned solution map is sampled iteratively at inference as in **Equation (15)**. The actor is trained on noised versions of dataset actions, but the denoising map can still produce actions outside the empirical support.  
    Why this matters: this is a central offline RL issue, especially for highly expressive policies. The paper would be stronger if it included diagnostics such as action-distribution support overlap, critic-value calibration for generated actions, or failure cases on narrow datasets.

11. **There are several notation and exposition issues that make the technical story harder to trust than it should be.**  
    A few examples:
    - The notation for \(\phi\), \(\Phi\), and \(\phi^{\mathrm{inst}}\) is conceptually related but easy to confuse; the transition from **Equations (3)-(5)** on **Page 4** to the actual losses on **Pages 7-8** is not as clean as it could be.
    - In **Equation (6)**, the text says the right-hand side is “composed forward to \(s\)” even though the time ordering is \(t>u>s\), which is a slightly confusing phrasing.
    - The theorem and appendix use \(\tilde f\), \(\hat f\), and \(\bar f\) in closely related roles, which is unnecessary notation drift.
    Why this matters: none of these alone is fatal, but together they create friction in a paper whose selling point is a clean unified mathematical framework.

12. **The visual evidence is suggestive rather than probative.**  
    The supplementary visualizations are appealing, especially **Figure 7** in the appendix, where the multi-goal environment shows GTP capturing multiple modes. However, because this is not a standard benchmark and the figure is qualitative, it is supportive illustration rather than decisive evidence. Similarly, **Figure 2(b)** nicely communicates the intended effect of value guidance, but it also reveals a potential limitation: the method is still conceptualized as moving a BC trajectory toward a local high-value region, which may not be enough for tasks requiring stronger distributional shift or long-horizon compositional planning. The paper would benefit from stronger quantitative support around these visual claims.

## Questions
1. The most important clarification I need is about **what is genuinely new algorithmically relative to CTMs and related solution-map methods**. Please spell out, in one paragraph, the exact delta between GTP and a CTM-style policy adapted to offline RL with standard advantage weighting. If the main novelty is the particular training recipe for offline RL, I would prefer the paper to state that more directly.

2. Please correct and clarify **Theorem 1** on **Page 6**, especially the definition of
   \[
   f^\star(\mathbf{x}_t,t).
   \]
   Is the denominator intended to be \(t\), as written in **Equation (32)** of the appendix? If so, please confirm that the theorem statement in the main paper is a typo and verify whether any other parts of the theorem depend on this notation.

3. Can the authors more carefully explain the relationship between the theorem-supported objective and the algorithm actually used? In particular, **Equation (10)** compares two solver-based losses, while **Equation (11)** effectively bypasses the solver. What is the formal or at least intuitive justification for the final training target used in **Equation (17)**?

4. How exactly is the **advantage \(A(s,a)\)** computed in practice for **Equation (14)**? Is \(V(s)\) estimated explicitly or implicitly? Also, over what set is \(\mathrm{std}(A)\) computed, minibatch, replay buffer, or running estimate?

5. What distributions are used to sample \(t\), \(u\), and \(\tau\) in **Equations (17)-(18)**? This is important for reproducibility and possibly for fairness against baselines.

6. Could the authors provide a stronger ablation that separates the effect of:
   - learning the full map \(\Phi(\cdot,t,s)\),
   - the score approximation,
   - the advantage weighting,
   - and the two actor losses \(\mathcal{L}_{\mathrm{Consistency}}\) and \(\mathcal{L}_{\mathrm{Flow}}\)?
   Right now, **Table 3** is helpful but too limited to isolate the source of gains.

7. For the efficiency claim, could the authors include a more systematic comparison of **training cost and inference cost across several tasks**, not just a single environment? This would materially increase my confidence in the “bridging the trade-off” claim.

8. Since offline RL is sensitive to action support, do the authors have diagnostics showing how often sampled actions from **Equation (15)** lie outside dataset support, or how critic values for generated actions compare to behavior actions?

9. Some of the benchmark improvements are concentrated on AntMaze. Do the authors have an explanation for why the method appears particularly strong there? Is it primarily due to multimodality, long-horizon structure, or the value-guidance formulation?

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
No major ethics concerns are apparent from the submission. The work uses standard offline RL benchmarks and does not involve human subjects, private data, or obviously high-risk deployment claims in the paper.

## Soundness Rating
2: fair. The method is plausible and the empirical evidence is strong, but the core theoretical claims are narrower than advertised, there is a significant typo/inconsistency in a central theorem statement, and several implementation details needed to fully assess the method are under-specified.

## Presentation Rating
3: good. The paper is generally readable and well organized, with useful figures such as **Figure 1** and **Figure 2**, but there are important notation inconsistencies and some over-claiming that reduce clarity.

## Contribution Rating
2: fair. The empirical results are strong and the unified perspective is useful, but the paper does not yet cleanly establish how much of the contribution is a genuinely new policy paradigm versus a careful integration of existing solution-map generative modeling ideas with offline RL heuristics.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted. The paper has real strengths, especially the benchmark results and the attempt to unify modern generative policies for offline RL, but I do not think the current version cleanly justifies the breadth of its novelty and theoretical claims. The main concerns are the blurry distinction from prior solution-map methods, a central mathematical inconsistency in Theorem 1, and insufficiently isolating experiments for the claimed contributions.

## Reviewer Confidence
4: confident. I am confident in this assessment, though not absolutely certain. I am familiar with offline RL and generative-policy literature, and I checked the main equations and experimental claims with care.