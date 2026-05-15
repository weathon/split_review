Now I have a thorough understanding of the paper. Let me compose the final consolidated review.

## Summary

This paper introduces Denoising Task Routing (DTR), a parameter-free add-on for diffusion models that applies task-specific binary masks to channels within residual blocks. The mask uses a sliding window that shifts according to a power-law schedule in timestep \(t\), encoding two priors: (1) task affinity — adjacent timesteps share more channels, (2) task weights — higher timesteps (early denoising) get more dedicated channels. Experiments on FFHQ, ImageNet, and MS-COCO with both UNet (ADM) and Transformer (DiT) backbones show consistent FID/IS/Precision/Recall improvements without extra parameters, accelerated convergence, and compatibility with MTL loss-weighting methods.

## Strengths

- **Consistent gains across architectures, datasets, and model scales**: DTR improves generative metrics on FFHQ (unconditional), ImageNet (class-conditional), and MS-COCO (text-to-image) when applied to both ADM and DiT backbones, with larger models benefiting more. The ablation studies (hyperparameters \(\alpha, \beta\)) are systematic and yield interpretable design guidelines (\(\beta=0.8, \alpha=4\)).

- **Accelerated convergence with clear quantification**: Training DiT-B/2 reaches FID 31 in 200K iterations with DTR vs. 400K without — a concrete, non-trivial speedup. The convergence analysis also shows that DTR mitigates saturation that appears when using MTL loss-weighting alone (e.g., ANT-UW at 300K iterations).

- **Complementarity with MTL loss-weighting is explicitly demonstrated**: Tables \ref{tab:loss_orthogonality} and Figure \ref{fig:loss_ortho_graph} show that combining DTR with ANT-UW, Min-SNR, or P2 consistently outperforms each technique alone on class-conditional ImageNet, validating the orthogonal nature of architectural masking and optimization-based MTL approaches.

- **Method is simple, architecture-agnostic, and has zero added parameters**: DTR requires only a few lines of code and a negligible channel-multiplication cost, making it practical for adoption across existing diffusion model pipelines.

## Weaknesses

### Fatal
None.

### Major
- **Multi-experts comparison is mentioned but never quantified in the main text**: Section \ref{sec:exp:analysis} (lines 316–318) states "Here, we show that DTR outperforms the multi-experts denoiser method" but provides **no numerical results** — no FID, parameter count comparison, or any quantitative evidence. This is a claimed comparison that the reader cannot evaluate from the main paper. The appendix table (if it exists) is not a substitute; a claim of outperformance requires at least one concrete number in the main text to substantiate it.

- **The headline claim (DiT-L matching DiT-XL with 2M vs. 7M iterations) is undersupported in the main paper**: The abstract and Section \ref{sec:exp:comparative_eval} (line 262) report that DiT-L/2 + DTR + ANT-UW achieves FID 2.33 after 2M iterations, matching DiT-XL/2 after 7M iterations. However, the main text provides no details on whether the DiT-XL baseline was reproduced under identical conditions (same optimizer, batch size, augmentations, evaluation protocol) or simply cited from the original DiT paper. Given that this is the paper's most striking result, the main text should at minimum state whether the baseline was reproduced and what the exact configuration was. (Note: the referenced appendix table \ref{app:tab:long_iter} likely exists in the original submission, but the main text lacks sufficient context to assess the fairness of the comparison.)

- **No measurement of negative transfer**: The paper motivates DTR by the need to mitigate negative transfer between denoising tasks, but never directly measures it. Prior MTL-for-diffusion work (Go et al. 2023, Hang et al. 2023) quantifies gradient conflicts or loss interference; the CKA analysis here is post-hoc and does not establish a causal link. The performance improvement could stem from implicit regularization, effective capacity modulation, or other mechanisms. An explicit measurement (e.g., gradient alignment with/without DTR) would substantially strengthen the core claim.

### Minor
- **No error bars or variance reporting**: All quantitative results (Tables \ref{tab:fid}, \ref{tab:mask_init_abl}, \ref{tab:scalability_abl}, convergence curves in Figure \ref{fig:training_speed}) are presented as single numbers without standard deviations or multiple-seed runs. Some improvements are modest (e.g., FFHQ unconditional reported as 10.81 → 10.07 FID in the critic's summary; the paper's own tables are in \input files but the text describes "significant performance enhancements"), making it impossible to assess whether gains are within the noise floor. While single-run evaluation is common in large-scale diffusion model papers (DiT, ADM all report single runs), the lack of any variance indication weakens the claim of *consistent* improvement.

