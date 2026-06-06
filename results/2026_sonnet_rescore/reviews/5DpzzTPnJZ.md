---

## Summary

This paper addresses plasticity loss in deep reinforcement learning by developing a theoretical framework connecting RL's non-stationarity (shifting data distributions + bootstrapping targets) to two mechanisms: NTK rank collapse and Θ(1/k) gradient magnitude decay. Based on the second mechanism, the authors propose Sample Weight Decay (SWD), which preferentially samples recent replay buffer entries to counteract gradient attenuation. Experiments span TD3/MuJoCo, Double DQN/ALE, and SimBa-SAC/DMC, demonstrating consistent IQM improvements of 13.7–30.1%.

---

## Strengths

1. **Theorem 3 and the Θ(1/k) gradient decomposition**: Equation 4 provides a genuine formal decomposition of the initial gradient into a distributional-shift term (scaling 1/k) and a target-drift term. Proposition 1 underpins it with a clean recursive characterization of the replay buffer distribution. Even with the boundary-case caveat (see Weaknesses), this is the clearest formal link yet between growing replay buffers and diminishing gradient signal.

2. **Consistent empirical improvements across diverse settings**: SWD improves IQM across TD3 on 5 MuJoCo tasks (Figure 2), Double DQN on 3 ALE games (Figure 3), and SimBa-SAC on 4 DMC tasks (Figure 4), with aggregate metrics in Figure 1 showing improvements in IQM and optimality gap across all three algorithm families. This breadth—spanning discrete and continuous control, different architectures, and multiple algorithms—is a genuine strength.

3. **Reverse validation via SWA**: Section 6.2 constructs the symmetric counterpart (Sample Weight Augmentation, weighting older samples higher) and shows it degrades performance (Figure 5a), reduces gradient L1 norms (Figure 5b), and lowers GraMa plasticity scores (Figure 5c). This controlled reversal is a clean and principled ablation that directly tests the causal claim.

4. **GraMa tracking confirms plasticity mechanism**: Figure 6 shows SWD maintains higher GraMa values throughout training in Humanoid Run/Walk/Stand, particularly in mid-to-late training, consistent with the paper's prediction that gradient attenuation is a late-training phenomenon ("gradient attenuation is not severe in the early stage," Section 6.3).

5. **Low hyperparameter sensitivity and practical efficiency**: Section 6.6 reports grid-search stability across T and w_min; the bucket-based approximation (Appendix D) reduces compute overhead with no performance cost, making SWD deployable without extensive tuning.

---

## Weaknesses

### Fatal

*None.*

### Major

- **Theorem 3's core result (Θ(1/k) dominance) is formally established only at the terminal timestep h = H, not in general.** Section 4.2 reads: "By setting f̂_{H+1} ≡ 0. This eliminates the target-drift term entirely, leaving only the distributional-shift component." This is the *terminal boundary condition*, which holds for h = H by definition. For all h < H, the target f̂^k_{h+1} changes across iterations, and the target-drift term in Equation 4 is non-zero. Whether 1/k dominates the target-drift term at intermediate steps is never established. The paper's headline theoretical claim — that gradient decay scales as Θ(1/k) throughout training — thus rests on a single boundary case that corresponds to a thin slice of the actual computation. The method's empirical success suggests the intuition is sound, but the formal motivation covers only h = H; the paper does not acknowledge this limitation.

- **Competitive comparison with other plasticity methods is conducted in a single environment.** Section 6.5 compares SWD against ReGraMa, S&P, and Plasticity Injection only in Humanoid Run on DMC. Performance rankings among plasticity-targeting methods can be highly environment-specific, and a single-environment evaluation does not establish that SWD is broadly superior or complementary. This is the paper's most important competitive result, and its breadth is insufficient to support the generality claimed.

### Minor

- **ALE evaluation covers only 3 games (DemonAttack, Phoenix, Breakout).** The paper states "three ALE environments" and Figure 1(c) presents aggregate IQM for Double DQN, which could be read as characterizing ALE-scale performance. Conclusions about "consistent improvement across ALE tasks" are limited given the narrow base; the aggregate bar inherits whatever sample selection effects exist. The paper should explicitly scope its ALE claims to these three environments.

- **Section 4.1 (NTK degeneration) contains no new formal result.** The section argues that RL's warm initialization breaks the full-rank NTK guarantee of random initialization, citing Du et al. (2019) and Allen-Zhu et al. (2019). No new theorem is proved. The paper acknowledges it "focuses primarily on the second mechanism," so Section 4.1 serves mainly to retrospectively explain prior methods (reset, ReDo, noise injection). This is useful context but is presented alongside Theorem 3 as a co-equal theoretical contribution, overstating the theoretical depth of this half.

- **The claimed "neutralization" of the 1/k attenuation by SWD is intuitive but not rigorously derived.** Section 5 states SWD "neutralizes the 1/k attenuation," but Theorem 3 describes a gradient evaluated at the previous iterate, while SWD modifies the sampling distribution of the loss. These are different operations; the paper does not formally show that linear weighting by recency compensates exactly for the 1/k factor. Presenting this as a rigorous consequence rather than a motivated analogy slightly overclaims.

