Now I have a thorough understanding of the paper. Let me now write the consolidated review.

The key issues to evaluate:

1. **Linearization concern**: The harsh critic argues that substituting Z_{t-1} with Z_0 eliminates dynamic routing. This is a valid point — in the implemented/evaluated version (Eq. 17-20), the routing uses Z_0 instead of Z_{t-1}, so the routing is fixed based on initial memory + current input rather than history-dependent. However, the paper acknowledges this explicitly (Section 3.1 "Linearisation"), and Theorem 2 proves the general recurrent case also has the desired properties. Figure 3 shows that the linearized version works well. But the critic's concern is that the *motivated* advantage (dynamic, history-dependent routing) is not actually evaluated. This is a legitimate concern.

2. **Permutation experiment confound**: The harsh critic argues that FACTS uses set-function embedders (which are permutation-invariant by construction) while baselines use position-dependent embedders. This is partially true but needs verification. From line 183: "We use the exact same setup... with the exception of the pre- and post-processing modules (referred to as the 'embedders' and 'projectors' in TSLib). In our implementation, we replace these with set functions to accommodate the output structure of FACTS." So FACTS uses set-function embedders, and baselines use standard embedders. The critic's point is that the permutation robustness could come from the embedder, not the SSM mechanism. However, the set-function embedder is *part of the FACTS architectural design* — FACTS requires permutation-invariant embedders to maintain its properties. The comparison is fair in that it tests the full system. But the claim about what specifically makes FACTS robust (the factored SSM vs. the embedder) is hard to disentangle.

3. **"Consistent factor representations" claim**: The paper claims "consistent factor representations over time" (contribution 3, line 27). Theorems 1-2 prove permutation invariance/equivariance, but the critic argues this is different from "semantic consistency" (e.g., the same factor tracking the same object over time). This is a fair criticism — the formal properties prove invariance to input permutations, not that factors are semantically consistent. However, the claim in line 27 says "consistent factor representations over time, regardless of changes in the spatial order of input features" — this is closer to the formal property being proved.

4. **Element-wise operations restriction**: The harsh critic notes that using element-wise multiplication instead of matrix multiplication restricts cross-factor communication. This is true, but the paper acknowledges it explicitly as a design choice for achieving permutation invariance. However, the lack of comparison with a simpler diagonal SSM + set embedder baseline is a notable gap.

5. **Graph data evaluation**: Only METR-LA with 12-step horizon. This is indeed limited but not a fatal flaw.

6. **World modeling claim**: The paper frames itself as a "world model" but only evaluates prediction/forecasting. This is a scope concern but the paper explicitly says it evaluates by prediction accuracy.

Let me now write the final review.</think>Now I have a thorough understanding of the paper. Let me write the final consolidated review.

## Summary

FACTS proposes a factored state-space model for spatio-temporal world modelling that constructs a graph-structured memory with attention-based routing to dynamically assign input features to latent factors. The key idea is to use element-wise operations and set-based routing to achieve permutation invariance with respect to input features (right permutation invariance, R.P.I.) and permutation equivariance of the memory (left permutation equivariance, L.P.E.), formally proved in Theorems 1–2. A linearization step substitutes Z_{t-1} with Z_0 in routing to enable parallel computation. The model is evaluated on multivariate time series forecasting, object-centric prediction on CLEVRER, unsupervised object discovery on MOVi-A, and graph-based traffic prediction on METR-LA.

## Strengths

