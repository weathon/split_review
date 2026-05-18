Now I have a thorough understanding of the paper and all the review inputs. Let me produce the consolidated review.

---

## Summary

This paper introduces the Subgraph Multilinear Extension (SubMT) as a theoretical lens for analyzing intrinsically interpretable GNNs (XGNNs). The authors observe that existing attention-based XGNNs approximate the expectation of the classifier output over subgraphs by feeding a soft (attention-weighted) adjacency matrix through a nonlinear GNN, creating a systematic gap due to Jensen's inequality. They propose two practical remedies — GMT-lin (reducing weighted message-passing to one round) and GMT-sam (Monte Carlo sampling from the learned subgraph distribution) — along with a counterfactual fidelity metric. Empirical results across regular and geometric graph benchmarks show consistent improvements over prior XGNNs like GSAT and LRI, often by sizable margins.

## Strengths

- **Consistent and sizable empirical improvements.** Tables 1–4 show that both GMT variants outperform state-of-the-art XGNNs across multiple datasets and backbones (GIN, PNA, EGNN). The gains reach up to 15% on Spurious-Motif and 6–8% on MNIST-75sp and geometric benchmarks, with shadowed entries indicating statistical robustness. This is the paper's strongest evidence and directly supports the claim of practical effectiveness.

- **Generality across graph types and backbones.** The evaluation covers both regular graphs (BA-2Motifs, Mutag, MNIST-75sp, Spurious-Motif, Graph-SST2, OGBG-MolHIV) and geometric graphs (ACTSTRACK, TAU3MU, SYNMOL, PLBIND), using three different GNN backbones. This breadth convincingly shows that the SubMT framework and GMT improvements are not tied to a single architecture or domain.

- **Useful conceptual framework (SubMT).** The formulation of interpretable subgraph learning as a multilinear extension (Definition 3.1) provides a clean mathematical abstraction that clarifies what existing XGNNs are trying to compute. While the core observation (nonlinearity creates a gap between f(𝔼[A]) and 𝔼[f(A)]) is basic, the paper is the first to formalize this as SubMT and connect it to XGNN architecture design. This framing has pedagogical value and provides a clear motivation for the proposed methods.

- **Provably correct estimation via sampling (Theorem 5.1).** Theorem 5.1 provides a probabilistic guarantee that GMT-sam's Monte Carlo estimate converges to the SubMT expectation under the learned attention distribution. While this is structurally a standard Hoeffding concentration bound, its application to the XGNN setting is novel and directly supports the claim that GMT-sam better approximates SubMT than methods that simply feed the soft adjacency through a nonlinear GNN.

## Weaknesses

### Fatal

None.

### Major

- **Overclaimed theoretical contribution relative to what is actually proved.** The paper is framed as providing a "theoretical framework" for XGNN expressivity, but the theoretical content is substantially thinner than the rhetoric suggests:
  - **Proposition 3.3** claims that linear GNNs with k>1 "cannot approximate SubMT." The main text supports this with a single example (k=2, |𝒱|=1) invoking Jensen's inequality. Even if a full proof resides in the appendix (which was stripped by the parser), presenting a sweeping impossibility claim with only an illustrative example in the main body creates a misleading impression of rigor. The proposition as stated is essentially the observation that nonlinear functions do not commute with expectation — which, while true, does not constitute a deep theoretical characterization of when and how XGNNs fail.
  - **Section 3 as a whole** does not deliver the promised "theoretical framework for characterizing the expressivity of XGNNs." There is no taxonomy of existing XGNN architectures by their SubMT approximation error, no quantitative bounds on the gap for specific GNN families (e.g., GIN with sum pooling, PNA), and no analysis of how the gap propagates through training. The paper identifies a real problem but does not provide the systematic theoretical apparatus that the framing advertises.

- **Theorem 5.1's scope is narrower than the paper's central claims about it.** Theorem 5.1 shows that, *given* the attention matrix Â, GMT-sam's Monte Carlo average approximates the expectation under the *same* distribution with high probability. This is a correct but unsurprising concentration bound. The theorem says nothing about whether Â (and therefore the subgraph distribution) is itself close to the true causal subgraph distribution — which is what interpretability and OOD generalization ultimately require. The paper's claim that GMT-sam is "provably more powerful" conflates unbiased estimation of a *fixed* expectation with better *learning* of the subgraph distribution. The real empirical improvements likely come from the training dynamics (e.g., Gumbel softmax gradients, avoiding weighted message passing during training), but these are not covered by Theorem 5.1. The paper would be stronger if it separated what is formally proven (concentration under a fixed distribution) from what is empirically observed (better subgraph learning).

- **The counterfactual fidelity metric mixes definition-level generality with measurement-level specificity in a problematic way.** Definition 4.1 is stated in terms of arbitrary full-graph pairs (G, G̃), but the interpretation (line 168) immediately translates it to "perturbations on Ĝ_c." The practical estimation (Eq. 11) then perturbs the attention matrix Ã rather than the subgraph directly. The "simulated SubMT" baseline used in Figures 2(b)/(c) is not clearly defined — the paper never specifies how the ground-truth subgraph distribution is obtained for datasets like BA-2Motifs and Mutag. Moreover, the high counterfactual fidelity of GMT-sam (Figure 3(a)) may be partially an artifact of Monte Carlo averaging smoothing the prediction, rather than a sign of better subgraph identification. The metric is a useful idea, but its formulation, estimation, and interpretation need significant clarification before it can support the paper's claims.

### Minor

