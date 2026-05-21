---
job_id: 7fea3a4b-c0ed-4abe-8fba-c81e458f6be7
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: iDki7djO2K.pdf
paper: Forgetting Is Everywhere
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, combining learning theory, probabilistic modeling, continual learning, reinforcement learning, and empirical analysis of learning dynamics.

## Minimum Quality
Pass ✅. The paper contains the expected core components, including abstract, introduction, related work, methodological/theoretical development, empirical analysis, and conclusion. Although I found substantial technical and empirical weaknesses, they do not rise to the level of an immediate desk rejection.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find any hidden prompts, suspicious reviewer-targeting instructions, or other manipulative content in the provided paper text.

# Expected Review Outcome:
## Summary
This paper proposes a general definition of forgetting based on predictive self-consistency: a learner forgets when updating on targets consistent with its own predictive distribution changes its induced predictive distribution over future interactions. Building on a general learner-environment interaction formalism, the paper defines a $k$-step consistency condition and an operational divergence-based quantity, the propensity to forget, intended to measure how much a learner is likely to forget. The empirical section studies this quantity across Bayesian regression, neural network classification and regression, generative modeling, continual learning, and reinforcement learning.

## Strengths
The paper is ambitious in scope and tries to treat forgetting as a property of learning dynamics rather than as a continual-learning-only metric. That reframing is interesting, and I do think the predictive-distribution viewpoint is a potentially useful lens for discussing forgetting across supervised learning, generative modeling, and RL in one language.

The learner-environment formalism in Section 3 is broad enough to cover several settings under one notation. In particular, separating learning-mode update $u$ and inference-mode update $u'$ is a sensible modeling move, and Figure 1 helps communicate the intended distinction between state evolution during training and induced futures under introspective rollout. Even though some notation around the figure is inconsistent with the text, the high-level picture is useful.

I also appreciated the attempt to separate forgetting from mere parameter drift or raw performance decay. The discussion around Desiderata 4.1-4.4, especially the claim that belief change alone should not be labeled forgetting, is thoughtful. Figure 2 is one of the stronger parts of the paper in this regard. The contrast between an exact Bayesian posterior, a diagonal Gaussian variational approximation, and a point-estimate learner makes the intended intuition fairly concrete: two learners can undergo parameter changes, but only some of those changes imply loss of supported predictive futures. That is a better illustration than the text alone.

The paper also deserves credit for testing the proposed quantity in multiple settings rather than only in a single continual learning benchmark. Figure 3 is useful as a broad sanity check, because it shows qualitatively different forgetting trajectories in regression, classification, generative modeling, and a class-incremental setting. Whether these plots fully validate the theory is a separate question, but the cross-domain effort is appreciable.

Finally, the appendix gives enough implementation detail to understand roughly how the Monte Carlo estimator is constructed. Table 3 and Table 4 at least make the experimental settings more inspectable, which is important given that the main paper omits many practical details.

## Weaknesses
1. **The core object of the theory, the hybrid distribution $q_e$, is underdefined in the main paper, and that is not a cosmetic issue, it is central to the validity of the definitions.**  
   The predictive rollout in Equation (3), the one-step consistency condition in Equation (7), the $k$-step condition in Equation (8), and the propensity-to-forget definition in Equation (9) all rely on sampling $X_t$ from $q_e(\cdot \mid H, Y)$. But on Page 4 this is only described informally as a “hybrid distribution” that “treats the learner’s predictions as targets while borrowing components from the environment as needed.” That leaves the mathematically essential part unspecified: what exactly is sampled, from what conditional law, and how does this differ across supervised learning, generative modeling, and RL? Since forgetting is defined by comparing predictive distributions induced through this rollout, the definition is only as precise as $q_e$. Right now, it is not precise enough in the main paper to support the claim of a general, algorithm- and task-agnostic formalism.

2. **There is a substantial mismatch between the abstract theory and the operational estimator actually used in experiments.**  
   Definition 4.6 on Page 7 defines $\Gamma_k(t)$ as a divergence between distributions over infinite futures, $q(H^{t+k:\infty}\mid \cdot)$ and $q_k^*(H^{t+k:\infty}\mid \cdot)$. In practice, the appendix replaces this with predictive distributions evaluated on finite held-out inputs, for example Equations (23)-(27) on Pages 21-22 for supervised classification. That may be a reasonable approximation, but the paper does not provide a theorem, bound, or even a careful argument showing when the empirical estimator is faithful to the theoretical quantity. This matters because the central empirical claims depend entirely on that estimator. At present, the experiments validate the behavior of one particular Monte Carlo proxy, not clearly the general theoretical object introduced in Section 4.

