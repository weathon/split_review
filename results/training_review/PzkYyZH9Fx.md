Now I have all the information needed. Let me synthesize the final review.

## Summary

The paper introduces NARCISSUS, an unsupervised anomaly detection method that exploits the observation that when training on a mixture of normal and anomalous data, neural networks converge on normal data first (before fitting anomalies). NARCISSUS uses a tailored Very Early Stopping (VES) scheme combined with an ensemble variant (RVES) to halt training before overfitting to anomalies, thereby turning semi-supervised models into unsupervised ones. Evaluations on time series, image, and graph datasets show NARCISSUS achieving accuracy comparable to semi-supervised methods while using no labels.

## Strengths

- **Novel and well-motivated core insight**: The observation that models converge faster on normal than on anomalous data during mixed training (supported by Theorem 4.2 and Figure 1) is intuitive yet practically valuable. The paper correctly identifies that this training dynamic can be exploited for unsupervised anomaly detection, which is a genuinely different approach from prior work that relied on pseudo-labeling or bootstrapping.

- **Strong empirical evidence that NARCISSUS outperforms existing unsupervised methods**: Table 1 shows large and consistent improvements over DAGMM, MSCRED, and Merlin across all six time-series datasets (e.g., F1 of 0.93 for N-GDN on NAB vs. 0.51 for DAGMM). This is a clean, uncontroversial win — all methods are unsupervised and evaluated on identical data.

- **Model-agnostic framework demonstrated across three data modalities**: The paper validates NARCISSUS not only on time series but also on images (PatchCore, AnoGAN) and graphs (AddGraph), showing AUC comparable to semi-supervised training. This breadth supports the generality of the approach.

- **Ablation studies justify both VES and RVES components**: Figure 3 convincingly shows that naive bootstrapping produces F1 scores ranging from 0.43 to 0.97 (unstable), and the paper reports (via Table 7 in the appendix) that removing RVES degrades performance. This evidence substantiates the need for both algorithmic components.

## Weaknesses

### Fatal
None.

### Major

1. **Unclear experimental protocol for time-series data splits**: Section 5.2 does not specify whether the original training and test sets were kept separate or merged for the time-series experiments. Section 5.3 explicitly states that for images/graphs the train and test data were merged, but makes no such clarification for time series. Since the semi-supervised baselines in Table 2 were trained on clean normal data (their original setup), it is critical to know whether NARCISSUS also trained only on a (unlabeled) training split or on merged data. This omission makes it impossible to fully evaluate the fairness of the comparison — not because there is evidence of wrongdoing, but because the paper does not provide enough information to rule it out. The authors must clarify this for the time-series experiments in any revision.

2. **Results reported without any measure of uncertainty**: All performance numbers in Tables 1–5 are point estimates with no confidence intervals, standard deviations, or significance tests. Given that RVES involves random validation splits and random initialization, variance is expected. The ablation study (Figure 3) itself demonstrates that performance can vary enormously (F1 from 0.43 to 0.97) under different random seeds for related methods — yet the paper does not report the variance of NARCISSUS itself. The reported F1 differences of ≤0.02 between NARCISSUS and semi-supervised methods could easily fall within noise. This undermines confidence in the central claim of "comparable accuracy."

3. **For image/graph experiments, merging train and test data creates an asymmetric comparison with semi-supervised baselines**: Section 5.3 explicitly states that NARCISSUS trains on merged train+test data, while the semi-supervised baseline (type iii) trains only on the original clean training set. This means NARCISSUS has access to more data (including test anomalies) during training. While the paper is transparent about this choice, it makes the comparison to semi-supervised methods not directly controlled — NARCISSUS may benefit from additional data volume. The comparison to bootstrapping (type ii) remains fair since both use the same merged data.

### Minor

1. **The VES convergence metric is never formally defined**: Algorithm 1 refers to a "convergence metric" and states that "conventional early stopping is applied" on the intersection of filtered subsets, but the paper does not specify what this metric is (loss plateau? gradient norm? threshold?). This directly affects reproducibility.

2. **VES hyperparameters are not analyzed**: The paper does not study sensitivity to the number/size of validation subsets, the threshold η, or the stopping criterion. Given that VES is the core algorithmic contribution, the lack of any hyperparameter analysis is a gap.

3. **The theoretical analysis is motivational rather than derivational**: Theorem 4.2 is a simple inequality bounding gradient contributions, and the optimization problem in Equation 3 is never used to derive the algorithm. Lemma 4.1 is trivial (existence is obvious). The paper does not overclaim on theory — it presents theory as motivation — but the theory section adds limited rigor beyond what common sense would suggest.

