Now I have a thorough understanding of the paper. Let me carefully assess each of the harsh critic's points against the actual paper content.

**Key findings from the paper:**

1. **KL divergence in Eq. 2 (line 62):** The paper writes `D_KL(p(y=ỹ|z,x) || c(ỹ|z)p(z|x))`. The left argument is a conditional distribution over ỹ (given z,x), while the right argument is `c(ỹ|z)p(z|x)` — the product of a conditional distribution over ỹ and a marginal over z. This is indeed problematic: the left side is a conditional p(ỹ|z,x) (which, when multiplied by p(z,x), gives a joint over (ỹ,z)), while the right is c(ỹ|z)p(z|x) (which, when multiplied by p(x), gives a joint over (ỹ,z,x)). They don't directly share the same support. However, let me think more carefully.

Actually, looking more carefully at the notation: `p(y=ỹ|z,x)` — this is the conditional probability of Y matching ỹ, given z and x. This gives a distribution over ỹ. And `c(ỹ|z)p(z|x)` — c(ỹ|z) is a conditional over ỹ, p(z|x) is marginal over z. The product c(ỹ|z)p(z|x) is a joint distribution over (ỹ, z), conditioned on x. So the right side, conditioned on x, gives a joint p(ỹ,z|x). But the left side is a conditional p(ỹ|z,x). 

Wait — KL divergence between a conditional and a joint (both conditioned on x) is indeed not well-defined in the standard sense. The left is p(ỹ|z,x) which sums to 1 over ỹ (for fixed z,x), while the right c(ỹ|z)p(z|x) does NOT sum to 1 over ỹ (since p(z|x) < 1). So this is a genuine mathematical issue.

2. **Frozen encoder (line 98):** The paper explicitly states "All models were trained over a frozen encoder of the vanilla model." This is indeed a significant experimental limitation — with a frozen encoder, the IB mechanism cannot learn the representation Z, so the experiments are only testing decoder-level regularization effects.

3. **Missing variational derivation:** The paper derives the bound for I(Z;X) (the standard VIB part) in Section 3.2 but then jumps to Section 4 (Experiments). The variational derivation of the novel SIB terms — λI(Z;Ỹ) and the KL divergence constraint — is absent from the paper.

4. **Duality concern:** The paper claims VIB has a "duality" where Y serves dual roles. The harsh critic argues this is standard variational practice and not problematic. Let me check the paper's argument more carefully...

The paper argues that in VIB, Y is used both as observed (from data) and as variational approximation. This is a valid conceptual observation — though whether it constitutes a "problem" requiring a "resolution" is debatable.

5. **The Lagrangian combination** — the paper simply combines two constrained optimization problems into one objective. The harsh critic raises concerns about this. Let me look at the actual SIB objective: `L_SIB = βI(X;Z) - I(Z;Y) + λI(Z;Ỹ) + D_KL(...)`. The paper doesn't formally justify combining these Lagrangians.

Now let me assess the Strength Finder's claims:

- "Principled resolution of the Y duality" — this is a conceptual contribution, somewhat overstated.
- "Information-theoretic derivation of decoder regularization" — the paper claims this but never formalizes it. Section 2.3 mentions the connection but the derivation is absent.
- "Empirical superiority" — the experiments use frozen encoders, which undermines claims about IB framework superiority.
- "Controlled experimental design" — this is a genuine strength: isolating the effect of the objective function.
- "Multi-modal evaluation" — this is a genuine strength.

Let me now write the final review.</think>Now I have a thorough understanding of the paper's content. Let me carefully verify the key criticisms and compose the final review.

## Summary

The paper proposes the Supervised Information Bottleneck (SIB), an extension of the Information Bottleneck (IB) framework that introduces a second bottleneck term to account for the learned classifier $\tilde{Y}$ in addition to the true label $Y$, addressing what the authors call a "duality" in how VIB treats the downstream variable. The SIB objective combines compression of $Z$ w.r.t. $X$, relevance w.r.t. $Y$, compression w.r.t. $\tilde{Y}$, and a KL divergence distortion constraint between the true distribution and the modeled classifier. Experiments on ImageNet (with InceptionV3) and IMDB (with BERT) compare SVIB against VIB and VCEB under a frozen-encoder protocol.

## Strengths

- **Controlled experimental design isolating objective function effects:** The paper explicitly freezes the encoder (Section 4) and varies only the objective function, enabling a clean attribution of performance differences to the loss function rather than architecture or training differences.
- **Multi-modal evaluation demonstrating generality:** Experiments span vision (ImageNet/InceptionV3) and NLP (IMDB/BERT), showing that SVIB's effects extend across modalities, not just one domain.
- **Conceptual motivation for incorporating the classifier into the IB framework:** The idea that the learned classifier variable $\tilde{Y}$ should be explicitly modeled in the IB objective when moving from unsupervised to supervised settings is a legitimate insight, consistent with and extending prior work by Geiger & Fischer (2020) and Piran et al. (2020).

