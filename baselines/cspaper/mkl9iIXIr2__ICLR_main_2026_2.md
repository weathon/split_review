---
job_id: 189d2e27-38a7-402b-ac3c-6bd4b0c7d711
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: mkl9iIXIr2.pdf
paper: Online Inventory Optimization in Non-Stationary Environment
main_score_norm: 0.6
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope through online learning, optimization, and learning theory, with a sequential decision-making formulation connected to OCO and SOCO.

## Minimum Quality
Pass ✅. The paper contains the required scientific components, including abstract, introduction, related work, methodology, theoretical analysis, experiments, and conclusion, and it presents a technically substantial contribution with nontrivial proofs and empirical support, even though some aspects remain underexplained.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find any hidden prompts, manipulative instructions, or suspicious text targeting automated review behavior in the provided manuscript content.

# Expected Review Outcome:
## Summary
This paper studies online inventory optimization in non-stationary environments and argues that static regret is the wrong benchmark when demand varies over time. The main contribution is a two-stage projection algorithm that reduces OIO to a smoothed online convex optimization problem, leading to dynamic regret bounds of order \(\tilde{\mathcal O}(\sqrt{L_{\max}(1+P_T)T})\), plus a matching-in-order static lower bound \(\Omega(\sqrt{L_{\max}T})\). The paper also provides an algorithmic instantiation based on OGD/SOGD together with a doubling trick for unknown \(L_{\max}\), and includes a small synthetic experiment comparing against MaxCOSD.

## Strengths
1. The paper tackles a genuinely relevant gap in the OIO literature. The motivation in Section 1 is convincing: for inventory systems under drifting demand, static regret against a fixed comparator is often too weak to reflect meaningful adaptation. The simple example on Pages 1 to 2 makes this point well.

2. The main technical idea, namely separating the unconstrained base learner decision \(\hat y_t\) from the feasible inventory decision \(y_t=\Pi_{\mathcal C(x_t)}(\hat y_t)\), is interesting and conceptually clean. The reduction from OIO to an SOCO-style regret decomposition in Equation (8) is the core insight of the paper, and it is one of the stronger parts of the submission.

3. The paper does more than just give an upper bound. The lower bound in Theorem 5 is important because it argues that the \(\sqrt{L_{\max}}\) dependence is not an artifact of analysis. Relative to prior OIO work that appears to incur \(L_{\max}\sqrt T\)-type static regret, the stated \(\tilde{\mathcal O}(\sqrt{L_{\max}T})\) static guarantee is a meaningful improvement.

4. Table 1 on Page 3 is useful. It gives a compact comparison to prior inventory-learning papers across setting, assumptions, and regret rate. Even though some entries require careful interpretation, the table helps position the paper and makes the intended improvement visible, especially the contrast between prior \(O(L_{\max}\sqrt T)\) static bounds and the paper’s \(O(\sqrt{L_{\max}T})\) static bound.

5. There is substantial technical content. The authors do not stop at an informal theorem statement; they provide a full chain from the cycle-based projection analysis to a generic base-learner theorem (Theorem 2), then instantiate it with OGD and SOGD. The appendix contains the missing proof details rather than hand-waving away the main argument.

6. The synthetic experiment, while limited, does at least align qualitatively with the main claim. In Figure 1 on Page 27, both proposed methods, especially the SOGD-based variant, show much slower regret growth than MaxCOSD as \(T\) increases. The separation is visually large and consistent with the argument that dynamic adaptation matters in fluctuating demand.

## Weaknesses
1. The empirical section is much too thin for the breadth of the claims. The paper’s main pitch is “online inventory optimization in non-stationary environments,” but the experiments in Appendix I / Page 26 to 27 evaluate only a single-item synthetic sinusoidal demand process with a single Newsvendor loss and a single baseline, MaxCOSD. There is no multi-item experiment, despite the main formulation and theory being multi-item; no experiment under adversarial or abruptly shifting demand, despite the adversarial framing in Section 3; no sensitivity study in \(L_{\max}\), \(P_T\), or dimension \(N\); and no runtime or restart analysis. This matters because the proposed algorithm is positioned as a general method for OIO under non-stationarity, yet the empirical evidence only supports a very narrow corner case.

2. The comparison set is not strong enough to support the practical claims. Since the paper’s main mechanism is “OIO via SOCO,” one would expect comparisons not only to MaxCOSD but also to simpler projected OGD-style heuristics, ablations without the doubling trick, and ideally a variant that directly uses the unconstrained base learner without the projection correction. As it stands, Figure 1 only shows proposed OGD/SOGD variants versus MaxCOSD, which makes it hard to tell whether the gains come from the dynamic-regret design, from the particular synthetic demand, or simply from having tuned update behavior for a drifting sinusoid. A paper making such strong algorithmic claims should do more than beat one older baseline in one friendly setting.

