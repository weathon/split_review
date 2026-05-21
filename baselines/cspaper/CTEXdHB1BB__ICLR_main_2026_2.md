---
job_id: 604571fa-ea4c-4159-8d5e-baaf09e178d6
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: CTEXdHB1BB.pdf
paper: Conditional Advantage Estimation for Reinforcement Learning in Large Reasoning Models
main_score_norm: 0.6
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, it studies reinforcement learning and advantage estimation for large reasoning models, with methodological contributions and empirical evaluation on reasoning benchmarks.

## Minimum Quality
Pass ✅. The paper contains the required scientific components, namely abstract, introduction, related work, method, experiments, quantitative results, analysis, and conclusion, and it presents a non-trivial method with substantial empirical support, even though several technical and presentation issues remain.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did notice explicit prompt text in Appendix C.4/C.5, but it is presented as the model system prompt used in experiments rather than as hidden instructions targeting reviewers or automated review systems.

# Expected Review Outcome:
## Summary
This paper proposes CANON, a conditional advantage estimation method for RL with verifiable rewards, where sampled responses are split into two groups according to a rollout metric such as entropy or response length, and the policy is updated using a combination of inter-group and intra-group advantages. The paper argues that this lets the training process amplify the effect of a metric without hard-coding whether “higher is better” or “lower is better,” and evaluates the approach on math reasoning and high-complexity logic benchmarks across several open models. The experiments also include dynamic scheduling between inter- and intra-group components, as well as a weighted length-based variant aimed at improving reasoning efficiency.

## Strengths
The paper addresses a real and timely problem in RLVR for reasoning models. A lot of recent work injects priors through reward or advantage shaping with a fixed directional bias, and the authors’ motivation, namely that metrics like entropy or length can help but their preferred direction is context dependent, is sensible and well articulated in Sections 1 and 4.

The core method is simple enough to be implemented in existing GRPO-style pipelines, but it is not just a cosmetic rewrite. The decomposition into inter-group and intra-group comparisons in Equations (3)-(5) gives a usable knob for favoring either the higher-performing metric trend or the better sample within a weaker trend. This is a practically meaningful design choice, especially in RLVR where sparse binary rewards often make credit assignment brittle.

The empirical evaluation is broader than average for this line of work. Table 1 reports results on six math benchmarks and three complexity buckets from ZebraLogic, and Table 2 extends the dynamic variant across three backbones. The method is not merely shown on one preferred model and one dataset. In particular, Table 1 supports the paper’s main qualitative claim that the two components behave differently: entropy-based CANON-Inter is strongest on math average accuracy, while entropy-based CANON-Intra is clearly better on the high-complexity logic average. That separation of regimes is interesting and not obvious a priori.

The efficiency experiments are also useful rather than decorative. Table 3 and Figure 4 together show that the weighted length-based variant can improve the performance-cost trade-off compared with clipping and length-penalty baselines. Even if the exact degree of dominance depends on tuning, the fact that CANON-Eff can move the Pareto frontier in Figure 4(c) is a practical contribution.

The figures generally help communicate the story. Figure 1 gives a clean overview of the regrouping-and-comparison mechanism, and it is one of the clearer method diagrams in this area. Figure 2 is also informative: panels (b)-(e) make the distinction between CANON-Inter and CANON-Intra more concrete by showing that entropy, length, and downstream task performance evolve differently under the two extremes of $\mu$. This is much better than only reporting endpoint numbers.

The paper includes at least some theoretical effort rather than only intuition. The observation in Equation (7), that DR.GRPO can be written as an equal mixture of inter- and intra-group terms under equal-size grouping, is a nice unifying perspective and helps position CANON relative to a known baseline.

## Weaknesses
1. **The theoretical claims are narrower and less convincing than the prose around them suggests.**  
   Theorems 1 and 2 in Section 4.2 sound stronger in the main text than what is actually established. Theorem 1 states that the inter-group advantage gives a “clearer advantage signal” only when the groups are equally sized, but this conclusion depends on a stylized expectation-level analysis with binary correctness rewards and a fixed condition probability; the actual statement in Equation (6) is also awkwardly phrased, and the appendix derivation relies on average advantages, not on the noisy sample-wise estimator used in training. In other words, the theorem does not really establish optimization improvement, lower variance, or better learning dynamics in the practical finite-sample RL setting. This matters because the paper leans on the theorem to justify the equal split design choice, but the formal result is much weaker than that design justification.

