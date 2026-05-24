Now I have all the information needed. Let me write the consolidated review.

---

## Summary

This paper introduces Continuous Online Action Detection (COAD), a task formulation that enables OAD models to continuously learn and adapt from streaming egocentric video in a single pass without storing data. It curates Ego-OAD, a large-scale egocentric OAD benchmark (87 classes, ~23k instances, 263 hours) from Ego4D. The method combines three training strategies — state continuity, orthogonal gradient projection (Han et al., 2025), and non-uniform loss weighting (An et al., 2023) — to align online training dynamics with causal inference constraints. Experiments on Ego-OAD and EPIC-KITCHENS show that COAD improves out-of-stream generalization over naive online training baselines.

## Strengths

- **New task formulation with explicit constraints**: Section 4.5 precisely defines COAD under strict causal, single-pass, memory-limited conditions — no data storage, no replay, batch-size-one processing. This formulation is clearly distinguished from standard offline OAD training (Section 4.3) and is a genuine addition to the OAD landscape.

- **Large-scale egocentric OAD benchmark Ego-OAD**: The dataset (87 classes, 22,991 instances, 263 hours, 36% label overlap) fills a gap: prior egocentric OAD datasets are confined to single environments (e.g., EPIC-KITCHENS), while Ego-OAD spans diverse daily-life scenarios. The splits follow the established protocol of Carreira et al. (2024a) with pretrain/in-stream/out-of-stream subsets.

- **COAD improves out-of-stream generalization over a fair online-training baseline**: Table 1 shows COAD achieves 76.0 Top-5 Recall (Ego pretrain, out-of-stream) versus 71.6 for w/o COAD — a credible +4.4 point gain. The w/o COAD baseline also improves over Pretrained Only (+2.5), so the incremental benefit of the proposed components is clearly measurable.

- **Thorough component ablation (Table 3)**: The ablation cleanly decomposes the contributions. The orthogonal gradient + non-uniform loss combination drives most of the out-of-stream gain (Row 4, ✗ ✓ ✓: 75.8 Top-5 Recall vs. Row 1, ✓ ✓ ✓: 76.0), showing that these two components are the primary drivers. State continuity provides marginal additional benefit on out-of-stream (76.0 vs. 75.8). This decomposition is informative and honestly presented.

- **Continuous learning approaches the IID upper bound**: Figure 4 traces performance on out-of-stream data as COAD processes more in-stream data, steadily narrowing the gap to the offline IID-trained upper bound despite single-pass constraints.

- **Demonstrates that egocentric pretraining significantly impacts OAD**: Table 1 (Ego vs. Exo pretraining) and Table 4 (TimeSformer vs. TSN) convincingly show that egocentric representations and clip-level architectures are important for egocentric OAD — a direction largely overlooked in prior OAD work.

## Weaknesses

### Fatal
None.

### Major
- **Headline claims conflate "any adaptation" with "COAD-specific" gains**: The abstract claims "up to 20% adaptation" (in-stream Exo Top-5: 57.5→80.0) and "up to 7% generalization" (out-of-stream Ego Top-5: 69.1→76.0). Both Δ values are computed relative to the *Pretrained Only* baseline, which has never seen any in-stream data. The w/o COAD baseline (which also trains on in-stream data) achieves 76.2 and 71.6 respectively — meaning the COAD-specific gains are roughly +3.8 (in-stream) and +4.4 (out-of-stream) percentage points, not 20% and 7%. While the tables themselves are transparent (Δ columns are clearly labeled), the abstract and introduction's framing misleadingly suggests the gains are attributable entirely to the proposed components. This should be corrected.

### Minor
- **No existing OAD methods benchmarked on Ego-OAD**: For a paper that claims dataset contribution, no results from established OAD models (e.g., LSTR, TeSTra, GateHub, MiniROD) trained offline on Ego-OAD are reported. Without these baselines, readers cannot assess how difficult the dataset is or whether COAD's performance is competitive with state-of-the-art offline-trained models on the same data. The "IID Training" baseline in Figure 4 partially addresses this, but it uses the same GRU head, not existing OAD architectures.

- **User-level adaptation is not evaluated**: The paper frames COAD as enabling "adaptation to the user's environment" and "personalized egocentric AI" (Abstract, Section 1, contributions), yet the in-stream/out-of-stream splits are video-level, not user-level. Ego4D contains user identifiers that could support per-user evaluation. The current setup measures adaptation to video-level distributions, not personalization to individual users, creating a gap between the motivation and the evidence.

- **EPIC-KITCHENS results tell a partially different story**: On EPIC-KITCHENS in-stream, COAD roughly matches the Pretrained Only baseline (verb mAP 29.0 both, noun Top-5 13.9 vs. 14.7, action Top-5 20.5 vs. 22.9), while w/o COAD collapses (verb mAP 16.6, action Top-5 14.4). This suggests COAD's role on this dataset is *preventing catastrophic forgetting* during online adaptation rather than improving over the offline model. The paper acknowledges this ("exhibiting signs of overfitting") but the framing in the abstract and introduction emphasizes improvement, not stabilization. This should be more carefully delineated.

