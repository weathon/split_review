Now I have a thorough understanding of the paper. Let me analyze each of the harsh critic's claims carefully.

**Claim 1: Exogeneity assumption contradicts the problem setup.**
The paper states in Lemma 3.2 that Φ must be exogenous relative to Y. The harsh critic says this contradicts the existence of spurious correlations (confounders). Let me think about this. The exogeneity assumption in the PNS context means that there are no unobserved confounders between Φ and Y. However, spurious correlations are precisely about confounders creating non-causal associations. The paper applies PNS to learned representations Φ_t and Φ_v, not to raw input features. So the question is whether the learned representations can satisfy exogeneity. The paper doesn't discuss this. This is a valid concern - the paper assumes exogeneity but doesn't verify or justify it in the VLM context. However, it's also worth noting that this assumption is inherited from Yang et al. (2023b), which the paper directly follows. The concern is valid but partly mitigated by the fact that the PNS is applied in a practical way where the exogeneity might be approximately satisfied through the intervention mechanism. Let me keep this as a major concern rather than fatal.

**Claim 2: Assumption 4.1 (Y ⊥ Φ_v | Φ_t) undermines the paper's motivation.**
The paper states Assumption 4.1: "textual representations Φ_t are fully informative for determining the target Y, i.e., Y ⊥ Φ_v | Φ_t." The critic claims this makes the visual modality redundant. Let me think... If Y is conditionally independent of Φ_v given Φ_t, then Φ_v provides no additional information about Y beyond Φ_t. However, this is about conditional independence - the visual modality still matters for *predicting* Φ_t or *learning* Φ_t. In practice, during training, you need visual features to inform the textual representations. The assumption is used for the theoretical bound derivation, not to claim visual features are useless. That said, the assumption is strong and not justified. In a VLM where textual representations are class-level prompt embeddings, the assumption essentially says that given the class-level text features, the visual features don't add information about the label - which is almost tautologically true in a classification setting where Y determines Φ_t and vice versa. This is actually somewhat reasonable for VLMs where class-conditional text embeddings are deterministically generated from labels. Still, the paper doesn't justify it. I think this is a legitimate concern but not fatal - it's a formal assumption for the theorem, not a claim about reality. Keep as a minor concern (or minor-major).

**Claim 3: Equation 10 objective is incoherent (min_{Q,h} max_{Q,h}).**
Looking at line 150: `\operatorname*{min}_{Q,h}\operatorname*{max}_{Q,h}`. This does appear to have both min and max over the same variables Q,h. However, looking at the PNS formulation in Eq. 7 (line 116-117): `\operatorname*{min}_{\omega,\theta}\operatorname*{max}_{\xi}`, which clearly has different optimization variables for min vs max. In Eq. 10, the cross-modal PNS uses (f([Q,CLASS]), h, h̄) and the textual PNS uses (h(g(X)), f([Q,CLASS]), f([Q̄,CLASS])). The intervention variables (h̄ and Q̄) are the ones that should be maximized. The paper description says h and h̄ are "two filters" (separate networks, Fig 1), and Q and Q̄ are separate prompt variables. So the Eq. 10 notation is incorrect as written - it should be min over {Q, h} and max over {Q̄, h̄} or some similar formulation. The paper describes h̄ as "a linear layer" (separate from h), and Q̄ is the intervention prompt. The actual implementation likely optimizes these separately. This IS a genuine notational/conceptual error in the main equation, which is concerning but probably just a typo rather than a fundamental flaw - the implementation likely does the right thing. Keep as a major concern (important notation issue in the main equation) but note it's likely a typo.

**Claim 4: The intervention mechanism Q̄ is completely unspecified.**
The paper describes Q̄ as "the intervention prompt" (from Figure 1 caption). It says "f([Q̄, CLASS])" serves as ξ for textual PNS. The paper doesn't explicitly describe how Q̄ is parameterized or learned. From the PNS framework (Section 3.3), ξ parameterizes the intervention distribution. In the cross-modal case, h̄ is described as "a linear layer" (a separate filter). But for Q̄, the reader must infer it's a separate learnable prompt (analogous to Q). This is a gap in specification that harms reproducibility, but it's also somewhat inferable. Keep as a minor concern.

