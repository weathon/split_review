---
job_id: 18c7b4c1-2808-4e0d-b533-6ca8dbca9539
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: Y9TgNFsNyP.pdf
paper: FF-Erase: Machine Unlearning and Verification for Forward-Forward Models
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, it studies machine unlearning, privacy auditing, and optimization for Forward-Forward neural networks, which fits general machine learning, privacy, and learning algorithms.

## Minimum Quality
Pass ✅. The paper contains the expected scientific structure, including Abstract, Introduction, Related Work, Methodology, Experiments, quantitative results, and Conclusion, and it presents a concrete method with empirical evaluation; while there are important weaknesses in rigor and positioning, they do not rise to desk-reject level.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find hidden prompts, manipulative instructions, or suspicious embedded text targeting automated reviewers in the provided manuscript content.

# Expected Review Outcome:
## Summary
This paper studies machine unlearning for Forward-Forward (FF) models, a setting that the authors argue has not been addressed previously. The proposed method, FF-Erase, uses a separate guidance model to produce target layer-wise goodness distributions, then updates the original FF model by matching forgetting samples to the guidance goodness with a KL-based objective while periodically running a recovery step on remaining data. The paper also introduces a goodness-based membership inference attack, G-MIA, as a black-box auditing tool tailored to FF models, and evaluates both components on several image benchmarks and FF architectures.

## Strengths
The paper tackles a reasonably well-motivated niche problem. If one accepts FF models as a meaningful alternative training paradigm, then unlearning and verification for that family is a natural missing piece, and the paper identifies concrete reasons why naively porting backprop-based unlearning may fail.

The main intuition of FF-Erase is sensible. Using a guidance model that is trained without the forget set, then steering the original model toward that guidance distribution instead of performing unrestricted ascent, is a plausible way to stabilize updates in a layer-wise FF setting. The paper also tries to address a practical issue, namely the cost of obtaining the guidance model, via the mini-retrained and fast-distilled variants.

I appreciated the use of visual explanations in **Figure 2**. In particular, **Figure 2(a)** helps clarify the FF training pipeline and the multi-class goodness construction, while **Figure 2(b)** makes the two-stage unlearning loop, forgetting forward plus recovering forward, much easier to follow than the pseudocode alone. This figure does real explanatory work rather than serving as decoration.

The empirical section does provide some evidence that a tailored method is preferable to direct gradient ascent for FF models. In **Figure 4**, the FF-Erase curves appear to approach retraining-level forget-set accuracy and similar test accuracy much faster than full retraining, while the GA baseline visibly destabilizes. Likewise, **Figure 5** is useful because it checks multiple values of $\lambda$ rather than a single unfavorable setting, which strengthens the claim that the failure of plain GA is not just due to one bad hyperparameter.

The ablation in **Table 1** is one of the stronger parts of the paper. It shows the efficiency and effectiveness trade-off across different guidance-model budgets and also includes the randomly initialized guidance model, which is an important sanity check. The poor performance of R.G.M. supports the paper’s central claim that the quality of the guidance distribution matters.

G-MIA is also a reasonable FF-specific auditing proposal. Even if the high-level recipe resembles standard shadow-model MIAs, adapting the attack features to layer-wise goodness vectors is a natural and potentially useful design choice for this architecture family. The results in **Figure 3** suggest that goodness vectors carry stronger membership signals than the final output alone.

## Weaknesses
1. **The mathematical formulation of the FF model is unclear and in places internally inconsistent.**  
   The core definition in **Equation (1), Page 4** is hard to parse. The paper writes
   $$
   \boldsymbol g^l = \|\boldsymbol h^l\|_1,
   $$
   but immediately afterwards states that $\boldsymbol g^l = [g_1^l,\dots,g_J^l]$ is a $J$-dimensional goodness vector containing one score per class. A plain $L_1$ norm of $\boldsymbol h^l$ is a scalar, not a class-wise vector. This is not a cosmetic notation issue, it affects the meaning of every later expression, including the softmax cross-entropy in **Equation (2)** and the KL divergence used in **Section 4.1**. The lower-right inset of **Figure 2(a)** visually suggests class-partitioned activation channels, but the paper never formalizes how hidden units map to class-specific goodness components. If the goodness is computed by grouping activations per class, the grouping rule must be defined explicitly. As written, the objective is underspecified.

2. **Algorithm 1 and the corresponding equations are not mathematically well specified enough to reproduce or verify the method.**  
   In **Algorithm 1, Page 5**, the pseudocode sets
   $$
   \ell_1[l] = \nabla D_{\mathrm{KL}}([g^l],[g_*^l]), \quad \theta_o^l = \theta_o^l - \eta \ell_1[l],
   $$
   and similarly for $\ell_2[l] = \nabla \mathcal L_{\mathrm{ff}}([g^l],y)$ in RFwd. This abuses notation in a way that obscures what is being differentiated with respect to what. Gradients should be written as $\nabla_{\theta_o^l} D_{\mathrm{KL}}(\cdot)$ or $\nabla_{\theta_o^l}\mathcal L_{\mathrm{ff}}(\cdot)$, otherwise $\ell_1[l]$ and $\ell_2[l]$ are neither scalar losses nor clearly defined gradient tensors. More importantly, in FFwd the paper forwards both the original model and the guidance model layer by layer, but it does not specify whether $z_g^{l-1}$ is computed from the guidance network independently, nor whether gradients stop through $g_*^l$ as constants, which they presumably should. Also, **Equation (5)** includes $(x,y)$ in $\boldsymbol g^l(\boldsymbol x,y;\theta^l)$ even though the KL term itself does not appear to use $y$ directly. These sound like small formal issues until one tries to implement the method, at which point they become central.

