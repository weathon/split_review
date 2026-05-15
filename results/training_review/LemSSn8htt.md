Now I have a thorough understanding of the paper. Let me write the final consolidated review.

## Summary

The paper proposes Δ-AI (Delta-Amortized Inference), a local objective for amortized inference in sparse probabilistic graphical models. Instead of requiring a full instantiation of all variables (as in GFlowNet objectives like trajectory balance and detailed balance), Δ-AI's loss involves only a single variable and its Markov blanket. The method is grounded in a theoretical result (Proposition 1) showing that matching local conditional distributions is sufficient for global distribution matching. Empirically, Δ-AI converges faster in wall-clock time than GFlowNet baselines and MCMC on synthetic PGMs and in a variational EM setting for MNIST.

## Strengths

- **Novel, theoretically motivated objective**: The Δ-AI loss (Eq. 10) is a clean local constraint derived from the equality of conditional distributions under the Markov network and Bayesian network factorizations. Proposition 1 formally establishes that the local constraint (Eq. 9) is sufficient for global distribution matching, and the connection to concrete score matching provides a rigorous footing.

- **Clear empirical speed advantage in wall-clock time**: Figure 4 shows Δ-AI converging significantly faster than trajectory balance, detailed balance, and forward-looking DB across three synthetic graphical models (Ising ladder, Ising lattice, factor lattice). The advantage is maintained in the more challenging bilevel variational EM setting (Figure 7). This speedup arises naturally from the locality of the loss computation.

- **Amortization over multiple DAG orders is demonstrated to be practical**: The paper introduces the idea of training a single parametric model $q_\theta$ to match conditionals across multiple I-maps for the same Markov network. Figure F.2 (appendix) shows that learning over multiple orders barely increases convergence time, which is non-obvious and has practical value.

- **Clean ablation over structured vs. unstructured inference**: The paper compares against mean-field EM (factorized posterior), wake-sleep variants, and multiple GFlowNet objectives — all using the same model architecture — providing a clear picture of where the benefit comes from.

## Weaknesses

### Fatal
None.

### Major

- **Partial-inference capability is claimed but not experimentally demonstrated**. The paper asserts in the abstract, introduction, and conclusion that Δ-AI enables "inference over partial subsets of variables" and that this "reduces sampling time." The mechanism (amortizing over multiple DAG orders so that downstream variables need not be sampled) is described at a high level in Section 3 (line 180), but no experiment actually demonstrates training or inference on a subset of variables. All experiments train on fully instantiated states. An advertised first-order advantage therefore rests entirely on speculation. While this does not invalidate the paper's other contributions, it creates a significant gap between what is claimed and what is shown.

- **The claimed "stronger local training signal" is not disentangled from cheaper per-step computation**. All comparisons use wall-clock time, and GFlowNet baselines inherently require more expensive per-step computation (full energy evaluation). The paper attributes faster convergence to both (i) cheaper steps *and* (ii) better credit assignment from the local objective (Section 1, point ii). But no experiment controls for the number of gradient steps, reward evaluations, or effective samples per parameter update. The advantage could plausibly come entirely from cheaper computation. A controlled comparison (e.g., equalizing the number of reward evaluations or gradient steps) is needed to support the "stronger signal" claim.

### Minor

- **Chordalization sensitivity is acknowledged but unquantified**. The paper correctly notes (Section 6) that chordalization can create large Markov blankets, undermining locality. But no analysis or experiment characterizes how blanket size affects per-step cost or convergence. The tested graphs (Fig. 3) have modest chordalization overhead; the scope of applicability to broader classes of sparse graphs remains unclear. The stochastic estimator (§E) is mentioned but never evaluated.

- **The synthetic experiments (Fig. 4) do not report variance across runs**; only means are shown. The MNIST experiment (Fig. 7) does report mean±std over 5 runs. The absence of error bars on the central synthetic results weakens confidence in the comparison.

- **The number of importance samples used for NLL estimation** (Section 5, via Burda et al., 2016) is not reported, making it difficult to assess the reliability of the reported NLL numbers.

