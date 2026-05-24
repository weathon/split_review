Now I have all the information needed for a calibrated review. Let me produce the final consolidated review.

## Summary

This paper expands the scope of machine unlearning by decoupling class labels from target concepts, identifying three novel mismatched scenarios (target mismatch, model mismatch, data mismatch) beyond the conventional all-matched forgetting. The authors provide a theoretical analysis connecting representation distance to forgetting dynamics (Theorem 3.2, "representation gravity"), and propose TARF, a unified framework using annealed gradient ascent on forgetting data coupled with target-aware gradient descent on identified hard-to-affect retaining data. Experiments across CIFAR-10/100, Tiny-ImageNet, ImageNet-1k, and real-world applications (Stable Diffusion concept removal, TOFU LLM unlearning) demonstrate consistent improvements over existing methods.

## Strengths

- **Novel problem formulation that identifies a genuine gap.** The paper convincingly shows that prior unlearning methods fail when the class label and target concept do not coincide — a scenario that is clearly motivated by practical concerns (privacy, fairness, copyright). The four-scenario taxonomy (all-matched, target mismatch, model mismatch, data mismatch) is clean and well-illustrated in Figure 1. This reframing of the unlearning task is more fundamental and broadly applicable than incremental improvements to existing methods.

- **Theoretical grounding of forgetting dynamics (Theorem 3.2).** The paper connects representation distance to loss dynamics during gradient ascent, introducing the concept of "representation gravity" as a formal principle. This goes beyond the heuristic approach common in unlearning papers — Remars 3.1–3.3 directly explain why each mismatched setting creates distinct failure modes, and the empirical validation in Figure 3 (t-SNE visualizations and loss dynamics) matches the theoretical predictions.

- **Strong and consistent empirical results across scales.** TARF achieves the lowest or near-lowest Gap↓ on virtually all 12 task-dataset combinations in Tables 3 and 4. The gains are often dramatic in mismatched settings (e.g., CIFAR-100 target mismatch: TARF Gap↓=0.21 vs. best baseline BS=15.20). The ImageNet-1k results (Table 4) confirm scalability, and the real-world applications (Figure 6, Table 5) demonstrate practical utility beyond classification benchmarks.

- **Systematic ablations that validate design choices.** Figure 7 provides controlled experiments on the initialized strength *k*, annealed vs. constant gradient ascent, model architectures, and gradient operations on selected data. These ablations directly support the design decisions in Eq. 3–5 and give practical guidance for hyperparameter selection.

## Weaknesses

### Major

None.

### Minor

- **Table formatting issue with Retrained Gap values.** In Table 3, the Retrained rows show non-zero Gap values (e.g., 4.33 for CIFAR-10 all-matched, 1.47 for CIFAR-100 all-matched). Since Gap is defined as the average absolute difference with the Retrained reference, the Retrained model's own Gap should be zero (as correctly shown with "−" in Table 4). This is likely a formatting artifact (perhaps comparing against the original trained model rather than itself), but it undermines trust in the numerical presentation. The authors should clarify or correct these values.

- **Missing oracle-informed baseline to isolate the contribution of identification vs. separation.** The paper shows that TARF outperforms naive baselines (GA, FT, etc.) in mismatched settings. However, it does not compare against an "informed" baseline that knows target concept membership (e.g., running gradient ascent on all data from the classes belonging to the target concept, using oracle knowledge). Such a comparison would clarify whether TARF's advantage comes from its target identification phase, its separation-and-annealing procedure, or both. Without it, the necessity of the full TARF pipeline is not fully isolated.

- **Target identification boundary not empirically probed.** The paper acknowledges in the conclusion that the representation-gravity-based identification may weaken in challenging regimes (fine-grained, long-tailed, multi-attribute data). However, no experiments systematically probe this boundary — e.g., by varying representational distance or using datasets where the target concept is not well-clustered. A synthetic experiment varying the alignment between representation space and concept structure would strengthen the paper's claims about generalizability.

- **Standard deviations missing from main tables.** The paper states that complete results with mean and std are in Appendix F.7 (stripped). The main tables would benefit from at least standard deviations or confidence intervals for the key Gap metric, as readers cannot assess statistical significance from the presented single-run values.

### Trivial

- The Gap computation for a few individual baselines in the parsed table appears inconsistent with the stated formula (e.g., BS in CIFAR-10 model mismatch shows Gap↓=0.79, which does not match the published UA/RA/TA/MIA values given the formula). This may be a PDF-parsing artifact but should be verified.

## Nice-to-Haves

- An ablation or sensitivity analysis of the β threshold (currently set as top-10% accuracy drop) would improve practical guidance. How sensitive is TARF's performance to this percentile choice?
- The computational time column shows TARF is comparable to FT and L1-sparse but much slower than GA. A brief discussion of whether the improved gap justifies the computational overhead would be helpful.