3. Figure 1 itself raises questions that the text does not answer. The solid curves, which correspond to the doubling-trick versions, sometimes outperform the dashed curves that are given \(L_{\max}\) information. The authors briefly explain this by saying the known-\(L_{\max}\) learner uses a smaller learning rate and adapts more slowly, but this deserves a much more careful unpacking. If the “oracle” knowledge variant is routinely worse, that suggests either the parameterization is conservative, the finite-time constants are unfavorable, or the practical story is more nuanced than the theory suggests. The figure is thus interesting, but also underanalyzed.

4. The scope and interpretation of Table 1 need more care. The caption states that regret bounds from prior work are “replaced” using the paper’s indicator \(L_{\max}\), but the main paper does not explain in enough detail how these translations are done and what assumptions are needed for them to be comparable. In particular, the papers listed differ in item setting, demand assumptions, losses, capacity constraints, and sometimes lead-time structure. Presenting them all in one table is helpful, but it also risks implying apples-to-apples comparability that is not fully justified in the main text. Because Table 1 is central to the novelty positioning, this matters.

5. Some key assumptions are restrictive and their practical meaning is somewhat buried. The entire analysis depends on the sell-out period \(L_{\max}\) from Definition 1 on Page 5, which effectively rules out long periods of low demand. The paper does acknowledge on Page 6 that sublinear regret is impossible when \(L_{\max}=\Omega(T)\), which is fair, but the narrative sometimes presents the assumption as mild without really discussing when realistic inventory systems would satisfy it, especially in multi-item settings where a single slow-moving item can dominate the guarantee. The gap between theory and realistic demand processes could have been discussed more honestly.

6. The paper states an adversarial environment in Section 3, but the comparator and environment model are not fully reconciled in the main text. On Page 6, the authors note that if one adopts a feasible comparator satisfying \(\max(0,u_t^i-d_t^i)\le u_{t+1}^i\), then \(P_T\) becomes bounded, and they defer details to the appendix. But the main dynamic regret result in Theorem 1 is stated for any comparator sequence \(u_1,\dots,u_T\in\mathcal C(\mathbf 0)\), not just feasible state-consistent ones. This is mathematically stronger, but also potentially misleading from an inventory perspective, because unconstrained comparator variation can be disconnected from any realizable inventory policy. The paper should better explain what class of comparator sequences is meaningful in applications and how the stated guarantee should be interpreted.

7. There are several places where the mathematical presentation is harder to trust than it should be, even if the broad argument may be correct.

   - In Equation (7) on Page 7, the bound is written with \(L_t^i\) and \(\|\hat y_t-\hat y_{t+1}\|_1\), but the subsequent SOCO interpretation in Equation (8) uses \(L_t^*\) as if it were an observable switching-cost coefficient. The very next paragraph then says this coefficient is time-dependent and delayed in observability. This is not a contradiction, but the transition from a hindsight quantity in the proof to an implementable algorithm is not especially crisp in the main text.
   - Theorem 2 on Page 8 assumes a decomposition \(\mathcal R_{L,T}^{\mathcal E(L,T)}=L^\alpha \mathcal R(T)\) and a switching bound \(\|\hat y_t-\hat y_{t+1}\|_1\le \mathcal O(L^{-\beta})\). These are quite specific regularity assumptions on the base learner, yet they are stated abstractly and verified only later for the particular OGD/SOGD instances. The theorem is therefore less general than it initially sounds.
   - Theorem 3 requires \(T\ge L_{\max}(3+P_T/D)\), while Theorem 4 requires \(T\ge \sqrt{L_{\max}}(\log_2 T+e)\). These side conditions are not discussed much in the main text. In particular, the statement “without knowing \(L_{\max}\) and \(P_T\) a priori” in Theorem 1 is only fully realized by the SOGD-based construction, not by the OGD instantiation in Theorem 3, which still needs \(P_T\) to tune \(\eta\).
   - There are also several notation and transcription issues in Algorithms 3 to 5 on Page 9. For example, Algorithm 3 line 3 writes \(y_{t+1}=\Pi_{\mathcal C(\mathbf 0)}(y_t-ng_t)\), which presumably means \(\eta g_t\), not \(ng_t\). In Algorithm 5, line 17 says “Return \(g_{t+1}=v^K_{t+1}\),” which almost surely should be \(y_{t+1}=v^K_{t+1}\) or an equivalent decision variable, not a gradient. These may be typographical issues, but in a theory-heavy paper, such slips weaken confidence.

8. The lower bound is interesting but not perfectly aligned with the dynamic-regret headline. Theorem 5 is a static comparator lower bound of \(\Omega(GD\sqrt{L_{\max}T})\), and Corollary 1 is then used to claim an SOCO lower bound. This supports the static part of the story and the necessity of \(\sqrt{L_{\max}}\), but it does not directly show a dynamic-regret lower bound that matches \(\tilde{\mathcal O}(\sqrt{L_{\max}(1+P_T)T})\). Since dynamic regret is the main advertised contribution, the lower-bound discussion is a bit less complete than the introduction suggests.