### Trivial

- **Figure 8 shows SWD and SWD+S&P achieving nearly identical IQM (~240) in Humanoid Run.** The paper interprets this as validating orthogonality (S&P being compatible), but the near-zero marginal gain from combining suggests limited synergy in this specific setting. The framing should acknowledge this.

---

## Nice-to-Haves

- Extend Theorem 3 to cover intermediate timesteps h < H: even an informal bounding argument showing when/whether 1/k dominates the target-drift term would substantially strengthen the theoretical core and close the gap between what is proved and what is claimed.
- Measure gradient L1 norms (as in Figure 5b) across all experimental environments in Sections 6.1–6.4, not just the SWA comparison. This would directly connect the performance improvements to the posited mechanism across the full evaluation suite.
- For Section 6.4 (UTD ratios), include confidence intervals or uncertainty bands on the Figure 7 bar chart. The observed non-monotonicity (+25.4% → +17.3% → +30.1%) would be easier to interpret with explicit uncertainty.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Harsh Critic: "SWA orthogonality claim invalidated by near-identical SWD vs SWD+S&P performance."** The paper claims orthogonality (compatibility), not synergy. SWD+S&P being the best result (even marginally) and not hurting performance supports the orthogonality framing. The absence of large synergy is a fair observation but is already noted as Trivial above.

- **Harsh Critic: "UTD section lacks confidence intervals for UTD comparison."** Moved to Nice-to-Haves as this is not standard in all RL papers and the overall trend is interpretable from the reported numbers.

- **Harsh Critic (general framing critique): "abstract overstates the theoretical contribution."** Subsumed into the Major weakness about Section 4.1 and the Minor weakness about NTK.

- **Strength Finder: "Orthogonality to existing methods" as a standalone strength.** The evidence in Figure 8 is real but the marginal improvement from SWD+S&P over SWD alone is ambiguous (nearly identical numbers). Removed from Strengths as a standalone item; it is noted in context of the Trivial weakness.

---

## Novel Insights

The paper's most genuinely novel observation is the formal decomposition in Theorem 3 (Equation 4), which isolates a *structurally inevitable* source of gradient attenuation in RL — namely, that as the replay buffer grows, the contribution of the most-recent on-policy data to the aggregate gradient is attenuated by a factor of 1/k by the averaging operation, independently of the Bellman target quality. Prior work on prioritized experience replay addresses a related problem (sample efficiency from a TD-error perspective) but does not identify or quantify this distributional-attenuation mechanism. The reverse validation via SWA (designing and testing the symmetric opposite) is a methodologically clean technique that could serve as a template for validating gradient-signal hypotheses in future RL work.

---

## Suggestions

1. **Prove or bound Theorem 3 for h < H.** Even if a full proof is unavailable, bounding |target-drift term| relative to the distributional-shift term under some mild condition (e.g., bounded target change) would establish that the 1/k term dominates in the regime relevant to the algorithm. This is the single highest-leverage improvement.
2. **Expand Section 6.5** to at least 3–4 environments for the competitive comparison, or frame Section 6.5 explicitly as a case study rather than a general claim of superiority.
3. **Explicitly scope ALE claims** to the three tested games in Section 6.1 and revise Figure 1(c)'s caption accordingly.
4. **Reframe the theory in Section 4.1** as "theoretical perspective on existing methods" rather than a co-equal contribution, and lead with Theorem 3 as the paper's primary theoretical advance.

---

## Score and Decision

**Originality**: The 1/k gradient decay mechanism is novel; the method is simple but principled. The theoretical framing is original even if incomplete. **[4/5]**

**Importance**: Plasticity loss is a central challenge in RL; a lightweight remedy with theoretical grounding is valuable to practitioners. **[4/5]**

**Claims Supported**: Empirical claims are generally well supported. The central theoretical claim (Θ(1/k) dominance) is only formally established at the terminal step; this is a real gap. **[3/5]**

**Soundness of Experiments**: Multi-algorithm, multi-suite evaluation with 5 seeds. Reverse validation is elegant. Narrow competitive comparison (1 environment) and narrow ALE (3 games) are shortcomings. **[3/5]**

**Clarity of Writing**: Paper is well organized; the intuition is clearly motivated; the boundary-case limitation of Theorem 3 is not acknowledged and should be. **[3/5]**

**Value to Research Community**: SWD is practical, orthogonal to existing methods, and easy to implement. The theoretical framework, even if incomplete, advances understanding. **[4/5]**

Overall: The paper offers a genuine, novel contribution with solid (if not comprehensive) empirical validation and a useful theoretical framing. The major weakness — that the central theorem is rigorously proved only at the terminal step — is real but does not invalidate the method or the empirical findings. The competitive evaluation being restricted to one environment is the most important experimental gap. Taken together, these issues warrant acceptance with revision requests rather than rejection; the core contribution is real and the paper advances the field.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>

<subscores>
<originality>4</originality>
<importance>4</importance>
<claims_supported>3</claims_supported>
<soundness>3</soundness>
<clarity>3</clarity>
<community_value>4</community_value>
</subscores>