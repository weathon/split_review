---
job_id: 0479017a-471a-44a4-b436-d899041d6c21
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: FDlvVdh1sB.pdf
paper: Flow-Guided Latent Refiner Policies for Safe Offline Reinforcement Learning
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, specifically offline reinforcement learning, safe RL, and generative modeling with normalizing flows.

## Minimum Quality
Pass ✅. The paper contains the required components, including abstract, introduction, methodology, experiments/results, related work, and conclusion, and it presents a complete empirical study; however, there are several technical and clarity issues that affect the final rating rather than triggering desk rejection.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find any hidden instructions, suspicious prompt-targeting text, or other manipulative content in the paper text provided.

# Expected Review Outcome:
## Summary
This paper proposes FLRP, an offline safe RL method that combines Hamilton-Jacobi-inspired feasibility critics, a conditional flow-based latent action prior, and a three-expert latent refiner operating in Gaussian base space. The stated goal is to achieve near-zero safety violations while controlling out-of-distribution action drift, and the paper supports the method with theoretical bounds on policy deviation induced by base-space KL control and experiments on DSRL benchmarks spanning Safety-Gymnasium, Bullet-Safety-Gym, and Safe MetaDrive.

## Strengths
The paper tackles a meaningful problem. Safe offline RL under hard or near-zero-violation requirements is genuinely difficult, and the paper tries to address two coupled issues at once, namely safety enforcement and OOD control, rather than treating them as separate engineering concerns.

The overall design has a coherent intuition. The combination of a feasibility estimator, a density model, and a refinement mechanism is reasonably well motivated. In particular, the choice to refine in the Gaussian base space, while freezing the decoder, gives the method a clean structural story about how policy shifts are induced and why they may be easier to control there than in action space.

The empirical scope is fairly broad. **Table 1** covers a large number of tasks across three benchmark suites, which is better than the narrow-task evaluation one often sees in safe offline RL papers. FLRP is consistently among the lowest-cost methods, and on the averaged rows it indeed achieves much lower normalized cost than several strong baselines. For example, on Bullet-Safety-Gym Avg in **Table 1**, FLRP reports cost \(0.04\) versus \(0.17\) for FISOR, \(0.88\) for LSPC, and \(1.41\) for CDT, while still maintaining competitive reward. Even where it is not the highest-return method, the safety profile is clearly strong.

The ablations do provide some evidence that the proposed components matter. **Table 2** suggests that replacing the HJ-style feasibility mechanism with the paper’s heuristic non-HJ alternative worsens safety substantially on several tasks, especially DroneRun. **Table 3** also suggests that the flow prior is not interchangeable with a plain Gaussian prior. This is useful because the flow prior is one of the main advertised pieces of the method.

I appreciated the effort to visualize the mechanism. **Figure 2** is one of the better parts of the paper because it concretely illustrates the tension among feasibility, reward, and decoder density in a 2D action space. The three panels make the authors’ motivation more tangible: the reward-improving direction is not always aligned with safety, and neither is guaranteed to align with data support. That figure helps justify why a shared regularizing refiner might be useful instead of a single monolithic latent update.

The paper also makes a decent attempt at theory. The KL contraction chain in **Lemma 3 / Equation 18** is standard but relevant, and the high-level message that a frozen decoder plus invertible flow allows one to upper bound action/policy divergence by base-space divergence is reasonable in spirit. For a paper in this area, having at least some mathematically explicit control statement is a positive.

## Weaknesses
I have substantial concerns. The paper is ambitious, but the current version overclaims on theory, leaves key parts of the method underspecified, and the empirical evidence does not fully support the stronger claims made in the introduction and conclusion.

1. **There are several mathematical inconsistencies and notation errors in the core formulation, and they are not cosmetic.**  
   On **Page 2, Eq. (1)**, the paper defines \(V_r^\pi(s)\) and then immediately defines the cost value function but again writes \(V_r^\pi(s)\) instead of \(V_c^\pi(s)\). This is a basic notation error in the problem statement. More importantly, the paper moves from an expected-cost CMDP constraint in Eq. (1) to a state-wise hard-safety requirement in **Eq. (4)**, but the relationship between these two problems is not established rigorously in the main paper. This is not a minor presentation issue, because the method’s claimed contribution is precisely about replacing soft constraints with a state-wise zero-violation perspective. If the optimization target changes, the paper needs to be much clearer about whether FLRP is solving a different problem, an approximation, or a surrogate.