**Claim 5: ERM baseline includes projection head h.**
The paper explicitly states: "different from CoOp under our model framework, the ERM method will use the causal projection layer (i.e., h in Figure 1)." So the ERM baseline already includes h. The critic is right that this makes it hard to disentangle the contribution of the PNS objectives from simply adding the projection head. However, this comparison is not unfairly biased in favor of the authors' method - having h in ERM gives ERM more capacity, making it a *stronger* baseline, not a weaker one. If LogicAl-PT outperforms ERM+h, that's a fairer comparison. The concern about not having a bare ERM without h is still valid for ablation purposes, but it doesn't invalidate the comparison. Keep as a minor concern.

Let me now verify the "tighter bound" claim more carefully.

Looking at Remark 4.3, the paper claims that their method "can guarantee a tighter generalization error bound compared with the state-of-the-art prompt-tuning schemes." The argument is: (1) Theorem 4.2 provides a bound with three error terms - empirical, textual, and alignment. (2) The PNS objectives drive the textual and alignment terms toward zero, making the total bound tighter. (3) The claim of "tighter" relies on referencing "Theorem 4.3 in (Yang et al., 2023b)" - which is a prior work. The paper does not provide an explicit comparison showing their bound is numerically tighter than any specific baseline bound. More critically, the bound contains |X| and |Z| which for image data are enormous, making the bound potentially vacuous in practice. This is a valid concern but is common in theoretical ML papers. Keep as a minor concern.

Now let me also address the "monotonicity measurement term dropped" claim. Looking at Eq. 7, the PNS objective includes M_S^ω(θ,ξ) + SF_S(ω,θ). The M_S^ω term comes from the upper bound in Proposition 3.3. Then in the paper's own objective (Eq. 7 from Yang et al.), the PNS loss is defined as M_S^ω + SF_S + λR_KL. This is from Yang et al. (2023b), so it's properly cited. The paper doesn't drop M_S - it includes it in the PNS loss definition.

Wait, let me re-read. Looking at line 116-117: `L_PNS(ω,θ,ξ) := M_S^ω(θ,ξ) + SF_S(ω,θ) + λR_KL`. The PNS objective from Yang et al. already includes M_S. The paper uses this form. But then in the overall objective (Eq. 10), the min-max is over `L_PNS(f([Q,CLASS]),h,h̄)` and `L_PNS(h(g(X)),f([Q,CLASS]),f([Q̄,CLASS]))`. So the M_S term is included within L_PNS. The critic's claim that M_S is "dropped" is incorrect - it's included in the L_PNS formulation that the paper inherits.

Now let me assess the overall claims:

1. Exogeneity assumption: Valid concern that the key assumption isn't justified in the VLM context, but it's inherited from prior work and applied to learned representations. Major.

2. Assumption 4.1: Valid concern about the strength and lack of justification of this assumption. For VLMs where text prompts are class-determined, it may be approximately reasonable. Minor-to-major.

3. Eq. 10 notational error: The notation `min_{Q,h} max_{Q,h}` is clearly wrong - it should distinguish between main variables and intervention variables. This is a real problem in the paper's main equation. Major (notation/conceptual clarity in the core objective).

4. Q̄ specification: Some specification gap, but inferable from context. Minor.

5. ERM baseline concerns: The inclusion of h in ERM actually makes it a *stronger* baseline. But wanting to see a pure ablation is reasonable. Minor.

6. "Tighter bound" claim: The claim is somewhat overblown given the bounds involve |X| and |Z|. Minor.

7. Assumption 4.1 making visual modality redundant: This overstates the case. The assumption is about the conditional independence of Y from Φ_v given Φ_t, which doesn't make Φ_v useless in training. It just means the theoretical guarantee holds under a specific conditional independence. Major concern if viewed as undermining the theoretical contribution, but not fatal since the method still works empirically.

Let me now write the final review.</think>Now I have a thorough understanding of the paper. Let me synthesize the final review.

## Summary

The paper proposes LogicAl-PT, a framework that uses causally motivated "logic alignment" based on probability of necessity and sufficiency (PNS) to mitigate spurious correlations in both visual and textual modalities during prompt tuning of vision-language models. The method decomposes the objective into two PNS terms: textual alignment (Y ⇔ Φ_t) that removes spurious correlations from textual representations, and cross-modal alignment (Φ_t ⇔ Φ_v) that jointly handles visual spurious correlations and representation alignment. The paper derives a generalization error bound and demonstrates empirical improvements on four OOD benchmark datasets.

