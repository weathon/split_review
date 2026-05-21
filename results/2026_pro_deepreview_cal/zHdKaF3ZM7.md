Now I have all the calibration data I need. Let me synthesize the final review.

---

## Summary

This paper introduces WARP (Weight-space Adaptive Recurrent Prediction), a sequence model where the hidden state of a linear RNN is the flattened weights of an auxiliary MLP (the "root network"). The recurrence θ_t = A θ_{t-1} + B Δx_t is linear in the weight-space, enabling parallel training, while the decoding y_t = MLP_{θ_t}(τ) reintroduces non-linearity. The authors demonstrate the model on image completion, energy/traffic forecasting, dynamical system reconstruction, time-series classification, and in-context learning, with a physics-informed variant (WARP-Phys) achieving >10× improvement over baselines on dynamical systems.

## Strengths

- **Genuinely novel architecture**: The core idea — using the weights of an MLP as the hidden state of a linear RNN — is creative and, to my knowledge, original. The unification of weight-space learning with linear recurrence is a fresh direction that opens interesting possibilities for gradient-free weight adaptation and physics-informed modeling.

- **Impressive performance on image completion**: On MNIST (Table 1), WARP achieves the best MSE and BPD across all context lengths (L=100, 300, 600), matching or surpassing S4 while using comparable parameters. On CelebA, it substantially outperforms all listed baselines. The qualitative results in Fig. 3(a) are visually compelling.

- **Physics-informed variant shows genuine gains**: WARP-Phys on the MSD dataset achieves MSE of 0.03 vs. 0.34 for the Transformer (Table 3), a >10× improvement. This demonstrates that the architecture's design — where the root network can directly embed physical formulations — provides a meaningful advantage over black-box alternatives.

- **Strong classification on several UEA benchmarks**: WARP establishes new state-of-the-art on Ethanol (36.49%) and Heartbeat (80.65%), and places competitively (top-3) on SCP2 and Motor (Table 4), despite not being explicitly designed for very long-range dependencies.

- **Well-motivated design choices**: The input-difference recurrence (Δx_t rather than x_t), the identity initialization of A, and the zero initialization of B are theoretically grounded (connecting to NCDE theory and gradient-descent analogies) and practically sensible.

- **Clear exposition of the core idea**: The architecture is well-explained in Section 2, with Fig. 1 and Fig. 2 effectively communicating the conceptual leap from standard RNNs to weight-space linear RNNs.

## Weaknesses

### Fatal

None. The core contribution — a linear recurrence operating in weight space with non-linear self-decoding — is sound and the paper reports substantive empirical results across multiple domains.

### Major

- **Traffic forecasting result lacks sufficient scrutiny and detail**: WARP's PEMS08 result (MAE 6.59, RMSE 10.10; Table 2) represents a >50% improvement over graph-aware SOTA methods — an extraordinary margin for a model that claims not to use spatial structure. The paper provides limited explanation of how this is achieved: the τ coordinate, the non-causal convolution preprocessing, and the non-AR training mode are mentioned but their roles are not analyzed. Without an ablation showing that the coordinate system does not encode spatial information (e.g., node identities), the claim that WARP outperforms graph methods without graph structure cannot be fully evaluated.

- **Weak baselines on key benchmarks**: The ETT energy forecasting evaluation (Fig. 3b) compares only against GRU and LSTM — no Transformer, SSM, or other modern architecture that defines the state of the art on this dataset. On CelebA image completion (Table 1), S4 is omitted despite being present in the MNIST comparison. The in-context learning experiments (Section 3.4) contain no quantitative metrics and no comparison to any existing ICL method (e.g., Transformers, linear attention). These omissions prevent assessment of WARP's standing relative to the true state of the art on these tasks.

- **"Gradient-free adaptation" is oversold**: The paper frames gradient-free test-time adaptation as a core advantage (Section 2.3, Abstract), but during inference every RNN updates its hidden state without gradient computation — the forward pass IS the adaptation. What WARP uniquely offers is adaptation specifically in weight space (the hidden state IS the weights of a network), which is interesting but different from the claimed novelty. No experiment demonstrates a task where WARP's weight-space adaptation solves a problem that a standard RNN's hidden-state update cannot.