2. **The feasible Bellman operator and its connection to HJ reachability are not fully convincing as presented in the main text.**  
   In **Definition 2 / Eq. (7)**, the operator is written as
   \[
   (\mathcal{P}^\star Q)(s,a) := (1-\gamma) h(s) + \gamma \max\{h(s), V^\star(s')\},
   \]
   but the dependence on the transition kernel is suppressed in the equation, while in Appendix C.2 the proof suddenly inserts an expectation over \(s'\). In the main text, the operator therefore appears deterministic in \(s'\), which is formally wrong for stochastic transitions. Also, the paper claims that as \(\gamma \uparrow 1\), this recovers the undiscounted HJ-style value from **Definition 1**, but this limit statement is delicate and absolutely depends on assumptions not stated in the main text. The main paper asks the reader to accept a fairly strong bridge between a discounted fixed-point equation and a max-over-time reachability objective without enough precision. Since feasibility estimation is the backbone of the whole method, this gap matters.

3. **The variational objective is internally inconsistent, especially around the role of the weighting function \(w(s,a)\), the KL coefficient \(\beta\), and the lemma claiming exact KL projection.**  
   In **Eq. (11)**, the objective is a safety-weighted ELBO with a coefficient \(\beta\) multiplying the KL term. Then **Lemma 1** claims the objective equals a KL projection under the weighted empirical distribution. But in the appendix the proof works cleanly only for \(\beta=1\), and for \(\beta \neq 1\) it changes the prior to a temperature-adjusted prior \(p_\phi^{(\beta)} \propto p_\phi^\beta\). That is not the same statement as the main-paper lemma. The main text presents a neat variational interpretation for the actual training loss, while the proof quietly proves a different statement unless one modifies the model class. This is exactly the sort of theoretical slippage that papers in this area should avoid.

4. **The prior-shaping loss in Eq. (12) is underspecified and likely flawed in notation.**  
   The expression
   \[
   \mathcal{L}_{\text{shape}}=\mathbb{E}\left[\exp(Q_r(s,a)-V_r(s)/\beta_r)\cdot \mathbf{I}_{\text{feas}}(s,a)\cdot \|T_\phi^{-1}(z_q \mid s)\|^2\right]
   \]
   is ambiguous. As written, the exponent is \(Q_r(s,a)-V_r(s)/\beta_r\), not \((Q_r(s,a)-V_r(s))/\beta_r\), which changes the scaling substantially. The paper then says this “encourages the flow prior to assign higher and smoother base-space density,” but minimizing \(\|u\|^2\) for selected posterior codes is only a very indirect proxy for density shaping, and the exact mechanism is not explained. Also, \(z_q\) comes from the posterior recognizer, but the text says “maps a decoded action back to the latent base space,” which is a different object. This section needs a much sharper mathematical definition of what distribution is being shaped and why the chosen penalty corresponds to higher prior density in a principled way.

5. **The central OOD-control claims are stronger than what the theory really supports.**  
   The paper repeatedly suggests “explicit, tunable guarantees on distribution shift” and even ties this to OOD suppression. However, **Lemma 2** introduces a bounded density-ratio term \(R_\theta(s)\), and the final bound becomes
   \[
   D_{\mathrm{KL}}(\Pi_\theta \| \pi_\beta) \le D_{\mathrm{KL}}(q_u\|\mathcal N) + \log R_\theta(s).
   \]
   The second term is not controlled by the training objective and is not estimated in experiments. So the practical controllability is only partial. Similarly, **Corollary 1 / Eq. (20)** gives an OOD-mass upper bound involving both the base KL and \(\operatorname{TV}(\pi_0,\pi_\beta)\), but again the latter is not measured. In short, the paper has a nice symbolic chain, but the actual end-to-end OOD guarantee depends on mismatch terms that are neither bounded nor empirically diagnosed. The rhetoric of “explicit OOD control” is therefore overstated.

6. **The shared refiner regularizer does not actually optimize the KL quantity featured in the theory.**  
   The theory revolves around \(D_{\mathrm{KL}}(q_u\|\mathcal N)\), but the implemented shared loss in **Eq. (16)** is
   \[
   \mathcal L_{\text{sh}}=\|u_T\|^2+\|u_T-u_0\|^2.
   \]
   This is at best a heuristic surrogate. It does not define a distribution \(q_u\), does not estimate KL, and does not obviously upper bound KL unless one imposes additional parametric assumptions on the refined latent distribution. The paper leans heavily on the theoretical story that “keeping base KL small controls everything downstream,” but the actual optimization does not appear to compute or constrain that KL. This disconnect between theory and algorithm weakens one of the paper’s main claims.

7. **There are multiple objective-definition issues in the refiner section, making the training procedure difficult to reconstruct precisely.**  
   In **Eq. (14)**, the expectation is written over \(s,a \sim \mathcal D\), but the weight is then defined as \(w_h(s)\) and depends on \(\bar a\), not on dataset action \(a\), while the displayed formula includes \(w_h(s,a)\). The indicator \(\mathbf{I}_{\text{feas}}\) is introduced earlier as \(\mathbf{1}\{Q_h(s,a)\le 0\}\), but here it seems intended to apply to the refined action, not the dataset action. In **Eq. (15)**, the reward loss uses \(\tilde a(s,u_T)\), but this symbol was not the one defined above; elsewhere the decoded mean is \(\bar a(s,u_T)\). The formula also contains \(\lceil Q_r(s,a)-V_r(s)\rceil/\beta_r\), which looks like a ceiling operator, almost certainly not what was intended. There is also a typo \(\mathbf{I}_{\text{feat}}\) instead of \(\mathbf{I}_{\text{feas}}\). These are not isolated typos anymore. In the core training objectives, such inconsistencies make it hard to know what was actually implemented.

8. **Algorithm 1 does not match the method description in an important way.**  
   The main text in **Section 3.3** emphasizes *sequential* refinement steps by safety, reward, and shared experts, and **Figure 3** is explicitly about the order of those refiners. But **Algorithm 1** on **Page 26** trains the three refiners independently from the same base code \(u_q\), with separate updates for \(R_s\), \(R_r\), and \(R_{\text{sh}}\), rather than showing the sequential composition \(u \to R_s \to R_r \to R_{\text{sh}}\). This mismatch matters because the claimed benefit of the method is precisely the ordered, decoupled refinement process. If training is independent while inference is sequential, the paper should say so explicitly and justify why this mismatch is sensible. Right now the algorithm and the narrative do not line up cleanly.

9. **The empirical results are interesting but not as decisive as the writing suggests, especially on return.**  
   **Table 1** shows that FLRP is usually very safe, but it is not uniformly competitive on reward. On Safety-Gym Avg, FLRP’s reward \(0.33\) is well below CDT’s \(0.51\). On MetaDrive Avg, FLRP gets reward \(0.34\), far below LSPC’s \(0.71\) and even below BCQL’s \(0.64\), though with much lower cost. So the method is best described as a strongly conservative safe method, not one that “matches or outperforms baselines in return” in any broad sense. The paper should present the result as a sharper safety-first trade-off rather than implying dominance on both axes. This matters because acceptance at ICLR should hinge on what the method actually demonstrates, not on optimistic framing.

10. **The comparison protocol may not be fully fair or sufficiently informative for a paper centered on hard-safety claims.**  
   The paper states in **Section 4** that it uses a uniform cost limit of 10 for all tasks, while earlier in the method section it says the focus is the zero-cost-budget case \((\ell=0)\). The connection between training for state-wise zero violation and evaluating under normalized cost with \(\kappa=10\) is not discussed carefully. Also, reporting only normalized reward/cost can hide absolute violation counts and variance in a hard-safety setting. Since the pitch is “near-zero violation,” I would expect clearer reporting of actual violation frequency or proportion of fully safe episodes, not just normalized aggregate cost. The authors do mention three seeds and ten evaluation episodes per seed in the appendix, which is a rather small evaluation budget for noisy RL benchmarks.

11. **Some ablations are useful, but others expose weaknesses rather than strengthen the case.**  
   **Figure 3** does support the claim that order matters, but the pattern is not entirely stable across tasks, and the paper does not report whether the chosen default order is the one used in all main experiments or whether it was tuned. Also, **Table 3** is more mixed than the text implies. On CarButton1 and CarButton2, the Gaussian prior variant actually has *lower* cost than the flow prior, though lower reward too. So the flow prior is not a straightforward win on safety, and the claim that it “consistently yields higher returns and lower costs” is simply false from the table itself. This kind of overstatement hurts trust.

12. **The paper’s positioning relative to prior latent-manifold offline RL is not fully convincing.**  
   The closest prior work cited by the authors already includes flow-based offline RL and latent-space safe offline RL, notably CNF, LSPC, and FISOR. The paper does explain its intended distinction in **Table 4**, but the claimed originality is still somewhat incremental: flow prior + safety critic + latent refinement + decoder freezing. I am not saying there is zero novelty, but the paper should do a better job of isolating exactly which piece is new algorithmically versus a recombination of existing ingredients. At present, the method feels like a fairly elaborate composition of known ideas, and the empirical gains, while real on safety, are not strong enough to settle the novelty question by themselves.

13. **Presentation quality is uneven, with enough notation and typo issues to impede technical assessment.**  
   There are many small but cumulative problems: inconsistent use of \(\pi_\theta\), \(\Pi_\theta\), and \(\pi_0\); switching between \(T_\phi\), \(f_\phi\), and \(g_\theta\); repeated typos like “iI”, “feat”, malformed expectations, and grammar issues in theorem statements and proofs. **Figure 1** gives the high-level pipeline, but even there the notation \(p_\phi(z|,u)\) appears malformed. Because this paper makes several technical claims, this level of sloppiness is more damaging than it would be in a purely empirical submission.

## Questions
1. The theory repeatedly relies on \(D_{\mathrm{KL}}(q_u\|\mathcal N)\), but the implemented shared loss in **Eq. (16)** is only \(\|u_T\|^2+\|u_T-u_0\|^2\). Can the authors clarify what family of refined distributions \(q_u\) they assume, and whether Eq. (16) is intended as an upper bound, proxy, or merely heuristic regularizer for the base KL? A precise derivation here would materially increase my confidence.

2. Please clarify the exact refiner training procedure relative to **Algorithm 1** and **Section 3.3**. Are the three refiners trained independently from the same posterior sample \(u_q\), or are they trained in the same sequential order used at inference? If the former, why should the theoretical and empirical conclusions about order transfer cleanly?

3. In **Eqs. (12), (14), and (15)**, several symbols appear inconsistent or malformed. Please provide the exact implemented formulas, with unambiguous parentheses and indicator definitions, especially for the reward-advantage exponent, the feasibility mask, and whether the losses use dataset action \(a\) or refined action \(\bar a\). This is important because these losses define the method.

4. The jump from the expected-cost CMDP in **Eq. (1)** to the state-wise hard constraint in **Eq. (4)** is central. Can the authors explain in the rebuttal whether FLRP is solving a different optimization problem than the baselines, or whether they view Eq. (4) as a surrogate for Eq. (1)? If it is a different problem, the empirical comparison should be framed more carefully.

5. Since the paper emphasizes “explicit OOD control,” can the authors report any empirical proxy for the theory’s extra mismatch terms, such as \(\operatorname{TV}(\pi_0,\pi_\beta)\), estimated action-support distance, decoder likelihood under learned policies, or some measured OOD-action rate? This would make the theory much more credible in practice.

6. For **Table 1**, can the authors provide uncertainty estimates on the averaged rows and perhaps absolute safety metrics, such as fraction of violation-free episodes? For a hard-safety paper, normalized cost alone is not enough to understand whether “near-zero violation” really holds.

7. In **Table 3**, the text says the flow prior “consistently yields higher returns and lower costs,” but the cost is worse for the flow prior on some tasks such as CarButton1 and CarButton2. Please revise the claim or explain what notion of consistency is intended.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
None beyond standard caution that safe RL methods can be over-interpreted if deployed in real systems without robust external validation. The paper’s experiments are simulation-only and do not raise a specific ethics flag on their own.

## Soundness Rating
2: fair. The paper has a plausible method and nontrivial experiments, but the technical claims are weakened by inconsistencies in the loss definitions, gaps between theory and implementation, and some overstated conclusions.

## Presentation Rating
2: fair. The overall structure is complete, but notation errors, objective-definition ambiguities, and mismatches between the algorithm and the text materially hurt readability and confidence.

## Contribution Rating
2: fair. The problem is important and the safety results are interesting, but the methodological novelty feels moderate and the evidence does not fully support the paper’s stronger claims about explicit OOD control and broad return competitiveness.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted. The paper has a real idea and some promising safety-first empirical results, but in its current form I do not think the technical presentation and support are strong enough for ICLR main track. Too many core pieces are underspecified or overclaimed, and the theory-to-algorithm connection needs tightening.

## Reviewer Confidence
4: confident. I am confident in this assessment, though not absolutely certain. The paper is in my area, and I checked the equations, tables, and the main theoretical claims carefully, but some implementation specifics remain unclear from the manuscript.