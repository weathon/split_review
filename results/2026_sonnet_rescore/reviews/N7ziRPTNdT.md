## Summary

This paper asks whether generation is *required* for data-efficient visual perception, specifically whether non-generative (encoder-only) or generative (decoder-inversion) approaches can guarantee compositional generalization. Building on Brady et al. (2025), the authors prove that constraining an encoder to the inverse function class $\mathcal{G}_{\text{int}}$ requires knowledge of the data manifold in out-of-domain regions (Theorem 3.2), while constraining a decoder to $\mathcal{F}_{\text{int}}$ (Eq. 3.1) is manifold-independent and achievable via architecture or regularization. They then describe two practical generative inversion strategies — gradient-based search and generative replay — and validate on photorealistic PUG datasets, finding that generative methods yield large OOD accuracy gains without additional data, while non-generative methods require large-scale pretraining.

---

## Strengths

- **Rigorous asymmetry between encoder and decoder constraints (Theorem 3.2 + Sec. 3.1):** The paper establishes a mathematically non-trivial distinction: for generators $f \in \mathcal{F}_{\text{int}}$, the derivative structure to be enforced (Eq. 3.1) is globally aligned with coordinate axes and thus manifold-independent. For inverses $g \in \mathcal{G}_{\text{int}}$, the analogous constraint (Eq. 3.4) requires projection onto the tangent space $T_x\mathcal{X}$, making it unavoidably geometry-dependent and ill-posed on unobserved OOD regions. This is a concrete, non-trivial theoretical result.

- **Clean empirical confirmation of the $n=0$ theoretical prediction:** The paper predicts that when concepts do not interact ($n=0$, PUG-Object split), the encoder class $\mathcal{G}_{\text{int}}$ is more structured and non-generative methods should be able to generalize compositionally. Fig. 5C confirms this directly — *all* tested non-generative models achieve near-perfect OOD accuracy on PUG-Object, while failing substantially on the interacting splits (PUG-Background, PUG-Texture). This is a direct theory-to-experiment correspondence and one of the paper's strongest moments.

- **Practical generative inversion with measurable gains (Fig. 6):** Search and replay applied to the same decoders consistently improve OOD accuracy across all base encoders on PUG-Background and PUG-Texture without any additional data. This is not a marginal gain: models trained from scratch or with small pretraining go from near-zero to meaningful OOD accuracy.

- **Principled formalization of compositional generalization for both paradigms:** The distinction between learning $\hat{f} \in \mathcal{F}_{\text{int}}$ and inverting it (Eq. 2.2) vs. learning $\hat{g} \in \mathcal{G}_{\text{int}}$ directly (Eq. 2.3) is clearly articulated and provides an identifiability-theoretic basis that goes beyond prior empirical studies.

- **Connection to causal/anti-causal learning:** The analysis provides a formal justification for the Kilbertus et al. (2018) conjecture that generalization is structurally easier in the causal direction, a clean intellectual contribution.

---

## Weaknesses

### Fatal
None.

### Major

- **Gap between Theorem 3.2 and the "cannot be enforced" claim in the abstract:** The abstract states that inductive biases required for compositional generalization "cannot be enforced on an encoder through practical means such as regularization or architectural constraints." Theorem 3.2 establishes that $Dg$ and $D^2g$ for $g \in \mathcal{G}_{\text{int}}$ can be arbitrary when $d_x \geq d_z^3$, and that the relevant structural constraint (Eq. 3.4) is tangent-space-dependent. What is proved is that the *derivative characterization* of $\mathcal{G}_{\text{int}}$ depends on the manifold geometry; what is concluded is that all practical constraint methods are infeasible. These are not the same. The main text (Sec. 3.1) is more careful — it says constraints are "challenging," "impractical," and "suggests that... is infeasible" — but the abstract uses "cannot," which is stronger than the theorems establish. A formal lower bound showing that *any* regularizer or architectural constraint encoding $\hat{g} \in \mathcal{G}_{\text{int}}$ must rely on manifold knowledge would close this gap; absent that, "generally infeasible" or "no known practical approach" is the most defensible framing. The gap is real but doesn't undermine the core theoretical asymmetry — it requires careful reframing.

### Minor

- **Structured decoder ablation deferred to appendix:** The main experimental comparison uses a regularized cross-attention Transformer decoder specifically designed to approximate $\mathcal{F}_{\text{int}}$ (pixels query slots, attention regularized to encourage slot specialization). This decoder carries strong inductive bias aligned with the theory. An ablation with unstructured decoders appears in Appendix C but is not summarized in the main results. This matters because the central claim is that the *generative inversion mechanism* (not decoder architecture alone) drives OOD gains. If structured and unstructured decoders produce similar replay/search gains, the architectural prior is the primary driver; if structured decoders are substantially better, the theory is confirmed more cleanly. Since this ablation exists in the appendix, the gap is not fatal, but the paper would be stronger if a summary finding from Appendix C were surfaced in Sec. 5.2.

- **Assumption $f \in \mathcal{F}_{\text{int}}$ lacks empirical grounding:** All theoretical guarantees are conditional on the ground-truth generator belonging to $\mathcal{F}_{\text{int}}$ — a class constructed precisely to enable OOD identifiability. For PUG data rendered by a 3D engine, the true generator is unlikely to be exactly in $\mathcal{F}_{\text{int}}$. The paper acknowledges this in Sec. 7 ("Our theory is limited to generators which belong to $\mathcal{F}_{\text{int}}$"), but a brief discussion of why $\mathcal{F}_{\text{int}}$ is a reasonable approximation for rendered or natural images would strengthen the paper's practical relevance.

