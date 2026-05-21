---
job_id: 0718fe35-904f-4b7b-8c87-9d3d34bebe0e
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: SzXDuBN8M1.pdf
paper: TD-JEPA: Latent-Predictive Representations for Zero-Shot Reinforcement Learning
main_score_norm: 0.8
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is squarely in scope for ICLR, combining self-supervised representation learning, reinforcement learning, learning theory, and applications to zero-shot control from offline data.

## Minimum Quality
Pass ✅. The paper contains all core scientific components, including abstract, introduction, method, theory, experiments with quantitative results, related work, and conclusion; it presents a technically substantial method with nontrivial analysis and broad empirical evidence, despite some limitations and clarity issues.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find any hidden instructions, suspicious reviewer-directed text, or other manipulative content in the provided paper text and figures.

# Expected Review Outcome:
## Summary
This paper proposes TD-JEPA, a latent-predictive method for zero-shot unsupervised RL that learns from offline, reward-free transitions. The core idea is to replace standard one-step latent prediction with a policy-conditioned temporal-difference objective that learns a state encoder, a task encoder, latent predictors, and latent-parameterized policies jointly, so that the predictor approximates successor features in latent space and can be used for zero-shot policy extraction at test time. The paper also provides a tabular-linear theoretical analysis relating the proposed losses to low-rank approximation of successor measures, non-collapse under idealized dynamics, and bounded policy-evaluation error, and evaluates the method across ExoRL/DMC and OGBench with both proprioceptive and pixel observations.

## Strengths
1. The paper has a clear and coherent high-level idea. The connection between JEPA-style latent prediction and successor-feature-based zero-shot RL is not cosmetic; it is central to the algorithmic design. In particular, the progression from Eq. (5) to Eq. (7), then to the asymmetric variant in Eq. (8)-(9), and finally to the zero-shot policy extraction mechanism in Section 3.3, is conceptually well motivated.

2. The method is technically interesting because it moves beyond the usual one-step or single-policy self-predictive setup. The proposed TD loss in **Equation (7)** is a meaningful extension: it uses off-policy one-step transitions while targeting long-term, policy-conditional latent structure. This is the main technical contribution of the paper, and it is a sensible one for offline zero-shot RL.

3. The theoretical section is stronger than what is typical for papers in this space. The analysis is admittedly idealized, but it is still substantial. **Theorem 1** and **Theorem 3** do more than gesture vaguely toward intuition; they explicitly connect the latent-predictive losses to low-rank approximation objectives over successor measures. **Theorem 2** also gives a concrete non-collapse statement in the fast-predictor continuous-time regime. Even if these assumptions are restrictive, the theory is not fluff.

4. The paper does a good job articulating the role of separate state and task encoders. This is not just an architectural flourish. The argument in Section 3.2 is reasonable, and the empirical comparison to the symmetric variant partially supports it.

5. The empirical evaluation is broad. **Table 1** reports results across 13 datasets and multiple modalities, and the method is competitive essentially everywhere while being particularly strong in visual settings. This breadth matters, because many zero-shot RL papers look good on one benchmark family and brittle elsewhere. Here, TD-JEPA appears consistently strong rather than cherry-picked.

6. More specifically, **Table 1** supports one of the paper’s main empirical claims, namely that TD-JEPA is especially effective from pixels. On **DMCRGB (avg)**, TD-JEPA achieves \(628.8 \pm 5.5\), ahead of BYOL-\(\gamma^*\) at \(582.4 \pm 9.8\), RLDP at \(525.7 \pm 13.3\), and FB at \(456.2 \pm 8.6\). On **OGBenchRGB (avg)**, TD-JEPA is essentially tied for the top group at \(41.34 \pm 0.45\), with BYOL-\(\gamma^*\) at \(41.58 \pm 0.64\) and BYOL* at \(40.33 \pm 0.52\). That is a strong showing in the regime where representation quality matters most.

7. The figures are actually useful rather than decorative. **Figure 1** communicates the central intuition cleanly, namely that the predictor trained with TD approximates a discounted barycenter of future latent features, aligning the method with successor features. This figure materially improves readability because the actual equations can otherwise feel abstract. **Figure 2** is also informative: the probability-of-improvement presentation helps demonstrate consistency across domains rather than relying only on suite averages, which can hide uneven behavior.

8. The ablations are relevant to the claimed contributions. **Figure 3 (left)** directly probes the central claim that policy-aware multi-step prediction is preferable to modeling the behavior policy, and **Figure 3 (right)** addresses the separate-state/task-encoder choice. The adaptation study in **Figure 4** also adds value by showing that the learned state representations are usable beyond the zero-shot setting.