3. **The training objective for unlearning is heuristic and lacks justification relative to the stated problem formulation in Equation (4).**  
   The problem statement in **Equation (4), Page 4** defines unlearning as
   $$
   \min_{\theta^u \in \Theta} \mathcal L(\theta_u;\mathbb D_{\mathrm{forget}}) - \lambda \mathcal L(\theta_u;\mathbb D_{\mathrm{remain}}),
   $$
   which is already unusual because minimizing the forget loss is the opposite of most unlearning formulations that seek to worsen performance on forget data or approximate retraining on the remain set. Then in **Section 4.1** the actual method does not optimize this objective. Instead, it minimizes
   $$
   D_{\mathrm{KL}}(\boldsymbol g^l \| \boldsymbol g_*^l)
   $$
   on forgetting samples and periodically applies standard FF training on remaining samples. The paper should explain more carefully why matching the guidance model’s goodness distribution on forgetting samples is the right surrogate for unlearning, and in what sense it approximates retraining on $\mathbb D_{\mathrm{remain}}$. Right now the connection between **Equation (4)** and **Equations (5)-(6)** is asserted rather than established. This matters because the entire paper hangs on the claim that the guidance distribution is not just stabilizing updates, but also moving the model toward a meaningfully unlearned state.

4. **The experimental comparison is too narrow for the strength of the claims.**  
   The main text compares primarily against retraining and direct gradient ascent. I understand the authors’ argument that GA is representative, and the appendix reportedly includes more baselines, but the review standard should be based on the main paper. A paper making “first method for FF unlearning” claims should compare in the main text against stronger approximate unlearning families, especially teacher-student or distillation-style methods, since FF-Erase itself is effectively teacher-guided. Limiting the main evidence to RE and GA makes the empirical case look thinner than the narrative suggests. The appendix may help, but the central paper should stand on its own.

5. **The evaluation protocol for unlearning effectiveness is not fully convincing, and some metrics are interpreted too optimistically.**  
   In **Section 6.2, Page 8**, the paper argues that because $\mathbb D_{\mathrm{forget}}$, $\mathbb D_{\mathrm{train}}$, and $\mathbb D_{\mathrm{test}}$ share the same distribution, effective unlearning should yield accuracy on $\mathbb D_{\mathrm{forget}}$ similar to the original model’s accuracy on $\mathbb D_{\mathrm{test}}$. This is a rough heuristic, not a reliable criterion. Similar accuracy on a held-out sample from the same distribution does not by itself imply the removed points no longer have special influence. The paper does include G-MIA, which is better than accuracy-only reporting, but G-MIA itself is still a learned empirical attack, not a definitive verification tool. The manuscript should be much more careful in distinguishing “appears similar to retraining under these metrics” from “effectively removes influence.”

6. **The gains over retraining are meaningful but not overwhelming once guidance-model cost is included, and the presentation around efficiency is slightly slippery.**  
   **Figure 4** and **Table 1** show speedups in the rough range advertised, but a notable fraction of the savings comes from using partial-data or partial-epoch guidance models whose quality then directly affects unlearning quality. In **Table 1**, some of the faster guidance settings degrade both G-MIA and test accuracy, sometimes nontrivially. That is not fatal, but the framing in the abstract and conclusion is more confident than the table supports. This is not a free lunch, it is a trade-off between guidance quality, utility, and unlearning effectiveness. The paper would be stronger if it foregrounded this trade-off rather than mostly emphasizing the best-case speedup.

7. **The claims about G-MIA being a “strict black-box” method are overstated given the access assumptions.**  
   In **Section 5, Page 7**, the attacker is assumed to obtain layer-wise goodness vectors from all layers of the target FF model and to synthesize data from a similar distribution. For conventional black-box auditing, this level of interface access is stronger than merely observing the final prediction API. It is black-box in the sense of no parameters or gradients, yes, but the paper repeatedly compares G-MIA to standard black-box attacks without really acknowledging that it enjoys richer outputs. This matters when the paper claims that G-MIA is both more practical and almost white-box-strength. If the deployment API must expose all layer-wise goodness vectors, that is a specialized access model, not the generic black-box setting readers may infer.

8. **The empirical support for G-MIA is somewhat incomplete in the main paper.**  
   **Figure 3** reports ACC across datasets and architectures and indeed suggests that G-MIA is often stronger than FL and competitive with some white-box attacks. But the main paper omits AUC, despite introducing it as another evaluation metric, and the richer analysis of attack input dimensionality appears only in the appendix. Since G-MIA is presented as a major contribution, the main text should more fully characterize when it wins, when it does not, and what the access-cost trade-off is. The current main-paper evidence is suggestive, not definitive.

