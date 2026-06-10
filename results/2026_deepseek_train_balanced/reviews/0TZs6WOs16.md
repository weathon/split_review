Below is my consolidated meta-review.

---

## Summary

The paper extends the SASRec sequential recommendation architecture by replacing its Euclidean inner-product output layer with a hyperbolic (Poincaré ball) classifier, producing models HSASRec (BCE loss) and HSASRecCE (full cross-entropy loss).  Two accompanying empirical findings are emphasized: (1) negative sampling via BCE undermines the hierarchical structure that hyperbolic models are designed to exploit, so cross-entropy is the correct loss; (2) the machine-precision setting used in δ-hyperbolicity estimation (ε = 10⁻¹² versus the conventional 10⁻⁵) changes estimated curvature by an order of magnitude and measurably affects recommendation quality.  A δ-hyperbolicity convergence diagnostic is proposed to identify datasets compatible with hyperbolic geometry.

---

## Strengths

- **Identification of negative sampling as a failure mode for hyperbolic sequential recommenders.**  Table 1 and Figure 2 provide concrete evidence that uniform negative sampling creates a popularity bias (Figure 2) that degrades the hierarchical representations hyperbolic models rely on.  The ablation HSASRec (BCE) vs. HSASRecCE (CE) cleanly isolates this effect, and the paper connects it to a principled argument about popularity hierarchies rather than simply reporting a performance gap.

- **Machine-precision-aware curvature estimation yielding measurable quality gains.**  Section 3.3 and Figure 4 show that changing ε from 10⁻⁵ (used in prior hyperbolic work) to 10⁻¹² produces an order-of-magnitude change in estimated curvature *c* and empirically links improved precision to better recommendation quality.  This is a concrete, reproducible methodological improvement that subsequent hyperbolic recommendation work should adopt.

- **δ-hyperbolicity convergence criterion as a diagnostic for dataset-model compatibility.**  Figures 5–6 introduce a practical diagnostic: datasets whose δ estimates plateau with increasing sample/embedding sizes (MovieLens-1M, Grocery) are compatible with hyperbolic models, while datasets where δ grows without bound (Office Products, Arts Crafts) are not.  This provides an evidence-based rule (rather than speculation) for when hyperbolic geometry helps, and the pattern in Table 1 is consistent with this diagnostic.

- **Clean ablation isolating geometry from architecture.**  The paper deliberately benchmarks against the simplest SASRec variant (not graph-based or BERT-based hyperbolic models) and controls for loss function by including both BCE and CE Euclidean baselines.  This design choice correctly isolates the effect of hyperbolic geometry from architectural complexity.

- **No Riemannian optimization required.**  All learnable weights remain Euclidean (Section 3.1, Equations 5–6); only the prediction-layer computation becomes hyperbolic.  This makes the approach practical and easy to integrate into existing SASRec pipelines without specialized optimizers.

---

## Weaknesses

### Fatal
None.

### Major

- **Asymmetric embedding-size design prevents clean validation of the compactness claim.**  
  Hyperbolic models are limited to embedding sizes {32, 64, 128} while Euclidean baselines explore {256, 512, 728}, justified solely by an expectation that hyperbolic models are "more expressive" (Section 4.1, line 172).  Because Euclidean SASRecCE is *never evaluated at the same small dimensions*, the claim that hyperbolic models achieve better results with "considerably smaller embeddings size, making the models more compact" (Conclusions) cannot be fully assessed.  If Euclidean SASRecCE at d=128 matches HSASRecCE at d=128, the advantage vanishes; if it does not, the gap is genuine — but the experiment as designed does not distinguish these cases.  This is a directly fixable design issue (add Euclidean at {32, 64, 128}), but it undermines one of the paper's central advertised benefits.

- **No error bars, variance, or statistical significance reported.**  
  All results in Table 1 are point estimates from a single train/test split with no indication of variance across random seeds or initialization.  On only 4 datasets (2 where the method works, 2 where it does not), a ~3% improvement over the proper CE baseline without any variance measure could lie within evaluation noise.  This is a weakness that, while common in the recommender-systems literature, is consequential here because the claimed improvement is small and conditional on dataset choice.

- **The "good/bad" dataset categorization is descriptive, not predictive, and rests on a tiny sample.**  
  The paper classifies 2 datasets as "good" and 2 as "bad" based on the method's own performance, then shows that δ-hyperbolicity estimates behave differently for these two groups.  With N=4, this is a post-hoc description, not a validated predictor for unseen datasets.  The framework is interesting as a hypothesis but is presented as a contribution (contribution 2 in the introduction) when it is still preliminary.  A stronger test would involve making a prediction for a held-out dataset based on its δ-plateau behavior, then validating against the actual model performance.

