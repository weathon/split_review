I have thoroughly read the paper and cross-checked the claims from both reviewers against the actual paper content. Let me now produce the consolidated review.

---

## Summary

This paper proposes CoMiGS, a federated fine-tuning framework for on-device LLMs that employs a Mixture-of-Experts architecture where some LoRA experts are aggregated across users ("generalists") while others remain local ("specialists"), with token-level routing learned via a separate validation set through a bi-level optimization formulation. The method claims to be the first to simultaneously address both system heterogeneity (varying numbers of experts per user) and data heterogeneity (distribution shifts across users), and presents experiments on GPT-2 small with 4 clients across multilingual, topic, and out-of-distribution settings.

## Strengths

- **Token-level routing with validation-set-based router learning.** The paper formalizes the MoE learning objective as a bi-level optimization (Eq. 1) where router parameters are updated on a *separate validation set* while expert parameters are updated on the training set. This design is empirically validated: CoMiGS-1G1S outperforms pFedMoE (which updates all parameters simultaneously) by 5–9 perplexity points on multilingual and SlimPajama (Table 1: e.g., 47.19 vs. 52.27 on Multilingual). The ablation studies (CoMiGS-2S and CoMiGS-2G) isolate the effect of the validation-set-trained router from the generalist/specialist distinction.

- **Simultaneous handling of system and data heterogeneity.** The approach allows users to have different numbers of LoRA experts (system heterogeneity) while dynamically routing tokens to generalists (shared) or specialists (local) based on the token's nature (data heterogeneity). In the heterogeneous setting (Table 2), CoMiGS-1GXS outperforms HetLoRA and FlexLoRA on 4 of 6 configurations (e.g., 46.48 vs. 57.76 for Multilingual with (2,2,4,4); 22.10 vs. 23.33 for SlimPajama with (2,4,4,2)).

- **Insightful routing analysis and overfitting mitigation.** The token-level visualization (Figure 2) confirms that function words route to generalists and domain-specific tokens route to specialists, validating the design intuition. The layer-wise analysis (Figure 3) reveals a phase transition in out-of-distribution tasks absent in pFedMoE. Additionally, Figures 4–5 demonstrate that the shared generalist regularizes low-data users against overfitting even when they have many local specialists, which is a practically important finding.

- **Controlled experimental design with ablations.** The paper includes three datasets, two distribution shift scenarios, parameter-count-matched baselines, and ablations (2 specialists, 2 generalists) run over three seeds. The extended tables and the rank-indicator visualizations provide a clear picture of relative performance.

## Weaknesses

### Fatal
None.

### Major

- **AG News failure case is not discussed or analyzed.** In the heterogeneous setting (Table 2), HetLoRA significantly outperforms CoMiGS-1GXS on the out-of-distribution AG News task for both configurations (e.g., 31.58 vs. 33.66 for (4,2,2,2); 31.58 vs. 34.22 for (2,4,4,4)). Similarly, in the homogeneous setting (Table 1), CoMiGS-1G1S (33.53) underperforms CoMiGS-2G (31.18) and FedAvg (31.84). The paper states that CoMiGS "outperforms the baseline methods most of the time" — which is accurate — but does not analyze *why* the method fails on this particular task. Possible explanations (e.g., that a strong aggregated generalist is more robust when the target is a mixture of training distributions) are directly relevant to the paper's core claims. This omission weakens the empirical narrative.

- **Architectural confound in the heterogeneous-setting comparisons.** CoMiGS uses an MoE architecture (multiple LoRA experts with Top-2 routing), while the baselines HetLoRA and FlexLoRA use a single LoRA module per layer. Matching active or full parameter counts does not match representational capacity — routing enables dynamic per-token specialization that a single LoRA cannot replicate. The paper does not include a heterogeneous-setting ablation that uses the same MoE architecture but with *all* experts being generalists (analogous to CoMiGS-2G but extended to the heterogeneous case). Without this, it is unclear how much of the observed improvement comes from the MoE architecture itself versus the generalist-specialist split. This does not invalidate the results but limits their interpretability.

### Minor