- **The claim that "none of the baselines are capable of partial inference over subsets of variables" (line 252) is overstated**. Gibbs sampling can straightforwardly condition on a subset of variables (though it is not amortized). The intended meaning is that no *amortized* baseline can do partial inference, but the sentence as written is imprecise.

- **The 12-hour training budget in Figure 7 leaves open the question of asymptotic ranking**. Some baselines (e.g., IW) have slopes suggestive of continued improvement; an asymptotic comparison or discussion would strengthen the claims.

### Trivial

- Line 92 contains a duplicated word ("energy energy").
- The text in Algorithm 1 is rendered as an image, making it inaccessible to text-based parsing.

## Nice-to-Haves

- A small-scale controlled experiment (equal gradient steps, not wall-clock time) comparing Δ-AI to GFlowNet variants, to separate the benefit of cheaper computation from better credit assignment.
- An explicit demonstration of partial-variable inference on a small model, e.g., inferring only a subset of latents in the MNIST pyramid while conditioning on observations.
- Reporting variance across runs for the synthetic experiments.
- Reporting the number of importance samples used for NLL estimation in Section 5.

## Removed Points

These points are flagged to be removed, treat them with caution:

1. **"Missing comparison with structured variational inference"** — The paper already compares against GFlowNets (TB, DB, FL-DB) and wake-sleep (IW, sleep), all of which learn structured posteriors with the same graphical model structure. The critic's request for "a VAE whose encoder and decoder share the same graph structure" is already reflected in these baselines (same architecture, same structure, different training objective). The vanilla VAE shown in Figure 7 is an additional reference point, not the primary comparison. The comparison against structured-posterior methods is present.

2. **"Memory cost claim is misleading — forward pass still samples full trajectory"** — The paper's statement (line 16, point ii) says "memory cost is very low because computing each gradient update only involves a small subset of variables." This refers to the gradient update (backward pass), which is indeed local. Modern deep learning frameworks consume the bulk of training memory on storing activations for backpropagation; locality in the backward pass meaningfully reduces memory. This criticism conflates forward sampling cost with gradient computation memory.

3. **"Proposition 1 relies on the condition holding for all x, u, x'_u, but in practice loss is minimized over finite samples"** — This is a generic criticism applicable to essentially all ML training objectives (including all GFlowNet baselines). Proposition 1 is a theoretical statement about sufficiency; the paper does not claim that finite-sample optimization achieves exact equality. This is not a weakness specific to Δ-AI.

4. **"The practical difficulty of chordalization (NP-hard) is not mentioned"** — Finding an optimal (minimum-fill) chordalization is NP-hard, but any graph can be chordalized by a greedy heuristic (e.g., maximum cardinality search), which is standard practice. The paper mentions chordalization as a standard operation in graphical models and the experiments use it. This criticism would benefit from a citation, which the reviewer did not provide.

5. **Various minor phrasing issues and section-by-section nits** — Many of the Section-by-Section notes in the harsh review are either answered by the paper text (e.g., "Algorithm 1 requires a full sample" — yes, that's the basic form; the multi-DAG amortization is a distinct variant described afterward) or are minor presentation preferences.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a perspective on the work that the authors themselves have not already identified.

## Suggestions

1. **Add a controlled comparison** isolating credit assignment from computational cost: compare Δ-AI and a GFlowNet baseline with the same number of gradient steps (or same number of reward evaluations) rather than wall-clock time, on a small graph. Report the number of gradient steps needed to reach a target NLL.

2. **Demonstrate partial inference**: Train Δ-AI on a setting where inference is needed only over a subset of variables (e.g., condition on observed pixels and infer only a subset of latents). Show that the local loss can be optimized without sampling all variables, and report wall-clock savings relative to full sampling.

3. **Characterize chordalization effects**: For the graphs tested, report the average and maximum Markov blanket size in the chordalized graph. This helps readers assess the degree of locality achieved.

4. **Report variance on synthetic experiments** and the number of importance samples used for NLL estimation.

5. **Clarify the asymptotic behavior**: Discuss whether the convergence ordering in Figure 7 is expected to persist asymptotically or whether some baselines might catch up.

## Score and Decision

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>