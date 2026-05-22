Now I have a clear picture. Let me finalize my calibration:

**Round 1 bracket:** 6.0–8.0

**Round 2 narrowed bracket:** CaPT sits around 7.0–7.5. It is clearly stronger than SemiCLIP (5.80) and the 6.0 SSL papers. It is comparable to CLIP Data Selection (7.50) and PLENCH (7.50), and slightly below the stronger 8.0 papers (HyCoCLIP, CLIP DFKD) which have slightly cleaner contributions or scale advantages.

Now let me write the final consolidated review.

---

## Summary
This paper identifies and theoretically formalizes a fundamental limitation in semi-supervised learning: the utility of unlabeled data is coupled to the quantity and quality of labeled samples, causing SSL performance to collapse under extreme label scarcity. The authors propose CaPT, an asymmetric-modalities co-training framework that integrates CLIP as a "prior teacher." A fully fine-tuned unimodal network and an adapter-tuned CLIP branch exchange entropy-weighted co-pseudo-labels, enabling the unimodal network to leverage CLIP's zero-shot knowledge while CLIP is refined by unlabeled data. CaPT achieves state-of-the-art performance across the USB benchmark, ImageNet, extreme-scarce-label regimes, and fine-grained datasets, with dramatic gains (e.g., +21.38% on CIFAR-100 with one label per class).

## Strengths

- **Compelling problem identification with both theoretical and empirical grounding.** Theorem 1.1 derives a pseudo-label error bound under a Gaussian mixture model showing that label quality/quantity directly tightens the margin and inflates error, while Figure 1 empirically demonstrates performance collapse under extreme label scarcity and low prototypicality. This dual motivation is clear and convincing.

- **Dramatic and consistent empirical gains.** On the USB benchmark (Table 1), CaPT outperforms all 12 baselines across all 6 settings, with particularly large margins in low-label regimes (+4.09% on CIFAR-100 at 2 labels/class, +6.18% on STL-10 at 4 labels/class). Under extreme scarcity (Table 3, 1 label/class), CaPT improves over the next-best method by +21.38% on CIFAR-100 and +4.05% on EuroSAT. ImageNet results (Table 2) show +9.33% at 10 labels/class. These gains directly validate the core claim that a VLM prior breaks SSL's label dependency.

- **Systematic and thorough ablation study.** Table 6 cleanly isolates the contribution of each design choice: adapter tuning (CaPT-Deb, -12.73% on EuroSAT), bidirectional flow (CaPT-Uni, -1.49%), feature-augmented consistency (-1.81%), entropy-based weighting (-1.57%), and the necessity of both UPM and MPM branches. The ablation confirms that the full framework is necessary for the reported performance.

- **Practical efficiency.** Table 4 demonstrates that CaPT adds only 8% memory and 11% training time over a standard FreeMatch baseline while substantially outperforming it, and is both cheaper and more accurate than RegMixMatch. This makes the method genuinely usable.

- **Honest treatment of limitations and scope.** Section 5 explicitly acknowledges that CLIP's prior is weak on certain fine-grained datasets (FGVCAircraft) and that CaPT's portability allows swapping in stronger future VLMs. The fine-grained experiments (Table 5) and discussion of CLIP training data overlap (Appendix M, acknowledged in text) show the authors are not overselling.

- **Well-designed asymmetric co-training.** Figure 3 provides qualitative evidence that CLIP's cross-modal attention diverges from pure-vision ViTs, supporting the claim that asymmetric modalities mitigate the pattern-homogeneity bottleneck of conventional co-training. The entropy-weighted co-pseudo-label mechanism (Eq. 11–13) is a principled way to adaptively balance supervision from the two branches.

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