- **No qualitative comparison figure**: The paper states "our method for training diffusion models produces images that exhibit improved realism and fidelity" (line 259) but provides no sample images. A side-by-side comparison of generated samples (baseline vs. DTR) is a standard expectation and would make the improvements tangible beyond the numerical metrics.

- **Overclaim in novelty framing**: Line 329 states "our study is the first to advance diffusion model architecture from an MTL perspective." Prior work (adaLN, FiLM conditioning, adaptive group normalization) already incorporates MTL-like architectural conditioning, even if not framed in MTL terminology. The paper's contribution — a fixed, prior-informed mask — is novel and useful, but the "first" claim is overstated given the existing implicit conditioning literature.

### Trivial
None.

## Nice-to-Haves

- **Comparison to a learned mask baseline**: Adding a simple differentiable mask (e.g., Gumbel-softmax with the same channel budget \(\beta\)) on one setting (e.g., ImageNet 256×256, DiT-B/2) would help isolate whether DTR's success stems from the specific hand-crafted structure or merely from having *any* sensible masking. This would strengthen the claim that the task affinity / task weight priors are the key factor.

- **Ablation over different masks per block**: The same mask is applied to all residual blocks for a given timestep. An ablation studying whether different blocks benefit from different mask assignments could provide architectural insight.

## Removed Points

- **"No comparison to adaptive or learned routing baselines" treated as a core weakness**: Moved to Nice-to-Haves. The paper's contribution is a *fixed, parameter-free* mask informed by domain priors; comparing against learned masks would be informative but is outside the paper's stated scope and does not invalidate the core contribution.

- **Criticism that the DiT-XL matching result "cannot be verified" because it's in the appendix**: The appendix table exists in the original submission (the parser strips appendices). The substantive concern (lack of detail on whether the baseline was reproduced) is kept as a Major weakness; the complaint about appendix referencing is removed per instructions.

- **"Table 2 unconditional results contradict complementarity claim"**: The paper explicitly addresses this (lines 253–255), explaining that in unconditional generation DTR subsumes the role of loss weighting. The reviewer's concern is already answered in the paper.

- **Formatting/style nitpicks, requests for hyperparameter listings**: Removed as these are either parser artifacts or standard reproducibility concerns that do not undermine the contribution.

## Novel Insights

The key insight that emerges across the reviewers' input is that DTR's strength is also its limitation: the fixed, hand-crafted sliding-window mask is simple and effective, but the paper would be significantly stronger if it provided direct evidence for the causal mechanism (negative transfer reduction) and at least one quantitative data point for the multi-experts comparison. The method itself is clean and the experiments are broad, but the evidence for the highest-impact claims (DiT-L matching DiT-XL, outperforming multi-experts) is either deferred to the appendix or missing entirely from the main text. The paper would benefit from trading some breadth (e.g., fewer hyperparameter ablations) for depth in the most impactful comparisons.

## Suggestions

1. **Add error bars** for at least the main FID results (Table \ref{tab:fid}) and the convergence plot (Figure \ref{fig:training_speed}) using 3 seeds.
2. **Report the multi-experts comparison numbers** (FID, parameter count, training cost) in the main text rather than just stating outperformance.
3. **Expand the DiT-XL matching description** to clarify whether the baseline was reproduced and under what conditions, even if full details remain in the appendix.
4. **Replace or augment the qualitative statement with an actual figure** showing generated samples from baseline vs. DTR.
5. **Add a direct negative-transfer measurement** (gradient alignment across timesteps) or soften the causal claim about negative transfer mitigation.

## Score and Decision

The paper presents a clean, practical idea with consistent experimental support across multiple architectures and datasets. The main weaknesses — lack of variance reporting, missing quantitative results for the multi-experts comparison, and undersupport for the headline XL-matching claim — are addressable in revision and do not invalidate the core contribution. The method is simple, parameter-free, and shows genuine improvements in both quality and convergence speed.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>