- **In-stream evaluation on Ego-OAD shows mixed results for COAD**: On in-stream Ego (Table 1), w/o COAD actually achieves higher mAP than COAD in some settings (Ego in-stream: w/o COAD 39.0 mAP vs. COAD 36.8; Exo in-stream: w/o COAD 31.0 mAP vs. COAD 31.0). The paper explains this as a trade-off between adaptation and generalization, but this asymmetry deserves more discussion — it indicates that COAD's components sometimes hurt in-stream performance while improving out-of-stream generalization.

### Trivial
- **Figure 5 (qualitative results)**: Shows per-frame predictions but without ground-truth overlays, making it difficult to assess correctness visually.

## Nice-to-Haves
- **Test on additional backbones**: The method is only validated on GRU. Testing on a lightweight transformer or even a linear probe on frozen features would strengthen claims about architecture-agnostic applicability.
- **Per-class performance breakdown**: Showing per-class recall would reveal whether COAD helps rare classes or specific action types.
- **Analysis of forgetting/forward-backward transfer**: Continual learning benchmarks typically measure stability on previously seen distributions.
- **Gradient correlation visualization**: A plot of cosine similarity between consecutive gradients, with and without orthogonal projection, would directly demonstrate the decorrelation effect claimed.

## Removed Points

*These points were flagged by reviewers but are removed (with justification) from the main review.*

- **"State continuity alone in Table 3 shows near-identical performance to w/o COAD" [REMOVED — factually wrong]**: The critic claimed that row 3 of Table 3 represents "state continuity only (State Cont. ✓, all others ✗)." In fact, row 3 is (✓ ✗ ✓) — it has both state continuity AND non-uniform loss. No row in Table 3 isolates state continuity alone. The specific numerical comparison cited (25.3/37.4 vs. 25.5/39.0) compares a configuration with two components against none, not state continuity in isolation.

- **"Unfair baseline — w/o COAD should include state continuity" [REMOVED — the w/o COAD baseline is clearly defined and the ablation provides the fair comparison]**: The paper explicitly defines w/o COAD as removing *all three* proposed strategies. The ablation (Table 3) provides rows that isolate each component, allowing readers to assess the contribution of state continuity independently. Moreover, Row 4 (✗ ✓ ✓, 75.8 Top-5) vs. Row 1 (✓ ✓ ✓, 76.0 Top-5) shows state continuity adds only 0.2 points — so even if the main tables had included it, the conclusions would not materially change.

- **"Missing appendix content" [REMOVED — parser strips appendices]**: Criticisms about missing inter-annotator agreement, manual grouping criteria, etc., are about content the paper states is in the appendix. The parser removes appendices from all submissions.

- **"In-stream evaluation measures training metrics, not test metrics" [REMOVED — misunderstands protocol]**: In-stream evaluation measures the model's ability to adapt to the data it is processing, which is standard for continual/online learning evaluations. The protocol follows Carreira et al. (2024a) and is clearly described.

- **"Orthogonal gradient is from Han et al., non-uniform loss from An et al." [REMOVED — proper attribution is a strength, not a weakness]**: The paper correctly cites these sources. Adapting existing techniques to a new problem setting (OAD under streaming constraints) is standard practice.

- **"Pretraining set is too small (186 videos)" [REMOVED — justified design choice]**: The paper explicitly states this is intentional "to better assess the impact of continuous learning." A larger pretraining set would reduce the headroom for measuring adaptation gains, making the experiment less informative, not more. This is a reasoned design choice.

## Novel Insights

The reviews reveal an interesting tension: the orthogonal gradient + non-uniform loss combination is the true driver of COAD's out-of-stream generalization gains (Row 4 of Table 3: ✗ ✓ ✓ = 75.8 Top-5), while state continuity contributes negligibly to generalization (adding it moves from 75.8 to 76.0). Yet state continuity is conceptually necessary for the COAD framing itself (it's what makes training resemble inference). This suggests that the paper's most publishable insight may be that gradient decorrelation and asymmetric loss weighting, not temporal state propagation, are what enable effective single-pass streaming adaptation for OAD. The state continuity is a prerequisite for the setup but not a performance driver — a useful disentanglement that the ablation makes visible.

## Suggestions

1. **Revise the headline numbers**: Frame the abstract and introduction claims using the *w/o COAD* baseline as the reference for COAD-specific gains, or at minimum explicitly state "relative to a model with no in-stream training" when reporting the 20%/7% figures.
2. **Add existing OAD method baselines on Ego-OAD (offline)**: Report at least 2–3 existing OAD models (e.g., MiniROD, LSTR) trained offline on the combined pretraining + in-stream sets, evaluated on the out-of-stream split. This will validate the dataset and contextualize COAD's performance.
3. **Either add user-level evaluation or adjust the framing**: If user identifiers are available in Ego4D, conduct a per-user evaluation. Otherwise, replace "personalization" and "user's environment" language with more precise terms like "video-level distribution adaptation."
4. **Discuss the EPIC-KITCHENS results more carefully**: Acknowledge that on this dataset COAD's primary role is preventing degradation during online training, and clearly distinguish between settings where COAD *improves* vs. *stabilizes* performance.

## Score and Decision

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>