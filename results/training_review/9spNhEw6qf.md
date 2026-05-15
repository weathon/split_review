Now I have a thorough understanding of both the paper and the reviewer claims. Let me produce the consolidated review.

---

## Summary

This paper investigates whether knowledge distillation (KD) from a pre-grokked teacher model can induce grokking in settings where standard training fails: (1) below the "critical data regime" (data fractions where generalization is normally impossible), (2) under distribution shift (different modulus P), and (3) in continual pretraining. The core experiments, on modular arithmetic with 1-layer transformers, show that KD enables successful generalization at 20% data fractions where baseline training without KD fails, and that this occurs even without weight decay and with increasing weight norms. These results challenge prior claims that weight decay and norm reduction are necessary for grokking.

## Strengths

- **Demonstrates grokking below the critical data regime via KD (Figures 4a–4b):** The paper shows that at a 20% data fraction, no model generalizes without KD, but with KD grokking is observed. This provides a concrete, reproducible demonstration that the "critical data size" barrier can be overcome through distillation, extending the known boundaries of where grokking can occur. This is the paper's most significant empirical finding.

- **Provides empirical counterexamples to the necessity of weight decay and weight norm reduction (Figures 3, 4b):** The L2 weight norm plots (Figure 3) show continuously increasing norms across training for successful grokking runs, including for Adam without any weight decay. These results directly challenge mechanistic theories (Nanda et al., 2023; Liu et al., 2022b; Varma et al., 2023) that frame weight decay's cleanup phase or norm minimization as essential to the grokking transition. Even if the refutation is not definitive, the counterexamples are meaningful and worth community attention.

- **Shows cross-distribution grokking transfer (Figure 2b):** A student model trained on distribution p₂ (different modulus P) groks successfully when distilled from a teacher grokked on p₁, regardless of optimizer (Adam or AdamW). This goes beyond single-distribution studies and demonstrates a practical pathway for leveraging pre-grokked models under distribution shift, directly addressing the question of grokking's practical utility.

## Weaknesses

### Fatal
None. The core empirical claims are supported by visible trends in the figures, and the paper's contributions are real even if not as strongly established as one might wish.

### Major

- **Central claim of "refuting" prior theories is overclaimed relative to the evidence.** The paper uses strong language ("refute," "disproving the necessity," "ruling out these factors as the primary reasons") to describe its challenge to Nanda et al. and Varma et al. However, the experiments all involve KD, which is itself a strong regularizer. The proper reading — that KD can substitute for weight decay's role — does not constitute a refutation that weight decay plays the role prior work described in settings without KD. The results are important counterexamples that *complicate* prior theories, but the paper would benefit from more measured framing.

- **No quantitative rigor.** All experiments show single runs without error bars, multiple seeds, or statistical measures. For a paper making strong counter-claims to established findings, at least 5–10 seeds with mean/std reporting would be expected. This is particularly important for Figure 4b, where the caption acknowledges "weight decay helps in achieving a better generalisation" — without error bars, it is impossible to know whether the no-weight-decay runs reliably reach perfect test accuracy or whether the claim of "grokking" holds across runs.

### Minor

- **No comparison to other regularization techniques.** The paper attributes KD's benefit partly to label smoothing (line 110) but never compares against direct label smoothing, Mixup, or other regularizers that might similarly enable grokking below the critical data size. Without such baselines, it is unclear whether KD's effect is specific to its knowledge-transfer mechanism or simply a consequence of stronger regularization.

- **Model and training details are underspecified for reproducibility.** The paper states "1 layer Transformer" but provides no details on embedding dimension, number of attention heads, hidden dimension, or the size of the "larger model" used in Section 5. Hyperparameters beyond learning rate and batch size are not reported (no scheduling, no precision info). While this level of specification is common in workshop-style grokking papers, it limits independent reproduction.

- **The continual pretraining narrative is muddled.** The paper states that KD "prevented the occurrence of grokking" in the continual learning setting, while earlier showing KD *induces* grokking. These are not actually contradictory (the former starts from a grokked checkpoint, the latter from scratch), but the paper does not explain this distinction, and the phrasing will confuse readers.

- **Scope is narrow.** All experiments use modular arithmetic (addition, subtraction) with 1-layer transformers. The paper acknowledges this but does not provide evidence or argument that the findings extend to more complex tasks (e.g., polynomial arithmetic, small NLP tasks). This limits the generalizability claim.

### Trivial
- Minor grammatical issues throughout (e.g., "This is can be highly useful," inconsistent use of "grokking" vs. "grokk," run-on sentences). These do not impede understanding but should be cleaned up.
- Figure axis labels and numerical values are not legible in the PDF extraction; this should be verified in the actual submission.