- **Clean formalization of permutation properties**: Definitions 1–2 and Theorems 1–2 precisely formalize L.P.E. and R.P.I. for the FACTS framework, and Theorem 2 extends the result to the general recurrent case (Z_{t-1}-dependent routing). This is a genuine and useful theoretical contribution that could inform future SSM designs.
- **Permutation robustness demonstrated**: Figure 2 shows that FACTS maintains stable performance under random input feature permutation while iTransformer and S-Mamba degrade substantially (e.g., S-Mamba's MSE on Traffic increases >3×). This validates the core practical advantage of the permutation-invariant design.
- **Versatile evaluation across task types**: The paper evaluates on MTSF (9 datasets), object-centric video prediction (CLEVRER), unsupervised object discovery (MOVi-A), and graph-structured prediction (METR-LA), showing competitive or superior performance across diverse domains.
- **Linearization with minimal performance loss**: Figure 3 shows that varying the window size from fully recurrent (1) to fully parallel (96) on Electricity yields consistent performance, supporting the practical viability of the Z_0 substitution for parallel computation.

## Weaknesses

### Fatal
None.

### Major

- **Gap between motivated dynamic routing and the evaluated linearized version**: The paper's core motivation (Section 1, Section 3.1) emphasizes that "input features are dynamically assigned to distinct state-space factors" and that the routing between memory and inputs "dynamically determin[es] which features correspond to which latent factors" using Z_{t-1} as queries (Eq. 12). However, the actually implemented and evaluated version (Eq. 17–20) substitutes Z_{t-1} with Z_0, making routing dependent only on a fixed initial memory and the current input, not accumulated history. The paper acknowledges this in the "Linearisation" paragraph, but the language throughout (e.g., "dynamically assigns," "adapting through selective state-space propagation") continues to imply history-dependent routing. The degree to which dynamic routing contributes is unclear because no experiment compares the full recurrent version (Z_{t-1}-dependent routing) against the linearized version on a task that requires dynamic feature-to-factor reassignment. Figure 3 shows similar performance across window sizes, but this only varies how often Z_0 is refreshed, not whether Z_{t-1}-dependent routing differs from Z_0-dependent routing. This matters because if the linearized model already works well with fixed-query routing, the paper's central architectural claim about "selective memory-input routing" needs reframing—the primary benefit may be the factored/element-wise structure and permutation-invariant embedders, not the routing dynamics.

- **Permutation experiment confounded by embedder design**: In Scenario 2 (Section 4.1.2), FACTS uses set-function embedders (line 183), which are inherently permutation-invariant, while iTransformer and S-Mamba use standard position-dependent embedders that assign different representations based on positional index. This makes the baselines vulnerable to permutation by construction of their input pipelines, independently of the SSM mechanism. The experiment therefore cannot isolate whether FACTS' robustness stems from its factored state-space design or from its permutation-invariant preprocessing. While set-function embedders are a legitimate architectural choice within FACTS, the claimed architectural contribution of the factored SSM is not separately validated. Adding a baseline that uses a diagonal SSM with set-function embedders would help disentangle these contributions.

### Minor

- **"Consistent factor representations" claim exceeds formal guarantees**: Contribution 3 (line 27) states "FACTS achieves consistent factor representations over time," but Theorems 1–2 establish permutation invariance/equivariance—i.e., that reordering inputs does not change outputs. This is a formal mathematical property, not a guarantee that the same latent factor semantically tracks the same entity over time (e.g., object identity consistency). No experiment directly measures factor-to-object tracking accuracy. The claim would be more precise if stated as "permutable state-space memory that is invariant to input feature permutation."

- **Limited graph evaluation scope**: The graph-structured data experiment (Section 4.3) uses only a single dataset (METR-LA) at a single horizon (12-step), which provides limited evidence for the claim of versatility across graph-structured data.

- **Element-wise operations restrict cross-factor communication**: The use of element-wise (Hadamard) multiplication instead of matrix multiplication in the state update (Eq. 10) eliminates cross-factor communication through the state transition matrices A and B. While this is necessary for the permutation properties, the representational cost is not analyzed. The paper does not compare against a simpler diagonal SSM with set-function embedders, which would also be permutation-invariant for similar structural reasons, making it unclear how much the routing mechanism adds beyond the element-wise factor structure.

### Trivial
None.

## Nice-to-Haves

- Compare the full recurrent FACTS (Z_{t-1}-dependent routing) against the linearized version (Z_0-dependent routing) on a task requiring dynamic feature-to-factor reassignment, to quantify the benefit of history-dependent routing.
- Test iTransformer/S-Mamba with set-function embedders as an additional baseline in Scenario 2 to isolate the contribution of the FACTS SSM mechanism from the embedder design.
- Report factor-to-object tracking consistency (e.g., Hungarian-matched identity persistence) in the object-centric experiments to directly validate the semantic consistency claim.
- Add a diagonal SSM + set embedder baseline to clarify whether the attention-based routing mechanism provides benefits beyond the element-wise factor structure.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"World modelling scope overclaimed"** (from Harsh Critic): The paper frames itself as a general "world model" but only evaluates prediction/forecasting tasks. However, the paper explicitly states in Section 4: "We frame world modelling as a prediction task" — this scoping is clear and standard in the literature. Removed as the paper already addresses this.

- **"Insufficient object-centric baselines"** (from Harsh Critic): Requesting comparison with SAVi+Transformer, STEVE, DINOSAUR. The paper does compare with SlotFormer (the main baseline for slot dynamics) and SAVi (for unsupervised discovery). Missing baselines is not a fatal flaw for a general-purpose framework paper, and the cited models may have different training setups. Removed as demand for additional baselines is a generic suggestion rather than a demonstrated deficiency in the current comparison.

- **"Routing mechanism not sufficiently distinguished from Slot Attention/Perceiver"** (from Harsh Critic): This is a related work positioning concern. The paper explicitly presents its contribution as combining cross-attention routing with per-slot SSM dynamics, which is a distinct design. Removed as a missing-related-work issue without external verification.

- **"Metric-selective reporting (6/9 on MAE)"** (from Harsh Critic): The paper reports both MSE and MAE for all datasets, and its claim of "6 out of 9" on MAE is factually stated. Readers can see the MSE results in the same table. This is not misleading reporting; it highlights FACTS' stronger metric. Removed as nitpick.

- **Strength Finder claim that "Theorem 1 formally proves L.P.E. and R.P.I."** as a strength separate from the broader formalization strength. This is already captured in the main formalization strength. Removed as redundant.

- **Strength Finder claim about "unsupervised object discovery demonstrating factor interpretability"**: The paper references Table 7 (appendix) for quantitative claims, and the main text provides only qualitative visualization. Kept as minor but removed as a standalone strength because the quantitative evidence is not in the main paper.

## Novel Insights

The key tension in this paper is between the theoretical appeal of history-dependent routing (Eq. 10–14, using Z_{t-1} as queries) and the practical implementation that replaces Z_{t-1} with a fixed Z_0. Theorems 1 and 2 are both stated for the linearized version and the general case respectively, suggesting the authors view both as valid FACTS configurations. However, the paper's strongest motivational language ("dynamic," "selective," "adapting") best describes the recurrent version, while the evaluated version functions more like learned-prototype matching. Whether this matters depends on the application—for time series forecasting where input-feature-to-factor mappings are relatively stable, the linearized version may be sufficient; for scenarios requiring genuine online reassignment, the gap could be consequential. This distinction deserves more transparency in the paper's narrative.

## Suggestions

- Reframe the narrative to be transparent about the linearization: explicitly acknowledge that the evaluated model uses fixed-query routing (Z_0) rather than history-dependent routing (Z_{t-1}), and discuss the trade-off this represents. The current language of "dynamic" routing overclaims for the implemented version.
- Add an ablation comparing Z_{t-1}-routing vs. Z_0-routing (even if only on a small/benchmark task) to inform readers whether dynamic routing adds value or the linearized version is sufficient.
- In the permutation experiment, add a diagonal SSM with set-function embedders as a baseline to isolate the contribution of the factored state-space structure from the preprocessing choice.

## Overall Assessment

**Originality**: The formalization of L.P.E. and R.P.I. properties for SSMs and the factored state-space design with permutation-invariant routing is novel and well-motivated. The combination of cross-attention routing with per-factor SSM dynamics is a creative architectural contribution.

**Importance**: Permutation sensitivity in SSMs for world modelling is a real and practical problem, especially for multi-agent systems and scenarios with variable input orderings. The problem is clearly articulated.

**Claim support**: The core claims are partially but not fully supported. The permutation invariance is formally proved and empirically validated, but the experiment is confounded by embedder choice. The "consistent factor representations" claim exceeds the formal guarantees. Most importantly, the evaluated model's routing uses Z_0 rather than Z_{t-1}, which materially weakens the "dynamic routing" narrative—the paper's main selling point.

**Experimental soundness**: Evaluation across MTSF, object-centric prediction, and graph tasks is commendable. The graph evaluation (single dataset/horizon) and the missing ablation separating embedder vs. SSM contributions are notable gaps.

**Clarity**: The paper is generally well-written, with clear theoretical exposition, though the framing of the linearized model as "dynamic routing" is somewhat misleading.

**Community value**: The formal framework and clean definitions provide a useful addition to the SSM design space, even if the empirical contribution of the routing mechanism per se remains unclear.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>