9. The paper is well positioned relative to closely related lines such as FB, HILP, RLDP, BYOL-\(\gamma\), and ICVF. I appreciated that the authors do not pretend to have invented zero-shot RL from latent prediction ex nihilo; they make the relationship to successor-feature methods explicit.

## Weaknesses
1. The main theoretical guarantees rely on assumptions that are much stronger than the practical setting, and the paper does not fully bridge that gap in the main text. In **Theorem 1** and **Theorem 3** on **Pages 5-6**, the key assumptions include orthonormal representations, uniform state distribution, and, most notably, symmetric \(P^{\pi_z}\). That last one is especially restrictive for controlled MDPs and seems misaligned with the practical domains considered later, where transition structure is neither reversible nor symmetric in any meaningful sense. The paper acknowledges in passing that assumptions can be relaxed in the appendix, but the main-paper takeaways remain somewhat optimistic given how far the theory is from the deep visual-control regime. This matters because the theory is used to motivate claims such as “sound approach for zero-shot policy evaluation” in Section 4, yet the supporting statements are only established under highly stylized conditions.

2. The non-collapse analysis in **Theorem 2** is interesting but idealized to the point that its practical relevance remains uncertain. The theorem assumes a continuous-time relaxation in which predictors are optimized to stationarity at every step before representation updates are taken. That is a very strong two-timescale assumption. In actual **Algorithm 1** on **Page 5**, all components are updated jointly with SGD/Adam using target networks and EMA, not exact predictor minimization. The theorem therefore establishes a property of a different dynamical system than the one actually trained. This is not fatal, but the paper should be more careful in how strongly it ties the theorem to practical collapse avoidance, especially since the algorithm also depends on explicit orthonormality regularization.

3. There is some mathematical sloppiness and notation drift in important places. On **Page 3**, the definition of \(T_\phi\) near the start of Section 3.1 appears corrupted or malformed, “\(T_\phi := \mathcal{D}\in \mathcal{S}\times\mathcal{D}\) ...”, which makes the predictor definition harder to parse. In Section 3.3 on **Page 5**, the policy is described as \(\pi_z(\phi(s)) = \arg\max_a T_\phi(\phi(s), z, a)^\top z\), whereas earlier the predictor arguments are written as \((\phi(s), a, z)\). This argument ordering inconsistency is minor syntactically, but here it touches the core object of the paper. A method paper that leans heavily on formal definitions should be cleaner than this.

4. The zero-shot framing is slightly stronger in rhetoric than in the actual protocol. At test time, the method still requires a reward-labeled inference dataset \(\mathcal{D}_{\mathrm{rwd}} = \{(s,r)\}\) and then solves a linear regression problem to obtain \(z_r\), as stated in Section 3.3 on **Page 5**. That is standard in this literature, but it is not “any reward function at test time” in an unrestricted sense. It is “any reward for which a useful linear fit on top of \(\psi\) can be inferred from reward-labeled samples.” The paper partially addresses this in **Theorem 4**, but the practical limitations of this protocol should be spelled out more directly in the empirical discussion. Otherwise, the framing risks sounding broader than the actual deployment scenario.

5. Some of the empirical gains are real but not as decisive as the narrative suggests. **Table 1** shows clear wins in DMCRGB, but the picture is more mixed elsewhere. For example, on **OGBenchRGB (avg)** TD-JEPA at \(41.34 \pm 0.45\) is slightly below BYOL-\(\gamma^*\) at \(41.58 \pm 0.64\), and on **OGBench (avg)** TD-JEPA ties HILP at \(37.98\) while remaining below FB on some antmaze tasks, especially **antmaze-me**, where FB has \(51.60 \pm 2.65\) versus TD-JEPA’s \(20.20 \pm 2.39\). The paper is careful enough to say “matches or outperforms,” which is fair, but parts of the surrounding prose still give the impression of a more uniform dominance than the numbers support.

6. The baseline comparison is broad, but the analysis of why TD-JEPA helps is still somewhat confounded by several moving parts. The method introduces a TD latent-predictive objective, explicit state and task encoders, asymmetric training, target networks, orthonormal regularization, and a particular actor training rule. **Figure 3** helps, but it does not fully isolate which component contributes what across the benchmark families. In particular, since the symmetric variant in **Figure 3 (right)** is often fairly close, the practical advantage of the full asymmetric formulation feels somewhat narrower than the main narrative suggests.

7. I found **Figure 2** helpful, but also a bit too aggregated to fully diagnose where the method is actually stronger. Probability of improvement is a nice summary statistic, yet it compresses away the magnitude and task structure of gains. In a paper that emphasizes robustness across very heterogeneous suites, some additional main-text decomposition by domain type or dataset coverage would make the claim more convincing. Right now one still has to stare at **Table 1** and reconstruct the story manually.