## Strengths

- **Addresses a genuine gap in prior work**: Unlike CoOPood which only handles visual spurious correlations and assumes uniform distribution, LogicAl-PT mitigates spurious correlations in both modalities without requiring spurious feature annotations or distributional assumptions. This cross-modal angle is a meaningful contribution to prompt-tuning research.

- **Conceptually clean decomposition via the equivalence chain**: The formulation Y ⇔ Φ_t ⇔ Φ_v maps the two sub-problems (textual spurious correlation elimination and cross-modal alignment) to two distinct PNS objectives (Eqs. 8–9), making the framework modular and interpretable. Each component has a clear causal interpretation.

- **Empirical improvements on worst-group accuracy**: Table 1 shows LogicAl-PT achieves substantial improvements over prior methods on Waterbird (94.9 vs. 87.2 for CoOPood) and CelebA (80.9 vs. 73.4), and consistently ranks among the best across all benchmarks.

## Weaknesses

### Fatal
None.

### Major

- **The overall objective (Eq. 10) has an ill-posed min-max formulation**: The equation reads min_{Q,h} max_{Q,h}, minimizing and maximizing over the same variables. In the PNS framework (Eq. 7), the min-max is correctly formulated as min_{ω,θ} max_{ξ} — the main parameters are minimized while intervention parameters are maximized. In Eq. 10, the intervention variables are Q̄ (textual) and h̄ (visual), which are separate from Q and h, but the notation fails to distinguish them. Although the implementation likely handles this correctly, the main mathematical formulation for the overall objective is not well-defined as written, which is a serious clarity issue in the core contribution.

- **Exogeneity assumption is not discussed or justified in the VLM context**: The PNS computation via Lemma 3.2 requires that Φ be exogenous relative to Y — i.e., no confounders between them. The paper's entire motivation is that spurious correlations (confounders) exist, yet the key mathematical tool requires their absence. The paper imports this assumption from Yang et al. (2023b) without discussing whether the learned representations Φ_t and Φ_v satisfy it, or acknowledging the apparent tension. This matters because all derived objectives (Eqs. 8–10) rest on this assumption.

- **Assumption 4.1 (Y ⊥ Φ_v | Φ_t) is strong and unmotivated**: The generalization bound of Theorem 4.2 relies on Y being conditionally independent of Φ_v given Φ_t, meaning visual features provide no additional label information beyond textual features. While one might argue this is approximately true for VLMs where class-conditional text embeddings are deterministic, the paper never justifies this assumption. The claimed "tighter bound" (Remark 4.3) depends on it, and if the assumption doesn't hold, the theoretical contribution weakens substantially.

### Minor

- **The intervention prompt Q̄ is under-specified**: While h̄ is described as "a linear layer" (a separate filter from h), the textual intervention Q̄ receives no explicit parameterization or learning rule in the text. The reader must infer it is a separate learnable prompt analogous to Q. A brief clarification would improve reproducibility.

- **The "tighter generalization error bound" claim is overstated**: Theorem 4.2's bound contains |X| and |Z| (cardinalities of input and representation spaces), which are enormous for image data, rendering the bound vacuous in practice. The comparison in Remark 4.3 shows the additional terms *can* be driven to zero by the PNS objectives, but does not provide an explicit numerical comparison with any baseline bound. The claim of "tighter" is conditional on Assumption 4.1 and remains qualitative rather than demonstrated.

- **The ERM baseline includes the projection head h, limiting ablation interpretation**: As the paper acknowledges, ERM already uses h, making it impossible to separate the contribution of adding the projection head from that of the PNS objectives. A proper ablation with ERM (no h) would strengthen the analysis. That said, the current comparison is conservative (ERM+h has more capacity than ERM), so it does not unfairly favor the proposed method.

- **Cross-modal PNS uses f([Q, CLASS]) simultaneously as classifier ω and causal feature θ**: In the textual PNS objective (Eq. 9), f([Q, CLASS]) plays both roles — ω (classifier via prototypes) and θ (causal representation) — potentially conflating two distinct roles in the PNS framework. The paper does not discuss implications of this dual role.

