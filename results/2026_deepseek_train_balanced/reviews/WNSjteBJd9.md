Now I've read the full paper and verified each claim against the text. Let me construct the consolidated review.

## Summary

This paper proposes Decodable Unique Watermarking (DUW), a backdoor-based watermarking framework for federated learning that simultaneously enables ownership verification and tracking of which specific client leaked the model. DUW uses a pre-trained encoder to embed client-unique keys into OoD trigger sets and a decoder (replacing the classifier head) to give each client a unique target label in a higher-dimensional space, avoiding collisions. Experiments across Digits, CIFAR-10, and CIFAR-100 show 100% tracking accuracy (TAcc) under standard conditions and after fine-tuning, pruning, model extraction, and parameter perturbation attacks, with watermark success rates (WSR) exceeding 99% in most settings.

## Strengths

- **100% tracking accuracy across all benchmarks (TAcc = 1.0000):** Table 1 (`tab:benchmark_results`) shows that DUW correctly identifies the infringing client in every trial on Digits, CIFAR-10, and CIFAR-100. This directly supports the paper's central claim of accurate IP tracking (R1), which prior work WAFFLE cannot do at all and FedTracker requires parameter access for.

- **Decoder ablation proves the mechanism addresses the collision problem:** Table `tab:decoder` shows TAcc jumps from 6% (without decoder) to 100% (with decoder) in a 100-client CIFAR-10 experiment. This is a clean causal demonstration that the decoder's higher-dimensional target labels — not dataset idiosyncrasies — drive collision avoidance (R1).

- **TAcc remains 100% under all four attack families tested:** Fine-tuning (Table `tab:finetune`), pruning up to 50% rate (Fig. `fig:prune`), model extraction via knockoff (Table `tab:extraction`), and parameter perturbation up to α_noise=10⁻² (Fig. `fig:noise`) all preserve perfect tracking accuracy. This is a stronger robustness result than many watermarking papers in FL, which often test fewer attack types.

- **Scalability demonstrated up to 600 clients:** Table `tab:diff_client` shows TAcc remains 100% even with 600 clients, with WSR at 73.37% and WSR_Gap at 63.83%. This substantially exceeds the typical cross-silo FL setting (tens to low hundreds of clients) that the paper targets.

- **Data-free utility preservation with clear ablation:** The l₂ regularization approach (Eq. 8) requires no client data, and the β ablation (Fig. `fig:beta_iter`) shows β=0.1 improves validation accuracy by 6.88% over β=0 while keeping WSR above 90%, providing principled guidance for the utility-watermark trade-off.

## Weaknesses

### Fatal

None.

### Major

- **No experimental comparison against prior work (WAFFLE, FedTracker).** The paper qualitatively positions itself relative to WAFFLE (lines 45–46, 110–111) and FedTracker (lines 47–50, 90–92), claiming WAFFLE cannot track individual infringers and FedTracker requires parameter access. Yet the experimental section (§4) evaluates DUW in complete isolation. There is no table, ablation, or benchmark showing what WAFFLE or FedTracker achieve on the same datasets, under the same attacks, with the same metrics (WSR, TAcc, Acc). Without this, the reader cannot assess whether DUW actually improves on existing approaches. While WAFFLE fundamentally cannot track individuals, FedTracker also does individual-level tracking, and both prior methods could serve as baselines for shared evaluation dimensions (utility preservation, robustness). This gap substantially weakens the paper's claimed contribution of advancing the state of the art. — *Verifiable: the paper contains no baseline comparison tables.*

- **Collusion attack scenario and multi-client information sharing are not considered.** Since each client receives a *different* watermarked model, two or more colluding clients could compare their models, average them, or interpolate between them to isolate and remove client-specific watermark components. This is a natural attack surface that shared-watermark schemes (WAFFLE) do not face, so DUW's client-unique watermarks create this vulnerability. Similarly, the paper does not consider a client who accumulates multiple rounds of differently-watermarked models over time. The threat model (§4.2) only covers independent single-client attacks. — *Verifiable: the robustness section (lines 318–395) lists only fine-tuning, pruning, extraction, and parameter perturbation; collusion is absent.*

- **Verification threshold σ is never specified.** The paper defines σ as the threshold for establishing ownership (Definition 1, Eq. 2, line 108) and uses it in the tracking logic (line 225). However, no concrete value is reported anywhere, nor is a procedure for setting it described. Without σ, the reader cannot assess whether a degraded WSR (e.g., 66.38% after model extraction on CIFAR-10) would actually pass verification. — *Verifiable: the paper mentions σ in lines 101, 108, 225 but never assigns or discusses a specific value.*

- **Cross-client aggregation (FedAvg) interaction with per-client watermarks is unanalyzed.** In each round (Algorithm 1), the server injects different watermarks into each client's model (using the decoder), clients train locally (without the decoder, which is swapped back to the classifier h at line 193), then the server averages all client models via FedAvg. This means watermark information from different clients is mixed during aggregation. The paper does not analyze how this averaging affects watermark persistence across rounds, or whether watermarks from different clients interfere destructively during aggregation. — *Verifiable: lines 265–266 show the aggregation step `θ_g ← 1/|A| Σ_{k∈A} θ_k`; there is no analysis of how per-client watermarks survive this averaging.*