- **Bi-level optimization framing is oversold relative to the algorithm.** The paper calls the bi-level formulation a "key innovation" (abstract, contributions), but the actual algorithm (Algorithm 1) performs simple alternating gradient updates on expert and router parameters using separate data splits. The paper itself cites Chen et al. (2021) noting alternating updates are standard for bi-level optimization. The genuine contribution — using a separate validation set for the router — is well-motivated by the bi-level framing, but the formulation itself is not solved as a genuine bi-level optimization (the inner problem is neither solved to optimality nor approximated with a gradient-unrolling scheme). The paper would be stronger by recalibrating this claim around the *validation-based router update* rather than "innovative bi-level optimization."

- **CoMiGS-1G1S does not consistently "closely track" the best model on AG News.** In Table 1, CoMiGS-1G1S (33.53) is 2.35 perplexity points worse than CoMiGS-2G (31.18) on AG News — a substantially larger gap than the 0.43–0.83 point gaps on Multilingual and SlimPajama. This weakens the paper's claim that 1G1S "can always closely track the best-performing model." The discrepancy deserves a brief explanation.

- **Limited experimental scale.** Experiments use 4 clients and GPT-2 small. The paper's framing around "on-device collaborative LLMs" implies relevance to larger models and more users. While scaling is acknowledged as future work, the gap between the claims and the evidence base is notable, particularly for claims about addressing system heterogeneity with up to 4 users.

### Trivial
- Some figure references in the text (e.g., Figure 4, Figure 5) use formatting that is difficult to parse in the extracted text, but this is a parser artifact, not an author error.

## Nice-to-Haves
- Reporting statistical significance tests (e.g., confidence intervals over seeds) to support claims of improvement.
- A communication cost comparison: CoMiGS communicates one generalist LoRA per round per user; HetLoRA/FlexLoRA communicate differently. A head-to-head communication budget comparison would strengthen the practical relevance.
- A brief discussion of convergence behavior for the alternating update scheme (e.g., risk of oscillation, whether the router and expert updates can be proven to converge under the standard FL assumptions).
- Extending the CoMiGS-2G ablation to the heterogeneous setting to isolate the effect of the generalist-specialist split from the MoE architecture.

## Removed Points
- **"The bi-level optimization framing is overstated as a critical issue"**: The harsh critic frames this as a "critical" problem that invalidates the contribution. The paper is transparent about using alternating updates (citing Chen et al. 2021). The framing is somewhat oversold but the underlying idea — separate validation set for the router — is genuinely novel and empirically validated. Demoted from critical to minor.
- **"Token-level visualization is qualitative"**: This is a descriptive weakness about what visualization inherently is; the analysis is appropriate for this type of result and no better quantitative metric is proposed.
- **"Rank-indicator bars are a parser artifact"**: Removed as a formatting nitpick — this is not an author error.
- **Generic strengths about the problem being important**: Removed as generic/superficial. Kept only concrete strengths with specific evidence.

## Novel Insights
Both the validation-set-based routing and the regularizing effect of shared generalists on low-data users are insightful. A particularly interesting finding from combining the reviewers is the *asymmetric vulnerability* of the method: CoMiGS excels when the target distribution matches one of the training distributions (in-distribution), but can be worse than a pure-generalist baseline when the target is a uniform mixture of all distributions (AG News OOD). This suggests a fundamental trade-off between personalization and robustness that the paper does not explore, and it surfaces a potential boundary condition for when the generalist-specialist design is beneficial versus when simple aggregation suffices.

## Suggestions
1. Add a brief analysis of the AG News failure case in the paper — even one paragraph hypothesizing why HetLoRA beats CoMiGS on OOD tasks would significantly strengthen the paper's credibility and intellectual honesty.
2. Add a heterogeneous-setting baseline where *all* experts are generalists (using the same MoE architecture and validation-set router) to disentangle the architectural advantage of MoE from the generalist-specialist contribution.
3. Recalibrate the claim about bi-level optimization from "innovative formulation" to "validation-set-based bilevel formulation for MoE routing" — the key novelty is the data-split strategy, not the optimization technique.
4. Qualify the claim that "1G1S always closely tracks the best model" to acknowledge the larger gap on AG News.

## Score and Decision

This paper makes a solid empirical contribution with a well-motivated method, clean ablations, and an insightful routing analysis. The weaknesses are genuine but manageable — the AG News omission and the architectural confound are the most significant, but neither invalidates the core contribution. The paper would benefit from a more measured framing of the bi-level optimization claim and a transparent discussion of the failure case. I assess this as a solid paper that should be accepted conditioned on addressing the major weaknesses, particularly the AG News analysis and the architectural confound discussion.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>