## Weaknesses

### Fatal

- **The KL divergence in the SIB formulation (Eq. 2) is mathematically ill-defined as written.** The constraint reads $D_{KL}(p(y{=}\tilde{y}|z,x) \| c(\tilde{y}|z)p(z|x)) \leq D_2$. The left argument $p(y{=}\tilde{y}|z,x)$ is a conditional distribution over $\tilde{y}$ given $(z,x)$, which sums to 1 over $\tilde{y}$ for each $(z,x)$. The right argument $c(\tilde{y}|z)p(z|x)$ is a product of a conditional over $\tilde{y}$ and a marginal over $z$, yielding a quantity that does not sum to 1 over $\tilde{y}$ for each $(z,x)$. A KL divergence requires both arguments to be probability distributions over the same space; here they are not. Since the SIB objective (Eq. 3) directly includes this term, the central theoretical contribution of the paper — the proposed new objective — is mathematically incoherent as stated.

### Major

- **The complete variational derivation of the SVIB loss function is absent from the paper.** Section 3.2 derives only the standard VIB upper bound for $I(Z;X)$ and then stops. The variational treatment of the novel SIB terms — $\lambda I(Z;\tilde{Y})$ and the KL divergence constraint — is never presented, nor is the final explicit SVIB training objective. The paper claims to "derive a tractable variational approximation for SIB" (line 73, Section 3.2), but no such derivation appears in the main text. Without the final loss function, it is impossible to verify what was actually implemented and whether it corresponds to the claimed theoretical contribution.

- **Experiments with a frozen encoder cannot evaluate the core IB mechanism.** The paper states (Section 4): "All models were trained over a frozen encoder of the vanilla model, to allow faster experimentation." The IB framework's central purpose is to learn a compressed representation $Z$ via the encoder $p(z|x)$. Freezing the encoder means $I(Z;X)$ is constant during training, eliminating the compression mechanism entirely. What remains is a comparison of decoder-level regularizations under identical (unregularized) representations. This is a valid diagnostic experiment, but it fundamentally cannot support claims about SVIB as an information bottleneck framework — only about it as a decoder regularizer. The paper does acknowledge this design choice but does not acknowledge how it limits the claims supported by the experiments.

- **The claimed connection to conditional entropy regularization / label smoothing is asserted but never formally derived.** The Discussion (Section 5) proposes "a new motivation for conditional entropy regularization" and "a definition for decoder overfitting," and Section 2.3 states that "a conditional entropy term emerges during the derivation of our proposed adaptation of the IB objective." Yet no such derivation appears anywhere in the paper. Without a formal derivation, this claimed contribution remains unsupported.

### Minor

- **The combination of two constrained optimization problems into a single Lagrangian lacks formal justification.** The SIB objective (Eq. 3) combines a first bottleneck (Eq. 1, with multiplier $\beta$) and a second bottleneck (Eq. 2, with multiplier $\lambda$ and an explicit KL constraint). Combining constraints from two separate optimization problems into a single objective through simple addition of Lagrangians can couple the dual variables in ways that require justification; none is provided. This is not fatal to the approach (it can be valid under certain conditions), but it leaves a gap in the theoretical development.

- **The "duality" motivation for SIB is overstated.** The paper presents the inconsistent treatment of $Y$ in VIB as a "duality" requiring resolution. However, this is standard variational methodology: observable data provides empirical samples while a variational distribution $q(y|z)$ approximates intractable posteriors. The paper does not demonstrate that this standard practice produces any theoretical or practical problem, making the motivation for the second bottleneck somewhat question-begging.

### Trivial

- **Inconsistent notation between $\dot{Y}$ and $\tilde{Y}$:** The paper uses both $\dot{Y}$ and $\tilde{Y}$ interchangeably for the learned classifier variable (e.g., line 59: "also assume that $\dot{Y}$ and $Y$ share the same support" and line 27: "$Y\leftrightarrow X\leftrightarrow Z\leftrightarrow\dot{Y}$"), which is confusing even though they appear to refer to the same variable.

## Nice-to-Haves

- Experiments with trainable encoders to validate whether SVIB actually improves representation learning (the core IB claim), beyond its effects as a decoder regularizer.
- Comparison to simple decoder regularization baselines (label smoothing, entropy regularization / Pereyra et al. 2017), especially given that under a frozen encoder, SVIB effectively functions as a decoder regularizer.
- Information plane visualizations ($I(Z;X)$ vs. $I(Z;Y)$) during training to assess whether the IB framework is functioning as intended.
- Reporting the number of ($\beta$, $\lambda$) combinations searched for SVIB, since its 2D hyperparameter space may confer a selection advantage over the 1D spaces of VIB and VCEB.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Not yet released" / availability concerns about models or datasets** — Removed per hard rule. The paper cites InceptionV3, BERT, ImageNet, and IMDB, all of which exist and are available.