### Minor

- **Model extraction attack degrades WSR substantially for CIFAR-10 with limited analysis.** WSR drops from 100% to 66.38% after knockoff extraction on CIFAR-10 (Table `tab:extraction`). The paper states "WSR is still over 65%" and notes TAcc remains 100%, but it does not report WSR_Gap for this attack (the extraction table omits WSR_Gap), making it impossible to assess whether the gap between the top and second-best client narrows dangerously. The paper also does not discuss what the practical WSR threshold needs to be for reliable verification. — *Verifiable: extraction table (lines 355–367) lacks WSR_Gap column; line 390 only mentions "over 65%".*

- **Fine-tuning attack evaluation uses a weak setting without justification.** The paper uses 50 epochs with a learning rate of 10⁻⁵ (line 329). A malicious client with more compute or a higher learning rate could potentially cause greater watermark degradation. The paper does not justify why this specific configuration is representative of realistic attacks. — *Verifiable: line 329.*

- **Scalability at 600 clients shows narrowing WSR_Gap without discussion.** WSR_Gap drops from 98.95% (40 clients) to 63.83% (600 clients) (Table `tab:diff_client`). This means the second-highest-responding benign client is within ~10 percentage points of the tracked malicious client, increasing collision risk. The paper states "WSR is still over 73% and TAcc remains 100%" (line 491) without addressing the narrowing gap concern. — *Verifiable: Table `tab:diff_client` lines 499–501.*

- **No statistical variance reported.** Results are point estimates without standard deviations or confidence intervals. Given FL's inherent randomness (client selection, non-IID splits), some measure of variance would strengthen reliability. — *Verifiable: no error bars or confidence intervals in any table.*

- **CIFAR-10 baseline accuracy is 40.23% before injection (line 286), rising to only 55.83% after.** While this likely reflects the highly non-IID setup (3 random classes per client), the paper does not contextualize whether this is expected for the chosen configuration, making it harder to assess the utility claim. — *Verifiable: line 286.*

### Trivial

- **Orthogonal initialization of the decoder weights** (line 186) may be infeasible when the decoder output dimension d (≥ K) exceeds the feature extractor's output dimension. For example, with ResNet18 feature dim=512 and K=600, full row-wise orthogonality of 600 rows in 512-dimensional space is impossible. This is a minor technical detail that can be addressed (e.g., approximate orthogonality).

## Nice-to-Haves

- Compare against FedTracker's parameter-based fingerprints on shared metrics (accuracy degradation, robustness) to quantify DUW's claimed advantage of being parameter-access-free.
- Extend the OoD dataset ablation to more datasets (beyond Digits) to test generality of the trade-off patterns.
- Add a sensitivity analysis of the fine-tuning attack across learning rates and epoch counts to bracket worst-case watermark degradation.

## Removed Points

The following points from the harsh critic were removed per the filtering rules:

1. **"The pitfall experiment references \cref{sec:baseline} which does not appear in main text"** — This is a reference to the appendix. The parser strips appendix content from all papers; the appendix exists in the original submission. Removed per rule: "REMOVE weaknesses about missing appendix."

2. **"The decoder orthogonal initialization feasibility concern as a reproducibility issue"** — This is a minor technical detail. Retained as Trivial rather than the critic's implied severity (reproducibility concern).

3. **"Paper would benefit from reporting non-watermarked FL accuracy as a reference point"** — The paper already reports baseline accuracy before injection (line 286). Removed as factually inaccurate criticism.

4. **Strength Finder's generic/superficial strengths** — The Strength Finder claimed strengths about the importance of the problem and the data-free nature generally. These were already well-covered by the concrete strength points listed above, so the generic framings are dropped to avoid redundancy.

## Novel Insights

None beyond the paper's own contributions. The reviews surface known issues (missing baselines, incomplete threat model) rather than novel observations about the method itself.

## Suggestions

1. **Add direct experimental comparisons** against WAFFLE and FedTracker on the same benchmarks, using the same metrics (WSR, TAcc, Acc, robustness curves). For WAFFLE (which cannot track individuals), compare on watermark success rate, utility degradation, and robustness. For FedTracker, compare on tracking accuracy and the impact of parameter-access vs. black-box verification. This single addition would transform the paper's evidential quality.

2. **Address the collusion threat model** explicitly: either conduct experiments where two or more clients average/interpolate their watermarked models and measure TAcc and WSR degradation, or clearly scope this out as a limitation with an argument for why it is unlikely in the target setting.

3. **Specify σ and report WSR_Gap consistently** across all robustness tables (including model extraction). Provide a procedure for setting σ empirically and discuss how the 66.38% WSR after extraction on CIFAR-10 relates to the chosen threshold.

4. **Analyze the FedAvg aggregation effect** on per-client watermark persistence across rounds. This would substantially strengthen the methodological analysis.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>