- **Supervised loss term not explicitly stated in the method section.** The paper thoroughly describes the unsupervised consistency losses (Eq. 15) and the co-pseudo-label mechanism, but the standard supervised cross-entropy loss on labeled data—a basic component of any SSL method—is never written down. Section 3.1 says the process "follows common practices in current SSL methods," which implies but does not specify this term. For reproducibility, the supervised loss composition (including whether CLIP's branch receives direct label supervision or only co-pseudo-labels) should be stated explicitly. This is easily addressable in a camera-ready revision.

- **Theorem 1.1 is a loose motivation, not a design guide.** The theorem uses a nearest-prototype classifier under a Gaussian mixture model to illustrate how label quality affects pseudo-label error. This motivates the problem well, but the connection to the actual CaPT architecture (deep neural networks, entropy-weighted co-training, CLIP integration) is tenuous. A brief remark acknowledging that the theorem is an analytically tractable proxy would help manage reader expectations. This does not undermine the core contribution.

### Trivial

- Figure 5 demonstrates that adapter-tuning reduces CLIP's class bias, which directly supports the design choice. It would be even more informative to see corresponding pseudo-label accuracy curves of CaPT vs. CaPT-Deb during training, connecting bias correction to actual SSL dynamics. This would strengthen but is not required for the current claims.

## Nice-to-Haves

- A small-scale study replacing CLIP with a different VLM (e.g., SigLIP or a stronger CLIP variant) on one dataset would directly demonstrate that the framework is VLM-agnostic, as the paper argues. This would strengthen the "future-proof" claim.

- Directly showing that CaPT's pseudo-label accuracy stays high as labeled-data quality degrades (extending Figure 1b to CaPT) would provide a more direct empirical test of the core "breaking label dependency" claim, rather than relying solely on final test accuracy.

- An ablation where CLIP receives only co-pseudo-labels (no direct label supervision) would clarify whether the CLIP prior alone can bootstrap the unimodal model, strengthening the "decoupling" claim.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"Comparison to SSL baselines that do not use CLIP may not be entirely fair in terms of resource usage due to CLIP's web-scale pre-training."** The harsh critic raised this and then correctly dismissed it. The paper explicitly discusses CLIP pre-training data overlap (Appendix M) and evaluates on fine-grained datasets where overlap is unlikely. CLIP's pre-training is the entire point of the approach—it replaces label dependency with a VLM prior. This is a feature, not a hidden advantage.

- **"The theoretical bound is a toy model."** The harsh critic noted this as a minor gap, which is retained above. The "fatal" framing was never present; the harsh critic correctly categorized it as acceptable for motivation.

- **"Runtime comparisons could include FLOP counts."** This is a nitpick. Table 4 already provides wall-clock time and memory, which are more practically meaningful than FLOPs for this setting.

- **Strength Finder's generic framing about "important problem."** While the problem is indeed important, this is filtered as a generic strength without concrete evidence beyond what is already captured in the specific strengths above.

## Novel Insights

Beyond the paper's own contributions, the key insight that emerges from synthesizing the reviews is: CaPT succeeds not merely because it adds CLIP to SSL, but because the asymmetric architecture creates a division of labor—CLIP provides a label-independent prior (reliable but capacity-constrained via adapter-tuning), while the unimodal network provides learning capacity (flexible but label-dependent). The entropy-weighted bidirectional exchange lets the system transition smoothly from CLIP-dominated early training to unimodal-dominated later training as the unimodal network catches up. This temporal division of labor, combined with the cross-modal complementarity that breaks co-training's pattern-homogeneity bottleneck, is what makes the framework more than the sum of its parts.

## Suggestions

- In the camera-ready version, add one sentence explicitly stating the supervised cross-entropy loss on labeled data for both the UPM and MPM branches, and clarify whether the CLIP branch receives direct label supervision or only co-pseudo-labels.

- Add a brief remark after Theorem 1.1 acknowledging that the nearest-prototype classifier under a Gaussian mixture is an analytically tractable proxy for the more complex neural-network pseudo-labeling used in practice, to manage reader expectations about the theory-method connection.

- Consider adding a single ablation with a different VLM backbone on one dataset to strengthen the portability claim.

## Score and Decision

**Anchor comparison:**

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| FwkYeLovHk (Weak-to-Strong CLIP) | 3.33 | 1 | CaPT is clearly far stronger |
| HfJxXbXlYJ (LLM2CLIP) | 3.00 | 1 | CaPT is clearly far stronger |
| E0UsEIRBQ8 (SSL underwater detection) | 3.00 | 1 | Different domain, CaPT stronger |
| hgayrNSbri (Image captioning) | 3.40 | 1 | Different task, CaPT stronger |
| 97D725GJtQ (SemiCLIP) | 5.80 | 1 | CaPT clearly stronger: more dramatic gains, better ablations, broader evaluation |
| 1rgMkDWfYV (Label noise + CLIP) | 4.50 | 1 | Different focus, CaPT stronger |
| RgWATMmWmz (WSL with CLIP) | 4.75 | 1 | Different paradigm, CaPT stronger |
| PD8JVDg8mB (Annotation bootstrapping) | 4.25 | 1 | Different focus, CaPT stronger |
| 3i13Gev2hV (HyCoCLIP) | 8.00 | 1 | HyCoCLIP slightly cleaner, but CaPT's empirical gains are more dramatic |
| RvUVMjfp8i (SSL open environments) | 8.00 | 2 | Evaluation paper; CaPT is a method paper with strong gains |
| FtX6oAW7Dd (PLENCH) | 7.50 | 2 | CaPT comparable: both thorough, PLENCH is evaluation-focused |
| HvkXPQhQvv (SSME) | 6.00 | 2 | CaPT clearly stronger |
| dnqPvUjyRI (SemiReward) | 6.00 | 2 | CaPT clearly stronger |
| WPsnH6875d (Unseen-class SSL) | 6.00 | 2 | CaPT clearly stronger |
| 1aF2D2CPHi (CLIP DFKD) | 8.00 | 2 | DFKD strong but CaPT's gains are more dramatic and motivation more compelling |
| 9bMZ29SPVx (CLIP data selection) | 7.50 | 2 | CaPT comparable; both are CLIP-powered frameworks with thorough evaluation |
| b20VK2GnSs (MLLM concept drift) | 7.00 | 2 | CaPT slightly stronger: clearer contribution, more dramatic gains |

**Final placement:** CaPT sits solidly in the 7.0–7.5 range. It is clearly above the 5.80–6.00 SSL papers and comparable to the 7.50 CLIP-powered framework papers. The weaknesses are genuinely minor (missing explicit supervised loss, loose theory-method connection) and do not threaten the core contribution. The paper's strengths—dramatic empirical gains under extreme label scarcity, systematic ablation, practical efficiency, honest limitations discussion—are substantial. I score it at **7.5**.

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>