- **Missing related works** — Removed per hard rule. The harsh critic mentions Geiger & Fischer (2020) and Piran et al. (2020), which the paper actually cites and discusses. No external works should be flagged as "missing."

- **Formatting / notation nitpicks** — Removed per hard rule. The parser-introduced artifacts are ignored. The $\dot{Y}$/$\tilde{Y}$ notation inconsistency is kept as trivial since it genuinely affects clarity.

- **Reproducibility concerns about hyperparameter search** — The harsh critic notes SVIB has a 2D search space vs. 1D for VIB/VCEB and that the number of ($\beta$,$\lambda$) combinations is not reported, which could confer a selection advantage. This is a valid methodological concern and is retained as a nice-to-have rather than a weakness, since it is standard in this field to tune hyperparameters.

- **"5 runs per setting with Wilcoxon rank-sum test suffers from selection bias"** — The selection-after-tuning concern is valid but minor; retained implicitly in the nice-to-haves. The specific statistical critique is weakened because the paper does state its methodology for significance testing.

- **Strength Finder claim: "Principled resolution of the Y duality"** — Removed. The "duality" is standard variational practice, not a genuine problem requiring resolution, as discussed in Minor weaknesses.

- **Strength Finder claim: "Information-theoretic derivation of decoder regularization"** — Removed. This is claimed but never formally derived in the paper, making it an unsupported claim rather than a demonstrated strength.

- **Strength Finder claim: "Empirical superiority over VIB and VCEB with statistical significance"** — Removed as a strong claim. The experiments use frozen encoders, meaning the comparison only shows decoder-level regularization effects, not superiority of the full IB framework. The results are genuine but their interpretation is limited by the experimental design.

## Novel Insights

The paper's conceptual observation that the supervised setting should explicitly model the classifier variable $\tilde{Y}$ in the IB framework is legitimate and aligns with concurrent work. However, the theoretical formulation is undermined by a mathematically ill-defined KL divergence, and the experiments cannot validate the core IB claim due to the frozen-encoder design. The combination means the paper is, in its current form, a proposal for a promising direction that is not yet substantiated — the formulation needs repair and the experiments need to test the actual information bottleneck mechanism.

## Suggestions

- **Repair the KL divergence formulation in Eq. 2** so both arguments are proper probability distributions over the same space. For instance, if the intended constraint was purely conditional, $D_{KL}(p(\tilde{y}|z,x) \| c(\tilde{y}|z)) \leq D_2$, then the $p(z|x)$ marginal should be removed; if a joint constraint was intended, reformulate both arguments accordingly.
- **Provide the complete SVIB variational bound derivation**, including the variational treatment of $\lambda I(Z;\tilde{Y})$ and the KL term, and state the final explicit loss function used in experiments.
- **Run at least one experiment with a trainable (non-frozen) encoder** to validate that the SIB framework actually learns better representations, which is the fundamental claim of any IB method.

## Score and Decision

The paper proposes a conceptually interesting direction but is substantially incomplete in its current form: (1) the central mathematical formulation contains a structurally flawed KL divergence that renders the SIB objective ill-defined, (2) the variational derivation — the key technical contribution — is absent, making it impossible to verify what was actually implemented, and (3) the experimental design freezes the encoder, which removes the information bottleneck mechanism that the paper claims to evaluate. These issues collectively undermine the paper's core claims. The controlled experimental setup and multi-modal evaluation are genuine strengths, but they cannot compensate for the fundamental theoretical and methodological gaps.

**Originality:** The conceptual idea of adding a second bottleneck for $\tilde{Y}$ extends prior work (Geiger & Fischer 2020; Piran et al. 2020), but the mathematical realization is flawed.  
**Importance of research question:** Reasonable — connecting IB to decoder regularization is worthwhile.  
**Claims supported:** Not well — the mathematical formulation is incoherent, the derivation is absent, and experiments do not test the core mechanism.  
**Experiment soundness:** Limited by frozen-encoder design; results show decoder regularization effects but not IB mechanism effects.  
**Clarity:** Moderate — the motivation is clear but notation is inconsistent ($\dot{Y}$ vs. $\tilde{Y}$) and key derivations are missing.  
**Community value:** Low in current form — needs significant revision before the claimed contribution can be evaluated.

MY FINAL SCORE: <pineapple>3.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>