3. **There are multiple notation and equation inconsistencies, including some that directly obstruct understanding of the formalism.**  
   A few examples:
   - In Definition 3.2 on Page 3, histories are sequences of $(X_i, Y_i)$ from $i=0$ to $t$, implying the existence of $Y_0$. But in Definition 3.5 on Page 4, the interaction process initializes only $Z_0$ and $X_0$, and then samples $Y_t$ for $t>0$ from $q_f(\cdot \mid Z_{t-1}, X_{t-1})$. So the indexing of the initial pair is inconsistent.
   - Figure 1 on Page 5 captions the predictive distribution as $q(H^{t+1:\infty}\mid Z_{t-1}, H_{0:t})$, while Definition 3.6 on Page 4 uses $q(H^{t+1:\infty}\mid Z_t, H_{0:t})$. That is not a harmless typo, because it changes which state induces the future.
   - Page 7 contains a duplicated “Definition 4.5.” followed by multiple repeated versions of $\Gamma_k(t)$ in Equations (10)-(13), with inconsistent arguments, apparently left from editing. This is a serious presentation and correctness problem in the section where the main contribution is formally defined.
   - On Page 8, Equation (12) is reused for a different statement after Equation (15), suggesting numbering drift and lack of careful proofreading.

   For a paper whose main claim is conceptual and formal, these inconsistencies are damaging. They make it hard to know which definition the authors actually intend.

4. **The paper repeatedly frames forgetting as “loss of predictive information,” but that information-theoretic claim is not really developed.**  
   The abstract says forgetting “manifests as a loss of predictive information,” yet the formal development does not define predictive information as a mutual information or any other standard information quantity. Instead, the operational definition is an arbitrary divergence $\mathrm{D}(\cdot\|\cdot)$ between predictive distributions in Definition 4.6. That is a meaningful construction, but it is not the same thing as a principled information-theoretic quantity unless additional assumptions or results are provided. As written, the paper overstates the information-theoretic grounding. The related work is also light on directly relevant predictive-information literature that would help situate this claim.

5. **The empirical validation is too qualitative and too weakly comparative to substantiate the paper’s stronger claims.**  
   Figure 3 and Figure 5 show trajectories of the proposed quantity, but there is very little quantitative validation beyond “the curves look sensible.” There are no direct comparisons against established continual-learning forgetting metrics, no comparison to parameter drift or representational drift measures, and no demonstration that the proposed quantity better isolates forgetting from backward transfer in a controlled setting. Since one of the central claims is that prior metrics “mischaracterise forgetting,” the paper should do more than present standalone plots of $\Gamma_k(t)$. It should show, on a concrete example, where standard metrics fail and this one succeeds.

6. **Several causal interpretations in the empirical section go beyond what the evidence supports.**  
   The text around Figure 5 on Pages 9-10 claims that the forgetting curve “follows the TD loss because forgetting information is the mechanism by which the agent manages this process,” and later that forgetting is “an essential component of RL.” But Figure 5 shows correlation in one DQN CartPole setup, not evidence of mechanism. Many quantities in DQN co-vary during training, especially under changing exploration and replay distributions. The paper needs to separate descriptive association from causal interpretation. Right now the RL section is rhetorically stronger than the data justify.

7. **The “Bayesian learners are unforgetful” point is plausible but not established at the level of the paper’s own general framework.**  
   On Pages 7-8, the argument relies on standard posterior marginalization and exchangeability in Equations (14)-(15). That supports the intuition that exact Bayesian updating is self-consistent in classical Bayesian settings. However, the paper’s general learner formalism in Section 3 is broader than exchangeable supervised learning, and the text moves quickly from the Bayesian identity to statements about satisfying the $k$-step consistency condition. Figure 2 is informative visually, but it is not a substitute for a precise proposition that maps the general Definition 4.5 to exact Bayesian inference under clearly stated assumptions. As it stands, the claim is suggestive rather than fully nailed down.

8. **The “generality” claim is overstated given how environment-specific the empirical implementation is.**  
   In the supervised classification estimator on Pages 21-22, future inputs are sampled uniformly from a held-out validation set. That is a very specific design choice, and it bakes in a particular empirical approximation to $q_e$. Similar hidden choices presumably exist in the other domains. Table 3 and Table 4 list hyperparameters, but they also reveal how small and toy-like many settings are, for example two-moons classification and sinusoid regression. This is not fatal by itself, but it weakens the claim that the paper has empirically established a broadly applicable operational measure. The evidence is still at the “interesting proof-of-concept” stage.

9. **The efficiency-forgetting trade-off is intriguing, but currently undercontrolled and somewhat underjustified.**  
   Figure 4 on Page 9 shows an “elbow” relationship between mean $\Gamma_{40}(t)$ and training efficiency for momentum and model size variations. However, training efficiency is defined as inverse normalized area under the training loss curve, which mixes convergence speed, optimization noise, and final fit quality. That proxy may be acceptable for exploratory analysis, but the paper then draws broad conclusions like “optimal training efficiency occurs at a non-zero level of forgetting.” Without stronger controls, more tasks, error bars on the trade-off plots, and perhaps test performance measures, this conclusion feels too strong. The figure is provocative, but not yet decisive.

