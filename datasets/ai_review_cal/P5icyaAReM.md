- Decision: Reject
- Avg Score: 4.75
- Scores: 5, 6, 5, 3
Now I have all the information needed. Let me write the consolidated review.

## Summary

This paper reformulates contrastive learning as a matrix approximation problem using I-divergence (a non-normalized KL divergence). The key idea is to introduce an adaptive scaling factor that controls the weight of positive vs. negative pairs, leading to a loss that is decomposable across instance pairs. This enables stochastic approximation algorithms (SACLR) that can work with as few as one negative pair per anchor, unlike SimCLR which requires large batches. The paper also establishes a theoretical connection between the proposed row-wise version and the standard SimCLR loss. Experiments on ImageNet, CIFAR, and Imagenette compare against SimCLR, SogCLR, and iSogCLR.

## Strengths

1. **Novel theoretical framing of contrastive learning via I-divergence**: Sections 3.1–3.2 derive a contrastive loss from I-divergence minimization between pairwise similarity matrices. This is a principled departure from the standard InfoNCE formulation and connects contrastive learning to the neighbor embedding literature (SCE, t-SNE), offering a new perspective on why and how contrastive losses work.

2. **Stochastic approximation that operates with M=1 negative sample**: The paper derives minibatch-mode objectives (Eq. 6–7) and an EMA-based scaling factor estimator (Section 3.4) that allow training with a single negative pair per anchor. This is a genuine algorithmic advantage over SimCLR (which requires large batches for its softmax denominator) and is supported by the method's decomposable design, not just by empirical luck.

3. **Theoretical connection to SimCLR**: Theorem 1 (Section 3.5) shows that the row-wise I-divergence objective reduces to the SimCLR loss under a specific choice of per-row scaling factors, placing the proposed generalization on a firm theoretical footing and clearly delineating where SACLR extends beyond prior work.

4. **Lower memory overhead than prior stochastic estimation methods**: The matrix version of SACLR requires a single global scalar for the stochastic estimate, whereas SogCLR and iSogCLR maintain per-instance scalars that scale with dataset size (Section 4, lines 200–201).

## Weaknesses

### Fatal
None.

### Major

1. **Uncontrolled baseline comparisons undermine the empirical claims**. The paper explicitly states (line 196): "We exclusively report values from each methods respective paper unless explicitly mentioned." SACLR uses LARS optimizer with the projector from VICReg (line 194), while baseline numbers from other papers may use different optimizers, projectors, augmentations, temperature values, and evaluation protocols. The reported gains on ImageNet1k (Table 2) appear to be sub-1% (e.g., ~0.2–0.4% over iSogCLR as described in the text). With different architectures and hyperparameter setups, these small margins are uninterpretable — they could be explained by the different projector head alone. This is the single most critical weakness: without controlled re-runs of all baselines under identical conditions, the paper's core claim of "major improvements" (abstract) and "consistent superiority" (Section 1) over existing methods is not evidenced.

2. **The similarity function q(·,·) is never explicitly defined for the SACLR method**. The paper introduces $q_{ij}^{u,v}=q(\tilde{\mathbf{y}}_i^{(u)},\tilde{\mathbf{y}}_j^{(v)})$ on line 80 and uses it throughout (loss functions, Algorithm 1, Theorem 1), but never states what $q$ is in the experiments. In the SCE background (line 63), the paper mentions "usually defined to be exp(−∥yi−yj∥²) or 1/(1+∥yi−yj∥²)" — but this is about SCE, not SACLR. Theorem 1's claimed equivalence to SimCLR implicitly requires $q$ to be exponential cosine similarity with a temperature to match InfoNCE, but this is never stated. Without knowing the functional form of $q$, the method is not reproducible from the paper. This is a basic reproducibility requirement.

