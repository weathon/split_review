Now I have a thorough understanding of the paper. Let me synthesize the final review, carefully verifying every claim against the paper text.

---

## Summary

This paper addresses the Lookback Window Limitation (LWL) in long-term time series forecasting—the phenomenon where increasing the historical window past a certain point degrades performance. The authors propose two model-agnostic modules: an Information Bottleneck Filter (IBF) that learns to select informative temporal patches while discarding redundant ones, and a Hybrid-Transformer-Mamba (HTM) architecture that uses Mamba for long-range modeling and Transformers for shorter partitioned subsequences. Integrated with patching (PIH), the method extends lookback windows to L=1024—longer than typical prior work—and shows monotonic performance improvements where PatchTST peaks and declines.

## Strengths

- **Principled decomposition of LWL into two distinct causes.** The paper separately addresses information redundancy (via IBF's information bottleneck) and Transformer architectural limitations (via HTM's hybrid design). This is more principled than heuristic approaches like patching alone, and both modules are model-agnostic, as demonstrated on Transformer, Informer, and Autoformer backbones (Section 4.2, Fig. 4–5).

- **Clear empirical evidence that LWL can be overcome on average.** Fig. 3(a) shows that PIH achieves monotonically improving MSE as the lookback window grows from 96 to 1024, while PatchTST peaks at L=512 and declines at L=1024. This directly supports the paper's central claim and is the strongest evidence in the paper.

- **Computational efficiency gains.** HTM reduces runtime and memory by 2–3× compared to PatchTST (Fig. 3(b)), and the IBF adds negligible overhead, demonstrating that overcoming LWL does not require prohibitive compute.

- **Interpretability byproduct.** The IBF module's learned patch importance weights (Fig. 3(c)) provide a form of explainability—concentrating on peak positions in the Electricity dataset—which is rarely offered in LTSF methods.

## Weaknesses

### Fatal
None.

### Major

1. **The IBF compression loss (Eq. 9) contains undefined symbols A and B.** Line 113 states:  
   `-I(z^{noise},z) ≤ 𝔼_z(-½ log A + 1/(2N)A + 1/(2N)B²) := L_comp(z^{noise},z)`  
   Neither A nor B are defined anywhere in the paper, and no derivation is provided from a variational bound. The reference to Yu et al. (2021a) does not clarify the specific form used here. This is a missing mathematical definition that makes a core component of the method non-reproducible. The authors must supply the definition of A and B and/or the full derivation from a standard KL or Gaussian-prior bound.

### Minor

1. **Complexity analysis contains a minor error.** The paper states the HTM time complexity as O(L/P) + O((L/PK)²) (line 132). The Transformer processes K blocks of length N/K (N = L/P); the correct cost is K·O((N/K)²) = O(N²/K), not O(N²/K²). The qualitative conclusion that complexity is significantly reduced still holds, but the expression is off by a factor of K.

2. **The SOTA claim is overcalimed relative to the baseline set.** The paper claims "state-of-the-art results" but compares against only 7 models (PatchTST, S-Mamba, FEDformer, Autoformer, Informer, DLinear, NLinear). While this set is adequate for demonstrating LWL overcoming, it is limited for an unqualified SOTA claim. Stronger recent Transformer/Mamba-based forecasting models would strengthen the evaluation.

3. **Fig. 3(a) shows only averaged MSE across 7 datasets.** Per-dataset window-size sensitivity curves for the key comparison (PIH vs. PatchTST at L = 96, 336, 512, 1024) are not provided. Since different datasets may have different LWL thresholds, individual trends would strengthen the claim.

4. **No statistical significance is reported.** The observed improvements in the ablation study (Fig. 6) are described as ~0.01–0.02 MSE. Without confidence intervals or significance tests, it is unclear whether these differences are reliable, especially given the use of averaged metrics across datasets.