9. The presentation quality is uneven. The overall structure is reasonable, but the paper relies heavily on appendix-only details to make the main proof line believable, and there are multiple language issues, notation overload, and formatting glitches. For instance, the algorithm blocks on Pages 6 to 9 are harder to parse than they should be, some symbols appear before being fully contextualized, and the connection between the informal theorem, the generic theorem, and the instantiated theorems is not as streamlined as it could be. This does not make the paper unsound, but it does make it more work than necessary for the reader.

10. The practical relevance is asserted more than demonstrated. The introduction frames the problem as highly relevant to real-world inventory management, but the algorithm is only evaluated on synthetic data and the method depends on observing subgradients of convex losses. Remark 1 gives one plausible route for Newsvendor-style gradients under censored demand, which is appreciated, but the broader claim of practical applicability would be stronger with either more realistic simulations, a real dataset, or at least a fuller discussion of how subgradients are obtained for general convex losses in multi-item systems.

## Questions
1. The main theorem is stated for arbitrary comparator sequences \(u_t\in \mathcal C(\mathbf 0)\), but some discussion later suggests state-consistent comparators are especially meaningful in inventory systems. Could the authors clarify which comparator class they believe is the right practical benchmark, and whether the guarantee changes if one restricts to feasible inventory trajectories satisfying \(\max(0,u_t^i-d_t^i)\le u_{t+1}^i\)?

2. Can the authors provide more intuition for Lemma 1 and Equation (7), specifically why the projection-induced discrepancy \(\sum_t \langle g_t, y_t-\hat y_t\rangle\) scales with cumulative switching of \(\hat y_t\) weighted by cycle lengths? This is the paper’s central bridge to SOCO, and a small worked example would increase confidence substantially.

3. In Theorem 2, the assumptions \(\mathcal R_{L,T}^{\mathcal E(L,T)}=L^\alpha \mathcal R(T)\) and \(\|\hat y_t-\hat y_{t+1}\|_1\le \mathcal O(L^{-\beta})\) are fairly special. Are there natural SOCO base learners beyond OGD/SOGD that satisfy these conditions? If not, the authors should probably present Theorem 2 more as an OGD/SOGD-oriented template than as a general reduction.

4. For Theorem 3, the learning rate depends on \(P_T\), which is generally unknown. How sensitive is performance to misspecification of \(P_T\)? A short empirical sweep or theoretical robustness remark would help.

5. Figure 1 shows that the doubling-trick variants sometimes beat the versions with access to \(L_{\max}\). Could the authors quantify how often this happens and whether it is due to conservative parameter tuning, restart benefits, or artifacts of the specific sinusoidal demand? Right now the explanation is plausible but a bit hand-wavy.

6. Could the authors add experiments beyond the single-item sinusoidal case, in particular:
   - a genuinely multi-item setting,
   - an abrupt piecewise-stationary or adversarial demand sequence,
   - an ablation comparing projected versus unprojected base learner outputs,
   - and a comparison against a simpler dynamic OGD-style heuristic?
   Positive evidence on even two of these would materially increase my confidence.

7. Table 1 is useful, but the translation of prior bounds into the \(L_{\max}\) notation is important for positioning. Can the authors make explicit in the main text, not only in supplementary discussion, how each listed bound is mapped and what assumptions are required for comparability?

8. There appear to be notation issues in Algorithms 3 and 5 on Page 9, such as \(y_t-ng_t\) and “Return \(g_{t+1}=v^K_{t+1}\).” Please confirm whether these are typographical errors and provide corrected pseudocode.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
No ethics concerns identified from the paper content. The work is theoretical/algorithmic and uses synthetic experiments only.

## Soundness Rating
3: good. The paper contains substantial theory and the central claims are mostly supported, but some assumptions, theorem framing, and presentation of the mathematical details leave room for clarification.

## Presentation Rating
2: fair. The overall organization is serviceable, but the paper has noticeable notation issues, some confusing algorithm descriptions, and an empirical section that is too limited relative to the scope of the claims.

## Contribution Rating
3: good. The reduction from OIO to SOCO under carryover constraints and the resulting dynamic-regret guarantee are worthwhile contributions, even though the empirical validation and practical framing lag behind the theory.

## Overall Rating
6: Marginally above the acceptance threshold. But would not mind if paper is rejected. The core technical idea is strong enough and sufficiently relevant to merit serious consideration, and the static improvement plus dynamic-regret result make this more than a minor tweak. That said, the paper is not an easy accept: the experiments are narrow, several technical assumptions and comparator choices need clearer interpretation, and the presentation has enough rough edges to reduce confidence. I lean positive because the theoretical contribution appears meaningful, but the work would benefit from a sharper main-paper exposition and a much stronger empirical section.

## Reviewer Confidence
4: confident. I am comfortable assessing online learning / regret-analysis papers and I checked the main logic and several technical details carefully, though I did not fully verify every appendix proof line by line.