8. The exposition in the theory section is dense and sometimes too compressed for the paper’s own good. For example, **Theorem 4** on **Page 6** jumps from successor-measure approximation error to a max-over-rewards value-function bound, then adds the statement that \(\mathcal{L}_{\mathrm{SM}}\le c\mathcal{L}_{\mathrm{fw}}\) and \(\mathcal{L}_{\mathrm{SM}}\le c\mathcal{L}_{\mathrm{low}}\) “for some \(c\).” The appendix later gives \(c = \frac{S}{(1-\gamma)^2}\), but the main text leaves this abstract. Since the dependence on \(S\) and \((1-\gamma)^{-2}\) is not innocent, hiding it in the main paper blunts the interpretability of the result.

9. There is a small but annoying mismatch between theory and practice regarding the asymmetric update. In Section 3.2, the text motivates training \(\psi\) symmetrically through an inverted latent-predictive objective. But later, Section 5 explicitly notes that the practical TD-JEPA objective is not bi-directional in the same sense as BYOL-\(\gamma\). The appendix clarifies this, but the main paper could better separate what is theoretically clean, what is implementable off-policy, and what the actual algorithm does. As written, these layers are easy to conflate.

## Questions
1. The biggest issue I would like clarified is the role of the symmetry assumption in the theory. In **Theorem 1** and **Theorem 3**, the main-text results require symmetric \(P^{\pi_z}\). Can the authors explain, in a concise main-paper way, which parts of the theoretical story survive without symmetry, and whether the practical algorithm should be thought of as approximating the “forward” part only? A sharp answer here would increase my confidence in how much of Section 4 genuinely applies to the implemented method.

2. In **Section 3.3** and **Algorithm 1**, the test-time reward inference step assumes a linear fit \(r(s)\approx \psi(s)^\top z_r\) from a reward-labeled dataset. How many reward-labeled samples are used in the experiments for this inference step, and how sensitive are results to that number? This is important for interpreting the actual difficulty of the “zero-shot” protocol.

3. **Table 1** shows that the method is strongest in visual domains, but more mixed on some proprioceptive OGBench tasks. Do the authors have evidence that the advantage comes primarily from representation learning rather than from the particular actor or regularization choices? A sharper ablation where the actor-learning and regularization pipeline is held fixed and only the representation objective is changed would help isolate the contribution.

4. Could the authors clarify the malformed notation at the start of **Section 3.1** and the argument-order inconsistency in **Section 3.3** for \(T_\phi\)? This is not a conceptual objection, but the current notation around the predictor is unnecessarily confusing.

5. In **Figure 3 (right)**, the asymmetric method tends to outperform the symmetric one, but often by modest margins. Under what practical conditions should a user prefer the full asymmetric TD-JEPA over the simpler symmetric variant? If the answer is mostly “pixels and more heterogeneous tasks,” that would be useful to state explicitly.

6. Since **Figure 4** suggests that the learned \(\phi\) is reusable for downstream adaptation, it would be useful to know whether the gains persist if one removes the zero-shot actor initialization and reuses only the representation. If this comparison already exists in the supplementary material, a short summary in rebuttal would help.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
No specific ethics concerns are raised by the paper as written. The work uses standard simulated RL benchmarks and does not involve human subjects, sensitive personal data, or deployment claims that would by themselves require ethics review.

## Soundness Rating
3: good. The core method is technically sensible and supported by substantial experiments, and the theoretical analysis is meaningful within its assumptions. I am not at 4 because the practical-theoretical gap is real, and several claims are established only in idealized settings.

## Presentation Rating
3: good. The paper is generally well written and well structured, with useful figures and a comprehensive empirical section. I am not higher because notation is sometimes inconsistent, the theory section is dense, and a few crucial points require appendix-level clarification.

## Contribution Rating
4: excellent. The paper makes a strong contribution at the intersection of latent-predictive representation learning and zero-shot RL, especially through the policy-conditioned TD formulation and the empirical breadth across offline visual-control settings.

## Overall Rating
8: Accept, good paper (poster). I have real reservations about how far the theory reaches beyond the stylized setting, and the zero-shot framing should be described a bit more carefully. Still, the central idea is strong, the empirical evidence is broad and convincing, and the paper offers a meaningful advance over existing latent-predictive and successor-feature approaches.

## Reviewer Confidence
4: confident. I am confident in the assessment and checked the main derivations and empirical claims carefully, though some appendix-level generalizations were not verified line by line.