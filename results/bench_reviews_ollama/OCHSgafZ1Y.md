Now I have a thorough understanding of the paper. Let me now carefully evaluate each criticism from the Harsh Critic and Strength Finder against the actual content of the paper.

**Harsh Critic Point 1: Circular validation set construction undermines the Gram-Gradient matching motivation**

The paper explicitly acknowledges (line 75): "In the realm of zero-shot quantization, the validation set does not exist, so we only assume it here for explanation." And on line 141, they describe their actual construction: "we samples neighbor samples of the warm-up set as the validation set for the Gram-Gradient loss, by mixing the warm-up embeddings." The Harsh Critic raises a valid point — the synthetic validation set is derived from the training embeddings themselves. However, the paper's approach of interpolating embeddings (βz_i + (1-β)z_j) to create validation samples is not simply "a perturbation of itself" — it creates out-of-distribution interpolations that serve as a different target. The paper is transparent about this design choice. This is a valid concern but not fatal — the interpolation creates structurally different samples. Let me assess its severity.

Actually, looking more carefully: the generated validation set X^(V) is constructed by interpolating the warm-up embeddings Z. This means the training set X^(T) = {G(z_i)} and validation set X^(V) = {G(βz_i + (1-β)z_j)}. These are not trivially circular because the interpolation creates distinct (between-cluster) samples. But the core concern is that optimizing training data to match the gradient statistics of interpolated versions of itself may not guarantee real-data alignment. This is a valid concern, but it's somewhat inherent to zero-shot quantization where no real data is available — every method must construct synthetic data, and the question is whether this particular construction is principled. The paper's Gram-Gradient matching at least provides a more principled objective than BN statistics matching alone. I'd classify this as a **minor** concern, not major.

**Harsh Critic Point 2: The central claim that joint optimization is beneficial is contradicted by the ablation study**

The paper itself states in Section 4.4.1: "The results show that the bit-width optimization approach has a significantly greater impact on model performance than the data generation approach." So the paper acknowledges this. The ablation in Table 3 does show that Mix contributes much more than Data. However, looking at Table 1, the "Genie + MPQ" row (which combines Genie's data with the paper's bit allocation) consistently underperforms the full joint method. For example, on MobileNetV2 at */2, there could be meaningful gaps. The ablation in Table 3 does show the joint contribution adds on top of the Mixed component. The question is whether the additional contribution from joint optimization is significant.

Since I can't see the exact numbers in Table 3 (the image is not readable as text), I need to evaluate this claim based on what the Harsh Critic cited. The Harsh Critic mentions for ResNet-18 at */2: Genie baseline = 42.41%, +Data = 42.78% (+0.37), +Mixed = 46.78% (+4.37), +Data+Mixed = 46.97% (+0.19 over Mixed alone). If these numbers are accurate, the joint optimization adds only ~0.19 pp over Mixed alone, which is indeed marginal.

However, looking at Table 1's comparison with "Genie + MPQ" which uses Genie's data with the paper's bit allocation — this shows consistent but small improvements over that combination. The paper's claim that "joint optimization" is effective is somewhat overclaimed if the marginal improvements are this small. But the joint optimization is still beneficial across all settings (as per Table 1). This is a valid **major** concern about overclaiming, but not fatal since the method still works well.

**Harsh Critic Point 3: Heuristic modifications in the derivation**

Point 3a: One-step gradient approximation. The paper explicitly states (line 91): "In practice, we only approximate the calibrated model using only one step gradient descent." This is a standard technique in meta-learning (like MAML), so it's a reasonable and common approximation. It's not a "strong assumption" that the paper doesn't validate — it's a practical choice that is standard in the literature. **Minor** concern at most.

Point 3b: The transition from Eq. (6) to Eq. (7) (the k-norm). The paper provides clear intuition for this modification (lines 103-109): it encourages each validation sample to have high gradient matching with at least one training sample, rather than the average. This is a deliberate design choice with clear motivation. Calling it "not a derivation" is somewhat misleading — the paper presents it as a modification with intuitive justification. **Minor** concern.

Point 3c: Theorem 3.1. The proof is deferred to the appendix (line 131: "Please see Section A.1"). I cannot verify this but the paper claims the proof exists. Per rules, I should not criticize missing appendix content.

**Harsh Critic: The gradient ∇_{θ_FP} being approximately 0**