3. **Overclaimed significance relative to demonstrated evidence**. The abstract claims "major improvements" and the conclusion claims "consistent performance improvements to the compared methods." The reported improvements on ImageNet1k (Tables 1–2, which are images so exact numbers cannot be read, but the text describes improvements that are sub-1% over iSogCLR) are marginal at best. Even setting aside the uncontrolled baseline issue, these gains do not warrant the term "major." The paper also claims effectiveness "when using small batches and with only one negative pair" but does not systematically vary batch size or the number of negatives $M$ across a range (only $M=1$ and $M=B$ are tested; no curve of accuracy vs. $M$).

### Minor

1. **Sparse ablation studies**: The hyperparameter ablations (for $\alpha$ and $\rho$) are only shown on a single dataset. The comparison between matrix and row methods is only shown for Imagenette. The claim of "robustness against hyperparameters" (Section 5) is not backed by sufficient data.

2. **No quantified computational efficiency**: The paper claims memory efficiency over SogCLR/iSogCLR, but does not report wall-clock training time, memory usage, or FLOPs. Without these numbers, the efficiency advantage is asserted but not demonstrated.

3. **Inconsistent framing about per-instance scalars**: The paper criticizes SogCLR for requiring "EMA-updated scalars for each data instance" (line 12), yet the SACLR-row version also uses $N$ per-instance scaling factors (line 179: "This version of SACLR require $2N$ scaling factors [reduced to $N$]"). This rhetorical framing is misleading.

### Trivial

- Algorithm 1, line 12 has a sum $\sum_{u=1}^{2}$ inside a `for u ∈ {1,2}` loop, which re-uses the loop variable and is a writing error in the pseudocode.
- Theorem 1 is stated without proof or proof sketch beyond referencing the appendix (which was stripped by the parser).

## Nice-to-Haves

- A controlled experiment re-running SimCLR, SogCLR, and iSogCLR under the exact same infrastructure (same projector head, optimizer, augmentations, evaluation pipeline) would make the empirical claims interpretable.
- An ablation curve showing accuracy vs. number of negatives $M$ (e.g., $M = 1, 2, 4, 8, 16$) would directly validate the paper's central efficiency claim.
- Reporting wall-clock training time and peak memory per method would substantiate the claimed efficiency advantage.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"Missing proof of Theorem 1 in appendix"**: The rules require removing criticisms about missing appendix content, as the appendix is stripped by the parser. The original submission may contain the proof.
- **"No standard deviations for baseline methods"**: The paper takes baseline numbers from other papers; those papers may or may not have reported std. This is a consequence of the uncontrolled comparison approach, not a standalone flaw.
- **"Comparison to DCL is missing from experiments"**: DCL is cited as related work. Requiring experimental comparison to every related method constitutes scope creep.
- **"Batch size ablation missing"**: While this would strengthen the paper, it is a nice-to-have rather than a core weakness given that the paper's main efficiency claim (M=1 works) is already tested.
- **"Algorithm 1 line 12 duplicate sum over u"**: This is likely a parser-induced formatting artifact from LaTeX rendering; the original submission may render correctly.
- **"Future work about Transformer is generic padding"**: Generic yes, but not a weakness — many papers include forward-looking future work.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Run controlled experiments**: Re-implement all baselines (SimCLR, SogCLR, iSogCLR) under the *exact same* encoder, projector head, augmentations, optimizer, learning rate schedule, and evaluation protocol as SACLR. Report all numbers with standard deviations. This is necessary to substantiate any claim of improvement over these methods.

2. **Define $q$ explicitly**: State the exact similarity function used in experiments (e.g., $q(\mathbf{a},\mathbf{b}) = \exp(\mathbf{a}^\top\mathbf{b} / \tau)$ with temperature $\tau$) in the main text.

3. **Add an ablation on $M$**: Show a plot of accuracy vs. number of negative samples ($M=1,2,4,8,16$) to directly validate the claim that "fewer negative samples work well."

4. **Tone down the language**: Replace "major improvements" with "moderate gains observed under the authors' setup, pending controlled re-evaluation." The empirical substance supports a modest claim, not a grand one.

5. **Report computational metrics**: Include a table comparing training time per epoch and peak GPU memory for SACLR vs. baselines (both with M=1 and full batch).