## Removed Points

The following points raised by the reviewers were removed for the stated reasons:

- "The paper does not include standard deviations in the main table" — The paper states complete results with mean and std are in Appendix F.7 (which was stripped by the parser). Not a paper error.
- Criticisms about missing proofs in the appendix — The parser strips these sections; they exist in the original submission.
- "Missing related works" — I cannot verify this claim without external sources.
- Formatting/style nitpicks (typos, capitalization, etc.) — Parser artifacts, not author errors.
- "The MIA metric's behavior masks potential distinction between true forgetting and model collapse" — This is speculative and not supported by evidence in the paper; the paper's MIA evaluation follows standard practice.
- "The real-world application examples (Figure 6, Table 5) are too abbreviated" — The paper notes that full details are in the appendix (stripped); the main text provides sufficient summary.
- Some strengths from the Strength Finder that were generic or superficial (e.g., "this paper addressed an important problem") — Removed for lacking specific, concrete content.

## Novel Insights

The key insight that synthesizes across the paper's contributions — and is genuinely novel — is that the standard unlearning assumption of "class label = target concept" fundamentally limits the field's ability to handle realistic requests, and that the representation geometry of the model (specifically, latent-space distances between data subsets) provides a principled signal for both identifying and separating target concepts during forgetting. This reframes unlearning from a pure optimization problem (maximize loss on D_f, minimize loss on D_r) into a structured representation-learning problem where forgetting dynamics reveal concept membership. The "representation gravity" concept (Definition 3.3) — that samples with similar representations exhibit coupled forgetting dynamics — is the operational lever that turns this insight into a practical algorithm. This bridges representation learning theory and unlearning practice in a way that prior work has not attempted.

## Suggestions

- **Clarify Table 3 Gap column.** Replace the Retrained Gap values with "−" (as in Table 4) or add a footnote explaining what these numbers represent if they are not standard Gap values.
- **Add one oracle-informed baseline experiment** for a single mismatched setting (e.g., target mismatch on CIFAR-100) where the baseline uses ground-truth knowledge of target concept membership. This would cleanly isolate whether TARF's advantage comes from identification, separation, or both.
- **Include standard deviations** or error bars for the Gap metric in the main tables, or add a note that variance was low across runs.
- **Add a boundary-probing experiment** for target identification, e.g., using CIFAR-100 with randomly shuffled superclass assignments to create a condition where representation alignment breaks down.

## Score and Decision

### Calibration Report

**Round 1 (Bracketing):**
- Weak band (<3.5): Returned "An Unlearning Framework for Continual Learning" (2.00), "POCO Unlearning" (2.00), "Suppressive MU" (2.50), "Learning to Unlearn" (3.00) — all low-quality or withdrawn papers.
- Middle band (3.5–7.5): Returned "Unlearning Isn't Deletion" (4.00, Reject), "Forget Vectors at Play" (4.50, Reject), "MU-Mis" (4.00, Accept Poster), "Source-Free Class Unlearning" (4.50, Reject).
- Strong band (>7.5): Returned papers on RL, quantum computing, rotation estimation — topically unrelated to unlearning, confirming no unlearning paper at this level.

**Initial bracket: 5.0–7.0.** The paper is clearly stronger than the 4.0–4.5 unlearning papers but does not reach the 7+ level (no comparable work exists at that level in this space).

**Round 2 (Narrowing within bracket):**
- Anchors in (4.5, 6.5): "Distributional Unlearning" (6.00, Accept Poster), "Retain-Forget Entanglement" TMU (5.50, Accept Poster), "Memorize to Forget" (5.50, Reject).
- Anchors in (5.0, 7.5): "REM" (5.00, Accept Poster), "Mode Connectivity Unlearning" (5.50).

**Comparative assessment against key anchors:**
- vs. "Distributional Unlearning" (6.00): TARF has a more novel problem formulation, broader experiments (ImageNet-1k vs. synthetic/text/small-image), and a method that directly addresses model-level forgetting rather than data selection. Comparable theory depth. TARF is slightly stronger.
- vs. "Retain-Forget Entanglement" (5.50): TARF has a broader problem scope (4 scenarios vs. 1), deeper theory (Theorem 3.2), larger-scale experiments, and real-world applications. TARF is clearly stronger.
- vs. "REM" (5.00): TARF has stronger novelty, better theory, and cleaner method without the scalability concerns of REM's parameter-doubling. TARF is stronger.

**Final score: 6.0.** The paper makes a genuinely novel contribution to the machine unlearning literature with a clear problem formulation, solid theoretical grounding, and comprehensive empirical validation. The main weaknesses (table formatting issues, missing oracle baseline, and unprobed identification boundary) are real but minor and do not threaten the core contribution.

**MY FINAL SCORE: <score>6.0</score>**
**MY FINAL DECISION: <decision>Accept</decision>**