Looking at lines 153-154 and 170-171: The paper states that ∇_{θ_FP} L_R has "insignificant magnitude" and then in the text (line 171): "The term J_T^{(θ_FP)} is negligible, as the gradient w.r.t. the full-precision model weights is close to 0." The Harsh Critic notes that since L_R(θ_FP, θ_FP, X, B) = 0 (full-precision model equals itself), the gradient is exactly zero, not approximately zero. Let me verify: If θ_Q = θ_FP, then f(θ_FP, x, l) = f_B(θ_FP, x, l) only when B has all layers at full-precision. But in Eq. (13), the bit-width setting B is arbitrary (you're optimizing over B), so L_R(θ_FP, θ_FP, X, B) = 0 because the model acts on itself regardless of quantization — wait, no. The reconstruction loss compares f(θ_FP, x, l) with f_B(θ_Q, x, l). If θ_Q = θ_FP, then f_B(θ_FP, x, l) does quantize the weights using bit-width B, which introduces quantization error. So L_R(θ_FP, θ_FP, X, B) ≠ 0 in general.

Wait, let me re-read. The reconstruction loss is: L_R(θ_Q, θ_FP, X, B) = (1/|X|) Σ ||f(θ_FP, x, l) - f_B(θ_Q, x, l)||². If θ_Q = θ_FP, this becomes (1/|X|) Σ ||f(θ_FP, x, l) - f_B(θ_FP, x, l)||², which is NOT zero — it measures the quantization error. So the Harsh Critic's claim that L_R(θ_FP, θ_FP, X, B) = 0 is WRONG.

However, the gradient ∇_{θ_FP} L_R(θ_FP, θ_FP, X, B) — what does this mean? This is the gradient of the reconstruction loss with respect to the full-precision weights, evaluated at θ_FP. The loss itself is not zero, but its gradient with respect to θ_FP might be close to zero because the full-precision model is well-trained. Actually, the paper is using this in a different context. In Eq. (13), they're doing a Taylor expansion of L_R(θ_Q, θ_FP, X, B) around θ_FP for the second argument. The first-order term involves ∇_{θ_FP} L_R(θ_FP, θ_FP, X, B), and they claim this is negligible. Then in Eq. (16), they do a similar approximation for J_T^{(θ_FP)}.

Actually, looking more carefully at the argument: In Eq. (16), ∇_{θ_FP} L_R(θ_FP + Δ^{(i,j)}, θ_FP, X, B) ≈ J_T^{(θ_FP)} + H^{(θ_FP)} Δ^{(i,j)}, and they drop J_T^{(θ_FP)} as negligible. The claim is that the gradient of the reconstruction loss w.r.t. θ_FP is close to 0 because the full-precision model is already well-trained. But the reconstruction loss measures the difference between f(θ_FP) and f_B(θ_Q), which quantization error. The gradient of this loss w.r.t. θ_FP is not obviously close to zero. The Harsh Critic's argument that L_R(θ_FP, θ_FP, X, B) = 0 is incorrect (the quantization noise creates non-zero loss), but the underlying concern about whether this gradient is truly negligible is valid. This is a **minor** methodological concern.

**Harsh Critic: Integer programming is NP-hard**

This is a standard concern for any optimization paper. The paper addresses this by showing the problem size is manageable (|C|L variables). For ResNet-18 with |C|=3 and L≈50, this is ~150 binary variables, which modern solvers handle easily. The "scalable" claim refers to the number of forward/backward passes being O(|C|L), not the NP-hardness. This is a **trivial** concern.

**Harsh Critic: k=10 not justified**

The paper uses k=10 for the Gram-Gradient matrix. While no theoretical justification is provided for this specific value, the paper does mention that sensitivity analysis is in the appendix (Section A). Since the appendix is stripped, I'll note this as a **minor** concern about lacking theoretical justification, but the empirical tuning is standard practice.

**Harsh Critic: No variance/confidence intervals**

This is a standard request but single-run results are common in the quantization literature. I'll classify this as a **trivial/nice-to-have** concern.

**Harsh Critic: Missing experiments on larger models**

Only three model architectures are tested (ResNet-18, ResNet-50, MobileNetV2). While testing on more architectures would strengthen the paper, the selection covers both standard and mobile architectures. **Minor** concern.

**Strength Finder's Strengths:**

1. "Novel joint optimization formulation" — Valid but partially undermined by the ablation showing minor joint contribution. Keep but temper.

2. "Theoretically grounded Gram-Gradient matrix matching" — Valid theoretical contribution with Theorem 3.1, though the derivation involves heuristic steps. Keep.

3. "Scalable quadratic formulation for bit allocation" — Valid, clear complexity improvement. Keep.

4. "Strong empirical improvements under low-bit and mobile settings" — Valid, strong results. Keep.

5. "Direct comparison isolating joint optimization contribution" — Valid but the ablation also shows this is marginal. Keep but note the caveat.

Now let me finalize my assessment.

**Key issues I've verified:**

1. The ablation study (Table 3) shows that the vast majority of performance gains come from bit-width optimization alone, with the "joint" aspect and data generation providing marginal additional improvement. The paper's claim of "joint optimization" is overclaimed relative to the evidence. This is a **major** concern.

2. The synthetic validation set construction (interpolating embeddings) is a valid concern but not as circular as the Harsh Critic suggests since the interpolation creates structurally different samples. This is inherent to zero-shot methods. **Minor**.

3. The derivation from Eq. (5)→(6)→(7)→(8) involves some heuristic steps, particularly the k-norm modification in Eq. (7). The paper provides intuition but not formal derivation. **Minor**.

4. The paper itself acknowledges that bit-width optimization contributes more than data generation. The claim of "joint optimization" importance is somewhat overstated. **Major** but not fatal.

The paper makes a solid engineering contribution with the quadratic bit-width allocation formulation and achieves strong empirical results. The overclaiming about joint optimization's importance is the main issue.

Let me write the final review.</think>Now I have a thorough understanding of the paper. Let me write the consolidated review.

## Summary

The paper proposes ZMPQ, a zero-shot mixed-precision quantization framework that jointly optimizes calibration data generation (via Gram-Gradient matrix matching) and bit-width allocation (via a scalable quadratic integer program). The data generation objective is derived from a bi-level optimization formulation through gradient matching, and the bit-allocation problem reduces to O(|C|L) forward-backward passes, a significant improvement over prior work CLADO's O(|C|²L²).

## Strengths

- **Scalable quadratic formulation for bit-width allocation (Section 3.3):** The reformulation of bit-width selection as a quadratic integer program in Eq. (17) that requires only O(|C|L) forward-backward passes (vs. O(|C|²L²) for CLADO) is a concrete and practical contribution to mixed-precision quantization efficiency.

- **Strong empirical results on ImageNet, especially in low-bit and mobile settings:** Table 1 shows consistent and substantial improvements over zero-shot baselines. Improvements on MobileNetV2 are particularly notable (11.76%, 7.47%, 1.69% for */2, */3, */4 settings over the next best zero-shot method).

- **Theoretically motivated data generation via Gram-Gradient matching:** The derivation from bi-level gradient matching (Eq. 4) through the k-equivalence concept (Theorem 3.1) to the practical Gram-Gradient cosine similarity loss (Eq. 8) provides a principled framework connecting dataset optimization to higher-order gradient statistics, beyond the BN-matching objectives common in prior ZSQ work.

- **Competitive performance with data-dependent MPQ methods:** Table 2 shows the zero-shot method achieves competitive accuracy with mixed-precision methods that require real data (e.g., 69.37% vs. 68.87% for OMPQ at 4.0 MB budget on ResNet-18), which is a meaningful result for a data-free approach.

## Weaknesses

### Fatal
None.

### Major

- **The contribution of joint optimization is overstated relative to the evidence.** The paper's central claim is that "jointly optimizing both the calibration data and the bit-width" provides meaningful gains. However, the ablation study (Table 3) shows that nearly all performance improvement comes from the bit-width optimization component ("Mixed") alone, while adding the data generation component on top contributes marginal additional gains. The paper itself acknowledges this: "The results show that the bit-width optimization approach has a significantly greater impact on model performance than the data generation approach." As reported in the ablation, on ResNet-18 at */2, Mixed alone adds +4.37pp over baseline while Data+Mixed jointly adds +4.56pp — a marginal 0.19pp incremental improvement from the joint aspect. The "joint optimization" framing implies an interdependent co-optimization benefit, but the empirical evidence primarily supports a strong bit-width allocation method with a minor data generation add-on. The paper would be more honestly presented as a scalable mixed-precision allocation method with a secondary data improvement.

- **The synthetic validation set construction undermines the Gram-Gradient matching's theoretical grounding.** The derivation in Section 3.2 (Eqs. 4–8) motivates Gram-Gradient matching as equating the gradient statistics of the training set X^(T) with a validation set X^(V). Since no real validation data exists in zero-shot settings, the paper constructs X^(V) by interpolating training embeddings (line 141: X^(V) = {G(βz_i + (1-β)z_j)}). This means the target that G_G R A M loss optimizes toward is derived from the very data being optimized. While this is an inherent limitation of zero-shot settings (no real data is available), the paper presents the derivation as if X^(V) were a genuine validation set, and the practical substitute lacks theoretical guarantees that matching interpolated versions of one's own data improves real-data alignment. The derivation from Eqs. (5)–(7) assumes a genuine validation set, but the actual implementation uses a proxy whose relationship to real data is undocumented.

### Minor

- **The k-norm modification in Eq. (7) is a heuristic without formal justification.** The transition from pairwise gradient inner products (Eq. 6) to the k-norm formulation (Eq. 7) is presented as "intuitive" — it up-weights training samples with high gradient matching to each validation sample. This is a reasonable design choice, but it is not derived from the original optimization objective. The specific choice of k=10 is used throughout experiments with no theoretical justification in the main text (the appendix sensitivity analysis is not available), though it is a standard hyperparameter.

- **The one-step gradient approximation (Eq. 6) is a strong simplification.** The approximation δ_{θ_Q} = -α∇_{θ_Q} L_R(θ_Q, θ_FP, X^(T), B) assumes that a single gradient step captures the full training trajectory. While common in meta-learning literature (e.g., MAML), it is a known loose approximation, particularly for the non-smooth loss landscapes typical of quantization.

- **Limited evaluation model diversity.** Only three architectures are tested (ResNet-18, ResNet-50, MobileNetV2). While these cover standard and mobile settings, validation on larger models (e.g., ResNet-101, transformers) would strengthen the scalability claim.

### Trivial
- None worth noting.

## Nice-to-Haves

- An oracle experiment replacing the synthetic validation set X^(V) with a small held-out real data subset would directly test whether the Gram-Gradient matching objective improves with better validation data, and quantify the ceiling of the current design.
- Sensitivity analysis of the k parameter in the Gram-Gradient formulation beyond the appendix.
- Visualization of the learned bit-width allocations across layers versus sensitivity-based allocations.

## Removed Points

- **Formatting/typo complaints:** The harsh critic's note about garbled text in Eq. (15) is a parser artifact, not a paper issue. Removed.
- **NP-hardness of quadratic programming:** Integer quadratic programming being NP-hard in general is standard textbook knowledge; the paper's problem sizes (|C|L ≈ 150 variables for ResNet-18) are tractable. The "scalable" claim refers to forward/backward pass count, not solver complexity. Removed as irrelevant.
- **Claim that L_R(θ_FP, θ_FP, X, B) = 0 so the gradient is exactly zero:** This is factually incorrect. When θ_Q = θ_FP but quantization bit-width B is applied, f_B(θ_FP, x, l) ≠ f(θ_FP, x, l) because quantization still distorts the weights. The gradient is approximately small (well-trained model), not exactly zero. Removed as factually wrong.
- **Missing variance/confidence intervals:** Single-run results are standard in the quantization literature; requiring variance across runs is disproportionate for this venue. Demoted to nice-to-have.
- **Strength claiming "joint optimization is confirmed by Table 3":** Table 3 shows the joint contribution is marginal (0.19pp in the example cited). This strength is tempered by the major weakness above. Removed from strengths.
- **Concern about missing appendix proofs for Theorem 3.1:** Appendix content is stripped from the parsed submission. Removed per rules.

## Novel Insights

The paper reveals an interesting asymmetry: in zero-shot mixed-precision quantization, bit-width allocation is far more impactful than calibration data generation, calling into question the premise that these two problems must be "jointly" optimized. The most genuine technical insight is the quadratic reformulation of bit allocation (reducing from O(|C|²L²) to O(|C|L) passes), which stands on its own irrespective of the joint optimization framing. The Gram-Gradient formulation, while formally motivated, relies on a synthetic validation target that partially undermines its theoretical grounding.

## Suggestions

- Reframe the contribution to foreground the scalable bit-width optimization as the primary contribution, with the data generation and joint framework as secondary supporting contributions. This aligns with the empirical evidence and avoids the overclaim.
- Add a direct comparison isolating the quadratic formulation's benefit: replace Genie's uniform quantization with your bit allocation (already done as "Genie + MPQ"), and additionally compare against a simpler mixed-precision baseline (e.g., HAWQ-style sensitivity scores) on the same data to show what the quadratic formulation specifically contributes beyond any mixed-precision strategy.
- Discuss the theoretical implications of using an interpolated synthetic validation set for Gram-Gradient matching, either acknowledging the limitation or providing empirical evidence (e.g., oracle experiment) that the interpolation strategy is a reasonable proxy.

## Score and Decision

The paper makes a solid, practical contribution in the scalable quadratic bit-width allocation formulation and achieves strong empirical results on ImageNet benchmarks. However, the central narrative of "joint optimization" is significantly overstated — the ablation study clearly demonstrates that the joint aspect contributes marginal improvements over bit-width optimization alone. The Gram-Gradient data generation, while theoretically motivated, relies on a synthetic validation target that partially undercuts its theoretical claims. These issues are significant but do not invalidate the paper's core engineering contribution.

Originality: Moderate — the quadratic formulation is novel and practical; the Gram-Gradient matching is an incremental derivation from existing gradient matching ideas.
Importance: Moderate — zero-shot mixed-precision is a practical problem, and achieving competitive results without real data is meaningful.
Claims support: Partially — the bit allocation claims are well-supported; the joint optimization claim is overclaimed.
Experimental soundness: Good — comprehensive benchmarks, ablation included, but variance not reported.
Clarity: Adequate — the derivation is dense but followable.
Community value: Moderate — the quadratic bit-allocation formulation is useful for practitioners.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>