2. **There are mathematical and notational inconsistencies that make the method harder to verify than it should be.**  
   Equation (1) has several typos and inconsistencies: the policy subscript appears as $\theta_{\mathrm{cll}}$, which looks like a typo for $\theta_{\mathrm{old}}$ or similar; the clipping notation is defined as $\mathrm{clip}_o^b(x)=\max(\min(x,a),b)$, mixing $o$, $a$, and $b$ in a confusing way; and the ratio term inside the clipped objective appears once as $r_{o,t}(\theta)$ and once as $r_{o_t,t}(\theta)$, which is inconsistent. In Section 4.1, the set notation also slips, first defining $C_q^+$ but then writing $C_q^- = G_q \setminus C_q$ instead of $G_q \setminus C_q^+$. These are not just cosmetic issues, because this paper’s contribution is an advantage estimator, so precise definitions matter.

3. **Equation (3) and Equation (4) deserve a clearer derivation and interpretation, especially for edge cases.**  
   The paper says the responses are split into two equally sized groups after sorting an ordinal metric, but it never specifies what happens when many samples tie at the split boundary, which can happen for coarse metrics such as reflection counts and even for length. Since the whole method depends on deterministic regrouping, tie handling should be specified explicitly. More importantly, the advantages in Equations (3) and (4) are written as response-level quantities but are then used as token-level $\hat A_{q,o,t}$ in PPO-style loss, without any discussion of whether the same scalar is broadcast to all tokens. This is standard in GRPO-like methods, but in a paper whose main contribution is an alternative advantage estimator, being explicit here would help avoid ambiguity.

4. **The presentation around the role of CANON-Intra is conceptually muddy.**  
   Section 4.2 claims that CANON-Intra “prioritizes correct responses from the group with a lower average reward,” and the following parenthetical explanation is hard to parse because of mismatched parentheses and missing braces. More fundamentally, the intuition is not fully unpacked. In Equation (4), each sample is compared only to its own group mean; the claim that this prioritizes underrepresented but valuable behavior is true only indirectly through differing group averages and the binary reward structure. This is one of the central conceptual hooks of the paper, and right now it reads more like hand-waving than a crisp argument.

5. **The empirical evaluation is broad, but not always controlled enough to isolate what exactly is helping.**  
   Table 1 compares against several baselines, but the proposed method receives multiple forms of adaptation at once across the paper: regrouping by different metrics, different $\mu$ values, dynamic schedules, and weighted inter-group terms with $\alpha$. As a result, it is not always clear whether gains come from the conditional structure itself, from extra tuning flexibility, or from model-specific scheduling. Table 2 makes this issue sharper, since the best “CANON-Dynamic” result is chosen from model-specific schedules, including different strategies for different backbones. That is perfectly reasonable for practical optimization, but it weakens the claim of a generally robust method unless the paper also reports a single schedule applied uniformly across models.

6. **The comparison to prior work is not as strong as it could be for advantage-estimation methods specifically.**  
   The paper compares against ReMax, RLOO, GRPO, DR.GRPO, and two entropy-related baselines, which is a decent start, but the related work and empirical section do not do enough to distinguish CANON from other recent modifications of advantage estimation beyond the immediate GRPO family. Given how crowded this area has become, stronger positioning against alternative advantage-estimation strategies would help establish whether the main contribution is truly the conditional regrouping idea rather than just another useful GRPO variant. This matters for contribution rating, not because the method is irrelevant, but because the paper’s novelty claim is mostly at the level of estimator design.

7. **Some experimental choices raise fairness and interpretability questions.**  
   On Page 6, the Qwen2.5-Math-7B context limit is expanded from 4096 to 16384 by changing RoPE theta, and the maximum answer length is set to 8192. Appendix C.3 explains this was done because clipping above 30% made outcomes hard to compare. I appreciate the honesty, but this also means the reported numbers are somewhat entangled with a non-trivial architectural or inference-context intervention, not only the advantage estimator. Since length is one of the core studied metrics, changing the context limit can influence the exact behavior of both the baseline and the method. The paper should discuss more explicitly how much of the effect is attributable to CANON versus the extended context setting.

8. **The efficiency section is promising, but the strongest claims are a little overstated relative to the evidence shown.**  
   In Section 5.3, the paper claims CANON-Eff “Pareto dominates” certain baselines. Table 3 does show a strong trade-off, and Figure 4(c) is visually favorable, but the frontier comparison depends on a finite and somewhat asymmetric hyperparameter sweep. The text itself notes instability for Length Reward (+), for example a drop from 54.8 to 22.5 when changing the coefficient from 0.004 to 0.005. That instability supports the authors’ narrative, but it also suggests the baselines may not have been explored uniformly enough to make dominance claims feel airtight. A stronger claim would be “achieves a better frontier in our sweep” rather than a broad Pareto-dominance statement.