## Nice-to-Haves

- Comparison against direct label smoothing or other regularizers to isolate whether KD's effect is due to smoothing or something richer (e.g., instance-specific gradient information).
- Ablation of teacher quality: does the student benefit from a *perfectly* grokked teacher, or would a partially-generalized teacher suffice?
- Systematic sweep of data fractions (5%, 10%, 15%, 20%, 25%) to empirically locate the critical threshold for this specific setup, rather than relying on Varma et al.'s values for a different architecture.

## Removed Points

These points are flagged to be removed, treat them with caution:

1. **"The paper never actually defines or measures the critical data regime for its own tasks"** — REMOVED (factually incorrect). The paper explicitly verifies this: Figure 4a shows that at 20% without KD, no generalization occurs, while Figure 2a shows grokking at 30%. This constitutes measurement of the critical threshold relative to the paper's own setup.

2. **"The continual pretraining experiment contradicts the earlier narrative that KD induces grokking"** — REMOVED (misunderstands the paper). The continual learning setting starts from a *grokked* checkpoint, where the model has already formed generalizing circuits; immediate generalization (no delayed grokking) is expected. The paper is clear that "delayed generalization was not observed in either scenario." This is not a contradiction.

3. **"The paper presents KD-forgetting-mitigation as a new insight but it is a known property"** — WEAKENED to minor. The value is in the *specific application* to grokked models and the demonstration that this works even below the critical data threshold. The framing does not claim this as a new discovery of KD's properties.

4. **"The paper conflates 'weight decay is helpful' with 'weight decay is necessary'"** — WEAKENED. The paper does acknowledge that weight decay helps (line 106: "weight decay helps in reducing the number of iterations"). Its claim is that weight decay is not *necessary* — a claim for which it provides counterexamples. The language of "refutation" is strong but the distinction is not a confusion.

5. **"Figure 4b appears to show final test accuracy below 1.0 for several tasks with Adam"** — This cannot be verified without the actual figure. The paper's text claims grokking is observed. If true, this would be a weakness, but it must be checked by examining the figure directly (not the extracted text). I treat the paper's textual claims as authoritative.

## Novel Insights

Beyond the paper's own contributions, the reviews do not surface a genuinely novel insight that the paper itself misses. The most interesting observation is that the paper's results suggest a functional equivalence between KD and weight decay in the grokking mechanism — both may serve to suppress memorization components, KD through label smoothing / teacher signal and weight decay through norm penalty. If this equivalence were explicitly explored (e.g., by ablating KD's temperature to match the strength of weight decay regularization), it could yield a mechanistic understanding that neither the paper nor the reviews fully articulate.

## Suggestions

1. **Reframe the contribution.** Replace "refuting" / "disproving" language with "providing counterexamples that challenge" or "complicating prior theories." The results are valuable without the overclaim.

2. **Add multi-seed experiments (≥5 seeds) with mean±std for the central results:** Figures 2b, 3, and 4b need error bars to be credible as refutations or demonstrations of reliability.

3. **Add at least one baseline regularizer** (label smoothing, or even just stronger weight decay) in the below-critical-data experiment (Figure 4) to disentangle whether KD's effect is specific or general.

4. **Clarify the continual learning narrative.** Add a sentence explicitly noting that the absence of grokking in that setting is expected because the model initializes from a grokked state rather than from scratch.

5. **Report full architecture details** (embedding dimension, number of heads, hidden dimension, parameter count) in the experimental setup.

## Score and Decision

The paper makes genuine contributions — it shows that KD can enable grokking below the critical data regime, demonstrates counterexamples to weight-decay necessity, and extends grokking to cross-distribution settings. These findings are of interest to the grokking community and plausibly impactful. However, the strength of the claims ("refuting," "disproving") exceeds what the evidence supports, particularly given the lack of statistical rigor and the narrow experimental scope. The paper is not fatally flawed, but it requires substantial revision (reframing claims, adding baselines, reporting error bars) before it meets the standards of a top-tier venue.

**Originality:** Moderate. The application of KD to enable grokking below critical data is novel, though individual components (KD, grokking) are well-studied.

**Quality:** Below the bar. Single-run experiments without error bars, missing baselines, underspecified architecture details.

**Clarity:** Below average. Several confusing phrasings and unclear logical transitions, especially around the continual learning experiment.

**Significance:** Moderate. If the claims hold with proper rigor, the paper would meaningfully advance our understanding of grokking.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>