5. **Table 1's comparison protocol could be clearer.** The paper compares PIH (L=1024) against baselines where some (PatchTST, DLinear, NLinear) use L=1024 and others (S-Mamba, FEDformer, Autoformer, Informer) use their individually best window from {24, 48, 96, 192, 336, 720, 1024}. This design is actually *generous* to baselines, not unfair. However, the paper does not report which window each baseline selected per dataset, and the unusual MSE values noted for some models on Weather (if confirmed) suggest possible tuning sensitivity that warrants discussion.

### Trivial

- The interval split vs. block split comparison in Fig. 6 shows near-identical performance, which the paper acknowledges. This reduces the significance of the split design but does not invalidate HTM.

## Nice-to-Haves

- An ablation of the β hyperparameter in the IBF loss (β for balancing prediction vs. compression) would show whether the information bottleneck is necessary or simple random subsampling works.
- Testing at L=2048 would further substantiate the claim that "even longer windows" are beneficial.
- Extending the interpretability analysis (Fig. 3(c)) to more datasets and showing the full weight distribution (not just top 20 patches) would strengthen the qualitative analysis.

## Removed Points

- **Critical Issue 1 (Table 1 comparison is unfair/misleading):** REMOVED. The reviewer claimed the comparison conflates different window choices and is misleading. In fact, the paper compares PIH at L=1024 against baselines at their *best* selected window from 7 options—this is generous to baselines, not unfair. The paper also explicitly compares PatchTST at L=1024 alongside PIH. The comparison is valid and supports the authors' claims. The reviewer's framing that this is a conflation misreads the experimental design.

- **Critical Issue 3 (Missing baselines such as TimesNet, iTransformer, foundation models):** MOVED TO NICE-TO-HAVE/was MINOR. The baseline set is adequate for the paper's primary claim (overcoming LWL), but the accompanying SOTA claim is somewhat overclaimed. The reviewer's framing as a "critical" omission is disproportionate.

- **Complexity analysis error (the reviewer claimed O(N²/K) vs O((N/K)²)):** KEPT as MINOR but note the paper uses \bar{O} notation which may indicate amortized complexity. The difference is a factor of K which doesn't change the qualitative conclusion.

- **Strawman about "overcoming LWL" being imprecise:** REMOVED. The paper demonstrates improvement up to L=1024 on the datasets tested. The claim is appropriately scoped; the abstract and conclusion both acknowledge limitations (e.g., not all datasets benefit).

- **Formatting nitpicks and missing appendix concerns:** REMOVED per hard rules (parser artifacts).

- **Criticism about not addressing Mamba pathologies on long sequences:** REMOVED as scope creep.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Define A and B in Eq. 9 and provide the derivation** of the variational upper bound for the compression loss. Without this, the IBF module cannot be independently implemented.
2. **Add per-dataset window-size sensitivity curves** (MSE vs. L) for PIH and PatchTST to complement the averaged Fig. 3(a).
3. **Include confidence intervals or error bars** on the main results (Table 1, Fig. 6) to establish statistical reliability of the observed improvements.
4. **Tone down the "state-of-the-art" framing** to match the actual baseline scope, or expand the baseline set to include more recent methods.

## Score and Decision

The paper makes a genuine contribution: it identifies a real problem (LWL), proposes a principled two-part solution, and provides solid evidence (particularly Fig. 3(a)) that the approach demonstrably mitigates the issue. The method is model-agnostic and the efficiency gains are convincing. 

The most serious weakness is the incomplete specification of the IBF loss (undefined A and B), which is a reproducibility barrier. However, this is fixable in revision—it is a missing definition rather than a fundamental flaw. The other weaknesses (limited baselines for SOTA claim, missing per-dataset curves, no significance testing) are addressable. The paper's core claim—that longer windows can be made beneficial through careful redundancy filtering and hybrid architecture—is supported by the evidence presented.

Given that the fundamental contribution is sound but the paper has a clear reproducibility gap in its core technical section, this merits a borderline score. With the missing definitions supplied, the paper would be acceptable.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>