## Nice-to-Haves

- A synthetic experiment testing what happens when the exogeneity and/or monotonicity assumptions are violated would significantly strengthen the causal justification.

- Quantitative feature attribution metrics (e.g., pointing accuracy) rather than relying solely on Grad-CAM visualizations.

- Explicit comparison of the derived bound's numerical values against a baseline bound, rather than just claiming "tighter."

## Removed Points

These points are flagged to be removed, treat them with caution.

- **Claim that Assumption 4.1 makes the visual modality "informationally redundant" and thus the cross-modal alignment unnecessary**: The assumption Y ⊥ Φ_v | Φ_t is a conditional independence used in the theoretical bound derivation; it doesn't mean Φ_v is irrelevant during training or for inference. In the VLM framework, visual features are still needed to produce Φ_t and to train the alignment. The assumption is about what happens at equilibrium of the bound, not about the necessity of the algorithmic procedure. The critic's claim that this undermines the entire cross-modal effort is an overstatement, though the assumption itself remains a valid concern.

- **Claim that the monotonicity measurement term M_S is "dropped without discussion"**: Re-reading Eq. 7 and the PNS formulation, the term M_S^ω(θ,ξ) is *included* in L_PNS(ω,θ,ξ) := M_S^ω(θ,ξ) + SF_S(ω,θ) + λR_{KL}. The paper does not drop it — it inherits the full PNS risk from Yang et al. (2023b).

- **Claim about missing OOD baselines like MaPLe**: Per the rules, do not flag missing related works that we cannot confirm exist in a comparable setting.

- **Claim that Grad-CAM visualizations are "qualitative and weak evidence"**: This is standard practice in the interpretability of spurious correlation papers. While quantitative metrics would be nicer, this is a nice-to-have, not a weakness.

- **Claim about unfair comparison with ERM+h**: Since ERM+h is a *stronger* baseline (it has more capacity than plain ERM), the asymmetry favors the baseline, not the proposed method. Per the hard rules, this criticism is removed.

- **Claim that the circular dependency between f([Q, CLASS]) and h(g(X)) is never analyzed**: This is a repackaging of the dual-role concern already listed under minor weaknesses. The critic's version implies this is more severe than warranted — the prototypes from h(g(X)) are computed on a per-class basis and used as a linear classifier ω, which is a well-defined operation even if the representations are simultaneously being learned. Many contrastive learning methods use similar online prototype computation.

## Novel Insights

The core insight of this paper — that PNS can be applied to two separate logical equivalences (Y ⇔ Φ_t and Φ_t ⇔ Φ_v) in a VLM, thereby jointly addressing textual spurious correlations and cross-modal misalignment — is genuinely novel. However, the theoretical foundation has notable gaps: the exogeneity assumption required by the PNS framework sits in tension with the existence of spurious correlations that motivate the work, and Assumption 4.1 (conditional independence of Y from Φ_v given Φ_t) is asserted without justification. The method's practical effectiveness appears to stem more from the well-motivated regularization structure of the two PNS objectives than from the theoretical guarantees, whose assumptions deserve closer scrutiny. The notation error in Eq. 10 (min_{Q,h} max_{Q,h}) also raises concerns about how carefully the min-max game has been formulated versus simply being implemented as alternating optimization.

## Suggestions

- Fix Eq. 10 to properly distinguish the min and max optimization variables (e.g., min over Q,h and max over Q̄,h̄) and clarify the optimization procedure.

- Add a brief discussion of the exogeneity assumption in the VLM context — even a paragraph acknowledging the tension and arguing why learned representations might approximately satisfy it would strengthen the causal justification.

- Justify Assumption 4.1 or provide an ablation/diagnostic showing it approximately holds in practice.

## Score and Decision

This paper makes a meaningful contribution to an under-explored problem (cross-modal spurious correlation mitigation in VLM prompt tuning) and shows strong empirical results. However, the theoretical claims rest on assumptions that are neither justified nor discussed (exogeneity, Assumption 4.1), the main objective function has a notational error that renders it ambiguous, and the "tighter bound" claim is overblown. These issues significantly weaken the theoretical contribution, though the empirical results and conceptual framework are solid.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>