10. **Presentation quality is below the standard expected for a theory-heavy ICLR paper.**  
    The paper is readable at a high level, but the execution is rough in important places. The duplicated equations and mislabeled definitions on Page 7 are especially problematic. The appendix also contains awkward notation shifts, for example the output line “Property to Forget $\Gamma_k(t)$” in Algorithm 1 on Page 22, and there are small but recurring indexing inconsistencies across main text and appendix. These issues matter because the paper’s contribution is primarily definitional and formal. If the formal statement itself is unstable on the page, confidence in the scientific claim drops.

11. **Related-work positioning is somewhat selective for a paper making a “first general definition” claim.**  
    The paper does cite many continual learning and RL references, and it cites Jagielski et al. for memorized example forgetting. Still, the “to our knowledge, this is the first generalised definition of forgetting” claim in Section 6 needs more cautious positioning. In particular, the paper would benefit from deeper engagement with information-theoretic work on predictive information and with adjacent efforts that define forgetting via predictive or representational changes rather than only task accuracy. When the novelty claim is framed so broadly, the literature review needs to be especially careful.

## Questions
1. **Can you give a precise formal definition of the hybrid distribution $q_e$ in the main paper, not only domain-specific approximations in the appendix?**  
   This is the main point I would want clarified in rebuttal. In particular, what is the measurable object sampled by $q_e$, what parts come from the learner, what parts come from the environment, and how should one instantiate it in supervised learning versus RL versus generative modeling? If this is fully formalizable, that would increase my confidence substantially.

2. **Can you explain the intended canonical definition of $\Gamma_k(t)$ and fix the duplicated/inconsistent equations on Page 7?**  
   Please state clearly which of Equations (9)-(13) is the intended definition, and whether the first argument should be $q(H^{t+k:\infty}\mid Z_{t-1},H_{0:t-1})$ or $q(H^{t+k:\infty}\mid Z_t,H_{0:t})$. Right now this section is too unstable for a central definition.

3. **What formal relationship, if any, do you claim between your divergence-based $\Gamma_k(t)$ and “predictive information”?**  
   If the intention is only heuristic motivation, please tone down the wording. If a stronger information-theoretic claim is intended, please provide the relevant definition and argument.

4. **Can you provide at least one controlled experiment directly comparing your metric with standard forgetting metrics?**  
   For example, a setting with backward transfer or beneficial adaptation would be useful. I would like to see a case where a standard task-performance metric says “forgetting” but your measure does not, or vice versa, with a convincing explanation.

5. **For Figure 4, how robust is the efficiency-forgetting trade-off to the choice of efficiency metric and to evaluation on validation/test performance rather than training loss?**  
   This matters because the current proxy could reward optimization dynamics that do not correspond to better generalization.

6. **For Figure 5, can you moderate or support the causal claim that forgetting is the mechanism by which DQN balances acquisition and retention?**  
   A more careful analysis, for example interventions on replay, target update rate, or training frequency tied back to the same causal story, would help.

7. **Can you formalize the Bayesian non-forgetting result as a proposition under explicit assumptions?**  
   A clean statement connecting exact Bayesian inference to Definition 4.5 would make Section 5.1 much stronger.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
None beyond standard caution about reinforcement learning experiments and broad claims about learning systems. I did not identify a specific ethics issue requiring escalation based on the current submission.

## Soundness Rating
2: fair. The paper has an interesting formal direction, but the central mathematical object $q_e$ is underdefined, the core definitions contain inconsistencies, and the empirical evidence is more qualitative than validating.

## Presentation Rating
2: fair. The high-level narrative is understandable, and some figures are helpful, but notation drift, duplicated equations/definitions, and dependence on appendix details hurt clarity significantly.

## Contribution Rating
2: fair. The predictive self-consistency perspective is interesting and potentially useful, but the current version does not yet support the breadth of its claims strongly enough for me to view it as a solid ICLR contribution in its present form.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted. The paper has a stimulating core idea and some memorable intuitions, especially around predictive self-consistency and the distinction between forgetting and mere parameter change. However, the formalism is not yet clean enough, the operationalization is too loosely connected to the theory, and the experiments do not sufficiently validate the stronger claims.

## Reviewer Confidence
4: confident. I am confident in the main concerns, especially the formal-definition issues, the notation inconsistencies, and the gap between theory and empirical operationalization, though I cannot rule out that some intended formal details exist but were not communicated clearly enough in the submission.