### Minor

- **In-context learning evaluation is qualitative only**: Section 3.4 shows scatter plots (Fig. 5) but reports no quantitative metrics (e.g., MSE on query predictions), no comparison to baselines, and no statistical evidence. The cumulative-sum transformation may also simplify the task — the final representation contains the sum of all keys, potentially making the regression solvable by a simple linear readout. The claimed computational savings ("process subsequent queries without re-evaluating the entire sequence") are not quantified.

- **LSTM pathology on CelebA unexamined**: The LSTM achieves BPD of 3869 at L=100 (Table 1), indicating a clear training failure. The paper neither acknowledges nor explains this, which undermines confidence in the experimental protocol for that dataset.

- **Abstract overclaims relative to evidence**: Phrases like "redefine sequence modeling" and "transformative paradigm" are promotional and not justified by the current evidence. The claim "featuring in the top three in 4 out of 6" datasets is technically true but masks that WARP ranks last on EigenWorms (70.93% vs. best 95.0%) and third on SCP2 by a large margin (57.89% vs. 70.3%).

- **No comparison to weight-space learning baselines**: The paper frames itself partly in the weight-space learning literature (Section 1) but does not compare against hypernetwork baselines, neural processes, or other methods that also generate network weights from data. Such comparisons would directly test whether the linear recurrence over weights adds value beyond simpler weight-generation schemes.

### Trivial

- The paper references ablation studies (Section 4.1: "Ablation studies confirm…") but these are only in the appendix; a brief summary in the main text would strengthen the architectural claims.
- LSTM BPD value of 3869 in Table 1 is printed without scientific notation, making the table harder to read.

## Nice-to-Haves

- A complexity analysis (wall-clock time, memory footprint as a function of D_θ) in the main body rather than only in the appendix, given that the paper claims computational efficiency as an advantage.
- An ablation removing potential spatial information from τ on the PEMS08 task to verify the "no graph structure" claim.
- Quantitative ICL results with comparison to at least one Transformer or linear-attention baseline.
- Standard deviations on the PEMS08 and ETT results (currently single values without error bars).

## Removed Points

These points are flagged to be removed — treat them with caution:

- **"Core mechanics severely underspecified — D_θ, root MLP depth/width never stated"**: The paper references Appendices C and D for experimental details; these exist in the original submission. Per policy, I do not penalize for appendix-only details. The main text does specify that the root network is a fixed-width MLP with D_x-dimensional input and D_y or 2×D_y output, which provides the structural framing.

- **Speculation about data leakage on PEMS08**: The harsh critic hypothesizes that the coordinate τ might include node IDs, making the "no graph structure" claim disingenuous. This is speculation — the paper describes τ as a coordinate system like normalized pixel locations or positional encoding. Without evidence of actual leakage, this remains a concern about insufficient detail, not an identified flaw.

- **"Gradient-free adaptation is exactly what every RNN does — the claimed test-time adaptation is a restatement of the forward pass"**: While the framing is indeed oversold (kept as a Major weakness), the harsh critic's framing that this makes the contribution vacuous is too strong. The distinction is that the hidden state IS the network weights, which is genuinely different from standard RNN hidden states.

- **"No physics-informed baseline to establish unique benefit"**: This is scope creep. WARP-Phys is compared to standard RNNs and Transformers, and the 10× improvement is striking even without a physics-informed baseline. Requiring a physics-informed baseline is a nice-to-have, not a flaw.

- **Demand for standard deviations, multiple runs, diagnostic plots across all experiments**: This is a generic criticism applied uniformly. The paper does report ± values for dynamical system results (Table 3) and classification (Table 4). The absence on some tables is noted appropriately in the minor section.