9. **Presentation quality is uneven, with several notation and writing issues that make an already specialized paper harder to trust.**  
   A few examples: on **Page 4**, $z^l$ is defined using “the normalization of $h^{l1}$,” which appears to be a typo; on **Page 5**, the phrase “collect the goodness vector $g_i x;\theta$” is malformed; in **Section 6.2**, the text says “FF-Erase(D) retains similar accuracy as retaining on test data (80.85 and 77.87, respectively),” which is confusing and seems to compare the retraining model and FF-Erase with the wrong labels. There are enough such issues that I repeatedly had to infer intended meaning. For a method paper with custom notation and architecture-specific losses, this hurts credibility.

10. **The literature positioning is decent but still incomplete in one relevant direction.**  
   The related work discusses approximate and exact unlearning for BP models, but it does not engage with layer-wise or layer-targeted unlearning ideas that are conceptually close to what this paper advocates. That omission makes the contribution appear slightly more isolated than it actually is. Even if prior methods are not directly applicable to FF models, the paper should situate its layer-wise guidance design more explicitly within that broader family.

## Questions
1. Please formally define the class-wise goodness vector used throughout the paper. In **Equation (1)**, how does $\|\boldsymbol h^l\|_1$ become a $J$-dimensional vector $\boldsymbol g^l = [g_1^l,\dots,g_J^l]$? Is there a fixed partition of channels/neurons by class, and if so, what is it exactly? A precise definition here would substantially increase confidence in the method.

2. Can you rewrite **Algorithm 1** and **Equations (5)-(6)** with explicit gradients, for example $\nabla_{\theta_o^l}$, and clarify whether $g_*^l$ is treated as a constant target with stop-gradient? Right now the optimization steps are not specified cleanly enough for faithful reproduction.

3. What is the conceptual link between the optimization target in **Equation (4)** and the actual KL-matching update in **Equation (5)**? If possible, please provide either a derivation, an approximation argument, or at least a more explicit explanation of why matching the guidance model on forget samples should approximate retraining on $\mathbb D_{\mathrm{remain}}$.

4. The paper emphasizes that G-MIA is black-box, but it assumes access to layer-wise goodness vectors from all layers. How realistic is this API assumption in the intended deployment setting? It would help if you clearly framed this as an intermediate access regime and, ideally, compared against a version using only final prediction outputs from the same FF model interface.

5. Could you move at least one stronger non-GA approximate unlearning baseline into the main paper results, not only the appendix, especially one that uses teacher-guided or distillation-style updates? Given the similarity in spirit to FF-Erase, that comparison would materially affect my assessment.

6. In **Table 1**, some settings with lower $t_0$ noticeably worsen G-MIA and test accuracy. Could you provide a clearer rule of thumb for choosing $(\alpha_1,\alpha_2)$ and perhaps show confidence intervals over multiple random forget splits? That would make the efficiency claims more practically useful.

7. Do the early stopping thresholds $\epsilon_1,\epsilon_2$ use a validation split, or are they selected based on the same data used for reporting? Please clarify how these thresholds are set, because threshold tuning can materially affect both effectiveness and utility.

## Flag For Ethics Review
- Yes, Privacy, security and safety

## Details Of Ethics Concerns
The paper is centrally about privacy-related auditing through membership inference and motivated by the right to be forgotten, so privacy and security are inherently implicated. In **Section 5**, the paper introduces a stronger attack tailored to FF models and assumes the attacker can synthesize data from a similar distribution and access all layer-wise goodness vectors. I do not view this as a reason to block the paper, but the authors should be careful to frame G-MIA as a dual-use auditing tool and clearly describe the access assumptions and deployment relevance.

## Soundness Rating
2: fair. The paper presents a plausible method with encouraging experiments, but the core FF/goodness formalization and the optimization details are not cleanly specified enough, and the empirical support in the main paper is narrower than the claims.

## Presentation Rating
2: fair. The paper is readable at a high level and the figures are helpful, especially **Figure 2**, but the notation, equations, and several passages need substantial cleanup for a top-tier methods paper.

## Contribution Rating
2: fair. Addressing unlearning for FF models is a useful direction and the guidance-based idea is sensible, but the contribution currently feels more like a targeted adaptation with incomplete methodological grounding than a clearly established advance.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted.  
My view is that the paper is promising and tackles a real gap, but it is not quite ready in its current form. The main blockers are the underspecified mathematical formulation of goodness and optimization, the somewhat narrow main-paper baseline suite, and overconfident framing around verification and efficiency. A cleaned-up version with tighter formulation and stronger main-text comparisons could move this upward.

## Reviewer Confidence
4: confident. I am confident in this assessment, though not absolutely certain. The paper is in an area I know well, and I checked the equations and empirical claims carefully, but the manuscript’s own ambiguities leave some room for interpretation.