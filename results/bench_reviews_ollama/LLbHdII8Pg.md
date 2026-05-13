## Summary
DeTrans is a post-hoc DNN IP-protection framework that modifies a tiny fraction of weights (0.07–0.18% of parameters, ~79–122 KB to fit a TEE) in high-transferability filters via a bi-level optimization over source and WAE-generated auxiliary domains. The goal is dual protection: degrade source-domain accuracy to random guessing for unauthorized inference, and reduce transferability (up to 81.23% drop) to unseen target domains, while authorized users recover the original behavior using weights stored in the TEE.

## Strengths
- Identifies a meaningful gap in prior work: NNSplitter degrades only source-domain accuracy and NTL/CUTI restrict only transferability and are training-from-scratch methods — DeTrans targets both objectives as a post-hoc modification of a pre-trained model (Sec. 2.4, Tabs. 1–2).
- Practical hardware-aware constraint: modifying one filter per conv layer keeps protected weights to 79 KB / 122 KB, fitting the 3–5 MB TEE secure memory budget (Sec. 4.1).
- Bi-level formulation is shown to be essential: the naive "defense-attack-defense" alternation yields only a 1.3% accuracy drop, whereas the bi-level version exceeds 80% (Tab. 3), supporting the optimization design choice.
- Reasonable robustness probe to attacker fine-tuning range: with p2 (one filter per layer), both last-layer and whole-model fine-tuning by the attacker on MN→US end up at ~20% accuracy versus a ~97% unprotected baseline (Tab. 4).

## Weaknesses

### Fatal
None.

### Major
- **Attacker strength is fixed at a single, weak point and the headline number is not stress-tested.** Throughout the paper the attacker has only 5% target-domain data and uses vanilla fine-tuning (Sec. 4.1, 5.1). Since only 0.07–0.18% of parameters are perturbed, an attacker with more data, longer fine-tuning, different LR schedules, or partial re-initialization of suspicious filters could plausibly wash out the perturbation. The paper sweeps neither attacker data budget nor fine-tuning recipe beyond "last-layer vs. whole-model" (still at 5%). The "up to 81.23%" claim is thus pinned to a single operating point of a threat model the paper itself describes as "strong."
- **No adaptive attacker.** The filter-selection criterion (Eq. 2–3) is computable from any extracted model, so an attacker aware of DeTrans could probe and reinitialize the highest-transferability filter per layer. This is the natural strongest attack and is not evaluated.
- **The auxiliary domains are never shown to approximate the real target domains used to report transferability.** The bi-level objective optimizes against WAE-generated auxiliary domains with a $(\mu,\sigma)$ schedule (Sec. 3.1), but transferability is reported on MN→SV, MN→US, CF10→STL10 (Tab. 2). The paper provides no measurement (MMD, Wasserstein, etc.) that the auxiliary distributions cover or even approach these real targets, so the link between what is optimized and what is reported is asserted rather than established. The paper even notes MN→SV is "complex" and far from MN — which sits in tension with the "target ≈ source" assumption.
- **Authorized-user accuracy is asserted but not tabled.** Tabs. 1–2 do not report top-1 accuracy when the TEE-restored weights are used. Since "preservation of authorized performance" is half of the "two birds" thesis, the absence of a direct measurement (even just to confirm exact restoration) is a real evidential gap.

### Minor
- **Filter selection contributes only +14.95% on top of random selection (Sec. 4.4 / Fig. 3).** The transferability-ranking pillar is therefore much weaker than the bi-level optimization pillar; the paper does not acknowledge or analyze this asymmetry, nor study the stability of which filter is selected across seeds/data subsamples.
- **No variance / multi-seed reporting.** Tabs. 1–3 give point estimates; the paper notes "10% with no variance" for balanced classes, but bi-level optimization with a warm-up initialization is sensitive to seed, and seed variance should be quantified — particularly for the MN-class numbers near 10% and the CF10→STL10 cells.
- **Naive-baseline comparison conflates threat models.** The naive defender in Eq. 7–8 has access to 5% of the target-domain data, while the bi-level DeTrans does not. The 1.3% vs >80% delta therefore reflects a more knowledgeable defender losing — informative, but the comparison is not strictly apples-to-apples and the paper does not flag this.
- **"Applicability beyond smaller models" rests on a single configuration.** ResNet-50 / CIFAR-10 (Tab. 5) is a single cell; one configuration is not a scalability claim.
- **WAE / auxiliary-domain hyperparameters under-justified.** $\mu \in [0,1]$ step 0.25, $\sigma \in \{0.5, 1\}$ is asserted without sensitivity analysis across source domains.