### Minor

- **The 8–18% improvement figure is relative to the weaker BCE baseline; the proper comparison yields ~3%.**  
  The paper is transparent about this in Section 6.2 (line 227: "within the 3% range" vs. SASRecCE), and the abstract does not cite percentages.  However, the conclusion states that hyperbolic models "consistently outperformed both the original SASRec baseline and the adjusted Euclidean baseline" without distinguishing the effect sizes, which is technically correct but could leave a reader with the impression of a uniformly larger improvement.

- **Additional baselines (PureSVD-N, EASEr) are listed but receive no analysis.**  
  They appear in Table 1 (presumably) but are never discussed in the Results section.  Either they should be analyzed or removed.

- **The offset parameter *r* and the "several publicly available datasets" tested beyond the reported four are not specified.**  
  The paper mentions (line 82) that non-zero offset *r* slightly improved hyperbolic models but does not report the values used or their effect on results.  Similarly, "several publicly available datasets" were tested but only four are reported (line 155); the reader cannot assess whether the four were cherry-picked to maximize the contrast.

### Trivial

- None beyond what has been covered above.

---

## Nice-to-Haves

- Run Euclidean SASRecCE at embedding sizes {32, 64, 128} to directly test whether the compactness advantage is real.
- Report results across multiple random seeds (at least 3–5) with mean and standard deviation.
- Pre-register a prediction: for a held-out fifth dataset, use δ-hyperbolicity convergence to predict whether HSASRecCE will improve over SASRecCE, then test it.  This would convert the categorization from description into a validated tool.
- Report the offset *r* values used and their impact on final results.
- Discuss the density, popularity skew, and sequence-length statistics of the four datasets to provide concrete intuition for why some are "good" and others "bad."

---

## Removed Points

These points were raised by one or both reviews but are removed after verification against the paper:

1. *"The negative sampling finding is not shown to be specific to hyperbolic geometry."* — The paper does not claim that negative sampling is *more* harmful for hyperbolic models than for Euclidean ones.  It claims that negative sampling disrupts the hierarchical structure that hyperbolic models rely on, provides a mechanism (popularity bias, Figure 2), and shows the empirical consequence (HSASRec underperforming).  The finding is about *why* negative sampling hurts hyperbolic models, not about a differential effect size.  Removed per Hard Rules (misreading of the paper).

2. *"The 8–18% improvement is misleading."* — The paper explicitly distinguishes (Section 6.2, lines 227–228) the 8–18% vs. SASRec (BCE) from the ~3% vs. SASRecCE (CE) in the same paragraph.  The abstract does not quote percentages.  The paper is reasonably transparent.  Demoted to a Minor framing note rather than a standalone criticism.

3. *Strength about "compact representations without Riemannian optimization" (compactness part).* — The compactness claim conflicts with the verified weakness about asymmetric embedding sizes (the evidence is incomplete).  Per the merging rule ("when a strength and weakness disagree, the weakness wins"), the compactness sub-claim is moved here.  The "no Riemannian optimization" sub-claim remains as Strength #5 (verified independently).

4. *"Missing related works" implied.* — The reviewer did not raise this, but as per instructions, I do not mention missing related works because I cannot verify their existence.

5. *"Pure formatting/style nitpicks" —* None present; removed preemptively.

---

## Novel Insights

The most interesting observation emerging from these reviews is the tension between the paper's two most compelling contributions: the machine-precision finding (ε = 10⁻¹²) and the δ-hyperbolicity diagnostic are genuinely useful for the community, yet they rest on the same experimental foundation whose design flaw (asymmetric embedding sizes) weakens the main performance claim.  This means that even if the compactness claim turns out to be unsupported, the paper's secondary contributions (precision-aware curvature estimation, negative sampling analysis, convergence-based diagnostic) remain independently valuable.  Conversely, if the compactness claim *is* supported, the paper's overall contribution is stronger than it appears at first glance.  A straightforward matched-size experiment would resolve this ambiguity and significantly sharpen the paper's message.

---

## Suggestions

- **Add Euclidean baselines at matched embedding sizes {32, 64, 128}.**  This single change would directly test whether hyperbolic models provide a genuine compactness advantage.  Report the results in a revised Table 1.
- **Report variance across multiple runs.**  At minimum, 5 random seeds with mean ± std for the headline metrics on the four datasets.
- **For the δ-hyperbolicity diagnostic, include a fifth dataset as a prediction test:** based solely on its δ-plateau behavior, predict whether HSASRecCE will improve over SASRecCE, then evaluate.  This would materially strengthen the claim that the diagnostic is predictive, not just descriptive.

---

## Score and Decision

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>