4. **The "well-bounded" data assumption is stated but not verified**: The paper assumes anomalous data is well-bounded (dynamic range not exceeding normal data by orders of magnitude) but does not verify this assumption on any of the datasets used. For time series like SWaT or SMAP, some anomalies could involve sudden spikes or dips — the paper should check whether the condition holds.

### Trivial

- Line 143: "fti" should be "fit" (parser artifact, but worth noting).
- The phrase "the difference is F1 score is within 0.02" on line 213 has a minor grammatical issue.

## Nice-to-Haves

- Reporting results with standard deviations over at least 10 random seeds would substantially strengthen the paper.
- A formal definition of the convergence metric used in VES.
- A sensitivity analysis of VES hyperparameters (validation subset size, η, stopping threshold).
- A per-epoch trace of detection performance (not just loss) to verify that the VES stopping point corresponds to near-optimal F1 on a held-out set.

## Removed Points

These points were flagged for removal. Treat them with caution — they are either factually incorrect, misread the paper, or violate the review guidelines.

1. **"VES is logically circular"** (Harsh Critic Point 2, part): The claim that VES is "circular" because it "uses the very signal (higher loss for anomalies) that the method is supposed to discover" misunderstands the method. NARCISSUS does not claim to *discover* that anomalies have higher loss — the loss-as-anomaly-score relationship is the standard operating principle of all deep semi-supervised AD methods (Eq. 2). The contribution is about *when to stop training*, not about discovering the loss-signal relationship. The VES filtering step uses loss to identify what is statistically likely normal, which is a reasonable statistical heuristic given the sparsity assumption. REMOVED as factually incorrect.

2. **"Data leakage invalidates central claim for time series"** (Harsh Critic Point 1, hyperbole): The paper does NOT state that train/test were merged for time series — the merging statement is explicitly in Section 5.3 (images/graphs). The reviewer's conditional ("if the same procedure was used") is speculation unsupported by the paper. The clarity concern is kept above, but the conclusion that the results are "invalid" is removed as it assumes something not stated in the paper.

3. **"The theoretical contribution does not justify the method"** (Harsh Critic Point 4, overstatement): The paper uses Theorem 4.2 as motivation, not as a formal derivation of VES. Claiming the theory "does not justify" the method is a scope creep — the paper never claims VES is derived from the theorem. The looser connection is acknowledged above as a minor weakness, but the stronger claim of invalidity is removed.

4. **"Dismissal of self-supervised methods is not justified"** (Section-by-section note on 5.1): The paper provides a clear rationale: self-supervised methods would need NARCISSUS as a module in their workflow, and NARCISSUS already matches semi-supervised accuracy, making self-supervision unnecessary. This is a reasonable scoping decision. REMOVED.

5. All pure formatting/style nitpicks and parser artifacts.

## Novel Insights

The reviews surface an interesting tension: the paper's primary strength (model-agnostic, simple early-stopping approach that matches semi-supervised performance) is also the source of its most significant evaluation challenges. Specifically, the simplicity of the method — "just stop training early on a loss signal" — makes it especially sensitive to evaluation rigor (clean data splits, variance quantification, hyperparameter sensitivity). The fact that the reviewers converged on concerns about experimental clarity rather than algorithmic flaws suggests the core idea is sound but needs more careful empirical validation. One genuinely novel observation from the reviews is that the ablation study's demonstration of bootstrapping's instability (F1 range 0.43–0.97) actually serves as strong indirect evidence for why NARCISSUS's VES/RVES approach is necessary — a framing the paper could emphasize more directly.

## Suggestions

1. **Clarify the time-series data split protocol**: State explicitly whether training and test sets were kept separate or merged for each dataset in Section 5.2. If they were kept separate, describe how validation subsets for VES were drawn without leaking test information.

2. **Add variance reporting**: Report means and standard deviations over at least 5-10 random seeds for all main results (Tables 1-5). This is critical because the ablation study (Figure 3) shows that related methods have high variance.

3. **Define the convergence metric formally**: Specify exactly when the model is considered to have "converged on the intersection" in VES. This is needed for reproducibility.

4. **Run a controlled comparison for the image/graph experiments** where NARCISSUS uses only the original training data (not merged) to directly compare with semi-supervised baselines on equal footing.

5. **Verify the "well-bounded" assumption** empirically for each dataset by reporting the dynamic range of anomalous versus normal values.

## Score and Decision

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>