### Trivial
- Eq. 2 as written has $\sigma^2 \propto \sum (x_j - \mu)$ rather than $(x_j-\mu)^2$; likely a transcription issue but worth fixing in the definition of the central transferability metric.

## Nice-to-Haves
- Per-layer visualization showing *which* filter is selected and how stable that selection is across runs/subsamples — this would directly support the "shared-features filter" rationale.
- An attacker-data sweep (5% → 100%) reporting transferability as a curve.
- Larger / more realistic pretraining→fine-grained transfer pairs (e.g., ImageNet-pretrained), where the IP value is higher and on-device-only argument is weaker.

## Removed Points
These points are flagged for removal; treat them with caution.

- *"NTL/CUTI are not a fair comparison"* (harsh critic point 5): The asymmetry favors the baselines (they're designed for one objective each and DeTrans is the only method attempting both). Per the rules, asymmetric comparisons that disadvantage the authors' own method should not be held against the paper.
- *Generic Strength Finder claims* (e.g., "reduces source-domain accuracy to random guessing" stated as a standalone strength without context, and "robustness to attackers' fine-tuning strategies" framed broadly): partially retained but the "robustness" claim conflicts with the Major weakness about a non-adaptive, fixed-budget attacker — the weakness wins, so the strength is narrowed to the specific Tab. 4 result rather than a general robustness claim.
- *Sec. 3.1 hyperparameter under-specification of the conditional WAE architecture / training-ratio details*: This is an appendix-style reproducibility nit and per rules is downweighted; kept the substantive sensitivity-analysis concern only.

## Novel Insights
None beyond the paper's own contributions. The reviews surface a useful structural observation already implicit in the paper — that the bi-level optimization rather than the transferability-ranked filter selection is doing most of the work (a ~15% gain over random selection vs. ~80% gain over no-protection) — but this is an interpretive reframing rather than new science.

## Suggestions
- Add an attacker-data sweep (5%, 10%, 25%, 50%, 100%) and at least one adaptive attacker that uses Eq. 2–3 to identify and reinitialize the protected filter.
- Quantify auxiliary-vs-target distributional overlap (MMD or Wasserstein in feature space) for each evaluation pair; this is the linchpin assumption.
- Add an "Authorized" column to Tabs. 1–2 showing top-1 accuracy after TEE restoration to close the dual-protection loop.
- Report mean ± std over ≥3 seeds for at least Tab. 2 and the ResNet-50 ablation; clarify whether the "10% with no variance" claim refers to within-run determinism or across-seed stability.
- Fix the variance definition in Eq. 2 and ablate $\mu, \sigma$ ranges.

## Evaluation
- **Originality:** Reasonable. Combining the two IP-threat models (unauthorized inference + cross-domain transfer) in a single post-hoc, TEE-compatible framework is a fresh angle.
- **Importance:** Moderate. On-device IP protection is a real concern, though the threat model is narrow.
- **Claims well supported:** Partially. The unauthorized-inference half is solid; the transferability half rests on an under-stressed attacker and an unvalidated auxiliary-domain proxy.
- **Soundness of experiments:** Mixed. Reasonable datasets and baselines, but no attacker sweep, no adaptive attack, no seed variance, no authorized-user accuracy table.
- **Clarity:** Generally clear, with a clean framework figure and well-organized ablations.
- **Value to community:** Useful as a first attempt at dual protection; needs stronger empirical scaffolding to be definitive.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>