9. **Several parts of the paper are under-edited, and this hurts trust more than it should.**  
   There are many small but noticeable issues: “Cosin” instead of “Cosine” in Table 2 and Section 5.2, repeated or broken sentences in Section 6 around Figure 5, inconsistent capitalization of subsection titles, and a missing reference in Appendix D.5 where Table “??” is cited. Figure 2’s caption and nearby discussion are also a bit overloaded, with Figure 2(f) discussed as “benefits of more rethinking” but the construction of that proxy living in Appendix C.1. None of these alone is fatal, but accumulated together they make the paper feel less polished than it should for a method paper whose main value is clarity of formulation.

10. **The paper’s main claims are currently limited to RLVR with binary verifiable rewards, but the framing sometimes sounds broader.**  
   Much of the intuition in Sections 1 and 4 is phrased as though CANON is a general way to incorporate human priors on metrics without sign assumptions. In reality, all experiments use 0/1 correctness rewards and settings where group reward means are easy to interpret. It is not clear whether the same regrouping logic remains useful under dense rewards, reward models, or softer verification signals. This limitation is partly acknowledged in Appendix A, but it should be surfaced more clearly in the main paper because it affects how broadly readers should interpret the contribution.

## Questions
1. In Equations (3)-(5), is the same response-level advantage broadcast to every token of the sampled response, as in standard GRPO-style training? Please state this explicitly in the main paper, because the notation $\hat A_{q,o,t}$ suggests token dependence but the formulas themselves do not.

2. How are ties handled when sorting samples by the grouping metric, especially at the boundary between the two equal-sized groups? This is important for reproducibility for length, entropy, and the reflection-count variant.

3. For the theoretical part, can the authors clarify exactly what Theorem 1 is intended to guarantee in practical training terms? Is the claim merely about larger expected magnitude relative to DR.GRPO under the stylized model, or is there a stronger statement about variance reduction / optimization quality that the paper wants readers to infer?

4. Can the authors report, in the main paper, a schedule-agnostic comparison for CANON-Dynamic, for example one fixed scheduling rule applied to all three models in Table 2? Right now, model-specific scheduling makes it harder to know how robust the method is without per-model tuning.

5. In Table 1, CANON-Inter based on entropy improves math performance, while CANON-Intra based on entropy improves logic performance. Can the authors provide a more mechanistic explanation for why the task split aligns so cleanly with the estimator split? Figure 2 is suggestive, but the current explanation still feels partly post hoc.

6. For the efficiency experiments in Table 3 and Figure 4, how extensive was the hyperparameter search for the length-penalty baselines relative to the sweep over $\alpha$ in CANON-Eff? A clearer accounting of tuning budget would increase confidence in the Pareto-frontier claims.

7. Since the paper modifies the Qwen2.5-Math context setting on Page 6, can the authors provide a short main-text statement on whether the same extension is applied to all compared training methods, and whether the relative conclusions hold without this change?

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
The work uses open-source models and benchmark datasets for reasoning tasks, and the paper does not introduce a new dataset involving human subjects or sensitive personal data. I do not see a concrete ethics issue that requires dedicated escalation based on the material in the submission.

## Soundness Rating
3: good. The paper is technically plausible and empirically supported by a substantial benchmark suite, but the theory is narrower than advertised and several equations / definitions need cleanup and clarification.

## Presentation Rating
2: fair. The overall structure is serviceable and some figures, especially Figure 1 and Figure 2, are helpful, but the paper has too many notation issues, typos, broken sentences, and under-explained mathematical points for me to call the presentation good.

## Contribution Rating
3: good. The method is a useful and reasonably original variant of group-relative advantage estimation, and the empirical evidence suggests practical value, especially for balancing performance and efficiency, even if the conceptual advance is not yet fully nailed down.

## Overall Rating
6: Marginally above the acceptance threshold. But would not mind if paper is rejected. The core idea is useful, the experiments are broad, and the results are strong enough to matter to the RLVR community, but the paper needs a more careful treatment of theory, notation, and evaluation control to fully justify its claims.

## Reviewer Confidence
4: confident. I am comfortable assessing RL for LLM reasoning and advantage-estimation methods, and I checked the main equations, tables, and figures carefully, although I did not independently verify appendix proofs line by line beyond consistency with the main-text claims.