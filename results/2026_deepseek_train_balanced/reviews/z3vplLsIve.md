Here is the final consolidated review.

---

## Summary

The paper proposes "Effect Alignment" (EAD) for dataset distillation, which replaces the standard paradigm of matching intermediate training quantities (gradients, trajectories, features) with a new objective: minimizing the estimated effect on final validation performance when real training data is replaced by synthetic data. The core of the method is an estimator (Proposition 3.2) based on gradient inner-products at sampled training checkpoints, which avoids backpropagation-through-time. A polynomial error bound (Proposition 3.3) is provided. However, the paper has a fatal structural incoherence: the introduction claims contributions about bias mitigation and reweighting on Colored MNIST, but the body describes a different method (effect alignment) evaluated on standard benchmarks. The experimental section also lacks the details needed for evaluation.

## Strengths

- **Distinct conceptual framing for dataset distillation.** The paper identifies the surrogate-mismatch problem of process-alignment methods (Section 2.2) and proposes a genuinely different objective — endpoint consistency rather than intermediate-state matching. This is a clean conceptual departure from the three dominant paradigms (meta-gradient, feature-space alignment, process alignment) and is meaningfully articulated in Section 2.2 and the introduction.

- **Polynomial error bound improves over exponential bounds in prior influence-estimation work.** Proposition 3.3 (Eq. 6) gives an explicit bound $|\mathcal{R}(\mathcal{G},\mathcal{A})-\hat{\mathcal{R}}(\mathcal{G},\mathcal{A})|\leqslant \ell T^2 C + T^2 g/|\mathcal{D}|$ that has polynomial dependence on $T$. Remark 3.4 correctly notes this contrasts with exponential-growth bounds in prior work (Hara et al., 2019; Schioppa et al., 2024). Even if the bound is loose (cubic in $T$ under SGD), the polynomial-vs-exponential distinction is a technically meaningful improvement in the formal guarantees offered.

- **The estimator avoids backpropagation-through-time, providing a computational advantage over meta-gradient methods.** Proposition 3.2 (Eq. 4–5) uses only inner products of gradients at sampled checkpoints, explicitly avoiding the BPTT bottleneck that limits meta-gradient approaches (Wang et al., 2018; Deng & Russakovsky, 2022). The paper draws this contrast clearly (lines 14–15).

## Weaknesses

### Fatal

1. **The introduction describes a completely different paper than the one presented in Sections 2–6.** Line 16 states: "Empirical results on diverse bias-injected datasets demonstrate that the proposed **reweighting scheme** significantly reduces **bias** in the distilled datasets. For example, on **Colored MNIST** with a 5% bias in conflicting samples and 50 images per class... our **reweighting method** produces a more balanced dataset, resulting in **91.5% accuracy**." The contributions listed are: "(1) We provide the first study on the impact of biases in the dataset condensation process. (2) We propose a simple yet effective **re-weighting scheme** to mitigate biases in two canonical types of dataset condensation methods." **None of this appears anywhere in the paper body.** A grep for "bias," "reweight," or "Colored" returns matches *only* in line 16 — zero occurrences in Sections 2–6. The method (Sections 3–4) describes effect alignment via gradient inner-product matching, not a reweighting scheme. The experiments (Section 5) evaluate on standard benchmarks (MNIST, CIFAR, etc.), not bias-injected datasets. The paper's title ("Learn to Synthesize Compact Datasets by Matching Effects") and abstract describe the body correctly, but the introduction paragraph (line 16) and the listed contributions describe a second, unrelated research project. This is not a minor phrasing issue — it is a fundamental structural incoherence. A reviewer cannot determine what this paper actually contributes because its own introduction contradicts the body.

### Major

1. **Experiments are missing essential methodological details needed for evaluation.** Section 5 omits:
   - **Network architecture** — the word "architecture" never appears in Section 5. No ConvNet, ResNet, or MLP specification is given.
   - **Hyperparameters** — no learning rate, batch size, optimizer, number of training iterations, number of synthetic update steps, or number of sampled time steps $t_m$ are reported.
   - **Variance measures** — no standard deviations, confidence intervals, or number of independent runs. Grepping for "seed," "trial," "repeat," "standard deviation," and "variance" returns zero matches.
   - The **results table is not rendered** — it exists only as an unreferenced image placeholder (line 135).
   - Baseline numbers are attributed to "(Lei & Tao, 2024)" rather than the authors' own implementation (line 133).
   Without these details, the empirical claims cannot be assessed or reproduced.