- **GMT-lin's theoretical motivation does not directly extend to the non-linear backbones used in experiments.** GMT-lin is derived under the assumption of a *linearized* GNN classifier (k=1 preserves linearity in A). Yet the experiments use GIN, PNA, and EGNN — all with non-linear activations and pooling. The paper acknowledges this gap (Section 5.2, line 208: "GMT-lin may also suffer from the SubMT approximation failure" with non-linear GNNs) and appeals to empirical results. This is acceptable but creates a disconnect between the theory (which requires linearity) and the practice (which does not enforce it). The paper should clarify what architectural changes GMT-lin actually makes when combined with a non-linear backbone, and whether the empirical gains stem from SubMT approximation or from other factors (e.g., reduced depth, different gradient flow).

- **Training details for GMT-sam are underspecified.** The paper mentions incorporating Gumbel softmax and straight-through estimators for backpropagating through discrete sampling (line 226) but gives no details on which specific variant is used, how the temperature is annealed, or what the sampling budget t is across datasets. The "learning neural SubMT" (retraining a classifier with frozen extractor) is described in a single paragraph (lines 228–232) with no experimental disentanglement of its contribution. These are not fatal omissions but harm reproducibility.

- **No computational cost analysis.** GMT-sam requires t forward passes per graph during both training and evaluation. The paper does not report t values, wall-time comparisons with GSAT, or any discussion of the accuracy-efficiency trade-off. A practitioner cannot assess whether the gains justify the overhead without this information.

### Trivial

- The "shadowed entries" criterion in Tables 1–4 (mean minus one standard deviation exceeding the best baseline mean) is non-standard; reporting mean ± std with explicit statistical significance tests would be more conventional.
- Figure 2 captions and descriptions are garbled in the extracted text, making the "simulated SubMT" procedure unclear.

## Nice-to-Haves

- An ablation separating the benefit of (i) training with soft subgraph + evaluating with sampling vs. (ii) training with sampling + evaluating with sampling would help isolate whether the improvements come from training or evaluation.
- Quantitative bounds on the SubMT approximation gap for specific GNN families (e.g., GIN with sum pooling, PNA with attention) would strengthen the theoretical contribution.
- Reporting the number of samples t used in GMT-sam and the resulting wall-clock time vs. GSAT would improve practical utility.

## Removed Points

These points were identified by reviewers but are removed or downgraded for the reasons noted:

- *"XGNN notation could cause confusion"* — The paper clearly defines XGNN as intrinsically interpretable GNNs in Section 2 (line 31). This is an explicit definition, not a source of confusion. **Removed (misunderstands the paper's clear definition).**
- *"The theoretical contribution is just Jensen's inequality"* — While the core mathematical observation is indeed Jensen's inequality, the paper's contribution lies in *framing* interpretable subgraph learning as SubMT, identifying its consequences for XGNN faithfulness, and designing architectures around it. Reducing the contribution to "just Jensen's inequality" ignores the framing and architectural novelty. **Removed (overly reductive characterization).**
- *"Proposition 3.3 proof is missing"* — The full proof may reside in the appendix, which was stripped by the parser. The main text provides an illustrative example; the complete proof likely exists in the original submission. **Removed (per rule: parser-stripped appendix content).**
- *"GMT-lin with non-linear backbones is insufficiently explained"* — The paper explicitly acknowledges this limitation (line 208). The claim is that GMT-lin *works empirically* with non-linear backbones, not that the theory covers this case. **Downgraded from major to minor.**
- *"Counterfactual fidelity is a new metric (strength)"* — This conflicts with the verified weakness that the metric's definition and measurement are misaligned. Per rules, when strength and weakness disagree, the weakness wins. **Moved to Removed Points.**
- *"Addresses practical deployment challenges (strength)"* — Generic, lacking specific evidence. **Moved to Removed Points.**

## Novel Insights

The most valuable observation from the review process is the identification of a confound in the counterfactual fidelity metric: Monte Carlo averaging in GMT-sam smooths the prediction, which could artifactually inflate the measured fidelity. This means the fidelity differences in Figure 3(a) may partially reflect prediction variance reduction rather than improved subgraph identification. Disentangling these two effects would substantially strengthen the paper's evaluation. Additionally, the review highlights that the paper's strongest evidence is empirical (consistent gains across diverse settings), while the theoretical framing — while useful — is best read as a motivating conceptual lens rather than a rigorous expressivity analysis.

## Suggestions

1. **Right-size the theoretical claims.** Reframe Section 3 as a "motivating observation" or "conceptual framework" rather than a full theoretical characterization. Qualify Proposition 3.3 to reflect what is actually shown. If the full proof is in the appendix, reference it explicitly in the main text.

2. **Clarify the scope of Theorem 5.1.** Acknowledge explicitly that the theorem bounds estimation error *under the learned distribution*, not the quality of the learned distribution itself. Separate the formal guarantee (concentration) from the empirical claim (better subgraph learning via training).

3. **Fix the counterfactual fidelity metric.** Align the definition with what is actually measured (sensitivity to attention perturbations). Explain how the "simulated SubMT" baseline is constructed. Discuss the potential confound that Monte Carlo averaging may inflate fidelity values.

4. **Provide missing experimental details.** Report: the number of samples t used in GMT-sam, the Gumbel softmax temperature schedule, wall-clock time vs. baselines, and whether the "learning neural SubMT" retraining is used in the main experiments.

5. **Include an ablation separating training vs. evaluation benefits.** Compare (train soft, eval sampling) vs. (train sampling, eval sampling) to attribute gains correctly.

## Score and Decision

This paper makes a genuine empirical contribution — the two proposed GMT variants consistently and substantially outperform existing XGNNs across diverse benchmarks. The SubMT formulation, while not deep as a theory, provides useful conceptual clarity. However, the paper systematically overstates its theoretical contributions, and several key claims (Proposition 3.3, Theorem 5.1's scope, counterfactual fidelity measurement) need correction or clarification. These issues are addressable in revision and do not undermine the core empirical findings.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>