- **Replay requires approximately independent slots, which is not guaranteed for a VAE trained on ID data:** Section 4.2 describes sampling $\tilde{z}$ from a distribution $p_{\tilde{z}}$ with independent slot-wise marginals. This is only valid for generating genuinely OOD combinations if the learned slots are approximately independent; for a standard VAE without explicit slot-independence constraints, this may not hold, producing samples near the ID support. This subtlety is not discussed.

### Trivial

- **SigLIP2 achieving ~80% OOD accuracy on PUG-Background as a non-generative model** is noted in Fig. 5A but warrants more than a passing explanation. The authors attribute this to large-scale pretraining providing implicit coverage of concept combinations, which is reasonable — but the paper could more precisely quantify how much of the non-generative performance gap closes as a function of pretraining scale, to better characterize where the generative advantage is most needed.

---

## Nice-to-Haves

- Constructing datasets with systematically varying interaction degree $n$ (beyond the current binary n=0 / n≥1 split) and showing OOD degradation for non-generative models as a function of $n$ would make the theory-to-experiment connection far more direct and compelling than aggregate comparisons across splits.
- A supervised generative baseline (category-conditional decoder) would clarify whether the asymmetry between supervised non-generative and unsupervised generative methods is driven by the generative mechanism or the supervision signal.
- A discussion of whether the dimension condition $d_x \geq d_z^3$ is satisfied in practical image settings (e.g., for $64\times64\times3$ images and $d_z \sim 10$–50) would give readers a concrete sense of when Theorem 3.2 applies.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Harsh Critic: Logical gap as "structural" / "fatal":** The critic frames the theorem-to-conclusion gap as structural enough to require rejection. However, the main text does hedge appropriately ("suggests that... is infeasible"), and the argument is a genuine insight about derivative constraints being manifold-dependent. The gap is better characterized as a calibration issue requiring revised abstract language, not a paper-invalidating flaw. Retained as Major but not Fatal.

- **Harsh Critic: Section 5.1 evaluation mismatch (readout trained on ID, gradient descent produces OOD latents in different space):** While this is a subtle point, the paper's evaluation framework (training a slot-wise readout on ID encoder outputs and evaluating on OOD inferred latents) is standard practice in the slot-based representation learning literature. No concrete evidence is presented that the latent spaces produced by gradient descent and the ID encoder are incompatible. Removed as speculative.

- **Harsh Critic: Missing comparison statement about Brady et al. (2025) contributions vs. paper's new contributions:** The paper explicitly states it "build[s] upon Brady et al. (2025)" and describes what is new (Theorem 3.2, the encoder infeasibility argument, the search and replay methodology, and the empirical study). This is adequately handled and does not require a formal contribution table. Removed.

- **Harsh Critic: Asymmetric comparison (supervised non-generative vs. unsupervised generative):** Both supervised and unsupervised non-generative methods are tested in Fig. 5; the comparison is not as asymmetric as claimed. Removed as a misread.

---

## Novel Insights

The most intellectually precise contribution of this paper is the formal demonstration that the structural constraint characterizing $\mathcal{G}_{\text{int}}$ (Eq. 3.4) is *tangent-space-dependent*, while the analogous constraint for $\mathcal{F}_{\text{int}}$ (Eq. 3.1) is globally aligned with the coordinate axes and therefore manifold-independent. This asymmetry provides a formal grounding for the long-standing intuition in causal representation learning (Kilbertus et al., 2018) that the causal direction is simpler than the anti-causal direction. The $n=0$ special case prediction — that non-interacting concepts should enable non-generative compositional generalization — and its direct empirical confirmation is a clean, falsifiable theory-experiment connection that goes beyond what prior empirical literature has established.

---

## Suggestions

1. **Revise the abstract** to replace "cannot be enforced" with "are generally infeasible in practice" or "no practical procedure is known to enforce" — aligning the summary claim with what Theorem 3.2 actually establishes.
2. **Surface a one-line summary of the Appendix C (unstructured decoder) ablation result in the main text** (Sec. 5.2), even if only as a parenthetical, so readers can see whether decoder architecture or the inversion mechanism drives the OOD gains.
3. **Add a brief discussion** of whether the condition $d_x \geq d_z^3$ is typical for real image data (with concrete numbers), to situate Theorem 3.2 in the practical context readers care about.
4. **Clarify the slot independence assumption for generative replay** (Sec. 4.2): state what property of the VAE training ensures approximate slot independence, or note this as a practical limitation.

---

**Axis Evaluation:**
- *Originality:* High — the encoder/decoder asymmetry result and its connection to causal learning is novel.
- *Importance:* High — addresses a foundational question about whether generation is necessary for human-level data-efficient perception.
- *Claims supported:* Moderate-high — the main text is appropriately hedged; the abstract is slightly overclaims. Theory and experiment are directionally consistent.
- *Soundness:* High — theorems are non-trivial and correctly stated; experiments use standard methodology.
- *Clarity:* High — well-organized, crisp formalism, good use of figures.
- *Community value:* High — provides theoretical grounding for both the causal representation learning and practical slot-based representation learning communities.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>

<subscores>
<originality>4</originality>
<importance>4</importance>
<claims_supported>3</claims_supported>
<soundness>4</soundness>
<clarity>4</clarity>
<community_value>4</community_value>
</subscores>