- **Strength Finder: "WARP-Phys attains MSE 0.03 vs 0.94 for the best alternative"**: The strength text says "0.94 for the best alternative" but Table 3 shows Transformer achieves 0.34 on MSD. The 0.94 is regular WARP. The 10×+ claim is still valid (0.03 vs 0.34), but the specific comparison figure was inaccurate. I've corrected this in the strengths above.

- **Strength Finder: "Input-difference recurrence enables continual adaptation"**: This is a design motivation, not a demonstrated strength. The paper does not show that input differences lead to better adaptation than raw inputs.

- **Strength Finder: "Ablation studies confirm architectural necessity"**: These are in the stripped appendix, so I cannot verify them. Not included as a strength.

## Novel Insights

The most interesting emergent insight from reviewing this paper is that the weight-space linear recurrence creates an unusual asymmetry: the recurrence itself is linear (enabling parallel scans and efficient training), but the decoding through the root MLP provides non-linear expressivity. This design sidesteps the expressivity limitations of purely linear RNNs without sacrificing their computational advantages. The paper would be strengthened by explicitly analyzing this tradeoff — e.g., measuring how much of the model's power comes from the recurrence dimension D_θ vs. the root network's depth/width.

## Suggestions

- **Make the PEMS08 evaluation the centerpiece of a revised empirical story**, with thorough ablations: vary the τ coordinate, remove the non-causal convolution, test with and without node identity information. This would either validate the impressive result or identify what's driving it.
- **Add at least one modern baseline to ETT** (e.g., a Transformer variant, PatchTST, or an SSM) and **add S4 to the CelebA comparison** to make those evaluations credible.
- **Replace the qualitative ICL section with a quantitative one**: report MSE on held-out queries, compare against a simple Transformer or linear attention baseline, and quantify the claimed computational savings.
- **Tone down the promotional language** in the abstract and conclusion. The architecture is interesting enough to stand on its own without phrases like "redefine sequence modeling" and "towards human-level artificial intelligence."
- **Add a paragraph summarizing the ablation studies** from Appendix E into the main text, particularly the ablations on input differences, identity initialization of A, and root network design.

## Score and Decision

### Calibration Anchors

| Anchor | Avg Score | Round | Comparison to WARP |
|--------|-----------|-------|--------------------|
| RotRNN (z6qmomJW91) | 4.00 | 1 | WARP is substantially more novel and has broader, stronger experiments |
| ProbeGen (XoYdD3m0mv) | 6.00 | 1 | WARP is comparably novel with broader scope; ProbeGen's evaluation is more tightly controlled |
| LinOSS (GRMfXcAAFh) | 8.00 | 1 | LinOSS has theoretical guarantees (universality proofs) and more thorough experiments; WARP lacks this depth |
| PIMRL (w3rbBVJ9Jg) | 6.25 | 2 | Comparable: both physics-informed, novel architectures; WARP's core idea is more original |
| PoDiNNs (U1DjXQeJRx) | 6.60 | 2 | PoDiNNs has stronger theory and more focused evaluation; WARP has broader scope but thinner evaluation in places |
| TimeCapsule (blgJ4g00rC) | 5.50 | 2 | WARP is more novel and has stronger results |

**Round 1 bracket**: 4.5–7.5. WARP is clearly stronger than RotRNN (4.0) and clearly weaker than LinOSS (8.0).

**Round 2 narrowing**: 5.5–6.5. WARP is more novel than TimeCapsule (5.50) and comparably ambitious to PIMRL (6.25). It is slightly below PoDiNNs (6.60) in execution quality but comparably novel. The score settles at **6.0**.

**Rationale**: WARP presents a genuinely novel and creative architecture with some impressive results (image completion, physics-informed modeling, competitive classification). However, significant evaluation gaps — weak baselines on ETT, missing S4 on CelebA, qualitative-only ICL evaluation, and an insufficiently scrutinized traffic forecasting result — prevent a higher score. The paper is above the accept/reject borderline but requires the authors to address these gaps in a rebuttal or revision. The overclaiming in the abstract is a presentation issue that compounds the concern about inflated claims.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>