2. **Results are communicated in vague, hedged prose rather than precise experimental reporting.** The text repeatedly uses language that would be unacceptable for a controlled experimental evaluation: "it is evident that our approach is competitive and **likely offers better performance**" (SVHN, line 163), "it can be inferred that our approach is **likely more effective**" (Tiny-ImageNet, line 167), and "our method has the **potential to offer better performance**" (SVHN, Tiny-ImageNet). For Tiny-ImageNet, the paper states "the specific accuracy values for our method on Tiny-ImageNet are **not provided in isolation**" (line 167). A paper reporting experimental results should give specific numbers with error bars, not hedged speculation.

3. **Ablation studies are promised but absent.** Line 81 states: "We will give suggestions of the choice of $t_m$ by performing ablation experiments in the experiments section." Line 16 also claims "extensive experiments and ablation studies." No ablation study appears anywhere in Section 5.

4. **CC3M evaluation is incoherent.** CC3M (Conceptual Captions 3 Million) is a multimodal image-caption dataset, not a classification benchmark. The paper nevertheless reports "accuracy" values on it (line 169: "accuracy of 0.14 for a total of 50000 samples") without explaining how a classification metric applies to a captioning dataset. The dataset description (lines 153) correctly identifies CC3M as being for "image captioning" and "visual question-answering," yet it is treated as a classification task. This experiment does not make sense as presented.

### Minor

1. **Key derivation deferred to inaccessible supplementary material.** Proposition 3.2, the paper's core technical enabler, states "See the supplementary material for detailed proof" (line 73) with no sketch or intuition in the main text. The supplementary material is not available, making the derivation unverifiable.

2. **The theoretical bound is very loose.** As acknowledged in Remark 3.4, under SGD $C \leq T g$, yielding an effective bound of $O(T^3 g + T^2 g/|\mathcal{D}|)$. For practical training where $T$ is in the thousands, this bound provides no meaningful constraint on estimation error. The polynomial-vs-exponential distinction is a formal improvement but has no practical force.

3. **No discussion of limitations.** The paper contains no limitations section or candid discussion of when the method might fail (e.g., when the Taylor approximation breaks down, when training trajectories are short, when networks are not smooth, when $t_m$ is small).

4. **Dataset descriptions are generic boilerplate consuming space that should contain experimental details.** Pages 141–153 are encyclopedic descriptions of standard datasets (MNIST: "The MNIST database is a well-known benchmark dataset in the field of machine learning and computer vision...") that serve no scientific purpose and occupy space needed for experimental specifications.

## Nice-to-Haves

- Comparison of computational cost (wall-clock time, memory usage) against baselines. The method claims efficiency but provides no quantitative evidence.
- Clarification of whether the method requires a pre-trained model on the full dataset (Algorithm 1 suggests it does) and, if so, controlled comparison against methods that use the same procedural advantage (e.g., MTT also uses expert trajectories).
- Sensitivity analysis on the hyperparameter $t_m$ (number of sampled time steps), as promised in the paper.
- Ablation showing how the effect alignment objective compares to the exact replacement effect via brute-force retraining on small problems.

## Removed Points

The following points from the inputs are removed with justification:

- *"Method depends on pre-training on full dataset, making comparison unfair"* — Demoted. While the method does require a pre-trained trajectory, several compared baselines (e.g., MTT) also use expert trajectories pre-trained on the full dataset, so the unfairness claim is overstated.
- *"Random minibatch for P provides unstable training signal"* — Removed. Speculative concern about training dynamics without evidence from the paper.
- *"Linear time complexity claim is misleading"* — Removed. The estimator genuinely avoids BPTT and requires only gradient computations at $t_m$ sampled checkpoints, which is linear in $t_m$.
- *"No code or reproducibility statement"* — Removed. Standard for anonymous conference submissions.
- *"Notation is sloppy"* — Removed. Purely a style nitpick.
- Strength Finder's *"introduction correctly identifies issues"* and generic descriptions — Removed. These are not specific evidence-based strengths.
- Formatting artifacts (table not rendering) — Removed as a standalone criticism; kept only as part of the broader experimental deficiency argument.

## Novel Insights

None beyond the paper's own contributions. The review process surfaced no observation about the paper's approach or results that the authors themselves did not state or imply.

## Suggestions

1. **Rewrite the introduction to match the actual paper** — remove all claims about bias mitigation, reweighting, and Colored MNIST. The paper should honestly frame its contribution as proposing effect alignment for dataset distillation.
2. **Provide a complete experimental setup** — specify the network architecture, all hyperparameters, and the number of independent runs with standard deviations for every reported number.
3. **Deliver the promised ablation studies**, especially the sensitivity to $t_m$.
4. **Clarify or remove the CC3M experiment** — either explain how accuracy applies to a captioning dataset or remove this incoherent result.
5. **Add a limitations discussion** that addresses when the Taylor approximation and estimator assumptions break down.

## Score and Decision

Score: 1.5, Decision: Reject

MY FINAL SCORE: <score>1.5</score>
MY FINAL DECISION: <decision>Reject</decision>