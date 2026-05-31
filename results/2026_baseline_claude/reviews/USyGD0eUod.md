Now I have read the full paper. Let me write my review.

---

## Summary

This paper presents an empirical study evaluating whether common sparse autoencoder (SAE) quality metrics and auto-interpretability pipelines can distinguish trained transformers from randomly initialized ones. Over a broad sweep of Pythia model sizes (70M–6.9B parameters) and multiple randomization schemes (re-randomized weights with/without embeddings, step-0 checkpoints, and a Gaussian input control), the authors find that SAEs trained on randomly initialized transformers frequently produce auto-interpretability scores (AUROC via "fuzzing" and "detection") and standard reconstruction metrics that are remarkably similar to those from fully trained models. They propose token distribution entropy as a preliminary measure of feature "abstractness" that better distinguishes the two regimes, and provide toy model analyses suggesting that random neural networks preserve or amplify superposition in their inputs.

---

## Strengths

- **Addresses a critical blind spot in the field.** The paper applies a principled sanity check (Adebayo et al., 2020-style model randomization) to SAE evaluation — a step that the mechanistic interpretability community has largely skipped. The core empirical finding — that aggregate auto-interpretability scores do not distinguish trained from randomly initialized models — is demonstrated convincingly across multiple Pythia model sizes and three distinct randomization schemes, providing high reliability.

- **Particularly alarming pattern in Figure 1.** For Pythia-6.9b, the randomized variants (AUROCs ~0.87–0.88) actually exceed the trained model (AUROC ~0.79). This is not merely a failure to detect a gap; the metrics actively prefer the randomly initialized model, which makes the community's reliance on these metrics especially problematic.

- **Token distribution entropy as a discriminating measure.** The observation that trained model features show monotonically increasing entropy with layer depth (reflecting growing abstraction), while randomized model features remain concentrated on single token IDs, is genuinely novel and actionable. This gives practitioners a concrete, cheap-to-compute diagnostic to add to their evaluation suite.

- **Comprehensive experimental scope.** The results span five model scales, four randomization variants, two auto-interpretability task formats ("fuzzing" and "detection"), and multiple SAE hyperparameters (expansion factors R=16–128, sparsities k=16 and 32). Robustness is also checked at 1B tokens (Appendix C) and over multiple random seeds (Appendix E), lending confidence to the findings.

- **Honest engagement with related work.** The paper correctly situates its findings relative to Bricken et al. (2023) (who found discrimination worked for a one-layer model), Karvonen et al. (2024c) (board game data vs. language data), and Lecomte et al. (2024) (polysemanticity vs. superposition), clearly delineating what is new.

---

## Weaknesses

### Fatal
None.

### Major

- **The central finding is size-dependent in a way that weakens the broad framing.** The abstract and introduction suggest SAE metrics generally fail to distinguish trained from random, but the paper itself acknowledges (Section 2, last paragraph of "Random one-layer transformers") that randomized models score relatively low for Pythia-70m and the gap narrows only for larger models. Figure 2 (AUROC rows) visually confirms this — the trained and randomized curves diverge at 70M but converge at 6.9B. The paper does not analyze where exactly this crossover occurs, leaving practitioners without guidance on when to be concerned. A supplemental analysis characterizing the threshold (model size, architecture, data size) at which metrics become unreliable would significantly strengthen the practical implications.

- **Token distribution entropy is not sufficiently validated as a measure of "abstractness."** The paper introduces entropy as a proof-of-concept but does not establish that low entropy in randomized models reflects a distinct mechanistic cause rather than an artifact of architecture (e.g., random weights producing sharper, more token-specific projections by chance). There is no causal or functional validation: do high-entropy features actually correspond to SAE latents that matter for model behavior (via circuit-style interventions), while low-entropy features do not? Without this, entropy remains a suggestive correlation rather than a validated metric.

- **The toy model analysis (Section 4) is qualitative and not connected to the main empirical findings.** The demonstration that MLPs preserve or amplify superposition is plausible but does not explain *quantitatively* how much of the auto-interpretability score similarity is attributable to data structure vs. architectural amplification. The paper concedes the question is left to future work, which is fair, but Section 4 occupies considerable space while contributing only weak mechanistic grounding for the central claim.

### Minor

- **Lack of intervention-based evaluation.** The paper correctly identifies that CE loss score is only meaningful for trained models, but it does not explore whether any other causal-style evaluation (steering, activation patching, probing for specific concepts) would distinguish the two regimes. Even a small-scale experiment of this kind would sharpen the recommendation to use "targeted measures."

- **The Gaussian input control is described as expected to perform at chance, and it does.** This makes it an easy win; the hard question is whether *any* baseline exists that unambiguously differentiates the trained and randomized regimes by a large margin on the metrics SAE practitioners currently use. The paper identifies the problem but does not propose a strong positive control.

### Trivial
- Figure descriptions contain redundant text from OCR parser (multi-caption duplicates), which is a parser artifact and not a paper flaw.

---

## Nice-to-Haves

- A characterization of the model size/training compute threshold at which the auto-interpretability gap collapses would substantially increase the practical utility of the paper.
- Providing even preliminary intervention-based evidence (e.g., checking whether latents that can steer model behavior have systematically higher token distribution entropy) would validate entropy as more than a proxy.

---

## Novel Insights

The paper's most genuinely novel insight is the *direction* of the failure: for large Pythia models, SAEs trained on randomly initialized weights achieve *higher* auto-interpretability AUROCs than those trained on the actual trained model. This is not a null result — it is a reversal that implies the metrics may be measuring something other than computational significance, perhaps the degree to which data or architecture constrains SAE features to be token-specific (low entropy, high auto-interpretability score). The token distribution entropy profile — increasing monotonically with layer depth for trained models but flat for randomized models — further suggests that the standard auto-interpretability pipeline conflates "activates consistently on identifiable tokens" with "captures learned computation," a confusion that becomes more dangerous as models scale up.

---

## Suggestions

- Perform a systematic sweep over model size to identify the scale at which the metric gap collapses; report this as a "failure threshold" curve so practitioners know when to be alarmed.
- Validate token distribution entropy against a behavioral criterion (e.g., does entropy predict whether a latent can be used for model steering?), even on a small sample of latents in a single model.
- Clarify whether the similar reconstruction metrics (cosine similarity, explained variance) also fail to discriminate, or whether only the auto-interpretability AUROC is the primary failure mode — this has different implications for practitioners who rely on reconstruction quality rather than auto-interpretability.

---

## Score and Decision

The paper raises a well-supported, genuinely important methodological concern for the mechanistic interpretability community: that common SAE evaluation metrics — including the widely-used auto-interpretability AUROC — fail to discriminate trained transformers from randomly initialized ones at scale. The experimental coverage is broad and results are robust. The core finding is alarming in the right direction for the field and has immediate practical implications. The weaknesses (size-dependent effect not fully characterized, entropy not causally validated, toy models loosely connected) are real but do not invalidate the central message. This is the kind of careful null-model analysis that the field needs more of.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>